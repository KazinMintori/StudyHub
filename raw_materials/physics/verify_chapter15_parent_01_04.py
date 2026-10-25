"""Independent arithmetic, phase and derivation checks for owned prose15.1–15.4."""
from pathlib import Path
import math,json,hashlib
import numpy as np

OUT=Path(__file__).resolve().parent
checks=[]
def eq(id,actual,expected,atol=1e-10):
    actual,expected=float(actual),float(expected)
    assert math.isclose(actual,expected,rel_tol=0,abs_tol=atol),(id,actual,expected)
    checks.append(dict(id=id,computed=actual,expected=expected,tolerance=atol,status='passed'))

g=9.8
examples={}
f,v=262.,344.
lam=v/f
examples['15.1']=dict(lambda_m=lam,high_frequency_Hz=4*f,high_wavelength_m=v/(4*f),speed_ft_s=v/.3048)
eq('15.1.lambda',lam,1.31,.005)
eq('15.1.high_frequency',4*f,1048)
eq('15.1.high_lambda',v/(4*f),.328,.0005)
eq('15.1.sound_ft_s',v/.3048,1130,2)

A,f,v=.075,2.,12.
omega=2*math.pi*f;k=omega/v;lam=v/f;period=1/f
examples['15.2']=dict(A_m=A,f_Hz=f,v_m_s=v,omega_rad_s=omega,k_rad_m=k,period_s=period,lambda_m=lam)
eq('15.2.omega',omega,4*math.pi)
eq('15.2.k',k,math.pi/3)
eq('15.2.period',period,.5)
eq('15.2.lambda',lam,6)
for t in np.linspace(0,period,21):
    yy=A*math.cos(k*3-omega*t)
    eq(f'15.2.point3.t{t}',yy,-A*math.cos(omega*t),1e-12)
eq('15.2.origin_maximum',A*math.cos(0),A)
eq('15.2.origin_instantaneous_rest',-omega*A*math.sin(0),0)

mass,L,box=2.,80.,20.
mu=mass/L;tension=box*g;v=math.sqrt(tension/mu);lam=v/2
top_tension=(box+mass)*g;top_speed=math.sqrt(top_tension/mu)
examples['15.3']=dict(rope_mass_kg=mass,L_m=L,box_mass_kg=box,mu_kg_m=mu,tension_ignoring_rope_weight_N=tension,speed_m_s=v,wavelength_at_2Hz_m=lam,cycles=L/lam,top_tension_with_rope_weight_N=top_tension,top_speed_m_s=top_speed)
for id,value,expected,tolerance in [('mu',mu,.025,1e-12),('tension',tension,196,1e-12),('speed',v,88.5,.05),('lambda',lam,44.3,.05),('cycles',L/lam,1.81,.005),('top_speed',top_speed,92.9,.05)]:
    eq('15.3.'+id,value,expected,tolerance)
eq('15.3.rope_weight_fraction',mass/box,.1)

# Source selfcheck15.3: Figure15.8initialA/C=-1andB=+1,T=1.
omega=2*math.pi
t=.25
eq('self15.3.Aup_speed_max',omega*math.sin(omega*t),omega)
t=.5
eq('self15.3.Bup_accel_max',-omega**2*math.cos(omega*t),omega**2)
t=5/8
yC=-math.cos(omega*t);vyC=omega*math.sin(omega*t);ayC=-omega**2*yC
assert yC>0 and vyC<0 and ayC<0
selfchecks=dict(section151='Transverse:verticaldisplacement/horizontalpropagation.',
section152=dict(choice='iv',speed_ratio=1,frequency_ratio=.5),
section153=dict(Amaxup_t_over_T=.25,Bmaxupaccel_t_over_T=.5,Cdown_v_and_a_t_over_T=5/8,yC=yC,vyC=vyC,ayC=ayC),
section154='ii:lowestmuundernearlysametension.')
eq('self15.2.frequency_factor',1/2,.5)

# Phase/time-delay and PDE signs. No division by derivatives at zeros is used.
cases=[]
for A,k,v in [(.075,math.pi/3,12),(.03,2.5,7.),(.001,11,20)]:
    om=k*v
    for x,t in [(.23,.07),(.51,.13),(.89,.29)]:
        delayed=A*math.cos(om*(t-x/v))
        right=A*math.cos(k*x-om*t)
        left=A*math.cos(k*x+om*t)
        advanced=A*math.cos(om*(t+x/v))
        eq(f'phase_delay.{A}.{x}',delayed,right,1e-12)
        eq(f'phase_advance.{A}.{x}',advanced,left,1e-12)
        ytt=-om**2*right;yxx=-k**2*right
        eq(f'PDE.{A}.{x}',yxx-ytt/v**2,0,1e-10)
        eq(f'SHM.{A}.{x}',ytt+om**2*right,0,1e-10)
        cases.append(dict(A=A,k=k,v=v,x=x,t=t))

# Newton finite difference converges to F*y_xx=mu*y_tt for sinusoidalprofile.
F,mu,A,k=25.,.03,.002,2.1
v=math.sqrt(F/mu);om=k*v
x,t=.37,.009
def slope(xx):return -k*A*math.sin(k*xx-om*t)
exact_yxx=-k*k*A*math.cos(k*x-om*t)
errs=[]
for dx in [1e-2,1e-3,1e-4,1e-5]:
    quotient=(slope(x+dx)-slope(x))/dx
    errs.append(abs(quotient-exact_yxx))
assert all(b<a for a,b in zip(errs,errs[1:]))
ytt=-om*om*A*math.cos(k*x-om*t)
eq('Newton_PDE_dynamic_identity',F*exact_yxx,mu*ytt,1e-10)

# Impulse derivation with growing mass uses a constantparticlevelocity.
impulse_cases=[]
for F,mu,vy,time in [(30,.2,.1,.4),(100,.05,.2,.3),(5,.4,.05,2.)]:
    v=math.sqrt(F/mu)
    Fy=F*vy/v
    movingmass=mu*v*time
    eq(f'impulse.F{F}',Fy*time,movingmass*vy,1e-12)
    impulse_cases.append(dict(F=F,mu=mu,vy=vy,t=time,v=v,Fy=Fy,movingmass=movingmass))

report=dict(status='passed',checksCount=len(checks),checks=checks,examples=examples,selfchecks=selfchecks,phasePDECases=cases,finiteDifferenceErrors=errs,impulseCases=impulse_cases,sourceTheoryScope='15.1–15.4')
print(json.dumps(report,ensure_ascii=False,indent=2))
