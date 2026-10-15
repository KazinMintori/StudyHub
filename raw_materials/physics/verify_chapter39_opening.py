from pathlib import Path
import json
import numpy as np
root=Path(__file__).resolve().parents[2]
h=6.626e-34;c=2.998e8;m=9.109e-31
rows=[]
for p in np.geomspace(1e-29,1e-20,51):
 photonE=p*c
 electronE=np.hypot(m*c*c,p*c)
 assert electronE>photonE
 invariant=electronE**2-photonE**2
 assert np.isclose(invariant,(m*c*c)**2,rtol=1e-10,atol=0)
 rows.append({'p':float(p),'electron_energy_exceeds_photon_at_same_p':True})
# Imaging resolution is linked to wavelength and hence momentum, not to comparing total energies at fixed p.
ps=np.geomspace(1e-29,1e-20,51)
assert np.all(np.diff(h/ps)<0)
assert 100e-9==.1e-6
d=dict(status='passed',openingAnswer='i as the reason for finer imaging',energyComparisonIv='true but not a separate resolution mechanism at fixed p',testedMomenta=len(rows),sourceScale100nmEquals0_1micrometer=True)
q=root/'qa/physics/chapter39';q.mkdir(parents=True,exist_ok=True);(q/'opening-numeric.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
print('Verified opening resolution argument, equal-p energy comparison and scale conversion.')
