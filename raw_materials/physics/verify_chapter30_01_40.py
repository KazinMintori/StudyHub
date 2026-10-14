"""Recalculate the source data of inductance exercises30.1–30.40."""
from pathlib import Path
import math,json
mu0=4*math.pi*1e-7
eps0=8.8541878128e-12
results={}
def put(n,**values):results[str(n)]=values
put(1,emf=3.25e-4*830)
M=1.65e-3/.242
put(2,M=M,flux=M*1.20/25,emf1=M*.360)
M=400*.0320/6.52
put(3,M=M,flux1=M*2.54/700)
A=math.pi*.01**2;B=mu0*300*.120/.250;M=mu0*300*25*A/.250
put(4,flux=B*A,M=M,emf=M*1750)
put(5,turns=math.sqrt(.00250*2*math.pi*.060/(mu0*2e-4)),rate=2/.00250)
L=mu0*500**2*6.25e-4/(2*math.pi*.04)
put(6,L=L,emf=L*1000)
put(7,L=.0160/.0640,flux=.0160/.0640*.720/400)
L=.0126/.0260
put(8,L=L,turns=L*1.40/.00285)
put(9,emf=.260*.0180,Vab=.260*.0180)
put(10,rate=-1.04/.260,current2=12-1.04/.260*2)
put(11,L=mu0*50**2*math.pi*(.00150/2)**2/.050)
L=800*.00325/2.90
put(12,L=L,rate=.00620/L)
L=.600/2000
put(13,L=L,B=L*3/(1200*25e-6))
put(14,U=.5*12*.5**2,power=.5**2*180)
L=2*.390/12**2
put(15,L=L,turns=math.sqrt(L*2*math.pi*.150/(mu0*5e-4)))
B=mu0*300*5/(2*math.pi*.12);L=mu0*300**2*4e-4/(2*math.pi*.12)
U=.5*L*25;volume=2*math.pi*.12*4e-4
assert math.isclose(B*B/(2*mu0),U/volume,rel_tol=1e-12)
put(16,B=B,L=L,U=U,density=B*B/(2*mu0),volume=volume)
B=mu0*400*80/.250;L=mu0*400**2*5e-5/.250
put(17,B=B,density=B*B/(2*mu0),U=.5*L*80**2,L=L)
put(18,U=150*86400,L=2*150*86400/80**2)
put(19,U=4.80**2/(2*mu0)*10e-6)
c=1/math.sqrt(mu0*eps0)
put(20,ratio=c,B=500/c)
put(21,rateInitial=6/2.50,rateAtHalfAmp=(6-8*.5)/2.50,current025=6/8*(1-math.exp(-8*.250/2.50)),finalCurrent=6/8)
tau=-.002/math.log(.280/(6.30/15))
put(22,L=tau*15,time1percent=tau*math.log(100))
tau=.00125/50
put(23,halfCurrentTime=tau*math.log(2),halfEnergyTime=-tau*math.log(1-1/math.sqrt(2)))
R=240/15;L=(240-R*5)/20
put(24,R=R,L=L,T=-L/R*math.log(1-5/15))
I=math.sqrt(2*.400/.600)
put(25,I=I,VL=50-30*I)
put(26,halfTime=12/36*math.log(2))
I=.25*math.exp(-240*.000400/.160)
put(27,initialCurrent=.25,current=I,Vbc=-240*I,halfTime=.160/240*math.log(2))
put(28,VabInitial=0,VbcInitial=60,VabFinal=60,VbcFinal=0,VabAt015=240*.150,VbcAt015=60-240*.150)
put(29,Vab=18-.380*7.20)
put(30,initialPower=0,U=.5*2.50*(6/8)**2,power=6**2/8)
put(31,PLinitial=0,PLfinal=0,PLatHalfNormalized=.25)
C=15e-6;L=.280e-3;omega=1/math.sqrt(L*C);U=.5*C*150**2
put(32,frequency=omega/(2*math.pi),U=U,ULat013=U*math.sin(omega*.00130)**2)
put(33,Qmax=.000850*math.sqrt(.085*3.20e-6),chargeAt05=math.sqrt(.085*3.20e-6*(.000850**2-.000500**2)))
C=7.50e-9;T=8.60e-5;L=(T/(2*math.pi))**2/C;Q=C*12
put(34,L=L,Qmax=Q,U=.5*C*12**2,Imax=2*math.pi/T*Q)
C=6e-5;L=1.50;omega=1/math.sqrt(L*C);Q=C*12;t=.0230
q=Q*math.cos(omega*t);i=-omega*Q*math.sin(omega*t);UE=q*q/(2*C);UB=.5*L*i*i
assert math.isclose(UE+UB,.5*C*12**2,rel_tol=1e-12)
put(35,omega=omega,period=2*math.pi/omega,Q0=Q,U0=.5*C*12**2,q=q,i=i,UE=UE,UB=UB)
L=1/(4.18e-12*(2*math.pi*1600e3)**2)
put(36,L=L,Cmax=1/(L*(2*math.pi*540e3)**2))
L=.080;C=1.25e-9;omega=1/math.sqrt(L*C)
put(37,Qmax=.750/omega,frequency=omega/(2*math.pi),UL=.5*L*.750**2*math.sin(omega*.00250)**2)
L=.022;C=15e-9;R=75;alpha=R/(2*L);omega=math.sqrt(1/(L*C)-alpha**2)
put(38,frequency=omega/(2*math.pi),decayTime=math.log(10)/alpha,Rcritical=2*math.sqrt(L/C))
L=.450;C=2.50e-5
put(39,omega0=1/math.sqrt(L*C),R=2*math.sqrt(L/C*(1-.95**2)))
L=.400;C=7e-6;R=320;Q0=2.80e-4;alpha=R/(2*L);omega=math.sqrt(1/(L*C)-alpha**2)
phase=-math.atan(alpha/omega);amplitude=Q0/math.cos(phase);T=2*math.pi/omega
assert math.isclose(amplitude*math.cos(phase),Q0,rel_tol=1e-12)
assert abs(-amplitude*(alpha*math.cos(phase)+omega*math.sin(phase)))<1e-14
put(40,alpha=alpha,omega=omega,amplitude=amplitude,phase=phase,period=T,chargeAfterPeriod=Q0*math.exp(-alpha*T))
assert len(results)==40
out=Path(__file__).resolve().parents[2]/'qa/physics/chapter30'
out.mkdir(parents=True,exist_ok=True)
(out/'exercises-01-40-checks.json').write_text(json.dumps({'status':'data-recalculated','results':results},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(results,ensure_ascii=False,indent=2))
