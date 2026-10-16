"""Independent checks of sensitive source inputs, boundaries and approximation domains."""
from pathlib import Path
import json,math
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
from scipy.special import eval_hermite
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'qa/physics/chapter40';OUT.mkdir(parents=True,exist_ok=True)
h=6.62607015e-34
hb=h/(2*math.pi)
e=1.602176634e-19
me=9.1093837e-31
c=299792458.
rows={}

def finite_well(L,UeV,m=me):
    U=UeV*e
    R=L*math.sqrt(2*m*U)/(2*hb)
    roots=[]
    # Even/odd roots bracketed separately between poles; no false tangent roots.
    for j in range(int(2*R/math.pi)+1):
        left=j*math.pi/2
        right=min((j+1)*math.pi/2,R)
        if right<=left:continue
        delta=min(1e-10,(right-left)/1e5)
        if j%2==0:
            f=lambda z:z*math.tan(z)-math.sqrt(max(0,R*R-z*z))
        else:
            f=lambda z:-z/math.tan(z)-math.sqrt(max(0,R*R-z*z))
        if f(left+delta)*f(right-delta)>=0:continue
        z=brentq(f,left+delta,right-delta,xtol=1e-14)
        E=2*hb*hb*z*z/(m*L*L)
        assert 0<E<U
        assert abs(f(z))<1e-9
        roots.append(dict(z=z,energyEV=E/e,residual=f(z)))
    return roots

# The printed VP40.6.4 answer 0.010eV is not an empirical 2/3-depth rule.
L=.400e-9;U=.015
weak=finite_well(L,U)
assert len(weak)==1
E=weak[0]['energyEV']
R=L*math.sqrt(2*me*U*e)/(2*hb)
z_claim=L*math.sqrt(2*me*.010*e)/(2*hb)
claim_residual=z_claim*math.tan(z_claim)-math.sqrt(R*R-z_claim*z_claim)
assert abs(claim_residual)>.05
assert .0147<E<.0149
rows['VP40.6.4']=dict(widthNm=.400,depthEV=U,infiniteGroundEV=h*h/(8*me*L*L*e),
    exactGroundEV=E,bindingEV=U-E,rootResidual=weak[0]['residual'],
    printedAnswerEV=.010,printedAnswerBoundaryResidual=claim_residual,
    noJustifiedTwoThirdsDepthApproximation=True)

L=.50e-9;Einfinity=h*h/(8*me*L*L*e)
states=finite_well(L,6*Einfinity)
assert len(states)==3
ratios=[state['energyEV']/Einfinity for state in states]
assert np.allclose(ratios,[.6252691024,2.4346729672,5.0861098462],rtol=1e-9)
rows['sixDepthWell']=dict(ratios=ratios,energyEV=[s['energyEV'] for s in states])

# Independent quadrature of low oscillator states, rather than assuming the
# uncertainty values from the classical amplitudes being compared.
grid=np.linspace(-12,12,200001)
oscillator=[]
for n in range(5):
    normalization=math.pi**(-.25)/math.sqrt(2**n*math.factorial(n))
    gaussian=np.exp(-grid*grid/2)
    hermite=eval_hermite(n,grid)
    derivative_hermite=np.zeros_like(grid) if n==0 else 2*n*eval_hermite(n-1,grid)
    state=normalization*hermite*gaussian
    derivative=normalization*(derivative_hermite-grid*hermite)*gaussian
    norm=float(np.trapezoid(abs(state)**2,grid))
    x2=float(np.trapezoid(grid*grid*abs(state)**2,grid))
    p2=float(np.trapezoid(abs(derivative)**2,grid))
    assert math.isclose(norm,1,rel_tol=1e-12)
    assert math.isclose(x2,n+.5,rel_tol=1e-12)
    assert math.isclose(p2,n+.5,rel_tol=1e-12)
    oscillator.append(dict(n=n,norm=norm,positionVariance=x2,momentumVariance=p2))
rows['40.34OscillatorMomentsHbarMassOmegaOne']=oscillator

# 40.2 and40.3: Periodic density repeats, while an individual maximum travels.
k=1.;w=1.;time=2*math.pi
rho2=lambda x,t:2-2*np.cos(k*x-3*w*t)
rho3=lambda x,t:2+2*np.cos(2*k*x-8*w*t)
assert abs(rho2(math.pi,0)-4)<1e-12
assert abs(rho2(math.pi,time)-4)<1e-12
assert abs(rho2(7*math.pi,time)-4)<1e-12
assert abs(rho3(math.pi,time)-4)<1e-12
assert abs(rho3(8*math.pi,time)-4)<1e-12
rows['movingPeaks']=dict(
    exercise40_2=dict(smallestPositiveAtBothTimes=[math.pi,3*math.pi],trackedFirstFinal=7*math.pi,velocity=3),
    exercise40_3=dict(smallestPositiveFinal=math.pi,trackedOriginFinal=8*math.pi,velocity=4))

# 40.43: Independent flux check for a finite step, E>U0.
flux=[]
for E,U in [(2,1),(5,.2),(5,4.999)]:
    k1=math.sqrt(E);k2=math.sqrt(E-U)
    reflection=(k1-k2)/(k1+k2)
    transmission=2*k1/(k1+k2)
    assert abs(1+reflection-transmission)<1e-12
    assert abs(k1*(1-reflection)-k2*transmission)<1e-12
    R=reflection**2;T=(k2/k1)*transmission**2
    assert abs(R+T-1)<1e-12
    flux.append(dict(E=E,U=U,R=R,T=T))
rows['40.43Flux']=flux

# 40.62: Ring normalization, travelling interference maximum and speed at a0.
theta=np.linspace(0,2*math.pi,200001)
omega=1.;time=.31
psi=(np.exp(1j*theta-1j*omega*time)+np.exp(2j*theta-4j*omega*time))/math.sqrt(4*math.pi)
rho=abs(psi)**2
assert abs(np.trapezoid(rho,theta)-1)<1e-12
assert np.max(abs(rho-(1+np.cos(theta-3*omega*time))/(2*math.pi)))<1e-12
a0=5.291772109e-11
ring_speed=3*hb/(2*me*a0)
rows['40.62']=dict(peakAngularSpeedInOmega=3,bohrRadiusSpeedMPerS=ring_speed)

# 40.60: Fit actual five source observations, including rounded data scatter.
energies=np.array([4.,5.,6.,7.,7.6])
transmissions=np.array([2.4e-6,1.5e-5,1.2e-4,1.3e-3,8.1e-3])
G=16*(energies/8)*(1-energies/8)
kappa=np.sqrt(2*me*(8-energies)*e)/hb
slope,intercept=np.polyfit(kappa,np.log(transmissions/G),1)
width=-slope/2
rows['40.60']=dict(widthNm=width*1e9,intercept=intercept,
    maxLogResidual=float(max(abs(np.log(transmissions/G)-(slope*kappa+intercept)))))
assert .69<width*1e9<.71

# WKB exercises use the supplied nh/2 rule. Compare levels by ordinal rank.
for n in [1,2,5]:
    mass=1.;omega=2.;energy=n*hb*omega
    amplitude=math.sqrt(2*energy/(mass*omega*omega))
    integral=quad(lambda u:math.sqrt(max(0,1-u*u)),-1,1,epsabs=1e-12)[0]*2*energy/omega
    assert math.isclose(integral,n*h/2,rel_tol=1e-10)
    exact_same_rank=(n-.5)*hb*omega
    assert math.isclose(energy-exact_same_rank,.5*hb*omega,rel_tol=1e-12)
rows['40.65']=dict(suppliedRule='integral(p dx)=nh/2, n>=1',
    approximationOverestimatesSameOrdinalRank=True,offsetInHbarOmega=.5)

mass=1.;A=2.;h_unit=1.
levels=[]
for n in range(1,20):
    energy=(3*mass*A*h_unit/4)**(2/3)*n**(2/3)/(2*mass)
    turning=energy/A
    integral=2*quad(lambda x:math.sqrt(2*mass*(energy-A*x)),0,turning)[0]
    assert math.isclose(integral,n*h_unit/2,rel_tol=1e-10)
    levels.append(energy)
assert np.all(np.diff(np.diff(levels))<0)
rows['40.66']=dict(verifiedIntegrals=19,gapsStrictlyDecrease=True)

# Alpha example28 is near the edge of the opaque-barrier approximation.
alpha=6.64e-27
checks=[]
for energyMeV in [29.,20.]:
    energy=energyMeV*1e6*e;U=30e6*e;L=2e-15
    kappa=math.sqrt(2*alpha*(U-energy))/hb
    G=16*(energy/U)*(1-energy/U)
    approximate=G*math.exp(-2*kappa*L)
    exact=1/(1+U*U*math.sinh(kappa*L)**2/(4*energy*(U-energy)))
    checks.append(dict(energyMeV=energyMeV,approximate=approximate,exact=exact,relativeError=approximate/exact-1))
rows['40.28']=checks
(OUT/'critical-numeric.json').write_text(json.dumps(dict(status='passed',results=rows),indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows,indent=2))
