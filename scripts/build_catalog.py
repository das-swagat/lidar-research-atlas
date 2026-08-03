#!/usr/bin/env python3
from pathlib import Path
import argparse, csv, html, json, yaml
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
VERSION='0.2.2'
GENERATED='2026-08-03'

def load(kind):
    return [yaml.safe_load(p.read_text(encoding='utf-8')) for p in sorted((ROOT/'catalog'/kind).glob('*.yml'))]
def esc(s): return html.escape(str(s))
def badge(text): return f'<span class="atlas-badge">{esc(text)}</span>'
def write(path,text): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(text.rstrip()+'\n',encoding='utf-8')
def filter_box(target, placeholder):
    return f'<div class="atlas-filter"><input type="search" data-atlas-filter="{target}" placeholder="{esc(placeholder)}" aria-label="{esc(placeholder)}"></div>'

def dataset_page(d):
    scope=d['scope']; access=d['access']; src=d['authoritative_sources']; lic=d['license']; status=d['verification']['status']
    dims=' '.join(badge(x) for x in scope['dimensions']); env=' '.join(badge(x) for x in scope['environments'])
    adjacent='\n!!! warning "Adjacent non-LiDAR resource"\n    This record is included for transferable 3D research, but its primary geometry is not LiDAR-derived.\n' if scope.get('adjacent_non_lidar') else ''
    discovery='''\n!!! warning "Discovery-only record"\n    This entry was expanded from scholarly resource lists and an official project URL. Access, contributor names, publication, and license fields have **not yet completed independent atlas verification**. The provider's current page controls.\n''' if status=='discovery_only' else ''
    steps='\n'.join(f'{i}. {x}' for i,x in enumerate(d['download_guide']['steps'],1))
    tasks='\n'.join(f'- {x}' for x in d['tasks'])
    sources='\n'.join(f'- `{x}`' for x in d.get('discovery_sources',[]))
    sources_block=f'\n## Discovery provenance\n{sources}\n' if sources else ''
    return f'''# {d['name']}

{dims} {env}

**Original contributors:** {d['original_contributors']}  
**First release/publication year:** {d['year']}  
**Verification:** `{status}` — checked {d['verification']['last_checked']}
{adjacent}{discovery}
## Research uses
{tasks}

## Authoritative sources

- [Official dataset/project page]({src['official_page']})
- [Primary publication or project source]({src['primary_publication']})
- [Current terms or license source]({src['terms_or_license']})

## Access and legal status

| Field | Curated status |
|---|---|
| Access class | `{access['class']}` |
| Account required | `{access['account_required']}` |
| Agreement required | `{access['agreement_required']}` |
| Commercial use | `{access['commercial_use']}` |
| Redistribution | `{access['redistribution']}` |
| Automated download | `{access['automated_download']}` |
| Dataset/license label | {lic['name']} |

!!! danger "Do not redistribute from this atlas"
    This project hosts no scans, labels, calibration archives, credentials, signed links, or model weights. The provider's current terms control.

## Lawful access workflow
{steps}

## Citation
{d['citation']['instruction']}

Recommended source: [{d['citation']['recommended_source']}]({d['citation']['recommended_source']})

## Curator note
{d.get('notes') or 'No additional note.'}
{sources_block}'''

def method_page(m):
    src=m['authoritative_sources']; imp=m['implementation']; status=m['verification']['status']; datasets=', '.join(m.get('commonly_evaluated_on') or []) or 'Varies by implementation and paper.'
    discovery='''\n!!! warning "Discovery-expanded record"\n    This method was added from a source collection and has not yet completed independent implementation-license verification. Review the original paper and repository.\n''' if status=='discovery_only' else ''
    sources='\n'.join(f'- `{x}`' for x in m.get('discovery_sources',[]))
    sources_block=f'\n## Discovery provenance\n{sources}\n' if sources else ''
    return f'''# {m['name']}

{badge(m['category'])} {badge(m['representation'])}

**Original authors:** {m['original_authors']}  
**Year:** {m['year']}  
**Verification:** `{status}` — checked {m['verification']['last_checked']}
{discovery}
## Authoritative sources

- [Primary publication]({src['primary_publication']})
- [Implementation/project source]({src['implementation']})

## Implementation relationship

| Field | Curated status |
|---|---|
| Relationship | `{imp['relationship']}` |
| Code license | {imp['license']} |
| Model weights | {imp['weights_terms']} |
| Common evaluation resources | {datasets} |

!!! info "Authorship boundary"
    The method and implementation remain the work of their original authors and maintainers. This page is an independently written index record.

## Citation
{m['citation']['instruction']}

## Curator note
{m.get('notes') or 'Review the original paper and repository for architecture, preprocessing, training, and evaluation details.'}
{sources_block}'''

def ecosystem_page(e):
    repo=f'- [Repository or organization]({e["repository_url"]})\n' if e.get('repository_url') else ''
    sources='\n'.join(f'- `{x}`' for x in e['source_collections'])
    return f'''# {e['name']}

{badge(e['category'])} {badge(e.get('subcategory',e['category']))}

**Verification:** `{e['verification']['status']}` — checked {e['verification']['last_checked']}

{e['summary']}

## Official sources

- [Official page]({e['official_url']})
{repo}
## Legal and attribution note

{e['legal_note']}

The atlas provides an independently written discovery record and does not claim affiliation, endorsement, ownership, or maintenance responsibility.

## Discovery provenance
{sources}
'''

def dataset_table(items):
    rows=['| Resource | Year | Geometry | Environment | Tasks | Access | Status |','|---|---:|---|---|---|---|---|']
    for d in sorted(items,key=lambda x:x['name'].lower()):
        rows.append(f"| [{d['name']}]({d['id']}.md) | {d['year']} | {', '.join(d['scope']['dimensions'])} | {', '.join(d['scope']['environments'][:3])} | {', '.join(d['tasks'][:3])} | `{d['access']['class']}` | `{d['verification']['status']}` |")
    return '\n'.join(rows)
def method_table(items):
    rows=['| Method | Year | Category | Representation | Source relationship | Status |','|---|---:|---|---|---|---|']
    for m in sorted(items,key=lambda x:x['name'].lower()):
        rows.append(f"| [{m['name']}]({m['id']}.md) | {m['year']} | {m['category']} | {m['representation']} | `{m['implementation']['relationship']}` | `{m['verification']['status']}` |")
    return '\n'.join(rows)
def eco_table(items):
    rows=['| Resource | Category | Purpose | Verification |','|---|---|---|---|']
    for e in sorted(items,key=lambda x:(x['category'],x['name'].lower())):
        rows.append(f"| [{e['name']}]({e['id']}.md) | `{e['category']}` | {e['summary']} | `{e['verification']['status']}` |")
    return '\n'.join(rows)

def source_register(ds,ms,eco):
    rows=[]
    for d in ds:
        for role,url in d['authoritative_sources'].items(): rows.append(['dataset',d['id'],d['name'],role,url,d['verification']['last_checked'],d['verification']['status']])
    for m in ms:
        for role,url in m['authoritative_sources'].items(): rows.append(['method',m['id'],m['name'],role,url,m['verification']['last_checked'],m['verification']['status']])
    for e in eco:
        rows.append(['ecosystem_resource',e['id'],e['name'],'official_url',e['official_url'],e['verification']['last_checked'],e['verification']['status']])
        if e.get('repository_url'): rows.append(['ecosystem_resource',e['id'],e['name'],'repository_url',e['repository_url'],e['verification']['last_checked'],e['verification']['status']])
    with (ROOT/'catalog/source-register.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f, lineterminator="\n"); w.writerow(['resource_type','id','name','source_role','url','last_checked','verification_status']); w.writerows(rows)

def main(check=False):
    ds=load('datasets'); ms=load('methods'); eco=load('ecosystem'); ps=load('portals')
    if check:
        expected=len(ds)+len(ms)+len(eco)
        actual=sum(len([p for p in (DOCS/'catalog'/kind).glob('*.md') if p.name!='index.md']) for kind in ('datasets','methods','ecosystem'))
        if expected!=actual: raise SystemExit(f'Generated page mismatch: expected {expected}, found {actual}. Run build_catalog.py')
        print(f'Generated catalog current: {actual} pages'); return
    for d in ds: write(DOCS/'catalog/datasets'/f"{d['id']}.md",dataset_page(d))
    for m in ms: write(DOCS/'catalog/methods'/f"{m['id']}.md",method_page(m))
    for e in eco: write(DOCS/'catalog/ecosystem'/f"{e['id']}.md",ecosystem_page(e))
    dsv=sum(d['verification']['status']=='verified' for d in ds); dsp=sum(d['verification']['status']=='partial' for d in ds); dsd=sum(d['verification']['status']=='discovery_only' for d in ds)
    msv=sum(m['verification']['status']=='verified' for m in ms); msp=sum(m['verification']['status']=='partial' for m in ms); msd=sum(m['verification']['status']=='discovery_only' for m in ms)
    write(DOCS/'catalog/datasets/index.md',f'''# Dataset catalog

<div class="atlas-stat-grid"><div><strong>{len(ds)}</strong><span>dataset records</span></div><div><strong>{dsv}</strong><span>verified</span></div><div><strong>{dsp}</strong><span>partial</span></div><div><strong>{dsd}</strong><span>discovery-only</span></div></div>

The expanded catalog spans indoor and outdoor 2D/3D LiDAR, autonomous driving, robotics, mapping, aerial sensing, natural environments, construction, synthetic data, and heterogeneous sensor research. A discovery-only record is an indexed lead, not a completed license determination.

{filter_box('dataset-table','Filter datasets by name, task, sensor, environment, year, or status…')}

<div id="dataset-table" class="atlas-table-wrap" markdown="1">

{dataset_table(ds)}

</div>''')
    write(DOCS/'catalog/methods/index.md',f'''# Method catalog

<div class="atlas-stat-grid"><div><strong>{len(ms)}</strong><span>method records</span></div><div><strong>{msv}</strong><span>verified</span></div><div><strong>{msp}</strong><span>partial</span></div><div><strong>{msd}</strong><span>discovery-only</span></div></div>

Methods cover point representations, semantic and moving-object segmentation, 3D detection, ground segmentation, registration, SLAM, odometry, place recognition, self-supervised learning, and sensor calibration.

{filter_box('method-table','Filter methods by name, category, representation, year, or status…')}

<div id="method-table" class="atlas-table-wrap" markdown="1">

{method_table(ms)}

</div>''')
    counts={c:sum(e['category']==c for e in eco) for c in sorted({e['category'] for e in eco})}
    cards=''.join(f'<div><strong>{n}</strong><span>{c.replace("-"," ")}</span></div>' for c,n in counts.items())
    write(DOCS/'catalog/ecosystem/index.md',f'''# LiDAR ecosystem catalog

<div class="atlas-stat-grid atlas-stat-grid--ecosystem">{cards}</div>

This section expands beyond datasets and papers to the surrounding LiDAR ecosystem: sensor manufacturers, point-cloud libraries, autonomous-system frameworks, simulators, visualization and annotation tools, and related curated lists. These records are discovery aids. Product status, software licenses, export controls, and commercial terms must be verified at the linked source.

{filter_box('ecosystem-table','Filter manufacturers, libraries, frameworks, simulators, tools, or lists…')}

<div id="ecosystem-table" class="atlas-table-wrap" markdown="1">

{eco_table(eco)}

</div>''')
    rows=[
        '# Research portals',
        '',
        '<div id="portal-table" class="atlas-table-wrap" markdown="1">',
        '',
        '| Portal | Purpose | Legal note |',
        '|---|---|---|',
    ]
    for p in ps:
        rows.append(f"| [{p['name']}]({p['url']}) | {p['purpose']} | {p['legal_note']} |")
    rows.extend(['', '</div>'])
    write(DOCS/'catalog/portals/index.md','\n'.join(rows))
    dump={'version':VERSION,'generated':GENERATED,'datasets':ds,'methods':ms,'ecosystem':eco,'portals':ps}
    (ROOT/'docs/assets/catalog.json').write_text(json.dumps(dump,indent=2)+'\n',encoding='utf-8')
    source_register(ds,ms,eco)
    print(f'Generated {len(ds)} dataset pages, {len(ms)} method pages, {len(eco)} ecosystem pages, and catalog.json')
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); a=ap.parse_args(); main(a.check)
