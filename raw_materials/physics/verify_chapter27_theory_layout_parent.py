"""Independent model checks for scoped mobile formula repairs in chapter27."""
from pathlib import Path
import json,math,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch27-theory-layout-repair-20261028';OUT.mkdir(exist_ok=True)
records=[]
def near(name,a,b,tol=1e-11,scale=None):
 a,b=np.asarray(a,dtype=float),np.asarray(b,dtype=float)
 reference=max(np.max(np.abs(a)),np.max(np.abs(b)),scale or 0,1e-300)
 assert np.allclose(a/reference,b/reference,rtol=tol,atol=tol),(name,a,b)
 records.append({'name':name,'actual':a.tolist(),'expected':b.tolist(),'physicalScale':float(reference)})
q=1.6e-19;v=3e5;B=2;phi=math.radians(30);vx=v*math.sin(phi);vz=v*math.cos(phi)
near('27.1 prefactor arithmetic',1.6*3.0*2.0,9.6)
near('27.1 magnitude',abs(q)*v*B*math.sin(phi),4.8e-14)
near('27.1 vx/vz',[vx,vz],[1.5e5,2.598076211353316e5])
near('27.1 unitvector product xz',np.cross([1,0,0],[0,0,1]),[0,-1,0])
near('27.1 parallel product zero',np.cross([0,0,1],[0,0,1]),[0,0,0],scale=1)
near('27.1 vectorforce independentcross',q*np.cross([vx,0,vz],[0,0,B]),[0,-q*vx*B,0])
near('27.1 electron force reverses',-q*np.cross([vx,0,vz],[0,0,B]),[0,4.8e-14,0])
for angle in[0,10,30,60,89,90]:
 a=math.radians(angle)
 near('27loop complementary sine '+str(angle),math.sin(math.pi/2-a),math.cos(a),scale=1)
 for I,b,B in[(.3,.04,.7),(3,2,5)]:
  near('27loop sideforce '+str((angle,I,b,B)),I*b*B*math.sin(math.pi/2-a),I*b*B*math.cos(a),scale=I*b*B)
historical_ratio=1.758820024e11;historical_mass=9.10938356e-31;historical_e=1.6021766208e-19
near('27.13 printedcharge/mass ratio',historical_e/historical_mass,historical_ratio,tol=1e-9)
for accel_voltage,Bsel in[(500,.001),(2000,.004),(80,.02)]:
 speed=math.sqrt(2*historical_e*accel_voltage/historical_mass)
 Esel=speed*Bsel
 near('27.15 independent selectedvelocity derivation',Esel**2/(2*accel_voltage*Bsel**2),historical_ratio,tol=1e-9)
V,I,r=120,4,2;back=V-I*r;Pin=V*I;heat=I*I*r;mech=back*I
near('27.11 backEMF',back,112)
near('27.11 source power',Pin,480)
near('27.11 coil heat',heat,32)
near('27.11 mechanical power',mech,448)
near('27.11 energy balance',Pin,heat+mech)
near('27.11 mechanical efficiency',mech/Pin,448/480)
near('27.11 stalledcurrent',V/r,60)
near('27.11 stalledheat',(V/r)**2*r,7200)
near('27.11 stalledsourcepower',(V/r)*V,(V/r)**2*r)
t,w=2e-3,1.5e-2;area=t*w;current=75;J=current/area;By=.4;q_e=-1.6e-19;Ez=.81e-6/w
n=-J*By/(q_e*Ez);drift=J/(n*q_e)
near('27.12 geometric area',area,3e-5)
near('27.12 currentdensity',J,2.5e6)
near('27.12 measuredHallfield',Ez,5.4e-5)
near('27.12 groupedexponents',((2.5*.4)/(1.6*5.4))*1e30,n)
near('27.12 carrier density',n,1.1574074074074075e29)
near('27.12 Hallforce cancellation',Ez+drift*By,0,scale=Ez)
near('27.12 implieddrift',drift,-.000135)
files=['02-tu-truong.md','05-ung-dung.md','07-vong-day-mo-men.md','08-dong-co-dien.md','09-hieu-ung-hall.md']
paths=['raw_materials/physics/translations/chapter-27/'+n for n in files]
mass_source=(ROOT/paths[1]).read_text(encoding='utf8')
assert '1{,}758820024(11)'in mass_source and '9{,}10938356(11)'in mass_source
records.append({'name':'Sourceallprecisionanduncertaintydigits retained','passed':True})
report={'status':'passed-scoped-chapter27-physicalchecks','checks':len(records),'records':records,
 'sourceSHA256':{p:hashlib.sha256((ROOT/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()for p in paths},
 'scopeLimit':'Onlythechangedtheoretical expressions and worked-example transformations. Fullsource/content/figure/exercise/Wiki/cheatsheet and actualviewport acceptance remain separate.'}
(OUT/'numeric-checks.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(records),'independent Lorentz, loop, motor andHall checks.')
