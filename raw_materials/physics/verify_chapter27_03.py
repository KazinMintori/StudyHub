"""Independent arithmetic, flux signs and axis-field shape for section27.3."""
import numpy as np
area=3.0e-4; flux=0.90e-3
field=flux/(area*np.cos(np.pi/3))
assert np.isclose(field,6.0)
assert np.isclose(field*area*np.cos(2*np.pi/3),-flux)
# A uniform field has cancelling flux through opposing faces of a closed box.
B=np.array([.3,-.8,1.2]);areas=[np.array([2.,0,0]),np.array([-2.,0,0]),np.array([0,3.,0]),np.array([0,-3.,0]),np.array([0,0,4.]),np.array([0,0,-4.])]
assert np.isclose(sum(B@a for a in areas),0)
# Normalized on-axis loop field: positive along the axis, largest at x=0.
x=np.array([-10.,-2.,-1.,0.,1.,2.,10.])
b=1/(1+x*x)**1.5
assert np.all(b>0) and np.argmax(b)==3
assert np.all(np.diff(b[:4])>0) and np.all(np.diff(b[3:])<0)
print('Section27.3 passed: B=6.0T, flux sign, zero closed flux, axial strength/direction.')
