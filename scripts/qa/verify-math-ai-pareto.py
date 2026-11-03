"""Independent certificates and arithmetic for the multiobjective lesson."""
from fractions import Fraction as F
from itertools import product
from math import sqrt

A = [[F(x) for x in row] for row in [(1,2),(2,1),(1,1),(3,1)]]
b = [F(x) for x in (3,1,2,4)]
H = [[sum(row[i]*row[j] for row in A) for j in (0,1)] for i in (0,1)]
g = [sum(row[i]*target for row,target in zip(A,b)) for i in (0,1)]
assert H == [[15,8],[8,7]] and g == [19,13]
error = lambda point: sum((sum(row[i]*point[i] for i in (0,1))-target)**2 for row,target in zip(A,b))
def ridge(penalty):
    first,second=15+penalty,7+penalty
    determinant=first*second-64
    return [(19*second-104)/determinant,(13*first-152)/determinant]
assert ridge(F(0)) == [F(29,41),F(43,41)]
assert error(ridge(F(0))) == F(120,41)
assert ridge(F(1)) == [F(3,4),F(7,8)]
assert error(ridge(F(1))) == F(195,64)
for penalty in map(F,(0,1,10)):
    point=ridge(penalty)
    assert all(sum(H[i][j]*point[j] for j in (0,1))+penalty*point[i]==g[i] for i in (0,1))

for penalty in [F(0),F(1),F(12),F(86,7),F(20),F(38),F(100)]:
    point=[(29+penalty/2)/41,(43-F(7,2)*penalty)/41] if penalty<=F(86,7) else [max(F(0),(19-penalty/2)/15),F(0)]
    gradient=[2*(sum(H[i][j]*point[j] for j in (0,1))-g[i]) for i in (0,1)]
    for value,derivative in zip(point,gradient):
        assert derivative+penalty==0 if value>0 else abs(derivative)<=penalty

# The least-squares estimator plus a nonzero null-space perturbation.
inverse=[[F(7,41),F(-8,41)],[F(-8,41),F(15,41)]]
estimator=[[sum(inverse[i][j]*A[k][j] for j in (0,1)) for k in range(4)] for i in (0,1)]
delta=[[F(1),F(1),F(-3),F(0)],[F(0)]*4]
assert all(sum(delta[i][k]*A[k][j] for k in range(4))==0 for i,j in product((0,1),repeat=2))
modified=[[estimator[i][k]+delta[i][k] for k in range(4)] for i in (0,1)]
for i,j in product((0,1),repeat=2):
    assert sum(modified[i][k]*modified[j][k]-estimator[i][k]*estimator[j][k] for k in range(4))==sum(delta[i][k]*delta[j][k] for k in range(4))

plans=[(1,7,5),(3,4,4),(5,3,6),(7,1,3),(4,6,8),(2,8,7),(6,5,1),(1,9,9)]
for dimension,expected in [(2,[0,1,2,3]),(3,[0,1,2,3,6])]:
    front=[i for i,p in enumerate(plans) if not any(all(q[k]<=p[k] for k in range(dimension)) and any(q[k]<p[k] for k in range(dimension)) for q in plans)]
    assert front==expected
assert plans[2][0]==F(plans[1][0]+plans[3][0],2)
assert plans[2][1]-F(plans[1][1]+plans[3][1],2)==F(1,2)
for w in map(F,(0,1,2)):
    assert 5*(w-2)**2+5*w*w==10*(w-1)**2+10
assert (0-3)**2-(1-3)**2==5
assert F(6,100)/F(48,1000)==F(5,4)
for risk in map(F,(1,5,20)):
    allocation=min(F(1),max(F(0),(F(6,100)/risk+F(8,1000))/F(56,1000)))
    variance=F(28,1000)*allocation**2-F(8,1000)*allocation+F(25,10000)
    assert variance>0
    print('risk',float(risk),'weight A',float(allocation),'return',float(F(4,100)+F(6,100)*allocation),'std',sqrt(variance))
print('Verified ridge/lasso KKT, estimator covariance, Pareto sets, unsupported point, local versus finite tradeoff and portfolio threshold.')
