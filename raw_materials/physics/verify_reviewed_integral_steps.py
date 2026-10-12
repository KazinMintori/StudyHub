from pathlib import Path
from math import sqrt,log,isclose
import json
root=Path(__file__).resolve().parents[2];checks={}
def check(name,x,y,tol=1e-7):
 assert isclose(x,y,rel_tol=tol,abs_tol=1e-10),(name,x,y)
 checks[name]={'actual':x,'expected':y}
def integrate(f,a,b,n=10000):
 h=(b-a)/n
 return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))
def deriv(f,x,h=1e-6):return (f(x+h)-f(x-h))/(2*h)
for a,L in [(.1,.5),(.4,.2)]:
 G=lambda u:u/(a*a*sqrt(a*a+u*u))
 for y in [0,.1*L,.5*L,.9*L,L]:
  direct=integrate(lambda u:(a*a+u*u)**(-1.5),y-L,y)
  check('21.93-first-integral-'+str((a,L,y)),direct,G(y)-G(y-L))
 check('21.93-second-integral-'+str((a,L)),integrate(lambda y:y/sqrt(a*a+y*y),0,L),sqrt(a*a+L*L)-a)
 H=lambda s:sqrt(s*s+L*L)-s-L*log((L+sqrt(s*s+L*L))/s)
 for s in [a,2*a,4*a]:
  check('21.93-energy-primitive-'+str((a,L,s)),deriv(H,s),sqrt(s*s+L*L)/s-1,1e-6)
 J=lambda x:log((x+a/2)/(x+a/2+L))
 direct=integrate(lambda x:1/(x+a/2)-1/(x+a/2+L),a/2,a/2+L)
 check('21.97-primitive-'+str((a,L)),direct,J(a/2+L)-J(a/2))
 check('21.97-log-ratio-'+str((a,L)),direct,log((a+L)**2/(a*(a+2*L))))
for alpha in [.2,.5,.9]:
 R=.1;delta=2*R*alpha/(1-alpha*alpha)
 check('21.91-turning-depth-'+str(alpha),alpha*delta,sqrt(delta*delta+R*R)-R)
distances=[.01,.015,.02,.025,.03,.035,.04]
fieldsA=[2.72e5,1.79e5,1.34e5,1.07e5,.902e5,.770e5,.677e5]
fieldsB=[5.45e5,2.42e5,1.34e5,.861e5,.605e5,.443e5,.335e5]
check('22.55-mean-Er',sum(E*r for E,r in zip(fieldsA,distances))/7,2695.57,1e-5)
check('22.55-mean-Er2',sum(E*r*r for E,r in zip(fieldsB,distances))/7,54.0971,1e-5)
out=root/'qa/physics/reviews/integral-steps-checks.json';out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({'status':'passed','groups':len(checks),'checks':checks},indent=2),encoding='utf8')
print('Passed',len(checks),'independent checks of expanded integral and turning-point steps.')
