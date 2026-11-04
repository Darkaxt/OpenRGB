"""Verify and install an OpenRGB trial archive into a new directory.

SPDX-License-Identifier: GPL-2.0-or-later
"""
import argparse
import hashlib
import json
import stat
import zipfile
from pathlib import Path, PurePosixPath


def digest(data):
    return hashlib.sha256(data).hexdigest().upper()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--sha256', required=True)
    parser.add_argument('--source-commit', required=True)
    parser.add_argument('--version', default='1.1-office.0.1.0')
    parser.add_argument('--destination', type=Path, required=True)
    args = parser.parse_args()
    archive_hash = digest(args.archive.read_bytes())
    if archive_hash != args.sha256.upper():
        raise RuntimeError('Archive hash differs from expected download')
    if args.destination.exists():
        raise FileExistsError('Installation must use a new destination')
    files = {}
    with zipfile.ZipFile(args.archive) as archive:
        for info in archive.infolist():
            path = PurePosixPath(info.filename)
            if path.is_absolute() or any(part in ('..', '.') or ':' in part or '\\' in part for part in path.parts):
                raise ValueError('Unsafe archive path')
            if info.is_dir():
                continue
            if stat.S_ISLNK(info.external_attr >> 16) or info.filename.casefold() in files:
                raise ValueError('Duplicate or link archive member')
            files[info.filename.casefold()] = (info.filename, archive.read(info))
    build = json.loads(files['office-build.json'][1].decode('utf-8-sig'))
    if build['source'] != args.source_commit or build['version'] != args.version:
        raise ValueError('Package provenance does not match requested source/version')
    exe = files['openrgb.exe'][1]
    pe = int.from_bytes(exe[0x3C:0x40], 'little')
    if exe[:2] != b'MZ' or exe[pe:pe+4] != b'PE\0\0' or exe[pe+4:pe+6] != b'\x64\x86':
        raise ValueError('Expected Windows x64 executable')
    if 'ambientSource' in build:
        plugin = json.loads(files['plugins/installed-plugin.json'][1])
        if plugin['source'] != build['ambientSource'] or plugin['openrgb'] != build['nativeSource'] or digest(files['plugins/openrgb_ambient.dll'][1]) != plugin['sha256']:
            raise ValueError('Packaged plugin provenance differs from the native build')
        if 'panelSha256' in plugin:
            if digest(files['officecontrol.exe'][1]) != plugin['panelSha256'] or digest(files['qt6network.dll'][1]) != plugin['networkSha256']:
                raise ValueError('Packaged control panel provenance differs from the plugin build')
    args.destination.mkdir(parents=True)
    hashes = {}
    for name, data in files.values():
        target = args.destination.joinpath(*PurePosixPath(name).parts)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as file:
            file.write(data)
        hashes[name] = digest(data)
        if digest(target.read_bytes()) != hashes[name]:
            raise RuntimeError(f'Installed file readback failed: {name}')
    manifest = {'version': build['version'], 'source': build['source'], 'archiveSha256': archive_hash,
                'executableSha256': digest(exe), 'files': hashes}
    if 'nativeSource' in build:
        manifest['nativeSource'] = build['nativeSource']
    if 'ambientSource' in build:
        manifest['ambientSource'] = build['ambientSource']
    (args.destination / 'installed-manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(json.dumps({'installed': str(args.destination), 'verified_members': len(hashes),
                      'version': build['version'], 'source': build['source'], 'executable_sha256': digest(exe)}))


if __name__ == '__main__':
    main()
