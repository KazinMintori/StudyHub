from pathlib import Path
import hashlib,json,math,re,xml.etree.ElementTree as ET
import numpy as np,pymupdf
ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-early-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);R=B/'review-042-048'
text=(B/'parent-11-bai-tap-001-059.md').read_text(encoding='utf8');checks=[]
def yes(name,value):
    assert value,name
    checks.append(dict(name=name,passed=True))
def near(name,actual,expected,tol=1e-9):
    assert math.isclose(float(actual),float(expected),rel_tol=tol,abs_tol=tol),(name,actual,expected)
    checks.append(dict(name=name,actual=float(actual),expected=float(expected)))
g=9.8
period=2*math.pi*math.sqrt(3/(.4*g))
near('42 actual minimum period',period,5.4966421292651315)
for mass in [30,60,90]:
    near('42 friction limit mass independence '+str(mass),mass*4*math.pi**2*3/period**2,.4*mass*g)
near('43 actual maximum speed',math.sqrt(60*.9/.8),8.215838362577491)
near('43 threshold centripetal force',.8*8.215838362577491**2/.9,60)
mass=.0125*52;omega=2*math.pi*2
fx=mass*omega**2*.75;w=mass*g
near('44 source hand mass',mass,.65)
near('44 actual horizontal wrist force',fx,76.98291432849699)
near('44 actual horizontal force/handweight ratio',fx/w,12.085229878884928)
near('44 actual vertical contact component',w,6.37)
yes('44 resultant is distinct from requested horizontal component',math.hypot(fx,w)>fx)
near('45 bottom normal',1.6*(12**2/5+g),61.76)
near('45 top normal',1.6*(12**2/5-g),30.4)
yes('45 positive contact at top',12**2/5>g)
near('46 bottom minus top=2mg',6+2*.8*g,21.68)
speed=math.sqrt((6+.8*g)*5/.8)
near('46 reconstruct same speed at bottom',.8*(speed**2/5-g),6)
speed=math.sqrt(1.5*g*5)
near('47 actual revolutiontime',2*math.pi*5/speed,3.664428086176754)
near('47 reconstruct bottom normal/weight',1+speed**2/(5*g),2.5)
near('47 top normal still positive',speed**2/(5*g)-1,.5)
mu=25**2/(g*170)
near('48 actual minimum coefficient',mu,.3751500600240096)
near('48 icy maximum speed',math.sqrt(mu/3*g*170),14.433756729740645)
near('48 squared speed responds linearly to coefficient',(25/math.sqrt(3))**2/25**2,1/3)
ns={'s':'http://www.w3.org/2000/svg'};arrows=0
for n,count in [(43,3),(44,2)]:
    root=ET.parse(ROOT/f'docs/vat-ly-1/bai-giang/img/young-05/solution-s5-{n}-fbd.svg').getroot()
    lines=[p for p in root.findall('.//s:line',ns) if p.get('marker-end')]
    yes(f'SVG{n} actual forces count',len(lines)==count);arrows+=len(lines)
    ds=np.array([[float(p.get('x2'))-float(p.get('x1')),float(p.get('y2'))-float(p.get('y1'))] for p in lines])
    near(f'SVG{n} vertical balance',ds[:,1].sum(),0,1e-6)
    if n==43:
        near('43 real tension scale',ds[2,0],-2.5*60)
        near('43 full downward gravity',ds[1,1],2.5*.8*g)
        near('43 no extra centripetal force arrow',ds[:,0].sum(),ds[2,0])
    else:
        near('44 actual wrist force horizontal component',ds[0,0],-2*fx,1e-6)
        near('44 actual wrist force vertical component',ds[0,1],-2*w)
        near('44 actual hand gravity',ds[1,1],2*w)
        yes('44 one true wrist force, not2independentforces',ds[0,0]<0 and ds[0,1]<0 and len(ds)==2)
near('five actual arrows in2requestedFBDs',arrows,5)
report={'status':'passed','scope':'Independent physical computations and actual SVG geometry; full source/crop/structure binding handled by canonical entrypoint.','checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'numeric-042-048.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS 042-048',len(checks),'physical/geometry checks.')
