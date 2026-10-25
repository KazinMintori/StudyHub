"""Independent checks for the exact data used in chapter13 opening and13.1–13.4."""
from pathlib import Path
import math,json
from scipy.integrate import quad

OUT=Path(__file__).resolve().parent
G=6.67e-11
ME,RE=5.97e24,6.37e6
records=[]
def equal(name,actual,expected,rel=1e-12,abs_tol=1e-12):
    assert math.isclose(actual,expected,rel_tol=rel,abs_tol=abs_tol),(name,actual,expected)
    records.append({'id':name,'actual':actual,'expected':expected,'status':'passed'})
def rounded(name,value,expected,rel):
    equal(name,value,expected,rel=rel)

F=G*.0100*.5/.05**2
equal('13.1:F',F,1.334e-10,abs_tol=1e-22)
equal('13.1:numerator',G*.01*.5,3.335e-13,abs_tol=1e-25)
equal('13.1:r2',.05**2,.0025)
equal('13.2:a1',F/.01,1.334e-8,abs_tol=1e-20)
equal('13.2:a2',F/.5,2.668e-10,abs_tol=1e-22)
equal('13.2:ratio',(F/.01)/(F/.5),50)
M,m,d=8e30,1e30,2e12
F1=G*M*m/(2*d*d);F2=G*M*m/(d*d)
fx=F1/math.sqrt(2)+F2;fy=F1/math.sqrt(2)
net=math.hypot(fx,fy);angle=math.degrees(math.atan2(fy,fx))
rounded('13.3:F1',F1,6.67e25,1e-12)
rounded('13.3:F2',F2,1.334e26,1e-12)
rounded('13.3:Fx',fx,1.81e26,.003)
rounded('13.3:Fy',fy,4.72e25,.001)
rounded('13.3:Fnet',net,1.87e26,.003)
rounded('13.3:angle',angle,14.6,.003)
rounded('13.3:acceleration',net/m,1.87e-4,.003)
# Direction to center of mass of two equal large masses: atan(.5), not resultant.
assert abs(angle-math.degrees(math.atan(.5)))>10
equal('13.3:not-to-CM',float(angle<20),1)
rounded('13.3:Amalthea-to-Jupiter',7.17e18/1.90e27,3.8e-9,.01)

equal('TY13.1:force-ratio',100/10**2,1)
equal('TY13.1:acceleration-ratio',1/10**2,.01)
rounded('13.2:Earth-mass-from-g',9.8*RE**2/G,5.96e24,.001)
volume=4*math.pi*RE**3/3
rounded('13.2:Earth-volume',volume,1.08e21,.003)
rounded('13.2:Earth-mean-density',ME/volume,5500,.003)
loss=1-(RE/(RE+1e4))**2
rounded('13.2:10km-weight-loss',loss,.00313,.001)
equal('13.2:density-unit-conversion',5500/1000,5.5)
mass=3430/9.8;gm=G*6.42e23/(3.39e6)**2
equal('13.4:lander-mass',mass,350)
rounded('13.4:Mars-g',gm,3.73,.002)
rounded('13.4:Mars-weight',mass*gm,1.30e3,.004)
for i,(mp,rp,result)in enumerate([(2,2,.5),(4,4,.25),(4,2,1),(2,4,.125)],1):
    equal(f'TY13.2:{i}',mp/rp**2,result)

# Radial work versus direct numerical quadrature for inward and outward paths.
work_tests=[]
for r1,r2 in [(1.,2.),(2.,1.),(1.,10.),(10.,1.),(2.,2.),(5.,8.)]:
    numeric,error=quad(lambda r:-1/r**2,r1,r2,epsabs=1e-12,epsrel=1e-12)
    analytic=1/r2-1/r1
    equal(f'13.8:radial-work-{r1}-{r2}',numeric,analytic)
    work_tests.append({'r1':r1,'r2':r2,'numericWorkPerGMm':numeric,'error':error})
vA=math.sqrt(G*ME/RE);vesc=math.sqrt(2*G*ME/RE)
rounded('13.5:to-height-RE',vA,7.91e3,.001)
equal('13.5:energy-at-2RE',vA*vA/2-G*ME/RE,-G*ME/(2*RE))
equal('13.5:escape-energy',vesc*vesc/2-G*ME/RE,0,abs_tol=1e-7)
rounded('13.5:escape-speed',vesc,1.12e4,.002)
rounded('13.5:to-RE-km-h',vA*3.6,2.85e4,.002)
rounded('13.5:to-RE-mph',vA/.44704,1.77e4,.002)
rounded('13.5:escape-km-h',vesc*3.6,4.03e4,.002)
rounded('13.5:escape-mph',vesc/.44704,2.50e4,.002)
rounded('13.5:Mars-escape',math.sqrt(2*G*6.42e23/3.39e6),5.03e3,.001)
rounded('13.5:Jupiter-escape',math.sqrt(2*G*1.9e27/6.99e7),6.02e4,.001)
rounded('13.5:Sun-escape',math.sqrt(2*G*1.99e30/6.96e8),6.18e5,.001)
for Rratio in(.25,1,4):equal(f'TY13.3:equal-g-{Rratio}',math.sqrt(Rratio),{.25:.5,1:1,4:2}[Rratio])
rounded('TY13.3:Saturn',math.sqrt(100/10),3.2,.02)

for radius in(6.8e6,3.84e8):
    v=math.sqrt(G*ME/radius);T=2*math.pi*math.sqrt(radius**3/(G*ME))
    equal(f'13.4:circle-force-{radius}',G*ME/radius**2,v*v/radius)
    equal(f'13.4:period-{radius}',v*T,2*math.pi*radius)
    E=v*v/2-G*ME/radius
    equal(f'13.13:energy-{radius}',E,-G*ME/(2*radius))
    equal(f'13.4:escape-circle-ratio-{radius}',math.sqrt(2*G*ME/radius)/v,math.sqrt(2))
v=math.sqrt(G*ME/6.8e6);T=2*math.pi*6.8e6/v
rounded('13.4:ISS-v-km-s',v/1000,7.7,.01)
rounded('13.4:ISS-period-min',T/60,93,.01)
# Moon source27.3d observational rounded; circular fixed-Earth model27.42d, do not force equality.
moonT=2*math.pi*math.sqrt((3.84e8)**3/(G*ME))/86400
rounded('13.4:Moon-period-model',moonT,27.3,.01)
r=RE+340000;m=1000
v=math.sqrt(G*ME/r);T=2*math.pi*r/v;acc=v*v/r
E1=-G*ME*m/RE;E2=-G*ME*m/(2*r)
equal('13.6:orbit-radius',r,6.71e6)
rounded('13.6:orbit-speed',v,7700,.001)
rounded('13.6:T-s',T,5470,.001)
rounded('13.6:T-min',T/60,91.2,.001)
rounded('13.6:arad',acc,8.84,.001)
rounded('13.6:E1',E1,-6.25e10,.001)
rounded('13.6:E2',E2,-2.97e10,.002)
rounded('13.6:launch-work',E2-E1,3.28e10,.002)
rounded('13.6:extra-work',-E2,2.97e10,.002)
rounded('13.6:rotation-K',m*410**2/2,8.41e7,.001)
assert math.sqrt(G*ME/(.99*r))>v
equal('TY13.4:shrinking-circle-speed-increases',1,1)
equal('TY13.4:K=-E',m*v*v/2,-E2)
equal('TY13.4:U=2E',-G*ME*m/r,2*E2)
equal('opening:half-radius-speed-ratio',math.sqrt(1/.5),math.sqrt(2))
equal('opening:half-radius-acceleration-ratio',1/.5**2,4)

result={'status':'passed','scope':'Opening and13.1–13.4 prose proposal; source-model numerical checks only','numericAssertions':len(records),'examplesChecked':['13.1','13.2','13.3','13.4','13.5','13.6'],'selfChecksChecked':['13.1','13.2','13.3','13.4'],'openingChecked':True,'radialWorkQuadratures':work_tests,'assertions':records,'sourceReconciliations':[
 'Example13.2 uses unroundedF1.334e-10 and so a2rounds2.67e-10; source2.66camefromroundingFfirst.',
 'Example13.6 consistently usesr6.71e6 andG6.67e-11, avoiding two printed substitution typos.',
 'Example13.5 escape speed converted from unrounded value gives4.03e4km/h; source4.02e4 uses a different intermediate rounding.',
 'Moon27.3days is a source observational example, not asserted exact result of circular fixed-Earth approximation.'
]}
print(json.dumps(result,ensure_ascii=False,indent=2))
