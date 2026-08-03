#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
pat=re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
for md in ROOT.rglob('*.md'):
    if any(x in md.parts for x in ('.git','site')): continue
    text=md.read_text(encoding='utf-8',errors='ignore')
    for target in pat.findall(text):
        target=target.strip().split('#',1)[0]
        if not target or target.startswith(('http://','https://','mailto:','#')): continue
        target=target.split(' ',1)[0]
        p=(md.parent/target).resolve()
        if not p.exists(): errors.append(f'{md.relative_to(ROOT)} -> {target}')
if errors:
    print('Broken internal links:\n'+'\n'.join(errors)); sys.exit(1)
print('Internal Markdown link check passed')
