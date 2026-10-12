from pathlib import Path
from math import sqrt, isclose
import json
root=Path(__file__).resolve().parents[2]
checks={}
def check(name,values,targets,tol=.005):
    for a,b in zip(values,targets):
        assert isclose(a,b,rel_tol=tol,abs_tol=1e-15),(name,a,b)
    checks[name]=values
check('VP25.3.1',[1.45/35,1.45/1.2,2.75e-8*35/(1.45/1.2)],[.0414,1.21,7.97e-7])
check('VP25.3.2',[.0065*20/.218,(.0065*20/.218)*8.19e-7/20],[.596,2.44e-8])
check('VP25.3.3',[2/4,1/(2/4),2/4,1/2],[.5,2,.5,.5])
check('VP25.3.4',[1.5/2.4,1.5/2,((1.5/2)/(1.5/2.4)-1)/60],[.625,.750,.00333])
I=9/16.4
check('VP25.5.1',[I,I*15.3,9-I*1.1],[.549,8.40,8.40])
check('VP25.5.2',[.480*25,(12.6-.480*25)/.480],[12,1.25])
I=1.3/20
check('VP25.5.3',[I,(1.5-1.3)/I],[.065,3.08])
check('VP25.5.4',[1.5/2-.160,1.5-2*.160],[.590,1.18])
I=24/19.3
check('VP25.9.1',[I,24*I,I*I*1.3,24*I-I*I*1.3,I*I*18],[1.24,29.8,2.01,27.8,27.8])
assert isclose(24*I, I*I*1.3+I*I*18,rel_tol=1e-14)
I=sqrt(6.54/12)
check('VP25.9.2',[I,6.54,I*12,(9-I*12)/I],[.738,6.54,8.86,.191])
I=.720;r=(12-I*16)/I
check('VP25.9.3',[I*16,r,I*I*16,12*I,I*I*r],[11.52,.667,8.29,8.64,.346])
assert isclose(12*I,I*I*r+I*I*16,rel_tol=1e-14)
for x in [.01,.25,.5,.999]:
    ratio_I=(1+x)/(2+x)
    ratio_P=2*ratio_I**2
    assert ratio_I<1 and ratio_P<1
checks['VP25.9.4']={'ratioCurrent':'(R+r)/(2R+r)','ratioPower':'2*(R+r)^2/(2R+r)^2','checked_r_R':[.01,.25,.5,.999]}
check('bridge',[20+(1.35/1.23-1)/4.5e-4,120*1.35,120*1.23,120/1.35,120/1.23],[236.8,162,147.6,88.889,97.561])
out=root/'qa/physics/chapter25';out.mkdir(parents=True,exist_ok=True)
(out/'guided-checks.json').write_text(json.dumps({'status':'passed','groups':len(checks),'checks':checks},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Passed',len(checks),'guided numerical and inequality groups.')
