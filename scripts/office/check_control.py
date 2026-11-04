"""Exercise the complete installed control boundary, retaining mapping rollback.

prepare saves a reversible named-zone/settings edit; after restarting the native
owner, restore proves persistence and restores the original map. No RGB SDK writer.
"""
import argparse
import copy
import json
import struct
import base64
from pathlib import Path
from office_control import Control

def rejected(client,request,fragment):
    try: client.call(**request)
    except ValueError as error:
        assert fragment in str(error),str(error)
    else: raise AssertionError('Invalid edit was accepted')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state',type=Path,required=True)
    p.add_argument('--record',type=Path,required=True)
    p.add_argument('phase',choices=['prepare','restore','observe'])
    a=p.parse_args()
    with Control(a.state) as client:
        snapshot=client.call('snapshot',preview=True)
        assert len(snapshot['layout'])==6 and sum(len(d['regions']) for d in snapshot['layout'])==314
        assert {d['id'] for d in snapshot['layout']}=={'H6609','H8048','Keychron','Legion','Secretlab','Logitech'}
        for device in snapshot['layout']:
            assert len(device['led_names'])==len(device['regions'])
            for l,t,r,b in device['regions']: assert 0<=l<r<=1 and 0<=t<b<=1
        if a.phase=='prepare':
            request=dict(command='save',revision=snapshot['revision'],settings=snapshot['settings'],layout=snapshot['layout'])
            invalid=copy.deepcopy(request);invalid['layout'][0]['regions'][0]=[0,0,2,1]
            rejected(client,invalid,'inside the LG')
            invalid=copy.deepcopy(request);invalid['revision']+=1
            rejected(client,invalid,'another panel')
            invalid=copy.deepcopy(request);invalid['layout'][0]['led_names'][0]='incorrect'
            rejected(client,invalid,'metadata')
            assert client.call('snapshot')['revision']==snapshot['revision']
            candidate=copy.deepcopy(request)
            candidate['settings']['smoothing_ms']+=1
            candidate['layout'][0]['groups'][0]['name']+=' [persistence check]'
            saved=client.call(**candidate)
            assert saved['layout']==candidate['layout'] and saved['settings']==candidate['settings']
            rejected(client,request,'another panel')
            document={'baseline':snapshot,'candidate':candidate,'rejections_verified':True,'saved_revision':saved['revision']}
            a.record.write_text(json.dumps(document,indent=2),encoding='utf-8')
            print(json.dumps({'saved_for_restart':True,'six_devices':True,'invalid_and_stale_rejected':True,'mapping_regions_unchanged':True}))
        elif a.phase=='restore':
            record=json.loads(a.record.read_text());baseline=record['baseline'];candidate=record['candidate']
            assert snapshot['layout']==candidate['layout'] and snapshot['settings']==candidate['settings'],'Restart persistence differs'
            restored=client.call('save',revision=snapshot['revision'],settings=baseline['settings'],layout=baseline['layout'])
            assert restored['layout']==baseline['layout'] and restored['settings']==baseline['settings']
            record['restart_persistence_verified']=True;record['baseline_restored']=True
            record['restored_revision']=restored['revision'];a.record.write_text(json.dumps(record,indent=2),encoding='utf-8')
            print(json.dumps({'restart_persistence_verified':True,'original_map_and_settings_restored':True}))
        else:
            png=base64.b64decode(snapshot['preview_png'])
            assert png[:8]==b'\x89PNG\r\n\x1a\n','No actual native preview yet'
            dimensions=struct.unpack('>II',png[16:24]);assert dimensions[0]<=640 and dimensions[1]<=270
            assert snapshot['status']['has_valid_frame'] and snapshot['status']['output_fps']>10
            assert len(snapshot['colors'])==6 and sum(map(len,snapshot['colors']))==314
            a.record.write_text(json.dumps({'status':snapshot['status'],'preview_size':dimensions,
                'devices':[{'id':d['id'],'leds':len(d['regions'])} for d in snapshot['layout']],
                'actual_preview':True,'actual_output':True},indent=2),encoding='utf-8')
            print(json.dumps({'actual_preview':dimensions,'actual_six_device_output':True,'output_fps':snapshot['status']['output_fps']}))

if __name__=='__main__':main()
