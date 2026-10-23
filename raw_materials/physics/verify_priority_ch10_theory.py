"""Recompute actual teaching examples and check the symbolic model numerically."""
from pathlib import Path
import math,json
import numpy as np
ROOT=Path(__file__).resolve().parents[2];Q=ROOT/'qa/physics1-priority';Q.mkdir(exist_ok=True)
cases={}
F=900;r=.8;angle=math.radians(109)
lever=r*math.sin(angle);torque=F*lever
assert math.isclose(torque,r*F*math.cos(math.radians(19)),rel_tol=1e-12)
assert math.isclose(torque,680.7733744315,rel_tol=1e-10)
cases['10.1']=dict(force_N=F,r_m=r,angle_deg=109,lever_m=lever,torque_Nm=torque,tangentialForce_N=F*math.cos(math.radians(19)))
M=50;R=.06;F=9;I=.5*M*R*R;alpha=F*R/I;a=R*alpha;v=math.sqrt(2*a*2)
assert math.isclose(alpha,6,rel_tol=1e-12) and math.isclose(a,.36,rel_tol=1e-12)
assert math.isclose(.5*I*(v/R)**2,F*2,rel_tol=1e-12)
cases['10.2']=dict(I_kg_m2=I,alpha_rad_s2=alpha,acceleration_m_s2=a,speedAfter2m_m_s=v)
values=[]
for M,m,R in [(50,1,.06),(1,3,.1),(.01,10,2),(10000,.2,.05)]:
 a=9.8/(1+M/(2*m));T=m*9.8/(1+2*m/M)
 assert math.isclose(m*9.8-T,m*a,rel_tol=1e-9)
 assert math.isclose(T*R,.5*M*R**2*(a/R),rel_tol=1e-12)
 assert 0<a<9.8 and 0<T<m*9.8
 h=2;v=math.sqrt(2*a*h)
 assert math.isclose(m*9.8*h,.5*m*v*v+.25*M*v*v,rel_tol=1e-12)
 values.append(dict(M=M,m=m,R=R,a=a,T=T))
cases['10.3']=values
# These source examples are symbolic; evaluate their conservation balances on several positive inputs.
for M,R,h in [(1,.2,1),(3,.1,5),(.02,.02,.1)]:
 v=math.sqrt(4*9.8*h/3);Ktrans=.5*M*v*v;Krot=.25*M*v*v
 assert math.isclose(Ktrans+Krot,M*9.8*h,rel_tol=1e-12)
 assert math.isclose(Ktrans/(Ktrans+Krot),2/3,rel_tol=1e-12)
cases['10.4']=dict(speedSquaredFactor=4/3,translationFraction=2/3,rotationFraction=1/3)
coefficients=[2/5,1/2,2/3,1]
speeds=[math.sqrt(2*9.8/(1+c)) for c in coefficients]
assert all(speeds[i]>speeds[i+1] for i in range(3))
cases['10.5']=dict(shapeInertiaCoefficients=coefficients,speedsAfterOneMeter_m_s=speeds)
for M,R in [(1,.1),(10,.01),(.02,.02)]:
 a=2*9.8/3;T=M*9.8/3
 assert math.isclose(M*9.8-T,M*a,rel_tol=1e-12)
 assert math.isclose(T*R,.5*M*R*R*a/R,rel_tol=1e-12)
cases['10.6']=dict(acceleration_m_s2=2*9.8/3,tensionWeightFraction=1/3)
for M,beta in [(1,.1),(3,.6),(.2,1)]:
 a=5/7*9.8*math.sin(beta);friction=2/7*M*9.8*math.sin(beta)
 assert math.isclose(M*9.8*math.sin(beta)-friction,M*a,rel_tol=1e-12)
 assert math.isclose(friction,(2/5)*M*a,rel_tol=1e-12)
cases['10.7']=dict(accelerationSlopeFactor=5/7,frictionWeightSineFactor=2/7)
torque=10;I=2;t=8;alpha=torque/I;theta=.5*alpha*t*t;omega=alpha*t
W=torque*theta;K=.5*I*omega*omega
assert W==K==1600 and W/t==200 and torque*omega==400
cases['10.8']=dict(alpha_rad_s2=alpha,angle_rad=theta,omega_rad_s=omega,work_J=W,kineticEnergy_J=K,averagePower_W=W/t,finalPower_W=torque*omega)
I=2.5;t=3;omega=40*t*t;L=I*omega;tau=I*80*t
assert L==900 and tau==600
cases['10.9']=dict(t_s=t,omega_rad_s=omega,L_kg_m2_s=L,torque_Nm=tau)
I1=3+2*5*1**2;I2=2.2+2*5*.2**2;omega1=math.pi;omega2=I1/I2*omega1
K1=.5*I1*omega1**2;K2=.5*I2*omega2**2
assert math.isclose(I1*omega1,I2*omega2,rel_tol=1e-12)
assert math.isclose(omega2/(2*math.pi),2.5,rel_tol=1e-12) and math.isclose(K2/K1,5,rel_tol=1e-12)
cases['10.10']=dict(I1=I1,I2=I2,omega1_rad_s=omega1,omega2_rad_s=omega2,K1_J=K1,K2_J=K2,work_J=K2-K1)
IA=.5*2*.2**2;IB=.5*4*.1**2;wa=50;wb=200;w=(IA*wa+IB*wb)/(IA+IB)
K1=.5*(IA*wa**2+IB*wb**2);K2=.5*(IA+IB)*w*w;loss=IA*IB/(2*(IA+IB))*(wa-wb)**2
assert math.isclose(K2/K1,2/3,rel_tol=1e-12)
assert math.isclose(K1-K2,loss,rel_tol=1e-12)
cases['10.11']=dict(IA=IA,IB=IB,wa=wa,wb=wb,commonOmega=w,K1_J=K1,K2_J=K2,energyLost_J=loss)
m=.01;v=400;d=1;M=15;l=.5;Idoor=M*d*d/3;Ibullet=m*l*l;L=m*v*l;omega=L/(Idoor+Ibullet)
K1=.5*m*v*v;K2=.5*(Idoor+Ibullet)*omega**2
assert math.isclose(omega,.39980009995,rel_tol=1e-10)
cases['10.12']=dict(L_kg_m2_s=L,Idoor=Idoor,Ibullet=Ibullet,omega_rad_s=omega,K1_J=K1,K2_J=K2,energyRatio=K2/K1,quarterTurnTime_s=(math.pi/2)/omega)
r=.02;R=.03;period=4;Omega=2*math.pi/period;omega=2*9.8*r/(R*R*Omega)
assert math.isclose(omega,277.28327863121325,rel_tol=1e-12)
cases['10.13']=dict(precessionPeriod_s=period,precessionOmega_rad_s=Omega,spinOmega_rad_s=omega,spin_rev_min=omega/(2*math.pi)*60,precessionSpinRatio=Omega/omega)
# Explicit center-of-mass decomposition for actual planar rigid rotations.
masses=np.array([1.,2.,3.]);positions=np.array([[0.,1.],[2.,0.],[-1.,-1.]])
center=np.average(positions,axis=0,weights=masses);relative=positions-center
angular=2.7;u=np.array([3.,-.4]);w=angular*np.column_stack((-relative[:,1],relative[:,0]));velocities=u+w
assert np.allclose(np.sum(masses[:,None]*w,axis=0),0)
K=.5*np.sum(masses*np.sum(velocities**2,axis=1));I=np.sum(masses*np.sum(relative**2,axis=1))
assert math.isclose(K,.5*masses.sum()*float(u@u)+.5*I*angular**2,rel_tol=1e-12)
cases['kineticDecomposition']=dict(totalK=K,centerOfMass=center.tolist(),relativeMomentum=np.sum(masses[:,None]*w,axis=0).tolist())
out=dict(status='passed',scope='All13 actual teaching examples, multiple symbolic parameter sets and the center-of-mass energy identity; source coverage, figure integrity and display are checked separately.',cases=cases)
(Q/'ch10-theory-parent-ledger.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(status='passed',teachingExamples=13,additionalIdentityChecks=1,doorOmega=cases['10.12']['omega_rad_s'],gyroscopeSpin_rad_s=omega)))
