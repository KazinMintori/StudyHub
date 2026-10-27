"""Independent physical models for chapter8 guided."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad,solve_ivp
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/"qa/physics1-remaining/ch08-guided-recomputed";OUT.mkdir(parents=True,exist_ok=True)
checks=[]
def near(name,a,b,tol=1e-9):
 assert np.allclose(a,b,rtol=tol,atol=tol),(name,a,b)
 checks.append(dict(name=name,actual=np.asarray(a).tolist(),expected=np.asarray(b).tolist()))
def yes(name,c):
 assert c,name
 checks.append(dict(name=name,passed=True))
vb=-.125*.6/.375
near('VP8.6.1a signed velocity B',vb,-.2)
near('VP8.6.1a full spring-separation momentum',.125*.6+.375*vb,0)
p=.125*.6+.75*(-.4);va=(p-.75*(-.15))/.125
near('VP8.6.1b correct distinct A-C system velocity',va,-.9)
near('VP8.6.1b distinct two-body momentum',.125*va+.75*(-.15),p)
ub=(65*(-3)+55*3.5-65*6)/55;dm=-3-6;db=3.5-ub
near('VP8.6.2a source reconstructed Buffy velocity',ub,-7.136363636363637)
near('VP8.6.2a full signed before/after momentum',65*6+55*ub,65*(-3)+55*3.5)
near('VP8.6.2b both velocity changes',[dm,db],[-9,10.636363636363637])
near('VP8.6.2b opposite interaction impulses',[65*dm,55*db],[-585,585])
yes('VP8.6.2b lighter Buffy larger velocity change',abs(db)>abs(dm))
alpha,beta=math.pi/6,math.pi/4
p1y=2.4*3.6*math.sin(alpha);v2=p1y/(4*math.sin(beta));p1x=2.4*3.6*math.cos(alpha);p2x=4*v2*math.cos(beta);px=p1x+p2x
near('VP8.6.3a both requested vertical momenta',[p1y,-p1y],[4.32,-4.32])
near('VP8.6.3b outgoing heavy-stone speed',v2,1.5273506473629423)
near('VP8.6.3c both explicit horizontal momenta',[p1x,p2x],[7.482459488697551,4.32])
near('VP8.6.3c total final horizontal momentum',px,11.80245948869755)
near('VP8.6.3d reconstructed incoming speed',px/2.4,4.91769145362398)
near('VP8.6.3 complete vertical momentum',p1y-4*v2*math.sin(beta),0)
for degrees in [5,20,40,50]:
 a=math.radians(degrees);u=3.7;m=1.8;vp=u/(2*math.cos(a));vs=u/(4*math.cos(a))
 near('VP8.6.4a outgoing speed ratio '+str(degrees),vs/vp,.5)
 near('VP8.6.4b x momentum '+str(degrees),(m*vp+2*m*vs)*math.cos(a),m*u)
 near('VP8.6.4b y momentum '+str(degrees),(m*vp-2*m*vs)*math.sin(a),0)
 # No elastic-collision assumption was used.
 near('VP8.6.4 actual energy fraction '+str(degrees),(vp*vp+2*vs*vs)/u**2,3/(8*math.cos(a)**2))
for vp,vs in [(1.,1.),(2.,.5)]:
 near('VP8.6.4 theta0 compatible horizontal momentum '+str(vp),vp+2*vs,3)
 near('VP8.6.4 theta0 y equation degenerates '+str(vp),(vp-2*vs)*math.sin(0),0)
yes('VP8.6.4 theta0 does not fix ratio',not math.isclose(1/1,.5/2))
near('VP8.6.4 theta90 cannot carry nonzero initial x momentum',math.cos(math.pi/2),0)
for moving,rest,expected in [(1,4,[8,1.6,6.4,25.6]),(4,1,[4,3.2,25.6,6.4])]:
 ki=32;u=math.sqrt(2*ki/moving);v=moving*u/(moving+rest);kf=.5*(moving+rest)*v*v;loss=ki-kf
 near('VP8.9.1 all requested numerical quantities '+str(moving),[u,v,kf,loss],expected)
 near('VP8.9.1 exact momentum '+str(moving),moving*u,(moving+rest)*v)
 near('VP8.9.1 independent reduced-mass loss '+str(moving),loss,.5*moving*rest/(moving+rest)*u*u)
 near('VP8.9.1 general loss fraction '+str(moving),loss/ki,rest/(moving+rest))
yes('VP8.9.1c heavier target loses larger fraction',25.6/32>6.4/32)
v=.5*1.4/.7;ki=.5*.5*1.4**2;kf=.5*.7*v*v
near('VP8.9.2a combined speed',v,1)
near('VP8.9.2a collision initial/final energy',[ki,kf],[.49,.35])
near('VP8.9.2a positive collision loss',ki-kf,.14)
near('VP8.9.2a exact horizontal momentum',.7*v,.5*1.4)
t=math.sqrt(2*.6/9.8);vx=v;vy=-9.8*t;speed=math.hypot(vx,vy)
near('VP8.9.2b independent projectile speed',speed,3.57211421989835)
near('VP8.9.2b independent energy equation',.5*.7*speed**2,.5*.7*v*v+.7*9.8*.6)
near('VP8.9.2b nonzero gravity impulse',.7*vy,-.7*9.8*t)
yes('VP8.9.2b total vector momentum changes',abs(.7*vy)>0)
vbox=2.4*(1.5-.825)/1.2
near('VP8.9.3a box speed',vbox,1.35)
near('VP8.9.3a exact signed momentum',2.4*.825+1.2*vbox,2.4*1.5)
kci=.5*2.4*1.5**2;kcf=.5*2.4*.825**2;kbf=.5*1.2*vbox**2
near('VP8.9.3b all requested body energies',[kci,kcf,kbf],[2.7,.81675,1.0935])
near('VP8.9.3c total final energy',kcf+kbf,1.91025)
near('VP8.9.3c actual energy loss',kci-kcf-kbf,.78975)
yes('VP8.9.3c inelastic not completely inelastic',kci>kcf+kbf and not math.isclose(.825,vbox))
p=np.array([1+2*math.cos(math.pi/4),2*math.sin(math.pi/4)])
near('VP8.9.4 explicit dimensionless initial momentum',p,[1+math.sqrt(2),math.sqrt(2)])
near('VP8.9.4 north-of-east angle',math.degrees(math.atan2(p[1],p[0])),30.361193404821716)
near('VP8.9.4 direction of final common velocity',math.degrees(math.atan2((p/3)[1],(p/3)[0])),30.361193404821716)
mass=np.array([.5,1.25,.75]);position=np.array([[0,0],[.15,.20],[.20,-.80]]);cm=mass@position/sum(mass)
near('VP8.14.1 both CM coordinates',cm,[.135,-.140])
near('VP8.14.1 explicit mass moments',mass@position,[.3375,-.3500])
near('VP8.14.1 weighted deviations sumzero',mass@(position-cm),[0,0])
x3=(6.2*(-.2)-2*1.5)/1.2
near('VP8.14.2 third coordinate',x3,-3.5333333333333337)
near('VP8.14.2 reconstructed CM',(3*0+2*1.5+1.2*x3)/6.2,-.2)
dxB=-.125*(-.96)/.5
near('VP8.14.3 correct displacement',dxB,.24)
near('VP8.14.3 stationary CM displacement',.125*(-.96)+.5*dxB,0)
# VP8.14.4 is underdetermined without initial total momentum. Construct two
# actual Newtonian systems with pairwise reciprocal forces, all original
# positions for objects1/2 preserved at t=1, but different third positions.
r0=np.array([[-1.,0],[1,0],[0,1.]])
c0=r0.mean(axis=0);q0=r0-c0
counterexamples=[]
for vcm in [np.array([0.,0]),np.array([.2,-.1])]:
 dt=1.;cf=c0+vcm*dt
 rf=np.array([[-1/3,.25],[.5,-1.],[-1/6+3*vcm[0]*dt,7/4+3*vcm[1]*dt]])
 qf=rf-cf
 w0=(qf-q0*math.cos(dt))/math.sin(dt)
 initial_velocities=w0+vcm
 def rhs(t,z):
  r=z[:6].reshape(3,2);vel=z[6:].reshape(3,2)
  # Pairwise Fij=(rj-ri)/3, m_i=1, angular frequency1.
  f=np.stack([sum((r[j]-r[i])/3 for j in range(3) if j!=i) for i in range(3)])
  return np.r_[vel.ravel(),f.ravel()]
 z0=np.r_[r0.ravel(),initial_velocities.ravel()]
 sol=solve_ivp(rhs,[0,dt],z0,rtol=1e-11,atol=1e-12)
 actual=sol.y[:6,-1].reshape(3,2)
 near('VP8.14.4 original first-two final positions '+str(vcm),actual[:2],rf[:2])
 near('VP8.14.4 full physical final positions '+str(vcm),actual,rf)
 near('VP8.14.4 CM inertial motion '+str(vcm),actual.mean(axis=0),cf)
 near('VP8.14.4 initial CM speed '+str(vcm),initial_velocities.mean(axis=0),vcm)
 near('VP8.14.4 final total momentum '+str(vcm),sol.y[6:,-1].reshape(3,2).sum(axis=0),3*vcm)
 counterexamples.append(actual[2].tolist())
near('VP8.14.4 conditional standard third location',counterexamples[0],[-1/6,7/4])
yes('VP8.14.4 same stated source data admits two third locations',not np.allclose(counterexamples[0],counterexamples[1]))
r=dict(status="passed",checksCount=len(checks),checks=checks)
(OUT/"numeric-guided.json").write_bytes((json.dumps(r,ensure_ascii=False,indent=2)+"\n").encode("utf8"))
print("PASS guided:",len(checks),"independent physical checks.")
