from pathlib import Path
import hashlib,json,math,re
import numpy as np

ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-late-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True);P=B/'parent-12-bai-tap-060-118.md';text=P.read_text(encoding='utf8');checks=[]
def near(name,a,b):
 assert math.isclose(float(a),float(b),rel_tol=1e-9,abs_tol=1e-9),(name,a,b)
 checks.append({'name':name,'actual':float(a),'expected':float(b)})
def yes(name,c):
 assert c,name
 checks.append({'name':name,'passed':True})
g=9.8
v=96.29953270914662;decel=.75*32.2;t=v/decel
near('86 displacement by integrating velocity',v*t-.5*decel*t*t,192)
near('86 speed converted to miles per hour',v*3600/5280,65.65877230169087)
yes('86 above stated limit in the exercise',v*3600/5280>45)
T=.57;fr=.57;floor=1.83
near('87 upper body net force',T-fr,0)
near('87 lower body net force',2.97-T-fr-floor,0)
near('87 floor supports both bodies',floor/.3,1.9+4.2)
f=.4*2*g;a=f/5;Pmax=10.976
near('88 upper body',Pmax-f,2*a)
near('88 lower body',f,5*a)
near('88 whole system',Pmax,7*a)
yes('88 above force bound slips',5*(Pmax+.01)/7>f)
mA=4;mB=12;mC=12.897435897435898;TL=47.2;TR=100.6;a=2
near('89 bodyA upward',TL-mA*g,mA*a)
near('89 bodyB right',TR-TL-.25*mB*g,mB*a)
near('89 bodyC down',mC*g-TR,mC*a)
forces=np.array([100*g*.5,50*g*math.sin(math.radians(53.1))])
a,T=np.linalg.solve([[100,1],[50,-1]],[forces[0],-forces[1]])
near('90 independent linear-system acceleration',a,.6543634489421705)
near('90 independent linear-system tension',T,424.56365510578297)
yes('90 left body drives system',forces[0]>forces[1] and a>0)
# Moving-pulley constraint, independent linear solve and finite displacements.
for m1 in [.1,1,10,100]:
 for m2 in [.1,1,10,100]:
  a1,a2,T=np.linalg.solve([[-m1,0,1],[0,-m2,-2],[1,-2,0]],[0,-m2*g,0])
  near(f'91 a1 for masses {m1}/{m2}',a1,2*m2*g/(4*m1+m2))
  near(f'91 a2 for masses {m1}/{m2}',a2,m2*g/(4*m1+m2))
  near(f'91 dynamic body1 {m1}/{m2}',T,m1*a1)
  near(f'91 dynamic body2 {m1}/{m2}',m2*g-2*T,m2*a2)
  near(f'91 actual rope-length change {m1}/{m2}',-.5*a1*3**2+2*.5*a2*3**2,0)
  yes(f'91 positive physical directions {m1}/{m2}',0<a2<g and 0<a1<2*g and T>0)
# Solve each separate body with the rope attached to the LOWER body A.
def bodies92(mC):return np.linalg.solve([[0,1,-5],[1,-1,-8],[-1,0,-mC]],[0,0,-mC*g])
T,f,a=bodies92(39)
near('92 threshold acceleration',a,7.35)
near('92 threshold friction',f,36.75)
near('92 threshold tension',T,95.55)
near('92 friction exactly at static limit',f,.75*5*g)
for mC in [1,10,38.9]:yes(f'92 below limit holds mC={mC}',bodies92(mC)[1]<.75*5*g)
yes('92 above39slips',bodies92(39.1)[1]>.75*5*g)
# 93: A common Cartesian axis verifies cancellation of internal friction.
T=7.75;f=4.75;a=1.5
near('93 upper block right',T-f,2*a)
near('93 lower block left on common rightward axis',T+f-20,-5*a)
near('93 actual whole-system external resultant',2*T-20,(2-5)*a)
near('93 kinetic coefficient',f/(2*g),.2423469387755102)

unit_hashes={}
for n in range(86,94):
 unit=next(c for c in re.split(r'(?=^### )',text,flags=re.M) if re.match(r'### 5\.'+str(n)+r'\b',c));unit_hashes[f'5.{n}']=hashlib.sha256(unit.strip().encode('utf8')).hexdigest()
 yes(f'{n} one closed solution',unit.count('<details>')==unit.count('</details>')==1 and '<details open' not in unit)
 for marker in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']:yes(f'{n} {marker}',marker in unit)
 if n==86:yes('86 actual speed question restored','Tốc độ của xe lúc bắt đầu đạp phanh bằng bao nhiêu?' in unit.split('<details>',1)[0])
 if n==91:yes('91 rope shortening has correct sign',r'-x_1 + 2y_2 = 0.' in unit)
 if n==92:
  yes('92 source rope attaches to A','gắn vào khối $A$' in unit.split('<details>',1)[0])
  yes('92 no contradictory11.5result',not re.search(r'11[.,{]5|11\{,\}5',unit))
 if n==93:yes('93 opposite-axis elimination distinguished','không phải phép cộng lực ngoài' in unit)
report={'status':'passed-numeric-and-structure-scope','scope':'Eight actual source units 5.86–5.93; source PDF186/187 visually inspected. Original-frame and browser checks separate, full chapter not accepted.','checksCount':len(checks),'reviewedUnitsSHA256':unit_hashes,'checks':checks}
(REVIEW_OUTPUT/'independent-086-093-review.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(checks),'independent force, rope-constraint, source-subpart and structure checks for eight units.')
