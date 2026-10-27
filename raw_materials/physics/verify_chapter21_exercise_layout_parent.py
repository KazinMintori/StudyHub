"""Independent physical checks for source-preserving chapter21 exercise layout repairs."""
from pathlib import Path
import json,math,re,hashlib
import numpy as np
from scipy.integrate import quad,dblquad
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[2];RAW=ROOT/'raw_materials/physics/translations/chapter-21'
OUT=ROOT/'qa/physics-global-audit/ch21-parent-format-repair';checks=[]
K=8.9875517923e9;e=1.602176634e-19;eps=1/(4*math.pi*K)
def near(name,a,b,tol=1e-9):
 a,b=np.asarray(a,dtype=float),np.asarray(b,dtype=float)
 scale=max(np.max(np.abs(a)),np.max(np.abs(b)),1e-300)
 assert np.allclose(a/scale,b/scale,rtol=tol,atol=tol),(name,a,b)
 checks.append({'name':name,'actual':a.tolist(),'expected':b.tolist()})
def force(q,Q,r,at):
 d=np.array(at)-np.array(r);return K*q*Q*d/np.linalg.norm(d)**3
near('VP21.4.3 direct vector Coulomb superposition',
 force(6e-9,-2.5e-9,[0,.2],[.15,0])+force(-6e-9,-2.5e-9,[0,-.2],[.15,0]),
 [0,2*(K*6e-9*2.5e-9/.25**2)*(.2/.25)])
r1=math.hypot(.25,.2);F1=K*4e-9*1.5e-9/r1**2;F2=K*4e-9*1.5e-9/.25**2
near('VP21.4.4 direct vector Coulomb superposition',
 force(4e-9,-1.5e-9,[0,.2],[.25,0])+force(-4e-9,-1.5e-9,[0,0],[.25,0]),
 [F2-F1*.25/r1,F1*.2/r1])
near('VP21.10.1b signed field',force(4e-9,1,[0,.2],[0,.4])+force(-5e-9,1,[0,0],[0,.4]),[0,K*4e-9/.2**2-K*5e-9/.4**2])
near('21.10 direct signed forces',force(4e-9,-6e-9,[.2,0],[0,0])+force(5e-9,-6e-9,[-.3,0],[0,0]),[K*24e-18/.2**2-K*30e-18/.3**2,0])
near('21.17 direct signed forces',force(-1.5e-9,5e-9,[0,-.6],[0,-.4])+force(3.2e-9,5e-9,[0,0],[0,-.4]),[0,-K*7.5e-18/.2**2-K*16e-18/.4**2])
b=.11e-9
def D(r):return K*e*e*(1/(r-b)**2-1/r**2)
for r,target in [(.28e-9,5.04e-9),(.29e-9,4.38e-9),(.3e-9,3.83e-9)]:
 near('DNA chain rounded result '+str(r),D(r),target,tol=.002)
near('21.18 chain sum',D(.28e-9)+D(.3e-9),8.87e-9,tol=.001)
near('21.19 chain sum',2*D(.29e-9)+D(.3e-9),1.26e-8,tol=.002)
near('21.18 hydrogen comparison',K*e*e/(.0529e-9)**2,8.24e-8,tol=.001)
direct=sum((force(q,1,r,[.06,0])for q,r in [(-5e-6,[0,.08]),(-2e-6,[0,0]),(-5e-6,[0,-.08])]),start=np.zeros(2))
near('21.37 direct vector superposition',direct,[-(K*2e-6/.06**2+2*K*5e-6/.1**2*.6),0])
for label,x in [('A',.15),('B',-.1)]:
 direct=force(-6.25e-9,1,[0,0],[x,0])+force(-12.5e-9,1,[.25,0],[x,0])
 expected=K*12.5e-9/.1**2-K*6.25e-9/.15**2 if label=='A' else K*6.25e-9/.1**2+K*12.5e-9/.35**2
 near('21.39 signed fields '+label,direct,[expected,0])
near('21.40 unit-vector fields source1',force(-5e-9,1,[0,0],[0,.04]),[0,-2.81e4],tol=.002)
near('21.40 unit-vector fields source2',force(3e-9,1,[.03,0],[0,.04]),[-6.47e3,8.63e3],tol=.002)
near('21.40 vector sum',force(-5e-9,1,[0,0],[0,.04])+force(3e-9,1,[.03,0],[0,.04]),[-6.47e3,-1.95e4],tol=.002)
near('21.44 direct fields',force(-4e-9,1,[.6,.8],[0,0])+force(6e-9,1,[.6,0],[0,0]),[.6*K*4e-9-K*6e-9/.6**2,.8*K*4e-9])
for unit,q0,qx,qt,at,source2 in [('21.59',5e-9,-2e-9,6e-9,[.04,.03],[.04,0]),('21.70',-3e-9,2e-9,5e-9,[.03,.04],[0,.04])]:
 direct=force(q0,qt,[0,0],at)+force(qx,qt,source2,at)
 target=[8.63e-5,-5.52e-5] if unit=='21.59' else [6.75e-5,-4.31e-5]
 near(unit+' direct two-dimensional forces',direct,target,tol=.002)
for R,x in[(.025,.2),(.025,.1),(2,.3),(.5,3)]:
 Q=.7
 direct=K*Q/(math.pi*R*R)*quad(lambda r:2*math.pi*r*x/(x*x+r*r)**1.5,0,R)[0]
 E0=Q/(2*math.pi*eps*R*R);rho=math.hypot(x,R)
 near('21.81 disk direct integration '+str((R,x)),direct,E0*(1-x/rho))
for R1,R2 in[(.1,.3),(.02,2)]:
 sigma=2.3;q=1.7;m=.4
 kappa=q*sigma/(2*eps)*(1/R1-1/R2)
 for x in[-.5,-.03,0,.03,.5]:
  r1,r2=math.hypot(x,R1),math.hypot(x,R2)
  direct=2*math.pi*K*sigma*quad(lambda r:r*x/(x*x+r*r)**1.5,R1,R2)[0]
  near('21.87 annulus direct integral '+str((R1,R2,x)),direct,sigma*x/(2*eps)*(1/r1-1/r2))
 h=R1*1e-5;derivative=(sigma*h/(2*eps)*(1/math.hypot(h,R1)-1/math.hypot(h,R2)))/h
 near('21.87 small-displacement restoring coefficient',q*derivative,kappa,tol=1e-8)
 near('21.87 frequency squared',((math.sqrt(kappa/m)/(2*math.pi))**2),kappa/(4*math.pi**2*m))
for R,delta in[(.05,.107),(.5,.3),(2,.05)]:
 F0=1.9
 ell=math.hypot(delta,R)-R
 direct=-F0*quad(lambda s:s/math.hypot(s,R),0,delta)[0]
 near('21.91 electric work integral '+str((R,delta)),direct,-F0*ell)
 for alpha in[.2,.6,.9]:
  turning=2*R*alpha/(1-alpha*alpha)
  near('21.91 turning equality '+str((R,alpha)),alpha*turning,math.hypot(turning,R)-R)
for u in[.23,.5,math.pi/4,1.1,1.3]:
 g1=lambda u:math.cos(u)/math.sin(u)**2
 g2=lambda u:math.sin(u)/math.cos(u)**2
 h=1e-5
 d1=(g1(u+h)-g1(u-h))/(2*h);d2=(g2(u+h)-g2(u-h))/(2*h)
 near('21.92 first quotient derivative '+str(u),d1,-1/math.sin(u)-2*math.cos(u)**2/math.sin(u)**3,tol=2e-8)
 near('21.92 second quotient derivative '+str(u),d2,1/math.cos(u)+2*math.sin(u)**2/math.cos(u)**3,tol=2e-8)
near('21.92 derivative at equilibrium',(-1/math.sin(math.pi/4)-2*math.cos(math.pi/4)**2/math.sin(math.pi/4)**3)-(1/math.cos(math.pi/4)+2*math.sin(math.pi/4)**2/math.cos(math.pi/4)**3),-6*math.sqrt(2))
f=lambda theta:math.sin(theta)**2*math.tan(theta)
theta1=math.radians(25);theta2=brentq(lambda t:f(t)-4*f(theta1),1e-8,math.pi/2-1e-8)
near('21.61 actual angle root',math.degrees(theta2),39.5,tol=.002)
charge=math.sqrt(.015*9.8*(2*1.2*math.sin(theta1))**2*math.tan(theta1)/K)
near('21.61 conserved charge',charge,2.80e-6,tol=.002)
near('21.61 same force balance after shortening',charge**2*K/(2*.6*math.sin(theta2))**2,.015*9.8*math.tan(theta2))
for a,L in[(.1,.5),(.4,.7),(2,.1)]:
 k=3.17;Q=.7;lam=Q/L
 for y in[0,L*.2,L*.5,L]:
  direct=quad(lambda z:1/(a*a+(y-z)**2)**1.5,0,L)[0]
  r0,rL=math.hypot(a,y),math.hypot(a,L-y);A=y/r0;B=(L-y)/rL
  near('21.93 inner integral '+str((a,L,y)),direct,(A+B)/a**2)
  near('21.93 differential xforce '+str((a,L,y)),k*lam**2*a*direct,k*lam**2/a*(A+B))
 force_direct=k*lam**2*a*dblquad(lambda y1,y2:1/(a*a+(y2-y1)**2)**1.5,0,L,lambda _:0,lambda _:L)[0]
 near('21.93 force double integral '+str((a,L)),force_direct,2*k*Q*Q/L**2*(math.sqrt(1+(L/a)**2)-1))
 U_direct=k*lam**2*dblquad(lambda y1,y2:1/math.sqrt(a*a+(y2-y1)**2),0,L,lambda _:0,lambda _:L)[0]
 Ra=math.hypot(a,L);Ta=math.log((L+Ra)/a);C=2*k*Q*Q/L**2
 near('21.93 electrostatic energy double integral '+str((a,L)),U_direct,C*L*Ta+C*a-C*Ra,tol=2e-10)
 h=1e-5*a
 H=lambda s:math.hypot(s,L)-s-L*math.log((L+math.hypot(s,L))/s)
 near('21.93 H antiderivative '+str((a,L)),(H(a+h)-H(a-h))/(2*h),math.hypot(a,L)/a-1,tol=1e-7)
 for x in[.2,.7,3]:
  c=x+a/2
  direct=k*lam*quad(lambda t:1/(c+t)**2,0,L)[0]
  near('21.97 direct rod axial integral '+str((a,L,x)),direct,k*Q/L*(1/c-1/(c+L)))
  near('21.97 appendix expression equivalence '+str((a,L,x)),direct,2*k*Q/(L*(2*x+a))-2*k*Q/(L*(2*L+2*x+a)))
original_prompts=0
ledger=json.loads((ROOT/'raw_materials/physics/reviews/ch21-exercise-layout-original-prompts-20261028.json').read_text(encoding='utf8'))
for row in ledger['files']:
 current=(ROOT/row['file']).read_text(encoding='utf8')
 units=re.findall(r'::: exercise[^\n]*\n[\s\S]*?\n:::',current)
 assert [hashlib.sha256(u.encode()).hexdigest()for u in units]==row['completePromptSHA256'],('Originalexercise text changed',row['file'])
 original_prompts+=len(units)
 checks.append({'name':'Originalcomplete prompts unchanged '+row['file'],'prompts':len(units),'passed':True})
files=[p for p in RAW.glob('*.md')if p.name in['09-luyen-tap-huong-dan.md','11-bai-tap-01-30.md','12-bai-tap-31-56.md','13-bai-tong-hop-57-80.md','14-bai-tong-hop-81-92.md','15-bai-nang-cao-mcat.md','17-dap-so-bai-le.md']]
result={'status':'passed-scoped-exercise-layout-physical-models','checks':len(checks),'originalCompletePromptsUnchanged':original_prompts,
 'sourceSHA256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n')).hexdigest()for p in files},
 'records':checks,'limitation':'Verifies the changed physical computations and source preservation. Fullchapter source audit, allpartsofsolutions and actual finalviewport acceptance require separate proof.'}
(OUT/'exercise-layout-models.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(checks),'independent physical-model checks;',original_prompts,'completeoriginal prompts unchanged.')
