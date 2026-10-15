from math import sqrt,isclose
import json
c=3e8
def g(b):return 1/sqrt((1-b)*(1+b))
def close(a,b):assert isclose(a,b,rel_tol=1e-11,abs_tol=1e-14),(a,b)
r={}
r['Newton_missile_m_s']=1000+2000
r['example37.1_muon_lifetime_s']=g(.99)*2.2e-6
t=4.8e6/300;b=300/c;lag=t*b*b/(1+sqrt(1-b*b))
r['example37.2']={'ground_time_s':t,'plane_time_s':t-lag,'lag_s':lag,'beta2':b*b}
r['example37.3']={'Stanley_station_s':9e7/(.6*c),'Mavis_station_s':9e7/(.6*c*g(.6)),'Stanley_blink_s':.4/g(.6)}
r['example37.4_length_m']=400/g(.99)
r['example37.5_distance_m']=56.4/g(.99)
r['checks37.1']={'wavefront':'sphere','center':'emission position','if_beta_half_ship_radius_ratio':.5}
r['checks37.2']={'answer':'iii after noon'}
r['checks37.3']={'both_local_comparisons_moving_clock_s':10/g(.6)}
r['checks37.4']={'ordering':'ii > i=iii > iv'}
earth=100/.995;proper=earth/g(.995)
r['grandmother']={'earth_trip_years':earth,'traveler_trip_years':proper,'traveler_return_age_years':20+proper,'grandchild_age_years':earth-20}
delta=.1/c;gamma=1/sqrt(delta*(2-delta));r['SLAC']={'length_earth_m':3000,'length_electron_m':3000/gamma}
r['gamma_examples']={'beta_point2':g(.2),'beta_point0002':g(.0002)}
# Light-clock triangles and longitudinal flight times give the same dilation/contraction.
for b in [.1,.6,.99]:
 gamma=g(b);d=2.;tau0=2*d/c;t=gamma*tau0;ell=sqrt(d*d+(b*c*t/2)**2);close(2*ell/c,t)
 l0=400;l=l0/gamma;t1=l/(c-b*c);t2=l/(c+b*c);close(t1+t2,gamma*2*l0/c)
close(r['example37.3']['Mavis_station_s'],.4)
close(r['example37.3']['Stanley_blink_s'],.32)
print(json.dumps(dict(status='passed',results=r),indent=2))
