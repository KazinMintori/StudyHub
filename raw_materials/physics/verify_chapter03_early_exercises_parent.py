"""Independent calculations from chapter3 original early exercise inputs.

Final prose and plots must separately be compared to these values. No worker
solution text is executed or used as the expected numerical answer.
"""
from math import sin,cos,sqrt,hypot,radians,degrees,atan2,isclose
import json
g=9.8
def polar(x,y):return {'x':x,'y':y,'magnitude':hypot(x,y),'angle_deg':degrees(atan2(y,x))%360}
out={}
out['3.3']={'average_cm_s':polar(5,5),'instantaneous_cm_s':{t:polar(5*t,5) for t in [0,1,2]},'path':'x=4+0.1*y^2, 0<=y<=10 (cm)'}
t=5.;x=.280*t+.0360*t*t;y=.0190*t**3
out['3.4']={'distance_m':hypot(x,y),'velocity_m_s':polar(.280+2*.0360*t,3*.0190*t*t)}
out['3.5']={'average_acceleration_m_s2':polar((-170-90)/30,(40-110)/30)}
vx=2.6+.45*cos(radians(31))*10;vy=-1.8+.45*sin(radians(31))*10
out['3.6']={'final_velocity_m_s':polar(vx,vy)}
out['3.7']={'position2_m':[4.8,-1.8],'velocity2_m_s':polar(2.4,-4.8),'acceleration_m_s2':polar(0,-2.4),'v_dot_a':(-4.8)*(-2.4),'speed_change':'increasing','turning':'clockwise'}
t=8.;vx=5-.018*t*t;vy=2+.550*t
out['3.8']={'velocity8_m_s':polar(vx,vy),'acceleration8_m_s2':polar(-.036*t,.550)}
t=.480;vx=1.10;vy=-g*t
out['3.9']={'table_height_m':g*t*t/2,'horizontal_distance_m':vx*t,'impact_velocity_m_s':polar(vx,vy),'graphs':'x=1.10t,y=-4.90t^2,vx=1.10,vy=-9.80t; launch origin'}
out['3.10']={'minimum_speed_m_s':1.75/sqrt(2*9/g)}
out['3.11']={'range_m':.950*2.70}
top=12/g
out['3.12']={'top_time_s':top,'height_m':12**2/(2*g),'flight_s':2*top,'range_m':20*2*top,'graphs':'x=20t,y=12t-4.90t^2,vx=20,vy=12-9.80t'}
t=sqrt(2*(21.3-1.8)/g);vx=48/t;vy=-g*t
out['3.13']={'launch_speed_m_s':vx,'flight_s':t,'impact_speed_m_s':hypot(vx,vy)}
vy=sqrt(2*g*.587);vx=vy*cos(radians(58))/sin(radians(58))
out['3.14']={'launch_speed_m_s':vy/sin(radians(58)),'range_m':vx*2*vy/g}
out['3.15']={'planet_acceleration_m_s2':g/2.76**2}
vx=40*cos(radians(60));vy=40*sin(radians(60))
out['3.16']={'launch_components_m_s':[vx,vy],'top_time_s':vy/g,'max_height_m':vy*vy/(2*g),'range_m':vx*2*vy/g,'top_velocity_m_s':[vx,0],'top_acceleration_m_s2':[0,-g]}
vx=30*cos(radians(36.9));vy=30*sin(radians(36.9));disc=vy*vy-2*g*10
times=[(vy-sqrt(disc))/g,(vy+sqrt(disc))/g]
assert all(isclose(vy*t-g*t*t/2,10,abs_tol=1e-10) for t in times)
out['3.17']={'times_at10m_s':times,'velocities_at10m_m_s':[polar(vx,vy-g*t) for t in times],'return_velocity_m_s':polar(vx,-vy)}
assert isclose(out['3.11']['range_m'],2.565)
assert out['3.7']['v_dot_a']>0
print(json.dumps({'status':'passed','scope':'Original-input numerical ledger for3.3–3.17; final source/prose/plot comparison remains required','items':out},indent=2))
