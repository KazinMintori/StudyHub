"""Independent exact proofs/numbers for the quadratic-program article and Labs."""
from fractions import Fraction as F
from itertools import product
from math import sqrt

data=[(F(i),F(y)) for i,y in [(1,'2'),(2,'3.5'),(3,'5.5'),(4,'7')]]
for a in map(F,('0','.5','1','1.7','2.2')):
 b=F(9,2)-F(5,2)*a
 residual=sum((a*u+b-y)**2 for u,y in data)
 assert residual==5*(a-F(17,10))**2+F(1,20)
assert sum((u+2-y)**2 for u,y in data)==F(5,2)
for center in product(map(F,(-1,0,1,3)),repeat=2):
 for rho in map(F,('0','.6','1')):
  clip=lambda v:min(F(2),max(F(0),v))
  candidates=[]
  for bound in map(F,(0,2)):
   candidates.extend([(bound,clip(center[1]-rho*(bound-center[0]))),(clip(center[0]-rho*(bound-center[1])),bound)])
  if all(0<=x<=2 for x in center):candidates.append(center)
  cost=lambda p:(p[0]-center[0])**2+2*rho*(p[0]-center[0])*(p[1]-center[1])+(p[1]-center[1])**2
  point=min(candidates,key=cost)
  gradient=[2*(point[i]-center[i]+rho*(point[1-i]-center[1-i])) for i in (0,1)]
  for x,g in zip(point,gradient):assert (x==0 and g>=0) or (x==2 and g<=0) or (0<x<2 and g==0)
# Coupled metric's edge optimum differs from coordinate clipping.
assert (F(2)-3)**2+F(6,5)*(F(2)-3)*(F(8,5)-1)+(F(8,5)-1)**2==F(16,25)
# Complete the square with P=diag(2,8), q=(-4,8), center=(2,-1).
# Choosing constant r=7,8,9 changes the minimum to -1,0,1 respectively.
for r in (7,8,9):
 for x,y in product(range(-2,4),repeat=2):
  assert x*x+4*y*y-4*x+8*y+r==(x-2)**2+4*(y+1)**2+r-8
 assert 2**2+4*(-1)**2-4*2+8*(-1)+r==r-8
# Nonconvex constraint's feasible midpoint counterexample.
assert (-1)**2>=1 and 1**2>=1 and 0**2<1
# All five-support distributions: k^2 <= 4k gives a sharp variance bound.
for k in range(5):assert k*k<=4*k
for p0,p4 in [(F(1,2),F(1,2)),(F(0),F(0)),(F(3,4),F(1,4)),(F(2,5),F(1,5))]:
 p2=1-p0-p4;mean=2*p2+4*p4;var=4*p2+16*p4-mean**2
 assert 1<=mean<=2 and 0<=var<=4
# Portfolio in squared percentage points: v=280w^2-80w+25.
v=lambda w:225*w*w-30*w*(1-w)+25*(1-w)**2
assert v(F(1,7))==F(135,7) and v(F(1,2))==55
assert 4+6*F(1,7)==F(34,7)
assert F(10)-F(4)==6 and F(21,2)>10
# Box LS counterexample and exact constrained optimum certificate.
A=[(F(1),F(9,10)),(F(9,10),F(1)),(F(1),F(11,10))];b=[F(5,2),F(1,5),F(13,5)]
cost=lambda x:sum((row[0]*x[0]+row[1]*x[1]-y)**2 for row,y in zip(A,b))
assert cost([F(1),F(0)])==F(53,10)
opt=[F(1),F(241,302)]
assert cost(opt)==F(101979,30200)<F(53,10)
grad=[sum(row[i]*(row[0]*opt[0]+row[1]*opt[1]-y) for row,y in zip(A,b)) for i in range(2)]
assert grad==[-F(588,3775),0]
assert (2-3)**2+(0+1)**2==2
assert (3-1)**2+(2-1)**2==5
assert F(3,2)**2+F(1)**2+F(3,5)**2==F(19,10)**2==F(361,100)
# The cut identity used in the hardness explanation holds on every triangle sign pattern.
for signs in product((-1,1),repeat=3):
 edges=[(0,1,1),(1,2,2),(0,2,3)]
 quadratic=sum(weight*(signs[i]-signs[j])**2 for i,j,weight in edges)
 cut=sum(weight for i,j,weight in edges if signs[i]!=signs[j])
 assert quadratic==4*cut
print('Exact checks passed: box KKT, reduced LS, QCQP counterexample, probability bound, portfolio, correlated box LS and exercises. Portfolio standard deviations:',sqrt(F(135,7)),sqrt(55))
