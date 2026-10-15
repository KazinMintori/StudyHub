"""Calculations and independent sequential-lens checks for exercises40–65."""
from pathlib import Path
import json,math
import numpy as np

root=Path(__file__).resolve().parents[2]
r={}
def put(n,**kw):r[str(n)]={'status':'passed',**kw}
def image(f,s):
 sp=1/(1/f-1/s);m=-sp/s
 assert math.isclose(1/s+1/sp,1/f,rel_tol=1e-12)
 return sp,m
def pair(f1,f2,s1,L,h):
 sp1,m1=image(f1,s1);s2=L-sp1;sp2,m2=image(f2,s2);X=L+sp2
 # Independent ray-transfer intersection for two arbitrary object rays.
 P=lambda d:np.array([[1.,d],[0.,1.]])
 lens=lambda f:np.array([[1.,0.],[-1/f,1.]])
 matrix=lens(f2)@P(L)@lens(f1)@P(s1)
 found=-matrix[0,1]/matrix[1,1]
 assert math.isclose(found,sp2,rel_tol=1e-12)
 final=P(sp2)@matrix
 assert abs(final[0,1])<1e-12
 assert math.isclose(final[0,0],m1*m2,rel_tol=1e-12)
 return {'firstImageDistance':sp1,'firstMagnification':m1,'firstImageHeight':m1*h,'secondObjectDistance':s2,'secondImageDistance':sp2,'finalXFromFirstLens':X,'totalMagnification':m1*m2,'finalHeight':h*m1*m2,'finalImageReal':sp2>0}
for num,f in [(40,12.),(41,-48.)]:
 sp=-17.;s=1/(1/f-1/sp);m=-sp/s
 put(num,propagation='right-to-left;virtualimageonrightincoming-side',objectDistanceCm=s,imageDistanceCm=sp,magnification=m,objectHeightMm=8/m,objectAndImagePhysicalSide='right')
s=16.;sp=36.;f=1/(1/s+1/sp);put(42,focalLengthCm=f,imageDistanceCm=sp,imageHeightMm=-sp/s*8,magnification=-sp/s)
put(43,**pair(40.,60.,50.,300.,1.2))
put(44,cases=[pair(40.,-60.,50.,300.,1.2),pair(-40.,60.,50.,300.,1.2),pair(-40.,-60.,50.,300.,1.2)])
put(45,**pair(-12.,12.,20.,9.,2.5))
f=-25.;sp=-18.;s=1/(1/f-1/sp);put(46,objectDistanceCm=s,imageDistanceCm=sp,magnification=-sp/s)
sp,m=image(1.,2/3);put(47,imageDistanceOverF=sp,imageHeightOverObjectHeight=m)
L=260.;M=2.5;s=L/(M+1);sp=M*s;f=1/(1/s+1/sp);put(48,objectDistanceCm=s,imageDistanceCm=sp,focalLengthCm=f,magnification=-M)
sp,m=image(85.,3900.);put(49,lensSensorDistanceMm=sp,imageHeightMm=abs(m)*1750,portrait36mmDimensionFits=abs(m)*1750<=36,landscape24mmDimensionFits=abs(m)*1750<=24)
s=150.;sp=9000.;f=1/(1/s+1/sp);mag=sp/s;put(50,focalLengthMm=f,screenMinimumDimensionsMm=[24*mag,36*mag],magnification=-mag)
zoom=[]
for L in [4.,8.]:
 sp1=12.;s2=L-sp1;sp2,m=image(-12.,s2);zoom.append({'separationCm':L,'firstImageXCm':sp1,'secondObjectDistanceCm':s2,'secondImageDistanceCm':sp2,'finalXCm':L+sp2})
put(51,cases=zoom)
put(52,corneaRadiusCm=.4/(1/40+1.4/2.6),modelIndex=1.4,retinaDistanceCm=2.6)
put(53,nearPointCm=100/(4-2.75),farPointCm=100/1.30,referenceReadingDistanceCm=25.)
s=.25;sp=-.45;power=1/s+1/sp;put(54,focalLengthM=1/power,powerDiopters=power,type='converging',condition='hyperopic-nearpointmodel')
s=.25-.02;sp=-(.45-.02);power=1/s+1/sp;put(55,focalLengthM=1/power,powerDiopters=power,objectLensDistanceM=s,imageLensDistanceM=sp)
put(56,focalLengthM=-.75,powerDiopters=-1/.75,type='diverging',condition='myopia')
fupper=-2.;flower=.5;eyeOffset=.02;nearSp=1/(1/flower-1/(.25-eyeOffset));nearFromEye=abs(nearSp)+eyeOffset
upperClosest=1/(1/fupper-1/nearSp)+eyeOffset
put(57,farPointM=abs(fupper)+eyeOffset,nearPointM=nearFromEye,closestThroughUpperM=upperClosest,nearVirtualImageLensCoordinateM=nearSp)
put(58,relaxedAngularMagnification=25/6,closestObjectDistanceCm=1/(1/6+1/25))
s=1/(1/8+1/25);m=25/s;put(59,objectDistanceCm=s,magnification=m,imageHeightMm=m)
put(60,focalLengthM=.002/.032)
fo=.95;fe=.15;H=60.;S=3000.;put(61,angularMagnification=-fo/fe,objectiveImageHeightM=-fo*H/S,finalAngularSizeRad=abs(fo/fe)*H/S,model='distant-object-paraxial')
put(62,objectiveFocalLengthM=1.20-.09,angularMagnification=-(1.20-.09)/.09)
fo=1.30/2;fe=.011;put(63,mirrorEyepieceDistanceM=fo+fe,angularMagnification=-fo/fe)
f1=14.;s1=16.;sp1,m1=image(f1,s1);f2=20.;M2=250/f2;M=m1*M2;Mapprox=-sp1/f1*M2
put(64,firstImageDistanceMm=sp1,lensSeparationMm=sp1+f2,objectiveMagnification=m1,totalAngularMagnification=M,approxAngularMagnification=Mapprox,relativeApproximationErrorPercent=100*abs(Mapprox-M)/abs(M))
M=-178.;f2=15.;L=202.;M2=250/f2;m1=M/M2;sp1=L-f2;s1=-sp1/m1;f1=1/(1/s1+1/sp1)
put(65,objectiveFocalLengthMm=f1,objectiveObjectDistanceMm=s1,firstImageDistanceMm=sp1,objectiveMagnification=m1)
assert set(r)=={str(i) for i in range(40,66)}
q=root/'qa/physics/chapter34';q.mkdir(parents=True,exist_ok=True)
(q/'exercises-40-65-data-checks.json').write_text(json.dumps({'status':'passed','numberedExercises':26,'results':r},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(r,ensure_ascii=False,indent=2))
