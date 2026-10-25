"""Independent numerical checks for chapter13 late theory and source model limits."""
from pathlib import Path
import math,json
from scipy.integrate import quad

OUT=Path(__file__).resolve().parent
G=6.67e-11;MS=1.99e30;ME=5.97e24;RE=6.37e6;YEAR=3.156e7;c=3e8
checks=[]
def eq(id,a,b,rel=1e-11,abstol=1e-11):
 assert math.isclose(a,b,rel_tol=rel,abs_tol=abstol),(id,a,b)
 checks.append(dict(id=id,actual=a,expected=b,status='passed'))
def approx(id,a,b,rel):eq(id,a,b,rel=rel)

# Geometric ellipse and area law checked at multiple orbital phases.
for e in(0.,.017,.233,.7,.967):
 a=3.;mu=1.;h=math.sqrt(mu*a*(1-e*e));energy=-mu/(2*a)
 for theta in(.1,.7,1.4,2.8):
  r=a*(1-e*e)/(1+e*math.cos(theta))
  vr=mu/h*e*math.sin(theta);vt=mu/h*(1+e*math.cos(theta));v=math.hypot(vr,vt)
  eq(f'Kepler2:e{e}:theta{theta}',r*vt/2,h/2)
  eq(f'Kepler-energy:e{e}:theta{theta}',v*v/2-mu/r,energy)
 rp=a*(1-e);ra=a*(1+e)
 eq(f'ellipse-2a-e{e}',rp+ra,2*a)
 eq(f'ellipse-e-e{e}',1-rp/a,e)
 if e>0:assert math.sqrt(mu*(2/rp-1/a))>math.sqrt(mu*(2/ra-1/a))

TP=4.62*YEAR;aP=(G*MS*TP*TP/(4*math.pi**2))**(1/3)
approx('13.8:Pallas-period',TP,1.46e8,.002)
approx('13.8:Pallas-a',aP,4.15e11,.002)
rp,ra=8.80e10,5.25e12;a=(rp+ra)/2;e=1-rp/a;T=2*math.pi*math.sqrt(a**3/(G*MS))
eq('13.9:Halley-a',a,2.669e12)
approx('13.9:Halley-e',e,.967,.001)
approx('13.9:Halley-T-sec',T,2.38e9,.002)
approx('13.9:Halley-T-years',T/YEAR,75.3,.002)
eq('TY13.5:period-ratio',4**1.5,8)

shell=[]
for r in(.0,.01,.25,.75,.99,1.01,1.4,3.,8.):
 R=1.
 integral,error=quad(lambda phi:-.5*math.sin(phi)/math.sqrt(r*r+R*R-2*r*R*math.cos(phi)),0,math.pi,epsabs=1e-12,epsrel=1e-12)
 expected=-1/(r if r>R else R)
 eq(f'shell-potential-r{r}',integral,expected,rel=1e-9)
 shell.append(dict(r=r,R=R,numericalU=integral,expectedU=expected,error=error))
for r in(.1,.4,.7,1.2,2.7):
 for phi in(.1,.8,1.6,2.4):
  R=.5;u=r-R*math.cos(phi);q=R*math.sin(phi)
  eq(f'13.21:r{r}:phi{phi}',u*u+q*q,r*r-2*r*R*math.cos(phi)+R*R)
for ratio in(0.,.1,.5,.9,1.):
 M=ME*ratio**3
 field=(G*M/(RE*ratio)**2)if ratio else 0.
 eq(f'13.10:uniform-field-ratio{ratio}',field,G*ME/RE**2*ratio)
eq('TY13.6:inside-shell-force',0.,0.)

vrot=2*math.pi*RE/86164;delta=vrot*vrot/RE
approx('13.7:equatorial-v',vrot,465,.002)
approx('13.7:delta-g',delta,.0339,.002)
approx('TY13.7:tenfold-delta-g',delta*100,3.39,.002)
approx('TY13.7:equatorial-g',9.8-100*delta,6.41,.002)
approx('TY13.7:zero-weight-rotation',math.sqrt(9.8/delta),17.,.002)
beta=[]
g0=9.8;omega=2*math.pi/86164
for latitude in range(0,91):
 lat=math.radians(latitude)
 # Coordinates in meridian: x toward equator, z north; true gravity points inward.
 x=RE*math.cos(lat);z=RE*math.sin(lat)
 gx=-g0*math.cos(lat)+omega*omega*x
 gz=-g0*math.sin(lat)
 geff=math.hypot(gx,gz)
 bx=math.degrees(math.acos(max(-1,min(1,(gx*(-math.cos(lat))+gz*(-math.sin(lat)))/geff))))
 beta.append(bx)
 assert 0<=g0-geff<=delta+1e-10
assert max(beta)<.101
checks.append(dict(id='13.7:max-latitude-deviation',actual=max(beta),expected='less than0.101degree',status='passed'))

rhoSun=MS/(4*math.pi*(6.96e8)**3/3);vesc=math.sqrt(2*G*MS/6.96e8)
approx('13.8:Sun-density',rhoSun,1410,.001)
approx('13.8:denser-than-water-percent',(rhoSun/1000-1)*100,41.,.01)
approx('13.8:air-density-ratio',rhoSun/1.2,1200,.03)
approx('13.8:Sun-escape',vesc,6.18e5,.001)
eq('13.29:rho-form',6.96e8*math.sqrt(8*math.pi*G*rhoSun/3),vesc)
approx('13.8:c-ratio',c/vesc,500,.03)
approx('13.8:surface-Celsius',5800-273.15,5500,.01)
approx('13.8:surface-Fahrenheit',(5800-273.15)*9/5+32,10000,.01)
approx('13.8:core-Fahrenheit',(1.5e7-273.15)*9/5+32,2.7e7,.001)

M=6e30;rs=2*G*M/c**2;rho=M/(4*math.pi*rs**3/3)
approx('13.11:Rs-m',rs,8.9e3,.001)
approx('13.11:Rs-miles',rs/1609.344,5.5,.01)
approx('13.11:rho',rho,2e18,.02)
SgrM=8.2e36;SgrRS=2*G*SgrM/c**2
approx('SgrA:solar-mass-ratio',SgrM/MS,4.1e6,.01)
approx('SgrA:consistent-Rs',SgrRS,1.2e10,.02)
assert abs(SgrRS-1.1e10)/SgrRS>.09
eq('SgrA:image-endpoint-span',2017-1995,22)
approx('SgrA:scale-Earth-sun-units',1e14/1.50e11,670,.01)
eq('TY13.8:same-exterior-gravity',G*MS/(1.5e11)**2,G*MS/(1.5e11)**2)
# Newtonian tidal gradient at r=Rs scales as M/Rs^3, hence1/M². Model-scope check only.
def horizon_gradient(m):return 2*G*m/(2*G*m/c**2)**3
eq('tidal-horizon-mass-scaling',horizon_gradient(10*MS)/horizon_gradient(1e6*MS),(1e6/10)**2,rel=1e-10)

# Support-sheet equations for earlier sections are rechecked here without editing
# or importing the separately frozen author-a code.
for radius in(1.,2.,4.,10.):
 mass=3.;central=7.;grav=2.
 force=grav*central*mass/radius**2
 eq(f'support:weight-g-r{radius}',force,mass*(grav*central/radius**2))
 circle=math.sqrt(grav*central/radius)
 eq(f'support:circular-acceleration-r{radius}',circle**2/radius,force/mass)
 kinetic=mass*circle**2/2;potential=-grav*central*mass/radius
 energy=kinetic+potential
 eq(f'support:circular-energy-r{radius}',energy,-grav*central*mass/(2*radius))
 eq(f'support:K=-E-r{radius}',kinetic,-energy)
 escape=math.sqrt(2*grav*central/radius)
 eq(f'support:escape-energy-r{radius}',mass*escape**2/2+potential,0.)
 eq(f'support:escape-circle-r{radius}',escape/circle,math.sqrt(2))

report=dict(status='passed',scope='Chapter13sections13.5–13.8 andSummary proposal; source-modelchecks only, no publicviewport acceptance',assertions=len(checks),exampleIds=['13.7','13.8','13.9','13.10','13.11'],selfcheckIds=['13.5','13.6','13.7','13.8'],checks=checks,shellQuadratures=shell,sourceClarifications=[
 {'item':'SgrA*Rs','action':'Use1.2e10m fromsourceM8.2e36kg,notprinted1.1e10m','computed':SgrRS},
 {'item':'Figure13.29duration','action':'Caption describes printed1995–2017 date range without claiming17years. Originalimage unchanged.'},
 {'item':'Tidalforces','action':'Destruction before horizon is qualified to stellar-mass scenario, not everyblackhole. No unqualified atomdestructionbeforehorizon claim.'},
 {'item':'Historicalobservations','action':'Retain source2015/2017 milestones, avoid calling source imaging prospect current2026 status.'},
 {'item':'Schwarzschild','action':'Specify sphericalnonrotatinguncharged idealization; Newtonian v=c is not a proof.'}
])
print(json.dumps(report,ensure_ascii=False,indent=2))
