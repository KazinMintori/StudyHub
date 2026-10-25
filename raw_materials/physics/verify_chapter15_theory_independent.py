"""Independent chapter15 source-model checks, without importing author code."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad,solve_ivp

OUT=Path(__file__).resolve().parent;checks=[];examples={};selfchecks={}
def eq(name,a,b,rtol=1e-9,atol=1e-11):
 assert math.isclose(float(a),float(b),rel_tol=rtol,abs_tol=atol),(name,a,b)
 checks.append({'id':name,'actual':float(a),'expected':float(b),'passed':True})

# Derive the first examples directly from original input values.
v=344.;f=262.
examples['15.1']={'wavelength_m':v/f,'high_C_f_Hz':4*f,'high_C_wavelength_m':v/(4*f),'speed_ft_s':v/.3048}
eq('ex15.1:fourth_wavelength',examples['15.1']['wavelength_m']/4,examples['15.1']['high_C_wavelength_m'])
eq('ex15.1:rounding',v/f,1.31,rtol=.003)
A=.075;f=2.;v=12.;w=2*math.pi*f;k=w/v
examples['15.2']={'A_m':A,'omega_rad_s':w,'T_s':1/f,'lambda_m':v/f,'k_rad_m':k}
def y(x,t):return A*math.cos(k*x-w*t)
def yt(x,t):return w*A*math.sin(k*x-w*t)
def yx(x,t):return -k*A*math.sin(k*x-w*t)
eq('ex15.2:source_initial_y',y(0,0),A);eq('ex15.2:source_initial_v',yt(0,0),0)
for t in [.02,.09,.17,.40]:eq('ex15.2:opposite_phase:'+str(t),y(3,t),-y(0,t))
for x,t in [(0,.06),(.7,.13),(3,.29),(8,.41)]:
 h=1e-4
 yxx=(y(x+h,t)-2*y(x,t)+y(x-h,t))/h**2
 htt=h/v
 ytt=(y(x,t+htt)-2*y(x,t)+y(x,t-htt))/htt**2
 eq(f'PDE:fd:{x}:{t}',yxx,ytt/v**2,rtol=3e-6,atol=2e-7)
 eq(f'Newton:segment:{x}:{t}',36*yxx,.25*ytt,rtol=3e-6,atol=2e-6)
 eq(f'right-moving:kinematic:{x}:{t}',yt(x,t),-v*yx(x,t))

mr=2.;L=80.;mb=20.;g=9.80;mu=mr/L;F=mb*g
speed=math.sqrt(F/mu);lam=speed/2;cycles=L/lam;top=math.sqrt((mr+mb)*g/mu)
examples['15.3']={'linear_density_kg_m':mu,'tension_N':F,'speed_m_s':speed,'wavelength_m':lam,'spatial_cycles':cycles,'top_speed_with_weight_m_s':top}
eq('ex15.3:mass_conserved',mu*L,mr);eq('ex15.3:source_N',cycles,1.81,rtol=.002)
eq('ex15.3:top_speed',top,92.9,rtol=.001)
assert cycles!=round(cycles)
# Independent travel-time integral for variable tension: Weight is ignored only
# in the constant-tension approximation, never in inertial mass density.
tau=quad(lambda z:math.sqrt(mu/(g*(mb+mu*z))),0,L)[0]
closed=2*(math.sqrt(mb+mu*L)-math.sqrt(mb))/math.sqrt(g*mu)
eq('weighted_vertical_rope:travel_integral',tau,closed)
assert L/top<tau<L/speed

# Work transported through a cut is integrated numerically over a complete cycle.
mu=.250;F=36.;w=4*math.pi;A=.075;v=math.sqrt(F/mu);k=w/v
def power(x,t):
 slope=-k*A*math.sin(k*x-w*t)
 velocity=w*A*math.sin(k*x-w*t)
 return -F*slope*velocity
pavg=quad(lambda t:power(.623,t),0,.5,epsabs=1e-12)[0]/.5
pmax=math.sqrt(mu*F)*w*w*A*A
examples['15.4']={'Pmax_W':pmax,'Pavg_W_integrated':pavg,'reduced_Pavg_W':pavg/100,'wave_speed_m_s':v}
eq('ex15.4:mean_from_work',pavg,.5*pmax)
eq('ex15.4:rounding_max',pmax,2.66,rtol=.002)
eq('ex15.4:rounding_reduced',pavg/100,.0133,rtol=.002)
for t in np.linspace(0,.5,31):assert power(.623,float(t))>=0
r1=15.;I1=.250;I2=.010;r2=r1*math.sqrt(I1/I2)
examples['15.5']={'r2_m':r2,'source_power_W':4*math.pi*r1*r1*I1}
eq('ex15.5:equal_spherical_power',4*math.pi*r2*r2*I2,4*math.pi*r1*r1*I1)
eq('ex15.5:distance',r2,75.)

f=440.;v=143.;component_A=.000750;S=2*component_A;w=2*math.pi*f;k=w/v;lam=v/f
examples['15.6']={'standing_amplitude_m':S,'omega_rad_s':w,'k_rad_m':k,'wavelength_m':lam,'node_spacing_m':lam/2,'vmax_m_s':w*S,'amax_m_s2':w*w*S,'amax_over_g':w*w*S/g}
eq('ex15.6:vmax',w*S,4.15,rtol=.001)
eq('ex15.6:amax',w*w*S,1.15e4,rtol=.005)
for x,t in[(0,.001),(.17,.0002),(.35,.00061),(.62,.0017)]:
 combined=-component_A*math.cos(k*x+w*t)+component_A*math.cos(k*x-w*t)
 eq(f'standing:sum:{x}:{t}',combined,S*math.sin(k*x)*math.sin(w*t))
for n in range(7):
 x=n*lam/2
 for fraction in [.09,.25,.57,.88]:
  eq(f'standing:node:{n}:{fraction}',S*math.sin(k*x)*math.sin(2*math.pi*fraction),0,atol=1e-15)
# Local energy is not constant at a cut and instantaneous flux is not zero.
# Numerically check the string energy continuity law ∂t(e)+∂x(P)=0.
F=14.3**2;mu=F/v**2
def energy(x,t):
 vel=S*w*math.sin(k*x)*math.cos(w*t)
 slope=S*k*math.cos(k*x)*math.sin(w*t)
 return .5*mu*vel*vel+.5*F*slope*slope
def flux(x,t):return -F*S*S*k*w*math.sin(k*x)*math.cos(k*x)*math.sin(w*t)*math.cos(w*t)
for x,t in[(.03,.00013),(.14,.00061),(.29,.00117)]:
 dt=1e-8;dx=1e-6
 de=(energy(x,t+dt)-energy(x,t-dt))/(2*dt)
 dp=(flux(x+dx,t)-flux(x-dx,t))/(2*dx)
 eq(f'standing:energy_continuity:{x}:{t}',de,-dp,rtol=2e-6,atol=1e-6)
 assert abs(flux(x,t))>1e-4
 mean=quad(lambda z:flux(x,z),0,1/f,epsabs=1e-12)[0]*f
 eq(f'standing:mean_flux:{x}',mean,0,atol=1e-11)

L=5.;mu=.0400;f1=20.;F=(2*L*f1)**2*mu
examples['15.7']={'tension_N':F,'tension_lbf':F/4.4482216152605,'f2_Hz':2*f1,'lambda2_m':L,'f3_Hz':3*f1,'lambda3_m':2*L/3}
eq('ex15.7:tension',F,1600.);eq('ex15.7:normal_mode_velocity',math.sqrt(F/mu),200.)
examples['15.8']={'air_frequency_Hz':f1,'air_wavelength_m':344/f1,'string_wavelength_m':2*L,'wavelength_ratio':(344/f1)/(2*L)}
eq('ex15.8:air_wavelength',344/f1,17.2);eq('ex15.8:ratio',344/200,1.72)

selfchecks['15.1']={'answer':'i','reason':'Crowd displacement vertical, propagation horizontal.'}
eq('self15.1:orthogonal_motion',np.dot([0,1],[1,0]),0)
selfchecks['15.2']={'answer':'iv','speed_ratio':1,'frequency_ratio':.5}
eq('self15.2:lambda_doubled',12/(2*6),.5*(12/6))
A=1.;w=2*math.pi
# Reference A,C start at −A, B starts at+A exactly as Fig15.8.
state=lambda sign,t:(sign*math.cos(w*t),-sign*w*math.sin(w*t),-sign*w*w*math.cos(w*t))
Ay,Av,Aa=state(-1,.25);By,Bv,Ba=state(1,.5);Cy,Cv,Ca=state(-1,5/8)
eq('self15.3:A_at_Tquarter_y',Ay,0,atol=1e-12);eq('self15.3:A_max_upward_v',Av,w)
eq('self15.3:B_max_upward_a',Ba,w*w);assert Cy>0 and Cv<0 and Ca<0
eq('self15.3:B_at_Tquarter_velocity',state(1,.25)[1],-w)
eq('self15.3:B_at_3Tquarter_velocity',state(1,.75)[1],w)
eq('self15.3:A_at_3Tquarter_velocity',state(-1,.75)[1],-w)
eq('self15.3:C_at_3Tquarter_velocity',state(-1,.75)[1],-w)
selfchecks['15.3']={'answers':['T/4','T/2','5T/8'],'A':state(-1,.25),'B':state(1,.5),'C':state(-1,5/8)}
mus=[.1,.2,.4];vs=[math.sqrt(10/u)for u in mus];assert vs[0]>vs[1]>vs[2]
selfchecks['15.4']={'answer':'ii','assumption':'Comparable guitar strings, thickness tracks linear mass density.'}
ratios=[math.sqrt(F/10)*(A/1)**2 for F,A in[(10,1),(40,1),(10,4),(20,2)]]
for i,expected in enumerate([1,2,16,4*math.sqrt(2)]):eq(f'self15.5:ratio{i+1}',ratios[i],expected)
selfchecks['15.5']={'order':['iii','iv','ii','i'],'ratios':ratios}
def bump(s):return np.where(abs(s)<=1,np.cos(math.pi*s/2)**4,0)
minimum=1e9
for t in[0,2,3,4,6]:
 x=np.linspace(-5,5,2001);y1=bump((x+3-t)/.5);y2=.30*bump((x-3+t)/1.2)
 minimum=min(minimum,float(np.min(y1+y2)))
 assert np.all(y1+y2>=0)
eq('self15.6:nonnegative_sum_minimum',minimum,0)
selfchecks['15.6']={'nonnegative':True,'source_erratum_confirmed':'Printed negative narrow pulse contradicts positive initial pulses. Source image15.22 preserved; new correct solution additive.'}
for n in range(12):eq(f'self15.7:old_node_preserved:{n}',math.sin(2*math.pi*n),0,atol=1e-12)
selfchecks['15.7']={'answer':'Every old node remains; new node at midpoint of each old gap.'}
for n in range(1,10):eq(f'self15.8:midpoint_amplitude:{n}',abs(math.sin(n*math.pi/2)),1 if n%2 else 0,atol=1e-12)
selfchecks['15.8']={'excluded_modes':[1,3,5,7,9],'allowed_modes':[2,4,6,8]}

# Fourier coefficients independently from direct triangle integrals. Height1,
# length1, pluck at1/4. No author Fourier routine or source formula imported.
def triangle(x):return x/.25 if x<=.25 else(1-x)/.75
B=[]
for n in range(1,9):
 integral=2*(quad(lambda x:triangle(x)*math.sin(n*math.pi*x),0,.25,epsabs=1e-12)[0]+quad(lambda x:triangle(x)*math.sin(n*math.pi*x),.25,1,epsabs=1e-12)[0])
 B.append(integral)
eq('Fourier:B2_over_B1',B[1]/B[0],1/(2*math.sqrt(2)))
eq('Fourier:B3_over_B1',B[2]/B[0],1/9)
eq('Fourier:B4',B[3],0,atol=1e-12)
assert not math.isclose(B[0],1)
for x in [.1,.4,.7]:
 ode=solve_ivp(lambda t,z:[z[1],-(2*math.pi*20)**2*z[0]],(0,.04),[B[0]*math.sin(math.pi*x),0],rtol=1e-11,atol=1e-12)
 expected=B[0]*math.sin(math.pi*x)*math.cos(2*math.pi*20*.04)
 eq('normal_mode:ODE:'+str(x),ode.y[0,-1],expected,rtol=3e-9)

assert len(examples)==8 and len(selfchecks)==8
report={'status':'passed','scope':'Independent source and proposal physics models for chapter15 theory; not browser/deployment acceptance','assertions':len(checks),'exampleCount':8,'selfcheckCount':8,'examples':examples,'selfchecks':selfchecks,'fourier_triangle_coefficients':B,'checks':checks,'sourceLimits':['Uniform flexible string, small transverse slopes, constant equilibrium tension and inertia unless explicitly qualified.','Ideal standing wave transports zero time-average power but has nonzero local instantaneous energy flux.','Biology illustrations retained as source models, not independently verified population or clinical claims.']}
print(json.dumps(report,ensure_ascii=False,indent=2))
