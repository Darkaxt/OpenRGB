"""Package a verified native build with current support scripts and exact provenance.

SPDX-License-Identifier: GPL-2.0-or-later
"""
import argparse
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path
from govee_trial import detector_inventory
from office_devices import DETECTORS


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--sha256', required=True)
    parser.add_argument('--native-receipt', type=Path, required=True)
    parser.add_argument('--plugin-archive', type=Path, required=True)
    parser.add_argument('--plugin-receipt', type=Path, required=True)
    parser.add_argument('--ambient-source', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--version', required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]

    def git(*arguments):
        return subprocess.check_output(['git', '-C', str(root), *arguments], text=True).strip()

    if git('status', '--porcelain'):
        raise RuntimeError('Commit the verified package sources before packaging')
    actual = hashlib.file_digest(args.archive.open('rb'), 'sha256').hexdigest()
    if actual != args.sha256.lower():
        raise ValueError('Compiled artifact hash mismatch')
    with zipfile.ZipFile(args.archive) as archive:
        members = {item.filename: archive.read(item) for item in archive.infolist() if not item.is_dir()}
    build = json.loads(members['office-build.json'].decode('utf-8-sig'))
    native_source = build['source']
    native_receipt = json.loads(args.native_receipt.read_text())
    if native_receipt['source'] != native_source or native_receipt['sha256'] != actual:
        raise RuntimeError('Native CI receipt differs from compiled artifact')
    source = git('rev-parse', 'HEAD')
    changed = git('diff', '--name-only', native_source, source).splitlines()
    for name in changed:
        if not (name.startswith(('scripts/office/','office-validation/')) or name in (
            'office-govee-specification.md', 'office-integration-specification.md', '.github/workflows/office-windows.yml')):
            raise RuntimeError(f'Native source changed after compilation: {name}')
    receipt = json.loads(args.plugin_receipt.read_text())
    plugin_digest = hashlib.sha256(args.plugin_archive.read_bytes()).hexdigest()
    if plugin_digest != receipt['sha256']:
        raise RuntimeError('Plugin archive digest mismatch')
    ambient_commit = subprocess.check_output(['git','-C',str(args.ambient_source),'rev-parse','HEAD'],text=True).strip()
    if ambient_commit != receipt['source'] or subprocess.check_output(['git','-C',str(args.ambient_source),'status','--porcelain'],text=True).strip():
        raise RuntimeError('Ambient source differs from the verified clean build')
    with zipfile.ZipFile(args.plugin_archive) as plugin:
        provenance = json.loads(plugin.read('office-plugin-build.json').decode('utf-8-sig'))
        dll = plugin.read('openrgb_ambient.dll')
        network = plugin.read('Qt6Network.dll')
        offscreen = plugin.read('plugins/platforms/qoffscreen.dll')
    if provenance['openrgb'] != native_source or provenance['source'] != ambient_commit or provenance['qt'] != '6.8.3':
        raise RuntimeError('Plugin/native ABI provenance differs')
    members['plugins/openrgb_ambient.dll'] = dll
    members.pop('OfficeControl.exe', None)
    members['Qt6Network.dll'] = network
    members['platforms/qoffscreen.dll'] = offscreen
    members['LICENSE-EDAmbilight-MIT.txt'] = (args.ambient_source/'LICENSE-EDAmbilight-MIT.txt').read_bytes()
    members['LICENSE-LightBulb-MIT.txt'] = (args.ambient_source/'LICENSE-LightBulb-MIT.txt').read_bytes()
    members['office/lightbulb.ico'] = (args.ambient_source/'assets/office/lightbulb.ico').read_bytes()
    members['office/LIGHTBULB.md'] = (args.ambient_source/'LIGHTBULB.md').read_bytes()
    for name in ('LICENSE-Material-Symbols.txt','LICENSE-Orbitron.txt','LICENSE-Rajdhani.txt'):
        members[name]=(args.ambient_source/'assets/office'/name).read_bytes()
    members['office-font-provenance.json']=(args.ambient_source/'assets/office/provenance.json').read_bytes()
    preview_names = subprocess.check_output(['git','-C',str(args.ambient_source),'ls-files','third_party/ed-preview'],text=True).splitlines()
    for name in preview_names:
        members['preview/'+str(Path(name).relative_to('third_party/ed-preview')).replace('\\','/')] = (args.ambient_source/name).read_bytes()
    plugin_manifest = dict(provenance,sha256=hashlib.sha256(dll).hexdigest().upper(),archiveSha256=plugin_digest,ci=receipt['run'],
                           applicationModel='unified',networkSha256=hashlib.sha256(network).hexdigest().upper(),
                           offscreenSha256=hashlib.sha256(offscreen).hexdigest().upper())
    members['plugins/installed-plugin.json'] = json.dumps(plugin_manifest,indent=2).encode()
    members = {name: data for name, data in members.items() if not name.startswith('office/') or name in ('office/lightbulb.ico','office/LIGHTBULB.md')}
    for name in git('ls-files', 'scripts/office').splitlines():
        members['office/' + Path(name).name] = (root / name).read_bytes()
    members['office/AMBIENCE.md'] = (args.ambient_source/'OFFICE.md').read_bytes()
    members['office/ambient-upstream-README.md'] = (args.ambient_source/'README.md').read_bytes()
    detectors = detector_inventory(root)
    if not DETECTORS <= detectors.keys():
        raise ValueError('Required office detector registration missing')
    detectors = {name:name in DETECTORS for name in detectors}
    members['office/detectors.json'] = json.dumps(detectors, indent=2).encode()
    members['office-govee-specification.md'] = (root / 'office-govee-specification.md').read_bytes()
    members['office-integration-specification.md'] = (root / 'office-integration-specification.md').read_bytes()
    for name in git('ls-files','office-validation').splitlines():
        members[name] = (root/name).read_bytes()
    build.update(version=args.version,source=source, nativeSource=native_source, compiledArtifactSha256=actual,
                 verificationRun=native_receipt['run'],nativeExecutableSha256=hashlib.sha256(members['OpenRGB.exe']).hexdigest().upper(),
                 applicationModel='unified',ambientSource=ambient_commit,ambientArchiveSha256=plugin_digest,
                 ambientVerificationRun=receipt['run'])
    build['lightbulbUpstream']='f74285784be7bc191872c06b1b5e644eb209b98b'
    build['lightbulbIconSha256']=hashlib.sha256(members['office/lightbulb.ico']).hexdigest().upper()
    members['office-build.json'] = json.dumps(build, indent=2).encode()
    # Exact allow-list excludes private state, pairing credentials, captures and
    # temporary analysis. The native artifact and tracked public scripts/docs
    # are the only package inputs.
    if any(name.startswith(('state/','runtime-temp/')) or name.endswith(('.bmp','.png')) for name in members):
        raise RuntimeError('Unexpected runtime state or capture in release inputs')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, 'x', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(members.items()):
            archive.writestr(name, data)
    digest = hashlib.file_digest(args.output.open('rb'), 'sha256').hexdigest()
    args.output.with_suffix('.zip.sha256').write_text(f'{digest}  {args.output.name}\n', encoding='ascii')
    print(json.dumps({'package': str(args.output), 'sha256': digest, 'source': source,
                      'nativeSource': native_source, 'nativeSourceUnchanged': True}))


if __name__ == '__main__':
    main()
