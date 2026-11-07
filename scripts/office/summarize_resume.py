"""Retain bounded, private-value-free capture recovery timing from native logs."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--logs', type=Path, required=True)
    parser.add_argument('--prefix', required=True, help='UTC timestamp prefix')
    parser.add_argument('--pid', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    events = []
    waiting = 0
    for path in args.logs.glob('office-ambience-events.jsonl*'):
        with path.open(encoding='utf-8') as source:
            for line in source:
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue  # The active writer may not have completed its line.
                if row.get('pid') != args.pid or not row.get('utc', '').startswith(args.prefix):
                    continue
                event, data = row['event'], row.get('data', {})
                if event == 'source_switch_begin' and not data.get('new_hwnd'):
                    waiting += 1
                    continue
                if event in ('source_switch_begin', 'capture_first_frame', 'session_event',
                             'rest_transition', 'gpu_create_begin', 'gpu_create_complete',
                             'capture_start_complete', 'capture_error', 'capture_create_error',
                             'wallpaper_image_ready','wallpaper_image_submitted','wallpaper_image_replaced'):
                    safe = {key: data[key] for key in ('notification', 'reason', 'generation',
                            'old_generation', 'new_hwnd', 'mode', 'source_process', 'hresult',
                            'load_ms','load_to_submit_ms','device_submissions','hardware_acknowledged') if key in data}
                    events.append({'utc': row['utc'], 'elapsed_ms': row['elapsed_ms'],
                                   'event': event, 'data': safe})
    events.sort(key=lambda row: row['elapsed_ms'])
    report = {'pid': args.pid, 'utc_prefix': args.prefix, 'waiting_observations': waiting, 'events': events}
    args.output.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
