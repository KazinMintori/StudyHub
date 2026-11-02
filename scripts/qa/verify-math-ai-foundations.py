"""Independent numerical checks for the mathematics visual review."""
import json
import math
from pathlib import Path
import numpy as np
from statistics import NormalDist
from fractions import Fraction

a = np.array([1., 2., 3.])
b = np.array([1., 2., 2.])
w = a @ b / (a @ a)
r = a * w - b
assert np.isclose(w, 11 / 14) and np.isclose(a @ r, 0)
assert np.isclose(r @ r / 2, 5 / 28)
for candidate in [0, .2, 11/14, 1., 1.5]:
    for sigma in [.2, .6, 1.2]:
        f = np.sum((a*candidate-b)**2)/2
        log_likelihood = -np.sum((a*candidate-b)**2)/(2*sigma**2)
        optimum_log = -np.sum(r**2)/(2*sigma**2)
        assert np.isclose(log_likelihood-optimum_log, -(f-5/28)/sigma**2)
assert 7 + 2*(7-1) == 19
assert np.isclose((4*0**3), 0) and np.isclose(12*0**2, 0)
for yaw in np.linspace(-45, 45, 19):
    for s in np.linspace(-.5, .5, 11):
        for t in np.linspace(-.5, .5, 11):
            p = np.array([1., 1., 1.]) + s*np.array([-2.,1.,0.]) + t*np.array([-3.,0.,1.])
            assert np.isclose(np.array([1.,2.,3.]) @ p, 6.)
for s in [0, .25, .5, .75, 1]:
    p = np.array([-2.,-1.])+s*np.array([4.,2.])
    margin = min(np.linalg.norm(p-np.array([-2.,-1.])), np.linalg.norm(p-np.array([2.,1.])))
    assert np.isclose(margin, min(s,1-s)*math.sqrt(20))
for p in [[0,0],[.3,-.2],[1,0],[1,-1]]:
    margin = min(1-abs(p[0]), 1-abs(p[1]))
    assert (margin > 0) == (abs(p[0]) < 1 and abs(p[1]) < 1)
for u,v in [(.3,.3),(.8,.4),(1/3,1/3),(-.1,.4)]:
    probabilities=np.array([u,v,1-u-v])
    assert np.isclose(probabilities.sum(),1)
    tetra=np.array([1-u-v-.2,u,v,.2])
    assert np.isclose(tetra.sum(),1)
assert np.linalg.matrix_rank(np.eye(3)[:2]-np.eye(3)[2])==2
assert np.linalg.matrix_rank(np.eye(3))==3
assert 2**50 > 10**15 and 2*50==100

systems = []
for A, rhs in [(np.array([[1., 2.]]), np.array([2.])),
               (np.array([[1., 1., 0.], [0., 1., 1.]]), np.array([2., 4.]))]:
    x = np.linalg.lstsq(A, rhs, rcond=None)[0]
    _, _, v = np.linalg.svd(A, full_matrices=True)
    z = v[-1]
    for t in np.linspace(-2, 2, 81):
        y = x + t * z
        assert np.allclose(A @ y, rhs)
        assert np.isclose(y @ y, x @ x + t * t * (z @ z))
    systems.append({'A': A.tolist(), 'b': rhs.tolist(), 'minimum_norm': x.tolist(), 'squared_norm': float(x @ x)})

for c in [-1, 0, 0.5, 1, 2, 4]:
    for y in np.linspace(-1.2, 1.2, 13):
        x = -y
        q = x*x + 2*x*y + c*y*y
        assert np.isclose(q, (c-1)*y*y)
    for theta in np.linspace(0, math.pi, 37):
        d = np.array([math.cos(theta), math.sin(theta)])
        H = np.array([[2., 2.], [2., 2*c]])
        def f(p): return p[0]**2 + 2*p[0]*p[1] + c*p[1]**2
        h = 1e-3
        finite = (f(h*d) - 2*f([0, 0]) + f(-h*d)) / h**2
        assert np.isclose(finite, d @ H @ d)

H = np.array([[4., 2.], [2., 3.]])
L = np.linalg.cholesky(H)
y = np.linalg.solve(L, [6., 5.])
x = np.linalg.solve(L.T, y)
assert np.allclose(x, [1., 1.])
A_lq=np.array([[1.,1.,0.],[0.,1.,1.]])
Q1,R=np.linalg.qr(A_lq.T,mode='reduced')
L1=R.T
y_lq=np.linalg.solve(L1,[2.,4.])
x_lq=Q1@y_lq
assert Q1.shape==(3,2) and L1.shape==(2,2)
assert np.allclose(A_lq,L1@Q1.T) and np.allclose(Q1.T@Q1,np.eye(2))
assert np.allclose(x_lq,[0,2,2]) and np.allclose(A_lq@x_lq,[2,4])
for u,v,t in [(.4,.3,.8),(.8,0,.8),(0,0,0),(.1,.2,-.2)]:
    matrix=np.array([[(t+u)/math.sqrt(2),v/math.sqrt(2)],[v/math.sqrt(2),(t-u)/math.sqrt(2)]])
    eigen=np.linalg.eigvalsh(matrix)
    assert np.allclose(eigen,[(t-math.hypot(u,v))/math.sqrt(2),(t+math.hypot(u,v))/math.sqrt(2)])
    assert np.isclose(np.sum(matrix**2),u*u+v*v+t*t)

gaussian = []
for s1, s2, rho in [(1, .6, 0), (.3, 1.2, .8), (1.2, .3, -.8)]:
    covariance = np.array([[s1*s1, rho*s1*s2], [rho*s1*s2, s2*s2]])
    for theta in np.linspace(0, 2*math.pi, 37):
        p = np.array([s1*math.cos(theta), s2*(rho*math.cos(theta)+math.sqrt(1-rho*rho)*math.sin(theta))])
        assert np.isclose(p @ np.linalg.solve(covariance, p), 1)
    gaussian.append({'sigma1': s1, 'sigma2': s2, 'rho': rho, 'determinant': float(np.linalg.det(covariance))})
assert np.isclose(100*(1-math.exp(-.5)), 39.3469340287)

report = {'prediction': {'w': w, 'gradient': float(a @ r), 'loss': float(r @ r / 2)}, 'least_norm': systems,
          'cholesky': {'H': H.tolist(), 'L': L.tolist(), 'y': y.tolist(), 'x': x.tolist()},
          'gaussian': gaussian, 'probability_q_le_1': 1-math.exp(-.5), 'status': 'passed'}
design=np.column_stack([np.arange(3),np.ones(3)])
observations=np.array([1.,2.,4.])
fit=np.linalg.lstsq(design,observations,rcond=None)[0]
fit_residual=design@fit-observations
assert np.allclose(fit,[1.5,5/6])
assert np.allclose(fit_residual,[-1/6,1/3,-1/6])
assert np.allclose(design.T@fit_residual,0)
assert np.isclose(fit_residual@fit_residual,1/6)
report['line_fit']={'parameters':fit.tolist(),'residual':fit_residual.tolist(),'squared_error':float(fit_residual@fit_residual)}
duplicate=np.array([[0,1],[1,1],[2,1],[1,1]],dtype=float)
assert np.allclose(np.linalg.lstsq(duplicate,[1,2,4,2],rcond=None)[0],[1.5,.75])
lp_vertices=np.array([[0,0],[4.5,0],[3,3],[0,6]])
assert np.allclose(lp_vertices@np.array([5,4]),[0,22.5,27,24])
assert np.allclose(3*np.array([1,1])+np.array([2,1]),[5,4])
assert np.allclose(np.array([3,1])+np.array([1,2]),[4,3])
data=np.array([1,3,4,12])
assert data.mean()==5
for location in np.linspace(3,4,17):assert np.isclose(np.abs(location-data).sum(),12)
assert np.max(np.abs(6.5-data))==5.5
for weights,margin in [([1,1],2),([1,-1],0)]:
    weights=np.array(weights)
    corners=np.array([[-.5,-.5],[-.5,.5],[.5,-.5],[.5,.5]])
    assert np.isclose(np.min((np.array([2,1])+corners)@weights),margin)
    assert np.isclose(weights@np.array([2,1])-.5*np.abs(weights).sum(),margin)
assert np.isclose(3*math.cos(math.pi/3)+3*math.cos(2*math.pi/3),0)
assert np.isclose(3*math.cos(0)-3*math.cos(0),0)
assert min(3*math.cos(t) for t in np.linspace(-math.pi/3,math.pi/3,501))>1
well_roots=np.roots([4,0,-8,1])
for root in [-1.47299760111403,1.3469974085277738]:
    assert np.min(np.abs(well_roots-root))<1e-12
report['introductory_models']='Verified duplicated observation, LP certificates, three constant fits, robust box margins, trigonometric counterexample and quartic minima.'
resource=[]
for choice in [[0,0],[3,3],[16/5,9/5],[5,0],[.2,4]]:
    choice=np.array(choice);z=np.diag([3,4])@choice;radius=np.linalg.norm(z)
    u=z/radius if radius else np.zeros(2)
    coefficient=np.array([5,5])+np.diag([3,4])@u
    cost=5*choice.sum()+radius;t=37-5*choice.sum()
    matrix=np.array([[t,z[0],z[1]],[z[0],t,0],[z[1],0,t]])
    assert np.isclose(coefficient@choice,cost)
    assert np.allclose(np.linalg.eigvalsh(matrix),[t-radius,t,t+radius])
    if radius: assert np.isclose(u@u,1)
    resource.append({'x':choice.tolist(),'u':u.tolist(),'worst_cost':float(cost),'eigenvalues':np.linalg.eigvalsh(matrix).tolist()})
assert np.isclose(math.hypot(1/3,1/4),5/12)
for total in np.linspace(.01,7,70):
    for fraction in np.linspace(0,1,41):
        choice=total*np.array([fraction,1-fraction])
        assert np.linalg.norm(np.diag([3,4])@choice)>=12*total/5-1e-9
normal=NormalDist();chance=[]
for eta in [.5,.9,.95,.99]:
    quantile=normal.inv_cdf(eta);amount=10/(2+.3*quantile)
    assert np.isclose(normal.cdf((10-2*amount)/(.3*amount)),eta)
    chance.append({'eta':eta,'quantile':quantile,'maximum_amount':amount})
assert np.isclose(chance[2]['maximum_amount'],4.010497737571281)
report['ellipsoid_resource']=resource
report['gaussian_chance_constraint']=chance
ridge=[]
for gamma in [0,5,1000]:
    parameter=10/(5+gamma);f1=5*(parameter-2)**2;f2=parameter**2
    assert np.isclose(f1+gamma*f2,20*gamma/(5+gamma))
    assert np.isclose((10+2*gamma)*parameter-20,0)
    ridge.append({'gamma':gamma,'w':parameter,'F1':f1,'F2':f2})
report['ridge_pareto']=ridge
gp=[]
rng=np.random.default_rng(0)
for n in range(2,7):
    costs=2.**np.arange(n);threshold=np.prod(costs)**(1/n)
    for a_bound in [.25,1,2,8]:
        first=max(a_bound,threshold)
        common=(np.prod(costs[1:])/first)**(1/(n-1))
        point=np.r_[first,common/costs[1:]]
        value=costs@point
        assert np.isclose(np.prod(point),1) and point[0]>=a_bound
        for _ in range(100):
            delta=rng.uniform(-1,1,n);delta-=delta.mean()
            trial=point*np.exp(delta)
            if trial[0]>=a_bound:assert costs@trial>=value-1e-9
        gp.append({'n':n,'a':a_bound,'point':point.tolist(),'cost':float(value)})
assert np.isclose(gp[4]['cost'],6)
assert np.isclose(gp[7]['cost'],10)
report['parameterized_gp']=gp
lo,hi=Fraction(1,2),Fraction(3,2);steps=[]
for step in range(4):
    tau=(lo+hi)/2
    left=max(Fraction(0),(3-tau)/(2+tau));right=min(Fraction(1),(2*tau-1)/(2-tau))
    feasible=left<=right
    if feasible:hi=tau
    else:lo=tau
    steps.append({'tau':str(tau),'lower':str(left),'upper':str(right),'feasible':feasible,'bracket':[str(lo),str(hi)]})
assert (lo,hi)==(Fraction(7,8),Fraction(15,16))
assert Fraction(28,29)-(Fraction(13,14)+1)/2==Fraction(1,812)
solution=(math.sqrt(6)-1)/2;level=2*math.sqrt(6)-4
assert np.isclose((2*solution+1)/(solution+2),level)
assert np.isclose((3-2*solution)/(solution+1),level)
report['minimax_ratio']={'steps':steps,'s_star':solution,'value':level,'nonconvex_midpoint_gap':'1/812'}
out = Path('qa/math-ai-visuals/lecture00-numerical.json')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print('PASS: foundations, geometry, ellipsoid resource, Gaussian probabilities, ridge Pareto, minimax and parameterized GP')
