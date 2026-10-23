"""Parent's independent calculation of every chapter3 Guided Practice item.

Only the original prompt inputs are used; no authored solution is evaluated as
code. Symbolic cases are also tested numerically across positive input values.
"""
from math import sin,cos,sqrt,pi,radians,degrees,atan2,isclose
import json
g=9.8
ledger={}
vx=25*cos(radians(36.9));vy=25*sin(radians(36.9))
t=vy/g
ledger['VP3.9.1']={'top_time_s':t,'top_height_m':vy*vy/(2*g),'flight_s':2*t,'range_m':vx*2*t}
vy=g*1.05
ledger['VP3.9.2']={'launch_m_s':vy/sin(radians(30)),'height_m':vy*vy/(2*g)}
vx=15*cos(radians(50));vy=15*sin(radians(50));t=(vy+sqrt(vy*vy+2*g*20))/g
assert isclose(20+vy*t-g*t*t/2,0,abs_tol=1e-12)
ledger['VP3.9.3']={'flight_s':t,'range_m':vx*t,'final_vx':vx,'final_vy':vy-g*t}
for speed in [1.,3.,15.,100.]:
    t=2*speed/g;x=speed*t;y=-g*t*t/2
    assert isclose(x,-y)
    t=speed/g
    assert isclose(-g*t,-speed)
    assert isclose(speed*t,speed*speed/g)
ledger['VP3.9.4']={'equal_displacement_t':'2*v0/g','x':'2*v0**2/g','y':'-2*v0**2/g','direction45_t':'v0/g','direction45_x':'v0**2/g','direction45_y':'-v0**2/(2*g)'}
ledger['VP3.12.1']={'radius_m':10**2/5}
ledger['VP3.12.2']={'period_s':2*pi*265/40,'radial_m_s2':40**2/265}
ledger['VP3.12.3']={str(r):{'speed_m_s':2*pi*r/.670,'radial_m_s2':(2*pi/.670)**2*r} for r in [.10,.20]}
ledger['VP3.12.4']={name:{'speed_m_s':2*pi*r/(days*86400),'radial_m_s2':4*pi*pi*r/(days*86400)**2} for name,r,days in [('Venus',1.08e11,225),('Earth',1.50e11,365),('Mars',2.28e11,687)]}
ledger['VP3.12.5']={'TA_TB':4,'aA_aB':1/8}
ledger['VP3.15.1']={'police_relative_SUV_m_s':35-(-18),'SUV_relative_police_m_s':-18-35}
ledger['VP3.15.2']={'A_relative_B_east_m_s':90,'B_relative_A_east_m_s':-90,'component_along_line_m_s':0}
ledger['VP3.15.3']={'truck_relative_SUV':[16,20],'SUV_relative_truck':[-16,-20],'speed_m_s':sqrt(16**2+20**2),'angle_north_of_east_deg':degrees(atan2(20,16))}
wind=40/sqrt(2);vx=-wind;vy=155-wind
ledger['VP3.15.4']={'air_vx_east':vx,'air_vy_north':vy,'airspeed_m_s':sqrt(vx*vx+vy*vy),'heading_west_of_north_deg':degrees(atan2(-vx,vy))}
assert len(ledger)==13
assert isclose(ledger['VP3.12.1']['radius_m'],20)
assert isclose(ledger['VP3.12.5']['TA_TB'],4)
assert ledger['VP3.15.1']['police_relative_SUV_m_s']==53
print(json.dumps({'status':'passed','scope':'Independent original prompt calculations; numerical values require comparison to the final authored prose before publication','items':ledger},ensure_ascii=False,indent=2))
