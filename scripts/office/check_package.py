"""Check the complete delivered package and installer rejection before writes."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

EXPECTED = {'Govee','Nanoleaf','Keychron RGB QMK/ZMK Keyboard','Lenovo Legion 7 Gen 8','Logitech HID++ 2.0'}
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--archive',type=Path,required=True)
p.add_argument('--source',required=True)
p.add_argument('--version',required=True)
p.add_argument('--ambient-source',required=True)
p.add_argument('--plugin-receipt',type=Path,required=True)
p.add_argument('--native-receipt',type=Path,required=True)
p.add_argument('--native-archive',type=Path,required=True)
p.add_argument('--work',type=Path,required=True)
a=p.parse_args()
with zipfile.ZipFile(a.archive) as z:
    members={item.filename:z.read(item) for item in z.infolist() if not item.is_dir()}
build=json.loads(members['office-build.json'])
assert build['source']==a.source and build['version']==a.version
native=json.loads(a.native_receipt.read_text())
assert build['nativeSource']==native['source'] and build['verificationRun']==native['run']
assert hashlib.sha256(a.native_archive.read_bytes()).hexdigest()==native['sha256']==build['compiledArtifactSha256']
with zipfile.ZipFile(a.native_archive) as n:
    assert members['OpenRGB.exe']==n.read('OpenRGB.exe')
assert build['ambientSource']==a.ambient_source
assert build['lightbulbUpstream']=='f74285784be7bc191872c06b1b5e644eb209b98b'
assert hashlib.sha256(members['office/lightbulb.ico']).hexdigest().upper()==build['lightbulbIconSha256']
assert 'LICENSE-LightBulb-MIT.txt' in members and 'office/LIGHTBULB.md' in members
assert 'office/AWAKE.md' in members and build['powerToysAwakeReference']=='ba946c9885d189dda9b40e2990c5cbf3b4835bbc'
receipt=json.loads(a.plugin_receipt.read_text())
assert receipt['source']==a.ambient_source and receipt['sha256']==build['ambientArchiveSha256']
assert hashlib.sha256(members['OpenRGB.exe']).hexdigest().upper()==build['nativeExecutableSha256']
plugin=json.loads(members['plugins/installed-plugin.json'])
assert plugin['source']==a.ambient_source and plugin['archiveSha256']==receipt['sha256']
assert hashlib.sha256(members['plugins/openrgb_ambient.dll']).hexdigest().upper()==plugin['sha256']
assert build['applicationModel']==plugin['applicationModel']=='unified' and 'OfficeControl.exe' not in members
assert hashlib.sha256(members['Qt6Network.dll']).hexdigest().upper()==plugin['networkSha256']
assert hashlib.sha256(members['platforms/qoffscreen.dll']).hexdigest().upper()==plugin['offscreenSha256']
detectors=json.loads(members['office/detectors.json'])
assert {name for name,value in detectors.items() if value}==EXPECTED
assert not any(Path(name).name.casefold() in ('openrgb.json','owner.json','office-control.json','office-ambience-status.json') for name in members)
assert not any(name.endswith(('.bmp','.png')) for name in members)
def private_keys(value):
    if isinstance(value,dict):
        assert not {'auth_token','private_key','password','Latitude','Longitude','WhitelistedApplications'} & value.keys()
        for child in value.values(): private_keys(child)
    elif isinstance(value,list):
        for child in value: private_keys(child)
for name,data in members.items():
    if name.endswith('.json'): private_keys(json.loads(data))
assert all(name in members for name in ('office/AMBIENCE.md','office/Start-Office.ps1','office/Stop-Office.ps1','office/Open-Office-Control.ps1','LICENSE','LICENSE-EDAmbilight-MIT.txt'))
assert all(name in members for name in ('LICENSE-Material-Symbols.txt','LICENSE-Orbitron.txt','LICENSE-Rajdhani.txt','office-font-provenance.json'))

# Corrupt only the plugin's expected digest. The installer must reject the
# package before creating the destination or extracting any native executable.
a.work.mkdir(parents=True,exist_ok=False)
for field,message in (('sha256','Packaged plugin provenance differs'),('networkSha256','Packaged runtime provenance differs')):
    corrupt=dict(plugin);corrupt[field]='0'*64
    negative=a.work/f'wrong-{field}.zip'
    with zipfile.ZipFile(negative,'x') as z:
        for name,data in members.items(): z.writestr(name,json.dumps(corrupt).encode() if name=='plugins/installed-plugin.json' else data)
    target=a.work/f'must-not-exist-{field}'
    result=subprocess.run([sys.executable,'-B',str(Path(__file__).with_name('install_package.py')),
        '--archive',str(negative),'--sha256',hashlib.sha256(negative.read_bytes()).hexdigest(),
        '--source-commit',a.source,'--version',a.version,'--destination',str(target)],capture_output=True,text=True)
    assert result.returncode!=0 and message in result.stderr and not target.exists(),result.stderr
print(json.dumps({'package_members':len(members),'native_and_plugin_hashes_verified':True,
    'five_detectors_six_devices':True,'private_state_excluded':True,'corrupt_plugin_and_runtime_rejected_before_write':True,'single_application_package':True}))
