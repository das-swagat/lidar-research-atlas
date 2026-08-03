from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
def records(kind):
    return [yaml.safe_load(p.read_text()) for p in (ROOT/'catalog'/kind).glob('*.yml')]
def test_unique_ids():
    all_items=records('datasets')+records('methods')
    ids=[(x['resource_type'],x['id']) for x in all_items]
    assert len(ids)==len(set(ids))
def test_no_atlas_hosting():
    assert all(x['download_guide']['atlas_hosts_files'] is False for x in records('datasets'))
def test_sources_are_http():
    for x in records('datasets')+records('methods'):
        for url in x['authoritative_sources'].values(): assert url.startswith(('http://','https://'))
def test_adjacent_resources_are_labeled():
    for x in records('datasets'):
        if any(k in x['name'].lower() for k in ('scannet','matterport','sensaturban')):
            assert x['scope']['adjacent_non_lidar'] is True or 'ScanNet++' in x['name']
