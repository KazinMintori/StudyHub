"""Source-transcribed chapter13 guided exercises and bridge, private QA only."""
from pathlib import Path
import math,json
import numpy as np
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parent
G=6.67e-11;ME=5.97e24;RE=6.37e6;MS=1.99e30;MM=6.42e23;RM=3.39e6;YEAR=3.156e7
MU=G*ME;MUS=G*MS;MUM=G*MM
records={};assertions=[]
def eq(id,a,b,rel=1e-11,atol=1e-10):
 assert math.isclose(a,b,rel_tol=rel,abs_tol=atol),(id,a,b)
 assertions.append(dict(id=id,actual=float(a),expected=float(b),status='passed'))

m=478.;work=MU*m/RE
integral=quad(lambda q:1/q**2,1,np.inf)[0]*MU*m/RE
eq('VP13.5.1:radialworkintegral',work,integral)
records['VP13.5.1']=dict(mass_kg=m,work_min_J=work)

ri=1.5*RE;v=math.sqrt(2*MU*(1/RE-1/ri))
eq('VP13.5.2:energy',v*v/2-MU/RE,-MU/ri)
gravityWork=quad(lambda u:1/u**2,1,1.5)[0]*MU/RE
eq('VP13.5.2:integratedacceleration',v*v/2,gravityWork)
records['VP13.5.2']=dict(initial_radius_m=ri,initial_height_m=.5*RE,impact_speed_m_s=v)

v0=3000.;epsilon=v0*v0/2-MUM/RM;rmax=-MUM/epsilon;h=rmax-RM
root=brentq(lambda q:epsilon+MUM/(q*RM),1,3)*RM
eq('VP13.5.3:turningpointroot',rmax,root)
eq('VP13.5.3:worktoapex',quad(lambda q:MUM/RM/q**2,1,rmax/RM)[0],v0*v0/2)
records['VP13.5.3']=dict(Mars_mass_kg=MM,Mars_radius_m=RM,launch_speed_m_s=v0,maximum_radius_m=rmax,height_m=h,escape_speed_m_s=math.sqrt(2*MUM/RM))

rf=2.50e8;vf=8500.;v0=math.sqrt(vf*vf+2*MU*(1/RE-1/rf))
eq('VP13.5.4:energy',v0*v0/2-MU/RE,vf*vf/2-MU/rf)
eq('VP13.5.4:gravitationalwork',.5*(vf*vf-v0*v0),quad(lambda q:-MU/RE/q**2,1,rf/RE)[0])
records['VP13.5.4']=dict(final_radius_m=rf,final_speed_m_s=vf,launch_speed_m_s=v0)

v=4000.;r=MU/v**2;h=r-RE;T=2*math.pi*r/v
eq('VP13.6.1:centripetal',v*v/r,MU/r**2)
eq('VP13.6.1:Kepler',T,2*math.pi*math.sqrt(r**3/MU))
records['VP13.6.1']=dict(speed_m_s=v,radius_m=r,altitude_m=h,period_s=T,period_h=T/3600)

T=24.66*3600;r=(MUM*T*T/(4*math.pi**2))**(1/3);v=2*math.pi*r/T
eq('VP13.6.2:centripetal',v*v/r,MUM/r**2)
eq('VP13.6.2:speed',v,math.sqrt(MUM/r))
records['VP13.6.2']=dict(period_h=24.66,radius_m=r,speed_m_s=v,altitude_m=r-RM)

m=1000.;r1=1.50e11;r2=1.08e11
K1=MUS*m/(2*r1);K2=MUS*m/(2*r2);U1=-MUS*m/r1;U2=-MUS*m/r2
dK=K2-K1;dU=U2-U1;dE=(K2+U2)-(K1+U1)
eq('VP13.6.3:changesum',dE,dK+dU)
eq('VP13.6.3:circularvirial',dU,-2*dK)
eq('VP13.6.3:potentialwork',dU,quad(lambda q:MUS*m/r1/q**2,1,r2/r1)[0])
records['VP13.6.3']=dict(mass_kg=m,initial_radius_m=r1,final_radius_m=r2,delta_K_J=dK,delta_U_J=dU,delta_E_J=dE)

m=1500.;r=RE+3.50e6;v0=7500.;vc=math.sqrt(MU/r);ve=math.sqrt(2*MU/r)
wc=.5*m*(vc*vc-v0*v0);we=.5*m*(ve*ve-v0*v0);e0=.5*m*v0*v0-MU*m/r
eq('VP13.6.4:circularenergy',wc,-MU*m/(2*r)-e0)
eq('VP13.6.4:escapetozerototalenergy',we,-e0)
assert wc<0<we
assertions.append(dict(id='VP13.6.4:worksigns',status='passed',actual=[wc,we],expected='negative circularization, positive escape'))
records['VP13.6.4']=dict(mass_kg=m,altitude_m=3.50e6,initial_speed_m_s=v0,radius_m=r,circular_speed_m_s=vc,escape_speed_m_s=ve,work_circular_J=wc,work_escape_J=we,condition='Speed-change work at fixed point. Circularization requires tangential final direction, possible local impulse/reorientation; not a specified finite thrust trajectory.')

rp=6.00e9;ra=3.00e12;a=(rp+ra)/2;e=(ra-rp)/(ra+rp);T=2*math.pi*math.sqrt(a**3/MUS)
eq('VP13.9.1:perihelion',a*(1-e),rp,rel=1e-10)
eq('VP13.9.1:aphelion',a*(1+e),ra)
records['VP13.9.1']=dict(perihelion_m=rp,aphelion_m=ra,semimajor_m=a,eccentricity=e,period_s=T,period_y=T/YEAR)

T=7.85*YEAR;e=.250;a=(MUS*T*T/(4*math.pi**2))**(1/3);rp=a*(1-e);ra=a*(1+e)
eq('VP13.9.2:Kepler',2*math.pi*math.sqrt(a**3/MUS),T)
eq('VP13.9.2:axis',rp+ra,2*a)
records['VP13.9.2']=dict(period_y=7.85,eccentricity=e,semimajor_m=a,perihelion_m=rp,aphelion_m=ra)

an=4.5e12;e=.25;a=an*(3/2)**(2/3);rp=a*(1-e)
eq('VP13.9.3:periodresonance',(a/an)**1.5,1.5)
assert rp<an
assertions.append(dict(id='VP13.9.3:insideNeptune',actual=rp/an,expected='less than 1',status='passed'))
records['VP13.9.3']=dict(Neptune_radius_m=an,minorToNeptunePeriodRatio=1.5,semimajor_m=a,perihelion_m=rp,perihelion_to_Neptune_radius=rp/an,location='inside Neptune orbit at perihelion, by the specified orbital radii')

a=7.41e9;e=.173;T=4.39*86400;rp=a*(1-e);mass=4*math.pi**2*a**3/(G*T*T)
eq('VP13.9.4:backsubstitutedperiod',2*math.pi*math.sqrt(a**3/(G*mass)),T)
records['VP13.9.4']=dict(semimajor_m=a,eccentricity=e,period_days=4.39,period_s=T,periapsis_m=rp,star_mass_kg=mass,periapsis_to_Mercury=.0+rp/4.60e10,star_to_solar_mass=mass/MS,approximation='Neglect planet mass compared with host star; otherwise Kepler measures sum of masses.')

# Bridge: geometric source data from Example13.9 (PDF430), not rounded e=.967.
m=2.2e14;rp=8.80e7*1000;ra=5.25e9*1000;a=(rp+ra)/2;e=(ra-rp)/(ra+rp)
vp=math.sqrt(MUS/a*(1+e)/(1-e));va=math.sqrt(MUS/a*(1-e)/(1+e))
Kp=.5*m*vp**2;Ka=.5*m*va**2;Up=-MUS*m/rp;Ua=-MUS*m/ra;Et=-MUS*m/(2*a)
eq('bridge:angularmomentum',rp*vp,ra*va)
eq('bridge:energyperi',Kp+Up,Et)
eq('bridge:energyaphe',Ka+Ua,Et)
eq('bridge:workintegral',Ka-Kp,quad(lambda q:-MUS*m/rp/q**2,1,ra/rp)[0])
eq('bridge:visvivaperi',vp*vp,MUS*(2/rp-1/a))
eq('bridge:visvivaaphe',va*va,MUS*(2/ra-1/a))

# Independent dimensionless Newtonian orbit integration. Start at perihelion.
# Length unit a, time unit sqrt(a^3/(GM)), speed unit sqrt(GM/a).
# Integrate the smooth eccentric-anomaly-parametrized orbit to avoid a near-
# perihelion time-step issue; also directly integrate Cartesian Newton equations.
for ecc in(0.,.1,.25,.7,.9,.9670288497564631):
 q=1-ecc;pp=math.sqrt((1+ecc)/(1-ecc));aa=math.sqrt((1-ecc)/(1+ecc))
 eq('bridge:generalenergyperi',pp*pp/2-1/q,-.5,rel=1e-10)
 eq('bridge:generalenergyaphe',aa*aa/2-1/(1+ecc),-.5,rel=1e-10)
 eq('bridge:generalmomentum',q*pp,(1+ecc)*aa)
 b=math.sqrt(1-ecc*ecc);area=math.pi*b;angular=math.sqrt(1-ecc*ecc)
 eq('bridge:areaperiod',2*area/angular,2*math.pi)
 def fun(t,z):
  x,y,vx,vy=z;r=math.hypot(x,y)
  return(vx,vy,-x/r**3,-y/r**3)
 sol=solve_ivp(fun,(0,math.pi),(q,0,0,pp),rtol=3e-12,atol=1e-13,max_step=.025)
 assert sol.success
 rr=math.hypot(sol.y[0,-1],sol.y[1,-1]);vv=math.hypot(sol.y[2,-1],sol.y[3,-1])
 eq('bridge:Newtonaphelionradius',rr,1+ecc,rel=5e-8,atol=1e-9)
 eq('bridge:Newtonaphelionspeed',vv,aa,rel=2e-7,atol=1e-9)
 if ecc==0: eq('bridge:circularlimit',pp,aa)

records['bridge']=dict(sourcePerihelion_m=rp,sourceAphelion_m=ra,semimajor_m=a,eccentricity=e,comet_mass_kg=m,
  perihelion_speed_m_s=vp,aphelion_speed_m_s=va,perihelion_K_J=Kp,aphelion_K_J=Ka,
  perihelion_U_J=Up,aphelion_U_J=Ua,total_energy_J=Et,angular_momentum_kg_m2_s=m*rp*vp,
  formula_vp='sqrt(GMs/a*(1+e)/(1-e))',formula_va='sqrt(GMs/a*(1-e)/(1+e))',
  sourceGuideParts=9,condition='0≤e<1, comet mass negligible compared with Sun, inertial fixed-Sun approximation, potential zero at infinity')
assert len(records)==13
out=dict(status='passed',scope='12 guided problems plus one bridging problem only',constants=dict(G=G,ME=ME,RE=RE,MS=MS,MarsM=MM,MarsR=RM,secondsPerYear=YEAR),records=records,assertionCount=len(assertions),assertions=assertions)
print(json.dumps(out,ensure_ascii=False,indent=2))
