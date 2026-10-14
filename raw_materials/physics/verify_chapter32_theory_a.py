"""Independent SI computations, vector Maxwell identities, and unchanged figure pixels."""
from pathlib import Path
import math,json,ast,hashlib
import numpy as np
import pymupdf as fitz
from PIL import Image
root=Path(__file__).resolve().parents[2];out=root/'qa/physics/chapter32'
c=3e8;mu0=4*math.pi*1e-7;eps0=1/(mu0*c*c)
exact_c=1/math.sqrt(8.8541878128e-12*mu0)
assert math.isclose(exact_c,299792458,rel_tol=1e-8)
rounded_c=1/math.sqrt(8.854e-12*1.257e-6)
assert math.isclose(rounded_c,2.998e8,rel_tol=.0003)
ex={}
lam=10.6e-6;E0=1.5e6;B0=E0/c;k=2*math.pi/lam;w=c*k
assert math.isclose(B0,.005,rel_tol=1e-12)
assert math.isclose(k,5.93e5,rel_tol=.001)
assert math.isclose(w,1.78e14,rel_tol=.001)
assert np.array_equal(np.cross([0,0,1],[0,1,0]),[-1,0,0])
ex['32.1']={'wavelengthM':lam,'Emax':E0,'Bmax':B0,'k':k,'omega':w,'direction':'-x','electricAxis':'z','magneticAxis':'y'}
frequency=5.09e14;v=c/math.sqrt(5.84);frequency_f=90e6;vf=c/math.sqrt(10*1000)
assert math.isclose(v/frequency,244e-9,rel_tol=.002)
assert math.isclose(vf/frequency_f,.0333,rel_tol=.002)
ex['32.2']={'diamond':{'frequencyHz':frequency,'vacuumWavelengthM':c/frequency,'speed':v,'wavelengthM':v/frequency},'ferrite':{'frequencyHz':frequency_f,'vacuumWavelengthM':c/frequency_f,'speed':vf,'wavelengthM':vf/frequency_f}}
# Evaluate both curls as vectors to detect component-sign mistakes.
X,T=np.meshgrid(np.linspace(0,2*math.pi,47),np.linspace(0,2*math.pi,43))
direction=np.array([1.,0.,0.]);maxwell=[]
for sign,eaxis,baxis in [(1,np.array([0,1,0]),np.array([0,0,1])),(-1,np.array([0,1,0]),np.array([0,0,-1])),(-1,np.array([0,0,1]),np.array([0,1,0]))]:
 phase=X-sign*T;s=np.sin(phase)[...,None]
 # Use k=1,w=c,E0=1,B0=1/c and dimensional derivatives.
 dEdx=-s*eaxis;dBdx=-s*baxis/c
 dEdt=sign*c*s*eaxis;dBdt=sign*s*baxis
 curlE=np.cross(direction,dEdx);curlB=np.cross(direction,dBdx)
 f_res=float(np.max(np.abs(curlE+dBdt)))
 a_res=float(np.max(np.abs(curlB-mu0*eps0*dEdt)))
 assert f_res<1e-12 and a_res<1e-20
 assert np.array_equal(np.cross(eaxis,baxis),[sign,0,0])
 assert np.allclose(dEdx[...,0],0) and np.allclose(dBdx[...,0],0)
 maxwell.append({'direction':sign,'faradayResidual':f_res,'ampereResidual':a_res,'gaussDivergenceZero':True})
# Three source direction questions are checked with independent cross products.
for E,B,vdir in [([1,0,0],[0,1,0],[0,0,1]),([0,0,-1],[-1,0,0],[0,1,0]),([0,0,1],[0,1,0],[-1,0,0])]:
 assert np.array_equal(np.cross(E,B),vdir)
assert math.isclose(1/math.sqrt(1.8),.745,rel_tol=.001)
rows=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for script,scale in [('scripts/prepare-physics32-theory-a-assets.py',2.5),('scripts/prepare-physics32-theory-b-assets.py',3),('scripts/prepare-physics32-exercise-assets.py',3)]:
  tree=ast.parse((root/script).read_text(encoding='utf-8-sig'))
  crops=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='CROPS' for t in n.targets))
  for stem,(p,box) in crops.items():
   image=root/f'docs/vat-ly-2/bai-giang/img/young-32/{stem}.png'
   pix=pdf[p-1].get_pixmap(matrix=fitz.Matrix(scale,scale),clip=fitz.Rect(box),alpha=False)
   with Image.open(image) as im:
    assert im.size==(pix.width,pix.height),stem
    assert im.convert('RGB').tobytes()==pix.samples,stem
   rows.append({'file':image.relative_to(root).as_posix(),'pdfPage':p,'clipPoints':box,'scale':scale,'decodedPixelsMatch':True,'sha256':hashlib.sha256(image.read_bytes()).hexdigest()})
assert len(rows)==37
(out/'source-image-checks.json').write_text(json.dumps({'status':'passed','originalImages':37,'images':rows},indent=2),encoding='utf-8')
(out/'theory-a-numeric-checks.json').write_text(json.dumps({'status':'passed','examples':ex,'maxwell':maxwell,'selfchecks':3,'speedFromRoundedConstants':rounded_c,'waterSpeedRatio':1/math.sqrt(1.8)},indent=2),encoding='utf-8')
print('Passed2 theory-A examples,3 selfchecks,3 vector Maxwell cases and37 unchanged source PNGs.')
