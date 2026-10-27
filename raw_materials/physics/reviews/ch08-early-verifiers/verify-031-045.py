"""Independent physical models for source-reviewed chapter8 units 031-045."""
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
for n,m1,u1,m2,u2,expected in [(31,70,5.5,110,-4,-.3055555555555556),(32,70,4,65,-2.5,.8703703703703703)]:
 v=(m1*u1+m2*u2)/(m1+m2)
 near(f'{n} signed common velocity',v,expected)
 near(f'{n} full momentum balance',(m1+m2)*v,m1*u1+m2*u2)
 yes(f'{n} velocity within two initial velocities',min(u1,u2)<v<max(u1,u2))
 loss=.5*m1*u1*u1+.5*m2*u2*u2-.5*(m1+m2)*v*v
 near(f'{n} independent reduced-mass kinetic loss',loss,.5*(m1*m2/(m1+m2))*(u1-u2)**2)
v=15*1.1/19.5;ki=.5*15*1.1**2;kf=.5*19.5*v*v
near('33 original fish speed after swallowing',v,.8461538461538461)
near('33 full system momentum',19.5*v,16.5)
near('33 original initial/final energies',[ki,kf],[9.075,6.980769230769231])
near('33 positive mechanical energy dissipated',ki-kf,2.0942307692307702)
near('33 independent reduced-mass loss',ki-kf,.5*15*4.5/19.5*1.1**2)
for mass,u in [(1,1),(7,6),(25,15)]:
 m=mass/4;v=m*u/(mass+m);g=9.8
 near('34 dart-to-combined velocity ratio '+str(mass),v/u,.2)
 near('34 momentum before/after '+str(mass),(mass+m)*v,m*u)
 # Independently integrate the slack-rope ballistic segment until vertical speed zero.
 def apex(t,y):return y[1]
 apex.terminal=True;apex.direction=-1
 sol=solve_ivp(lambda t,y:[y[1],-g],[0,2*v/g],[0,v],events=apex,rtol=1e-11,atol=1e-12)
 h=sol.y_events[0][0,0]
 near('34 integrated rise '+str(mass),h,u*u/(50*g))
 near('34 energy during slack-rope rise '+str(mass),(mass+m)*g*h,.5*(mass+m)*v*v)
 yes('34 collision loses kinetic energy '+str(mass),.5*(mass+m)*v*v<.5*m*u*u)
va=(-7-6*.5)/4
near('35 actual outgoing A signed velocity',va,-2.5)
near('35 exact momentum',4*va+6*.5,4*2+6*(-2.5))
ki=.5*4*2**2+.5*6*2.5**2;kf=.5*4*va**2+.5*6*.5**2
near('35 full two-block energies',[ki,kf],[26.75,13.25])
near('35 decrease is positive energy magnitude',ki-kf,13.5)
m,M,u,U=1050,6320,-15.,10.
v=(m*u+M*U)/(m+M);Ub=-m*u/M
near('36 common eastward velocity',v,6.4382632293080055)
near('36 original momentum balance',(m+M)*v,47450)
near('36 truck speed for complete stopping',Ub,2.492088607594937)
near('36 second-case total momentum zero',m*u+M*Ub,0)
ki=.5*m*u*u+.5*M*U*U;kf=.5*(m+M)*v*v;delta_a=kf-ki;delta_b=-(.5*m*u*u+.5*M*Ub*Ub)
near('36 part c initial/final case-a energies',[ki,kf],[434125,152747.79511533244])
near('36 part c both requested changes',[delta_a,delta_b],[-281377.20488466753,-137750.19778481012])
near('36 case a independent reduced-mass loss',-delta_a,.5*m*M/(m+M)*(u-U)**2)
near('36 case b independent reduced-mass loss',-delta_b,.5*m*M/(m+M)*(u-Ub)**2)
yes('36 larger absolute decrease in case a',abs(delta_a)>abs(delta_b))
p=np.array([85*7.2,110*8.8]);v=p/195
near('37 two original initial momenta',p,[612,968])
near('37 common velocity vector',v,[3.1384615384615384,4.964102564102565])
near('37 common speed',np.linalg.norm(v),5.873010735162334)
near('37 north-of-east angle',math.degrees(math.atan2(v[1],v[0])),57.69764021664984)
near('37 exact two-axis momentum',195*v,p)
theta=math.radians(65);speed=22500/(3500*math.sin(theta));ua=3500*speed*math.cos(theta)/2000
vf=speed*np.array([math.cos(theta),-math.sin(theta)])
near('38 source-angle final speed',speed,7.093143764758876)
near('38 reconstructed incident car A speed',ua,5.245961154243734)
near('38 complete two-axis momentum',3500*vf,[2000*ua,-1500*15])
near('38 final direction south of east',-math.degrees(math.atan2(vf[1],vf[0])),65)
vjack=5*np.array([math.cos(math.radians(34)),math.sin(math.radians(34))]);vjill=(np.array([55*8.,0])-55*vjack)/48
near('39 full Jill velocity vector',vjill,[4.4169722405700735,-3.2037093428011536])
near('39 Jill speed',np.linalg.norm(vjill),5.456500465235756)
near('39 south-of-east direction',-math.degrees(math.atan2(vjill[1],vjill[0])),35.954051656451696)
near('39 two-axis momentum balance',55*vjack+48*vjill,[440,0])
yes('39 Jill opposite deflection side from Jack',vjill[1]<0<vjack[1])
pfalconi=np.array([0.,.6*20]);pfalconf=np.array([0.,-.6*5]);praven_i=np.array([1.5*9,0]);vraven=(pfalconi+praven_i-pfalconf)/1.5
near('40 source rebound gives transfer sum not difference',pfalconi-pfalconf,[0,15])
near('40 raven final components in axes of solution',vraven,[9,10])
near('40 full two-bird two-axis momentum',1.5*vraven+pfalconf,pfalconi+praven_i)
near('40 raven turn from own original direction',math.degrees(math.atan2(vraven[1],vraven[0])),48.01278750418334)
near('40 raven speed',np.linalg.norm(vraven),13.45362404707371)
a=math.radians(24);vf=16*np.array([math.sin(a),math.cos(a)]);uc=2850*vf[0]/950;ut=2850*vf[1]/1900
near('41 exact source angle measured east of north',math.degrees(math.atan2(vf[0],vf[1])),24)
near('41 source car/pickup initial speeds',[uc,ut],[19.52335886763841,21.92509098342242])
near('41 separate original momenta',[950*uc,1900*ut],2850*vf)
m,M,mu,d,g=.005,1.2,.20,.310,9.8
v=math.sqrt(2*mu*g*d);u=(M+m)/m*v
near('42 postcollision sliding speed',v,1.1023611023616535)
near('42 original bullet incident speed',u,265.6690256691585)
near('42 momentum at impact',m*u,(m+M)*v)
near('42 sliding work energy',mu*(m+M)*g*d,.5*(m+M)*v*v)
near('42 independent stopping displacement from Newton',v*v/(2*mu*g),d)
m,M,u,L,g=.012,6,380,.7,9.8;v=m*u/(M+m);h=v*v/(2*g)
near('43 common postimpact speed',v,.7584830339321359)
near('43 exact impact momentum',m*u,(m+M)*v)
near('43 source part-a vertical rise',h,.029351862896066203)
near('43 source part-b initial bullet energy',.5*m*u*u,866.4)
near('43 source part-c final bullet-plus-pendulum energy',.5*(m+M)*v*v,1.72934131736527)
near('43 rise gains exactly postimpact kinetic energy',(m+M)*g*h,.5*(m+M)*v*v)
yes('43 source wire length permits turning before horizontal',0<h<L)
loss=.5*m*u*u-.5*(m+M)*v*v
near('43 independent reduced-mass loss',loss,.5*m*M/(m+M)*u*u)
V=3*(8-(-2))/15;x=V*math.sqrt(15/500)
near('44 block speed includes stone reversed momentum',V,2)
near('44 separate stone/block momentum',3*8,3*(-2)+15*V)
near('44 actual maximum spring compression',x,.34641016151377546)
near('44 block only spring energy balance',.5*15*V*V,.5*500*x*x)
yes('44 stone no longer counted in oscillating mass',not math.isclose(x,V*math.sqrt(18/500)))
v=.2*12/(.8+.2);T=(.8+.2)*(9.8+v*v/1.5)
near('45 actual postimpact speed',v,2.4)
near('45 exact impact momentum',(.8+.2)*v,.2*12)
near('45 actual immediate wire tension',T,13.64)
near('45 radial Newton balance',T-(.8+.2)*9.8,(.8+.2)*v*v/1.5)
yes('45 tension exceeds full combined weight',T>(.8+.2)*9.8)
report=dict(status="passed",checksCount=len(checks),checks=checks)
(OUT/"numeric-031-045.json").write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+"\n").encode("utf8"))
print("PASS 031-045:",len(checks),"independent physical checks.")
