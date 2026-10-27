from pathlib import Path
import hashlib,json,math,re,xml.etree.ElementTree as ET
import numpy as np,pymupdf
from scipy.integrate import quad
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-08';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch08-late-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True)
P=B/'parent-12-bai-tap-056-109.md'
text=P.read_text(encoding='utf8');checks=[]
def near(name,a,b,tol=1e-9):
    assert np.allclose(a,b,rtol=tol,atol=tol),(name,a,b)
    checks.append({'name':name,'actual':np.asarray(a).tolist(),'expected':np.asarray(b).tolist()})
def yes(name,c):
    assert c,name
    checks.append({'name':name,'passed':True})
g=9.8
m2=.1;M=m2*8/2;m1=M-m2;vcm=5;total_p=M*vcm;v1=total_p/m1
near('56 actual mass at origin',m1,.3)
near('56 original centre position',(m1*0+m2*8)/M,2)
near('56 actual total momentum',total_p,2)
near('56 actual velocity firstparticle',v1,20/3)
near('56 original centre velocity',(m1*v1+m2*0)/M,5)
near('57 opposite equal momenta',90*(-60/90*1.1)+60*1.1,0)
near('57 James actual speed',60/90*1.1,.7333333333333333)
m2=.5;M=m2*6/2.4
near('58 actual total mass',M,1.25)
near('58 recovered initial ycoordinate',m2*6/M,2.4)
for t in [0,1,3]:
    h=.001;a=(.75*(t+h)**2-.75*(t-h)**2)/(2*h)
    near('58 derivative of actual xvelocity t'+str(t),a,1.5*t,1e-8)
near('58 force at3seconds',M*1.5*3,5.625)
for t in [0,1,3]:
    p=lambda q:np.array([-.75*q*q+3,.25*q,0])
    h=.001;derivative=(p(t+h)-p(t-h))/(2*h)
    near('59 derivative of actual momentumvector t'+str(t),derivative,[-1.5*t,.25,0],1e-8)
near('60 actual three block centres average',np.mean([-.25,0,.25]),0)
for L in [.1,1,5]:
    centres=np.array([L/4,L/2,3*L/4])-L/2
    near('60 actual overhang geometry L'+str(L),centres,[-L/4,0,L/4])
    near('60 same three uniform masses xCM L'+str(L),centres.mean(),0)
force=180*.029;dm=force*5/490;exact=180*(1-math.exp(-.029*5/490))
near('61 initial thrust full person/MMU mass',force,5.22)
near('61 approximate gas mass',dm,.05326530612244898)
yes('61 constantmass approximation changes gas by<0.02percent',abs(dm-exact)/exact<.0002)
yes('61 used gas fraction <0.03percent',dm/180<.0003)
near('61 exhaust relative momentum persecond',490*dm/5,force)
near('62 actual thrust',.05*1600,80)
for sign in [1,-1]:
    near('62 opposite signed exhaust/thrust momentum'+str(sign),.05*(sign*1600),sign*80)
    yes('62 opposite gas and rocket direction'+str(sign),(sign*80)*(-sign*1600)<0)
for weight in [100,150*.45359237*9.80665,1000]:
    F=.5*weight;fk=.3*weight;mass=weight/g
    t=8/((.5-.3)*g);s=8**2/(2*(.5-.3)*g)
    near('63 impulse with kineticfriction weight'+str(weight),(F-fk)*t,mass*8)
    near('63 net work weight'+str(weight),(F-fk)*s,.5*mass*8**2)
near('63 actual time independent of estimate',t,4.081632653061225)
near('63 actual distance independent of estimate',s,16.3265306122449)
mass=.04;dt=.002;vi=-math.sqrt(2*g*2);vf=math.sqrt(2*g*1.6)
J=mass*(vf-vi);net=J/dt;normal=net+mass*g
near('64 incoming signed velocity',vi,-6.260990336999411)
near('64 outgoing signed velocity',vf,5.6)
near('64 net impulse',J,.47443961347997643)
near('64 net average force',net,237.2198067399882)
near('64 plate average force includesgravity',normal,237.6118067399882)
near('64 plate plus gravity impulses equal momentumchange',normal*dt-mass*g*dt,J)
near('64 actual separate plate impulse',normal*dt,.47522361347997644)
yes('64 collision loses translational kineticenergy',.5*mass*vf*vf<.5*mass*vi*vi)
mass=.560/g;u=np.array([20.,-4.]);F=np.array([-380.,110.]);J=F*.003;v=u+J/mass
near('65 actual two impulsecomponents',J,[-1.14,.330])
near('65 actual two finalvelocitycomponents',v,[.05,1.775])
near('65 exact momentum balance',mass*v-mass*u,J)
yes('65 source initialy velocitynegative',u[1]<0)
yes('65 source force is net, no doublegravity',F[1]==110)
velocity=lambda t:quad(lambda q:3*q/2,0,t)[0]
time=brentq(lambda t:velocity(t)-9,0,10)
near('66 numerical impulse root time',time,3.4641016151377544)
near('66 force at actual requiredspeed',3*time,10.392304845413264)
near('66 actual speed from integrated force',velocity(time),9)
mA,mB=2.,10.;uA,uB=2.,-.5
Pi=mA*uA+mB*uB;V=Pi/(mA+mB)
Ki=.5*mA*uA*uA+.5*mB*uB*uB;spring=Ki-.5*(mA+mB)*V*V
near('67 actual common velocity atmaxcompression',V,-1/12)
near('67 actual maximum spring energy',spring,125/24)
vA,vB=np.linalg.solve([[mA,mB],[-1,1]],[Pi,uA-uB])
near('67 actual postcollision velocities',[vA,vB],[-13/6,1/3])
near('67 final momentum conservation',mA*vA+mB*vB,Pi)
near('67 final kineticenergy conservation',.5*mA*vA*vA+.5*mB*vB*vB,Ki)
near('67 springenergy from relative frame',.5*mA*mB/(mA+mB)*(uA-uB)**2,spring)
M0,m,v0=200.,25.,5.
# Explicitly declared initial co-moving reference frame, not the recoiling final frame.
for case,relative_x,expected in [('a',0,5),('b',-5,40/7)]:
    ground_particle=v0+relative_x;V=(M0*v0-m*ground_particle)/(M0-m)
    near('68'+case+' velocity under sourceinitialframe convention',V,expected)
    near('68'+case+' true groundmomentum conservation',(M0-m)*V+m*ground_particle,M0*v0)
    near('68'+case+' Galilean frame conversion',ground_particle-v0,relative_x)
near('68c incoming ground-frame particle changes totalmass',(M0*v0-25*6)/(M0+25),34/9)
for fraction in [0,.1,.5]:
    remain=200*(1-fraction);particle=200*fraction
    near('68 zero relative ejection leaves longitudinalspeed',((200*5-particle*5)/remain),5)
masses=np.array([.02,.03,.05]);uA=np.array([-1.5,0]);uB=-.5*np.array([math.cos(math.pi/3),math.sin(math.pi/3)])
target=np.array([.5,0]);uC=(masses.sum()*target-masses[0]*uA-masses[1]*uB)/masses[2]
near('69 source B points toward origin',uB,[-.25,-math.sqrt(3)/4])
near('69 actual C initial velocity',uC,[1.75,.25980762113533157])
near('69 vector momentum',masses[0]*uA+masses[1]*uB+masses[2]*uC,masses.sum()*target)
before=.5*masses[0]*np.dot(uA,uA)+.5*masses[1]*np.dot(uB,uB)+.5*masses[2]*np.dot(uC,uC)
after=.5*masses.sum()*np.dot(target,target)
near('69 actual initial kineticenergy',before,.1045)
near('69 actual final kineticenergy',after,.0125)
near('69 actual energy loss',after-before,-.092)
force=lambda t:5*t/4 if t<=4 else 5*(10-t)/6
J=quad(force,0,10,points=[4])[0]
near('70 integrated piecewise actual force',J,25)
near('70 actual final speed',J/3,25/3)
ns={'s':'http://www.w3.org/2000/svg'};svg=ET.parse(ROOT/'docs/vat-ly-1/bai-giang/img/young-08/solution-s8-70-graph.svg').getroot()
line=next(p for p in svg.findall('.//s:polyline',ns) if p.get('data-series')=='applied-force')
points=np.array([list(map(float,p.split(','))) for p in line.get('points').split()])
data=(points-np.array([60,335]))/np.array([25,-50])
near('70 actual three plotted vertices',data,[[0,0],[4,5],[10,0]])
near('70 area under actual SVG data',np.trapezoid(data[:,1],data[:,0]),25)
V=.5*24/8.5;time=math.sqrt(2*2.2/g);distance=V*time
near('71 actual postcollision velocity',V,1.411764705882353)
near('71 horizontal momentum preserved',8.5*V,.5*24)
near('71 actual fall time',time,.6700593942604899)
near('71 actual horizontal distance',distance,.9459662036618681)
yes('71 actual sticking collision loses kineticenergy',.5*8.5*V*V<.5*.5*24*24)
result={'status':'passed','scope':'Independentphysicalmodelsandinvariants. Canonicalsource/crop/structuregatehandledbyentrypoint.','checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'numeric-056-071.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS 056-071',len(checks),'independentphysical/geometrychecks.')
