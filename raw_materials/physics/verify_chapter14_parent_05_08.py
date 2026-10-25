from pathlib import Path
import math,json
import numpy as np
from scipy.integrate import quad,solve_ivp
from scipy.special import ellipk
from scipy.optimize import minimize_scalar
out=Path('qa/physics1-remaining/ch14-author-b');checks=[]
def add(id,val,expected,rtol=1e-10,atol=1e-12):
 assert math.isclose(float(val),float(expected),rel_tol=rtol,abs_tol=atol),(id,val,expected)
 checks.append(dict(id=id,value=float(val),expected=float(expected),rtol=rtol,atol=atol,passed=True))
g=9.8;L=1;T=2*math.pi*math.sqrt(L/g);f=1/T
add('ex14.8.T_s',T,2.007,atol=.0005);add('ex14.8.f_Hz',f,.4982,atol=.00005)
add('small_angle.sin_0p1',math.sin(.1),.0998,atol=.00005);add('small_angle.relative_force_error_0p1',(0.1-math.sin(.1))/.1,.002,atol=.0004)
for degrees in[1,6,15,45,90,150]:
 theta=math.radians(degrees);q=math.sin(theta/2);exact=2/math.pi*ellipk(q*q)
 direct=2/math.pi*quad(lambda a:1/math.sqrt(1-q*q*math.sin(a)**2),0,math.pi/2,epsabs=1e-12)[0]
 add(f'pendulum.finite_amplitude_quad_{degrees}',direct,exact)
 series=1+.25*q*q+9/64*q**4
 if degrees<=15:add(f'pendulum.truncated_series_{degrees}',series,exact,rtol=1e-6)
 if degrees==15:add('pendulum.15deg_error_below_halfpercent',(exact-1)<.005,1)
add('ex14.9.rodT_s',2*math.pi*math.sqrt(2/3/g),1.64,atol=.005)
add('ex14.9.rod_simple_ratio',math.sqrt(2/3),.816,atol=.0005)
L=3.1;S=4;Tr=2*math.pi*math.sqrt(2*L/(3*g));vr=S/Tr
add('ex14.10.T_s',Tr,2.9,atol=.05);add('ex14.10.v_m_s',vr,1.4,atol=.05);add('ex14.10.v_km_h',vr*3.6,5.0,atol=.05);add('ex14.10.v_mi_h',vr*3600/1609.344,3.1,atol=.05)
Tc=2*math.pi*math.sqrt((L*L/15)/(g*L/4));vc=S/Tc
add('ex14.10.tapered_T_s',Tc,1.825,atol=.001);add('ex14.10.tapered_v_m_s',vc,2.19,atol=.005)
add('ex14.10.tapered_period_ratio',Tc/Tr,math.sqrt(.4));add('ex14.10.tapered_speed_increases',vc>vr,1)
add('selfcheck14.5.bottom_a_up',.5**2/1>0,1);add('selfcheck14.5.bottom_tension_gt_mg',g+.5**2>g,1)
add('selfcheck14.6.rod_simple_ratio',math.sqrt(4/3),1.1547005383792515)
# Damped ODE and analytical solutions independent of the source's phase choice.
m=2.;k=8.;omega0=math.sqrt(k/m)
for b in[.2,1.,3.]:
 beta=b/(2*m);wd=math.sqrt(k/m-beta*beta);A=.7;phi=.4
 x0=A*math.cos(phi);v0=-A*(beta*math.cos(phi)+wd*math.sin(phi))
 def analytic(t):
  phase=wd*t+phi;e=math.exp(-beta*t)
  x=A*e*math.cos(phase);v=-A*e*(beta*math.cos(phase)+wd*math.sin(phase));acc=A*e*((beta*beta-wd*wd)*math.cos(phase)+2*beta*wd*math.sin(phase))
  return x,v,acc
 sol=solve_ivp(lambda t,y:[y[1],(-b*y[1]-k*y[0])/m],[0,5],[x0,v0],rtol=2e-11,atol=1e-12,dense_output=True)
 for t in[0,.3,1,2.5,5]:
  x,v,a=analytic(t);yn=sol.sol(t)
  add(f'damped.b{b}.t{t}.x',x,yn[0],atol=2e-10)
  add(f'damped.b{b}.t{t}.v',v,yn[1],atol=2e-10)
  add(f'damped.b{b}.t{t}.ODE',m*a+b*v+k*x,0,atol=1e-11)
  add(f'damped.b{b}.t{t}.energy',m*v*a+k*x*v,-b*v*v,atol=1e-11)
 add(f'damped.b{b}.phi0_not_at_rest',-beta*A!=0,1)
for b in[2*math.sqrt(k*m),10,14]:
 sol=solve_ivp(lambda t,y:[y[1],(-b*y[1]-k*y[0])/m],[0,12],[1,0],rtol=1e-10,atol=1e-12,dense_output=True)
 ts=np.linspace(0,12,200);x=sol.sol(ts)[0]
 add(f'nonoscillating.b{b}.positive_release',np.min(x)>-1e-10,1)
 add(f'nonoscillating.b{b}.monotonic',np.max(np.diff(x))<1e-10,1)
# Forced amplitude formula, peak frequency, fixed-force susceptibility.
# Critical closed forms, arbitrary initial velocity, and mechanical/RLC mapping.
for x0,v0 in[(1.,0.),(1.,-8.),(-.4,.3)]:
 m=2.;k=8.;bc=2*math.sqrt(k*m);beta=bc/(2*m)
 C1=x0;C2=v0+beta*x0
 numerical=solve_ivp(lambda t,y:[y[1],(-bc*y[1]-k*y[0])/m],[0,3],[x0,v0],rtol=1e-11,atol=1e-12,dense_output=True)
 for t in[0,.2,1.,3.]:
  e=math.exp(-beta*t);x=(C1+C2*t)*e;v=(C2-beta*(C1+C2*t))*e
  a=(-2*beta*C2+beta**2*(C1+C2*t))*e
  tag=f'critical.x{x0}.v{v0}.t{t}'
  add(tag+'.x',x,numerical.sol(t)[0],atol=1e-10)
  add(tag+'.v',v,numerical.sol(t)[1],atol=1e-10)
  add(tag+'.ODE',m*a+bc*v+k*x,0,atol=1e-11)
 Lc=.02;Cc=.0005;Rc=2*math.sqrt(Lc/Cc);alpha=Rc/(2*Lc)
 add(f'critical.RLC_mapping.x{x0}.v{v0}',alpha**2,1/(Lc*Cc))
m=1.7;k=6.3;F=2.;w0=math.sqrt(k/m)
def amp(w,b):return F/math.sqrt((k-m*w*w)**2+b*b*w*w)
for ratio in[.2,.4,.7,1.,math.sqrt(2),2.]:
 b=ratio*math.sqrt(k*m);peak_sq=k/m-b*b/(2*m*m);theory=math.sqrt(max(0,peak_sq))
 opt=minimize_scalar(lambda w:-amp(w,b),bounds=(0,2*w0),method='bounded',options={'xatol':1e-12})
 if ratio<math.sqrt(2):add(f'forced.peak_ratio{ratio}',opt.x,theory,atol=5e-7)
 else:add(f'forced.no_nonzero_peak_ratio{ratio}',amp(opt.x,b),amp(0,b),rtol=1e-10)
 add(f'forced.static_ratio{ratio}',amp(0,b),F/k)
 if ratio<math.sqrt(2):add(f'forced.peak_below_undamped{ratio}',theory<w0,1)
for wd in[.001*w0,.1*w0,w0,10*w0,100*w0]:add(f'selfcheck14.8.w{wd}',amp(wd,.2)>amp(wd,1),1)
add('selfcheck14.8.zero_frequency_equal',amp(0,.2),amp(0,1))
# Verify steady sinusoidal response by complex susceptibility at several drives.
for wd in[.2,.8,2.,5.]:
 b=.7;z=k-m*wd*wd+1j*b*wd;C=F/z
 add(f'forced.complex_amplitude_w{wd}',abs(C),amp(wd,b))
 add(f'forced.real_equation_w{wd}',abs(z*C-F),0,atol=1e-12)
result=dict(status='passed',count=len(checks),checks=checks,notes=['Ex14.10period2.885...s andspeed1.386...m/s retained tosourceprecision.','No unsupported optimal rodpivot point added: L/sqrt12 is not stated in these sourcepages.','Zero phase in damped solution yields nonzero initial velocity whenb>0.','Resonance amplitude peak frequency differs from free damped and undamped natural frequencies.'])
print(json.dumps(result,ensure_ascii=False,indent=2))
