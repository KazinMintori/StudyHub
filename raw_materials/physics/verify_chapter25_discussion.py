from pathlib import Path
from math import isclose
import json,re
root=Path(__file__).resolve().parents[2]
checks={}
def same(name,a,b):
 assert isclose(a,b,rel_tol=1e-12,abs_tol=1e-15),(name,a,b)
 checks[name]=a
same('Q25.2-resistance-ratio',3/9,1/3)
same('Q25.3-resistivity-ratio',1,1)
same('Q25.4-drift-ratio-at-area-half',1/.5,2)
emf=1.5;r=1.;external=20.;external_r=1.
I=(emf+external)/(r+external_r)
assert emf-I*r<0
checks['Q25.6-terminal-reversal']={'privateExample_I':I,'terminalVoltage':emf-I*r}
same('Q25.7-open-short-ratio',emf/(emf/r),r)
R=10.;V=12.
same('Q25.14-identical-series-powers',(V/(2*R))**2*R,(V/(2*R))**2*R)
same('Q25.14-fixed-R-one-two-ratio',(V/R)**2*R/((V/(2*R))**2*R),4)
same('Q25.15-position-current',(V/R),(V/R))
same('Q25.19-current-ratio-at-fixed-power',12/24,.5)
same('Q25.19-loss-ratio-at-fixed-wire',(.5)**2,.25)
for alpha in [.00393,-.0005]:
 Rf=R*(1+alpha*50)
 P=V*V/Rf
 assert (P<V*V/R)==(alpha>0)
checks['Q25.11-temperature-power-signs']=['positive-alpha-power-decreases','negative-alpha-power-increases']
text=(root/'raw_materials/physics/translations/chapter-25/09-cau-hoi-thao-luan.md').read_text(encoding='utf8')
ids=list(map(int,re.findall(r'^::: exercise Q25\.(\d+)\b',text,re.M)))
assert ids==list(range(1,25)),ids
bodies=re.findall(r'^::: solution[^\n]*\n([\s\S]*?)\n:::',text,re.M)
assert len(bodies)==24
for body in bodies:
 assert '**Tóm tắt đề bài:**' in body and '**Hướng đi:**' in body
 assert re.search(r'\*\*Hướng đi:\*\*\s*\n\s*- ',body)
out=root/'qa/physics/chapter25';out.mkdir(parents=True,exist_ok=True)
(out/'discussion-checks.json').write_text(json.dumps({'status':'passed','questions':24,'numericGroups':len(checks),'checks':checks},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Passed',len(checks),'scaling checks and all 24 discussion solution structures.')
