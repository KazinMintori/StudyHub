"""Models for actual chapter14guided/discussion/bridge prompts.

Values are transcribed from PDF475–476. Independent ODE, energy and geometric
checks complement direct arithmetic. They do not establish source completeness.
"""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import solve_ivp,quad
from scipy.special import ellipk
BASE=Path(__file__).resolve().parent
checks=[];records={};g=9.80
def eq(name,a,b,rtol=1e-10,atol=1e-11):
 assert math.isclose(float(a),float(b),rel_tol=rtol,abs_tol=atol),(name,a,b)
 checks.append({'id':name,'actual':float(a),'expected':float(b),'passed':True})
def truth(name,a):eq(name,bool(a),True)

m=.400;f=4.15;w=2*math.pi*f;T=1/f;k=m*w*w;F=k*.0200
records['VP14.3.1']=dict(mass_kg=m,frequency_Hz=f,period_s=T,omega_rad_s=w,k_N_m=k,force_at_0p0200m_N=F)
eq('VP14.3.1:Tomega',T*w,2*math.pi);eq('VP14.3.1:roundT',T,.241,rtol=.003)
k=4.50;T=1.20;w=2*math.pi/T;m=k/w**2;A=1.20/w**2
records['VP14.3.2']=dict(k_N_m=k,T_s=T,mass_kg=m,amax_m_s2=1.20,A_m=A)
eq('VP14.3.2:Newton_at_turn',k*A/m,1.20)
f=50.;w=2*math.pi*f;x=.0300;v=12.4;A=math.hypot(x,v/w);vmax=w*A
records['VP14.3.3']=dict(f_Hz=f,x_m=x,v_m_s=v,A_m=A,vmax_m_s=vmax)
eq('VP14.3.3:phase_space',vmax**2,v*v+w*w*x*x)
m=5.;k=185.;w=math.sqrt(k/m);f=w/(2*math.pi);A=1.52/w**2
records['VP14.3.4']=dict(total_mass_kg=m,k_N_m=k,f_Hz=f,accel_limit_m_s2=1.52,max_A_m=A)
eq('VP14.3.4:threshold',k*A/m,1.52)
m=.150;k=8.;vmax=.350;w=math.sqrt(k/m);A=vmax/w;E=.5*m*vmax*vmax;x=.0300;U=.5*k*x*x;K=E-U
records['VP14.4.1']=dict(mass_kg=m,k_N_m=k,vmax_m_s=vmax,A_m=A,E_J=E,x_m=x,U_J=U,K_J=K)
eq('VP14.4.1:turn_energy',.5*k*A*A,E);truth('VP14.4.1:x_inside',x<A);eq('VP14.4.1:energy',U+K,E)
m=.300;A=.0440;E=.0600;k=2*E/A**2;v=math.sqrt(E/m)
records['VP14.4.2']=dict(mass_kg=m,A_m=A,E_J=E,k_N_m=k,speed_at_U_halfE_m_s=v)
eq('VP14.4.2:kinetic_half',.5*m*v*v,E/2)
E=.00400;A=.0300;vmax=.125;k=2*E/A**2;m=2*E/vmax**2;w=math.sqrt(k/m);amax=w*w*A;U=.00300;x=math.sqrt(2*U/k);a=w*w*x
records['VP14.4.3']=dict(E_J=E,A_m=A,vmax_m_s=vmax,k_N_m=k,mass_kg=m,amax_m_s2=amax,U_J=U,abs_x_m=x,abs_accel_m_s2=a)
eq('VP14.4.3:energy_at_x',.5*k*x*x,U);eq('VP14.4.3:ratio',a/amax,math.sqrt(U/E))
records['VP14.4.4']=dict(K_over_E=[1/3,4/5],abs_x_over_A=[math.sqrt(2/3),1/math.sqrt(5)])
for fraction,xr in zip(records['VP14.4.4']['K_over_E'],records['VP14.4.4']['abs_x_over_A']):eq('VP14.4.4:energy_fraction'+str(fraction),1-xr*xr,fraction)
L=.500;f=.609;T=1/f;ga=(2*math.pi*f)**2*L
records['VP14.9.1']=dict(L_m=L,f_Hz=f,T_s=T,g_m_s2=ga)
eq('VP14.9.1:recoverf',math.sqrt(ga/L)/(2*math.pi),f)
m=.350;k=8.75;L=m*g/k
records['VP14.9.2']=dict(glider_mass_kg=m,k_N_m=k,g_m_s2=g,L_m=L,f_Hz=math.sqrt(k/m)/(2*math.pi))
eq('VP14.9.2:equal_omega',math.sqrt(g/L),math.sqrt(k/m))
records['VP14.9.3']=dict(inertia='2MR²',pivot_CG_distance='R',frequency='sqrt(g/(2R))/(2pi)',small_angle=True)
for M,R in[(1.,.3),(2.,.8)]:eq('VP14.9.3:inertia_M'+str(M),2*M*R*R,M*R*R+M*R*R)
m=.600;d=.500;T=1.59;I=m*g*d*(T/(2*math.pi))**2
records['VP14.9.4']=dict(rod_length_m=.900,mass_kg=m,pivot_CG_m=d,T_s=T,pivot_inertia_kg_m2=I)
eq('VP14.9.4:recoverT',2*math.pi*math.sqrt(I/(m*g*d)),T)

# Recover oscillator periods from actual NewtonODE zero-crossing events.
def down(t,y):return y[0]
down.direction=-1
for name,m,k,A in [('VP14.3.1',.400,records['VP14.3.1']['k_N_m'],.0200),('VP14.3.2',records['VP14.3.2']['mass_kg'],4.50,records['VP14.3.2']['A_m']),('VP14.3.4',5.,185.,.0300),('VP14.4.1',.150,8.,records['VP14.4.1']['A_m'])]:
 T=2*math.pi*math.sqrt(m/k)
 ode=solve_ivp(lambda t,y:[y[1],-k/m*y[0]],(0,3*T),[A,0.],events=down,max_step=T/80,rtol=1e-11,atol=1e-12)
 times=ode.t_events[0]
 eq(name+':ODEperiod',times[1]-times[0],T,rtol=1e-8)
 energies=.5*m*ode.y[1]**2+.5*k*ode.y[0]**2
 eq(name+':ODEenergy',max(energies)-min(energies),0,atol=1e-9)

for A in [.03,.06]:
 w=3.;T=2*math.pi/w
 distance=quad(lambda t:abs(-w*A*math.sin(w*t)),0,T,epsabs=1e-12)[0]
 eq('Q14.1:distance_A'+str(A),distance,4*A)
records['Q14.1']=dict(distance_factor=2,period_factor=1,vmax_factor=2)
records['Q14.2']=dict(examples=['Smallangleplaygroundswing','Carverticalsuspension','Smalltuningforktinevibration'],limits=['Sinetorquenonlinearity','Dampingandforcing','Finiteamplitudenonlinearityanddamping'],scope='Models, not empirical accuracy estimates.')
records['Q14.3']=dict(tuningfork='ApproximatelySHMatsmallamplitude',musical_need='Frequencynearlyindependentofamplitudewhiletonesdecay')
M=2.;pebble=.5;k=18.;A=.04;oldw=math.sqrt(k/(M+pebble));neww=math.sqrt(k/M);E=.5*k*A*A
Kbox_old=.5*M*(oldw*A)**2;Kbox_new=.5*M*(neww*A)**2
records['Q14.4']=dict(box_mass_example_kg=M,pebble_mass_example_kg=pebble,frequency_ratio=neww/oldw,period_ratio=oldw/neww,A_ratio=1,total_maxK_ratio=1,box_only_Kmax_ratio=Kbox_new/Kbox_old,vmax_ratio=neww/oldw)
truth('Q14.4:box_only_kinetic_increases',Kbox_new>Kbox_old);eq('Q14.4:total_energy_unchanged',Kbox_new,E)
records['Q14.5']=dict(half_spring_k_ratio=2,frequency_ratio=math.sqrt(2))
eq('Q14.5:series_halves',1/(1/(2*k)+1/(2*k)),k)
records['Q14.6']=dict(friction='m_coin*omega²*abs(x)',max_positions='x=±A',min_position='x=0')
m=1.7;k=12.;relativew=math.sqrt(2*k/m)
ode=solve_ivp(lambda t,z:[z[1],k/m*(z[2]-z[0]),z[3],-k/m*(z[2]-z[0])],(0,4),[-.04,0,.04,0],rtol=1e-11,atol=1e-12,dense_output=True)
for t in [.2,.7,1.2]:
 q=ode.sol(t);eq('Q14.7:COM'+str(t),(q[0]+q[2])/2,0);eq('Q14.7:relative'+str(t),q[2]-q[0],.08*math.cos(relativew*t),rtol=1e-8)
records['Q14.7']=dict(relative_omega='sqrt(2k/m)',period_ratio_to_fixed_end=1/math.sqrt(2),COM_rest_required_for_lab_periodicity=True)
records['Q14.8']=dict(pendulum_period_Mars_to_Earth_ratio=math.sqrt(9.8/3.7),assumption='Room stationary on planet, same known or estimated pendulumlength, smallangle.')
records['Q14.9']=dict(three_cases_period_ratio=[1,1,1],equilibrium_shift_depends_effective_gravity=True)
records['Q14.10']=dict(pendulum='No gravitational restoring oscillation in ideal freelyfalling localframe; no finite period.',spring_period_s=5.)
ratios=[math.sqrt(g/(g+5)),1.,math.sqrt(g/(g-5))]
records['Q14.11']=dict(elevator_accel_up_positive_m_s2=[5.,0.,-5.,-9.8],period_ratio_to_rest=ratios+['No restoring gravity, no finite period'])
truth('Q14.11:up_shorter',ratios[0]<1);truth('Q14.11:down_longer',ratios[2]>1)
records['Q14.12']=dict(length_ratio_for_frequency_double=.25,length_ratio_for_period_double=4.,length_ratio_for_angularfrequency_double=.25)
for f,Lr in [(2,.25),(.5,4)]:eq('Q14.12:scale'+str(f),1/math.sqrt(Lr),f)
records['Q14.13']=dict(mountain_period_increases=True,clock_loses_time=True)
theta=[.1,.3,.8,1.2];periodratios=[2/math.pi*ellipk(math.sin(a/2)**2)for a in theta]
truth('Q14.14:period_increases',all(a<b for a,b in zip(periodratios,periodratios[1:])))
truth('Q14.14:restoring_per_angle_decreases',all(math.sin(a)/a>math.sin(b)/b for a,b in zip(theta,theta[1:])))
records['Q14.14']=dict(angles_rad=theta,finite_amplitude_period_to_smallangle=periodratios,same_sine_torque_for_physical_pendulum=True)
records['Q14.15']=dict(similar_shape_stepfrequency='proportional1/sqrt(leglength)',mass_cancels=True)
theta0=.7;L=1.2;mass=.4
bottom=mass*g*(3-2*math.cos(theta0));turn=mass*g*math.cos(theta0)
for theta in np.linspace(-theta0,theta0,31):
 tension=mass*g*(3*math.cos(theta)-2*math.cos(theta0))
 truth('Q14.16:tension_bounds'+str(theta),turn-1e-12<=tension<=bottom+1e-12)
records['Q14.16']=dict(Tension_formula='mg(3costheta−2costheta0)',greatest='bottom',least='turningpoints',domain='Releasedfromrest, tautstring, idealpendulum theta0<pi/2.')
records['Q14.17']=dict(pendulum_standard_dependencies=['length','localgravity','amplitude','temperature','damping'],atomic_standard='Specified atomic transition frequency, not a pendulum-length history claim.')
records['Q14.18']=dict(angularspeed='abs(dtheta/dt),variable',smallangle_angularfrequency='sqrt(g/L),constant for fixedsystem')
# At finite amplitude, an ideal conservative pendulum still has a repeatable
# period; the value is not the small-angle sqrt(g/L) approximation.
theta0=.4;L=.8;Tfinite=4*math.sqrt(L/g)*ellipk(math.sin(theta0/2)**2)
pendulum=solve_ivp(lambda t,z:[z[1],-g/L*math.sin(z[0])],(0,4*Tfinite),[theta0,0],events=down,max_step=Tfinite/100,rtol=1e-11,atol=1e-12)
events=pendulum.t_events[0]
eq('Q14.18:finiteAmplitudeODEperiod',events[1]-events[0],Tfinite,rtol=1e-8)
eq('Q14.18:repeatedPeriod',events[2]-events[1],Tfinite,rtol=1e-8)
truth('Q14.18:finitePeriodExceedsSmallAngle',Tfinite>2*math.pi*math.sqrt(L/g))
records['Q14.19']=dict(natural_frequencies='Avoid dominant excitationbands',damping='Sufficient controlleddamping reduces resonance; not arbitrarily infinite damping.')

# Rolling bridge: Integrate translational and angular accelerations together.
M=1.4;R=.12;k=18.;I=.5*M*R*R;A=.035;we=math.sqrt(k/(M+I/R**2));T=2*math.pi/we
ode=solve_ivp(lambda t,z:[z[1],-k*z[0]/(M+I/R**2)],(0,3*T),[A,0],events=down,max_step=T/100,rtol=1e-11,atol=1e-12)
eq('bridge:ODEperiod',ode.t_events[0][1]-ode.t_events[0][0],T,rtol=1e-8)
for x,v in zip(ode.y[0,::25],ode.y[1,::25]):
 a=-k*x/(M+I/R**2);alpha=a/R;friction=-I*a/R**2
 eq('bridge:translation',M*a,-k*x+friction)
 eq('bridge:rotation',I*alpha,-R*friction)
 eq('bridge:staticfriction',friction,k*x/3)
 eq('bridge:energy',.5*(M+I/R**2)*v*v+.5*k*x*x,.5*k*A*A,rtol=1e-8)
records['bridge']=dict(total_inertia='.5MR²',acceleration='−2kx/(3M)',period='2pi sqrt(3M/(2k))',friction='kx/3, signedleft',coordinate='Positiveleft;positiveanglecounterclockwise; a=Ralpha; torque=-Rf.',smooth_nonrolling_period='2pi sqrt(M/k)',period_ratio_to_nonrolling=math.sqrt(1.5),sourceGuideParts=7,example_period_s=T)
assert len([k for k in records if k.startswith('VP')])==12
assert len([k for k in records if k.startswith('Q')])==19
report={'status':'passed','scope':'12guided+19discussion+1bridge, not numbered14.1–96 or wholechapter','assertions':len(checks),'records':records,'checks':checks,'sourcePages':[475,476],'numberedInventory':{'first':1,'last':96,'challenge':[92,93],'MCAT':[94,95,96]}}
print(json.dumps(report,ensure_ascii=False,indent=2))
