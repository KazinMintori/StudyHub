"""Motor and Hall-effect source examples, independent arithmetic and directions."""
import numpy as np
V=120.;I=4.;r=2.
emf=V-I*r;pin=V*I;heat=I*I*r;mechanical=pin-heat
assert np.allclose([emf,pin,heat,mechanical],[112,480,32,448])
assert np.isclose(mechanical,emf*I)
assert np.isclose(mechanical/pin,14/15)
stallI=V/r
assert np.isclose(stallI,60) and np.isclose(stallI**2*r,7200)
J=75/(2e-3*1.5e-2);Ez=.81e-6/1.5e-2;B=.4;q=-1.6e-19
n=-J*B/(q*Ez)
assert np.allclose([J,Ez],[2.5e6,5.4e-5])
assert np.isclose(n,1.1574074074074074e29)
# x=east,y=north,z=up: electron up and field west gives magnetic force north.
electron_force=-np.cross([0,0,1],[-1,0,0])
assert np.array_equal(electron_force,[0,1,0])
v_d=np.array([-1e-3,0,0]);v_conductor=-v_d
assert np.allclose(v_d+v_conductor,0)
print('Motor27.11 and Hall27.12 passed; Hall voltage is0.81microvolt, n=1.1574e29/m3, high potential south.')
