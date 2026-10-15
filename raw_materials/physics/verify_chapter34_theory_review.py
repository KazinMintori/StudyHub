"""Independent chapter34 review: source examples, full exercise inventory and unchanged source pixels."""
from pathlib import Path
import ast,json,math,re,hashlib
import numpy as np
import pymupdf as fitz
from PIL import Image
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter34';q.mkdir(parents=True,exist_ok=True)
raw=root/'raw_materials/physics/translations/chapter-34'
texts={p.name:p.read_text(encoding='utf-8-sig') for p in raw.glob('*.md')}
theory='\n'.join(texts[x] for x in sorted(texts) if x[:2].isdigit() and int(x[:2])<9)
end='\n'.join(texts[x] for x in sorted(texts) if x[:2].isdigit() and 10<=int(x[:2])<18)
ex={};defchecks=[]
def image(f,s):
 if s==f:return None,None
 sp=1/(1/f-1/s);m=-sp/s
 assert math.isclose(1/s+1/sp,1/f,rel_tol=1e-12,abs_tol=1e-12)
 return sp,m
def get(i):
 m=re.search(r'### Ví dụ 34\.'+str(i)+r':([\s\S]*?)(?=\n### Ví dụ 34\.|\Z)',theory)
 assert m,i
 return m[1]
# All inputs below transcribed independently from sourcePDF1137–1162.
R=2/(1/10+1/300);ex['1']={'Rcm':R,'fcm':R/2,'m':-30,'imageHeightMm':-150}
ex['2']={'imageComplete':True,'intensityRatioHalfArea':.5}
sp,m=image(-1.8,75.);ex['3']={'sprimeCm':sp,'m':m,'heightCm':160*m};assert abs(sp+1.7578125)<1e-12
ex['4']={'fcm':10.,'cases':[{'s':s,'sprime':image(10.,s)[0],'m':image(10.,s)[1]} for s in [30.,20.,10.,5.]]}
n1,n2,R,s=1.,1.52,2.,8.;sp=n2/((n2-n1)/R-n1/s);m=-n1*sp/(n2*s)
ex['5']={'sprimeCm':sp,'mFullPrecision':m,'mUsingRounded11point3':-11.3/(1.52*8)}
n1=1.33;sp=n2/((n2-n1)/R-n1/s);ex['6']={'sprimeCm':sp,'m':-n1*sp/(n2*s)}
ex['7']={'sprimeM':-2/1.33,'m':1.}
ex['8']={'doubleConvexFcm':1/(.52*(1/10-1/(-10))),'doubleConcaveFcm':1/(.52*(1/(-10)-1/10))}
ex['9']={'fcm':20,'cases':[{'s':s,'sprime':image(20,s)[0],'m':image(20,s)[1]} for s in [50.,20.,15.,-40.]]}
sp,m=image(-20.,40.);ex['10']={'s':40,'sprime':sp,'m':m}
a,m1=image(8.,12.);b,m2=image(6.,36-a);ex['11']={'sprime1':a,'s2':36-a,'sprime2':b,'m1':m1,'m2':m2,'m':m1*m2,'heightCm':8*m1*m2}
assert (round(a),round(b),round(8*m1*m2))==(24,12,16)
ex['12']={'maxApertureMm':200/2.8,'minApertureMm':200/22,'intensityRatio':(22/2.8)**2,'exposureSeconds':(22/2.8)**2/1000}
ex['13']={'fcm':1/(1/25-1/100),'powerD':4-1}
ex['14']={'ordinaryFcm':-48.,'ordinaryPowerD':-1/.48,'contactFcm':-50.,'contactPowerD':-2.}
# Check distinctive source data survive in the prose, not merely in a verifier.
anchors={
1:['dây tóc','5{,}00','3{,}00','10{,}0'],
2:['bồ hóng'],
3:['Noel','7{,}20','0{,}750','1{,}6'],
4:['30','20','10','5'],
5:['1{,}52','8{,}00','2{,}00'],
6:['1{,}33','8{,}00'],
7:['2{,}00','1{,}33'],
8:['34.35','34.31','1{,}52','10'],
9:['20','50','15','-40'],
10:['20','1','3'],
11:['8{,}0','6{,}0','36{,}0','12{,}0','16'],
12:['200','2{,}8','22'],
13:['100','25'],
14:['50','48','2']
}
for i,words in anchors.items():
 section=get(i)
 for w in words:assert w in section,(i,w)
tags=re.findall(r'\\tag\{34\.(\d+)\}',theory)
assert sorted(map(int,tags))==list(range(1,26)),tags
assert set(re.findall(r'### Ví dụ 34\.(\d+)',theory))=={str(i) for i in range(1,15)}
assert set(re.findall(r'Câu (?:hỏi )?tự kiểm tra 34\.(\d+)',theory))=={str(i) for i in range(1,9)}
ids=re.findall(r'^::: exercise (.+)$',end,re.M)
assert len(ids)==148 and len(set(ids))==148
assert set(re.findall(r'^::: exercise 34\.(\d+)\s*$',end,re.M))=={str(i) for i in range(1,112)}
solutions=re.findall(r'^::: solution Lời giải chi tiết\n([\s\S]*?)^:::',end,re.M)
assert len(solutions)==148
for k,sol in enumerate(solutions):
 assert '**Tóm tắt đề bài:**' in sol and '**Hướng đi:**' in sol,(k,ids[k])
 assert re.search(r'^\- ',sol,re.M),(k,ids[k])
# Explicitdisplacementbaseline is exercise52's40cm, not the25cmnearpoint convention.
assert '40{,}0' in texts['16-bai-tap-nang-cao.md']
eyeR=.4/(1/40+1.4/2.6);se=1.333/((1.4-1.333)/eyeR-1.4/2.6)
fwater=2+abs(se);fair=fwater*(1.62/1.333-1)/.62
assert abs(fair-1.736911424)<1e-8
data={'status':'passed','examples':14,'selfChecks':8,'endSolutions':148,'numberedExercises':111,'guided':12,'discussion':24,'bridge':1,'exampleCalculations':ex,'underwaterCorrection':{'corneaRadiusCm':eyeR,'waterFcm':fwater,'airFcm':fair},'scope':'Numeric checks and structural source anchors. Detailed semantic and visual review recorded separately.'}
(q/'numeric-checks.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
# Unchanged exactsource rectangles; no image masking/reassembly/retouching.
rows=[];pdfpath=root/'raw_materials/physics/source/young-freedman-15.pdf'
assert hashlib.sha256(pdfpath.read_bytes()).hexdigest()=='f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff'
with fitz.open(pdfpath) as pdf:
 for script,scale in [('opening',3),('theory-a',2.5),('theory-b',3),('exercise',3),('supplement',3)]:
  path=root/f'scripts/prepare-physics34-{script}-assets.py'
  tree=ast.parse(path.read_text(encoding='utf-8-sig'))
  node=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='CROPS' for t in n.targets))
  crops=ast.literal_eval(node.value)
  for stem,(page,box) in crops.items():
   actual=root/f'docs/vat-ly-2/bai-giang/img/young-34/{stem}.png'
   pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(scale,scale),clip=fitz.Rect(box),alpha=False)
   im=Image.open(actual).convert('RGB');assert im.tobytes()==pix.samples,stem
   rows.append({'path':actual.relative_to(root).as_posix(),'pdfPage':page,'box':box,'scale':scale,'sha256':hashlib.sha256(actual.read_bytes()).hexdigest()})
assert len(rows)==81 and len(set(x['path'] for x in rows))==81
actual={p.relative_to(root).as_posix() for p in (root/'docs/vat-ly-2/bai-giang/img/young-34').glob('*.png')}
assert actual=={x['path'] for x in rows}
(q/'source-image-checks.json').write_text(json.dumps({'status':'pixel-match-passed-visual-review-separate','sourceSha256':hashlib.sha256(pdfpath.read_bytes()).hexdigest(),'count':len(rows),'images':rows},indent=2),encoding='utf-8')
print('Passed14example calculations,8selfchecks,148solutionstructure,111numberedIDs,25equationtags,81unchangedsourcePNG.')
