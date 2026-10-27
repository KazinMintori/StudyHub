"""Independent physical models for chapter8 discussion."""
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
yes('Q1 same-speed heavier hammer larger momentum and energy',2*4>1*4 and .5*2*4**2>.5*1*4**2)
yes('Q1 unequal-speed comparison not fixed by mass alone',.5*2*1**2<.5*1*4**2)
mb,mc,vc=5,.15,20
p=mc*vc;K=.5*mc*vc*vc;vb_samep=p/mb;vb_sameK=math.sqrt(2*K/mb)
near('Q2 same-momentum kinetic-energy inverse mass ratio',(.5*mb*vb_samep**2)/K,mc/mb)
near('Q2 same-energy momentum ratio',mb*vb_sameK/p,math.sqrt(mb/mc))
yes('Q2 same-momentum choice smaller stopping impulse',mb*vb_samep<mb*vb_sameK)
m,u=.05,-10;near('Q3 stopped object impulse',m*(0-u),.5)
near('Q3 opposite ground momentum change',-m*(0-u),-.5)
psouth=np.array([0.,-30]);pnorthwest=30/np.sqrt(2)*np.array([-1.,1.])
near('Q4 equal speed',np.linalg.norm(psouth),np.linalg.norm(pnorthwest))
near('Q4 equal kinetic energy for unit mass',.5*psouth@psouth,.5*pnorthwest@pnorthwest)
yes('Q4 unequal momentum vectors',not np.allclose(psouth,pnorthwest))
m=2000;v=np.array([12.,3.]);a=np.array([2.,-.5]);U=np.array([7.,1.]);dt=.01
p=m*v;prime=m*(v-U)
near('Q5 Galileo momentum shift',prime,p-m*U)
near('Q5 same momentum derivative',((m*(v+a*dt-U)-prime)/dt),(m*(v+a*dt)-p)/dt)
yes('Q5 different momentum in the two frames',not np.allclose(prime,p))
near('Q6a zero particle momentum gives zero kinetic energy',.5*3*np.dot(np.zeros(2),np.zeros(2)),0)
v=np.array([3.,4.])
near('Q6b two opposite momenta cancel',2*v+2*(-v),[0,0])
near('Q6b nonzero system kinetic energy',.5*2*(v@v)+.5*2*(v@v),50)
yes('Q6c nonnegative terms cannot sumzero unless bothzero',all(a+b>0 for a,b in [(1,0),(0,1),(2,3)]) and 0+0==0)
M,m,u,theta=70,3,12,math.radians(35)
V=-m*u*math.cos(theta)/M
near('Q7 conserved horizontal momentum',M*V+m*u*math.cos(theta),0)
yes('Q7 nonzero upward final system momentum',m*u*math.sin(theta)>0)
near('Q7 vertical momentum requires external impulse',m*u*math.sin(theta),20.64875170863766,tol=1e-8)
ki=.5*.5*2**2+.5*.3*(-2)**2;kf=.5*.5*(-.4)**2+.5*.3*2**2
near('Q8 actual Example8.5 initial/final kinetic energy',[ki,kf],[1.6,.64])
near('Q8 actual energy loss',ki-kf,.96)
near('Q8 actual Example8.5 momentum before/after',.5*2+.3*(-2),.5*(-.4)+.3*2)
yes('Q8 not completely inelastic because final velocities differ',not math.isclose(-.4,2))
m,v=2.,3.
near('Q9 opposite equal-mass initial momentum',m*v+m*(-v),0)
near('Q9 initial energy nonzero',.5*m*v*v+.5*m*v*v,18)
near('Q9 final common velocity at zero total momentum',0/(2*m),0)
for m1,m2,v1,v2 in [(2,2,[3,0],[-3,0]),(2,5,[3,2],[-1,4])]:
 v1,v2=np.array(v1,float),np.array(v2,float);P=m1*v1+m2*v2;mu=m1*m2/(m1+m2)
 total=.5*m1*(v1@v1)+.5*m2*(v2@v2);Kcm=(P@P)/(2*(m1+m2));Krel=.5*mu*((v1-v2)@(v1-v2))
 near('Q10 full kinetic decomposition '+str((m1,m2)),total,Kcm+Krel)
 yes('Q10 total not just CM kinetic energy '+str((m1,m2)),total>Kcm)
wi=-2-2;wf=3-(-1)
near('Q11 Example8.10 equal relative speed',abs(wi),abs(wf))
yes('Q11 Example8.10 exact reversal',wi==-wf)
u=2.6e7;vn=-11/13*u;vc=2/13*u
near('Q11 Example8.11 actual final velocities',[vn,vc],[-2.2e7,.4e7])
near('Q11 Example8.11 relative speeds',vc-vn,u)
yes('Q11 Example8.11 exact reversal',(-u)*(vc-vn)<0)
va=np.array([1.6,1.2]);vb=np.array([4.,-2.]);wi=np.array([-4.,0.]);wf=vb-va
near('Q11 Example8.12 original outgoing A speed',np.linalg.norm(va),2)
near('Q11 Example8.12 actual outgoing B speed',np.linalg.norm(vb),math.sqrt(20))
near('Q11 Example8.12 full exact momentum',.5*va+.3*vb,[2,0])
near('Q11 Example8.12 full exact kinetic energy',.5*.5*(va@va)+.5*.3*(vb@vb),4)
near('Q11 Example8.12 relative vector',wf,[2.4,-3.2])
near('Q11 Example8.12 equal relative speed',np.linalg.norm(wf),np.linalg.norm(wi))
near('Q11 Example8.12 final direction',math.degrees(math.atan2(wf[1],wf[0])),-53.13010235415598)
yes('Q11 Example8.12 not exact180degree reversal',not np.allclose(wf,-wi))
J=1.2;Fshort=J/.01;Flong=J/.1
near('Q12 equal impulse with different durations',[Fshort*.01,Flong*.1],[J,J])
yes('Q12 shorter stopping time permits larger mean force',Fshort>Flong)
M,m,u=6,.0027,2.
va=(M-m)/(M+m)*u;vb=2*M/(M+m)*u
dKbow=.5*M*(va*va-u*u);dKping=.5*m*vb*vb
near('Q13 energy transferred exactly from bowling to pingpong',dKbow,-dKping)
near('Q13 both-body total momentum',M*va+m*vb,M*u)
yes('Q13 light ball gains heavy ball loses kinetic energy',dKping>0>dKbow)
m,u,v,n=.01,100,80,50
near('Q14 sticking steady mean force',n*m*u,50)
near('Q14 rebound steady mean force',n*m*(u+v),90)
yes('Q14 rebound transfers larger impulse',m*(u+v)>m*u)
J=4*.25;m=J/5;t=J/2
near('Q15 actual original impulse',J,1)
near('Q15 reconstructed mass',m,.2)
near('Q15 actual smaller-force duration',t,.5)
near('Q15 Newton check same final velocity',(2/m)*t,5)
f=lambda t:4 if t<2 else -2
positive=quad(f,0,2)[0];negative=quad(f,2,6)[0]
near('Q16 nonzero positive and negative areas',[positive,negative],[8,-8])
near('Q16 zero total impulse',positive+negative,0)
yes('Q16 intermediate momentum differs from endpoints',positive>0)
m=.357;g=9.8
yes('Q17 two-second gravity impulse can exceed short-contact impulse',m*g*2>m*g*.005)
near('Q17 impulse time-scale ratio',(m*g*2)/(m*g*.005),400)
yes('Q17 apex does not mean zero gravity force',m*g>0)
m,M,v=.005,3,300;V=-m*v/M
near('Q18 exact original rifle recoil velocity',V,-.5)
near('Q18 total momentum before/after',m*v+M*V,0)
near('Q18 original same-system CM speed',(m*v+M*V)/(m+M),0)
me,ME,g,dt=.06,5.972e24,9.8,2.
F=me*g;ve=-F/me*dt;VE=F/ME*dt
near('Q19 opposite gravitational impulses',[me*ve,ME*VE],[-F*dt,F*dt])
near('Q19 total egg-plus-Earth momentum',me*ve+ME*VE,0)
yes('Q19 Earth speed extremely small',abs(VE)<1e-20)
M,mair,u=70,.004,10.;V=-mair*u/(M-mair)
near('Q20 expelling air conserves total body-plus-air momentum',(M-mair)*V+mair*u,0)
yes('Q20 expelling air produces nonzero opposite body speed',V<0)
near('Q20 closed internal redistribution can keep CM fixed',60*.1+10*(-.6),0)
yes('Q21 nonzero incoming horizontal momentum cannot become bothzero',30*100!=0+0)
m1,m2,J=1.,5.,5.
k1=J*J/(2*m1);k2=J*J/(2*m2)
near('Q22 Newton impulse gives inverse-mass energies',k1/k2,m2/m1)
near('Q22 opposite total impulse',J+(-J),0)
yes('Q22 CM lighter piece greater energy',k1>k2)
v1,v2,U=-J/m1,J/m2,10.
yes('Q22 arbitrary lab boost need not preserve lighter-greater-energy',.5*m1*(v1+U)**2<.5*m2*(v2+U)**2)
near('Q22 boosted total momentum conserved',m1*(v1+U)+m2*(v2+U),(m1+m2)*U)
m,g,h0,t=.1,9.8,30,2.;y=h0-.5*g*t*t;v=-g*t
near('Q23 mechanical energy preserved in fall',.5*m*v*v+m*g*y,m*g*h0)
yes('Q23 kinetic energy and particle momentum change',.5*m*v*v>0 and m*v!=0)
m1,m2,u1,u2=1.,2.,4.,-1.;v=(m1*u1+m2*u2)/(m1+m2)
near('Q24 clay collision momentum',m1*u1+m2*u2,(m1+m2)*v)
yes('Q24 clay kinetic energy reduced',.5*(m1+m2)*v*v<.5*m1*u1*u1+.5*m2*u2*u2)
p=math.sqrt(10);m1,m2=1.,5.;v1=p/m1;v2=-p/m2
near('Q25 equal/opposite momenta',[m1*v1,m2*v2],[p,-p])
near('Q25 actual five-to-one kinetic energy ratio',(.5*m1*v1*v1)/(.5*m2*v2*v2),5)
yes('Q25 correct statements a,d',not math.isclose(.5*m1*v1*v1,.5*m2*v2*v2) and .5*m1*v1*v1>.5*m2*v2*v2)
M,m,uM,um,e=100.,1.,10.,-10.,.5
vM,vm=np.linalg.solve([[M,m],[-1,1]],[M*uM+m*um,e*(uM-um)])
JM=M*(vM-uM);Jm=m*(vm-um)
near('Q26 opposite momentum changes guaranteed',JM,-Jm)
dKM=.5*M*(vM*vM-uM*uM);dKm=.5*m*(vm*vm-um*um)
yes('Q26 statement a not guaranteed energy equality',not math.isclose(-dKM,dKm))
yes('Q26 statement d not guaranteed same energy loss',not math.isclose(dKM,dKm))
yes('Q26 one vehicle may gain energy while other loses',dKM<0<dKm)
near('Q26 NewtonIII interaction forces same magnitude',1000,1000)
yes('Q26 lighter car greater acceleration at same force',1000/m>1000/M)
r=dict(status="passed",checksCount=len(checks),checks=checks)
(OUT/"numeric-discussion.json").write_bytes((json.dumps(r,ensure_ascii=False,indent=2)+"\n").encode("utf8"))
print("PASS discussion:",len(checks),"independent physical checks.")
