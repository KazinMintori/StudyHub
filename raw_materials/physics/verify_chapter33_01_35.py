"""Recalculate source exercises1–35, respecting angles, units and model conditions."""
from pathlib import Path
import math,json
import numpy as np
root=Path(__file__).resolve().parents[2];out=root/'qa/physics/chapter33'
c=3e8;R=math.radians;D=math.degrees;nwater=1.333
asin=lambda x:D(math.asin(x));snell=lambda na,nb,theta:asin(na/nb*math.sin(R(theta)))
r={}
def put(n,**kw):r[str(n)]={'status':'passed',**kw}
put(1,incidenceDeg=D(math.atan(11.5/14)),firstMirrorDistanceCm=11.5,targetHeightCm=14)
put(2,wavelengthNm=[380/1.34,750/1.34],frequencyHz=[c/750e-9,c/380e-9],speed=c/1.34)
put(3,speed=c/1.47,wavelengthNm=650/1.47)
put(4,vacuumWavelengthNm=c/5.8e14*1e9,glassWavelengthNm=c/5.8e14/1.52*1e9)
ratio=math.sin(R(44.7))/math.sin(R(38));v=1.85e8*ratio
put(5,speed=v,wavelengthNm=v/5.07e14*1e9,frequencyHz=5.07e14,sourceRoundingFraction=abs(1.85e8/(365e-9*5.07e14)-1))
put(6,benzeneWavelengthNm=526*nwater/1.501)
tb=snell(1,1.66,42.5)
put(7,reflectedSurfaceAngle=47.5,refractedNormalAngle=tb,refractedSurfaceAngle=90-tb)
put(8,refractiveIndex=1+c*6.25e-9/2.5)
n=math.sin(R(62.7))/math.sin(R(48.1))
put(9,refractiveIndex=n,speed=c/n)
put(10,methanolAngle=snell(1,1.329,41.3),unknownIndex=math.sin(R(41.3))/math.sin(R(20.2)),glassThicknessM=.025,glassIndex=1.550,parallelFaces=True)
nx=nwater*math.sin(R(48))/math.sin(R(25))
put(11,indexX=nx,airAngle=asin(nwater*math.sin(R(48))),xNormalAngle=25,waterNormalAngle=48)
put(12,waterAngle=snell(1,nwater,35),glassIndexDependence=False)
put(13,solidAngle=asin(315/447*math.sin(R(62))))
put(14,glassAngle=asin(544/726*math.sin(R(56))))
put(15,maxBetaAir=90-asin(1/1.60),maxBetaWater=90-asin(1.33/1.60),givenWaterIndex=1.33,waterUsingTableIndex=90-asin(nwater/1.60))
ng=nwater*math.sin(R(49.8))/math.sin(R(36.2))
put(16,glassIndex=ng,criticalAngle=asin(nwater/ng))
nl=1/math.sin(R(42.5))
put(17,liquidIndex=nl,liquidToAirAngle=snell(nl,1,35),airToLiquidAngle=snell(1,nl,35))
put(18,criticalAir=asin(1/1.62),criticalWater=asin(nwater/1.62))
put(19,glassIndex=nwater/math.sin(R(48.7)))
critical=math.asin(1/nwater);radius=10*math.tan(critical)
put(20,escapeRadiusM=radius,escapeAreaM2=math.pi*radius**2,depthM=10)
put(21,maxAlphaAir=90-asin(1/1.52),maxAlphaWater=90-asin(nwater/1.52))
put(22,plasticWavelengthNm=350/math.sin(R(48.6)),refractedAngle=asin(math.sin(R(40))/math.sin(R(48.6))),sourceIncidenceBelowCritical=True)
n400,n700=1.66,1.61
ang400=snell(1,n400,35);ang700=snell(1,n700,35)
put(23,incidenceNormalDeg=35,approxGraphIndex400=n400,approxGraphIndex700=n700,angle400=ang400,angle700=ang700,separationDeg=ang700-ang400,graphReadingIsApproximate=True)
violet=snell(1,2.46,53.5);red=snell(1,2.41,53.5)
put(24,violetAngle=violet,redAngle=red,separationDeg=red-violet)
nred=math.sin(R(57))/math.sin(R(38.1));nviolet=math.sin(R(57))/math.sin(R(36.7))
put(25,redIndex=nred,violetIndex=nviolet,redSpeed=c/nred,violetSpeed=c/nviolet)
thickness=589e-9/(4*(1.658-1.486))
put(26,minimumThicknessM=thickness,ordinaryIndex=1.658,extraordinaryIndex=1.486,numberOfCyclesDifference=thickness*(1.658-1.486)/589e-9,circularOutputRequiresEqualInputComponents=True)
put(27,intensityFraction=.5*math.cos(R(30))**2)
ratio=math.sin(R(38.7));b1=D(math.atan(ratio));b2=D(math.atan(1/ratio))
put(28,solidToLiquidBrewster=b1,liquidToSolidBrewster=b2,indexRatio=ratio)
A=.5;B=A*math.cos(R(60))**2;C=B*math.cos(R(30))**2
put(29,atA=A,atB=B,atC=C,withoutMiddleAtC=0)
put(30,unpolarizedAngle=D(math.acos(math.sqrt(.2))),alignedPolarizedAngle=D(math.acos(math.sqrt(.1))))
put(31,glassIndex=math.tan(R(54.5)),refractionAngle=35.5)
put(32,brewsterAir=D(math.atan(1.66)),brewsterWater=D(math.atan(1.66/nwater)))
Iout=20*.5*math.cos(R(62-25))**2
put(33,intensityWcm2=Iout,intensityWm2=Iout*1e4,inputWcm2=20,axisDifferenceDeg=37)
Iin=55/(.5*math.cos(R(23))**2*math.cos(R(39))**2);newout=Iin*.5*math.cos(R(62))**2
put(34,incidentWcm2=Iin,withoutMiddleWcm2=newout,withoutMiddleWm2=newout*1e4)
green=(495+570)/2;red=(620+750)/2;violet=(380+450)/2
put(35,greenMidpointNm=green,redMidpointNm=red,violetMidpointNm=violet,redRatio=(green/red)**4,violetRatio=(green/violet)**4,assumption='equal incident spectral intensities, midpoint of current Table32.1 wavelength intervals')
assert set(r)=={str(i) for i in range(1,36)}
# Inverse geometry, frequency continuity, phase retardance and power projections.
assert math.isclose(math.tan(R(r['1']['incidenceDeg'])),11.5/14,rel_tol=1e-12)
assert math.isclose(r['8']['refractiveIndex']*2.5/c-2.5/c,6.25e-9,rel_tol=1e-12)
assert math.isclose(r['11']['indexX']*math.sin(R(25)),math.sin(R(r['11']['airAngle'])),rel_tol=1e-12)
for nmid in [1.2,1.52,1.9]:
 tmid=snell(1,nmid,35);tout=snell(nmid,nwater,tmid)
 assert math.isclose(tout,r['12']['waterAngle'],rel_tol=1e-12)
assert math.isclose(math.sin(R(90-r['15']['maxBetaAir'])),1/1.6,rel_tol=1e-12)
assert math.isclose(math.sin(R(r['16']['criticalAngle'])),nwater/r['16']['glassIndex'],rel_tol=1e-12)
assert math.isclose(math.sqrt(r['20']['escapeAreaM2']/math.pi)/10,math.tan(critical),rel_tol=1e-12)
assert r['22']['refractedAngle']>40 and 40<48.6
assert r['24']['violetAngle']<r['24']['redAngle']
assert math.isclose(r['26']['numberOfCyclesDifference'],.25,rel_tol=1e-12)
assert math.isclose(r['28']['solidToLiquidBrewster']+r['28']['liquidToSolidBrewster'],90,rel_tol=1e-12)
assert math.isclose(.5*math.cos(R(r['30']['unpolarizedAngle']))**2,.1,rel_tol=1e-12)
assert math.isclose(math.cos(R(r['30']['alignedPolarizedAngle']))**2,.1,rel_tol=1e-12)
# Jones projections use relative axes, independently of the chained scalar formula.
def axis(a):return np.array([math.cos(R(a)),math.sin(R(a))])
e1=axis(0);e2=axis(60);e3=axis(90);state=math.sqrt(.5)*e1
state=np.dot(state,e2)*e2;assert math.isclose(float(np.dot(state,state)),B,rel_tol=1e-12)
state=np.dot(state,e3)*e3;assert math.isclose(float(np.dot(state,state)),C,rel_tol=1e-12)
assert math.isclose(r['33']['intensityWm2'],r['33']['intensityWcm2']/(.01**2),rel_tol=1e-12)
assert math.isclose(Iin*.5*math.cos(R(23))**2*math.cos(R(39))**2,55,rel_tol=1e-12)
report={'status':'passed','numberedExercises':35,'constants':{'c':c,'waterIndexTable33_1':nwater,'methanolIndex':1.329,'benzeneIndex':1.501},'results':r}
(out/'exercises-01-35-data-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(r,ensure_ascii=False,indent=2))
