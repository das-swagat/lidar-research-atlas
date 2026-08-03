#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
blocked_ext={'.las','.laz','.pcd','.ply','.bag','.db3','.ckpt','.pth','.pt','.onnx','.7z','.rar'}
blocked_names={'.env','credentials.json','token.json','id_rsa'}
max_bytes=5*1024*1024
errors=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.parts or p.resolve() == Path(__file__).resolve(): continue
    if p.suffix.lower() in blocked_ext or p.name in blocked_names:
        errors.append(f'blocked file: {p.relative_to(ROOT)}')
    if p.stat().st_size > max_bytes and p.suffix.lower() not in {'.png'}:
        errors.append(f'large file requires review: {p.relative_to(ROOT)} ({p.stat().st_size} bytes)')
    if p.suffix.lower() in {'.md','.yml','.yaml','.json','.py','.txt','.csv'}:
        text=p.read_text(errors='ignore').lower()
        for marker in ('-----begin private key-----','x-amz-signature=','aws_secret_access_key'):
            if marker in text: errors.append(f'sensitive marker in {p.relative_to(ROOT)}: {marker}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('Restricted-file and credential scan passed')
