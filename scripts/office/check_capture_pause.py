"""Read-only delivery verification; never requests previews, recovery or lighting changes."""
import argparse
import ctypes as C
from ctypes import wintypes as W
import hashlib
import json
from pathlib import Path
import subprocess
from office_control import Control
from runtime_control import owned_process


def preserved(state):
    files = [state/name for name in ('OpenRGB.json', 'office-ambience.json',
             'office-screen.json', 'office-awake.json', 'office-rest.json')]
    user = C.WinDLL('user32', use_last_error=True)
    active, timeout = W.BOOL(), W.UINT()
    if not user.SystemParametersInfoW(16, 0, C.byref(active), 0) or not user.SystemParametersInfoW(14, 0, C.byref(timeout), 0):
        raise C.WinError(C.get_last_error())
    return {'files': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.exists()},
            'screensaver_active': bool(active.value), 'screensaver_timeout': timeout.value,
            'power_plan': subprocess.check_output(['powercfg.exe', '/getactivescheme'], text=True).strip()}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state', type=Path, required=True)
    p.add_argument('--baseline', type=Path, required=True)
    p.add_argument('--capture-baseline', action='store_true')
    p.add_argument('--record', type=Path)
    a = p.parse_args()
    baseline = preserved(a.state)
    if a.capture_baseline:
        a.baseline.write_text(json.dumps(baseline, indent=2), encoding='utf-8')
        print(json.dumps({'baseline_captured': True, 'application_not_started': True}))
        return
    assert baseline == json.loads(a.baseline.read_text()), 'Private preferences or OS power settings changed'
    with Control(a.state) as client:
        native, process = owned_process(client.owner_pid, a.state)
        native.FindFirstChangeNotificationW.argtypes = [W.LPCWSTR, W.BOOL, W.DWORD]
        native.FindFirstChangeNotificationW.restype = W.HANDLE
        native.FindNextChangeNotification.argtypes = [W.HANDLE]
        native.FindCloseChangeNotification.argtypes = [W.HANDLE]
        native.WaitForMultipleObjects.argtypes = [W.DWORD, C.POINTER(W.HANDLE), W.BOOL, W.DWORD]
        notification = native.FindFirstChangeNotificationW(str(a.state), False, 0x1b)
        if notification == C.c_void_p(-1).value:
            native.CloseHandle(process)
            raise C.WinError(C.get_last_error())
        handles = (W.HANDLE*2)(process, notification)
        try:
            while True:
                snapshot = client.call('snapshot')
                status = snapshot['status']
                expected = status['output_paused'] or not snapshot['settings']['enabled']
                assert not status['diagnostic_error'] and not status['controller_error']
                assert not status['rest_resume']['error']
                if status['capture_paused'] == expected and snapshot['screen']['gamma_valid']:
                    break
                event = native.WaitForMultipleObjects(2, handles, False, 0xffffffff)
                if event == 0:
                    raise RuntimeError('Owner exited before policy publication')
                if event != 1 or not native.FindNextChangeNotification(notification):
                    raise C.WinError(C.get_last_error())
        finally:
            native.FindCloseChangeNotification(notification)
            native.CloseHandle(process)
        if expected:
            assert not status['capture_active'] and not status['source_hwnd'] and not status['input_frames']
            assert not status['has_valid_frame'] and not status['wallpaper_image_active']
            if status['output_paused']:
                assert all(c == [0, 0, 0] for row in snapshot['colors'] for c in row)
        ids = {device['id'] for device, online in zip(snapshot['layout'], snapshot['online']) if online}
        assert {'H6609', 'H8048', 'Secretlab'} <= ids, 'Required wireless device unavailable'
        assert snapshot['screen']['managed'] and snapshot['screen']['gamma_valid']
        assert preserved(a.state) == baseline, 'Delivery changed preserved preferences'
        result = {'owner_pid': client.owner_pid, 'capture_paused': status['capture_paused'],
                  'capture_active': status['capture_active'], 'output_paused': status['output_paused'],
                  'capture_policy_matches_current_preferences': True, 'mode': status['mode'],
                  'rest_reason': status['rest_reason'], 'required_wireless_verified': True,
                  'gamma_valid': True, 'settings_and_power_preferences_preserved': True,
                  'read_only_verification': True, 'live_pause_resume_experiment_performed': False,
                  'preview_or_capture_recovery_requested': False}
        if a.record:
            a.record.write_text(json.dumps(result, indent=2), encoding='utf-8')
        print(json.dumps(result))


if __name__ == '__main__':
    main()
