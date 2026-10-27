from pathlib import Path
import hashlib,json,math,re,xml.etree.ElementTree as ET
import numpy as np,pymupdf
ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-early-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);R=B/'review-037-041'
text=(B/'parent-11-bai-tap-001-059.md').read_text(encoding='utf8');checks=[]
def yes(name,value):
    assert value,name
    checks.append(dict(name=name,passed=True))
def near(name,actual,expected,tol=1e-9):
    assert math.isclose(float(actual),float(expected),rel_tol=tol,abs_tol=tol),(name,actual,expected)
    checks.append(dict(name=name,actual=float(actual),expected=float(expected)))
g=9.8
for ma,mb,mu in [(5,3,.4),(1,9,.2),(12,1,.6)]:
    T,F=np.linalg.solve([[1,0],[-1,1]],[mu*ma*g,mu*mb*g])
    near('37 exact symbolic total force '+str((ma,mb,mu)),F,mu*(ma+mb)*g)
    near('37 exact symbolic inner tension '+str((ma,mb,mu)),T,mu*ma*g)
for m,mu,theta in [(90,.35,25),(1,.5,0),(10,.2,75)]:
    t=math.radians(theta);c,s=math.cos(t),math.sin(t)
    # Solve vertical and horizontal balance with N,F as unknowns.
    n,f=np.linalg.solve([[1,s],[-mu,c]],[m*g,0])
    near('38 force from Cartesian independent system '+str(theta),f,mu*m*g/(c+mu*s))
    near('38 normal remains positive '+str(theta),n,m*g*c/(c+mu*s))
    yes('38 actual contact '+str(theta),n>0)
near('38 actual patient force',.35*90*g/(math.cos(math.radians(25))+.35*math.sin(math.radians(25))),292.8219692290797)
a,T=np.linalg.solve([[-2.25,1],[1.3,1]],[.45*2.25*g,1.3*g])
near('39 acceleration from actual two equations',a,.7936619718309859)
near('39 speed after3cm',math.sqrt(2*a*.03),.2182194269762873)
near('39 tension from independent system',T,11.70823943661972)
near('39 hanging block NewtonII',1.3*g-T,1.3*a)
yes('39 kinetic motion branch selfconsistent',1.3*g>.45*2.25*g)
for v in [.5,-.5]:
    ay=-g-math.copysign(g*v*v,v)
    near('40 correct signed drag'+str(v),ay,(-1.25 if v>0 else -.75)*g)
for theta in [10,30,60]:
    t=math.radians(theta);c,s=math.cos(t),math.sin(t);critical=c/s
    for mu in [0,.2*critical,.99*critical]:
        f=mu*10*g/(c-mu*s);n=10*g+f*s
        near('41 steady sliding horizontal balance '+str((theta,mu)),f*c,mu*n)
        yes('41 contact and positive-force domain '+str((theta,mu)),n>0 and f>=0)
    for mu in [critical,1.1*critical]:
        for f in [1,100,1e9]:
            yes('41 no finite initiating force '+str((theta,mu,f)),f*c<=mu*(10*g+f*s))
ns={'s':'http://www.w3.org/2000/svg'};arrows=0
for number,counts in [(37,[4,5]),(39,[4,2])]:
    root=ET.parse(ROOT/f'docs/vat-ly-1/bai-giang/img/young-05/solution-s5-{number}-fbd.svg').getroot()
    panels=[p for p in root.findall('.//s:g',ns) if p.get('transform','').startswith('translate(')]
    yes(f'SVG{number} required panels',len(panels)==len(counts))
    ds=[]
    for i,(panel,count) in enumerate(zip(panels,counts)):
        lines=[p for p in panel.findall('s:line',ns) if p.get('marker-end')]
        yes(f'SVG{number}panel{i} all actualforces',len(lines)==count);arrows+=len(lines)
        d=np.array([[float(p.get('x2'))-float(p.get('x1')),float(p.get('y2'))-float(p.get('y1'))] for p in lines]);ds.append(d)
        near(f'SVG{number}panel{i} correct vertical resultant',d[:,1].sum(),0 if number==37 or i==0 else 4*1.3*a,1e-6)
        if number==37:
            near('37 actual force balance panel'+str(i),d[:,0].sum(),0)
        elif i==0:near('39 horizontal resultant matches acceleration',d[:,0].sum(),4*2.25*a,1e-6)
        else:near('39 no horizontal force on hangingbody',d[:,0].sum(),0)
    if number==37:
        near('37 opposite tensions same magnitude',ds[0][2,0],-ds[1][3,0])
        near('37 actual illustrative friction ratioA',-ds[0][3,0]/ds[0][1,1],.4)
        near('37 actual illustrative friction ratioB',-ds[1][4,0]/ds[1][1,1],.4)
    else:near('39 actual same cable tension horizontal/vertical',ds[0][2,0],-ds[1][0,1])
near('15 real arrows in2 required diagrams',arrows,15)
report={'status':'passed','scope':'Independent physical computations and actual SVG geometry; full source/crop/structure binding handled by canonical entrypoint.','checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'numeric-037-041.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS 037-041',len(checks),'physical/geometry checks.')
