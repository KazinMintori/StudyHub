"""Independent ledger from original Chapter4 exercises 4.1–4.30.

Numerical inputs transcribed from PDF144–145; figure angles read visually.
This ledger does not certify a worker's prose without a separate comparison.
"""
from math import sin,cos,radians,degrees,hypot,atan2,sqrt,isclose
import json
g=9.80
def component(f,angle):
 return [f*cos(radians(angle)),f*sin(radians(angle))]
def polar(x,y):
 return dict(x=x,y=y,magnitude=hypot(x,y),angle_deg=degrees(atan2(y,x))%360)
out={}
out['4.1']=polar(270+300*cos(radians(60)),300*sin(radians(60)))
forces=[component(985,31),component(788,122),component(411,233)]
out['4.2']={'individual_N':forces,'resultant_N':polar(sum(f[0] for f in forces),sum(f[1] for f in forces))}
T=5/(2*cos(radians(75/2)))
assert isclose(2*T*cos(radians(37.5)),5)
out['4.3']={'tension_N':T,'angle_between_straps_deg':75}
F=90/cos(radians(30));out['4.4']={'F_N':F,'normal_component_N':F*sin(radians(30))}
f1=component(9,120);f2=component(6,233.1)
out['4.5']=polar(f1[0]+f2[0],f1[1]+f2[1])
a=(3e6)**2/(2*.018);t=3e6/a
assert isclose(.5*a*t*t,.018)
out['4.6']={'a_m_s2':a,'time_s':t,'net_force_N':9.11e-31*a}
out['4.7']={'force_N':68.5*(0-2.4)/3.52,'direction':'Opposite initial velocity'}
out['4.8']={'normal_N':625/g*(g+2.50),'package_tension_N':3.85*(g+2.50)}
out['4.9']={'mass_kg':48/2.20}
a=2*11/5**2
out['4.10']={'acceleration_m_s2':a,'mass_kg':80/a,'next_5s_distance_m':a*5*5}
a=.250/.160;v2=a*2;x2=.5*a*2**2;x5=x2+v2*3
out['4.11']={'x2_m':x2,'v2_m_s':v2,'x5_m':x5,'x7_m':x5+v2*2+.5*a*2**2,'v7_m_s':v2+a*2}
a=14/32.5
out['4.12']={'a_m_s2':a,'x10_m':.5*a*10**2,'v10_m_s':a*10}
out['4.13']={'max_force_N':4.50*10,'max_interval_s':[2,4],'zero_at_s':[0,6],'constant_intervals':'[2,4] and after6 if the graph is extended with zero acceleration'}
out['4.14']={'max_force_N':2.75*(8/2),'max_interval_s':[0,2],'zero_interval_s':[2,6],'force_at_8_5_N':2.75*(12-8)/(10-6)}
A=100;B=(150-100)/2**2
out['4.15']={'A_N':A,'B_N_s2':B,'net_at_0_N':A-8*g,'a0_m_s2':A/8-g,'net_at_3_N':A+B*3**2-8*g,'a3_m_s2':(A+B*3**2)/8-g,'a3_no_gravity_m_s2':(A+B*3**2)/8}
mass=17.5/g
out['4.16']={'mass_kg':mass,'moon_g_m_s2':3.24/mass}
out['4.17']={'horizontal_force_N':2400/g*12}
out['4.18']={'flea_mass_kg':210e-9,'flea_weight_N':210e-9*g,'froghopper_mass_kg':12.3e-6,'froghopper_weight_N':12.3e-6*g,'cat_weight_lb':45/4.448221615260,'cat_mass_kg':45/g,'source_note':'PDF visually gives 210 micrograms, not210mg. Text extraction drops the Greek mu.'}
mass=44/g
out['4.19']={'mass_earth_and_io_kg':mass,'weight_io_N':mass*1.81}
out['4.20']={'type':'Estimate','weight_lb_per_mass_kg':g/4.448221615260,'restriction':'Any assumed masses must be labeled assumptions; no invented universal class averages'}
out['4.21']={'force_N':55*15,'force_on_sprinter':'Starting blocks, through contact with the feet'}
out['4.22']={'force_on_car_N':1600,'direction':'West'}
out['4.23']={'system_a_m_s2':250/(20+5),'contact_force_N':5*250/(20+5)}
out['4.24']={'acceleration_m_s2':(620-650)/(650/g),'normal_reaction':'Passenger pushes the floor down with620N','weight_reaction':'Passenger attracts the Earth upward with650N'}
out['4.25']={'earth_acceleration_m_s2':45*g/6e24}
out['4.26']={'frictionless_case':'A: mg down, normal up, static friction horizontally in the direction of the pull on B','balanced_pull_case':'Constant shared velocity: A has no horizontal force in the ideal model'}
out['4.27']={'a':'F/(mA+mB)','T':'mB*F/(mA+mB)','threshold':'Any nonzero horizontal force accelerates the frictionless system, irrespective of its total weight'}
a=-350**2/(2*.130);t=-350/a
assert isclose(350*t+.5*a*t*t,.130)
out['4.28']={'stopping_time_s':t,'force_N':.00180*a}
out['4.29']={'uniform_velocity':'Vertical tension balances weight','accelerating_east':'Ball hangs west of attachment; tension has east component; net force is east'}
out['4.30']={'normal_N':12*g+40*sin(radians(37))}
assert out['4.18']['flea_weight_N']<out['4.18']['froghopper_weight_N']
assert isclose(out['4.23']['contact_force_N'],50)
print(json.dumps({'status':'passed','scope':'Original-input independent reference values; final authored solutions require explicit comparison','items':out},indent=2))
