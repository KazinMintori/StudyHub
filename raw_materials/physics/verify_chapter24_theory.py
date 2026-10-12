"""Private arithmetic and independent integral checks for chapter24 theory."""
from math import pi,sqrt,isclose,log
from pathlib import Path
import json
root=Path(__file__).resolve().parents[2];eps=8.85e-12;checks={}
def check(name,actual,target,tol=.025):
 aa=actual if isinstance(actual,(list,tuple)) else [actual]
 bb=target if isinstance(target,(list,tuple)) else [target]
 for x,y in zip(aa,bb):assert isclose(x,y,rel_tol=tol,abs_tol=1e-30),(name,x,y)
 checks[name]={'actual':actual,'target':target}
def simpson(f,lo,hi,n=10000):
 h=(hi-lo)/n
 return h/3*(f(lo)+f(hi)+sum((4 if i%2 else 2)*f(lo+i*h) for i in range(1,n)))
A=.001/eps
check('example24.1',[A,sqrt(A),A*.001,(A*.001)**(1/3)],[1.1e8,1.06e4,1.1e5,48],.03)
C=eps*2/.005
check('example24.2',[C,C*1e4,1e4/.005],[3.54e-9,35.4e-6,2e6])
check('example24.3',4*pi*eps*.095*.105/.01,110e-12)
check('example24.4-prefactor',2*pi*eps,55.6e-12)
C1,C2,V=6e-6,3e-6,18;Cs=1/(1/C1+1/C2)
check('example24.5-series',[Cs,Cs*V,Cs*V/C1,Cs*V/C2],[2e-6,36e-6,6,12])
check('example24.5-parallel',[C1+C2,C1*V,C2*V],[9e-6,108e-6,54e-6])
Ci=1/(1/12+1/6);Cm=Ci+3+11;Ce=1/(1/Cm+1/9);Q=Ce*9
check('example24.6-network',[Ci,Cm,Ce,Q],[4,18,6,54])
Vm=Q/Cm;Qbranch=Ci*Vm
check('example24.6-all-charges',[3*Vm,11*Vm,Qbranch,Qbranch,Q],[9,33,12,12,54])
check('example24.6-all-voltages',[Vm,Vm,Qbranch/12,Qbranch/6,Q/9],[3,3,1,2,6])
C1,C2,V0=8e-6,4e-6,120;Q0=C1*V0;Vf=Q0/(C1+C2)
check('example24.7',[Q0,.5*C1*V0**2,Vf,C1*Vf,C2*Vf,.5*(C1+C2)*Vf**2],[960e-6,.0576,80,640e-6,320e-6,.0384])
check('example24.8',[sqrt(2/eps),100],[4.75e5,100])
for Q,ra,rb in [(2e-9,.095,.105),(5e-9,.1,.3)]:
 C=4*pi*eps*ra*rb/(rb-ra)
 integral=simpson(lambda r:.5*eps*(Q/(4*pi*eps*r*r))**2*4*pi*r*r,ra,rb)
 check('example24.9-integral-'+str(Q),integral,Q*Q/(2*C),1e-9)
A=.2;d=.01;C0=eps*A/d;Q=C0*3000;K=3;C=K*C0;Qi=Q*(1-1/K)
check('example24.10',[C0,Q,C,K,K*eps,Qi,3000/d,1000/d],[177e-12,.531e-6,531e-12,3,2.655e-11,.354e-6,3e5,1e5])
check('example24.11',[.5*C0*3000**2,.5*C*1000**2,.5*eps*3e5**2,.5*K*eps*1e5**2],[7.97e-4,2.66e-4,.398,.133])
check('polycarbonate-voltage',3e7*1e-5,300)
check('cell-membrane-field',.07/7e-9,1e7)
check('molecular-field-ratio',[1,2/3,1/3],[1,2/3,1/3])
check('example24.12',4*pi*(K*eps)*.095*.105/.01,K*4*pi*eps*.095*.105/.01,1e-12)
check('charge-in-dielectric',simpson(lambda _:K*(2e-9/(4*pi*K*eps*.2**2)),0,4*pi*.2**2),2e-9/eps,1e-9)
out=root/'qa/physics/chapter24';out.mkdir(parents=True,exist_ok=True)
(out/'theory-checks.json').write_text(json.dumps({'status':'passed','groups':len(checks),'checks':checks},ensure_ascii=False,indent=2),encoding='utf8')
print('Passed',len(checks),'chapter24 theory numerical and integral groups.')
