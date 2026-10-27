"""Independent integral/model checks for chapter28 mobile formula repairs."""
from pathlib import Path
import math,hashlib,json
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch28-theory-layout-repair-20261028';OUT.mkdir(exist_ok=True)
mu=4*math.pi*1e-7;records=[]
def near(name,a,b,tol=1e-10,scale=None):
 ref=max(abs(a),abs(b),scale or 0,1e-300)
 assert math.isclose(a/ref,b/ref,rel_tol=tol,abs_tol=tol),(name,a,b)
 records.append({'name':name,'actual':a,'expected':b,'physicalScale':ref})
near('28.3 magneticconstant coefficient',mu/(2*math.pi),2e-7)
near('28.3 current/field ratio',1/(.5e-4),2e4)
r=mu*1/(2*math.pi*.5e-4)
near('28.3 distance metres',r,4e-3)
near('28.3 distance millimetres',r*1000,4)
near('28.3 originalfield recovered',mu/(2*math.pi*r),.5e-4)
for I in[-3,.4,7]:
 for radius in[.003,.12,1.7]:
  # Circle integral in units of mu0*I avoids an absolute tolerance masking tiny fields.
  integral=quad(lambda t:math.sin(t)**2+math.cos(t)**2,0,2*math.pi,epsabs=1e-12,epsrel=1e-12)[0]
  near('28.7 independentcircleparametrization '+str((I,radius)),mu*I/(2*math.pi)*integral,mu*I)
  B=mu*I/(2*math.pi*radius)
  near('28.7 constantBcircle reduction '+str((I,radius)),B*(2*math.pi*radius),mu*I)
  for length_ratio in[2,20,200]:
   dimensionless=quad(lambda u:(1+u*u)**(-1.5),-length_ratio,length_ratio,epsabs=1e-12,epsrel=1e-12)[0]
   numerical=mu*I/(4*math.pi*radius)*dimensionless
   expected=mu*I/(2*math.pi*radius)*length_ratio/math.sqrt(1+length_ratio**2)
   near('28.3 independent finitewire integral '+str((I,radius,length_ratio)),numerical,expected)
   near('28.3 finitewirefraction approacheslongwire '+str((I,radius,length_ratio)),numerical/B,length_ratio/math.sqrt(1+length_ratio**2))
files=['raw_materials/physics/translations/chapter-28/'+n for n in['03-day-thang.md','07-ung-dung-ampere.md']]
result={'status':'passed-scoped-ch28-integral-and-unitchecks','checks':len(records),'records':records,
 'sourceSHA256':{p:hashlib.sha256((ROOT/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()for p in files},
 'scopeLimit':'Onlythechangedtheory expressions and theunderlyingstraightwire/Amperecircle model. Fullchapter source/content/images/exercises/cheatsheet/Wiki and actualviewport acceptance remain separate.'}
(OUT/'numeric-checks.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(records),'independent Biot-Savart/Ampere/unit checks.')
