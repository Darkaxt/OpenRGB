"""Inventory redundant fork refs; apply only reviewed, unchanged branch identities."""
import argparse
import json
from pathlib import Path
import subprocess

root=Path(__file__).resolve().parents[2]
def git(*args):return subprocess.check_output(['git','--no-lazy-fetch','-C',str(root),*args],text=True).strip()
def heads(remote):return {line.split('\t')[1].removeprefix('refs/heads/'):line.split('\t')[0] for line in git('ls-remote','--heads',remote).splitlines()}
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--inventory',type=Path,required=True)
p.add_argument('--apply',action='store_true')
a=p.parse_args()
if not a.apply:
    origin=heads('origin');upstream=heads('upstream');kept={};remove={}
    default=json.loads(subprocess.check_output(['gh','api','repos/Darkaxt/OpenRGB'],text=True))['default_branch']
    protected={default,'master','codex/govee-office'}
    for name,sha in origin.items():
        if name in protected or name.startswith(('codex/','release','rollback')):kept[name]=dict(sha=sha,reason='active/default/release/rollback ref')
        elif upstream.get(name)==sha:remove[name]=dict(sha=sha,reason='exact duplicate of canonical upstream branch')
        elif subprocess.run(['git','--no-lazy-fetch','-C',str(root),'merge-base','--is-ancestor',sha,'HEAD'],capture_output=True).returncode==0:
            remove[name]=dict(sha=sha,reason='already reachable from maintained office branch')
        else:kept[name]=dict(sha=sha,reason='unique or unverified history preserved')
    result=dict(repository='Darkaxt/OpenRGB',origin=git('remote','get-url','origin'),upstream=git('remote','get-url','upstream'),
                protected=sorted(protected),remove=remove,keep=kept,total=len(origin))
    a.inventory.write_text(json.dumps(result,indent=2))
    print(json.dumps(dict(total=len(origin),remove=len(remove),keep=len(kept),preserved=list(kept))))
else:
    reviewed=json.loads(a.inventory.read_text())
    assert reviewed['repository']=='Darkaxt/OpenRGB' and git('remote','get-url','origin')==reviewed['origin']
    current=heads('origin');upstream=heads('upstream')
    for name,entry in reviewed['remove'].items():
        assert current.get(name)==entry['sha'],f'Branch changed since review: {name}'
        if entry['reason'].startswith('exact duplicate'):assert upstream.get(name)==entry['sha']
        else:assert subprocess.run(['git','--no-lazy-fetch','-C',str(root),'merge-base','--is-ancestor',entry['sha'],'HEAD'],capture_output=True).returncode==0
    if reviewed['remove']:
        subprocess.run(['git','-C',str(root),'push','--atomic','origin',*[':refs/heads/'+name for name in reviewed['remove']]],check=True)
    after=heads('origin')
    assert not set(after)&set(reviewed['remove'])
    assert all(after.get(name)==entry['sha'] for name,entry in reviewed['keep'].items())
    reviewed.update(applied=True,remaining=after)
    a.inventory.write_text(json.dumps(reviewed,indent=2))
    print(json.dumps(dict(removed=len(reviewed['remove']),remaining=len(after),protected_preserved=True)))
