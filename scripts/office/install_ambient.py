"""Install the verified ambient DLL beside a matching native OpenRGB package."""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--archive', type=Path, required=True)
p.add_argument('--receipt', type=Path, required=True)
p.add_argument('--destination', type=Path, required=True)
a = p.parse_args()
receipt = json.loads(a.receipt.read_text(encoding='utf-8'))
if hashlib.sha256(a.archive.read_bytes()).hexdigest() != receipt['sha256']:
    raise RuntimeError('Downloaded plugin archive digest differs')
native = json.loads((a.destination / 'installed-manifest.json').read_text())
with zipfile.ZipFile(a.archive) as z:
    dll = z.read('openrgb_ambient.dll')
    provenance = json.loads(z.read('office-plugin-build.json').decode('utf-8-sig'))
if provenance['source'] != receipt['source'] or provenance['openrgb'] != native['source'] or provenance['qt'] != '6.8.3':
    raise RuntimeError('Plugin/native build provenance differs')
pe = int.from_bytes(dll[0x3c:0x40], 'little')
if dll[:2] != b'MZ' or dll[pe:pe+6] != b'PE\0\0\x64\x86':
    raise RuntimeError('Expected an x64 plugin DLL')
destination = a.destination / 'plugins'
destination.mkdir(exist_ok=False)
target = destination / 'openrgb_ambient.dll'
with target.open('xb') as f:
    f.write(dll)
digest = hashlib.sha256(dll).hexdigest().upper()
if hashlib.sha256(target.read_bytes()).hexdigest().upper() != digest:
    raise RuntimeError('Installed plugin readback differs')
record = dict(provenance, sha256=digest, archiveSha256=receipt['sha256'], ci=receipt['run'])
(destination / 'installed-plugin.json').write_text(json.dumps(record, indent=2))
print(json.dumps({'plugin': str(target), **record}))
