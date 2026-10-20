#!/usr/bin/env python3
"""Generate an explicitly fictional synthetic panel for UI testing and scenario exploration.
This contains no real interview respondents and makes no empirical distribution claims.
"""
import json, random, pathlib, hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
SEED=20261020
CATEGORIES=['Groceries','Ready meals','Essentials','Personal care']
SEGMENTS=['Convenience-led','Value-first','Worker-aware','Context-dependent']

def clip(x,a,b): return max(a,min(b,x))

def generate(n=1200,seed=SEED):
    rng=random.Random(seed)
    items=[]
    for i in range(n):
        seg=SEGMENTS[i%len(SEGMENTS)]
        base_fee={'Convenience-led':4.45,'Value-first':2.35,'Worker-aware':3.7,'Context-dependent':3.4}[seg]
        base_eta={'Convenience-led':32,'Value-first':42,'Worker-aware':40,'Context-dependent':34}[seg]
        base_safeguard={'Convenience-led':48,'Value-first':50,'Worker-aware':82,'Context-dependent':62}[seg]
        eta=round(clip(rng.gauss(base_eta,8),12,65))
        maxfee=round(clip(rng.gauss(base_fee,.88),.5,8.0),2)
        threshold=round(clip(rng.gauss(base_safeguard,13),20,98))
        if seg=='Context-dependent': allowed_contexts=[rng.choice(['Home','Work'])]
        else: allowed_contexts=['Home','Work'] if rng.random()>.28 else [rng.choice(['Home','Work'])]
        category_allowed={}
        for cat in CATEGORIES:
            baseline={'Groceries':.75,'Ready meals':.69,'Essentials':.83,'Personal care':.52}[cat]
            adjustment={'Convenience-led':.12,'Value-first':-.05,'Worker-aware':.02,'Context-dependent':-.07}[seg]
            category_allowed[cat]=rng.random()<clip(baseline+adjustment,.15,.95)
        if not any(category_allowed.values()):category_allowed['Essentials']=True
        items.append(dict(
            id=f'SYN-{i+1:04d}', segment=seg,
            context_allow=allowed_contexts, category_allow=category_allowed,
            maximum_fee_gbp=maxfee, maximum_eta_minutes=eta,
            minimum_courier_safeguard=threshold,
            minimum_reliability_pct=round(clip(rng.gauss(91 if seg=='Context-dependent' else 87,7),65,99)),
            convenience_need=round(rng.uniform(.15,.96),3),
            value_sensitivity=round(rng.uniform(.35,1.3)*(1.35 if seg=='Value-first' else 1),3),
            ethical_salience=round(rng.uniform(.25,1)*(1.55 if seg=='Worker-aware' else 1),3),
            carbon_sensitivity=round(rng.uniform(.1,1),3)
        ))
    return items

def main():
    items=generate()
    out=ROOT/'data'/'synthetic_panel.json'
    out.write_text(json.dumps(items,indent=2)+'\n',encoding='utf-8')
    digest=hashlib.sha256(out.read_bytes()).hexdigest()
    print(f'{len(items)} fictional profiles; sha256: {digest}')
if __name__=='__main__':main()
