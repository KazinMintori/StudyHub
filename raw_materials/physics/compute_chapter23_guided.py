from math import sqrt,log,pi
from pathlib import Path
import json
root=Path(__file__).resolve().parents[2]
k=8.987551787e9;e=1.602176634e-19;mp=1.672621898e-27
a={}
C=k*82*e*e
a['VP23.2.1']=[C*(1/1e-10-1/5e-10),C*(1/8e-12-1/5e-10)]
K=mp*2.5e6**2/2
a['VP23.2.2']=[K,K*5.29e-13/(k*e)]
q2=8.10e-6*.04/(k*5e-9);W=2e-9*k*(5e-9/.03+q2/.05)
a['VP23.2.4']=[q2,W]
a['VP23.7.1']=[25,15,0,-25]
a['VP23.7.2']=[k*12e-9/.03,k*12e-9/.05,k*6e-9*(1/.05+1/.11)]
Va=k*5.9e-9*(1/.08-1/.1);Vb=-Va
a['VP23.7.3']=[Va,Vb,sqrt(3e5**2+2*e*(Vb-Va)/mp)]
a['VP23.12.2']=[24*.003/.0045,2e-9*24*.003/.0045,sqrt(2*2e-9*24*.003/.0045/5e-9)]
C=k*5e-9*3e-9;Ua=C/sqrt(.08**2+.025**2);Ub=C/.025;Kb=4e-9*60**2/2+Ua-Ub
a['VP23.12.3']=[Ua,Ub,Kb,sqrt(2*Kb/4e-9)]
out=root/'qa/physics/chapter23';out.mkdir(parents=True,exist_ok=True)
(out/'guided-calculations.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(a,ensure_ascii=False,indent=2))
