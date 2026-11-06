"""Verify the sundial's metadata against the real owner's complete cycle preview.

Uses the authenticated existing owner; no separate clock/gamma writer, desktop
input or private settings output. The monitoring cadence never ends the preview.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path
from office_control import Control


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state', type=Path, required=True)
    p.add_argument('--record', type=Path, required=True)
    a = p.parse_args()
    original_file = Path.home()/'AppData/Roaming/LightBulb/Settings.json'
    original_hash = hashlib.sha256(original_file.read_bytes()).hexdigest()
    samples = []
    with Control(a.state) as client:
        before = client.call('snapshot')
        screen = before['screen']
        assert screen['managed'] and screen['gamma_valid'] and not screen['preview']
        initial = client.call('screen', action='preview')
        assert initial['preview'] and initial['cycle_times']
        started = time.monotonic()
        try:
            while True:
                value = client.call('snapshot')
                s = value['screen']
                assert not s['error'], s['error']
                if not s['preview']:
                    break
                assert s['gamma_valid'] and 0 <= s['cycle_seconds'] < 86400
                assert set(s['cycle_times']) == {'sunrise_start', 'sunrise_end', 'sunset_start', 'sunset_end'}
                assert s['cycle_state'] in ('day', 'night', 'transition')
                assert abs(s['temperature']-s['target_temperature']) <= 15.1
                assert abs(s['brightness']-s['target_brightness']) <= .011
                samples.append({'elapsed': time.monotonic()-started, 'seconds': s['cycle_seconds'],
                                'state': s['cycle_state'], 'brightness': s['brightness']})
                # Read-only diagnostic cadence; completion is the owner's actual
                # preview->normal transition, with no cancellation deadline.
                time.sleep(.2)
            advances = [(b['seconds']-a['seconds']) % 86400 for a,b in zip(samples,samples[1:])]
            assert sum(advances) > 80000, 'Did not observe the actual complete preview day'
            elapsed = samples[-1]['elapsed']-samples[0]['elapsed']
            assert 5900 < sum(advances)/elapsed < 6100, 'Sundial metadata diverges from owner preview clock'
        finally:
            if client.call('snapshot')['screen']['preview']:
                client.call('screen', action='preview')
        after = client.call('snapshot')
        for key in ('settings', 'layout'):
            assert after[key] == before[key]
        for key in ('settings', 'managed', 'screen_pause', 'lighting_pause', 'temperature_offset', 'brightness_offset'):
            assert after['screen'][key] == screen[key]
        assert hashlib.sha256(original_file.read_bytes()).hexdigest() == original_hash
        record = {'real_owner_full_day_preview': True, 'cycle_clock_speed': sum(advances)/elapsed,
                  'applied_gamma_matches_preview_target': True, 'samples': samples,
                  'settings_topology_pauses_offsets_preserved': True, 'standalone_source_preserved': True,
                  'owner_pid': client.owner_pid, 'preview_completed_natively': True}
        a.record.write_text(json.dumps(record, indent=2), encoding='utf-8')
        print(json.dumps({k:v for k,v in record.items() if k != 'samples'}))


if __name__ == '__main__':
    main()
