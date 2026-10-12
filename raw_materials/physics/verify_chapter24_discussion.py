from pathlib import Path
from math import isclose
import json,re
root=Path(__file__).resolve().parents[2];eps=8.8541878128e-12
A=.01;d=.001;V=10;K=3
C=eps*A/d;Q=C*V;E=V/d;U=C*V*V/2;u=eps*E*E/2
checks={}
def check(name,actual,target):
 aa=actual if isinstance(actual,(list,tuple)) else [actual]
 bb=target if isinstance(target,(list,tuple)) else [target]
 assert len(aa)==len(bb)
 for x,y in zip(aa,bb):assert isclose(x,y,rel_tol=1e-10,abs_tol=1e-30),(name,x,y)
 checks[name]={'actual':actual,'expected':target}
C2=eps*A/(2*d)
check('Q24.6-fixed-V',[(V/(2*d))/E,(C2*V)/Q,(C2*V*V/2)/U],[.5,.5,.5])
check('Q24.7-fixed-Q',[(Q/(eps*A))/E,(Q/C2)/V,(Q*Q/(2*C2))/U],[1,2,2])
check('Q24.8-small-v-large',[(V/d)/(V/(2*d)),C/C2,(eps*(V/d)**2/2)/(eps*(V/(2*d))**2/2)],[2,2,4])
Wext=Q*Q/(2*eps*A)*d
check('Q24.9-isolated-energy',Q*Q/(2*C2)-Q*Q/(2*C),Wext)
WextV=eps*A*V*V/2*(1/d-1/(2*d));Wsource=V*(C2*V-C*V)
deltaU=(C2-C)*V*V/2
check('Q24.9-source-energy-balance',WextV+Wsource,deltaU)
check('Q24.12-MV-conversions',[3e7/1e6,2e7/1e6,1e7/1e6],[30,20,10])
check('Q24.17-flux',[E/K*A/(E*A),K*E/K*A/(E*A)],[1/K,1])
check('Q24.18-fixed-V',[E/E,(K*C*V)/Q,(K*C*V*V/2)/U],[1,K,K])
check('Q24.18-fixed-Q',[(Q/(K*eps*A))/E,Q/Q,(Q*Q/(2*K*C))/U],[1/K,1,1/K])
p=root/'raw_materials/physics/translations/chapter-24/09-cau-hoi-thao-luan.md'
text=p.read_text(encoding='utf8')
ids=re.findall(r'<!-- detailed-solution:Q24\.(\d+) -->',text)
assert [int(i) for i in ids]==list(range(1,22))
for body in re.findall(r'<!-- detailed-solution:Q24\.\d+ -->\s*::: solution[^\n]*\n([\s\S]*?)\n:::',text):
 assert '**Tóm tắt đề bài:**' in body
 assert re.search(r'\*\*Hướng đi:\*\*\s*\n\s*- ',body)
out=root/'qa/physics/chapter24/discussion-checks.json'
out.write_text(json.dumps({'status':'passed','groups':len(checks),'questions':len(ids),'checks':checks},ensure_ascii=False,indent=2),encoding='utf8')
print('Passed',len(checks),'scaling and energy checks; all 21 discussion solutions have the requested structure.')
