"""Independent exact checks for SOCP examples, certificates and boundary cases."""
from fractions import Fraction as F
from itertools import product
from math import sqrt
from statistics import NormalDist

point = (F(2), F(3, 2))
radius = F(1, 5)
norm = F(5, 2)
assert sum(value**2 for value in point) == norm**2
rows = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1)]
limits = [3, 2, 4, 1, 1]
slacks = [limit - sum(a*x for a, x in zip(row, point)) - radius*norm
          for row, limit in zip(rows, limits)]
assert all(slack >= 0 for slack in slacks)
assert slacks[1] == slacks[2] == 0
gradient = tuple(radius*value/norm for value in point)
first = (gradient[0], 1+gradient[1])
second = (1+gradient[0], 1+gradient[1])
weights = (F(15, 14), F(5, 7))
assert tuple(weights[0]*a + weights[1]*b for a, b in zip(first, second)) == (1, 2)
assert point[0] + 2*point[1] == 5

# Ellipsoid example: a feasible point attains the Cauchy-Schwarz upper bound 5.
optimum = (F(16, 5), F(9, 5))
z = (3*optimum[0], 4*optimum[1])
assert sum(optimum) == 5 and sum(value**2 for value in z) == 144
assert 5*sum(optimum) + 12 == 37
assert z[0]/F(1, 3) == z[1]/F(1, 4)
assert F(1, 3)**2 + F(1, 4)**2 == F(5, 12)**2
assert 3*F(34, 5) + 3*F(41, 5) == 45

# Rotated-cone identity, including zero product and a negative-sum counterexample.
for x1, x2, y, z_value in product(range(-2, 3), range(-2, 3), range(4), range(4)):
    squared_norm = 4*(x1*x1+x2*x2)+(y-z_value)**2
    assert (y+z_value)**2-squared_norm == 4*(y*z_value-x1*x1-x2*x2)
    assert (x1*x1+x2*x2 <= y*z_value) == (squared_norm <= (y+z_value)**2)
assert 1 > -1 and 1**2 <= (-1)**2
assert 0 <= 0*2 and not F(9, 4) <= 0*2

normal = NormalDist()
quantile = normal.inv_cdf(.95)
amount = 10/(2+.3*quantile)
boxes = (sqrt(40+(4*quantile/100)**2)-4*quantile/100)**2
assert abs(amount-4.01050) < 5e-6
assert abs(boxes-39.17638) < 5e-6
assert abs(normal.cdf((10-2*amount)/(.3*amount))-.95) < 1e-12
assert 50*39 + 4*quantile*sqrt(39) <= 2000 < 50*40+4*quantile*sqrt(40)
assert normal.cdf(-1) > .1

# Standard deviations shown by the illustration after normalization of each unit.
for count in range(1, 10):
    common_variance = count*count
    independent_variance = count
    assert common_variance >= independent_variance
assert sqrt(9) == 3 and sqrt(9*9) == 9
print('SOCP checks passed: exact robust certificate, ellipsoid optimum, rotated-cone identity and boundaries, Gaussian quantiles, and variance scaling.')
