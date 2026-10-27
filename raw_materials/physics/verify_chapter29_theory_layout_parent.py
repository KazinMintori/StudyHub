"""Independent physical checks for scoped chapter29 mobile equation repairs."""
from pathlib import Path
import math,json,hashlib
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch29-theory-layout-repair-20261028';OUT.mkdir(exist_ok=True)
mu=4*math.pi*1e-7;eps=8.8541878128e-12;records=[]
def near(name,a,b,tol=1e-10,scale=None):
 ref=max(abs(a),abs(b),scale or 0,1e-300)
 assert math.isclose(a/ref,b/ref,rel_tol=tol,abs_tol=tol),(name,a,b)
 records.append({'name':name,'actual':a,'expected':b,'physicalScale':ref})
A=math.pi*.04**2;N=500;rate=-.2
flux_rate=quad(lambda theta:math.cos(math.pi/6)*rate*.04**2/2,0,2*math.pi)[0]
near('29.2 actual area',A,.005026548245743669)
near('29.2 geometric flux derivative',flux_rate,A*rate*math.cos(math.pi/6))
near('29.2 EMF independent flux integral',-N*flux_rate,.4353118474162123)
near('29.2 prefactor',-N*rate,100)
near('29.2 grouped units result',100*A*math.cos(math.pi/6),-N*flux_rate)
B,L,v,R=.6,.1,2.5,.03;emf=v*B*L;I=emf/R
near('29movingbar EMF',emf,.15)
near('29movingbar current',I,5)
near('29movingbar force',I*L*B,.3)
near('29movingbar mechanical/electrical power balance',I*L*B*v,I*I*R)
n,A,rate,r=500,4e-4,100,.02;Bdot=mu*n*rate
near('29inducedfield magnetic derivative',Bdot,.06283185307179587)
near('29inducedfield prefactor regrouping',(4*math.pi)*5e-3,Bdot)
near('29inducedfield EMF',-mu*n*A*rate,-2.5132741228718347e-5)
near('29inducedfield grouped EMF',-A*Bdot,-mu*n*A*rate)
electric=A*Bdot/(2*math.pi*r)
near('29inducedfield magnitude',electric,2e-4)
near('29inducedfield line integral',quad(lambda t:electric*r,0,2*math.pi)[0],A*Bdot)
for Ic,Id in[(0,2),(2,0),(-3,.6),(8,-5),(0,0)]:
 near('29.15 sharedconstant factoring '+str((Ic,Id)),mu*Ic+mu*Id,mu*(Ic+Id),scale=mu)
for conductor,fluxrate in[(0,3e9),(2,.7e9),(-.3,0),(0,0)]:
 near('29.21 same-surface AmpereMaxwell '+str((conductor,fluxrate)),mu*conductor+mu*eps*fluxrate,mu*(conductor+eps*fluxrate),scale=mu)
for plate_radius in[.03,.2]:
 for I in[.4,3]:
  E_rate=I/(eps*math.pi*plate_radius**2)
  near('29displacement equals chargingcurrent '+str((plate_radius,I)),eps*E_rate*math.pi*plate_radius**2,I)
  for radius_fraction in[.1,.5,.9,1]:
   radius=radius_fraction*plate_radius;Id=eps*E_rate*math.pi*radius**2
   field=mu*radius*I/(2*math.pi*plate_radius**2)
   near('29.17 magnetic circulation '+str((plate_radius,I,radius_fraction)),field*2*math.pi*radius,mu*Id)
paths=['raw_materials/physics/translations/chapter-29/'+n for n in['02-dinh-luat-faraday.md','04-suat-dien-dong-chuyen-dong.md','05-dien-truong-cam-ung.md','07-dong-dien-dich-maxwell.md']]
result={'status':'passed-scoped-ch29-faraday-motional-ampere-models','checks':len(records),'records':records,
 'sourceSHA256':{p:hashlib.sha256((ROOT/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()for p in paths},
 'scopeLimit':'Changed source expressions and associated physical models only. Completechapter source/prose/figures/exercises/Wiki/cheatsheet and viewport/publicrelease acceptance remain separate.'}
(OUT/'numeric-checks.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(records),'independent Faraday/energy/displacementcurrent checks.')
