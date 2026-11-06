"""Observe a natural screensaver cycle on the one native owner, without input/settings changes.

Only state, input-event timestamps and output counts are retained. No keys, pixel
captures, locations, authentication material or complete private snapshots.
"""
import argparse
import ctypes as C
from ctypes import wintypes as W
import json
from pathlib import Path
from office_control import Control
from runtime_control import owned_process


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase', choices=['rest', 'resume'])
    p.add_argument('--state', type=Path, required=True)
    p.add_argument('--record', type=Path, required=True)
    a = p.parse_args()
    record = json.loads(a.record.read_text()) if a.phase == 'resume' else {'observations': []}
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
        previous = None
        try:
            while True:
                value = client.call('snapshot')
                status = value['status']
                gate = status['rest_resume']
                assert not gate['error'], gate['error']
                online = {d['id'] for d, yes in zip(value['layout'], value['online']) if yes}
                assert {'H6609', 'H8048', 'Secretlab'} <= online, 'Required wireless light missing'
                black = all(c == [0, 0, 0] for row in value['colors'] for c in row)
                state = (status['rest_reason'], gate['held'], gate['last_input_tick'], black, status['output_paused'])
                observation = {'utc': status['updated_utc'], 'pid': client.owner_pid,
                               'rest_reason': status['rest_reason'], 'mode': status['mode'],
                               'gate': gate, 'all_314_output_colors_black': black,
                               'awake_active': status['awake']['active'],
                               'manual_lighting_pause': status['output_paused'],
                               'device_submissions': status['device_submissions'],
                               'led_writes': status['led_writes'], 'online': sorted(online)}
                if state != previous:
                    record['observations'].append(observation)
                    a.record.write_text(json.dumps(record, indent=2))
                    print(json.dumps(observation), flush=True)
                    previous = state
                if gate['held']:
                    assert black and not status['awake']['active'], 'Rest gate failed to suppress RGB/Awake'
                if a.phase == 'rest' and status['rest_reason'] == 'automatic-screensaver' and gate['held'] and black and not status['output_paused']:
                    assert gate['input_query_ok']
                    record['natural_rest'] = observation
                    a.record.write_text(json.dumps(record, indent=2))
                    print(json.dumps({'natural_idle_screensaver_observed': True,
                                      'black_output_and_awake_release_verified': True,
                                      'physical_radio_acknowledgment': False}), flush=True)
                    return
                if a.phase == 'resume' and not gate['held'] and not status['rest_reason'] and status['has_valid_frame'] and status['input_frames'] > 0:
                    assert gate['input_query_ok'] and gate['last_input_tick'] != record['natural_rest']['gate']['entry_input_tick'], 'Resume lacked a new input event'
                    record['natural_resume'] = observation
                    record['fresh_frame_after_input_verified'] = True
                    a.record.write_text(json.dumps(record, indent=2))
                    print(json.dumps({'new_input_resume_and_fresh_capture_verified': True}), flush=True)
                    return
                result = native.WaitForMultipleObjects(2, handles, False, 0xffffffff)
                if result == 0:
                    raise RuntimeError('Original native owner exited during natural-cycle observation')
                if result != 1 or not native.FindNextChangeNotification(notification):
                    raise C.WinError(C.get_last_error())
        finally:
            native.FindCloseChangeNotification(notification)
            native.CloseHandle(process)


if __name__ == '__main__':
    main()
