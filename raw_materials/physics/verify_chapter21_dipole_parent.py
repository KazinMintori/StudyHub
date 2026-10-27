"""Scoped numerical verification of the parent chapter21 dipole-format repair."""
from pathlib import Path
from decimal import Decimal,localcontext
import math,json,hashlib
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'qa/physics-global-audit/ch21-parent-format-repair';OUT.mkdir(parents=True,exist_ok=True)
checks=[]
def near(name,a,b,tol=1e-12):
 assert math.isclose(a,b,rel_tol=tol,abs_tol=0),(name,a,b)
 checks.append({'name':name,'actual':a,'expected':b})
p=(1.6e-19)*(0.125e-9);E=5e5;angle=math.radians(145)
near('21.13 dipole moment',p,2e-29)
near('21.13 pE',p*E,1e-23)
near('21.13 torque',p*E*math.sin(angle),5.73576436351046e-24)
near('21.13 potential energy',-p*E*math.cos(angle),8.191520442889917e-24)
near('21.13 force cancellation',1.6e-19*E+(-1.6e-19)*E,0)
with localcontext() as ctx:
 ctx.prec=70
 for ratio in ['2','3','10','20','100','1000','1000000']:
  for ds in ['0.003','2.0','350']:
   d=Decimal(ds);y=d*Decimal(ratio);kq=Decimal('3.17');u=d/(2*y)
   exact=kq/(y-d/2)**2-kq/(y+d/2)**2
   A=(1-u)**(-2);B=(1+u)**(-2)
   factored=kq/y**2*(A-B)
   assert abs((factored-exact)/exact)<Decimal('1e-54'),(ratio,ds)
   near('21.14 equivalent exact fields '+ratio+'/'+ds,float(factored),float(exact))
   approx=2*kq*d/y**3
   expected_relative_error=2*u*u-u**4
   near('21.14 leading-order relative error '+ratio+'/'+ds,float((exact-approx)/exact),float(expected_relative_error))
for u in [-.01,-.001,.001,.01]:
 A=(1-u)**(-2);B=(1+u)**(-2)
 near('21.14 linear difference '+str(u),(1+2*u)-(1-2*u),4*u)
 n=-2;remainder=(1+u)**n-1-n*u
 assert abs(remainder-n*(n-1)/2*u*u)<4.1*abs(u)**3
 checks.append({'name':'Binomial quadratic coefficient '+str(u),'passed':True})
near('21.98 source30pC electron deficit',30e-12/1.602e-19,1.8726591760299626e8)
near('21.1 ratio Coulomb/gravitational constants',9e9/6.67e-11,1.3493253373313343e20)
near('21.1 alpha charge/mass ratio',3.2e-19/6.64e-27,4.8192771084337346e7)
near('21.1 electric/gravitational force ratio',(9e9/6.67e-11)*(3.2e-19/6.64e-27)**2,3.133866366279772e35)
near('21.2 charge product',abs(25e-9*(-75e-9)),1.875e-15)
near('21.2 magnitude',9e9*1.875e-15/.030**2,.01875)
near('21.3 first force',9e9*1e-9*5e-9/.02**2,112.5e-6)
near('21.3 second force',9e9*3e-9*5e-9/.04**2,84.375e-6)
near('21.4 identical force magnitudes',9e9*4e-6*2e-6/.5**2,.288)
near('21.8 pointa first field',9e9*12e-9/.06**2,30000)
near('21.8 pointc vector sum',2*9e9*12e-9/.13**2*(5/13),4915.794264906691)
for x,R in [(.1,.05),(.1,5),(2,1),(7,.2)]:
 e0=3.17
 integral=(e0*x/2)*quad(lambda u:u**(-1.5),x*x,x*x+R*R,epsabs=1e-12,epsrel=1e-12)[0]
 factored=e0*x*(1/x-1/math.sqrt(x*x+R*R))
 final=e0*(1-x/math.sqrt(x*x+R*R))
 near('21.11 independent disk integral '+str((x,R)),integral,final,tol=2e-10)
 near('21.11 intermediate factor '+str((x,R)),factored,final)
source=ROOT/'raw_materials/physics/translations/chapter-21/13-bai-tong-hop-57-80.md'
text=source.read_text(encoding='utf8')
for number in [57,71]:
 assert text.count('(img/young-21/loi-giai-21-'+str(number)+'.svg)')==1
 checks.append({'name':'Exactlyone original solution diagram21.'+str(number),'passed':True})
paths=['raw_materials/physics/translations/chapter-21/07-luong-cuc-dien.md',
       'raw_materials/physics/translations/chapter-21/01-dien-tich.md',
       'raw_materials/physics/translations/chapter-21/03-dinh-luat-coulomb.md',
       'raw_materials/physics/translations/chapter-21/05-tinh-dien-truong.md',
       'raw_materials/physics/translations/chapter-21/13-bai-tong-hop-57-80.md',
       'docs/.vitepress/physics21-image-annotations.mjs']
result={'status':'passed-scoped-dipole-format-and-duplicate-image-repair','checks':len(checks),'records':checks,
 'sourceSHA256':{p:hashlib.sha256((ROOT/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest() for p in paths},
 'scopeLimit':'Onlythis mathematical/diagram repair. Does not certify allchapter21theory/exercises or the complete two-course audit.'}
(OUT/'numeric-checks.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(checks),'independent scoped physical/structure checks.')
