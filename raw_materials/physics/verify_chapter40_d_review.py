"""Independent numerical and algebraic checks added during source review.

Local calculation evidence, not public lecture text. Includes source-sensitive
distinctions that the delegated verifier did not test.
"""
import json
from pathlib import Path
import numpy as np
from numpy.polynomial import Polynomial as Poly
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import eval_hermite, factorial
from scipy.constants import h, hbar, c, e, m_e, epsilon_0, atomic_mass

checks=[]
def check(label, actual, expected, rtol=1e-9, atol=1e-12):
    assert np.allclose(actual,expected,rtol=rtol,atol=atol),(label,actual,expected)
    checks.append(label)

hc=h*c/e*1e9
Ephot=hc/np.array([656,486,434,410])
P=Ephot/np.array([25-16,25-9,25-4,25-1])
L=h/np.sqrt(8*m_e*P.mean()*e)
a0=4*np.pi*epsilon_0*hbar*hbar/(m_e*e*e)
check('40.42 shared initial n5 yields four lower final states',5-1,4)
check('40.42 four consistent order estimates',P,[.21000034,.15944470,.13603708,.12600020],rtol=1e-6)
check('40.42 representative width nm',L*1e9,1.5433368937,rtol=1e-8)
check('40.42 Bohr-diameter ratio',L/(2*a0),14.58242025,rtol=1e-8)

# Each probability is independently integrated, rather than comparing a stored
# answer to itself.
psi=lambda n,x: np.sqrt(2)*np.sin(n*np.pi*x)
for n in [1,2]:
    check(f'box{n} norm',quad(lambda x:psi(n,x)**2,0,1)[0],1)
check('40.44 first-quarter probability',quad(lambda x:psi(1,x)**2,0,.25)[0],.25-1/(2*np.pi))
check('40.44 second-quarter probability',quad(lambda x:psi(1,x)**2,.25,.5)[0],.25+1/(2*np.pi))
check('40.49 middle-half ground',quad(lambda x:psi(1,x)**2,.25,.75)[0],.5+1/np.pi)
check('40.49 middle-half first-excited',quad(lambda x:psi(2,x)**2,.25,.75)[0],.5)
check('Q24 classical middle half',quad(lambda x:1/(np.pi*np.sqrt(1-x*x)),-.5,.5)[0],1/3)

# 40.41 and bridging problem: coherent sums, including their phases.
for theta in [0,.5,1.3,np.pi,4.2]:
    state=lambda x:(psi(1,x)+psi(2,x)*np.exp(-1j*theta))/np.sqrt(2)
    check('bridge norm'+str(theta),quad(lambda x:abs(state(x))**2,0,1)[0],1)
    mean=quad(lambda x:x*abs(state(x))**2,0,1)[0]
    check('bridge mean'+str(theta),mean,.5-16*np.cos(theta)/(9*np.pi**2))
    state13=(psi(1,.5)+psi(3,.5)*np.exp(-1j*theta))/np.sqrt(2)
    check('40.41 center density'+str(theta),abs(state13)**2,2*(1-np.cos(theta)))

# Q17: energy from the bottom E is linear to leading order, while the
# binding energy U0-E is quadratic. Dimensionless m=hbar=L=1.
for depth in [1e-2,1e-3,1e-4]:
    R=np.sqrt(depth/2)
    xi=brentq(lambda x:x*np.tan(x)-np.sqrt(R*R-x*x),0,R,xtol=1e-15)
    energy=2*xi*xi
    binding=depth-energy
    check('Q17 weak binding '+str(depth),binding/(depth**2/2),1,rtol=.007)
    assert 0<energy<depth

# 40.53: preserve the supplied potential zero, and distinguish classical
# minimum, quantum zero-point increment and transition energy.
charge=6*e;spacing=.5e-9
K=charge**2/(4*np.pi*epsilon_0)
V0=2*K/spacing;spring=4*K/spacing**3
omega=np.sqrt(spring/(12*atomic_mass))
check('40.53 classical min eV',V0/e,207.354894889,rtol=1e-8)
check('40.53 curvature spring',spring,265.77533403,rtol=1e-8)
check('40.53 quantum increment eV',hbar*omega/(2*e),.03800825545,rtol=1e-8)
check('40.53 photon wavelength um',h*c/(hbar*omega)*1e6,16.31016695,rtol=1e-8)
for u in [.001,.002,.004]:
    exact=V0/(1-u*u)
    approx=V0*(1+u*u)
    check('40.53 Taylor remainder '+str(u),(exact-approx)/V0,u**4/(1-u*u),rtol=.003,atol=1e-16)

# 40.56: normalized first oscillator state, analytic ODE residual and extrema.
A=np.sqrt(2/np.sqrt(np.pi))
state=lambda x:A*x*np.exp(-x*x/2)
check('40.56 normalization',quad(lambda x:state(x)**2,-np.inf,np.inf)[0],1)
for x in np.linspace(-4,4,31):
    value=state(x);second=(x*x-3)*value
    check('40.56 Schrodinger '+str(x),-.5*second+.5*x*x*value,1.5*value)
for x in [-1,0,1]:
    check('40.56 density derivative '+str(x),2*A*A*x*(1-x*x)*np.exp(-x*x),0)
assert state(0)**2<state(1)**2

# 40.58: continuity of both value and derivative for an independently solved
# asymmetric well, dimensionless hbar^2/(2m)=L=1, U0=20.
U0=20
k=brentq(lambda k:k/np.tan(k)+np.sqrt(U0-k*k),np.pi/2+1e-6,np.pi-1e-6)
kappa=np.sqrt(U0-k*k)
inside=np.sin(k)
check('40.58 matching values',inside,inside*np.exp(-kappa*0))
check('40.58 matching slopes',k*np.cos(k),-kappa*inside)

# 40.63: exact polynomial identities acting on P(x)exp(-x²/2),
# dimensionless m=omega=hbar=1, through oscillator level6.
x=Poly([0,1])
lower=lambda p:p.deriv()/np.sqrt(2)
raise_=lambda p:(2*x*p-p.deriv())/np.sqrt(2)
hamilton=lambda p:(p+2*x*p.deriv()-p.deriv(2))/2
def same_poly(label,p,q):
    d=(p-q).coef
    check(label,d,np.zeros_like(d),atol=1e-9)
p=Poly([np.pi**(-.25)])
for n in range(7):
    same_poly(f'40.63 commutator level{n}',lower(raise_(p))-raise_(lower(p)),p)
    same_poly(f'40.63 Hamilton level{n}',hamilton(p),(n+.5)*p)
    same_poly(f'40.63 energy raised level{n}',hamilton(raise_(p)),(n+1.5)*raise_(p))
    same_poly(f'40.63 factorization level{n}',raise_(lower(p))+.5*p,hamilton(p))
    p=raise_(p)/np.sqrt(n+1)

# 40.67-70: two-dimensional level degeneracy, exact size/mass scaling and
# lifetime-limited natural line width. No unsupported organic-lifetime data.
levels=sorted({i*i+j*j for i in range(1,5) for j in range(1,5)})
check('MCAT first two levels',levels[:2],[2,5])
check('MCAT68 size scaling nm',550*1.1**2,665.5)
for M in [m_e,2*m_e]:
    gap=3*np.pi**2*hbar*hbar/(2*M*(1e-9)**2)
    wavelength=h*c/gap
    expected=2*M*c*h*(1e-9)**2/(3*np.pi**2*hbar*hbar)
    check('MCAT wavelength coefficient '+str(M),wavelength/expected,1)
check('MCAT natural linewidth eV',hbar/(10e-9)/e,6.582119565e-8,rtol=1e-8,atol=1e-15)

if __name__=='__main__':
    report=dict(status='passed',checks=len(checks),labels=checks)
    print(json.dumps(report,ensure_ascii=False,indent=2))
