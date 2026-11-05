"""Read-only native monitor/window source diagnostics; no desktop interaction."""
import ctypes as C
from ctypes import wintypes as W
import json

user = C.WinDLL('user32', use_last_error=True)
MONITORPROC = C.WINFUNCTYPE(W.BOOL, W.HANDLE, W.HDC, C.POINTER(W.RECT), W.LPARAM)
WINDOWPROC = C.WINFUNCTYPE(W.BOOL, W.HWND, W.LPARAM)


class MonitorInfo(C.Structure):
    _fields_ = [('size', W.DWORD), ('monitor', W.RECT), ('work', W.RECT), ('flags', W.DWORD), ('device', W.WCHAR * 32)]


def main():
    monitors, shells = [], []
    user.SetThreadDpiAwarenessContext.argtypes = [C.c_void_p]
    user.SetThreadDpiAwarenessContext.restype = C.c_void_p
    previous_dpi = user.SetThreadDpiAwarenessContext(C.c_void_p(-4))
    user.GetMonitorInfoW.argtypes = [W.HANDLE, C.POINTER(MonitorInfo)]
    user.GetClassNameW.argtypes = [W.HWND, W.LPWSTR, C.c_int]
    user.GetWindowRect.argtypes = [W.HWND, C.POINTER(W.RECT)]
    user.IsWindowVisible.argtypes = [W.HWND]
    user.EnumDisplayMonitors.argtypes = [W.HDC, C.c_void_p, MONITORPROC, W.LPARAM]
    user.EnumWindows.argtypes = [WINDOWPROC, W.LPARAM]

    @MONITORPROC
    def monitor(handle, dc, rect, data):
        value = MonitorInfo()
        value.size = C.sizeof(value)
        if user.GetMonitorInfoW(handle, C.byref(value)):
            monitors.append({'name': value.device, 'primary': bool(value.flags & 1), 'bounds': [value.monitor.left, value.monitor.top, value.monitor.right, value.monitor.bottom]})
        return True

    @WINDOWPROC
    def window(handle, data):
        name = C.create_unicode_buffer(256)
        user.GetClassNameW(handle, name, len(name))
        if name.value in ('Progman', 'WorkerW'):
            rect = W.RECT()
            user.GetWindowRect(handle, C.byref(rect))
            shells.append({'hwnd': int(handle), 'class': name.value, 'visible': bool(user.IsWindowVisible(handle)), 'bounds': [rect.left, rect.top, rect.right, rect.bottom]})
        return True

    user.EnumDisplayMonitors(None, None, monitor, 0)
    user.EnumWindows(window, 0)
    if previous_dpi:
        user.SetThreadDpiAwarenessContext(previous_dpi)
    print(json.dumps({'monitors': monitors, 'wallpaper_hosts': shells}, indent=2))


if __name__ == '__main__':
    main()
