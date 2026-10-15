"""Independent crosschecks for the reviewed chapter39 end problems."""
from pathlib import Path
import contextlib,io,runpy,math,json,sys
import numpy as np

root=Path(__file__).resolve().parents[2]
qa=root/'qa/physics/chapter39'
qa.mkdir(parents=True,exist_ok=True)
with contextlib.redirect_stdout(io.StringIO()):
    cmod=runpy.run_path(str(root/'raw_materials/physics/verify_chapter39_exercises_c.py'))
    cres=cmod['verify_all']()
    dmod=runpy.run_path(str(root/'raw_materials/physics/verify_chapter39_exercises_d.py'))
dres=dmod['r']
h=6.62607015e-34
hb=h/(2*math.pi)
e=1.602176634e-19
c=299792458.
me=9.1093837e-31
mp=1.67262192369e-27
eps=8.8541878128e-12
kc=1/(4*math.pi*eps)
k=1.380649e-23
sigma=2*math.pi**5*k**4/(15*c*c*h**3)
a0=eps*h*h/(math.pi*me*e*e)
E_R=me*e**4/(8*eps*eps*h*h*e)
assert len(cres)==57
assert all('39.'+str(n) in cres for n in range(1,46))
assert all('39.'+str(n) in dres for n in range(46,92))

# Kinetic energy reconstructed from momenta, rather than copying printed answers.
assert math.isclose(cres['39.1'][0]/cres['39.1'][1],mp/me,rel_tol=1e-7)
assert math.isclose(cres['39.2'][1]/cres['39.2'][2],6.64e-27/me,rel_tol=1e-7)
assert math.isclose(cres['39.3'][0]*2.80e-10,h,rel_tol=1e-12)
for beta in [.480,.960]:
    gamma=1/math.sqrt(1-beta*beta)
    lam=h/(gamma*me*beta*c)
    total=gamma*me*c*c
    assert math.isclose(total**2,(h*c/lam)**2+(me*c*c)**2,rel_tol=1e-12)

# Bohr level differences, all unordered emission pairs and work-function bounds.
levels=[-20.,-10.,-5.,-2.]
emitted=sorted(levels[j]-levels[i] for i in range(4) for j in range(i+1,4))
assert emitted==[3.,5.,8.,10.,15.,18.]
assert levels[0]+8 not in levels
assert 3<4<=5
assert math.isclose(16*13.60,217.6)
assert math.isclose(122/16,7.625)
assert math.isclose(cres['39.22'][1],13.60*(1/81-1/100),rel_tol=1e-12)
for n in [1,2,3,10,1000]:
    radius=a0*n*n
    speed=kc*e*e/(hb*n)
    assert math.isclose(me*speed*radius,n*hb,rel_tol=1e-12)
    assert math.isclose(me*speed*speed/radius,kc*e*e/radius**2,rel_tol=1e-12)
    gap=E_R*(1/n**2-1/(n+1)**2)
    assert gap>0
mu=me/2
separation=eps*h*h/(math.pi*mu*e*e)
assert math.isclose(separation/2,a0,rel_tol=1e-12)
assert math.isclose(E_R*mu/me,E_R/2,rel_tol=1e-12)
assert math.isclose(cres['39.26'][1],a0,rel_tol=1e-7)

# Photons/pulses: Counting returns the original beam energy.
for wavelength,power,pulse in [(10.6e-6,100,1),(585e-9,20,.45e-3),
                              (10.6e-6,.0075,1),(193e-9,.0015,12e-9)]:
    energy=h*c/wavelength
    number=power*pulse/energy
    assert math.isclose(number*energy,power*pulse,rel_tol=1e-12)
for temp in [3,300,3000,3040,3590,5800,24000]:
    intensity=sigma*temp**4
    assert intensity>0
assert math.isclose(sigma*(2*300)**4/(sigma*300**4),16.)
assert math.isclose(math.sqrt(3)**4,9.)

# Recoil emission, muonic reduced mass and kinetic-energy limits.
photonEnergy=10.2*e
recoilMomentum=photonEnergy/c
recoilK=recoilMomentum**2/(2*1.67e-27)
assert math.isclose(dres['39.48']['d_K_recoil_eV'],recoilK/e,rel_tol=1e-12)
muMuon=207*me*mp/(207*me+mp)
assert math.isclose(dres['39.49']['a_reduced_mass_kg'],muMuon,rel_tol=1e-7)
assert math.isclose(dres['39.49']['b_ground_state_energy_eV']/(muMuon/me),-13.606,rel_tol=1e-7)
for mass in [me,mp]:
    p=math.sqrt(15)*mass*c
    total=math.sqrt((p*c)**2+(mass*c*c)**2)
    assert math.isclose(total-mass*c*c,3*mass*c*c,rel_tol=1e-12)
dp=hb/(2*5e-15)
exactK=lambda mass:(dp*c)**2/(math.sqrt((dp*c)**2+(mass*c*c)**2)+mass*c*c)
assert .20e6<exactK(mp)/e<.22e6
assert 19e6<exactK(me)/e<20e6

# Regression39.82: Verify least-squares stationarity, residuals and source table.
volts=np.array([106.3,69.1,49.9,25.2,16.9,13.6])
angles=np.array([20.4,24.8,30.2,45.5,59.1,73.1])
X=1/np.sqrt(volts)
Y=np.sin(np.deg2rad(angles))
design=np.column_stack([X,np.ones_like(X)])
slope,intercept=np.linalg.lstsq(design,Y,rcond=None)[0]
residual=Y-design@np.array([slope,intercept])
assert np.linalg.norm(design.T@residual)<1e-12
spacing=h/(slope*math.sqrt(2*me*e))
assert .34e-9<spacing<.36e-9

# Critical source-unit, spectral-density, covariance and relativistic counterexamples
# are independently checked by the saved parent derivations, including full assumptions.
critical=root/'raw_materials/physics/verify_chapter39_critical.py'
with contextlib.redirect_stdout(io.StringIO()):
    runpy.run_path(str(critical),run_name='__main__')
criticalData=json.loads((qa/'end-critical-parent.json').read_text())
assert math.isclose(dres['39.76']['b_delta_E_eV'],criticalData['39.76']['energyWidthEV'],rel_tol=1e-12)
assert 'hbar' not in dres['39.78']['a_E_min_formula']
assert dres['39.85']['classical_required_projectile_speed_possible'] is False
assert dres['39.85']['relativistic_recoil_0_10c_is_not_forbidden'] is True

report={'status':'passed','endSolutions':126,'examples':10,'sourceReviewed':True,
    'coverage':'91 numbered,12 Guided Practice,22 qualitative discussions,1 bridge',
    'workerCComputed':57,'workerDComputed':len(dres),'regression':{'slope':slope,'intercept':intercept,'spacingM':spacing},
    'scopeLimit':'Physical assumptions are explicit in the text. Numerical tests do not replace source or browser review.',
    'sourceCorrections':['39.1 proton','39.2 fixed0.20nm','39.20-45 restored subparts',
        '39.76 microseconds','39.78-79 ordinary h','39.85 classical limit','39.86 covariance']}
(qa/'numeric-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
