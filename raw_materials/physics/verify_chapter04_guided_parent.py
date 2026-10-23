"""Recalculate all twelve Chapter4 variation problems and chain bridge."""
from math import sin,cos,radians,hypot,atan2,degrees,isclose
import json
g=9.8
def polar(x,y):return dict(x=x,y=y,magnitude=hypot(x,y),angle_deg=degrees(atan2(y,x))%360)
out={}
out['VP4.1.1']=polar(40+60*cos(radians(36.9)),-80+60*sin(radians(36.9)))
out['VP4.1.2']=polar(45-235*cos(radians(36.9)),105+235*sin(radians(36.9)))
out['VP4.1.3']=polar(60*cos(radians(70))+15*cos(radians(160)),60*sin(radians(70))+15*sin(radians(160))-60)
out['VP4.1.4']=polar(-24*cos(radians(30))-35,-24*sin(radians(30))-50)
out['VP4.4.1']={'a_m_s2':25/55}
out['VP4.4.2']={'a_m_s2':.50/2,'forces':'Gravity, normal, hand push'}
out['VP4.4.3']={'horizontal_force_N':.16*75,'normal_over_weight':1}
out['VP4.4.4']={'net_force_N':.8*12,'friction_N':14-.8*12,'friction_direction':'Opposite push'}
out['VP4.5.1']={'friction_N':20*3**2/(2*2.25)}
out['VP4.5.2']={'stopping_distance_m':1.7e5*75**2/(2*2.9e5)}
a=-25**2/(2*48)
out['VP4.5.3']={'stop_time_s':-25/a,'acceleration_m_s2':a,'braking_force_magnitude_N':2.4e3*abs(a)}
a=1.4**2/(2*5)
out['VP4.5.4']={'a_m_s2':a,'friction_N':800-1.15e3*a,'forces':'Weight, normal, road friction, combined push'}
bridge=[]
for force in [9,7.35]:
 a=force/(3*.25)-g
 top_middle=2*.25*(g+a);middle_bottom=.25*(g+a)
 assert isclose(force-top_middle-.25*g,.25*a,abs_tol=1e-12)
 assert isclose(top_middle-middle_bottom-.25*g,.25*a,abs_tol=1e-12)
 assert isclose(middle_bottom-.25*g,.25*a,abs_tol=1e-12)
 bridge.append(dict(applied_force_N=force,a_m_s2=a,top_on_middle_N=top_middle,middle_on_bottom_N=middle_bottom))
out['bridge']={'cases':bridge,'force_order':'Bottom contact < upper contact < rope pull, for both positive applied forces'}
assert len([k for k in out if k.startswith('VP')])==12
print(json.dumps({'status':'passed','scope':'Independent source-input reference; compare final authored solutions separately','items':out},indent=2))
