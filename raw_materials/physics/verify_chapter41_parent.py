"""Independent source-sensitive calculations for chapter41 parent review."""
from pathlib import Path
import json,itertools,collections
import numpy as np
from scipy.integrate import quad
from scipy.constants import h,hbar,c,e,m_e,m_p,epsilon_0,Avogadro
ROOT=Path(__file__).resolve().parents[2]
QA=ROOT/'qa/physics/chapter41';QA.mkdir(parents=True,exist_ok=True)
rows={}
def check(label,a,b,rtol=1e-10,atol=0):
    assert np.allclose(a,b,rtol=rtol,atol=atol),(label,a,b)

mr=m_e*m_p/(m_e+m_p)
a=4*np.pi*epsilon_0*hbar*hbar/(mr*e*e)
EH=mr*e**4/(2*(4*np.pi*epsilon_0)**2*hbar*hbar)
muB=e*hbar/(2*m_e)
alpha=e*e/(4*np.pi*epsilon_0*hbar*c)
rows['hydrogen']=dict(reducedMass=mr,bohrRadius=a,energyScaleEV=EH/e,alpha=alpha,magnetonBohrJT=muB)
rows['atomicProblemSolvingScale']=dict(coulombPotentialAtPoint1nmEV=-e/(4*np.pi*epsilon_0*.1e-9),
 frequencyAt500nmHz=c/(500e-9))
rows['figure41.23']=dict(accelerationVoltage=35000,bremsstrahlungMinimumPM=h*c/(e*35000)*1e12)
check('atomic strategy potential scale',rows['atomicProblemSolvingScale']['coulombPotentialAtPoint1nmEV'],-14.3996,rtol=1e-5)
check('hydrogen scale',EH/e,13.5983,rtol=1e-5)
check('radius',a,5.29465e-11,rtol=1e-5,atol=1e-16)
check('1s radial norm',quad(lambda u:4*u*u*np.exp(-2*u),0,np.inf)[0],1)
check('radial vs volume density maximum',quad(lambda u:4*u*u*np.exp(-2*u),0,1)[0],1-5*np.exp(-2))
radial1s5=4*5**2*np.exp(-10)
radial2p5=5**4*np.exp(-5)/24
assert radial2p5>radial1s5
outer2s=3+np.sqrt(5)
assert outer2s!=4
def dP2s(u):
    return np.exp(-u)/8*(2*u*(2-u)**2-2*u*u*(2-u)-u*u*(2-u)**2)
check('2s outer radial extremum',dP2s(outer2s),0,atol=5e-15)
rows['selfcheck41.3']=dict(radial1sAt5a=radial1s5,radial2pAt5a=radial2p5,
 angularIntegrated2pIndependentOfM=True,outer2sPeakInA=outer2s,
 sourceOvergeneralization='r=n²a applies to circular states, not everyl')

levels=collections.defaultdict(list)
for state in itertools.product(range(1,8),repeat=3):levels[sum(n*n for n in state)].append(state)
first=sorted(levels)[:5]
check('first box sums',first,[3,6,9,11,12])
check('first orbital degeneracies',[len(levels[n]) for n in first],[1,3,3,3,1])
check('titanium22 occupancy',2*sum(len(levels[n]) for n in first),22)
for n in range(1,9):
    orbital=[(l,ml) for l in range(n) for ml in range(-l,l+1)]
    full=[(l,ml,ms) for l,ml in orbital for ms in [-.5,.5]]
    check('orbital count'+str(n),len(orbital),n*n)
    check('withspin count'+str(n),len(full),2*n*n)
rows['box']=dict(firstEnergySums=first,orbitalDegeneracies=[len(levels[n]) for n in first])

# Singlet norm, exchange sign, no-signalling and opposite-axis results.
up=np.array([1.,0.]);down=np.array([0.,1.])
singlet=(np.kron(up,down)-np.kron(down,up))/np.sqrt(2)
check('singlet norm',np.vdot(singlet,singlet),1)
check('exchange parity',singlet.reshape(2,2).T,-singlet.reshape(2,2))
sigma=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
for i,s in enumerate(sigma):
    check('singlet same-axis correlation'+str(i),np.vdot(singlet,np.kron(s,s)@singlet),-1)
check('reduced density',singlet.reshape(2,2)@singlet.reshape(2,2).conj().T,np.eye(2)/2)
rows['entanglement']=dict(singleParticleDensity=[[.5,0],[0,.5]],sameAxisCorrelation=-1)

# Original teaching examples, not substitute sodium3p/3d examples.
g=2.00232
spinMu=g*muB/2
lambda1=588.995e-9
lambda2=589.592e-9
deltaE7=h*c*(1/lambda1-1/lambda2)
B7=deltaE7/(2*spinMu)
check('source41.7 field',B7,18.3902157843,rtol=1e-9)
rows['example41.7']=dict(wavelengthsNM=[lambda1*1e9,lambda2*1e9],
 deltaEV=deltaE7/e,effectiveB=B7,printedB=18.0,
 sourceSignNote='Shorter wavelength has larger photon energy. Printed18.0T is arithmetically inconsistent with the source inputs.')
def fine(n,j):
    return -13.60/n**2*(1+alpha**2/n**2*(n/(j+.5)-.75))
e23=fine(2,1.5);e21=fine(2,.5);e11=fine(1,.5)
photons=np.array([e23-e11,e21-e11])
check('source41.8 splitting',e23-e21,4.53e-5,rtol=.002)
assert e23>e21 and photons[0]>photons[1]
lambdaExact=h*c/e/photons
assert lambdaExact[0]<lambdaExact[1]
deltaLambdaApprox=(121.6e-9/10.20)*(e23-e21)
check('source41.8 wavelength split',deltaLambdaApprox,5.40e-13,rtol=.003,atol=1e-17)
rows['example41.8']=dict(stateEnergiesEV=[e23,e21],groundEV=e11,photonEnergiesEV=photons.tolist(),
 wavelengthSplitM=deltaLambdaApprox,largerWavelengthInitialJ=.5)
zSodium3s=3*np.sqrt(5.138/13.6)
check('source41.9 sodium3s',zSodium3s,1.844,rtol=.001)
rows['example41.9']=dict(state='sodium3s',energyEV=-5.138,effectiveZ=zSodium3s)
rows['example41.10']=dict(atom='potassium',state='4f',estimateEV=-13.6/16,
 comparedMeasuredEV=dict(f=-.85,d=-.94,p=-2.73,s=-4.339),
 magnesiumIon3dEV=-4*13.6/9)
rows['41.34']=dict(states=['4s','4p','4d'],energyEV=[-4.339,-2.73,-.94],
 effectiveZ=(4*np.sqrt(np.array([4.339,2.73,.94])/13.6)).tolist())
check('source41.10 potassium4f',rows['example41.10']['estimateEV'],-.85)
check('source41.10 Mg+3d',rows['example41.10']['magnesiumIon3dEV'],-6.04444444444)
rows['selfcheck41.7']=dict(temperature='high',occupiedN=[1,2,3],
 ionizationThresholdEV=[13.6/n**2 for n in [1,2,3]],answer='all-three')
product=(np.kron(up,up)+np.kron(up,down))/np.sqrt(2)
check('selfcheck41.8 normalization',np.vdot(product,product),1)
check('selfcheck41.8 factorization',product,np.kron(up,(up+down)/np.sqrt(2)))
check('selfcheck41.8 one-particle rank',np.linalg.matrix_rank(product.reshape(2,2)),1)
baseEnergy=h*c/(600e-9)/e
shift=muB*2/e
lambdaZeeman=h*c/e/(baseEnergy+np.array([shift,0,-shift]))
check('example41.5 Zeeman wavelengths',lambdaZeeman*1e9,[599.966,600,600.034],rtol=2e-6)
rows['example41.5']=dict(fieldT=2,wavelengthNM=600,energyShiftsEV=[-shift,0,shift],
 wavelengthsNM=(lambdaZeeman*1e9).tolist())

# Source bridging problem. Distinguish continuum/Bohr values from the model.
radiusTi=1.47e-10
boxL=(4*np.pi/3)**(1/3)*radiusTi
scale=h*h/(8*m_e*boxL*boxL)
photon=9*scale
moseley=h*2.48e15*(22-1)**2
coulomb=e*e/(4*np.pi*epsilon_0*(boxL/2))
rows['bridge']=dict(side=boxL,occupiedEV=[n*scale/e for n in first],
 photonEV=photon/e,moseleyEV=moseley/e,electronRepulsionEV=coulomb/e)
check('bridgeL',boxL,2.37e-10,rtol=.001,atol=1e-16)
check('bridgePhoton',photon/e,60.3,rtol=.002)
check('bridgeMoseley',moseley/e,4.52e3,rtol=.002)

# Actual inverse-geometry data in41.42, not the substituted Ly=2L problem.
Ax=(2.24-(3.47-2.24)/3)/2
Ay=(3.47-2.24)/3
lengths=h/np.sqrt(8*m_e*e*np.array([Ax,Ay,Ax]))
inverseLevels=collections.defaultdict(list)
for triple in itertools.product(range(1,8),repeat=3):
    value=Ax*(triple[0]**2+triple[2]**2)+Ay*triple[1]**2
    inverseLevels[round(value,10)].append(triple)
firstInverse=sorted(inverseLevels)[:3]
check('41.42 actual lowest energies',firstInverse,[2.24,3.47,4.985])
check('41.42 actual degeneracy including spin',[2*len(inverseLevels[k]) for k in firstInverse],[2,2,4])
rows['41.42']=dict(lengthsNM=(lengths*1e9).tolist(),
 energiesEV=firstInverse,states=[inverseLevels[k] for k in firstInverse],spinDegeneracies=[2,2,4])
rectangularLevels=collections.defaultdict(list)
for triple in itertools.product(range(1,8),repeat=3):
    rectangularLevels[4*triple[0]**2+triple[1]**2+triple[2]**2].append(triple)
four=sorted(rectangularLevels)[:4]
check('41.40 four-level sums',four,[6,9,12,14])
check('41.40 with-spin degeneracies',[2*len(rectangularLevels[k]) for k in four],[2,4,2,4])
scale40=h*h/(8*m_e*(1.2e-9)**2)/e
rows['41.40']=dict(energiesEV=[scale40*k for k in four],
 states=[rectangularLevels[k] for k in four],spinDegeneracies=[2,4,2,4])
slabHalf=quad(lambda x:2*np.sin(np.pi*x)**2,0,.5)[0]
slabQuarter=quad(lambda x:2*np.sin(np.pi*x)**2,.25,.5)[0]
slabFirst=quad(lambda x:2*np.sin(np.pi*x)**2,0,.25)[0]
check('41.43 half-slab',slabHalf,.5)
check('41.43 complementary quarters',slabQuarter+slabFirst,.5)
rows['41.43']=dict(halfSlab=slabHalf,quarterToHalf=slabQuarter,zeroToQuarter=slabFirst)
B55=h*c*(.0462e-9)/((575.050e-9)**2*muB)
silverMass=107.87*1.66053906892e-27
flightTime=.500/375
gradient=1e-3*silverMass/(muB*flightTime**2)
rows['41.55']=dict(wavelengthNM=575.050,separationNM=.0462,fieldT=B55)
rows['41.56']=dict(regionM=.500,speedMS=375,separationM=.001,gradientTM=gradient)
check('41.56 separation reconstruction',muB*gradient/silverMass*flightTime**2,.001)
lam60=np.array([67.09608,67.09761])*1e-6
split60=h*c*(1/lam60[0]-1/lam60[1])
field60=split60/(2*spinMu)
rows['41.60']=dict(sourceWavelengthsUM=(lam60*1e6).tolist(),splitEV=split60/e,
 effectiveFieldT=field60,ratioToExample417=field60/B7,
 note='Use literal printed micrometre givens; do not replace by familiar lithium visible wavelengths.')
# Enumerate all magnetic transition pairs, not merely three final wavelengths.
transition54=[(i,f) for i in range(-2,3) for f in range(-1,2) if abs(f-i)<=1]
check('41.54 transition count',len(transition54),9)
base54=h*c/e/(475.082e-9)
shift54=muB*3.5/e
waves54=h*c/e/(base54+np.array([-1,0,1])*shift54)
rows['41.54']=dict(photonEV=base54,transitions=transition54,
 split3dEV=(-8.5+np.arange(-2,3)*shift54).tolist(),wavelengthsNM=(waves54*1e9).tolist())
# Fine-line bounds using exactly the Δl rule requested by41.53. Also record
# the stricter dipole Δj filter separately so no hidden assumption changes the exercise.
def orbitalJ(n):
    return [(l,j) for l in range(n) for j in sorted(set([abs(l-.5),l+.5]))]
def fineShift(n,j):
    return -13.60*alpha**2/n**4*(n/(j+.5)-.75)
trans53=[dict(initial=initial,final=final,
 shiftEV=fineShift(5,initial[1])-fineShift(2,final[1]))
 for initial in orbitalJ(5) for final in orbitalJ(2) if abs(initial[0]-final[0])==1]
base53=13.60*(1/4-1/25)
def bounds53(transitions):
    minimum=min(transitions,key=lambda t:t['shiftEV'])
    maximum=max(transitions,key=lambda t:t['shiftEV'])
    wavelengthShifts=[-434*t['shiftEV']/base53 for t in [maximum,minimum]]
    return dict(shortest=maximum,longest=minimum,wavelengthShiftsNM=wavelengthShifts,
      totalWidthNM=wavelengthShifts[1]-wavelengthShifts[0])
rows['41.53']=dict(statePairs5=orbitalJ(5),statePairs2=orbitalJ(2),
 levelShifts5EV=[fineShift(5,j) for j in [.5,1.5,2.5,3.5,4.5]],
 levelShifts2EV=[fineShift(2,j) for j in [.5,1.5]],
 specifiedDeltaLOnly=bounds53(trans53),
 withAdditionalDeltaJ=bounds53([t for t in trans53 if abs(t['initial'][1]-t['final'][1])<=1]))

# Data41.63 retains all7actual observed pairs.
B=np.array([.51,.74,1.03,1.52,2.02,2.48,2.97])
lam=np.array([21.4,14.3,10.7,7.14,5.35,4.28,3.57])*1e-3
freq=c/lam
slope,intercept=np.polyfit(B,freq,1)
moment=h*slope/2
gamma=2*moment/hbar
rows['41.63']=dict(slopeHzPerTesla=slope,interceptHz=intercept,momentJT=moment,
 gamma=gamma,ratioToElectronChargeMass=gamma/(e/m_e),
 requestedRatioToEOver2M=gamma/(e/(2*m_e)),points=7)
check('gyro consistency',gamma,2*np.pi*slope)

# Data41.65. Ionic energies are per mole, not individual-particle joules.
n=np.arange(2,8)
ionKJmol=np.array([520.2,495.8,418.8,403.0,375.7,380.0])
ionEV=ionKJmol*1000/Avogadro/e
effective=n*np.sqrt(ionEV/13.6)
assert ionEV[-1]>ionEV[-2]
assert np.all(np.diff(effective)>0)
rows['41.65']=dict(n=n.tolist(),ionEV=ionEV.tolist(),effectiveZ=effective.tolist(),
 ionEnergyFranciumExceedsCaesium=True,effectiveZIncreasesAcrossGivenRows=True)

# Degeneracy41.66: Integral tuples, every axis permutation, both spins.
ground=3
gap1=h*c/(624e-9)
unit=gap1/3
side=h/np.sqrt(8*m_e*unit)
N_final=ground+h*c/(234e-9)/unit
states=levels[int(round(N_final))]
check('41.66 final sum',N_final,11)
rows['41.66']=dict(side=side,energySum=N_final,spatialStates=states,degeneracyWithSpin=2*len(states))
check('41.66 spin-count',2*len(states),6)

# Spin3/2 three-particle antisymmetrization: Exactly6signed permutations.
coeff=np.zeros((4,4,4))
for permutation in itertools.permutations([0,1,2]):
    inversions=sum(permutation[i]>permutation[j] for i in range(3) for j in range(i+1,3))
    coeff[permutation]=(-1)**inversions/np.sqrt(6)
check('41.67 normalization',np.sum(coeff**2),1)
check('41.67 antisymmetry',coeff.swapaxes(0,1),-coeff)
spinBasis=np.array([-.5,.5,-1.5,1.5])
conditional=coeff[1,:,:];weight=np.sum(abs(conditional)**2)
check('41.67 first measurement probability',weight,1/3)
check('41.67 conditional second probability',np.sum(abs(conditional[0,:])**2)/weight,.5)
normalizedAfterA=conditional/np.sqrt(weight)
probabilityB=np.sum(abs(normalizedAfterA)**2,axis=1)
check('41.67 B after A=+1/2',probabilityB,[.5,0,.5,0])
afterC=normalizedAfterA[:,2]
afterC/=np.linalg.norm(afterC)
check('41.67 B after C=-3/2',abs(afterC)**2,[1,0,0,0])
rows['41.67']=dict(nonzeroTerms=int(np.count_nonzero(coeff)),singleOutcomeProbability=weight,
 spinBasis=spinBasis.tolist(),measuredA=.5,probabilityBAfterA=probabilityB.tolist(),
 measuredC=-1.5,probabilityBAfterC=(abs(afterC)**2).tolist())
for N in range(1,12):
    energy=2*sum(k+.5 for k in range(N))
    check('41.68 filled oscillator energy'+str(N),energy,N*N)

# Two-electron Bohr ring model, no replacement by a different approximation.
k=e*e/(4*np.pi*epsilon_0)
rHe=4*(4*np.pi*epsilon_0*hbar*hbar/(m_e*e*e))/7
v=hbar/(m_e*rHe)
F_nucleus=2*k/rHe**2
F_repulsion=k/(2*rHe)**2
check('41.69 force balance',m_e*v*v/rHe,F_nucleus-F_repulsion)
kinetic=m_e*v*v;potential=-4*k/rHe+k/(2*rHe)
total=kinetic+potential
check('41.69 virial',potential,-2*kinetic)
rows['41.69']=dict(radius=rHe,speed=v,kineticEV=kinetic/e,potentialEV=potential/e,
 totalEV=total/e,removeBothEV=-total/e,observedRemoveBothEV=79.0)
rows['MCAT']=dict(nAtRadius1um=np.sqrt(1e-6/a),
 atomsPerCM3AtSpacing20um=1/(20e-4)**3,orbitalMomentumAtL2=np.sqrt(6),
 statesAtN100L2=2*(2*2+1))
check('MCAT density choice',rows['MCAT']['atomsPerCM3AtSpacing20um'],1.25e8)
if __name__=='__main__':
    result=dict(status='passed',scope='Parent source-sensitive checks, not a completion certification',results=rows)
    (QA/'parent-numeric.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))
