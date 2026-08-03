#!/usr/bin/env python3
from pathlib import Path
import argparse, csv, json, time, urllib.request, urllib.error
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(); p.add_argument('--report',default='link-audit.json'); p.add_argument('--limit',type=int,default=0); args=p.parse_args()
rows=list(csv.DictReader((ROOT/'catalog/source-register.csv').open()))
if args.limit: rows=rows[:args.limit]
results=[]
for row in rows:
    req=urllib.request.Request(row['url'],headers={'User-Agent':'LiDAR-Research-Atlas-Link-Audit/0.1 (+scholarly metadata verification)'},method='HEAD')
    try:
        with urllib.request.urlopen(req,timeout=15) as resp: status=resp.status
    except urllib.error.HTTPError as e: status=e.code
    except Exception as e: status=f'ERROR:{type(e).__name__}'
    results.append({**row,'http_status':status}); print(status,row['url']); time.sleep(.15)
(ROOT/args.report).write_text(json.dumps(results,indent=2)+'\n')
print(f'Wrote {args.report}. HTTP failures require manual review; they do not automatically prove a source is unavailable.')
