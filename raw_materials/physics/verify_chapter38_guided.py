from math import pi,cos,acos,degrees,sqrt,isclose
import json
h=6.626e-34;c=2.998e8;e=1.602e-19;me=9.109e-31;hbar=h/(2*pi)
lambdaC=h/(me*c)
r={}
lam=625e-9;E=h*c/lam
r['VP38.3.1']={'a_E_J':E,'a_p_kg_m_s':h/lam,'b_power_W':2.13e16*E}
r['VP38.3.2']={'a_threshold_Hz':4.55*e/h,'b_frequency_Hz':(4.55+1.53)*e/h}
phi=h*c/(475e-9)/e-1.37
r['VP38.3.3']={'a_work_function_eV':phi,'b_stopping_V':h*c/(425e-9)/e-phi}
K=.5*me*(6.95e5)**2;E=h*c/(306e-9)
r['VP38.3.4']={'a_K_eV':K/e,'b_photon_eV':E/e,'c_work_function_eV':(E-K)/e}
shift=lambdaC*(1-cos(14.5*pi/180))
r['VP38.6.1']={'a_shift_nm':shift/1e-9,'b_percent':shift/(.251e-9)*100}
fin=1.260e18;lam=c/fin
r['VP38.6.2']={'a_frequency90_Hz':c/(lam+lambdaC),'b_frequency180_Hz':c/(lam+2*lambdaC)}
mp=1.673e-27;lcproton=h/(mp*c);lam=2.5e-12
r['VP38.6.3']={str(percent):degrees(acos(1-(percent/100)*lam/lcproton)) for percent in [.0100,.0800]}
r['VP38.6.4']={str(K):{'energy_each_MeV':938.3+K,'wavelength_each_m':h*c/((938.3+K)*1e6*e)} for K in [0,545]}
lam=633e-9;L=7e-6;p=h/lam;dp=hbar/(2*L);E=p*c;dE=dp*c
r['VP38.7.1']={'a_p_kg_m_s':p,'b_dpmin_kg_m_s':dp,'b_percent':dp/p*100,'c_E_J':E,'d_dEmin_J':dE,'d_percent':dE/E*100}
f=3e9;dE=5.5e-29;t=hbar/(2*dE)
r['VP38.7.2']={'a_duration_s':t,'b_length_m':c*t,'c_photon_J':h*f,'d_dfmin_Hz':dE/h}
dE=2.33e-20;E=dE/.067
r['VP38.7.3']={'a_wavelength_m':h*c/E,'a_frequency_Hz':E/h,'b_dfmin_Hz':dE/h,'c_duration_s':hbar/(2*dE)}
E=2.39*e;dE=.0155*e
r['VP38.7.4']={'a_duration_s':hbar/(2*dE),'b_wavelength_m':h*c/E,'c_pulse_energy_J':5e12*E,'c_pulse_energy_microJ':5e12*E*1e6}
scattered=.0830e-9;incident=scattered-2*lambdaC;p=h/incident+h/scattered
Eelectron=sqrt((me*c*c)**2+(p*c)**2);Kexact=(p*c)**2/(Eelectron+me*c*c);v=p*c*c/Eelectron;Knon=p*p/(2*me);Kphotons=h*c/incident-h*c/scattered
assert isclose(Kexact,Kphotons,rel_tol=1e-12)
assert v/c<.1
r['bridge']={'a_incident_wavelength_nm':incident*1e9,'b_electron_p_kg_m_s':p,'b_exact_speed_m_s':v,'b_nonrel_speed_m_s':p/me,'c_exact_K_J':Kexact,'c_nonrel_K_J':Knon,'energy_difference_J':Kphotons}
assert len(r)==13
assert isclose(r['VP38.7.4']['c_pulse_energy_J'],1.91439e-6,rel_tol=1e-12)
for key in ['VP38.7.1','VP38.7.2','VP38.7.3','VP38.7.4']:assert r[key]
print(json.dumps(dict(status='passed',constants=dict(h=h,c=c,e=e,me=me,hbar=hbar),tasks=r),indent=2))
