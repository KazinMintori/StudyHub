from pathlib import Path
import math,json,re,hashlib,xml.etree.ElementTree as ET
import numpy as np,pymupdf
ROOT=Path(__file__).resolve().parents[2]
B=ROOT/'raw_materials/physics/translations/chapter-03';checks=[]
def sha256_asset(path):
 data=path.read_bytes()
 if path.suffix.lower()in {'.md','.svg'}:data=data.replace(b'\r\n',b'\n')
 return hashlib.sha256(data).hexdigest()
def ck(unit,label,actual,expected,tol=1e-8):
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(unit,label,actual,expected)
 checks.append({'unit':unit,'check':label,'actual':np.asarray(actual).tolist(),'expected':np.asarray(expected).tolist(),'passed':True})
def st(unit,label,condition):
 assert condition,(unit,label);checks.append({'unit':unit,'check':label,'passed':True})
g=9.8;rad=math.radians
vx=25*math.cos(rad(36.9));vy=25*math.sin(rad(36.9));th=vy/g;tf=2*th
for k,v,e in [('time to apex',th,1.5316840561595026),('height',vy*vy/2/g,11.495947040938704),('flight time',tf,3.063368112319005),('range',vx*tf,61.24606428161445)]:ck('VP3.9.1',k,v,e,tol=.001)
ck('VP3.9.1','apex vy',vy-g*th,0);ck('VP3.9.1','landing y',vy*tf-.5*g*tf*tf,0)
ck('VP3.9.2','launch speed',g*1.05/math.sin(rad(30)),20.58);ck('VP3.9.2','height',.5*g*1.05**2,5.40225)
vx=15*math.cos(rad(50));vy=15*math.sin(rad(50));t=(vy+math.sqrt(vy*vy+2*g*20))/g
ck('VP3.9.3','landing height',vy*t-.5*g*t*t,-20)
ck('VP3.9.3','time',t,3.51,tol=.001);ck('VP3.9.3','range',vx*t,33.8,tol=.002);ck('VP3.9.3','impact vx',vx,9.64,tol=.001);ck('VP3.9.3','impact vy',vy-g*t,-22.9,tol=.002)
ck('VP3.9.3','energy identity',vx*vx+(vy-g*t)**2,15**2+2*g*20)
for speed in [1.,12.,35.]:
 ta=2*speed/g;tb=speed/g
 ck('VP3.9.4','equal displacements v0='+str(speed),speed*ta,.5*g*ta**2)
 ck('VP3.9.4','45degree velocity v0='+str(speed),speed,g*tb)
 ck('VP3.9.4','yb v0='+str(speed),-.5*g*tb**2,-speed*speed/(2*g))
ck('VP3.12.1','radius',10**2/5,20)
ck('VP3.12.2','period',2*math.pi*265/40,41.626102660064756)
ck('VP3.12.2','centripetal acceleration',40**2/265,6.037735849056604)
for r,v,a in [(.1,.938,8.79),(.2,1.88,17.6)]:
 speed=2*math.pi*r/.670;ck('VP3.12.3','speed r='+str(r),speed,v,tol=.003);ck('VP3.12.3','acceleration r='+str(r),speed**2/r,a,tol=.003)
ck('VP3.12.3','radius scaling speed',(.2/.1),2);ck('VP3.12.3','radius scaling acceleration',(.2/.1),2)
lastv=lasta=float('inf')
for name,r,days,v,a in [('Venus',1.08e11,225,3.49e4,1.13e-2),('Earth',1.50e11,365,2.99e4,5.95e-3),('Mars',2.28e11,687,2.41e4,2.55e-3)]:
 speed=2*math.pi*r/(days*86400);acc=speed**2/r
 ck('VP3.12.4',name+'speed',speed,v,tol=.003);ck('VP3.12.4',name+'acceleration',acc,a,tol=.003)
 st('VP3.12.4',name+'decreasing speed and acceleration',speed<lastv and acc<lasta);lastv,lasta=speed,acc
ck('VP3.12.5','period A/B',(2*math.pi*8/3)/(2*math.pi*4/6),4)
ck('VP3.12.5','acceleration A/B',(3**2/8)/(6**2/4),1/8)
ck('VP3.15.1','police relative to SUV',35-(-18),53);ck('VP3.15.1','SUV relative to police',-18-35,-53)
ck('VP3.15.2','A relative to B vector',[45-(-45),0],[90,0]);ck('VP3.15.2','no radial relative velocity',np.dot([90,0],[0,1]),0)
v=np.array([16.,0])-np.array([0.,-20]);ck('VP3.15.3','relative components',v,[16,20]);ck('VP3.15.3','relative speed',np.linalg.norm(v),25.6,tol=.001);ck('VP3.15.3','relative angle',math.degrees(math.atan2(v[1],v[0])),51.3,tol=.001)
wind=np.array([40/math.sqrt(2),40/math.sqrt(2)]);air=np.array([0.,155])-wind
ck('VP3.15.4','wind+airspeed=ground',wind+air,[0,155]);ck('VP3.15.4','airspeed magnitude',np.linalg.norm(air),130,tol=.002);ck('VP3.15.4','west of north',math.degrees(math.atan2(-air[0],air[1])),12.6,tol=.002)
for angle in [-.5,.5]:
 radial=np.array([math.sin(angle),-math.cos(angle)]);tangent=np.array([math.cos(angle),math.sin(angle)]);acc=-g*math.sin(angle)*tangent
 ck('Q3.1','turning point acceleration is tangential',acc@radial,0)
 st('Q3.1','restoring tangential sign',np.dot(acc,tangent)*angle<0)
ck('Q3.1','bottom acceleration upward',[0,4**2/2],[0,8])
ck('Q3.2','velocity change',150-230,-80)
for U,V,h in [(1.,4.,.5),(20.,15.,10.)]:
 T=V/g
 ck('Q3.3','orthogonality at apex',np.dot([0,-g],[U,V-g*T]),0)
 st('Q3.3','nonzero horizontal excludes parallel acceleration',U!=0)
 fall=math.sqrt(2*h/g);s1=math.hypot(U,g*fall);s2=math.hypot(2*U,g*fall)
 st('Q3.4','impact speed strictly between v and2v',s1<s2<2*s1)
 ck('Q3.4','same flight time regardless vx',fall,math.sqrt(2*h/g))
 ck('Q3.5','equal vertical fall',h-.5*g*fall**2,0)
 ck('Q3.6','plane-relative x',U*fall-U*fall,0)
 ck('Q3.8','verticalheight/rangemax',(U*U/2/g)/(U*U/g),.5)
 ck('Q3.9','apex vy',V-g*T,0)
 ck('Q3.16','positive minimum speed',math.hypot(U,V-g*T),U)
ck('Q3.10','closed orbit displacement',[2-2,0],[0,0]);ck('Q3.10','closed orbit velocity change',[0,3]-np.array([0,3]),[0,0])
ck('Q3.11','speedtripled factor',3**2,9);ck('Q3.11','radius halved factor',1/.5,2)
st('Q3.12','nonzero tangential acceleration not perpendicular',np.dot([2,3],[4,0])!=0)
ck('Q3.13','rain relative to car',np.array([0.,-8])-np.array([12.,0]),[-12,-8])
ck('Q3.14','rain relative to walker',np.array([3.,-8])-np.array([1.,0]),[2,-8])
ck('Q3.15','minimumtime',60/1.5,40);ck('Q3.15','drift',1.2*40,48);ck('Q3.15','groundpathangle',math.degrees(math.atan2(1.2,1.5)),38.659808254090095)
for theta in np.linspace(0,math.radians(80),9):
 opt=math.pi/4-theta/2;v0=20.;Rmax=v0*v0/(g*(1+math.sin(theta)))
 for phi in np.linspace(.01,math.pi/2-theta-.01,8):
  alpha=theta+phi;t=2*v0*math.sin(phi)/(g*math.cos(theta));x=v0*math.cos(alpha)*t;y=v0*math.sin(alpha)*t-.5*g*t*t
  R=2*v0*v0*math.cos(alpha)*math.sin(phi)/(g*math.cos(theta)**2)
  ck('bridge','landing onincline',y,x*math.tan(theta));ck('bridge','range fromcoordinates',math.hypot(x,y),R)
  st('bridge','range bounded by predictedmaximum',R<=Rmax+1e-8)
 alpha=theta+opt;Ro=2*v0*v0*math.cos(alpha)*math.sin(opt)/(g*math.cos(theta)**2)
 ck('bridge','optimal range',Ro,Rmax);ck('bridge','first derivative zero',math.cos(theta+2*opt),0)
 st('bridge','second derivative negative',-4*math.sin(theta+2*opt)<0)
fragments={name:(B/name).read_text(encoding='utf-8')for name in ['parent-09-luyen-tap-huong-dan.md','parent-10-cau-hoi-thao-luan.md','parent-16-bai-tap-cau-noi.md']};ledger=[]
expected=[*(f'VP3.9.{i}'for i in range(1,5)),*(f'VP3.12.{i}'for i in range(1,6)),*(f'VP3.15.{i}'for i in range(1,5)),*(f'Q3.{i}'for i in range(1,17)),'Bài tập cầu nối']
for name,text in fragments.items():
 for match in re.finditer(r'^### (VP3\.\d+\.\d+|Q3\.\d+|Bài tập cầu nối)[^\n]*\n([\s\S]*?)(?=^### |\Z)',text,re.M):
  unit,body=match[1],match[2];prompt=body.split('<details>',1)[0]
  st(unit,'one closed solution',body.count('<details>')==body.count('</details>')==1 and'<details open'not in body)
  st(unit,'all3solution stages',all(body.count(s)==1 for s in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']))
  if unit=='Bài tập cầu nối':st(unit,'9original guidequestions beforebox',re.findall(r'^(\d+)\. ',prompt,re.M)==list(map(str,range(1,10))))
  ledger.append({'id':unit,'file':name,'line':text[:match.start()].count('\n')+1,'sourcePDFPages':[111,112]if unit=='Bài tập cầu nối'else[112]if unit.startswith('Q')else[111]})
st('all','exact30sourceunits',sorted(expected)==sorted(r['id']for r in ledger))
sha=sha256_asset
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as pdf:
 for row in json.loads((B/'parent-image-assets.json').read_text(encoding='utf-8')):
  actual=pymupdf.Pixmap(ROOT/row['publicFile']);expectedpix=pdf[row['pdfPage1Based']-1].get_pixmap(matrix=pymupdf.Matrix(row['scale'],row['scale']),clip=pymupdf.Rect(row['rectangle']),alpha=False)
  st(row['key'],'unchanged PDFcrop pixels',actual.samples==expectedpix.samples and actual.width==expectedpix.width and actual.height==expectedpix.height)
  st(row['key'],'SHA matches',sha(ROOT/row['publicFile'])==row['sha256'])
models={'x':(lambda t:t,0,2.15),'y':(lambda t:t-.5*t*t,0,.55),'vx':(lambda t:1,0,1.2),'vy':(lambda t:1-t,-1.2,1.2),'ax':(lambda t:0,-1.2,1.2),'ay':(lambda t:-1,-1.2,1.2)}
for key,(func,lo,hi)in models.items():
 svg=ET.parse(ROOT/f'docs/vat-ly-1/bai-giang/img/young-03/solution-s-q3-7-{key}.svg').getroot();poly=svg.find('.//{*}polyline');pts=np.array([[float(v)for v in item.split(',')]for item in poly.get('points').split()]);st('Q3.7','201actual samples '+key,len(pts)==201)
 for i,(px,py)in enumerate(pts):
  tau=i/100;ck('Q3.7',key+f'point{i}',[px,py],[64+125*tau,205-(func(tau)-lo)/(hi-lo)*140],tol=1e-4)
svg=ET.parse(ROOT/'docs/vat-ly-1/bai-giang/img/young-03/solution-s-q3-2-antiparallel.svg').getroot();lines=[n for n in svg.findall('.//{*}line')if n.get('stroke')=='#2458a6'];ck('Q3.2','actual SVG arrow directions',[float(n.get('x2'))-float(n.get('x1'))for n in lines],[230,150,-80])

progress=json.loads((B/'parent-exercise-progress.json').read_text(encoding='utf-8'))
assert progress['status']=='partially-reviewed-not-ready'and progress['reviewedUnits']==30 and progress['expectedUnits']==115
assert sha(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')==progress['sourcePDFSHA256']
for row in progress['files']:assert sha(B/row['file'])==row['sha256']
manifest=json.loads((B/'parent-solution-image-manifest.json').read_text(encoding='utf-8'))['assets']
for row in manifest:assert sha(ROOT/row['publicFile'])==row['sha256']
print(json.dumps({'status':'passed-partial30units','sourceUnits':len(ledger),'checks':len(checks),'actualPlotSamplesChecked':1206,'originalCrops':4,'solutionDiagrams':7,'wholeChapterComplete':False,'pendingNumberedRange':'3.1–3.85'},ensure_ascii=False))
