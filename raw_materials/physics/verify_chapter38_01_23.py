from math import sqrt,pi,cos,acos,degrees,isclose
import json
h=6.626e-34;c=2.998e8;e=1.602e-19;me=9.109e-31;mp=1.673e-27;hb=h/(2*pi);lc=h/(me*c)
def photon(l):return dict(f_Hz=c/l,p_kg_m_s=h/l,E_J=h*c/l,E_eV=h*c/l/e)
r={}
r['38.1']=photon(520e-9)
E=h*c/(505e-9);r['38.2']={**photon(505e-9),'bacterium_mass_kg':9.5e-15,'bacterium_speed_m_s':sqrt(2*E/(9.5e-15))}
E=h*c/(600e-9);r['38.3']={'frequency_Hz':c/(600e-9),'photons_per_s':75/E}
E=h*c/(652e-9);r['38.4']={'pulse_energy_J':.6*.020,'pulse_energy_eV':.6*.020/e,'photon_J':E,'photon_eV':E/e,'photons_per_pulse':.6*.020/E}
p=8.24e-28;r['38.5']={'energy_J':p*c,'energy_eV':p*c/e,'wavelength_m':h/p,'region':'near infrared'}
K=h*c/(235e-9)-5.1*e;r['38.6']={'kinetic_J':K,'max_speed_m_s':sqrt(2*K/me),'work_function_eV':5.1}
r['38.7']={'new_K_eV':1.1+h*c/e*(1/(300e-9)-1/(400e-9))}
K=h*c/(190e-9)-2.3*e;r['38.8']={'stopping_V':K/e,'K_eV':K/e,'speed_m_s':sqrt(2*K/me)}
phi=h*c/(254e-9)-.181*e;r['38.9']={'threshold_wavelength_m':h*c/phi,'work_function_eV':phi/e,'table_copper_eV':4.7}
r['38.10']={'minimum_wavelength_m':h*c/(15e3*e)}
E=.7*50e3*e;r['38.11']={'energy_eV':E/e,'frequency_Hz':E/h,'wavelength_m':h*c/E,'momentum_kg_m_s':E/c}
r['38.12']={'a_min_voltage_V':h*c/(.150e-9*e),'b_min_wavelength_m':h*c/(30e3*e)}
K=h*c/(.100e-9)-h*c/(.110e-9)
r['38.13']={'energy_only_K_J':K,'energy_only_K_eV':K/e,'given_shift_m':.010e-9,'maximum_free_electron_shift_m':2*lc,'free_electron_single_Compton_possible':False}
assert .010e-9>2*lc
lam=h*c/(24e3*e);sc=lam+lc*(1-cos(pi/4));r['38.14']={'initial_wavelength_m':lam,'scattered_wavelength_m':sc,'scattered_energy_eV':h*c/(sc*e)}
r['38.15']={'longest_wavelength_m':.0665e-9+2*lc,'angle_deg':180}
v=8.9e6;gamma=1/sqrt(1-v*v/c**2);K=(gamma-1)*me*c*c;lam=.1385e-9;sc=h*c/(h*c/lam-K);co=1-(sc-lam)/lc
assert -1<=co<=1
r['38.16']={'exact_angle_deg':degrees(acos(co)),'electron_K_J':K,'scattered_wavelength_m':sc}
lam=.04250e-9;dl=lc*(1-cos(35*pi/180));sc=lam+dl;change=h*c/sc-h*c/lam
r['38.17']={'a_shift_m':dl,'b_scattered_wavelength_m':sc,'c_photon_change_J':change,'d_electron_gain_J':-change}
r['38.18']={'incident_wavelength_m':2*h/(mp*c)/.1}
Ei=2*me*c*c;Es=Ei/(1+Ei/(me*c*c)*(1-cos(20*pi/180)))
r['38.19']={'nonzero_scatter_keeps_pair_threshold':False,'b_scattered_momentum_kg_m_s':Es/c,'scattered_energy_MeV':Es/(1e6*e)}
gamma=1/sqrt(1-.5**2);E0=me*c*c;E=gamma*E0
r['38.20']={'a_K_each_eV':(gamma-1)*E0/e,'b_photon_eV':E/e,'c_photon_wavelength_m':h*c/E,'rest_annihilation_wavelength_m':h*c/E0,'wavelength_ratio':1/gamma}
t=9e-15;L=c*t;r['38.21']={'momentum_kg_m_s':h/(556e-9),'min_uncertainty_kg_m_s':hb/(2*L)}
a=.0620e-3;R=2;lam=585e-9;dp=hb/(2*a);p=h/lam
r['38.22']={'a_min_vertical_dp':dp,'b_min_two_sigma_screen_scale_m':2*R*dp/p,'actual_central_max_width_small_angle_m':2*R*lam/a,'caveat':'Uncertainty lower bound is not the first-minimum width; exact hard-slit variance also requires care.'}
r['38.23']={'minimum_duration_s':hb/(2*.01*h*c/(625e-9))}
assert len(r)==23
print(json.dumps(dict(status='passed',results=r),indent=2))
