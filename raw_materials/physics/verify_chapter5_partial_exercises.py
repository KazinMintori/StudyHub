from pathlib import Path
import json,math,re,hashlib,xml.etree.ElementTree as ET
import numpy as np,pymupdf
from scipy.optimize import linprog
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parents[2];B=ROOT/'raw_materials/physics/translations/chapter-05';records=[]
def ck(unit,label,actual,expected,tol=1e-8):
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(unit,label,actual,expected)
 records.append({'unit':unit,'check':label,'actual':np.asarray(actual).tolist(),'expected':np.asarray(expected).tolist(),'passed':True})
def st(unit,label,value):
 assert value,(unit,label);records.append({'unit':unit,'check':label,'passed':True})
g=9.8;rad=math.radians
T=255.;w=T/math.sin(rad(36.9));ck('VP5.5.1','cartweight',w,425,tol=.002);ck('VP5.5.1','cart slope balance',w*math.sin(rad(36.9)),T)
T=155.;w=T/math.sin(rad(25));ck('VP5.5.2','cart weight',w,367,tol=.002);ck('VP5.5.2','combined weight',w+T,522,tol=.002)
alpha=math.asin(65/175);ck('VP5.5.3','incline angle',math.degrees(alpha),21.8,tol=.001);ck('VP5.5.3','tension',65*g,637);ck('VP5.5.3','cart tension',175*g*math.sin(alpha),637)
for theta in [10,35,70]:
 s=math.sin(rad(theta));c=math.cos(rad(theta));w=100.;f=w*(1-s);n=w*c;mu=f/n
 ck('VP5.5.4','slope balance '+str(theta),w-w*s-f,0)
 st('VP5.5.4','friction less than weight '+str(theta),0<f<w)
 ck('VP5.5.4','minimum coefficient '+str(theta),mu*n,f)
for unit,theta,sign,Texpected,Nexpected in [('VP5.15.1',20,1,79.3,298),('VP5.15.2',15,-1,90.2,348)]:
 s=math.sin(rad(theta));c=math.cos(rad(theta));T=.25*325/(c+sign*.25*s);n=325-sign*T*s
 ck(unit,'tension',T,Texpected,tol=.002);ck(unit,'normal',n,Nexpected,tol=.002);ck(unit,'horizontal balance',T*c-.25*n,0);ck(unit,'vertical balance',n+sign*T*s,325)
n=475-125*math.sin(rad(12));a=(125*math.cos(rad(12))-.2*n)/(475/g)
ck('VP5.15.3','normal',n,449,tol=.001);ck('VP5.15.3','acceleration',a,.670,tol=.002);st('VP5.15.3','speed increases',a>0)
for theta in [0,20,55]:
 mu=.45;m=12.;s=math.sin(rad(theta));c=math.cos(rad(theta));T=mu*m*g/(c+mu*s);n=m*g-T*s
 ck('VP5.15.4','recover staticcoefficient '+str(theta),T*c/n,mu)
 st('VP5.15.4','maintained contact '+str(theta),n>0)
L=.8;m=.25;b=rad(20);R=L*math.sin(b);period=2*math.pi*math.sqrt(L*math.cos(b)/g);tension=m*g/math.cos(b)
ck('VP5.22.1','radius',R,.274,tol=.002);ck('VP5.22.1','period',period,1.74,tol=.002);ck('VP5.22.1','tension',tension,2.61,tol=.002)
ck('VP5.22.1','horizontal dynamics',tension*math.sin(b),m*4*math.pi**2*R/period**2);ck('VP5.22.1','vertical dynamics',tension*math.cos(b),m*g)
b=rad(40);R=12.5**2/(g*math.tan(b));a=12.5**2/R;n=64*g/math.cos(b)
ck('VP5.22.2','turn radius',R,19.,tol=.002);ck('VP5.22.2','centripetalacceleration',a,8.22,tol=.002);ck('VP5.22.2','normal',n,819,tol=.002)
ck('VP5.22.2','horizontal normal component',n*math.sin(b),64*a);ck('VP5.22.2','vertical normal component',n*math.cos(b),64*g)
b=math.atan(80**2/(175*g));n=80*g/math.cos(b)
ck('VP5.22.3','bankangle',math.degrees(b),75,tol=.001);ck('VP5.22.3','apparentweight',n,3030,tol=.002);ck('VP5.22.3','load ratio',n/(80*g),3.86,tol=.002)
for x in [1.1,2,4]:
 m=70.;v=13.;b=math.acos(1/x);net=m*g*math.sqrt(x*x-1);R=v*v/(g*math.sqrt(x*x-1))
 ck('VP5.22.4','normal horizontal '+str(x),x*m*g*math.sin(b),net);ck('VP5.22.4','radius dynamics '+str(x),m*v*v/R,net)
for seat in [0,.3,.9]:
 w=100.;ws=seat*w;T=(w+ws)/2;n=(w-ws)/2
 ck('Q5.1','whole system '+str(seat),2*T,w+ws);ck('Q5.1','person '+str(seat),T+n,w);st('Q5.1','seat contact '+str(seat),n>=0)
ck('Q5.2','incline normal',10*g*math.cos(rad(30)),84.870489570875,tol=1e-6)
for theta in [.5,.1,.01]:
 T=100/(2*math.sin(theta));ck('Q5.3','clotheslineverticalbalance '+str(theta),2*T*math.sin(theta),100)
ck('Q5.4','net force driving uphill atconstantspeed',100*g*math.sin(rad(20))+15-(100*g*math.sin(rad(20))+15),0)
ck('Q5.5','inertialmassminusapparatus',12/(12/(70+8.5))-8.5,70)
for theta in [15,30,60]:
 s=math.sin(rad(theta));c=math.cos(rad(theta))
 for mu in [0,.3,.8]:
  parallel=10*g*(s+mu*c);denom=c-mu*s
  if denom>0:
   horiz=parallel/denom;st('Q5.6','parallelrequiresless '+str((theta,mu)),horiz>parallel)
   ck('Q5.6','fullhorizontalforcebalance '+str((theta,mu)),horiz*c-mu*(10*g*c+horiz*s),10*g*s)
ck('Q5.7','relativefreefallacceleration',g-g,0)
for theta in [10,35,70]:
 s=math.sin(rad(theta));c=math.cos(rad(theta));mu=math.tan(rad(theta))+.2
 up=10*g*(s+mu*c);down=10*g*(mu*c-s)
 ck('Q5.8','threshold difference '+str(theta),up-down,20*g*s);st('Q5.8','down easier '+str(theta),0<=down<up)
 mu=.1;aup=g*(s+mu*c);adown=g*(s-mu*c)
 st('Q5.9','ascentlargeracceleration '+str(theta),aup>abs(adown))
for theta in [10,30,50]:
 s=math.sin(rad(theta));c=math.cos(rad(theta));mu=.3;pull=mu*100*g/(c+mu*s);push=mu*100*g/(c-mu*s)
 st('Q5.10','pull smaller '+str(theta),pull<push)
 ck('Q5.10','pullbalance '+str(theta),pull*c,mu*(100*g-pull*s));ck('Q5.10','pushbalance '+str(theta),push*c,mu*(100*g+push*s))
st('Q5.11','jump and horizontalrungnormalexist',np.dot([0,1],[1,0])==0)
st('Q5.12','slidingforcebelowstaticmaximum',.2*100<.4*100)
normal=[10*(g+a)for a in[-.4*g,0,.4*g]];st('Q5.13','normalordering',normal[0]<normal[1]<normal[2])
ck('Q5.14','kineticfrictionacceleratesstationarybox',(.3*2*g)/2,.3*g)
for theta in np.linspace(0,2*math.pi,9):
 r=np.array([math.cos(theta),math.sin(theta)]);v=np.array([-math.sin(theta),math.cos(theta)])
 ck('Q5.15','centripetalforceworkzero',(-r)@v,0);ck('Q5.19','tangentnotradial',r@v,0)
b=rad(15);R=50.;v0=math.sqrt(g*R*math.tan(b));v=.6*v0
st('Q5.16','upslopestaticfrictionneeded',g*math.sin(b)-v*v/R*math.cos(b)>0)
for theta in [.1,.5,1.]:ck('Q5.17','verticaltension',10*g/math.sin(theta)*math.sin(theta),10*g)
for R in [2.,7.,20.]:
 vt2=g*R;vb2=vt2+4*g*R;ck('Q5.20','circularloopminimumload',1+vb2/(g*R),6)
dt=.1;t=np.arange(0,1.1,dt);y=.5*g*t*t;gaps=np.diff(y)
ck('Q5.21','vacuumfirstgapratio',gaps[:3]/gaps[0],[1,3,5])
vt=15.;t=np.linspace(0,6,61);v=vt*np.tanh(g*t/vt);acc=g/(np.cosh(g*t/vt)**2)
st('Q5.25','accelerationstartsgravityanddecays',acc[0]==g and np.all(np.diff(acc)<0)and acc[-1]<.02*g)
st('Q5.26','velocityincreasingwithdecliningslope',v[0]==0 and np.all(np.diff(v)>0)and np.all(np.diff(np.diff(v))<0))
for ratio in [.1,.5,1,3,10]:
 v0=ratio*vt;ta=vt/g*math.atan(ratio);td=vt/g*math.asinh(ratio);H=vt*vt/(2*g)*math.log1p(ratio*ratio)
 return_speed=vt*math.tanh(g*td/vt)
 st('Q5.22','returnspeedlessthanlaunch '+str(ratio),return_speed<v0)
 st('Q5.23','airresistanceascentshorter '+str(ratio),ta<td)
 ck('Q5.23','descentheightclosedsolution '+str(ratio),vt*vt/g*math.log(math.cosh(g*td/vt)),H)
for H in [2.,15.,40.]:
 times=[]
 for mass in [.06,.2]:
  terminal=math.sqrt(mass*g/.01);fall=terminal/g*math.acosh(math.exp(g*H/terminal**2));times.append(fall)
  st('Q5.24','airfallslowerthanvacuum '+str((H,mass)),fall>math.sqrt(2*H/g))
 st('Q5.24','heavierballlandsfirst '+str(H),times[1]<times[0])
for vx,vy in [(2.,7.),(12.,0),(30.,-15.)]:
 k=.03*math.hypot(vx,vy);ax=-k*vx;ay=-g-k*vy
 ck('Q5.27','exacttrajectorycurvature '+str((vx,vy)),(ay*vx-ax*vy)/(vx**3),-g/(vx*vx))
dragCases=[]
for drag in [.002,.01,.05]:
 for angle in [20,45,70]:
  def fun(t,z):
   speed=math.hypot(z[2],z[3]);return[z[2],z[3],-drag*speed*z[2],-g-drag*speed*z[3]]
  def apex(t,z):return z[3]
  apex.direction=-1
  def ground(t,z):return z[1]
  ground.direction=-1;ground.terminal=True
  sol=solve_ivp(fun,[0,60],[0,0,30*math.cos(rad(angle)),30*math.sin(rad(angle))],events=[apex,ground],rtol=1e-10,atol=1e-12,max_step=.03)
  st('Q5.27','eventsfound '+str((drag,angle)),len(sol.t_events[0])==len(sol.t_events[1])==1)
  up=sol.y_events[0][0][0];down=sol.y_events[1][0][0]-up
  st('Q5.27','ascendinghorizontalrangegreater '+str((drag,angle)),up>down)
  dragCases.append({'dragPerMass':drag,'angleDegrees':angle,'xUp':float(up),'xDown':float(down)})
for vx,vy in [(20.,-10.),(-20.,10.),(0.,0.)]:
 def flow(t,z):
  speed=math.hypot(*z);return[-.04*speed*z[0],g-.04*speed*z[1]]
 sol=solve_ivp(flow,[0,60],[vx,vy],rtol=1e-10,atol=1e-12,max_step=.1)
 ck('Q5.28','terminalvectorpositiveydown '+str((vx,vy)),sol.y[:,-1],[0,math.sqrt(g/.04)],tol=1e-7)
coneCases=[]
for degrees in [10.,35.,60.,80.]:
 b=rad(degrees);s=math.sin(b);c=math.cos(b)
 for mu in [0,.2,.55,1.5,3.,math.tan(b),1/math.tan(b)]:
  amin=max(0,g*(s-mu*c)/(c+mu*s));finite=(c-mu*s)>1e-9;amax=g*(s+mu*c)/(c-mu*s)if finite else math.inf
  eq=[[s,-c,-1],[c,s,0]];rhs=[0,g];ub=[[-mu,1,0],[-mu,-1,0]]
  low=linprog([0,0,1],A_ub=ub,b_ub=[0,0],A_eq=eq,b_eq=rhs,bounds=[(0,None),(None,None),(0,None)],method='highs')
  st('bridge','independentLPminimumsucceeds '+str((degrees,mu)),low.success)
  ck('bridge','independentLPminimum '+str((degrees,mu)),low.x[2],amin,tol=1e-7)
  high=linprog([0,0,-1],A_ub=ub,b_ub=[0,0],A_eq=eq,b_eq=rhs,bounds=[(0,None),(None,None),(0,None)],method='highs')
  if finite:st('bridge','independentLPmaximumsucceeds',high.success);ck('bridge','independentLPmaximum',high.x[2],amax,tol=1e-7)
  else:st('bridge','independentLPunboundedmaximum',high.status==3)
  for a in [0,.5,3.,20.,1000.]:
   n=g*c+a*s;f=g*s-a*c;feasible=abs(f)<=mu*n+1e-7;pred=(a>=amin-1e-7 and a<=amax+1e-7)
   st('bridge','rangeequivalenttofrictioncone '+str((degrees,mu,a)),feasible==pred)
  if amin>1e-8 and finite:
   h=.2;R=h/math.tan(b);tmax=2*math.pi*math.sqrt(R/amin);tmin=2*math.pi*math.sqrt(R/amax)
   st('bridge','minimumperiodnotgreater',tmin<=tmax+1e-9)
   qminus=(c+mu*s)/(s-mu*c);qplus=(c-mu*s)/(s+mu*c)
   ck('bridge','Tmaxexplicitmatchesdynamics',2*math.pi*math.sqrt(h*qminus/(g*math.tan(b))),tmax)
   ck('bridge','Tminexplicitmatchesdynamics',2*math.pi*math.sqrt(h*qplus/(g*math.tan(b))),tmin)
  coneCases.append({'betaDegrees':degrees,'mu':mu,'aMin':amin,'aMax':amax if finite else'unbounded','LPMinimumStatus':low.status,'LPMaximumStatus':high.status})
for b in [rad(15),rad(35),rad(70)]:
 h=.2;R=h/math.tan(b);a=g*math.tan(b);ck('bridge','frictionlessperiod',2*math.pi*math.sqrt(R/a),2*math.pi/math.tan(b)*math.sqrt(h/g))
progress=json.loads((B/'parent-exercise-progress.json').read_text(encoding='utf-8'));fragments={r['file']:(B/r['file']).read_text(encoding='utf-8')for r in progress['files']};ledger=[]
expected=[*(f'VP5.5.{i}'for i in range(1,5)),*(f'VP5.15.{i}'for i in range(1,5)),*(f'VP5.22.{i}'for i in range(1,5)),*(f'Q5.{i}'for i in range(1,29)),'Bài tập cầu nối']
for name,text in fragments.items():
 for match in re.finditer(r'^### (VP5\.\d+\.\d+|Q5\.\d+|Bài tập cầu nối)[^\n]*\n([\s\S]*?)(?=^### |\Z)',text,re.M):
  unit,body=match[1],match[2];prompt=body.split('<details>',1)[0]
  st(unit,'oneclosedsolution',body.count('<details>')==body.count('</details>')==1 and'<details open'not in body)
  st(unit,'threepedagogicalstages',all(body.count(s)==1 for s in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']))
  st(unit,'Vietnamese prompt',bool(re.search('[À-ỹ]',prompt)))
  if unit=='Bài tập cầu nối':st(unit,'actual10sourceguideitems',re.findall(r'^(\d+)\. ',prompt,re.M)==list(map(str,range(1,11))))
  if unit=='Q5.25':st(unit,'actualsourcepanel(d)', 'Chọn phương án (d)'in body)
  if unit=='Q5.26':st(unit,'actualsourcepanel(a)', 'Chọn phương án (a)'in body)
  if unit=='Q5.23':st(unit,'actualsourcewithairresistancepreserved','không bỏ qua lực cản'in prompt.lower())
  ledger.append({'id':unit,'file':name,'headingLine':text[:match.start()].count('\n')+1,'sourcePages':[178]if unit=='Bài tập cầu nối'else[177]if unit.startswith('VP')else[178]if int(unit.split('.')[1])<=11 else[179]})
st('all','exact41sourceunits',sorted(expected)==sorted(r['id']for r in ledger))
def sha(p):
 data=p.read_bytes()
 if p.suffix.lower()in {'.md','.svg'}:data=data.replace(b'\r\n',b'\n')
 return hashlib.sha256(data).hexdigest()
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as pdf:
 for row in json.loads((B/'parent-image-assets.json').read_text(encoding='utf-8')):
  p=ROOT/row['publicFile'];actual=pymupdf.Pixmap(p);expectedpix=pdf[row['pdfPage1Based']-1].get_pixmap(matrix=pymupdf.Matrix(row['scale'],row['scale']),clip=pymupdf.Rect(row['rectangle']),alpha=False)
  st(row['key'],'exactunchangedPDFpixels',actual.samples==expectedpix.samples and actual.width==expectedpix.width and actual.height==expectedpix.height)
  st(row['key'],'SHA matches',sha(p)==row['sha256'])
for row in json.loads((B/'parent-solution-image-manifest.json').read_text(encoding='utf-8'))['assets']:
 p=ROOT/row['publicFile'];st(row['key'],'solutionSHA',sha(p)==row['sha256']);svg=ET.parse(p).getroot()
 panelGroups=[node for node in svg.findall('.//{*}g')if node.get('transform','').startswith('translate(')]
 for panelIndex,panel in enumerate(row.get('panels',[])):
  n=np.array(panel['normalVector']);f=np.array(panel['frictionVector']);w=np.array(panel['weightVector']);normal=np.array(panel['normalUnit']);tangent=np.array(panel['downSlopeUnit'])
  ck('bridgeSVG','normalperpendiculartowall',normal@tangent,0)
  ck('bridgeSVG','normalparallel',np.cross(np.r_[normal,0],np.r_[n,0]),[0,0,0])
  ck('bridgeSVG','frictionparallelwall',np.cross(np.r_[tangent,0],np.r_[f,0]),[0,0,0])
  ck('bridgeSVG','verticalforcebalance',(n+f+w)[1],0)
  st('bridgeSVG','resultantinward',(n+f+w)[0]>0)
  ck('bridgeSVG','limitingfrictionratio',np.linalg.norm(f)/np.linalg.norm(n),panel['illustrativeFrictionCoefficient'])
  group=panelGroups[panelIndex]
  for color,expectedVector in [('#2563eb',n),('#15803d',f),('#7e22ce',w)]:
   line=next(node for node in group.findall('{*}line')if node.get('stroke')==color)
   start=np.array([float(line.get('x1')),float(line.get('y1'))]);end=np.array([float(line.get('x2')),float(line.get('y2'))])
   ck('bridgeSVG','actualSVGstart'+str((panelIndex,color)),start,panel['origin'],tol=1e-5)
   ck('bridgeSVG','actualSVGforcevector'+str((panelIndex,color)),end-start,expectedVector,tol=1e-5)
 if 'geometry'in row:
  geom=row['geometry'];ck('Q5.1SVG','threeforcesbalance',np.sum(geom['forceVectors'],axis=0),[0,0])
  for i,color in enumerate(['#2563eb','#15803d','#7e22ce']):
   line=next(node for node in svg.findall('.//{*}line')if node.get('stroke')==color)
   start=np.array([float(line.get('x1')),float(line.get('y1'))]);end=np.array([float(line.get('x2')),float(line.get('y2'))])
   ck('Q5.1SVG','actualSVGforcestart'+color,start,geom['forceStarts'][i]);ck('Q5.1SVG','actualSVGforcevector'+color,end-start,geom['forceVectors'][i])
assert progress['reviewedUnits']==41 and progress['expectedUnits']==159 and progress['status']=='partially-reviewed-not-ready'
assert sha(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')==progress['sourcePDFSHA256']
for row in progress['files']:assert sha(B/row['file'])==row['sha256']
print(json.dumps({'status':'passed-partial41units','units':len(ledger),'checks':len(records),'independentConeLPCases':len(coneCases),'dragTrajectoryCases':len(dragCases),'originalCrops':9,'solutionDiagrams':2,'wholeChapterComplete':False,'pendingNumberedRange':'5.1–5.118'},ensure_ascii=False))
