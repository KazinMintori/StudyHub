"""Check the examples and the degenerate slices in the SDP lesson."""
from fractions import Fraction as F
from itertools import product
from math import pi, sqrt


def determinant(a, b, c):
    return 1 + 2*a*b*c - a*a - b*b - c*c


grid = [F(-1), F(-3, 5), F(0), F(3, 5), F(1)]
for a, b, c in product(grid, repeat=3):
    assert determinant(a, b, c) == (1-a*a)*(1-c*c) - (b-a*c)**2
    if abs(c) == 1:
        assert (determinant(a, b, c) >= 0) == (b == c*a)

assert determinant(F(4, 5), F(7, 25), F(4, 5)) == 0
assert determinant(F(4, 5), F(1), F(4, 5)) == 0
assert determinant(F(3, 5), -1, F(-3, 5)) == 0
assert determinant(F(3, 5), F(7, 25), F(-3, 5)) == 0
assert determinant(F(9, 10), F(-9, 10), F(1, 2)) < 0
assert abs((1.5-sqrt(.25+8*.9**2))/2+.5471121771) < 1e-6
assert round(100*pi*sqrt(1-.8**2)/4, 1) == 47.1

for x, y in [(1, 2), (2, 3), (1, 1)]:
    v1, v2 = -x, 1
    assert v1*v1+2*x*v1*v2+y*v2*v2 == y-x*x

print('Verified correlation intervals, singular slices and quadratic-form witnesses.')
