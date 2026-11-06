"""Exercise native screen lifecycle, hotkey/exclusion and restart contracts.

Targets only the authenticated owner's hidden event window. No desktop input,
foreground changes, external gamma writes, process termination or clock changes.
"""
import argparse
import copy
import ctypes as C
from ctypes import wintypes as W
import json
from pathlib import Path
from office_control import Control
from inspect_gamma import inspect
from inspect_sources import user, WINDOWPROC


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase', choices=['exercise','prepare','restore'])
    p.add_argument('--state', type=Path, required=True)
    p.add_argument('--record', type=Path, required=True)
    a=p.parse_args()
    with Control(a.state) as client:
        baseline=client.call('snapshot');screen=baseline['screen'];evidence={}
        assert screen['managed'] and screen['gamma_valid']
        if a.phase=='prepare':
            assert not screen['lighting_disabled'] and not screen['screen_disabled']
            client.call('screen',action='offset',name='brightness_offset',delta=-.1)
            client.call('screen',action='pause',target='lighting',mode='duration',minutes=5)
            result=client.call('screen',action='pause',target='screen',mode='sunrise')
            record={'original_brightness_offset':screen['brightness_offset'],
                    'lighting_pause':result['lighting_pause'],'screen_pause':result['screen_pause'],
                    'layout':baseline['layout'],'settings':baseline['settings']}
            a.record.write_text(json.dumps(record,indent=2))
            print(json.dumps({'persistent_pause_and_offset_prepared':True}));return
        if a.phase=='restore':
            record=json.loads(a.record.read_text())
            assert screen['lighting_pause']==record['lighting_pause'] and screen['screen_pause']==record['screen_pause']
            assert screen['brightness_offset']==record['original_brightness_offset']-.1
            assert baseline['layout']==record['layout'] and baseline['settings']==record['settings']
            assert baseline['status']['output_paused']
            assert all(c==[0,0,0] for row in baseline['colors'] for c in row)
            client.call('screen',action='pause',target='lighting',mode='enable')
            client.call('screen',action='pause',target='screen',mode='enable')
            client.call('screen',action='offset',name='brightness_offset',delta=.1)
            record['restart_persistence_verified']=True;record['original_pauses_and_offsets_restored']=True
            a.record.write_text(json.dumps(record,indent=2))
            print(json.dumps({'restart_persistence_verified':True,'original_pauses_and_offsets_restored':True}));return

        user.GetWindowThreadProcessId.argtypes=[W.HWND,C.POINTER(W.DWORD)]
        user.GetClassNameW.argtypes=[W.HWND,W.LPWSTR,C.c_int]
        user.EnumWindows.argtypes=[WINDOWPROC,W.LPARAM]
        user.SendMessageW.argtypes=[W.HWND,W.UINT,W.WPARAM,W.LPARAM]
        user.SendMessageW.restype=C.c_ssize_t
        windows=[]
        @WINDOWPROC
        def window(hwnd,unused):
            pid=W.DWORD();user.GetWindowThreadProcessId(hwnd,C.byref(pid));name=C.create_unicode_buffer(256)
            user.GetClassNameW(hwnd,name,256)
            if pid.value==client.owner_pid and name.value=='OpenRGBOfficeCaptureEvents':windows.append(hwnd)
            return True
        user.EnumWindows(window,0);assert len(windows)==1
        hwnd=windows[0]
        kernel=C.WinDLL('kernel32',use_last_error=True)
        kernel.OpenProcess.argtypes=[W.DWORD,W.BOOL,W.DWORD];kernel.OpenProcess.restype=W.HANDLE
        kernel.QueryFullProcessImageNameW.argtypes=[W.HANDLE,W.DWORD,W.LPWSTR,C.POINTER(W.DWORD)]
        kernel.CloseHandle.argtypes=[W.HANDLE]
        user.GetForegroundWindow.restype=W.HWND
        foreground=user.GetForegroundWindow();pid=W.DWORD();user.GetWindowThreadProcessId(foreground,C.byref(pid))
        process=kernel.OpenProcess(0x1000,False,pid.value);assert process
        try:
            path=C.create_unicode_buffer(32768);length=W.DWORD(32768)
            assert kernel.QueryFullProcessImageNameW(process,0,path,C.byref(length))
        finally:kernel.CloseHandle(process)
        assert Path(path.value).name.lower() not in ('explorer.exe','shellexperiencehost.exe','startmenuexperiencehost.exe')

        def save(settings):
            current=client.call('snapshot')['screen']
            return client.call('screen',action='save',revision=current['revision'],settings=settings)

        # Native requests execute on the existing worker. Await actual output
        # frame transitions, never sleep to assume that a timer has fired.
        def frames_after(before):
            while True:
                result=client.call('snapshot')
                assert not result['screen']['error'],result['screen']['error']
                if result['status']['output_frames']>=before+2:return result

        try:
            client.call('screen',action='managed',enabled=False);neutral=inspect()
            settings=copy.deepcopy(screen['settings'])
            settings.update(IsManualSunriseSunsetEnabled=True,IsPauseWhenFullScreenEnabled=False,
                            IsApplicationWhitelistEnabled=False,IsConfigurationSmoothingEnabled=False,
                            IsGammaPollingEnabled=False,ManualSunriseTime='07:00:00',ManualSunsetTime='19:00:00')
            settings['DayConfiguration']=settings['NightConfiguration']={'Temperature':6600,'Brightness':.8}
            settings['ToggleHotKey']='Ctrl+Alt+Shift+F12'
            save(settings);client.call('screen',action='managed',enabled=True)
            for message,w in ((0x007e,32),(0x0218,0x12),(0x001e,0)):
                before=client.call('snapshot')['status']['output_frames'];user.SendMessageW(hwnd,message,w,0)
                value=frames_after(before);assert value['screen']['gamma_valid']
                current=inspect()
                originals={d['display']:d for d in neutral}
                for d in current:
                    assert abs(d['ramps_rgb'][0][192]/originals[d['display']]['ramps_rgb'][0][192]-.8)<.002
            evidence['display_resume_time_events_preserve_single_gamma_factor']=True
            user.SendMessageW(hwnd,0x0312,0x4c00,0)
            value=client.call('snapshot');assert value['screen']['screen_disabled'] and not value['status']['output_paused']
            user.SendMessageW(hwnd,0x0312,0x4c00,0)
            assert not client.call('snapshot')['screen']['screen_disabled']
            evidence['native_hotkey_handler_toggles_screen_only']=True
            settings['IsApplicationWhitelistEnabled']=True
            settings['WhitelistedApplications']=[{'ExecutableFilePath':path.value}]
            assert user.GetForegroundWindow()==foreground,'Foreground changed before exclusion test'
            save(settings);before=client.call('snapshot')['status']['output_frames'];value=frames_after(before)
            assert user.GetForegroundWindow()==foreground,'Foreground changed during exclusion test'
            assert value['screen']['automatic_pause']=='excluded-application'
            assert not value['status']['output_paused'] and value['status']['has_valid_frame']
            assert value['screen']['brightness']==1
            evidence['actual_foreground_exclusion_preserves_rgb_capture']=True
        finally:
            client.call('screen',action='pause',target='screen',mode='enable')
            save(screen['settings']);client.call('screen',action='managed',enabled=screen['managed'])
            result=client.call('snapshot')
            assert result['layout']==baseline['layout'] and result['settings']==baseline['settings']
            assert result['screen']['settings']==screen['settings']
            evidence['original_settings_and_map_restored']=True
        a.record.write_text(json.dumps(evidence,indent=2));print(json.dumps(evidence))


if __name__=='__main__':main()
