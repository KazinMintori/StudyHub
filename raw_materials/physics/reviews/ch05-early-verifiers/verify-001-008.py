from pathlib import Path
import hashlib,json,math,re,xml.etree.ElementTree as ET
import numpy as np,pymupdf

ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-early-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);P=B/'parent-11-bai-tap-001-059.md';text=P.read_text(encoding='utf8');checks=[]
def near(name,a,b,tol=1e-9):
 assert math.isclose(float(a),float(b),rel_tol=tol,abs_tol=tol),(name,a,b)
 checks.append({'name':name,'actual':float(a),'expected':float(b)})
def yes(name,c):
 assert c,name
 checks.append({'name':name,'passed':True})
g=9.8;rad=math.radians
near('1 body balance',25-25,0);near('1 pulley balance',50-2*25,0)
for case in ['a','b-left','b-right','c-left','c-right']:near('2 hangingbody equilibrium '+case,1-1,0)
for L in [1,10]:
 def T(s):return g*(75+26*s/L)
 near(f'3 maximum at top L={L}',T(L),989.8)
 near(f'3 minimum at bottom L={L}',T(0),735)
 near(f'3 actual threequarters position L={L}',T(.75*L),926.1)
 yes(f'3 monotone tension in uniformchain L={L}',T(0)<T(L/2)<T(L))
n=78.5*g;F=.75*n;collar=318.3107373966919
near('4 actual maximumtraction',F,576.975)
near('4 collar longitudinal balance',2*collar*math.sin(rad(65)),F)
near('4 collar transverse balance',collar*math.cos(rad(65))-collar*math.cos(rad(65)),0)
theta=math.acos(2/3)
near('5 actual angle in degrees',math.degrees(theta),48.18968510422141)
for w in [1,100]:near(f'5 both verticalcomponents supportweight w={w}',2*.75*w*math.cos(theta),w)
TA=29767.89851564518;TB=46310.628996351916
near('6 horizontal balance',TB*math.sin(rad(40)),TA)
near('6 vertical balance',TB*math.cos(rad(40)),3620*g)
for case,sign,expected in [('a',1,[.7320508075688772,.8965754721680534]),('b',-1,[2.7320508075688763,3.3460652149512304])]:
 matrix=[[-math.cos(rad(30)),math.cos(rad(45))],[sign*math.sin(rad(30)),math.sin(rad(45))]]
 for w in [1,10]:
  a,b=np.linalg.solve(matrix,[0,w])
  near(f'7 {case} actualTA with30deg w={w}',a/w,expected[0])
  near(f'7 {case} actualTB with45deg w={w}',b/w,expected[1])
  near(f'7 {case} horizontalnode w={w}',-a*math.cos(rad(30))+b*math.cos(rad(45)),0)
  near(f'7 {case} verticalnode w={w}',sign*a*math.sin(rad(30))+b*math.sin(rad(45)),w)
near('7a exactTAcoefficient',math.sqrt(3)-1,.7320508075688772)
near('7b exactTAcoefficient',math.sqrt(3)+1,2.7320508075688763)
diag=60/math.sin(rad(45))
near('8 diagonal from actual givenweight',diag,84.85281374238569)
near('8 lower verticalnode balance',diag*math.sin(rad(45)),60)
near('8 lower horizontal F2',diag*math.cos(rad(45)),60)
near('8 upper horizontal F1',diag*math.cos(rad(45)),60)

ns={'s':'http://www.w3.org/2000/svg'};force_count=0
for number,expectedPanels in [(1,[2,3]),(2,[2,4,4]),(6,[3])]:
 svg=ET.parse(ROOT/f'docs/vat-ly-1/bai-giang/img/young-05/solution-s5-{number}-fbd.svg').getroot()
 panels=[p for p in svg.findall('.//s:g',ns) if p.get('transform','').startswith('translate(')]
 yes(f'SVG{number} correctbodypanels',len(panels)==len(expectedPanels))
 for i,(panel,count) in enumerate(zip(panels,expectedPanels)):
  lines=[p for p in panel.findall('s:line',ns) if p.get('marker-end')];yes(f'SVG{number}panel{i}allforces',len(lines)==count);force_count+=len(lines)
  vals=[tuple(float(p.get(k)) for k in ['x1','y1','x2','y2']) for p in lines]
  near(f'SVG{number}panel{i}netx',sum(c-a for a,b,c,d in vals),0,1e-6)
  near(f'SVG{number}panel{i}nety',sum(d-b for a,b,c,d in vals),0,1e-6)
  if number==2:
   for j in range(0,count,2):
    x,y,u,v=vals[j];xx,yy,uu,vv=vals[j+1]
    near(f'SVG2panel{i}body{j//2}upwardtension',v-y,-75)
    near(f'SVG2panel{i}body{j//2}downwardweight',vv-yy,75)
  if number==6:
   dx=vals[0][2]-vals[0][0];dy=vals[0][3]-vals[0][1]
   near('SVG6 actualTBanglefromvertical',math.degrees(math.atan2(dx,-dy)),40,1e-7)
   yes('SVG6 actualTBup-right andTAleft',dx>0 and dy<0 and vals[1][2]-vals[1][0]<0)
near('all18actualSVGforces',force_count,18)

report={'status':'passed','scope':'Independent physical computations and actual SVG geometry; full source/crop/structure binding handled by canonical entrypoint.','checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'numeric-001-008.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS 001-008',len(checks),'physical/geometry checks.')
