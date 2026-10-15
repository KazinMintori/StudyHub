from pathlib import Path
from math import sqrt, pi, exp, isclose
import json
import numpy as np

qa = Path(__file__).resolve().parents[2]/'qa/physics/chapter39'
qa.mkdir(parents=True,exist_ok=True)
h=6.62607015e-34
hb=h/(2*pi)
c=299792458.
e=1.602176634e-19
me=9.1093837e-31
mp=1.67262192369e-27
k=1.380649e-23
result={}

# Source PDF1334,39.1 asks electron and proton at the SAME speed.
v=4.70e6
result['39.1']={'electronWavelengthM':h/(me*v),'protonWavelengthM':h/(mp*v)}
assert isclose(result['39.1']['electronWavelengthM']/result['39.1']['protonWavelengthM'],mp/me)

# Source39.2 fixes wavelength0.20nm; it does not give d0.280nm/theta60deg.
lam=.20e-9
result['39.2']={'photonEnergyEV':h*c/(lam*e),'electronKineticEV':h*h/(2*me*lam*lam*e),
    'alphaKineticEV':h*h/(2*6.64e-27*lam*lam*e)}
assert result['39.2']['photonEnergyEV']>result['39.2']['electronKineticEV']>result['39.2']['alphaKineticEV']

#39.84: Jacobian transformation, positive energy-density peak.
lo,hi=2.,4.
for _ in range(100):
    x=(lo+hi)/2
    if 3-x-3*exp(-x)>0:lo=x
    else:hi=x
x=(lo+hi)/2
assert abs(x-2.8214393721220787)<1e-12
A=4*pi*1.23**2
out=[]
for T in [1000.,5000.]:
    E0=x*k*T
    spectral=lambda E: 2*pi*E**3/(h**3*c**2*np.expm1(E/(k*T)))
    energy=np.linspace(.99*E0,1.01*E0,10001)
    exactBand=float(np.trapezoid(spectral(energy),energy))
    peakBand=float(spectral(E0)*.02*E0)
    assert abs(exactBand/peakBand-1)<5e-5
    # Reverse transformation checked at a nonpeak wavelength as well.
    for En in [E0,.7*E0]:
        wavelength=h*c/En
        byLambda=2*pi*h*c*c/(wavelength**5*np.expm1(h*c/(wavelength*k*T)))
        assert isclose(float(spectral(En)),float(byLambda*h*c/En**2),rel_tol=1e-12)
    P=A*peakBand
    out.append({'T':T,'E0J':E0,'E0EV':E0/e,'spectralPeak':float(spectral(E0)),
        'powerW':P,'currentA':sqrt(P/1000.),'relativeNarrowBandError':abs(exactBand/peakBand-1)})
assert isclose(out[1]['powerW']/out[0]['powerW'],625.,rel_tol=1e-13)
result['39.84']={'peakRoot':x,'results':out}

#39.85: preserve the mass in this actual exercise, not an externally corrected gold mass.
m=6.64e-27
M=1.32e-25
K=5.e6*e
v0=sqrt(2*K/m)
V=2*m*v0/(m+M)
u=(m-M)*v0/(m+M)
fraction=4*m*M/(m+M)**2
assert isclose(m*v0,m*u+M*V,rel_tol=1e-13)
assert isclose(K,.5*m*u*u+.5*M*V*V,rel_tol=1e-13)
assert isclose(.5*M*V*V/K,fraction,rel_tol=1e-13)
requiredClassical=.1*(m+M)/(2*m)
assert requiredClassical>1
# A recoil0.10c itself is NOT prohibited. Construct a valid relativistic elastic solution.
beta=.1
gamma=1/sqrt(1-beta*beta)
eta=gamma*beta/(gamma+1)
massRatio=M/m
projectileGamma=(eta*eta*massRatio+sqrt(1-eta*eta+eta*eta*massRatio*massRatio))/(1-eta*eta)
projectileBeta=sqrt(1-1/projectileGamma**2)
pInitial=sqrt(projectileGamma**2-1) # momentum in mc units
energyInitial=projectileGamma+massRatio # energy in mc^2 units
targetMomentum=massRatio*gamma*beta
targetEnergy=massRatio*gamma
projectileFinalEnergy=energyInitial-targetEnergy
projectileFinalMomentum=pInitial-targetMomentum
assert abs(projectileFinalEnergy**2-projectileFinalMomentum**2-1)<1e-12
assert projectileFinalEnergy>=1
result['39.85']={'givenMassM':M,'VoverCClassical':V/c,'fractionTransferred':fraction,
    'requiredClassicalProjectileSpeedOverC':requiredClassical,
    'relativisticCounterexample':{'initialProjectileBeta':projectileBeta,'initialProjectileGamma':projectileGamma,
        'targetFinalBeta':beta,'energyMomentumMassShellChecked':True}}

#39.86: distinguish a width-sum estimate from standard deviation with specified covariance.
t=sqrt(2*25/9.80)
a=hb*t/(2*.0200)
initial=sqrt(a)
linear=2*initial
uncorrelated=sqrt(2*a)
xs=initial*np.logspace(-3,3,1001)
assert (xs+a/xs).min()>=linear*(1-1e-12)
assert np.sqrt(xs*xs+(a/xs)**2).min()>=uncorrelated*(1-1e-12)
# Covariance term cannot be assumed zero for every free Gaussian. Construct a focused Gaussian.
mass=.0200
focusWidth=initial/10
sigmaP=hb/(2*focusWidth)
sigmaXi2=focusWidth**2+(t*sigmaP/mass)**2
cov=-t*sigmaP**2/mass
assert isclose(sigmaXi2*sigmaP**2-cov**2,(hb/2)**2,rel_tol=1e-9)
sigmaFinal2=sigmaXi2+(t*sigmaP/mass)**2+2*t*cov/mass
assert isclose(sigmaFinal2,focusWidth**2,rel_tol=1e-8)
assert sqrt(sigmaFinal2)<uncorrelated
result['39.86']={'fallTimeS':t,'initialWidthOptM':initial,'sumEstimateOptM':linear,
    'zeroCovarianceFinalSDOptM':uncorrelated,'correlatedCounterexampleFinalSDM':sqrt(sigmaFinal2),
    'requiresPreparationModel':True}

#39.76: source-image unit is microseconds, a thousandfold difference from OCR.
tau=2.e-6
energyWidth=hb/(2*tau)
result['39.76']={'lifetimeS':tau,'photonEnergyEV':3.50,'wavelengthNM':h*c/(3.50*e)*1e9,
    'energyWidthJ':energyWidth,'energyWidthEV':energyWidth/e,'relativeWidth':energyWidth/(3.5*e)}

#39.78–79 explicitly ask for the order-of-magnitude px≈h approximation.
# Dimensionless instances check calculus stationary points, minima and energy partition.
for action in [h, .0663, 1.]:
    for mass, spring, slope in [(1.,1.,1.),(.2,7.,3.),(3.,.4,.2)]:
        x0=(action*action/(mass*spring))**.25
        K0=action*action/(2*mass*x0*x0)
        U0=spring*x0*x0/2
        assert isclose(K0,U0,rel_tol=1e-12)
        assert isclose(K0+U0,action*sqrt(spring/mass),rel_tol=1e-12)
        values=x0*np.logspace(-2,2,1001)
        assert (action*action/(2*mass*values*values)+spring*values*values/2).min()>=(K0+U0)*(1-1e-12)
        x1=(action*action/(mass*slope))**(1/3)
        E1=action*action/(2*mass*x1*x1)+slope*x1
        assert isclose(E1,1.5*(action*action*slope*slope/mass)**(1/3),rel_tol=1e-12)
result['39.78-79']={'sourceApproximation':'p*x approximately h, not hbar','calculusMinimaAndPartitionChecked':True}

#Q39.19: full diffraction distribution, not one-order width, enters Heisenberg.
qrows=[]
grid=np.linspace(-15,15,2**15,endpoint=False)
dx=grid[1]-grid[0]
pgrid=np.fft.fftshift(np.fft.fftfreq(len(grid),d=dx))*2*pi
for count in [2,4,6]:
    centres=3*(np.arange(count)-(count-1)/2)
    psi=sum(np.exp(-(grid-centre)**2/(4*.2**2)) for centre in centres)
    prob=abs(psi)**2
    prob/=np.trapezoid(prob,grid)
    sigmaX=sqrt(float(np.trapezoid(grid*grid*prob,grid)))
    transformed=np.fft.fftshift(np.fft.fft(psi))
    pprob=abs(transformed)**2
    pprob/=np.trapezoid(pprob,pgrid)
    sigmaP=sqrt(float(np.trapezoid(pgrid*pgrid*pprob,pgrid)))
    assert sigmaX*sigmaP>=.5
    qrows.append({'slits':count,'positionSD':sigmaX,'momentumSDWithHbarOne':sigmaP,
        'uncertaintyProduct':sigmaX*sigmaP,'centralOrderAngularScale':2*pi/(3*count)})
assert qrows[-1]['momentumSDWithHbarOne']>.99*qrows[0]['momentumSDWithHbarOne']
result['Q39.19']={'dimensionlessHbar':1,'fullDistributionChecks':qrows}

(qa/'end-critical-parent.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('Independent source/math checks passed for39.1,39.2,39.84–86. Recorded source corrections and stated physical assumptions checked.')
for key in result: print(key,json.dumps(result[key]))
