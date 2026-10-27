from pathlib import Path
import hashlib,json,math,re,xml.etree.ElementTree as ET
import numpy as np,pymupdf
ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-early-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);R=B/'review-049-059'
text=(B/'parent-11-bai-tap-001-059.md').read_text(encoding='utf8');checks=[]
def yes(name,value):
    assert value,name
    checks.append(dict(name=name,passed=True))
def near(name,actual,expected,tol=1e-9):
    assert math.isclose(float(actual),float(expected),rel_tol=tol,abs_tol=tol),(name,actual,expected)
    checks.append(dict(name=name,actual=float(actual),expected=float(expected)))
g=9.8
v=65*1609.344/3600;angle=math.atan(v*v/(g*225))
near('49 actual speed conversion',v,29.0576)
near('49 actual bank angle from unrounded speed',math.degrees(angle),20.95296748299537)
for m,expected in [(1125,11805.657530603614),(2250,23611.315061207228)]:
    n=m*math.hypot(g,v*v/225)
    near('49 exact normal for mass'+str(m),n,expected)
    near('49 vertical normal component mass'+str(m),n*math.cos(angle),m*g)
    near('49 horizontal normal component mass'+str(m),n*math.sin(angle),m*v*v/225)
near('49 same angle mass independence',math.atan((2250*v*v/225)/(2250*g)),angle)
radius=3+5*math.sin(math.pi/6)
period=2*math.pi*math.sqrt(radius/(g*math.tan(math.pi/6)))
near('50 actual radius includes arm offset',radius,5.5)
near('50 actual period',period,6.19481710632848)
for m in [30,70,120]:
    T=m*g/math.cos(math.pi/6)
    near('50 same angle with actual period mass'+str(m),T*math.sin(math.pi/6),m*4*math.pi**2*radius/period**2)
# Solve two actual cable forces from vertical and inward equations.
omega=28*2*math.pi/60;w=1080;m=w/g
upper,horizontal=np.linalg.solve([[math.cos(math.radians(40)),0],[math.sin(math.radians(40)),1]],[w,m*omega**2*7.5])
near('51 actual upper tension',upper,1409.839872478861)
near('51 actual horizontal tension',horizontal,6199.887567112875)
near('51 actual required resultant radial force',m*omega**2*7.5,7106.115168784338)
yes('51 two ropes physically taut',upper>0 and horizontal>0)
near('52 speed with tension3weights',math.sqrt(2*g*15),17.146428199482248)
near('52 zero bottom speed when tension=weight',math.sqrt((1-1)*g*15),0)
for a,expected in [(9.8,1.4947013411760721),(3.7,.9184219367058162)]:
    rpm=60*math.sqrt(a/400)/(2*math.pi)
    near('53 correct rpm for acceleration'+str(a),rpm,expected)
    near('53 inverse rpm conversion recovers acceleration'+str(a),(rpm*2*math.pi/60)**2*400,a)
speed=2*math.pi*50/60;acc=speed**2/50
near('54 speed',speed,5.235987755982989)
near('54 top apparent weight',882-90*acc,832.6519779945532)
near('54 bottom apparent weight',882+90*acc,931.3480220054468)
near('54 zero top support period',2*math.pi*math.sqrt(50/g),14.192268951137288)
near('54 bottom support at critical period',90*(g+g),1764)
for m,r in [(1,1),(.4,2),(5,.6)]:
    top=math.sqrt(g*r);bottom=2*top
    near('55 limiting top tension '+str((m,r)),m*top*top/r-m*g,0)
    near('55 requested local bottom tension '+str((m,r)),m*(g+bottom*bottom/r),5*m*g)
near('56 actual minimum radius',95**2/(4*g),230.22959183673467)
near('56 contact force includes gravity',50*(g+4*g),2450)
near('57 actual minimum top bucket speed',math.sqrt(g*.6),2.4248711305964283)
near('57 critical normal zero',g*.6/.6-g,0)
near('58 actual upward radial acceleration',4.2**2/3.8,4.642105263157895)
near('58 actual rope tension including fullweight',71.2*(1+4.2**2/(3.8*g)),104.92631578947368)
# Solve knot equilibrium for actual angles, not an appendix-rounded answer.
t1=5000;t2=t1*math.cos(math.pi/3)/math.cos(math.radians(40))
weight=t1*math.sin(math.pi/3)+t2*math.sin(math.radians(40))
near('59 actual other rope tension',t2,3263.5182233306973)
near('59 actual maximum supported weight',weight,6427.876096865393)
yes('59 steeper rope reaches material limit first',t1>t2 and t2<5000)
near('59 horizontal balance',-t1*math.cos(math.pi/3)+t2*math.cos(math.radians(40)),0,1e-8)
ns={'s':'http://www.w3.org/2000/svg'}
root=ET.parse(ROOT/'docs/vat-ly-1/bai-giang/img/young-05/solution-s5-59-fbd.svg').getroot()
lines=[p for p in root.findall('.//s:line',ns) if p.get('marker-end')]
yes('59 three actual cable forces',len(lines)==3)
ds=np.array([[float(p.get('x2'))-float(p.get('x1')),float(p.get('y2'))-float(p.get('y1'))] for p in lines])
near('59 actual SVG horizontal balance',ds[:,0].sum(),0,1e-6)
near('59 actual SVG vertical balance',ds[:,1].sum(),0,1e-6)
near('59 actual SVG rope60degree reference',math.degrees(math.atan2(-ds[0,1],-ds[0,0])),60,1e-6)
near('59 actual SVG rope40degree reference',math.degrees(math.atan2(-ds[1,1],ds[1,0])),40,1e-6)
near('59 actual SVG downcable scale',ds[2,1],.02*weight,1e-7)
report={'status':'passed','scope':'Independent physical computations and actual SVG geometry; full source/crop/structure binding handled by canonical entrypoint.','checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'numeric-049-059.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS 049-059',len(checks),'physical/geometry checks.')
