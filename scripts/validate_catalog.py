#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
errors=[]; seen=set(); counts={}
for kind,schema_name in (('datasets','dataset'),('methods','method'),('ecosystem','ecosystem')):
    schema=json.loads((ROOT/'catalog/schemas'/f'{schema_name}.schema.json').read_text())
    validator=Draft202012Validator(schema); counts[kind]=0
    for path in sorted((ROOT/'catalog'/kind).glob('*.yml')):
        counts[kind]+=1; data=yaml.safe_load(path.read_text())
        key=(data.get('resource_type'),data.get('id'))
        if key in seen: errors.append(f'{path}: duplicate id {key}')
        seen.add(key)
        for err in validator.iter_errors(data): errors.append(f"{path}: {'/'.join(map(str,err.path))}: {err.message}")
        text=path.read_text().lower()
        for token in ('password:', 'api_key:', 'access_token:', 'secret_key:'):
            if token in text: errors.append(f'{path}: forbidden credential-like field {token}')
        if kind=='datasets':
            if data.get('download_guide',{}).get('atlas_hosts_files') is not False: errors.append(f'{path}: atlas_hosts_files must be false')
            if not data.get('authoritative_sources',{}).get('terms_or_license'): errors.append(f'{path}: missing terms/license source')
            if data.get('verification',{}).get('status')=='discovery_only' and data.get('access',{}).get('class')!='UNVERIFIED_PROVIDER_CONTROLLED': errors.append(f'{path}: discovery-only dataset must use conservative access class')
if errors: print('\n'.join(errors)); sys.exit(1)
print(f"Catalog valid: {counts['datasets']} datasets, {counts['methods']} methods, {counts['ecosystem']} ecosystem resources")
