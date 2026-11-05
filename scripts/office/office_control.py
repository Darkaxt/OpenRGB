"""Authenticated control of the existing native owner; never writes RGB itself."""
import argparse
import ctypes as C
from ctypes import wintypes as W
import json
from pathlib import Path

kernel=C.WinDLL('kernel32',use_last_error=True)
kernel.CreateFileW.argtypes=[W.LPCWSTR,W.DWORD,W.DWORD,C.c_void_p,W.DWORD,W.DWORD,W.HANDLE]
kernel.CreateFileW.restype=W.HANDLE
kernel.ReadFile.argtypes=[W.HANDLE,C.c_void_p,W.DWORD,C.POINTER(W.DWORD),C.c_void_p]
kernel.WriteFile.argtypes=kernel.ReadFile.argtypes
kernel.CloseHandle.argtypes=[W.HANDLE]

def wait_ready(state,pid):
    """Wait for completed plugin/UI construction before reading its endpoint.

    The host creates Show only after the worker has constructed the engine and
    committed its private QSaveFile. Directory notifications can arrive while
    that file is still being replaced; they are not a publication barrier.
    """
    from runtime_control import wait_ready as native_ready
    native_ready(pid,state,event_name='Show')
    info=json.loads((state/'office-control.json').read_text(encoding='utf-8-sig'))
    if info.get('pid')!=pid or info.get('protocol')!=1:
        raise RuntimeError('Ready application published a different control endpoint')
    print(json.dumps({'control_ready':True,'pid':pid,'same_owner_endpoint':True}))

class Control:
    def __init__(self,state):
        info=json.loads((Path(state)/'office-control.json').read_text(encoding='utf-8-sig'))
        if info['protocol']!=1: raise ValueError('Incompatible owner protocol')
        self.token=info['token']; self.serial=0; self.pending=b''
        self.state=Path(state);self.owner_pid=info['pid']
        self.handle=kernel.CreateFileW('\\\\.\\pipe\\'+info['endpoint'],0xc0000000,0,None,3,0,None)
        if self.handle==C.c_void_p(-1).value: raise C.WinError(C.get_last_error())
    def __enter__(self): return self
    def __exit__(self,*args): kernel.CloseHandle(self.handle)
    def preview(self,**arguments):
        """Await asynchronous preview publication, driven by native status writes or owner exit."""
        from runtime_control import owned_process
        native,process=owned_process(self.owner_pid,self.state)
        native.FindFirstChangeNotificationW.argtypes=[W.LPCWSTR,W.BOOL,W.DWORD]
        native.FindFirstChangeNotificationW.restype=W.HANDLE
        native.FindNextChangeNotification.argtypes=[W.HANDLE]
        native.FindCloseChangeNotification.argtypes=[W.HANDLE]
        native.WaitForMultipleObjects.argtypes=[W.DWORD,C.POINTER(W.HANDLE),W.BOOL,W.DWORD]
        notification=native.FindFirstChangeNotificationW(str(self.state),False,0x1b)
        if notification==C.c_void_p(-1).value:
            native.CloseHandle(process);raise C.WinError(C.get_last_error())
        handles=(W.HANDLE*2)(process,notification)
        try:
            while True:
                value=self.call('snapshot',preview=True,**arguments)
                if value.get('preview_png'):return value
                if value.get('preview_error'):raise RuntimeError(value['preview_error'])
                result=native.WaitForMultipleObjects(2,handles,False,0xffffffff)
                if result==0:raise RuntimeError('Owner exited before preview publication')
                if result!=1:raise C.WinError(C.get_last_error())
                if not native.FindNextChangeNotification(notification):raise C.WinError(C.get_last_error())
        finally:
            native.FindCloseChangeNotification(notification);native.CloseHandle(process)
    def call(self,command,**arguments):
        self.serial+=1
        packet=(json.dumps(dict(arguments,command=command,id=self.serial,token=self.token))+'\n').encode()
        count=W.DWORD()
        if not kernel.WriteFile(self.handle,packet,len(packet),C.byref(count),None) or count.value!=len(packet):
            raise C.WinError(C.get_last_error())
        while b'\n' not in self.pending:
            buffer=C.create_string_buffer(65536)
            if not kernel.ReadFile(self.handle,buffer,len(buffer),C.byref(count),None): raise C.WinError(C.get_last_error())
            if not count.value: raise EOFError('Native owner disconnected')
            self.pending+=buffer.raw[:count.value]
            if len(self.pending)>2*1024*1024: raise ValueError('Oversized native reply')
        line,self.pending=self.pending.split(b'\n',1); response=json.loads(line)
        if response['id']!=self.serial: raise ValueError('Reply identity mismatch')
        if not response['ok']: raise ValueError(response['error'])
        return response['result']

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state',type=Path,default=Path('D:/Tools/OpenRGB/state-integration'))
    p.add_argument('--request',type=Path,help='JSON command document, without authentication values')
    p.add_argument('--output',type=Path)
    p.add_argument('--wait-ready',type=int,metavar='OWNER_PID')
    a=p.parse_args()
    if a.wait_ready:
        wait_ready(a.state,a.wait_ready);return
    request=json.loads(a.request.read_text()) if a.request else {'command':'snapshot'}
    with Control(a.state) as client: result=client.call(**request)
    encoded=json.dumps(result,indent=2)
    if a.output: a.output.write_text(encoded,encoding='utf-8')
    else: print(encoded)

if __name__=='__main__': main()
