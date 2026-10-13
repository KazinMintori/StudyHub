"""Numerical vector and scaling checks for chapter 29 discussion solutions."""
from pathlib import Path
import json,math
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def record(name,passed,**data):
 assert passed,(name,data)
 checks.append({'id':name,**data})
def loop_field(points,radius=1.,segments=4096):
 theta=(np.arange(segments)+.5)*2*np.pi/segments
 source=np.c_[radius*np.cos(theta),radius*np.sin(theta),np.zeros(segments)]
 dl=np.c_[-radius*np.sin(theta),radius*np.cos(theta),np.zeros(segments)]*(2*np.pi/segments)
 values=[]
 for point in points:
  dr=point-source
  values.append(np.sum(np.cross(dl,dr)/np.linalg.norm(dr,axis=1)[:,None]**3,axis=0))
 return np.array(values)

omega,B,A,R=7.,.3,.04,2.
phi=.7
emf=lambda w:w*B*A*np.sin(phi)
torque=lambda w:emf(w)/R*A*B*np.sin(phi)
power=lambda w:w*w*B*B*A*A/(2*R)
record('Q29.2/double-speed',math.isclose(emf(2*omega)/emf(omega),2) and math.isclose(torque(2*omega)/torque(omega),2) and math.isclose(power(2*omega)/power(omega),4))
outside=loop_field([[2.,0.,0.]])[0]
record('Q29.3/field-outside',outside[2]<0,field=outside.tolist())
# East +x, north +y and up +z. Right of an eastbound observer is south.
force=np.cross([1.,0.,0.],[0.,0.,1.])
record('Q29.7/right-wing',np.allclose(force,[0.,-1.,0.]),force=force.tolist())
# Small loop lies inside the large loop and is displaced toward the left.
# Its induced clockwise current opposes an increasing CCW source current.
theta=(np.arange(1024)+.5)*2*np.pi/1024
small_r=.25;center=np.array([-.20,0.,0.])
points=center+np.c_[small_r*np.cos(theta),small_r*np.sin(theta),np.zeros(1024)]
dl=-np.c_[-small_r*np.sin(theta),small_r*np.cos(theta),np.zeros(1024)]*(2*np.pi/1024)
field=loop_field(points)
total_force=np.sum(np.cross(dl,field),axis=0)
record('Q29.8/force-toward-center',total_force[0]>0 and abs(total_force[1])<1e-9,force=total_force.tolist())
# A rectangular loop at x>0 near a straight wire has a greater attractive
# force at the near edge than the repulsive force at the far edge.
near,far=.2,.5
record('Q29.9/attraction',1/near-1/far>0)
r=.03;rate=.12
emf_r=math.pi*r*r*rate;emf_2r=math.pi*(2*r)**2*rate
electric_r=emf_r/(2*math.pi*r);electric_2r=emf_2r/(2*math.pi*2*r)
record('Q29.13/radius-doubled',math.isclose(emf_2r/emf_r,4) and math.isclose(electric_2r/electric_r,2))
file=ROOT/'qa/physics/chapter29/discussion-checks.json';file.parent.mkdir(parents=True,exist_ok=True)
file.write_text(json.dumps({'status':'passed','checks':checks},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('PASS:',len(checks),'independent vector and scaling checks.')
