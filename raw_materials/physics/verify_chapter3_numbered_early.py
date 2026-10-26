from pathlib import Path
import json,math,re,hashlib,xml.etree.ElementTree as ET
import numpy as np,pymupdf
ROOT=Path(__file__).resolve().parents[2];B=ROOT/'raw_materials/physics/translations/chapter-03';checks=[];failures=[];g=9.8;rad=math.radians
def ck(unit,label,actual,expected,tol=1e-8):
 passed=bool(np.allclose(actual,expected,rtol=tol,atol=tol))
 if not passed:
  failures.append((unit,label,np.asarray(actual).tolist(),np.asarray(expected).tolist()));print('MISMATCH',failures[-1])
 checks.append({'unit':unit,'check':label,'actual':np.asarray(actual).tolist(),'expected':np.asarray(expected).tolist(),'passed':passed})
def st(unit,label,condition):
 assert condition,(unit,label);checks.append({'unit':unit,'check':label,'passed':True})
def polar(v,d):return np.array([v*math.cos(rad(d)),v*math.sin(rad(d))])
def motion(v,d,h=0):
 vx,vy=polar(v,d);tf=(vy+math.sqrt(vy*vy+2*g*h))/g
 return float(vx),float(vy),tf
def sha(p):
 data=p.read_bytes()
 if p.suffix.lower()in {'.md','.svg'}:data=data.replace(b'\r\n',b'\n')
 return hashlib.sha256(data).hexdigest()
file=B/'parent-11-bai-tap-001-043.md';text=file.read_text('utf8')
units={int(m[1]):m[2]for m in re.finditer(r'^### 3\.(\d+)[^\n]*\n([\s\S]*?)(?=^### |\Z)',text,re.M)}
st('all','43uniqueorderedunits',list(units)==list(range(1,44)))
for n,body in units.items():
 st(n,'oneclosedsolution',body.count('<details>')==body.count('</details>')==1 and'<details open'not in body)
 st(n,'all3pedagogicalstages',all(body.count(x)==1 for x in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']))
st('all','inlinebalanced',not any(l.replace('$$','').count('$')%2 for l in text.splitlines()))
st('all','no controlchar or thinker monologue',not any(ord(c)<32 and c not in '\n\r\t'for c in text)and not re.search(r'\b(?:Khoan đã|À không|Wait|Nhầm rồi)\b',text,re.I))
for n,labels in [(4,'abc'),(5,'abc'),(7,'abcd'),(18,'abcdef'),(20,'abc')]:
 prompt=units[n].split('<details>')[0];solution=units[n].split('**Lời giải:**')[1]
 st(n,'actualsourcepartsintheprompt',all('('+x+')'in prompt for x in labels));st(n,'eachsourcepartanswered',all('('+x+')'in solution for x in labels))
v=(np.array([5.3,-.5])-[1.1,3.4])/3;ck(1,'averagecomponents',v,[1.4,-1.3]);ck(1,'averagespeed',np.linalg.norm(v),1.91049731745428)
r=12*np.array([-3.8,4.9]);ck(2,'position',r,[-45.6,58.8]);ck(2,'distance',np.linalg.norm(r),74.40967679005198)
ck(3,'averagedisplacementvelocity',([14,10]-np.array([4,0]))/2,[5,5])
for t in [0.,1.,2.]:
 ck(3,'velocityderivative '+str(t),[np.polynomial.polynomial.polyval(t,np.polynomial.polynomial.polyder([4,0,2.5])),5],[5*t,5])
 ck(3,'positiononparabola '+str(t),4+2.5*t*t,4+.1*(5*t)**2)
ck(4,'position5s',[.28*5+.036*25,.019*125],[2.3,2.375]);ck(4,'velocity5s',[.28+.072*5,.057*25],[.64,1.425]);ck(4,'distance',math.hypot(2.3,2.375),3.3061495731439616)
for t in [0,1,5]:
 ck(4,'xvelocitypolynomialderivative '+str(t),np.polynomial.polynomial.polyval(t,np.polynomial.polynomial.polyder([0,.28,.036])),.28+.072*t)
 ck(4,'yvelocitypolynomialderivative '+str(t),np.polynomial.polynomial.polyval(t,np.polynomial.polynomial.polyder([0,0,0,.019])),.057*t*t)
a=(np.array([-170,40])-[90,110])/30;ck(5,'averageacceleration',a,[-26/3,-7/3]);ck(5,'magnitude',np.linalg.norm(a),8.975274678557506);st(5,'correct8.98inactualfragment',r'8{,}98'in units[5])
vf=np.array([2.6,-1.8])+10*polar(.45,31);ck(6,'finalvelocity',vf,[6.457252853159506,.517671337095243],tol=1e-6);st(6,'actual10and20secondtimesretained',r't_1=10{,}0'in units[6]and r't_2=20{,}0'in units[6])
ck(7,'position2s',[2.4*2,3-1.2*4],[4.8,-1.8]);ck(7,'velocity2s',[2.4,-2*1.2*2],[2.4,-4.8]);ck(7,'acceleration',[0,-2*1.2],[0,-2.4]);st(7,'speedincreasing',np.dot([2.4,-4.8],[0,-2.4])>0);st(7,'clockwiseturn',2.4*(-2.4)-(-4.8)*0<0)
v=np.array([5-.018*64,2+.55*8]);a=np.array([-.036*8,.55]);ck(8,'sourcevelocity',v,[3.848,6.4]);ck(8,'sourceacceleration',a,[-.288,.55]);ck(8,'speed',np.linalg.norm(v),7.47,tol=.001);ck(8,'accelerationmagnitude',np.linalg.norm(a),.621,tol=.001)
st(8,'sourcegivenvelocitynotintegratedasacceleration',r'v_x(t)=5{,}00-0{,}0180t^2'in units[8]and r'a_x(t) = -0{,}0360t'in units[8])
t=.48;ck(9,'height',.5*g*t*t,1.12896);ck(9,'range',1.1*t,.528);ck(9,'impactvelocity',[1.1,-g*t],[1.1,-4.704])
t=math.sqrt(2*9/g);ck(10,'ledgegrazingthreshold',1.75/t,1.291,tol=.001);ck(10,'recovercliffheight',.5*g*t*t,9)
ck(11,'horizontalcricketdistance',.95*2.7,2.565)
tf=24/g;ck(12,'timeup',12/g,1.2244897959183672);ck(12,'height',12**2/(2*g),7.346938775510203);ck(12,'range',20*tf,48.97959183673469);ck(12,'sameheight',12*tf-.5*g*tf**2,0)
t=math.sqrt(2*(21.3-1.8)/g);v=48/t;ck(13,'minimumspeed',v,24.1,tol=.002);ck(13,'impactenergy',math.hypot(v,g*t),math.sqrt(v*v+2*g*19.5))
v0=math.sqrt(2*g*.587)/math.sin(rad(58));ck(14,'takeoffspeed',v0,4.,tol=.001);ck(14,'range',v0*v0*math.sin(rad(116))/g,1.47,tol=.002)
ck(15,'lowerplanetgravity',g/2.76**2,1.2864944339424493)
vx,vy,tf=motion(40,60);ck(16,'initialcomponents',[vx,vy],[20,20*math.sqrt(3)]);ck(16,'topheight',vy*vy/(2*g),61.2244897959);ck(16,'range',vx*tf,141.3919026587);ck(16,'apexvy',vy-g*(vy/g),0)
vx17,vy17,_=motion(30,36.9);root=math.sqrt(vy17*vy17-2*g*10);ts=[(vy17-root)/g,(vy17+root)/g]
ck(17,'unroundedtimes',ts,[.6815154862212255,2.9945267096515336]);ck(17,'recoverheightatbothroots',[vy17*t-.5*g*t*t for t in ts],[10,10]);ck(17,'oppositeverticalvelocities',[vy17-g*t for t in ts],[root,-root]);st(17,'unroundedfirstrootboundtofragment',r'0{,}682'in units[17])
vx18,vy18=polar(12,51);tf18=2.08;h18=.5*g*tf18**2-vy18*tf18
ck(18,'sourceinitialcomponents',[vx18,vy18],[7.55184469259805,9.32575153748365]);ck(18,'sourcehorizontalrange',vx18*tf18,15.707836960603945);ck(18,'derivedlaunchheight',h18,1.801796802034012);ck(18,'sourcefinalcomponents',[vx18,vy18-g*tf18],[7.55184469259805,-11.058248462516353]);st(18,'sourcegivensintheactualprompt',all(x in units[18].split('<details>')[0]for x in [r'12{,}0',r'51{,}0',r'2{,}08'])and r'18{,}0'not in units[18].split('<details>')[0])
vx,vy=polar(6.4,60);t=2.1/vx;ck(19,'height',vy*t-.5*g*t*t,1.5270527896446424);ck(19,'impactvy',vy-g*t,-.88868741578)
ck(20,'angle',math.degrees(math.acos((45/3)/25)),53.13010235415599);ck(20,'apexspeed',45/3,15);ck(20,'wallheight',20*3-.5*g*9,15.9);ck(20,'wallspeed',math.hypot(15,20-g*3),17.7,tol=.002)
vx21,vy21,tf21=motion(30,33,15);ck(21,'returnheight',vy21*tf21-.5*g*tf21**2,-15);ck(21,'impactenergy',math.hypot(vx21,vy21-g*tf21),math.sqrt(30**2+2*g*15));ck(21,'range',vx21*tf21,103,tol=.005)
vx22,vy22=polar(15,53);root=math.sqrt(vy22*vy22-2*g*5);ts=[(vy22-root)/g,(vy22+root)/g];ck(22,'twoactualsourceroots',ts,[.5340287517058324,1.9107738300715944]);ck(22,'twoheights',[vy22*t-.5*g*t*t for t in ts],[5,5]);ck(22,'oppositeverticalcomponents',[vy22-g*t for t in ts],[root,-root]);st(22,'15metrespersecondand5metresintheprompt',r'15{,}0'in units[22].split('<details>')[0]and r'5{,}00'in units[22].split('<details>')[0])
R=50;ck(23,'estimatedlaunchspeed',math.sqrt(g*R),22.1359436212);ck(23,'verticalheight',g*R/(2*g),25);ck(23,'Marsrange',g*R/3.7,132.43243243243242)
R=6*.3048;T=4;v=2*math.pi*R/T;a=v*v/R;ck(24,'radius',R,1.8288);ck(24,'estimatedspeed',v,2.87,tol=.002);ck(24,'halvedperiodfactor',(4*math.pi**2*R/(T/2)**2)/a,4)
R=6.38e6;T=86400;a=4*math.pi**2*R/T**2;Tc=2*math.pi*math.sqrt(R/g);ck(25,'centripetalacceleration',a,.03374,tol=.001);ck(25,'fractionofgravity',a/g,.0034429,tol=.001);ck(25,'criticalperiodseconds',Tc,5070,tol=.001);st(25,'strictlosscontactcondition',r'T<T_{\mathrm c}'in units[25])
a=(2*math.pi*3)**2*.07;ck(26,'inner-earacceleration',a,24.871403091);ck(26,'ingunits',a/g,2.5378982746)
R=.8*math.sin(rad(37));ck(27,'horizontalorbitradius',R,.48145201852163864);ck(27,'radialacceleration',4*math.pi**2*R/.6**2,52.8,tol=.001)
omega=550*2*math.pi/60;ck(28,'tiplinearspeed',omega*3.4,195.82594207376);ck(28,'tipradialaccelerationing',omega**2*3.4/g,1150,tol=.002)
v=math.sqrt(5.5*g*280);ck(29,'thresholdspeed',v,122.849502237);ck(29,'mphconversion',v/.44704,274.8065081949931)
for v,T in [(2.,3.),(15.,20.)]:
 R=v*T/(2*math.pi);ck(30,'radiuselimination',v*v/R,2*math.pi*v/T);ck(30,'doublevdoubleT',2*math.pi*(2*v)/(2*T),2*math.pi*v/T);ck(30,'doublerootTfor2R',4*math.pi**2*(2*R)/(math.sqrt(2)*T)**2,v*v/R)
ck(31,'radialacceleration',6**2/14,2.5714285714285716);ck(31,'period',2*math.pi*14/6,14.660765716752367)
for v1,v2,R in [(2.,3.,4.),(4.,10.,12.)]:ck(32,'bottomtopratio',(v2*v2/R)/(v1*v1/R),(v2/v1)**2)
omega=math.sqrt(12.5*g/8.84);ck(33,'headspeed',omega*8.84,32.907445084,tol=1e-7);ck(33,'headfeetdifference',omega**2*2,27.71493212669683);ck(33,'rotationrpm',omega*60/(2*math.pi),35.5482,tol=1e-5)
for planet,R,days,v,a in [('Earth',1.5e11,365,2.99e4,5.95e-3),('Mercury',5.79e10,88,4.78e4,.0395)]:
 T=days*86400;ck(34,planet+'orbitspeed',2*math.pi*R/T,v,tol=.002);ck(34,planet+'radialacceleration',4*math.pi**2*R/T**2,a,tol=.002)
ck(35,'walkwaytimes',[35/(1.5+1),35/(1.5-1)],[14,70]);ck(36,'threeflatcarrelativevelocities',np.array([18,-3,0])-13,[5,-16,-13])
v=polar(.4,-45)-[.5,0];ck(37,'relativecanoecomponents',v,[-.217157287525381,-.282842712474619]);ck(37,'relativespeed',np.linalg.norm(v),.3566,tol=.001)
ck(38,'rowerroundtrip',1.5/(4+2.8)+1.5/(4-2.8),1.4705882352941178);ck(38,'walkerroundtrip',3/4,.75)
speed=math.sqrt(100**2-40**2);ck(39,'westofsouthangle',math.degrees(math.asin(.4)),23.578178478201835);ck(39,'groundsouthspeed',speed,91.6515138991168);ck(39,'travelhours',500/speed,5.45544725589981)
wind=np.array([-10/math.sqrt(2),-10/math.sqrt(2)]);air=np.array([0,-35]);v=air+wind;ck(40,'groundcomponents',v,[-7.0710678118654755,-42.071067811865476]);ck(40,'groundspeed',np.linalg.norm(v),42.7,tol=.002)
v=np.array([4.2,-2]);t=500/4.2;ck(41,'groundspeed',np.linalg.norm(v),4.651881339845203);ck(41,'crosstime',t,119.04761904761904);ck(41,'southdrift',2*t,238.09523809523807)
east=math.sqrt(4.2**2-2**2);ck(42,'headingnorthofeast',math.degrees(math.asin(2/4.2)),28.436890148855372);ck(42,'eastvelocity',east,3.693237062523878);ck(42,'crossingtime',500/east,135.38,tol=.001)
east=-math.sqrt(320**2-80**2);ck(43,'airspeedwithcrosswind',np.linalg.norm([east,80]),320);ck(43,'groundsouthcomponent',80-80,0);ck(43,'headingnorthofwest',math.degrees(math.asin(.25)),14.477512185929925);ck(43,'groundspeed',-east,309.83866769659335)
originals=json.loads((B/'parent-numbered-early-image-assets.json').read_text('utf8'))
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as pdf:
 for row in originals:
  p=ROOT/row['publicFile'];pix=pymupdf.Pixmap(p);expected=pdf[row['pdfPage1Based']-1].get_pixmap(matrix=pymupdf.Matrix(row['scale'],row['scale']),clip=pymupdf.Rect(row['rectangle']),alpha=False)
  st(row['key'],'exactoriginalpixels',pix.samples==expected.samples and pix.width==expected.width and pix.height==expected.height);st(row['key'],'sourceimageSHA',sha(p)==row['sha256']);st(row['key'],'canonicalsourceimagelink',text.count('(/'+row['publicFile'].removeprefix('docs/')+')')==1)
expectedModels={9:(1.1,0,.48),12:(20,12,24/g),18:(vx18,vy18,2.08),21:(vx21,vy21,tf21)}
plots=0
for row in json.loads((B/'parent-numbered-early-solution-image-manifest.json').read_text('utf8'))['assets']:
 p=ROOT/row['publicFile'];st(row['sourceUnit'],'solutionSHA',sha(p)==row['sha256']);svg=ET.parse(p).getroot();n=int(row['sourceUnit'].split('.')[1])
 if n in expectedModels:
  vx,vy,tf=expectedModels[n];expectedFunctions={'x':lambda t:vx*t,'y':lambda t:vy*t-.5*g*t*t,'vₓ':lambda t:vx,'vᵧ':lambda t:vy-g*t}
  for panel in row['panels']:
   node=next(p for p in svg.findall('.//{*}polyline')if p.get('data-quantity')==panel['quantity']);pts=np.array([[float(a)for a in q.split(',')]for q in node.get('points').split()]);st(n,'201plottedtimes '+panel['quantity'],len(pts)==201);lo,hi=panel['valueRange']
   for i,(x,y)in enumerate(pts):
    value=expectedFunctions[panel['quantity']](tf*i/200);ck(n,panel['quantity']+'actualSVGpoint'+str(i),[x,y],[72+240*i/200,190-(value-lo)/(hi-lo)*140],tol=1e-6);plots+=1
 else:
  mapping=row['screenMapping'];center=np.array(mapping['centerWorld']);origin=np.array(mapping['centerScreen']);scale=mapping['scale']
  def world(p):return(np.array(p)-center)*[scale,-scale]+origin
  for i,arrow in enumerate(row['arrows']):
   line=next(x for x in svg.findall('.//{*}line')if x.get('data-arrow')==str(i));actual=[[float(line.get(k))for k in ['x1','y1']],[float(line.get(k))for k in ['x2','y2']]];ck(n,'actualarrow'+str(i),actual,[world(arrow['startWorld']),world(arrow['endWorld'])],tol=1e-6)
  if n in [3,7]:
   node=next(x for x in svg.findall('.//{*}polyline')if x.get('data-trajectory')=='true');pts=np.array([[float(a)for a in q.split(',')]for q in node.get('points').split()]);st(n,'201actualtrajectorypoints',len(pts)==201)
   for i,point in enumerate(pts):
    t=i/100;expected=[4+2.5*t*t,5*t]if n==3 else[2.4*t,3-1.2*t*t];ck(n,'actualtrajectorypoint'+str(i),point,world(expected),tol=1e-6);plots+=1
   if n==3:
    for t,arrow in zip([0,1,2],row['arrows']):ck(n,'actualtangentvelocity'+str(t),(np.array(arrow['endWorld'])-arrow['startWorld'])/.4,[5*t,5])
   else:
    ck(n,'actualvelocityarrow',(np.array(row['arrows'][0]['endWorld'])-row['arrows'][0]['startWorld'])/.3,[2.4,-4.8]);ck(n,'actualaccelerationarrow',(np.array(row['arrows'][1]['endWorld'])-row['arrows'][1]['startWorld'])/.5,[0,-2.4])
  if n==5:ck(n,'actualsourcevelocities',[row['arrows'][i]['endWorld']for i in [0,1]],[[90,110],[-170,40]])
  if n==6:ck(n,'actualsourcevelocities',[row['arrows'][i]['endWorld']for i in [0,1]],[[2.6,-1.8],vf])
  if n==40:ck(n,'sourcevectors',[row['sourceParameters']['air'],row['sourceParameters']['wind']],[air,wind])
  if n==43:ck(n,'cancelcrosswind',row['sourceParameters']['ground'],[east,0])
st('all','every43unithasanindependentnumericorsymboliccheck',set(range(1,44)).issubset(set(x['unit']for x in checks)))
assert not failures,failures
print(json.dumps({'status':'passed-canonical-early43units','units':43,'checks':len(checks),'actualPlotPointsChecked':plots,'originalCrops':6,'solutionDiagrams':10,'scope':'Numberedearlyonly;whole115gate separate.'},ensure_ascii=False))
