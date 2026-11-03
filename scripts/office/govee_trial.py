"""Headless OpenRGB Govee trial. No desktop input or wallpaper capture.

SPDX-License-Identifier: GPL-2.0-or-later
"""
import argparse
import json
import re
import time
from pathlib import Path


def detector_inventory(source):
    names = set()
    for path in (source / 'Controllers').rglob('*.cpp'):
        text = path.read_text(encoding='utf-8-sig', errors='replace')
        names.update(re.findall(r'REGISTER_[A-Z_]*DETECTOR[A-Z_]*\s*\(\s*"([^"\n]+)"', text))
    if 'Govee' not in names or len(names) < 500:
        raise RuntimeError('Incomplete detector inventory')
    return {name: name == 'Govee' for name in sorted(names)}


def prepare(args):
    detectors = json.loads(args.detectors.read_text(encoding='utf-8-sig'))
    if [name for name, value in detectors.items() if value] != ['Govee']:
        raise RuntimeError('Expected a Govee-only detector inventory')
    args.config.mkdir(parents=True, exist_ok=True)
    target = args.config / 'OpenRGB.json'
    settings = {
        'Detectors': {'detectors': detectors},
        'GoveeDevices': {'devices': [{'ip': args.strip_ip}, {'ip': args.bars_ip}]},
        'LogManager': {'log_console': False, 'log_file': True, 'file_count_limit': 5},
    }
    with target.open('x', encoding='utf-8') as file:
        json.dump(settings, file, indent=2)
    print(json.dumps({'prepared': str(target), 'enabled_detectors': ['Govee']}))


def devices(client):
    found = {}
    for device in client.devices:
        sku = next((sku for sku in ('H6609', 'H8048') if sku in device.name), None)
        if sku is None or sku in found or len(device.leds) != 20:
            raise RuntimeError(f'Unexpected device: {device.name}, LEDs={len(device.leds)}')
        found[sku] = device
    if set(found) != {'H6609', 'H8048'}:
        raise RuntimeError(f'Expected both models, found {list(found)}')
    return found


def control(args):
    from openrgb import OpenRGBClient
    from openrgb.utils import RGBColor
    client = OpenRGBClient(args.host, args.port, name='Office Govee Trial', protocol_version=3)
    try:
        found = devices(client)
        if args.action == 'inventory':
            print(json.dumps([{'model': sku, 'leds': len(d.leds), 'zones': [z.name for z in d.zones],
                               'led_names': [led.name for led in d.leds]} for sku, d in found.items()], indent=2))
            return
        for device in found.values():
            device.set_mode('Direct')
        if args.action == 'solid':
            colours = {'H6609': RGBColor(255, 0, 0), 'H8048': RGBColor(0, 0, 255)}
            for sku, device in found.items():
                device.set_colors([colours[sku]] * 20)
        elif args.action == 'pattern':
            red, green, blue, yellow = RGBColor(255, 0, 0), RGBColor(0, 255, 0), RGBColor(0, 0, 255), RGBColor(255, 255, 0)
            found['H6609'].set_colors([red]*3 + [green]*7 + [blue]*4 + [yellow]*6)
            found['H8048'].set_colors([red]*10 + [blue]*10)
        elif args.action == 'stream':
            import threading
            # Frame pacing is the requested output rate, not a completion timeout.
            pacer = threading.Event()
            began = time.monotonic()
            for frame in range(args.frames):
                value = frame % 256
                for sku, device in found.items():
                    colour = RGBColor(value, 255-value, 32) if sku == 'H6609' else RGBColor(32, value, 255-value)
                    device.set_colors([colour]*20, fast=True)
                pacer.wait(max(0, began + (frame+1)/args.fps - time.monotonic()))
            print(json.dumps({'frames_per_device': args.frames, 'elapsed_seconds': time.monotonic()-began, 'hardware_acknowledged': False}))
        for device in found.values():
            device.update()
        print(json.dumps({'action': args.action, 'models': list(found), 'sdk_completed': True, 'hardware_acknowledged': False}))
    finally:
        client.disconnect()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=6742)
    sub = parser.add_subparsers(dest='action', required=True)
    inventory = sub.add_parser('detectors')
    inventory.add_argument('--source', type=Path, required=True)
    inventory.add_argument('--output', type=Path, required=True)
    config = sub.add_parser('prepare')
    config.add_argument('--detectors', type=Path, required=True)
    config.add_argument('--config', type=Path, required=True)
    config.add_argument('--strip-ip', required=True)
    config.add_argument('--bars-ip', required=True)
    for name in ('inventory', 'solid', 'pattern'):
        sub.add_parser(name)
    stream = sub.add_parser('stream')
    stream.add_argument('--frames', type=int, default=1800)
    stream.add_argument('--fps', type=int, default=15, choices=range(1, 31))
    args = parser.parse_args()
    if args.action == 'detectors':
        values = detector_inventory(args.source)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(values, indent=2), encoding='utf-8')
        print(json.dumps({'registered_names': len(values), 'output': str(args.output)}))
    elif args.action == 'prepare':
        prepare(args)
    else:
        control(args)


if __name__ == '__main__':
    main()
