"""Exercise the complete installed control boundary, retaining mapping rollback.

prepare saves a reversible named-zone/settings edit; after restarting the native
owner, restore proves persistence and restores the original map. No RGB SDK writer.
"""
import argparse
import copy
import json
import struct
import base64
import time
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
    p.add_argument('phase',choices=['prepare','restore','observe','exercise'])
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
        elif a.phase=='exercise':
            baseline=snapshot
            def next_frame(previous):
                while True:
                    value=client.call('snapshot')
                    if value['status']['output_frames']>previous['status']['output_frames']: return value
            def save(settings,layout):
                current=client.call('snapshot')
                return client.call('save',revision=current['revision'],settings=settings,layout=layout)
            evidence={}
            try:
                settings=copy.deepcopy(baseline['settings']);settings.update(enabled=False,smoothing_ms=0,fps=20)
                disabled=next_frame(save(settings,baseline['layout']))
                assert all(c==[0,0,0] for row in disabled['colors'] for c in row)
                evidence['global_disable_verified']=True
                settings['enabled']=True;layout=copy.deepcopy(baseline['layout']);layout[0]['enabled']=False
                partial=next_frame(save(settings,layout))
                assert all(c==[0,0,0] for c in partial['colors'][0])
                assert any(any(c) for row in partial['colors'][1:] for c in row)
                evidence['per_device_enable_verified']=True
                save(settings,baseline['layout'])
                client.call('calibrate');calibrated=next_frame(client.call('snapshot'))
                for d,row in zip(baseline['layout'],calibrated['colors']):
                    for index,(rect,color) in enumerate(zip(d['regions'],row)):
                        l,t,r,b=rect;expected=[int((l+r)*127.5),int((1-(t+b)/2)*255),40 if index%2 else 160]
                        assert all(abs(x-y)<=1 for x,y in zip(expected,color)),(index,expected,color)
                evidence['spatial_calibration_uses_actual_regions']=True
                client.call('identify',device=baseline['layout'][0]['id']);identified=next_frame(client.call('snapshot'))
                assert all(c==[255,255,255] for c in identified['colors'][0])
                assert all(c==[0,0,0] for row in identified['colors'][1:] for c in row)
                client.call('stop_test');normal=next_frame(client.call('snapshot'));assert normal['test_mode']=='none'
                evidence['identify_and_return_verified']=True
                began=time.perf_counter();first=normal['status']['output_frames'];last=normal
                while last['status']['output_frames']-first<20: last=next_frame(last)
                rate=(last['status']['output_frames']-first)/(time.perf_counter()-began)
                assert 15<rate<25,rate
                evidence['requested_20fps_measured']=rate
                generation=last['status']['source_generation'];client.call('recover')
                while True:
                    recovered=client.call('snapshot')
                    if recovered['status']['source_generation']>generation and recovered['status']['input_frames']>0: break
                    if recovered['status']['error'] and recovered['status']['source_generation']>generation:
                        raise AssertionError(recovered['status']['error'])
                evidence['explicit_native_capture_recovery_verified']=True
            finally:
                client.call('stop_test')
                restored=save(baseline['settings'],baseline['layout'])
                assert restored['layout']==baseline['layout'] and restored['settings']==baseline['settings']
            evidence['baseline_restored']=True;a.record.write_text(json.dumps(evidence,indent=2),encoding='utf-8')
            print(json.dumps(evidence))
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
