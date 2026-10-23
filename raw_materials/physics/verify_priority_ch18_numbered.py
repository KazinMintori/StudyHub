"""Parent invokes all actual numeric cases and checks corrected source exceptions."""
from pathlib import Path
import contextlib,io,importlib.util,json,math
import numpy as np
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2];Q=ROOT/'qa/physics1-priority'
def load_module(letter):
 p=ROOT/f'raw_materials/physics/verify_chapter18_exercises_{letter}.py'
 spec=importlib.util.spec_from_file_location('worker_'+letter,p)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 return module
d=load_module('d');e=load_module('e')
results={}
for number in range(1,45):
 results[f'18.{number}']=getattr(d,f'verify_18_{number}')()
with contextlib.redirect_stdout(io.StringIO()):e.run_verifications()
assert len({row['id'] for row in e.ledger})==43
assert all(row['status']=='PASS' for row in e.ledger)
# Independent checks of corrected inputs and conservation balances.
volume=math.pi*7.5**2*2.5
ballast=volume-4430/1025
assert math.isclose(ballast,437.46451569155244,rel_tol=1e-12)
assert abs((4430+1025*ballast)-1025*volume)<1e-7
for mass,radius,speed in [(2.3e-26,94e-12,514),(2,3,4),(.07,.2,7)]:
 inertia=2*mass*radius**2;omega=speed/radius
 assert math.isclose(2*mass*speed**2,inertia*omega**2,rel_tol=1e-12)
 assert math.isclose(4*mass*radius*speed,2*inertia*omega,rel_tol=1e-12)
 old_v=-.6*speed;old_omega=.8*speed/radius
 old_angular=4*mass*radius*old_v+2*inertia*old_omega
 assert not math.isclose(old_angular,4*mass*radius*speed,rel_tol=.01,abs_tol=0)
scores=[10,20,30,40,50,60,70,80,90,100]
counts=[11,12,24,15,19,10,12,20,17,10]
assert sum(counts)==150
assert sum(x*n for x,n in zip(scores,counts))==8190
assert sum(x*x*n for x,n in zip(scores,counts))==559500
properties={}
# E73/E76: Evaluate the actual moment integrals, not constants compared to themselves.
for a in [.25,1,2]:
 C=4*a**1.5/math.sqrt(math.pi)
 moment2=C*quad(lambda v:v**4*math.exp(-a*v*v),0,np.inf,epsabs=1e-12)[0]
 moment1=C*quad(lambda v:v**3*math.exp(-a*v*v),0,np.inf,epsabs=1e-12)[0]
 assert math.isclose(moment2,3/(2*a),rel_tol=1e-11)
 assert math.isclose(moment1,2/math.sqrt(math.pi*a),rel_tol=1e-11)
properties['73_76_moment_integrals']='three positive Gaussian scales'
# E75: Numerical probabilities distinguish the requested narrow-bin approximation.
intervals=[]
for T in [300,600,150]:
 vmp=math.sqrt(2*e.R*T/.032)
 f=lambda v:4/math.sqrt(math.pi)/vmp**3*v*v*math.exp(-(v/vmp)**2)
 for multiple in [1,7]:
  center=multiple*vmp
  approximate=f(center)*20
  exact=quad(f,center-10,center+10,epsabs=1e-35,epsrel=1e-12)[0]
  relative=abs(exact-approximate)/exact
  assert relative<.05
  intervals.append(dict(T_K=T,multipleOfMostProbable=multiple,width_m_s=20,approximateFraction=approximate,integratedCenteredFraction=exact,relativeApproximationError=relative))
properties['75_actual_intervals']=intervals
# E77: Force obtained directly from the gas law agrees with the nonlinear law.
for mass,radius,height in [(1.2,.08,.5),(3,.1,1),(10,.2,.3)]:
 area=math.pi*radius**2;p0=1.013e5;peq=p0+mass*9.8/area
 force=lambda y:peq*height/(height+y)*area-p0*area-mass*9.8
 for y in [-.2*height,.2*height]:
  assert math.isclose(force(y),-peq*area*y/(height+y),rel_tol=1e-12)
 step=height*1e-6
 derivative=(force(step)-force(-step))/(2*step)
 assert math.isclose(derivative,-peq*area/height,rel_tol=1e-8)
 assert not math.isclose(force(.2*height)/(.2*height),force(-.2*height)/(-.2*height),rel_tol=.01)
properties['77_nonlinear_piston']='gas-law force and small-amplitude derivative at three positive parameter sets'
temperatures=np.array([-195.8,0,33.3,100,232])
pressures=np.array([254,890,999,1214,1635])
slope,intercept=np.polyfit(temperatures,pressures,1)
assert math.isclose(float(slope),3.23021153253,rel_tol=1e-10)
properties['78_independent_least_squares']=dict(slope=float(slope),intercept=float(intercept),absoluteZero_C=float(-intercept/slope),volumeChangeFraction=3.6e-5*(232+195.8))
properties['83_crossing_collisions']=(20*9.46e15)/(1/(4*math.pi*math.sqrt(2)*(5e-11)**2*5e7))
assert properties['83_crossing_collisions']>4e5
for db,intensity in [(140,1e2),(120,1),(95,3.2e-3),(90,1e-3),(70,1e-5),(65,3.2e-6),(50,1e-7),(40,1e-8),(20,1e-10),(10,1e-11),(0,1e-12)]:
 assert math.isclose(1e-12*10**(db/10),intensity,rel_tol=.015)
properties['47_reference_table_rows']=11
for ratio in [1.1,2,4]:
 outside=288.15;inside=outside*ratio
 mass_inside=101300*.01*.0288/(8.3145*inside)
 mass_outside=101300*.01*.0288/(8.3145*outside)
 acceleration=(mass_outside-mass_inside)*9.8/mass_inside
 assert math.isclose(acceleration,9.8*(inside/outside-1),rel_tol=1e-12)
 assert math.isclose(inside,outside*(1+acceleration/9.8),rel_tol=1e-12)
properties['55_all_four_parts']=dict(testTemperatureRatios=[1.1,2,4],illustrativeAccelerationOverG=1,illustrativeTemperature_C=2*288.15-273.15)
venus_speed=math.sqrt(3*8.3145*733.15/.044)
assert math.isclose(venus_speed,644.68,rel_tol=1e-4)
properties['56_same_isothermal_speed_at_both_altitudes_m_s']=venus_speed
initial_moles=101300*.0015/(8.3145*300)
retained_moles=101300*.0015/(8.3145*550)
assert retained_moles<initial_moles
properties['58_open_heating_then_closed_cooling']=dict(initialMoles=initial_moles,retainedMoles=retained_moles,finalPressure_Pa=101300*300/550)
thermal_velocities=np.array([[1.,2.,3.],[-1.,-2.,-3.],[2.,-1.,4.],[-2.,1.,-4.]])
boost=np.array([300.,0.,0.])
assert np.allclose(thermal_velocities.mean(axis=0),0)
initial_energy=.5*np.sum(thermal_velocities**2)
boosted_energy=.5*np.sum((thermal_velocities+boost)**2)
assert math.isclose(boosted_energy-initial_energy,.5*len(thermal_velocities)*float(boost@boost),rel_tol=1e-12)
assert np.allclose((thermal_velocities+boost)-(thermal_velocities+boost).mean(axis=0),thermal_velocities)
properties['68_Galilean_boost']='Bulk kinetic energy changes; velocities relative to the center of mass do not.'
inertia=.5*(.016/6.02214076e23)*(1.21e-10)**2
omega=math.sqrt(1.380649e-23*300/inertia)
machine_omega=10000*2*math.pi/60
assert math.isclose(omega/machine_omega,4.4e9,rel_tol=.01)
properties['74_required_machine_comparison']=dict(molecularOmega_rad_s=omega,machineOmega_rad_s=machine_omega,ratio=omega/machine_omega)
result=dict(status='passed',scope='44 actualD verifier cases,43 actualE case IDs with numerical checks, plus independent corrected buoyancy/angular-momentum/moment/piston/data identities. Source prose and figures remain separate reviews.',numberedCases=87,dCases=results,eChecks=e.ledger,independentPropertyChecks=properties,correctedBellRadius_m=7.5,correctedBallast_m3=ballast,sourceScoreCounts=counts)
(Q/'ch18-numbered-parent-ledger.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(status='passed',dCases=len(results),eCaseIds=43,eChecks=len(e.ledger),sourceRadius_m=7.5,ballast_m3=ballast)))
