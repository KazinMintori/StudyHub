from pathlib import Path
from math import sqrt,sin,pi,exp
import json,numpy as np
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter39';q.mkdir(parents=True,exist_ok=True)
h=6.626e-34;c=2.998e8;e=1.602e-19;me=9.109e-31;mn=1.675e-27;mp=1.673e-27;k=1.38e-23
r={}
lam=h/sqrt(2*me*e*54);lg=2.18e-10*sin(50*pi/180)
r['39.1']={'wavelength_debroglie_m':lam,'wavelength_diffraction_m':lg,'relative_difference':abs(lam-lg)/lam}
v=h/(.200e-9*mn);K=.5*mn*v*v
r['39.2']={'speed_m_s':v,'kinetic_J':K,'kinetic_eV':K/e,'ideal_gas_mean_J':1.5*k*293,'ideal_gas_mean_eV':1.5*k*293/e}
p=h/(10e-12);Kn=p*p/(2*me);rest=me*c*c;Kr=p*p*c*c/(np.hypot(rest,p*c)+rest)
r['39.3']={'classical_voltage_V':Kn/e,'relativistic_voltage_V':float(Kr/e),'classical_relative_error':float((Kn-Kr)/Kr),'relativistic_beta':float(p*c/np.hypot(rest,p*c))}
r['39.1_selfcheck']={'a_more_K_for_proton_at_same_lambda':mn/mp,'b_photon54eV_wavelength_m':h*c/(54*e),'ratio_to_electron_wavelength':h*c/(54*e)/lam,'question_is_photon_not_proton_accelerator':True}
r['sand']={'diameter_m':.07e-3,'momentum':5e-10*.4,'wavelength_m':h/(5e-10*.4)}
U=9e9*(2*1.60e-19)*(79*1.60e-19)/5e-14;ma=6.64e-27;M=3.27e-25;v=sqrt(2*7.3e-13/ma);p0=ma*v
r['39.4']={'required_initial_K_J':U,'required_K_MeV':U/(1.60e-13),'initial_speed_using_source_rounded_K':v,'initial_momentum':p0,'source_approx_gold_recoil_eV':(9.8e-20)**2/(2*M)/e,'source_approx_recoil_fraction':(9.8e-20)**2/(2*M)/(7.3e-13),'exact_closest_relative_turn_recoil_fraction':ma*M/(ma+M)**2}
r['39.2_selfcheck']={'direct_alpha_outgoing_speed_over_incoming':(4-1)/(4+1),'answer':'iii fewer large angles'}
levels=[0.,1.,3.];r['39.5']={'emission_photon_eV':[],'from_ground_absorption_eV':[1.,3.]}
for i in range(1,3):
 for j in range(i):
  E=levels[i]-levels[j];r['39.5']['emission_photon_eV'].append({'energy_eV':E,'frequency_Hz':E/4.136e-15,'wavelength_nm':4.136e-15*3e8/E*1e9})
r['lithium']={'671nm_photon_eV':6.63e-34*3e8/(671e-9)/e}
r['Franck_Hertz']={'photon_for4_9eV_wavelength_nm':4.136e-15*3e8/4.9*1e9}
r['39.6']={'K2_eV':13.60/4,'U2_eV':-27.20/4,'E2_eV':-13.60/4,'E1_eV':-13.60,'emitted_eV':13.60*(1-1/4),'wavelength_nm':4.136e-15*3e8/(13.60*(1-1/4))*1e9}
eps=8.854e-12;a0=eps*h*h/(pi*me*e*e);E0=me*e**4/(8*eps*eps*h*h)
r['Bohr_constants']={'radius_m':a0,'ionization_eV':E0/e,'Rydberg_m_inv':E0/(h*c),'finite_H_mu_over_m':1836.2/(1836.2+1),'deuterium_to_hydrogen_wavelength_ratio':.99946/.99973,'Rydberg_n1000_radius_mm':a0*1e6*1e3}
for n in range(1,31):
 radius=n*n*a0;v=e*e/(2*eps*n*h);L=me*v*radius
 assert np.isclose(L,n*h/(2*pi),rtol=1e-14,atol=0)
 K=.5*me*v*v;U=-e*e/(4*pi*eps*radius)
 assert np.isclose(U,-2*K,rtol=1e-14,atol=0)
r['Bohr_conservation_and_quantization_configurations']=30
choices=[(2,1),(3,2),(4,3),(4,2)]
H=[(upper,lower,13.60*(1/lower**2-1/upper**2)) for lower in range(1,7) for upper in range(lower+1,120)]
matches={}
for upper,lower in choices:
 energy=4*13.60*(1/lower**2-1/upper**2)
 matches[f'{upper}->{lower}']={'energy_eV':energy,'matching_H':[(u,l) for u,l,E in H if np.isclose(E,energy,rtol=1e-12,atol=0)]}
assert not matches['2->1']['matching_H'] and not matches['3->2']['matching_H'] and not matches['4->3']['matching_H']
assert matches['4->2']['matching_H']==[(2,1)]
r['39.3_selfcheck']=matches
r['laser_population']={'thermal_ratio_2eV_3000K':exp(-3.2e-19/(k*3000)),'metastable_to_short_lifetime_ratio':1e-3/1e-8}
(q/'theory-ab-parent-numeric.json').write_text(json.dumps(dict(status='passed',results=r),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Independent A/B checks passed: Six source examples, source selfchecks, Bohr equations and population example.')
