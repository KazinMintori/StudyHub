"""Independent numerical and original-frame checks for the reviewed chapter2 theory.

This is deliberately NOT a certificate for the unfinished whole chapter.
"""
from pathlib import Path
import ast,hashlib,json,math,sys
from decimal import Decimal
import pymupdf as fitz
from PIL import Image
from scipy.integrate import quad

ROOT=Path(__file__).resolve().parents[2]
checks=[]
def check(name,actual,expected,rel=1e-10,absolute=1e-11):
 assert math.isclose(actual,expected,rel_tol=rel,abs_tol=absolute),(name,actual,expected)
 checks.append({'name':name,'computed':actual,'expected':expected})

# Source examples2.1–2.3 and the interval's geometric meaning.
check('Dragster displacement, m',277-19,258)
check('Dragster average velocity, m/s',(277-19)/(4-1),86)
check('Truck signed displacement, m',19-277,-258)
check('Truck average velocity, m/s',(19-277)/(25-16),-258/9)
check('Swimmer average speed, m/s',100/46.91,2.131741632914091)
for value,expected in[('.1','10.5'),('.01','10.05'),('.001','10.005')]:
 dt=Decimal(value);x=lambda t:Decimal(20)+Decimal(5)*t*t
 check('Cheetah difference quotient dt='+value,float((x(1+dt)-x(Decimal(1)))/dt),float(expected))
check('Cheetah instantaneous velocity at1s, m/s',10*1,10)
check('Cheetah average velocity over1–2s, m/s',((20+5*2**2)-(20+5*1**2))/(2-1),15)
check('Tangent slope figure2.7, m/s',160/4,40)
for i,(u,v,want)in enumerate([(.8,1.2,.2),(1.6,1.2,-.2),(-.4,-1,-.3),(-1.6,-.8,.4)],1):
 check('Astronaut average acceleration interval'+str(i),(v-u)/2,want)
for value,expected in[('.1','1.05'),('.01','1.005'),('.001','1.0005')]:
 dt=Decimal(value);v=lambda t:Decimal(60)+Decimal('.5')*t*t
 check('Car acceleration difference quotient dt='+value,float((v(1+dt)-v(Decimal(1)))/dt),float(expected))
check('Car average acceleration over1–3s',(64.5-60.5)/(3-1),2)

# Each constant-acceleration formula checked against independent integration,
# including rest, positive/negative acceleration and passage through v=0.
for x0 in[-5,0,12]:
 for v0 in[-8,0,15]:
  for a in[-9.8,0,4]:
   for t in[.7,2]:
    velocity=v0+quad(lambda _:a,0,t)[0]
    position=x0+quad(lambda u:v0+a*u,0,t)[0]
    check(f'Position x0{ x0 } v0{ v0 } a{ a } t{ t }',position,x0+v0*t+.5*a*t*t)
    check(f'No-time relation x0{ x0 } v0{ v0 } a{ a } t{ t }',velocity**2-v0**2,2*a*(position-x0),absolute=1e-9)
    check(f'Trapezoid displacement x0{ x0 } v0{ v0 } a{ a } t{ t }',position-x0,.5*(v0+velocity)*t)

# Variable acceleration: One explicit counterexample to blanket use of the
# trapezoid formula, and one nonconstant example where equality happens to hold.
v=lambda t:2+t*t
check('Nonconstant velocity integral',quad(v,0,1)[0],7/3)
assert not math.isclose(quad(v,0,1)[0],(v(0)+v(1))/2)
v=lambda t:2+t+.1*math.sin(2*math.pi*t)
check('Accidental trapezoid equality despite variable acceleration',quad(v,0,1)[0],(v(0)+v(1))/2)
assert not math.isclose(1+.2*math.pi,1-.2*math.pi)
for v0 in[5.5,12,15]:
 g=9.8;top=v0/g;H=v0*v0/(2*g);T=2*top
 check('Freefall peak velocity v0'+str(v0),v0-g*top,0)
 check('Freefall peak height v0'+str(v0),v0*top-.5*g*top**2,H)
 check('Return elevation v0'+str(v0),v0*T-.5*g*T*T,0)
 check('Return signed velocity v0'+str(v0),v0-g*T,-v0)

# All numerical branches of Examples2.4–2.9 and both scaling questions.
check('Example2.4 position at2s',5+quad(lambda u:15+4*u,0,2)[0],43)
check('Example2.4 velocity at2s',15+4*2,23)
check('Example2.4 time at25m/s',(25-15)/4,2.5)
check('Example2.4 position at25m/s',5+(25**2-15**2)/(2*4),55)
catch=2*15/3
check('Example2.5 catch time',catch,10)
check('Example2.5 police velocity',3*catch,30)
check('Example2.5 police displacement',quad(lambda u:3*u,0,catch)[0],150)
check('Example2.5 motorist displacement',15*catch,150)
check('Example2.5 equal-velocity time',15/3,5)
for t,y,v in[(1,-4.9,-9.8),(2,-19.6,-19.6),(3,-44.1,-29.4)]:
 check('Example2.6 coin position at'+str(t),-.5*9.8*t*t,y)
 check('Example2.6 coin velocity at'+str(t),-9.8*t,v)
for t,y,v in[(1,10.1,5.2),(4,-18.4,-24.2)]:
 check('Example2.7 ball position at'+str(t),15*t-.5*9.8*t*t,y)
 check('Example2.7 ball velocity at'+str(t),15-9.8*t,v)
check('Example2.7 squared speed at5m',15**2-2*9.8*5,127)
for y,D in[(-5,323),(5,127),(15,-69)]:
 actual=15**2-2*9.8*y;check('Example2.8 discriminant at'+str(y),actual,D)
 if D<0:continue
 for sign in[-1,1]:
  t=(15+sign*math.sqrt(D))/9.8
  check('Example2.8 root substitution '+str((y,sign)),15*t-.5*9.8*t*t,y)
check('Selfcheck2.5 double-speed height ratio',(2*15)**2/(2*9.8)/(15**2/(2*9.8)),4)
check('Selfcheck2.5 double-speed time ratio',((2*15)/9.8)/(15/9.8),2)
A=2.;B=.1
acc=lambda u:A-B*u
vel=lambda u:10+quad(acc,0,u)[0]
pos=lambda u:50+quad(vel,0,u)[0]
for t in[0,1,20,30,20+math.sqrt(600)]:
 check('Example2.9 velocity via quadrature at'+str(t),vel(t),10+A*t-.5*B*t*t)
 check('Example2.9 position via nested quadrature at'+str(t),pos(t),50+10*t+.5*A*t*t-B*t**3/6)
check('Example2.9 velocity maximum time',A/B,20)
check('Example2.9 maximum velocity',vel(A/B),30)
check('Example2.9 coordinate at maximum',pos(A/B),1550/3)
check('Figure2.29 stopping root',vel(20+math.sqrt(600)),0)
assert acc(19)>0 and acc(21)<0
check('Swimmer rounded result tolerance',round(100/46.91,3),2.132)
check('Derivative example x² at3',2*3,6)
check('Derivative of3x+2',3,3)
check('Integral0to2 x',quad(lambda x:x,0,2)[0],2)
check('Integral0to1 constant2',quad(lambda _:2,0,1)[0],2)

# All53 source crops are checked against the actual supplied PDF raster.
# Manual context review, recorded separately, is needed for frame completeness.
tree=ast.parse((ROOT/'scripts/prepare-physics-translation-assets.py').read_text('utf8'))
spec=next(ast.literal_eval(n.value)for n in tree.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='chapter2'for t in n.targets))
figures=[]
with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as doc:
 for name,(printed,box)in spec.items():
  asset=ROOT/'docs/vat-ly-1/bai-giang/img/young-02'/(name+'.png')
  im=Image.open(asset).convert('RGB');pix=doc[printed+19].get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(box))
  original=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
  assert im.size==original.size and im.tobytes()==original.tobytes(),name
  figures.append({'asset':asset.relative_to(ROOT).as_posix(),'pdfPage':printed+20,'crop':box,'originalPixelMatch':True,'sha256':hashlib.sha256(asset.read_bytes()).hexdigest()})
names=[p.name for p in sorted((ROOT/'raw_materials/physics/translations/chapter-02').glob('*.md'))if p.name[:2]in['00','01','02','03','04','05','06','07']]
source_hashes={str(Path('raw_materials/physics/translations/chapter-02')/name).replace('\\','/'):hashlib.sha256((ROOT/'raw_materials/physics/translations/chapter-02'/name).read_bytes().replace(b'\r\n',b'\n')).hexdigest()for name in names}
result={'status':'passed-reviewed-theory-and-original-pixels-only','limitations':'All127 end solutions remain under separate source review. Pixel matching alone cannot prove complete framing. Actual browser acceptance is separate. No whole-chapter completion claim.',
 'numericalCheckCount':len(checks),'numericalChecks':checks,'figures':figures,'reviewedTheorySHA256':source_hashes}
if '--output'in sys.argv:
 out=Path(sys.argv[sys.argv.index('--output')+1]);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':result['status'],'numericalChecks':len(checks),'actualOriginalFrames':len(figures)}))
