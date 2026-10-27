"""Independent physical models for source-reviewed chapter8 units 046-055."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad,solve_ivp
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/"qa/physics1-remaining/ch08-early-recomputed";OUT.mkdir(parents=True,exist_ok=True)
checks=[]
def ck(n,label,a,b,tol=1e-9):
 assert np.allclose(a,b,rtol=tol,atol=tol),(n,label,a,b)
 checks.append({'unit':n,'check':label,'actual':np.asarray(a).tolist(),'expected':np.asarray(b).tolist()})
def st(n,label,c):
 assert c,(n,label);checks.append({'unit':n,'check':label,'passed':True})
for n,m1,m2,u1,u2,expected in [(46,.15,.3,.8,-2.2,[-3.2,-.2]),(47,2.,6.,2.,0.,[-1,1]),(48,.01,.03,-.4,.2,[.5,-.1])]:
 momentum=m1*u1+m2*u2
 # Solve momentum plus restitution, independent of the closed-form fractions.
 final=np.linalg.solve([[m1,m2],[1,-1]],[momentum,-(u1-u2)])
 ck(n,'independentsystemsolution',final,expected);ck(n,'momentumconserved',[m1,m2]@final,momentum);ck(n,'energyconserved',np.array([m1,m2])@(final*final),m1*u1*u1+m2*u2*u2)
 ck(n,'oppositeimpulses',m1*(final[0]-u1),-m2*(final[1]-u2));ck(n,'kinetictransferscancel',m1*(final[0]**2-u1*u1)/2,-m2*(final[1]**2-u2*u2)/2)
ck(46,'displayedinitialmomentum',.15*.8+.3*(-2.2),-.54);ck(46,'displayedinitialenergy',(.15*.8**2+.3*2.2**2)/2,.774)
V=(2*2+6*0)/8;ck(47,'maxcompressioncommonvelocity',V,.5);ck(47,'storedspringenergy',2*2**2/2-8*V**2/2,3)
ck(48,'smallmarbleimpulse',.01*(.5-(-.4)),.009);ck(48,'largemarbleimpulse',.03*(-.1-.2),-.009);ck(48,'smallmarbleenergychange',.01*(.5**2-.4**2)/2,.00045)
speedFraction=abs((1-2)/(1+2));ck(49,'speedfraction',speedFraction,1/3);ck(49,'energyfraction',speedFraction**2,1/9)
st(49,'10collisionsminimal',speedFraction**10<=1/59000<speedFraction**9)
m=1.;M=9.;u=1.5e7;vf=np.linalg.solve([[m,M],[1,-1]],[m*u,-u]);ck(50,'protonreboundwithmass9',vf[0],-1.2e7);ck(50,'targetspeed',vf[1],3e6);ck(50,'conservedenergy',m*vf[0]**2+M*vf[1]**2,m*u*u)
vf=np.linalg.solve([[1,3],[1,-1]],[6,-6]);ck(51,'massratio3',vf,[-3,3]);ck(51,'halfinitialvelocityforB',vf[1],6/2)
MS=1.99e30;MJ=1.90e27;d=7.78e11;x=MJ*d/(MS+MJ);ck(52,'centerofmass',x,742105527.3859129);ck(52,'massmomentsbalance',MS*x,MJ*(d-x));st(52,'outsidesun',x>6.96e8)
q=(1250/2370)**3;x=19700*q/(1+q);ck(53,'distancefromPluto',x,2520.5446343305002);ck(53,'massmomentsbalance',x,q*(19700-x));st(53,'outsidePluto',x>2370/2)
x=(1200*0+1800*40)/3000;P=1200*12+1800*20;V=P/3000;ck(54,'centerofmass',x,24);ck(54,'totalmomentum',P,50400);ck(54,'centerofmassspeed',V,16.8);ck(54,'momentumfromCM',3000*V,P)
side=np.cbrt(.027);y=(.5*side/2+.8*(side+.4))/1.3;ck(55,'cubeside',side,.3);ck(55,'CMheight',y,.48846153846153845);st(55,'betweenobjectcenters',side/2<y<side+.4)
report=dict(status="passed",checksCount=len(checks),checks=checks)
(OUT/"numeric-046-055.json").write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+"\n").encode("utf8"))
print("PASS 046-055:",len(checks),"independent physical checks.")
