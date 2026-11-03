"""Private configuration and SDK checks for the six-device office installation.

No firmware, keymap, onboard-profile or boot-configuration changes.
SPDX-License-Identifier: GPL-2.0-or-later
"""
import argparse
import json
import os
import time
from pathlib import Path

from govee_trial import detector_inventory
from process_metrics import snapshot

DETECTORS = {'Govee', 'Nanoleaf', 'Keychron RGB QMK/ZMK Keyboard',
             'Lenovo Legion 7 Gen 8', 'Logitech HID++ 2.0'}
COUNTS = {'H6609': 20, 'H8048': 20, 'Secretlab': 48, 'Keychron': 109, 'Legion': 109, 'Logitech': 8}


def prepare(args):
    import winreg
    settings = json.loads((args.baseline / 'OpenRGB.json').read_text(encoding='utf-8-sig'))
    detectors = detector_inventory(args.source)
    if not DETECTORS <= detectors.keys():
        raise RuntimeError('Required detector registration missing')
    settings['Detectors']['detectors'] = {key: key in DETECTORS for key in detectors}
    registry_path = rf'Software\WhirlwindFX\SignalRgb\services\Secretlab MAGRGB (Nanoleaf)\{args.secretlab_ip}'
    # Reuse the existing pairing locally. Never print or package its credential.
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path) as key:
        token = winreg.QueryValueEx(key, 'token')[0]
        count = int(winreg.QueryValueEx(key, 'zonesOverride')[0])
    if count != 48 or not token:
        raise RuntimeError('Expected the already-paired 48-section MAGRGB')
    settings['NanoleafDevices'] = {'devices': [{'ip': args.secretlab_ip, 'port': 16021,
                                               'auth_token': token, 'zone_count': count}]}
    args.state.mkdir(parents=True, exist_ok=True)
    with (args.state / 'OpenRGB.json').open('x', encoding='utf-8') as file:
        json.dump(settings, file, indent=2)
    print(json.dumps({'state': str(args.state), 'enabled_detectors': sorted(DETECTORS),
                      'credential': 'reused locally; omitted from output'}))


def identify(device):
    if 'H6609' in device.name: return 'H6609'
    if 'H8048' in device.name: return 'H8048'
    if 'NL72S2' in device.description: return 'Secretlab'
    if 'Q6 HE ISO' in device.name: return 'Keychron'
    if 'Lenovo Legion 7 Gen 8' in device.name: return 'Legion'
    if 'G502 X PLUS' in device.name.upper(): return 'Logitech'
    raise RuntimeError(f'Unexpected controller: {device.name}')


def inventory(client):
    found = {}
    for device in client.devices:
        key = identify(device)
        if key in found or len(device.leds) != COUNTS[key]:
            raise RuntimeError(f'Duplicate or unexpected LED count: {key}, {len(device.leds)}')
        found[key] = device
    if set(found) != set(COUNTS):
        raise RuntimeError(f'Incomplete integration: found {sorted(found)}, expected {sorted(COUNTS)}')
    return found


def control(args):
    from openrgb import OpenRGBClient
    from openrgb.utils import RGBColor
    client = OpenRGBClient('127.0.0.1', 6742, name='Office integration', protocol_version=3)
    try:
        found = inventory(client)
        if args.action == 'inventory':
            print(json.dumps([{'model': key, 'name': device.name, 'leds': len(device.leds),
                               'mode': device.modes[device.active_mode].name,
                               'zones': [{'name': z.name, 'leds': len(z.leds)} for z in device.zones],
                               'led_names': [led.name for led in device.leds]}
                              for key, device in found.items()], indent=2))
            return
        for device in found.values():
            if device.modes[device.active_mode].name != 'Direct':
                device.set_mode('Direct')
        if args.action == 'pattern':
            patterns = {
                'H6609': [(255,0,0)]*3 + [(0,255,0)]*7 + [(0,0,255)]*4 + [(255,255,0)]*6,
                'H8048': [(255,0,0)]*10 + [(0,0,255)]*10,
                'Secretlab': [(0,255,0)]*48,
                'Keychron': [(255,0,0)]*109,
                'Legion': [(0,0,255)]*109,
                'Logitech': [(160,0,255)]*8,
            }
            for key, device in found.items():
                device.set_colors([RGBColor(*rgb) for rgb in patterns[key]])
        elif args.action == 'stream':
            import colorsys
            import threading
            pacer = threading.Event()
            began = time.monotonic()
            native_pid = json.loads((args.state / 'owner.json').read_text(encoding='utf-8-sig'))['pid']
            native_before = snapshot(native_pid)
            sender_before = snapshot(os.getpid())
            for frame in range(args.frames):
                for index, device in enumerate(found.values()):
                    colours = [RGBColor(*(round(value*180) for value in colorsys.hsv_to_rgb(
                        (frame/(args.fps*12) + led/max(1, len(device.leds)-1)*0.15 + index*0.12) % 1, 1, 1)))
                               for led in range(len(device.leds))]
                    device.set_colors(colours, fast=True)
                pacer.wait(max(0, began + (frame+1)/args.fps - time.monotonic()))
            elapsed = time.monotonic()-began
            native_after = snapshot(native_pid)
            sender_after = snapshot(os.getpid())
            if native_before['start_filetime'] != native_after['start_filetime']:
                raise RuntimeError('OpenRGB process identity changed during measurement')
            resources = {}
            for name, before, after in [('OpenRGB', native_before, native_after), ('sender', sender_before, sender_after)]:
                resources[name] = {**after, 'whole_machine_cpu_percent':
                    (after['cpu_seconds']-before['cpu_seconds'])/elapsed/os.cpu_count()*100}
            report = {'frames_per_controller': args.frames, 'fps': args.fps,
                      'elapsed_seconds': elapsed, 'resources': resources}
            if args.output:
                with args.output.open('x', encoding='utf-8') as file:
                    json.dump(report, file, indent=2)
            print(json.dumps(report))
        for device in found.values():
            device.update()
        print(json.dumps({'action': args.action, 'controllers': sorted(found),
                          'sdk_completed': True, 'physical_confirmation_required': True}))
    finally:
        client.disconnect()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    config = sub.add_parser('prepare')
    config.add_argument('--source', type=Path, required=True)
    config.add_argument('--baseline', type=Path, required=True)
    config.add_argument('--state', type=Path, required=True)
    config.add_argument('--secretlab-ip', required=True)
    for name in ('inventory', 'pattern'):
        sub.add_parser(name)
    stream = sub.add_parser('stream')
    stream.add_argument('--frames', type=int, default=1800)
    stream.add_argument('--fps', type=int, default=15, choices=range(1,31))
    stream.add_argument('--state', type=Path, required=True)
    stream.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.action == 'prepare': prepare(args)
    else: control(args)


if __name__ == '__main__':
    main()
