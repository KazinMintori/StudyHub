from pathlib import Path
import json,math,hashlib
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch02-numbered37-46-recheck';OUT.mkdir(parents=True,exist_ok=True);checks=[]
def ck(unit,name,actual,expected,tol=1e-9):
 assert math.isclose(actual,expected,rel_tol=tol,abs_tol=tol),(unit,name,actual,expected)
 checks.append({'unit':unit,'quantity':name,'computed':float(actual),'expected':float(expected)})
g=9.8
for t,want in[(1,14.2),(3,-5.4)]:ck('2.37','velocity'+str(t),24-g*t,want)
assert (24-g*1)*(-g)<0 and(24-g*3)*(-g)>0
T=1.9;H=.5*g*T*T
ck('2.38','height',H,17.689);ck('2.38','impactspeed',g*T,18.62)
ck('2.38','distanceintegral',quad(lambda t:g*t,0,T)[0],H)
d=.176;t=math.sqrt(2*d/g);ck('2.39','reactiontime',t,.18952141659173713);ck('2.39','distancesubstitution',.5*g*t*t,d)
gm=1.6;u=.8;H=5;U=math.sqrt(u*u+2*gm*H);t=(U-u)/gm
ck('2.40','impactspeed',U,4.079215610874228);ck('2.40','fall-distance',u*t+.5*gm*t*t,H)
h1=525;a1=2.25;uc=math.sqrt(2*a1*h1);tc=uc/a1
ck('2.41','powered-height',.5*a1*tc*tc,h1)
ck('2.41','enginecutvelocity',a1*tc,uc)
up=uc/g;maxheight=h1+uc*up-.5*g*up*up
ck('2.41','maxheight',maxheight,645.5357142857143)
tau=brentq(lambda t:h1+uc*t-.5*g*t*t,up,30);impact=uc-g*tau
ck('2.41','cuttoimpacttime',tau,16.43764156496341)
ck('2.41','impactspeed',abs(impact),112.4833320985825)
ck('2.41','postcut-energyinvariant',impact*impact,uc*uc+2*g*h1)
ck('2.41','postcut-displacementintegral',quad(lambda t:uc-g*t,0,tau)[0],-h1)
h=40;u=5
for t,y,v in[(.25,40.94375,2.55),(1,40.1,-4.8)]:
 ck('2.42','heightat'+str(t),h+u*t-.5*g*t*t,y);ck('2.42','velocityat'+str(t),u-g*t,v)
T=brentq(lambda t:h+u*t-.5*g*t*t,0,5);U=math.sqrt(u*u+2*g*h)
ck('2.42','impacttime',T,3.412543398638345);ck('2.42','impactspeed',abs(u-g*T),U)
ck('2.42','maximumheight',h+u*u/(2*g),41.275510204081634)
T=3.6;u=g*T/2;ck('2.43','maxheight',u*u/(2*g),15.876);ck('2.43','returnposition',u*T-.5*g*T*T,0)
T=5.;y=-30;u=(y+.5*g*T*T)/T
ck('2.44','initialspeed',u,18.5);ck('2.44','targetposition',u*T-.5*g*T*T,y)
ck('2.44','maximumheight',u*u/(2*g),17.461734693877556);ck('2.44','topvelocity',u-g*(u/g),0)
ge=g*(1.75/18.6)**2
ck('2.45','inferredgravity',ge,.08675135853855936)
ck('2.45','sameheight',.5*ge*18.6**2,.5*g*1.75**2)
u=40
for v,want in[(20,20/g),(-20,60/g),(0,40/g)]:
 t=brentq(lambda t:u-g*t-v,0,10);ck('2.46','velocity-root'+str(v),t,want)
for t in[0,2*u/g]:ck('2.46','zero-displacement'+str(t),u*t-.5*g*t*t,0)
ck('2.46','maxheight',u*u/(2*g),81.63265306122449)
for t in[2,40/g,6]:
 eps=1e-5;ck('2.46','acceleration-at'+str(t),((u-g*(t+eps))-(u-g*(t-eps)))/(2*eps),-g)


print("PASS",len(checks),"independent checks for2.37–2.46.")
