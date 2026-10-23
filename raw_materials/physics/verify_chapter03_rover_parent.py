"""Independent source-input checks for Example3.1 and the following acceleration.

Outputs must be compared with the final authored example before publication.
"""
from math import hypot,atan2,degrees,isclose
import json
def position(t):return [2-.25*t*t,t+.025*t**3]
def velocity(t):return [-.5*t,1+.075*t*t]
def acceleration(t):return [-.5,.15*t]
r0=position(0);r2=position(2)
displacement=[b-a for a,b in zip(r0,r2)]
average=[v/2 for v in displacement];v2=velocity(2)
assert r2==[1,2.2]
assert isclose(average[0],-.5) and isclose(average[1],1.1)
assert isclose(v2[0],-1) and isclose(v2[1],1.3)
for t in [0,1,2,4]:
 h=1e-5
 derivative=[(b-a)/(2*h) for a,b in zip(position(t-h),position(t+h))]
 assert all(isclose(a,b,rel_tol=1e-7,abs_tol=1e-7) for a,b in zip(derivative,velocity(t)))
 second=[(b-a)/(2*h) for a,b in zip(velocity(t-h),velocity(t+h))]
 assert all(isclose(a,b,rel_tol=1e-7,abs_tol=1e-7) for a,b in zip(second,acceleration(t)))
print(json.dumps({'status':'passed','example':'3.1','r2_m':r2,'distance_m':hypot(*r2),'displacement_m':displacement,'average_m_s':average,'instantaneous_m_s':v2,'speed_m_s':hypot(*v2),'direction_deg':degrees(atan2(v2[1],v2[0])),'samples':{t:{'r':position(t),'v':velocity(t),'a':acceleration(t)} for t in [0,1,2,4]}},indent=2))
