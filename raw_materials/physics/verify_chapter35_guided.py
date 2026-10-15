"""Compute all12variationproblems and bridge using source inputs, preserving branches."""
from pathlib import Path
import math,json
import numpy as np
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter35';q.mkdir(parents=True,exist_ok=True)
r={};c=3e8
def put(k,**v):r[k]=v
# Farfield approximations used in the source examples, c=3.00e8m/s.
d=.180e-3;R=1.50;y=11.4e-3;lam=y*d/(2*R)
put('VP35.2.1',wavelengthNm=lam*1e9,thirdFringeDistanceMm=3*lam*R/d*1e3)
d=810;freq=1.05e6;lam=c/freq;maxima=[];minima=[]
for m in range(20):
 v=m*lam/d
 if v<=1:maxima.append(math.degrees(math.asin(v)))
 v=(m+.5)*lam/d
 if v<=1:minima.append(math.degrees(math.asin(v)))
put('VP35.2.2',wavelengthM=lam,maximaDeg=maxima,minimaDeg=minima)
lam=685e-9;R=2.10;y=9.15e-3;d=3*lam*R/y
put('VP35.2.3',slitSpacingMm=d*1e3,greenFringeDistanceMm=3*515e-9*R/d*1e3)
d=.370e-3;theta=math.radians(.407);lam=d*math.sin(theta)/4
put('VP35.2.4',wavelengthNm=lam*1e9,m2DarkAngleDeg=math.degrees(math.asin(2.5*lam/d)))
d=13.;lam=c/59.3e6;I0=.033
put('VP35.3.1',wavelengthM=lam,intensityWm2=I0*math.cos(math.pi*d*math.sin(math.radians(5))/lam)**2,nearestHalfIntensityAngleDeg=math.degrees(math.asin(lam/(4*d))))
lam=655e-9;d=.230e-3;R=1.75;y=6.50e-3;I0=.052
put('VP35.3.2',intensityWm2=I0*math.cos(math.pi*d*y/(lam*R))**2,nearestQuarterIntensityDistanceMm=lam*R/(3*d)*1e3)
d=8.;theta=math.radians(6);I0=.054;I=.0303
alpha=math.acos(math.sqrt(I/I0));lam=math.pi*d*math.sin(theta)/alpha
put('VP35.3.3',wavelengthM=lam,intensityAt12degWm2=I0*math.cos(math.pi*d*math.sin(math.radians(12))/lam)**2,continuousDecreaseSelectsFirstLobe=True)
d=.110e-3;R=5.;y=.0105;alpha=math.acos(.3);branches=[]
for z in [alpha,math.pi-alpha]:
 lam=math.pi*d*y/(R*z);near=math.acos(math.sqrt(.3))*lam*R/(math.pi*d)
 assert math.isclose(math.cos(math.pi*d*y/(lam*R))**2,.09,abs_tol=1e-12)
 assert 0<y<lam*R/d
 assert math.isclose(math.cos(math.pi*d*near/(lam*R))**2,.3,abs_tol=1e-12)
 branches.append({'wavelengthNm':lam*1e9,'nearest30PercentIntensityDistanceMm':near*1e3,'pointBeforeFirstDark':z<math.pi/2})
put('VP35.3.4',branches=branches,sourceDoesNotLocatePointRelativeToDarkFringe=True)
lam=565e-9;L=.080;dy=.00130;t=lam*L/(2*dy)
put('VP35.6.1',paperThicknessMicrometers=t*1e6,ethanolFringeSpacingMm=dy/1.36*1e3)
def visible(t,n,relativeFlip=True):
 out={'constructiveNm':[],'destructiveNm':[]}
 for m in range(20):
  for name,den in [('constructiveNm',m+.5 if relativeFlip else m),('destructiveNm',m if relativeFlip else m+.5)]:
   if den==0:continue
   lam=2*n*t/den
   if 380<=lam<=750:out[name].append(lam)
 return out
put('VP35.6.2',air=visible(146,1),carbonTetrachloride=visible(146,1.46))
put('VP35.6.3',air=visible(172,1),ethanol=visible(172,1.36))
put('VP35.6.4',firstThicknessNm=565/(4*1.60),secondThicknessNm=3*565/(4*1.60))
n=1.45;t=380.;reflected=visible(t,n)
put('bridge',reflectedWavelengthsNm=reflected['constructiveNm'],transmittedWavelengthsInAirNm=reflected['destructiveNm'],reflectedColors=['deep red','violet'],transmittedDominantColor='green',diverReflectedWavelengthsNm=visible(t,n)['constructiveNm'],visibleRangeNm=[380,750],sourceAppendixOmitsDeepRedRoot=True)
assert len(r)==13
(q/'guided-data-checks.json').write_text(json.dumps({'status':'passed','solutions':13,'results':r},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(r,ensure_ascii=False,indent=2))
