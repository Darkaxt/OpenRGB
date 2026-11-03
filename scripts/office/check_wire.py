"""Exercise the real OpenRGB SDK/controller path against loopback Govee peers.

SPDX-License-Identifier: GPL-2.0-or-later
"""
import argparse
import base64
import json
import queue
import selectors
import socket
import subprocess
import threading
import time
from pathlib import Path

from openrgb import OpenRGBClient
from openrgb.utils import RGBColor
from govee_trial import detector_inventory, devices


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exe', type=Path, required=True)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    args = parser.parse_args()
    args.work.mkdir(parents=True, exist_ok=True)
    config = args.work / 'OpenRGB.json'
    config.write_text(json.dumps({
        'Detectors': {'detectors': detector_inventory(args.source)},
        'GoveeDevices': {'devices': [{'ip': '127.0.0.1'}, {'ip': '127.0.0.2'}]},
        'LogManager': {'log_console': False, 'log_file': True},
    }), encoding='utf-8')
    peers = {'127.0.0.1': 'H6609', '127.0.0.2': 'H8048'}
    packets = {sku: queue.Queue() for sku in peers.values()}
    enables = {sku: 0 for sku in peers.values()}
    selector = selectors.DefaultSelector()
    sockets = []
    for address, port in [('0.0.0.0', 4001), ('127.0.0.1', 4003), ('127.0.0.2', 4003)]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((address, port))
        sockets.append(sock)
        selector.register(sock, selectors.EVENT_READ, None if port == 4001 else peers[address])
    stop = threading.Event()

    def receive():
        while not stop.is_set():
            for key, _ in selector.select():
                data, sender = key.fileobj.recvfrom(65535)
                if stop.is_set():
                    return
                msg = json.loads(data.rstrip(b'\0'))['msg']
                if key.data is None and msg['cmd'] == 'scan':
                    for ip, sku in peers.items():
                        reply = json.dumps({'msg': {'cmd': 'scan', 'data': {'ip': ip, 'sku': sku}}}).encode()
                        key.fileobj.sendto(reply, (sender[0], 4002))
                elif key.data and msg['cmd'] == 'razer':
                    packet = base64.b64decode(msg['data']['pt'])
                    if packet[3] == 0xB1 and packet[4] == 1:
                        enables[key.data] += 1
                    packets[key.data].put((time.monotonic(), packet))

    receiver = threading.Thread(target=receive, daemon=True)
    receiver.start()
    log = (args.work / 'server-output.log').open('w', encoding='utf-8')
    process = subprocess.Popen([str(args.exe), '--config', str(args.work), '--noautoconnect', '--server',
                                '--server-host', '127.0.0.1', '--loglevel', 'info', '-v'],
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                               creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    client = None
    try:
        for line in process.stdout:
            log.write(line)
            log.flush()
            if 'SDK listening host=' in line:
                break
        else:
            raise RuntimeError(f'OpenRGB exited before SDK readiness: {process.wait()}')
        # Drain stdout independently so a filled pipe cannot block device writes.
        def drain():
            for line in process.stdout:
                log.write(line)
                log.flush()
        drainer = threading.Thread(target=drain, daemon=True)
        drainer.start()
        actual = json.loads(config.read_text(encoding='utf-8-sig'))['Detectors']['detectors']
        assert [name for name, enabled in actual.items() if enabled] == ['Govee'], 'Other detectors enabled'
        (args.exe.parent / 'office' / 'detectors.json').write_text(json.dumps(actual, indent=2), encoding='utf-8')
        client = OpenRGBClient(protocol_version=3, name='Office wire acceptance')
        found = devices(client)

        def frame_for(sku, colours, after=0):
            expected = bytes(channel for colour in colours for channel in (colour.red, colour.green, colour.blue))
            while True:
                # Observation of a UDP test peer; expiry reports a missing packet,
                # never retries or changes the tested application's operation.
                arrival, packet = packets[sku].get(timeout=50)
                if arrival < after:
                    continue
                if packet[3] != 0xB0 or packet[6:-1] != expected:
                    continue
                assert packet[0] == 0xBB and int.from_bytes(packet[1:3], 'big') == 62
                assert packet[4:6] == bytes([0, 20])
                checksum = 0
                for value in packet:
                    checksum ^= value
                assert checksum == 0 and len(packet) == 67
                return arrival

        colours = [RGBColor(i*10, 200-i*7, i*5) for i in range(20)]
        first = {}
        for sku, device in found.items():
            device.set_mode('Direct')
            device.set_colors(colours)
            first[sku] = frame_for(sku, colours)
        # The next idle B0 comes from OpenRGB's real 30-second keepalive boundary.
        # It must preserve the last frame and must not repeat the blanking B1.
        gaps = {sku: frame_for(sku, colours, after=first[sku] + 30) - first[sku] for sku in found}
        assert enables == {'H6609': 1, 'H8048': 1}, enables
        print(json.dumps({'models': list(found), 'zones_each': 20, 'packet_length': 67,
                          'idle_frame_preserved': True, 'idle_gap_seconds': gaps, 'stream_enables': enables,
                          'scope': 'real executable and SDK with simulated UDP peers'}))
    finally:
        if client is not None:
            client.disconnect()
        if process.poll() is None:
            process.terminate()  # Explicit teardown of this test-owned process.
        process.wait()
        if 'drainer' in locals():
            drainer.join()
        stop.set()
        sockets[0].sendto(b'{}', ('127.0.0.1', 4001))
        receiver.join()
        selector.close()
        for sock in sockets:
            sock.close()
        log.close()


if __name__ == '__main__':
    main()
