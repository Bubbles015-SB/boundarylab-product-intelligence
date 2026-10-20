#!/usr/bin/env python3
"""Reproduce synthetic profiles and verify no sensitive respondent records entered the project."""
import json, pathlib, sys, hashlib
from make_panel import generate
ROOT=pathlib.Path(__file__).resolve().parents[1]
D=ROOT/'data'/'synthetic_panel.json'
P=json.loads(D.read_text())
assert P==generate(), 'Synthetic panel differs from deterministic code-generated dataset'
assert len({x['id'] for x in P})==len(P),'Nonunique synthetic IDs'
assert all(x['id'].startswith('SYN-') for x in P)
assert all(set(x['context_allow']).issubset({'Home','Work'}) for x in P)
assert all(set(x['category_allow'])=={'Groceries','Ready meals','Essentials','Personal care'} for x in P)
assert all(0<=x['minimum_courier_safeguard']<=100 for x in P)
assert all(0<=x['minimum_reliability_pct']<=100 for x in P)
assert all(0<=x['maximum_fee_gbp']<=20 for x in P)
assert all(0<=x['maximum_eta_minutes']<=180 for x in P)
assert not any(k in str(P[0]).lower() for k in ('email','phone','interview_quote','transcript','respondent_name'))
e=json.loads((ROOT/'data'/'research_evidence.json').read_text());h=json.loads((ROOT/'data'/'hypotheses.json').read_text())
assert len(e['claims'])==6 and len(h)==6
assert set(x['evidence'] for x in h).issubset(set(x['id'] for x in e['claims']))
print(f'Dataset audit passed: {len(P)} synthetic records; sha256 {hashlib.sha256(D.read_bytes()).hexdigest()[:16]}...')
