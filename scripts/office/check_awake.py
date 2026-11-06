"""Verify Awake through the single native owner without desktop input or power-plan changes.

Baseline/evidence contains hashes of private settings, never the settings themselves.
Expiry waits on native status publication or owner exit, without a cancellation deadline.
"""
import argparse
import ctypes as C
from ctypes import wintypes as W
import hashlib
import json
import subprocess
import time
from pathlib import Path
from office_control import Control
from runtime_control import owned_process


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def preserved(state, snapshot):
    user = Path.home()
    files = [state/'office-ambience.json', user/'AppData/Roaming/LightBulb/Settings.json',
             user/'AppData/Local/Microsoft/PowerToys/Awake/settings.json']
    user32 = C.WinDLL('user32', use_last_error=True)
    active, timeout = W.BOOL(), W.UINT()
    if not user32.SystemParametersInfoW(16, 0, C.byref(active), 0) or not user32.SystemParametersInfoW(14, 0, C.byref(timeout), 0):
        raise C.WinError(C.get_last_error())
    return {'files': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.exists()},
            'settings': digest(snapshot['settings']), 'layout': digest(snapshot['layout']),
            'screen_settings': digest(snapshot['screen']['settings']),
            'screen_managed': snapshot['screen']['managed'],
            'screensaver_active': bool(active.value), 'screensaver_timeout': timeout.value,
            'power_plan': subprocess.check_output(['powercfg.exe', '/getactivescheme'], text=True).strip()}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state', type=Path, required=True)
    p.add_argument('--baseline', type=Path, required=True)
    p.add_argument('--record', type=Path)
    p.add_argument('--capture-baseline', action='store_true')
    p.add_argument('--exercise', action='store_true')
    restart = p.add_mutually_exclusive_group()
    restart.add_argument('--arm-restart', type=Path)
    restart.add_argument('--verify-restart', type=Path)
    a = p.parse_args()
    with Control(a.state) as client:
        before = client.call('snapshot')
        invariants = preserved(a.state, before)
        if a.capture_baseline:
            a.baseline.write_text(json.dumps(invariants, indent=2), encoding='utf-8')
            print(json.dumps({'baseline_captured': True, 'private_values_excluded': True}))
            return
        assert invariants == json.loads(a.baseline.read_text()), 'Existing settings or OS power preferences changed'
        initial = before['status']['awake']
        if a.arm_restart:
            assert initial['mode'] == 'automatic' and not before['status']['rest_reason']
            client.call('awake', action='display', enabled=True)
            armed = client.call('awake', action='mode', mode='interval', seconds=3600)
            assert armed['active'] and armed['display_required'] and not armed['error']
            a.arm_restart.write_text(json.dumps({'initial': initial, 'armed': armed,
                                                'previous_pid': client.owner_pid}, indent=2))
            print(json.dumps({'restart_interval_armed': True, 'pid': client.owner_pid}))
            return
        if a.verify_restart:
            record = json.loads(a.verify_restart.read_text())
            assert client.owner_pid != record['previous_pid'], 'Actual cold restart required'
            assert initial['mode'] == 'interval' and initial['until_ms'] == record['armed']['until_ms']
            assert initial['active'] and initial['display_required'] and not initial['error']
            client.call('awake', action='display', enabled=record['initial']['keep_screen_on'])
            client.call('awake', action='mode', mode='automatic')
            record.update(restored_after_actual_restart=True, new_pid=client.owner_pid)
            a.verify_restart.write_text(json.dumps(record, indent=2))
            before = client.call('snapshot')
            initial = before['status']['awake']
        evidence = {'initial_awake': initial, 'actual_owner_pid': client.owner_pid}
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

        def await_mode(mode):
            while True:
                value = client.call('snapshot')['status']['awake']
                assert not value['error'], value['error']
                if value['mode'] == mode:
                    return value
                result = native.WaitForMultipleObjects(2, handles, False, 0xffffffff)
                if result == 0:
                    raise RuntimeError('Native owner exited during Awake verification')
                if result != 1 or not native.FindNextChangeNotification(notification):
                    raise C.WinError(C.get_last_error())

        def command(**args):
            result = client.call('awake', **args)
            assert not result['error'], result['error']
            return result

        try:
            if a.exercise:
                assert not before['status']['rest_reason'], 'Interactive desktop required for actual manual requests'
                command(action='display', enabled=False)
                system = command(action='mode', mode='indefinite')
                assert system['system_required'] and not system['display_required']
                display = command(action='display', enabled=True)
                assert display['system_required'] and display['display_required']
                off = command(action='mode', mode='off')
                assert not off['active'] and not off['required']
                interval = command(action='mode', mode='interval', seconds=1)
                disk = json.loads((a.state/'office-awake.json').read_text())
                assert disk['mode'] == 'interval' and disk['until_ms'] == interval['until_ms']
                assert not await_mode('off')['active']
                command(action='mode', mode='expiration', until_ms=int(time.time()*1000)+1000)
                assert not await_mode('off')['active']
                try:
                    client.call('awake', action='mode', mode='expiration', until_ms=1)
                except ValueError:
                    pass
                else:
                    raise AssertionError('Past expiration accepted')
                evidence['manual_system_display_off_interval_expiration_verified'] = True
        finally:
            try:
                if a.exercise:
                    command(action='display', enabled=initial['keep_screen_on'])
                    mode = initial['mode']
                    if mode in ('interval', 'expiration'):
                        command(action='mode', mode='expiration', until_ms=initial['until_ms']) if initial['until_ms'] > int(time.time()*1000) else command(action='mode', mode='off')
                    else:
                        command(action='mode', mode=mode)
            finally:
                native.FindCloseChangeNotification(notification)
                native.CloseHandle(process)
        after = client.call('snapshot')
        awake, status = after['status']['awake'], after['status']
        assert awake['mode'] == 'automatic' and not awake['error']
        assert awake['active'] == (status['mode'] == 'app' and not status['rest_reason'])
        assert awake['display_required'] == awake['system_required'] == awake['active']
        ids = {d['id'] for d, online in zip(after['layout'], after['online']) if online}
        assert {'H6609', 'H8048', 'Secretlab'} <= ids, 'A required wireless light is unavailable'
        assert after['screen']['managed'] and after['screen']['gamma_valid'], 'Integrated gamma owner not valid'
        assert preserved(a.state, after) == invariants, 'Verification changed preserved state'
        evidence.update(automatic_matches_real_main_display_source=True, final_awake=awake,
                        source_mode=status['mode'], rest_reason=status['rest_reason'], online_devices=sorted(ids),
                        required_wireless_verified=True, optional_usb_devices_do_not_gate=True,
                        gamma_valid=True, settings_and_power_plan_preserved=True)
        if a.record:
            a.record.write_text(json.dumps(evidence, indent=2), encoding='utf-8')
        print(json.dumps(evidence))


if __name__ == '__main__':
    main()
