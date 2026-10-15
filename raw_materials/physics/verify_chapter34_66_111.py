"""Compute problems66–111; retain all source data and identify inconsistent wording."""
from pathlib import Path
import json,math
import numpy as np
import pymupdf as fitz

root=Path(__file__).resolve().parents[2]
q=root/'qa/physics/chapter34';q.mkdir(parents=True,exist_ok=True)
r={};nw=1.333
def put(n,**kw):r[str(n)]={'status':'passed',**kw}
def image(f,s):
 sp=1/(1/f-1/s);m=-sp/s
 assert math.isclose(1/s+1/sp,1/f,rel_tol=1e-12,abs_tol=1e-12)
 return sp,m
def pair(f1,f2,s,L,h):
 a,m1=image(f1,s);s2=L-a;b,m2=image(f2,s2)
 return {'firstImageDistanceCm':a,'firstImageHeightMm':m1*h,'secondObjectDistanceCm':s2,'finalImageDistanceFromSecondCm':b,'finalXCm':L+b,'magnification':m1*m2,'finalHeightMm':m1*m2*h}
put(66,objectDistanceOverR=.3,imageDistanceOverR=-.75,magnification=2.5)
sp=8.;m=-240/6;s=-sp/m;f=1/(1/s+1/sp);put(67,objectDistanceM=s,radiusM=2*f)
M=3.5;gap=3.;s=gap/(M-1);sp=M*s;put(68,objectDistanceM=s,mirrorWallDistanceM=sp,radiusM=2/(1/s+1/sp))
s=2.;f=-.75;sp,m=image(f,s);s_dot=-1.9*(s/sp)**2
put(69,imageDistanceM=sp,relativeTruckVelocityMps=s_dot,highwayTruckSpeedMps=25-s_dot)
put(70,apparentDepthCm=4.20/1.50+5.70/1.33)
sp,m=image(-9.,900.);put(71,imageDistanceCm=sp,magnification=m,imageHeightCm=150*m)
sp,m=image(18.,10.);put(72,lensType='converging',frontFocusGridSquares=9,objectLensGridSquares=5,horizontalCmPerSquare=2,focalLengthCm=18,objectDistanceCm=10,imageDistanceCm=sp,magnification=m,verticalScaleNotPhysical=True)
put(73,magnification=-20/150,imageHeightCm=-20/150*18)
a,m1=image(8.4,28.);s2=8-a;m2=-5.6/4/m1;b=-m2*s2;f2=1/(1/s2+1/b)
put(74,firstImageDistanceCm=a,secondObjectDistanceCm=s2,secondImageDistanceCm=b,secondFocalLengthCm=f2,objectFinalImageSeparationCm=28+8+b)
put(75,index=2.)
for x in np.linspace(0,2,101):
 m=nw/(nw-(nw-1)*x)
 assert m>=1 and np.isfinite(m)
mb=nw/(2-nw);put(76,magnificationFormula='n/(n-(n-1)s/|R|)',backMagnification=mb,indexFromBackMagnification=2*mb/(mb+1),requiresUserEstimate=True,thinWallApproximation=True)
put(77,realImage={'lens':'converging','objectDistanceCm':52.5,'imageDistanceCm':105.,'magnification':-2},virtualImage={'lens':'converging','objectDistanceCm':17.5,'imageDistanceCm':-35.,'magnification':2})
# Autocollimation: the offset screen selects the collimated solution rather than
# a mirror precisely at a finite intermediate image which returns to the object.
a,b=22.,38.
P=lambda d:np.array([[1.,d],[0.,1.]])
L=lambda f:np.array([[1.,0.],[-1/f,1.]])
for f in [a,a*b/(a+b)]:
 matrix=P(a)@L(f)@P(2*b)@L(f)@P(a)
 assert abs(matrix[0,1])<1e-10
response1=(P(a)@L(a)@P(b))[0,1]
response2=(P(a)@L(a*b/(a+b))@P(b))[0,1]
assert math.isclose(response1,22.) and abs(response2)<1e-10
put(78,focalLengthCm=22,mirrorCoordinateCm=60,lensCoordinateCm=22,tiltedMirrorAdjacentScreenSelectsCollimatedCase=True,finiteConjugateDegeneracyFcm=a*b/(a+b))
m=5/3;s=214/(1+m);sp=m*s;put(79,focalLengthCm=1/(1/s+1/sp),objectDistanceCm=s,imageDistanceCm=sp,magnification=-m)
for n,s,sp,h in [(80,8.,-3.,6.5),(81,16.,-22.,3.25)]:
 f=1/(1/s+1/sp);m=-sp/s;put(n,objectDistanceCm=s,imageDistanceCm=sp,focalLengthCm=f,magnification=m,imageHeightMm=m*h)
n=15/8.2;sp=1/((1-n)/(-10)-n/15);put(82,index=n,curvedApparentDepthCm=-sp,imageDistanceCm=sp)
n=1.35;d=2.5;R=(n-1)*d/n;sp_near=n/((n-1)/R-1/25);sp_actual=n*.5/(n-1)
put(83,requiredRadiusMm=10*R,nearTextImageDistanceMm=10*sp_near,actualCorneaMountainFocusMm=10*sp_actual,retinaMm=25.,actualFocusBeforeRetina=True,positiveLensPlacedBeforeFirstFocusCannotMoveFocusToMoreDistantRetina=True)
f=1/(.6*(1/12-1/28));put(84,focalLengthCm=f,partA=pair(f,f,45.,315.,5.),partB=pair(f,f,45.,315.,5.),partC=pair(f,f,45.,45.,5.))
# Quinoline display: s is downward distance from top, s' is upward image height.
n=1.627;power=(n-1)/2.5
object_for=lambda sp:n/(power-1/sp)
lo,hi=object_for(100),object_for(50);mid=(lo+hi)/2;amp=(hi-lo)/2
spmid=1/(power-n/mid);dspds=-n/(power*mid-n)**2
sdot=-2*math.pi*amp;image_velocity_cmps=dspds*sdot
assert image_velocity_cmps>0
put(85,minimumHeightLimitCm=n/power,objectDistanceMinCm=lo,objectDistanceMaxCm=hi,objectMidpointCm=mid,amplitudeCm=amp,imageAtObjectMidpointCm=spmid,imageVelocityMps=image_velocity_cmps/100,imageDirectionForUpwardObject='upward',maximumImageDiameterCm=power*100-1,printedSinusoidNeedsMeanOffset=True,sourceAppendixDirectionInconsistent=True)
D=22.;f=3.;roots=np.roots([1,-D,f*D]);put(86,lensObjectDistancesCm=sorted(roots.tolist()),magnifications=[-(D-x)/x for x in sorted(roots)])
sp=-.83;s=1/(2.25-1/sp);near_ordinary=s+.02;near_contact=1/(2.25+1/.85)
put(87,ordinaryNearPointCm=near_ordinary*100,contactNearPointCm=near_contact*100)
put(88,minimumObjectScreenDistanceOverF=4.)
sp,m=image(32.,85.);put(89,directImageDistanceFromLensCm=sp,directMagnification=m,reflectedImageDistanceFromLensCm=sp,reflectedTotalMagnification=-m,bothImagesReal=True)
glass_power=(1.55-1)*(1/4.5-1/9);liquid_power=(1.46-1)/9
put(90,totalPowerRule='1/f=1/f1+1/f2',glassFocalLengthCm=1/glass_power,liquidFocalLengthCm=1/liquid_power,combinationFocalLengthCm=1/(glass_power+liquid_power))
s=-15.;sp=30+19.2-15.;put(91,divergingFocalLengthCm=1/(1/s+1/sp),virtualObjectDistanceCm=s,newImageDistanceCm=sp)
put(92,liquidLensmakerFactor='(n_glass/n_liquid-1)',immersedFocalLengthCm=18*(1.60-1)/(1.60/1.42-1))
ims=[]
for s in [10.,30.]:
 sp,m=image(-24.,s);ims.append({'objectDistanceFromSphericalCm':s,'imageXCm':sp,'heightCm':m*.250,'magnification':m})
put(93,twoClosestImages=ims)
cell=5e-6;near=.25;retina=.025;small=cell*near/retina;angle=small/near
put(94,cellDiameterMicrometers=5,minimumObjectSizeM=small,angleRad=angle,angleArcminutes=math.degrees(angle)*60,sourceOCRMillimeterIsMicrometer=True)
positions=[0.,52.,104.];prev_x=-80.;steps=[]
for x in positions:
 s=x-prev_x;sp,m=image(40.,s);prev_x=x+sp;steps.append({'lensXCm':x,'objectDistanceCm':s,'imageDistanceCm':sp,'imageXCm':prev_x,'magnification':m})
put(95,steps=steps,finalXCm=prev_x,imageDistanceLeftOfOriginalObjectCm=-80-prev_x)
near_sp,_=image(90.,1300.);far_sp,_=image(90.,6500.)
put(96,nearSensorDistanceMm=near_sp,farSensorDistanceMm=far_sp,changeMm=far_sp-near_sp,direction='toward sensor')
put(97,powerDiopters=1/.24,contactFocalLengthM=.24)
sp=1.4/(.4/.75-1/36);put(98,retinaDistanceCm=sp,referenceRetinaDistanceCm=2.6,longerModelEye=True)
for f1,magf2,d in [(12.,18.,0.),(12.,18.,4.),(15.,20.,3.)]:
 denom=magf2-f1+d;sp=magf2*(f1-d)/denom
 assert math.isclose(1/(d-f1)+1/sp,-1/magf2)
 eff=f1*magf2/denom
 assert math.isclose(eff,sp*f1/(f1-d))
put(99,maxFocalLengthCm=36,minFocalLengthCm=21.6,separationFor30Cm=1.2,effectiveFormula='f1*|f2|/(|f2|-f1+d)')
put(100,eyepieceFocalLengthCm=-15.,angularMagnification=95/15,galileanLengthCm=80.,keplerLengthCm=110.)
results=[]
for separation,final in [(20.,42.8),(25.,31.6)]:
 s2=separation-29.7;sp2=final-separation;f2=1/(1/s2+1/sp2);m=-29.7/20*(-sp2/s2)
 results.append({'separationCm':separation,'secondObjectDistanceCm':s2,'secondImageDistanceCm':sp2,'focalLengthCm':f2,'magnification':m})
put(101,measurements=results,meanDivergingFocalLengthCm=float(np.mean([x['focalLengthCm'] for x in results])),tallestImageAtSeparationCm=20.)
# Use all five actual vector markers in the original magnification graph.
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 markers=[]
 for d in pdf[1176].get_drawings():
  b=d['rect']
  if d.get('fill') and 220<b.x0<305 and 350<b.y0<415 and 3.99<b.width<4.01 and 3.99<b.height<4.01:
   markers.append(((b.x0+b.x1)/2,(b.y0+b.y1)/2))
markers.sort();assert len(markers)==5
x102=np.array([(x-303.4415)/((303.4415-224.298)/2) for x,y in markers])
y102=np.array([(415.49301-y)/.6 for x,y in markers])
slope,intercept=np.polyfit(x102,y102,1)
assert abs(intercept-25)<.3 and abs(slope+25)<.3
put(102,allFiveSourcePoints={'inverseMagnification':x102.tolist(),'objectDistanceCm':y102.tolist()},fitInterceptCm=float(intercept),fitSlopeCm=float(slope),reportedFocalLengthCm=25.,objectFor8mmImageCm=37.5,objectFor12mmImageCm=25*(1+1/3),moveCloserCm=37.5-25*(1+1/3),at25ImageAtInfinity=True)
s=np.array([22.5,25,30,35,40,45.]);sp=np.array([271.6,148.3,89.4,71.1,60.8,53.2]);x=1/s;y=1/sp
beta,alpha=np.polyfit(x,y,1);n=-1/beta;R=(n-1)/(n*alpha)
newsp=n/((n-1)/R-1/15.)
put(103,objectDistancesCm=s.tolist(),imageDistancesCm=sp.tolist(),fitSlope=float(beta),fitInterceptPerCm=float(alpha),glassIndex=float(n),radiusCm=float(R),imageForObject15Cm=float(newsp),allSixPointsUsed=True,fitMethod='unweighted linear least squares in inverse distances')
# Parabolic mirror: exact vector reflection independently checks trigproof.
checks=0
for a in [.02,.1,1.,2.]:
 for radial in np.linspace(.01,20.,100):
  normal=np.array([-2*a*radial,1.]);normal/=np.linalg.norm(normal)
  inc=np.array([0.,-1.]);out=inc-2*np.dot(inc,normal)*normal
  t=-radial/out[0];focus_y=a*radial**2+t*out[1]
  assert math.isclose(focus_y,1/(4*a),rel_tol=1e-10,abs_tol=1e-10)
  phi=math.atan(2*a*radial);angle=2*phi-math.pi/2;b=radial*math.tan(angle)
  assert math.isclose(a*radial**2-b,1/(4*a),rel_tol=1e-10,abs_tol=1e-10)
  checks+=1
put(104,focalLengthFormula='1/(4a)',slope='2ar',normalSlope='-1/(2ar)',phi='atan(2ar)',alpha='2phi-pi/2',b='ar^2-1/(4a)',exactReflectionCases=checks)
u=np.linspace(1.001,10,100000);D=u*u/(u-1)
assert D.min()>=4 and abs(u[np.argmin(D)]-2)<.001
put(105,minimumObjectImageDistanceOverF=4.,objectAtMinimumOverF=2.,domain='real object and real image: f>0,s>f',normalizedDistanceFormula='u^2/(u-1)')
delta=8/math.sqrt(2);points={}
for name,s,y in [('A',45+delta,15-delta),('B',45-delta,15+delta),('C',45.,15.)]:
 sp,m=image(20.,s);yp=m*y;assert math.isclose(yp,60-2*sp,abs_tol=1e-11)
 points[name]={'objectDistanceCm':s,'objectHeightCm':y,'imageDistanceCm':sp,'imageHeightCm':yp}
length=math.hypot(points['B']['imageDistanceCm']-points['A']['imageDistanceCm'],points['B']['imageHeightCm']-points['A']['imageHeightCm'])
put(106,points=points,imageLengthCm=length,imageTiltDeg=-math.degrees(math.atan(2)),imageLine='yprime=60-2*xprime')
n_eye=1.4;retina=2.6;R_cornea=.4/(1/40+1.4/retina)
s_eye=nw/((n_eye-nw)/R_cornea-n_eye/retina);f_water=2+abs(s_eye)
f_air=f_water*(1.62/nw-1)/(1.62-1)
put(107,corneaRadiusFromExercise52Cm=R_cornea,corneaVirtualObjectDistanceCm=s_eye,underwaterLensFocalLengthCm=f_water,airLensFocalLengthCm=f_air,waterIndex=nw,lensIndex=1.62)
f=1/(1/10+1/.8);newsp=1/(1/f-1/15)
put(108,choice='a',frogLensFocalLengthCm=f,newLensRetinaSeparationCm=newsp,moveTowardRetinaCm=.8-newsp)
put(109,choice='d',farPointCm=100/6)
put(110,choice='b',reason='water reduces corneal convergence')
for s in [.1,.3,1.]:assert abs(1/(-15-1/s))<abs(1/(-9-1/s))
put(111,choice='b',strongerNegativeLensGivesCloserVirtualObject=True)
assert set(r)=={str(i) for i in range(66,112)}
(q/'exercises-66-111-data-checks.json').write_text(json.dumps({'status':'passed','numberedExercises':46,'results':r},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(r,ensure_ascii=False,indent=2))
