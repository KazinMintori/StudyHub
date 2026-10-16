"""Independent numerical model checks for chapter41 end exercises.

This script recomputes source inputs and enumerates states. It does not certify
prose proofs, prompt completeness or browser layout.
"""
from pathlib import Path
import json,itertools,collections
import numpy as np
from scipy.integrate import quad
from scipy.constants import h,hbar,c,e,m_e,m_p,epsilon_0,mu_0

root=Path(__file__).resolve().parents[2]
q=root/'qa/physics/chapter41'
results={}
checks=0
def close(name,value,expected,rtol=1e-8,atol=0):
    global checks
    assert np.allclose(value,expected,rtol=rtol,atol=atol),(name,value,expected)
    checks+=1
def record(name,**kwargs):
    results[name]=kwargs
a0=4*np.pi*epsilon_0*hbar**2/(m_e*e**2)
muB=e*hbar/(2*m_e)
g=2.00232
evnm=h*c/e*1e9
def scale(m,L): return h*h/(8*m*L*L)/e
def band(n,lo,hi):
    return quad(lambda x:2*np.sin(n*np.pi*x)**2,lo,hi)[0]
def angular(n):
    return [(l,ml) for l in range(n) for ml in range(-l,l+1)]
levels=collections.defaultdict(list)
for triple in itertools.product(range(1,8),repeat=3):
    levels[sum(x*x for x in triple)].append(triple)
close('41.1 spatial degeneracy',[len(levels[3]),len(levels[9])],[1,3])
record('41.1',states=[levels[3],levels[9]],degeneracy=[1,3])
L=(4*np.pi/3)**(1/3)*5.29e-11
gap=3*scale(m_e,L)
record('41.2',sideM=L,gapEV=gap,bohrGapEV=13.6*.75,ratio=gap/(13.6*.75))
close('41.2 volume',L**3,4*np.pi/3*(5.29e-11)**3)
gap=6*scale(m_e,8e-11)
record('41.3',photonEV=gap,wavelengthNM=evnm/gap)
close('41.3 photon energy',h*c/(evnm/gap*1e-9)/e,gap)
points={}
for triple in [(1,1,1),(2,2,1)]:
    locations=list(itertools.product(*[[(2*k+1)/(2*n) for k in range(n)] for n in triple]))
    points[str(triple)]=locations
    for point in locations:
        close('41.4 maximum density',np.prod([np.sin(n*np.pi*x)**2 for n,x in zip(triple,point)]),1)
record('41.4',maximaInL=points)
boxSide=np.sqrt(6*h*8e-9/(8*m_e*c))
close('41.5 gap reconstruction',6*scale(m_e,boxSide),evnm/8)
record('41.5',sideNM=boxSide*1e9)
record('41.6',gapMEV=3*scale(m_p,1e-14)/1e6)
nodes=[('x',1/3),('x',2/3),('y',.5)]
for axis,t in nodes:
    n={'x':3,'y':2}[axis]
    close('41.7 node',np.sin(n*np.pi*t),0,atol=1e-14)
record('41.7',nodesInL=nodes)
record('41.8',cases=[dict(n=n,LmaxInHbar=np.sqrt(n*(n-1)),LbohrInHbar=n,
 percentRelativeBohr=100*(1-np.sqrt(1-1/n))) for n in [3,30]])
record('41.9',Lmin=0,LmaxJS=np.sqrt(12)*hbar,LzMaxJS=3*hbar,SzMaxJS=hbar/2,
 spinToOrbitalZRatios=[-1/6,1/6])
angleRows=[]
for l in range(5):
    row=dict(l=l,Lhbar=float(np.sqrt(l*(l+1))),ml=list(range(-l,l+1)))
    row['anglesDegrees']=None if l==0 else [float(np.degrees(np.arccos(ml/np.sqrt(l*(l+1))))) for ml in range(-l,l+1)]
    angleRows.append(row)
record('41.10',states=angleRows)
close('41.10 state count',sum(len(row['ml']) for row in angleRows),25)
lApprox=(-1+np.sqrt(1+4*(4.716e-34/hbar)**2))/2
close('41.11 nearest orbital integer',round(lApprox),4)
record('41.11',unroundedL=lApprox,l=round(lApprox))
record('41.12',Lhbar=np.sqrt(6),LzMaxHbar=2,anglesDegrees=angleRows[2]['anglesDegrees'])
val=np.cos(np.radians(26.6))**2
record('41.13',unroundedL=val/(1-val),l=round(val/(1-val)))
val=(2/np.cos(np.radians(63.4)))**2
lApprox=(-1+np.sqrt(1+4*val))/2
record('41.14',l=round(lApprox),minimumN=round(lApprox)+1)
close('41.14 correct l',round(lApprox),4)
record('41.15',n=8,energyEV=-13.6/64,LmaxJS=np.sqrt(56)*hbar,
 maximumAngleDegrees=np.degrees(np.arccos(-7/np.sqrt(56))))
record('41.16',states=angular(4),energyEV=-13.6/16)
close('41.16 spatial count',len(angular(4)),16)
angle=np.degrees(np.arccos(4/np.sqrt(20)))
record('41.17',states=9,minAngleDegrees=angle,maxAngleDegrees=180-angle)
def radialProbability(lo,hi):
    return quad(lambda u:4*u*u*np.exp(-2*u),lo,hi)[0]
p1=radialProbability(0,.5);p2=radialProbability(.5,1)
close('41.18 source probabilities',[p1,p2],[.0803013970714,.2430221867455],rtol=1e-10)
record('41.18',belowHalfA=p1,betweenHalfAndA=p2)
for ml in range(-8,9):
    close('41.19 periodic phase',np.exp(2j*np.pi*ml),1,atol=1e-13)
record('41.20',nFromPeak=np.sqrt(.476e-9/a0),nl='3d',peak4fNM=16*a0*1e9)
record('41.21',fieldT=2.71e-5/(muB/e),levelCount=3)
record('41.22',adjacentSplitEV=muB*.8/e,mlEnergiesRelativeEV=(np.arange(-2,3)*muB*.8/e).tolist())
record('41.23',adjacentSplitEV=muB*.6/e,totalSplitEV=8*muB*.6/e,levelCount=9)
record('41.24',transitionML=[(-1,0),(0,0),(1,0)],longer=(-1,0),shorter=(1,0),same=(0,0))
S=np.sqrt(.75)*hbar
omega=S/(.4*m_e*(1e-17)**2)
record('41.25',uniformSolidSphereOmega=omega,equatorSpeedMS=omega*1e-17,speedToC=omega*1e-17/c)
close('41.25 rotational angular momentum',.4*m_e*1e-34*omega,S)
record('41.26',frequencyHz=5.9e-6*e/h,wavelengthCM=h*c/(5.9e-6*e)*100,
 effectiveFieldT=5.9e-6/(2*muB/e))
record('41.27',splittingEV=2*muB*1.45/e,lowerMS=.5)
record('41.28',interactionEV=-muB*1.6/e,orbitalInteraction=False)
statesNe=[(1,0,0,ms) for ms in [-.5,.5]]+[(2,l,ml,ms) for l in [0,1] for ml in range(-l,l+1) for ms in [-.5,.5]]
close('41.29 neon state count',len(statesNe),10)
assert len(set(statesNe))==10
record('41.29',states=statesNe)
configGe={'1s':2,'2s':2,'2p':6,'3s':2,'3p':6,'4s':2,'3d':10,'4p':2}
close('41.30 germanium electron count',sum(configGe.values()),32)
record('41.30',configuration=configGe)
for name,Z,config in [('Be',4,[2,2]),('Mg',12,[2,2,6,2]),('Ca',20,[2,2,6,2,6,2]),('C',6,[2,2,2]),('Si',14,[2,2,6,2,2])]:
    close('41.31/32 '+name,sum(config),Z)
record('41.33',ionizationEV=13.6*(2.771/5)**2)
record('41.35',N2plusConfiguration=[2,2,1],P2plusConfiguration=[2,2,6,2,1],
 lowestBoundEV=[-13.6*9/4,-13.6*9/9])
close('41.35 N2+count',sum(results['41.35']['N2plusConfiguration']),7-2)
close('41.35 P2+count',sum(results['41.35']['P2plusConfiguration']),15-2)
record('41.36',unroundedZ=1+np.sqrt(7460/10.2),element='Ni',Z=28)
record('41.37',model='Empirical Moseley f=2.48e15(Z-1)^2; derive E and lambda consistently',
 elements=[dict(element=name,Z=Z,frequencyHz=2.48e15*(Z-1)**2,
 energyKEV=h*2.48e15*(Z-1)**2/e/1000,wavelengthNM=c/(2.48e15*(Z-1)**2)*1e9)
 for name,Z in [('Ca',20),('Co',27),('Cd',48)]])
record('41.38',kaWavelengthNM=evnm/57500,kbWavelengthNM=evnm/67300)
filled=sum(2*len(levels[N]) for N in [3,6])
close('41.39 first two filled levels',filled,8)
record('41.39',highestEnergyToGround=9/3,occupancyByEnergySum=[2,6,2])
probGround=band(1,0,.25)**3
probExc=band(2,0,.25)*band(1,0,.25)**2
record('41.41',volumeFraction=1/64,groundProbability=probGround,excitedProbability=probExc)
close('41.41 factorization check',probGround,(.25-1/(2*np.pi))**3)
record('41.44',groundFactor=1.5,firstExcitedFactor=2.5,spatialDegeneracies=[1,3],
 firstExcitedTriples=[(1,0,0),(0,1,0),(0,0,1)])
record('41.45',groundCoefficients=[1,.5],firstExcitedCoefficients=[1,1.5],spatialDegeneracies=[1,1])
record('41.46',gapInXEnergyUnit=.75,firstExcitedSpatialDegeneracy=1,maximumInLX=[.5,1,1/3])
for n in range(1,12):close('41.47 enumerate shell spin count',2*len(angular(n)),2*n*n)
record('41.47',shell50States=5)
Nsun=2e30/1.7e-27;Ve=(4*np.pi/3)*(7e6)**3/Nsun;Vcarbon=6*Ve
Lcarbon=Vcarbon**(1/3)
record('41.48',hydrogenBasedElectronEstimate=Nsun,volumePerElectronM3=Ve,
 volumePerCarbonM3=Vcarbon,sideM=Lcarbon,highestElectronEV=6*scale(m_e,Lcarbon))
close('41.49 forbidden probability',radialProbability(2,np.inf),13*np.exp(-4))
record('41.49',turningRadiusInA=2,forbiddenProbability=13*np.exp(-4))
record('41.50',radialPeakInA=1)
record('41.51',radialPeakInA=4)
mpApprox=1.7e-27
muP=e*hbar/(4*mpApprox)
current=muP/(np.pi*(.85e-15)**2)
B=mu_0*muP/(2*np.pi*((.40*a0)**2+(.85e-15)**2)**1.5)
U=muB*B
record('41.52',modelProtonMomentJT=muP,currentA=current,fieldT=B,
 hyperfineEnergyEV=U/e,wavelengthM=h*c/(2*U))
close('41.52 current moment',current*np.pi*(.85e-15)**2,muP)
r=4*a0;v=np.sqrt(2)*hbar/(m_e*r)
B=mu_0*e*v/(4*np.pi*r*r)
record('41.58',radiusM=r,speedMS=v,numeratorMu0EV=mu_0*e*v,denominator4PiR2=4*np.pi*r*r,fieldT=B)
close('41.58 orbital momentum',m_e*v*r,np.sqrt(2)*hbar)
record('41.59',firstNobleAtomicNumbers=[4,20],sodiumConfiguration={'1s':4,'2s':4,'2p':3})
close('41.59 sodium electron count',sum(results['41.59']['sodiumConfiguration'].values()),11)
lambda0=evnm/((3/4)*13.606)
Egamma=(3/4)*13.606-muB*2.20/e
lambdaB=evnm/Egamma
record('41.61',zeroWavelengthNM=lambda0,withFieldWavelengthNM=lambdaB,shiftNM=lambdaB-lambda0)
assert lambdaB>lambda0
B62=h*c/(2*muB*.042)
record('41.62',wavelengthM=.042,fieldT=B62)
close('41.62 resonance',2*muB*B62,h*c/.042)
def fine(n,j):return -13.60/n**2*(1+(1/137.04)**2/n**2*(n/(j+.5)-.75))
split=fine(3,1.5)-fine(3,.5)
ground=fine(2,.5)
lambdaHigh=evnm/(fine(3,1.5)-ground)
lambdaLow=evnm/(fine(3,.5)-ground)
record('VP41.8.4-and41.64',higherInitialEnergyEV=fine(3,1.5),lowerInitialEnergyEV=fine(3,.5),
 finalEnergyEV=ground,splittingEV=split,wavelengthDifferenceNM=lambdaLow-lambdaHigh,longerInitialJ=.5)
assert lambdaLow>lambdaHigh

# Recompute all twelve guided-practice numerical outputs by quadrature/enumeration.
record('VP41.1.1',nodesInL=[('x',.5),('z',1/3),('z',2/3)],probability=band(2,0,1/3))
record('VP41.1.2',probabilities=[band(n,.25,.75) for n in range(1,5)])
record('VP41.1.3',probabilities=[band(nx,0,.25)*band(ny,0,.25) for nx,ny in [(1,1),(2,1),(3,2),(4,1)]])
record('VP41.1.4',volumeFraction=.125,probability=band(1,.25,.75)**3)
record('VP41.4.1',stateCount=len(angular(6)),LmaxHbar=np.sqrt(30),LzMaxHbar=5)
record('VP41.4.2',states=angular(3),minAngleNegativeZ=np.degrees(np.arccos(2/np.sqrt(6))),selectedState=[2,-2])
record('VP41.4.3',photonEV=[13.6*(1/nf**2-1/ni**2) for ni,nf in [(3,2),(4,2),(2,1)]])
record('VP41.4.4',probabilities=[radialProbability(0,2),radialProbability(1,3),radialProbability(4,np.inf)])
record('VP41.8.1',splittingEV=g*muB*3.14/e,higherMS=.5)
f=g*muB*2.36/h
record('VP41.8.2',frequencyHz=f,wavelengthMM=c/f*1000)
split=h*c*(1/(766.490e-9)-1/(769.896e-9))
record('VP41.8.3',splittingEV=split/e,effectiveFieldT=split/(2*muB))
for label,expected in [('VP41.1.1',.402249445),('VP41.1.4',.547943)]:
    close(label,results[label]['probability'],expected,rtol=5e-5)
if __name__=='__main__':
    output=dict(status='passed',computedCases=len(results),assertions=checks,
      scope='Independent numerical/source-input checks only; analytical prose, figure boundaries, completeness and browser acceptance are separate.',results=results)
    (q/'end-independent-numeric.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(status=output['status'],computedCases=len(results),assertions=checks),indent=2))
