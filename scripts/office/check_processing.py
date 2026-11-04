"""Verify installed GPU control wiring through the actual native owner.

Preserves the current six-device map and restores all settings in finally.
No separate RGB writer and no host desktop interaction.
"""
import argparse
import copy
import json
from pathlib import Path
from office_control import Control


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state', type=Path, required=True)
    parser.add_argument('--record', type=Path, required=True)
    args = parser.parse_args()
    evidence = {}
    with Control(args.state) as client:
        baseline = client.call('snapshot', preview=True)
        assert baseline['test_mode'] == 'none', 'Finish the current identify/calibration first'
        settings = copy.deepcopy(baseline['settings'])

        def save():
            current = client.call('snapshot')
            result = client.call('save', revision=current['revision'], settings=settings, layout=baseline['layout'])
            assert result['layout'] == baseline['layout']
            assert result['settings'] == settings
            while True:
                value = client.call('snapshot')
                if value['status']['output_frames'] > result['status']['output_frames']:
                    return value

        try:
            settings.update(enabled=True, smoothing_ms=0, smoothing_mode='time', brightness=0)
            dark = save()
            assert all(c == [0, 0, 0] for row in dark['colors'] for c in row)
            evidence['brightness_reaches_native_led_output'] = True
            settings.update(brightness=1, saturation=0)
            gray = save()
            assert all(max(c)-min(c) <= 1 for row in gray['colors'] for c in row)
            assert any(any(c) for row in gray['colors'] for c in row)
            evidence['saturation_reaches_native_led_output'] = True
            settings.update(saturation=1, depth=12, adaptive_min=3, adaptive_max=20, blur=2)
            for strategy in ('mapped', 'fixed', 'adaptive', 'percentile', 'dominant'):
                settings['strategy'] = strategy
                result = save()
                assert len(result['effective_regions']) == 6
                for regions, device in zip(result['effective_regions'], baseline['layout']):
                    assert len(regions) == len(device['regions'])
                    for left, top, right, bottom in regions:
                        assert 0 <= left < right <= 1 and 0 <= top < bottom <= 1
                evidence[strategy] = {'settings_roundtrip': True, 'live_gpu_regions': True}
            revision = result['revision']
            invalid = copy.deepcopy(settings)
            invalid['adaptive_min'] = 40
            try:
                client.call('save', revision=revision, settings=invalid, layout=baseline['layout'])
            except ValueError as error:
                assert 'minimum' in str(error)
            else:
                raise AssertionError('Inverted adaptive bounds accepted')
            unchanged = client.call('snapshot')
            assert unchanged['revision'] == revision and unchanged['settings'] == settings
            evidence['invalid_settings_transaction_leaves_map_and_settings_unchanged'] = True
        finally:
            settings = baseline['settings']
            restored = save()
            assert restored['settings'] == baseline['settings'] and restored['layout'] == baseline['layout']
            evidence['original_map_and_settings_restored'] = True
        args.record.write_text(json.dumps(evidence, indent=2), encoding='utf-8')
        print(json.dumps(evidence))


if __name__ == '__main__':
    main()
