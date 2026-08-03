#!/usr/bin/env python3
from pathlib import Path
import csv, json, yaml
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'exports'; OUT.mkdir(exist_ok=True)
VERSION='0.2.1'; GENERATED='2026-08-03'
def load(kind): return [yaml.safe_load(p.read_text()) for p in sorted((ROOT/'catalog'/kind).glob('*.yml'))]
ds=load('datasets'); ms=load('methods'); eco=load('ecosystem')
with (OUT/'datasets.csv').open('w',newline='',encoding='utf-8') as f:
    fields=['id','name','year','dimensions','environments','sensors','platforms','tasks','original_contributors','official_page','primary_publication','terms_or_license','access_class','account_required','agreement_required','commercial_use','redistribution','license_name','verification_status','last_checked','discovery_sources','adjacent_non_lidar','notes']
    w=csv.DictWriter(f,fieldnames=fields,lineterminator="\n"); w.writeheader()
    for d in ds: w.writerow({'id':d['id'],'name':d['name'],'year':d['year'],'dimensions':' | '.join(d['scope']['dimensions']),'environments':' | '.join(d['scope']['environments']),'sensors':' | '.join(d['scope']['sensors']),'platforms':' | '.join(d['scope'].get('platforms',[])),'tasks':' | '.join(d['tasks']),'original_contributors':d['original_contributors'],**d['authoritative_sources'],'access_class':d['access']['class'],'account_required':d['access']['account_required'],'agreement_required':d['access']['agreement_required'],'commercial_use':d['access']['commercial_use'],'redistribution':d['access']['redistribution'],'license_name':d['license']['name'],'verification_status':d['verification']['status'],'last_checked':d['verification']['last_checked'],'discovery_sources':' | '.join(d.get('discovery_sources',[])),'adjacent_non_lidar':d['scope'].get('adjacent_non_lidar',False),'notes':d.get('notes','')})
with (OUT/'methods.csv').open('w',newline='',encoding='utf-8') as f:
    fields=['id','name','year','category','representation','original_authors','primary_publication','implementation','implementation_relationship','code_license','weights_terms','commonly_evaluated_on','verification_status','last_checked','discovery_sources','notes']
    w=csv.DictWriter(f,fieldnames=fields,lineterminator="\n"); w.writeheader()
    for m in ms: w.writerow({'id':m['id'],'name':m['name'],'year':m['year'],'category':m['category'],'representation':m['representation'],'original_authors':m['original_authors'],'primary_publication':m['authoritative_sources']['primary_publication'],'implementation':m['authoritative_sources']['implementation'],'implementation_relationship':m['implementation']['relationship'],'code_license':m['implementation']['license'],'weights_terms':m['implementation']['weights_terms'],'commonly_evaluated_on':' | '.join(m.get('commonly_evaluated_on',[])),'verification_status':m['verification']['status'],'last_checked':m['verification']['last_checked'],'discovery_sources':' | '.join(m.get('discovery_sources',[])),'notes':m.get('notes','')})
with (OUT/'ecosystem.csv').open('w',newline='',encoding='utf-8') as f:
    fields=['id','name','category','subcategory','official_url','repository_url','summary','source_collections','legal_note','verification_status','last_checked']
    w=csv.DictWriter(f,fieldnames=fields,lineterminator="\n"); w.writeheader()
    for e in eco: w.writerow({'id':e['id'],'name':e['name'],'category':e['category'],'subcategory':e.get('subcategory',''),'official_url':e['official_url'],'repository_url':e.get('repository_url',''),'summary':e['summary'],'source_collections':' | '.join(e['source_collections']),'legal_note':e['legal_note'],'verification_status':e['verification']['status'],'last_checked':e['verification']['last_checked']})
(OUT/'catalog.json').write_text(json.dumps({'version':VERSION,'generated':GENERATED,'datasets':ds,'methods':ms,'ecosystem':eco},indent=2)+'\n')
print(f'Exported {len(ds)} datasets, {len(ms)} methods, and {len(eco)} ecosystem resources')
