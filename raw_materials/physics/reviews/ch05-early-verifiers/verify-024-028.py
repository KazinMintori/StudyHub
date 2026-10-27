from pathlib import Path
import hashlib,json,math,re,xml.etree.ElementTree as ET
import pymupdf
ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-early-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);R=B/'review-024-028'
text=(B/'parent-11-bai-tap-001-059.md').read_text(encoding='utf8');checks=[]
def yes(name,value):
    assert value,name
    checks.append(dict(name=name,passed=True))
def near(name,actual,expected,tol=1e-9):
    assert math.isclose(float(actual),float(expected),rel_tol=tol,abs_tol=tol),(name,actual,expected)
    checks.append(dict(name=name,actual=float(actual),expected=float(expected)))
us,uk=75/135,50/135
near('24 actual static coefficient',us,5/9);near('24 actual kinetic coefficient',uk,10/27)
for W,speak,plateau in [(135,75,50),(270,150,100)]:
    near('24 actual static peak'+str(W),us*W,speak);near('24 kinetic plateau'+str(W),uk*W,plateau)
    for P in [0,25,speak]:
        yes('24 rest equilibrium within bound'+str((W,P)),P<=us*W)
near('25 actual applied force',.2*16.8*9.8,32.928)
near('25 stopping distance',3.5**2/(2*.2*9.8),3.125)
near('25 kinetic work removes initial energy',.2*16.8*9.8*3.125,.5*16.8*3.5**2)
near('26 critical force',.4*40,16);near('26 sliding friction',.2*40,8)
for P,friction,moving in [(0,0,False),(6,6,False),(16,16,False),(18,8,True)]:
    yes('26 actual regime'+str(P),P>.4*40 if moving else P<=.4*40)
    near('26 actual friction'+str(P),.2*40 if moving else P,friction)
near('26 acceleration at18N',(18-8)*9.8/40,2.45)
mu_s,mu_k=313/(45*9.8),208/(45*9.8)
near('27 actual static coefficient',mu_s,.709750566893424)
near('27 actual kinetic coefficient',mu_k,.4716553287981859)
near('27 exact required moving force',208+45*1.1,257.5)
near('27 lunar critical force unrounded',mu_s*45*1.62,51.74081632653061)
near('27 lunar sliding friction unrounded',mu_k*45*1.62,34.38367346938775)
near('27 lunar acceleration from actual force',(257.5-mu_k*45*1.62)/45,4.958140589569161)
yes('27 same applied force can start motion on Moon but not at rest on Earth',51.74081632653061<257.5<313)
theta=math.pi/3;coef=math.sin(theta)+.5*math.cos(theta)
near('28 incline coefficient',coef,1.1160254037844386)
near('28 actual ratio',.5/coef,.4480184754795918)
for W0 in [100,600,1000]:
    F=.5*W0;W=F/coef
    near('28 Newton incline equilibrium W0='+str(W0),F-W*math.sin(theta)-.5*W*math.cos(theta),0)
    near('28 proportional personal estimate W0='+str(W0),W/W0,.4480184754795918)
lbf=.45359237*9.80665
near('28 sample pound force conversion',(300/coef)/lbf,60.43113597702636)
near('28 sample level pound force',600/lbf,134.8853658598263)
ns={'s':'http://www.w3.org/2000/svg'}
svg=ET.parse(ROOT/'docs/vat-ly-1/bai-giang/img/young-05/solution-s5-24-graph.svg').getroot()
expected={'static':[[0,0],[150,150]],'transition':[[150,150],[150,100]],'kinetic':[[150,100],[300,100]]}
vertices=0
for series,data in expected.items():
    line=next(x for x in svg.findall('.//s:polyline',ns) if x.get('data-series')==series)
    actual=[tuple(map(float,p.split(','))) for p in line.get('points').split()]
    yes('24 answer plot all vertices '+series,len(actual)==len(data))
    for i,((x,y),(p,f)) in enumerate(zip(actual,data)):
        near('24 plot actual P '+series+str(i),(x-60)*300/244,p,1e-6)
        near('24 plot actual friction '+series+str(i),(335-y)*180/250,f,1e-6)
        vertices+=1
near('24 six plotted physical vertices',vertices,6)

report={'status':'passed','scope':'Independent physical computations and actual SVG geometry; full source/crop/structure binding handled by canonical entrypoint.','checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'numeric-024-028.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS 024-028',len(checks),'physical/geometry checks.')
