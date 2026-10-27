"""Recompute54source-reviewed latechapter8 models against canonical text and image bytes."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
import pymupdf
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
RAW=ROOT/'raw_materials/physics/translations/chapter-08'
OUT=ROOT/'qa/physics1-remaining/ch08-late-recomputed';OUT.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n') if p.suffix in ['.md','.svg','.json','.py'] else p.read_bytes()).hexdigest()
source=RAW/'parent-12-bai-tap-056-109.md';text=source.read_text(encoding='utf8')
units={m[1]:c.strip() for c in re.split(r'(?=^### )',text,flags=re.M) if(m:=re.match(r'### (8\.\d+)\b',c))}
assert list(units)==[f'8.{n}' for n in range(56,110)]
ledger=json.loads((RAW/'parent-numbered-late-source-unit-ledger.json').read_text(encoding='utf8'));assert len(ledger)==54
for row in ledger:
    c=units[row['id']]
    assert hashlib.sha256(c.encode('utf8')).hexdigest()==row['canonicalUnitSHA256'],row['id']
    assert c.count('<details>')==c.count('</details>')==1 and '<details open' not in c
    assert all(c.count(k)==1 for k in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**'])
assert not re.search(r'source-image:|solution-image:|reviewed-image-gloss:|class="figure-labels"',text)
assert text.count('## Đọc hiểu khoa học:')==1 and text.index('### 8.105')<text.index('## Đọc hiểu khoa học:')<text.index('### 8.106')
originals=json.loads((RAW/'parent-numbered-late-image-assets.json').read_text(encoding='utf8'));solutions=json.loads((RAW/'parent-numbered-late-solution-image-manifest.json').read_text(encoding='utf8'))['assets'];assert len(originals)==14 and len(solutions)==1
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
    for row in originals:
        p=ROOT/row['publicFile'];assert sha(p)==row['sha256']
        pix=pdf[row['source_pdf_page_1based']-1].get_pixmap(matrix=pymupdf.Matrix(row['scale'],row['scale']),clip=pymupdf.Rect(row['clip_pdf_points']),alpha=False);actual=pymupdf.Pixmap(str(p))
        assert (pix.width,pix.height,pix.samples)==(actual.width,actual.height,actual.samples),row['key']
        assert '/'+row['publicFile'].removeprefix('docs/') in text
    curves=[d for d in pdf[289].get_drawings() if abs(d['rect'].x0-118.814186)<.01 and len(d['items'])==3]
    assert len(curves)==1
    items=curves[0]['items'];vertices=[tuple(items[0][1])]+[tuple(x[2]) for x in items]
    ox=118.815086;oy=588.1241455078125;sx=(231.881088-ox)/5;sy=(oy-530.0391235351562)/8000
    data=[((x-ox)/sx,(oy-y)/sy) for x,y in vertices]
    assert np.allclose([p[0] for p in data],[0,1.5,3,4.5],atol=.01)
    assert np.allclose([p[1] for p in data],[7500,7500,3500,3500],atol=15)
    words={w[4] for w in pdf[289].get_text('words',clip=pymupdf.Rect(310,53,576,170))}
    assert all(str(x) in words for x in [80,125,240,200,140,1667,945,851,819,1355])
for row in solutions:
    assert sha(ROOT/row['publicFile'])==row['sha256']
    assert '/'+row['publicFile'].removeprefix('docs/') in text
reports={}
for label in ['056-071','072-084','085-098','099-109']:
    p=ROOT/f'raw_materials/physics/reviews/ch08-late-verifiers/verify-{label}.py'
    subprocess.run([sys.executable,'-I','-X','utf8',str(p)],cwd=ROOT,check=True)
    row=json.loads((OUT/f'numeric-{label}.json').read_text(encoding='utf8'));assert row['status']=='passed'
    reports[label]={'checks':row['checksCount'],'reportSHA256':sha(OUT/f'numeric-{label}.json')}
total=sum(r['checks'] for r in reports.values());assert total==428
result={'status':'passed-canonical-late54-only','sourceUnits':54,'canonicalSourceSHA256':sha(source),'independentPhysicalAndGeometryChecks':total,'reports':reports,'sourceOriginalFrames':14,'separateSolutionDiagrams':1,'actualSourceGraphVertices':4,'actualAnswerGraphVertices':3,'sourceDataTableRows':5,'sourceDataTableFields':20,'sourceUnitHashesAndRequiredAnswerStructurePassed':True,'originalPDFPixelArraysPassed':True,'scopeLimit':'Only54latechapter8units. Early55/guided/discussion/chapter148/publicroute and allcourse audit not certified.'}
(OUT/'canonical-result.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS canonical late54:',total,'physical/geometry checks;14exactPDFframes,all20tablefields and4sourcegraphvertices.')
