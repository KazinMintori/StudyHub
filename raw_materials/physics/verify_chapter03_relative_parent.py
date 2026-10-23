"""Independent original-input ledger for chapter3 exercises3.31–3.45.

The ledger does not certify completeness of final prose, diagrams or all parts.
"""
from math import pi,sqrt,hypot,atan2,degrees,asin,isclose
import json
g=9.8
def polar(x,y):return {'components':[x,y],'magnitude':hypot(x,y),'angle_from_east_deg':degrees(atan2(y,x))%360}
out={}
out['3.31']={'bottom_a_up_m_s2':36/14,'top_a_down_m_s2':36/14,'period_s':2*pi*14/6}
out['3.32']={'top_direction':'toward center, downward','bottom_direction':'toward center, upward','bottom_top_ratio':'(v2/v1)^2'}
r=8.84;a=12.5*g;omega=sqrt(a/r)
out['3.33']={'head_speed_m_s':omega*r,'head_feet_acceleration_difference_m_s2':omega**2*2,'rpm':omega*60/(2*pi)}
out['3.34']={name:{'speed_m_s':2*pi*r/(T*86400),'radial_m_s2':4*pi*pi*r/(T*86400)**2} for name,r,T in [('Earth',1.5e11,365),('Mercury',5.79e10,88)]}
out['3.35']={'same_direction_time_s':35/2.5,'opposite_direction_time_s':35/.5}
out['3.36']={'scooter_relative_flatcar_rightward_m_s':[18-13,-3-13,0-13]}
x=.4/sqrt(2)-.5;y=-.4/sqrt(2)
out['3.37']={'canoe_relative_river_m_s':polar(x,y)}
out['3.38']={'boat_round_trip_h':1.5/(4+2.8)+1.5/(4-2.8),'walk_round_trip_h':3/4}
south=sqrt(100**2-40**2)
out['3.39']={'heading_west_of_south_deg':degrees(asin(.4)),'ground_speed_km_h':south,'flight500km_h':500/south}
out['3.40']={'ground_velocity_m_s':polar(-10/sqrt(2),-35-10/sqrt(2))}
out['3.41']={'ground_velocity_m_s':polar(4.2,-2),'crossing_s':500/4.2,'south_drift_m':2*500/4.2}
east=sqrt(4.2**2-2**2)
out['3.42']={'heading_north_of_east_deg':degrees(asin(2/4.2)),'ground_east_m_s':east,'crossing_s':500/east}
out['3.43']={'heading_north_of_west_deg':degrees(asin(80/320)),'ground_west_km_h':sqrt(320**2-80**2)}
t=8.;x=.4*t*t/2;y=-.18*t**3/6
out['3.44']={'position_m':[x,y],'distance_m':hypot(x,y)}
out['3.45']={'positive_time':'2*b/(3*c)','exclude':'t=0 because zero velocity has no direction'}
for b,c in [(1.,2.),(3.,4.),(.1,5.)]:
 t=2*b/(3*c)
 assert isclose(2*b*t,3*c*t*t)
assert isclose(out['3.35']['opposite_direction_time_s'],70)
assert out['3.38']['boat_round_trip_h']>out['3.38']['walk_round_trip_h']
assert isclose(east**2+2**2,4.2**2)
print(json.dumps({'status':'passed','scope':'Source-input independent calculations; final written answers and figures require comparison','items':out},indent=2))
