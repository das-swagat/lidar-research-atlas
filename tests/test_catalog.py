from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
def records(kind): return [yaml.safe_load(p.read_text()) for p in (ROOT/'catalog'/kind).glob('*.yml')]
def test_unique_ids():
    all_items=records('datasets')+records('methods')+records('ecosystem')
    ids=[(x['resource_type'],x['id']) for x in all_items]
    assert len(ids)==len(set(ids))
def test_no_atlas_hosting(): assert all(x['download_guide']['atlas_hosts_files'] is False for x in records('datasets'))
def test_sources_are_http():
    for x in records('datasets')+records('methods'):
        for url in x['authoritative_sources'].values(): assert url.startswith(('http://','https://'))
    for x in records('ecosystem'): assert x['official_url'].startswith(('http://','https://'))
def test_adjacent_resources_are_labeled():
    for x in records('datasets'):
        if any(k in x['name'].lower() for k in ('scannet','matterport','sensaturban')): assert x['scope']['adjacent_non_lidar'] is True or 'ScanNet++' in x['name']
def test_discovery_records_are_conservative():
    for x in records('datasets'):
        if x['verification']['status']=='discovery_only':
            assert x['access']['class']=='UNVERIFIED_PROVIDER_CONTROLLED'
            assert x['download_guide']['atlas_mirrors_files'] is False
def test_expanded_scope():
    assert len(records('datasets')) >= 80
    assert len(records('methods')) >= 50
    assert len(records('ecosystem')) >= 60
