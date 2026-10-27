"""Recompute 55 source-reviewed early chapter8 models and verify canonical units/images."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
import pymupdf
ROOT=Path(__file__).resolve().parents[2];RAW=ROOT/'raw_materials/physics/translations/chapter-08'
OUT=ROOT/'qa/physics1-remaining/ch08-early-recomputed';OUT.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n') if p.suffix in ['.md','.svg','.json','.py'] else p.read_bytes()).hexdigest()
source=RAW/'parent-11-bai-tap-001-055.md';text=source.read_text(encoding='utf8')
units={m[1]:c.strip() for c in re.split(r'(?=^### )',text,flags=re.M) if(m:=re.match(r'### (8\.\d+)\b',c))}
assert list(units)==[f'8.{n}' for n in range(1,56)]
ledger=json.loads((RAW/'parent-numbered-early-source-unit-ledger.json').read_text(encoding='utf8'));assert len(ledger)==55
for row in ledger:
 c=units[row['id']]
 assert hashlib.sha256(c.encode('utf8')).hexdigest()==row['canonicalUnitSHA256'],row['id']
 assert c.count('<details>')==c.count('</details>')==1 and '<details open' not in c,row['id']
 assert all(c.count(k)==1 for k in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']),row['id']
 for part in row['requiredParts']:assert f'({part})' in c.split('<details>',1)[0] and f'({part})' in c.split('<details>',1)[1],(row['id'],part)
 assert not re.search(r'^!\[[^\n]*\]\s*$',c,re.M),row['id']
assert not re.search(r'source-image:|solution-image:|image-gloss:|class="figure-labels"',text)
originals=json.loads((RAW/'parent-numbered-early-image-assets.json').read_text(encoding='utf8'))
assert len(originals)==8
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for row in originals:
  p=ROOT/row['publicFile'];assert sha(p)==row['sha256']
  px=pdf[row['source_pdf_page_1based']-1].get_pixmap(matrix=pymupdf.Matrix(row['scale'],row['scale']),clip=pymupdf.Rect(row['clip_pdf_points']),alpha=False)
  actual=pymupdf.Pixmap(str(p))
  assert (px.width,px.height,px.samples)==(actual.width,actual.height,actual.samples),row['key']
  assert text.count('(/'+row['publicFile'].removeprefix('docs/')+')')==1,row['key']
reports={}
for label in ['001-010','011-020','021-030','031-045','046-055']:
 p=ROOT/f'raw_materials/physics/reviews/ch08-early-verifiers/verify-{label}.py'
 subprocess.run([sys.executable,'-I','-X','utf8',str(p)],cwd=ROOT,check=True)
 result=json.loads((OUT/f'numeric-{label}.json').read_text(encoding='utf8'));assert result['status']=='passed'
 reports[label]=dict(checks=result['checksCount'],reportSHA256=sha(OUT/f'numeric-{label}.json'))
total=sum(r['checks'] for r in reports.values())
result=dict(status='passed-canonical-early55-only',sourceUnits=55,canonicalSourceSHA256=sha(source),independentPhysicalChecks=total,reports=reports,sourceOriginalFrames=8,sourceUnitHashesAndAllRequiredAnswerPartsPassed=True,originalPDFPixelArraysPassed=True,scopeLimit='Only early55 numbered units. Guided12/discussion26, whole148 theory/wiki/cheatsheet/routing/public release and all-course audit not certified.')
(OUT/'canonical-result.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS canonical early55:',total,'independent physical checks; eight unchanged PDF frames and all required solution parts.')
