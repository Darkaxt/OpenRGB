"""Observe actual office output progress and Windows process resource counters.

Diagnostic observation only: no timeout cancels or restarts capture, and no LEDs
are written by this observer. Its endpoint is an actual output-counter advance.
"""
import argparse
import ctypes
from ctypes import wintypes
import json
import os
from pathlib import Path
import time
import hashlib
from process_metrics import snapshot
from runtime_control import owned_process
from office_devices import inventory
from openrgb import OpenRGBClient

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--state', type=Path, required=True)
p.add_argument('--frames', type=int, default=450)
p.add_argument('--output', type=Path, required=True)
a = p.parse_args()
owner = json.loads((a.state / 'owner.json').read_text(encoding='utf-8-sig'))
kernel, process = owned_process(owner['pid'], a.state)
kernel.FindFirstChangeNotificationW.argtypes = [wintypes.LPCWSTR, wintypes.BOOL, wintypes.DWORD]
kernel.FindFirstChangeNotificationW.restype = wintypes.HANDLE
kernel.FindNextChangeNotification.argtypes = [wintypes.HANDLE]
kernel.FindCloseChangeNotification.argtypes = [wintypes.HANDLE]
kernel.WaitForMultipleObjects.argtypes = [wintypes.DWORD, ctypes.POINTER(wintypes.HANDLE), wintypes.BOOL, wintypes.DWORD]
change = kernel.FindFirstChangeNotificationW(str(a.state), False, 0x1B)
if change == ctypes.c_void_p(-1).value:
    raise ctypes.WinError(ctypes.get_last_error())
handles = (wintypes.HANDLE * 2)(process, change)
path = a.state / 'office-ambience-status.json'
kernel.CreateFileW.argtypes = [wintypes.LPCWSTR,wintypes.DWORD,wintypes.DWORD,ctypes.c_void_p,wintypes.DWORD,wintypes.DWORD,wintypes.HANDLE]
kernel.CreateFileW.restype = wintypes.HANDLE
kernel.GetFileSizeEx.argtypes = [wintypes.HANDLE,ctypes.POINTER(ctypes.c_longlong)]
kernel.ReadFile.argtypes = [wintypes.HANDLE,ctypes.c_void_p,wintypes.DWORD,ctypes.POINTER(wintypes.DWORD),ctypes.c_void_p]

def read_status():
    # QSaveFile replaces the file identity. A diagnostic reader must permit that
    # replacement, unlike Python's default Windows file sharing mode.
    handle = kernel.CreateFileW(str(path),0x80000000,7,None,3,0,None)
    if handle == ctypes.c_void_p(-1).value:
        code = ctypes.get_last_error()
        if code in (2,5,32):
            return None  # A replacement is in progress; await the directory event.
        raise ctypes.WinError(code)
    try:
        size = ctypes.c_longlong()
        if not kernel.GetFileSizeEx(handle,ctypes.byref(size)):
            raise ctypes.WinError(ctypes.get_last_error())
        buffer = ctypes.create_string_buffer(size.value)
        read = wintypes.DWORD()
        if not kernel.ReadFile(handle,buffer,size.value,ctypes.byref(read),None):
            raise ctypes.WinError(ctypes.get_last_error())
        if read.value != size.value:
            raise RuntimeError('Incomplete immutable status record')
        return json.loads(buffer.raw)
    finally:
        kernel.CloseHandle(handle)
baseline = None
samples = []
began = time.perf_counter()
before = snapshot(owner['pid'])
client = OpenRGBClient('127.0.0.1',6742,name='Office ambience observer',protocol_version=3)
devices = inventory(client)
try:
    while True:
        report = read_status()
        if report is not None:
            if not samples or report['updated_utc'] != samples[-1]['updated_utc']:
                report['controller_colors'] = {}
                for name,device in devices.items():
                    device.update()
                    rgb = bytes(channel for color in device.colors for channel in (color.red,color.green,color.blue))
                    report['controller_colors'][name] = dict(leds=len(device.colors),sha256=hashlib.sha256(rgb).hexdigest(),maximum=max(rgb),minimum=min(rgb))
                samples.append(report)
                if baseline is None:
                    baseline = report['output_frames']
                print(json.dumps({key: report[key] for key in ('mode', 'output_frames', 'input_frames', 'has_valid_frame', 'error')}), flush=True)
                if report['output_frames'] - baseline >= a.frames:
                    break
        # Windows can delay notifications; this health rescan never decides
        # completion or failure from elapsed time. Only progress or exit does.
        result = kernel.WaitForMultipleObjects(2, handles, False, 1000)
        if result == 0:
            raise RuntimeError('Native owner exited before requested output progress')
        if result == 1:
            if not kernel.FindNextChangeNotification(change):
                raise ctypes.WinError(ctypes.get_last_error())
        elif result != 0x102:
            raise ctypes.WinError(ctypes.get_last_error())
    after = snapshot(owner['pid'])
    elapsed = time.perf_counter() - began
    outcome = dict(pid=owner['pid'], elapsed_seconds=elapsed,
                   observed_output_fps=(samples[-1]['output_frames']-baseline)/elapsed,
                   total_cpu_percent=(after['cpu_seconds']-before['cpu_seconds'])/elapsed/os.cpu_count()*100,
                   resources=after, status_samples=samples)
    with a.output.open('x', encoding='utf-8') as f:
        json.dump(outcome, f, indent=2)
    print(json.dumps({key: value for key,value in outcome.items() if key != 'status_samples'}))
finally:
    client.disconnect()
    kernel.FindCloseChangeNotification(change)
    kernel.CloseHandle(process)
