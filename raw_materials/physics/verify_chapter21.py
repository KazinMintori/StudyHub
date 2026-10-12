"""Independent arithmetic, vector sums and numerical integration for chapter21."""
from pathlib import Path
from math import sqrt,sin,cos,radians,pi,atan2,degrees,log,isclose
import json,re

ROOT=Path(__file__).resolve().parents[2]
k=8.987551787e9
e=1.602176634e-19
eps=1/(4*pi*k)
me=9.10938356e-31
mp=1.672621898e-27
NA=6.02214076e23
results={}

def check(name,calculated,expected,tol=.015):
    aa=calculated if isinstance(calculated,(list,tuple)) else [calculated]
    bb=expected if isinstance(expected,(list,tuple)) else [expected]
    assert len(aa)==len(bb),name
    for a,b in zip(aa,bb):
        assert isclose(a,b,rel_tol=tol,abs_tol=max(1e-30,abs(b)*tol)),(name,a,b)
    results[name]={'calculated':calculated,'expected':expected}

def field(charges,p):
    x=y=0
    for q,sx,sy in charges:
        dx,dy=p[0]-sx,p[1]-sy
        r=sqrt(dx*dx+dy*dy)
        x+=k*q*dx/r**3;y+=k*q*dy/r**3
    return x,y

def force(charges,p,q):return tuple(q*v for v in field(charges,p))
def simpson(f,lo,hi,n=4000):
    h=(hi-lo)/n
    return h/3*(f(lo)+f(hi)+sum((4 if i%2 else 2)*f(lo+i*h) for i in range(1,n)))

check('example21.1',9e9/6.67e-11*(3.2e-19/6.64e-27)**2,3.1e35)
check('example21.2',9e9*25e-9*75e-9/.03**2,.019,.02)
check('example21.3',force([(1e-9,.02,0),(-3e-9,.04,0)],(0,0),5e-9)[0],-28e-6)
check('example21.4',force([(2e-6,0,.3),(2e-6,0,-.3)],(.4,0),4e-6),(.46,0))
check('example21.5',k*4e-9/2**2,9)
check('example21.6',field([(-8e-9,0,0)],(1.2,-1.6)),(-11,14),.05)
a=-1.60e-19*1e4/9.11e-31;v=sqrt(2*a*(-.01))
check('example21.7',[a,v,.5*9.11e-31*v*v,v/(-a)],[-1.76e15,5.9e6,1.6e-17,3.4e-9])
charges=[(12e-9,0,0),(-12e-9,.1,0)]
check('example21.8',[field(charges,(.06,0))[0],field(charges,(-.04,0))[0],field(charges,(.05,.12))[0]],[9.8e4,-6.2e4,4.9e3])
for x,a,Q in [(.5,.2,2e-9),(2,.1,-3e-9)]:
    lam=Q/(2*pi*a)
    integral=simpson(lambda t:k*lam*a*x/(x*x+a*a)**1.5,0,2*pi)
    check('example21.9-integral-'+str(x),integral,k*Q*x/(x*x+a*a)**1.5,1e-9)
for x,a,Q in [(.2,.4,2e-9),(.9,.1,3e-9)]:
    integral=simpson(lambda y:k*Q/(2*a)*x/(x*x+y*y)**1.5,-a,a)
    check('example21.10-integral-'+str(x),integral,k*Q/(x*sqrt(x*x+a*a)),1e-8)
check('line-limit-relative-difference',1-1/sqrt(1+.02**2),.00019994,.001)
for x,R,sigma in [(.1,.5,3e-9),(.3,.2,1e-9)]:
    integral=simpson(lambda r:k*2*pi*sigma*r*x/(x*x+r*r)**1.5,0,R)
    check('example21.11-integral-'+str(x),integral,sigma/(2*eps)*(1-x/sqrt(x*x+R*R)),1e-8)
sigma=1.2e-9
check('example21.12-between',sigma/(2*eps)+sigma/(2*eps),sigma/eps,1e-10)
check('example21.12-outside',sigma/(2*eps)-sigma/(2*eps),0,1e-10)
p=1.6e-19*.125e-9
check('example21.13',[p,p*5e5*sin(radians(145)),-p*5e5*cos(radians(145))],[2e-29,5.7e-24,8.2e-24])
q=2e-9;d=.001;y=.1
exact=k*q*((y-d/2)**-2-(y+d/2)**-2)
check('example21.14-far-field',exact,2*k*q*d/y**3,.0001)

check('VP21.4.1',force([(4e-9,0,0),(-1.2e-9,.06,0)],(.04,0),-2e-9)[0],-98.9e-6)
f1=k*3.6e-9*2e-9/.04**2;f2=54e-6-f1
check('VP21.4.2',[f1,f2,f2*.08**2/(k*2e-9)],[40.5e-6,13.6e-6,4.82e-9])
check('VP21.4.3',force([(6e-9,0,.2),(-6e-9,0,-.2)],(.15,0),-2.5e-9),(0,3.45e-6))
check('VP21.4.4',force([(4e-9,0,.2),(-4e-9,0,0)],(.25,0),-1.5e-9),(.452e-6,.329e-6))
for name,point,expected in [('a',(0,.1),(0,-8.09e3)),('b',(0,.4),(0,6.18e2)),('c',(.2,0),(-8.06e2,-3.18e2))]:
    check('VP21.10.1'+name,field([(4e-9,0,.2),(-5e-9,0,0)],point),expected)
check('VP21.10.2',[k*1.8e-9/.02**2,6.75e4-k*1.8e-9/.02**2,-(6.75e4-k*1.8e-9/.02**2)*.02**2/k],[4.05e4,2.70e4,-1.20e-9])
check('VP21.10.3-positive',k*e*(1-1/(2*sqrt(2))),9.3086e-10,.001)
check('VP21.10.4',simpson(lambda x:-k*2e-9/.2/x**2,.2,.4),-k*2e-9/(2*.2**2),1e-8)
p=6.13e-30
check('VP21.14.1',[p*3e5*sin(radians(50)),-p*3e5*cos(radians(50))],[1.41e-24,-1.18e-24])
check('VP21.14.2',6.6e-26/(8.5e4*1.1e-10),7.06e-21)
check('VP21.14.3',4.6e-25/(2*1.2e5),1.92e-30)
check('VP21.14.4',[3.5e-29/1.6e-19,(2*k*3.5e-29/8e4)**(1/3)],[2.19e-10,1.99e-8])
check('bridging-semiring',simpson(lambda t:-k*1e-9/(pi*.2**2)*sin(t),0,pi),-2*k*1e-9/(pi*.2**2),1e-8)

check('odd21.1',[3.2e-9/e,(3.2e-9/e)/(.008/.207*NA)],[2e10,8.59e-13])
check('odd21.3',[k*e*e/(2e-10)**2/mp,k*e*e/(2e-10)**2/me],[3.4e18,6.3e21],.02)
check('odd21.5',5.6e11*e*.015,1.3e-9,.04)
check('odd21.7',sqrt(k/650),3700,.01)
check('odd21.9',[sqrt(.22*.15**2/k),sqrt(.22*.15**2/k/4),4*sqrt(.22*.15**2/k/4)],[.742e-6,.371e-6,1.48e-6])
check('odd21.11',k*e*e/(2.5e-3)**2/mp,2.21e4)
check('odd21.13',3e-9*(.02/.04)**2,.750e-9)
check('odd21.15',force([(-3e-9,.04,0),(5e-9,0,0)],(.02,0),1e-9)[0],1.8e-4)
check('odd21.17',force([(-1.5e-9,0,-.6),(3.2e-9,0,0)],(0,-.4),5e-9)[1],-2.58e-6)
check('odd21.21',[e*2750,e*2750/mp,e*2750/mp*1e-6],[4.40e-16,2.63e11,2.63e5])
a=4.5e6**2/(2*.032)
check('odd21.23',[mp*a/e,4.5e6/a,me*a/e],[3.30e6,14.2e-9,1.8e3])
check('odd21.25',[-.00145*9.8/650,mp*9.8/e],[-21.9e-6,1.02e-7])
time=.02/1.6e6;E=2*.005*me/(e*time*time)
check('odd21.27',[E,.005*me/mp],[364,2.73e-6])
F=2e-6*k*(4.8e-9*.2)/(.05*sqrt(.05**2+.1**2))
check('odd21.31-corrected',F,3.09e-3)
check('odd21.33',8*.1/(8-4),.2)
for x,E in [(.2,574),(1.2,-268),(-.2,-404)]:check('odd21.35-'+str(x),field([(2e-9,0,0),(-5e-9,.8,0)],(x,0))[0],E)
check('odd21.37',abs(field([(-2e-6,0,0),(-5e-6,0,.08),(-5e-6,0,-.08)],(.06,0))[0]),1.04e7)
for point,val in [((.15,0),8740),((-.1,0),6540)]:check('odd21.39-'+str(point),field([(-6.25e-9,0,0),(-12.5e-9,.25,0)],point)[0],val)
check('odd21.41',2*k*e*e/(1.5e-10)**2*cos(radians(65/2)),1.73e-8)
charges=[(6e-9,.15,0),(6e-9,-.15,0)]
check('odd21.43b',field(charges,(.3,0)),(2660,0))
check('odd21.43c',field(charges,(.15,-.4)),(129,-510))
check('odd21.43d',field(charges,(0,.2)),(0,1380))
check('odd21.45',(8e-9-4e-9-6e-9)/(2*eps),-113)
EA=2700*.04**2/.03**2;EB=2700*.04**2*2/.05**2
check('odd21.47',[EA-EB,EA+EB],[1340,8260])
E=k*.125e-9*.4/(.4**2+.025**2)**1.5
check('odd21.49',[E,E*2.5e-6],[7,1.75e-5])
check('odd21.51',[4.5e-9*.0031,7.2e-9/(4.5e-9*.0031*sin(radians(36.9)))],[1.4e-11,860])
F=k*10e-6*5e-6/.02**2
check('odd21.55',[2*F*.015/.02,2*F*sqrt(.02**2-.015**2)/.02*.015],[1680,22.3])
check('odd21.59',force([(5e-9,0,0),(-2e-9,.04,0)],(.04,.03),6e-9),(8.63e-5,-5.52e-5))
q=sqrt(.015*9.8*sin(radians(25))/cos(radians(25))*(2*1.2*sin(radians(25)))**2/k)
check('odd21.61b',q,2.80e-6)
check('odd21.63',.0123*9.8*sin(radians(17.4))/cos(radians(17.4))/1.11e-6,3.41e4)
check('odd21.65-estimate',[sqrt(.004*9.8*(500e-6)**2/k),10*sqrt(.004*9.8*(500e-6)**2/k)/e],[1e-9,6e10],.1)
check('odd21.67',1.2/(1+sqrt(8/.5)),.24)
check('odd21.75',sqrt(k*e*e/(me*5.29e-11)),2.19e6)
check('odd21.77',[mp*(4e5*sin(radians(30)))**2/(2*e*500),mp*(4e5)**2*sin(radians(60))/(e*500)],[.418,2.89])
Q=7e-12;R=.025;x=.2;sigma=Q/(pi*R*R)
check('odd21.81a',sigma/(2*eps)*(1-x/sqrt(x*x+R*R)),1.56)
check('odd21.85',sqrt(2)*k*2.5e-6/(.6*sqrt(.6**2+.6**2)),6.25e4)
check('odd21.89-minus',force([(8e-6,0,0),(3e-6,.4,0)],(-.2,0),4e-6)[0],-7.5)
check('odd21.89-zero',.4*sqrt(8)/(sqrt(8)+sqrt(3)),.248)
mmax=1e-6*1e-5/(2*9.8*eps);alpha=.025/mmax
check('odd21.91g',[mmax,2*.1*alpha/(1-alpha*alpha)],[.0577,.107])
Q=10e-6;L=.5;a=.1
W=Q*Q/(2*pi*eps*L*L)*(L*log((L+sqrt(a*a+L*L))/a)+a-sqrt(a*a+L*L))
check('odd21.93f-corrected',2*sqrt(W/.5),6.55)
check('MCAT21.98',30e-12/e,1.9e8,.02)
check('MCAT21.101',k*40e-12/.15**2,16)

files=sorted((ROOT/'raw_materials/physics/translations/chapter-21').glob('*.md'))
text='\n'.join(p.read_text(encoding='utf8') for p in files)
for n in range(1,102):assert re.search(rf'^::: exercise 21\.{n}(?: |\n)',text,re.M),n
for n in range(1,24):assert re.search(rf'^::: exercise Q21\.{n}(?: |\n)',text,re.M),n
for n in range(1,15):assert f'### Ví dụ 21.{n}:' in text,n
for n in range(1,19):assert rf'\tag{{21.{n}}}' in text,n
for section in [4,10,14]:
    for n in range(1,5):assert f'::: exercise VP21.{section}.{n}\n' in text
out=ROOT/'qa/physics/chapter21/numeric-checks.json';out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({'status':'passed','numericGroups':len(results),'results':results,'exerciseCount':101,'discussionQuestions':23,'examples':14,'equations':18},ensure_ascii=False,indent=2),encoding='utf8')
print('Passed',len(results),'numeric groups, continuous-source integrations, 101 exercises, 23 discussion questions,14 examples and18 equations.')
