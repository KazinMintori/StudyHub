"""Recalculate numerical exercises 29.1–29.30 from their stated data."""
from pathlib import Path
import math,json
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
mu0=4*math.pi*1e-7
results={}
def put(n,**values):results[str(n)]=values
put(1,emf=.0900*.190,current=.0900*.190/.600)
flux=6e-5*12e-4;put(2,initialFlux=flux,finalFlux=0.,averageEmf=200*flux/.040)
a=1.60;b=a/(3*.5**2);put(3,a=a,b=b,emfAt025=-a+3*b*.25**2)
put(4,charge=150*4.50e-4*.200/30)
put(5,averageEmf=1.5*math.pi*.12**2/.002)
emf6=500*math.pi*.04**2*(.012+12e-5*5**3);put(6,emfAt5=emf6,currentAt5=emf6/600)
put(7,emf=mu0*.24/(2*math.pi)*math.log(.36/.12)*9.60)
put(8,initialEmf=math.pi*.75**2*1.4*.057*math.cos(math.radians(30)),timeToTenth=math.log(10)/.057)
circ=1.650-.120*9;put(9,circumferenceAt9=circ,emf=.500*circ*.120/(2*math.pi))
put(10,averageEmf=80*.25*.40*1.70*(1-math.sin(math.radians(37)))/.0600)
imax=math.pi*.02**2*3/(.6*.5);put(11,maximumCurrent=imax,currentAt15=imax*math.exp(-1.5/.5))
put(13,angularSpeed=.024/(120*.075*.016**2))
emf14=math.pi*.048**2*.680;put(14,emf=emf14,power=emf14**2/.160)
time22=(1.33/.380)**(1/3);put(22,time=time22,current=math.pi*.025**2*3*.380*time22**2/.390)
cross=np.cross([18.,24.,72.],[0.,.080,0.]);put(23,crossProduct=cross.tolist(),emfAlongZ=cross[2]*.50,emfAlongY=cross[1]*.50)
# E29.24: the short vertical side is 1.50 cm.
put(24,force=2.40**2*.015**2*3/.600)
put(25,potentialDifference=.450*5*.300,electricField=.450*5)
put(26,emfWhenPartial=1.25*.400*.0200)
emf27=.800*.500*7.50;current27=emf27/1.50;force27=current27*.500*.800
put(27,emf=emf27,current=current27,force=force27,mechanicalPower=force27*7.50,thermalPower=current27**2*1.50)
put(28,emf=.750*.650*5.0,current=.750*.650*5.0/25.0)
emf29=.650*.360*5.90;put(29,emf=emf29,power=emf29**2/45.)
put(30,speed=math.sqrt(.840*45)/(.650*.360))
expected={1:{'emf':.0171,'current':.0285},2:{'initialFlux':7.2e-8,'averageEmf':.00036},
3:{'emfAt025':-1.20},4:{'charge':.000450},5:{'averageEmf':33.92920066},
6:{'currentAt5':.0001130973355},7:{'emf':5.062405427e-7},
8:{'initialEmf':.1221252079,'timeToTenth':40.3962297},9:{'emf':.00544309905},
10:{'averageEmf':90.2552614},11:{'maximumCurrent':.01256637061,'currentAt15':.000625642753},
13:{'angularSpeed':10.4166666667},14:{'power':.000151411209},
22:{'current':.01323067995},23:{'emfAlongZ':.720,'emfAlongY':0.},24:{'force':.00648},
25:{'potentialDifference':.675,'electricField':2.25},26:{'emfWhenPartial':.0100},
27:{'emf':3.,'current':2.,'force':.800,'mechanicalPower':6.,'thermalPower':6.},
28:{'emf':2.4375,'current':.09750},29:{'power':.042357768},30:{'speed':26.274}}
for n,values in expected.items():
 for key,target in values.items():
  actual=results[str(n)][key]
  if not math.isclose(actual,target,rel_tol=3e-4,abs_tol=1e-12):
   raise AssertionError((n,key,actual,target))
out=ROOT/'qa/physics/chapter29';out.mkdir(parents=True,exist_ok=True)
(out/'exercises01-30-checks.json').write_text(json.dumps({'status':'passed','results':results},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(results,ensure_ascii=False,indent=2))
