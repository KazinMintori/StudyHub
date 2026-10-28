"""Independent geometric-optics models for source-preserving mobile repairs."""
from pathlib import Path
import math,json,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch34-theory-layout-repair-20261028';OUT.mkdir(exist_ok=True)
records=[]
def near(name,a,b,tol=1e-10,scale=None):
 a,b=np.asarray(a,dtype=float),np.asarray(b,dtype=float);ref=max(np.max(np.abs(a)),np.max(np.abs(b)),scale or 0,1e-300)
 assert np.allclose(a/ref,b/ref,rtol=tol,atol=tol),(name,a,b)
 records.append({'name':name,'actual':a.tolist(),'expected':b.tolist(),'physicalScale':float(ref)})
Rx=np.diag([-1,1]);Ry=np.diag([1,-1])
for point in[(1,2),(-3,5),(.2,-.8),(0,0)]:
 p=np.array(point)
 near('34two orthogonal reflections xy '+str(point),Rx@Ry@p,-p,scale=1)
 near('34two orthogonal reflections yx '+str(point),Ry@Rx@p,-p,scale=1)
s,sp=10,300;curvature=2/(1/s+1/sp)
near('34mirror radius reciprocalsum',curvature,19.35483870967742)
near('34mirror inverse object',1/s,.100)
near('34mirror inverse image',1/sp,.00333,tol=.001)
near('34mirror radius round',curvature,19.4,tol=.003)
near('34mirror imageheight',(-30)*.5,-15)
f,s=-1.8,75;sp=1/(1/f-1/s)
near('34convex mirror image',sp,-1.7578125)
near('34convex mirror negative image root',1/s+1/sp,1/f)
for na,nb,R,s in[(1,1.52,2,8),(1.33,1.52,2,8)]:
 P=(nb-na)/R;Q=na/s;sp=nb/(P-Q)
 # Direct paraxial ray transfer: Two different initial ray heights agree on image.
 transfer=np.array([[1,0],[-(nb-na)/(nb*R),na/nb]])
 image_distances=[]
 for height in[.001,.004,.008]:
  incoming=np.array([height,height/s]);outgoing=transfer@incoming
  image_distances.append(-outgoing[0]/outgoing[1])
 near('34surface image independentraytransfer '+str(na),image_distances,[sp]*3)
 near('34surface source imaging equation '+str(na),na/s+nb/sp,(nb-na)/R)
 near('34surface grouped components '+str(na),nb/sp,P-Q)
 near('34surface magnification '+str(na),-na*sp/(nb*s),-(na/nb)*sp/s)
near('34air caseP',(.52)/2,.260)
near('34water caseP',(.19)/2,.095)
near('34water caseQ',1.33/8,.16625)
for n,R1,R2 in[(1.52,10,-10),(1.52,-10,10),(1.4,8,-6),(1.6,-8,7)]:
 P1=(n-1)/R1;P2=-(n-1)/R2
 near('34lensmaker summing surfaces '+str((n,R1,R2)),P1+P2,(n-1)*(1/R1-1/R2))
 f=1/(P1+P2)
 near('34thin lens focal length '+str((n,R1,R2)),1/f,P1+P2)
 for s in[15,50,100]:
  if abs((P1+P2)-1/s)<1e-12:continue
  sp=1/((P1+P2)-1/s);intermediate=n/(P1-1/s)
  near('34twointerfaces eliminatemiddleimage '+str((n,R1,R2,s)),1/s+1/sp,P1+P2)
  near('34second surface equation '+str((n,R1,R2,s)),-n/intermediate+1/sp,P2)
near('34positive symmetriclens focal',1/(.52*(1/10-1/-10)),9.615384615384615)
near('34negative symmetriclens focal',1/(.52*(1/-10-1/10)),-9.615384615384615)
near('34diverging lens objectposition',-2*(-20),40)
near('34combinedmagnification',(-2)*(-1),2)
near('34final imageheight',2*8,16)
stops=[1.4,2,2.8,4,5.6,8,11,16,22]
assert len(stops)==9
for first,second in zip(stops,stops[1:]):
 near('34aperture halflight approximate stops '+str((first,second)),(first/second)**2,.5,tol=.07)
paths=['raw_materials/physics/translations/chapter-34/'+n for n in['01-guong-phang.md','02-guong-cau.md','03-khuc-xa-mat-cau.md','04-thau-kinh-mong.md','05-may-anh.md']]
result={'status':'passed-scoped-ch34-mirror-surface-lens-models','checks':len(records),'records':records,
 'sourceSHA256':{p:hashlib.sha256((ROOT/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()for p in paths},
 'scopeLimit':'Changedtheoretical expressions/modelsonly. Fullsource/figure/exercise/Wiki/cheatsheet andactualviewport acceptance remainseparate.'}
(OUT/'numeric-checks.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(records),'independentopticalmodel/units/sign checks.')
