"""Independent geometry checks for the draft opening and section34.1."""
from pathlib import Path
import json
import numpy as np

root=Path(__file__).resolve().parents[2]
rng=np.random.default_rng(34)
mirror_x=np.diag([-1.,1.,1.])
mirror_y=np.diag([1.,-1.,1.])
for _ in range(100):
 p=rng.uniform(-10,10,3)
 assert np.allclose(mirror_x@(mirror_y@p),mirror_y@(mirror_x@p))
 assert np.allclose(np.linalg.norm(mirror_x@p),np.linalg.norm(p))
 # Arbitrary real object in front of mirrorx=0, arbitrary point at which it reflects.
 p[0]=-abs(p[0])-.1
 hit=np.array([0.,rng.uniform(-10,10),rng.uniform(-10,10)])
 incoming=(hit-p)/np.linalg.norm(hit-p)
 reflected=mirror_x@incoming
 virtual=mirror_x@p
 apparent=(hit-virtual)/np.linalg.norm(hit-virtual)
 assert np.allclose(reflected,apparent)
 assert np.isclose(-p[0],abs(virtual[0]))
 # Separation derivative as the object approaches mirror, v=arbitrarypositive.
 v=float(rng.uniform(.1,10));s=float(rng.uniform(1,20));dt=1e-6
 dD=(2*(s-v*dt)-2*s)/dt
 assert np.isclose(dD,-2*v,rtol=1e-7)
 # Transverse heights are preserved by plane reflection.
 q=p+np.array([0.,2.3,0.])
 assert np.isclose((mirror_x@q-mirror_x@p)[1]/(q-p)[1],1.)
q=root/'qa/physics/chapter34';q.mkdir(parents=True,exist_ok=True)
(q/'opening-data-checks.json').write_text(json.dumps({'status':'passed','randomGeometries':100,'planeMirrorRays':'reflectionlaw-and-virtualintersection','twoPerpendicularMirrorsCommute':True,'magnification':1,'relativeApproachSpeedFactor':2,'sourceCoverage':'opening-and34.1-only','fullChapter':'incomplete'},indent=2),encoding='utf-8')
print('Verified100 plane-mirror geometries,signs,magnification and relative speed. Chapter34 remains incomplete.')
