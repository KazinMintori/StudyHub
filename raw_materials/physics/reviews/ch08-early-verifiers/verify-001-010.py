"""Independent physical models for source-reviewed chapter8 units 001-010."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad,solve_ivp
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/"qa/physics1-remaining/ch08-early-recomputed";OUT.mkdir(parents=True,exist_ok=True)
checks=[]
def near(name,a,b,tol=1e-9):
    assert np.allclose(a,b,rtol=tol,atol=tol),(name,a,b)
    checks.append(dict(name=name,actual=np.asarray(a).tolist(),expected=np.asarray(b).tolist()))
def yes(name,c):
    assert c,name
    checks.append(dict(name=name,passed=True))
near('1 actualtruck momentum',10000*12,120000)
near('1 actualSUV speed equalp',10000*12/2000,60)
near('1 actualSUV speed equalK',math.sqrt(10000/2000)*12,26.832815729997478)
near('1 kineticenergy same at computed speed',.5*2000*(math.sqrt(5)*12)**2,.5*10000*12**2)
vx=15*math.cos(math.radians(40));vy=15*math.sin(math.radians(40))
near('2 actual initial px',7.3*vx,83.8818665215281)
near('2 actual initial py',7.3*vy,70.38524326067605)
near('2 norm of projected momentum',math.hypot(7.3*vx,7.3*vy),7.3*15)
momentumA=np.array([0,-5*11.]);momentumB=6*10*np.array([math.cos(math.pi/3),math.sin(math.pi/3)]);momentumC=np.array([-10*3.,0])
near('3 actual A momentumvector',momentumA,[0,-55])
near('3 actual B momentumvector',momentumB,[30,30*math.sqrt(3)])
near('3 actual C momentumvector',momentumC,[-30,0])
near('3 actual A+C total',momentumA+momentumC,[-30,-55])
near('3 actual B+C total',momentumB+momentumC,[0,51.96152422706631])
near('3 actual A+B+C total',momentumA+momentumB+momentumC,[0,-3.038475772933689])
near('3 keep B precision ratherthan prematureround',30*math.sqrt(3)-55,-3.038475772933689)
p1=np.array([-2500*14.,0]);p2=np.array([0,1500*23.]);total=p1+p2
near('4 actual totalvector',total,[-35000,34500])
near('4 actual norm',np.linalg.norm(total),49145.193050795926)
near('4 actual directiondegrees from+x',math.degrees(math.atan2(total[1],total[0])),135.41219274140232)
near('4 actual northofwest angle',math.degrees(math.atan2(total[1],-total[0])),44.58780725859768)
near('5 actual signedmomentum',110*2.75-125*2.6,-22.5)
near('5 actualfirst kineticenergy',.5*110*2.75**2,415.9375)
near('5 actualsecond kineticenergy',.5*125*2.6**2,422.5)
near('5 actual totalkineticenergy',.5*110*2.75**2+.5*125*2.6**2,838.4375)
yes('5 near cancellation ofp notcancellation ofK',abs(110*2.75-125*2.6)<min(110*2.75,125*2.6))
for name,u,v,J,force in [('serve',0,73,4.161,138.7),('return',73,-55,-7.296,-243.2)]:
    near('6 '+name+' actualsignedimpulse',.057*(v-u),J)
    near('6 '+name+' actual meanforce',.057*(v-u)/.03,force)
    near('6 '+name+' impulse changesmomentum',.057*v-.057*u,force*.03)
near('7 actual impulse',.045*25,1.125)
near('7 actual meannetforce',.045*25/.002,562.5)
near('7 gravityforce actualmagnitude',.045*9.8,.441)
near('7 small gravityimpulse fraction',.045*9.8*.002/(.045*25),.000784)
near('8 exact opposite velocities impulse',.145*(55-(-45)),14.5)
near('8 exact averageforce',.145*100/.002,7250)
for force,v,expectedJ in [(25,10.8125,1.25),(-12,-.75,-.6)]:
    near('9 actual impulse F'+str(force),force*.05,expectedJ)
    near('9 actual velocity F'+str(force),3+force*.05/.160,v)
    near('9 actual finalmomentum F'+str(force),.160*v,.160*3+expectedJ)
u=np.array([40.,0]);v=52*np.array([-math.cos(math.pi/6),math.sin(math.pi/6)])
force=.145*(v-u)/.00175
near('10 actual outgoingvelocitycomponents',v,[-45.03332099679081,26])
near('10 actual avg horizontalforce',force[0],-7045.618025448382)
near('10 actual avg verticalforce',force[1],2154.285714285714)
near('10 actual vectorimpulse',force*.00175,.145*(v-u))
yes('10 correct quadrant leftup',force[0]<0 and force[1]>0)
report=dict(status="passed",checksCount=len(checks),checks=checks)
(OUT/"numeric-001-010.json").write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+"\n").encode("utf8"))
print("PASS 001-010:",len(checks),"independent physical checks.")
