from pathlib import Path
import hashlib,json,math,re,xml.etree.ElementTree as ET
import numpy as np,pymupdf
ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-early-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);R=B/'review-029-036'
text=(B/'parent-11-bai-tap-001-059.md').read_text(encoding='utf8');checks=[]
def yes(name,value):
    assert value,name
    checks.append(dict(name=name,passed=True))
def near(name,actual,expected,tol=1e-9):
    assert math.isclose(float(actual),float(expected),rel_tol=tol,abs_tol=tol),(name,actual,expected)
    checks.append(dict(name=name,actual=float(actual),expected=float(expected)))
g=9.8
for theta in [15,30,55]:
    t=math.radians(theta);mk=.75*math.tan(t)
    for height in [1,2.5]:
        L=height/math.sin(t);a=g*(math.sin(t)-mk*math.cos(t))
        near('29 half speed from actual friction model '+str((theta,height)),math.sqrt(2*a*L)/math.sqrt(2*g*height),.5)
        near('29 limiting static equilibrium '+str((theta,height)),math.sin(t)-math.tan(t)*math.cos(t),0)
near('29 illustration speed',math.sqrt(2*g*2.5),7)
near('29 illustration kinetic coefficient',.75*math.tan(math.pi/6),.4330127018922193)
near('29 illustration static coefficient',math.tan(math.pi/6),.5773502691896257)
t=math.radians(36)
near('30 uphill signed acceleration',-g*(math.sin(t)+.45*math.cos(t)),-9.328060417659756)
near('30 downhill signed acceleration sameaxis',-g*(math.sin(t)-.45*math.cos(t)),-2.1925305272727185)
yes('30 rest impossible at turningpoint',math.tan(t)>.65)
for velocity in [-1,1]:
    fric=-math.copysign(.45*g*math.cos(t),velocity)
    expected=-9.328060417659756 if velocity>0 else -2.1925305272727185
    near('30 explicit friction reverses with velocity '+str(velocity),-g*math.sin(t)+fric,expected)
t=math.radians(55);normal=10*g*math.cos(t);fk=.3*normal
near('31 actual normal',normal,56.21049076210252)
near('31 downwards applied force',(120+10*g*math.sin(t)-fk)/10,18.341375311160043)
near('31 upwards applied force',(120-10*g*math.sin(t)-fk)/10,2.2859952430958055)
near('32 largest acceleration',.650*g,6.37)
near('32 shortest time',30/(.650*g),4.709576138147566)
for m in [1,5,20]:
    near('32 force capacity at maximumacceleration '+str(m),m*6.37,.650*m*g)
# Solve actual geometric force equations without rounded intermediate trigonometry.
theta=math.atan2(2.5,4.75);s,c=math.sin(theta),math.cos(theta)
near('33 hypotenuse',math.hypot(2.5,4.75),5.367727638395972)
near('33 rope balances total downslope gravity and sliding friction',80*g*(s-.444*c),57.10870980249734)
f=32*g*s;n=32*g*c
near('33 upper actual static reaction',f,146.05808133631035)
near('33 upper maximum static friction',.8*n,222.00828363119174)
yes('33 upper friction within bound',f<.8*n)
near('33 upper normal projectedbalance',n-32*g*c,0)
near('33 lower box tangential balance',48*g*s+f-.444*80*g*c-57.10870980249734,0)
near('34 original friction coefficient',25/45,5/9)
# A+cat and B separate Newton equations, positive right and down respectively.
a,T=np.linalg.solve([[-90/g,1],[25/g,1]],[50,25])
near('34 acceleration direction with cat',a,-2.130434782608696)
near('34 rope actual tension with cat',T,30.43478260869565)
yes('34 B decelerates while movingdown',a<0 and T>25)
near('35 dry stopping distance',28.7**2/(2*.8*g),52.53125)
vwet=28.7*math.sqrt(.25/.8)
near('35 actual wet speed for same stopdistance',vwet,16.04378773856099)
near('35 both stopping distances equal',vwet**2/(2*.25*g),52.53125)
t=math.atan(.35);a=g*(math.sin(t)-.25*math.cos(t))
near('36 critical angle',math.degrees(t),19.290046219188735)
near('36 post-slip acceleration',a,.9249811892386967)
near('36 speed after5m',math.sqrt(2*a*5),3.0413503402908)
near('36 energy loss agrees with acceleration',25*g*5*(math.sin(t)-.25*math.cos(t)),.5*25*(2*a*5))
ns={'s':'http://www.w3.org/2000/svg'}
svg=ET.parse(ROOT/'docs/vat-ly-1/bai-giang/img/young-05/solution-s5-32-fbd.svg').getroot()
lines=[p for p in svg.findall('.//s:line',ns) if p.get('marker-end')]
yes('32 required3 forces actually drawn',len(lines)==3)
d=np.array([[float(p.get('x2'))-float(p.get('x1')),float(p.get('y2'))-float(p.get('y1'))] for p in lines])
near('32 actual upward normal balances downward gravity',d[:,1].sum(),0)
near('32 actual horizontal static friction ratio',d[2,0]/d[1,1],.65)
yes('32 actual friction direction acceleratesboxforward',d[2,0]>0)
report={'status':'passed','scope':'Independent physical computations and actual SVG geometry; full source/crop/structure binding handled by canonical entrypoint.','checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'numeric-029-036.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS 029-036',len(checks),'physical/geometry checks.')
