"""Exercise the native NL72S2 driver through the SDK and simulated HTTP/UDP peers.

SPDX-License-Identifier: GPL-2.0-or-later
"""
import argparse
import json
import os
import socket
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from check_wire import ReadinessLog
from govee_trial import detector_inventory
from runtime_control import request_shutdown


def main():
    from openrgb import OpenRGBClient
    from openrgb.utils import RGBColor

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exe', type=Path, required=True)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    args = parser.parse_args()
    args.work.mkdir(parents=True, exist_ok=False)
    writes = []

    class API(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass

        def do_GET(self):
            if self.path == '/api/v1/test/effects/select':
                value = '*ExtControl*'
            elif self.path == '/api/v1/test':
                value = dict(name='Secretlab MAGRGB test', serialNo='test', manufacturer='Nanoleaf',
                             model='NL72S2', firmwareVersion='4.0.0',
                             state={'brightness': {'value': 39}}, effects=None, panelLayout=None)
            else:
                self.send_error(404)
                return
            body = json.dumps(value).encode()
            self.send_response(200)
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_PUT(self):
            writes.append(json.loads(self.rfile.read(int(self.headers['Content-Length']))))
            self.send_response(204)
            self.end_headers()

    server = ThreadingHTTPServer(('127.0.0.1', 0), API)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(('127.0.0.1', 60222))
    # Diagnostic receive boundary only: expiry fails the test, never restarts the device.
    udp.settimeout(10)
    detectors = detector_inventory(args.source)
    detectors.update(Govee=False, Nanoleaf=True)
    (args.work / 'OpenRGB.json').write_text(json.dumps({
        'Detectors': {'detectors': detectors},
        'NanoleafDevices': {'devices': [{'ip': '127.0.0.1', 'port': server.server_port,
                                         'auth_token': 'test', 'zone_count': 48}]},
        'LogManager': {'log_console': True, 'log_file': True},
    }), encoding='utf-8')
    log_path = args.work / 'native.log'
    log = log_path.open('wb')
    readiness = ReadinessLog(args.work, marker='Graceful shutdown event ready')
    env = dict(os.environ, TEMP=str(args.work), TMP=str(args.work), OPENRGB_OFFICE_SHUTDOWN='1')
    process = subprocess.Popen([str(args.exe), '--config', str(args.work), '--noautoconnect',
                                '--server', '--server-host', '127.0.0.1', '--loglevel', 'info'],
                               stdout=log, stderr=subprocess.STDOUT, env=env)
    client = None
    try:
        readiness.wait(process)
        client = OpenRGBClient('127.0.0.1', 6742, name='NL72S2 wire check', protocol_version=3)
        assert len(client.devices) == 1, [d.name for d in client.devices]
        device = client.devices[0]
        assert len(device.leds) == 48, len(device.leds)
        colours = [RGBColor(i, 255-i, i*3) for i in range(48)]
        device.set_colors(colours)
        data, _ = udp.recvfrom(2048)
        assert len(data) == 386 and int.from_bytes(data[:2], 'big') == 48
        for i, colour in enumerate(colours):
            item = data[2+i*8:10+i*8]
            assert item == i.to_bytes(2, 'big') + bytes([colour.red, colour.green, colour.blue, 0, 0, 0]), (i, item)
        assert writes == [{'write': {'command': 'display', 'animType': 'extControl', 'extControlVersion': 'v2'}}], writes
        client.disconnect()
        client = None
        request_shutdown(process.pid)
        assert process.wait() == 0, 'Graceful shutdown failed'
        print(json.dumps({'model': 'NL72S2', 'zones': 48, 'null_metadata_supported': True,
                          'packet_bytes': len(data), 'stream_enables': len(writes),
                          'graceful_shutdown': True,
                          'scope': 'native executable and SDK against simulated HTTP/UDP'}))
    finally:
        if client:
            client.disconnect()
        if process.poll() is None:
            process.terminate()
        process.wait()
        readiness.close()
        log.close()
        udp.close()
        server.shutdown()
        thread.join()
        server.server_close()


if __name__ == '__main__':
    main()
