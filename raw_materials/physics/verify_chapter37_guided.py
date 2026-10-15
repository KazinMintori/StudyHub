"""Independent numerical and invariant checks for all12 guided tasks and bridge."""
from math import sqrt,isclose
import json

c=3.00e8
mp=1.67e-27
me=9.11e-31
MeV=1.602e-13
def g(b):return 1/sqrt((1-b)*(1+b))
def beta_from_gamma(gamma):return sqrt((gamma-1)*(gamma+1))/gamma
def forward(x,t,b):return g(b)*(x-b*c*t),g(b)*(t-b*x/c)
def inverse(x,t,b):return g(b)*(x+b*c*t),g(b)*(t+b*x/c)
def transform_velocity(v,b):return (v-b)/(1-b*v)
def close(a,b):assert isclose(a,b,rel_tol=1e-10,abs_tol=1e-9),(a,b)

r={}
r['VP37.5.1']={'a_s':g(.8)*1.23e-8,'b_s':g(.8)*1.23e-8}
r['VP37.5.2']={'a_s':20/g(.6),'b_s':24*g(.6)}
t=1.5e11/(.95*c)
r['VP37.5.3']={'a_s':t,'b_length_m':1.5e11/g(.95),'b_time_s':t/g(.95)}
close(r['VP37.5.3']['b_length_m']/(.95*c),r['VP37.5.3']['b_time_s'])
r['VP37.5.4']={'gamma':6/2,'beta':beta_from_gamma(3),'a_km':3.84e5/3,'b_m':24*3}
xa,ta=forward(0,2.5,.75);xb,tb=inverse(4e8,2.5,.75)
r['VP37.7.1']={'a_xprime_m':xa,'a_tprime_s':ta,'b_x_m':xb,'b_t_s':tb}
close(c*c*2.5**2,c*c*ta**2-xa**2)
close(c*c*2.5**2-(4e8)**2,c*c*tb**2-xb**2)
dx=.600*c/(g(.8)*.8)
r['VP37.7.2']={'a_dx_m':dx,'b_dxprime_m':g(.8)*dx}
close(abs(forward(dx,0,.8)[1]),.600)
r['VP37.7.3']={'a_beta':(-.6+.8)/(1-.8*.6),'b_beta':transform_velocity(.7,.8)}
r['VP37.7.4']={'a_beta':abs(transform_velocity(.65,-.75)),'b_beta':abs(transform_velocity(-.65,-.75))}
gamma=g(.925);F=9e-14
r['VP37.11.1']={'a_p_kg_m_s':gamma*mp*.925*c,'b_aparallel_m_s2':F/(gamma**3*mp),'c_aperp_m_s2':F/(gamma*mp)}
E=4e-13;E0=me*c*c
r['VP37.11.2']={'a_K_J':E-E0,'b_gamma':E/E0,'c_beta':beta_from_gamma(E/E0)}
p=2.60e-22;E=sqrt((p*c)**2+E0**2)
r['VP37.11.3']={'a_E_J':E,'b_gamma':E/E0,'c_beta':p*c/E}
close(r['VP37.11.3']['c_beta'],beta_from_gamma(E/E0))
Eeach=3686/2;gamma=Eeach/495
r['VP37.11.4']={'E_each_MeV':Eeach,'a_K_MeV':Eeach-495,'b_gamma':gamma,'c_beta':beta_from_gamma(gamma)}
close(2*(r['VP37.11.4']['a_K_MeV']+495),3686)
a=2-sqrt(3);E0p=mp*c*c/MeV
Klab=(g(a)-1)*E0p;Kfixed=(g(.5)-1)*E0p
r['bridge']={'a_beta':a,'b_K_each_lab_MeV':Klab,'c_K_other_rest_frame_MeV':Kfixed,'evaluation_total_beam_K_MeV':2*Klab,'evaluation_fixed_target_K_MeV':Kfixed}
close(2*a/(1+a*a),.5)
# Both setups have identical invariant collision energy.
s_beam=(2*g(a)*E0p)**2
s_fixed=(g(.5)*E0p+E0p)**2-(g(.5)*E0p*.5)**2
close(s_beam,s_fixed)
assert len(r)==13
print(json.dumps(dict(status='passed',c_m_s=c,tasks=r),indent=2))
