"""Verify integrated screen adjustment through the installed native owner.

Uses the existing authenticated pipe and read-only gamma inspection. Never writes
gamma itself, sends desktop input, or creates another RGB owner. Restores the
original screen settings and RGB topology in finally; evidence excludes location.
"""
import argparse
import copy
import ctypes as C
from ctypes import wintypes as W
import hashlib
import json
import subprocess
from pathlib import Path
from office_control import Control
from inspect_gamma import inspect
from runtime_control import owned_process


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state', type=Path, required=True)
    p.add_argument('--record', type=Path, required=True)
    p.add_argument('--guard-only', action='store_true')
    a = p.parse_args()
    source = Path.home()/'AppData/Roaming/LightBulb/Settings.json'
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    evidence = {}
    with Control(a.state) as client:
        baseline = client.call('snapshot')
        original = baseline['screen']
        imported = json.loads(source.read_text(encoding='utf-8-sig'))
        assert all(original['settings'].get(k) == v for k, v in imported.items()), 'Imported source settings differ'
        evidence['all_original_settings_imported'] = True
        if a.guard_only:
            assert not original['managed']
            processes = subprocess.check_output(['tasklist', '/FI', 'IMAGENAME eq LightBulb.exe', '/FO', 'CSV', '/NH'], text=True)
            if 'lightbulb.exe' not in processes.lower():
                # A user may gracefully exit it while rendered validation runs.
                # Preserve an earlier guard receipt; never enable gamma merely
                # to test rejection when there is no competing owner.
                print(json.dumps({'competing_owner_guard': 'not applicable: standalone already exited',
                                  'gamma_ownership_changed': False}))
                return
            try:
                client.call('screen', action='managed', enabled=True)
            except ValueError as error:
                assert 'standalone LightBulb' in str(error)
            else:
                raise AssertionError('Competing standalone owner was accepted')
            evidence['competing_gamma_owner_rejected'] = True
        else:
            assert original['managed'], 'Enable the integrated owner after standalone exits'
            assert not original['lighting_disabled'] and not original['screen_disabled']
            assert baseline['test_mode'] == 'none'
            native, process = owned_process(client.owner_pid, a.state)
            native.FindFirstChangeNotificationW.argtypes = [W.LPCWSTR, W.BOOL, W.DWORD]
            native.FindFirstChangeNotificationW.restype = W.HANDLE
            native.FindNextChangeNotification.argtypes = [W.HANDLE]
            native.FindCloseChangeNotification.argtypes = [W.HANDLE]
            native.WaitForMultipleObjects.argtypes = [W.DWORD, C.POINTER(W.HANDLE), W.BOOL, W.DWORD]
            notification = native.FindFirstChangeNotificationW(str(a.state), False, 0x1b)
            if notification == C.c_void_p(-1).value:
                native.CloseHandle(process)
                raise C.WinError(C.get_last_error())
            handles = (W.HANDLE*2)(process, notification)

            def await_state(predicate):
                while True:
                    value = client.call('snapshot')
                    assert not value['screen']['error'], value['screen']['error']
                    if predicate(value):
                        return value
                    result = native.WaitForMultipleObjects(2, handles, False, 0xffffffff)
                    if result == 0:
                        raise RuntimeError('Native owner exited during screen verification')
                    if result != 1 or not native.FindNextChangeNotification(notification):
                        raise C.WinError(C.get_last_error())

            def save(settings):
                current = client.call('snapshot')['screen']
                return client.call('screen', action='save', revision=current['revision'], settings=settings)

            try:
                rgb_settings = copy.deepcopy(baseline['settings'])
                rgb_settings['follow_display_brightness'] = True
                client.call('save', revision=baseline['revision'], settings=rgb_settings, layout=baseline['layout'])
                client.call('screen', action='managed', enabled=False)
                neutral = inspect()
                assert neutral and all(d['read_ok'] for d in neutral)
                settings = copy.deepcopy(original['settings'])
                settings.update(IsManualSunriseSunsetEnabled=True, IsPauseWhenFullScreenEnabled=False,
                                IsApplicationWhitelistEnabled=False, IsConfigurationSmoothingEnabled=False,
                                IsGammaPollingEnabled=False, ManualSunriseTime='07:00:00', ManualSunsetTime='19:00:00')
                settings['DayConfiguration'] = settings['NightConfiguration'] = {'Temperature': 4500, 'Brightness': .8}
                settings['ToggleHotKey'] = 'Ctrl+Alt+Shift+F12'
                save(settings)
                client.call('screen', action='managed', enabled=True)
                adjusted = await_state(lambda v: v['screen']['gamma_valid'] and v['screen']['brightness'] == .8
                                       and abs(v['status']['display_brightness_factor']-.8) < .001)
                assert not adjusted['screen']['hotkey_error'], adjusted['screen']['hotkey_error']
                evidence['native_global_hotkey_registration'] = True
                ramps = inspect()
                originals = {d['display']: d for d in neutral}
                for d in ramps:
                    before = originals[d['display']]
                    assert d['read_ok']
                    assert abs(d['ramps_rgb'][0][192]/before['ramps_rgb'][0][192]-.8) < .002
                    assert d['ramps_rgb'][2][192] < d['ramps_rgb'][0][192]
                assert adjusted['status']['display_brightness_valid']
                assert abs(adjusted['status']['display_brightness_factor']-.8) < .001
                evidence['real_gamma_temperature_brightness_readback'] = True
                evidence['rgb_follows_applied_factor_once'] = True
                durations = [1, 5, 15, 30, 60, 180, 360, 720, 1440]
                for target in ('lighting', 'screen'):
                    other = 'screen' if target == 'lighting' else 'lighting'
                    for minutes in durations:
                        result = client.call('screen', action='pause', target=target, mode='duration', minutes=minutes)
                        pause = result[target+'_pause']
                        assert pause['kind'] == 'duration' and pause['until']-pause['started'] == minutes*60000
                        assert result[target+'_disabled'] and not result[other+'_disabled']
                    for mode in ('sunrise', 'forever'):
                        result = client.call('screen', action='pause', target=target, mode=mode)
                        assert result[target+'_pause']['kind'] == mode
                    if target == 'lighting':
                        paused = await_state(lambda v: v['status']['output_paused'] and all(c == [0, 0, 0] for row in v['colors'] for c in row))
                        assert paused['screen']['gamma_valid'] and abs(paused['screen']['brightness']-.8) < .001
                    else:
                        paused = await_state(lambda v: v['screen']['gamma_valid'] and v['screen']['brightness'] == 1)
                        assert not paused['status']['output_paused']
                    client.call('screen', action='pause', target=target, mode='enable')
                evidence['all_pause_choices_independent'] = True
                client.call('screen', action='managed', enabled=False)
                restored = inspect()
                assert {d['display']: d['ramps_rgb'] for d in restored} == {d['display']: d['ramps_rgb'] for d in neutral}
                evidence['exact_native_gamma_baseline_restored'] = True
                stale = client.call('snapshot')['screen']['revision']-1
                try:
                    client.call('screen', action='save', revision=stale, settings=settings)
                except ValueError as error:
                    assert 'reload' in str(error)
                else:
                    raise AssertionError('Stale screen draft accepted')
                evidence['stale_screen_edit_rejected'] = True
            finally:
                try:
                    client.call('screen', action='pause', target='lighting', mode='enable')
                    client.call('screen', action='pause', target='screen', mode='enable')
                    save(original['settings'])
                    client.call('screen', action='managed', enabled=original['managed'])
                    rgb = client.call('snapshot')
                    client.call('save', revision=rgb['revision'], settings=baseline['settings'], layout=baseline['layout'])
                    result = client.call('snapshot')
                    assert result['layout'] == baseline['layout'] and result['settings'] == baseline['settings']
                    assert result['screen']['settings'] == original['settings']
                    evidence['original_settings_and_topology_restored'] = True
                finally:
                    native.FindCloseChangeNotification(notification)
                    native.CloseHandle(process)
        assert hashlib.sha256(source.read_bytes()).hexdigest() == source_hash
        evidence['standalone_source_preserved'] = True
        a.record.write_text(json.dumps(evidence, indent=2), encoding='utf-8')
        print(json.dumps(evidence))


if __name__ == '__main__':
    main()
