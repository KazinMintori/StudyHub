from pathlib import Path
import json,math,hashlib
import numpy as np,pymupdf
from numpy.polynomial import Polynomial
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-late-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);ROOT=B.parents[3];g=9.8;mass=210e-9
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as pdf:
 drawings=pdf[185].get_drawings()
 def black(d):return d.get('color')is not None and max(d['color'])<.2
 yzero=next(d['rect'].y0 for d in drawings if black(d)and d['rect'].height<.001 and d['rect'].width>118 and 390<d['rect'].y0<400 and 120<d['rect'].x0<125)
 xzero=next(d['rect'].x0 for d in drawings if black(d)and d['rect'].width<.001 and d['rect'].height>80 and 120<d['rect'].x0<125 and 310<d['rect'].y0<311)
 y150=next(d['rect'].y0 for d in drawings if d.get('color')and .7<d['color'][0]<.85 and d['rect'].height<.001 and d['rect'].width>118 and 310<d['rect'].y0<311)
 x1ms=next(d['rect'].x0 for d in drawings if d.get('color')and .7<d['color'][0]<.85 and d['rect'].width<.001 and d['rect'].height>80 and 190<d['rect'].x0<191)
 curve=next(d for d in drawings if d.get('color')and d['color'][0]>.9 and .5<d['color'][1]<.7 and d['color'][2]<.3 and d['rect'].x1<250 and 310<d['rect'].y0<320)
 assert len(curve['items'])==3 and all(item[0]=='c'for item in curve['items'])
 controls=[[[float(p.x),float(p.y)]for p in item[1:]]for item in curve['items']]
def cubic(values):
 p0,p1,p2,p3=values
 return Polynomial([p0,3*(p1-p0),3*(p0-2*p1+p2),-p0+3*p1-3*p2+p3])
segments=[];integral=0.;peak=(-math.inf,None);sampled=[]
for controls4 in controls:
 p=np.array(controls4);x=cubic(p[:,0]);y=cubic(p[:,1]);ratio=(Polynomial([yzero])-y)*(150/(yzero-y150));dt=x.deriv()*(1e-3/(x1ms-xzero));area=(ratio*dt).integ();exact=area(1)-area(0);numerical=quad(lambda s:ratio(s)*dt(s),0,1,epsabs=1e-13)[0]
 assert abs(exact-numerical)<1e-10
 integral+=exact
 candidates=[0.,1.]+[float(r.real)for r in ratio.deriv().roots()if abs(r.imag)<1e-10 and 0<=r.real<=1]
 for s in candidates:
  if ratio(s)>peak[0]:peak=(float(ratio(s)),float((x(s)-xzero)/(x1ms-xzero)))
 for s in np.linspace(0,1,301):sampled.append([float((x(s)-xzero)/(x1ms-xzero)),float(ratio(s))])
 segments.append({'controlPointsPDF':controls4,'integratedRatioSeconds':float(exact),'independentQuadRatioSeconds':float(numerical)})
initial=sampled[0][1];vmax=g*integral;weight=mass*g
assert 55<initial<70 and 135<peak[0]<150 and 1.05<peak[1]<1.2 and 1.1<vmax<1.5
assert all(b[0]>=a[0]-1e-8 for a,b in zip(sampled,sampled[1:]))
report={'status':'passed-source-curve-extraction-and-independent-integration','sourcePDFPage':186,'sourceFigure':'P5.78','sourcePDFSHA256':hashlib.sha256((ROOT/'raw_materials/physics/source/young-freedman-15.pdf').read_bytes()).hexdigest(),'massKg':mass,'weightN':weight,'calibrationPDF':{'xAt0ms':xzero,'xAt1ms':x1ms,'yAt0g':yzero,'yAt150g':y150},'initialAccelerationInG':initial,'initialNetForceN':mass*g*initial,'peakAccelerationInG':peak[0],'peakTimeMs':peak[1],'peakNetForceN':mass*g*peak[0],'maxSpeedFromWholeCurveMps':vmax,'endTimeMs':sampled[-1][0],'segments':segments,'sampledCurve':sampled,'readingLimit':'The PDFcurve is anillustration of measurements. Dense extraction doesnotcreate originalmeasurementprecision; learnerresults mustremain graph-basedestimates.','nominalReadableEstimates':{'initialAccelerationInG':60,'initialNetForceN':mass*g*60,'peakAccelerationInG':140,'peakNetForceN':mass*g*140}}
(REVIEW_OUTPUT/'flea-source-curve-review.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print(json.dumps({key:report[key]for key in ['status','initialAccelerationInG','initialNetForceN','peakAccelerationInG','peakTimeMs','peakNetForceN','maxSpeedFromWholeCurveMps','endTimeMs']},ensure_ascii=False))
