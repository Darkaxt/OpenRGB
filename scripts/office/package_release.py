"""Package a verified native build with current support scripts and exact provenance.

SPDX-License-Identifier: GPL-2.0-or-later
"""
import argparse
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--sha256', required=True)
    parser.add_argument('--detectors', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
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
        if not (name.startswith('scripts/office/') or name in (
            'office-govee-specification.md', '.github/workflows/office-windows.yml')):
            raise RuntimeError(f'Native source changed after compilation: {name}')
    members = {name: data for name, data in members.items() if not name.startswith('office/')}
    for name in git('ls-files', 'scripts/office').splitlines():
        members['office/' + Path(name).name] = (root / name).read_bytes()
    detectors = json.loads(args.detectors.read_text(encoding='utf-8-sig'))
    if [name for name, enabled in detectors.items() if enabled] != ['Govee']:
        raise ValueError('Expected verified Govee-only runtime detector inventory')
    members['office/detectors.json'] = json.dumps(detectors, indent=2).encode()
    members['office-govee-specification.md'] = (root / 'office-govee-specification.md').read_bytes()
    build.update(source=source, nativeSource=native_source, compiledArtifactSha256=actual,
                 verificationRun=41729321503)
    members['office-build.json'] = json.dumps(build, indent=2).encode()
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
