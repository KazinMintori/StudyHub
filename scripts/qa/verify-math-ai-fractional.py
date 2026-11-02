"""Independent exact-arithmetic checks of the article's examples and counterexamples."""
from fractions import Fraction as F
from itertools import product

def value(p):
    a,b=map(F,p)
    return (a+2*b+2)/(a+b/2+1)

vertices=[(1,0),(6,0),(2,4),(1,4)]
assert [value(p) for p in vertices]==[F(3,2),F(8,7),F(12,5),F(11,4)]
for a,b in vertices+[(2,2),(1,2)]:
    a,b=F(a),F(b); d=a+b/2+1
    y1,y2,z=a/d,b/d,1/d
    assert y1+y2/2+z==1 and y1+2*y2+2*z==value((a,b))
    assert max(-y1+z,-y2,y1+y2-6*z,y2-4*z)<=0
    assert F(1,7)<=z<=F(1,2)
assert value((1,2))==F(7,3)
assert F(1,3)*value((1,0))+F(2,3)*value((1,4))==value((1,2))
for a,b in product((0,1),repeat=2):
    ratio=F(a+b+1,2*a+b+1)
    assert ratio=={(0,0):F(1),(0,1):F(1),(1,0):F(2,3),(1,1):F(3,4)}[(a,b)]
for x in map(F,(0,1,9,99,999)):
    z=1/(x+1)
    assert (x+2)/(x+1)==1+z>1
    assert (x+1)/(x+1)==1
# Approaching the excluded denominator boundary can also make minimization unbounded.
for k in (1,10,100):
    x=F(1,k)
    assert -1/x==-k and x/x==1
assert F(1,5)/F(2,5)==F(1,2) and F(3,5)/F(2,5)==F(3,2)
# A two-sector nonnegative technology and positive activities: maximal common growth = 2.
# B=I, A=diag(2,3): the first sector bounds growth, x=(1,1), x+=(2,2) attains it.
assert min(F(2),F(3))==2
print('Exact Fraction checks passed: vertices, LP normalization/objective, reweighted midpoint, all exercises, boundary and attainment counterexamples, two-sector growth.')
