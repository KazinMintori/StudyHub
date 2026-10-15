"""Numerical and geometric checks for source problems36–64 and all19 plot markers."""
from pathlib import Path
import json,math
import numpy as np
import pymupdf as fitz
root=Path(__file__).resolve().parents[2];out=root/'qa/physics/chapter33'
c=3e8;nwater=1.333;R=math.radians;D=math.degrees
asin=lambda x:D(math.asin(x));snell=lambda na,nb,a:asin(na/nb*math.sin(R(a)))
r={}
def put(n,**kw):r[str(n)]={'status':'passed',**kw}
#36: User measurement problem; independently check exact and small-angle formulas.
approximations=[]
for d_H in [.1,.02,.001]:
 H=1.;d=d_H;ta=math.atan(d/H);tb=math.asin(nwater*math.sin(ta));s=H*math.tan(tb)-d
 nexact=(d+s)/d*math.sqrt(H*H+d*d)/math.sqrt(H*H+(d+s)**2)
 nest=1+s/d
 assert math.isclose(nexact,nwater,rel_tol=1e-12)
 approximations.append(nest)
assert abs(approximations[-1]-nwater)<abs(approximations[0]-nwater)
put(36,incidenceTangent='d/H',refractionTangent='(s+d)/H',smallAngleIndex='1+s/d',requiresActualMeasurements=True,illustrativeSmallAngleSequence=approximations)
put(37,frequencyRangeMHz=[1,5],muscleIndex=344/1480,entryAngle=asin(1480/344*math.sin(R(9.73))),criticalAngle=asin(344/1480))
n=1+c*(21.2-17.0)*1e-9/.840
put(38,index=n,wavelengthNm=490/n,airPathLengthM=c*17e-9)
put(39,maximumAirIncidence=asin(math.sqrt(1.38**2-1)),blockIndex=1.38)
put(40,insideIncidence=60,outsideAngles=[72,80.5],indexes=[math.sin(R(72))/math.sin(R(60)),math.sin(R(80.5))/math.sin(R(60))])
put(41,maximumOilIndex=1.52*math.sin(R(57.2)))
n=1/math.sin(R(50));air=asin(n*math.sin(R(40)))
put(42,index=n,firstRefractionAngle=40,criticalAngle=50,airIncidence=air)
N=(.018-.0025)/540e-9+.0025/(540e-9/1.40)
put(43,wavelengthCount=N,opticalLengthM=.018+.4*.0025)
tair=D(math.atan(1.5/1.2));tw=snell(1,nwater,tair);distance=1.5+4*math.tan(R(tw))
put(44,airAngle=tair,waterAngle=tw,keyDistanceM=distance)
ta=math.atan(.08/.16);tb=math.atan(.04/.16)
put(45,liquidIndex=math.sin(ta)/math.sin(tb),airAngle=D(ta),liquidAngle=D(tb))
n1,n2=1.465,1.450;NA=math.sqrt(n1*n1-n2*n2)
put(46,criticalAngle=asin(n2/n1),numericalAperture=NA,acceptanceHalfAngle=asin(NA))
put(47,withIceAngle=asin(1/nwater),afterMeltingAngle=asin(1/nwater),iceIndex=1.309)
def fraction(N,totalAngle=math.pi/2):return math.exp(2*N*math.log(math.cos(totalAngle/N)))
def minimum(threshold):
 return next(N for N in range(1,2000) if fraction(N)>threshold)
mins={str(x):minimum(x) for x in [.9,.95,.99]}
for threshold,Nmin in zip([.9,.95,.99],mins.values()):assert fraction(Nmin)>threshold and fraction(Nmin-1)<=threshold
table=[{'N':N,'fraction':fraction(N)} for N in [1,2,3,5,10,20,23,24,48,49,245,246]]
put(48,printedIncrement='pi/(4N)',printedTotalRotationDeg=45,printedFractionForN10=fraction(10,math.pi/4),target90DegreeMinimumCounts=mins,table90DegreeRotation=table,sourceAngleAndRotationInconsistent=True)
ref=asin(1.66*math.sin(R(25)));put(49,emergentAngle=ref,separation=2*(ref-25))
put(50,maximumLiquidIndex=1.56*math.sin(R(60)),internalIncidence=60)
Earth=6378.;h=20.;natm=1.0003
beta=math.asin(Earth/(Earth+h));alpha=math.asin(natm*Earth/(Earth+h));delta=D(alpha-beta)
put(51,deltaDeg=delta,solarAngularRadiusDeg=.25,ratioToSolarRadius=delta/.25,earthRadiusKm=Earth,layerThicknessKm=h)
refr=snell(1,1.8,66);shift=.024*math.sin(R(66-refr))/math.cos(R(refr))
put(52,refractionAngle=refr,lateralShiftM=shift)
bp=D(math.atan(1.61));water_angle=snell(1,nwater,90-bp)
put(53,wallBrewster=bp,waterIncidence=90-bp,waterRefraction=water_angle)
#54: Conserve normal power flux; transmitted and incident cross-sections differ.
n=1.62;I0=150.;bp=math.atan(n);bt=math.pi/2-bp
rs=math.sin(bp-bt)/math.sin(bp+bt);Rs=rs*rs
Iref=.5*I0*Rs;Is=(.5*I0-Iref)*math.cos(bp)/math.cos(bt);Ip=.5*I0*math.cos(bp)/math.cos(bt)
ts=2*math.cos(bp)/(math.cos(bp)+n*math.cos(bt));tp=2*math.cos(bp)/(n*math.cos(bp)+math.cos(bt))
assert math.isclose(Is,.5*I0*n*ts*ts,rel_tol=1e-12)
assert math.isclose(Ip,.5*I0*n*tp*tp,rel_tol=1e-12)
assert math.isclose((Is+Ip)*math.cos(bt),(I0-Iref)*math.cos(bp),rel_tol=1e-12)
ecc=math.sqrt(1-Is/Ip);assert math.isclose(ecc,abs(rs),rel_tol=1e-12)
put(54,brewsterDeg=D(bp),refractionDeg=D(bt),amplitudeReflectionRatio=rs,reflectedIntensity=Iref,transmittedSIntensity=Is,transmittedPIntensity=Ip,eccentricity=ecc,ellipseMinorMajorRatio=math.sqrt(Is/Ip),figureMajorAxis='E1',figureMinorAxis='E2',sourceEccentricityRatioReversed=True)
angles=[36.4,40.5,32.1,35.2];indices=[math.sin(R(60))/math.sin(R(t)) for t in angles]
put(55,indexes=indices,dielectricConstants=[x*x for x in indices],frequencyHz=c/589e-9,identifications=['carbon tetrachloride','water','carbon disulfide','benzene'])
indices56=[math.sqrt(1.52**2-math.sin(R(a))**2) for a in [52,44.3,36.3]]
put(56,indexes=indices56,vacuumWavelengthNm=638)
# Read each actual black vector marker using the source chart's calibrated axes.
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 markers=[]
 for d in pdf[1127].get_drawings():
  rr=d['rect']
  if 370<rr.x0<500 and 185<rr.y0<270 and 3.9<rr.width<4.1 and 3.9<rr.height<4.1 and d['fill']:
   markers.append(((rr.x0+rr.x1)/2,(rr.y0+rr.y1)/2))
markers.sort();assert len(markers)==19
a57=np.array([round((x-381.2995)/(491.5245-381.2995)*200) for x,y in markers],dtype=float)
y57=np.array([(265.13608-y)/(265.13608-192.53647)*30 for x,y in markers]);assert np.array_equal(a57,np.arange(0,181,10))
design=np.column_stack([np.ones(19),np.cos(np.deg2rad(2*a57)),np.sin(np.deg2rad(2*a57))]);A,B,C=np.linalg.lstsq(design,y57,rcond=None)[0]
amp=math.hypot(B,C);theta=(D(math.atan2(C,B))/2)%180;unpolarized=2*(A-amp);polarized=2*amp
assert 34.9<theta<35.1 and abs(unpolarized-10)<.1 and abs(polarized-20)<.1
# Independently scan phase while solving only the two remaining linear parameters.
phase_candidates=np.linspace(34.95,35.05,1001);sse=[]
for phase in phase_candidates:
 basis=np.column_stack([np.ones(19),np.cos(np.deg2rad(a57-phase))**2]);coef=np.linalg.lstsq(basis,y57,rcond=None)[0];sse.append(np.sum((basis@coef-y57)**2))
assert abs(float(phase_candidates[int(np.argmin(sse))])-theta)<.0002
put(57,sourcePoints=19,anglesDeg=a57.tolist(),readIntensityWm2=y57.tolist(),coefficients=[float(A),float(B),float(C)],orientationDeg=theta,unpolarizedIntensity=unpolarized,polarizedIntensity=polarized,sourceReadingApproximate=True)
put(58,magnification=1.53,objectDiameterMm=45,apparentDiameterMm=1.53*45,resinRadiusMm=80,constructionRequiresNRLessThanR=True)
#59: Uniform critical curvature and repeated inner-tangent chords, as drawn.
dcore=50e-6;ni=1.4475;no=1.4440;radius=dcore*(ni+no)/(2*(ni-no));rin=radius-dcore/2;rout=radius+dcore/2
incidence=math.asin(rin/rout);critical=math.asin(no/ni);assert math.isclose(incidence,critical,rel_tol=1e-12)
half_angle=math.acos(rin/rout);chord=2*math.sqrt(rout*rout-rin*rin);arc=2*radius*half_angle
path_ratio=chord/arc;compact_ratio=math.tan(half_angle/2)/(half_angle/2)
assert math.isclose(path_ratio,compact_ratio,rel_tol=1e-12)
extra=1000*(path_ratio-1);time_excess=(ni*1000*path_ratio-1000)/c
put(59,criticalRadiusM=radius,incidenceDeg=D(incidence),halfBendAngleDeg=D(half_angle),pathToCenterlineArcRatio=path_ratio,extraPathM=extra,timeExcessS=time_excess,coreThicknessM=dcore,coreIndex=ni,claddingIndex=no,curvatureAssumption='uniform critical bend and repeated tangent chords')
#60/61: Check stationary angular deflection for both reflection orders.
rainbows={}
for m in [1,2]:
 colors={}
 for color,n in [('violet',1.342),('red',1.330)]:
  i=math.acos(math.sqrt((n*n-1)/(m*(m+2))));rr=math.asin(math.sin(i)/n)
  deviation=m*math.pi+2*i-2*(m+1)*rr
  derivative=2-2*(m+1)*math.cos(i)/(n*math.cos(rr));assert abs(derivative)<1e-12
  fun=lambda x:m*math.pi+2*x-2*(m+1)*math.asin(math.sin(x)/n)
  step=1e-5;numerical=(fun(i+step)-fun(i-step))/(2*step);assert abs(numerical)<1e-8
  bow_radius=(math.pi-deviation) if m==1 else (deviation-math.pi)
  colors[color]={'incidenceDeg':D(i),'refractionDeg':D(rr),'orientedDeviationDeg':D(deviation),'bowRadiusDeg':D(bow_radius)}
 rainbows[m]=colors
assert rainbows[1]['red']['bowRadiusDeg']>rainbows[1]['violet']['bowRadiusDeg']
assert rainbows[2]['violet']['bowRadiusDeg']>rainbows[2]['red']['bowRadiusDeg']
put(60,colors=rainbows[1],higherColor='red')
put(61,colors=rainbows[2],higherColor='violet',deviationIsOriented=True)
put(62,choice='a',horizontalIntensityFraction=math.cos(R(45))**2,verticalIntensityFraction=math.sin(R(45))**2)
n=1.50;normal_incidence=(n-1)**2/(n+1)**2;thetaB=math.atan(n)
assert math.isclose(normal_incidence,.04,rel_tol=1e-12)
put(63,choice='d',normalIncidenceBothPolarizationsPresent=True,nearBrewsterReflectedPolarization='horizontal')
assert math.isclose(.5*math.cos(R(0))**2,.5,rel_tol=1e-12)
put(64,choice='b',secondAxisParallelFirst=True,transmittedPolarization='vertical')
assert set(r)=={str(i) for i in range(36,65)}
(out/'exercises-36-64-data-checks.json').write_text(json.dumps({'status':'passed','numberedExercises':29,'results':r},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in r.items() if k!='57'},ensure_ascii=False,indent=2));print('57:',theta,unpolarized,polarized,'all19 markers used')
