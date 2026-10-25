"""Independent calculations for chapter 15.5–15.8; no public writes."""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
from scipy.integrate import quad

HERE = Path(__file__).resolve().parent
results = []

def check(name, actual, expected, *, rel=1e-10, abs_tol=1e-11):
    a = np.asarray(actual, dtype=float)
    e = np.asarray(expected, dtype=float)
    ok = bool(np.allclose(a, e, rtol=rel, atol=abs_tol))
    if not ok:
        raise AssertionError((name, a.tolist(), e.tolist()))
    results.append({'name': name, 'actual': a.tolist(), 'expected': e.tolist()})

def truth(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    results.append({'name': name, 'passed': True})

mu, tension, freq, amp = .250, 36., 2., .075
omega = 2*math.pi*freq
speed = math.sqrt(tension/mu)
k = omega/speed
pmax = math.sqrt(mu*tension)*omega**2*amp**2
pavg = pmax/2
check('15.4.wave-speed', speed, 12.)
check('15.4.maximum-power', pmax, 2.6647931882941267)
check('15.4.average-power', pavg, 1.3323965941470633)
check('15.4.reduced-average-power', pavg*(.0075/.075)**2, .013323965941470634)
check('15.4.amplitude-factor', (.0075/.075)**2, .01)
check('15.4.period', 1/freq, .5)

# Force times transverse velocity and two equivalent mechanical-power forms.
for i, phase in enumerate(np.linspace(-2.3, 3.2, 11)):
    sx = -k*amp*math.sin(phase)
    vt = omega*amp*math.sin(phase)
    force_power = -tension*sx*vt
    check(f'power.derivative-product.{i}', force_power, pmax*math.sin(phase)**2)
    truth(f'power.nonnegative-running-wave.{i}', force_power >= -1e-14)
for i, x in enumerate([-.13, 0., .87, 2.4]):
    integrated = quad(lambda t: pmax*math.sin(k*x-omega*t)**2, 0., 1/freq)[0]*freq
    check(f'power.cycle-integral.{i}', integrated, pavg)

r1, i1, i2 = 15., .250, .010
r2 = r1*math.sqrt(i1/i2)
check('15.5.distance', r2, 75.)
check('15.5.equal-spherical-power', 4*math.pi*r1*r1*i1, 4*math.pi*r2*r2*i2)
check('15.5.intensity-ratio', i1/i2, 25.)
check('15.5.radius-factor', r2/r1, 5.)
rank = [math.sqrt(f)*a*a for f,a in [(10.,1.),(40.,1.),(10.,4.),(20.,2.)]]
check('self15.5.relative-powers', np.array(rank)/rank[0], [1.,2.,16.,4*math.sqrt(2)])
truth('self15.5.order', list(np.argsort(rank)[::-1]+1) == [3,4,2,1])
check('duck.speed-kmh', .7*3.6, 2.52)
check('duck.speed-mph', .7/0.44704, 1.5658554044380815)

def bump(s):
    q = np.asarray(s, dtype=float)
    return np.where(np.abs(q) <= 1., np.cos(math.pi*q/2)**4, 0.)

def pulse1(x,t):
    return bump((np.asarray(x)+3-t)/.5)

def pulse2(x,t):
    return .30*bump((np.asarray(x)-3+t)/1.2)

xgrid = np.linspace(-7,7,14001)
times = [0., 2.6, 3., 3.4, 6.]
for i,t in enumerate(times):
    y1, y2 = pulse1(xgrid,t), pulse2(xgrid,t)
    total = y1+y2
    truth(f'self15.6.nonnegative.{i}', np.min(total) >= 0.)
    check(f'self15.6.linear-sum.{i}', total, y1+y2)
    check(f'self15.6.invariant-maxima.{i}', [np.max(y1),np.max(y2)], [1.,.3])
check('self15.6.coincident-height', pulse1(0.,3.)+pulse2(0.,3.), 1.3)
check('self15.6.separated-total-max', np.max(pulse1(xgrid,0)+pulse2(xgrid,0)), 1.)
check('self15.6.final-shape-translation', pulse1(xgrid,6.), pulse1(xgrid-6.,0.))
check('self15.6.final-shape-translation-left', pulse2(xgrid,6.), pulse2(xgrid+6.,0.))
# Reflection endpoint conditions independently on an arbitrary even pulse.
for i,t in enumerate(np.linspace(-1,1,9)):
    check(f'fixed-end.cancellation.{i}', bump(t)-bump(-t), 0.)
    h=1e-5
    slope = ((bump(h+t)+bump(h-t))-(bump(-h+t)+bump(-h-t)))/(2*h)
    check(f'free-end.zero-slope.{i}', slope, 0., abs_tol=1e-10)

# Exact trigonometric superposition and independent finite-difference PDE checks.
for i,(x,t) in enumerate([(.13,.05),(.44,.19),(.71,.42),(1.1,.65),(-.24,.93)]):
    a, kk, ww = .003, 4.2, 18.3
    incident = -a*math.cos(kk*x+ww*t)
    reflected = a*math.cos(kk*x-ww*t)
    exact = 2*a*math.sin(kk*x)*math.sin(ww*t)
    check(f'standing.superposition.{i}', incident+reflected, exact)
    f = lambda z,s: 2*a*math.sin(kk*z)*math.sin(ww*s)
    h = 1e-4
    dxx = (f(x+h,t)-2*f(x,t)+f(x-h,t))/(h*h)
    dtt = (f(x,t+h)-2*f(x,t)+f(x,t-h))/(h*h)
    check(f'standing.finite-difference-PDE.{i}', dxx, dtt/(ww/kk)**2, rel=1e-6, abs_tol=1e-8)

a, f, v = .000750, 440., 143.
asw = 2*a
ww = 2*math.pi*f
kk = ww/v
lam = v/f
vmax = ww*asw
amax = ww*ww*asw
check('15.6.standing-amplitude-m', asw, .0015)
check('15.6.omega', ww, 2764.601535159018)
check('15.6.wave-number', kk, 19.33287786824488)
check('15.6.wavelength', lam, .325)
check('15.6.nodes', [n*lam/2 for n in range(4)], [0.,.1625,.325,.4875])
check('15.6.antinodes', [(2*n+1)*lam/4 for n in range(3)], [.08125,.24375,.40625])
check('15.6.max-speed', vmax, 4.146902302738527)
check('15.6.max-acceleration', amax, 11464.5324723054)
check('15.6.acceleration-g', amax/9.8, 1169.850252276061)
check('15.6.speed-kmh', vmax*3.6, 14.928848289858697)
check('15.6.speed-mph', vmax/.44704, 9.276356260599783)
for n in range(8):
    check(f'15.6.node-displacement.{n}', math.sin(kk*n*lam/2), 0., abs_tol=1e-13)
    check(f'self15.7.old-node-remains.{n}', math.sin(2*kk*n*lam/2), 0., abs_tol=1e-13)
for n in range(7):
    newx = (n+.5)*lam/2
    check(f'self15.7.added-midpoint-node.{n}', math.sin(2*kk*newx), 0., abs_tol=1e-13)

# A nonzero instantaneous standing-wave flux integrates to zero; local energy
# balance and total energy conservation are separately checked.
tt = 25.
mm = .04
vv = math.sqrt(tt/mm)
LL = 1.7
kn = 3*math.pi/LL
wn = vv*kn
aa = .004
period = 2*math.pi/wn
for i,x in enumerate([.13,.27,.48,1.12]):
    p = lambda t: -tt*(aa*kn*math.cos(kn*x)*math.sin(wn*t))*(aa*wn*math.sin(kn*x)*math.cos(wn*t))
    avg = quad(p,0,period,epsabs=1e-12)[0]/period
    check(f'standing.mean-flux-zero.{i}', avg, 0., abs_tol=1e-11)
    truth(f'standing.instantaneous-flux-not-zero.{i}', abs(p(period/8)) > 1e-8)
    # ∂_t u + ∂_x P = 0 from directly differentiated energy density.
    t = period*.173
    ux_t = mm*aa*aa*wn**3*(math.cos(kn*x)**2-math.sin(kn*x)**2)*math.sin(wn*t)*math.cos(wn*t)
    px = -tt*aa*aa*kn*kn*wn*math.cos(2*kn*x)*math.sin(wn*t)*math.cos(wn*t)
    check(f'standing.local-energy-balance.{i}', ux_t+px, 0., abs_tol=1e-12)
energies=[]
for t in np.linspace(0,period,9):
    energy=quad(lambda x: .5*mm*(aa*wn*math.sin(kn*x)*math.cos(wn*t))**2+.5*tt*(aa*kn*math.cos(kn*x)*math.sin(wn*t))**2,0,LL)[0]
    energies.append(energy)
check('standing.conserved-total-energy', energies, [energies[0]]*len(energies))

LL, mm, f1 = 5., .0400, 20.
F = 4*mm*LL*LL*f1*f1
check('15.7.tension-N', F, 1600.)
check('15.7.tension-lbf', F/4.4482216152605, 359.6943089595368)
check('15.7.second-harmonic', [2*f1,2*LL/2], [40.,5.])
check('15.7.second-overtone', [3*f1,2*LL/3], [60.,10/3])
check('15.8.sound-wavelength', 344./f1, 17.2)
check('15.8.string-wavelength', 2*LL, 10.)
check('15.8.string-speed', 2*LL*f1, 200.)
check('15.8.ratio', (344./f1)/(2*LL), 1.72)
for n in range(1,13):
    wave_n = n*math.pi/LL
    check(f'mode.right-fixed-end.{n}', math.sin(wave_n*LL), 0., abs_tol=2e-14)
    check(f'mode.left-fixed-end.{n}', math.sin(wave_n*0.), 0.)
    mid = math.sin(n*math.pi/2)
    if n % 2 == 0:
        check(f'self15.8.even-midpoint-node.{n}', mid, 0., abs_tol=2e-14)
    else:
        check(f'self15.8.odd-midpoint-antinode.{n}', abs(mid), 1.)

# Fourier coefficients from integration of the actual triangular initial shape,
# not an assumed normalization of the first component by the triangle's peak.
def triangle(x):
    return 4*x if x <= .25 else (1-x)/.75
b=[]
for n in range(1,9):
    bn=2*(quad(lambda x: triangle(x)*math.sin(n*math.pi*x),0,.25)[0]+quad(lambda x: triangle(x)*math.sin(n*math.pi*x),.25,1.)[0])
    b.append(bn)
check('Fourier.triangle-b2-b1', b[1]/b[0], 1/(2*math.sqrt(2)))
check('Fourier.triangle-b3-b1', b[2]/b[0], 1/9)
check('Fourier.triangle-b4', b[3], 0., abs_tol=1e-12)
truth('Fourier.A-not-triangle-peak', not math.isclose(b[0],1.))
check('Fourier.phase-release-zero-velocity', [-n*math.pi*math.sin(0.) for n in range(1,9)], [0.]*8)

out={'status':'passed','checks':len(results),'scope':'Chapter15.5–15.8 examples15.4–8/selfchecks15.5–8 plus numerical power integrals, reflection conditions, finite-difference PDE, local/total energy, Fourier coefficients. No browser certification.','examples':{
 '15.4':{'pmax_W':pmax,'pavg_W':pavg,'reduced_pavg_W':pavg/100},
 '15.5':{'r2_m':r2},
 '15.6':{'asw_m':asw,'omega_rad_s':ww,'k_rad_m':kk,'lambda_m':lam,'max_v_m_s':vmax,'max_a_m_s2':amax},
 '15.7':{'F_N':F,'f2_Hz':40.,'lambda2_m':5.,'f3_Hz':60.,'lambda3_m':10/3},
 '15.8':{'f_Hz':20.,'sound_lambda_m':17.2,'string_lambda_m':10.,'ratio':1.72}},'Fourier':{'coefficients_for_unit_peak_triangle':b},'results':results}
print(json.dumps(out,ensure_ascii=False,indent=2))
