"""Verify phasor cancellations and the quantitative models used in discussion answers."""
from pathlib import Path
import math,cmath,json
import numpy as np
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter36';q.mkdir(parents=True,exist_ok=True)
cases=[]
for N,angles in [(4,[math.pi/2,math.pi,3*math.pi/2]),(8,[3*math.pi/4,math.pi/4,3*math.pi/2,7*math.pi/4])]:
 for phi in angles:
  waves=[cmath.exp(1j*k*phi) for k in range(N)];total=sum(waves);assert abs(total)<1e-13
  step=1 if N==4 and math.isclose(phi,math.pi) else 2 if math.isclose(phi,3*math.pi/2) else N//2
  pairs=[(j,j+step) for start in range(0,N,2*step) for j in range(start,start+step)]
  assert sorted(j for pair in pairs for j in pair)==list(range(N))
  for j,k in pairs:assert abs(waves[j]+waves[k])<1e-13
  cases.append(dict(N=N,phasePi=phi/math.pi,residual=abs(total),pairsOneBased=[[j+1,k+1] for j,k in pairs]))
for N in range(2,41):
 for m in range(1,N):assert abs(sum(cmath.exp(2j*math.pi*m*k/N) for k in range(N)))<1e-10
# Illustrative width estimate with an explicit chosen two-degree color spread.
fog_diameter=1.22*550e-9/math.sin(math.radians(2))
# Fixed hologram zone radii imply inverse scaling of reconstruction distance with wavelength.
record=600e-9;replay=500e-9;distance=1.;newdistance=record/replay*distance
for m in range(1,20):
 radius=math.sqrt(2*m*record*distance)
 assert math.isclose(radius**2/(2*newdistance),m*replay,rel_tol=1e-14)
# A sign change in the image-bearing amplitude cannot invert its intensity.
field=np.array([1+2j,.1-.3j,-.7+.5j]);assert np.allclose(abs(field)**2,abs(-field)**2)
data=dict(status='passed',discussionQuestions=19,phasorCases=cases,fogEstimateDiameterUm=fog_diameter*1e6,fogAssumptions=dict(wavelengthNm=550,chosenAngularSpreadDeg=2),normalPlaneWaveHologramAxialScale=newdistance/distance,negativePositiveIdealImageIntensitySame=True)
(q/'discussion-data-checks.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
print(json.dumps(data,indent=2))
