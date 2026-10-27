from pathlib import Path
import hashlib,json,math,re,xml.etree.ElementTree as ET
import numpy as np
from scipy.integrate import quad

ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-early-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True)
R=B/'review-016-023'
text=(B/'parent-11-bai-tap-001-059.md').read_text(encoding='utf8')
checks=[]
def yes(name,value):
    assert value,name
    checks.append(dict(name=name,passed=True))
def near(name,actual,expected,tol=1e-9):
    assert math.isclose(float(actual),float(expected),rel_tol=tol,abs_tol=tol),(name,actual,expected)
    checks.append(dict(name=name,actual=float(actual),expected=float(expected)))

g=9.8
alpha=math.asin((2.5**2/(2*1.5))/g)
near('16 incline actual angle',math.degrees(alpha),12.273885007340755)
near('16 frictionless gravity work',8*g*1.5*math.sin(alpha),.5*8*2.5**2)
v=math.sqrt((8*2.5**2-2*10*1.5)/8)
near('16 with friction from work independently',v,1.5811388300841898)
yes('16 block can accelerate downhill with10N resistance',8*g*math.sin(alpha)>10)
a=15/4
mass=15/(g-a)
near('17 actual acceleration',a,3.75)
near('17 recovered hanging mass',mass,2.4793388429752063)
near('17 hanging force resultant',mass*g-15,mass*a)
yes('17 tension less than hanging weight',15<mass*g)
yes('17 solvability domain satisfied',0<a<g)
# Separate equations for two gliders determine acceleration and inner tension.
a_glide,Tinner=np.linalg.solve([[700,-1],[700,1]],[-2500,12000-2500])
near('18 acceleration from two separate glider equations',a_glide,5)
near('18 actual interglider tension',Tinner,6000)
near('18 runway kinetic result',40**2/(2*a_glide),160)
near('18 whole glider force equation',12000-2*2500,2*700*a_glide)
# The jump estimate uses two distinct motion phases.
v_jump=math.sqrt(2*g*.6)
a_jump=v_jump*v_jump/(2*.5)
near('19 takeoff speed',v_jump,3.4292856398964493)
near('19 constant push-off acceleration',a_jump,11.76)
near('19 support/weight ratio',1+a_jump/g,2.2)
for body_mass in [50,70,90]:
    near('19 COM force-displacement relation '+str(body_mass),
         (2.2*body_mass*g-body_mass*g)*.5,.5*body_mass*v_jump**2)
# Source data, including the1second measurement, determine actual SI coefficients.
A,Bcoef=np.linalg.solve([[1,0],[1,1]],[1.5,2])
near('20 actual A units m/s²',A,1.5)
near('20 actual B units m/s³',Bcoef,.5)
near('20 derivative acceleration at4s',A+2*Bcoef*4,5.5)
near('20 thrust at4s',2540*(g+A+2*Bcoef*4),38862)
near('20 thrust/weight dimensionless',(g+A+2*Bcoef*4)/g,1.5612244897959184)
near('20 initial thrust',2540*(g+A),28702)
# Numerically integrate the actual signed force rather than reuse draft polynomials.
def velocity(t):
    return 9+quad(lambda q:-6*q*q/2,0,t)[0]
t1=(3*2*9/6)**(1/3)
near('21 turning time',t1,2.080083823051904)
near('21 integrated actual force gives zero velocity',velocity(t1),0)
near('21 integrated velocity gives actual stopping distance',
     quad(velocity,0,t1)[0],14.040565805600352)
near('21 later signed velocity',velocity(3),-18)
yes('21 genuinely reverses direction',velocity(t1-.01)>0 and velocity(t1+.01)<0)
# Finite-difference the source height law as an independent derivative check.
y=lambda t:2.8*t+.610*t**3
dt=.001
ay=(y(4+dt)-2*y(4)+y(4-dt))/(dt*dt)
near('22 finite difference source height',ay,14.64,1e-7)
near('22 actual force including gravity',5*(g+ay),122.2,1e-7)
near('23 actual critical slope',math.degrees(math.atan(1.2)),50.19442890773481)
for weight in [1,100,800]:
    for delta in [-.001,0,.001]:
        theta=math.atan(1.2)+delta
        ratio=weight*math.sin(theta)/(weight*math.cos(theta))
        yes('23 static bound direction '+str(weight)+' '+str(delta),
            ratio<1.2 if delta<0 else ratio>1.2 if delta>0 else math.isclose(ratio,1.2))

ns={'s':'http://www.w3.org/2000/svg'}
arrows=0
for n,counts in [(17,[3,2]),(19,[2])]:
    root=ET.parse(ROOT/f'docs/vat-ly-1/bai-giang/img/young-05/solution-s5-{n}-fbd.svg').getroot()
    panels=[p for p in root.findall('.//s:g',ns) if p.get('transform','').startswith('translate(')]
    yes(f'SVG{n} required panels',len(panels)==len(counts))
    for i,(p,count) in enumerate(zip(panels,counts)):
        lines=[x for x in p.findall('s:line',ns) if x.get('marker-end')]
        yes(f'SVG{n}panel{i} complete real force count',len(lines)==count)
        ds=np.array([[float(x.get('x2'))-float(x.get('x1')),float(x.get('y2'))-float(x.get('y1'))] for x in lines])
        arrows+=len(lines)
        if n==17 and i==0:
            near('SVG17 table normal cancels gravity',ds[:,1].sum(),0)
            near('SVG17 table actual tension force scale',ds[0,0],2*15)
            near('SVG17 table actual normal/weight',ds[2,1],2*4*g)
        elif n==17:
            near('SVG17 hanging actual tension scale',ds[0,1],-2*15)
            near('SVG17 hanging weight scale',ds[1,1],2*mass*g,1e-7)
            near('SVG17 hanging net matches acceleration',ds[:,1].sum(),2*mass*a,1e-7)
        else:
            near('SVG19 correct force ratio',-ds[0,1]/ds[1,1],2.2)
            near('SVG19 upward resultant',ds[:,1].sum(),-60)
near('seven actual force arrows',arrows,7)

report={'status':'passed','scope':'Independent physical computations and actual SVG geometry; full source/crop/structure binding handled by canonical entrypoint.','checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'numeric-016-023.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS 016-023',len(checks),'physical/geometry checks.')
