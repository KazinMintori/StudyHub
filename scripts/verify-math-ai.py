"""Recompute authored numbers and execute the Python demonstrations in Notes.
Run from the repository root with a standard-library Python 3 interpreter.
"""
import ast
import json
import math
import re
from fractions import Fraction as F
from pathlib import Path

def close(a, b, eps=1e-9):
    assert abs(a-b)<eps, (a,b)

a,b=[1,2,3],[1,2,2]
loss=lambda w:sum((F(ai)*w-bi)**2 for ai,bi in zip(a,b))/2
assert loss(F(11,14))==F(5,28)
assert loss(F(1,2))==F(3,4) and loss(F(1))==F(1,2)
assert [F(ai)*F(11,14)-bi for ai,bi in zip(a,b)]==[F(-3,14),F(-3,7),F(5,14)]
assert F(3,4)-F(5,28)==F(4,7)
assert F(9,2)-11*F(11,14)+7*F(11,14)**2==F(5,28)
assert F(1,2)*((F(3,2)-2)**2+F(-1,2)**2)==F(1,4)
assert F(1,2)-F(1,2)**2==F(1,4)
for t,value in [(F(1),F(1620)),(F(1,2),F(641,2)),(F(1,4),F(369,8)),(F(1,8),F(89,32))]:
    x,y=2-2*t,2-20*t
    assert (x*x+10*y*y)/2==value
assert (F(4,7)**4+F(4,7)**2)==F(1040,2401)
targets=[0,2]
theta,v=F(0),F(0)
for expected in [F(1,10),F(28,100),F(514,1000)]:
    v=F(9,10)*v-F(1,10)*(theta-1);theta+=v
    assert theta==expected
m1,v1=F(1,5),F(1,250)
m2=F(9,10)*m1+F(1,10)
v2=F(999,1000)*v1+F(1,1000)
assert m2==F(28,100) and v2==F(4996,1000000)
assert m2/(1-F(9,10)**2)==F(28,19)
assert v2/(1-F(999,1000)**2)==F(4996,1999)
close(.1*float(F(28,19))/math.sqrt(float(F(4996,1999))),.093217963907425,
      1e-8)
assert [3*x+2*y for x,y in [(0,0),(2,0),(2,2),(0,4)]]==[0,6,10,8]
assert [3*x+y for x,y in [(1,6),(2,4),(4,2)]]==[9,10,14]
assert [3*x+2*y for x,y in [(1,6),(2,4),(4,2)]]==[15,14,16]
assert [x+3*y for x,y in [(1,6),(2,4),(4,2)]]==[19,14,10]
close(math.sqrt(6/12),1/math.sqrt(2))
assert (F(2,3)+F(3,4)*F(4,9),F(2,3)+F(3,4)*F(-2,9))==(1,F(1,2))
# The remaining small examples, computed independently of the browser model.
def dot(u,v):return sum(a*b for a,b in zip(u,v))
def matvec(matrix,v):return [dot(row,v) for row in matrix]
def transpose(matrix):return list(map(list,zip(*matrix)))
def matmul(a,b):return [[dot(row,col) for col in zip(*b)] for row in a]
A=[[1,2],[0,1]];w=[2,-1];targets=[0,2]
prediction=matvec(A,w);residual=[p-b for p,b in zip(prediction,targets)]
assert prediction==[0,-1] and residual==[0,-3]
assert F(dot(residual,residual),2)==F(9,2)
assert matvec(transpose(A),residual)==[0,-3]
d=[1,-1]
assert dot(d,matvec([[1,2],[2,1]],d))==-2
assert dot(d,matvec([[1,-1],[-1,1]],d))==4
assert ((-1)**2-1)**2==0 and ((1)**2-1)**2==0 and (0**2-1)**2==1
for x in [F(-3),F(-1),F(0),F(1),F(3)]:
    actual=abs(x-1)+2*abs(x+1)
    assert actual==(-3*x-1 if x<=-1 else x+3 if x<=1 else 3*x+1)
assert (F(-1)-1)**2==4
assert (F(0)-F(2,5))**2==F(4,25) and (F(1)-F(2,5))**2==F(9,25)
assert F(1,2)*(2-1)**2+F(1,2)*(-1)**2==1
J=lambda theta:(theta*theta+(theta-2)**2)/4
assert J(F(1))==F(1,2) and J(F(9,10))==F(101,200)
close(.1*2/math.sqrt(.4),.31622776601683794)
close(.1*2/math.sqrt(8),.07071067811865475)
theta=F(0);velocity=F(0)
for expected in [F(1,10),F(271,1000)]:
    lookahead=theta+F(9,10)*velocity
    velocity=F(9,10)*velocity-F(1,10)*(lookahead-1)
    theta+=velocity;assert theta==expected
H=[[F(1),F(0)],[F(0),F(2)]];r=[F(1),F(1)];p=r[:];z=[F(0),F(0)]
alpha=dot(r,r)/dot(p,matvec(H,p));assert alpha==F(2,3)
z=[a+alpha*b for a,b in zip(z,p)];r2=[a-alpha*b for a,b in zip(r,matvec(H,p))]
assert z==[F(2,3),F(2,3)] and r2==[F(1,3),F(-1,3)]
gamma=dot(r2,r2)/dot(r,r);assert gamma==F(1,9)
p2=[a+gamma*b for a,b in zip(r2,p)];assert p2==[F(4,9),F(-2,9)]
assert dot(p,matvec(H,p2))==0
alpha2=dot(r2,r2)/dot(p2,matvec(H,p2));assert alpha2==F(3,4)
# BFGS inverse update with M=I, s=(1,0), y=(2,0).
s=[F(1),F(0)];y=[F(2),F(0)];rho=1/dot(y,s)
I=[[F(1),F(0)],[F(0),F(1)]]
left=[[I[i][j]-rho*s[i]*y[j] for j in range(2)] for i in range(2)]
M=matmul(left,transpose(left))
M=[[M[i][j]+rho*s[i]*s[j] for j in range(2)] for i in range(2)]
assert M==[[F(1,2),0],[0,1]] and matvec(M,y)==s
assert matvec([[2,1],[1,2]],[F(-2,3),F(1,3)])==[-1,0]
# Log-sum-exp Hessian equals a nonnegative weighted variance.
ps=[F(1,6),F(1,3),F(1,2)];vs=[-1,2,3];mean=dot(ps,vs)
assert dot(ps,[v*v for v in vs])-mean*mean==sum(p*(v-mean)**2 for p,v in zip(ps,vs))>=0

executed=[]
for path in Path('docs/toan-cho-ai/bai-giang').glob('*.md'):
    body=path.read_text(encoding='utf-8')
    for code in re.findall(r'```python\n(.*?)\n```',body,re.S):
        ast.parse(code)
        namespace={}
        exec(compile(code,str(path),'exec'),namespace)
        if 'backtrack' in namespace:
            result=namespace['backtrack'](lambda z:(z[0]**2+10*z[1]**2)/2,[2,2],[2,20],[-2,-20])
            assert result==(1/8,[1.75,-.5])
        if 'sgd_scalar' in namespace:
            result=namespace['sgd_scalar'](0,[0,2],.1,[0,1,0,1])
            for value,expected in zip(result,[0,0,.2,.18,.362]):close(value,expected)
        if 'logistic_loss_gradient_hessian' in namespace:
            logistic=namespace['logistic_loss_gradient_hessian']
            result=logistic(0,[(-1,0),(1,1)])
            close(result[0],2*math.log(2));close(result[1],-1);close(result[2],.5)
            for w in [-1000,-2,0,2,1000]:
                assert all(math.isfinite(v) for v in logistic(w,[(-1,0),(1,1)]))
            assert logistic(2,[(-1,0),(1,1)])[0]<result[0]
        executed.append(str(path))
print(json.dumps({'status':'passed','checks':'authored numeric examples and solutions', 'python_blocks':executed},ensure_ascii=False,indent=2))
