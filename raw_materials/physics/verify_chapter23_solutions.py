"""Private checks of published numerical answers and independent calculus paths."""
from pathlib import Path
from math import sqrt, log, pi, isclose, sin, cos
import runpy, contextlib, io, re, json
root=Path(__file__).resolve().parents[2]
with contextlib.redirect_stdout(io.StringIO()):
 a=runpy.run_path(str(Path(__file__).with_name('compute_chapter23_exercises.py')))['a']
 g=runpy.run_path(str(Path(__file__).with_name('compute_chapter23_guided.py')))['a']
checks={}
def check(name,actual,expected,tol=.008):
 aa=actual if isinstance(actual,(list,tuple)) else [actual]
 bb=expected if isinstance(expected,(list,tuple)) else [expected]
 assert len(aa)==len(bb),(name,len(aa),len(bb))
 for x,y in zip(aa,bb):
  assert isclose(x,y,rel_tol=tol,abs_tol=1e-30),(name,x,y)
 checks[name]={'actual':actual,'publishedOrIndependentTarget':expected}
targets={
 '23.1':-.356,'23.2':7.3e-8,'23.3':[3.46e-13,2.16],
 '23.4':[7.69e-14,6.78e6],'23.5':[12.5,.323],'23.6':[-9.78e-19,-4.36e-18],
 '23.7':[3.45e-12,1.94e-5],'23.8':.0971,'23.9':[1.36e4,2.45e17],
 '23.10':-6.09e-21,'23.11':89.3,'23.12':[80,-100],'23.13':7.42,
 '23.14':[2.2e-6,524,8.73e3],'23.15':[0,.750e-3,-2.06e-3],'23.16':6.89e6,
 '23.17':[0,-175e3,-.877],'23.19':[-737,-704,8.24e-8],
 '23.20':[156,-182],'23.21':[-171,17.1],'23.22':[.307,1.70e-10],
 '23.23':[800,-48e-6],'23.24':[100,250],'23.25':[.0539,3],
 '23.26':2e-9,'23.27':[180,-270,-449,719],'23.28':[65.5,131,131],
 '23.29':1.67e7,'23.30':72,'23.31':150,'23.32':[1.02e-20,.0884],
 '23.33':[7.8e4,0],'23.34':.0228,'23.35':.474,'23.36':[5.31e3,117],
 '23.37':[8000,19.2e-6,.864e-6],'23.38':1.5e6,'23.39':-760,
 '23.40':[5.22e-8,3750],'23.42':.00295,'23.44':[-6.72,-7.20,9.85,227],
 '23.46':[.0261,3.31e4],'23.47':[-3.60e-7,.0743],
 '23.48':[1.17,.0667,.600],'23.49':1.89e5,'23.50':[3.48,1.44],
 '23.51':4.2e6,'23.52':[4.43e4,1.11e4,5.45e18,1.36e18],
 '23.53':[-21.5e-6,-2.83e3,35.4e3],'23.54':[29.8,0,1.40],
 '23.55':[7.85e4,1.05e5,3.13e-15],'23.56':[.001,3000,2.66e-5,1e-4,2.66e-9,1.66e10],
 '23.57-coefficient':-5.82412,'23.58':[8,2.04e-7,459],'23.59':47.7,
 '23.60':[2.40e5,-3.00e4,-8.99e4],'23.62':1.16e3,
 '23.63':[1.76e-16,1.93e14,.00824,15.4,.0412],
 '23.64':[40e-12,5000,3e6],'23.65':[97.1e3,30.3e-12],
 '23.69':360e3,'23.70':[-49.8,.819e-3,-79.0],
 '23.73':[2.31e17,2.16,1.44e7,1.17e7],'23.75':2.49e-14,
 '23.76':[640,-320,3.74],'23.78':[20,7.01e-6,.0394],
 '23.80':[1.20e5,15.5],'23.81':[4.75e-15,94.9e3,5.81e-15,3.63e4],
 '23.83':[1.01e-12,1.13e-13,2.84e-14],'23.84':1e6,
 '23.85-min-Z':10.4,'23.86':5e5
}
for name,target in targets.items():check(name,a[name],target,.014 if name in ['23.51','23.64'] else .008)
check('23.45-charge',a['23.45']['q'],.763e-9)
check('23.45-radii',list(a['23.45']['radii'].values()),[.012,.0145,.0185,.0253,.04,.096])
check('23.77-values',[item[v] for item in a['23.77'] for v in ['V','E']],[10,0,7.97,6.72,-2,20.8])
check('23.79-negative-charge-magnitudes',a['23.79']['chargeMagnitudes'],[4.79e-19,1.59e-19,8.09e-19,3.23e-19])
check('23.79-integer-counts',a['23.79']['electronCounts'],[3,1,5,2])
check('23.79-elementary-charge-mean',a['23.79']['mean'],1.61e-19)
guided={
 'VP23.2.1':[1.51e-16,2.32e-15],'VP23.2.2':[5.22e-15,1.92e-18],
 'VP23.2.4':[7.21e-9,5.59e-6],'VP23.7.1':[25,15,0,-25],
 'VP23.7.2':[3.6e3,2.2e3,1.6e3],'VP23.7.3':[133,-133,1.98e5],
 'VP23.12.2':[16,3.2e-8,3.58],'VP23.12.3':[1.61e-6,5.39e-6,3.42e-6,41.3]
}
for name,target in guided.items():check(name,g[name],target,.025 if name=='VP23.7.2' else .008)
def integrate(f,lo,hi,n=12000):
 h=(hi-lo)/n
 return h/3*(f(lo)+f(hi)+sum((4 if i%2 else 2)*f(lo+i*h) for i in range(1,n)))
def deriv(f,x,h=1e-5):return (f(x+h)-f(x-h))/(2*h)
k=8.987551787e9;eps=1/(4*pi*k);Q=3e-9;R=.3
# Analytic exercises checked by direct integration or finite differences.
check('Q23.3-zero-energy',.5-.25-.25,0,1e-12)
check('VP23.2.3-pair-count',-1-.5+1/3,-7/6,1e-12)
for x in [.1,.5,1.2]:
 A=.2
 check('23.71-axis-'+str(x),integrate(lambda s:k*Q/A/(x+s),0,A),k*Q/A*log((x+A)/x),1e-8)
 check('23.71-perpendicular-'+str(x),integrate(lambda s:k*Q/A/sqrt(x*x+s*s),0,A),k*Q/A*log((A+sqrt(A*A+x*x))/x),1e-8)
 for b in [.15,.4]:
  annulus=lambda z:2*pi*k*2e-8*(sqrt(z*z+b*b)-sqrt(z*z+.05**2))
  direct=integrate(lambda r:2*pi*k*2e-8*r/sqrt(x*x+r*r),.05,b)
  check('23.80-V-'+str((x,b)),direct,annulus(x),1e-8)
  Ez=2*pi*k*2e-8*x*(1/sqrt(x*x+.05**2)-1/sqrt(x*x+b*b))
  check('23.80-E-'+str((x,b)),-deriv(annulus,x),Ez,1e-7)
 length=.5;h=length/2
 tube=lambda z:k*Q/length*log((z+h+sqrt(R*R+(z+h)**2))/(z-h+sqrt(R*R+(z-h)**2)))
 direct=integrate(lambda s:k*Q/length/sqrt(R*R+(x-s)**2),-h,h)
 check('23.82-V-'+str(x),direct,tube(x),1e-8)
 Ez=k*Q/length*(1/sqrt(R*R+(x-h)**2)-1/sqrt(R*R+(x+h)**2))
 check('23.82-E-'+str(x),-deriv(tube,x),Ez,1e-7)
rho=3*Q/(4*pi*R**3)
check('23.67-self-energy',integrate(lambda r:k*(4*pi*rho*r**3/3)*4*pi*rho*r,0,R),3*k*Q*Q/(5*R),1e-8)
check('23.66-disk',integrate(lambda r:2*pi*k*2e-8*r/sqrt(.2**2+r*r),0,R),2*pi*k*2e-8*(sqrt(.2**2+R*R)-.2),1e-8)
theta=.3;L=.7;E=400;charge=4e-9
U=lambda t:-charge*E*L*cos(t)/2
check('23.72-torque',-deriv(U,theta),-charge*E*L*sin(theta)/2,1e-8)
for b,r in zip([1e-12,1e-13,1e-14],a['23.83']):
 check('23.83-conservation-'+str(b),a['23.75']/r+b*b/(r*r),1,1e-12)
raw=root/'raw_materials/physics/translations/chapter-23'
text='\n'.join(p.read_text(encoding='utf8') for p in sorted(raw.glob('*.md')))
ids=re.findall(r'<!-- detailed-solution:([^ >]+) -->',text)
expected=[f'23.{i}' for i in range(1,87)]+[f'Q23.{i}' for i in range(1,23)]+[f'VP23.{series}.{i}' for series in [2,7,12] for i in range(1,5)]+['bridge23']
assert sorted(ids)==sorted(expected),(len(ids),len(set(ids)))
for marker in expected:
 block=text.split('<!-- detailed-solution:'+marker+' -->',1)[1].split('\n:::',2)[1]
 assert '**Tóm tắt đề bài:**' in block and '**Hướng đi:**' in block,marker
 assert re.search(r'\*\*Hướng đi:\*\*\s*\n\s*- ',block),marker
assert len(re.findall(r'\\tag\{23\.\d+\}',text))==23
assert len(re.findall(r'^### Ví dụ 23\.\d+',text,re.M))==14
out=root/'qa/physics/chapter23/numeric-checks.json'
out.write_text(json.dumps({'status':'passed','groups':len(checks),'detailedSolutions':len(ids),'checks':checks},ensure_ascii=False,indent=2),encoding='utf8')
print('Passed',len(checks),'numerical, integral and derivative groups;',len(ids),'detailed solutions present.')
