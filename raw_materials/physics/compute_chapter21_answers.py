from math import sqrt,atan2,degrees,sin,cos,tan,radians,pi,log
from pathlib import Path
import json,runpy

root=Path(__file__).resolve().parents[2]
v=runpy.run_path(str(root/'raw_materials/physics/verify_chapter21.py'))
k,e,me,mp,eps,NA=[v[key] for key in ['k','e','me','mp','eps','NA']]
field,force=v['field'],v['force']
a={}
def polar(x,y):return {'x':x,'y':y,'magnitude':sqrt(x*x+y*y),'angle':degrees(atan2(y,x))}
a['21.2']=[2e4*100e-6,2e4*100e-6/e]
a['21.4']=polar(*force([(2e-6,0,-.3),(4e-6,.4,0)],(0,.3),2e-6))
a['21.6']=sqrt(3.33e-21*.2**2/k)/e
n=.025/.026982*NA*13;q=sqrt(1e4*.8**2/k)
a['21.8']=[n,q/e,q/(n*e)]
a['21.10']=polar(*force([(4e-9,.2,0),(5e-9,-.3,0)],(0,0),-6e-9))
a['21.12']=[.6*.3**2/(k*.550e-6),.6]
a['21.14']=polar(*force([(2e-6,0,.3),(-2e-6,0,-.3)],(.4,0),4e-6))
a['21.16']=-sqrt(k*3e-6*8e-6/(7+k*3e-6*5e-6/.2**2))
a['21.18']=[k*e*e*((.17e-9)**-2-(.28e-9)**-2+(.19e-9)**-2-(.30e-9)**-2),k*e*e/(.0529e-9)**2]
a['21.19']=k*e*e*(2*((.18e-9)**-2-(.29e-9)**-2)+(.19e-9)**-2-(.30e-9)**-2)
acc=2*.016/(3.2e-6)**2;a['21.20']=[mp*acc/e,acc*3.2e-6]
a['21.22']=[k*5e-9/.25**2,sqrt(k*5e-9/12)]
acc=2*4.5/(3e-6)**2;a['21.24']=[acc,me*acc/e,acc/9.8]
a['21.26']=[6.5e-6*1.85e8-k*8.75e-6*6.5e-6/.025**2,6.5e-6*1.85e8+k*8.75e-6*6.5e-6/.025**2]
acc=e*364/me;t=.02/1.6e6;a['21.28']=sqrt((1.6e6)**2+(acc*t)**2)
a['21.30']=[sqrt((4.5e5)**2+2*e*1.5*.375/me),sqrt((1.9e4)**2-2*e*1.5*.375/mp)]
a['21.36']={str(x):field([(-4e-9,0,0),(-5e-9,.8,0)],(x,0))[0] for x in [.2,1.2,-.2]}
a['21.38-unit']=4*sqrt(2)*k/.1**2
a['21.40']={'E1':field([(-5e-9,0,0)],(0,.04)),'E2':field([(3e-9,.03,0)],(0,.04)),'total':field([(-5e-9,0,0),(3e-9,.03,0)],(0,.04))}
q=5.6e11*e*.1e-3;a['21.42']=[q,k*q/.05**2,sqrt(k*q/1e-6)]
a['21.44']=polar(*field([(-4e-9,.6,.8),(6e-9,.6,0)],(0,0)))
a['21.46']=5e-9*(.2/.6)**2
a['21.48']=3.2e-10/(2*pi*eps*2.5)
Q=175e-9*.085;R=.085/(2*pi)
a['21.50']=[k*Q/(.06*sqrt(.06**2+(.085/2)**2)),k*Q*.06/(.06**2+R*R)**1.5]
delta=5e-30*1.6e6;a['21.52']=[delta,delta/(1.5*1.380649e-23)]
a['21.54']=e*2*k*6.17e-30/(3e-9)**3
a['21.58']=-.6/(sqrt(3.5/2.5)-1)
lo,hi=0,pi/2-1e-6
target=4*sin(radians(25))**2*tan(radians(25))
for _ in range(70):
 mid=(lo+hi)/2
 if sin(mid)**2*tan(mid)>target:hi=mid
 else:lo=mid
a['21.61-angle']=degrees((lo+hi)/2)
a['21.62-horizontal']=(sqrt(5**2-2*9.8*.6)-2)/sqrt(2*.6/9.8)*.0005/5e-6
a['21.62-downward']=( (5**2-2**2)/(2*.6)-9.8)*.0005/5e-6
a['21.66']=[.0025/.06538*NA*30,.0025/.06538*NA*30*e,k*(.0025/.06538*NA*30*e)**2/.02**2]
a['21.68']=[(45-k*3e-9/1.2**2)*.6**2/k,(-45-k*3e-9/1.2**2)*.6**2/k]
a['21.70']=polar(*force([(-3e-9,0,0),(2e-9,0,.04)],(.03,.04),5e-9))
h=sqrt(.03**2-(.045/2)**2);q= .005*324/(2*k*1.75e-6*(.045/2)/.03**3);a['21.72']=[q,-q]
distance=2*.530*sin(radians(29));a['21.74']=(6.8e-6*9.8*tan(radians(29))+k*(72e-9)**2/distance**2)/(72e-9)
omega=2*eps*.1*9.8/(1e-6*(10e-9/1e-4));a['21.76']=[omega,.05*(1-omega)/sqrt(omega*(2-omega))]
a['21.78']=2*.0125*(5e3)**2/(800*.26*(.26+2*.56))
for x in [.2,.1]:
 R=.025;Q=7e-12;E=Q/(pi*R*R)/(2*eps)*(1-x/sqrt(x*x+R*R));Ep=k*Q/x**2;a['21.81-'+str(x)]=(Ep-E)/Ep*100
t=.02/50;q=2*1.4e-11*.00030/(8e4*t*t);a['21.88']=[q,q/e,q/4]
a['21.90']=[50/k,(50/700)**(1/3)]
q2=2e-6*(3/4)*(.03/.04)**2
F1=k*4e-6*2e-6/.04**2
a['21.95']=[q2,(4/5+3/5*3/4)*F1]
# Geometry E21.96: the two legs at P are perpendicular. q1 and q2 lie on y=0, with P at (5²/13,60/13)cm.
xp=.05**2/.13;yp=.05*.12/.13; q1=-3e-6
q2=-q1*xp/(xp-.13)*(.12/.05)**3;a['21.96']={'q2':q2,'E':polar(*field([(q1,0,0),(q2,.13,0)],(xp,yp)))}
out=root/'qa/physics/chapter21/answers-computed.json';out.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(a,ensure_ascii=False,indent=2))
