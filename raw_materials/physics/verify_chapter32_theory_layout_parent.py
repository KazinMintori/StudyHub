"""Independent traveling/standingwave checks for chapter32 presentation repairs."""
from pathlib import Path
import math,json,hashlib
import numpy as np
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch32-theory-layout-repair-20261028';OUT.mkdir(exist_ok=True)
mu=4*math.pi*1e-7;c=3e8;eps=1/(mu*c*c);records=[]
def near(name,a,b,tol=1e-10,scale=None):
 a,b=np.asarray(a,dtype=float),np.asarray(b,dtype=float);ref=max(np.max(np.abs(a)),np.max(np.abs(b)),scale or 0,1e-300)
 assert np.allclose(a/ref,b/ref,rtol=tol,atol=tol),(name,a,b)
 records.append({'name':name,'actual':a.tolist(),'expected':b.tolist(),'physicalScale':float(ref)})
near('32laserBamplitude',1.5e6/c,5e-3)
k=2*math.pi/(10.6e-6);omega=c*k
near('32laserwavenumber',k,5.93e5,tol=.001)
near('32laserfrequency',omega,1.78e14,tol=.001)
near('32laser regroupedangularfrequency',(3*5.93)*1e13,1.78e14,tol=.001)
for phase in[0,.3,1.4,2.8,4.7,6.1]:
 E0=17.;B0=E0/c;E=E0*math.cos(phase);B=B0*math.cos(phase)
 near('32electricmagneticenergy equality '+str(phase),.5*eps*E*E,B*B/(2*mu))
 near('32totalenergy substitution '+str(phase),.5*eps*E*E+B*B/(2*mu),eps*E*E)
 near('32Poyntingcrossproduct '+str(phase),np.cross([0,E,0],[0,0,B])/mu,[E0*B0/mu*math.cos(phase)**2,0,0])
 near('32timeharmonicPoyntingidentity '+str(phase),E0*B0/mu*math.cos(phase)**2,E0*B0/(2*mu)*(1+math.cos(2*phase)),scale=E0*B0/mu)
 near('32negativeXlaser direction '+str(phase),np.cross([0,0,E],[0,B,0])/mu,[-E*B/mu,0,0])
near('32average cosineenergy',quad(lambda t:math.cos(t)**2,0,2*math.pi)[0]/(2*math.pi),.5)
near('32.3 actual100Vpmenergyflux',8.85e-12*3e8*100**2,26.55)
near('32radio squaredamplitude',(2*mu*c)*(7.96e-7),6e-4,tol=.001)
near('32radio amplitude',math.sqrt(2*mu*c*7.96e-7),2.45e-2,tol=.001)
near('32solarpanel power',1.4e3*4,5.6e3)
near('32solarpanel force',4.7e-6*4,1.9e-5,tol=.02)
for x in[0,.1,.4,.7,1.1]:
 for t in[0,.17,.6,1.2,2.4]:
  E0,B0=2,3;k,w=1.7,2.3
  cp,cm=math.cos(k*x+w*t),math.cos(k*x-w*t)
  Et=E0*(cp-cm);Bt=-B0*(cp+cm)
  a=math.sin(k*x)*math.sin(w*t);b=math.cos(k*x)*math.cos(w*t)
  near('32standingEfromsuperposition '+str((x,t)),Et,-2*E0*a,scale=E0)
  near('32standingBfromsuperposition '+str((x,t)),Bt,-2*B0*b,scale=B0)
  near('32standingfluxgrouping '+str((x,t)),Et*Bt,4*E0*B0*a*b,scale=E0*B0)
  near('32standingdoubleangleidentity '+str((x,t)),4*a*b,math.sin(2*k*x)*math.sin(2*w*t),scale=1)
for x in[.1,.4,.7]:
 near('32standingaverageflux '+str(x),quad(lambda t:math.sin(2*1.7*x)*math.sin(2*t),0,2*math.pi)[0]/(2*math.pi),0,scale=1)
near('32surfaceelectricboundary',math.cos(.7)-math.cos(-.7),0,scale=1)
paths=['raw_materials/physics/translations/chapter-32/'+n for n in['03-song-hinh-sin.md','04-nang-luong-dong-luong.md','05-song-dung-dien-tu.md']]
result={'status':'passed-scoped-ch32-wavemodels','checks':len(records),'records':records,
 'sourceSHA256':{p:hashlib.sha256((ROOT/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()for p in paths},
 'scopeLimit':'Changedexpressions/models only. Fullchapter source/figures/exercises/cheatsheet/Wiki andactualviewport acceptance areseparate.'}
(OUT/'numeric-checks.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(records),'independentwave/energy/boundary checks.')
