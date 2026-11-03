"""Request graceful teardown of an office-owned Windows OpenRGB server.

The caller must verify its recorded process identity before using this helper.
SPDX-License-Identifier: GPL-2.0-or-later
"""
import argparse
import ctypes
from ctypes import wintypes


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
    request_shutdown(parser.parse_args().pid)
