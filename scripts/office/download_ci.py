"""Retrieve a completed native CI artifact and verify GitHub's archive digest.

SPDX-License-Identifier: GPL-2.0-or-later
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path


def metadata(path):
    return json.loads(subprocess.check_output(['gh', 'api', path], text=True))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=int, required=True)
    parser.add_argument('--source-commit', required=True)
    parser.add_argument('--artifact', default='OpenRGB-1.1-office.0.2.0-windows-x64')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = 'repos/Darkaxt/OpenRGB/actions'
    run = metadata(f'{root}/runs/{args.run}')
    if run['status'] != 'completed' or run['conclusion'] != 'success' or run['head_sha'] != args.source_commit:
        raise RuntimeError('CI is not a successful completed run of the requested source')
    artifacts = metadata(f'{root}/runs/{args.run}/artifacts')['artifacts']
    selected = [item for item in artifacts if item['name'] == args.artifact and not item['expired']]
    if len(selected) != 1 or not selected[0].get('digest', '').startswith('sha256:'):
        raise RuntimeError('Expected one unexpired artifact with a SHA256 digest')
    artifact = selected[0]
    with args.output.open('xb') as file:
        subprocess.run(['gh', 'api', f"{root}/artifacts/{artifact['id']}/zip"], stdout=file, check=True)
    actual = hashlib.sha256(args.output.read_bytes()).hexdigest()
    if artifact['digest'] != f'sha256:{actual}':
        raise RuntimeError('Downloaded archive does not match the published CI digest')
    receipt = {'run': args.run, 'source': args.source_commit, 'artifact': artifact['name'],
               'artifact_id': artifact['id'], 'sha256': actual, 'archive': str(args.output)}
    args.output.with_suffix('.receipt.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
    print(json.dumps(receipt))


if __name__ == '__main__':
    main()
