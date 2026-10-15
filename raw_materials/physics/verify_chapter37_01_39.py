from math import sqrt,isclose
import json
c=3e8;mp=1.67e-27;me=9.11e-31;e=1.602e-19
def g(b):return 1/sqrt((1-b)*(1+b))
def b_from_g(v):return sqrt((v-1)*(v+1))/v
def close(a,b):assert isclose(a,b,rel_tol=1e-10,abs_tol=1e-14),(a,b)
r={}
r['37.1']={'ground_first':'rear'}
r['37.2']={'tau_s':g(.9)*2.2e-6,'distance_m':g(.9)*2.2e-6*.9*c}
r['37.3']={'beta':b_from_g(2)}
r['37.4']={'proper_frame':'Mars','tau_spaceship_s':g(.985)*75e-6}
gamma=4.2e-7/2.6e-8;b=b_from_g(gamma)
r['37.5']={'beta':b,'distance_m':b*c*4.2e-7}
r['37.6']={'a_pilot_time_s':(1.2e8/(.8*c))/g(.8),'a_your_frame_time_s':1.2e8/(.8*c),'b_distance_m':.8*c*.3,'c_your_time_pilot_simultaneity_s':.3/g(.8)}
r['37.7']={'proper_time_s':.012,'beta':b_from_g(.150/.012)}
r['37.8']={'time_s':100,'x_m':b_from_g(100)*c*100}
r['37.9']={'length_rest_m':74*g(.6)}
r['37.10']={'beta':sqrt(1-.3048**2)}
tau0=2.2e-6;gamma=g(.999)
r['37.11']={'a_upper_distance_m':c*tau0,'b_lab_lifetime_s':gamma*tau0,'b_distance_m':.999*c*gamma*tau0,'c_contracted_atmosphere_m':1e4/gamma,'c_travel_time_s':1e4/gamma/(.999*c)}
r['37.12']={'a_height_m':2/g(.91),'b_rest_height_m':2*g(.91),'c_both_height_m':2}
gamma=g(4e7/c)
r['37.13']={'a_runway_m':3600/gamma,'b_earth_time_s':3600/4e7,'c_pilot_time_s':3600/(4e7*gamma)}
r['37.14']={'locus':'xprime=-x, x=gamma*u*t/(gamma+1)'}
r['37.15']={str(b):(b+.6)/(1+.6*b) for b in [.4,.9,.99]}
r['37.16']={'a_x_m':g(.8)*.8*c*5,'a_t_s':g(.8)*5,'b_time_s':g(.8)*5,'c_distance_m':g(.8)*5*.8*c}
r['37.17']={'velocity_beta':(.6-.8)/(1-.6*.8)}
b=(.4+.7)/(1+.4*.7)
r['37.18']={'a_beta':b,'b_travel_s':8e9/(b*c)}
b=(.95-.65)/(1-.95*.65)
r['37.19']={'beta':b};close((.65+b)/(1+.65*b),.95)
r['37.20']={'relative_beta':2*.938/(1+.938**2)}
b=.89/(1+sqrt(1-.89**2));r['37.21']={'each_lab_beta':b};close(2*b/(1+b*b),.89)
r['37.22']={'observed_frequency_Hz':8.64e14*sqrt((1-.52)/(1+.52))}
b=(675**2-575**2)/(675**2+575**2)
r['37.23']={'a_beta':b,'b_speed_km_h':b*c*3.6,'b_fine_dollars':b*c*3.6-90}
close(r['37.23']['b_speed_km_h'],b*c*3600/1000)
# Doppler consistency: lambda_source/lambda_observed = frequency ratio.
close(sqrt((1+b)/(1-b)),675/575)
r['37.24']={'beta':(1.25**2-1)/(1.25**2+1),'direction':'approaching'}
b1=b_from_g(1.12);b2=2*b1
r['37.25']={'beta1':b1,'beta2':b2,'gamma2':g(b2),'momentum_ratio_equal_masses':2*g(b2)/1.12}
r['37.26']={str(b):{'parallel_N':.145*g(b)**3,'perpendicular_N':.145*g(b)} for b in [10/c,.9,.99]}
r['37.27']={'p_over_p0':g(.8)*.8/(g(.4)*.4)}
gamma=120/90;b=b_from_g(gamma)
r['37.28']={'diameter_m':25,'beta':b,'momentum_kg_m_s':gamma*4e3*b*c}
r['37.29']={'a_beta':b_from_g(2),'b_beta':b_from_g(2**(1/3))}
massloss=3.8e26/c**2;Msun=1.99e30
r['37.30']={'mass_loss_kg_s':massloss,'short_ton_s':massloss/(2000*.45359237),'duration_s':Msun/massloss,'duration_yr':Msun/massloss/(365.25*86400)}
r['37.31']={'a_beta':b_from_g(2),'b_beta':b_from_g(6)}
mmu=207*me
r['37.32']={'momentum_kg_m_s':g(.999)*mmu*.999*c,'kinetic_J':(g(.999)-1)*mmu*c*c}
r['37.33']={'a_kinetic_J':3*mp*c*c,'b_momentum_kg_m_s':sqrt(15)*mp*c,'c_beta':sqrt(15)/4}
wa=g(.09)-1;wb=g(.99)-g(.9)
r['37.34']={'a_work_over_mc2':wa,'b_work_over_mc2':wb,'c_ratio':wb/wa}
m=6.64e-27;p=2.10e-18;E0=m*c*c;E=sqrt(E0**2+(p*c)**2)
r['37.35']={'a_E_J':E,'b_K_J':E-E0,'c_K_over_E0':(E-E0)/E0}
K=7.5e5*e;gamma=1+K/(me*c*c)
r['37.36']={'a_beta':b_from_g(gamma),'b_classical_speed_m_s':sqrt(2*K/me),'b_classical_beta':sqrt(2*K/me)/c}
r['37.37']={str(v):{'classical_J':.5*mp*v*v,'relativistic_J':(g(v/c)-1)*mp*c*c,'ratio':(g(v/c)-1)*mp*c*c/(.5*mp*v*v)} for v in [8e7,2.85e8]}
m=9.75e-28;gamma=1+m/(2*mp);K=m*c*c/2
r['37.38']={'a_beta':b_from_g(gamma),'b_K_each_MeV':K/(1e6*e),'c_eta_rest_energy_MeV':2*K/(1e6*e)}
close(2*gamma*mp,2*mp+m)
K=(g(.98)-1)*me*c*c
r['37.39']={'a_potential_V':K/e,'b_K_J':K,'b_K_eV':K/e}
assert len(r)==39
print(json.dumps(dict(status='passed',c_m_s=c,results=r),indent=2))
