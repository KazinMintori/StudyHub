"""Exercises1–17 from visually checked source units, with explicit farfield domains."""
from pathlib import Path
import json,math
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter35';q.mkdir(parents=True,exist_ok=True);r={}
def put(i,**kw):r[str(i)]=kw
c=3e8
lam=c/120e6;L=9.;positions=[]
for m in range(-20,21):
 x=(L-m*lam)/2
 if 0<x<L:positions.append(x)
put(1,wavelengthM=lam,constructivePositionsM=sorted(positions))
put(2,longestDestructiveWavelengthM=240.,longestConstructiveWavelengthM=120.)
put(3,initialPathDifferenceM=math.hypot(6,8)-8,initialType='constructive',newPathDifferenceM=math.hypot(6,17)-17,newType='near-destructive-not-exact',exactFirstDestructiveObserverDistanceM=17.5)
# PDF1199actualunit ismicrometer, notOCRmm.
delta=2040.
maxima=[delta/m for m in range(1,20) if 380<=delta/m<=750]
minima=[delta/(m+.5) for m in range(20) if 380<=delta/(m+.5)<=750]
put(4,pathDifferenceMicrometers=2.04,constructiveNm=maxima,destructiveNm=minima,nonCollinearSamePathDifferenceUnchanged=True,extraAssumptionNeededForNumericAnswer='sources in phase;coherencealone does notspecifyrelativephase')
L=40;lam=7;ps=[(L-m*lam)/2 for m in range(-20,21) if 0<(L-m*lam)/2<L]
put(5,constructivePoints=len(ps),firstPositionM=min(ps),allPositionsM=sorted(ps))
lam=500e-9;R=2.;dy=.0353;d=lam*R/dy
def ym(m):
 u=m*lam/d;assert abs(u)<1
 return R*u/math.sqrt(1-u*u)
put(6,spacingM=d,position49M=ym(49),position50M=ym(50),outerFringeSeparationM=ym(50)-ym(49),centralSmallAngleApproximation=True)
put(7,slitSpacingMm=20*502e-9*1.20/.0106*1e3)
put(8,slitSpacingMm=450e-9*1.80/.00390*1e3)
put(9,adjacentDarkSpacingMm=500e-9*.750/.450e-3*1e3)
f1=5.60e12;f2=7.47e12;d=c/((f2-f1)*math.sin(math.radians(60)))
put(10,slitSpacingMicrometers=d*1e6,fringeOrderRatio=f1/(f2-f1),roundedInputFrequencies=True)
d=.0116e-3;lam=585e-9;m=math.floor(d/lam)
put(11,maxOrder=m,totalBrightFringes=2*m+1,outerAngleDeg=math.degrees(math.asin(m*lam/d)))
put(12,centralWidthMm=400e-9*4/.200e-3*1e3,firstOrderWidthMm=400e-9*4/.200e-3*1e3,definition='width between adjacentdarkboundaries in smallangle model')
# PDF1200actualunit is1.80micrometers, consistentnon-smallanglehint.
d=1.80e-6;lam=550e-9;R=.350
y=lambda order:R*(order*lam/d)/math.sqrt(1-(order*lam/d)**2)
put(13,slitSpacingMicrometers=1.80,firstDarkPositionCm=y(.5)*100,secondDarkPositionCm=y(1.5)*100,darkSeparationCm=(y(1.5)-y(.5))*100)
put(14,firstBrightSeparationMm=(660e-9-470e-9)*4/.300e-3*1e3)
put(15,darkWavelengthNm=1200.,darkIndexConvention='firstminimum m=0 in(m+.5)lambda',samePathDifferenceNm=600.)
lam=c/6.32e14;R=.85;y3=.0311;d=3*lam*R/y3
put(16,slitSpacingMicrometers=d*1e6,thirdDarkDistanceCm=(2.5*lam*R/d)*100,exactAngularSlitSpacingMicrometers=(3*lam*math.hypot(R,y3)/y3)*1e6)
put(17,intensityRatio=math.cos(math.radians(60)/2)**2,pathDifferenceNm=480/6)
assert set(r)=={str(i) for i in range(1,18)}
(q/'exercises-01-17-data-checks.json').write_text(json.dumps({'status':'passed','numberedExercises':17,'results':r},indent=2),encoding='utf-8')
print(json.dumps(r,indent=2))
