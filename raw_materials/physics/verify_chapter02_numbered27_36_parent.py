from pathlib import Path
import json,math,hashlib
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch02-numbered27-36-recheck';OUT.mkdir(parents=True,exist_ok=True);checks=[]
def ck(unit,name,actual,expected,tol=1e-9):
 assert math.isclose(actual,expected,rel_tol=tol,abs_tol=tol),(unit,name,actual,expected)
 checks.append({'unit':unit,'quantity':name,'computed':float(actual),'expected':float(expected)})
g=9.8;vf=5000;d=4;a=vf*vf/(2*d);T=vf/a
ck('2.27','acceleration',a,3125000);ck('2.27','duration',T,.0016);ck('2.27','distanceviaquadrature',quad(lambda t:a*t,0,T)[0],d);assert a/g<450000
# E2.28 is a qualitative source sketch. These functions are one ILLUSTRATIVE
# sketch consistent with rounded positions/intersections, not extracted laws.
xa=lambda t:3+t*t;xb=lambda t:4*t
for t in[1,3]:ck('2.28','illustrative sharedposition at'+str(t),xa(t),xb(t))
ck('2.28','illustrative commonvelocity time',brentq(lambda t:2*t-4,0,4),2)
assert xa(0)>xb(0)and xa(2)<xb(2)and xa(4)>xb(4)
def vel(t):
 return 20 if t<=5 else 20+6.25*(t-5)if t<=9 else 45-11.25*(t-9)
for t,want in[(3,0),(7,6.25),(11,-11.25)]:
 eps=1e-5;ck('2.29','acceleration'+str(t),(vel(t+eps)-vel(t-eps))/(2*eps),want)
for t,want in[(5,100),(9,230),(13,320)]:ck('2.29','distance'+str(t),quad(vel,0,t,points=[p for p in[5,9]if p<t])[0],want)
a=3.8**2/(2*6.8)
ck('2.30','halfway speed',math.sqrt(2*a*3.4),3.8/math.sqrt(2))
u=math.sqrt(2*g*.44);T=2*u/g
ck('2.31','speed',u,2.9366647748764243);ck('2.31','flighttime',T,.5993193418115151)
ck('2.31','apexheight',u*(T/2)-.5*g*(T/2)**2,.44)
u=22;H=30;U=math.sqrt(u*u+2*g*H);T=(u+U)/g
ck('2.32','impacttime',T,5.585858274233653);ck('2.32','impactposition',u*T-.5*g*T*T,-H);ck('2.32','impactvelocity',u-g*T,-U)
T=2*8.2/g;ck('2.33','returnposition',8.2*T-.5*g*T*T,0)
u=9.5;H=3.6;v=math.sqrt(u*u-2*g*H);T=(u-v)/g
ck('2.34','ceilingfirsttime',T,.516597801380943);ck('2.34','ceilingposition',u*T-.5*g*T*T,H);assert u-g*T>0
gm=.379*g;T=8.5;u=gm*T/2;H=gm*T*T/8
ck('2.35','initialspeed',u,15.78535);ck('2.35','maximumheight',H,33.54386875);ck('2.35','returnheight',u*T-.5*gm*T*T,0)
H=80*.3048;d=3*.3048;u=math.sqrt(2*g*H);T=2*u/g;a=u*u/(2*d);tau=u/a
ck('2.36','assumedheightmetres',H,24.384);ck('2.36','assumeddistancemetres',d,.9144);ck('2.36','conditionalmeanacceleration',a,261.3333333333333)
ck('2.36','handstrokeviaquadrature',quad(lambda t:a*t,0,tau)[0],d);ck('2.36','flightreturn',u*T-.5*g*T*T,0)


print("PASS",len(checks),"independent checks for2.27–2.36, with qualitative/estimate conditions retained.")
