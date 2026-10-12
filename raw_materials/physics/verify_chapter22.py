"""Arithmetic and independent integral checks for chapter22. Never included on the site."""
from math import pi,sin,cos,sqrt,atan,degrees,exp
from fractions import Fraction
from pathlib import Path
import json,re

root=Path(__file__).resolve().parents[2]
k=8.987551787e9;eps=1/(4*pi*k);e=1.602176634e-19;me=9.10938356e-31;mp=1.672621898e-27;g=9.8
a={}
a['ex22.1']=[2e3*pi*.1**2*cos(pi/6),0,2e3*pi*.1**2]
a['ex22.3']=3e-6/eps
a['ex22.10']=-180*.3**2/k
a['ex22.11']=[5,2]
a['ex22.12']=[-150*eps,-150*eps*4*pi*(6.38e6)**2]
a['22.1']=14*.25*.5
a['22.2']=90*.4*.6*sin(pi/9)
a['22.3']=[1.25e6*4*pi*.15**2,1.25e6*.15**2/k]
a['22.4']=[3e-6*.4/eps]*2+[3e-6*.8/eps]
a['22.5']=4.44/(6.66e-4*sin(pi/3))
a['22.6']=[-4000*sin(53.1*pi/180)*.1**2,0,4000*sin(53.1*pi/180)*.1**2,0,4000*cos(53.1*pi/180)*.1**2,-4000*cos(53.1*pi/180)*.1**2]
a['22.7']=5*eps/(87.6e-12/(29.2e-4))
a['22.8']=[q*1e-9/eps for q in [4,-7.8,-3.8,6.4,-1.4]]
a['22.9']=[0,k*49e-6/.06**2,k*49e-6/.11**2]
a['22.10']=[0,-6e-9/eps,-2e-9/eps]
a['22.11']=-8.65e-12/eps
a['22.12']=[k*92*e/(7.4e-15)**2,k*92*e/(1e-10)**2,0]
a['22.13']=2*k*(5.2e-6)**2*.05/.3
a['22.14']=[k*.25e-9/.55**2,0]
a['22.15']=[350,700,1400]
RM=3.39e6
a['22.16']=[-3.63e16*eps,-3.63e16/(4*pi*RM**2),-3.63e16*eps/(4*pi*RM**2)]
a['22.17']=[2*k*(4.8e-6/.2+2.4e-6/.2),2*k*(4.8e-6/.6-2.4e-6/.2)]
a['22.18']=840*.4*.02/(2*k)
Q=6.37e-6*4*pi*.25**2-.5e-6
a['22.19']=[Q/(4*pi*.25**2),k*Q/.25**2,-.5e-6/eps]
a['22.20']=400
Q=1750*.5**2/k;rho=Q/(4*pi*.355**3/3)
a['22.21']=[rho,rho*.2/(3*eps)]
Q=-3e-6+7.35e-4*4*pi*(.095**3-.065**3)/3
a['22.22']=k*Q/.095**2
W=e*2.9e-12/(2*eps)*.25
a['22.23']=[W,sqrt(2*W/me)]
Q=940*.08**2/k;rho=Q/(4*pi*.04**3/3)
a['22.24']=[rho,k*Q*.02/.04**3]
a['22.25']=[6,-1]
a['22.26']=[4.5e-9/.8**2/(2*eps),k*4.5e-9/100**2]
a['22.28']=[-5e-6/(2*eps),-7e-6/(2*eps),-3e-6/(2*eps)]
a['22.29']=sqrt(970**2+(e*2.34e-9/(2*eps)/mp*5e-8)**2)
a['22.30']=sqrt(2*6.5e-9*5.9e-8/(2*eps)*.3/8.2e-9)
a['22.31']=degrees(atan(5e-8*2.5e-9/(2*eps)/(4e-6*g)))
a['22.32']=[0,3*.3**3,0,0,-5*.3**3,0,eps*(-2*.3**3)]
a['22.33']=[125*6,0,125+24e-9/(6*eps)]
a['22.34']=964*.35**3/2
a['22.36']=[.1+50e-6/(pi*100e-6),.1-50e-6/(pi*100e-6)]
a['22.46']=(k*e*e/(me*(2*pi*4.57e14)**2))**(1/3)
Q=-1390*.15**2/k;a['22.48']=[abs(Q)/e,k*abs(Q)/.25**2]
rr=[.01,.015,.02,.025,.03,.035,.04];A=[2.72,1.79,1.34,1.07,.902,.770,.677];B=[5.45,2.42,1.34,.861,.605,.443,.335]
cA=sum(r*x*1e5 for r,x in zip(rr,A))/7;cB=sum(r*r*x*1e5 for r,x in zip(rr,B))/7
a['22.55']=[cA/(2*k),3*cB/(4*pi*k*.008**3)]
a['22.56']=3*eps*(7.5e4/.01)
def enclosed57(r):
 total=0
 for lo,hi,rho in [(0,.002,10e-6),(.002,.004,4e-6),(.004,.006,-2e-6)]:
  if r>lo:total+=rho*4*pi*(min(r,hi)**3-lo**3)/3
 return total
a['22.57']=[k*enclosed57(r)/r**2 for r in [.001,.003,.005,.007]]
Qbee=75000*e;diameter=.01
a['22.58']=[Qbee,k*Qbee/diameter**2,-10e-12/(k*Qbee/diameter**2)]
sig=100e-6;R=.03;F=sig**2*pi*R*R/(2*eps)
a['22.60']=[F,F/.1-g]
total=Fraction(3,32)+Fraction(47,120)
assert total==Fraction(233,480)
a['22.62']={'alphaCoefficient':480/233,'outerChargeFraction':188/233,'fieldHalfCoefficient':180/233}
a['22.63']=-1e6*25**2/k;a['22.64']=1e6*(25/2.5)**2
a['VP22.4.2']=[8e-9/(2*eps),-4e-9/(2*eps),-4e-9/(2*eps)]
a['VP22.4.3']=[6e-9/eps,6e-9/(6*eps)]
a['VP22.4.4']=[3e-9/eps,-5e-9/eps,-5e-9/eps]
a['VP22.10.1']=[k*3e-9*.04/.05**3,k*3e-9/.06**2,0]
a['VP22.10.2']=2*k*3e-9*4e-9/.09
a['VP22.10.3']=2*eps*k*1.8e-9/.04**2
a['VP22.10.4']=eps*22e-6/3.6e-9
a['VP22.12.3']=[0,3e5*.9**2/k,eps*3e5]
a['VP22.12.4']=[-4e-9,-2e-9,k*4e-9/.12**2,k*2e-9/.33**2]

def simpson(f,lo,hi,n=2000):
 h=(hi-lo)/n
 return h/3*(f(lo)+f(hi)+sum((4 if i%2 else 2)*f(lo+i*h) for i in range(1,n)))
evidence=[]
for r in [.1,.3,.8]:
 rho=lambda s:2e-9*(1-s)
 Q=simpson(lambda s:4*pi*s*s*rho(s),0,r)
 exact=4*pi*2e-9*(r**3/3-r**4/4)
 assert abs(Q-exact)<1e-20
 evidence.append({'test':'22.47/50-integral','r':r,'numericalCharge':Q,'exactCharge':exact})
for u in [.2,.5,.8,1,2]:
 profile=lambda s:1.5*s if s<=.5 else 1-s*s
 Q=simpson(lambda s:4*pi*s*s*profile(s),0,min(u,1))
 expected=pi*(1.5*u**4 if u<=.5 else ((4*u**3/3-4*u**5/5-23/480) if u<=1 else 233/480))
 assert abs(Q-expected)<1e-9,(u,Q,expected)
 evidence.append({'test':'22.62-piecewise-integral','rOverR':u,'numericalCharge':Q,'exactCharge':expected})
for u in [.01,.2,1,2,4]:
 # Electron density is integrated in dimensionless coordinates.
 Q=1-4*simpson(lambda s:s*s*exp(-2*s),0,u)
 expected=exp(-2*u)*(1+2*u+2*u*u)
 assert abs(Q-expected)<1e-10
 evidence.append({'test':'hydrogen-bridge-integral','rOverA0':u,'numericalChargeRatio':Q,'closedFormRatio':expected})

# Compare the published rounded values, rather than merely printing arithmetic.
targets={'ex22.1':[54,0,63],'ex22.3':3.4e5,'ex22.10':-1.80e-9,
 'ex22.12':[-1.33e-9,-6.8e5],'22.1':1.75,'22.2':7.39,
 '22.3':[3.53e5,3.13e-6],'22.4':[1.36e5,1.36e5,2.71e5],'22.5':7.70e3,
 '22.6':[-32,0,32,0,24,-24],'22.7':14.8e-4,'22.8':[452,-881,-429,723,-158],
 '22.9':[0,1.22e8,3.64e7],'22.10':[0,-678,-226],'22.11':-.977,
 '22.12':[2.4e21,1.3e13,0],'22.13':.0810,'22.14':[7.43,0],
 '22.15':[350,700,1400],'22.16':[-3.21e5,-251,-2.23e-9],
 '22.17':[6.47e5,-7.19e4],'22.18':.374e-9,'22.19':[5.73e-6,6.48e5,-5.65e4],
 '22.20':400,'22.21':[2.60e-7,1.96e3],'22.22':-1.20e6,
 '22.23':[6.56e-21,1.20e5],'22.24':[2.50e-6,1.88e3],'22.25':[6,-1],
 '22.26':[397,4.04e-3],'22.28':[-2.82e5,-3.95e5,-1.69e5],
 '22.29':1.16e3,'22.30':39.8,'22.31':10.2,
 '22.32':[0,.0810,0,0,-.135,0,-4.78e-13],'22.33':[750,0,577],
 '22.34':20.7,'22.36':[.259,-.0592],'22.46':3.13e-10,
 '22.48':[2.17e10,500],'22.55':[1.50e-7,2.81e-3],'22.56':2.0e-4,
 '22.57':[377,653,274,0],'22.58':[1.20e-14,1.08,-9.3e-12],
 '22.60':[1.60,6.17],'22.63':-.070,'22.64':1e8,
 'VP22.4.2':[452,-226,-226],'VP22.4.3':[678,113],
 'VP22.4.4':[339,-565,-565],'VP22.10.1':[8.63e3,7.49e3,0],
 'VP22.10.2':2.40e-6,'VP22.10.3':1.79e-7,'VP22.10.4':5.41e-8,
 'VP22.12.3':[0,2.7e-5,2.7e-6],'VP22.12.4':[-4e-9,-2e-9,2.50e3,165]}
for key,expected in targets.items():
 actual=a[key]
 aa=actual if isinstance(actual,list) else [actual]
 bb=expected if isinstance(expected,list) else [expected]
 assert len(aa)==len(bb),key
 for x,y in zip(aa,bb):assert abs(x-y)<=max(abs(y)*.02,1e-10 if y==0 else 1e-28),(key,x,y)

for r in [.2,.4,.7]:
 alpha=2e-9;inner=.1
 integral=simpson(lambda s:4*pi*s*s*alpha/s,inner,r)
 expected=2*pi*alpha*(r*r-inner*inner)
 assert abs(integral-expected)<1e-21
 evidence.append({'test':'22.45-variable-density-shell','r':r,'numericalCharge':integral,'closedFormCharge':expected})
for r in [.1,.3,.8]:
 alpha=3e-9;R=1
 integral=simpson(lambda s:2*pi*s*alpha*(1-s/R),0,r)
 expected=2*pi*alpha*(r*r/2-r**3/(3*R))
 assert abs(integral-expected)<1e-21
 evidence.append({'test':'22.49/59-cylinder-density','r':r,'numericalChargePerLength':integral,'closedForm':expected})
R,L,Q=.4,1.2,3e-9
side=simpson(lambda z:2*pi*k*Q*R*R/(R*R+z*z)**1.5,-L/2,L/2)
cap=simpson(lambda s:2*pi*k*Q*(L/2)*s/(s*s+(L/2)**2)**1.5,0,R)
assert abs(side+2*cap-Q/eps)<1e-8
evidence.append({'test':'22.61-independent-surface-integrals','side':side,'eachCap':cap,'total':side+2*cap,'gauss':Q/eps})

text='\n'.join(p.read_text(encoding='utf8') for p in (root/'raw_materials/physics/translations/chapter-22').glob('*.md'))
for n in range(1,67):assert re.search(rf'^::: exercise 22\.{n}(?: |\n)',text,re.M),n
for n in range(1,17):assert re.search(rf'^::: exercise Q22\.{n}(?: |\n)',text,re.M),n
for n in range(1,13):assert f'### Ví dụ 22.{n} —' in text,n
for n in range(1,11):assert rf'\tag{{22.{n}}}' in text,n
solutions=re.findall(r'<!-- detailed-solution:([^>]+) -->\s*::: solution[^\n]*\n([\s\S]*?)\n:::',text)
assert len(solutions)==95,len(solutions)
for key,body in solutions:
 assert '**Tóm tắt đề bài:**' in body and '**Hướng đi:**' in body,key
 assert re.search(r'^- ',body,re.M),key
 for word in ['assert','numeric-checks','tự kiểm chứng','mã kiểm chứng']:assert word not in body.lower(),(key,word)
out=root/'qa/physics/chapter22';out.mkdir(parents=True,exist_ok=True)
(out/'numeric-checks.json').write_text(json.dumps({'status':'passed','numericGroups':len(a),'roundedValuesAsserted':len(targets),'results':a,'independentIntegrals':evidence,'exerciseCount':66,'solutionBoxes':95},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(a,ensure_ascii=False,indent=2))
