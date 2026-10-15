from math import sqrt,isclose
import json
import numpy as np
c=3e8
def g(b):return 1/sqrt((1-b)*(1+b))
def close(a,b):assert np.allclose(a,b,rtol=1e-10,atol=1e-13),(a,b)
r={}
r['example37.6']={'message_x_m':g(.6)*(-300),'message_t_s':g(.6)*.6*(-300)/c,'minimum_signal_time_s':300/c}
r['example37.7']={'probe_beta':(.7+.9)/(1+.7*.9),'scout_beta':(.95-.9)/(1-.95*.9)}
ratio=6.66e14/5.55e13;b=(ratio*ratio-1)/(ratio*ratio+1)
r['example37.8']={'frequency_ratio':ratio,'beta':b,'observed_wavelength_m':c/6.66e14,'source_wavelength_m':c/5.55e13,'erroneous_classical_beta':ratio-1}
me=9.11e-31;F=1.60e-19*5e5
r['example37.9']={str(b):{'gamma':g(b),'p_kg_m_s':g(b)*me*b*c,'parallel_a_m_s2':F/(g(b)**3*me),'perp_a_m_s2':F/(g(b)*me)} for b in [.01,.9,.99]}
me=9.109e-31;ce=2.998e8;e=1.602e-19;E0=me*ce*ce
r['example37.10']={'rest_J':E0,'rest_eV':E0/e,'cases':{str(V):{'gamma':1+e*V/E0,'beta':sqrt(1-1/(1+e*V/E0)**2)} for V in [2e4,5e6]}}
mp=1.67e-27;mpi=2.4e-28;gamma=1+mpi/(2*mp)
r['example37.11']={'gamma':gamma,'beta':sqrt(1-1/gamma**2),'K_each_MeV':(gamma-1)*mp*c*c/(1.602e-13),'pion_rest_MeV':mpi*c*c/(1.602e-13)}
close(2*gamma*mp,2*mp+mpi)
r['check37.5']={'same_position_first':'P1','simultaneous_different_x_first_positive_u':'P4'}
r['check37.7']={'answer':'ii greater than2','initial_speed_constraint':'0<v<c/2'}
r['check37.8']={'answer':'i same work F times1m'}
r['GPS']={'frequency_difference_Hz':(10.23-10.22999999543)*1e6,'fractional_frequency_difference':(10.23-10.22999999543)/10.23}
# Invariance, velocities and exact derivative relations at representative inputs.
for b in [.1,.6,.9]:
 M=g(b)*np.array([[1,-b],[-b,1]])
 close(M.T@np.diag([1,-1])@M,np.diag([1,-1]))
 for v in [-.9,0,.8]:
  vp=(v-b)/(1-b*v);assert abs(vp)<1;close((vp+b)/(1+b*vp),v)
 close((1-b)/(1-b),1.)
 # dp/dv analytic derivative has factor gamma^3.
 close(g(b)+g(b)**3*b*b,g(b)**3)
print(json.dumps(dict(status='passed',results=r),indent=2))
