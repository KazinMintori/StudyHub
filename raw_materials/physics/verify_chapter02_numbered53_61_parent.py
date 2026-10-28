from pathlib import Path
import json,math,hashlib
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch02-numbered53-61-recheck';OUT.mkdir(parents=True,exist_ok=True);checks=[]
def ck(unit,name,actual,expected,tol=1e-9):
 assert math.isclose(actual,expected,rel_tol=tol,abs_tol=tol),(unit,name,actual,expected)
 checks.append({'unit':unit,'quantity':name,'computed':float(actual),'expected':float(expected)})
g=9.8
# Three distances, independently invert the piecewise displacement.
distance=lambda t:2.5*t*t if t<=2 else 10+10*(t-2)
ck('2.53','accelerationdistance',distance(2),10)
for L,T,want in[(50,6,25/3),(100,11,100/11),(200,21,200/21)]:
 actual=brentq(lambda t:distance(t)-L,0,30)
 ck('2.53','racetime'+str(L),actual,T)
 ck('2.53','averagevelocity'+str(L),L/actual,want)
b=800;c=60;d=1.05;y=lambda t:b-c*t+d*t*t;v=lambda t:-c+2*d*t
ck('2.54','initialvelocity',v(0),-60)
first=brentq(y,0,c/(2*d))
ck('2.54','firstimpactvelocity',v(first),-math.sqrt(240))
ck('2.54','firstimpacttime',first,(c-math.sqrt(240))/(2*d))
assert first<c/(2*d) and (c+math.sqrt(240))/(2*d)>first
D=33/(1/3.5-1/6.5);ck('2.55','distancekm',D,250.25);ck('2.55','arrivaltimedifference',D/3.5-D/6.5,33)
for H in[1,30,100]:
 u=math.sqrt(2*g*H/3);T=3*u/g
 ck('2.56','groundposition'+str(H),u*T-.5*g*T*T,-H)
 ck('2.56','timeratio'+str(H),T/(u/g),3)
ck('2.57','lateaverage',(1000-63)/4.75,197.26315789473685)
ck('2.57','wholeaverage',1000/5.9,169.4915254237288)
v=lambda t:12-2*t;x=lambda t:quad(v,0,t)[0]
ck('2.58','returntime',brentq(x,6,20),12);ck('2.58','maximizingtime',brentq(v,0,10),6);ck('2.58','maximumdistance',x(6),36)
a=9/16;u=math.sqrt(2*a*16);T=u/a
ck('2.59','speed16',u,3*math.sqrt(2));ck('2.59','distance16',.5*a*T*T,16)
ck('2.59','duration',T,32/(3*math.sqrt(2)))
vf=1.6*14;tb=vf/3.5
ck('2.60','accelerationstage',quad(lambda t:1.6*t,0,14)[0],156.8)
ck('2.60','constantstage',vf*70,1568)
ck('2.60','brakingstage',quad(lambda t:vf-3.5*t,0,tb)[0],71.68)
ck('2.60','distancecombined',156.8+1568+71.68,1796.48)
v=lambda t:4+.8*t if t<=10 else 12-6*(t-10)
ck('2.61','distance',quad(lambda t:abs(v(t)),0,12,points=[10])[0],92)
ck('2.61','displacement',quad(v,0,12,points=[10])[0],92)
for t,want in[(5,.8),(11,-6)]:
 eps=1e-5;ck('2.61','acceleration'+str(t),(v(t+eps)-v(t-eps))/(2*eps),want)
assert not math.isclose((v(10)-v(10-1e-6))/1e-6,(v(10+1e-6)-v(10))/1e-6)


print("PASS",len(checks),"independent checks for2.53–2.61.")
