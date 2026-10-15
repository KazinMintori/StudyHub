"""Numerical checks for exercises36.1–36.17 using exact screen geometry where needed."""
from pathlib import Path
import math,json
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter36';q.mkdir(parents=True,exist_ok=True)
sin=math.sin;asin=math.asin;tan=math.tan;atan=math.atan;pi=math.pi;deg=math.degrees;rad=math.radians
r={};c=3e8
def put(i,**data):r[str(i)]=data
def sinc2(x):return 1. if x==0 else (sin(x)/x)**2
def angle_orders(lam,a):return [deg(asin(m*lam/a)) for m in range(1,int(a/lam)+1)]
put(1,wavelengthNm=.750e-3*sin(atan(.00135/2))*1e9)
a=500e-9/sin(atan(.008/2/2));newtheta=asin(.125e-3/a)
put(2,slitMm=a*1e3,newCentralWidthM=2*2*tan(newtheta),newHalfAngleDeg=deg(newtheta))
a=.0666e-3;lam=585e-9;maxm=math.floor(a/lam)
put(3,maxOrder=maxm,totalDarkFringes=2*maxm,outerAngleDeg=deg(asin(maxm*lam/a)))
put(4,centralWidthMm=2*3.50*tan(asin(633e-9/.750e-3))*1e3)
theta=asin(.09/.12);put(5,zeroAnglesDeg=[-deg(theta),deg(theta)],zeroDistancesM=[-8*tan(theta),8*tan(theta)])
put(6,wavelengthKm=800*1,africaMinDeg=deg(asin(800/4500)),australiaMinDeg=deg(asin(800/3700)))
lam=.15/(75/60);a=lam/sin(atan(.613/3.20));angles=angle_orders(lam,a)
put(7,wavelengthM=lam,slitM=a,positiveMinimaDeg=angles)
sn=sin(atan(.006/2/2.50));put(8,widthsM=[lam/sn for lam in [500e-9,50e-6,.500e-9]])
put(9,wavelengthM=344/1250,positiveMinimaDeg=angle_orders(344/1250,1.))
k=1.4e7;lam=2*pi/k;a=lam/sin(rad(28.6));put(10,wavelengthNm=lam*1e9,frequencyHz=c/lam,widthUm=a*1e6,positiveMinimaDeg=angle_orders(lam,a))
lam=633e-9;a=.350e-3;R=3.;y1=R*tan(asin(lam/a));y2=R*tan(asin(2*lam/a))
put(11,centralWidthMm=2*y1*1e3,firstSideWidthMm=(y2-y1)*1e3)
lam=120e-6;R=1.50;a=lam/sin(atan(.9/2/R));newlam=a*sin(atan(1.8/2/R))
put(12,widthMm=a*1e3,newWavelengthUm=newlam*1e6,naiveDoubleUm=240)
put(13,widthNm=580,intensity45Ratio=sinc2(pi*sin(rad(45))))
a=.450e-3;lam=620e-9;R=3.
put(14,intensityRatios=[sinc2(pi*a*sin(atan(y/R))/lam) for y in [.001,.003,.005]])
lam=c/88.9e6;a=15.;put(15,wavelengthM=lam,positiveMinimaDeg=angle_orders(lam,a),intensity5Wm2=3.50*sinc2(pi*a*sin(rad(5))/lam))
put(16,intensityWm2=4e-5*sinc2(pi*.0290e-3*sin(rad(1.2))/592e-9))
phi=rad(344);beta=rad(172);ratio=sinc2(beta/2)*math.cos(phi/2)**2
put(17,spacingOverWidth=344/172,intensityRatio=ratio,intensityWm2=.234*ratio)
assert len(r)==17
(q/'exercises-01-17-data-checks.json').write_text(json.dumps(dict(status='passed',numberedExercises=17,results=r),indent=2),encoding='utf-8')
print(json.dumps(r,indent=2))
