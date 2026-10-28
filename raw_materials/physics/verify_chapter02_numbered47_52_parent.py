from pathlib import Path
import json,math,hashlib
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq,minimize_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch02-numbered47-52-recheck';OUT.mkdir(parents=True,exist_ok=True);checks=[]
def ck(unit,name,actual,expected,tol=1e-9):
 assert math.isclose(actual,expected,rel_tol=tol,abs_tol=tol),(unit,name,actual,expected)
 checks.append({'unit':unit,'quantity':name,'computed':float(actual),'expected':float(expected)})
g=9.8;T=6;u=g*T/2;U=math.sqrt(u*u+2*g*28);tf=(u+U)/g
ck('2.47','returnposition',u*T-.5*g*T*T,0)
ck('2.47','waterheight',u*tf-.5*g*tf*tf,-28)
ck('2.47','impactspeed',abs(u-g*tf),37.59202042987315)
v=lambda t:8-4*t/3
ck('2.48','area',quad(v,0,6)[0],24)
ck('2.48','averagevelocity',quad(v,0,6)[0]/6,4)
ck('2.48','distanceviaequation',8*6-.5*(4/3)*6**2,24)
A=2.8
v=lambda t:quad(lambda u:A*u,0,t)[0]
y=lambda t:quad(v,0,t)[0]
ck('2.49','height10',y(10),1400/3)
ts=brentq(lambda t:y(t)-325,0,10)
ck('2.49','targettime',ts,(6*325/A)**(1/3))
ck('2.49','speed325',v(ts),109.9965563660247)
assert 0<ts<10
k=.032;b=15
a=lambda t:-k*(b-t)
v=lambda t:8+quad(a,0,t)[0]
x=lambda t:-14+quad(v,0,t)[0]
ck('2.50','initialposition',x(0),-14)
ck('2.50','initialvelocity',v(0),8)
ck('2.50','signedacceleration0',a(0),-.48)
ck('2.50','signedacceleration10',a(10),-.16)
ck('2.50','velocity10',v(10),4.8)
ck('2.50','position10nestedquadrature',x(10),142/3)
A=1.5;B=.12
a=lambda t:A*t-B*t*t
v=lambda t:quad(a,0,t)[0]
x=lambda t:quad(v,0,t)[0]
for t in[0,2,12.5]:
 ck('2.51','velocityfunction'+str(t),v(t),.5*A*t*t-B*t**3/3)
 ck('2.51','positionfunction'+str(t),x(t),A*t**3/6-B*t**4/12)
maximum=minimize_scalar(lambda t:-v(t),bounds=(0,25),method='bounded')
ck('2.51','maxvelocity',v(maximum.x),A**3/(6*B**2),1e-7)
ck('2.51','maximizingtime',maximum.x,A/B,2e-7)
assert a(12)>0 and a(13)<0
alpha=1.2
v=lambda t:5+quad(lambda u:alpha*u,1,t)[0]
x=lambda t:6+quad(v,1,t)[0]
ck('2.52','velocitygivenat1',v(1),5)
ck('2.52','positiongivenat1',x(1),6)
ck('2.52','velocityat2',v(2),6.8)
ck('2.52','positionat2nestedquadrature',x(2),11.8)
ck('2.52','inferredvelocityat0',v(0),4.4)
ck('2.52','inferredpositionat0',x(0),1.4)


print("PASS",len(checks),"independent checks for2.47–2.52.")
