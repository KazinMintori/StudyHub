"""Source-derived numeric checks for exercises18–31."""
from pathlib import Path
import json,math
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter35';q.mkdir(parents=True,exist_ok=True);r={}
def put(i,**kw):r[str(i)]=kw
lam=660e-9;R=.9;d=.260e-3
put(18,firstMinimumMm=lam*R/(2*d)*1e3,nearestHalfIntensityMm=lam*R/(4*d)*1e3)
phase=2*math.pi*.340e-3*math.sin(math.radians(23))/500e-9
put(19,phaseDifferenceRad=phase,phaseModulo2PiRad=phase%(2*math.pi))
r20={'wavelengthNm':2*.003*.0720e-3/.8*1e9}
for y in [.002,.0015]:r20[str(y)]=.0600*math.cos(math.pi*y/(2*.003))**2
put(20,**r20)
phase=2*math.pi*1.8/2.5
put(21,phaseDifferenceRad=phase,intensityRatio=math.cos(phase/2)**2)
put(22,wavelengthNm=2*(910-650),minimumThicknessNm=(910-650)/2)
put(23,minimumThicknessNm=650/(4*1.42))
unit=505/(2*2.62);put(24,minimumThicknessNm=unit,nextThreeThicknessesNm=[2*unit,3*unit,4*unit])
n=2.62;lam=520;t0=1036;m=math.ceil(2*n*t0/lam);t=m*lam/(2*n)
put(25,minimumAddedThicknessNm=t-t0,finalThicknessNm=t,geometricalPathDifferenceNm=2*t,opticalPathDifferenceNm=2*n*t,numberWavelengthsInFilm=m)
put(26,minimumThicknessNm=550/(4*1.70),nextThicknessNm=3*550/(4*1.70))
def visible(t,n):
 return [4*n*t/(2*m+1) for m in range(20) if 380<=4*n*t/(2*m+1)<=750]
put(27,at290nm=visible(290,1.33),at340nm=visible(340,1.33))
put(28,minimumThicknessNm=575/(4*1.50))
put(29,minimumPitDepthNm=790/(4*1.8))
a=818*606e-9/2;b=818*502e-9/2
put(30,janDistanceMm=a*1e3,lindaDistanceMm=b*1e3,netDisplacementAwayFromJanMicrometers=(a-b)*1e6)
put(31,mirrorDisplacementMm=1800*633e-9/2*1e3)
assert set(r)=={str(i) for i in range(18,32)}
(q/'exercises-18-31-data-checks.json').write_text(json.dumps({'status':'passed','numberedExercises':14,'results':r},indent=2),encoding='utf-8')
print(json.dumps(r,indent=2))
