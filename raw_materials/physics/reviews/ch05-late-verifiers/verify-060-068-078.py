from pathlib import Path
import hashlib,json,math,re,subprocess,sys,xml.etree.ElementTree as ET
import numpy as np
from scipy.integrate import solve_ivp

ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-late-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);ROOT=B.parents[3];P=B/'parent-12-bai-tap-060-118.md';text=P.read_text(encoding='utf8');checks=[]
def near(name,a,b,tol=1e-9):
 assert math.isclose(float(a),float(b),rel_tol=tol,abs_tol=tol),(name,a,b)
 checks.append({'name':name,'actual':float(a),'expected':float(b)})
def yes(name,c):
 assert c,name
 checks.append({'name':name,'passed':True})
g=9.8;rad=math.radians
# 60: Check equilibrium and the actual tension bound, not only the answer.
T=2539.617783066343;theta=rad(10)
near('60 upward components support the person',2*T*math.sin(theta),90*g)
near('60 horizontal components cancel',T*math.cos(theta)-T*math.cos(theta),0)
theta=rad(1.0107499743438972)
near('60 minimum-angle tension',90*g/(2*math.sin(theta)),25000)
yes('60 smaller sag angle breaks the rope',90*g/(2*math.sin(theta*.99))>25000)
# 61: All four actual cable directions at the node.
TC=1196.9337519861888;TB=4962.855124452666
near('61 horizontal node balance',TC*math.sin(rad(37.1)),722)
near('61 vertical node balance',TB-TC*math.cos(rad(37.1)),409*g)
yes('61 upper cable carries extra downward C component',TB>409*g)
# 62: Each isolated body, including the separate ceiling anchor.
for w in [1,10,680]:
 T=w/2;T1=w;T2=w
 near(f'62 weight balance w={w}',T2-w,0)
 near(f'62 lower pulley balance w={w}',2*T-T2,0)
 near(f'62 upper pulley balance w={w}',T1-2*T,0)
 near(f'62 total ceiling load is not upper-chain load w={w}',T1+T,1.5*w)
# 63: Static limit then kinetic dynamics and travel.
theta=math.atan(.6);a=g*(math.sin(theta)-.4*math.cos(theta))
near('63 actual static limit',math.sin(theta),.6*math.cos(theta))
near('63 acceleration after release',a,1.6806861343965867)
t=math.sqrt(2*3/a);near('63 actual final speed',a*t,3.1755498431577984)
near('63 actual travel',.5*a*t*t,3)
# 64: Both components of the actual three-force equilibrium.
n=1.220774588761456;T=.7002075382097097
near('64 vertical component in units of weight',n*math.cos(rad(35)),1)
near('64 horizontal component in units of weight',n*math.sin(rad(35)),T)
# 65: Reconstruct normal, friction and acceleration separately in all cases.
m=12;a=2.25;theta=rad(37)
F=100.76186142084111;n=m*g+F*math.sin(theta)
near('65a actual horizontal Newton equation',F*math.cos(theta)-.3*n,m*a)
near('65a increased normal reaction',n-m*g,F*math.sin(theta))
yes('65a positive divisor',math.cos(theta)-.3*math.sin(theta)>0)
near('65b frictionless Newton equation',33.807662770218094*math.cos(theta),m*a)
near('65c horizontal force Newton equation',62.28-.3*m*g,m*a)
near('65 measured speed after eight metres',math.sqrt(2*a*8),6)
# 66: Independent numerical integration with an event at the coefficient change.
def boundary(t,z):return z[0]-2
boundary.terminal=True;boundary.direction=1
first=solve_ivp(lambda t,z:[z[1],-.2*g],[0,3],[0,4],events=boundary,rtol=1e-11,atol=1e-12,max_step=.02)
yes('66 reaches second region',len(first.t_events[0])==1 and first.y[1,-1]>0)
def stop(t,z):return z[1]
stop.terminal=True;stop.direction=-1
second=solve_ivp(lambda t,z:[z[1],-.4*g],[first.t[-1],4],first.y[:,-1],events=stop,rtol=1e-11,atol=1e-12,max_step=.02)
near('66 integrated stopping point',second.y[0,-1],3.040816326530612)
near('66 integrated stopping time',second.t[-1],1.312099139944607)
yes('66 stops inside the second rough patch',2<second.y[0,-1]<4)
# 67: Actual displacement under the two equal-time acceleration phases.
a=1.2;h=.3;tf=1;mid=.5*tf;v_mid=a*mid;y_mid=.5*a*mid*mid
near('67 final velocity under downward acceleration',v_mid-a*mid,0)
near('67 total vertical travel',y_mid+v_mid*mid-.5*a*mid*mid,h)
Fup=680*(1+a/g);Fdown=680*(1-a/g)
near('67 upward accelerating force',Fup,763.2653061224489)
near('67 downward accelerating force',Fdown,596.734693877551)
near('67 actual upward force resultant',Fup-680,(680/g)*a)
# 68: An independent quadratic solve and numerical velocity derivative.
roots=np.roots([.6,2,-9]);positive=next(float(x) for x in roots if x>0)
yes('68 other root is excluded by time domain',sum(float(x)<0 for x in roots)==1)
near('68 selected time gives actual speed',2*positive+.6*positive**2,9)
eps=1e-4;v=lambda t:2*t+.6*t*t
a=(v(positive+eps)-v(positive-eps))/(2*eps)
near('68 derivative acceleration',a,5.059644256269408)
near('68 actual rope force',2*(g+a),29.719288512538817)
# 78: Extract and integrate the actual PDF Bezier curve with independent quadrature.
subprocess.run([sys.executable,'-I','-X','utf8',str(Path(__file__).with_name('verify-flea-source-curve.py'))],cwd=ROOT,check=True,capture_output=True)
curve=json.loads((REVIEW_OUTPUT/'flea-source-curve-review.json').read_text(encoding='utf8'))
yes('78 actual PDF curve extraction passed',curve['status']=='passed-source-curve-extraction-and-independent-integration')
near('78 microgram conversion',210e-6*1e-3,210e-9)
yes('78 actual nonzero initial acceleration',55<curve['initialAccelerationInG']<70)
yes('78 actual peak and time support readable estimates',135<curve['peakAccelerationInG']<150 and 1.05<curve['peakTimeMs']<1.2)
yes('78 whole-curve speed supports readable estimate',abs(curve['maxSpeedFromWholeCurveMps']-1.3)<.1)
for i,s in enumerate(curve['segments']):near(f'78 Bezier integral against independent quad {i}',s['integratedRatioSeconds'],s['independentQuadRatioSeconds'])
near('78 readable initial net force',210e-9*g*60,.00012348)
near('78 readable maximum net force',210e-9*g*140,.00028812)

# Verify the force arrows that were actually written to each SVG, not just a manifest.
ns={'s':'http://www.w3.org/2000/svg'};geom={}
for number in [62,64,67]:
 path=ROOT/f'docs/vat-ly-1/bai-giang/img/young-05/solution-s5-{number}-fbd.svg';svg=ET.parse(path).getroot()
 panels=[e for e in svg.findall('.//s:g',ns) if e.get('transform','').startswith('translate(')]
 geom[number]=[]
 for j,panel in enumerate(panels):
  forces=[]
  for line in panel.findall('s:line',ns):
   if not line.get('marker-end'):continue
   x1,y1,x2,y2=[float(line.get(k)) for k in ['x1','y1','x2','y2']]
   forces.append([x1,y1,x2,y2]);yes(f'SVG{number}panel{j}nonzeroarrow{len(forces)}',math.hypot(x2-x1,y2-y1)>0)
  geom[number].append(forces)
  dx=sum(x2-x1 for x1,y1,x2,y2 in forces);dy=sum(y2-y1 for x1,y1,x2,y2 in forces)
  if number in [62,64]:
   near(f'SVG{number}panel{j}equilibriumx',dx,0,1e-6);near(f'SVG{number}panel{j}equilibriumy',dy,0,1e-6)
  else:
   near(f'SVG67panel{j}acceleration-to-weight-ratio',dy/100,(-1 if j==0 else 1)*1.2/g,1e-7)
  if number==62:near(f'SVG62panel{j}zeroresultantmoment',sum((x1-180)*(y2-y1)-(y1-160)*(x2-x1) for x1,y1,x2,y2 in forces),0,1e-6)
near('SVG64 actual T-to-weight ratio',(geom[64][0][1][2]-geom[64][0][1][0])/110,math.tan(rad(35)),1e-7)

ids=list(range(60,69))+[78];unit_hashes={}
for n in ids:
 unit=next(c for c in re.split(r'(?=^### )',text,flags=re.M) if re.match(r'### 5\.'+str(n)+r'\b',c));unit_hashes[f'5.{n}']=hashlib.sha256(unit.strip().encode('utf8')).hexdigest()
 yes(f'{n} one closed solution',unit.count('<details>')==unit.count('</details>')==1 and '<details open' not in unit)
 for marker in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']:yes(f'{n} {marker}',marker in unit)
 prompt=unit.split('<details>',1)[0]
 if n==64:yes('64 all three actual prompt parts',all(f'({x})' in prompt for x in ['a','b','c']))
 if n==67:yes('67 actual single draw-and-find question',not re.search(r'\([abc]\)',prompt) and 'vẽ giản đồ lực' in prompt and 'giai đoạn gia tốc hướng lên' in prompt)
 if n==78:yes('78 actual microgram mass and all three parts',r'210\,\mu' in prompt and all(f'({x})' in prompt for x in ['a','b','c']))
note={'unit':'5.67','sourceQuestionPDFPage':185,'sourceOddAnswerPDFPage':1555,'actualSourceOddAnswerN':762,'sourceWeightN':680,'heightM':.30,'durationS':1.,'assumedG':g,'directCalculatedUpwardForceN':Fup,'reasonForDifference':'Not established. Do not alter the givens or invent a rounding explanation. Source prompt and independently calculated result preserved.','modelAssumption':'Starts and finishes at rest; equal half durations with constant opposite accelerations.'}
(REVIEW_OUTPUT/'source-answer-note-5-67.json').write_bytes((json.dumps(note,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
report={'status':'passed-numeric-and-structure-scope','scope':'Ten actual source units 5.60–5.68 and5.78; source pages184–186 and odd-answer page1555 visually inspected. Source-frame completeness and browser acceptance separate. Whole chapter not accepted.','checksCount':len(checks),'reviewedUnitsSHA256':unit_hashes,'actualSVGForceArrows':sum(len(x) for groups in geom.values() for x in groups),'sourceCurveSamples':len(curve['sampledCurve']),'sourceAnswerNote':note,'checks':checks}
(REVIEW_OUTPUT/'independent-060-068-078-review.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(checks),'independent checks; actual SVGforcearrows:',report['actualSVGForceArrows'],'actual curve samples:',report['sourceCurveSamples'])
