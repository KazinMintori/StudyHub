from pathlib import Path
import json,math,hashlib
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch02-numbered13-26-recheck';OUT.mkdir(parents=True,exist_ok=True);checks=[]
def ck(unit,name,actual,expected,tol=1e-9):
 assert math.isclose(actual,expected,rel_tol=tol,abs_tol=tol),(unit,name,actual,expected)
 checks.append({'unit':unit,'quantity':name,'computed':float(actual),'expected':float(expected)})
def deriv(f,t,h=1e-4):return(f(t+h)-f(t-h))/(2*h)
# 2.13: Solve signed-distance roots independently using bracketed position.
x=lambda t:50+2*t-.0625*t*t;v=lambda t:2-.125*t
ck('2.13','initialposition',x(0),50);ck('2.13','initialvelocity',deriv(x,0),2);ck('2.13','initialacceleration',deriv(v,0),-.125)
ck('2.13','stoppingtime',brentq(v,0,40),16)
ck('2.13','returntime',brentq(lambda t:x(t)-50,20,40),32)
for lo,hi,direction in[(0,16,1),(16,32,-1),(32,40,-1)]:
 t=brentq(lambda t:abs(x(t)-50)-10,lo,hi)
 ck('2.13','signed-distance root'+str(lo),abs(x(t)-50),10)
 assert np.sign(v(t))==direction
 expected=math.sqrt(1.5)if hi<=32 else math.sqrt(6.5)
 ck('2.13','root speed'+str(lo),abs(v(t)),expected)
ck('2.13','maximumposition',x(16),66)
# 2.14: Reject AGY's6.88m/s²; derivative at actual target time is6.42495.
t=brentq(lambda t:.86*t*t-12,0,5);a=deriv(lambda t:.86*t*t,t)
ck('2.14','targettime',t,math.sqrt(12/.86))
ck('2.14','instantacceleration',a,6.424951361683604)
# 2.15: Numerical differentiation and independent average.
f=lambda t:3+.1*t*t
ck('2.15','meanaccel',(f(5)-f(0))/5,.5)
for t,want in[(0,0),(5,1)]:ck('2.15','instantaccel'+str(t),deriv(f,t),want)
for u,w,ans in[(15,5,-1),(-5,-15,-1),(15,-15,-3)]:ck('2.16','signedmean'+str((u,w)),(w-u)/10,ans)
# 2.17: Position polynomial, derivative roots and correct acceleration.
x=lambda t:2.17+4.8*t*t-.1*t**6;v=lambda t:9.6*t-.6*t**5;a=lambda t:9.6-3*t**4
for t,wantx,wanta in[(0,2.17,9.6),(2,14.97,-38.4)]:
 ck('2.17','zero velocity'+str(t),v(t),0)
 ck('2.17','position'+str(t),x(t),wantx)
 ck('2.17','acceleration'+str(t),a(t),wanta)
 ck('2.17','numericfirstderivative'+str(t),deriv(x,t),v(t),2e-6)
 ck('2.17','numericsecondderivative'+str(t),deriv(v,t),a(t),2e-6)
ck('2.17','accelerationzero',brentq(a,0,2),(3.2)**.25)
mphft=5280/3600;mphm=.44704
u=30*mphft;w=70*mphft;T=10;mean=(w-u)/T
ck('2.18','distancefeet',quad(lambda t:u+mean*t,0,T)[0],2200/3)
ck('2.18','meanaccelfeet',mean,88/15)
ck('2.18','meanaccelSI',mean*.3048,1.78816)
v0=2*70/6-15;a=(15-v0)/6
ck('2.19','firstspeed',v0,25/3)
ck('2.19','acceleration',a,10/9)
ck('2.19','distanceviaquadrature',quad(lambda t:v0+a*t,0,6)[0],70)
T=.03;vf=73.14;a=vf/T
ck('2.20','acceleration',a,2438)
ck('2.20','distance',quad(lambda t:a*t,0,T)[0],1.0971)
vf=45;d=1.5;a=vf*vf/(2*d);T=vf/a
ck('2.21','accelerationconditionalrest',a,675)
ck('2.21','durationconditionalrest',T,1/15)
ck('2.21','distanceconditionalrest',.5*a*T*T,d)
v0=70*mphm;v1=30*mphm;T=5;b=(v0-v1)/T;T2=v1/b;total=T+T2
ck('2.22','chosenmeandecel',b,3.57632)
ck('2.22','extra time',T2,3.75)
ck('2.22','fullstopaftertime',v0-b*total,0)
ck('2.22','distanceconditionalconstant',quad(lambda t:v0-b*t,0,total)[0],136.906)
vf=105/3.6;b=250;d=vf*vf/(2*b)
ck('2.23','threshold distance',d,1.7013888888888888)
ck('2.23','stopvelocityinvariant',vf*vf-2*b*d,0)
vf=20;d=120;a=vf*vf/(2*d);T=vf/a
ck('2.24','acceleration',a,5/3);ck('2.24','duration',T,12);ck('2.24','trafficdistance',20*T,240)
b=60*9.8;T=.036;u=b*T;d=.5*b*T*T
ck('2.25','initialspeed',u,21.168);ck('2.25','stoppingdistance',d,.381024);ck('2.25','endpointvelocity',u-b*T,0)
v=lambda t:8-4*t/3
for t,want in[(4,8/3),(7,-4/3)]:ck('2.26','velocity'+str(t),v(t),want)
for t in[3,6,7]:ck('2.26','acceleration'+str(t),deriv(v,t),-4/3)
ck('2.26','distance0to4.5',quad(lambda t:abs(v(t)),0,4.5)[0],22.5)
ck('2.26','distance0to7',quad(lambda t:abs(v(t)),0,7,points=[6])[0],74/3)
ck('2.26','displacement0to7',quad(v,0,7)[0],70/3)
ck('2.26','positionmaximum',8*6-2*6**2/3,24)


(OUT/"result.json").write_text(json.dumps({"status":"passed","checks":checks,"numericChecks":len(checks)},ensure_ascii=False,indent=2)+"\n",encoding="utf8")
print("PASS",len(checks),"independent checks for2.13–2.26.")
