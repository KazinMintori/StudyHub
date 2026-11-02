"""Independent arithmetic and counterexamples for the four geometry topics."""
from fractions import Fraction as F
from pathlib import Path
from math import exp, isclose
import json
import numpy as np

report = {}
def perspective(x):
    return [v / x[-1] for v in x[:-1]]

for x, y, theta in [([1,1],[6,3],F(1,2)),([2,4],[6,1],F(1,3))]:
    x, y = list(map(F,x)), list(map(F,y))
    r = [theta*a+(1-theta)*b for a,b in zip(x,y)]
    mu = theta*x[-1]/r[-1]
    assert perspective(r) == [mu*a+(1-mu)*b for a,b in zip(perspective(x),perspective(y))]
    if theta == F(1,3):
        assert perspective(r) == [F(7,3)] and mu == F(2,3)
    else:
        assert perspective(r) == [F(7,4)] and mu == F(1,4)

for theta in np.linspace(0,1,101):
    for a in [0,.4,1]:
        for b in [0,.5,1]:
            denominator = theta*a+(1-theta)*b
            if denominator:
                probability = (theta*a*.25+(1-theta)*b*.8)/denominator
                mu = theta*a/denominator
                assert isclose(probability,mu*.25+(1-mu)*.8)
                assert .25-1e-12 <= probability <= .8+1e-12
assert (F(1,2)*F(1,10)+F(1,2)*F(4,10))/(F(1,2)*F(4,10)+F(1,2)*F(5,10)) == F(5,9)
report['conditional_example'] = {'posterior':'5/9','new_weight':'4/9','naive':'21/40'}

# A fixed real-size rectangle shrinks by 1/t along each image coordinate.
for depth in np.linspace(1.4,3.6,23):
    corners=np.array([[-.65,-.5],[.65,-.5],[.65,.5],[-.65,.5]])+[.5,.2]
    image=corners/depth
    area=abs(np.dot(image[:,0],np.roll(image[:,1],1))-np.dot(image[:,1],np.roll(image[:,0],1)))/2
    assert isclose(area/(1.3*1),1/depth**2)

# Strict separation with zero infimum distance, unlike uniform separation.
strict_pairs=[2*exp(-u) for u in [0,1,5,10,25]]
assert all(v>0 for v in strict_pairs) and strict_pairs[-1]<1e-9
assert 1/10**10<1e-9
report['separation']={'strict_vertical_gaps':strict_pairs,'strong_distance':1}

# XOR signs for the fixed plane, and its crossing threshold during a lift.
for lift in np.linspace(0,1,21):
    points=np.array([[0,0,0],[1,1,lift],[1,0,0],[0,1,0]])
    scores=points@np.array([1,1,-2])-.5
    assert np.allclose(scores,[-.5,1.5-2*lift,.5,.5])
    assert bool(np.all(scores[:2]<0) and np.all(scores[2:]>0)) == bool(lift>.75)
report['xor_full_scores']=[-.5,-.5,.5,.5]

# Cone witnesses: an arbitrarily small positive coordinate detects a negative
# dual coordinate, although the test vector lies strictly inside the quadrant.
for y in [[-1,2],[3,-.01],[-.02,-3]]:
    i=next(i for i,v in enumerate(y) if v<0)
    epsilon=min(1,-y[i]/(2*(abs(y[1-i])+1)))
    x=np.array([epsilon,epsilon]);x[i]=1
    assert np.all(x>0) and np.dot(x,y)<0
assert np.linalg.eigvalsh(np.array([[1,-1],[-1,1]])).tolist()==[0,2]

def minimal(points):
    return [i for i,x in enumerate(points) if not any(all(a<=b for a,b in zip(y,x)) and y!=x for y in points)]
assert minimal([(3,5),(4,2),(2,6),(5,1),(4,4),(6,6)])==[0,1,2,3]
points=[(2,9),(3,6.5),(5.5,4),(8,3),(6,7),(9,8)]
assert minimal(points)==[0,1,2,3]
choices=[]
for weight,expected in [([1,.2],[0]),([1,1],[1,2]),([.3,1],[3])]:
    costs=np.array(points)@weight
    chosen=np.flatnonzero(np.isclose(costs,min(costs))).tolist()
    assert chosen==expected
    choices.append({'weights':weight,'costs':costs.tolist(),'minimizers':chosen})
report['scalarization']=choices

c=np.array([.8,.6]);d=np.array([2.4,1.8]);normal=d-c
offset=(d@d-c@c)/2
assert np.allclose(normal,[1.6,1.2]) and isclose(offset,4)
assert np.allclose(np.array([[1,1],[-1,0],[0,-1]]).T@np.ones(3),[0,0])

output=Path('qa/math-ai-visuals/perspective-order-numerical.json')
output.parent.mkdir(parents=True,exist_ok=True)
output.write_text(json.dumps(report,indent=2),encoding='utf-8')
print('PASS: perspective, conditional mixtures, R3 area, separation counterexamples, XOR, cones, Pareto exercises and certificates')
