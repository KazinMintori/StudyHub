"""Parent numerical checks for source exercises11.49–95; independent source/diagram review is separate."""
from pathlib import Path
import math,json
import numpy as np
g=9.80;pi=math.pi
sd=lambda d:math.sin(math.radians(d))
cd=lambda d:math.cos(math.radians(d))
td=lambda d:math.tan(math.radians(d))
ad=lambda x:math.degrees(math.atan(x))
cases={}
def save(n,**v):
    assert all(math.isfinite(x) for x in v.values()),n
    cases[str(n)]=v
W=82*g;T=W*1.1*cd(35)/(1.4*sd(80));N=T*sd(25);f=W-T*cd(25)
save(49,T=T,normal=N,friction=f,mu=f/N)
T=1150*g*4*cd(30)/(6*sd(40))
save(50,T=T,wallHorizontal=T*cd(10))
w=(225*.75-255*.25)/.75
save(51,W=w,fulcrumShift=w*.25/(255+225+w))
save(52,handleF=400*.080*sd(60)/.300)
Ty=(16*g*.75+28*g*1.05)/1.5
save(53,Ty=Ty,T=Ty/math.sqrt(1-(1.5/2)**2),hingeY=44*g-Ty)
save(54,barOnHingeX=220,barOnHingeY=220*4/3)
m1=74*.215/2;m2=74*.14/2;mc=5.5
save(55,oneThighMass=m1,oneLowerLegMass=m2,strapPosition=(m1*.18+m2*.69+mc*.78)/(m1+m2+mc))
T=g*(18000*20+30000*30)*cd(30)/(40*sd(70))
Tx=-T*cd(40);Ty=T*sd(40)
assert math.isclose(40*cd(30)*Ty-40*sd(30)*Tx,g*(18000*20+30000*30)*cd(30))
save(56,T=T,hingeX=-Tx,hingeY=48000*g-Ty)
#57: Representative test of general angle and release formulas.
m,L,T=4.,3.,20.;theta=math.atan(m*g/(2*T));w=math.sqrt(3*g*math.sin(theta)/L)
assert math.isclose(T*L*math.sin(theta),m*g*L/2*math.cos(theta))
save(57,testTheta=math.degrees(theta),testOmega=w)
mf=72*.06/2;mw=7.5
B=g*(mf*.16+mw*.38)/.055
save(58,oneForearmHandMass=mf,biceps=B,elbowY=(mf+mw)*g-B)
#59: Angle relation and limiting cases.
for a in [.1,.5,1.]:
    theta=.7;Hx=a*g/math.tan(theta);Hy=(1-a)*g;beta=math.atan2(Hy,Hx)
    if a==.5:assert math.isclose(beta,theta)
    if a==1:assert math.isclose(beta,0)
save(59,equalAnglePositionFraction=.5,endLoadHingeAngle=0)
save(60,frictionOverWeight=.5,maxAngleForMuPoint4=ad(.4))
save(61,T=6490*3.75*cd(30)/(6*sd(40)))
W=45000.;T=2*W/td(37)
save(62,T=T,hingeX=T,hingeY=W,hingeMagnitude=math.hypot(T,W),hingeAngle=ad(W/T),releaseAlpha=3*g*cd(37)/(2*14),horizontalOmega=math.sqrt(3*g*sd(37)/14))
F=75*g*.125/.046
save(63,tendon=F,tendonOverWeight=F/(75*g),extension=F*.25/(1470e6*78e-6))
save(64,weight=(100*2-140*1)/4)
length=1.2/cd(30);dT=90*g/sd(30);dl=dT*length/(7e10*pi*.0025**2)
save(65,wireLength=length,increaseT=dT,additionalExtension=dl,smallAngleRotation=dl/(1.2*sd(30)))
TA=.036*g;TB=(.024+.036)*g
# Exact trigonometry for the printed36.9 and53.1 degree angles.
TC=TB/(sd(53.1)+cd(53.1)*td(36.9));TD=TC*cd(53.1)/cd(36.9)
FF=.120*g*.5+TD*sd(36.9)*.2+TC*sd(53.1)*.8
FE=.120*g+TB-FF
save(66,A=TA,B=TB,C=TC,D=TD,E=FE,F=FF)
legs=.9;upper=1.35;base=math.hypot(legs,upper);xh=legs**2/base;yh=legs*upper/base
xl=xh*(1-.41/legs);xu=xh+(.65/upper)*(base-xh)
Nh=(277*xl+473*xu)/base;Nf=750-Nh
ff=(xh*Nf-277*(xh-xl))/yh
assert math.isclose(Nf+Nh,750)
save(67,base=base,hipX=xh,hipY=yh,eachFootNormal=Nf/2,eachHandNormal=Nh/2,eachFootFriction=ff/2,eachHandFriction=-ff/2)
Y=9e10;A=6e-6;eps=2e-5;m=.08;r=1.4;T=Y*A*eps
save(68,T=T,bottomSpeed=math.sqrt((T/m-g)*r))
#69: Printed53 degree angle is between downward vertical and downward-left pull.
F=1250*1.1/(1.5*sd(53));N=1250+F*cd(53);f=F*sd(53)
save(69,F=F,normal=N,friction=f,mu=f/N)
mu=.4;theta=math.radians(15)
#70: a=x/L, Ty=W(.5+a), wall friction=W(1.5-a).
amin=(1.5-mu*.5/math.tan(theta))/(1+mu/math.tan(theta))
mu10=(1.5-.1)*math.tan(theta)/(.5+.1)
save(70,maxAngle=ad(mu),minimumX=amin,muAt10cm=mu10)
save(71,upperForce=200*g*(1-.5/1.25)/2,lowerForce=200*g*(1+.5/1.25)/2)
TL=620.;TR=TL*sd(30)/sd(50);W=TL*cd(30)+TR*cd(50)
save(72,rightTension=TR,weight=W,cgFromLeft=4*TR*cd(50)/W)
#73: Verify the derivative sign by finite differences for multiple tendon positions.
T,L,h=1000.,.4,.3
def maximum(D):return T*h*D/(L*math.sqrt(h*h+D*D))
for D in [.03,.07,.15]:
    exact=T*h**3/(L*(h*h+D*D)**1.5)
    numeric=(maximum(D+1e-6)-maximum(D-1e-6))/2e-6
    assert math.isclose(exact,numeric,rel_tol=1e-8) and exact>0
save(73,testDerivative=T*h**3/(L*(h*h+.07**2)**1.5))
#74: Force lever arms about the curb corner,0<h<R.
m,R,h=5,.4,.1;lever=math.sqrt(2*R*h-h*h)
save(74,testCenterF=m*g*lever/(R-h),testTopF=m*g*lever/(2*R-h))
T=700*2/(4*sd(30)+2*cd(30))
save(75,T=T,hingeBHorizontal=T*cd(30),combinedVertical=700-T*sd(30))
H=[sum(1/(2*k) for k in range(1,n+1)) for n in range(1,5)]
save(76,twoBlockOverhang=H[1],threeBlockOverhang=H[2],fourBlockOverhang=H[3],minimumBlocksFullOverhang=4)
m=.075
save(77,A=m*g/math.sqrt(3),B=2*m*g,C=m*g/math.sqrt(3),between=m*g/sd(60))
F=260*td(53/2)
save(78,crossbarCompression=F,hingeHorizontal=F,hingeVertical=0)
save(79,tipAngle=ad(.25/.50),slideAngleMuPoint6=ad(.60),slideAngleMuPoint4=ad(.40))
#80: Bottom short edge is inclined20 degrees to the floor. Pivot is the lower corner.
# Relative to that pivot, upper rope attachment=(L sin(theta),L cos(theta)).
L,d,theta,phi=3.75,1.75,math.radians(20),math.radians(58)
xcg=(L*math.sin(theta)-d*math.cos(theta))/2
ropeMomentArm=L*math.cos(theta+phi)
TOverW=-xcg/ropeMomentArm
assert xcg<0 and ropeMomentArm>0
save(80,totalTensionOverWeight=TOverW,eachWorkerForceOverWeight=TOverW/5,zeroForceAngle=ad(d/L))
F=.52*950
save(81,push=F,normalA=(950-F*1.60)/2,normalB=(950+F*1.60)/2,maximumH=1/.52)
m=12.;L=.70;omega=120*2*pi/60;Y=7e10;A=.014*1e-4;k=Y*A/L
# Self-consistent centripetal radius=L+extension; compare common small-extension approximation.
db=m*(omega**2*L+g)/(k-m*omega**2);dt=m*(omega**2*L-g)/(k-m*omega**2)
save(82,stiffness=k,bottomExtension=m*(omega**2*L+g)/k,topExtension=m*(omega**2*L-g)/k,quasiStaticRadiusRefinementBottom=db,quasiStaticRadiusRefinementTop=dt)
save(83,equalStressPositionFromA=1.05*4/(2+4),equalStrainPositionFromA=1.05*(4*1.2)/(2*1.8+4*1.2))
W=1900;L=15;Y=2e11;A=8e-4;k=Y*A/L;m=W/g;omega=12*2*pi/60
dv=W/k;T=m*omega**2*L/(1-m*omega**2/k);dr=T/k
save(84,restExtension=dv,rotatingT=T,rotatingExtension=dr,angle=math.degrees(math.acos(W/T)))
Fmax=1.4e10*.01*3e-4;m=70;dt=.030
v=(2*Fmax/m-g)*dt
save(85,oneBoneForce=Fmax,bothLegsForce=2*Fmax,landingSpeed=v,modelHeight=v*v/(2*g))
s=.422e-3;L=22;A=pi*.000860**2/4;Y=g*L/(A*s);m=9.5
T=m*g*(3-2*cd(36))
save(86,Y=Y,maximumTension=T,maximumExtension=s*T/g)
m2=np.array([1,1.5,2,2.5,3,4],dtype=float);x=np.array([3.50,2.83,2.50,2.32,2.16,2.00])
slope,intercept=np.polyfit(1/m2,x,1);pred=slope/m2+intercept;M=(2*1.3-slope)/.38
save(87,slope=float(slope),intercept=float(intercept),barMass=float(M),RSquared=float(1-np.sum((x-pred)**2)/np.sum((x-x.mean())**2)))
W=8.5*g
for label,x,theta in [('A',2,30),('B',1.5,60),('C',.75,37),('D',.5,75)]:
    T=W/(x*sd(theta));Hy=W-T*sd(theta);Hx=T*cd(theta)
    cases.setdefault('88',{})[label]={'T':T,'hingeX':Hx,'hingeY':Hy}
Wl,Wr=480,360
Nr=(Wl*1.6+Wr*4.1)/5;Nl=Wl+Wr-Nr
T=(3.2*Nl-1.6*Wl)/(2.4-.9)
Nlp=Nl+800*(5-3.2)/5
Tp=(3.2*Nlp-1.6*Wl)/(2.4-.9)
save(89,leftNormal=Nl,rightNormal=Nr,T=T,hingeForce=math.hypot(T,Wl-Nl),hingeOnLeftX=-T,hingeOnLeftY=Wl-Nl,TWithPainter=Tp)
mu=.30;cot=1/td(36.9)
Fhalf=mu*400/(1-.5*(1+mu*cot));Fpoint6=mu*400/(1-.6*(1+mu*cot))
save(90,midpointF=Fhalf,point6F=Fpoint6,criticalHeightFraction=1/(1+mu*cot))
k=2e11*(5e-3*1e-4)/1.5;mg=4.5*g;dx=.0005
wg=mg*dx;wf=.5*k*dx**2
save(91,initialExtension=mg/k,gravityWork=wg,appliedWork=wf,wireWork=-wg-wf,elasticEnergyChange=wg+wf)
mg=80*g;deltaT=mg*1*sd(30)/(1.5*cd(30))
save(92,tensionDifference=deltaT,T2=1160-deltaT)
save(93,differenceIncreaseForLargerAngle=1)
save(94,largerHoldingHeightReducesRequiredNetTension=1)
save(95,requiredMu=deltaT/mg,reducedMu=.50,noSlip=1)
assert deltaT<.50*mg
assert list(cases)==[str(n) for n in range(49,96)]
root=Path(__file__).resolve().parents[2];out=root/'qa/physics1-priority/ch11-numbered-e-values.json'
out.write_text(json.dumps({'status':'passed','scope':'Actual numerical inputs and explicit analytical model tests. Prompt subparts, source figures, prose and final layout remain separate review tasks.','cases':cases},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(cases,ensure_ascii=False,indent=2))
