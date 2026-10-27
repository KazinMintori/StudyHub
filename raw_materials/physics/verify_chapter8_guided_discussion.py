"""Verify source-reviewed guided12, discussion26 and bridge1 against canonical text and figures."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
import pymupdf
ROOT=Path(__file__).resolve().parents[2];RAW=ROOT/'raw_materials/physics/translations/chapter-08'
OUT=ROOT/'qa/physics1-remaining/ch08-guided-recomputed';OUT.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n') if p.suffix in ['.md','.svg','.json','.py'] else p.read_bytes()).hexdigest()
names=['parent-09-luyen-tap-huong-dan.md','parent-10-cau-hoi-thao-luan.md','parent-16-bai-tap-cau-noi.md']
texts={n:(RAW/n).read_text(encoding='utf8') for n in names};units={}
for n in names[:2]:
 for c in re.split(r'(?=^### )',texts[n],flags=re.M):
  if m:=re.match(r'### ((?:VP8\.\d+\.\d+|Q8\.\d+)):',c):units[m[1]]=c.strip()
units['bridge-8']=texts[names[2]].strip()
ledger=json.loads((RAW/'parent-guided-discussion-source-unit-ledger.json').read_text(encoding='utf8'))
assert len(units)==len(ledger)==39
for row in ledger:
 c=units[row['id']]
 assert hashlib.sha256(c.encode('utf8')).hexdigest()==row['canonicalUnitSHA256'],row['id']
 assert c.count('<details>')==c.count('</details>')==1 and '<details open' not in c
 assert all(c.count(k)==1 for k in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**'])
 for part in row['requiredParts']:
  prompt,answer=c.split('<details>',1)
  marker=f'#### '+str(dict(a=4,b=5,c=6,d=7,e=8,f=9)[part])+'.' if row['id']=='bridge-8' else f'({part})'
  assert f'({part})' in prompt and marker in answer,(row['id'],part)
bridge=units['bridge-8'];question,solution=bridge.split('<details>',1)
assert re.findall(r'^(\d+)\. ',question,re.M)==list(map(str,range(1,12)))
assert re.findall(r'^#### (\d+)\.',solution,re.M)==list(map(str,range(1,12)))
text='\n\n'.join(texts.values());assert not re.search(r'source-image:|solution-image:|image-gloss:|class="figure-labels"',text)
originals=json.loads((RAW/'parent-guided-discussion-image-assets.json').read_text(encoding='utf8'))
solutions=json.loads((RAW/'parent-guided-discussion-solution-image-manifest.json').read_text(encoding='utf8'))['assets']
assert len(originals)==7 and len(solutions)==1
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for row in originals:
  p=ROOT/row['publicFile'];assert sha(p)==row['sha256']
  px=pdf[row['source_pdf_page_1based']-1].get_pixmap(matrix=pymupdf.Matrix(row['scale'],row['scale']),clip=pymupdf.Rect(row['clip_pdf_points']),alpha=False)
  actual=pymupdf.Pixmap(str(p))
  assert (px.width,px.height,px.samples)==(actual.width,actual.height,actual.samples),row['key']
  assert text.count('(/'+row['publicFile'].removeprefix('docs/')+')')==1,row['key']
for row in solutions:assert sha(ROOT/row['publicFile'])==row['sha256']
reports={}
for label in ['guided','discussion','bridge']:
 p=ROOT/f'raw_materials/physics/reviews/ch08-guided-verifiers/verify-{label}.py'
 subprocess.run([sys.executable,'-I','-X','utf8',str(p)],cwd=ROOT,check=True)
 result=json.loads((OUT/f'numeric-{label}.json').read_text(encoding='utf8'))
 assert result['status'].startswith('passed')
 reports[label]=dict(checks=result.get('checksCount',result.get('checks')),reportSHA256=sha(OUT/f'numeric-{label}.json'))
total=sum(r['checks'] for r in reports.values())
result=dict(status='passed-canonical-guided39-only',sourceUnits=39,canonicalSourcesSHA256={n:sha(RAW/n) for n in names},independentPhysicalGeometryStructureChecks=total,reports=reports,sourceOriginalFrames=7,separateSolutionDiagrams=1,actualBridgeParts=6,actualBridgeGuideItems=11,actualSourceQuestionsAndOptionsReviewed=True,sourceUnitHashesAndAllRequiredAnswerPartsPassed=True,originalPDFPixelArraysPassed=True,scopeLimit='Onlyguided12/discussion26/bridge1. Whole148 theory/wiki/cheatsheet/routing/public release and all-course audit remain separate.')
(OUT/'canonical-result.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS canonical39:',total,'independent physical/geometry/structure checks;7unchanged PDF frames,1SVG,all6bridgeparts/11guides.')
