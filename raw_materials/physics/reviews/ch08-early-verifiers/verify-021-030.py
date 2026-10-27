"""Independent physical models for source-reviewed chapter8 units 021-030."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad,solve_ivp
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/"qa/physics1-remaining/ch08-early-recomputed";OUT.mkdir(parents=True,exist_ok=True)
checks=[]
def near(name,a,b,tol=1e-9):
 assert np.allclose(a,b,rtol=tol,atol=tol),(name,a,b)
 checks.append(dict(name=name,actual=np.asarray(a).tolist(),expected=np.asarray(b).tolist()))
def yes(name,c):
 assert c,name
 checks.append(dict(name=name,passed=True))
u=(-.250*.120+.350*.650)/.250
ki=.5*.250*u*u;kfa=.5*.250*.120**2;kfb=.5*.350*.650**2
near('21 reconstructed original incident speed',u,.790)
near('21 complete initial/final kinetic energies',[ki,kfa,kfb],[.0780125,.0018,.0739375])
near('21 change in kinetic energy',kfa+kfb-ki,-.002275)
near('21 signed momentum balance',.250*u,-.250*.120+.350*.650)
p=1750*1.5-1450*1.1;v2=(p-1750*.25)/1450
ki=.5*1750*1.5**2+.5*1450*1.1**2;kf=.5*1750*.25**2+.5*1450*v2**2
near('22 actual total initial momentum',p,1030)
near('22 actual light car velocity',v2,.4086206896551724)
near('22 full two-car initial/final energies',[ki,kf],[2846,175.74137931034483])
near('22 energy change not assumed elastic',kf-ki,-2670.2586206896553)
yes('22 light car leaves toward right',v2>0)
k=1.75*100;x=.20;m=.9;energy=.5*k*x*x;v=math.sqrt(energy/m)
near('23 stiffness conversion N/cm to N/m',k,175)
near('23 original spring energy',energy,3.5)
near('23 each block speed',v,1.9720265943665387)
near('23 both blocks receive all spring energy',2*(.5*m*v*v),energy)
near('23 net momentum zero',m*v+m*(-v),0)
va=-3*1.2;energy=.5*va**2+.5*3*1.2**2
near('24 signed final A velocity',va,-3.6)
near('24 exact net momentum',va+3*1.2,0)
near('24 full spring energy',energy,8.64)
M=72.5;m=.00420;u=965
for angle,expected in [(0,-.05590344827586207),(56,-.03126081155392308)]:
 vx=u*math.cos(math.radians(angle));V=-m*vx/M
 near('25 actual recoil angle '+str(angle),V,expected)
 near('25 horizontal momentum angle '+str(angle),M*V+m*vx,0)
 relative=-m*vx/(M+m)
 yes('25 muzzle-frame correction below stated precision '+str(angle),abs(V-relative)<.00001)
for ma,mb,va in [(.5,3,8),(3,.5,8),(2.5,7.5,100),(1,1,3)]:
 vb=ma/mb*va;ka=.5*ma*va*va;kb=.5*mb*vb*vb
 near('26 two-fragment momentum '+str((ma,mb)),ma*va-mb*vb,0)
 near('26 inverse mass kinetic energy ratio '+str((ma,mb)),ka/kb,mb/ma)
md,mr,u,v,alpha=65,45,13,8,math.radians(53.1)
vR=np.array([v*math.cos(alpha),v*math.sin(alpha)])
vD=(np.array([mr*u,0])-mr*vR)/md
near('27 full Rebecca velocity components',vR,[4.803361802607071,6.397477267896723])
near('27 independently solved Daniel vector',vD,[5.674595675118181,-4.4290227239285])
near('27 full two-axis momentum',md*vD+mr*vR,[585,0])
speed=np.linalg.norm(vD);angle=math.degrees(math.atan2(vD[1],vD[0]))
near('27 Daniel speed and opposite-side angle',[speed,angle],[7.198421936,-37.972043],tol=1e-7)
triangle_angle=-math.degrees(math.acos((u-v*math.cos(alpha))/math.sqrt(u*u+v*v-2*u*v*math.cos(alpha))))
near('27 direction independently from momentum triangle',angle,triangle_angle)
ki=.5*mr*u*u;kf=.5*mr*v*v+.5*md*speed**2
near('27 original initial energy',ki,3802.5)
near('27 actual total final energy',kf,3124.06154710225,tol=1e-8)
near('27 actual energy change',kf-ki,-678.43845289775,tol=1e-8)
V=-3/70*12*math.cos(math.radians(35))
near('28 ground-frame horizontal recoil',V,-.4212781942057672)
near('28 horizontal momentum balance',70*V+3*12*math.cos(math.radians(35)),0)
yes('28 vertical momentum would require external ice impulse',3*12*math.sin(math.radians(35))>0)
M,m,u=60,2.5,4.5;v=M*u/(M+m)
near('29 actual catch speed',v,4.32)
near('29 catch total horizontal momentum',(M+m)*v,M*u)
near('29 thrown vertically relative to skater keeps speed',(M*v+m*v)/(M+m),v)
near('29 alternative ground-vertical speed',(M+m)*v/M,4.5)
yes('29 no unforced recovery to original speed in skater frame',v<u)
a,b=math.radians(30),math.radians(45)
A=np.array([[math.cos(a),math.cos(b)],[math.sin(a),-math.sin(b)]])
va,vb=np.linalg.solve(A,np.array([40.,0.]))
near('30 source angles linear system solution',[va,vb],[29.282032302755095,20.705523608201663])
near('30 both momentum components',A@np.array([va,vb]),[40,0])
fraction=1-(va*va+vb*vb)/40**2
near('30 actual lost fraction',fraction,.19615242270663202)
yes('30 unequal outgoing speeds for unequal source angles',not math.isclose(va,vb))
report=dict(status="passed",checksCount=len(checks),checks=checks)
(OUT/"numeric-021-030.json").write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+"\n").encode("utf8"))
print("PASS 021-030:",len(checks),"independent physical checks.")
