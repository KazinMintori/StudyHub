"""Actual-case recomputation and requested plots for problems 9.49–9.95."""
from pathlib import Path
import contextlib,importlib.util,io,json,math,re,runpy,sys
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
import pymupdf
ROOT=Path(__file__).resolve().parents[2];Q=ROOT/'qa/physics1-priority'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-09'
Q.mkdir(parents=True,exist_ok=True);OUT.mkdir(parents=True,exist_ok=True)
with contextlib.redirect_stdout(io.StringIO()):
 previous=runpy.run_path(str(ROOT/'raw_materials/physics/verify_chapter09_exercises_e.py'))
cases=dict(previous['results']);g=9.8
def close(x,y,tol=1e-9):assert math.isclose(x,y,rel_tol=tol,abs_tol=tol),(x,y)
def save(n,**data):
 assert all(math.isfinite(x) for x in data.values() if isinstance(x,(float,int)))
 cases[f'9.{n}']=data
A=1.8/3;R=.25;t=math.sqrt(2*R*15/A)
save(61,A_m_s3=A,alphaCoefficient=A/R,t_s=t,theta_rad=A*t**3/(6*R))
omega=3*8;thickness=4*800/(8600*math.pi*.25**4*omega**2)
save(62,radius_m=.25,density_kg_m3=8600,omega_rad_s=omega,thickness_m=thickness)
a=.8*2*(8*2*math.pi)/5**2;m=2.5*a/(g-a)
save(63,a_m_s2=a,mass_kg=m)
initial=15*g*5;v=math.sqrt(2*(initial-250)/15)
save(64,earthTotal_J=initial,drumK_J=250,blockK_J=initial-250,MarsDrop_m=initial/(15*3.71),speed_m_s=v)
v=.2*8;mA=2*5*g*1.2/v**2-5-1.3/.2**2
save(65,speed_m_s=v,mA_kg=mA)
omega=2*3450*2*math.pi/60
save(66,blade_rpm=6900,omega_rad_s=omega,speed_m_s=.104*omega,radialAcceleration_m_s2=.104*omega**2)
save(67,frontRadius_m=.12,chainSpeed_m_s=.12*.6*2*math.pi,rearRadius_m=.12*.6*2*math.pi*.33/5)
t1=.0865/(math.sqrt(2)-1)
save(68,firstTurn_s=t1,alpha_rad_s2=4*math.pi/t1**2)
a=(1.5*g-9)/1.5;d=.5*a*2**2
save(69,a_m_s2=a,d_m=d,wheelK_J=9*d)
save(70,removedRadiusFraction=2**(-.25))
a=2*12/4**2;T=8.2*(g-a)
save(71,a_m_s2=a,tension_N=T,I_kg_m2=T*.32**2/a)
for R in [.04,.7,2.5]:
 m=.8;omega=math.sqrt(4*g/(3*R))
 close(.5*(.5*m*R**2+m*R**2)*omega**2,m*g*R)
save(72,omegaSquaredCoefficient=4*g/3)
omega=math.sqrt(3*g);tip=omega;free=math.sqrt(2*g)
save(73,deltaU_J=-.18*g*.5,omega_rad_s=omega,tip_m_s=tip,freeFall_m_s=free,tipOverFree=tip/free)
a=43*g/(43+9.6/.3**2)
save(74,a_m_s2=a,speed_m_s=math.sqrt(2*a*12),time_s=math.sqrt(24/a))
I=.12*.8**2/12+(.02+.05)*.4**2;drop=(.05-.02)*g*.4
save(75,I_kg_m2=I,potentialReleased_J=drop,omega_rad_s=math.sqrt(2*drop/I),sphereSpeed_m_s=.4*math.sqrt(2*drop/I))
for M,m,R,w0 in [(2,.3,.2,1),(.4,1,.08,4),(9,3,.7,0)]:
 w=math.sqrt(w0**2+4*math.pi*m*g/((M+2*m)*R))
 close(.5*(.5*M+m)*R**2*(w*w-w0*w0),m*g*math.pi*R)
save(76,symbolicEnergyIdentity=True,ropeLengthFactor=2*math.pi)
for mA,mB,mu,R,I,d in [(2,3,.2,.4,.5,1),(1,.7,.3,.2,.1,.8),(5,7,0,.1,2,2)]:
 v=math.sqrt(2*g*d*(mB-mu*mA)/(mA+mB+I/R**2))
 close(.5*(mA+mB+I/R**2)*v*v,(mB-mu*mA)*g*d)
save(77,symbolicEnergyIdentity=True)
v=math.sqrt(2*(4-2)*g*5/(4+2+.380/.160**2))
save(78,speed_m_s=v)
I=.5*.8*.025**2+.5*1.6*.05**2
v1=math.sqrt(2*1.5*g*2/(1.5+I/.025**2));v2=math.sqrt(2*1.5*g*2/(1.5+I/.05**2))
save(79,I_kg_m2=I,smallDiskSpeed=v1,largeDiskSpeed=v2)
E=.340*g*3-9;omega=math.sqrt(2*E/(.480+.340*.180**2))
assert E>0
save(80,availableK_J=E,omega_rad_s=omega)
v2=4*480/10;Kblock=.5*12*v2
save(81,speedSquared=v2,blockK_J=Kblock,drop_m=(480+Kblock)/(12*g))
save(82,effectiveMass_kg=3+5/2+2/2,speed_m_s=math.sqrt(2*3*g*2.5/(3+5/2+2/2)))
# An explicit illustrative body model, not a measurement of the reader.
M=60;Rh=.10;Rt=.13;s=.13;L=.65
head=.4*(.07*M)*Rh**2;torso=.5*(.80*M)*Rt**2
arms=.13*M*(s*s+s*L+L*L/3)
close(arms,2*(.065*M/L)*quad(lambda x:(s+x)**2,0,L)[0])
omega=72*2*math.pi/60;I=head+torso+arms
save(83,modelMass_kg=M,headMass_kg=.07*M,armsMass_kg=.13*M,torsoLegsMass_kg=.80*M,headRadius_m=Rh,torsoRadius_m=Rt,shoulderOffset_m=s,armLength_m=L,Ihead=head,Itorso=torso,Iarms=arms,Itotal=I,omega_rad_s=omega,K_J=.5*I*omega**2)
for a,M in [(.2,3),(2,.5),(1,7)]:
 single=(M/(4*a))*quad(lambda x:x*x+(a/2)**2,-a/2,a/2)[0]
 close(4*single,M*a*a/3)
save(84,frameCoefficient=1/3)
rho0=3000;beta=9000;R=.2
M=4*math.pi*quad(lambda r:(rho0-beta*r)*r*r,0,R)[0]
I=8*math.pi/3*quad(lambda r:(rho0-beta*r)*r**4,0,R)[0]
assert rho0-beta*R>0
close(M,4*math.pi*(rho0*R**3/3-beta*R**4/4))
close(I,8*math.pi/3*(rho0*R**5/5-beta*R**6/6))
save(85,mass_kg=M,I_kg_m2=I)
P=.0331;Pdot=4.22e-13;power=5e31;M=1.4*1.99e30
I=power*P**3/(4*math.pi**2*Pdot);R=math.sqrt(5*I/(2*M));v=2*math.pi*R/P;rho=M/(4*math.pi*R**3/3)
save(86,power_W=power,period_s=P,periodDerivative=Pdot,starMass_kg=M,I_kg_m2=I,radius_km=R/1000,speed_m_s=v,speedOverC=v/2.998e8,density_kg_m3=rho,densityOverRock=rho/3000,densityOverNucleus=rho/1e17)
tcube=(6*(2*2*math.pi)/1.2)**(1/3) # theta=(1.2/6)t^3
close(.2*tcube**3,4*math.pi)
save(87,alphaSlope_rad_s3=1.2,theta5_rad=.2*5**3,turns5=.2*5**3/(2*math.pi),omega5=.6*5**2,time2turns=tcube,omega2turns=.6*tcube**2)
theta=np.arange(.5,4.01,.5);acc=np.array([.678,1.07,1.52,1.98,2.45,2.92,3.39,3.87])
slope,intercept=np.polyfit(theta**2,acc**2,1)
alpha=math.sqrt(slope/(4*.8**2));speed=.8*math.sqrt(2*alpha*(135*math.pi/180))
phi=math.atan(2*math.pi/2)*180/math.pi
save(88,slope=slope,intercept=intercept,alpha_rad_s2=alpha,speed135_m_s=speed,angle90_deg=phi)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,ax=plt.subplots(figsize=(5,4),layout='constrained')
ax.scatter(theta**2,acc**2,label='Số liệu');xx=np.linspace(0,16,120);ax.plot(xx,slope*xx+intercept,label='Đường khớp')
ax.set(xlabel=r'$(\theta-\theta_0)^2$ (rad²)',ylabel=r'$a^2$ (m²/s⁴)');ax.legend();ax.grid(alpha=.25)
fig.savefig(OUT/'p-do-thi-9-88.png',dpi=180);plt.close(fig)
a=2*1.65;v=math.sqrt(2*a*1.5);R=.356/2;I=(2*5.6*g*1.5/v**2-5.6)*R**2;T=5.6*(g-a)
save(89,a_m_s2=a,speed_m_s=v,I_kg_m2=I,tension_N=T)
for R,h,M in [(.2,.6,2),(.8,.3,7),(.05,1,.3)]:
 rho=3*M/(math.pi*R*R*h)
 integral=quad(lambda z:.5*rho*math.pi*(R*z/h)**4,0,h)[0]
 close(integral,.3*M*R*R)
save(90,coneCoefficient=.3)
v=1.25;r0=.025;b=1.55e-6/(2*math.pi);tmax=74*60
D=lambda t:r0*r0+2*b*v*t
angle=lambda t:(np.sqrt(D(t))-r0)/b
omega=lambda t:v/np.sqrt(D(t))
alpha=lambda t:-b*v*v/D(t)**1.5
th=angle(tmax);close(r0*th+.5*b*th**2,v*tmax)
save(91,initialRadius_m=r0,pitch_m=1.55e-6,b_m_per_rad=b,playingTime_s=tmax,totalAngle_rad=float(th),turns=float(th/(2*math.pi)),outerRadius_m=float(math.sqrt(D(tmax))),omega0=float(omega(0)),omegaEnd=float(omega(tmax)),alpha0=float(alpha(0)),alphaEnd=float(alpha(tmax)))
times=np.linspace(0,tmax,400)
for name,values,ylabel in [('toc-do',omega(times),r'$\omega_z$ (rad/s)'),('gia-toc',alpha(times),r'$\alpha_z$ (rad/s²)')]:
 fig,ax=plt.subplots(figsize=(5,3.6),layout='constrained')
 ax.plot(times/60,values);ax.set(xlabel='Thời gian (phút)',ylabel=ylabel,xlim=(0,74));ax.grid(alpha=.25)
 fig.savefig(OUT/f'p-do-thi-9-91-{name}.png',dpi=180);plt.close(fig)
save(92,frameRotation_deg=14*360/120,answer='d')
save(93,alpha_rad_s2=22*2*math.pi/10,answer='d')
save(94,equivalentSpeed_m_s=.05*(14*2*math.pi)/math.sqrt(2),answer='c')
save(95,momentFactor=4,answer='d')
text=(ROOT/'raw_materials/physics/translations/chapter-09/12-bai-tap-049-095.md').read_text(encoding='utf-8')
ids=[int(n) for n in re.findall(r'^### 9\.(\d+)\s*$',text,re.M)]
complete=ids==list(range(49,96))
if '--complete' in sys.argv:assert complete,('Incomplete actual Markdown',ids)
report=dict(numericalStatus='passed',sourceDraftComplete=complete,coveredMarkdownIds=ids,expectedMarkdownIds=list(range(49,96)),cases=cases,generatedPlots=['p-do-thi-9-88.png','p-do-thi-9-91-toc-do.png','p-do-thi-9-91-gia-toc.png'])
(Q/'ch09-end-e-numerical-ledger.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(numericalStatus='passed',sourceDraftComplete=complete,actualMarkdownProblems=len(ids),expected=47,newCases={k:v for k,v in cases.items() if int(k.split('.')[1])>=61}),ensure_ascii=False,indent=2))
