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
        panel = plugin.read('OfficeControl.exe')
        network = plugin.read('Qt6Network.dll')
        offscreen = plugin.read('plugins/platforms/qoffscreen.dll')
    if provenance['openrgb'] != native_source or provenance['source'] != ambient_commit or provenance['qt'] != '6.8.3':
        raise RuntimeError('Plugin/native ABI provenance differs')
    members['plugins/openrgb_ambient.dll'] = dll
    members['OfficeControl.exe'] = panel
    members['Qt6Network.dll'] = network
    members['platforms/qoffscreen.dll'] = offscreen
    members['LICENSE-EDAmbilight-MIT.txt'] = (args.ambient_source/'LICENSE-EDAmbilight-MIT.txt').read_bytes()
    preview_names = subprocess.check_output(['git','-C',str(args.ambient_source),'ls-files','third_party/ed-preview'],text=True).splitlines()
    for name in preview_names:
        members['preview/'+str(Path(name).relative_to('third_party/ed-preview')).replace('\\','/')] = (args.ambient_source/name).read_bytes()
    plugin_manifest = dict(provenance,sha256=hashlib.sha256(dll).hexdigest().upper(),archiveSha256=plugin_digest,ci=receipt['run'],
                           panelSha256=hashlib.sha256(panel).hexdigest().upper(),networkSha256=hashlib.sha256(network).hexdigest().upper(),
                           offscreenSha256=hashlib.sha256(offscreen).hexdigest().upper())
    members['plugins/installed-plugin.json'] = json.dumps(plugin_manifest,indent=2).encode()
    members = {name: data for name, data in members.items() if not name.startswith('office/')}
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
                 verificationRun=41752570205,ambientSource=ambient_commit,ambientArchiveSha256=plugin_digest,
                 ambientVerificationRun=receipt['run'])
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
