"""Compute remaining exercises32–60, including full graph data and source-model ambiguities."""
from pathlib import Path
import json,math,cmath
import numpy as np
import pymupdf as fitz
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter35';q.mkdir(parents=True,exist_ok=True)
r={};c=3e8
def put(i,**kw):r[str(i)]=kw
#32: power is for the stated beam, 280 roundtrips.
I=1e5/1e-4;eps=8.8541878128e-12;E=math.sqrt(2*I/(eps*c));delta=2*math.pi*2*280*1e-18/(1064e-9)
put(32,intensityWm2=I,electricAmplitudeVm=E,phaseShiftRad=delta,minimumResultantFieldVm=E*delta,roundTrips=280)
put(33,plasticIndex=632.8e-9*3.25/(.225e-3*.00582))
put(34,newRingDiameterMm=.640/math.sqrt(1.33))
t=550/(4*1.432)
put(35,minCoatingThicknessNm=t,onlyCancelledVisibleNm=550,otherCancelledVisibleNm=[],enhancedVisibleNm=[])
put(36,minDropThicknessNm=600/(4*1.45),onCorneaConstructiveNm=[600],onCorneaDestructiveVisibleNm=[],onContactConstructiveVisibleNm=[],onContactDestructiveNm=[600])
firstx=.00115;tilt=(400e-9/4)/firstx
put(37,firstGreenMm=firstx*550/400*1e3,firstOrangeMm=firstx*600/400*1e3,secondVioletMm=3*firstx*1e3,secondGreenMm=3*firstx*550/400*1e3,secondOrangeMm=3*firstx*600/400*1e3,foilThicknessMicrometers=tilt*.110*1e6)
#38 use sourceTable16.1 air20C344m/s, exact path geometry to keep non-small angle.
speed=344.;freq=1000.;lam=speed/freq;d=.4;R=2.
y=lam/2*math.sqrt(1+4*R*R/(d*d-lam*lam))
design_freq=2000.;design_lam=speed/design_freq;target=1.75
design_d=design_lam*math.sqrt(1+R*R/(target*target-design_lam*design_lam/4))
assert math.isclose(math.hypot(R,target+design_d/2)-math.hypot(R,target-design_d/2),design_lam,rel_tol=1e-12)
put(38,lightSlitSpacingMicrometers=650e-9*1/.01*1e6,soundSpeedMps=speed,soundCentralToFirstMaximumM=y,soundSmallAngleEstimateM=lam*R/d,designFrequencyHz=design_freq,designSpeakerSeparationM=design_d,designFirstBrightDistanceM=target)
put(39,liquidIndex=math.sin(math.radians(35.20))/math.sin(math.radians(19.46)))
theta=math.radians(26.6);alpha=2e-5;DT=115.
shift=-alpha*DT*math.tan(theta)
exact=math.asin(math.sin(theta)/(1+alpha*DT))-theta
put(40,brassExpansionPerK=alpha,temperatureChangeK=DT,differentialShiftDeg=math.degrees(shift),exactShiftDeg=math.degrees(exact),moveCloser=True)
lam=c/5.80e6;points=[]
for m in range(20):
 path=(m+.5)*lam
 if path<200:
  x=(200**2-path**2)/(2*path)
  assert math.isclose(math.hypot(200,x)-x,path,rel_tol=1e-12)
  points.append({'order':m,'pathDifferenceM':path,'distanceM':x})
put(41,wavelengthM=lam,destructiveLocations=points)
#42: choosepositiveangle towardA (upper speaker in sourcefigure).
lam=340/444;angles=[]
for m in range(-20,21):
 sn=(m+.25)*lam/3.5
 if abs(sn)<=1:
  angle=math.degrees(math.asin(sn))
  # rB-rA = d sin(theta), A leads bypi/2.
  phi=math.pi/2+2*math.pi*3.5*sn/lam
  assert math.isclose(math.cos(phi),-1.,abs_tol=1e-12)
  angles.append(angle)
put(42,wavelengthM=lam,anglePositiveTowardA=angles)
put(43,linearExpansionPerK=(588.5/582.4-1)/150)
lam=c/1575.42e6;d=5.18;maxm=math.floor(d/lam)
put(44,wavelengthM=lam,otherPositiveMaxima=maxm,firstFourMaximaDeg=[math.degrees(math.asin(m*lam/d)) for m in range(1,5)],intensityAt4point65Deg=2*math.cos(math.pi*d*math.sin(math.radians(4.65))/lam)**2)
C=477*540.6/(540.6-477)
put(45,opticalRoundTripNm=C,thicknessMicrometers=C/(2*1.52)/1e3,orders=[7,8])
put(46,minNonzeroThicknessMaxTransmissionNm=510/(2*1.65),minThicknessMinTransmissionNm=510/(4*1.65))
put(47,otherVisibleWavelengthsNm=[2100/(m+.5) for m in range(20) if 380<=2100/(m+.5)<=750],needsSlitSpacing=False)
#48 independently compare reflection phases of five interfaces.
gu=1.80;cy=1.333;tg=74.;tc=100.;lam0=(4*gu*tg+4*cy*tc)/2
z=np.cumsum([0,gu*tg,cy*tc,gu*tg,cy*tc])
phases=[]
for j,opticaldepth in enumerate(z):
 refl_pi=math.pi if j%2==0 else 0.
 phases.append((4*math.pi*opticaldepth/lam0+refl_pi)%(2*math.pi))
qratio=gu/cy
R5=((qratio**10-1)/(qratio**10+1))**2
assert R5>.8
put(48,guanineQuarterWaveNm=4*gu*tg,cytoplasmQuarterWaveNm=4*cy*tc,approxMatchedWavelengthNm=lam0,allFiveReflectionPhasesRad=phases,dominantColor='green',idealQuarterWaveStack5HighLayersReflectance=R5)
ratio=1/(2*math.sin(math.radians(19)))
angle=math.asin(math.acos(math.sqrt(.1))/(math.pi*ratio))
put(49,spacingOverWavelength=ratio,first10PercentAngleDeg=math.degrees(angle))
#50: use all8actual vector markers. Originalpinkregression is also recorded.
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 markers=[]
 for dr in pdf[1202].get_drawings():
  b=dr['rect']
  if dr.get('fill') and 110<b.x0<250 and 230<b.y0<320 and 3.99<b.width<4.01 and 3.99<b.height<4.01:
   markers.append(((b.x0+b.x1)/2,(b.y0+b.y1)/2))
 assert len(markers)==8
markers.sort()
xs=np.array([(x-99.4977)/((275.8457-99.4977)/12) for x,y in markers])
ys=np.array([(323.8464-y)/((323.8464-230.1844)/6) for x,y in markers])
slope,intercept=np.polyfit(xs,ys,1)
pink_slope=((315.8591-239.3771)/((323.8464-230.1844)/6))/((246.4535-114.1935)/((275.8457-99.4977)/12))
put(50,allEightSourcePoints={'inverseSlitSpacingPerMm':xs.tolist(),'fringeSpacingMm':ys.tolist()},measuredPointFitSlopeMm2=float(slope),fitInterceptMm=float(intercept),wavelengthFromAllPointsNm=float(slope/900*1e6),sourceDrawnLineSlopeMm2=pink_slope,wavelengthFromDrawnLineNm=pink_slope/900*1e6,graphReadingPrecision='about600nm')
#51: ifmaximaareconsecutive, lambda6m. Withoutthisassumption,integerfamily.
put(51,consecutiveMaximaWavelengthM=6.,consecutiveMaximaFrequencyMHz=50.,greatestDestructiveXM=237.,nonConsecutiveFrequencyFamilyMHz='50k, kpositiveinteger',nonConsecutiveGreatestDestructiveXM='240-3/k')
Craw=496*386/(496-386);C=(3.5*496+4.5*386)/2
put(52,opticalRoundTripNm=C,glassThicknessNm=C/(2*1.40),longestConstructiveWavelengthNm=2*C,orderFromRoundedData=386/(496-386)-.5,rawDifferenceMethodOpticalRoundTripNm=Craw,individualRoundTripEstimatesNm=[3.5*496,4.5*386],roundedOrderEstimateUsed=True)
#53 explicit model distinctions, no forcedsemantic equivalence of pressure node and constructivephase.
def raypositions(lam,halfinteger):
 ps=[]
 for m in range(20):
  D=(m+.5)*lam if halfinteger else (m+1)*lam
  if D<=.5:
   x=(.5**2-D*D)/(2*D)
   assert math.isclose(math.hypot(x,.5)-x,D,abs_tol=1e-12)
   ps.append({'pathDifferenceM':D,'distanceM':x})
 return ps
put(53,airWavelengthM=344/2500,heliumWavelengthM=999/2500,
 constructiveThresholdRadiusOverLambda=.5,constructivePositiveAirLocations=raypositions(344/2500,False),constructivePositiveHeliumLocations=raypositions(999/2500,False),
 rigidWallPressureNodeThresholdRadiusOverLambda=.25,rigidWallPressureNodeAirLocations=raypositions(344/2500,True),rigidWallPressureNodeHeliumLocations=raypositions(999/2500,True),
 semanticIssue='Constructivepressureraysmakeantinodes,notnodes;one-endgeometryhasd>=0,notbothsigns.')
#54 threephasorschecked for100randomphases andtimes.
rng=np.random.default_rng(35)
for phi,wt in rng.uniform(-10,10,(100,2)):
 lhs=math.cos(wt)+math.cos(wt+phi)+math.cos(wt-phi)
 rhs=(1+2*math.cos(phi))*math.cos(wt)
 assert abs(lhs-rhs)<1e-13
put(54,amplitudeFormula='E*abs(1+2cosphi)',intensityRatioFormula='(1+2cosphi)^2/9',lesserMaxPhase='(2m+1)pi',lesserMaxIntensityRatio=1/9,nearestDarkPhaseRad=[-2*math.pi/3,2*math.pi/3],firstLesserMaxDistanceMm=650e-9*1/(2*.200e-3)*1e3,nearestOtherAbsoluteMaxDistanceMm=650e-9*1/.200e-3*1e3)
L=.03;n=1.48;dndT=2.5e-5;expansion=5e-6;rate=5.
put(55,fringesPerMinute=2*L*(dndT+(n-1)*expansion)*rate/589e-9,airReplacedByExpandingGlass=True)
d=2*.200*.00350*(1.50-1);R=.200+2.
put(56,virtualSourceSeparationM=d,sourceToScreenM=R,fringeSpacingMm=500e-9*R/d*1e3)
put(57,choice='d')
put(58,choice='c',relativePhaseAddedRad=math.pi)
put(59,choice='c',frequencyHz=340/(2*.34),firstMinimumAfterStartingMaximumAssumed=True)
for m in range(-5,6):
 assert math.isclose(math.cos((2*math.pi*m)/4)**2,1. if m%2==0 else 0.,abs_tol=1e-12)
for m in range(-5,6):
 assert math.isclose(math.cos(((2*m+1)*math.pi)/4)**2,.5,abs_tol=1e-12)
put(60,choice='c',originalMaximaSplitIntoBrightAndDark=True,originalMinimaBecomeHalfMaximum=True)
assert set(r)=={str(i) for i in range(32,61)}
(q/'exercises-32-60-data-checks.json').write_text(json.dumps({'status':'passed','numberedExercises':29,'results':r},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(r,ensure_ascii=False,indent=2))
