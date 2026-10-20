#!/usr/bin/env python3
"""Bundle source into standalone HTML, preserving no external JS, data or CSS requirements."""
import pathlib,re,json
ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=ROOT/'data'
src=(ROOT/'index.html').read_text()
css=(ROOT/'assets'/'styles.css').read_text().replace("@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');",'')
js=(ROOT/'src'/'engine.mjs').read_text().replace('export const ','const ').replace('export function ','function ')
app=(ROOT/'src'/'app.mjs').read_text()
app=re.sub(r"^import .*?from '\./(?:engine|data)\.mjs';\n",'',app,flags=re.M)
panel=json.loads((DATA/'synthetic_panel.json').read_text())
evidence=json.loads((DATA/'research_evidence.json').read_text())
hypotheses=json.loads((DATA/'hypotheses.json').read_text())
inline='const PANEL='+json.dumps(panel,separators=(',',':'))+';\nconst EVIDENCE='+json.dumps(evidence,separators=(',',':'))+';\nconst HYPOTHESES='+json.dumps(hypotheses,separators=(',',':'))+';\n'
standalone=src.replace('<link rel="stylesheet" href="assets/styles.css">','<style>'+css+'</style>').replace('<script type="module" src="src/app.mjs"></script>','<script type="module">'+js+'\n'+inline+'\n'+app+'</script>')
out=ROOT.parent/'BoundaryLab_Standalone.html';out.write_text(standalone)
# repo source stores data embedded in an importable module for offline deployment
(ROOT/'src'/'data.mjs').write_text('export const PANEL='+json.dumps(panel,separators=(',',':'))+';\nexport const EVIDENCE='+json.dumps(evidence,separators=(',',':'))+';\nexport const HYPOTHESES='+json.dumps(hypotheses,separators=(',',':'))+';\n')
print('Standalone',out.stat().st_size,'bytes; embedded data module',(ROOT/'src'/'data.mjs').stat().st_size)
