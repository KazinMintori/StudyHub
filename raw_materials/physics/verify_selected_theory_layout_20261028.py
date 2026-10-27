"""Scoped physics checks for mobile presentation repairs in chapters23,25,35,36and39."""
from pathlib import Path
import hashlib,json,math,random
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'qa/physics-global-audit/selected-theory-repairs-20261028';OUT.mkdir(exist_ok=True)
records=[]
def near(name,a,b,tol=1e-11,physical_scale=None):
 scale=max(abs(a),abs(b),physical_scale or 0,1e-300)
 assert math.isclose(a/scale,b/scale,rel_tol=tol,abs_tol=tol),(name,a,b)
 records.append({'name':name,'actual':a,'expected':b,'physicalScale':scale})
rng=random.Random(20261028)
for n in[2,3,5,9]:
 for j in range(6):
  q0=rng.uniform(-3,3)*1e-9
  qs=[rng.uniform(-5,5)*1e-9 for _ in range(n)]
  rs=[rng.uniform(.03,.7)for _ in range(n)]
  individual=[8.9875517923e9*q0*q/r for q,r in zip(qs,rs)]
  near('23.10 named interaction energies '+str((n,j)),math.fsum(individual),8.9875517923e9*q0*math.fsum(q/r for q,r in zip(qs,rs)),physical_scale=math.fsum(abs(u)for u in individual))
emf=12;r=2;R=4;I=emf/(r+R)
near('25terminal current',I,2)
near('25terminal load drop',I*R,8)
near('25terminal source minus internal drop',emf-I*r,I*R)
near('35two-source intensity at4degrees',math.cos(2*math.pi*math.sin(math.radians(4)))**2,.82,tol=.004)
for m in[-7,-5,-3,3,5,7]:
 sintheta=m/8
 theta=math.asin(sintheta)
 near('35additional half-intensity phase '+str(m),2*math.pi*math.sin(theta),m*math.pi/4)
 near('35additional half-intensity result '+str(m),math.cos(2*math.pi*math.sin(theta))**2,.5)
near('35selfchecki',math.cos(.8*math.pi)**2,.655,tol=.002)
near('35selfcheckii',math.cos(2)**2,.173,tol=.002)
near('35selfcheckiii',math.cos(1.5*math.pi)**2,0,physical_scale=1)
near('35selfcheckiv',math.cos(1)**2,.292,tol=.002)
ranking=sorted(range(4),key=lambda i:[math.cos(.8*math.pi)**2,math.cos(2)**2,0,math.cos(1)**2][i],reverse=True)
assert ranking==[0,3,1,2]
records.append({'name':'35actualdescending ranking','actual':ranking,'passed':True})
near('36second dark fringe location fromfirst',2*.016,.032)
near('36distance between second dark fringes',2*.032,.064)
for lam,a,target in[(4e-7,2e-4,2e-3),(6e-7,2e-4,3e-3),(4e-7,3e-4,1.33e-3),(6e-7,3e-4,2e-3)]:
 near('36selfcheck wavelength/slit ratio '+str((lam,a)),lam/a,target,tol=.003)
for m in[-3,-2,-1,0,1,2,3]:
 d=4e-6;lam=6e-7;theta=math.asin(m*lam/d)
 near('36grating peak condition '+str(m),d*math.sin(theta),m*lam)
for m in[1,2,3]:
 d=1e-9;lam=2e-10;theta=math.asin(m*lam/(2*d))
 near('36Bragg positive order '+str(m),2*d*math.sin(theta),m*lam)
hc_eVnm=1239.8419843320026
for n in[1,2,3,4,5]:
 K=13.60/n**2;U=-27.20/n**2;E=-13.60/n**2
 near('39Bohrsum n'+str(n),K+U,E)
 near('39Bohr virial relation n'+str(n),2*K+U,0,physical_scale=K)
near('39n2kinetic',13.60/4,3.40)
near('39n2potential',-27.20/4,-6.80)
near('39n1energy',-13.60,-13.60)
near('39n2to1photon',(-13.6/4)-(-13.6),10.2)
near('39n2to1wavelength',hc_eVnm/10.2,121.55313571882378)
near('39noninteger candidate from18',math.sqrt(18),4.24,tol=.001)
near('39candidate satisfies reciprocal square equation',1/math.sqrt(18)**2,1/18)
files=['chapter-23/01-the-nang-dien.md','chapter-25/04-suat-dien-dong.md',
 'chapter-35/03-cuong-do-giao-thoa.md','chapter-36/09-tom-tat.md','chapter-36/02-nhieu-xa-mot-khe.md',
 'chapter-39/03-muc-nang-luong-bohr.md']
result={'status':'passed-scoped-selected-theory-physics-checks','checks':len(records),'records':records,
 'sourceSHA256':{'raw_materials/physics/translations/'+p:hashlib.sha256((ROOT/'raw_materials/physics/translations'/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()for p in files},
 'scopeLimit':'Onlychanged expressions/steps for mobile presentation. This isnot a fullsource/content/image/exercise audit of thefive chapters.'}
(OUT/'numeric-checks.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS',len(records),'independent physical checks for selected theory repairs.')
