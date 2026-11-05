"""Request graceful teardown of an office-owned Windows OpenRGB server.

The caller must verify its recorded process identity before using this helper.
SPDX-License-Identifier: GPL-2.0-or-later
"""
import argparse
import ctypes
from ctypes import wintypes
import json
from pathlib import Path


def owned_process(pid, state):
    owner = json.loads((state / 'owner.json').read_text(encoding='utf-8-sig'))
    if owner['pid'] != pid or not owner.get('graceful'):
        raise RuntimeError('Expected the recorded shutdown-capable owner')
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    kernel.OpenProcess.restype = wintypes.HANDLE
    kernel.OpenEventW.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.LPCWSTR]
    kernel.OpenEventW.restype = wintypes.HANDLE
    kernel.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
    kernel.GetProcessTimes.argtypes = [wintypes.HANDLE] + [ctypes.POINTER(wintypes.FILETIME)]*4
    kernel.GetExitCodeProcess.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    process = kernel.OpenProcess(0x101000, False, pid)
    if not process:
        raise ctypes.WinError(ctypes.get_last_error())
    try:
        times = [wintypes.FILETIME() for _ in range(4)]
        if not kernel.GetProcessTimes(process, *(ctypes.byref(value) for value in times)):
            raise ctypes.WinError(ctypes.get_last_error())
        created = (times[0].dwHighDateTime << 32) | times[0].dwLowDateTime
        # FILETIME starts in 1601; .NET DateTime ticks start in year 1.
        if created + 504911232000000000 != owner['startUtcTicks']:
            raise RuntimeError('Process identity differs from the recorded owner')
        return kernel, process
    except BaseException:
        kernel.CloseHandle(process)
        raise


def wait_ready(pid, state, event_name='Shutdown'):
    """Observe this process's native ready event, or its actual exit."""
    kernel, process = owned_process(pid, state)
    try:
        while True:
            event = kernel.OpenEventW(0x100000, False, f'Local\\OpenRGB.Office.{event_name}.{pid}')
            if event:
                kernel.CloseHandle(event)
                print(json.dumps({'ready': True, 'pid': pid, 'native_event_observed': True}))
                return
            if ctypes.get_last_error() != 2:
                raise ctypes.WinError(ctypes.get_last_error())
            # Diagnostic observation interval only. Expiry never changes the
            # operation or declares readiness/failure; the event or exit does.
            result = kernel.WaitForSingleObject(process, 1000)
            if result == 0:
                raise RuntimeError('OpenRGB exited before native readiness')
            if result != 0x102:
                raise ctypes.WinError(ctypes.get_last_error())
    finally:
        kernel.CloseHandle(process)


def stop_and_wait(pid, state):
    kernel, process = owned_process(pid, state)
    try:
        request_shutdown(pid)
        if kernel.WaitForSingleObject(process, 0xFFFFFFFF) != 0:
            raise ctypes.WinError(ctypes.get_last_error())
        code = wintypes.DWORD()
        if not kernel.GetExitCodeProcess(process, ctypes.byref(code)):
            raise ctypes.WinError(ctypes.get_last_error())
        print(json.dumps({'stopped': pid, 'exit_code': code.value, 'native_process_exit_observed': True}))
        if code.value:
            raise RuntimeError(f'OpenRGB exited abnormally: {code.value}')
    finally:
        kernel.CloseHandle(process)


def show(pid, state):
    """Activate the verified existing application; no second owner or UI client."""
    kernel, process = owned_process(pid, state)
    try:
        while True:
            if kernel.WaitForSingleObject(process, 0) == 0:
                raise RuntimeError('Office application exited before UI readiness')
            event = kernel.OpenEventW(0x0002, False, f'Local\\OpenRGB.Office.Show.{pid}')
            if event:
                try:
                    kernel.SetEvent.argtypes = [wintypes.HANDLE]
                    if not kernel.SetEvent(event):
                        raise ctypes.WinError(ctypes.get_last_error())
                    print(json.dumps({'activated': pid, 'new_process': False}))
                    return
                finally:
                    kernel.CloseHandle(event)
            if ctypes.get_last_error() != 2:
                raise ctypes.WinError(ctypes.get_last_error())
            kernel.WaitForSingleObject(process, 1000)
    finally:
        kernel.CloseHandle(process)


def request_shutdown(pid):
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel.OpenEventW.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.LPCWSTR]
    kernel.OpenEventW.restype = wintypes.HANDLE
    kernel.SetEvent.argtypes = [wintypes.HANDLE]
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    event = kernel.OpenEventW(0x0002, False, f'Local\\OpenRGB.Office.Shutdown.{pid}')
    if not event:
        raise ctypes.WinError(ctypes.get_last_error())
    try:
        if not kernel.SetEvent(event):
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        kernel.CloseHandle(event)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pid', type=int, required=True)
    parser.add_argument('--wait-ready', action='store_true')
    parser.add_argument('--wait-exit', action='store_true')
    parser.add_argument('--show', action='store_true')
    parser.add_argument('--state', type=Path)
    args = parser.parse_args()
    if args.wait_ready or args.wait_exit or args.show:
        if not args.state:
            parser.error('Process observation requires --state')
        if args.show:
            show(args.pid, args.state)
        elif args.wait_ready:
            wait_ready(args.pid, args.state)
        else:
            stop_and_wait(args.pid, args.state)
    else:
        request_shutdown(args.pid)
