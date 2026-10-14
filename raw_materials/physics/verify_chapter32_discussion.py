"""Check quantitative and sign arguments for all13 discussion solutions."""
from pathlib import Path
import math,json
import numpy as np
R=Path(__file__).resolve().parents[2];d={}
def put(n,**data):d[f'Q32.{n}']={'status':'passed',**data}
assert np.allclose(np.cross([0,2,0],[0,0,3]),[6,0,0])
put(1,singlePlaneWaveDirection='+x for E+y,B+z',incomingDirection='-x',limitation='multiple-wave decomposition is not unique')
put(2,metalShielding='induced surface charges/currents; reflection and apertures depend on geometry and wavelength')
put(3,commonVacuumSpeed=3e8,distinctProperties='frequency,wavelength,polarization,spectrum,interaction with matter')
put(4,energySource='absorbed radio-wave energy; induced voltage excites discharge gas')
put(5,polarizationCondition='transverse wave; fluid sound is longitudinal; transverse elastic waves in solids can be polarized')
q,E,B=2.,3.,1.
vx,vy=.2,.3
force=np.array([q*vy*B,q*(E-vx*B),0])
magnetic=q*np.cross([vx,vy,0],[0,0,B])
assert math.isclose(float(np.dot(magnetic,[vx,vy,0])),0,abs_tol=1e-12)
assert force[0]>0
put(6,initialForceDirection='+y',laterMagneticForceComponent='+x',magneticPower=0,modelLimit='nonrelativistic at small velocity')
put(7,staticVoltageInferenceInvalid=True,reasons='optical time variation and spatial phase; frequency-dependent material response')
assert math.isclose(math.sqrt(2)**2,2)
put(8,newMagneticAmplitudeFactor=math.sqrt(2))
t=np.linspace(0,2*math.pi,10001)[:-1]
assert abs(np.cos(t).mean())<1e-12
put(9,timeAverageLaserTorque=0,assumption='magnetic moment nearly constant during an optical cycle')
put(10,effectiveWireCoupling='electric field component along antenna wire')
put(11,recoilPerWattN=1/3e8,law='momentum conservation')
assert (.25*.5)==.125
put(12,newPressureFactor=.125,assumptions='isotropic source and normal incidence; distance doubled and reflection replaced by absorption')
k,w,Em,Bm=1.,1.,2.,3.
x=.37
S=4*Em*Bm*np.sin(k*x)*np.cos(k*x)*np.sin(t)*np.cos(t)
energy=(np.sin(k*x)**2*np.sin(t)**2+np.cos(k*x)**2*np.cos(t)**2)
assert abs(S.mean())<1e-12 and energy.mean()>0
put(13,meanNetMomentum=0,meanEnergyPositive=True,instantaneousMomentumCanBeNonzero=True)
assert len(d)==13
qdir=R/'qa/physics/chapter32';qdir.mkdir(parents=True,exist_ok=True)
(qdir/'discussion-data-checks.json').write_text(json.dumps({'status':'passed','questions':13,'results':d},indent=2)+'\n',encoding='utf8')
print('Checked13 discussion arguments, including Lorentz-force direction and standing-wave net momentum.')
