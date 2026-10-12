"""Recompute the board examples and the added numerical illustrations."""
from fractions import Fraction as F
from itertools import permutations
from math import cos, sin, sqrt


def determinant(a):
    if len(a) == 1:
        return a[0][0]
    return sum((-1) ** j * a[0][j] * determinant([
        row[:j] + row[j + 1:] for row in a[1:]
    ]) for j in range(len(a)))


vertices = [(0, 0), (4, 0), (4, 2), (3, 3), (0, 3)]
values = [-3*x - 2*y for x, y in vertices]
assert values == [0, -12, -16, -15, -6]
assert min(x-y for x, y in [(0, 0), (1, 0), (0, 1)]) == -1
assert -3*6-2*0 == -18

# A small affine regression added to unpack the normal equation.
X = [[F(1), F(t)] for t in [0, 1, 2]]
y = [F(1), F(2), F(2)]
a = [F(7, 6), F(1, 2)]
r = [sum(v*w for v, w in zip(row, a))-yi for row, yi in zip(X, y)]
assert r == [F(1, 6), F(-1, 3), F(1, 6)]
assert all(sum(row[j]*ri for row, ri in zip(X, r)) == 0 for j in range(2))
assert sum(ri*ri for ri in r)/3 == F(1, 18)

for radius in [F(1, 2), F(1), F(2), F(3), F(5)]:
    if radius <= 2:
        x = [radius/2, radius/2, F(0)]
        mu, lam = [F(0), F(0), 1-radius/2], -radius/2
        expected = radius*radius/4
    else:
        x = [(radius+1)/3, (radius+1)/3, (radius-2)/3]
        mu, lam = [F(0)]*3, -(radius+1)/3
        expected = (radius*radius+2*radius-2)/6
    assert sum(x) == radius
    assert all(v >= 0 for v in x+mu)
    assert all(v*m == 0 for v, m in zip(x, mu))
    assert all(x[i] + (i == 2) - mu[i] + lam == 0 for i in range(3))
    assert x[2] + sum(v*v for v in x)/2 == expected

for x in set(permutations([-2, 0, 0])):
    assert sum(v**3 for v in x) == -8
    assert sum(v*v for v in x) == 4 and sum(x) <= 1
    assert all(3*v*v+6*v == 0 for v in x)
assert 3*F(-2, 3)**2 == F(4, 3)
assert 2*F(-2, 3)**2 + 3*F(-2, 3) == F(-10, 9)

for c in [F(-1), F(0), F(1, 2), F(1)]:
    h = [[4-c, F(2), F(1)], [F(2), F(2), F(0)], [F(1), F(0), F(4)]]
    assert determinant(h) == 14-8*c > 0
    assert determinant([row[:2] for row in h[:2]]) == 4-2*c > 0
    for t in [-2, 0, F(1, 3), 3]:
        shifted = [[h[i][j]-(t if i == j else 0) for j in range(3)] for i in range(3)]
        assert determinant(shifted) == -t**3+(10-c)*t**2-(27-6*c)*t+(14-8*c)
for x, y, z in [(-2, 1, 3), (.5, -.5, -.125), (0, 0, 0)]:
    f = 2*x*x+2*x*y+y*y+x*z+2*z*z+cos(x)
    completed = (y+x)**2+2*(z+x/4)**2+7*x*x/8+cos(x)
    assert abs(f-completed) < 1e-12
    assert f >= 1+3*x*x/8+(y+x)**2+2*(z+x/4)**2-1e-12

point = [F(2), F(1)]
trials = []
for iteration in range(2):
    gradient = [2*point[0], 4*point[1]]
    direction = [-v for v in gradient]
    value = point[0]**2+2*point[1]**2
    rate = F(1)
    while True:
        candidate = [v+rate*d for v, d in zip(point, direction)]
        candidate_value = candidate[0]**2+2*candidate[1]**2
        bound = value-F(1, 10)*rate*sum(v*v for v in gradient)
        trials.append((iteration, str(rate), str(candidate_value), str(bound), candidate_value <= bound))
        if candidate_value <= bound:
            break
        rate /= 2
    point = candidate
assert point == [0, 0]
assert trials == [(0, '1', '22', '14/5', False), (0, '1/2', '2', '22/5', True),
                  (1, '1', '18', '2/5', False), (1, '1/2', '2', '6/5', False),
                  (1, '1/4', '0', '8/5', True)]
assert 2**64 == 18446744073709551616
assert 2**100 == 1267650600228229401496703205376
assert sqrt(3**2+(-4)**2) == 5
assert abs(3)+abs(-4) == 7 and max(abs(3), abs(-4)) == 4
assert (2+1)/2 == F(3, 2)
for t in [F(-1), F(0), F(1, 4), F(1, 2), F(1)]:
    assert (2-4*t)**2+2*(1-4*t)**2 == 6-32*t+48*t*t
assert 2*16+4*16 == 96
assert [2-2, 1-1] == [0, 0]
print('All regression, LP, KKT, dual, Hessian, Taylor and line-search calculations passed.')
print('Armijo trials:', trials)
print('2^64 =', 2**64, '; 2^100 =', 2**100)
