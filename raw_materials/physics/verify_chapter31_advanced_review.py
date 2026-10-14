"""Independent reviewer checks for voltage-resonance conditions and MCAT units."""
from pathlib import Path
import json,math
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'qa/physics/chapter31'
OUT.mkdir(parents=True,exist_ok=True)
# Exact bivariate polynomial arithmetic. Keys are powers of (y,a).
def add(p,q,scale=1):
 r=p.copy()
 for k,v in q.items():r[k]=r.get(k,0)+scale*v
 return {k:v for k,v in r.items() if v}
def mul(p,q):
 r={}
 for (i,j),u in p.items():
  for (k,l),v in q.items():r[i+k,j+l]=r.get((i+k,j+l),0)+u*v
 return {k:v for k,v in r.items() if v}
def derivative(p):return {(i-1,j):i*v for (i,j),v in p.items() if i}
D={(0,0):1,(1,0):-2,(2,0):1,(1,1):1}
def quotientDerivativeNumerator(n):return add(mul(derivative(n),D),mul(n,derivative(D)),-1)
assert quotientDerivativeNumerator({(1,1):1})=={(0,1):1,(2,1):-1}
assert quotientDerivativeNumerator({(2,0):1})=={(1,0):2,(2,0):-2,(2,1):1}
assert quotientDerivativeNumerator({(0,0):1})=={(0,0):2,(1,0):-2,(0,1):-1}
for loss in [.05,.5,1,1.99]:
 yc0=1-loss/2;yl0=1/(1-loss/2)
 grid=np.geomspace(1e-7,1e5,100000)
 den=(1-grid)**2+loss*grid
 assert 1/((1-yc0)**2+loss*yc0)>=np.max(1/den)-1e-9
 assert yl0**2/((1-yl0)**2+loss*yl0)>=np.max(grid**2/den)-1e-9
 assert math.isclose(1/((1-yc0)**2+loss*yc0),4/(loss*(4-loss)))
 assert math.isclose(yl0**2/((1-yl0)**2+loss*yl0),4/(loss*(4-loss)))
for loss in [2,3,20]:
 grid=np.geomspace(1e-7,1e5,100000)
 den=(1-grid)**2+loss*grid
 assert np.all(np.diff(grid**2/den)>0)
 assert np.all(np.diff(1/den)<=1e-12)
 assert (1/den)[-1]<(1/den)[0]
 assert np.max(grid**2/den)<1

# PDF labels use micrometres and square roots, not the OCR's milli/12 strings.
rho=100*.01  # ohm cm -> ohm m
radius=20e-6/2
C=10e-9
RA=rho/(10*radius)
f=5000/math.pi
w=2*math.pi*f
XC=1/(w*C)
Z=math.hypot(RA,XC)
assert math.isclose(RA,1e4)
assert math.isclose(XC,1e4)
assert math.isclose(Z,math.sqrt(2)*1e4)
endToEnd=2*math.sqrt(2)*1.5e-9
R,L,Vin,f0=100,1e-6,10,1e5
w0=2*math.pi*f0
resonantCapacitance=1/(w0*w0*L)
outputAtResonance=Vin*w0*L/R
assert math.isclose(resonantCapacitance,2.533029591058445e-6)
# Ten alternating conducting plates have nine adjacent opposing-potential gaps.
plates=['A','B']*5
gaps=list(zip(plates[:-1],plates[1:]))
assert len(gaps)==9 and all(a!=b for a,b in gaps)
eps0=8.8541878128e-12
radius53,gap53,L53,R53,V53=.060,.002,100e-6,10,.100
w53=2*math.pi*1180e3
C53=1/(w53*w53*L53)
theta53=C53*gap53/(9*eps0*radius53**2)
C120=9*eps0*radius53**2*math.radians(120)/gap53
w120=1/math.sqrt(L53*C120)
assert 0<theta53<math.pi
assert math.isclose(9*eps0*(.5*radius53**2*theta53)/(gap53/2),C53)
gain3db=10**(-3/20)
ratio3db=1/math.sqrt(10**(.3)-1)
L65exact=100*ratio3db/(2*math.pi*1e4)
assert math.isclose(20*math.log10(ratio3db/math.sqrt(1+ratio3db**2)),-3)
L57,C57,R57,V57=.005,2.5e-6,75,15
X57=R57*math.sqrt(3)
disc57=math.sqrt(X57**2+4*L57/C57)
omegas57=[(-X57+disc57)/(2*L57),(X57+disc57)/(2*L57)]
for omega57 in omegas57:
 z=math.hypot(R57,omega57*L57-1/(omega57*C57))
 assert math.isclose(R57/z,.5)
 assert math.isclose(V57/z,.1)
report={
 'status':'passed',
 'problem31_68':{
  'definitions':'y=(omega/omega0)^2; a=R^2*C/L; R,L,C>0',
  'resistorPeakY':1,
  'capacitorPeakY':'1-a/2 for 0<a<2',
  'inductorPeakY':'1/(1-a/2) for 0<a<2',
  'largeResistance':'For a>=2, capacitor ratio decreases from1; inductor ratio increases toward1 without a finite-frequency maximum.',
  'peakVoltageRatioSquared':'4/(a*(4-a)) for 0<a<2',
  'idealZeroResistance':'At R=0 the finite driven steady-state resonance formula is singular.'
 },
 'problem31_66':{'inductanceH':L,'outputAcross':'capacitor',
                 'resonantCapacitanceF':resonantCapacitance,
                 'outputAtResonanceV':outputAtResonance,
                 'outputPhaseAtResonanceRad':-math.pi/2},
 'problem31_53':{'plates':10,'activeGaps':9,'gapBetweenOppositePlatesM':gap53/2,
                 'formula':'C=9*epsilon0*a^2*theta/g',
                 'CresF':C53,'thetaDegrees':math.degrees(theta53),
                 'outputAt1180kHzV':V53/R53*w53*L53,
                 'C120F':C120,'frequencyAt120DegreesHz':w120/(2*math.pi),
                 'outputAt120DegreesV':V53/R53*w120*L53,
                 'sourceKeyIssue':'Five-gap coefficient fits appendix but conflicts with ten alternating plates; do not choose model by answer fitting.'},
 'problem31_57':{'omegaBoth':omegas57,'phaseBothDegrees':[-60,60],
                 'Ipeak':.1,'resistorAveragePower':.375,'inductorAveragePower':0,
                 'capacitorAveragePower':0},
 'problem31_65':{'gainAtMinus3dB':gain3db,'omegaLOverR':ratio3db,
                 'inductanceExactFor10kHzH':L65exact,
                 'halfPowerApproximationH':100/(2*math.pi*1e4),
                 'halfPowerAttenuationdB':20*math.log10(1/math.sqrt(2))},
 'mcat':{'rhoOhmM':rho,'radiusM':radius,'accessResistanceOhm':RA,
         'frequencyHz':f,'angularFrequency':w,'XC':XC,'impedanceOhm':Z,
         'dcImpedance':'infinite','endToEndVoltageV':endToEnd,
         'highFrequencyImpedanceOhm':RA,'choices':['b','c','d','c']}
}
assert math.isclose(report['mcat']['angularFrequency'],2*math.pi*report['mcat']['frequencyHz'])
(OUT/'advanced-review-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
