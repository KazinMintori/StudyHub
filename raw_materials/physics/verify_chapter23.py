"""Private arithmetic, numerical integration and derivative checks for theory23."""
from math import sqrt,log,pi,isclose
from pathlib import Path
import json

root=Path(__file__).resolve().parents[2]
k=9.0e9;e=1.60e-19;m=9.11e-31
checks={}
def check(name,actual,expected,tol=.02):
 aa=actual if isinstance(actual,(list,tuple)) else [actual]
 bb=expected if isinstance(expected,(list,tuple)) else [expected]
 assert len(aa)==len(bb)
 for x,y in zip(aa,bb):assert isclose(x,y,rel_tol=tol,abs_tol=max(abs(y)*tol,1e-25)),(name,x,y)
 checks[name]={'actual':actual,'expected':expected}
def simpson(f,lo,hi,n=2000):
 h=(hi-lo)/n
 return h/3*(f(lo)+f(hi)+sum((4 if i%2 else 2)*f(lo+i*h) for i in range(1,n)))
ra,rb,va=1e-10,2e-10,3e6
Ka=m*va**2/2;Ua=k*2*e*e/ra;Ub=k*2*e*e/rb
check('ex23.1-positive',[Ka,Ua,Ub,sqrt(2*(Ka+Ua-Ub)/m),sqrt(2*(Ka+Ua)/m)],[4.10e-18,4.61e-18,2.30e-18,3.8e6,4.4e6])
Etot=Ka-Ua;turn=-k*2*e*e/Etot
check('ex23.1-electron',[Etot,turn,sqrt(2*(Ka-Ua+Ub)/m)],[-.51e-18,9e-10,2e6],.025)
checks['escape-question']={'minimumSpeed':sqrt(2*Ua/m)}
charge=[-e,e,e];position=[0,1,2]
energy=sum(k*charge[i]*charge[j]/abs(position[i]-position[j]) for i in range(3) for j in range(i+1,3))
check('ex23.2-assembly',energy,-k*e*e/2,1e-12)
check('ex23.2-third-particle',sum(k*charge[2]*charge[i]/abs(position[2]-position[i]) for i in [0,1]),k*e*e/2,1e-12)
check('ex23.3',[1.602e-19*1.5e7,1.602e-19*1.5e7*.5,1.5e7*.5],[2.4e-12,1.2e-12,7.5e6])
V=[k*12e-9*(1/.06-1/.04),k*12e-9*(1/.04-1/.14),0]
check('ex23.4',V,[-900,1930,0])
check('ex23.5',[4e-9*v for v in V],[-3.6e-6,7.7e-6,0])
Va=k*3e-9*(1/.01-1/.02);Vb=-Va
check('ex23.7',[Va,Vb,sqrt(2*2e-9*(Va-Vb)/5e-9)],[1350,-1350,46])
check('air-ionization',[.01*3e6,2*3e6],[3e4,6e6])
check('alpha-electron-volts',2*1.602e-19*1000,3.204e-16,1e-12)
check('shark-water-gallons-per-hour',500*3600/3.785411784,5e5,.06)
for x,a,Q in [(.2,.3,2e-9),(.8,.1,-4e-9)]:
 lam=Q/(2*pi*a)
 Vr=simpson(lambda t:k*lam*a/sqrt(x*x+a*a),0,2*pi)
 check('ring-potential-'+str(x),Vr,k*Q/sqrt(x*x+a*a),1e-9)
 Vrod=simpson(lambda y:k*Q/(2*a)/sqrt(x*x+y*y),-a,a)
 exact=k*Q/(2*a)*log((sqrt(x*x+a*a)+a)/(sqrt(x*x+a*a)-a))
 check('rod-potential-'+str(x),Vrod,exact,1e-9)
 h=1e-6
 Vfun=lambda z:k*Q/sqrt(z*z+a*a)
 gradient=-(Vfun(x+h)-Vfun(x-h))/(2*h)
 check('ring-gradient-'+str(x),gradient,k*Q*x/(x*x+a*a)**1.5,1e-8)
for point in [(.2,.3,.4),(-.5,.1,.8)]:
 Q=2e-9;h=1e-6;r=sqrt(sum(x*x for x in point))
 potential=lambda p:k*Q/sqrt(sum(t*t for t in p))
 deriv=[]
 for i in range(3):
  pa=list(point);pb=list(point);pa[i]+=h;pb[i]-=h
  deriv.append(-(potential(pa)-potential(pb))/(2*h))
 check('point-gradient-'+str(point),deriv,[k*Q*x/r**3 for x in point],1e-8)
out=root/'qa/physics/chapter23';out.mkdir(parents=True,exist_ok=True)
(out/'theory-checks.json').write_text(json.dumps({'status':'passed','groups':len(checks),'checks':checks},ensure_ascii=False,indent=2),encoding='utf8')
print('Passed',len(checks),'arithmetic, integration and derivative groups for chapter23 theory.')
