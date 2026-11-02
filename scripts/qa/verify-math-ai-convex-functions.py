"""Recompute lecture examples independently from browser/component code."""
from math import exp, log, ceil, acos, pi, isclose
from pathlib import Path
import json
import numpy as np
from fractions import Fraction as F
for x in [F(-3,2),F(0),F(7,3)]:
    for y in [F(-2),F(1,3),F(5)]:
        for t in [F(0),F(1,7),F(1,2),F(1)]:
            assert t*x*x+(1-t)*y*y-(t*x+(1-t)*y)**2 == t*(1-t)*(x-y)**2
assert np.allclose(np.linalg.eigvalsh([[0,1],[1,0]]),[-1,1])
assert min(1**2,1)>(min(0**2,1)+min(2**2,1))/2
assert -1>-4  # Cubic chord on [-2, 0].

report={}
xs=np.arange(1,5,dtype=float)
assert np.isclose(xs.var(),1.25)
values=np.array([2.5,3.5,4])
assert np.isclose(((values-3)**2).mean(),.5)
assert np.isclose(values.var(),7/18)
assert np.isclose((values.mean()-3)**2,1/9)
def bisect_root(fn,a,b):
    fa=fn(a)
    assert fa*fn(b)<0
    for _ in range(70):
        mid=(a+b)/2
        if fa*fn(mid)>0:a=mid;fa=fn(mid)
        else:b=mid
    return (a+b)/2
roots=[bisect_root(lambda v:v*v+exp(v)-3,-2,0),bisect_root(lambda v:v*v+exp(v)-3,0,2)]
assert np.allclose(roots,[-1.6772327085325383,.8344868653087588])
report['sublevel_axis_roots']=roots
report['jensen']={'square':float((xs*xs).mean()-xs.mean()**2),'negative_log':float(-np.log(xs).mean()+log(xs.mean())),'exp':float(np.exp(xs).mean()-exp(xs.mean()))}
assert np.allclose(list(report['jensen'].values()),[1.25,.12177727428716867,9.015262260226928])
q_examples=[]
for a in [.5,.1,.25,0,1]:
    q=np.array([a,1-a]);joint=np.array([.1,.3]);posterior=joint/.4
    nonzero=q>0
    elbo=float((q[nonzero]*np.log(joint[nonzero]/q[nonzero])).sum())
    kl=float((q[nonzero]*np.log(q[nonzero]/posterior[nonzero])).sum())
    assert np.isclose(log(.4)-elbo,kl) and kl>=-1e-12
    q_examples.append({'q':q.tolist(),'elbo':elbo,'kl':kl})
report['ELBO']=q_examples
p=np.array([.5,.3,.2]);q=np.array([.4,.4,.2])
assert np.isclose(-(p*np.log(q)).sum()+(p*np.log(p)).sum(),(p*np.log(p/q)).sum())

A=np.array([[1,2],[2,4],[3,6]],dtype=float);b=np.array([1,2,2])
assert np.allclose(np.linalg.eigvalsh(A.T@A),[0,70])
ridge=np.linalg.solve(A.T@A+np.eye(2),A.T@b)
assert np.allclose(ridge,[11/71,22/71])
assert np.isclose(np.linalg.norm(A@np.array([11/14,0])-b)**2,5/14)
report['collinear_ridge']=ridge.tolist()

for x,y in [(1.,2.),(-1.,.5),(0.,3.)]:
    u=np.array([y,-x])
    H=np.array([[2/y,-2*x/y**2],[-2*x/y**2,2*x*x/y**3]])
    assert np.allclose(H,2*np.outer(u,u)/y**3)
    assert np.allclose(H@np.array([x,y]),[0,0])
    assert np.linalg.eigvalsh(H).min()>-1e-10
assert np.allclose(np.linalg.eigvalsh([[2,3],[3,2]]),[-1,5])
assert np.allclose([acos(.2)/2,pi-acos(.2)/2],[.684719203002283,2.4568734505875103])
for gamma,expected in [(10,35),(100,346)]:
    ratio=((gamma-1)/(gamma+1))**2
    assert ceil(log(1e-6)/log(ratio))==expected
    point=np.array([gamma,1.]);P=np.diag([1,gamma])
    for _ in range(5):
        gradient=P@point;step=(gradient@gradient)/(gradient@P@gradient)
        next_point=point-step*gradient
        assert np.isclose((next_point@P@next_point)/(point@P@point),ratio)
        point=next_point

# Random spatial chords: exact quadratic gap, positive and negative witnesses.
rng=np.random.default_rng(42)
for sign in [1,-1]:
    P=np.diag([1,sign])
    for _ in range(100):
        a,b=rng.uniform(-1.4,1.4,(2,2));theta=rng.uniform()
        z=theta*a+(1-theta)*b
        gap=(theta*(a@P@a)+(1-theta)*(b@P@b)-z@P@z)/2
        assert np.isclose(gap,theta*(1-theta)*((a-b)@P@(a-b))/2)

output=Path('qa/math-ai-visuals/convex-functions-numerical.json')
output.parent.mkdir(parents=True,exist_ok=True)
output.write_text(json.dumps(report,indent=2),encoding='utf-8')
print('PASS: chords, Jensen, ELBO, entropy, sublevels, ridge, Hessians, line-search and spatial quadratic gaps')
