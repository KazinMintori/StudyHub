from math import sqrt,atan,degrees,isclose
import json
import numpy as np
c=3e8;mp=1.67e-27;me=9.11e-31;e=1.602e-19
def g(b):return 1/sqrt((1-b)*(1+b))
def b_from_g(x):return sqrt((x-1)*(x+1))/x
def close(a,b):assert isclose(a,b,rel_tol=1e-10,abs_tol=1e-12),(a,b)
r={}
r['37.40']={'a_earth_period_s':g(.75)*1.8,'b_spaceship_period_s':1.8/g(.75)}
r['37.41']={'beta':b_from_g(1.4),'direction':'parallel major axis'}
for b in [.1,.4,.8]:close((1/g(b))*1*1,1/g(b))
r['37.42']={'Vprime_over_a3':'sqrt(1-u^2/c^2)'}
r['37.43']={'earth_years':42.2/.993,'proper_years':42.2/(.993*g(.993)),'biological_age_years':19+42.2/(.993*g(.993))}
gamma=403/80.2;b=b_from_g(gamma);m=2.12e-27;E0=m*c*c
r['37.44']={'a_beta':b,'b_distance_m':b*c*403e-12,'c_E0_J':E0,'c_K_J':(gamma-1)*E0,'c_E_J':gamma*E0,'d_rest_E0_E_J':E0,'d_rest_K_J':0}
bB=(.98-.8)/(1-.98*.8)
r['37.45']={'B_east_beta':bB,'invariant_mass_kg_both':1,'historical_rel_mass_A_kg':g(.8),'historical_rel_mass_B_kg':g(bB)}
close((.8+bB)/(1+.8*bB),.98)
mph=.44704;cstar=65*mph;v=60*mph;b=60/65;gamma=g(b);gamma_rel=2*gamma**2-1
r['37.46']={'a_lag_s':3600*(1-1/gamma),'b_assumed_car_length_m':4.5,'c_road_car_length_m':4.5/gamma,'d_relative_mph':65*(2*b/(1+b*b)),'d_relative_beta':2*b/(1+b*b),'e_oncoming_length_m':4.5/gamma_rel,'f_work_alternate_J':(gamma-1)*2000*cstar*cstar,'g_work_real_J':.5*2000*v*v}
gamma=1+7e12*e/(mp*c*c)
delta=1/(gamma*gamma*(1+sqrt(1-1/gamma**2)))
r['37.47']={'gamma':gamma,'Delta':delta,'c_minus_v_m_s':c*delta,'historical_rel_mass_over_m':gamma}
angle=degrees(atan(g(.7)**2*np.tan(np.pi/6)))
r['37.48']={'accel_angle_degree':angle}
b=250/c;lag=14400*b*b/(1+sqrt(1-b*b))
r['37.49']={'difference_s':lag,'difference_ns':lag*1e9,'shorter':'airborne clock'}
T=sqrt(7.11**2+3.35**2);b=7.11/T
r['37.50']={'a_earth_years':T,'beta':b,'b_ship_ly':b*3.35};close(T/g(b),3.35)
r['37.51']={'threshold_beta':1/1.52,'threshold_K_eV':(g(1/1.52)-1)*me*c*c/e}
mu=4.12e-30;md=8.59e-30;gu=1+mp/(3*mu);gd=1+mp/(3*md)
r['37.52']={'a_gamma_up':gu,'b_gamma_down':gd,'c_beta_up':b_from_g(gu),'c_beta_down':b_from_g(gd),'d_gluon_fraction':1-g(.9)*(2*mu+md)/mp,'e_frequency_Hz':.9*c/(2*1.7e-15)}
E=12e-4*c*c
r['37.53']={'a_energy_J':E,'b_average_power_W':E/(4e-6),'c_water_mass_kg':E/(9.8*1000)}
b=.7/(1+sqrt(1-.7**2));r['37.54']={'each_beta':b};close(2*b/(1+b*b),.7)
# Exact field transformation and charge/current transformation for55/56.
tests=[]
for b in [.2,.7,.9]:
 gamma=g(b);v=np.array([b,0,0]);B=np.array([0,0,2.]);Bp=gamma*B;Ep=gamma*np.cross(v,B)
 # Dimensionless c=1, unit charge, sphere velocity=-v.
 close(np.linalg.norm(Ep+np.cross(-v,Bp)),0)
 # Initially neutral straight x-directed current, density j=1. Volume'=Volume/gamma.
 rho=-gamma*b;jx=gamma
 fyprime=rho*Ep[1]-jx*Bp[2]
 close(fyprime,-2.)
 tests.append({'beta':b,'sphere_net_force':0,'loop_force_ratio_exact':1/gamma,'loop_torque_parallel_ratio_exact':1/gamma})
r['37.55']={'conditional_fixed_current_mu_ratio':'1/gamma','field_perp_ratio':'gamma','exact_torque_parallel_ratio':'1/gamma','warning':'Torque invariant assumption and fixed-current approximation in prompt are not exact Lorentz laws.','checks':tests}
r['37.56']={'net_electromagnetic_force_both_frames':0,'Bprime':'-gamma*B*yhat','Eprime':'-gamma*v*B*zhat','magnetic_force':'gamma*Q*v*B*zhat'}
ratio=953.4/656.3;b=(ratio**2-1)/(ratio**2+1)
r['37.57']={'beta':b,'direction':'receding'}
r['37.58']={'separation_m':c*sqrt(2.15**2-1.8**2)}
delta=2.86e-7;b=delta/(2+delta)
r['37.59']={'baseball_beta':b,'speed_km_h':b*c*3.6};close((1+b)/(1-b)-1,delta)
mass=.058;v1=80;v2=1.8e8;vr=2.2e8;br=vr/c;bb=v2/c
r['37.60']={'a_classical_K_J':.5*mass*v1*v1,'b_rel_K_J':(g(bb)-1)*mass*c*c,'c_rabbit_beta_ball_frame':(br-bb)/(1-br*bb),'d_rabbit_distance_m':20/g(br),'e_players_time_s':20/vr,'f_rabbit_proper_time_s':20/(vr*g(br))}
r['37.61']={'force_N':g(.75)*mp*(.75*c)**2/628,'direction':'inward'}
b=.758;f0=345
fa=f0*sqrt((1+b)/(1-b));fr=f0*sqrt((1-b)/(1+b));ft=f0/g(b)
r['37.62']={'approach_MHz':fa,'recede_MHz':fr,'transverse_MHz':ft,'shift_approach_MHz':fa-f0,'shift_recede_MHz':fr-f0,'shift_transverse_MHz':ft-f0,'transverse_definition':'Photon propagation perpendicular to source velocity at emission; received later.'}
assert len(r)==23
print(json.dumps(dict(status='passed',results=r),indent=2))
