from pathlib import Path
import json
from math import pi,exp,log,log1p,sqrt
import numpy as np
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter39';q.mkdir(parents=True,exist_ok=True)
h=6.62607015e-34;c=299792458.;k=1.380649e-23;e=1.602176634e-19;hb=h/(2*pi)
sigma=2*pi**5*k**4/(15*c*c*h**3)
assert np.isclose(sigma,5.670374419e-8,rtol=1e-10)
lo=4.;hi=5.
for _ in range(80):
 x=(lo+hi)/2
 if 5*(-np.expm1(-x))-x>0:lo=x
 else:hi=x
xpeak=(lo+hi)/2;b=h*c/(xpeak*k)
t=np.linspace(1e-8,60,150001);J=float(np.trapezoid(t**3/np.expm1(t),t))
assert abs(J-pi**4/15)<1e-9
def planck(lam,T,h=h,c=c,k=k):
 x=h*c/(np.asarray(lam)*k*T)
 return 2*pi*h*c*c/np.asarray(lam)**5/np.expm1(x)
def logplanck(lam,T):
 x=h*c/(lam*k*T)
 denom=x+log1p(-exp(-x)) if x>50 else log(np.expm1(x))
 return log(2*pi*h*c*c)-5*log(lam)-denom
results={
 'planck_constants':{'positive_peak_root':xpeak,'wien_m_K':b,'sigma_W_m2_K4':sigma,'dimensionless_integral':J,'expected_integral':pi**4/15},
 'sunspot_relative_intensity':(4000/5800)**4,
 'blackbody_eyes_300K_peak_m':2.90e-3/300,
 'star_peaks_m':{str(T):2.90e-3/T for T in [12000,3000,5800]},
}
hr=6.626e-34;cr=2.998e8;kr=1.381e-23;er=1.602e-19;hbr=1.055e-34
pop={}
for lam in [3e-6,.5e-6]:
 E=hr*cr/lam;r=exp(-E/(kr*2000))
 pop[str(lam)]={'photon_eV':E/er,'N1_over_N0':r,'N1_over_Ntotal_full_ladder':r*(1-r)}
results['population_ratios_at2000K']=pop
I=5.67e-8*5800**4;factor=(6.96e8/1.50e11)**2
results['39.7']={'peak_m':2.90e-3/5800,'surface_W_m2':I,'geometric_reduction_factor':factor,'at_earth_W_m2':I*factor}
lam=602.5e-9;T=5800;interval=5e-9
mid=float(planck(lam,T,hr,cr,kr))*interval
grid=np.linspace(600e-9,605e-9,2001);numeric=float(np.trapezoid(planck(grid,T,hr,cr,kr),grid))
results['39.8']={'x':hr*cr/(lam*kr*T),'spectral_W_m3':float(planck(lam,T,hr,cr,kr)),'midpoint_band_W_m2':mid,'numerical_integral_band_W_m2':numeric,'relative_midpoint_error':abs(mid-numeric)/numeric,'fraction_of_total':mid/I}
assert abs(mid-numeric)/numeric<1e-4
dx=5.000e-11;dp=hbr/(2*dx);me=9.11e-31;K=dp*dp/(2*me)
p_nuc=hbr/(2e-14);rest=me*cr*cr;K_nuc=(p_nuc*cr)**2/(np.hypot(rest,p_nuc*cr)+rest)
results['39.9']={'estimate_position_width_m':dx,'min_dp_kg_m_s':dp,'associated_K_J':K,'associated_K_eV':K/er,'nuclear_confinement_dp_factor':p_nuc/dp,'nuclear_confinement_relativistic_K_MeV':float(K_nuc/er/1e6)}
dt=1.6e-8;dE=hbr/(2*dt);E=2.105*er
results['39.10']={'min_dE_J':dE,'min_dE_eV':dE/er,'fraction_unrounded':dE/E,'wavelength_width_nm_unrounded':589.0*dE/E,'wavelength_width_nm_with_source_intermediate_rounding':589.0*1.0e-8,'profile_caveat':'Lifetime-energy scale; convention for spectral width must be specified, not a generic standard deviation.'}
results['39.5_selfcheck']={'xray_0_1nm_log_spectral_SI':logplanck(1e-10,2000),'radio_1m_log_spectral_SI':logplanck(1,2000),'positive_at_every_finite_positive_wavelength':True}
results['39.6_selfcheck']={'minimum_bounds_kg_m_s':{'i':hb/(2*2e-15),'ii':hb/(2*4e-15),'iii':hb/(2*2e-15),'iv':hb/(2*4e-15)},'ranking_of_lower_bounds':'i=iii>ii=iv','actual_spreads_not_determined_by_position_bounds_alone':True}
# Scaling and Rayleigh-Jeans limit checked separately from the peak equation.
vals=[]
for T in [1250,1750,2000]:
 lam=b/T;vals.append(float(planck(lam,T)/T**5))
assert np.allclose(vals,vals[0],rtol=1e-14,atol=0)
x=1e-7
assert abs(x/np.expm1(x)-1)<1e-6
results['scaling_and_classical_limit']='passed'
(q/'theory-parent-numeric.json').write_text(json.dumps(dict(status='passed',results=results),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results,ensure_ascii=False,indent=2))
