"""Observe actual office output progress and Windows process resource counters.

Diagnostic observation only: no timeout cancels or restarts capture, and no LEDs
are written by this observer. Its endpoint is an actual output-counter advance.
"""
import argparse
import ctypes
import json
import os
from pathlib import Path
import time
import hashlib
from process_metrics import snapshot
from runtime_control import owned_process
from office_control import Control
from office_devices import inventory
from openrgb import OpenRGBClient

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--state', type=Path, required=True)
p.add_argument('--frames', type=int, default=450)
p.add_argument('--output', type=Path, required=True)
a = p.parse_args()
owner = json.loads((a.state / 'owner.json').read_text(encoding='utf-8-sig'))
kernel, process = owned_process(owner['pid'], a.state)
baseline = None
samples = []
began = time.perf_counter()
before = snapshot(owner['pid'])
client = OpenRGBClient('127.0.0.1',6742,name='Office ambience observer',protocol_version=3)
devices = inventory(client)
try:
    with Control(a.state) as control:
        if control.owner_pid != owner['pid']:
            raise RuntimeError('Control endpoint belongs to a different owner')
        while True:
            report = control.call('snapshot')['status']
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
            # This manually invoked diagnostic samples live IPC, never disk counters.
            # Its cadence does not decide completion/failure; only progress or exit does.
            result = kernel.WaitForSingleObject(process, 1000)
            if result == 0:
                raise RuntimeError('Native owner exited before requested output progress')
            if result != 0x102:
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
    kernel.CloseHandle(process)
