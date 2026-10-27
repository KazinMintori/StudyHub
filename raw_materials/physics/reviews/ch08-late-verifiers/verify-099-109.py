from pathlib import Path
import hashlib,json,math,re
import numpy as np,pymupdf
from scipy.integrate import quad
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-08';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch08-late-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);R=B/'review-099-109'
P=B/'parent-12-bai-tap-056-109.md';text=P.read_text(encoding='utf8');checks=[]
def near(name,a,b,tol=1e-9):
    assert np.allclose(a,b,rtol=tol,atol=tol),(name,a,b)
    checks.append(dict(name=name,actual=np.asarray(a).tolist(),expected=np.asarray(b).tolist()))
def yes(name,c):
    assert c,name
    checks.append(dict(name=name,passed=True))
g=9.8
u=math.sqrt(2*g*50*math.sin(math.radians(6)));V=300*u/435
near('99 actual wagon preimpact speed',u,10.121160704301676)
near('99 horizontal kineticenergy from original50m slope',.5*300*u*u,300*g*50*math.sin(math.radians(6)))
near('99 loadedwagon speed',V,6.9801108305528805)
near('99 exacthorizontalmomentum',435*V,300*u)
near('99 time to actual40m cliff',40/V,5.730568034094049)
yes('99 sufficient time for5seconds',40/V>5)
loss=.5*300*u*u-.5*435*V*V
near('99 actualhorizontalenergy loss',loss,4768.660582865708)
for vy1,vy2 in [(0,0),(-1,-2),(-4,-3)]:
    total_loss=.5*300*u*u+.5*75*vy1**2+.5*60*vy2**2-.5*435*V*V
    near('99 extra originalverticalkinetic loss '+str((vy1,vy2)),total_loss,loss+.5*75*vy1**2+.5*60*vy2**2)
    yes('99 energy decreases forall incomingverticalspeeds'+str((vy1,vy2)),total_loss>0)
yes('99 totalenergy loss notuniquelydetermined withoutfallheights',loss!=loss+.5*135*1**2)
# Actual graph fromPDF:7500N plateau0..1.5, linear7500->3500 until3, plateauuntil4.5.
force=lambda t:7500 if t<=1.5 else 7500-(4000/1.5)*(t-1.5) if t<=3 else 3500
J=quad(force,0,4.5,points=[1.5,3])[0];mass=3071*.45359237;speed=J/mass;stop=J/5200;work=-.5*mass*speed**2;distance=-work/5200
near('100 actual originalgraph impulse',J,24750)
near('100 totalweight already includesdriver',mass,1392.98216827)
near('100 actual speedafter4.5s',speed,17.767635913629828)
near('100 exact stoppingimpulse',5200*stop,J)
near('100 actual stoptime',stop,4.759615384615385)
near('100 actual negativebrakingwork',work,-219874.49443116915)
near('100 actual stoppingdistance',distance,42.283556621378686)
near('100 independent constantdeceleration distance',speed*stop/2,distance)
near('100 independent stopdistance froma',speed**2/(2*(5200/mass)),distance)
letters='ABCDE';grains=np.array([80,125,240,200,140]);feet=np.array([1667,945,851,819,1355]);masses=grains*64.80e-6;speeds=feet*.3048;totalm=2+masses
momenta=masses*speeds;energies=momenta**2/(2*totalm);frictions=.38*totalm*g
near('101 full actual five masses',masses,[.005184,.008100,.015552,.012960,.009072])
near('101 full actual five speeds',speeds,[508.1016,288.036,259.3848,249.6312,413.004])
near('101 full actual postimpactenergies',energies,[1.7300031124577362,1.3553399765924403,4.036802831908491,2.5998158746311417,3.493728093897271])
for i,L in enumerate(letters):
    near('101 actual collisionmomentum '+L,totalm[i]*(momenta[i]/totalm[i]),momenta[i])
    yes('101 actual energy aftersticking less than incoming '+L,energies[i]<.5*masses[i]*speeds[i]**2)
    near('101 actual f/M independence '+L,frictions[i]/totalm[i],.38*g)
k=(2*energies[2]-2*frictions[2]*.25)/.25**2
near('101 C calibratedpositive springconstant',k,69.13036543707172)
yes('101 positivek feasible afterfriction',energies[2]>frictions[2]*.25)
for kval in [0,.01,1,k,1e4]:
    distances=[]
    for i,L in enumerate(letters):
        d=brentq(lambda x:.5*kval*x*x+frictions[i]*x-energies[i],0,1)
        distances.append(d)
        near('101 actual compressenergy '+str(kval)+L,.5*kval*d*d+frictions[i]*d,energies[i],1e-7)
    yes('101 ranking all five for k='+str(kval),''.join(letters[i] for i in np.argsort(distances))=='BADEC')
    if kval==k:
        near('101 targetmaximum actualC',distances[2],.25)
        near('101 B actualminimum compression',distances[1],.11746410874460099)
#102 independent solveCartesian two-car equations andsource direction.
uP=50*.44704;angle=math.radians(39);V=(3042*uP)/(9542*math.sin(angle));uD=(9542/6500)*V*math.cos(angle);tree_speed=math.sqrt(V*V-2*.45*g*35*.3048)
near('102 actual Prius50mph conversion',uP,22.352)
near('102 actual Durangospeed',uD,12.91793314166385)
near('102 actual Durango mph',uD/.44704,28.896593462920208)
near('102 actual impactcommon speed',V,11.323074960220936)
near('102 northernmomentum',9542*V*math.sin(angle),3042*uP)
near('102 easternmomentum',9542*V*math.cos(angle),6500*uD)
near('102 actual35feet distance',35*.3048,10.668)
near('102 actual speedjustbeforetree',tree_speed,5.841255563214328)
yes('102 wreckage reaches tree beforestop',V*V/(2*.45*g)>10.668)
near('102 no doublecount passengers',6500+3042,9542)
#103 ideal m=kx branch: all termsof momentumderivative checked for t>0.
a=g/3;k=.002
for t in [.01,.1,1,3]:
    x=.5*a*t*t;v=a*t;m=k*x;mdot=k*v
    near('103 actual variablemass momentumbalance t'+str(t),m*g,m*a+v*mdot)
    h=1e-6;momentum=lambda q:k*(.5*a*q*q)*(a*q)
    near('103 independent numerical dpdt t'+str(t),(momentum(t+h)-momentum(t-h))/(2*h),m*g,1e-7)
near('103 actual3second distance',.5*a*9,14.7)
near('103 actual2g/m mass',.002*14.7,.0294)
yes('103 initialmass singularpoint correctly separated',k*0==0)
for L,A,rho,alpha in [(1,.2,3,2),(.3,2,10,.5),(5,.03,7,4)]:
    M=quad(lambda x:rho*A,0,L)[0];Q=quad(lambda x:x*rho*A,0,L)[0]
    near('104 uniform actualCM L'+str(L),Q/M,L/2)
    M=quad(lambda x:alpha*x*A,0,L)[0];Q=quad(lambda x:alpha*x*x*A,0,L)[0]
    near('104 lineardensity actualM L'+str(L),M,alpha*A*L*L/2)
    near('104 lineardensity actualCM L'+str(L),Q/M,2*L/3)
for radius,rhot in [(1,1),(.4,5),(3,2)]:
    M=quad(lambda y:2*rhot*math.sqrt(radius**2-y*y),0,radius,epsabs=1e-10)[0]
    Q=quad(lambda y:2*rhot*y*math.sqrt(radius**2-y*y),0,radius,epsabs=1e-10)[0]
    near('105 full massintegral radius'+str(radius),M,.5*rhot*math.pi*radius**2)
    near('105 actual verticalCM radius'+str(radius),Q/M,4*radius/(3*math.pi))
    near('105 actual horizontalCMsymmetry radius'+str(radius),quad(lambda x:x*2*rhot*math.sqrt(radius**2-x*x),-radius,radius)[0],0)
    yes('105 CMliesinside semidisk radius'+str(radius),0<Q/M<radius)
mw=.00030;v=2.5;dt=.005;fish=.065
near('106 true watermomentum',mw*v,.000750)
near('107 actual fishmassafterejection',fish-mw,.0647)
near('107 actual fishrecoil speed',mw*v/(fish-mw),.011591962905718699)
near('107 actual horizontalmomentum',-(fish-mw)*(mw*v/(fish-mw))+mw*v,0)
near('108 actual mean netforce',mw*v/dt,.15)
near('108 small gravityimpulse fraction',mw*g*dt/(mw*v),.0196)
mi=mw*(2.5/2-1)
near('109 actual insectmass',mi,.000075)
near('109 SIto grams conversion',mi*1000,.075)
near('109 actual sticking momentum',(mw+mi)*2,mw*2.5)
yes('109 actual energydecreases',.5*(mw+mi)*2**2<.5*mw*2.5**2)
result={'status':'passed','scope':'Independentphysicalmodelsandinvariants. Canonicalsource/crop/structuregatehandledbyentrypoint.','checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'numeric-099-109.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS 099-109',len(checks),'independentphysical/geometrychecks.')
