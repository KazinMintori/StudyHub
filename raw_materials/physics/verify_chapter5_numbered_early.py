"""Recompute early chapter5 physics and verify canonical text/original-image/diagram bindings."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
import pymupdf

ROOT=Path(__file__).resolve().parents[2]
RAW=ROOT/'raw_materials/physics/translations/chapter-05'
OUTPUT=ROOT/'qa/physics1-remaining/ch05-early-recomputed'
OUTPUT.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=RAW/'parent-11-bai-tap-001-059.md'
text=source.read_text(encoding='utf8')
units={int(m[1]):c.strip() for c in re.split(r'(?=^### )',text,flags=re.M) if (m:=re.match(r'### 5\.(\d+)\b',c))}
ledger=json.loads((RAW/'parent-numbered-early-source-unit-ledger.json').read_text(encoding='utf8'))
assert sorted(units)==list(range(1,60)) and len(ledger)==59
for row in ledger:
    n=int(row['id'].split('.')[1]);unit=units[n]
    assert hashlib.sha256(unit.encode('utf8')).hexdigest()==row['canonicalUnitSHA256'],f'Unreviewed canonical source change at5.{n}'
    assert unit.count('<details>')==unit.count('</details>')==1 and '<details open' not in unit
    assert all(unit.count(k)==1 for k in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**'])
assert not re.search(r'source-image:|solution-image:|reviewed-image-gloss:|class="figure-labels"',text)
originals=json.loads((RAW/'parent-numbered-early-image-assets.json').read_text(encoding='utf8'))
solutions=json.loads((RAW/'parent-numbered-early-solution-image-manifest.json').read_text(encoding='utf8'))['assets']
assert len(originals)==15 and len(solutions)==16
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
    for row in originals:
        p=ROOT/row['publicFile'];assert sha(p)==row['sha256'],row['key']
        pix=pdf[row['source_pdf_page_1based']-1].get_pixmap(matrix=pymupdf.Matrix(row['scale'],row['scale']),clip=pymupdf.Rect(row['clip_pdf_points']),alpha=False)
        actual=pymupdf.Pixmap(str(p))
        assert (pix.width,pix.height,pix.samples)==(actual.width,actual.height,actual.samples),row['key']
for row in solutions:
    assert sha(ROOT/row['publicFile'])==row['sha256'],row['key']
    assert '/'+row['publicFile'].removeprefix('docs/') in text,row['key']
count=sum(len(re.findall(r'\('+re.escape('/'+r['publicFile'].removeprefix('docs/'))+r'\)',text)) for r in originals)
assert count==18
reports={}
for label in ['001-008','009-015','016-023','024-028','029-036','037-041','042-048','049-059']:
    p=ROOT/f'raw_materials/physics/reviews/ch05-early-verifiers/verify-{label}.py'
    subprocess.run([sys.executable,'-I','-X','utf8',str(p)],cwd=ROOT,check=True)
    row=json.loads((OUTPUT/f'numeric-{label}.json').read_text(encoding='utf8'))
    assert row['status']=='passed'
    reports[label]={'checks':row['checksCount'],'reportSHA256':sha(OUTPUT/f'numeric-{label}.json')}
total=sum(r['checks'] for r in reports.values())
assert total==483
result={'status':'passed-canonical-early59-only','sourceUnits':59,'canonicalSourceSHA256':sha(source),'physicalAndNativeSVGGeometryChecks':total,'reports':reports,'sourceOriginalFrames':15,'displayedOriginalImageOccurrences':18,'separateSolutionDiagrams':16,'actualForceArrows':67,'actualAnswerPlotVertices':6,'sourceUnitHashesAndRequiredSolutionStructurePassed':True,'originalSourcePixelsPassed':True,'scopeLimit':'Recomputes the reviewed early59 models and native image geometry. It does not certify all159chapter units, live browser layout, publication, or the whole course.'}
(OUTPUT/'canonical-result.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS canonical early59:',total,'physical/geometry checks;15exactPDFframes;16solutionimages.')
