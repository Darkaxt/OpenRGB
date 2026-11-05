"""Read per-display gamma ramps without changing the display or LightBulb."""
import argparse
import ctypes as C
from ctypes import wintypes as W
import json
from pathlib import Path
from inspect_sources import MonitorInfo, MONITORPROC, user


def inspect():
    gdi=C.WinDLL('gdi32',use_last_error=True)
    gdi.CreateDCW.argtypes=[W.LPCWSTR,W.LPCWSTR,W.LPCWSTR,C.c_void_p]
    gdi.CreateDCW.restype=W.HDC
    gdi.DeleteDC.argtypes=[W.HDC]
    gdi.GetDeviceGammaRamp.argtypes=[W.HDC,C.c_void_p]
    gdi.GetDeviceGammaRamp.restype=W.BOOL
    user.GetMonitorInfoW.argtypes=[W.HANDLE,C.POINTER(MonitorInfo)]
    user.EnumDisplayMonitors.argtypes=[W.HDC,C.c_void_p,MONITORPROC,W.LPARAM]
    results=[]
    @MONITORPROC
    def monitor(handle,unused_dc,rect,data):
        info=MonitorInfo();info.size=C.sizeof(info)
        if not user.GetMonitorInfoW(handle,C.byref(info)):return True
        dc=gdi.CreateDCW('DISPLAY',info.device,None,None)
        channels=(W.WORD*256*3)()
        try:
            ok=bool(dc and gdi.GetDeviceGammaRamp(dc,C.byref(channels)))
            ramps=[list(channel) for channel in channels]
            results.append({'display':info.device,'primary':bool(info.flags&1),'read_ok':ok,
                'white_rgb':[c[-1]/65535 for c in ramps] if ok else None,
                'brightness_estimate':max(c[-1] for c in ramps)/65535 if ok else None,
                'ramp_samples_rgb':[[c[i] for i in (0,64,128,192,255)] for c in ramps] if ok else None,
                'ramps_rgb':ramps if ok else None})
        finally:
            if dc:gdi.DeleteDC(dc)
        return True
    if not user.EnumDisplayMonitors(None,None,monitor,0):raise C.WinError(C.get_last_error())
    return results


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--record',type=Path);a=p.parse_args()
    results=inspect()
    if a.record:
        a.record.parent.mkdir(parents=True,exist_ok=True)
        a.record.write_text(json.dumps(results,indent=2))
    print(json.dumps([{k:v for k,v in r.items() if k!='ramps_rgb'} for r in results],indent=2))
