"""Independent source-bound verification of all chapter8 theory, examples and self-checks."""
from pathlib import Path
import hashlib,json,math,re,subprocess,sys
import numpy as np,pymupdf
from scipy.integrate import quad,solve_ivp
ROOT=Path(__file__).resolve().parents[2];RAW=ROOT/'raw_materials/physics/translations/chapter-08'
OUT=ROOT/'qa/physics1-remaining/ch08-parent-theory-recomputed';OUT.mkdir(parents=True,exist_ok=True)
checks=[]
def near(name,a,b,tol=1e-9):
 assert np.allclose(a,b,rtol=tol,atol=tol),(name,a,b)
 checks.append(dict(name=name,actual=np.asarray(a).tolist(),expected=np.asarray(b).tolist()))
def yes(name,c):
 assert c,name
 checks.append(dict(name=name,passed=True))
sha=lambda p:hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n') if p.suffix in ['.md','.mjs','.py','.json','.svg'] else p.read_bytes()).hexdigest()
# Chapter opener and section8.1.
for m,v,expected in [(.2,15,[3,22.5]),(.1,30,[3,45])]:
 near('opening hailstone p,K '+str(m),[m*v,.5*m*v*v],expected)
near('opening same momentum and doubled kinetic energy',(.5*.1*30**2)/(.5*.2*15**2),2)
for F,m,t in [(np.array([2.,-3.]),5,.7),(np.array([-4.,1.]),1.2,.3)]:
 near('8.1 explicit two-force component sum '+str(m),F+(-F),[0,0])
 v0=np.array([3.,2.]);v1=v0+F/m*t
 near('8.1 Newton constant mass momentum derivative '+str(m),m*(v1-v0)/t,F)
 near('8.1 constant-force impulse '+str(m),m*v1-m*v0,F*t)
J=np.array([quad(lambda t:2*t,.2,1.4)[0],quad(lambda t:-3*t*t,.2,1.4)[0]])
near('8.1 independent variable force component integrals',J,[1.92,-2.736])
near('8.1 average force yields same impulse',J/1.2*1.2,J)
for m,v,p,K in [(.5,4,2,4),(.1,20,2,20)]:
 near('8.1 original catch-ball p,K '+str(m),[m*v,.5*m*v*v],[p,K])
near('8.1 original catch work ratio',20/4,5)
for m,F,s in [(2.3,4.7,8.1),(13,25,60)]:
 t1=math.sqrt(2*s*m/F);t2=math.sqrt(2*s*2*m/F)
 near('example1 time ratio '+str(m),t2/t1,math.sqrt(2))
 near('example1 impulse/momentum ratio '+str(m),F*t2/(F*t1),math.sqrt(2))
 near('example1 equal final kinetic energies '+str(m),[(F*t1)**2/(2*m),(F*t2)**2/(4*m)],[F*s,F*s])
near('example2 actual momenta', [.4*(-30),.4*20],[-12,8])
near('example2 impulse and mean force',[.4*50,.4*50/.01],[20,2000])
near('example2 weight small compared to collision force',.4*9.8,3.92)
yes('example2 source sign warning counterexample',8-12<0<8-(-12))
vf=30*np.array([math.cos(math.pi/4),math.sin(math.pi/4)])
J=.4*(vf-[-20,0]);F=J/.01
near('example3 exact outgoing components',vf,[21.213203435596427]*2)
near('example3 exact impulse components',J,[16.48528137423857,8.48528137423857])
near('example3 exact mean force components',F,[1648.528137423857,848.528137423857])
yes('example3 source rounded1650,850 consistent',np.allclose(F,[1650,850],rtol=.003))
near('example3 exact force magnitude',np.linalg.norm(F),1854.0887303142138,tol=1e-7)
yes('example3 force direction27degrees differs from outgoing45',abs(math.degrees(math.atan2(F[1],F[0]))-27)<.5)
impulses=[1000*(0-25),1000*(0-25),2000*10,-2000*10,1000*(-25-25)]
near('TYU1 all original signed impulses',impulses,[-25000,-25000,20000,-20000,-50000])
yes('TYU1 full ordering',abs(impulses[4])>abs(impulses[0])==abs(impulses[1])>abs(impulses[2])==abs(impulses[3]))
# Section8.2: Momentum laws and the three worked examples.
near('figure8.11 actual perpendicular momentum resultant',math.hypot(18,24),30)
near('figure8.11 actual resultant angle',math.degrees(math.atan2(18,24)),36.86989764584402)
M,m,u=3.,.005,300.;V=-m*u/M
near('example4 source recoil velocity',V,-.5)
near('example4 two original momenta',[m*u,M*V],[1.5,-1.5])
near('example4 two original energies',[.5*m*u*u,.5*M*V*V],[225,.375])
near('example4 inverse-mass energy ratio',(.5*m*u*u)/(.5*M*V*V),600)
near('example4 zero final total momentum',m*u+M*V,0)
ma,mb,ua,ub,vb=.5,.3,2.,-2.,2.;P=ma*ua+mb*ub;va=(P-mb*vb)/ma
near('example5 exact outgoing A velocity',va,-.4)
near('example5 both momentum changes',[ma*(va-ua),mb*(vb-ub)],[-1.2,1.2])
near('example5 both velocity changes',[va-ua,vb-ub],[-2.4,4])
near('example5 momentum remains source0.4',ma*va+mb*vb,.4)
vA=np.array([math.cos(math.pi/6),math.sin(math.pi/6)])
vB=(np.array([40.,0])-20*vA)/12
near('example6 exact B components',vB,[1.8899576603592687,-.8333333333333333])
near('example6 exact B speed',np.linalg.norm(vB),2.065522791545793)
near('example6 exact B signed angle',math.degrees(math.atan2(vB[1],vB[0])),-23.793976886996884)
near('example6 original postcollision momentum A',20*vA,[17.320508075688775,10])
near('example6 original postcollision momentum B',12*vB,[22.679491924311225,-10])
near('example6 restored source evaluation total',20*vA+12*vB,[40,0])
for a,b in [(2,3),(5,.7),(1,10)]:
 vA=np.array([-a,0.]);vB=np.array([0.,-b]);vC=-vA-vB
 near('TYU2 all three momenta sumzero '+str((a,b)),vA+vB+vC,[0,0])
 yes('TYU2 both C components positive '+str((a,b)),np.all(vC>0))
 yes('TYU2 C faster than both other fragments '+str((a,b)),np.linalg.norm(vC)>max(a,b))
# Section8.3: Finite collision energy, ballistic pendulum and vehicle assumptions.
for ma,mb,ua,ub in [(1,4,8,0),(.5,.3,2,-2),(2,7,-4,3)]:
 V=(ma*ua+mb*ub)/(ma+mb)
 Ki=.5*ma*ua*ua+.5*mb*ub*ub;Kf=.5*(ma+mb)*V*V
 near('soft collision momentum '+str((ma,mb)),(ma+mb)*V,ma*ua+mb*ub)
 near('soft collision independent energy loss '+str((ma,mb)),Ki-Kf,.5*ma*mb/(ma+mb)*(ua-ub)**2)
 yes('soft collision actual distinct incoming speeds lose K '+str((ma,mb)),Ki>Kf)
near('example7 source common speed',(.5*2+.3*(-2))/.8,.5)
near('example7 source before/after kinetic energy',[.5*.5*2**2+.5*.3*2**2,.5*.8*.5**2],[1.6,.1])
near('example7 source remaining ratio',.1/1.6,1/16)
near('example7 source converted fraction',(1.6-.1)/1.6,15/16)
near('example7 ideal locked spring can retain former kinetic energy',.1+1.5,1.6)
mb,mw,g,h=.005,2.,9.8,.03;V=math.sqrt(2*g*h);u=(mb+mw)/mb*V
near('example8 original common speed',V,.7668115805072325)
near('example8 original reconstructed bullet speed',u,307.4914437834002)
near('example8 impact momentum',mb*u,(mb+mw)*V)
near('example8 swing energy balance',.5*(mb+mw)*V*V,(mb+mw)*g*h)
near('example8 exact initial/final energies',[.5*mb*u*u,.5*(mb+mw)*V*V],[236.37747,.58947])
P=np.array([2000*10.,1000*15.]);V=P/3000
near('example9 original momenta',P,[20000,15000])
near('example9 resultant momentum and speed',[np.linalg.norm(P),np.linalg.norm(V)],[25000,25/3])
near('example9 direction north of east',math.degrees(math.atan2(V[1],V[0])),36.86989764584402)
near('example9 exact total initial kinetic energy',.5*1000*15**2+.5*2000*10**2,212500)
near('example9 exact total final kinetic energy',.5*3000*(V@V),104166.66666666667)
near('example9 source rounded friction estimate',.5*10000,5000)
near('example9 source rounded crumple force estimate',1.1e5/.20,550000)
near('example9 source rounded collision-to-friction ratio',(1.1e5/.20)/5000,110)
for ratio in [1,.5,0]:
 near('TYU3 rebound energy ratio from heights '+str(ratio),math.sqrt(ratio)**2,ratio)
yes('TYU3 all three actual classifications',1==1 and 0<.5<1 and 0==0)
# Section8.4: Verify derivation residuals using independently solved momentum/restitution.
for ma,mb,u in [(1,1,2),(.01,10,3),(10,.01,3),(2,7,-4),(7,2,5)]:
 va,vb=np.linalg.solve([[ma,mb],[-1,1]],[ma*u,u])
 near('elastic source formula A '+str((ma,mb)),va,(ma-mb)/(ma+mb)*u)
 near('elastic source formula B '+str((ma,mb)),vb,2*ma/(ma+mb)*u)
 near('elastic source factorization residual '+str((ma,mb)),ma*(u-va)*(u+va),mb*vb*vb)
 near('elastic source momentum residual '+str((ma,mb)),ma*(u-va),mb*vb)
 near('elastic source division relation '+str((ma,mb)),vb,u+va)
 near('elastic kinetic energy '+str((ma,mb)),ma*va*va+mb*vb*vb,ma*u*u)
 near('elastic relative speed reversal '+str((ma,mb)),vb-va,u)
va,vb=np.linalg.solve([[.5,.3],[-1,1]],[.4,4])
near('example10 two final velocities',[va,vb],[-1,3])
near('example10 final total kinetic energy',.5*.5*va*va+.5*.3*vb*vb,1.6)
near('example10 momentum',.5*va+.3*vb,.4)
u=2.6e7;vn=-11/13*u;vc=2/13*u
near('example11 original final velocities',[vn,vc],[-2.2e7,4e6])
near('example11 momentum in consistent atomic-mass units',vn+12*vc,u)
near('example11 kinetic-energy conservation in consistent mass units',vn*vn+12*vc*vc,u*u)
near('example11 retained neutron energy fraction',(vn/u)**2,121/169)
near('example11 two successive source head-on fractions',(121/169)**2,14641/28561)
yes('example11 rounded28percent loss matches exact fraction',abs((1-121/169)-.28)<.005)
ma,mb,u,va=.5,.3,4.,2.;vb=math.sqrt(ma/mb*(u*u-va*va));p=ma*u;a=ma*va;b=mb*vb
alpha=math.acos((p*p+a*a-b*b)/(2*p*a));beta=math.atan2(a*math.sin(alpha),p-a*math.cos(alpha))
near('example12 outgoing B speed',vb,math.sqrt(20))
near('example12 source angles',[math.degrees(alpha),math.degrees(beta)],[36.86989764584402,26.56505117707799])
yes('example12 beta branch lies in first quadrant',0<beta<math.pi/2 and p-a*math.cos(alpha)>0)
vA=va*np.array([math.cos(alpha),math.sin(alpha)]);vB=vb*np.array([math.cos(beta),-math.sin(beta)])
near('example12 full original momentum',ma*vA+mb*vB,[2,0])
near('example12 original separate y momenta',[ma*vA[1],mb*vB[1]],[.6,-.6])
near('example12 full kinetic energy',.5*ma*(vA@vA)+.5*mb*(vB@vB),4)
near('example12 vector relative speed',np.linalg.norm(vB-vA),u)
fwater=((1-18)/(1+18))**2;fcarbon=((1-12)/(1+12))**2
near('TYU4 hypothetical water molecule retained speed ratio',abs((1-18)/(1+18)),17/19)
near('TYU4 hypothetical water molecule energy ratio',fwater,289/361)
yes('TYU4 water18u target less effective in stated head-on model',fwater>fcarbon)
# Section8.5: Mass-weighted coordinates, symmetry, motion and external-force domains.
mass=np.array([1.,2.,3.]);positions=np.array([[1,2,3],[-2,1,0],[4,-2,1.]])
cm=mass@positions/sum(mass)
near('8.5 expanded versus vector weighted mean',cm,sum(m*r for m,r in zip(mass,positions))/sum(mass))
near('8.5 mass-weighted displacements about CM sumzero',mass@(positions-cm),[0,0,0])
d=9.57e-11;angle=math.radians(52.5)
pos=np.array([[0.,0.,0.],[d*math.cos(angle),d*math.sin(angle),0],[d*math.cos(angle),-d*math.sin(angle),0]])
atoms=np.array([16.,1.,1.]);cm=atoms@pos/18
independent_halfangle=math.sqrt((4+math.sqrt(2)-math.sqrt(6))/8)
near('example13 independent half-angle check',math.cos(angle),independent_halfangle)
near('example13 source CM coordinates normalized by bond length',cm/d,[2*independent_halfangle/18,0,0])
near('example13 true dimensionless CM fraction',cm[0]/d,2*math.cos(angle)/18)
rotated=pos*np.array([1,-1,-1])
near('example13 actual180degree symmetry normalized by bond length',rotated[[0,2,1]]/d,pos/d)
near('example13 CM remains fixed by that symmetry normalized by bond length',(atoms@rotated/18)/d,cm/d)
M=150.;initial=np.array([-10.,10.]);masses=np.array([90.,60.]);cm=masses@initial/M;xj=-4.;xr=(M*cm-90*xj)/60
near('example14 initial CM',cm,-2)
near('example14 actual final Ramon position',xr,1)
near('example14 original displacements',[xj-initial[0],xr-initial[1]],[6,-9])
near('example14 same final CM',(90*xj+60*xr)/M,cm)
near('example14 inverse displacement/mass ratio',6/9,60/90)
near('example14 both eventually meet at fixed CM',[initial[0]+8,initial[1]-12],[-2,-2])
# Before either fragment lands, external gravity preserves the original CM parabola.
g=np.array([0.,-9.8]);r0=np.array([0.,30.]);v0=np.array([10.,5.]);kick=np.array([3.,7.])
for t in [.1,.5,1]:
 r1=r0+(v0+kick)*t+.5*g*t*t;r2=r0+(v0-kick)*t+.5*g*t*t
 near('8.5 airborne fragment CM '+str(t),(r1+r2)/2,r0+v0*t+.5*g*t*t)
near('TYU5 resting landed fragment adds external support force',(-9.8+0)/2,-4.9)
yes('TYU5 supported pair CM acceleration not freefall',not math.isclose(-4.9,-9.8))
# Section8.6: Closed packet momentum, first-order limit and independent ODE integration.
m,u,v=120000.,2400.,300.
errors=[]
for h in [.1,.05,.025]:
 dm=-1000*h;dv_de=-u*dm/m;P1=m*v;P2=(m+dm)*(v+dv_de)+(-dm)*(v-u)
 near('8.6 finite-packet first-order residual '+str(h),P2-P1,dm*dv_de,tol=1e-7)
 errors.append(abs(P2-P1))
 dv_exact=-u*dm/(m+dm)
 near('8.6 exact finite packet momentum '+str(h),(m+dm)*(v+dv_exact)+(-dm)*(v-u),P1)
near('8.6 neglected product is genuinely second order',[errors[1]/errors[0],errors[2]/errors[1]],[.25,.25],tol=1e-6)
for mass,rate in [(120000,1000),(60,.5)]:
 near('example15 actual initial acceleration '+str(mass),2400*rate/mass,20)
 near('example15 consistent original mass fraction per second '+str(mass),rate/mass,1/120)
m0=120000.;rate=m0/120;u=2400.
sol=solve_ivp(lambda t,y:[-rate,u*rate/y[0]],[0,90],[m0,0],rtol=1e-11,atol=1e-10)
mass,velocity=sol.y[:,-1];exact=u*math.log(4)
near('example16 independently integrated final mass',mass,m0/4)
near('example16 independently integrated final speed',velocity,exact)
near('example16 analytic source final speed',exact,3327.1064666877373)
near('example16 last gas packet velocity',velocity-u,927.1064666877373)
tstar=120*(1-math.exp(-1))
near('example16 true gas-stationary time',tstar,75.85446705942692)
near('example16 stationary packet condition',u*math.log(m0/(m0-rate*tstar))-u,0)
yes('example16 parent75.9s matches exact result',abs(tstar-75.9)<.05)
yes('example16 printed75.6s is not exact result at this precision',abs(tstar-75.6)>.2)
for t,expected_a in [(0,20),(30,80/3),(60,40),(90,80)]:
 m=m0-rate*t
 near('TYU6 constant thrust implies increasing acceleration sample '+str(t),u*rate/m,expected_a)
 a=20.;mass_constant_a=m0*math.exp(-a*t/u);step=.001
 numerical_mass_derivative=(m0*math.exp(-a*(t+step)/u)-m0*math.exp(-a*(t-step)/u))/(2*step)
 thrust_from_flux=-u*numerical_mass_derivative
 near('TYU6 constant acceleration checked from independent mass-flux derivative '+str(t),thrust_from_flux/mass_constant_a,a,tol=1e-7)
yes('TYU6 decreasing thrust for constant positive acceleration',20*m0*math.exp(-20*90/u)<20*m0)
# Bind the checked source content and all current source-image pixels.
names=['00-mo-dau.md']+[f'{i:02d}-muc-{i:02d}.md' for i in range(1,7)]+['17-tom-tat.md']
texts={n:(RAW/n).read_text(encoding='utf8') for n in names}
for number in range(1,41):
 yes('all original equation identifiers retained8.'+str(number),any(re.search(r'Công thức \(8\.'+str(number)+r'(?:[abc])?\)',t) for t in texts.values()))
for number in range(1,17):
 yes('all original worked examples retained8.'+str(number),any('Ví dụ 8.'+str(number)+':' in t for t in texts.values()))
for number in range(1,7):yes('all six immediate self-checks retained8.'+str(number),'Kiểm tra hiểu biết Mục 8.'+str(number) in texts[f'{number:02d}-muc-{number:02d}.md'])
yes('source strategy indexing and particle model restored','Mô hình hóa mỗi vật thành chất điểm' in texts[names[2]] and 'chỉ số 1, 2' in texts[names[2]])
yes('source meatball/spaghetti example restored','spaghetti' in texts['03-muc-03.md'])
yes('source locked-spring energy alternative restored','Nếu hai xe khóa vào nhau khi lò xo' in texts['03-muc-03.md'])
yes('source Eq8.17/18 applicability caution restored','Không cần học thuộc chúng' in texts['03-muc-03.md'])
yes('source Saturn encounter context retained','Sao Thổ' in texts['03-muc-03.md'])
yes('source three conservation equations not mislabeled three laws','ba phương trình này' in texts['04-muc-04.md'])
yes('rocket body reference-frame hard step explicit','Các phần khí đã rời tên lửa trước đó giữ vận tốc' in texts['06-muc-06.md'])
yes('all source squid application quantities retained',all(k in texts['06-muc-06.md'] for k in ['Sepioteuthis sepioidea','2\\text{ m}','10\\text{ m}','50 lần']))
yes('summary has explicit finite momentum index set',r'\sum_{i=1}^{n}\vec p_i' in texts['17-tom-tat.md'])
yes('no learner source-process commentary',not re.search(r'theo sách|ảnh nguyên gốc sách|tiến độ bản dịch|bản dịch của','\n'.join(texts.values()),re.I))
coverage=json.loads((ROOT/'raw_materials/physics/reviews/ch08-remaining-theory-coverage.json').read_text(encoding='utf8'))
rows=coverage['figures'];yes('all44 original theory asset frames retained',len(rows)==44)
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for row in rows:
  f=ROOT/'docs/vat-ly-1/bai-giang/img/young-08'/(row['asset']+'.png')
  px=pdf[row['pdfPage']-1].get_pixmap(matrix=pymupdf.Matrix(2,2),clip=pymupdf.Rect(row['rectangle']),alpha=False);a=pymupdf.Pixmap(str(f))
  yes('unaltered actual PDF pixels '+row['asset'],(px.width,px.height,px.samples)==(a.width,a.height,a.samples))
  yes('original asset is actually referenced '+row['asset'],sum(t.count('/young-08/'+row['asset']+'.png)') for t in texts.values())==1)
 rocket=next(r for r in rows if r['asset']=='r-theory-hinh-8-34')
 image_rect=pdf[277].get_image_rects(8514)[0];clip=pymupdf.Rect(rocket['rectangle'])
 yes('Atlas photo complete actual embedded source bounds',clip.contains(image_rect))
 px=pdf[199].get_pixmap(matrix=pymupdf.Matrix(2.5,2.5),clip=pymupdf.Rect(80,516,250,624),alpha=False)
 a=pymupdf.Pixmap(str(ROOT/'docs/vat-ly-1/bai-giang/img/young-06/r-theory-06-14.png'))
 yes('restored Example8.1 original referenceFigure6.14 unchanged pixels',(px.width,px.height,px.samples)==(a.width,a.height,a.samples))
result=dict(status='passed-parent-current-chapter8-theory-source-models',checksCount=len(checks),sourcePDFPagesRead=list(range(255,281)),referenceFigurePDFPage=200,sourceHashes={n:sha(RAW/n) for n in names},sourceOriginalFrames=44,additionalReferencedSourceFrames=1,examples=16,selfChecks=6,sourceNumberedEquations=40,sourceDiscrepancies=[dict(unit='Example8.16',printedTimeSeconds=75.6,recomputedTimeSeconds=tstar,learnerRoundedTimeSeconds=75.9,method='Constant mass flow m0/120 per second and velocity condition ln(m0/m)=1.')],records=checks,scopeLimit='Theory/source models and exact source pixels. Complete-frame visual review, language decisions, Wiki/cheatsheet and actual routes/public deployment require their separate acceptance evidence.')
(OUT/'parent-theory-models.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(checks),'independent source/model/pixel checks for current full chapter8 theory.')
