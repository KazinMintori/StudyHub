"""Independent numerical ledger for actual chapter43 advanced end problems."""
from pathlib import Path
import math,json,runpy
ROOT=Path(__file__).resolve().parents[2];out={}
u=931.494;H=1.007825;n=1.008665;me=.000548579909;NA=6.02214076e23;e=1.602176634e-19;h=6.62607015e-34;c=299792458.;yr=3.156e7
def save(key,**data):
 assert all(math.isfinite(v) for v in data.values() if isinstance(v,(float,int)))
 out[key]=data
def Q(*masses):return sum(masses)*u
save('43.33',D_Gy=1750,E_J=1750*.220,Hx_Sv=1750,He_Sv=1750*1.5)
save('43.34',equivalent_exams=.012*75/(.00020*5))
N=1e-6/90*NA;dn=N*(1-2**(-1/29));E=dn*1.1e6*e
save('43.35',N0=N,decays_year=dn,energy_J=E,D_Gy=E/50,H_Sv=E/50)
save('43.36',H_rem=540,D_rad=540,E_J=5.4*65,heat_water_J=65*4190*.010)
E=5e10*h*c/(.0200e-9);save('43.37',E_J=E,H_rem=E/.600*100)
save('43.38',Q_MeV=Q(H,3.016049,-2*2.014102))
barrier=1.43996448*4/(1.2*(2**(1/3)+9**(1/3)))
save('43.39',Z_X=3,A_X=7,Q_MeV=Q(2.014102,9.012183,-7.016003,-4.002603),barrier_CM_MeV=barrier,barrier_lab_MeV=barrier*(2+9)/9)
save('43.40',Q_MeV=Q(3.016029,2.014102,-4.002603,-H))
q=Q(235.043930,-143.922953,-88.917631,-2*1.0086649);save('43.41',Q_MeV=q,E_MeV_g=q*NA/235.043930)
save('43.42',Z_X=2,A_X=4,photon_no_recoil_MeV=Q(23.985042,4.002603,-27.976927))
save('43.43',Z_X=5,A_X=10,Q_MeV=Q(4.002603,7.016003,-10.012937,-n))
q=Q(10.013535,-10.012937);g=1+q/.51099895;save('43.44',Q_MeV=q,electron_endpoint_beta=math.sqrt(1-g**-2))
gas=1.3e8/(3.788e-3*737*1000);fission=200e6*e*NA/235;sixp=26.7e6*e/(6*1.67262192369e-24)
save('43.45',gasoline_J_g=gas,fission_J_g=fission,fusion_J_g_six_protons=sixp,sun_gasoline_years=1.99e33*gas/3.86e26/yr)
save('43.46',proton_separation_MeV=Q(11.009305,H,-12),mean_binding_MeV=Q(6*H,6*n,-12)/12)
save('43.47',neutron_separation_MeV=Q(15.994915,n,-16.999132),mean_binding_MeV=Q(8*H,9*n,-16.999132)/17)
N=31e-6/238*NA;lam=math.log(2)/(4.47e9*yr);a=N*lam;p=a*52e6*e;pu=p*4e24
save('43.48',N_per_kg=N,lambda_s=lam,A_Bq_kg=a,p_W_kg=p,uraniumHeat_W=pu,radiogenicHeat_W=pu/.39,totalHeat_W=2*pu/.39)
save('43.49',Z_daughter=39,A_daughter=90,fraction_after56yr=.25,time_to_6_25percent_yr=112)
q=Q(230.033134,-226.025410,-4.002603);ka=q*226.025410/(226.025410+4.002603)
save('43.50',Q_MeV=q,K_alpha_MeV=ka)
save('43.51',beta_plus_Q_MeV=Q(24.990428,-24.985837,-2*me),EC_Q_MeV=Q(24.990428,-24.985837))
R=3.8e26/(26.73e6*e);intercept=(6370e3)**2/(4*(150e9)**2);area=math.pi*(6370e5)**2
save('43.52',fusion_s=R,neutrinos_s=2*R,intercept_fraction=intercept,earth_neutrinos_s=2*R*intercept,earth_area_cm2=area,flux_cm2_s=2*R*intercept/area)
q=Q(14.003242,-14.003074);A=75*.18*1000*.255;P=A*q*1e6*e;D=P*yr/75
save('43.53',Q_MeV=q,carbon_g=75*.18*1000,A_Bq=A,P_MeV_s=A*q,P_W=P,D_Gy=D,D_rad=100*D,H_Sv=1.5*D,H_rem=150*D)
Egamma=264*.51099895/2;save('43.54',photon_MeV=Egamma,wavelength_m=h*c/(Egamma*1e6*e),neededPions=.025*2/(2*Egamma*1e6*e))
save('43.55',mass_difference_u=11.011434-11.009305,available_mass_u=11.011434-11.009305-2*me,Q_MeV=Q(11.011434,-11.009305,-2*me))
A=.52e-6*3.7e10;E=A*yr*4e6*e;save('43.56',A_Bq=A,E_J=E,D_Gy=E/.5,H_Sv=20*E/.5)
save('43.57',half_lives=1e10/2e5,log10_remaining=-50000*math.log10(2))
E=7.75e12*4.77e6*e;A=math.log(2)/(1600*yr)*.032/226*NA
save('43.58',E_J=E,D_rad=E/70*100,H_rem=E/70*2000,A_Bq=A,time_s=7.75e12/A)
r=.2783/(1-.2783)*2**(4.6e9/4.75e10);save('43.59',initial_Rb87_fraction=r/(1+r))
save('43.60',ratio_after3min=2**(180*(1/26.9-1/122.2)),ratio_after12min=2**(720*(1/26.9-1/122.2)))
P=.5*2.6e-4*3.7e10*1.25e6*e;rate=P/.2*100;save('43.61',P_W=P,rad_per_s=rate,rem_per_s=.7*rate,time_s=200/(.7*rate))
E1=Q(2*H,-2.014102)-2*.51099895;mdc2=1875.613;enu=2*E1/(1+math.sqrt(1+2*E1/mdc2));total=Q(4*H,-4.002603)
save('43.62',E1_MeV=E1,neutrino_MeV_two_body_model=enu,fraction_E1=enu/E1,total_neutrino_MeV=2*enu,chain_fraction_two_body_model=2*enu/total)
q1=Q(3.016029,4.002603,-7.016930);q2=Q(7.016930,-7.016003);q3=Q(H,7.016003,-2*4.002603)
save('43.63',gamma_MeV=q1,EC_neutrino_MeV=q2,Li_reaction_MeV=q3,alpha_speed=math.sqrt(q3*1e6*e/(4.002603*1.6605390666e-27)),total_MeV=total,neutrino_fraction_approx=(enu+q2)/total)
endpoint=Q(8.024607,-8.0053051,-2*me);save('43.64',total_MeV=total,neutrino_endpoint_MeV=endpoint,upper_fraction=(endpoint+E1)/total)
save('43.65',age_yr=-5730/math.log(2)*math.log(.29))
equiv_decay=(.51*1.5+.66)*1e6*e;lam=math.log(2)/(30.07*yr);N=3.5/(equiv_decay*(1-math.exp(-lam*7*86400)))
save('43.66',N_Cs137_per_kg=N,mass_Cs137_g_per_kg=N/NA*137)
barrier=1.43996448/(2*1.2*2**(1/3));q=Q(2*2.014102,-3.016029,-n)
save('43.67',barrier_CM_MeV=barrier,Q_MeV=q,Q_J=q*1e6*e,energy_J_mol_D2=q*1e6*e*NA,chemical_ratio=q*1e6*e*NA/2.9e5)
# Independent regression, two-exponential fit, Bateman ODE and saturation ODE.
ind=runpy.run_path(str(ROOT/'raw_materials/physics/verify_chapter43_independent.py'));ind['main']()
independent=json.loads((ROOT/'qa/physics/chapter43/independent-end-numeric.json').read_text(encoding='utf-8'))
save('43.68-72-and-Bridge',independent_report='qa/physics/chapter43/independent-end-numeric.json',status=independent['status'])
save('43.73-77',answers=['a','b','d','d','b'],N_I131=3.7e9*(8.04*86400)/math.log(2),I123_Q_MeV=Q(122.904270,H,-122.905589,-n))
assert 6e13<out['43.48']['totalHeat_W']<7e13
assert .7<out['43.56']['D_Gy']<.9
assert .5e-4<out['43.53']['H_Sv']<.6e-4
q=ROOT/'qa/physics/chapter43';q.mkdir(parents=True,exist_ok=True)
(q/'end-parent-numeric.json').write_text(json.dumps(dict(status='passed',cases=out),ensure_ascii=False,indent=2),encoding='utf-8')
print('Actual chapter43 advanced numerical ledger:',len(out),'cases plus independent regressions/ODEs.')
