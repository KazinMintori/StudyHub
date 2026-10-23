"""Independent original-input ledger for Chapter4 problems 4.31–4.60.

Source PDF145–148, graphs read visually. Numerical reference calculations
are not a substitute for separately reviewing the final authored solution.
"""
from math import sin,cos,radians,sqrt,hypot,isclose
import json
g=9.8
out={}
out['4.31']={'type':'Estimate','formula_force_N':'m*v^2/(2*d)','mass_range_kg':[5*.028349523125,5.25*.028349523125],'reference_94mph_m_s':94*.44704,'chosen_mass_kg':.145,'chosen_speed_m_s':42.,'assumed_acceleration_distance_m':1.,'force_N':.145*42**2/2,'force_lb':(.145*42**2/2)/4.448221615260,'restriction':'Mass from MLB2019Rule3.01, representative speed from MLBglossary, acceleration distance explicitly assumed. No unique exact force is given.'}
assert out['4.31']['mass_range_kg'][0]<.145<out['4.31']['mass_range_kg'][1]
assert isclose(out['4.31']['force_N'],127.89)
assert 28.7<out['4.31']['force_lb']<28.8
gx=2*10/3.40**2
out['4.32']={'planet_g_m_s2':gx,'weight_N':.100*gx}
amax=75/5.60-g
out['4.33']={'max_a_m_s2':amax,'minimum_time_s':sqrt(2*12/amax)}
out['4.34']={'contact_force_N':12-6*1.80,'a_A_m_s2':(12-6*1.80)/2}
adult_x=100*cos(radians(60))+140*cos(radians(30))
adult_y=100*sin(radians(60))-140*sin(radians(30))
out['4.35']={'minimum_child_force_N':abs(adult_y),'child_direction':'Negative y','system_mass_kg':adult_x/2,'system_weight_N':adult_x/2*g}
v=45/3.6
out['4.36']={'net_force_N':-850*v*v/(2*.018)}
out['4.37']={'a_4kg_m_s2':2.5,'tension_N':4*2.5,'applied_force_N':(4+6)*2.5}
a=2*18/5**2;mass_total=60/a
out['4.38']={'a_m_s2':a,'mass_B_kg':mass_total-15,'tension_N':60-15*a}
t=.025;A=9e3;B=8e4;mass=1.50
out['4.39']={'length_m':A*t*t-B*t**3,'exit_v_m_s':2*A*t-3*B*t*t,'force_0_N':mass*2*A,'force_exit_N':mass*(2*A-6*B*t)}
v_off_squared=2*g*(400-100);powered_a=v_off_squared/(2*100)
out['4.40']={'shutdown_v_m_s':sqrt(v_off_squared),'powered_a_m_s2':powered_a,'thrust_N':400*(g+powered_a)}
out['4.41']={'a_at725_m_s2':(725-683)/(683/g),'a_at595_m_s2':(595-683)/(683/g)}
out['4.42']={'max_a_earth_m_s2':28000/2200-g,'max_a_moon_m_s2':28000/2200-1.62}
out['4.43']={'average_force_N':.145*(50-(-40))/.008,'direction':'Outgoing ball direction'}
out['4.44']={'net_force_magnitude':'2*m*a, independent of t and b'}
a=-2*12/4**2
out['4.45']={'a_upward_m_s2':a,'mass_B_kg':36/(g+a),'mass_A_kg':(80-36)/(g+a)}
total_mass=6+4+5;accel=200/total_mass-g
out['4.46']={'a_m_s2':accel,'tension_top_N':(4+5)*(g+accel),'tension_mid_N':(2+5)*(g+accel),'tension_bottom_N':5*(g+accel)}
assert isclose(200-out['4.46']['tension_top_N']-6*g,6*accel)
out['4.47']={'a_upward_m_s2':30**2/(2*80),'engine_thrust_N':20*(g+30**2/(2*80))}
a=2*16/2**2;m=12/a;gn=2*10/2.58**2
out['4.48']={'mass_kg':m,'planet_g_m_s2':gn,'weight_planet_N':m*gn,'weight_earth_N':m*g}
out['4.49']={'distance5_m':16.8*5**3/(6*45)}
out['4.50']={'same_distance_speed_ratio':sqrt(2),'same_time_speed_ratio':2}
mph=.44704
cars=[('Alpha Romeo 4C',895,4.4),('Honda Civic',1320,6.4),('Ferrari F430',1435,3.9),('Ford Focus',1468,5.4),('Volvo S60',1650,7.2)]
rows=[dict(car=name,car_net_force_N=m*60*mph/t,passenger_net_force_N=72*60*mph/t) for name,m,t in cars]
f60=1435*60*mph/3.9;f100=1435*100*mph/8.6
out['4.51']={'cars':rows,'Ferrari_0_100_force_N':f100,'Ferrari_0_100_over_0_60_ratio':f100/f60,'top_speed_net_force_N':0,'top_speed_condition':'Straight steady motion on a level road'}
m=2.75e5/g
out['4.52']={'net_force5_N':[m*.120*5,0,-m*.120],'net_force_magnitude_N':m*hypot(.120*5,.120)}
def fit(x,y):
 n=len(x);xm=sum(x)/n;ym=sum(y)/n
 slope=sum((a-xm)*(b-ym) for a,b in zip(x,y))/sum((a-xm)**2 for a in x)
 intercept=ym-slope*xm
 return slope,intercept
forces=[250,300,350,400,450,500];times=[3.3,2.2,1.7,1.5,1.3,1.2]
accelerations=[2*8/t**2 for t in times]
mass,intercept=fit(accelerations,forces)
out['4.53']={'accelerations_m_s2':accelerations,'fit_method':'Unweighted least squares of F on a; times rounded in supplied measurements','mass_kg':mass,'intercept_N':intercept,'planet_g_m_s2':intercept/mass}
mass=[8,11,15,20];dist=[8.22,10.75,9.45,7.10];time=[2.8,3.2,3.0,2.6]
v=[2*x/t for x,t in zip(dist,time)];accel_mag=[2*x/t**2 for x,t in zip(dist,time)];force=[m*a for m,a in zip(mass,accel_mag)]
slope,intercept=fit(mass,force)
out['4.54']={'first_two_accelerations_m_s2':[-2*8.22/2.8**2,-2*4.20/2.0**2],'initial_speeds_m_s':v,'max_min_speed_ratio':max(v)/min(v),'friction_magnitudes_N':force,'linear_fit_N_per_kg':slope,'intercept_N':intercept,'fit_through_origin_N_per_kg':sum(m*f for m,f in zip(mass,force))/sum(m*m for m in mass),'restriction':'The rounded measurements support approximately constant acceleration; two observations alone do not prove its detailed time dependence'}
m=2.;b=4.;a=6.
t_turn=2*b/a;t_return=3*b/a
out['4.55']={'positive_turn_time_s':t_turn,'max_x_m':b*t_turn**2/(2*m)-a*t_turn**3/(6*m),'force_at_turn_N':b-a*t_turn,'return_time_s':t_return,'return_v_m_s':b*t_return/m-a*t_return**2/(2*m)}
assert isclose(b*t_return**2/(2*m)-a*t_return**3/(6*m),0,abs_tol=1e-12)
out['4.56']={'y':'k3*t^3/(6*m)','vy':'k3*t^2/(2*m)','x':'k1*t^2/(2*m)+k2*k3*t^5/(120*m^2)','vx':'k1*t/m+k2*k3*t^4/(24*m^2)','source_force':'Fx=k1+k2*y, not k1+k2*t'}
# Sample residual check for the coupled symbolic expressions.
k1,k2,k3,m,t=2.,3.,5.,7.,.8
y=k3*t**3/(6*m);xdd=k1/m+k2*k3*t**3/(6*m*m)
assert isclose(m*xdd,k1+k2*y)
head_mass=.094*65;a=4/.2
out['4.57']={'head_mass_kg':head_mass,'neck_force_N':head_mass*(g+a),'choice':'d,180N'}
out['4.58']={'choice':'a','reason':'Same interaction pair, equal force magnitudes throughout the collision'}
# In flight the head itself is in free fall: gravity already produces a=-g.
# Therefore normal neck support vanishes in the idealized fixed-pose model.
out['4.59']={'neck_force_N':0,'choice':'a,0N','reason':'Head accelerates at -g, so F_neck-mg=-mg'}
out['4.60']={'time_s':.4,'choice':'a','reason':'Original PDF148 graph visually inspected: At0.4s the ground reaction is below initial body weight, so the dancer bends her legs and accelerates downward. Flight with zero ground reaction occurs later, near1.2–1.5s.'}
print(json.dumps({'status':'passed','scope':'Independent original-input reference ledger; original graph4.60 visually compared','items':out},indent=2))
