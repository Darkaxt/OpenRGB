"""Exercise the manual observer without hardware, desktop access or status files."""
import argparse
import contextlib
import io
import json
from pathlib import Path
import runpy
import sys
from types import SimpleNamespace
from unittest.mock import patch


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work', type=Path, required=True)
    work = parser.parse_args().work
    work.mkdir(parents=True, exist_ok=False)
    (work / 'owner.json').write_text(json.dumps({'pid': 123}), encoding='utf-8')
    source = Path(__file__).with_name('watch_ambience.py')

    for name, event, endpoint_pid, expected in (
        ('progress', 0x102, 123, None),
        ('owner-exit', 0, 123, 'Native owner exited'),
        ('different-owner', 0x102, 124, 'different owner'),
    ):
        calls = []
        closed = []

        class Control:
            owner_pid = endpoint_pid

            def __init__(self, state):
                assert state == work

            def __enter__(self):
                return self

            def __exit__(self, *args):
                closed.append('control')

            def call(self, command):
                assert command == 'snapshot'
                calls.append(command)
                return {'status': dict(mode='fixture', output_frames=20*(len(calls)-1),
                                       input_frames=len(calls), has_valid_frame=True,
                                       error='', updated_utc=str(len(calls)))}

        kernel = SimpleNamespace(WaitForSingleObject=lambda handle, cadence: event,
                                 CloseHandle=lambda handle: closed.append('process'))
        modules = {
            'office_control': SimpleNamespace(Control=Control),
            'runtime_control': SimpleNamespace(owned_process=lambda pid, state: (kernel, 1)),
            'process_metrics': SimpleNamespace(snapshot=lambda pid: {'cpu_seconds': 1}),
            'office_devices': SimpleNamespace(inventory=lambda client: {}),
            'openrgb': SimpleNamespace(OpenRGBClient=lambda *args, **kwargs:
                                     SimpleNamespace(disconnect=lambda: closed.append('sdk'))),
        }
        output = work / (name + '.json')
        with patch.dict(sys.modules, modules), patch.object(sys, 'argv', [
            str(source), '--state', str(work), '--frames', '20', '--output', str(output)
        ]), contextlib.redirect_stdout(io.StringIO()):
            try:
                runpy.run_path(str(source), run_name='__main__')
            except RuntimeError as error:
                assert expected and expected in str(error), str(error)
            else:
                assert expected is None, 'Observer accepted invalid owner/lifecycle'
                saved = json.loads(output.read_text())
                assert saved['status_samples'][-1]['output_frames'] == 20
                assert len(calls) == 2
        assert set(closed) == {'control', 'process', 'sdk'}, closed
        assert not (work / 'office-ambience-status.json').exists()
    print('PASS: live IPC progress, owner identity, early exit and resource release; no status file required')


if __name__ == '__main__':
    main()
