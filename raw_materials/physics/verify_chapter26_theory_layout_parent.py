"""Independent model checks for chapter26 source-preserving mobile formula repairs."""
from pathlib import Path
import math,hashlib,json,random
import numpy as np
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/ch26-theory-layout-repair-20261028';OUT.mkdir(exist_ok=True)
records=[]
def near(name,a,b,tol=1e-10,physical_scale=None):
 a,b=np.asarray(a,dtype=float),np.asarray(b,dtype=float)
 scale=max(np.max(np.abs(a)),np.max(np.abs(b)),physical_scale or 0,1e-300)
 assert np.allclose(a/scale,b/scale,rtol=tol,atol=tol),(name,a,b)
 records.append({'name':name,'actual':a.tolist(),'expected':b.tolist(),'physicalScale':float(scale)})
rng=random.Random(26)
for n in[2,3,4,8]:
 for j in range(5):
  Rs=np.array([rng.uniform(.2,20)for _ in range(n)]);V=rng.uniform(1,70)
  I=V/Rs.sum();drops=I*Rs
  near('26series voltage addition '+str((n,j)),drops.sum(),V)
  branch=V/Rs
  near('26parallel branch current addition '+str((n,j)),sum(branch),V*sum(1/Rs))
  gs=1/Rs;Req=1/gs.sum()
  near('26parallel inverse resistance '+str((n,j)),Req,1/(sum(branch)/V))
  near('26network power from branches '+str((n,j)),sum(branch**2*Rs),V*sum(branch))
near('26.1 parallel6and3',1/(1/6+1/3),2)
near('26.1 equivalent withseries4',1/(1/6+1/3)+4,6)
I=18/6;Vcb=I*2
near('26.1 current source',I,3)
near('26.1 branch drops',Vcb,6)
near('26.1 parallel currents',[Vcb/6,Vcb/3],[1,2])
near('26.1 branch conservation',Vcb/6+Vcb/3,I)
near('26.2 series bulbs',[8/(2+2),(8/(2+2))**2*2,2*(8/(2+2))**2*2],[2,8,16])
near('26.2 parallel bulbs',[8/2,(8/2)**2*2,2*(8/2)**2*2],[4,32,64])
near('26.1 selfcheck allfournetworks',[3,1/3,1+1/2,1/(1+1/2)],[3,1/3,1.5,2/3])
RA=4+7;RB=2+3;I=(12-4)/(RA+RB)
near('26.3 loop current',I,.5)
near('26.3 expanded loop residual',-I*4-4-I*7+12-I*2-I*3,0,physical_scale=12)
near('26.3 grouped loop same original',12-4,I*(RA+RB))
near('26.3 two paths same voltage',[I*7+4+I*4,12-I*2-I*3],[9.5,9.5])
near('26.3 grouped paths',[I*RA+4,12-I*RB],[9.5,9.5])
near('26.3 dissipated power',I*I*(4+7+2+3),4)
near('26.3 source power balance',12*I-4*I,I*I*(RA+RB))
Is=1+2;VL=2*3;r=(12-VL)/Is;Vr=1*1;emf=Vr-VL;Vs=Is*r
near('26.4 recovered unknowns',[Is,r,emf],[3,2,-5])
near('26.4 source loop',12-Is*r,2*3)
near('26.4 weakbattery loop',-emf+Vr-VL,0,physical_scale=6)
near('26.4 third loop',12-Vs-Vr+emf,0,physical_scale=12)
near('26.4 allpotential paths',[2*3,12-Is*r,-emf+Vr],[6,6,6])
near('26.5 source/heat/net',[12*Is,Is*Is*r,(12-Vs)*Is],[36,18,18])
near('26.5 load/storage balance',(12-Vs)*Is,2**2*3+1**2*1+abs(emf)*1)
mat=np.array([[2,0,-1],[0,3,2],[-1,1,-1]],float);rhs=np.array([13,13,0],float)
currents=np.linalg.solve(mat,rhs);I1,I2,I3=currents
near('26.6 independent matrix solution',currents,[6,5,-1])
near('26.6 first original voltage loop',I1*1+(I1-I3)*1,13)
near('26.6 second original voltage loop',I2*1+(I2+I3)*2,13)
near('26.6 original middle loop',-I1*1-I3*1+I2*1,0,physical_scale=13)
near('26.6 fivebranch currents',[I1,I2,I3,I1-I3,I2+I3],[6,5,-1,7,4])
near('26.6 equivalent resistance',13/(I1+I2),13/11)
near('26.6 power balance',13*(I1+I2),I1**2+I2**2+I3**2+(I1-I3)**2+2*(I2+I3)**2)
for _ in range(12):
 a,b,c=(rng.uniform(-9,9)for _ in range(3))
 original=-b-2*(b+c)+(a-c)+a
 near('26.2 selfcheck loop-difference grouping '+str(_),original,2*a-3*b-3*c,physical_scale=abs(a)+abs(b)+abs(c))
near('26.7 same voltage viaallpaths',[I3*1,-(I2+I3)*2+(I1-I3)*1],[-1,-1])
tau=10e6*1e-6;t=46
near('26RC actual time constant',tau,10)
near('26RC chargefraction',1-math.exp(-t/tau),.99,tol=.0001)
near('26RC currentfraction',math.exp(-t/tau),.010,tol=.006)
near('26RC fraction complement',(1-math.exp(-t/tau))+math.exp(-t/tau),1)
for R,C,Q in[(3,.2,.7),(1e4,1e-6,3e-6),(2e6,4e-9,8e-8)]:
 # Integrate on dimensionless time so the tiny SI scales remain observable.
 loss=quad(lambda u:math.exp(-2*u),0,np.inf)[0]*Q*Q/C
 near('26RC total resistor heat '+str((R,C,Q)),loss,Q*Q/(2*C))
paths=['raw_materials/physics/translations/chapter-26/'+n for n in['01-dien-tro-noi-tiep-song-song.md','02-quy-tac-kirchhoff.md','04-mach-rc.md']]
report={'status':'passed-ch26-theory-layout-physical-checks','checks':len(records),'records':records,
 'sourceSHA256':{p:hashlib.sha256((ROOT/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()for p in paths},
 'scopeLimit':'Onlythe changed theoretical equations and worked-example transformations. Fullsource/content/figure/exercise/support and actualviewport acceptance are separate.'}
(OUT/'numeric-checks.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(records),'independent circuit/model checks.')
