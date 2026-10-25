"""Parent checks using ODE events, finite differences and complex response.

Scope: Chapter14 theory assumptions and representative numerical models.
Source prompt completeness is verified separately against the PDF.
"""
import json,math
import numpy as np
from scipy.integrate import solve_ivp

checks=[]
def close(name,actual,expected,rtol=2e-8,atol=1e-10):
 assert math.isclose(float(actual),float(expected),rel_tol=rtol,abs_tol=atol),(name,actual,expected)
 checks.append({'id':name,'actual':float(actual),'expected':float(expected),'passed':True})

# Obtain pendulum periods from successive downward zero crossings, rather than
# the elliptic integral or truncated series used by the author verifiers.
g=9.8;length=1.0
def crossing(t,y):return y[0]
crossing.direction=-1
periods={}
for angle in [1,6,15,45,90,150]:
 theta0=math.radians(angle)
 ode=solve_ivp(lambda t,y:[y[1],-g/length*math.sin(y[0])],(0,18),[theta0,0],events=crossing,rtol=2e-11,atol=2e-12,max_step=.02)
 times=ode.t_events[0];assert len(times)>=2
 period=float(times[1]-times[0]);periods[angle]=period
 close(f'pendulum:{angle}:successive_periods',times[2]-times[1],period)
 if angle==15:
  close('pendulum:15deg:relative_correction',period/(2*math.pi/math.sqrt(g))-1,.00430058,rtol=1e-5)
assert all(periods[a]<periods[b] for a,b in zip([1,6,15,45,90],[6,15,45,90,150]))
close('example14.8:small_angle_limit',periods[1],2*math.pi/math.sqrt(g),rtol=2e-5)

# Linear damped solutions from a matrix exponential eigenmode calculation.
# This checks both critically/overdamped limits without a real sinusoidal ansatz.
from scipy.linalg import expm
m=.8;k=3.2
for multiplier in [.1,.4,1.,2.,3.]:
 b=multiplier*math.sqrt(k*m)
 A=np.array([[0,1],[-k/m,-b/m]])
 E=[]
 for t in [0,.13,.7,2.,6.]:
  y=expm(A*t)@np.array([.2,0.])
  derivative=A@y
  close(f'damped:{multiplier}:{t}:Newton',m*derivative[1],-k*y[0]-b*y[1])
  close(f'damped:{multiplier}:{t}:power',m*y[1]*derivative[1]+k*y[0]*y[1],-b*y[1]**2)
  E.append(.5*m*y[1]**2+.5*k*y[0]**2)
 assert all(E[i+1]<=E[i]+1e-12 for i in range(len(E)-1))
 if multiplier<2:
  beta=b/(2*m);wd=math.sqrt(k/m-beta*beta)
  # Rest release requires nonzero sine coefficient when b>0.
  t=.7
  y=expm(A*t)@np.array([.2,0.])
  x=.2*math.exp(-beta*t)*(math.cos(wd*t)+beta/wd*math.sin(wd*t))
  close(f'damped:{multiplier}:rest_initial_solution',y[0],x)
 if multiplier==2:
  t=.7;beta=b/(2*m)
  close('critical:rest_solution',(expm(A*t)@np.array([.2,0.]))[0],.2*(1+beta*t)*math.exp(-beta*t))

# Complex dynamic stiffness independently produces the forced amplitude and
# phase. Its derivative condition is checked by neighboring sample values.
F=1.7
for multiplier in [.2,.4,.7,1.,math.sqrt(2),2.]:
 b=multiplier*math.sqrt(k*m)
 for w in [0,.3,1.,2.,5.]:
  response=F/complex(k-m*w*w,b*w)
  close(f'forced:{multiplier}:{w}:amplitude',abs(response),F/math.hypot(k-m*w*w,b*w))
  if w==0:close(f'forced:{multiplier}:static',abs(response),F/k)
 if multiplier<math.sqrt(2):
  wr=math.sqrt(k/m-b*b/(2*m*m))
  def amp(w):return abs(F/complex(k-m*w*w,b*w))
  assert amp(wr)>amp(wr-.001) and amp(wr)>amp(wr+.001)
 else:
  grid=np.linspace(0,8,801)
  amplitudes=np.array([abs(F/complex(k-m*w*w,b*w))for w in grid])
  assert np.all(np.diff(amplitudes)<=1e-12)

# Force is the derivative of the full molecular potential. Compare its linear
# coefficient with symmetric finite differences in normalized separation.
U0=1.68e-21;R0=3.82e-10
def u(z):return z**-12-2*z**-6
def f(z):return 12*(z**-13-z**-7)
for z in [.9,.99,1.,1.01,1.1]:
 h=1e-6
 close(f'molecule:force:{z}',-(u(z+h)-u(z-h))/(2*h),f(z),rtol=1e-7,atol=2e-8)
h=1e-5
close('molecule:curvature',(u(1+h)-2*u(1)+u(1-h))/h**2,72.,rtol=2e-6)
km=72*U0/R0**2;mass=39.948*1.66e-27
fixed=math.sqrt(km/mass)/(2*math.pi)
free=math.sqrt(2*km/mass)/(2*math.pi)
close('example14.7:free_to_fixed_ratio',free/fixed,math.sqrt(2))
close('example14.7:fixed_Hz',fixed,5.63e11,rtol=.001)
close('example14.7:free_Hz',free,7.96e11,rtol=.001)

print(json.dumps({'status':'passed','scope':'Chapter14theory independent numerical models; no endchapter claim','assertions':len(checks),'checks':checks,'pendulum_periods_s':periods},ensure_ascii=False,indent=2))
