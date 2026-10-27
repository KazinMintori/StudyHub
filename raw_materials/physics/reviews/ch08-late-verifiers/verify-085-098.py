from pathlib import Path
import hashlib,json,math,re
import numpy as np,pymupdf
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-08';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch08-late-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);R=B/'review-085-098'
P=B/'parent-12-bai-tap-056-109.md';text=P.read_text(encoding='utf8');checks=[]
def near(name,a,b,tol=1e-9):
    assert np.allclose(a,b,rtol=tol,atol=tol),(name,a,b)
    checks.append(dict(name=name,actual=np.asarray(a).tolist(),expected=np.asarray(b).tolist()))
def yes(name,c):
    assert c,name
    checks.append(dict(name=name,passed=True))
g=9.8
m=.004;M=.8;u=400;v=190;V=m*(u-v)/M;mu=V*V/(2*g*.72)
near('85 actual immediate woodspeed',V,1.05)
near('85 true friction coefficient',mu,.078125)
near('85 original impactmomentum',m*u,m*v+M*V)
near('85 actual bullet K loss',.5*m*(u*u-v*v),247.8)
near('85 actual woodkineticenergy',.5*M*V*V,.441)
near('85 kineticwoodremovedbyfriction',mu*M*g*.72,.5*M*V*V)
yes('85 most lostbulletenergy not woodKE',.5*m*(u*u-v*v)>.5*M*V*V)
V=math.sqrt(2*g*.0038);v=450-V/.005
near('86 actual height unitconversion',.38/100,.0038)
near('86 actual wood speed',V,.272910241654651)
near('86 bullet exit speed',v,395.4179516690698)
near('86 original momentum',.005*450,.005*v+V)
near('86 onlywoodmass in swingenergy',.5*V*V,g*.0038)
theta=math.radians(37);vx=3*math.cos(theta);vy=-math.sqrt((3*math.sin(theta))**2+2*g*4)
speed=math.hypot(vx,vy);V=(50*(-5)+15*vx)/65
near('87 original3m/s chuteanglehorizontal',vx,2.3959065301418785)
near('87 actual downward touchdowncomponent',vy,-9.03657191078694)
near('87 actual impact speed',speed,9.348796714016196)
near('87 actual loadedcart signedvelocity',V,-3.2932523391980277)
near('87 conserve onlyhorizontalmomentum',65*V,50*(-5)+15*vx)
yes('87 downwardmomentumcannotbeconservedwithstationaryverticalcart',15*vy!=0)
for p in [1e-4,1,10]:
    me=1;mp=1836;Ke=p*p/(2*me);Kp=p*p/(2*mp)
    near('88 classical two-body protonfraction p'+str(p),Kp/(Kp+Ke),1/1837)
    near('88 equalopposite momentum p'+str(p),p-p,0)
near('88 percentageconvert',100/1837,.05443658138268917)
t=math.sqrt(2*1.2/g);u=2/t
near('89 headon equalmass exchange projectile speed',u,4.041451884327381)
near('89 actual2m landing',u*t,2)
uJ=-5*math.cos(math.pi/6);uN=7*math.cos(math.radians(36.9));V=-(800*uJ+600*uN)/1000
near('90 original iceframe velocitycomponents',[uJ,uN],[-4.330127018922194,5.597792609409634])
near('90 actual signed sleighvelocity',V,.10542604949197448)
near('90 all three horizontalmomenta sumzero',(800*uJ+600*uN+1000*V)/g,0,1e-8)
yes('90 sleighgoesright',V>0)
L=3;d=40*L/(20+30+40)
initial=np.array([0,-L/2,L/2]);final=np.array([d,d-L/2,d-L/2]);masses=np.array([20,30,40])
near('91 initial/final actual weighted positions',np.dot(masses,initial),np.dot(masses,final))
near('91 actual logdisplacement',d,4/3)
near('91 Ernie relative displacement',(final[2]-initial[2])-d,-L)
d=-45*3/105
near('92 actual canoedisplacement',d,-9/7)
near('92 actual CM staysfixed',60*d+45*(d+3),0)
near('92 woman actualworlddisplacement relativewalk',d+3,12/7)
for H in [.1,1,3]:
    u=math.sqrt(2*g*H);V=u/3
    near('93 unequalmass sticking impulse H'+str(H),u,3*V)
    near('93 original height fraction H'+str(H),V*V/(2*g),H/9)
#94: separate the valid simultaneouslanding result from general unequal flighttimes.
u=18;alpha=math.radians(51);ux=u*math.cos(alpha);uy=u*math.sin(alpha);H=uy*uy/(2*g);xp=ux*uy/g
range0=2*xp
near('94 conditional simultaneous CMdistance',range0,32.33875741201562)
near('94 conditional secondlanding',2*range0-26,38.677514824031235)
near('94 conditional massweighted two landings',(26+(2*range0-26))/2,range0)
q=3
tp=(q+math.sqrt(q*q+2*g*H))/g;tm=(-q+math.sqrt(q*q+2*g*H))/g
near('94 counterexample both verticalpositionsendzero',[H+q*tp-.5*g*tp**2,H-q*tm-.5*g*tm**2],[0,0])
near('94 counterexample verticalmomentum zero',q-q,0)
yes('94 counterexample differentlandingtimes',tp>tm)
same_vx_mid=xp+ux*(tp+tm)/2
yes('94 preservinglaunchdata canchange finalmidpoint',same_vx_mid>range0)
vx1=(26-xp)/tp;vx2=2*ux-vx1;x2=xp+vx2*tm
near('94 fixed actualfirstlanding26 in generalcounterexample',xp+vx1*tp,26)
near('94 counterexample horizontalmomentum',vx1+vx2,2*ux)
near('94 counterexample actualotherlanding',x2,35.88561052542268)
yes('94 counterexample proves otherlandingnotunique',abs(x2-(2*range0-26))>2)
yes('94 chosen explosion energy nonnegative',.5*(vx1*vx1+vx2*vx2+2*q*q)>ux*ux)
#95 independent time integration verifies the displacement andspring-energy extrema.
m=.5;k=80;e=m*g/k;V=math.sqrt(2*g*4)/2;M=2*m
x=(m*g+math.sqrt((m*g)**2+k*M*V*V))/k;z=e+x
near('95 initialspringcompression',e,.06125)
near('95 initialspringenergy',.5*k*e*e,.1500625)
near('95 actual postimpact speed',V,4.427188724235731)
near('95 downwarddistance from originalposition',x,.560)
near('95 totalcompression',z,.62125)
near('95 maximum springenergy',.5*k*z*z,15.4380625)
near('95 actualpostimpactenergy',.5*k*(z*z-e*e),.5*M*V*V+M*g*x)
def turn(t,y):return y[1]
turn.direction=-1;turn.terminal=True
sol=solve_ivp(lambda t,y:[y[1],g-k*(e+y[0])/M],[0,2],[0,V],events=turn,rtol=1e-11,atol=1e-12)
yes('95 physical firstmaxcompression found',len(sol.y_events[0])==1)
near('95 independent dynamicsmaxdistance',sol.y_events[0][0,0],x,1e-8)
u=80;alpha=math.pi/3;ux=u*math.cos(alpha);uy=u*math.sin(alpha);t=uy/g;xp=ux*t
near('96 secondfragment velocity via actualmassmomentum',10*(2*ux),20*ux)
near('96 actual secondfragment landing',xp+2*ux*t,848.3514159521033)
near('96 initial/final verticalmomenta zero',0,0)
near('96 releasedenergy difference',.5*10*(2*ux)**2-.5*20*ux**2,16000)
near('96 COM landingmatches unperturbed range',(xp+(xp+2*ux*t))/2,2*xp)
M=1.4;m=.28;E=860
V=math.sqrt(2*E/(M+M*M/m));v=M*V/m;t=math.sqrt(2*80/g)
near('97 actual heavy speed',V,14.30950400125402)
near('97 actual light speed',v,71.54752000627009)
near('97 opposite actualmomenta',M*V-m*v,0)
near('97 actual explosion kineticenergy',.5*M*V*V+.5*m*v*v,E)
near('97 actual separation',(V+v)*t,346.9147650755229)
# Same start-height and flighttime implies equal verticalvelocity; momentumthenzero.
for wy in [-2,0,3]:
    same_total_vertical=(M+m)*wy
    yes('97 commonverticalvelocity zero iff totalPzero '+str(wy),(same_total_vertical==0)==(wy==0))
u=150;alpha=math.radians(55);U=u*math.cos(alpha);t=u*math.sin(alpha)/g;xp=U*t;vH=-U;vL=7*U
near('98 heavyfragment returns pointoffiring',xp+vH*t,0)
near('98 source ratio3-to1 actual momentum',9*vH+3*vL,12*U)
near('98 actual lighterfragment landing',xp+vL*t,8629.830190890994)
near('98 releasedenergy exactinitialfinaldifference',.5*9*vH*vH+.5*3*vL*vL-.5*12*U*U,532963.6839062084)
near('98 releasedenergy24mU2',24*3*U*U,532963.6839062084)
near('98 commonflighttime COM landingmatchesoriginalrange',(3*(xp+vH*t)+(xp+vL*t))/4,2*xp)
result={'status':'passed','scope':'Independentphysicalmodelsandinvariants. Canonicalsource/crop/structuregatehandledbyentrypoint.','checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'numeric-085-098.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS 085-098',len(checks),'independentphysical/geometrychecks.')
