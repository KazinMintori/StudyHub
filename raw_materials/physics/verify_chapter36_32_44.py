"""Compute grating, Bragg and angular-resolution exercises36.32–36.44."""
from pathlib import Path
import math,json
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter36';q.mkdir(parents=True,exist_ok=True)
sin=math.sin;asin=math.asin;tan=math.tan;atan=math.atan;pi=math.pi;deg=math.degrees;rad=math.radians
r={}
def put(i,**data):r[str(i)]=data
lam=632.8e-9
put(32,cdAnglesDeg=[0,*[deg(asin(m*lam/1.60e-6)) for m in [1,2]]],dvdAnglesDeg=[0,deg(asin(lam/.740e-6))])
l1=656.45e-9;l2=656.27e-9;N=math.ceil((l1+l2)/2/(2*(l1-l2)));d=1/(500e3);angles=[deg(asin(2*lam/d)) for lam in [l1,l2]]
assert N*2>=(l1+l2)/2/(l1-l2) and (N-1)*2<(l1+l2)/2/(l1-l2)
put(33,minSlits=N,anglesDeg=angles,separationDeg=abs(angles[0]-angles[1]))
d=3.5e-10;lam=2*d*sin(rad(22));maxm=math.floor(2*d/lam)
put(34,wavelengthNm=lam*1e9,band='x rays',otherAnglesDeg=[deg(asin(m*lam/(2*d))) for m in range(2,maxm+1)])
put(35,planeSpacingNm=2*.0850/(2*sin(rad(21.5))))
put(36,wavelengthNm=2*.440*sin(rad(39.4)))
D=7.4e-6;lam=620e-9;R=4.5;theta=asin(1.22*lam/D)
put(37,apertureMicrometers=7.4,airyDiameterM=2*R*tan(theta),smallAngleDiameterM=2*R*1.22*lam/D)
lam=490e-9;R=1.2;delta=.00165
def gap(D):return R*(tan(asin(2.23*lam/D))-tan(asin(1.22*lam/D)))
lo=2.23*lam*(1+1e-8);hi=1.
for _ in range(100):
 mid=(lo+hi)/2
 if gap(mid)>delta:lo=mid
 else:hi=mid
D=(lo+hi)/2;assert math.isclose(gap(D),delta,rel_tol=1e-12)
put(38,apertureMm=D*1e3,smallAngleApertureMm=(2.23-1.22)*lam*R/delta*1e3)
put(39,minDishM=1.22*.036/sin(atan(28/1200)),model='Range1200km and projected transverse separation28km, near overhead.')
put(40,effectiveApertureMm=1.22*550e-9/sin(rad(1/60))*1e3)
put(41,visibleTelescopeDiameterM=8e6*550e-9/.020)
f=.135;R=11.5;lam=550e-9
put(42,minFeaturesMm=[R*tan(asin(1.22*lam/(f/N)))*1e3 for N in [4.,22.]])
moon_distance=3.84e8;hubble_lam=380e-9;hubble_D=2.4;theta_h=asin(1.22*hubble_lam/hubble_D);theta_a=asin(1.22*.75/305)
put(43,moonDistanceM=moon_distance,hubbleCraterM=moon_distance*tan(theta_h),areciboCraterKm=moon_distance*tan(theta_a)/1e3,minResolutionRad=theta_h,plateHeightAssumedM=.15,plateWidthAssumedM=.30,orbitUsingPlateHeightM=.15/tan(theta_h),orbitUsingPlateWidthM=.30/tan(theta_h),qualification='Plate dimensions and selected detail not supplied. Distinguish assumed sizes and use shortest380nm for optimal visible diffraction limit. Arecibo is a historical problem model, not a claim about present operation.')
put(44,minMirrorM=1.22*500e-9/sin(atan(250/5.93e8)))
assert len(r)==13
(q/'exercises-32-44-data-checks.json').write_text(json.dumps(dict(status='passed',numberedExercises=13,results=r),indent=2),encoding='utf-8')
print(json.dumps(r,indent=2))
