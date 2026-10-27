"""Independent phasorandpower checks for chapter31mobile presentation repairs."""
from pathlib import Path
import math,json,hashlib
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch31-theory-layout-repair-20261028';OUT.mkdir(exist_ok=True)
records=[]
def near(name,a,b,tol=1e-10,scale=None):
 ref=max(abs(a),abs(b),scale or 0,1e-300)
 assert math.isclose(a/ref,b/ref,rel_tol=tol,abs_tol=tol),(name,a,b)
 records.append({'name':name,'actual':a,'expected':b,'physicalScale':ref})
for R,XL,XC,I in[(300,600,200,.1),(3,2,7,.5),(4,8,8,2),(1,0,0,.3)]:
 phasor=complex(I*R,I*(XL-XC));V=abs(phasor);phi=math.atan2(phasor.imag,phasor.real)
 near('31Pythagoras directcomplex '+str((R,XL,XC,I)),V*V,(I*R)**2+(I*XL-I*XC)**2)
 near('31expandedsubstitution '+str((R,XL,XC,I)),V*V,I*I*R*R+I*I*(XL-XC)**2)
 near('31average independentquadrature '+str((R,XL,XC,I)),quad(lambda theta:V*I*math.cos(theta+phi)*math.cos(theta),0,2*math.pi,epsabs=1e-12,epsrel=1e-12)[0]/(2*math.pi),.5*I*I*R)
 for theta in[0,.1,math.pi/4,math.pi/2,2.7,5.8]:
  c,s=math.cos(theta),math.sin(theta)
  near('31cosineaddition '+str((R,theta)),math.cos(theta+phi),c*math.cos(phi)-s*math.sin(phi),scale=1)
  p1=V*I*math.cos(phi)*c*c;p2=V*I*math.sin(phi)*s*c
  near('31instantpower preserved terms '+str((R,theta)),V*I*math.cos(theta+phi)*c,p1-p2,scale=V*I)
 near('31cossquaredaverage '+str(R),quad(lambda theta:math.cos(theta)**2,0,2*math.pi)[0]/(2*math.pi),.5)
 near('31sincosaverage '+str(R),quad(lambda theta:math.sin(theta)*math.cos(theta),0,2*math.pi)[0]/(2*math.pi),0,scale=1)
near('31actualexamplevoltage magnitude',math.hypot(30,40),50)
near('31actualexamplepower',.5*50*.1*.6,1.5)
near('31actualresistorpower',.5*.1**2*300,1.5)
paths=['raw_materials/physics/translations/chapter-31/'+n for n in['03-mach-rlc-noi-tiep.md','04-cong-suat-xoay-chieu.md']]
result={'status':'passed-scoped-ch31-phasor-power-models','checks':len(records),'records':records,
 'sourceSHA256':{p:hashlib.sha256((ROOT/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()for p in paths},
 'scopeLimit':'Onlychangedtheoryderivations andassociatedmodels. Fullchapter source/figures/exercises/Wiki/Cheatsheet and actualviewport acceptance remainseparate.'}
(OUT/'numeric-checks.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(records),'independentphasor/instantaneous/average power checks.')
