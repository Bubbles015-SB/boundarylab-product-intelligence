import json,sys,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from make_panel import generate

def test_panel_is_reproducible():
    actual=json.loads((ROOT/'data'/'synthetic_panel.json').read_text())
    assert actual==generate()

def test_no_original_participants_or_quotes():
    data=json.loads((ROOT/'data'/'synthetic_panel.json').read_text())
    assert len(data)==1200
    assert all(row['id'].startswith('SYN-') for row in data)
    assert all('name' not in row and 'email' not in row and 'transcript' not in row for row in data)

def test_evidence_has_explicit_limits():
    evidence=json.loads((ROOT/'data'/'research_evidence.json').read_text())
    assert 'NOT' in evidence['provenance']
    assert all(r['unsupported'] for r in evidence['claims'])

def test_hypotheses_link_back_to_claims():
    ev=json.loads((ROOT/'data'/'research_evidence.json').read_text())
    hy=json.loads((ROOT/'data'/'hypotheses.json').read_text())
    ids={e['id'] for e in ev['claims']}
    assert all(h['evidence'] in ids for h in hy)
    assert all('untested' in h['status'].lower() for h in hy)
