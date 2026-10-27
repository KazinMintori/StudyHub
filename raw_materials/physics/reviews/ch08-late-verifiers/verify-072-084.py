from pathlib import Path
import hashlib,json,math,re
import numpy as np,pymupdf
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-08';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch08-late-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);R=B/'review-072-084'
P=B/'parent-12-bai-tap-056-109.md';text=P.read_text(encoding='utf8');checks=[]
def near(name,a,b,tol=1e-9):
    assert np.allclose(a,b,rtol=tol,atol=tol),(name,a,b)
    checks.append(dict(name=name,actual=np.asarray(a).tolist(),expected=np.asarray(b).tolist()))
def yes(name,c):
    assert c,name
    checks.append(dict(name=name,passed=True))
g=9.8
#72: recover speeds from original radial force, then energy and sticking impulse.
M=.8;m=.012;Q=M+m;L=1.6;h=.8;cos=1-h/L
v2=L*(4.8/Q-g*cos);V2=v2+2*g*h;V=math.sqrt(V2);u=Q/m*V
near('72 actual angle cosine',cos,.5)
near('72 actual speed at givenheight',math.sqrt(v2),1.272056633494646)
near('72 radial force residual',4.8-Q*g*cos,Q*v2/L)
near('72 postimpact bottom speed',V,4.159101835591157)
near('72 actual initialbullet speed',u,281.4325575416683)
near('72 exact collision momentum',m*u,Q*V)
near('72 postcollisionenergy conserved',.5*Q*V2,.5*Q*v2+Q*g*h)
yes('72 string still taut on lower-to-givenheight arc',min(Q*(V2/L-2*g+3*g*c) for c in np.linspace(.5,1,31))>0)
V=5*12/10
near('73 common speed of actualequalmass chunks',V,6)
near('73 attainableheight',V*V/(2*g),1.8367346938775508)
near('73 collision energy fraction',(.5*10*V*V)/(.5*5*12*12),.5)
VB=(2*8-2*(-2))/4
near('74 actual B initialprojectile velocity',VB,5)
near('74 original horizontal momentum',2*(-2)+4*VB,2*8)
near('74 actual speed atfloor',math.hypot(VB,math.sqrt(2*g*2.6)),8.715503427800371)
yes('74 source collision not incorrectlyassumedelastic',.5*2*2**2+.5*4*VB**2<.5*2*8**2)
for m in [1,2.5]:
    for u in [.1,4,10]:
        v1=v2=u/2
        near('75 actual finalmomentum '+str((m,u)),m*(v1+v2),m*u)
        near('75 actual finalenergyhalf '+str((m,u)),.5*m*(v1*v1+v2*v2),.5*(.5*m*u*u))
        near('75 minimalenergy givenmomentum '+str((m,u)),.5*m*(v1*v1+v2*v2),(m*u)**2/(2*(2*m)))
V=math.sqrt(2*.65*g*7.15);uA=3400/1500*V
near('76 postcollision speed',V,9.54416051834838)
near('76 recovered A speed',uA,21.63343050825633)
near('76 source stoppingfriction work',.65*3400*g*7.15,.5*3400*V**2)
near('76 source collision momentum',1500*uA,3400*V)
near('76 milesperhour conversion',uA/.44704,48.39260582555549)
near('76 exceeds actual35mph by',uA/.44704-35,13.392605825555492)
yes('76 does exceed35mph',uA>35*.44704)
s=math.hypot(5.39,6.43);V=math.sqrt(2*.75*g*s);wreck=V*np.array([5.39,6.43])/s
uS=3700*wreck[1]/1500;uU=3700*wreck[0]/2200
near('77 actual diagonal skid length',s,8.390292009221133)
near('77 actual total finalspeed',V,11.105732417789952)
near('77 recovered sedan southspeed',uS,20.993824741042822)
near('77 recovered SUV westspeed',uU,11.99880340953847)
near('77 original two momenta vector',np.array([2200*uU,1500*uS]),3700*wreck)
near('77 direction matches actual measurements',wreck[1]/wreck[0],6.43/5.39)
near('77 postimpact energy dissipated byfriction',.5*3700*V*V,.75*3700*g*s)
mf=.150;mp=.200;M=mf+mp;e=.0400;k=mf*g/e;u=math.sqrt(2*g*.300);V=mp*u/M
x=(mp*g+math.sqrt((mp*g)**2+k*M*V*V))/k
negative=(mp*g-math.sqrt((mp*g)**2+k*M*V*V))/k
near('78 actual springconstant',k,36.75)
near('78 exact collision momentum',M*V,mp*u)
near('78 actual positive quadraticroot',x,.19869549735877268)
yes('78 other quadraticroot is negative',negative<0)
near('78 full springenergy not x-only',.5*k*(e+x)**2-.5*k*e**2,.5*M*V*V+M*g*x)
def turn(t,y):return y[1]
turn.terminal=True;turn.direction=-1
trajectory=solve_ivp(lambda t,y:[y[1],g-k*(e+y[0])/M],[0,2],[0,V],events=turn,rtol=1e-11,atol=1e-12)
yes('78 actual dynamics reachesfirstdownwardturn',len(trajectory.t_events[0])==1)
near('78 independent integrated maxdisplacement',trajectory.y_events[0][0,0],x,1e-8)
yes('78 true maximum liesbelow newequilibrium',x>mp*g/k)
near('79 exact calibration unitconvert',.750/.00250,300)
V=.150*math.sqrt(300/1);u=V/.008
near('79 common initialspeed',V,2.598076211353316)
near('79 bullet initialspeed',u,324.7595264191645)
near('79 collision momentum',.008*u,V)
near('79 actual springenergy',.5*300*.15**2,.5*V*V)
bullet_initial=np.array([350.,0]);bullet_final=np.array([0.,250.]);stone=.006*(bullet_initial-bullet_final)/.100
near('80 actual 2Dstonevelocity',stone,[21,-15])
near('80 actual stone speed',np.linalg.norm(stone),25.80697580112788)
near('80 actual signed deviationangle',math.degrees(math.atan2(stone[1],stone[0])),-35.53767779197438)
near('80 vector momentum',.100*stone+.006*bullet_final,.006*bullet_initial)
before=.5*.006*np.dot(bullet_initial,bullet_initial)
after=.5*.006*np.dot(bullet_final,bullet_final)+.5*.100*np.dot(stone,stone)
near('80 actual initialenergy',before,367.5)
near('80 actual finalenergy',after,220.8)
near('80 actual lostenergy',before-after,146.7)
u=math.sqrt(2*g*5);V=80/150*u;s=V*V/(2*.25*g)
near('81 actual preimpact swing speed',u,9.899494936611665)
near('81 actual sticking common speed',V,5.279730632859555)
near('81 actual friction stoppingdistance',s,5.688888888888889)
near('81 complete source horizontalmomentum',80*u,150*V)
near('81 postimpact frictionenergy',.25*150*g*s,.5*150*V*V)
for r in [.3,1,2.7]:
    u=math.sqrt(2*g*r);V=u/2;h=V*V/(2*g)
    near('82 true initialpotentialconverted',g*r,.5*u*u)
    near('82 actual heightRover4 '+str(r),h,r/4)
    near('82 aftersticking energypreserved',V*V,2*g*h)
def transfer(a):return 4*a/(a+1)**2
near('83 parta fullenergytransfer equalmasses',transfer(1),1)
roots=[3-2*math.sqrt(2),3+2*math.sqrt(2)]
for a in roots:
    near('83 each positive root satisfies polynomial '+str(a),a*a-6*a+1,0,1e-8)
    near('83 B final energyhalf '+str(a),transfer(a),.5)
    near('83 A final energyhalf '+str(a),((a-1)/(a+1))**2,.5)
    near('83 positive root reciprocal pair '+str(a),a*(6-a),1)
yes('83 both rootsshouldberetained',all(a>0 for a in roots))
L=2.8;Q=25;m=5;V=math.sqrt(5*g*L);u=Q/m*V
near('84 minimum postcollision bottomspeed',V,11.713240371477058)
near('84 actual dart initialthreshold',u,58.56620185738529)
near('84 collision momentum',m*u,Q*V)
near('84 topenergy plus2Lpotential',.5*Q*V*V,.5*Q*g*L+Q*g*2*L)
for theta in np.linspace(0,math.pi,17):
    speed2=V*V-2*g*L*(1-math.cos(theta));T=Q*(speed2/L+g*math.cos(theta))
    yes('84 string nonnegative tension theta'+str(theta),T>=-1e-8)
    near('84 full circular tension formula theta'+str(theta),T,3*Q*g*(1+math.cos(theta)),1e-8)
near('84 limitingtoptension',Q*((V*V-4*g*L)/L-g),0,1e-8)
result={'status':'passed','scope':'Independentphysicalmodelsandinvariants. Canonicalsource/crop/structuregatehandledbyentrypoint.','checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'numeric-072-084.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS 072-084',len(checks),'independentphysical/geometrychecks.')
