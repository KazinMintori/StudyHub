"""Recalculate sinusoidal averaging, phase directions and Example31.1."""
from pathlib import Path
import json,math
import numpy as np
theta=np.linspace(0,2*math.pi,200001)
wave=np.cos(theta)
mean=float(np.trapezoid(wave,theta)/(2*math.pi))
rectified=float(np.trapezoid(abs(wave),theta)/(2*math.pi))
square=float(np.trapezoid(wave*wave,theta)/(2*math.pi))
assert abs(mean)<1e-12
assert math.isclose(rectified,2/math.pi,rel_tol=1e-9)
assert math.isclose(square,.5,rel_tol=1e-12)
for name,angle,sign,trend in [('A',math.pi/4,1,-1),('B',3*math.pi/4,-1,-1),('C',5*math.pi/4,-1,1),('D',7*math.pi/4,1,1)]:
 assert np.sign(math.cos(angle))==sign
 assert np.sign(-math.sin(angle))==trend
out=Path(__file__).resolve().parents[2]/'qa/physics/chapter31';out.mkdir(parents=True,exist_ok=True)
report={'status':'passed','cosineMean':mean,'rectifiedAverageFactor':rectified,'rmsFactor':math.sqrt(square),
 'angularFrequency60':2*math.pi*60,'angularFrequency50':2*math.pi*50,'household120Peak':math.sqrt(2)*120,
 'example31_1':{'meanCurrent':0,'meanSquareCurrent':2.7**2,'currentAmplitude':math.sqrt(2)*2.7},
 'selfcheck31_1':['D','A','B','C']}
(out/'section01-numeric-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
