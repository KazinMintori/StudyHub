"""Independent force, integration and domain checks for the reviewed nine units."""
from pathlib import Path
import hashlib, json, math, re
import numpy as np
from scipy.integrate import quad

ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-late-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True)
ROOT = B.parents[3]
P = B / 'parent-12-bai-tap-060-118.md'
text = P.read_text(encoding='utf8')
checks = []

def near(name, actual, expected, tol=1e-9):
    assert math.isclose(float(actual), float(expected), rel_tol=tol, abs_tol=tol), (name, actual, expected)
    checks.append({'name': name, 'actual': float(actual), 'expected': float(expected)})

def yes(name, condition):
    assert condition, name
    checks.append({'name': name, 'passed': True})

g = 9.8
rad = math.radians
# 5.69: Independent quadrature, not another evaluation of the written primitive.
a = lambda t: (36*t - 3*g)/3
v = lambda t: quad(a, 0, t)[0]
y = lambda t: quad(lambda tau: (t-tau)*a(tau), 0, t)[0]
near('5.69 v at 1 second', v(1), -3.8)
near('5.69 v at 3 seconds', v(3), 24.6)
near('5.69 return after launch', y(2.45), 0)
near('5.69 deepest position', y(g/6), -4.35737037037037)
yes('5.69 velocity changes from down to up', v(g/6-.001)<0<v(g/6+.001))
yes('5.69 acceleration zero is earlier than deepest point', g/12 < g/6)
# 5.70: Reconstruct actual acceleration from all forces and the final travel.
theta=rad(30);m=5.;F=43.696320136397226;n=m*g*math.cos(theta)
actual_a=(F-m*g*math.sin(theta)-.4*n)/m
near('5.70 displacement in six seconds', .5*actual_a*6**2, 8)
yes('5.70 overcomes static friction at launch', F-m*g*math.sin(theta)>.43*n)
near('5.70 static threshold', m*g*math.sin(theta)+.43*n, 42.74715525773812)
# 5.71: Many admissible slopes all reproduce both prescribed accelerations.
for angle in range(35,81,5):
    theta=rad(angle);mu=(math.sin(theta)-.5)/math.cos(theta);m=25;F=245
    near(f'5.71 initial acceleration at {angle} degrees',g*(math.sin(theta)-mu*math.cos(theta)),4.9)
    n=(m*g+F)*math.cos(theta)
    near(f'5.71 final acceleration at {angle} degrees',((m*g+F)*math.sin(theta)-mu*n)/m,9.8)
    yes(f'5.71 physical friction at {angle} degrees',mu>=0 and n>0)
unit71=next(c for c in re.split(r'(?=^### )',text,flags=re.M) if re.match(r'### 5\.71\b',c))
yes('5.71 complete actual questions restored','9{,}8' in unit71.split('<details>')[0] and 'So sánh' in unit71.split('<details>')[0])
yes('5.71 no false contact-force equality','F_{\\text{tiếp xúc}} = mg' not in unit71)
# 5.72: Threshold is slip, not loss of contact.
m=103.33919730563436;F=380;theta=rad(30);n=m*g-F*math.sin(theta)
near('5.72 threshold horizontal balance',F*math.cos(theta),.4*n)
yes('5.72 still touches floor',n>0)
yes('5.72 slightly smaller force remains static',(F-.01)*math.cos(theta)<.4*(m*g-(F-.01)*math.sin(theta)))
# 5.73: Cartesian force vectors, independently of scalar incline formulas.
m=8.;theta=rad(33);n=51.59115761653054
normal=n*np.array([-math.sin(theta),math.cos(theta)])
friction=.3*n*np.array([math.cos(theta),math.sin(theta)])
net=np.array([-26.,-m*g])+normal+friction
tangent=np.array([-math.cos(theta),-math.sin(theta)])
near('5.73 zero normal acceleration',np.dot(net,[-math.sin(theta),math.cos(theta)]),0)
near('5.73 tangential acceleration',np.dot(net,tangent)/m,6.12847347835)
near('5.73 velocity magnitude after two seconds',np.linalg.norm(net)/m*2,12.2569469567)
yes('5.73 positive contact',n>0)
# 5.74: Reconstruct the full two-body system and displacement.
m1=20.;m2=36.04829047603071;T=257.1444720623524;theta=rad(53.1)
a1=(T-m1*g*math.sin(theta)-.4*m1*g*math.cos(theta))/m1
a2=(m2*g-T)/m2
near('5.74 same rope acceleration',a1,a2)
near('5.74 descend twelve metres in three seconds',.5*a2*3**2,12)
# 5.75: Independent work/energy calculation as a private numeric cross-check.
net=96*math.sin(rad(60))-5*g-.3*96*math.cos(rad(60))
near('5.75 kinetic energy',.5*5*1.7771185109972205**2,net*.4)
yes('5.75 positive upward acceleration',net>0)
# 5.76: Node forces and actual static friction.
T=12/math.sin(rad(45));near('5.76 horizontal tension',T*math.cos(rad(45)),12)
yes('5.76 actual friction below maximum',12<.25*60)
near('5.76 limiting suspended weight',.25*60,15)
# 5.77: Random/edge combinations test static set membership and moving cases.
for angle in [0,10,30,45,70,89]:
 for mu in [0,.1,.4,1,2]:
    theta=rad(angle);m1=3.7;s=math.sin(theta);c=math.cos(theta)
    lower=max(0,m1*(s-mu*c));upper=m1*(s+mu*c)
    for m2 in [0,lower,(lower+upper)/2,upper,upper+.02]:
        required_f=m1*g*s-m2*g
        can_hold=abs(required_f)<=mu*m1*g*c+1e-10
        in_interval=lower-1e-10<=m2<=upper+1e-10
        yes(f'5.77 static set {angle}/{mu}/{m2:.6f}',can_hold==in_interval)
    m2up=m1*(s+mu*c)
    near(f'5.77 steady uphill {angle}/{mu}',m2up*g-m1*g*s-mu*m1*g*c,0)
    m2down=m1*(s-mu*c)
    if m2down>=0:near(f'5.77 steady downhill {angle}/{mu}',m1*g*s-m2down*g-mu*m1*g*c,0)
    else:yes(f'5.77 negative hanging mass excluded {angle}/{mu}',m1*g*s-mu*m1*g*c<0)
unit77=next(c for c in re.split(r'(?=^### )',text,flags=re.M) if re.match(r'### 5\.77\b',c))
yes('5.77 nonnegative static lower limit explicit',r'\max(0,L)' in unit77)
for number in range(69,78):
    unit=next(c for c in re.split(r'(?=^### )',text,flags=re.M) if re.match(r'### 5\.'+str(number)+r'\b',c))
    yes(f'5.{number} one closed solution',unit.count('<details>')==unit.count('</details>')==1 and '<details open' not in unit)
    for marker in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']:yes(f'5.{number} {marker}',marker in unit)

unit_hashes={f'5.{n}':hashlib.sha256(next(c for c in re.split(r'(?=^### )',text,flags=re.M) if re.match(r'### 5\.'+str(n)+r'\b',c)).strip().encode('utf8')).hexdigest() for n in range(69,78)}
report={'status':'passed-numeric-and-structure-scope','scope':'5.69–5.77; actual source PDF pages185–186 visually reviewed by parent. Runtime and crop completeness are separate gates. Whole chapter not accepted.', 'fragmentSHA256':hashlib.sha256(P.read_bytes()).hexdigest(),'reviewedUnitsSHA256':unit_hashes,'checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'independent-069-077-review.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(checks),'independent numeric/domain/structure checks; nine units only.')
