"""Independent values, limiting cases, and exact raster checks for theory3.

The reviewed source ledger separately records the full semantic PDF comparison.
This program does not infer semantic completeness from numerical assertions.
"""
from pathlib import Path
import ast,math,re,json,hashlib
import numpy as np,pymupdf
ROOT=Path(__file__).resolve().parents[2];RAW=ROOT/'raw_materials/physics/translations/chapter-03';g=9.8;checks=[]
def ck(unit,label,actual,expected,tol=1e-8):
 assert np.allclose(actual,expected,atol=tol,rtol=tol),(unit,label,actual,expected)
 checks.append({'unit':unit,'check':label})
def st(unit,label,c):
 assert c,(unit,label);checks.append({'unit':unit,'check':label})
def vel(u,d):return np.array([u*math.cos(math.radians(d)),u*math.sin(math.radians(d))])
theory='\n'.join((RAW/f).read_text('utf8')for f in ['01-muc-01.md','02-muc-02.md','03-muc-03.md','04-muc-04.md','05-muc-05.md'])
st('inventory','all15examples',re.findall(r'^::: example Ví dụ (?:khái niệm )?(3\.\d+)',theory,re.M)==[f'3.{i}'for i in range(1,16)])
st('inventory','all5immediatechecks',re.findall(r'^::: exercise Câu hỏi tự kiểm tra mục (3\.\d+)',theory,re.M)==[f'3.{i}'for i in range(1,6)])
tags=re.findall(r'\\tag\{3\.(\d+)[ab]?\}',theory);st('inventory','all36sourceequationnumbers',set(map(int,tags))==set(range(1,37)))
st('syntax','no missingmathrmcommand',not re.search(r'(?<!\\)\bmathrm\b',theory))
for t in [0,1,2,4]:
 x=2-.25*t*t;y=t+.025*t**3;vx=-.5*t;vy=1+.075*t*t;ax=-.5;ay=.15*t
 ck('3.1','positionderivativeX'+str(t),np.polynomial.polynomial.polyval(t,np.polynomial.polynomial.polyder([2,0,-.25])),vx)
 ck('3.1','positionderivativeY'+str(t),np.polynomial.polynomial.polyval(t,np.polynomial.polynomial.polyder([0,1,0,.025])),vy)
 ck('3.2','velocityderivativeX'+str(t),np.polynomial.polynomial.polyval(t,np.polynomial.polynomial.polyder([0,-.5])),ax)
 ck('3.2','velocityderivativeY'+str(t),np.polynomial.polynomial.polyval(t,np.polynomial.polynomial.polyder([1,0,.075])),ay)
ck('3.1','r2',[2-.25*4,2+.025*8],[1,2.2]);ck('3.1','averagevelocity',[(1-2)/2,2.2/2],[-.5,1.1]);ck('3.1','speed2',math.hypot(-1,1.3),1.6401219466856725)
ck('3.2','averageacceleration',([ -1,1.3]-np.array([0,1]))/2,[-.5,.15]);ck('3.2','instantacceleration2',[-.5,.15*2],[-.5,.3])
v=np.array([-1,1.3]);a=np.array([-.5,.3]);parallel=a@v/np.linalg.norm(v);normal=abs(np.linalg.det([v,a]))/np.linalg.norm(v)
ck('3.3','parallel',parallel,.5426,tol=.001);ck('3.3','perpendicular',normal,.2134,tol=.001);ck('3.3','orthogonalcomponents',parallel**2+normal**2,a@a)
for turn,rate in [(1,1),(1,0),(1,-1)]:
 tangent=np.array([1.,0]);inward=np.array([0.,1]);a=rate*tangent+turn*inward;ck('3.4','tangentcomponent'+str(rate),a@tangent,rate);ck('3.4','normalcomponent'+str(rate),a@inward,turn)
ck('3.5','freeflightsecondderivatives',[np.polynomial.polynomial.polyder([0,7],2).sum(),np.polynomial.polynomial.polyder([0,12,-g/2],2).sum()],[0,-9.8])
t=.5;ck('3.6','position',[9*t,-g*t*t/2],[4.5,-1.225]);ck('3.6','distance',math.hypot(4.5,1.225),4.66375654,tol=1e-6);ck('3.6','velocity',[9,-g*t],[9,-4.9])
vx,vy=vel(37,53.1);t=2;ck('3.7','sourceinitialcomponents',[vx,vy],[22.215,29.588],tol=.001);ck('3.7','position2',[vx*t,vy*t-g*t*t/2],[44.4,39.6],tol=.002);ck('3.7','speed2',math.hypot(vx,vy-g*t),24.4,tol=.002)
tf=2*vy/g;ck('3.7','sameheightreturn',vy*tf-.5*g*tf*tf,0);ck('3.7','landinginitialspeed',math.hypot(vx,vy-g*tf),37)
for u in [4.,12.,37.]:
 for degrees in [10.,30.,45.,70.,90.]:
  vx,vy=vel(u,degrees);tf=2*vy/g;h=vy*vy/(2*g);R=vx*tf
  ck('3.8','range'+str((u,degrees)),R,u*u*math.sin(2*math.radians(degrees))/g);st('3.8','rangebound'+str((u,degrees)),R<=u*u/g+1e-8);st('3.8','heightbound'+str((u,degrees)),h<=u*u/(2*g)+1e-8)
vx,vy=vel(10,-20);tf=(vy+math.sqrt(vy*vy+2*g*8))/g;ck('3.9','groundheight',vy*tf-g*tf*tf/2,-8);ck('3.9','horizontalrange',vx*tf,9.2,tol=.005)
for d,h,speed in [(5.,4.,15.),(12.,10.,25.),(30.,20.,40.)]:
 angle=math.atan2(h,d);time=d/(speed*math.cos(angle));dart=speed*math.sin(angle)*time-g*time*time/2;monkey=h-g*time*time/2;ck('3.10','samegravitationaldrop'+str((d,h,speed)),dart,monkey);st('3.10','abovegroundcondition',monkey>0)
ck('3.11','radiusat0.97g',40**2/(.97*g),168.3,tol=.002)
ck('3.12','rimspeed',2*math.pi*5/4,7.853981633974483);ck('3.12','radialacceleration',4*math.pi**2*5/4**2,12.337005501361698)
ck('3.13','truckrelativeyou',-104-88,-192);ck('3.13','yourelativetruck',88-(-104),192)
ck('3.14','groundvector',np.array([0,240])+[100,0],[100,240]);ck('3.14','groundspeed',math.hypot(240,100),260);ck('3.14','eastofnorth',math.degrees(math.atan2(100,240)),22.619864948040426)
north=math.sqrt(240**2-100**2);ck('3.15','compensatingairspeed',math.hypot(-100,north),240);ck('3.15','northgroundspeed',north,218.1742422927143);ck('3.15','westofnorth',math.degrees(math.asin(100/240)),24.624318352164078)
ck('TYU3.1','uniformstraightaverageandinstantaneous',(np.array([17,10])-[5,1])/3,[4,3]);ck('TYU3.2','crestradialinward',-np.array([0,1]),[0,-1])
ck('TYU3.4','speedratio4accel',math.sqrt(4),2);ck('TYU3.5','windvector',np.array([0,150])-[150,0],[-150,150]);ck('TYU3.5','windspeed',math.hypot(150,150),212.13203435596427)
# The TYU3.3 geometric premise comes from the figure. Verify a nontrivial
# realization in which the dart reaches its apex before the interception.
d,h,u=12.,18.,14.;alpha=math.atan2(h,d);tmeet=d/(u*math.cos(alpha));tapex=u*math.sin(alpha)/g
st('TYU3.3','apexprecedesmeeting',tapex<tmeet);dartheight=u*math.sin(alpha)*tapex-g*tapex**2/2;monkeyheight=h-g*tapex**2/2;st('TYU3.3','actualapexgeometricordering',monkeyheight>dartheight)
tree=ast.parse((ROOT/'scripts/prepare-physics1-remaining-03-theory-assets.py').read_text('utf8'));crops=next(ast.literal_eval(n.value)for n in tree.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='CROPS'for t in n.targets));st('images','47originalsourcecrops',len(crops)==47)
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as pdf:
 for name,page,rect,description in crops:
  actual=pymupdf.Pixmap(ROOT/'docs/vat-ly-1/bai-giang/img/young-03'/(name+'.png'));expected=pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(2.25,2.25),clip=pymupdf.Rect(rect),alpha=False)
  st(name,'unchangedPDFpixels',actual.samples==expected.samples and actual.width==expected.width and actual.height==expected.height)
print(json.dumps({'status':'passed-theory-values-and-images','checks':len(checks),'sourceExamples':15,'immediateSelfChecks':5,'sourceEquationNumbers':36,'originalCrops':47,'scope':'Values/symboliccases/exactrasters only; fullsemanticreview andbrowserproof recorded separately.'},ensure_ascii=False))
