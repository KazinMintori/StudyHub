"""Independent guided-practice calculation using printed data, not answer fitting."""
from pathlib import Path
import cmath,json,math
ROOT=Path(__file__).resolve().parents[2]
out=ROOT/'qa/physics/chapter31';out.mkdir(parents=True,exist_ok=True)
def circuit(R,L,C,w,V):
 z=complex(R,w*L-1/(w*C))
 I=V/abs(z)
 return {'XL':w*L,'XC':1/(w*C),'Z':abs(z),'I':I,'phiDeg':math.degrees(cmath.phase(z)),
         'powerFactor':R/abs(z),'VR':I*R,'VL':I*w*L,'VC':I/(w*C),'averagePower':.5*I**2*R}
r={}
XL=2*math.pi*108e6*2.50e-3
r['VP31.3.1']={'XL':XL,'I':4.20e3/XL}
r['VP31.3.2']={'VR':2.40e-3*125,'XC':1/(1.75e3*7e-6),'VC':2.40e-3/(1.75e3*7e-6)}
r['VP31.3.3']={'f':1/(2*math.pi*155*8e-6),'VR':155*4e-3,'VC':155*4e-3,'crossVoltages':[0,0]}
I=2.45/116
r['VP31.3.4']={'R':116,'I':I,'iAt3_5ms':I*math.cos(5100*.0035),
               'phaseAt3_5ms':5100*.0035,'VC':'underdetermined','C':'underdetermined'}
r['VP31.5.1']=circuit(255,.045,.400e-6,255/.045,55)
r['VP31.5.1']['f']=(255/.045)/(2*math.pi)
w,L,C,V,Z=5400,6.5e-3,.600e-6,20,474
R=math.sqrt(Z**2-(w*L-1/(w*C))**2)
r['VP31.5.2']=circuit(R,L,C,w,V);r['VP31.5.2']['R']=R
X=65*math.tan(math.radians(15))
r['VP31.5.3']={'X':X,'L':(X+1/(1.20e4*.965e-6))/1.20e4}
w,I,t=8000,.120,.305e-3
VR,VL,VC=I*95,I*w*.0065,I/(w*.440e-6)
r['VP31.5.4']={'VR':VR,'VL':VL,'VC':VC,'theta':w*t,
 'vR':VR*math.cos(w*t),'vL':-VL*math.sin(w*t),'vC':VC*math.sin(w*t)}
r['VP31.7.1']={'averagePower':120*3.95,'peakPower':2*120*3.95,'R':120/3.95}
data=circuit(275,.0823,1.10e-6,1300,35)
r['VP31.7.2']={k:data[k] for k in ['XL','XC','phiDeg','powerFactor']}
r['VP31.7.3']={k:data[k] for k in ['Z','I','averagePower']}
pf,w,L,C=.8,13000,.00750,.440e-6
XL,XC=w*L,1/(w*C)
phi=math.copysign(math.acos(pf),XL-XC)
R=abs(XL-XC)/math.tan(math.acos(pf))
r['VP31.7.4']={'XL':XL,'XC':XC,'phiDeg':math.degrees(phi),'R':R}
assert math.isclose(R,103.1002331002331)
assert phi<0
L,R,C,V=.0015,125,25e-9,35*math.sqrt(2)
X=R*math.sqrt(8)
low=(-X+math.sqrt(X**2+4*L/C))/(2*L)
high=(X+math.sqrt(X**2+4*L/C))/(2*L)
r['bridge']={'omegaLow':low,'omegaHigh':high,'Vsource':V,'Imax':V/R,
             'I':V/(3*R),'low':circuit(R,L,C,low,V),'high':circuit(R,L,C,high,V)}
for result in [r['bridge']['low'],r['bridge']['high']]:
 assert math.isclose(result['I'],r['bridge']['I'])
 assert math.isclose(result['Z'],3*R)
assert len(r)==13
report={'status':'passed','sourcePagesReviewed':'Printed1041,1047; PDF1061,1067, including direct images',
        'problems':12,'bridgingProblems':1,'printedDataIssues':['VP31.3.4 partsc,d underdetermined','VP31.7.4 key differs from printed C and phase'],
        'results':r}
(out/'guided-data-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
