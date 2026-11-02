"""Independent calculations for the forthcoming Lecture 03/HW 05 additions.

The source exercises have been read. This verifies numbers and candidate
certificates, not that the lecture or its browser interactions are finished.
"""
from pathlib import Path
import itertools
import json
import math
import numpy as np

report={}
Q=np.diag([1.,2.,1.]);A=np.array([[1.,1.,0.],[0.,1.,1.]]);b=np.array([1.,2.])
M=A@np.linalg.solve(Q,A.T)
nu=-np.linalg.solve(M,b);x=-np.linalg.solve(Q,A.T@nu)
objective=lambda z:float(z@Q@z/2)
dual=lambda v:float(-v@M@v/2-b@v)
assert np.allclose(x,[.25,.75,1.25]) and np.allclose(nu,[-.25,-1.25])
assert np.allclose(A@x,b) and np.allclose(Q@x+A.T@nu,0)
assert np.isclose(objective(x),11/8) and np.isclose(dual(nu),11/8)
assert dual(np.array([0.,-1.]))==1.25 and objective(np.array([0.,1.,1.]))==1.5
report['equality_qp']={'x':x.tolist(),'nu':nu.tolist(),'value':objective(x),'comparison_bracket':[1.25,1.5]}

for t in np.linspace(0,1,31):
    multipliers=np.array([1-t,1-t,t])
    assert np.all(multipliers>=0)
    assert np.allclose(multipliers@np.array([[1,1],[2,1],[3,2]]),[3,2])
report['redundant_lp']={'unique_primal':[1,2],'value':7,'lambda':'(1-t,1-t,t), 0<=t<=1','nonnegativity_multipliers':[0,0]}

def resource(budget):
    if budget<=1:return np.array([budget,0.]),2-budget,np.array([0.,1-budget])
    if budget<=3:return np.array([(budget+1)/2,(budget-1)/2]),(3-budget)/2,np.zeros(2)
    return np.array([2.,1.]),0.,np.zeros(2)

def resource_value(budget):
    point,_,_=resource(budget)
    return float(np.sum((point-[2,1])**2)/2)

for budget in [.1,1,1.5,2,3,4]:
    point,multiplier,mu=resource(budget)
    assert np.allclose(point-[2,1]+multiplier-mu,0)
    assert np.all(point>=0) and point.sum()<=budget+1e-9
    assert np.allclose(mu*point,0) and abs(multiplier*(point.sum()-budget))<1e-9
    for other in np.linspace(.05,4,80):
        assert resource_value(other)>=resource_value(budget)-multiplier*(other-budget)-1e-9
assert np.isclose(resource_value(2.2),.16)
report['resource_sensitivity']={'V(2)':resource_value(2),'V(2.2)':resource_value(2.2),'lower_bound_at_2.2':.15,'thresholds':[1,3]}

design=np.array([[1.,0.],[1.,1.],[1.,2.]])
observations=np.array([0.,0.,2.]);parameters=np.array([-.5,1.])
certificate=np.array([.25,-.5,.25]);residual=design@parameters-observations
assert np.allclose(design.T@certificate,0)
assert np.isclose(np.abs(certificate).sum(),1)
assert np.isclose(certificate@observations,.5)
assert np.isclose(np.max(np.abs(residual)),.5)
assert np.isclose(-certificate@residual,.5)
report['chebyshev']={'w':parameters.tolist(),'residual':residual.tolist(),'nu':certificate.tolist(),'value':.5}

probability=np.array([1.,2.,4.])/7
tau=math.log(7)-1;eta=-math.log(2);levels=np.arange(3)
entropy_objective=float(probability@np.log(probability))
entropy_dual=float(-np.exp(-1-tau-eta*levels).sum()-tau-eta*10/7)
assert np.allclose(np.log(probability)+1+tau+eta*levels,0)
assert np.isclose(probability@levels,10/7)
assert np.isclose(entropy_objective,entropy_dual)
assert -math.log(3)<entropy_objective
report['entropy']={'x':probability.tolist(),'tau':tau,'eta':eta,'primal':entropy_objective,'dual':entropy_dual}

for multiplier in [0,1,3,100]:
    approximations=[math.exp(-s)+multiplier/s**2 for s in [10,100,1000]]
    assert approximations[-1]<=approximations[0]
    assert approximations[-1]>=0
for s in np.linspace(-8,8,101):assert math.exp(-s)+s>=1-1e-12
report['slater_gap']={'at_u_zero':{'p':1,'d':0,'gap':1,'no_finite_kkt_multiplier':True},'equality_reformulation':{'nu':1,'dual':1},'u_positive':{'p':0,'d':0,'primal_attained':False,'dual_lambda':0}}

alpha=np.array([1.,2.,5.]);weights=np.array([2.,1.,2.]);caps=np.array([1.,2.,1.])
def allocation(budget):
    if budget<1:return np.array([budget,0,0]),(2/(1+budget),)*2
    if budget==1:return np.array([1.,0,0]),(.5,1.)
    if budget<1.5:return np.array([1.,budget-1,0]),(1/(budget+1),)*2
    if budget<=3:return np.array([1.,budget/3,2*budget/3-1]),(3/(budget+6),)*2
    return np.array([1.,budget-2,1.]),(1/budget,)*2

def value(budget):return float(-weights@np.log(alpha+allocation(budget)[0]))

water=[]
for budget in [.1,.9,1,1.2,1.5,2,3,3.5,3.9]:
    point,nu_interval=allocation(budget)
    assert np.isclose(point.sum(),budget)
    assert np.all(point>=-1e-9) and np.all(point<=caps+1e-9)
    for multiplier in np.linspace(*nu_interval,5):
        assert np.allclose(np.clip(weights/multiplier-alpha,0,caps),point)
        derivative=multiplier-weights/(alpha+point)
        lam=np.where(point<1e-9,np.maximum(derivative,0),0)
        mu=np.where(point>caps-1e-9,np.maximum(-derivative,0),0)
        assert np.allclose(derivative-lam+mu,0)
        for other in np.linspace(.05,3.95,79):
            assert value(other)>=value(budget)-multiplier*(other-budget)-1e-9
    water.append({'P':budget,'x':point.tolist(),'nu_interval':nu_interval,'value':value(budget)})
h=1e-6
assert np.isclose((value(1)-value(1-h))/h,-1,atol=1e-5)
assert np.isclose((value(1+h)-value(1))/h,-.5,atol=1e-5)
report['weighted_capped_waterfilling']={'cases':water,'thresholds':[1,1.5,3],'only_nondifferentiable_budget':1,'one_sided_derivatives':[-1,-.5]}

adjacency=np.zeros((5,5))
for i in range(5):adjacency[i,(i+1)%5]=adjacency[(i+1)%5,i]=1
integer=[]
for signs in itertools.product([-1,1],repeat=5):
    point=np.array(signs)
    integer.append((float(point@adjacency@point),signs))
best=min(v for v,_ in integer);optimal=[signs for v,signs in integer if v==best]
phi=(1+math.sqrt(5))/2
dual_matrix=adjacency+phi*np.eye(5)
angles=4*math.pi*np.arange(5)/5;vectors=np.column_stack([np.cos(angles),np.sin(angles)])
gram=vectors@vectors.T
assert best==-6 and len(optimal)==10
assert np.linalg.eigvalsh(dual_matrix).min()>-1e-12
assert np.allclose(np.diag(gram),1) and np.linalg.eigvalsh(gram).min()>-1e-12
assert np.isclose(np.trace(adjacency@gram),-5*phi)
assert np.linalg.matrix_rank(gram)==2
for _,signs in integer:
    point=np.array(signs);multipliers=-point*(adjacency@point)
    assert np.allclose((adjacency+np.diag(multipliers))@point,0)
report['cycle_five']={'integer_minimum':best,'optimal_sign_vectors':len(optimal),'SDP_minimum':-5*phi,'QP_duality_gap':best+5*phi,'SDP_rank':2,'max_cut':4,'relaxation_cut_bound':(10+5*phi)/4}

two_P=np.diag([2.,1.]);two_A=np.array([[1.,1.]])
two_nu=-np.linalg.solve(two_A@np.linalg.solve(two_P,two_A.T),[3.])
two_x=-np.linalg.solve(two_P,two_A.T@two_nu)
assert np.allclose(two_x,[1,2]) and np.allclose(two_nu,[-2])
assert np.isclose(two_x@two_P@two_x/2,3)
for s in np.linspace(0,2,41):
    point=np.array([s,4-1.5*s])
    assert min(point)>=0 and point.sum()>=3-1e-9 and 2*point[0]+point[1]>=4-1e-9
    assert np.isclose(3*point[0]+2*point[1],8)
triangle=np.ones((3,3))-np.eye(3)
integer_triangle=[np.array(signs)@triangle@np.array(signs) for signs in itertools.product([-1,1],repeat=3)]
assert min(integer_triangle)==-2
theta=np.arange(3)*2*math.pi/3
triangle_vectors=np.c_[np.cos(theta),np.sin(theta)]
triangle_gram=triangle_vectors@triangle_vectors.T
assert np.allclose(np.linalg.eigvalsh(triangle),[-1,-1,2])
assert np.allclose(np.diag(triangle_gram),1)
assert np.isclose(np.trace(triangle@triangle_gram),-3)
assert np.allclose((triangle+np.eye(3))@triangle_gram,0)
report['new_exercises']={'equality_QP':{'point':two_x.tolist(),'nu':two_nu.tolist(),'value':3},'modified_LP':{'value':8,'all_optima':'(s,4-3s/2), 0<=s<=2'},'triangle':{'integer_QP':-2,'SDP':-3,'gap':1,'max_cut':2,'cut_bound':2.25}}

out=Path('qa/math-ai-visuals/hw05-models-numerical.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print('PASS: eight HW 05 model calculations and certificates; lecture text and browser review still pending.')
