"""Read native caption/resize hit tests on the authenticated hidden Office owner.

No desktop input, foreground change, window movement or visibility change.
"""
import argparse
import ctypes as C
from ctypes import wintypes as W
import json
from pathlib import Path
from runtime_control import owned_process


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state',type=Path,required=True)
    p.add_argument('--record',type=Path,required=True)
    a=p.parse_args()
    owner=json.loads((a.state/'owner.json').read_text(encoding='utf-8-sig'))
    native,process=owned_process(owner['pid'],a.state)
    user=C.WinDLL('user32',use_last_error=True)
    callback=C.WINFUNCTYPE(W.BOOL,W.HWND,W.LPARAM)
    user.EnumWindows.argtypes=[callback,W.LPARAM]
    user.GetWindowThreadProcessId.argtypes=[W.HWND,C.POINTER(W.DWORD)]
    user.GetWindowTextW.argtypes=[W.HWND,W.LPWSTR,C.c_int]
    user.GetWindowRect.argtypes=[W.HWND,C.POINTER(W.RECT)]
    user.SendMessageW.argtypes=[W.HWND,W.UINT,W.WPARAM,W.LPARAM]
    user.SendMessageW.restype=C.c_ssize_t
    user.IsWindowVisible.argtypes=[W.HWND]
    user.SetThreadDpiAwarenessContext.argtypes=[W.HANDLE]
    user.SetThreadDpiAwarenessContext.restype=W.HANDLE
    previous=user.SetThreadDpiAwarenessContext(C.c_void_p(-4))
    windows=[]
    @callback
    def inspect(hwnd,unused):
        pid=W.DWORD();user.GetWindowThreadProcessId(hwnd,C.byref(pid))
        if pid.value==owner['pid']:
            title=C.create_unicode_buffer(256);user.GetWindowTextW(hwnd,title,256)
            if title.value=='Office Ambilight · OpenRGB':windows.append(hwnd)
        return True
    try:
        user.EnumWindows(inspect,0);assert len(windows)==1, 'Expected one native Office window'
        hwnd=windows[0];visible=bool(user.IsWindowVisible(hwnd));r=W.RECT()
        assert user.GetWindowRect(hwnd,C.byref(r))
        midx=(r.left+r.right)//2;midy=(r.top+r.bottom)//2
        tests=[('top-left',r.left+1,r.top+1,13),('top',midx,r.top+1,12),
               ('top-right',r.right-2,r.top+1,14),('right',r.right-2,midy,11),
               ('bottom-right',r.right-2,r.bottom-2,17),('bottom',midx,r.bottom-2,15),
               ('bottom-left',r.left+1,r.bottom-2,16),('left',r.left+1,midy,10)]
        for name,x,y,expected in tests:
            packed=(x&0xffff)|((y&0xffff)<<16)
            assert user.SendMessageW(hwnd,0x84,0,packed)==expected, name
        assert bool(user.IsWindowVisible(hwnd))==visible
        record={'owner_pid':owner['pid'],'all_eight_native_resize_edges_verified':True,
                'visibility_preserved':True,'headless':not visible,'desktop_input':False}
        a.record.write_text(json.dumps(record,indent=2),encoding='utf-8');print(json.dumps(record))
    finally:
        if previous:user.SetThreadDpiAwarenessContext(previous)
        native.CloseHandle(process)


if __name__=='__main__':main()
