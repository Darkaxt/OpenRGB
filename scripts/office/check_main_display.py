"""Check actual native main-display capture without changing Windows or the map."""
import argparse
import ctypes as C
from ctypes import wintypes as W
import hashlib
import json
from pathlib import Path
from office_control import Control
from inspect_sources import MonitorInfo, MONITORPROC, user


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state',type=Path,required=True)
    p.add_argument('--record',type=Path,required=True)
    p.add_argument('--expected-config-sha256',required=True)
    a=p.parse_args()
    saved=a.state/'office-ambience.json'
    before=hashlib.sha256(saved.read_bytes()).hexdigest()
    assert before==a.expected_config_sha256.lower(),'Saved settings changed before the check'
    user.SetThreadDpiAwarenessContext.argtypes=[C.c_void_p]
    user.SetThreadDpiAwarenessContext.restype=C.c_void_p
    user.GetMonitorInfoW.argtypes=[W.HANDLE,C.POINTER(MonitorInfo)]
    user.EnumDisplayMonitors.argtypes=[W.HDC,C.c_void_p,MONITORPROC,W.LPARAM]
    previous=user.SetThreadDpiAwarenessContext(C.c_void_p(-4))
    primary=[]
    @MONITORPROC
    def monitor(handle,dc,rect,data):
        info=MonitorInfo();info.size=C.sizeof(info)
        if user.GetMonitorInfoW(handle,C.byref(info)) and info.flags&1:
            primary.append({'name':info.device,'bounds':[info.monitor.left,info.monitor.top,info.monitor.right,info.monitor.bottom]})
        return True
    try:
        assert user.EnumDisplayMonitors(None,None,monitor,0) and len(primary)==1
        with Control(a.state) as client:
            actual=client.preview()
        status=actual['status']
        assert actual['settings']['monitor']=='primary' and status['monitor_policy']=='primary'
        assert status['capture_display']==primary[0]['name'] and status['capture_bounds']==primary[0]['bounds']
        assert status['has_valid_frame'] and status['input_frames']>0 and not status['rest_reason'] and not status['error']
        assert len(actual['layout'])==6 and sum(map(len,actual['colors']))==314
        assert hashlib.sha256(saved.read_bytes()).hexdigest()==before
        result={'windows_main_display':primary[0],'mode':status['mode'],'input_frames':status['input_frames'],
            'output_fps':status['output_fps'],'source_generation':status['source_generation'],
            'actual_preview':bool(actual['preview_png']),'configured_devices':6,'led_values':314,
            'online_devices':sum(actual['online']),'saved_settings_unchanged':True,
            'saved_settings_sha256':before,'actual_main_display_matches_native_capture':True,
            'physical_undock_tested':False}
        a.record.parent.mkdir(parents=True,exist_ok=True)
        a.record.write_text(json.dumps(result,indent=2))
        print(json.dumps(result))
    finally:
        if previous:user.SetThreadDpiAwarenessContext(previous)


if __name__=='__main__':main()
