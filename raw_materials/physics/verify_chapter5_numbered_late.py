"""Recompute all accepted numbered problems5.60–5.118 from canonical inputs.

This verifies the named59units only. It does not mark the chapter ready or
certify the whole course, browser rendering or a deployment.
"""
from pathlib import Path
import hashlib,json,re,subprocess,sys
import pymupdf

ROOT=Path(__file__).resolve().parents[2]
RAW=ROOT/'raw_materials/physics/translations/chapter-05'
MODULES=ROOT/'raw_materials/physics/reviews/ch05-late-verifiers'
OUT=ROOT/'qa/physics1-remaining/ch05-late-recomputed';OUT.mkdir(parents=True,exist_ok=True)
def sha(path):
 data=path.read_bytes()
 if path.suffix in ['.md','.svg','.mjs','.py']:data=data.replace(b'\r\n',b'\n')
 return hashlib.sha256(data).hexdigest()

reports=[]
for label in ['060-068-078','069-077','079-085','086-093','094-103','104-109','110-113','114-118']:
 command=[sys.executable,'-I','-X','utf8',str(MODULES/f'verify-{label}.py')]
 if label in ['104-109','110-113','114-118']:command=[sys.executable,'-I','-X','utf8',str(MODULES/'verify-104-118.py'),label]
 result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,encoding='utf8')
 if result.returncode:raise RuntimeError(f'{label} failed: '+result.stdout+result.stderr)
 r=json.loads((OUT/f'independent-{label}-review.json').read_text(encoding='utf8'));assert r['status']=='passed-numeric-and-structure-scope'
 reports.append(r)

source=RAW/'parent-12-bai-tap-060-118.md';text=source.read_text(encoding='utf8')
ids=[f'5.{n}' for n in range(60,119)]
assert re.findall(r'^### (5\.\d+)\b',text,re.M)==ids
assert text.count('<details>')==text.count('</details>')==59
assert not re.search(r'<details\s+open\b|source-image:|solution-image:|reviewed-image-gloss:',text)
assert text.count('## Đọc hiểu khoa học:')==1
assert not re.search(r'\b(?:Khoan đã|À không|Nhầm rồi|Thử lại nào)\b',text,re.I)
ledger=json.loads((RAW/'parent-numbered-late-source-unit-ledger.json').read_text(encoding='utf8'));assert [x['id'] for x in ledger]==ids
hashes={}
for report in reports:
 for key,h in report['reviewedUnitsSHA256'].items():assert key not in hashes;hashes[key]=h
assert set(hashes)==set(ids)
for unit in ledger:assert hashes[unit['id']]==unit['canonicalUnitSHA256'],unit['id']

orig=json.loads((RAW/'parent-numbered-late-image-assets.json').read_text(encoding='utf8'))
sols=json.loads((RAW/'parent-numbered-late-solution-image-manifest.json').read_text(encoding='utf8'))['assets']
assert len(orig)==29 and len(sols)==8
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for row in orig:
  path=ROOT/row['publicFile'];assert sha(path)==row['sha256']
  pix=pdf[row['source_pdf_page_1based']-1].get_pixmap(matrix=pymupdf.Matrix(row['scale'],row['scale']),clip=pymupdf.Rect(row['clip_pdf_points']),alpha=False)
  actual=pymupdf.Pixmap(str(path))
  assert (actual.width,actual.height,actual.samples)==(pix.width,pix.height,pix.samples),row['key']
  assert text.count('(/'+row['publicFile'].removeprefix('docs/')+')')>=1
for row in sols:
 path=ROOT/row['publicFile'];assert sha(path)==row['sha256']
 assert text.count('(/'+row['publicFile'].removeprefix('docs/')+')')==1

result={'status':'passed-canonical-late59-only','chapter':5,'numberedRange':[60,118],'units':59,'independentChecks':sum(r['checksCount'] for r in reports),'originalFramesExactPDFPixels':29,'separateSolutionSVGs':8,'actualSVGForceArrows':sum(r.get('actualSVGForceArrows',0) for r in reports),'actualSVGDataPoints':sum(r.get('actualSVGDataPointsChecked',0) for r in reports),'actualSVGFitSamples':sum(r.get('actualSVGFitSamplesChecked',0) for r in reports),'actualSourceCurveSamples':903,'canonicalSourceSHA256':sha(source),'scopeLimit':'Named59units only. Earlier59,whole159gate,actualcanonicalbrowser/publicreleaseandfullPhysics1/2auditremainseparate.'}
(OUT/'canonical-result.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print(json.dumps(result,ensure_ascii=False))
