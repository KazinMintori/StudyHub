"""Independent mutual/self inductance and dampedRLC checks for presentation repairs."""
from pathlib import Path
import math,json,hashlib
import numpy as np
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch30-theory-layout-repair-20261028';OUT.mkdir(exist_ok=True)
mu=4*math.pi*1e-7;records=[]
def near(name,a,b,tol=1e-10,scale=None):
 a,b=np.asarray(a,dtype=float),np.asarray(b,dtype=float)
 ref=max(np.max(np.abs(a)),np.max(np.abs(b)),scale or 0,1e-300)
 assert np.allclose(a/ref,b/ref,rtol=tol,atol=tol),(name,a,b)
 records.append({'name':name,'actual':a.tolist(),'expected':b.tolist(),'physicalScale':float(ref)})
N1,N2,A,length=1000,10,.001,.5
M=mu*A*N1*N2/length
near('30.1 geometric product',A*N1*N2,10)
near('30.1 mu/length',mu/length,8*math.pi*1e-7)
near('30.1 original mutualinductance',M,2.5132741228718347e-5)
near('30.1 grouped substitution',(8*math.pi)*10e-7,M)
for current in[.2,1,6,-3]:
 B=mu*N1/length*current;Phi=B*A
 near('30.1 original Faradayflux definition '+str(current),N2*Phi,M*current)
near('30.2 currentafter3us',2e6*3e-6,6)
near('30.2 flux rounded25uHmodel',25e-6*6/1000,1.5e-7)
near('30.2 reverse inducedEMF rounded25uHmodel',-25e-6*2e6,-50)
N,r,A=200,.1,5e-4;L=mu*N*N*A/(2*math.pi*r)
near('30.3 mu/circumference',mu/(2*math.pi*r),2e-6)
near('30.3 N squaredarea',N*N*A,20)
near('30.3 toroidinductance',L,40e-6)
near('30.4 linearcurrent derivative',6/3e-6,2e6)
near('30.4 inducedEMF',L*2e6,80)
for label,L,start,end,t,target in[('i',2e-6,1,2,.5,4e-6),('ii',4e-6,3,0,2,-6e-6),('iii',1e-6,4,4,1,0),('iv',1e-6,0,4,.25,16e-6)]:
 near('30selfcheck terminal voltage '+label,L*(end-start)/t,target,scale=1e-6)
for R,L,C in[(.4,1,.5),(.2,.3,.8),(2,3,.2)]:
 alpha=R/(2*L);omega=math.sqrt(1/(L*C)-alpha*alpha);A=.7;phase=.4
 q0=A*math.cos(phase);i0=-alpha*q0-omega*A*math.sin(phase)
 ts=np.linspace(0,8,65)
 numerical=solve_ivp(lambda t,s:[s[1],-R/L*s[1]-s[0]/(L*C)],[0,8],[q0,i0],t_eval=ts,rtol=1e-11,atol=1e-13)
 analytic=A*np.exp(-alpha*ts)*np.cos(omega*ts+phase)
 near('30.28 independent secondorder ODE '+str((R,L,C)),numerical.y[0],analytic,tol=1e-9)
 near('30.29 frequencyidentity '+str((R,L,C)),alpha*alpha+omega*omega,1/(L*C))
 for t in[0,.3,2.7,6.2]:
  a=math.exp(-alpha*t);theta=omega*t+phase
  q=A*a*math.cos(theta);qd=-A*a*(alpha*math.cos(theta)+omega*math.sin(theta))
  qdd=A*a*((alpha*alpha-omega*omega)*math.cos(theta)+2*alpha*omega*math.sin(theta))
  near('30derivative equation '+str((R,L,C,t)),qdd,-2*alpha*qd-(alpha*alpha+omega*omega)*q)
  near('30.27 original equation residual '+str((R,L,C,t)),L*qdd+R*qd+q/C,0,scale=abs(L*qdd)+abs(R*qd)+abs(q/C))
near('30damping selfcheck thresholds',[4*3e-6/6e-6,4*6e-6/3e-6,4*3e-6/3e-6],[2,8,4])
assert [4>=4*L/C for L,C in[(3e-6,6e-6),(6e-6,3e-6),(3e-6,3e-6)]]==[True,False,True]
records.append({'name':'30nonoscillating threshold classifications','passed':True})
paths=['raw_materials/physics/translations/chapter-30/'+n for n in['01-ho-cam.md','02-tu-cam.md','06-mach-rlc.md']]
result={'status':'passed-scoped-ch30-inductance-and-ODE-models','checks':len(records),'records':records,
 'sourceSHA256':{p:hashlib.sha256((ROOT/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()for p in paths},
 'scopeLimit':'Onlythechangedcalculations andassociated physicalmodels. Fullsource/figure/exercise/cheatsheet/Wiki andactualviewport acceptance remainseparate.'}
(OUT/'numeric-checks.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(records),'independent inductance/ODE/threshold checks.')
