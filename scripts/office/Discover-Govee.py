"""Read Govee discovery/status for explicitly selected addresses only.

SPDX-License-Identifier: GPL-2.0-or-later
"""
import argparse
import json
import socket
import time
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--strip-ip', required=True)
parser.add_argument('--bars-ip', required=True)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--interface-ip')
args = parser.parse_args()
expected = {args.strip_ip: 'H6609', args.bars_ip: 'H8048'}
received = {}
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(('0.0.0.0', 4002))
    if args.interface_ip:
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(args.interface_ip))
    sock.sendto(json.dumps({'msg': {'cmd': 'scan', 'data': {'account_topic': 'reserve'}}}).encode(), ('239.255.255.250', 4001))
    began = time.monotonic()
    # Discovery observation only; no retry or lighting-state changes on expiry.
    while len(received) < len(expected):
        remaining = 5 - (time.monotonic() - began)
        if remaining <= 0:
            break
        sock.settimeout(remaining)
        try:
            raw, sender = sock.recvfrom(4096)
        except socket.timeout:
            break
        if sender[0] not in expected:
            continue
        message = json.loads(raw.rstrip(b'\0'))['msg']
        if message['cmd'] == 'scan' and message['data'].get('ip') == sender[0]:
            data = message['data']
            if data.get('sku') != expected[sender[0]]:
                raise RuntimeError(f'Unexpected model at {sender[0]}')
            received[sender[0]] = data
if len(received) != len(expected):
    raise RuntimeError(f'Discovery incomplete: {list(received)}')
args.output.parent.mkdir(parents=True, exist_ok=True)
with args.output.open('x', encoding='utf-8') as output:
    json.dump(received, output, indent=2)
print(json.dumps({'verified_models': [item['sku'] for item in received.values()], 'observation_seconds': time.monotonic()-began}))
