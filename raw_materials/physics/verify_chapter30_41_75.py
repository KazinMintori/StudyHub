"""Check the models and numerical data of inductance problems30.41–30.75."""
from pathlib import Path
import math,json
import numpy as np
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[2]
mu0=4*math.pi*1e-7
results={}
def put(n,**values):results[str(n)]=values
def bisect(function,left,right):
 assert function(left)*function(right)<=0
 for _ in range(100):
  middle=(left+right)/2
  if function(left)*function(middle)<=0:right=middle
  else:left=middle
 return (left+right)/2

N=49;diameter=.007;L=mu0*N*N*math.pi*(diameter/2)**2/.04
put(41,assumedPencilDiameter=diameter,turns=N,L=L,U=.5*L)
R=16/.00645;tau=-.000940/math.log(1-.00486/.00645)
put(42,R=R,L=R*tau)
L=mu0*math.pi*.030/2
put(43,L=L,maximumEmf=L*2*math.pi*60*1.20)
L=.00750;omega=math.pi/.0250;I0=.680
put(44,maximumEmf=L*omega*I0,fluxMaximum=L*I0/400,emfAt018=L*omega*I0*math.sin(omega*.018))
speed=.4/math.sqrt(mu0*3e-4)
put(45,speed=speed,escapeRatio=speed/6e5)
put(46,externalInductancePerLengthCoefficient=mu0/(2*math.pi))
L=2*10/2**2;length=L/(mu0*math.pi*.02**2*1e4**2)
put(47,L=L,length=length)
x=np.linspace(0,12,10001);exp=np.exp(-x)
PR=(1-exp)**2;PL=exp-exp**2;PE=1-exp
assert np.max(abs(PR+PL-PE))<1e-14
assert abs(x[np.argmax(PL)]-math.log(2))<.001
put(48,normalizedPeakTime=math.log(2),normalizedPLpeak=.25)
C=2*.016/12**2;L=1/(C*(2*math.pi*3500)**2)
put(49,C=C,L=L)
put(50,initial=[8,8,0],final=[14,8,6],halfTime=.300/16*math.log(2),atHalf=[11,8,3])
torque=500*1*math.pi*.05**2*2*math.sin(math.pi/4)
inertia=.5*1.11*.05**2
put(51,magneticTorque=torque,barForce=torque/.05,releaseTime=.077/5*math.log(torque/.500),angularAcceleration=torque/inertia)
tau=.200/(8*6/(8+6))
put(52,initial=[48/14,48/14,0],final=[6,0,6],tau=tau,halfTime=tau*math.log(2),atHalf=[33/7,12/7,3])

# Exercise53 has two incompatible short-pulse assumptions if L is retained.
# Keep the resistive-impulse shortcut separate from the full RLC step response.
N=300;r=.0100;length=.100;C=10e-6;B=.100
L=mu0*N*N*math.pi*r*r/length
R=.0333*N*2*math.pi*r
impulse=N*math.pi*r*r*B
alpha=R/(2*L);omega0=1/math.sqrt(L*C);omega=math.sqrt(omega0**2-alpha**2)
qResistive=impulse/R
jump=impulse/L
firstMaximumTime=math.atan(omega/alpha)/omega
qStepMaximum=jump/omega*math.exp(-alpha*firstMaximumTime)*math.sin(omega*firstMaximumTime)
firstZeroAfterMaximum=(math.pi/2+math.atan(alpha/omega))/omega
def energyRatio(t):
 q=math.exp(-alpha*t)*(math.cos(omega*t)+alpha/omega*math.sin(omega*t))
 i=-math.exp(-alpha*t)*omega0**2/omega*math.sin(omega*t)
 return q*q+L*C*i*i
energyTime=bisect(lambda t:energyRatio(t)-.1,0,.01)
put(53,L=L,R=R,emfImpulse=impulse,frequency=omega/(2*math.pi),
    resistiveShortcutCharge=qResistive,resistiveShortcutEnergy=qResistive**2/(2*C),
    currentJumpForAbruptField=jump,chargeImmediatelyAfterAbruptField=0,
    firstChargeMaximumForAbruptField=qStepMaximum,energyAtThatMaximum=qStepMaximum**2/(2*C),
    firstMaximumTime=firstMaximumTime,firstZeroAfterMaximum=firstZeroAfterMaximum,
    exactEnergyTenthTime=energyTime,weakDampingEnergyTenthTime=L/R*math.log(10),
    modelIssue='The resistive charge shortcut neglects L during the field pulse; it is not the abrupt-field limit of the stated RLC circuit.')
C=6.40e-9;L=.0660;q=.0800e-6;U=.5*C*24**2;UE=q*q/(2*C);UB=U-UE
put(54,total=U,UE=UE,UB=UB,currentMagnitude=math.sqrt(2*UB/L),capacitorVoltage=q/C,inductorVoltage=-q/C,currentRate=-q/(L*C))
L=.060;C=250e-6;Q=6e-6;U=Q*Q/(2*C);Imax=Q/math.sqrt(L*C)
put(55,Vmax=Q/C,Imax=Imax,Umax=U,chargeAtHalfI=Q*math.sqrt(3)/2,energyAtHalfI=U/4)
L=.330;C=590e-6;i=2.50;rate=73
put(56,Vmax=math.sqrt((L*rate)**2+L/C*i*i))
Leq=.018*(.012+.015)/(.018+.012+.015);tau=Leq/75;t=.115e-3
put(57,Leq=Leq,tau=tau,initialCurrent=0,initialVoltage=20,finalCurrent=20/75,finalVoltage=0,currentAt0115ms=20/75*(1-math.exp(-t/tau)),voltageAt0115ms=20*math.exp(-t/tau))
assert math.isclose(results['57']['tau'],.144e-3,rel_tol=1e-12)
put(58,initialAmmeters=[1/3,0,1/3],initialVoltmeters=[100/3,50/3,0,50/3],finalAmmeters=[50/130,(50/130*30)/75,(50/130*30)/50],finalVoltmeters=[50/130*100,0,50/130*30,50/130*30])
resistance=np.array([3.,4.,5.,6.,7.,8.,10.,12.]);halves=np.array([.735,.654,.589,.536,.491,.453,.393,.347])
slope,intercept=np.polyfit(resistance,1/halves,1)
L=1/(slope*math.log(2));RL=intercept/slope
put(59,slope=float(slope),intercept=float(intercept),L=float(L),RL=float(RL),energyAt20=float(.5*L*20**2),powerAt20=float(RL*20**2),allDataPoints=len(resistance))
put(60,Qmax=3.50*math.sqrt(.0020*5e-6),currentAtQmax=0)
put(61,closedVab=60,closedVcd=60,openVab=-60/25*40,openVcd=-60/25*(40+25))
put(62,currentR1=60/40,currentR2=(60-.300*50)/25,currentR1AfterOpen=-60/25)
put(63,tau=4/(50+150),initialCurrent=0,initialVac=0,initialVcb=36,finalCurrent=36/200,finalVac=36/200*50,finalVcb=36/200*150)
put(64,tau=4/150,currentR0=36/50,initialCurrentR=.18,initialCurrentS2=.72-.18,finalCurrentR=0,finalCurrentS2=.72,Vac=36,Vcb=0)
Req=1/(1/5+1/10+1/15);It=25/(40+Req);Vp=It*Req
put(65,initial=[25/55,0,0,25/55],final=[It,Vp/5,Vp/10,Vp/15])
L=.020;C=25e-6*35e-6/(25e-6+35e-6);I=.600
put(66,initialCurrent=75/125,Qmax=I*math.sqrt(L*C),timeToMaximum=math.pi/2*math.sqrt(L*C),Leq=L,Ceq=C)

with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 page=pdf[1035]
 points67=[];points68=[]
 for drawing in page.get_drawings():
  rect=drawing['rect']
  if drawing.get('fill') and 2<rect.width<7 and 2<rect.height<7:
   x=(rect.x0+rect.x1)/2;y=(rect.y0+rect.y1)/2
   if 125<x<260 and 485<y<570:
    points67.append(((x-131.4196)/(246.8916-131.4196)*4.5,(559.9821-y)/(559.9821-499.4825)*25+20))
   if 370<x<495 and 85<y<155:
    points68.append(((x-378.8494)/(491.5213-378.8494)*15,(152.8683-y)/(152.8683-92.3683)*25))
 for num,points,offset,amplitude,kind in ((67,points67,20,30,'coil'),(68,points68,0,25,'resistor')):
  points.sort();ts=np.array([p[0] for p in points])*1e-3;vs=np.array([p[1] for p in points])
  transformed=np.log((vs-offset)/amplitude) if kind=='coil' else np.log(1-vs/amplitude)
  decay=-float(ts@transformed/(ts@ts));tau=1/decay
  if num==67:put(67,E=50,finalResistorVoltage=30,finalCurrent=3,RL=20/3,tau=tau,L=(10+20/3)*tau,allReadPoints=len(points),points=points)
  else:put(68,RL=0,tau=tau,L=50*tau,finalEnergy=.5*(50*tau)*.5**2,allReadPoints=len(points),points=points)
assert len(points67)==18 and len(points68)==13
N1=1200;N2=750;a=.01;b=.02;length=.20
Lopposed=mu0*math.pi/length*(N1*N1*(b*b-a*a)+(N1-N2)**2*a*a)
Laiding=mu0*math.pi/length*(N1*N1*(b*b-a*a)+(N1+N2)**2*a*a)
Icheck=.700
Bin=mu0*(N1-N2)*Icheck/length
Bannulus=mu0*N1*Icheck/length
energy=Bin**2/(2*mu0)*math.pi*a*a*length
energy+=Bannulus**2/(2*mu0)*math.pi*(b*b-a*a)*length
assert math.isclose(2*energy/Icheck**2,Lopposed,rel_tol=1e-12)
L1=mu0*math.pi*N1*N1*b*b/length
L2=mu0*math.pi*N2*N2*a*a/length
M=mu0*math.pi*N1*N2*a*a/length
assert math.isclose(Lopposed,L1+L2-2*M,rel_tol=1e-12)
assert math.isclose(Laiding,L1+L2+2*M,rel_tol=1e-12)
put(69,Lopposed=Lopposed,Laiding=Laiding)
fractions=np.array([.25,.50,.75,1.0]);L0=.63000
put(70,oxygen=[float(v) for v in L0*(1+1.52e-3*fractions)],mercury=[float(v) for v in L0*(1-2.9e-5*fractions)])
def i1(t):return 48/25*(1-math.exp(-t/(8/25)))
def i2(t):return 48/5000*math.exp(-t/(5000*20e-6))
t1=bisect(lambda t:i1(t)-i2(t),0,.1)
t2=bisect(lambda t:i1(t)+i2(t)-.96,0,1)
put(71,tauL=8/25,tauC=5000*20e-6,initial=[0,48/5000],final=[48/25,0],equalTime=t1,equalCurrent=i1(t1),halfTotalTime=t2)
put(72,turns=math.sqrt(4.4*2/(mu0*math.pi*.5**2)),choice='b')
put(73,halfTimeSeconds=4.4/.005*math.log(2),halfTimeMinutes=4.4/.005*math.log(2)/60,choice='b')
put(74,choice='a')
put(75,U=.5*4.4*750**2,heliumMass=.5*4.4*750**2/20900,choice='c')
assert len(results)==35
out=ROOT/'qa/physics/chapter30';out.mkdir(parents=True,exist_ok=True)
(out/'problems-41-75-checks.json').write_text(json.dumps({'status':'data-recalculated-model53-needs-explicit-assumptions','results':results},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Recalculated35 numbered problems; checked18 and13 plotted source points. Exercise53 retains an explicit model issue.')
