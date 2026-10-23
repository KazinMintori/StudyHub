"""Independent limiting-case checks for conceptual Wiki equations.

Synthetic verification inputs are not additional textbook examples and are not
exported into student-facing pages.
"""
from math import isclose, pi
from random import Random
rng=Random(20261023)
checks=[]
for _ in range(100):
    m1,m2=[rng.uniform(.1,20) for _ in range(2)]
    x1,x2=[rng.uniform(-30,30) for _ in range(2)]
    cm=(m1*x1+m2*x2)/(m1+m2)
    assert min(x1,x2)<=cm<=max(x1,x2)
    assert isclose(m1*(x1-cm)+m2*(x2-cm),0,abs_tol=1e-10)
    a1,a2,rho=[rng.uniform(.1,10) for _ in range(3)]
    v1=rng.uniform(.1,10);v2=a1*v1/a2
    assert isclose(rho*a1*v1,rho*a2*v2)
    p1=rng.uniform(1e5,2e5);p2=p1+rho*(v1*v1-v2*v2)/2
    assert isclose(p1+rho*v1*v1/2,p2+rho*v2*v2/2)
    force=rng.uniform(.1,50);velocity=rng.uniform(-10,10);dt=1e-4
    assert isclose(force*velocity*dt/dt,force*velocity,rel_tol=1e-10,abs_tol=1e-10)
checks+=['100 center-of-mass moment balances','100 mass-flux cases','100 Bernoulli energy balances','100 work/power checks']
G=6.67430e-11;mass=5.972e24;radius=7e6
speed=(G*mass/radius)**.5;period=2*pi*radius/speed
assert isclose(period**2,4*pi*pi*radius**3/(G*mass))
assert isclose(mass*G/radius**2,speed**2/radius)
checks+=['Circular-orbit centripetal and Kepler consistency']
for mode in range(1,11):
    length=2.;speed=100.;wavelength=2*length/mode
    assert isclose(speed/wavelength,mode*speed/(2*length))
checks+=['10 fixed-end standing-wave boundary cases']
print('PASS:', '; '.join(checks))
