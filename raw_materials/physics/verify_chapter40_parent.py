"""Numerical checks for parent-authored chapter40 opening and sections40.4–6."""
from pathlib import Path
import math,json
import numpy as np
root=Path(__file__).resolve().parents[2]
qa=root/'qa/physics/chapter40'
qa.mkdir(parents=True,exist_ok=True)
h=6.62607015e-34
hb=h/(2*math.pi)
c=299792458.
e=1.602176634e-19
me=9.1093837e-31
rows={}

#40.7: Both precise-constant and explicitly rounded textbook substitutions.
E=2.*e;U=5.*e
G=16*(E/U)*(1-E/U)
kappa=math.sqrt(2*me*(U-E))/hb
values=[]
for L in [1.e-9,.50e-9]:
    approx=G*math.exp(-2*kappa*L)
    exact=1/(1+U*U*math.sinh(kappa*L)**2/(4*E*(U-E)))
    rounded=3.8*math.exp(-2*8.9e9*L)
    assert 0<approx<1
    assert abs(approx/exact-1)<1e-3
    values.append({'widthM':L,'asymptotic':approx,'exactRectangularBarrier':exact,
        'roundedSubstitution':rounded,'relativeApproximationError':abs(approx/exact-1)})
assert values[1]['asymptotic']>values[0]['asymptotic']
rows['40.7']={'G':G,'kappaPerM':kappa,'values':values,
    'preciseWidthHalvingFactor':values[1]['asymptotic']/values[0]['asymptotic']}

#40.8: Sodium oscillator, energy and displacement are source data.
mass=3.82e-26
deltaU=.0075*e
displacement=.014e-9
spring=2*deltaU/displacement**2
omega=math.sqrt(spring/mass)
spacing=hb*omega
photonWavelength=h*c/spacing
assert math.isclose(.5*spring*displacement**2,deltaU,rel_tol=1e-12)
assert math.isclose(spacing,h*omega/(2*math.pi),rel_tol=1e-12)
rows['40.8']={'springNPerM':spring,'omegaRadPerS':omega,'spacingEV':spacing/e,'photonWavelengthM':photonWavelength}

# Gaussian normalization, exact Schrödinger residual and uncertainty product.
alpha=mass*omega/hb
normalizer=(alpha/math.pi)**.25
x=np.linspace(-10/math.sqrt(alpha),10/math.sqrt(alpha),200001)
psi=normalizer*np.exp(-alpha*x*x/2)
second=(alpha*alpha*x*x-alpha)*psi
Hamiltonian=-hb*hb/(2*mass)*second+.5*spring*x*x*psi
assert np.max(np.abs(Hamiltonian-.5*hb*omega*psi))<1e-12*np.max(np.abs(Hamiltonian))
probability=psi*psi
assert abs(np.trapezoid(probability,x)-1)<1e-10
positionVariance=float(np.trapezoid(x*x*probability,x))
momentumVariance=float(np.trapezoid((-alpha*x*psi)**2,x))*hb*hb
assert math.isclose(math.sqrt(positionVariance*momentumVariance),hb/2,rel_tol=1e-10)
rows['oscillatorGround']={'normalizer':normalizer,'positionSDM':math.sqrt(positionVariance),
    'momentumSDKgMPerS':math.sqrt(momentumVariance),'uncertaintyProduct':math.sqrt(positionVariance*momentumVariance)}
rows['TYU40.5']={'oscillatorGapRatio':1,'hydrogenSecondToFirstGap':(1/4-1/9)/(1-1/4),'boxSecondToFirstGap':5/3,'answer':'ii'}

# Measurement example40.6, light-beam momentum is total energy/c, not photon count.
puckMomentum=.165*1.
photonMomentum=h/500e-9
burstMomentum=100*1./c
minimumElectronMomentum=math.pi*hb/1e-6
assert burstMomentum/puckMomentum<3e-6
rows['measurement']={'puckMomentum':puckMomentum,'visiblePhotonMomentum':photonMomentum,
    '100JDirectedLightMomentum':burstMomentum,'electronGroundMomentumScale':minimumElectronMomentum}

# Source's two-counterpropagating-component picture is local to the box interval.
# A sine confined to a finite interval is not a global momentum eigenstate with only two deltas.
L=1.
n=1
grid=np.linspace(-10,10,2**16,endpoint=False)
inside=(grid>0)&(grid<L)
state=np.where(inside,np.sqrt(2/L)*np.sin(n*math.pi*grid/L),0.)
dk=grid[1]-grid[0]
momentum=np.fft.fftshift(np.fft.fftfreq(grid.size,d=dk))*2*math.pi
phi=np.fft.fftshift(np.fft.fft(state))
density=abs(phi)**2
density/=np.trapezoid(density,momentum)
mean=float(np.trapezoid(momentum*density,momentum))
variance=float(np.trapezoid(momentum**2*density,momentum))
assert abs(mean)<1e-8
assert abs(variance-(math.pi/L)**2)<.01
assert density[np.argmin(abs(momentum))]>0
rows['boxMomentumCaution']={'globalFourierMeanWithHbarOne':mean,'variance':variance,
    'distributionIsContinuousNotTwoDeltaPeaks':True,'twoModeCollapseRequiresAnExplicitMeasurementModel':True}
(qa/'parent-numeric.json').write_text(json.dumps({'status':'passed','results':rows},indent=2),encoding='utf-8')
print(json.dumps(rows,indent=2))
