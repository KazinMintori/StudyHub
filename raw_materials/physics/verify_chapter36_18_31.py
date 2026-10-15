"""Exercises36.18–36.31, including nonunique slit-width interpretations."""
from pathlib import Path
import math,json
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter36';q.mkdir(parents=True,exist_ok=True)
sin=math.sin;cos=math.cos;asin=math.asin;atan=math.atan;pi=math.pi;deg=math.degrees;rad=math.radians
r={}
def put(i,**data):r[str(i)]=data
def sinc2(x):return 1 if x==0 else (sin(x)/x)**2
lam=568e-9;a=.434e-3;d=.640e-3;theta=atan(.0009/.750)
put(18,intensityWm2=5e-4*sinc2(pi*a*sin(theta)/lam)*cos(pi*d*sin(theta)/lam)**2)
# Count nominal two-slit interference orders within the open envelope lobes.
def orders_in_lobe(ratio,lo,hi):return [m for m in range(-30,31) if lo*ratio<m<hi*ratio]
assert len(orders_in_lobe(3,-1,1))==5 and len(orders_in_lobe(2.2,-1,1))==5
put(19,intendedIntegerRatio=3,centralOrders=orders_in_lobe(3,-1,1),firstSideOrders=orders_in_lobe(3,1,2),nonIntegerCounterexample=2.2,nonUniqueGeneralRatio='2<d/a<=3')
put(20,intensityRatios=[sinc2(pi*m/3) for m in range(1,5)],missingOrderMultiple=3,centralBrightOrders=[-2,-1,0,1,2])
lam=580e-9;d=.530e-3;a=.320e-3
put(21,anglesDeg=[deg(asin(m*lam/d)) for m in [1,2]],intensityRatios=[sinc2(pi*m*a/d) for m in [1,2]])
d=500e-9*.90/.010
widths=[d/3,2*d/3]
for a in widths:
 assert abs(sin(pi*3*a/d))<1e-14
 assert all(abs(sin(pi*m*a/d))>1e-8 for m in [1,2])
put(22,slitSeparationUm=d*1e6,possibleNonoverlappingSlitWidthsUm=[a*1e6 for a in widths],selectionCondition='First single-slit minimum selects15um; condition is not explicit in prompt.')
put(23,widthsMm=[9/3,2*9/3])
cases=[]
for j in range(1,5):
 a_over_d=j/5
 assert abs(sin(pi*5*a_over_d))<1e-14
 assert all(abs(sin(pi*m*a_over_d))>1e-8 for m in range(1,5))
 ratio=sinc2(pi*a_over_d)/sinc2(2*pi*a_over_d)
 assert math.isclose(ratio,1/cos(pi*a_over_d)**2,rel_tol=1e-14)
 cases.append(dict(q=j,widthRatio=a_over_d,intensityRatio=ratio))
put(24,models=cases,sourceIntendedFirstMinimumRatio=cases[0]['intensityRatio'])
lam=632.8e-9;sn=sin(rad(17.8));d=lam/sn
put(25,linesPerCm=1/d/100,extraSpotCount=4,extraPositiveAnglesDeg=[deg(asin(m*sn)) for m in [2,3]])
put(26,fourthAngleDeg=deg(asin(4*sin(rad(11.3)))))
lam=550e-9;sn=sin(rad(66.6));d=4*lam/sn;a=3*lam/sn
put(27,separationUm=d*1e6,linesPerMm=1/d/1e3,widthUm=a*1e6)
put(28,violetSecondDeg=deg(asin(2*400/2100*sin(rad(65)))))
mean=(430.790+430.774)/2;delta=430.790-430.774;R=mean/delta
put(29,minResolvingPower=R,minOrder=math.ceil(R/12800))
d=1/(350e3);values={}
for m in [1,3]:
 lo=deg(asin(m*380e-9/d));hi=deg(asin(m*750e-9/d));values[str(m)]=dict(violetDeg=lo,redDeg=hi,widthDeg=hi-lo)
put(30,orders=values)
d=1/(5000*100);lam=d*sin(rad(13.5));put(31,wavelengthNm=lam*1e9,secondAngleDeg=deg(asin(2*lam/d)))
assert len(r)==14
(q/'exercises-18-31-data-checks.json').write_text(json.dumps(dict(status='passed',numberedExercises=14,results=r),indent=2),encoding='utf-8')
print(json.dumps(r,indent=2))
