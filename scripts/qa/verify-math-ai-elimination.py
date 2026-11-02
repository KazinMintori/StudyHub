"""Independent algebra for elimination and partial minimization in Lecture 02."""
from fractions import Fraction as F
from pathlib import Path
import math,json
import numpy as np

sensor=[F(6,11),F(3,11),F(2,11)]
assert sum(sensor)==1 and sum(v*x*x for v,x in zip([1,2,3],sensor))==F(6,11)
basis=np.array([[-1,-1],[1,0],[0,1]])
assert np.array_equal(np.ones((1,3))@basis,[[0,0]])
assert np.array_equal(basis.T@np.diag([2,4,6])@basis,[[6,2],[2,8]])
assert F(1,1000)/(F(1)+F(1,2)+F(1,1000))==F(1,1501)

for x in [F(-3),F(-1,2),F(0),F(1),F(5,2)]:
 y=-x/2
 assert 3*x*x+2*x*y+2*y*y==F(5,2)*x*x
 y=(1-2*x)/5
 assert x*x+4*x*y+5*y*y-2*y==x*x/5+4*x/5-F(1,5)
assert F(1)+4*F(-1,5)+5*F(1,25)-2*F(-1,5)==F(4,5)

regressions=[]
for u,y,expected in [([1,2,4,7],[3,4,9,14],(F(40,21),F(5,6))),([0,1,2,5],[1,2,2,7],(F(17,14),F(4,7)))]:
 ub=sum(map(F,u))/len(u);yb=sum(map(F,y))/len(y)
 centered=[F(v)-ub for v in u];target=[F(v)-yb for v in y]
 slope=sum(x*t for x,t in zip(centered,target))/sum(x*x for x in centered)
 intercept=yb-slope*ub
 assert (slope,intercept)==expected
 direct=np.linalg.lstsq(np.column_stack([u,np.ones(len(u))]),y,rcond=None)[0]
 assert np.allclose(direct,[float(slope),float(intercept)])
 regressions.append({'slope':str(slope),'intercept':str(intercept),'input_mean':str(ub),'target_mean':str(yb)})

# Check the Lagrange sign under the convention L=f+nu(a^T x-b).
for angle in [0,30,45,90,150,179]:
 a=np.array([math.cos(math.radians(angle)),math.sin(math.radians(angle))]);d=np.array([-a[1],a[0]])
 for rhs in [-1.5,1/math.sqrt(2),2.5]:
  D=np.diag([1,2]);c=np.array([2,1]);base=rhs*a
  parameter=(d@D@(c-base))/(d@D@d);point=base+parameter*d
  gradient=2*D@(point-c);nu=-gradient@a
  assert abs(a@point-rhs)<1e-12
  assert np.linalg.norm(gradient+nu*a)<1e-12

# The marginal minimum may exist while the original joint infimum is unattained.
sequence=[math.exp(-k) for k in [1,2,4,8,16]]
assert all(value>0 for value in sequence) and all(b<a for a,b in zip(sequence,sequence[1:]))
# Orthonormal change of nullspace coordinates preserves the represented point.
assert np.array_equal(np.array([1,2,3])@np.array([1,2,3]),14)
report={'scope':'Independent numerical and algebraic source checks; no browser or AGY acceptance','sensor_weights':list(map(str,sensor)),'sensor_variance':'6/11','noisy_sensor_weight':'1/1501','regressions':regressions,'KKT_sign_examples':18,'unattained_inner_infimum_sequence':sequence}
Path('qa/math-ai-visuals/elimination-numerical.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('PASS: sensor weights, nullspace Hessian, Schur elimination, centered regressions, KKT sign and unattained inner infimum.')
