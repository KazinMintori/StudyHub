"""Recalculate chapter29 exercises31–60, including RC and dynamical models."""
from pathlib import Path
import math,json
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
mu0=4*math.pi*1e-7;eps0=8.8541878128e-12
results={}
def put(n,**values):results[str(n)]=values
put(31,speed=1.75*6/(1.20*.250))
put(32,field=.001/(.15*.005))
put(33,current=1.25*.750*3/12.5,entryDuration=.500/3)
put(34,electricField=.0225*.250/2)
put(35,currentRate=2*math.pi*.035*8e-6/(mu0*400*math.pi*.011**2))
put(36,fieldAt005=mu0*900*36*.005/2,fieldAt01=mu0*900*36*.010/2)
put(37,averageEmf=12*mu0*9000*8e-4*.350/.0400)
j=.520/(math.pi*.040**2)
put(38,displacementDensity=j,electricRate=j/eps0,magneticAt02=mu0*.520*.020/(2*math.pi*.040**2),magneticAt01=mu0*.520*.010/(2*math.pi*.040**2))
put(39,charge=4.70*eps0*3e-4/.00250*120,currentRate=.006,displacement=.006)
q=.0018*.5e-6;E=q/(eps0*5e-4)
put(40,charge=q,electric=E,voltage=E*.002,electricRate=.0018/(eps0*5e-4),density=.0018/5e-4,displacement=.0018)
put(41,displacement=2.5*eps0*20*1.5**4,earlierTime=1.5/(6**.25))
put(42,superconductingMagnetization=-.130/mu0)
put(43,charge=70*3600,currentTwoWipers=2*20+10+2*5,currentThreeWipers=2*20+10+3*5,field=math.pi*14/(2*42*(2*math.pi*400)*math.pi*.025**2))
k44=2.90**2*.040**2/.005
put(44,accelerationAt003=(.180-k44*.030)/.024,terminal=.180/k44,accelerationOutside=.180/.024)
# The PDF explicitly gives C=20 microfarad and t=200 microsecond.
C45=20e-6;R045=10.;t45=200e-6;tau45=C45*R045
coupling=mu0*.200/(2*math.pi)*math.log((.050+.100)/.050)
smallR=25*2*(.100+.200)*1.
large45=100/R045*math.exp(-t45/tau45)
put(45,largeCurrent=large45,smallResistance=smallR,smallCurrent=25*coupling*(large45/tau45)/smallR)
put(46,smallCurrent=25*coupling*(5./tau45)/smallR)
t47=math.sqrt(3.20/.160)
put(47,time=t47,emf=5*mu0*9000*2e-4*.320*t47)
put(48,emfAboutY=.0600*35*.320,emfAboutX=0.,emfAboutZ=.0600*35*.320)
put(50,flux=.005*8e-4,passTime=.040/.020,emf=.005*8e-4/(.040/.020))
put(51,averageEmf=1.35*math.pi*(.0650/2)**2/.250)
beta52=1.50**2*.200**2/80.;terminal52=1.90/beta52;tau52=.120/beta52
time52=-tau52*math.log1p(-25./terminal52)
put(52,dragCoefficient=beta52,terminal=terminal52,timeTo25=time52)
field54,length54,res54,mass54,source54=2.4,.36,5.,.90,12.
put(54,initialAcceleration=field54*length54*source54/(mass54*res54),accelerationAt2=field54*length54*(source54-field54*length54*2)/(mass54*res54),terminal=source54/(field54*length54),timeConstant=mass54*res54/(field54**2*length54**2))
A56=math.pi*.042**2;B056=.080;t056=.0100
emf56=lambda t:A56*B056*(6*t/t056**2-6*t*t/t056**3)
emf_a=emf56(.005);emf_b=emf56(.0121)
put(56,emfAt005=emf_a,internalResistance=emf_a/.003-12.,emfAt0121=emf_b,reversal=t056)
put(57,endPivotEmf=.5*.650*8.80*.240**2,centerToEnd=.5*.650*8.80*(.240/2)**2)
v=np.array([6.80,0.,0.]);B=np.array([.120,-.220,-.0900]);rod=.250*np.array([math.cos(math.radians(36.9)),math.sin(math.radians(36.9)),0.])
put(58,signedEmf=float(np.dot(np.cross(v,B),rod)))
resPerLength=.0100;N1,N2,a,b,C,Q=5000,100,.400,.0400,10e-6,100e-6
R1=resPerLength*N1*2*math.pi*a;R2=resPerLength*N2*2*math.pi*b
I0=(Q/C)/R1;tau=R1*C;smallArea=math.pi*b*b
magneticPerAmp=mu0*N1/(2*a)
I1=lambda t:I0*math.exp(-t/tau)
I2=lambda t:N2*smallArea*magneticPerAmp*(I1(t)/tau)/R2
put(60,largeResistance=R1,smallResistance=R2,timeConstant=tau,initialLargeCurrent=I0,initialFluxPerSmallTurn=magneticPerAmp*I0*smallArea,smallCurrentAt126ms=I2(.00126))
assert math.isclose(results['31']['speed'],35.)
assert math.isclose(results['45']['largeCurrent'],10/math.e)
assert math.isclose(results['45']['smallCurrent'],.00134720926787,rel_tol=1e-3)
assert math.isclose(results['52']['timeTo25'],1.59075,rel_tol=1e-3)
assert math.isclose(results['56']['emfAt005'],.06650123329,rel_tol=1e-3)
assert results['56']['emfAt0121']<0
assert results['58']['signedEmf']>0
out=ROOT/'qa/physics/chapter29';out.mkdir(parents=True,exist_ok=True)
(out/'exercises31-60-checks.json').write_text(json.dumps({'status':'passed','results':results},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(results,ensure_ascii=False,indent=2))
