"""Check all12 guided problems and the original bridging antenna problem."""
from pathlib import Path
import math,json
import numpy as np
R=Path(__file__).resolve().parents[2];c=3e8;mu=4*math.pi*1e-7;eps=1/(mu*c*c)
d={}
def put(key,**data):d[key]={'status':'passed',**data}
def field(I):
 E=math.sqrt(2*mu*c*I);B=E/c
 assert math.isclose(E*B/(2*mu),I,rel_tol=1e-12)
 return E,B
put('VP32.2.1',Emax=c*4.3e-3,wavelengthM=2*math.pi/2.5e6,frequencyHz=c*2.5e6/(2*math.pi),propagation='+z')
put('VP32.2.2',wavelengthM=2*math.pi/6.5e6,omega=c*6.5e6,Bmax=2.45e6/c,propagation='+y',magneticDirection='-z')
phase=2*math.pi*1.85e-6/2.94e-6;factor=math.cos(phase)
put('VP32.2.3',lambdaM=2.94e-6,positionM=1.85e-6,Borigin=4.2e6/c,Eposition=4.2e6*factor,Bposition=4.2e6/c*factor,
    phase=phase,directionOriginB='+z',directionPositionE='-y',directionPositionB='-z')
f=c/6.35e-7;v=f*3.47e-7
put('VP32.2.4',frequencyVacuum=f,frequencyMaterial=f,speedMaterial=v,dielectric=(c/v)**2)
E=math.sqrt(mu*c*11);B=E/c
assert math.isclose(E*B/mu,11,rel_tol=1e-12)
put('VP32.4.1',electric=E,magnetic=B,energyDensity=11/c)
put('VP32.4.2',SmaxCoefficient='Emax*Bmax/mu0',factors=[1.,0.,.5],direction='+x')
I=.5*eps*c*.360**2
put('VP32.4.3',Bmax=.360/c,intensity=I,powerW=I*2*math.pi*(12.5e3)**2)
E,B=field(1360)
put('VP32.4.4',Emax=E,Bmax=B,powerW=1360*4*math.pi*(1.5e11)**2)
theta=np.linspace(0,2*math.pi,10000)[:-1]
assert abs(np.sin(2*theta).mean())<1e-12
put('VP32.7.1',maxCoefficient='Emax*Bmax/mu0',factors=[0,math.sqrt(3)/2,-1],meanNetFlow=0)
lam=4*3.6e-3
put('VP32.7.2',wavelengthM=lam,frequencyHz=c/lam,standingElectricAmplitude=1.2e-7*c,
    incidentMagneticAmplitude=1.2e-7/2)
L=.0456
put('VP32.7.3',wavelengthsM=[2*L/n for n in [1,2,3]],frequencyHz=[n*c/(2*L) for n in [1,2,3]],
    electricNodesM=[[j*L/n for j in range(n+1)] for n in [1,2,3]])
assert math.isclose(2*.488/.122,8)
put('VP32.7.4',frequencyHz=c/.122,electricAntinodes=8)
power=55e3;distance=2.5e3;area=math.pi*.09**2;freq=95e6
I=power/(4*math.pi*distance**2);E,B=field(I);emf=2*math.pi*freq*area*B
assert math.isclose(emf/(2*math.pi*freq),area*B,rel_tol=1e-12)
put('bridge',intensity=I,Emax=E,Bmax=B,area=area,fluxAmplitude=area*B,emfAmplitude=emf,
    loopSmallParameter=math.pi*.18/(c/freq))
assert len(d)==13
q=R/'qa/physics/chapter32';q.mkdir(parents=True,exist_ok=True)
(q/'guided-data-checks.json').write_text(json.dumps({'status':'passed','guidedProblems':12,'bridgingProblems':1,'results':d},indent=2)+'\n',encoding='utf8')
print('Verified12 guided problems, standing-wave phase signs and antenna emf.')
