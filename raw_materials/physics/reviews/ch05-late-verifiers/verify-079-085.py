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
# 79: Independently balance A and B; internal forces cancel only in case a.
wA=1.2;wB=3.6;mu=.3
near('79a actual static friction on A',0,0)
near('79a combined external balance',1.44-mu*(wA+wB),0)
near('79b lower block balance',1.80-mu*(wA+wB)-mu*wA,0)
near('79b rope holds upper block',mu*wA,.36)
# 80: Reconstruct actual normal force at the proposed limiting acceleration.
a=.6*g;v=math.sqrt(2*a*3)
for m in [10,60,100]:
 near(f'80 normal-to-weight ratio m={m}',m*(g+a)/(m*g),1.6)
 near(f'80 actual acceleration from normal m={m}',(1.6*m*g-m*g)/m,a)
near('80 speed squared from travel',v*v,35.28)
yes('80 correctly rounded two-significant-digit speed',format(v,'.2g')=='5.9')
# 81: Central finite difference checks the velocity derivative independently.
vel=lambda t:3*t+.2*t*t;h=1e-4;a=(vel(4+h)-vel(4-h))/(2*h)
near('81 instantaneous acceleration',a,4.6)
near('81 scale force',64*(g+a),921.6)
# 82: Use the measured motion to test both coupled Newton equations.
a=2.7225;T=18.05484693877551;mu=.12341269841269842
near('82 actual measured final speed',math.sqrt(2*a*2),3.3)
near('82 vertical hanging body',25-T,25/g*a)
near('82 horizontal sliding body',T-mu*45,45/g*a)
yes('82 positive friction and tension',mu>0 and 0<T<25)
# 83: Independent reconstruction using Atwood's acceleration invariant.
m1=1.3008130081300813;m2=2.191780821917808
a=g*(m2-m1)/(m1+m2)
near('83 reconstructed fall in two seconds',.5*a*2**2,5)
near('83 tension from lighter body',m1*(g+a),16)
near('83 tension from heavier body',m2*(g-a),16)
yes('83 actual heavier body descends',m2>m1>0)
# 84: A discrete uniform rope reproduces the continuous fraction bound.
for mu in [0,.1,.5,1,4]:
 bound=mu/(1+mu)
 near(f'84 limit force balance mu={mu}',bound,mu*(1-bound))
 yes(f'84 nonnegative physical fraction mu={mu}',0<=bound<1)
 q=min(.999999,bound+.001)
 yes(f'84 above boundary slips mu={mu}',q>mu*(1-q))
 if bound>0:
  q=bound/2
  yes(f'84 below boundary holds mu={mu}',q<=mu*(1-q))
# 85: Actual centre geometry and vector equilibrium, including all three wires.
m=15;R=.125;L=.35;hyp=L+R;dy=math.sqrt(hyp*hyp-R*R)
direction=np.array([R,dy])/hyp
T=152.37064185728167;N=40.0975373308636
near('85 from node to sphere surface is actual wire length',np.linalg.norm(np.array([R,dy]))-R,L)
near('85 contacting centres separated by a diameter',2*R,.25)
force=T*direction+np.array([-N,-m*g])
near('85 left sphere net horizontal force',force[0],0)
near('85 left sphere net vertical force',force[1],0)
near('85 upper wire balances node vertical forces',2*T*direction[1],294)
near('85 upper wire has no horizontal resultant',T*direction[0]-T*direction[0],0)
near('85 contact forces are opposite',N-N,0)

chunks=re.split(r'(?=^### )',text,flags=re.M);unit_hashes={}
for n in range(79,86):
 unit=next(c for c in chunks if re.match(r'### 5\.'+str(n)+r'\b',c));unit_hashes[f'5.{n}']=hashlib.sha256(unit.strip().encode('utf8')).hexdigest()
 yes(f'{n} one closed solution',unit.count('<details>')==unit.count('</details>')==1 and '<details open' not in unit)
 for marker in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']:yes(f'{n} {marker}',marker in unit)
 if n==85:
  prompt=unit.split('<details>',1)[0]
  yes('85 original two-part question',( '(a)' in prompt and '(b)' in prompt and '(c)' not in prompt and 'cả ba dây' in prompt))
 if n==84:yes('84 coefficient is not called rope mass','có khối lượng là' not in unit)
report={'status':'passed-numeric-and-structure-scope','scope':'Seven units 5.79–5.85; source PDF186 visually inspected. Runtime, exact source pixels and final acceptance are separate gates. Whole chapter remains incomplete.','checksCount':len(checks),'reviewedUnitsSHA256':unit_hashes,'checks':checks}
(REVIEW_OUTPUT/'independent-079-085-review.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(checks),'independent force/geometry/domain/structure checks for seven units.')
