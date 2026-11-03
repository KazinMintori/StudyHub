"""Numerical and exact checks of the Schur lesson examples."""
from fractions import Fraction as F
from itertools import product
from math import hypot, sqrt

for u, v, c in product([F(-3, 2), F(0), F(7, 10), F(3, 2)],
                       [F(-1), F(0), F(1)],
                       [F(1, 4), F(1, 2), F(1)]):
    assert 2*u*u + 2*u*v + c*v*v == 2*(u + v/2)**2 + (c - F(1, 2))*v*v
    minimizer = -v/2
    assert 2*minimizer**2 + 2*minimizer*v + c*v*v == (c - F(1, 2))*v*v

for epsilon in [0, .3, .8]:
    low, high = .5-epsilon, .5+epsilon
    assert abs(low*high-(.25-epsilon**2)) < 1e-12
    assert all(.5+hypot(x-.5, epsilon) >= high for x in [-1, 0, .5, 1, 2])

# In the 4×4 example, the nontrivial 2×2 restriction has entries 2, √3, 1.4.
assert abs(1.7-sqrt(3.09)+.0578395831) < 1e-7
assert F(3, 2) - 3*F(1, 2) == 0
assert F(7, 5) - 3*F(1, 2) == F(-1, 10)
# A singular leading block A=diag(2,0): B=(1,0) is in its range.
# The completed square remains valid and its residual is C-1/2.
for u1,u2,v in product([F(-1),F(0),F(1)],repeat=3):
    assert 2*u1*u1+2*u1*v+v*v == 2*(u1+v/2)**2+v*v/2
# Moving B to (1,1) violates the range condition; the free u2 gives -infinity.
for distance in (1,10,100):
    u1,u2,v=F(-1,2),-distance,F(1)
    assert 2*u1*u1+2*(u1+u2)*v+v*v == F(1,2)-2*distance
# A(x)=xI has a repeated largest eigenvalue but its parameter derivative is 1.
for x in (F(-1),F(0),F(1)):
    step=F(1,100)
    assert ((x+step)-x)/step == 1
print('Verified completion of the square, eigenvalue minima and the singular boundary.')
