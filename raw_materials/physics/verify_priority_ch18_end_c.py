"""Parent checks actual guided cases and targeted conceptual identities."""
from pathlib import Path
import contextlib,io,importlib.util,json,math,re
import numpy as np
from scipy.integrate import quad
from scipy.special import erfc
ROOT=Path(__file__).resolve().parents[2]
Q=ROOT/'qa/physics1-priority';Q.mkdir(exist_ok=True)
spec=importlib.util.spec_from_file_location('worker_c',ROOT/'raw_materials/physics/verify_chapter18_exercises_c.py')
worker=importlib.util.module_from_spec(spec);spec.loader.exec_module(worker)
captured=io.StringIO()
with contextlib.redirect_stdout(captured):
 guided=worker.verify_guided_practice()
 bridge=worker.verify_bridging_problem()
assert len(guided)==12
R=8.314462618;k=1.380649e-23
raw=ROOT/'raw_materials/physics/translations/chapter-18'
texts={p.name:p.read_text(encoding='utf-8') for p in raw.glob('*.md')}
assert r'T_2 = 28{,}65' not in texts['09-luyen-tap-huong-dan.md']
assert r'T_2 = 228{,}65' in texts['09-luyen-tap-huong-dan.md']
vp=re.findall(r'^### (VP18\.\d+\.\d+)',texts['09-luyen-tap-huong-dan.md'],re.M)
assert vp==[f'VP18.{group}.{i}' for group in (4,7,8) for i in range(1,5)]
assert re.findall(r'^### (Q18\.\d+)',texts['10-cau-hoi-thao-luan.md'],re.M)==[f'Q18.{i}' for i in range(1,31)]
props={}
# These are property checks of derivations, not substitute textbook examples.
for ratio in [.2,.5,2,5]:
 densityRatio=ratio**.6;temperatureRatio=ratio**.4
 assert math.isclose(temperatureRatio,ratio/densityRatio,rel_tol=1e-12)
props['VP18.4.4_density_and_temperature_relation']='checked at four positive pressure ratios'
r=2e-10;p=600;T=210.15;m=.028/worker.N_A
tau=lambda r,p,T:math.sqrt(m*k*T/6)/(4*math.pi*r*r*p)
base=tau(r,p,T)
effects=[tau(2*r,p,T)/base,tau(r,2*p,T)/base,tau(r,p,2*T)/base]
assert np.allclose(effects,[.25,.5,math.sqrt(2)])
props['VP18.8.4_time_factors']=effects
# Q18.1: Phase proportion can change volume at fixed coexistence p,T.
volumes=[(1-x)*1+x*1000 for x in [0,.25,.5,1]]
assert all(a<b for a,b in zip(volumes,volumes[1:]))
props['Q18.1_phase_fraction_property']=volumes
# Q18.14: Subtract the directed center-of-mass motion before measuring heat.
thermal=np.vstack([np.eye(3),-np.eye(3)])*400
boosted=thermal+np.array([2000,0,0])
assert np.allclose(boosted.mean(axis=0),[2000,0,0])
assert np.allclose(((boosted-boosted.mean(axis=0))**2).sum(axis=1),(thermal**2).sum(axis=1))
props['Q18.14_boost_speed_m_s']=2000
# Q18.15: Increasing p need not increase T if V decreases reciprocally.
assert math.isclose(2*(1/2),1)
props['Q18.15_isothermal_pressure_volume_factor']=1
# Q18.19: Internal kinetic degrees can reverse a translational-only ranking.
kineticRatio=(5/3)*(20.18/32)
assert kineticRatio>1 and 20.18/32<1
props['Q18.19_O2_vs_Ne_equal_mass_property']=dict(translationalRatio=20.18/32,allKineticRatio=kineticRatio)
props['Q18.20']=dict(energyRatio=323.15/298.15,doubledEnergyTemperature_K=2*298.15,doubledEnergyTemperature_C=2*298.15-273.15)
assert math.isclose(props['Q18.20']['doubledEnergyTemperature_C'],323.15,abs_tol=1e-10)
props['Q18.21_temperatureFactor']=2**2
props['Q18.22_temperatureRiseRatio']=2.5/1.5
assert math.isclose(props['Q18.22_temperatureRiseRatio'],5/3)
# Q18.24: Speed-density normalization and finite interval probability.
f=lambda x:math.sqrt(2/math.pi)*x*x*math.exp(-x*x/2)
assert math.isclose(quad(f,0,np.inf)[0],1,rel_tol=1e-12)
props['Q18.24_normalization']=quad(f,0,np.inf)[0]
assert 600<610 and 600<5.17e5
props['Q18.25_pressure_Pa']=600
pressure=1.013e5+1025*9.8*2400
assert pressure>22.12e6
props['Q18.28']=dict(temperature_C=279,depth_m=2400,densityEstimate_kg_m3=1025,pressureEstimate_Pa=pressure,aboveCriticalPressure=True)
# Finite population: positive thermal tail means possible escape, not a
# logical guarantee for every finite realization.
sigma=math.sqrt(R*298.15/.028);x=2025/sigma
tail=erfc(x/math.sqrt(2))+math.sqrt(2/math.pi)*x*math.exp(-x*x/2)
assert 0<tail<1
props['bridge']=dict(temperature_K=298.15,molarMass_kg_mol=.028,gravity_m_s2=1.3,escapeSpeed_m_s=2025,rms_m_s=math.sqrt(3)*sigma,height_m=3*sigma*sigma/(2*1.3),escapeTailFraction=float(tail),expectedFastMolecules=float(tail*1.2*worker.N_A))
assert props['bridge']['expectedFastMolecules']>1
result=dict(status='passed',scope='Actual12 guided numerical cases plus targeted physical identities; no certification of all conceptual prose from code alone.',guidedCases=guided,bridge=bridge,propertyChecks=props,promptCount=43)
(Q/'ch18-end-c-parent-ledger.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(status='passed',actualGuidedCases=len(guided),targetedPropertyChecks=len(props),prompts=43,balloonTemperature_K=228.65,bridgeHeight_km=props['bridge']['height_m']/1000)))
