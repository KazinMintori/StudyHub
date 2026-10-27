from pathlib import Path
import hashlib,json,math,re,sys,xml.etree.ElementTree as ET
from fractions import Fraction
import numpy as np
from scipy.integrate import solve_ivp

ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-late-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);P=B/'parent-12-bai-tap-060-118.md';text=P.read_text(encoding='utf8')
profiles={'104-109':range(104,110),'110-113':range(110,114),'114-118':range(114,119)}
requested=sys.argv[1:] or list(profiles)
g=9.8;rad=math.radians;ns={'s':'http://www.w3.org/2000/svg'}
for profile in requested:
 assert profile in profiles
 checks=[];plot_points=0;plot_line_samples=0
 def near(name,a,b,tol=1e-9):
  assert math.isclose(float(a),float(b),rel_tol=tol,abs_tol=tol),(name,a,b)
  checks.append({'name':name,'actual':float(a),'expected':float(b)})
 def yes(name,c):
  assert c,name
  checks.append({'name':name,'passed':True})
 if profile=='104-109':
  #104Actualtwo-stringgeometry and the physically admissible one-string branch.
  L=1.25;H=2;r=.75;m=4;omega=4.711687595755898
  near('104 both strings have actual length',math.hypot(r,H/2),L)
  near('104 vertical force balance',(80-31)*.8,m*g)
  near('104 radial force balance',(80+31)*.6,m*omega**2*r)
  near('104 actual rpm',omega*60/(2*math.pi),44.99330227015915)
  wc=3.1304951684997055;near('104 critical radial balance',49*.6,m*wc**2*r)
  low=3.;totalT=m*low**2*r/.6
  yes('104 a slower two-taut model requires negative lower tension',(totalT-49)/2<0)
  cost=g/(low**2*L);rr=L*math.sqrt(1-cost**2);TU=m*g/cost
  near('104 single-upper-string vertical balance',TU*cost,m*g)
  near('104 single-upper-string radial balance',TU*rr/L,m*low**2*rr)
  yes('104 actual lower wire is slack in new cone',math.hypot(rr,H-L*cost)<L)
  yes('104 cone shrinks below original radius',0<rr<r)
  #105IndependentODEintegration for positive masses/linear-dragcoefficients.
  for m in [.1,2,10]:
   for k in [.05,1,5]:
    vt=m*g/k;tau=m/k;times=tau*np.array([0,.2,1,2,5])
    ode=solve_ivp(lambda t,z:[g-k/m*z[0]],[0,float(times[-1])],[3*vt],t_eval=times,rtol=1e-11,atol=1e-12,max_step=tau/20)
    expected=vt*(1+2*np.exp(-times/tau))
    for j,(actual,e) in enumerate(zip(ode.y[0],expected)):near(f'105 actualODE m={m}/k={k}/sample={j}',actual,e,1e-8)
    yes(f'105 speed remains downward above terminal m={m}/k={k}',all(ode.y[0]>vt) and all(np.diff(ode.y[0])<0))
  #106Separateup/downNewtonkinematics, with actual speedratio and positive return.
  for angle in [10,30,60]:
   theta=rad(angle);mu=.6*math.tan(theta);au=g*(math.sin(theta)+mu*math.cos(theta));ad=g*(math.sin(theta)-mu*math.cos(theta))
   for v0 in [1,10]:
    d=v0*v0/(2*au);near(f'106 actual return ratio {angle}/{v0}',math.sqrt(2*ad*d)/v0,.5)
   yes(f'106 descendingbranchpositive {angle}',ad>0 and mu<math.tan(theta))
  #107Off-axis equilibrium must not be extended through division by sin(beta)=0.
  R=.1;omega=8*math.pi;beta=math.acos(g/(omega*omega*R));N=omega*omega*R
  near('107 actual angle degrees',math.degrees(beta),81.07461651232816)
  near('107 actual vertical balance per unitmass',N*math.cos(beta),g)
  near('107 actual radial balance per unitmass',N*math.sin(beta),omega**2*R*math.sin(beta))
  near('107 no vertical support at ring-centre height',N*math.cos(math.pi/2),0)
  omega=2*math.pi;yes('107 no off-axis solution at1rev/s',g/(omega*omega*R)>1)
  for d in [-.001,.001]:yes(f'107 stablebottom restoringforce at1rev/s {d}',d*math.sin(d)*(omega*omega*R*math.cos(d)-g)<0)
  #108Combinedsystemnormal is also the actual sphere-to-motorcycle force.
  R=13;vmin=math.sqrt(g*R);M=110;N=5390
  near('108 minimumtopreaction',M*vmin*vmin/R-M*g,0)
  yes('108 slower top speed loses contact',M*(.99*vmin)**2/R-M*g<0)
  near('108 total bottomradial resultant',N-M*g,M*(2*vmin)**2/R)
  riderload=5*70*g;near('108 motorcycle separately includes riderload',N-40*g-riderload,40*4*g)
  #109Keep actual questionorder(static,kinetic,Moon), and fit only sliding motion.
  m=1/.182;muk=.29;mus=.3714285714285714
  near('109 static measured threshold',mus*m*g,20)
  near('109 kinetic intercept magnitude',muk*g,2.842)
  for T in [25,30,50]:near(f'109 actual Newton acceleration T={T}',(T-muk*m*g)/m,.182*T-2.842)
  yes('109 kinetic line zero is not the static threshold',muk*m*g<20)
  for gp in [g/2,g/6]:
   near(f'109 smallergravity leaves slope gp={gp}',((30/m-muk*gp)-(25/m-muk*gp))/5,.182)
   yes(f'109 smallergravity raises negative intercept gp={gp}',-muk*g<-muk*gp<0)
 if profile=='110-113':
  #110Use every actual table value; independent normal-equationfit, not old five-pointdata.
  v=np.array([6.,8.,10.,12.,14.,16.]);N=np.array([8100.,7690.,7050.,6100.,5200.,4200.]);x=v*v;X=np.column_stack([np.ones(6),x]);intercept,slope=np.linalg.solve(X.T@X,X.T@N)
  mass=intercept/g;R=-mass/slope;vmax=math.sqrt(g*R)
  near('110 fitted mass',mass,897.3979552374743)
  near('110 fitted radius',R,49.51332805558528)
  near('110 actual contact speed',vmax,22.027950765895945)
  near('110 force at contact threshold',intercept+slope*vmax*vmax,0,1e-7)
  residual=N-(intercept+slope*x)
  near('110 residual orthogonal to intercept',sum(residual),0,1e-6)
  near('110 residual orthogonal to squaredspeed',sum(x*residual),0,1e-5)
  prompt110=next(c for c in re.split(r'(?=^### )',text,flags=re.M) if re.match(r'### 5\.110\b',c)).split('<details>',1)[0]
  actual=[]
  for line in prompt110.splitlines():
   m=re.fullmatch(r'\| ([\d,]+) \| (\d+) \|',line)
   if m:actual.append([float(m[1].replace(',','.')),float(m[2])])
  yes('110 actualsixpointprompt intact',actual==np.column_stack([v,N]).tolist())
  #111All7diameters/4fields, actualdiscreteselection, both area fits, static range.
  d=np.array([.25,.375,.5,.625,.75,.875,1.]);breaking=np.array([24.4,54.3,95.2,149.,212.,286.,372.]);safe=np.array([4.89,10.9,19.,29.7,42.3,57.4,74.3]);kgpm=np.array([.16,.36,.63,.98,1.41,1.92,2.50]);xx=d*d
  KB=np.linalg.lstsq(xx[:,None],breaking,rcond=None)[0][0];KS=np.linalg.lstsq(xx[:,None],safe,rcond=None)[0][0]
  near('111 actualoriginfitbreaking',KB,374.240565499943)
  near('111 actualoriginfitsafe',KS,74.8266605860221)
  near('111 predict queried9/16notalistrow',KS*(9/16)**2,23.675623076046055)
  free_slope,free_intercept=np.polyfit(xx,safe,1)
  near('111 free-intercept7pointfitprediction',free_intercept+free_slope*(9/16)**2,23.9409041262136)
  yes('111 both declared fitting choices give approximately24kN',23.5<KS*(9/16)**2<24 and 23.5<free_intercept+free_slope*(9/16)**2<24)
  yes('111 hypothesis is approximate within4.4percent',max(abs((safe-KS*xx)/safe))<.044 and max(abs((breaking-KB*xx)/breaking))<.044)
  theta=rad(40);a=16/4.2**2;n=2170*g*math.cos(theta);G=2170*g*math.sin(theta);T=G+.35*n+2170*a
  near('111 actual moving tension',T,21339.520670426777)
  chosen=int(np.where(safe*1000>=T)[0][0]);near('111 actual smallestlisteddiameter',d[chosen],.625)
  yes('111 preceding actual listeddiameter fails',safe[chosen-1]*1000<T)
  lower,upper=G-.62*n,G+.62*n
  for tv in [lower,G,T,upper]:yes(f'111 admissiblestatic T={tv}',abs(G-tv)<=.62*n+1e-7)
  yes('111 movingtension lies strictly inside static interval',lower<T<upper)
  yes('111 feasible static tension can be smallerORlarger',abs(G-(T+1000))<.62*n and abs(G-(T-1000))<.62*n)
  mc=kgpm[chosen]*9;extra=mc*(a+g*math.sin(theta));upperT=T+extra
  near('111 cable mass',mc,8.82)
  near('111 actual cablegravity ANDinertia correction',extra,63.55998983086571)
  near('111 whole blockpluscable Newton balance',upperT-(2170+mc)*g*math.sin(theta)-.35*n,(2170+mc)*a)
  yes('111 ignoringcable underestimates byabout0.30percent',.0029<extra/upperT<.0031)
  prompt111=next(c for c in re.split(r'(?=^### )',text,flags=re.M) if re.match(r'### 5\.111\b',c)).split('<details>',1)[0];table3=[];table2=[]
  for line in prompt111.splitlines():
   if not line.startswith('|'):continue
   cells=[s.strip() for s in line.strip('|').split('|')]
   try:
    dia=float(Fraction(cells[0].strip('$')))
    nums=[float(s.replace(',','.')) for s in cells[1:]]
   except (ValueError,ZeroDivisionError):continue
   if len(cells)==3:table3.append([dia,*nums])
   elif len(cells)==2:table2.append([dia,*nums])
  yes('111 all7breakingandsafevalues in prompt',table3==np.column_stack([d,breaking,safe]).tolist())
  yes('111 all7masspermeter values in prompt',table2==np.column_stack([d,kgpm]).tolist())
  #112Independentforce/constraintlinear solve for actual high-left/down-rightwedge.
  for M in [1,10,100]:
   for m in [.5,2]:
    for angle in [10,30,60]:
     al=rad(angle);s,c=math.sin(al),math.cos(al);A,ax,ay,normal=np.linalg.solve([[M,0,0,-s],[0,m,0,-s],[0,0,m,c],[-math.tan(al),-math.tan(al),1,0]],[0,0,m*g,0]);D=M+m*s*s
     near(f'112 wedgeaccel {M}/{m}/{angle}',A,m*g*s*c/D)
     near(f'112 blockax {M}/{m}/{angle}',ax,M*g*s*c/D)
     near(f'112 blockay {M}/{m}/{angle}',ay,(M+m)*g*s*s/D)
     near(f'112 horizontalmomentum {M}/{m}/{angle}',-M*A+m*ax,0)
     near(f'112 straightpath slope {M}/{m}/{angle}',ay/ax,(M+m)/M*math.tan(al))
     for t in [.2,1]:near(f'112 actualparametricstraightpath {M}/{m}/{angle}/{t}',.5*ay*t*t-(ay/ax)*.5*ax*t*t,0)
  #113The source(b)rightwardforce creates the common horizontal acceleration.
  for angle in [10,30,60]:
   al=rad(angle);m=2;M=5;n=m*g/math.cos(al);a=g*math.tan(al);F=(M+m)*a
   near(f'113 blockvertical {angle}',n*math.cos(al),m*g)
   near(f'113 blockhorizontal {angle}',n*math.sin(al),m*a)
   near(f'113 wedgehorizontal {angle}',F-n*math.sin(al),M*a)
  #Plotcoordinates in writtenSVG, calibrated by actual axisgeometry.
  for number,expected_panels in [(110,[(x,N,float(intercept),float(slope),[0,300],[3000,9000])]),(111,[(xx,breaking,0.,float(KB),[0,1.05],[0,400]),(xx,safe,0.,float(KS),[0,1.05],[0,80])])]:
   svg=ET.parse(ROOT/f'docs/vat-ly-1/bai-giang/img/young-05/solution-s5-{number}-graph.svg').getroot();panels=[q for q in svg.findall('.//s:g',ns) if q.get('class')=='plot-panel'];yes(f'SVG{number}allrequestedpanels',len(panels)==len(expected_panels))
   for j,(panel,expect) in enumerate(zip(panels,expected_panels)):
    ex,ey,b0,b1,xrange,yrange=expect;xa=next(q for q in panel.findall('s:line',ns) if q.get('class')=='x-axis');ya=next(q for q in panel.findall('s:line',ns) if q.get('class')=='y-axis');px0=float(xa.get('x1'));px1=float(xa.get('x2'));py0=float(ya.get('y1'));py1=float(ya.get('y2'))
    points=[q for q in panel.findall('s:circle',ns) if q.get('class')=='data-point'];yes(f'SVG{number}panel{j}allactualdatapoints',len(points)==len(ex));plot_points+=len(points)
    for k,(point,xv,yv) in enumerate(zip(points,ex,ey)):
     actualX=xrange[0]+(float(point.get('cx'))-px0)/(px1-px0)*(xrange[1]-xrange[0]);actualY=yrange[0]+(py1-float(point.get('cy')))/(py1-py0)*(yrange[1]-yrange[0])
     near(f'SVG{number}panel{j}actualpoint{k}x',actualX,xv,1e-6);near(f'SVG{number}panel{j}actualpoint{k}y',actualY,yv,1e-4)
    line=next(q for q in panel.findall('s:polyline',ns) if q.get('class')=='fit-line')
    for k,pair in enumerate(line.get('points').split()):
     sx,sy=map(float,pair.split(','));xxv=xrange[0]+(sx-px0)/(px1-px0)*(xrange[1]-xrange[0]);yyv=yrange[0]+(py1-sy)/(py1-py0)*(yrange[1]-yrange[0]);near(f'SVG{number}panel{j}actualfitpoint{k}',yyv,b0+b1*xxv,1e-3);plot_line_samples+=1
 if profile=='114-118':
  #114Independent6x6solve against all symbolic answers and both stringconstraints.
  for m1 in [.2,1,10]:
   for m2 in [.2,1,10]:
    for m3 in [.2,1,10]:
     mat=[[m1,0,0,0,1,0],[0,m2,0,0,1,0],[0,0,m3,0,0,1],[1,1,0,-2,0,0],[0,0,1,1,0,0],[0,0,0,0,-2,1]]
     a1,a2,a3,aB,TA,TC=np.linalg.solve(mat,[m1*g,m2*g,m3*g,0,0,0]);S=1/m1+1/m2+4/m3
     for name,actual,expected in [('a1',a1,g-4*g/(m1*S)),('a2',a2,g-4*g/(m2*S)),('a3',a3,g-8*g/(m3*S)),('aB',aB,-a3),('TA',TA,4*g/S),('TC',TC,8*g/S)]:near(f'114 {name} {m1}/{m2}/{m3}',actual,expected)
     yes(f'114 bothtensionspositive {m1}/{m2}/{m3}',TA>0 and TC>0)
     near(f'114 first actualropeconstraint {m1}/{m2}/{m3}',a1+a2-2*aB,0)
     near(f'114 second actualropeconstraint {m1}/{m2}/{m3}',aB+a3,0)
  for m in [.5,3,10]:
   S=4/m;TA=4*g/S;TC=8*g/S
   near(f'114 specialcase lowerforce m={m}',TA,m*g);near(f'114 specialcase upperforce m={m}',TC,2*m*g);near(f'114 specialcase acceleration m={m}',g-TC/(2*m),0)
  #115BeforecutstaticA differs from zero-radialacceleration turningpointB.
  for angle in [10,30,60]:
   beta=rad(angle);m=2;TA=m*g/math.cos(beta);TB=m*g*math.cos(beta)
   near(f'115 Abeforecutvertical {angle}',TA*math.cos(beta),m*g)
   near(f'115 Bturnpointradial {angle}',TB-m*g*math.cos(beta),0)
   near(f'115 actualratio {angle}',TB/TA,math.cos(beta)**2)
   yes(f'115 nonzero tangential acceleration atB {angle}',g*math.sin(beta)>0)
  #116–118Use exactstaticthreshold and every actual multiple-choicecondition.
  theta=math.atan(1.2);near('116 actualcriticalangle',math.degrees(theta),50.19442890773481)
  near('116 staticlimit',math.sin(theta),1.2*math.cos(theta))
  for al in [theta,theta+.01,rad(70),rad(89)]:yes(f'117 kineticacceleration positive {al}',g*(math.sin(al)-.90*math.cos(al))>0)
  for m in [1,70]:near(f'118 true maximumstaticacceleration m={m}',(1.2*m*g)/m,1.2*g)
  yes('116 nearestlistedangle is choiceb',min([42,50,64],key=lambda a:abs(a-math.degrees(theta)))==50)

 unit_hashes={}
 for number in profiles[profile]:
  unit=next(x for x in re.split(r'(?=^### )',text,flags=re.M) if re.match(r'### 5\.'+str(number)+r'\b',x));unit_hashes[f'5.{number}']=hashlib.sha256(unit.strip().encode('utf8')).hexdigest();prompt=unit.split('<details>',1)[0]
  yes(f'{number}oneclosedsolution',unit.count('<details>')==unit.count('</details>')==1 and '<details open' not in unit)
  for tag in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']:yes(f'{number}{tag}',tag in unit)
  if number==104:yes('104 allfouractualquestions',all(f'({x})' in prompt for x in 'abcd'))
  if number==105:yes('105 actualsinglequestion',not re.search(r'\([ab]\)',prompt))
  if number==107:yes('107 actualheightand1rev/squestions','cùng độ cao với tâm' in prompt and '(c)' in prompt and '1{,}00' in prompt)
  if number==109:yes('109 actualstatic/kinetic/Moonquestionorder',prompt.index('ma sát nghỉ')<prompt.index('ma sát trượt')<prompt.index('Mặt Trăng'))
  if number in [110,112]:yes(f'{number}actualthreequestions',all(f'({x})' in prompt for x in 'abc'))
  if number==111:yes('111 allfouractualquestions',all(f'({x})' in prompt for x in 'abcd'))
  if number==114:yes('114 allsevenactualquestions and fixedD',all(f'({x})' in prompt for x in 'abcdefg') and 'ròng rọc nhẹ, không ma sát $D$' in prompt)
  if number==115:yes('115 commonpassagepreservedafterclosedsolution','## Đọc hiểu khoa học:' in unit and unit.index('</details>')<unit.index('## Đọc hiểu khoa học:'))
  if number in [116,117,118]:yes(f'{number}allfourchoices',all(f'({x})' in prompt for x in 'abcd'))
 report={'status':'passed-numeric-and-structure-scope','scope':'ActualsourcePDF188–190andallnamedquestionparts compared by parent;independentNewton/ODE/fit/constraint calculations. Source-pixel and browser gates separate. Fullchapter not accepted.','checksCount':len(checks),'reviewedUnitsSHA256':unit_hashes,'actualSVGDataPointsChecked':plot_points,'actualSVGFitSamplesChecked':plot_line_samples,'checks':checks}
 (REVIEW_OUTPUT/f'independent-{profile}-review.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'));print(profile,'PASS',len(checks),'independentchecks;actualplotpoints',plot_points,'fitsamples',plot_line_samples)
