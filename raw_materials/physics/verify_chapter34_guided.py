"""All12 Guided Practice cases and independent four-surface wine-goblet tracing."""
from pathlib import Path
import math,json
import numpy as np

root=Path(__file__).resolve().parents[2]
r={}
def image(f,s):
 sp=1/(1/f-1/s)
 m=-sp/s
 assert math.isclose(1/s+1/sp,1/f,rel_tol=1e-12,abs_tol=1e-12)
 return {'objectDistanceCm':s,'imageDistanceCm':sp,'magnification':m,'realImage':sp>0,'erect':m>0,'larger':abs(m)>1+1e-12,'smaller':abs(m)<1-1e-12,'sameSize':math.isclose(abs(m),1.,rel_tol=1e-12)}
f=1/(1/15+1/450)
r['VP34.4.1']={'focalLengthCm':f,'radiusCm':2*f,**image(f,15)}
r['VP34.4.2']=[image(37/2,s) for s in [11,31,55]]
f=-44/2;sp=-18;s=1/(1/f-1/sp)
r['VP34.4.3']={'type':'convex',**image(f,s)}
r['VP34.4.4']=[image(-37/2,s) for s in [11,31,55]]
r['VP34.8.1']={'frontRadiusCm':2*(1.65-1)*30,'backRadiusCm':-2*(1.65-1)*30}
for key,R1,R2 in [('VP34.8.2',15,25),('VP34.8.3',25,15)]:
 f=1/((1.55-1)*(1/R1-1/R2))
 r[key]={'frontRadiusCm':R1,'backRadiusCm':R2,'focalLengthCm':f,'type':'converging' if f>0 else 'diverging','thicker':'center' if f>0 else 'edges'}
R2=1/(1/28-1/(14*(1.70-1)))
r['VP34.8.4']={'backRadiusCm':R2,'backShape':'convex','focalLengthCm':14}
r['VP34.10.1']=image(25,15)
f=1/(1/28+1/42);r['VP34.10.2']={'focalLengthCm':f,**image(f,28)}
r['VP34.10.3']={'type':'converging','focalLengthCm':24,**image(24,48)}
s=250;m=4/20;sp=-m*s;f=1/(1/s+1/sp)
r['VP34.10.4']={'focalLengthCm':f,'type':'diverging',**image(f,s)}
bridge={}
for fill in [1.,1.37]:
 positions=[0.,.6,7.4,8.]
 radii=[4.,3.4,-3.4,-4.]
 indices=[1.,1.5,fill,1.5,1.]
 previous_image=math.inf;steps=[];matrix=np.eye(2)
 for j,(x,R) in enumerate(zip(positions,radii)):
  na,nb=indices[j:j+2]
  obj=math.inf if j==0 else x-previous_image
  denom=(nb-na)/R-(0 if math.isinf(obj) else na/obj)
  sp=nb/denom
  previous_image=x+sp
  assert math.isclose((0 if math.isinf(obj) else na/obj)+nb/sp,(nb-na)/R,abs_tol=1e-12)
  steps.append({'surface':j+1,'xCm':x,'radiusCm':R,'na':na,'nb':nb,'objectDistanceCm':None if math.isinf(obj) else obj,'imageDistanceCm':sp,'imageXCm':previous_image})
  if j:
   d=x-positions[j-1]
   matrix=np.array([[1.,d/na],[0.,1.]])@matrix
  matrix=np.array([[1.,0.],[-(nb-na)/R,1.]])@matrix
 ray_sp=float(-indices[-1]*matrix[0,0]/matrix[1,0])
 assert math.isclose(ray_sp,steps[-1]['imageDistanceCm'],rel_tol=1e-12)
 bridge[str(fill)]={'fillIndex':fill,'steps':steps,'finalDistanceFromExitCm':ray_sp,'finalPositionFromFirstSurfaceCm':previous_image,'realImage':ray_sp>0,'independentReducedAngleMatrix':matrix.tolist()}
assert math.isclose(bridge['1.0']['finalDistanceFromExitCm'],-38.,abs_tol=1e-10)
assert bridge['1.37']['finalDistanceFromExitCm']>0
q=root/'qa/physics/chapter34';q.mkdir(parents=True,exist_ok=True)
(q/'guided-data-checks.json').write_text(json.dumps({'status':'passed','guidedPractice':12,'bridgingProblems':1,'cases':r,'goblet':bridge},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(r,indent=2));print(json.dumps(bridge,indent=2))
