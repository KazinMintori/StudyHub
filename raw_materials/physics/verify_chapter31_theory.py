"""Check all nine examples, sinusoidal identities, phase and resonance in chapter31.

The numerical integrations below use sampled instantaneous voltages/currents,
separately from the amplitude formulas used to obtain the example answers.
"""
from pathlib import Path
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'qa/physics/chapter31'
OUT.mkdir(parents=True, exist_ok=True)
theta = np.linspace(0, 2*math.pi, 200001)
def average(a):
    return float(np.trapezoid(a, theta)/(2*math.pi))
def close(a,b):
    assert math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-11), (a,b)

examples = {}
examples['31.1'] = dict(meanCurrent=0, meanSquareCurrent=2.7**2,
                       amplitude=2.7*math.sqrt(2))
# The printed data are 250 microamperes, not 250 milliamperes.
V,I,f = 3.60,250e-6,1.60e6
XL = V/I
L = XL/(2*math.pi*f)
examples['31.2'] = dict(XL=XL,L=L,current16MHz=V/(2*math.pi*16e6*L),
                       current160kHz=V/(2*math.pi*160e3*L))
close(XL,14400)
close(examples['31.2']['current16MHz'],25e-6)
close(examples['31.2']['current160kHz'],2.5e-3)
R,C,w,VR = 200,5e-6,2500,1.20
I=VR/R
XC=1/(w*C)
examples['31.3'] = dict(I=I,XC=XC,VC=I*XC,voltageFraction=XC/R)
close(I,.006); close(XC,80); close(I*XC,.48)

R,L,C,V,w = 300,.060,.5e-6,50,1e4
XL,XC=w*L,1/(w*C)
Z=math.hypot(R,XL-XC)
I=V/Z
phi=math.atan2(XL-XC,R)
examples['31.4'] = dict(XL=XL,XC=XC,Z=Z,I=I,phiRad=phi,
                       phiDegrees=math.degrees(phi),VR=I*R,VL=I*XL,VC=I*XC)
close(Z,500);close(phi,math.atan(4/3))
vR=I*R*np.cos(theta)
vL=-I*XL*np.sin(theta)
vC=I*XC*np.sin(theta)
source=V*np.cos(theta+phi)
assert np.max(np.abs(source-vR-vL-vC))<1e-12
examples['31.5']=dict(periodSeconds=2*math.pi/w,
                      kirchhoffMaxResidual=float(np.max(np.abs(source-vR-vL-vC))))
P,Vrms=1500,120
examples['31.6']=dict(R=Vrms**2/P,Irms=P/Vrms,peakPower=2*P)
examples['31.7']=dict(powerFactor=R/Z,averagePower=.5*V*I*math.cos(phi),
                      resistorPower=average(vR*I*np.cos(theta)),
                      inductorPower=average(vL*I*np.cos(theta)),
                      capacitorPower=average(vC*I*np.cos(theta)))
close(examples['31.7']['averagePower'],1.5)
close(examples['31.7']['resistorPower'],1.5)
close(examples['31.7']['inductorPower'],0)
close(examples['31.7']['capacitorPower'],0)
R,L,C,Vrms=500,.40e-3,100e-12,1.0
w0=1/math.sqrt(L*C)
XL=w0*L;XC=1/(w0*C);Irms=Vrms/R
examples['31.8']=dict(w0=w0,f0=w0/(2*math.pi),XL=XL,XC=XC,Z=R,
                      Irms=Irms,VRrms=Vrms,VLrms=Irms*XL,VCrms=Irms*XC)
close(XL,XC);close(Irms*XL,4)
P,V1,V2=960,120,240
I1,I2=P/V1,P/V2
load=V2**2/P
reflected=load/(V2/V1)**2
examples['31.9']=dict(turnsRatio=V2/V1,I1=I1,I2=I2,R=load,
                      primaryEffectiveResistance=reflected)
close(load,60);close(reflected,15);close(V1*I1,V2*I2)

# Verify the phase convention and power identity for both signs of reactance.
for R,L,C,w in [(300,.060,.5e-6,1e4),(300,.060,.5e-6,1e3),
                (5,2,.5e-6,1000),(300,.060,.5e-6,1/math.sqrt(.060*.5e-6))]:
    XL,XC=w*L,1/(w*C)
    Z=math.hypot(R,XL-XC)
    phi=math.atan2(XL-XC,R)
    I=50/Z
    vi=50*np.cos(theta+phi)*I*np.cos(theta)
    close(average(vi),.5*50*I*math.cos(phi))
    close(average(vi),.5*I**2*R)
    close(math.cos(phi),R/Z)
    i=I*np.cos(theta)
    # q=I sin(theta)/w: i=dq/dt, vC=q/C.
    q=I*np.sin(theta)/w
    close(float(q[50000]/C),I*XC)
    assert np.max(np.abs(50*np.cos(theta+phi)-
        (i*R-I*XL*np.sin(theta)+I*XC*np.sin(theta))))<1e-10

curve = {'w0':1/math.sqrt(2*.5e-6),'peakCurrentByR':{str(r):100/r for r in [200,500,2000]}}
close(curve['w0'],1000)
selfchecks={'31.1':['D','A','B','C'],'31.2':['iii','ii','i'],
            '31.3':{'currents':{'i':.1,'ii':50/300,'iii':50/600,'iv':50/200},
                    'order':['iv','ii','i','iii']},
            '31.4':{'a':'v','b':'iv'},'31.5':'ii',
            '31.6':{'secondaryTurns':[50,2000,25,500],'order':['ii','iv','i','iii']}}
assert sorted(selfchecks['31.3']['currents'],key=selfchecks['31.3']['currents'].get,
              reverse=True)==selfchecks['31.3']['order']
assert sorted(range(4),key=lambda k:selfchecks['31.6']['secondaryTurns'][k],
              reverse=True)==[1,3,0,2]
report={'status':'passed','examples':examples,'selfchecks':selfchecks,
        'resonanceCurve':curve,'averagingChecks':{'cosSquared':average(np.cos(theta)**2),
        'cosSin':average(np.cos(theta)*np.sin(theta))}}
(OUT/'theory-numeric-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
