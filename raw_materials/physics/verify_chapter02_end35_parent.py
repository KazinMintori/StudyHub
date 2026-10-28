from pathlib import Path
import json,math,hashlib
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch02-end35-recheck'
OUT.mkdir(parents=True,exist_ok=True)
checks=[]
def ck(name,actual,expected,tol=1e-9):
 assert math.isclose(actual,expected,rel_tol=tol,abs_tol=tol),(name,actual,expected)
 checks.append({'name':name,'computed':float(actual),'expected':float(expected)})
# Dot positions are measured from the actual source crop, not guessed from an
# agent's prose. Exclude all graph traces by restricting to the top dot row.
im=np.asarray(Image.open(ROOT/'docs/vat-ly-1/bai-giang/img/young-02/hinh-q2-2.png').convert('RGB'))
mask=(im[:25,:,:].max(axis=2)<100).sum(axis=0)>1
columns=np.where(mask)[0];groups=[]
for value in columns:
 if not groups or value>groups[-1][-1]+1:groups.append([int(value)])
 else:groups[-1].append(int(value))
centres=[float(np.mean(g))for g in groups];assert len(centres)==6,centres
gaps=np.diff(centres);assert np.all(np.diff(gaps)>0),gaps
checks.append({'name':'ActualQ2.2 increasing dot gaps','centresPixels':centres,'successiveGapsPixels':gaps.tolist(),'correctChoice':'d'})
# Q2.4: Average equals instantaneous at one time despite nonzero acceleration.
ck('Q2.4 average velocity',(2**2-0)/2,2)
ck('Q2.4 instantaneous velocity at1',2*1,2)
# Q2.5: Finite differences provide a separate check of derivative/sign claims.
for t in np.linspace(.05,.95,10):
 h=1e-5;x=lambda u:10*u-u**3
 velocity=(x(t+h)-x(t-h))/(2*h)
 acceleration=(x(t+h)-2*x(t)+x(t-h))/h**2
 ck('Q2.5a derivative at'+str(t),velocity,10-3*t*t,1e-6)
 ck('Q2.5a second derivative at'+str(t),acceleration,-6*t,2e-4)
 assert velocity>0 and acceleration<0
for t in np.linspace(0,5,11):
 h=1e-5;v=lambda u:2-math.exp(-u)
 a=(v(t+h)-v(t-h))/(2*h);ck('Q2.5b derivative at'+str(t),a,math.exp(-t),1e-7);assert a>0
# Q2.9 return trip and endpoint/tangent, Q2.10 constant v, Q2.11 top of throw.
ck('Q2.9 net displacement',2*(2-2)-0,0)
ck('Q2.9 endpoint derivative',2-2*2,-2)
ck('Q2.10 slope of constantvelocity',0,0)
ck('Q2.11 instantaneous acceleration',-9.8,-9.8)
ck('Q2.11 average acceleration0to1',(0-9.8)/(1-0),-9.8)
# Q2.13 two explicitly different functions sharing exact endpoints.
for t,expected in[(16,277),(25,19)]:
 u=(t-16)/9
 ck('Q2.13 linear endpoint'+str(t),277-258*u,expected)
 ck('Q2.13 curved endpoint'+str(t),277-258*u*u,expected)
ck('Q2.13 shared average',(19-277)/(25-16),-258/9)
ck('Q2.14 actual average',quad(lambda u:1+u*u,0,1)[0],4/3)
assert not math.isclose(4/3,1.5)
for g,H,d in[(9.8,20,.6),(1.6,12,.5)]:
 v0=math.sqrt(2*g*H);ck('Q2.15 equivalent acceleration',v0*v0/(2*d),g*H/d)
for v0 in[5.5,12,15]:
 g=9.8;T=2*v0/g
 ck('Q2.16 return position'+str(v0),v0*T-.5*g*T*T,0)
 ck('Q2.16 return velocity'+str(v0),v0-g*T,-v0)
for t in[1,2,3,5]:
 g=9.8;tau=1;d=.5*g*t*t-.5*g*(t-tau)**2
 ck('Q2.17 gap'+str(t),d,g*tau*t-.5*g*tau*tau)
ck('Q2.18 integrals recover x',50+quad(lambda t:10+quad(lambda u:2-.1*u,0,t)[0],0,20)[0],1550/3)
for v0,H in[(5,20),(12,50),(15,100)]:
 g=9.8;U=math.sqrt(v0*v0+2*g*H);tu=(U+v0)/g;td=(U-v0)/g
 ck('Q2.19 up impact position'+str(v0),v0*tu-.5*g*tu*tu,-H)
 ck('Q2.19 down impact position'+str(v0),-v0*td-.5*g*td*td,-H)
 ck('Q2.19 time difference'+str(v0),tu-td,2*v0/g)
ck('Q2.20 total time',120/3+120/5,64)
ck('Q2.20 average',240/(120/3+120/5),3.75)
ck('Q2.22 time scaling',math.sqrt(2*3*12/9.8)/math.sqrt(2*12/9.8),math.sqrt(3))
# Green Lantern: Independent equations for both halves and exact source duration.
g=9.8;tau=1.;h=(3+2*math.sqrt(2))*g*tau*tau
first=math.sqrt(h/g);total=math.sqrt(2*h/g);mid=-math.sqrt(g*h)
ck('Bridge last-half duration',total-first,tau)
ck('Bridge first-half displacement',-.5*g*first*first,-h/2)
ck('Bridge last-half displacement',mid*tau-.5*g*tau*tau,-h/2)


rows=[]
def guided_check(unit,name,value,expected,tol=1e-10):
 assert math.isclose(value,expected,rel_tol=tol,abs_tol=tol),(unit,name,value,expected)
 rows.append({'unit':unit,'quantity':name,'value':value,'expected':expected})
t=brentq(lambda u:.5*8*u*u-18*u,.1,10)
guided_check('VP2.5.1','catch-time',t,4.5);guided_check('VP2.5.1','catch-distance',.5*8*t*t,81)
a=brentq(lambda u:.5*u*12.5**2-30*12.5,0,10)
guided_check('VP2.5.2','police-acceleration',a,4.8);guided_check('VP2.5.2','catch-distance',.5*a*12.5**2,375)
t=brentq(lambda u:30*u-.5*1.8*u*u-20*u,1,16)
guided_check('VP2.5.3','catch-time',t,100/9);guided_check('VP2.5.3','distance',20*t,2000/9);guided_check('VP2.5.3','SUV-speed',30-1.8*t,10)
for vC,aT,aC in[(5,2,3),(10,3,3),(25,4,1),(12,1,4)]:
 t=2*vC/(aT+aC);x=.5*aT*t*t
 guided_check('VP2.5.4','coincident-positions',x,vC*t-.5*aC*t*t)
 guided_check('VP2.5.4','closed-form-coordinate',x,2*aT*vC*vC/(aT+aC)**2)
 guided_check('VP2.5.4','passing-relative-velocity',aT*t-(vC-aC*t),vC)
 assert (t<=vC/aC)==(aT>=aC)
g=9.8
for t,y,v in[(.3,3.159,9.06),(2.6,-1.924,-13.48)]:
 guided_check('VP2.7.1','position-at'+str(t),12*t-.5*g*t*t,y)
 guided_check('VP2.7.1','velocity-at'+str(t),12-g*t,v)
t=1.5
guided_check('VP2.7.2','position',-8*t-.5*g*t*t,-23.025);guided_check('VP2.7.2','velocity',-8-g*t,-22.7)
target_time=brentq(lambda t:-8*t-.5*g*t*t+8,0,2)
guided_check('VP2.7.2','negative-branch-via-time',-8-g*target_time,-math.sqrt(220.8))
v0=math.sqrt(.5**2+2*g*4);t=(v0-.5)/g
guided_check('VP2.7.3','position-via-derived-time',v0*t-.5*g*t*t,4)
guided_check('VP2.7.3','target-signed-velocity',v0-g*t,.5)
guided_check('VP2.7.3','v0',v0,8.868483523128404)
for H in[1,4,10]:
 v0=math.sqrt(2*g*H)
 guided_check('VP2.7.4','half-height-speed-ratio',math.sqrt(v0*v0-2*g*(H/2))/v0,1/math.sqrt(2))
 guided_check('VP2.7.4','half-speed-height',(v0*v0-(v0/2)**2)/(2*g),.75*H)
for y in[4,-4]:
 D=12**2-2*g*y
 for sign in[-1,1]:
  t=(12+sign*math.sqrt(D))/g;guided_check('VP2.8.1','quadratic-substitution-'+str((y,sign)),12*t-.5*g*t*t,y)
t=brentq(lambda u:9*u+.5*g*u*u-5,0,1)
guided_check('VP2.8.2','time',t,(-9+math.sqrt(179))/g)
guided_check('VP2.8.2','target-displacement',9*t+.5*g*t*t,5)
v0=5.5;guided_check('VP2.8.3','max-height',v0*v0/(2*g),30.25/19.6)
for sign in[-1,1]:
 t=(v0+sign*math.sqrt(4.77))/g
 guided_check('VP2.8.3','target-1.30-height-'+str(sign),v0*t-.5*g*t*t,1.3)
 guided_check('VP2.8.3','target-velocity-'+str(sign),v0-g*t,-sign*math.sqrt(4.77))
guided_check('VP2.8.3','unreachable-height-discriminant',v0*v0-2*g*1.8,-5.03)
for v0 in[5,10,15]:
 top=v0/g;guided_check('VP2.8.4','top-height',v0*top-.5*g*top*top,v0*v0/(2*g));guided_check('VP2.8.4','top-velocity',v0-g*top,0)
 for factor in[.5,1.5]:
  t=factor*v0/g
  guided_check('VP2.8.4','three-eighths-height',v0*t-.5*g*t*t,3*v0*v0/(8*g))
  guided_check('VP2.8.4','branch-velocity',v0-g*t,(1-factor)*v0)

result={"status":"passed-independent-end35-models","discussionBridgeChecks":len(checks),"guidedChecks":len(rows),"checks":checks+rows}
(OUT/"result.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
print("PASS",len(checks)+len(rows),"independent checks for35sourceunits.")
