"""Actual source cases18.5–18.8 and independent kinetic-model checks."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2];Q=ROOT/'qa/physics1-priority';Q.mkdir(parents=True,exist_ok=True)
N_A=6.02214076e23;k_exact=1.380649e-23
R_exact=N_A*k_exact
R=8.314;k=1.38e-23;T=300
speeds=np.array([500,600,700,800,900],dtype=float)
radius=2e-10;pressure=1.01e5
sigma=4*math.pi*radius**2
lam=k*T/(math.sqrt(2)*sigma*pressure)
rms=math.sqrt(3*R*T/.032)
cases={
 '18.5':dict(hydrogenAtom_kg=1.008e-3/N_A,oxygenMolecule_kg=.032/N_A),
 '18.6':dict(T_K=T,meanTranslational_J=1.5*k*T,molarTranslational_J=1.5*R*T,oxygenRms_m_s=rms,rmsFromRoundedMolecule_m_s=math.sqrt(3*k*T/5.31e-26)),
 '18.7':dict(speeds_m_s=speeds.tolist(),mean_m_s=float(speeds.mean()),meanSquare=float((speeds**2).mean()),rms_m_s=float(np.sqrt((speeds**2).mean()))),
 '18.8':dict(radius_m=radius,pressure_Pa=pressure,collisionArea_m2=sigma,meanFreePath_m=lam,meanFreeTime_s=lam/rms,collisionsPerSecond=rms/lam),
 'selfcheck18.2':dict(lengthFactor=2,volumeFactor=8,densityFactor=1/8),
 'selfcheck18.3':dict(T_over_M=[300/.032,300/.028,330/.032,330/.028]),
 'fundamentalConstants':dict(N_A=N_A,k=k_exact,R=R_exact)
}
assert math.isclose(lam,5.8e-8,rel_tol=.01)
assert math.isclose(rms,484,rel_tol=.002)
assert speeds.mean()==700 and (speeds**2).mean()==510000
assert np.argsort(-np.array(cases['selfcheck18.3']['T_over_M'])).tolist()==[3,1,2,0]
# Isotropy produces <vx²>=<v²>/3 without assuming equal speeds.
# For each chosen speed use all six cardinal directions.
vectors=np.array([direction*speed for speed in [180,370,620,1000] for direction in np.vstack([np.eye(3),-np.eye(3)])])
components=(vectors**2).mean(axis=0);meanv2=(vectors**2).sum(axis=1).mean()
assert np.allclose(components,meanv2/3)
m=.032/N_A;nu=pressure/(k_exact*T)
assert math.isclose(nu*m*components[0],nu*m*meanv2/3,rel_tol=1e-14)
# Independent Maxwell normalization and moments in dimensionless speed.
f=lambda x:4/math.sqrt(math.pi)*x*x*math.exp(-x*x)
norm=quad(f,0,np.inf)[0]
moment2=quad(lambda x:x*x*f(x),0,np.inf)[0]
assert math.isclose(norm,1,rel_tol=1e-12)
assert math.isclose(moment2,1.5,rel_tol=1e-12)
cases['kineticModelChecks']=dict(isotropicSecondMoments=components.tolist(),meanSpeedSquared=meanv2,maxwellNormalization=norm,maxwellDimensionlessSecondMoment=moment2)
rows=[('Hydrogen',13.80,.0704e5),('Deuterium',18.63,.171e5),('Neon',24.56,.432e5),('Nitrogen',63.18,.125e5),('Oxygen',54.36,.00152e5),('Ammonia',195.40,.0607e5),('Carbon dioxide',216.55,5.17e5),('Sulfur dioxide',197.68,.00167e5),('Water',273.16,.00610e5)]
assert [round(row[2]) for row in rows]==[7040,17100,43200,12500,152,6070,517000,167,610]
assert 600<rows[-1][2]
cases['phaseTable']=rows
(Q/'ch18-molecular-actual-cases.json').write_text(json.dumps(dict(status='passed',scope='Actual molecular examples, kinetic identities and phase-table unit conversions; separate source and browser review still required',cases=cases),ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(status='passed',actualExamples=4,meanFreePath_m=lam,meanFreeTime_s=lam/rms,phaseRows=len(rows))))
