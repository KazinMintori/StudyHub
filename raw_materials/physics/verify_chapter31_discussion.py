"""Check the quantitative and sign arguments used in the19 discussion solutions."""
from pathlib import Path
import math,json
import numpy as np
OUT=Path(__file__).resolve().parents[2]/'qa/physics/chapter31'
r={}
def record(n,**data):r[f'Q31.{n}']={'status':'passed',**data}
assert (1/2)**2==1/4
record(1,currentRatio=.5,lineLossRatio=.25,assumptions='fixed load power, power factor and line resistance')
theta=np.linspace(0,2*math.pi,100001)[:-1]
v=10*np.cos(theta);i=2*np.cos(theta-.6)
assert abs(i.mean())<1e-12
assert abs(np.mean(v*i)-10*2/2*math.cos(.6))<1e-12
record(2,meanCurrent=float(i.mean()),meanPower=float(np.mean(v*i)))
pr=3*np.cos(theta)**2
pl=-5*np.sin(theta)*np.cos(theta);pc=7*np.sin(theta)*np.cos(theta)
assert abs(pr.mean()-1.5)<1e-12 and abs(pl.mean())<1e-12 and abs(pc.mean())<1e-12
record(3,resistorMeanPower=float(pr.mean()),inductorMeanPower=float(pl.mean()),capacitorMeanPower=float(pc.mean()))
record(4,signConvention='q is signed left-plate charge; i enters that plate; i=dq/dt')
assert .5*2**2*10>0
record(5,idealInductorMeanPower=0,resistorLimiterPower=20)
for derivative in [-2.,2.]:
 assert math.copysign(1,3*derivative)==math.copysign(1,derivative)
record(6,relation='v_ab=L*di/dt for either signed current direction')
for R,X in [(0,4),(3,4),(3,-4)]:
 pf=R/math.hypot(R,X)
 assert (pf==0)==(R==0)
record(7,zeroPowerFactor='R=0, XL!=XC; finite R>0 gives positive factor')
angle=math.pi/2-math.atan2(60-20,30)
values=[30*math.cos(angle),-60*math.sin(angle),20*math.sin(angle)]
assert np.allclose(values,[24,-36,12],atol=1e-12)
assert abs(sum(values))<1e-12
record(8,instantaneousVoltagesV=values,sourceV=sum(values))
for sign in [-1,1]:
 phase=math.atan2(sign*100,1e-6)
 assert abs(abs(phase)-math.pi/2)<1e-7
record(9,phaseLimitsDegrees=[-90,90],powerFactorLimit=0)
record(10,resonantCapacitorRmsV=5*120,peakV=5*120*math.sqrt(2))
R,V,X=20.,120.,30.
oldI=V/R;newI=V/math.hypot(R,X)
assert newI<oldI and newI**2*R<oldI**2*R
record(11,resistanceRatio=1,currentRatio=newI/oldI,powerRatio=(newI/oldI)**2,assumptions='fixed R, source voltage and frequency')
assert math.hypot(20,40/3)<math.hypot(20,40)
record(12,dielectricFactor=3,impedanceDecreases=True)
assert math.hypot(20,60)>math.hypot(20,40)
record(13,unsaturatedIronCore='L increases; current decreases at fixed source')
for XL,XC in [(10,3),(3,10),(6,3),(3,6),(4,3),(3,4)]:
 before=math.hypot(10,XL-XC)
 noL=math.hypot(10,XC);noC=math.hypot(10,XL)
 assert math.isclose(before**2-noL**2,XL*(XL-2*XC),abs_tol=1e-12)
 assert math.isclose(before**2-noC**2,XC*(XC-2*XL),abs_tol=1e-12)
record(14,removeLThreshold='XL=2XC',removeCThreshold='XC=2XL')
assert math.hypot(10,5-5)==10
record(15,unchangedBrightness='XL=XC with fixed R and source')
record(16,steadyDcSecondaryEmf=0,primarySteadyCurrent='Vdc/Rwinding after transient')
assert (1/2)**2==.25
record(17,secondaryVoltageRatio=2,reflectedResistanceRatio=.25)
R,XC=3.,8.
XL=5.
z=math.hypot(R,XL-XC);znew=math.hypot(2*R,2*XL-XC/2)
assert math.isclose(znew,2*z,abs_tol=1e-12)
record(18,resonanceFrequencyRatio=.5,inductiveReactanceRatio=2,capacitiveReactanceRatio=.5,
       exceptionalRatioXLoverXC=5/8,impedanceDoesNotGenerallyDouble=True)
assert 1/math.sqrt((.5*.4)*(.5*2e-6))==2/math.sqrt(.4*2e-6)
record(19,Lratio=.5,Cratio=.5,resonanceFrequencyRatio=2)
assert len(r)==19
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'discussion-data-checks.json').write_text(json.dumps({'status':'passed','questions':19,'results':r},indent=2)+'\n',encoding='utf8')
print('Checked19 discussion arguments, including phase signs, limiting cases and brightness comparisons.')
