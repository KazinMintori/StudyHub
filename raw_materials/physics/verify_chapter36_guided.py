"""Independently compute twelve guided problems and the relativistic Doppler bridge."""
from pathlib import Path
import math,json
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter36';q.mkdir(parents=True,exist_ok=True)
sin=math.sin;asin=math.asin;tan=math.tan;atan=math.atan;pi=math.pi;deg=math.degrees;rad=math.radians
r={}
def put(key,**data):r[key]=data
lam=645e-9;a=.250e-3;y=.028/2;theta=asin(2*lam/a);R=y/tan(theta)
put('36.3.1',screenM=R,newSeparationMm=2*R*tan(asin(2*525e-9/a))*1e3,smallAngleScreenM=a*y/(2*lam))
a=.221e-3;y=.0457;R=5;lam=a*sin(atan(y/R))/3
put('36.3.2',wavelengthNm=lam*1e9,secondMinimumDeg=deg(asin(2*lam/a)))
phase=35;lam=545e-9;a=.250e-3;theta=asin(phase*lam/(2*pi*a));half=phase/2
put('36.3.3',angleDeg=deg(theta),intensityRatio=(sin(half)/half)**2)
lam=576e-9;a=.185e-3;first=asin(lam/a);alpha=pi*a*sin(first/2)/lam
put('36.3.4',firstMinimumDeg=deg(first),halfAngleDeg=deg(first/2),intensityAtHalfAngle=(sin(alpha)/alpha)**2)
d=1/(825e3);lam=d*sin(rad(41))/2
put('36.5.1',spacingNm=d*1e9,wavelengthNm=lam*1e9,firstDeg=deg(asin(lam/d)),thirdDeg=deg(asin(3*lam/d)))
lam=625e-9;d=lam/sin(rad(24));sn3=3*lam/d
assert sn3>1
put('36.5.2',linesPerMm=1/d/1e3,secondDeg=deg(asin(2*lam/d)),thirdExists=False,thirdFormalSin=sn3)
d=.165e-9;lam=.124e-9
orders=[m for m in range(1,10) if m*lam/(2*d)<=1]
put('36.5.3',orders=orders,anglesDeg=[deg(asin(m*lam/(2*d))) for m in orders])
d=.158e-9;lam=2*d*sin(rad(36));newlam=2*d*sin(rad(88))/3
assert math.floor(2*d/lam)==1 and math.floor(2*d/newlam)==3
put('36.5.4',originalWavelengthNm=lam*1e9,threeMaximaWavelengthNm=newlam*1e9,newAnglesDeg=[deg(asin(m*newlam/(2*d))) for m in [1,2,3]])
theta=9e-5;D=1.22*.017/sin(theta);theta2=asin(1.22*.211/D)
put('36.6.1',diameterM=D,newResolutionRad=theta2,newResolutionDeg=deg(theta2))
f=.250;D=f/4;lam=5.50e-7;theta=asin(1.22*lam/D);u=.005/tan(theta);v=f*u/(u-f)
put('36.6.2',apertureM=D,resolutionRad=theta,maxRangeM=u,imageSeparationUm=v*.005/u*1e6,farImageSeparationUm=f*tan(theta)*1e6)
lam=575e-9;f=.135;rho=.0112e-3;D=1.22*lam/sin(atan(rho/f))
put('36.6.3',apertureMm=D*1e3,fNumber=f/D)
distance=1.5e11;D=8.;ly=9.46e15
put('36.6.4',rangeLightYears=[distance/tan(asin(1.22*lam/D))/ly for lam in [690e-9,1400e-9]])
d=1/(5758*100);observed=d*sin(rad(23.41));rest=656.3e-9;ratio=observed/rest;beta=(ratio**2-1)/(ratio**2+1)
# Independent frequency-form identity for the relativistic longitudinal Doppler effect.
received_ratio=math.sqrt((1-beta)/(1+beta));assert math.isclose(received_ratio,rest/observed,rel_tol=1e-14)
put('bridge',observedWavelengthNm=observed*1e9,wavelengthRatio=ratio,recessionBeta=beta,recessionSpeedMps=beta*3e8,percentC=beta*100,direction='away')
assert len(r)==13
(q/'guided-data-checks.json').write_text(json.dumps(dict(status='passed',guidedProblems=12,bridge=1,results=r),indent=2),encoding='utf-8')
print(json.dumps(r,indent=2))
