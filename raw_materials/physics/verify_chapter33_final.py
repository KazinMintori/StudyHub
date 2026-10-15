"""Consolidate source coverage, exact figure pixels and reviewed numerical evidence."""
from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
import numpy as np
import pymupdf as fitz
from PIL import Image

root=Path(__file__).resolve().parents[2]
q=root/'qa/physics/chapter33'
raw=root/'raw_materials/physics/translations/chapter-33'
for suffix in ['a','b']:
 run=subprocess.run([sys.executable,'-X','utf8',str(root/f'raw_materials/physics/verify_chapter33_theory_{suffix}.py')],cwd=root,capture_output=True,text=True,encoding='utf-8')
 (q/f'theory-{suffix}-verification.log').write_text(run.stdout+run.stderr,encoding='utf-8')
 assert run.returncode==0,run.stdout+run.stderr
math=json.loads((q/'all-source-math-review.json').read_text(encoding='utf-8-sig'))
assert not math['findings']
assert json.loads((q/'end-content-checks.json').read_text(encoding='utf-8-sig'))['endSolutions']==102
body='\n'.join(p.read_text(encoding='utf-8-sig') for p in sorted(raw.glob('0*.md')) if p.name!='09-tom-tat.md')
assert set(re.findall(r'\\tag\{(33\.\d+)\}',body))=={f'33.{i}' for i in range(1,10)}
for number in range(1,7):assert re.search(r'Ví dụ 33\.'+str(number)+r'\b',body,re.I)
for number in [1,2,3,5,7]:assert re.search(r'Câu hỏi tự kiểm(?: tra)? 33\.'+str(number)+r'\b',body)
assert not re.search(r'Câu hỏi tự kiểm(?: tra)? 33\.[46]\b',body)
# An ideal quarter-wave retarder removes the quadrature of circular input.
phase=np.linspace(0,2*np.pi,1001)
for initial in [np.pi/2,-np.pi/2]:
 for retardance in [np.pi/2,-np.pi/2]:
  ey=np.cos(phase);ez=np.cos(phase+initial+retardance)
  assert min(np.max(np.abs(ey-ez)),np.max(np.abs(ey+ez)))<1e-12
rows=[]
source=root/'raw_materials/physics/source/young-freedman-15.pdf'
expected_hash='f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff'
assert hashlib.sha256(source.read_bytes()).hexdigest()==expected_hash
with fitz.open(source) as pdf:
 for script,var,scale in [('prepare-physics33-theory-a-assets.py','CROPS',2.5),('prepare-physics33-theory-b-assets.py','CROPS',3),('prepare-physics33-exercise-assets.py','CROPS',3),('prepare-physics33-extra-assets.py','regions',3)]:
  tree=ast.parse((root/'scripts'/script).read_text(encoding='utf-8-sig'))
  crops=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==var for t in n.targets))
  for stem,(page,box) in crops.items():
   name=stem if stem.endswith('.png') else stem+'.png'
   p=root/'docs/vat-ly-2/bai-giang/img/young-33'/name
   pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(scale,scale),clip=fitz.Rect(box),alpha=False)
   with Image.open(p) as im:
    assert im.size==(pix.width,pix.height),name
    assert im.convert('RGB').tobytes()==pix.samples,name
   rows.append({'path':p.relative_to(root).as_posix(),'pdfPage':page,'box':box,'scale':scale,'pixelMatch':True,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
assert len(rows)==76
assert {Path(r['path']).name for r in rows}=={p.name for p in (root/'docs/vat-ly-2/bai-giang/img/young-33').glob('*.png')}
(q/'source-image-checks.json').write_text(json.dumps({'status':'passed','sourceHash':expected_hash,'originalPngRegions':76,'images':rows},indent=2),encoding='utf-8')
(q/'numeric-checks.json').write_text(json.dumps({'status':'passed','chapter':33,'examples':6,'sectionSelfChecks':5,'chapterOpeningQuestion':1,'endSolutions':102,'sourceFigureRegions':76,'equationTags':9,'quarterWavePhaseConversion':'passed','numericEvidence':['end-content-checks.json','theory-a-verification.log','theory-b-verification.log'],'mathEvidence':'all-source-math-review.json','sourceImageEvidence':'source-image-checks.json','renderStatus':'pending-final-theory-review'},indent=2),encoding='utf-8')
print('Passed chapter33: Six examples,102 end solutions,nine equations,76 exact source crops and retarder phase conversion.')
