"""Actual source case checks supplement the worker ledgers and visual review."""
from pathlib import Path
import contextlib,io,importlib.util,json,math
import numpy as np
import pymupdf
from scipy.optimize import root as solve_root
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2];Q=ROOT/'qa/physics1-priority'
def load(letter):
 p=ROOT/f'raw_materials/physics/verify_chapter19_exercises_{letter}.py'
 spec=importlib.util.spec_from_file_location('ch19_'+letter,p)
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
c,d,e=[load(letter) for letter in 'cde']
with contextlib.redirect_stdout(io.StringIO()):
 c.main();dr=d.verify_exercises();er=e.verify_problems()
assert len(dr)==33 and len(er)==33 and len(c.results)==37
# Check the actual source artwork, independent of the initial worker prose.
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 paths=[d for d in pdf[654].get_drawings() if d.get('color') and d['color'][0]<.01 and .6<d['color'][1]<.8 and 425<d['rect'].y0<540 and 74<d['rect'].x0<265 and len(d['items'])==7]
 assert len(paths)==1
 curves=[np.array([[point.x,point.y] for point in item[1:]]) for item in paths[0]['items']]
 assert all(c.shape==(4,2) for c in curves)
def point(c,t):
 return (1-t)**3*c[0]+3*(1-t)**2*t*c[1]+3*(1-t)*t*t*c[2]+t**3*c[3]
cross=solve_root(lambda u:point(curves[1],u[0])-point(curves[4],u[1]),[.05,.98])
assert cross.success and all(0<u<1 for u in cross.x),cross
t,u=map(float,cross.x)
def sample(i,a=0,b=1):return np.array([point(curves[i],v) for v in np.linspace(a,b,1001)])
loopI=np.concatenate([sample(1,t,1),sample(2),sample(3),sample(4,0,u)])
loopII=np.concatenate([sample(4,u,1),sample(5),sample(6),sample(0),sample(1,0,t)])
def area(x):return abs(float(.5*np.sum(x[:,0]*np.roll(x[:,1],-1)-np.roll(x[:,0],-1)*x[:,1])))
areaI,areaII=area(loopI),area(loopII)
assert areaI>areaII>0,(areaI,areaII)
assert math.isclose(area(loopI[::2]),areaI,rel_tol=1e-4)
assert math.isclose(area(loopII[::2]),areaII,rel_tol=1e-4)
properties={'Q19.24':dict(source='PDF655 original vector Bezier curve; arrows visually determine signs.',geometricLoopI_pdfPointSquared=areaI,geometricLoopII_pdfPointSquared=areaII,largerLoop='I',workI='positive',workII='negative',netWork='positive',netHeat='into system')}
# Actual bridge: Integrate pressure, compare with its analytic antiderivative.
n=1.8;R=8.314;T=300;a=.554;b=6.38e-5;V1=.002;V2=.004
pressure=lambda V:n*R*T/(V-n*b)-a*n*n/(V*V)
numeric=quad(pressure,V1,V2,epsabs=1e-9)[0]
analytic=n*R*T*math.log((V2-n*b)/(V1-n*b))+a*n*n*(1/V2-1/V1)
assert V1>n*b and math.isclose(numeric,analytic,rel_tol=1e-12)
properties['bridge']=dict(n_mol=n,T_K=T,work_J=analytic,quadrature_J=numeric,idealWork_J=n*R*T*math.log(V2/V1))
# 19.61: Check all nearby integer compression ratios, not just the chosen integer.
energy=101e3*math.pi*.015**2*.3;T1=303.15
choices=[]
for ratio in range(2,12):
 f=ratio**.4;temp=T1*f;work=energy*(f*math.log(ratio)-(f-1)/.4)
 choices.append(dict(ratio=ratio,T_K=temp,W_J=work,permitted=temp<=673.15 and work>=25))
assert [r['ratio'] for r in choices if r['permitted']]==[7]
properties['19.61']=choices
out=dict(status='passed',guidedCases=12,discussionCases=24,numberedCases=66,bridgeCases=1,sourceGeometryAndIndependentChecks=properties,dCases=dr,eCases=er,conceptualLimit='Code supplements actual source reading, not a proof of every prose assertion.')
(Q/'ch19-end-parent-ledger.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(status='passed',numberedCases=66,guidedCases=12,sourceLoopAreaRatio=areaI/areaII,bridgeWork_J=analytic)))
