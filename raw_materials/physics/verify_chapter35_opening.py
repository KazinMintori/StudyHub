"""Check the three independent factors in normal-incidence film reflection."""
from pathlib import Path
import json,cmath,math
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter35';q.mkdir(parents=True,exist_ok=True)
def reflect(n0,n1,n2,t,lam):
 r01=(n0-n1)/(n0+n1);r12=(n1-n2)/(n1+n2)
 phase=cmath.exp(4j*math.pi*n1*t/lam)
 return abs((r01+r12*phase)/(1+r01*r12*phase))**2
# Exactlosslessfilmamplitudes demonstrate eachfactor without relyingonlyonraywording.
base=(1.,1.45,1.33,380e-9,550e-9)
v=reflect(*base)
changes={}
for index,name,value in [(3,'thickness',250e-9),(1,'filmIndex',1.60),(2,'substrateIndex',1.60)]:
 args=list(base);args[index]=value;answer=reflect(*args);assert abs(answer-v)>1e-6
 changes[name]={'baseReflectance':v,'changedReflectance':answer}
(q/'opening-data-checks.json').write_text(json.dumps({'status':'passed','openingChoice':'v','independentFactors':changes,'publicationNarration':False},indent=2),encoding='utf-8')
print('Openinganswerchecked: Filmthickness,filmindexandsubstrateindexindependentlyaffectreflection.')
