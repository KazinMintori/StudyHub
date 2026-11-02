"""Independent numerical and exact certificates for all LP-model examples."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from math import sqrt
import json,numpy as np

r=6-2*sqrt(5);center=np.array([r,r])
A=np.array([[-1,0],[0,-1],[1,2],[3,1],[-1,1]]);b=np.array([0,0,8,12,3])
slacks=b-A@center-r*np.linalg.norm(A,axis=1)
assert np.allclose(slacks[:3],0) and min(slacks[3:])>0
# A dual nonnegative combination bounds every feasible radius by r.
weights=np.array([1,2,1])/(3+sqrt(5))
assert np.allclose(weights@A[:3],0)
assert np.isclose(weights@np.linalg.norm(A[:3],axis=1),1)
assert np.isclose(weights@b[:3],r)
V=[(F(0),F(0)),(F(4),F(0)),(F(16,5),F(12,5)),(F(2,3),F(11,3)),(F(0),F(3))]
area=F(0);xx=F(0);yy=F(0)
for p,q in zip(V,V[1:]+V[:1]):
 cross=p[0]*q[1]-q[0]*p[1];area+=cross;xx+=(p[0]+q[0])*cross;yy+=(p[1]+q[1])*cross
centroid=[xx/(3*area),yy/(3*area)]
assert centroid==[F(12334,7335),F(11008,7335)]
for t in [1,1.5,2,3]:
 assert min(t,4-t,1,2-1)==1
# Piecewise-linear 1D and 2D minima have a convex-combination certificate.
for x in [F(i,6) for i in range(-12,31)]:
 pieces=[3-x,x/2,2*x-5]
 assert max(pieces)>=(pieces[0]+2*pieces[1])/3==1
for x,y in product([F(i,3) for i in range(-3,10)],repeat=2):
 pieces=[x+y-2,-x,-y]
 assert max(pieces)>=sum(pieces)/3==F(-2,3)
assert [F(2,3)+F(2,3)-2,-F(2,3),-F(2,3)]==[F(-2,3)]*3
# Pointwise polynomial majorant on the exact allowed support.
for k in range(5):assert F(k*(k-1),6)>=int(k>=3)
assert (F(2)-F(1))/6==F(1,6)
probabilities=[]
for s,t in [(F(0),F(0)),(F(1,6),F(0)),(F(0),F(1,12)),(F(1,12),F(1,48))]:
 p=[F(1,2)-s-3*t,3*s+8*t,F(1,2)-3*s-6*t,s,t]
 assert min(p)>=0 and sum(p)==1
 assert sum(i*v for i,v in enumerate(p))==1
 assert sum(i*i*v for i,v in enumerate(p))==2
 assert 0<=p[3]+p[4]<=F(1,6)
 probabilities.append(list(map(str,p)))
assert F(4,5)*F(1,2)+F(1,5)*3==1
assert F(4,5)*F(1,4)+F(1,5)*9==2
assert F(3,4)+F(1,4)==1
assert [F(3,5),F(3,10),F(1,10)]==[1-F(3,10)-F(1,10),F(1,2)-2*F(1,10),F(1,10)]
# Two periods, exact terminal inventory zero: q2=5-q1.
costs={q:F(q)+3*(5-q)+F(1,2)*(q-2) for q in [2,3,4]}
assert costs[4]==8 and costs[2]==11
report={'scope':'Independent arithmetic and optimality certificates; not browser QA','Chebyshev_radius':r,'Chebyshev_slacks':slacks.tolist(),'centroid':list(map(str,centroid)),'moment_distributions':probabilities,'moment_tail_bound':'1/6','period_costs':{str(k):str(v) for k,v in costs.items()}}
Path('qa/math-ai-visuals/lp-models-numerical.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('PASS: Chebyshev dual bound, centroid, piecewise-affine minima, finite-support probability bounds and two-period costs.')
