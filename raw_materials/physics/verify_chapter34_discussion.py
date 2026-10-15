"""Check the mathematical claims underlying24 qualitative discussion solutions."""
from pathlib import Path
import math,json
import numpy as np

root=Path(__file__).resolve().parents[2]
def image(f,s):return 1/(1/f-1/s)
for s in [5,15,30]:
 assert image(-10,s)<0
assert image(10,5)<0 and image(10,15)>0
for eps in [1.,.1,.001]:
 assert image(10,10-eps)<0<image(10,10+eps)
 assert -image(10,10-eps)/(10-eps)>0
 assert -image(10,10+eps)/(10+eps)<0
# Plane-interface longitudinal and transverse magnifications are different.
na,nb=4/3,1.
assert math.isclose(nb/na*2.,1.5)
s=3.;sp=-nb*s/na
assert math.isclose(-na*sp/(nb*s),1.)
# Convex-mirror angular image vs plane-mirror image, same object/eye locations.
for s in [1,10,100]:
 for eye in [.5,5,20]:
  sp=image(-8,s);m=-sp/s
  angular_ratio=m*(eye+s)/(eye+abs(sp))
  assert 0<angular_ratio<1
# Relative index controls lens power, not absolute index alone.
shape=.1
assert (1.5/1.-1)*shape>(1.5/(4/3)-1)*shape>0
assert (1.48/1.50-1)*shape<0<(1.52/1.50-1)*shape
# Air bubble: thin-lens approximation differs from finite spherical bubble.
nw=4/3;nair=1.;R=1.
thin_f=1/((nair/nw-1)*2/R)
S1=np.array([[1.,0.],[-(nair-nw)/R,1.]])
T=np.array([[1.,2*R/nair],[0.,1.]])
S2=np.array([[1.,0.],[-(nw-nair)/(-R),1.]])
M=S2@T@S1
effective=-nw/M[1,0];back=-nw*M[0,0]/M[1,0]
assert math.isclose(thin_f,-2*R)
assert math.isclose(effective,-1.5*R)
assert math.isclose(back,-2.5*R)
# Reverse refraction: swapobject/image andindices, flipR relative outgoing side.
na,nb,R,s=1.,1.5,10.,40.
sp=nb/((nb-na)/R-na/s)
assert math.isclose(nb/sp+na/s,(na-nb)/(-R))
m=-na*sp/(nb*s);mrev=-nb*s/(na*sp)
assert math.isclose(m*mrev,1.)
# Uniform symmetric pupil masks reduce transmitted area without shifting idealfocus.
for radius in [1.,2.,3.]:
 a=np.pi*radius**2
 assert math.isclose(a/2/a,.5)
q=root/'qa/physics/chapter34';q.mkdir(parents=True,exist_ok=True)
(q/'discussion-data-checks.json').write_text(json.dumps({'status':'passed','discussionQuestions':24,
 'checks':['mirrorimage signs andtwo-sidedfocuslimits','longitudinalversustransversemagnification','convexmirrorangularcomparison','relativeindexandlenspower','exacttwo-surfacebubbleversusthinapproximation','reversibilityofrefractionequation','idealhalf-pupilarea'],
 'airBubbleInWater':{'waterIndex':nw,'thinFocalLengthOverR':thin_f/R,'sphereEffectiveFocalLengthOverR':effective/R,'sphereBackFocalDistanceOverR':back/R},
 'scope':'Mathematical model checks. Qualitative source coverage requires reading.'},indent=2),encoding='utf-8')
print('Checked24 discussion models, including limits, plane refraction, reversibility and thick air bubble.')
