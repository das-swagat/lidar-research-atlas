#!/usr/bin/env python3
from pathlib import Path
import argparse, html, json, yaml
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'

def load(kind):
    return [yaml.safe_load(p.read_text()) for p in sorted((ROOT/'catalog'/kind).glob('*.yml'))]
def esc(s): return html.escape(str(s))
def badge(text): return f'<span class="atlas-badge">{esc(text)}</span>'
def write(path,text): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(text.rstrip()+'\n')

def dataset_page(d):
    scope=d['scope']; access=d['access']; src=d['authoritative_sources']; lic=d['license']
    dims=' '.join(badge(x) for x in scope['dimensions']); env=' '.join(badge(x) for x in scope['environments'])
    adjacent='\n!!! warning "Adjacent non-LiDAR resource"\n    This record is included for transferable 3D research, but its primary geometry is not LiDAR-derived.\n' if scope.get('adjacent_non_lidar') else ''
    steps='\n'.join(f'{i}. {x}' for i,x in enumerate(d['download_guide']['steps'],1))
    tasks='\n'.join(f'- {x}' for x in d['tasks'])
    return f'''# {d['name']}

{dims} {env}

**Original contributors:** {d['original_contributors']}  
**First release/publication year:** {d['year']}  
**Verification:** `{d['verification']['status']}` — checked {d['verification']['last_checked']}
{adjacent}
## Research uses
{tasks}

## Authoritative sources

- [Official dataset/project page]({src['official_page']})
- [Primary publication]({src['primary_publication']})
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
    This project hosts no scans, labels, calibration archives, credentials, or signed links. The provider's current terms control.

## Lawful access workflow
{steps}

## Citation
{d['citation']['instruction']}

Recommended source: [{d['citation']['recommended_source']}]({d['citation']['recommended_source']})

## Curator note
{d.get('notes') or 'No additional note.'}
'''

def method_page(m):
    src=m['authoritative_sources']; imp=m['implementation']; datasets=', '.join(m.get('commonly_evaluated_on') or []) or 'Varies by implementation and paper.'
    return f'''# {m['name']}

{badge(m['category'])} {badge(m['representation'])}

**Original authors:** {m['original_authors']}  
**Year:** {m['year']}  
**Verification:** `{m['verification']['status']}` — checked {m['verification']['last_checked']}

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
'''

def index_table(items, kind):
    if kind=='datasets':
        rows=['| Resource | Year | Geometry | Environment | Access | Status |','|---|---:|---|---|---|---|']
        for d in sorted(items,key=lambda x:(x['name'].lower())):
            rows.append(f"| [{d['name']}]({d['id']}.md) | {d['year']} | {', '.join(d['scope']['dimensions'])} | {', '.join(d['scope']['environments'][:3])} | `{d['access']['class']}` | `{d['verification']['status']}` |")
    else:
        rows=['| Method | Year | Category | Representation | Source relationship | Status |','|---|---:|---|---|---|---|']
        for m in sorted(items,key=lambda x:x['name'].lower()):
            rows.append(f"| [{m['name']}]({m['id']}.md) | {m['year']} | {m['category']} | {m['representation']} | `{m['implementation']['relationship']}` | `{m['verification']['status']}` |")
    return '\n'.join(rows)

def main(check=False):
    ds=load('datasets'); ms=load('methods'); ps=load('portals')
    if check:
        expected=len(ds)+len(ms)
        actual=len([p for p in (DOCS/'catalog/datasets').glob('*.md') if p.name != 'index.md'])+len([p for p in (DOCS/'catalog/methods').glob('*.md') if p.name != 'index.md'])
        if expected!=actual: raise SystemExit(f'Generated page mismatch: expected {expected}, found {actual}. Run build_catalog.py')
        print(f'Generated catalog current: {actual} pages'); return
    for d in ds: write(DOCS/'catalog/datasets'/f"{d['id']}.md",dataset_page(d))
    for m in ms: write(DOCS/'catalog/methods'/f"{m['id']}.md",method_page(m))
    write(DOCS/'catalog/datasets/index.md',f"# Dataset catalog\n\n{len(ds)} curated starter records. Use filters in the table and verify provider terms before access.\n\n"+index_table(ds,'datasets'))
    write(DOCS/'catalog/methods/index.md',f"# Method catalog\n\n{len(ms)} foundational and current method records. Official, author-maintained, community, and framework implementations are distinguished.\n\n"+index_table(ms,'methods'))
    rows=['# Research portals','', '| Portal | Purpose | Legal note |','|---|---|---|']
    for p in ps: rows.append(f"| [{p['name']}]({p['url']}) | {p['purpose']} | {p['legal_note']} |")
    write(DOCS/'catalog/portals/index.md','\n'.join(rows))
    dump={'version':'0.1.0','generated':'2026-08-03','datasets':ds,'methods':ms,'portals':ps}
    (ROOT/'docs/assets/catalog.json').write_text(json.dumps(dump,indent=2)+'\n')
    print(f'Generated {len(ds)} dataset pages, {len(ms)} method pages, and catalog.json')
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); a=ap.parse_args(); main(a.check)
