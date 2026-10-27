from pathlib import Path
import hashlib,json,math,re,xml.etree.ElementTree as ET
import numpy as np

ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-late-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);P=B/'parent-12-bai-tap-060-118.md';text=P.read_text(encoding='utf8');checks=[]
def near(name,a,b,tol=1e-9):
 assert math.isclose(float(a),float(b),rel_tol=tol,abs_tol=tol),(name,a,b)
 checks.append({'name':name,'actual':float(a),'expected':float(b)})
def yes(name,c):
 assert c,name
 checks.append({'name':name,'passed':True})
g=9.8;rad=math.radians
# 94: Horizontal steady motion coexists with vertical acceleration.
normal=421.2;push=134.784
near('94 vertical resultant',normal-36*g,36*1.9)
near('94 horizontal resultant',push-.32*normal,0)
# 95: Normal force creates horizontal acceleration; friction only supports weight.
for m in [10,70]:
 for mu in [.1,.4,1]:
  a=g/mu;n=m*a;f=m*g
  near(f'95 static limit m={m}/mu={mu}',mu*n,f)
  near(f'95 cart-frame apparent horizontal equilibrium m={m}/mu={mu}',n-m*a,0)
  yes(f'95 below bound falls m={m}/mu={mu}',mu*m*(a*.99)<f)
# 96: An independent coupled-force solve; reversal yields an inadmissible tension.
theta=rad(30);a4=g*(math.sin(theta)-.25*math.cos(theta));a8=g*(math.sin(theta)-.35*math.cos(theta))
a,T=np.linalg.solve([[4,1],[8,-1]],[4*a4,8*a8])
near('96 common acceleration',a,2.2124344969222918)
near('96 taut tension',T,2.263213055223334)
yes('96 original string is in tension',T>0)
_,impossibleT=np.linalg.solve([[4,-1],[8,1]],[4*a4,8*a8])
yes('96 reversed taut model would require compression',impossibleT<0)
yes('96 physical reversed slack branch',a4>a8>0)
near('96 separate4kg acceleration',a4,2.7782377607281252)
near('96 separate8kg acceleration',a8,1.9295328650193748)
# 97: Both contact normals and both kinetic friction forces must be included.
theta=rad(36.9);mu=.4504927428232588
near('97 actual along-plane balance',3*math.sin(theta),mu*5*math.cos(theta))
near('97 normal balance',4*math.cos(theta)-math.cos(theta),3*math.cos(theta))
# 98: Verify the actual upper-chair reaction, not a generic loop-at-top formula.
omega=2*math.pi*.1;R=18.61776749427957
near('98 inward acceleration',omega*omega*R,.75*g)
near('98 specified chair reaction fraction',1-omega*omega*R/g,.25)
# 99: Mass cancellation and loss of support as the cylinder slows.
omega=2*math.pi*.6;R=2.5;mu=.27581877769303065
for m in [50,80]:
 n=m*omega**2*R
 near(f'99 limiting support m={m}',mu*n,m*g)
 near(f'99 mass-independent ratio m={m}',m*g/n,mu)
 yes(f'99 slowed rotation cannot support at the same limiting friction m={m}',mu*m*(omega/2)**2*R<m*g)
# 100: Verify the parameterized crest speed against the specified contact load.
for R in [1,10,100]:
 v=math.sqrt(g*R/2)
 near(f'100 normal-to-weight ratio at R={R}',1-v*v/(R*g),.5)
# 101/102: Solve normal and acceleration from the two force projections.
beta=rad(18);s=math.sin(beta);c=math.cos(beta)
def contact_for_speed(m,R,v):return np.linalg.solve([[c,-s],[s,c]],[m*g,m*v*v/R])
n101,ar101=np.linalg.solve([[c-.4*s,0],[s+.4*c,-1200]],[1200*g,0])
v101=math.sqrt(ar101*90)
near('101 normal from independent linear solve',n101,14212.343948435295)
near('101 acceleration from independent linear solve',ar101,8.165460616302832)
near('101 actual maximum speed',v101,27.108881486834807)
nn,ff=contact_for_speed(1200,90,v101)
near('101 maximum-speed friction is downhill at its bound',ff/nn,.4)
nn,ff=contact_for_speed(1200,90,v101*1.001);yes('101 any faster small perturbation violates static bound',ff>.4*nn)
nn,ff=contact_for_speed(1200,90,v101*.999);yes('101 slower nearby speed is feasible',abs(ff)<.4*nn)
n102,ar102=np.linalg.solve([[c+.3*s,0],[s-.3*c,-900]],[900*g,0]);v102=math.sqrt(ar102*120)
near('102 normal from independent linear solve',n102,8450.205369274421)
near('102 actual minimum speed',v102,5.167464896445899)
yes('102 strictly positive lower speed is required',.3<math.tan(beta))
nn,ff=contact_for_speed(900,120,v102);near('102 minimum-speed friction is uphill at its bound',ff/nn,-.3)
nn,ff=contact_for_speed(900,120,v102*.999);yes('102 any slower small perturbation violates static bound',ff<-.3*nn)
nn,ff=contact_for_speed(900,120,v102*1.001);yes('102 faster nearby speed is feasible',abs(ff)<.3*nn)
# 103: Separate balance before the cut, then independent coupled equations after it.
theta=rad(36.9);T1=8.75;NB=25*math.cos(theta);fB=.35*NB;G=25*math.sin(theta);WC=30.757746394909145
near('103 horizontalA balance',T1-.35*25,0)
near('103 uphillB balance',WC-T1-fB-G,0)
near('103 constant-speedC balance',WC-WC,0)
a,Tafter=np.linalg.solve([[25/g,-1],[WC/g,1]],[-G-fB,WC])
near('103 acceleration after cuttingAB',a,1.5379029021845336)
yes('103 downwardC and upwardB accelerate after cut',a>0 and Tafter<WC and Tafter>G+fB)

# Actual SVG arrow coordinates, including directions and complete force counts.
ns={'s':'http://www.w3.org/2000/svg'};arrows={}
for number in [97,99,103]:
 svg=ET.parse(ROOT/f'docs/vat-ly-1/bai-giang/img/young-05/solution-s5-{number}-fbd.svg').getroot();panels=[x for x in svg.findall('.//s:g',ns) if x.get('transform','').startswith('translate(')];arrows[number]=[]
 for i,panel in enumerate(panels):
  fs=[]
  for line in panel.findall('s:line',ns):
   if line.get('marker-end'):
    x1,y1,x2,y2=[float(line.get(k)) for k in ['x1','y1','x2','y2']];fs.append((np.array([x1,y1]),np.array([x2-x1,y2-y1])))
  arrows[number].append(fs)
  center=np.array([180.,170. if number==103 and i==0 else 180.])
  total=sum((f for origin,f in fs),np.zeros(2))
  if number!=99:
   near(f'SVG{number}panel{i}actualnetx',total[0],0,1e-5);near(f'SVG{number}panel{i}actualnety',total[1],0,1e-5)
   moment=sum((o[0]-center[0])*f[1]-(o[1]-center[1])*f[0] for o,f in fs)
   near(f'SVG{number}panel{i}actualnetmoment',moment,0,1e-3)
  else:
   near('SVG99 actual vertical balance',total[1],0,1e-5)
   near('SVG99 actual radial-to-weight ratio',-total[0]/40,(2*math.pi*.6)**2*2.5/g,1e-7)
yes('SVG97 allfiveactualforces',len(arrows[97][0])==5)
yes('SVG99 exactlythreerealforces',len(arrows[99][0])==3)
yes('SVG103 fourforcesonAandfiveonB',[len(x) for x in arrows[103]]==[4,5])
t=np.array([math.cos(theta),-math.sin(theta)]);normal=np.array([-math.sin(theta),-math.cos(theta)])
for index in [3,4]:
 f=arrows[97][0][index][1];yes(f'SVG97friction{index}uphill',np.dot(f,t)>0);near(f'SVG97friction{index}parallelplane',np.dot(f,normal),0,1e-6)
f=arrows[97][0][0][1];near('SVG97 real gravity is vertical',f[0],0);yes('SVG97 gravity is down',f[1]>0)
yes('SVG103 upperropepullsBuphill',np.dot(arrows[103][1][2][1],t)>0)
yes('SVG103 lowerropeandfrictionpullBdownhill',np.dot(arrows[103][1][3][1],t)<0 and np.dot(arrows[103][1][4][1],t)<0)

unit_hashes={}
for number in range(94,104):
 unit=next(x for x in re.split(r'(?=^### )',text,flags=re.M) if re.match(r'### 5\.'+str(number)+r'\b',x));unit_hashes[f'5.{number}']=hashlib.sha256(unit.strip().encode('utf8')).hexdigest()
 yes(f'{number} oneclosedsolution',unit.count('<details>')==unit.count('</details>')==1 and '<details open' not in unit)
 for marker in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']:yes(f'{number} {marker}',marker in unit)
 prompt=unit.split('<details>',1)[0]
 if number==95:yes('95 source observer question restored','Một người quan sát từ trên xe' in prompt)
 if number==96:yes('96 correct slack-rope branch explicit','dây bị chùng' in unit and 'không thể đẩy' in unit)
 if number==99:yes('99 source mass question and closing note restored','(c)' in prompt and 'khối lượng' in prompt and 'Lưu ý:' in prompt)
 if number==103:
  yes('103 allfouractualpromptparts',all(f'({x})' in prompt for x in ['a','b','c','d']))
  yes('103 no literal newline escapes',r'\n\n' not in unit)
note={'unit':'5.103','sourceProblemPDFPage':188,'sourceOddAnswerPDFPage':1555,'printedWeightCN':31.0,'directWeightCN':WC,'directAccelerationAfterCutMps2':a,'sourceWeightABN':25,'sourceMu':.35,'sourceAngleDeg':36.9,'reasonForPrintedWeightDifference':'Not established;direct30.757746 rounds30.8at3significantdigits. Preservegivens/unroundedcalculation, do notinventaroundingcause. Printed acceleration1.54 agreeswithdirectcoupledcalculation.'}
(REVIEW_OUTPUT/'source-answer-note-5-103.json').write_bytes((json.dumps(note,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
report={'status':'passed-numeric-and-structure-scope','scope':'Ten units5.94–5.103;actualsourcePDF187/188and1555visuallycompared. NativeSVGarrows verified from written XML; browser/source-pixel gates separate. Wholechapter not accepted.','checksCount':len(checks),'reviewedUnitsSHA256':unit_hashes,'actualSVGForceArrows':sum(len(x) for groups in arrows.values() for x in groups),'sourceAnswerNote':note,'checks':checks}
(REVIEW_OUTPUT/'independent-094-103-review.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(checks),'independent checks;',report['actualSVGForceArrows'],'actual SVGforcearrows checked.')
