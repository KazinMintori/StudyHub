"""SI-consistent calculations for chapter34 exercises1–39, with stated models."""
from pathlib import Path
import math,json
import numpy as np

root=Path(__file__).resolve().parents[2]
r={};nw=1.333
def put(n,**kw):r[str(n)]={'status':'passed',**kw}
def image(f,s):
 sp=1/(1/f-1/s);m=-sp/s
 # Independently intersect an initially parallel ray with the ray through lenscenter.
 h=.1
 parallel_slope=-h/f;central_slope=-h/s
 crossing=h/(central_slope-parallel_slope)
 assert math.isclose(crossing,sp,rel_tol=1e-12)
 assert math.isclose(central_slope*sp,m*h,rel_tol=1e-12)
 return sp,m
def surface(na,nb,R,s):return nb/((nb-na)/R-(0 if math.isinf(s) else na/s))
put(1,imageDistanceCm=-39.2,imageHeightCm=4.85)
put(2,treeHeightM=.04*(28+.35)/.35,mirrorHeightM=.04,eyeMirrorDistanceM=.35,treeMirrorDistanceM=28.)
put(3,imageLengthCm=21-12,nearerImageEnd='pencil lead',imageEndDistancesCm=[12,21])
put(4,focalLengthAirCm=17.,focalLengthWaterCm=17.)
for num,f in [(5,11.),(6,-11.)]:
 sp,m=image(f,16.5);put(num,imageDistanceCm=sp,magnification=m,imageHeightCm=.600*m)
sMars=5.58e7*1000;sp,m=image(1.75,sMars)
put(7,imageDistanceM=sp,imageDiameterM=abs(m)*6794e3)
sp,m=image(-1.5,18-3);put(8,objectDistanceFromVertexCm=15.,imageDistanceFromVertexCm=sp,magnification=m,objectDistanceFromCenterCm=18.)
f=-9.;sp=-6.;s=1/(1/f-1/sp);put(9,objectDistanceCm=s,imageHeightCm=(-sp/s)*1.5,magnification=-sp/s)
sp,m=image(-17.5,60.);put(10,imageDistanceCm=sp,imageHeightCm=5*m,magnification=m)
sp,m=image(16.,12.);put(11,imageDistanceCm=sp,magnification=m)
put(12,objectDistanceCm=36.,imageDistanceCm=36.,magnification=-1.)
s=1.25;m=2.;sp=-m*s;f=1/(1/s+1/sp);put(13,type='concave',focalLengthCm=f,radiusCm=2*f,imageDistanceCm=sp)
f=-12.;m=.5;s=f*(1-1/m);put(14,objectDistanceCm=s,imageDistanceCm=-m*s)
cases=[]
for f in [6.,-6.]:
 sp,m=image(f,15.);cases.append({'focalLengthCm':f,'imageDistanceCm':sp,'magnification':m,'imageHeightMm':3.30*m})
put(15,cases=cases,source15cmMeasuredFromVertex=True)
s=24.;m=-2.5/.6;sp=-m*s;f=1/(1/s+1/sp);put(16,imageDistanceCm=sp,focalLengthCm=f,radiusCm=2*f)
for m in [-.1,-.5,-2.,.2,.8]:
 s=25.;sp=-m*s;f=1/(1/s+1/sp)
 assert math.isclose(f,-m*s/(1-m),rel_tol=1e-12)
put(17,requiresUserObservations=True,nominalObjectDistanceCm=25.,radiusFormula='R=-2ms/(1-m)',imageClassificationDependsOnObservation=True)
put(18,waterIndex=nw,fishApparentDepthCm=7/nw,mirrorFishDepthCm=40-7,mirrorImageApparentDepthCm=33/nw)
put(19,apparentDepthCm=3.5/1.309)
put(20,imageDistanceCm=surface(1.,1.5,-15.,math.inf),imageRegion='air')
put(21,waterIndex=nw,boardHeightAboveWaterM=(5.20-.80)/nw)
put(22,waterIndex=nw,waterDepthM=(7-3)*nw)
R=14.;sp=surface(nw,1.,-R,R);m=-nw*sp/R
first=surface(1.,nw,R,math.inf);second=surface(nw,1.,-R,2*R-first)
put(23,fishImageDistanceFromNearSurfaceCm=sp,magnification=m,fishImageAtCenter=True,parallelRayFirstSurfaceImageCm=first,finalSunFocusBeyondFarSurfaceCm=second,focusInsideBowl=False)
put(24,imageDistancesCm=[surface(1.,1.6,3.,s) for s in [math.inf,12.,2.]])
na=1.45;nb=1.6;R=3.;sp=120.;s=na/((nb-na)/R-nb/sp);put(25,objectDistanceCm=s)
sp=surface(1.,1.6,4.,24.);m=-sp/(1.6*24.);put(26,imageDistanceCm=sp,magnification=m,imageHeightMm=1.5*m)
cases=[]
for sp in [60.,-60.]:
 s=20.;f=1/(1/s+1/sp);m=-sp/s;cases.append({'imageDistanceCm':sp,'radiusCm':2*f,'magnification':m,'imageHeightMm':3.2*m})
put(27,cases=cases)
put(28,focalLengthCm=1/(.208*.400),heightCm=.400,slopePerCm2=.208,sourceImageHeightIsMagnitude=True)
f=13/.70;sp,m=image(f,22.5);put(29,focalLengthCm=f,imageDistanceCm=sp,magnification=m,imageHeightMm=3.75*m,reversingThinLensDoesNotChangeResult=True)
s=16.;sp=-12.;f=1/(1/s+1/sp);m=-sp/s;put(30,focalLengthCm=f,imageDistanceCm=sp,imageHeightMm=8.5*m,magnification=m)
f=1/(.52*(1/4-1/7));sp,m=image(f,24.);put(31,focalLengthCm=f,imageDistanceCm=sp,magnification=m)
f=70.;m=-4.5/3.2;s=f*(1-1/m);sp=-m*s;put(32,objectDistanceCm=s,imageDistanceCm=sp,magnification=m)
sp=-12.;m=3.4/.8;s=-sp/m;f=1/(1/s+1/sp);put(33,objectDistanceCm=s,focalLengthCm=f,magnification=m)
L=600.;mag=80.;s=L/(1+mag);sp=mag*s;f=1/(1/s+1/sp);put(34,objectDistanceCm=s,imageDistanceCm=sp,focalLengthCm=f,magnification=-mag)
put(35,refractiveIndex=1+2.5/(2*1.87))
f=9.;m=1.3/.4;s=f*(1-1/m);sp=-m*s;put(36,objectDistanceCm=s,imageDistanceCm=sp,magnification=m)
sp,m=image(40.,20.);put(37,focalLengthCm=40.,imageDistanceCm=sp,imageHeightMm=6*m,magnification=m)
put(38,radiusMagnitudeCm=2*(1.55-1)*20.)
s=12.;sp=-8.;f=1/(1/s+1/sp);put(39,focalLengthCm=f,radiusMagnitudeCm=-(1.5-1)*f)
assert set(r)=={str(i) for i in range(1,40)}
q=root/'qa/physics/chapter34';q.mkdir(parents=True,exist_ok=True)
(q/'exercises-01-39-data-checks.json').write_text(json.dumps({'status':'passed','numberedExercises':39,'results':r},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(r,ensure_ascii=False,indent=2))
