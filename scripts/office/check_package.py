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
p.add_argument('--work',type=Path,required=True)
a=p.parse_args()
with zipfile.ZipFile(a.archive) as z:
    members={item.filename:z.read(item) for item in z.infolist() if not item.is_dir()}
build=json.loads(members['office-build.json'])
assert build['source']==a.source and build['version']=='1.1-office.0.2.0'
assert build['nativeSource']=='82f150a276a800c01b6a5aed1de71520b9d138b4'
assert build['ambientSource']=='ec36299f4a6b4dc16ff0138b49820410a4895c2e'
assert hashlib.sha256(members['OpenRGB.exe']).hexdigest()=='31ef7f130009d994c97318a7c13e807a9074bf5583f4b2d966d61701704dcf28'
assert hashlib.sha256(members['plugins/openrgb_ambient.dll']).hexdigest()=='1a5baed1b4cc8d62f77e33ec27db6b4e37c2d0785622677a766f32d08c388c54'
detectors=json.loads(members['office/detectors.json'])
assert {name for name,value in detectors.items() if value}==EXPECTED
assert not any(Path(name).name.casefold() in ('openrgb.json','owner.json','office-ambience-status.json') for name in members)
assert not any(name.endswith(('.bmp','.png')) for name in members)
def private_keys(value):
    if isinstance(value,dict):
        assert not {'auth_token','private_key','password'} & value.keys()
        for child in value.values(): private_keys(child)
    elif isinstance(value,list):
        for child in value: private_keys(child)
for name,data in members.items():
    if name.endswith('.json'): private_keys(json.loads(data))
assert all(name in members for name in ('office/AMBIENCE.md','office/Start-Office.ps1','office/Stop-Office.ps1','LICENSE'))

# Corrupt only the plugin's expected digest. The installer must reject the
# package before creating the destination or extracting any native executable.
a.work.mkdir(parents=True,exist_ok=False)
plugin=json.loads(members['plugins/installed-plugin.json'])
plugin['sha256']='0'*64
members['plugins/installed-plugin.json']=json.dumps(plugin).encode()
negative=a.work/'wrong-plugin.zip'
with zipfile.ZipFile(negative,'x') as z:
    for name,data in members.items(): z.writestr(name,data)
target=a.work/'must-not-exist'
result=subprocess.run([sys.executable,'-B',str(Path(__file__).with_name('install_package.py')),
    '--archive',str(negative),'--sha256',hashlib.sha256(negative.read_bytes()).hexdigest(),
    '--source-commit',a.source,'--version','1.1-office.0.2.0','--destination',str(target)],capture_output=True,text=True)
assert result.returncode!=0 and 'Packaged plugin provenance differs' in result.stderr and not target.exists(),result.stderr
print(json.dumps({'package_members':len(members),'native_and_plugin_hashes_verified':True,
    'five_detectors_six_devices':True,'private_state_excluded':True,'corrupt_plugin_rejected_before_write':True}))
