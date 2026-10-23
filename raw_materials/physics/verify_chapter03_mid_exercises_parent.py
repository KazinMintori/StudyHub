"""Independent original-input checks for3.18–3.30, before final prose audit."""
from math import sin,cos,sqrt,pi,radians,degrees,acos,hypot,isclose
import json
g=9.8;out={}
vx=12*cos(radians(51));vy=12*sin(radians(51));t=2.08
height=g*t*t/2-vy*t
out['3.18']={'a':[0,-g],'initial_v':[vx,vy],'final_v':[vx,vy-g*t],'range_m':vx*t,'release_height_m':height,'range_formula_condition':'Launch and landing elevations differ','graphs':{'x':'v0x*t','y':'height+v0y*t-g*t^2/2','vx':'v0x','vy':'v0y-g*t'}}
assert isclose(height+vy*t-g*t*t/2,0,abs_tol=1e-12)
vx=6.4*cos(radians(60));vy=6.4*sin(radians(60));t=2.1/vx
out['3.19']={'height_m':vy*t-g*t*t/2,'impact_vy':vy-g*t}
vx=45/3;vy=sqrt(25**2-vx**2)
out['3.20']={'angle_deg':degrees(acos(vx/25)),'top_speed_m_s':vx,'top_a':[0,-g],'wall_height_m':vy*3-g*9/2,'wall_speed_m_s':hypot(vx,vy-g*3)}
vx=30*cos(radians(33));vy=30*sin(radians(33));t=(vy+sqrt(vy*vy+2*g*15))/g
out['3.21']={'height_above_roof_m':vy*vy/(2*g),'impact_speed_m_s':sqrt(30**2+2*g*15),'flight_s':t,'range_m':vx*t}
vx=15*cos(radians(53));vy=15*sin(radians(53));disc=vy*vy-2*g*5
times=[(vy-sqrt(disc))/g,(vy+sqrt(disc))/g]
out['3.22']={'times_s':times,'velocities_m_s':[[vx,vy-g*t] for t in times]}
assert all(isclose(vy*t-g*t*t/2,5,abs_tol=1e-12) for t in times)
out['3.23']={'parameterized_estimate':'For assumed maximum range R with equal launch/landing height and optimum angle45deg: v0=sqrt(g*R), vertical height=R/2, Mars range=g*R/3.7. Actual personal estimate remains an explicit assumption.'}
out['3.24']={'radius_m':6*.3048,'parameterized_estimate':'v=2*pi*r/T, ar=4*pi^2*r/T^2 for stated assumed period T','half_period_acceleration_factor':4}
r=6380e3;T=24*3600;a=4*pi*pi*r/T**2
out['3.25']={'equator_radial_m_s2':a,'fraction_g':a/g,'threshold_period_s':2*pi*sqrt(r/g),'escape_condition':'Rotation period below threshold in this stated surface-force model'}
a=(2*pi*3)**2*.07
out['3.26']={'radial_m_s2':a,'radial_g':a/g}
r=.8*sin(radians(37));out['3.27']={'orbit_radius_m':r,'radial_m_s2':4*pi*pi*r/.6**2}
omega=550*2*pi/60;v=omega*3.4
out['3.28']={'tip_m_s':v,'radial_g':omega**2*3.4/g}
v=sqrt(5.5*g*280)
out['3.29']={'threshold_m_s':v,'threshold_mph':v/.44704,'condition':'Above this speed, stipulated upward kinematic acceleration exceeds5.5g'}
out['3.30']={'radial':'2*pi*v/T','double_speed_period_factor':2,'double_radius_period_factor':sqrt(2)}
for v,T in [(1,2),(5,3),(40,20)]:
 r=v*T/(2*pi)
 assert isclose(v*v/r,2*pi*v/T)
 assert isclose(4*pi*pi*(2*r)/(sqrt(2)*T)**2,4*pi*pi*r/T**2)
print(json.dumps({'status':'passed','scope':'Independent source-input calculations, final authored prompts, solutions and requested plots still need direct comparison','items':out},indent=2))
