"""Verify fresh source rebuilds in the native owner without desktop interaction.

Waits on native publication/exit, never a recovery deadline. If no source is
currently eligible, records that boundary without manufacturing a foreground app.
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
    p.add_argument('--state', type=Path, required=True)
    p.add_argument('--record', type=Path, required=True)
    p.add_argument('--exercise-recovery', action='store_true')
    p.add_argument('--require-rebuilds', action='store_true')
    p.add_argument('--require-wallpaper-image', action='store_true')
    a = p.parse_args()
    with Control(a.state) as client:
        before = client.call('snapshot')
        status = before['status']
        if a.require_rebuilds and not status['rest_reason'] and not status['input_frames']:
            before = client.preview()
            status = before['status']
        assert not status['diagnostic_error'] and not status['controller_error']
        assert not status['rest_resume']['error']
        result = {'pid': client.owner_pid, 'initial_mode': status['mode'],
                  'initial_rest_reason': status['rest_reason'], 'rebuilds': []}
        if a.exercise_recovery and status['has_valid_frame'] and not status['rest_reason'] and not status['output_paused']:
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
            handles = (W.HANDLE * 2)(process, notification)
            try:
                for _ in range(2):
                    generation = client.call('snapshot')['status']['source_generation']
                    client.call('recover')
                    while True:
                        current = client.call('snapshot')['status']
                        if current['rest_reason'] or current['mode'] == 'waiting':
                            result['external_source_or_rest_transition'] = True
                            break
                        assert not current['controller_error'] and not current['diagnostic_error']
                        if current['source_generation'] > generation and current['has_valid_frame'] and current['input_frames'] > 0:
                            assert not current['error'] and current['input_frames'] > 0
                            result['rebuilds'].append({key: current[key] for key in (
                                'source_generation', 'mode', 'first_frame_after_switch_ms',
                                'input_frames', 'device_submissions', 'capture_display')})
                            break
                        event = native.WaitForMultipleObjects(2, handles, False, 0xffffffff)
                        if event == 0:
                            raise RuntimeError('Owner exited during capture recovery')
                        if event != 1 or not native.FindNextChangeNotification(notification):
                            raise C.WinError(C.get_last_error())
                    if result.get('external_source_or_rest_transition'):
                        break
            finally:
                native.FindCloseChangeNotification(notification)
                native.CloseHandle(process)
        after = client.call('snapshot')
        assert after['settings'] == before['settings'] and after['layout'] == before['layout']
        assert after['screen']['settings'] == before['screen']['settings']
        result.update(final_mode=after['status']['mode'],
                      final_rest_reason=after['status']['rest_reason'],
                      fresh_rebuilds_verified=len(result['rebuilds']) == 2,
                      actual_unlock_tested=False, saved_preferences_preserved=True)
        if a.require_wallpaper_image:
            rows=[]
            for path in (a.state/'logs').glob('office-ambience-events.jsonl*'):
                with path.open(encoding='utf-8') as source:
                    for line in source:
                        try:
                            event=json.loads(line)
                        except json.JSONDecodeError:
                            continue
                        if event.get('pid')==client.owner_pid and event.get('event') in (
                            'owner_start','wallpaper_image_ready','wallpaper_image_submitted',
                            'wallpaper_image_replaced','capture_first_frame'):
                            rows.append(event)
            starts=[row for row in rows if row['event']=='owner_start']
            assert starts, 'Missing current owner journal identity'
            session=max(starts,key=lambda row:row['utc'])['session']
            rows=sorted((row for row in rows if row['session']==session),key=lambda row:row['sequence'])
            first={}
            for row in rows:
                first.setdefault(row['event'],row)
            ordered=('wallpaper_image_ready','wallpaper_image_submitted','capture_first_frame','wallpaper_image_replaced')
            result['wallpaper_image_events']=[{'event':key,'elapsed_ms':first[key]['elapsed_ms'],
                'data':{k:v for k,v in first[key]['data'].items() if k in ('load_ms','load_to_submit_ms','device_submissions','generation','hardware_acknowledged')}}
                for key in ordered if key in first]
            result['wallpaper_image_first_verified']=all(key in first for key in ordered) and all(
                first[left]['sequence']<first[right]['sequence'] for left,right in zip(ordered,ordered[1:]))
            result['wallpaper_image_error']=after['status']['wallpaper_image_error']
        a.record.write_text(json.dumps(result, indent=2), encoding='utf-8')
        print(json.dumps(result))
        if a.require_rebuilds:
            assert result['fresh_rebuilds_verified'], 'Two real fresh capture rebuilds are required for delivery'
        if a.require_wallpaper_image:
            assert result['wallpaper_image_first_verified'] and not result['wallpaper_image_error'], 'Image-first submission and fresh live handoff required'


if __name__ == '__main__':
    main()
