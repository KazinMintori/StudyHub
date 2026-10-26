from pathlib import Path
import json,math,re,hashlib,xml.etree.ElementTree as ET
import numpy as np,pymupdf
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[2];B=ROOT/'raw_materials/physics/translations/chapter-03';g=9.8;rad=math.radians;checks=[];plotPoints=0
def ck(n,label,actual,expected,tol=1e-8):
 assert np.allclose(actual,expected,atol=tol,rtol=tol),(n,label,actual,expected)
 checks.append({'unit':n,'check':label,'actual':np.asarray(actual).tolist(),'expected':np.asarray(expected).tolist()})
def st(n,label,condition):
 assert condition,(n,label);checks.append({'unit':n,'check':label,'passed':True})
def v(u,d):return np.array([u*math.cos(rad(d)),u*math.sin(rad(d))])
def landing(vx,vy,h):return brentq(lambda t:h+vy*t-g*t*t/2,1e-8,100)
def launch_speed(x,y,d):
 c,s=math.cos(rad(d)),math.sin(rad(d))
 return brentq(lambda u:x*s/c-g*x*x/(2*u*u*c*c)-y,.01,1000)
def sha(p):
 data=p.read_bytes()
 if p.suffix.lower()in {'.md','.svg'}:data=data.replace(b'\r\n',b'\n')
 return hashlib.sha256(data).hexdigest()
file=B/'parent-12-bai-tap-044-085.md';text=file.read_text('utf8')
units={int(m[1]):m[2]for m in re.finditer(r'^### 3\.(\d+)[^\n]*\n([\s\S]*?)(?=^### |^## |\Z)',text,re.M)}
st('all','42orderedsourceunits',list(units)==list(range(44,86)))
for n,body in units.items():
 st(n,'oneclosedsolution',body.count('<details>')==body.count('</details>')==1 and'<details open'not in body)
 st(n,'threepedagogicalstages',all(body.count(x)==1 for x in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']))
st('all','balancedinline/controlchars',not any(l.replace('$$','').count('$')%2 for l in text.splitlines())and not any(ord(c)<32 and c not in '\n\r\t'for c in text))
st('all','nothinkingaloud',not re.search(r'\b(?:Khoan đã|À không|Wait|Nhầm rồi|Thử lại nào)\b',text,re.I))
for n,letters in [(46,'abc'),(47,'ab'),(48,'ab'),(50,'ab'),(51,'ab'),(52,'ab'),(55,'ab'),(57,'ab'),(59,'abcd'),(60,'ab'),(61,'abc'),(62,'ab'),(63,'ab'),(64,'ab'),(65,'ab'),(69,'ab'),(70,'abc'),(71,'ab'),(72,'ab'),(76,'abc'),(77,'abc'),(78,'ab'),(80,'ab')]:
 st(n,'allsourcequestionparts',all('('+x+')'in units[n].split('<details>')[0]for x in letters));st(n,'allsourcepartanswers',all('('+x+')'in units[n].split('**Lời giải:**')[1]for x in letters))
ck(44,'distanceaftertwointegrations',np.linalg.norm([.4*8**2/2,-.18*8**3/6]),19.994239170321034)
for b,c in [(1.,2.),(.5,7.),(4.,.1)]:
 t=2*b/(3*c);ck(45,'45degreevelocity '+str((b,c)),2*b*t,3*c*t*t);st(45,'nonzerovelocity',2*b*t>0)
a=2.5;beta=9.;gamma=1.4
th=brentq(lambda t:7+beta*t-gamma*t*t/2,1,30);tf46=brentq(lambda t:7*t+beta*t*t/2-gamma*t**3/6,1,40)
ck(46,'apextimefromroot',th,13.592825096068475);ck(46,'maxheight',7*th+4.5*th*th-gamma*th**3/6,340.58052492011655);ck(46,'returntime',tf46,20.732703574505827);ck(46,'xfromintegratedacceleration',tf46+a*tf46**4/12,38513.79976251896)
u=math.sqrt(2*1.9*200);vx,vy=v(u,35);h=200*math.sin(rad(35));tf=landing(vx,vy,h)
ck(47,'rampworkkinematics',u*u,760);ck(47,'heightaboveground',h+vy*vy/(2*g),127.47203959348707);ck(47,'rangefromA',200*math.cos(rad(35))+vx*tf,315.44844265420613)
t=4*math.tan(rad(30));ck(48,'velocityangle',math.degrees(math.atan2(-.045*t*t,.18*t)),-30);ck(48,'accelerationmagnitude',math.hypot(.18,-.09*t),.2749545416973504);ck(48,'accelerationdirection',math.degrees(math.atan2(-.09*t,.18)),-49.106605350869096)
ck(49,'horizontaldropdistance',64*landing(64,0,90),274.2857142857143)
t=math.sqrt(3*2.4/1.6);ck(50,'xzeroaftert0',2.4*t-1.6*t**3/3,0);ck(50,'heightatxzero',4*t*t/2,9)
tf51=landing(15,10,30);ck(51,'timefromheightroot',tf51,3.6969136833885714);ck(51,'matpositionsouth',15*tf51,55.45370525082857)
u52=launch_speed(60,25,43);vx52,vy52=v(u52,43);tedge=60/vx52
ck(52,'clearancevelocityroot',u52,32.64263051691944);ck(52,'heightatedge',vy52*tedge-.5*g*tedge**2,25);st(52,'descendingatedge',vy52-g*tedge<0);ck(52,'edgeverticalvelocity',vy52-g*tedge,-2.3677965980518643);st(52,'0beyondedgeinactualsolution',r'0\,\mathrm m'in units[52].split('**Lời giải:**')[1])
for k in [1.00001,1.001,1.01]:
 vx,vy=v(k*u52,43);tf=brentq(lambda t:vy*t-.5*g*t*t-25,vy/g,20);st(52,'fasterlaunchlandsbeyondedge'+str(k),vx*tf>60)
t=math.sqrt(60/g);ck(53,'horizontalintegration',12*t+1.6*t**3/6,33.732068205714576)
vx,vy=v(15,60);tf=landing(vx,vy,8.75);D=(vx+.45)*tf;ck(54,'shipinitialdistance',D,25.50185408465135);ck(54,'movingtargetinterception',D-.45*tf,vx*tf)
u55=launch_speed(18,8,60);vx55,vy55=v(u55,60);tf55=18/vx55;vf55=[vx55,vy55-g*tf55]
ck(55,'v0root',u55,16.552848154213542);ck(55,'heightatreachingwall',vy55*tf55-.5*g*tf55**2,8);ck(55,'speedandenergy',np.linalg.norm(vf55),math.sqrt(u55*u55-2*g*8));ck(55,'impactdirection',math.degrees(math.atan2(vf55[1],vf55[0])),-40.136311518973024)
vx,vy=v(75,55);ck(56,'haydropahead',vx*landing(vx,vy,150),629.3744743220334)
vy57=math.sqrt(2*g*.0674);u57=vy57/math.sin(rad(50));vx57=u57*math.cos(rad(50));tf57=1.06/vx57;ck(57,'takeoffspeed',u57,1.5003895040601698);ck(57,'cliffheight',.5*g*tf57**2-vy57*tf57,4.655965288171394)
for q in [9,9.2,9.5,9.8]:
 u2=q*g;near=6-g*36/u2;far=7-g*49/u2;ck(58,'nearclearancepredicate'+str(q),near>=2-1e-10,True);ck(58,'farclearancepredicate'+str(q),far<=2+1e-10,True);st(58,'descendingatmouth'+str(q),1-12/q<0)
for speed,theta,H in [(5,-90,4),(5,90,4),(20,35,10),(8,-25,30)]:
 vx,vy=v(speed,theta);t=landing(vx,vy,H);ck(59,'independentlandingenergy'+str((speed,theta,H)),math.hypot(vx,vy-g*t),math.sqrt(speed**2+2*g*H))
dx=36*.3048;dy=10*.3048;ck(60,'anglelowerbound',math.degrees(math.atan(dy/dx)),15.524110996754255);ck(60,'45degthreshold',launch_speed(dx,dy,45),12.202149621464875)
vx61,vy61=v(7,-40);tf61=landing(vx61,vy61,14);ck(61,'landingdistance',vx61*tf61,6.930366463283156);tm=4/vx61;ck(61,'heightatman',14+vy61*tm-.5*g*tm*tm,7.9170603696239255);st(61,'clears1.9mman',14+vy61*tm-.5*g*tm*tm>1.9)
vy62=math.sqrt(20**2-6**2);tf62=landing(6,vy62,45);ck(62,'launchangle',math.degrees(math.acos(6/20)),72.54239687627792);ck(62,'runnerrange',6*tf62,33.29235258231704);ck(62,'relativehorizontalzero',6*tf62-6*tf62,0)
u63=launch_speed(40,-15,53);vx,vy=v(u63,53);t=40/vx;ck(63,'farbankcondition',vy*t-.5*g*t*t,-15);vx,vy=v(u63/2,53);tf=landing(vx,vy,100);ck(63,'half-speedwaterlanding',vx*tf,28.448862301438155);st(63,'hitsrivernotbank',vx*tf<40)
tf=math.sqrt(76/g);u=3.05*(9+tf)/tf;ck(64,'throwvelocity',u,12.907087017658116);ck(64,'meetingpositions',u*tf,3.05*(9+tf));ck(64,'catchdistance',u*tf,35.94363507190495)
u=100/math.sqrt(40/g);ck(65,'minimumspeed',u,49.49747468305832);ck(65,'totaldrop45mrange',u*math.sqrt(90/g)-100,50)
vx66,vy66=v(25,53);roots=np.sort(np.roots([-g/2,vy66,-10]));ck(66,'twoheightroots',roots,[.584779272079947,3.4898916975490977]);ck(66,'twowallpositions',vx66*roots,[8.798223779140782,52.50673131896629])
ck(67,'timefromapexhorizontalspeed',50/8,6.25)
for alpha,u in [(10,3),(35,12),(65,8)]:
 t=2*u*math.tan(rad(alpha))/g;h=.5*g*t*t;ck(68,'intersectincline'+str(alpha),h,u*t*math.tan(rad(alpha)));ck(68,'explicitverticaldrop'+str(alpha),h,2*u*u*math.tan(rad(alpha))**2/g)
u69=launch_speed(14,3.4,56);vx,vy=v(u69,56);tf=landing(vx,vy,1.6);ck(69,'thresholdspeed',u69,13.302750197350338);ck(69,'fencetopheight',1.6+vy*(14/vx)-.5*g*(14/vx)**2,5);ck(69,'beyondfencerange',vx*tf-14,3.759980832529294)
vx,vy=v(16,60);R=2*vx*vy/g;H=vy*vy/(2*g);ck(70,'apexx',vx*vy/g,R/2);ck(70,'80percentheight',vy*(.8*R/vx)-.5*g*(.8*R/vx)**2,.64*H)
for a in [0,.5,.8,1]:ck(70,'universalparabola'+str(a),(vy*(a*R/vx)-.5*g*(a*R/vx)**2)/H,4*a*(1-a))
wind=np.array([-120,-20])/.5-[-220,0];ck(71,'windcomponents',wind,[-20,-40]);ck(71,'windspeed',np.linalg.norm(wind),44.721359549995796);ck(71,'cancelnewcrosswind',220*math.sin(math.asin(40/220))-40,0)
w=12/math.tan(rad(30));ck(72,'verticalrain',w,20.784609690826528);ck(72,'trainrainmagnitude',math.hypot(12,w),24)
relative=v(12,53)-[0,8];ck(73,'relativeballcomponents',relative,[7.22178027782458,1.583626120567514]);ck(73,'relativeballspeed',np.linalg.norm(relative),7.393374200655597)
ck(74,'runningeast',math.sqrt(9**2-6**2),6.708203932499369)
ball=v(5,-60)+[0,6];ck(75,'ballgroundscomponents',ball,[2.5,1.6698729810778072]);ck(75,'ballgroundspeed',np.linalg.norm(ball),3.0064057897984573)
# Independent extraction of all11actualsourcecirclecenters and calibration.
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as pdf:
 marks=[]
 for drawing in pdf[117].get_drawings():
  r=drawing['rect']
  if 405<r.x0<510 and 240<r.y0<320 and abs(r.width-4)<1e-4 and abs(r.height-4)<1e-4 and drawing['fill']and max(drawing['fill'])<.2:marks.append([(r.x0+r.x1)/2,(r.y0+r.y1)/2])
marks=np.array(sorted(marks));st(76,'11actualPDFvectormarks',len(marks)==11)
angles=15+60*(marks[:,0]-411.5910034)/(506.9400024-411.5910034);ranges=6+6*(marks[:,1]-317.8045959)/(245.2050018-317.8045959);X=np.sin(2*np.deg2rad(angles));xm,ym=X.mean(),ranges.mean();s76=np.sum((X-xm)*(ranges-ym))/np.sum((X-xm)**2);b76=ym-s76*xm
ck(76,'independentOLSslope',s76,10.952352651439703);ck(76,'independentOLSintercept',b76,.03832916363244599);ck(76,'sourcevelocityestimate',math.sqrt(g*s76),10.360166793257196);ck(76,'predictedheight',s76*math.sin(rad(36.9))**2/2,1.9741859178707135)
heights=np.array([2.,6.,9.,12.]);rr=np.array([10.4,17.1,21.3,25.8]);yy=rr**2;hm,ym=heights.mean(),yy.mean();s77=np.sum((heights-hm)*(yy-ym))/np.sum((heights-hm)**2);b77=ym-s77*hm
ck(77,'independentOLSslope',s77,55.20356164383561);ck(77,'independentOLSintercept',b77,-20.25082191780783);ck(77,'launchspeed',math.sqrt(g*s77/2),16.44680674340142);ck(77,'30degreerange',s77*math.sin(rad(60))/2,23.903843381470942)
w2=(9**2-6**2)/(1/11.2**2-1/20.1**2);width=math.sqrt(w2);current=math.sqrt(36-w2/20.1**2);ck(78,'width',width,90.4801193704579);ck(78,'current',current,3.966927207460404)
ck(78,'firsttriprecoverboatspeed',math.hypot(width/20.1,current),6);ck(78,'secondtriprecoverboatspeed',math.hypot(width/11.2,current),9);ck(78,'shortesttime',width/6,15.080019895076317);ck(78,'drift',current*width/6,59.821341210822425)
limit=math.asin(math.sqrt(8/9));ck(79,'maxangle',math.degrees(limit),70.52877936550931)
for theta in [0,20,60,math.degrees(limit),75,85]:
 u=20;vertex=3*u*math.sin(rad(theta))/(2*g);qmin=2*u*u-9*u*u*math.sin(rad(theta))**2/4
 st(79,'qmincriterion'+str(theta),(qmin>=-1e-8)==(theta<=math.degrees(limit)+1e-8))
 t=vertex;vx,vy=v(u,theta);r=np.array([vx*t,vy*t-.5*g*t*t]);vel=np.array([vx,vy-g*t]);ck(79,'radialderivativepolynomial'+str(theta),2*(r@vel),t*(g*g*t*t-3*g*u*math.sin(rad(theta))*t+2*u*u))
current80=1.5;canoe80=3.5;ck(80,'upstream1hour',canoe80-current80,2);ck(80,'downstream1hour',canoe80+current80,5);ck(80,'bottle2hourdrift',2*current80,5-2)
ax=3*g*math.cos(rad(30));ay=3*g*math.sin(rad(30));t2=math.sqrt(2000/ax)
t1=brentq(lambda q:-g*q*q/2-g*q*t2+ay*t2*t2/2,.001,20);tf81=t1+t2;vplane=850/3.6
ck(81,'independentdelayroot',t1,5.150577324659582);ck(81,'poweredflighttime',t2,8.862903420019995);ck(81,'returntosameheight',-.5*g*t1*t1-g*t1*t2+.5*ay*t2*t2,0);ck(81,'onekmseparation',.5*ax*t2*t2,1000)
for factor in [.5,.9,1.,1.2]:
 delay=factor*t1;power=delay*(2+math.sqrt(10))/3;gap=.5*ax*power*power;st(81,'minimumtimecriterion'+str(factor),(gap>=1000-1e-7)==(factor>=1))
vmax=math.sqrt(4.6**2+2*g*.2);ck(82,'conservativeframerate',vmax/.0002,25039.968051097825);st(82,'nominalchoiceandstrictlimitdistinguished','phương án (c)'in units[82]and r'25\,040'in units[82])
ck(83,'verticaltime',4.6/g,.4693877551020407);ck(84,'horizontalseedrange',4.6*math.sqrt(.4/g),.9293403409880338)
for u in [2.3,4.6]:
 theta=math.asin(1/math.sqrt(2+2*g*.2/u**2));Rmax=u/g*math.sqrt(u*u+2*g*.2)
 for angle in [0,10,20,30,math.degrees(theta),50,70,90]:
  vx,vy=v(u,angle);t=landing(vx,vy,.2);st(85,'optimizedrangemax'+str((u,angle)),vx*t<=Rmax+1e-8)
st(85,'interpretationnotcausalproof','chưa đủ để khẳng định'in units[85]and'(c)'in units[85])
for n in [82,83,84,85]:
 prompt=units[n].split('<details>')[0];st(n,'fouractualchoices',all('('+x+')'in prompt for x in 'abcd'))
originals=json.loads((B/'parent-numbered-late-image-assets.json').read_text('utf8'))
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as pdf:
 for row in originals:
  p=ROOT/row['publicFile'];actual=pymupdf.Pixmap(p);expected=pdf[row['pdfPage1Based']-1].get_pixmap(matrix=pymupdf.Matrix(row['scale'],row['scale']),clip=pymupdf.Rect(row['rectangle']),alpha=False)
  st(row['key'],'exactPDFpixels',actual.samples==expected.samples and actual.width==expected.width and actual.height==expected.height);st(row['key'],'imageSHA',sha(p)==row['sha256']);st(row['key'],'canonicalsourceimagelink',text.count('(/'+row['publicFile'].removeprefix('docs/')+')')==1)
def rocket_state(t):
 tau=max(0,t-t1)
 return[vplane*t+.5*ax*tau*tau,-.5*g*t*t]if t<=t1 else[vplane*t+.5*ax*tau*tau,-.5*g*t1*t1-g*t1*tau+.5*ay*tau*tau]
for row in json.loads((B/'parent-numbered-late-solution-image-manifest.json').read_text('utf8'))['assets']:
 p=ROOT/row['publicFile'];st(row['sourceUnit'],'solutionSHA',sha(p)==row['sha256']);svg=ET.parse(p).getroot();key=row['key'].removeprefix('solution-image:');n=int(re.match(r'S3\.(\d+)',key)[1])
 if n in [51,61]:
  vx,vy,tf,y0=(15,10,tf51,0)if n==51 else(vx61,vy61,tf61,14)
  fun={'x':lambda t:vx*t,'y':lambda t:y0+vy*t-g*t*t/2,'vₓ':lambda t:vx,'vᵧ':lambda t:vy-g*t}
  for panel in row['panels']:
   node=next(x for x in svg.findall('.//{*}polyline')if x.get('data-quantity')==panel['quantity']);pts=np.array([[float(a)for a in q.split(',')]for q in node.get('points').split()]);st(n,'201times'+panel['quantity'],len(pts)==201);lo,hi=panel['valueRange']
   for i,point in enumerate(pts):
    value=fun[panel['quantity']](tf*i/200);ck(n,panel['quantity']+'actualSVGsample'+str(i),point,[72+240*i/200,190-(value-lo)/(hi-lo)*140],tol=1e-6);plotPoints+=1
 else:
  for panel in row['panels']:
   xlo,xhi=panel['xRange'];ylo,yhi=panel['yRange']
   for series in panel['series']:
    node=next(x for x in svg.findall('.//{*}polyline')if x.get('data-series')==series['key']);pts=np.array([[float(a)for a in q.split(',')]for q in node.get('points').split()]);world=np.array(series['worldPoints']);ck(n,'samplecount'+series['key'],len(pts),len(world));q=series['key']
    for i,((wx,wy),point)in enumerate(zip(world,pts)):
     ck(n,q+'actualSVGmapping'+str(i),point,[76+(wx-xlo)/(xhi-xlo)*235,218-(wy-ylo)/(yhi-ylo)*145],tol=1e-6)
     if q=='ground-path':ck(n,'sourcegroundtrajectory'+str(i),wy,45+vy62*(wx/6)-g*(wx/6)**2/2)
     elif q=='runner-path':ck(n,'sourceconstantrelativex'+str(i),wx,0)
     elif q=='trajectory':ck(n,'sourcetargetparabola'+str(i),wy,vy66*(wx/vx66)-g*(wx/vx66)**2/2)
     elif q=='fire-height':ck(n,'sourcefireheight',wy,10)
     elif q=='fit':ck(n,'independentregression'+str(i),wy,(s76*wx+b76)if n==76 else(s77*wx+b77))
     elif q=='plane-path':ck(n,'planeconstantheight'+str(i),wy,0)
     elif q=='rocket-path':ck(n,'actualrocketpath'+str(i),wy,rocket_state(brentq(lambda t:rocket_state(t)[0]-wx,0,tf81+1))[1],tol=1e-6)
     elif q=='plane-x':ck(n,'planeX'+str(i),wy,vplane*wx)
     elif q=='plane-y':ck(n,'planeY'+str(i),wy,0)
     elif q=='rocket-x':ck(n,'rocketX'+str(i),wy,rocket_state(wx)[0])
     elif q=='rocket-y':ck(n,'rocketY'+str(i),wy,rocket_state(wx)[1])
     plotPoints+=1
   if n in [76,77]:
    expected=np.column_stack((X,ranges))if n==76 else np.column_stack((heights,rr*rr));ck(n,'actualsourceobservations',[point[:2]for point in panel['points']],expected)
  for i,panel in enumerate(row.get('vectorPanels',[])):
   state=panel['state'];t=state['time'];tau=max(0,t-t1);before=state['label'].startswith(('A:','B−:'));rv=[vplane+ax*tau,-g*t]if before else[vplane+ax*tau,-g*t1+ay*tau];ra=[0,-g]if before else[ax,ay]
   for key,color,value,scale in [('plane-v','#2563eb',[vplane,0],.4),('rocket-v','#be123c',rv,.4),('rocket-a','#15803d',ra,3)]:
    line=next(x for x in svg.findall('.//{*}line')if x.get('data-state')==str(i)and x.get('data-vector')==key);delta=np.array([float(line.get('x2'))-float(line.get('x1')),float(line.get('y2'))-float(line.get('y1'))]);ck(n,'actualstatevector'+str((i,key)),delta,np.array(value)*[scale,-scale],tol=1e-6)
st('all','all42unitshavemeaningfulchecks',set(range(44,86)).issubset(set(x['unit']for x in checks)))
print(json.dumps({'status':'passed-canonical-late42units','units':42,'checks':len(checks),'actualPlotPointsChecked':plotPoints,'originalCrops':9,'solutionDiagrams':9,'scope':'Numberedlateonly;whole115gate separate.'},ensure_ascii=False))
