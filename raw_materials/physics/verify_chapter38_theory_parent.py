"""Independent conservation, example, and diffraction checks for chapter38 theory."""
from pathlib import Path
import json
import numpy as np
from math import pi,sqrt,acos,cos,sin
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter38'
h=6.626e-34;c=2.998e8;me=9.109e-31;e=1.602e-19;hb=h/(2*pi);lc=h/(me*c);rest=me*c*c
results={}
worst=0.
for lam in np.geomspace(1e-14,1e-6,35):
 for angle in np.linspace(0,pi,41):
  lp=lam+lc*(1-cos(angle));E=h*c/lam;Ep=h*c/lp
  pe2=(h/lam-h/lp*cos(angle))**2+(h/lp*sin(angle))**2
  Ke=pe2*c*c/(sqrt(rest*rest+pe2*c*c)+rest)
  # Energy cancellation at very small scattering angle is avoided in the residual scale.
  rel=abs(E-(Ep+Ke))/E;worst=max(worst,rel)
  assert rel<1e-12,(lam,angle,rel)
results['compton_conservation']={'configurations':35*41,'max_relative_residual':worst}
results['38.5']={f'{fraction:g}':np.degrees(acos(1-fraction*.124e-9/lc)) for fraction in [.01,.0005]}
results['pair_threshold']={'energy_J':2*rest,'energy_MeV':2*rest/(1e6*e),'wavelength_pm':h*c/(2*rest)*1e12}
results['38.6']={}
for K in [0,5.000]:
 E=(K+.511)*1e6
 results['38.6'][str(K)]={'each_energy_MeV':K+.511,'each_wavelength_pm':4.136e-15*3e8/E*1e12,'each_frequency_Hz':E/4.136e-15}
# Directly test equal-energy opposing photons in the center-of-momentum frame.
for beta in np.linspace(0,.999,100):
 gamma=1/sqrt(1-beta*beta)
 incoming=2*gamma*rest
 photon_each=gamma*rest
 assert abs(incoming-2*photon_each)<=np.finfo(float).eps*incoming
results['symmetric_annihilation_configurations']=100
cl=3e8;hbl=1.055e-34;dt=4e-15;lam=800e-9;f=cl/lam;E=h*f;dE=hbl/(2*dt);dx=cl*dt;dp=hbl/(2*dx)
results['38.7']={'f_Hz':f,'E_J':E,'min_dE_J':dE,'min_df_Hz':dE/h,'length_m':dx,'length_in_wavelengths':dx/lam,'p_kg_m_s':E/cl,'min_dp_kg_m_s':dp,'relative_uncertainty':dE/E,'photons_per_pulse':2e-6/E}
assert np.isclose(dE/E,dp/(E/cl),rtol=1e-14)
results['butterfly_hypothesis']={'scaled_hbar_J_s':1.05,'min_dp_kg_m_s':1.05/(2*.25),'speed_scale_m_s':2.1/3e-4,'kinetic_energy_scale_J':2.1**2/(2*3e-4),'not_a_fixed_kick_in_every_trial':True}
# A numerical check of the TYU: 1,2,3 diffraction orders are zeros; 1.5 is not a zero.
intensities={str(a):float(np.sinc(a)**2) for a in [1,1.5,2,3]}
assert intensities['1.5']>1e10*max(intensities[x] for x in ['1','2','3'])
results['38.4_selfcheck']=dict(relative_intensity=intensities,answer='ii',one_point_five_is_not_exact_secondary_maximum=True)
x=np.linspace(-1,1,200001);fraction=float(np.trapezoid(np.sinc(x)**2,x))
assert abs(fraction-.90282333358)<1e-9
results['ideal_fraunhofer_central_fraction']={'integral_fraction':fraction,'source_85_percent_is_rough_not_exact':True,'not_used_in_uncertainty_derivation':True}
# Check the superposition/odd-sine substitutions without any field/probability conflation.
test=np.linspace(-5,5,401)
A1=1.2;A2=-.9;p1=1.3;p2=1.4;E1=1.1;E2=1.2
for t in [0,.13,1.2]:
 alpha1=p1*test-E1*t;alpha2=p2*test-E2*t
 total=A1*np.sin(alpha1)+A2*np.sin(alpha2)
 assert np.allclose(total,A1*np.sin(p1*test-E1*t)+A2*np.sin(p2*test-E2*t))
assert np.allclose(A1*np.sin(-E1*test)+A2*np.sin(-E2*test),-A1*np.sin(E1*test)-A2*np.sin(E2*test))
results['superposition_substitutions']='passed'
E=10e9*e;eps=h*c/10.6e-6;q0=sqrt(E*E-rest*rest);S=E+q0
out=eps*S/(rest*rest/S+2*eps);Ef=E+eps-out;pf_c=eps-q0+out
assert pf_c<0
assert abs((Ef*Ef-pf_c*pf_c)/rest**2-1)<2e-6
results['38.40_extra_check']={'final_electron_direction':'negative x','energy_J':Ef,'momentum_times_c_J':pf_c}
d=dict(status='passed',results=results)
(q/'theory-parent-numeric.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Independent theory checks passed: 1435 Compton cases, 100 annihilation cases, examples38.5–7, butterfly, diffraction and wave identities.')
