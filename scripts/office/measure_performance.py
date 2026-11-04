"""Observe the installed owner under metadata or preview demand; never edit settings."""
import argparse,hashlib,json,os,statistics,threading,time
from pathlib import Path
import psutil
from office_control import Control

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--preview',action='store_true');p.add_argument('--samples',type=int,default=101)
    a=p.parse_args();config=a.state/'office-ambience.json';before=hashlib.sha256(config.read_bytes()).hexdigest()
    rows=[];version='';process=None
    with Control(a.state) as client:
        info=json.loads((a.state/'office-control.json').read_text(encoding='utf-8-sig'));process=psutil.Process(info['pid'])
        cpu=process.cpu_times();first_cpu=cpu.user+cpu.system;began=time.perf_counter()
        for i in range(a.samples):
            start=time.perf_counter();snapshot=client.call('snapshot',preview=a.preview,preview_generation=version)
            image=snapshot.get('preview_png','')
            if image:version=snapshot.get('preview_generation','')
            rows.append({'at':time.perf_counter()-began,'request_ms':1000*(time.perf_counter()-start),
              'status':snapshot['status'],'preview_bytes':len(image),'preview_generation':snapshot.get('preview_generation'),
              'preview_encodes':snapshot.get('preview_encodes'),'preview_encode_ms':snapshot.get('preview_encode_ms')})
            if i+1<a.samples:threading.Event().wait(.2) # Explicit diagnostic demand: 5 requests/sec; no observed operation is cancelled.
        cpu=process.cpu_times();elapsed=time.perf_counter()-began
    span=rows[-1]['at']-rows[0]['at'];first=rows[0]['status'];last=rows[-1]['status']
    result={'summary':{'preview_requested':a.preview,'pid':process.pid,'exe':process.exe(),'seconds':elapsed,
       'output_fps':(last['output_frames']-first['output_frames'])/span,
       'reported_fps_median':statistics.median(r['status']['output_fps'] for r in rows),
       'input_fps':(last['input_frames']-first['input_frames'])/span,
       'request_ms_median':statistics.median(r['request_ms'] for r in rows),
       'gpu_ms_median':statistics.median(r['status']['gpu_processing_ms'] for r in rows),
       'submit_ms_median':statistics.median(r['status']['native_submit_ms'] for r in rows),
       'cpu_one_core_percent':100*(cpu.user+cpu.system-first_cpu)/elapsed,
       'cpu_total_percent':100*(cpu.user+cpu.system-first_cpu)/elapsed/os.cpu_count(),
       'working_set':process.memory_info().rss,'source_generations':sorted(set(r['status']['source_generation'] for r in rows)),
       'saved_state_unchanged':before==hashlib.sha256(config.read_bytes()).hexdigest()},'samples':rows}
    # The output clock remains active while stable hardware receives no update.
    # These counters are native API submissions, not hardware acknowledgements;
    # independent controller-protocol keepalives are intentionally not included.
    for counter,label in (('changed_input_frames','changed_input_fps'),('skipped_input_frames','skipped_input_fps'),
            ('sampling_passes','sampling_passes_per_second'),('device_submissions','device_updates_per_second'),('led_writes','led_writes_per_second')):
        if counter in first and counter in last:result['summary'][label]=(last[counter]-first[counter])/span
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2));print(json.dumps(result['summary'],indent=2))
if __name__=='__main__':main()
