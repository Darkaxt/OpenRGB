"""Verify native Windows SDK shutdown with no, idle and disconnecting clients.

All detectors are disabled. Uses actual native readiness/shutdown events and
process completion; no execution-kill deadline, retry or second RGB writer.
"""
import argparse
import ctypes as C
from ctypes import wintypes as W
import json
import os
from pathlib import Path
import socket
import subprocess
from govee_trial import detector_inventory
from runtime_control import wait_ready, stop_and_wait


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--exe',type=Path,required=True)
    p.add_argument('--source',type=Path,required=True)
    p.add_argument('--work',type=Path,required=True)
    a=p.parse_args();a.work.mkdir(parents=True,exist_ok=False)
    kernel=C.WinDLL('kernel32',use_last_error=True)
    kernel.GetProcessTimes.argtypes=[W.HANDLE]+[C.POINTER(W.FILETIME)]*4
    results=[]
    cases=[('no-client',0,False),('idle-client',1,False),('idle-clients',8,False),('disconnected-clients',32,True)]
    for round_number in range(3):
        for name,count,disconnect in cases:
            state=a.work/f'{round_number}-{name}';state.mkdir()
            (state/'OpenRGB.json').write_text(json.dumps({'Detectors':{'detectors':{k:False for k in detector_inventory(a.source)}},'LogManager':{'log_console':False,'log_file':True}}))
            environment=dict(os.environ,OPENRGB_OFFICE_SHUTDOWN='1',TEMP=str(state),TMP=str(state))
            environment.pop('OPENRGB_OFFICE_PLUGIN',None)
            clients=[]
            with (state/'stdout.log').open('w') as output:
                process=subprocess.Popen([str(a.exe.resolve()),'--config',str(state.resolve()),'--noautoconnect','--server','--server-host','127.0.0.1','--loglevel','info'],env=environment,stdout=output,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)
                times=[W.FILETIME() for _ in range(4)]
                assert kernel.GetProcessTimes(int(process._handle),*(C.byref(t) for t in times))
                ticks=((times[0].dwHighDateTime<<32)|times[0].dwLowDateTime)+504911232000000000
                (state/'owner.json').write_text(json.dumps({'pid':process.pid,'startUtcTicks':ticks,'executable':str(a.exe.resolve()),'graceful':True}))
                try:
                    wait_ready(process.pid,state)
                    for _ in range(count):clients.append(socket.create_connection(('127.0.0.1',6742)))
                    if disconnect:
                        for client in clients:client.close()
                        clients.clear()
                    stop_and_wait(process.pid,state)
                    assert process.wait()==0
                    results.append({'round':round_number,'case':name,'native_exit':0})
                    print(json.dumps(results[-1]),flush=True)
                finally:
                    for client in clients:client.close()
                    (a.work/'shutdown-results.json').write_text(json.dumps(results,indent=2))
    print(json.dumps({'sdk_shutdown_with_absent_idle_disconnected_clients':True,'all_detectors_disabled':True}))


if __name__=='__main__':main()
