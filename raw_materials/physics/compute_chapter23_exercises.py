from pathlib import Path
from math import sqrt,pi,sin,cos,log,atan2,degrees,exp
import json
root=Path(__file__).resolve().parents[2]
k=8.987551787e9;e=1.602176634e-19;mp=1.672621898e-27;me=9.10938356e-31;eps=1/(4*pi*k)
a={}
a['23.1']=k*2.40e-6*(-4.30e-6)*(1/.15-1/sqrt(.25**2+.25**2))
a['23.2']=5.4e-8+1.9e-8
a['23.3']=[3*k*e*e/(2e-15),3*k*e*e/(2e-15)/e/1e6]
W=k*e*e*(1/3e-15-1/2e-10);a['23.4']=[W,sqrt(W/mp)]
C=k*2.80e-6*7.80e-6;Ei=.0015*22**2/2+C/.8
a['23.5']=[sqrt(2*(Ei-C/.4)/.0015),C/Ei]
U=k*e*e*(-1/.17e-9+1/.28e-9-1/.19e-9+1/.30e-9)
a['23.6']=[U,-k*e*e/.0529e-9]
r=k*e*e/(mp*(2e5)**2);a['23.7']=[r,k*e*e/r**2]
a['23.8']=3*k*(1.2e-6)**2/.4
a['23.9']=[sqrt(k*e*e/(mp*.75e-9)),k*e*e/(mp*(.75e-9)**2)]
a['23.10']=8*k*e*e/(10e-9)*(sqrt(2)-1-1/sqrt(5))
a['23.11']=600*(.03-.02)+5*(1/.02-1/.03)
a['23.12']=[30-3e-7/(-6e-9),-100]
a['23.13']=sqrt(5**2+2*(-5e-6)*(200-800)/2e-4)
a['23.14']=[2.2e-6,2.2e-6/(4.2e-9),2.2e-6/(4.2e-9*.06)]
a['23.15']=[0,28e-9*4e4*.67,-28e-9*4e4*2.6/sqrt(2)]
dV=k*(3e-9/.1+2e-9/.4-5e-9/.25);a['23.16']=sqrt(2*e*dV/me)
Vb=k*2e-6*(1/(.03*sqrt(2))-1/.03);a['23.17']=[0,Vb,(-5e-6)*(0-Vb)]
Va=k*(2.4e-9/.05-6.5e-9/.05);Vb=k*(2.4e-9/.08-6.5e-9/.06);a['23.19']=[Va,Vb,2.5e-9*(Vb-Va)]
a['23.20']=[me*(8e6**2-3e6**2)/(2*e),-me*(8e6)**2/(2*e)]
a['23.21']=[-12/.07,12/.07*(.15-.05)]
r=4.98/16.2;a['23.22']=[r,4.98*r/k]
a['23.23']=[800,-.2e-6*240]
a['23.24']=[(-5e-4)/(-5e-6),250]
W=-(-.2e-6)*k*12e-6/.4;a['23.25']=[W,sqrt(2*W/.012)]
a['23.26']=18/k
potential27=lambda r:k*(6e-9/max(r,.03)-9e-9/max(r,.05))
a['23.27']=[potential27(r) for r in [0,.04,.06]]+[potential27(.03)-potential27(.05)]
a['23.28']=[k*3.5e-9/max(r,.24) for r in [.48,.24,.12]]
dV=k*24e-9*(1/.15-1/sqrt(.3**2+.15**2));a['23.29']=sqrt(2*e*dV/me)
a['23.30']=24*1.2/.4
a['23.31']=sqrt(2*k*5e-6*3e-6/(6e-5*.2))
K=mp*3.5e3**2/2;a['23.32']=[K,.18*exp(-K/(2*k*5e-12*e))]
a['23.33']=[2*k*8.5e-6*log(.1/.06),0]
a['23.34']=.025*(exp(175/(2*k*15e-9))-1)
a['23.35']=8e-6*2*k*3e-6*log(.045/.015)
a['23.36']=[47e-9/eps,47e-9/eps*.022]
a['23.37']=[360/.045,2.4e-9*360/.045,2.4e-9*360]
a['23.38']=1.5/1e-6
a['23.39']=-3800*.2
a['23.40']=[3750*.125/k,3750]
a['23.42']=2*eps/(6e-9)
Ex=-2*5*2*.4+8*.4**2;Ey=-5*2**2+2*8*2*.4
a['23.44']=[Ex,Ey,sqrt(Ex*Ex+Ey*Ey),degrees(atan2(Ey,Ex))%360]
q=500/(k*(1/.012-1/.096));a['23.45']={'q':q,'radii':{V:1/(1/.096+V/(k*q)) for V in [500,400,300,200,100,0]}}
C=k*5e-6*2e-6;Etotal=.004*40**2/2+C/.06
r=C/(Etotal-.004*25**2/2);a['23.46']=[r,C/r**2/.004]
a['23.47']=[k*(-60+8/.1-6/.1)*1e-18,(26-sqrt(26**2-4*60*1.6))/(2*60)]
a['23.48']=[.2*(3+2*sqrt(2)),.2/3,.6]
a['23.49']=2*k*5e-6*log(.2/.3)+8e-6/(2*eps)*.5
acc=9.8-7e-6*8e-12/(2*eps*5e-7);a['23.50']=[acc,sqrt(2*acc*.3)]
a['23.51']=k*79*e/(7.3e-15+2e-14)
U=2*k*e*e/(.225e-9);vp=sqrt(8*U/(5*mp));ap=2*k*e*e/(mp*(.225e-9)**2)
a['23.52']=[vp,vp/4,ap,ap/4]
We=4.35e-5-6.50e-5;a['23.53']=[We,We/(7.6e-9),abs(We)/(7.6e-9*.08)]
a['23.54']=[sqrt(2)*k*5e-6*3e-6/.08**2,0,2*k*5e-6*3e-6/.08*(sqrt(2)-1)]
C=240/.013**(4/3);Ehalf=4*C/3*(.013/2)**(1/3);a['23.55']=[C,4*C/3,e*Ehalf]
gap=.001;area=1e-4;sig=eps*3e6;Q=sig*area;a['23.56']=[gap,3e6*gap,sig,area,Q,Q/e]
points=[(x,y,z) for x in [0,1] for y in [0,1] for z in [0,1]]
signs=[(-1)**sum(p) for p in points];U=0
for i in range(8):
 for j in range(i+1,8):U+=signs[i]*signs[j]/sqrt(sum((points[i][t]-points[j][t])**2 for t in range(3)))
a['23.57-coefficient']=U
height=8;lam=22e3/(2*k*log(height/.02));a['23.58']=[height,lam,2*k*lam/height]
a['23.59']=.0015*9.8*(1/sqrt(3))/8.90e-6*.05
a['23.60']=[k*(3e-6/max(r,.05)-5e-6/max(r,.15)) for r in [.025,.1,.2]]
a['23.62']=2e4*.012*log(.018/(145e-6))
E=22/.02;ac=e*E/me;t=.06/6.5e6;vy=ac*t;yp=.5*ac*t*t
a['23.63']=[e*E,ac,yp,degrees(atan2(vy,6.5e6)),yp+vy*.12/6.5e6]
E=25/.005;a['23.64']=[eps*E*.03**2,E,sqrt(2*e*25/me)]
rw=90e-6;rc=.14;E=5e4/(log(rc/rw)*(rc+rw)/2);a['23.65']=[E,10*30e-9*9.8/E]
a['23.69']=k*4e-6/(2*.05)
R=.650e-3;Q=-3.6e-12;Vp=k*Q/R;a['23.70']=[Vp,2**(1/3)*R,2**(2/3)*Vp]
spring=k*e*e/(1e-15)**3;U=1.5*k*e*e/1e-15
a['23.73']=[spring,U/e/1e6,sqrt(U/mp),sqrt(k*e*e/(mp*1e-15))]
head=k*164*e*e/(9.5e6*e);a['23.75']=head
A=6e-5/(1.5e-6*.25**2);a['23.76']=[A,-2*A*.25,sqrt(1280/A+3*2**2)]
def potential77(x,y,z):return -6*x*x-4*y**3-2*z**6+10
def field77(x,y,z):return [12*x,12*y*y,12*z**5]
a['23.77']=[{'point':p,'V':potential77(*p),'E':sqrt(sum(v*v for v in field77(*p)))} for p in [(0,0,0),(.5,.5,.5),(1,1,1)]]
a['23.78']=[20,15.75*4e-4/(2*k*5e-8),15.75/400]
visc=1.81e-5;density=824;d=.001
Vs=[9.16,4.57,12.32,6.28];speeds=[2.54e-5,.767e-5,4.39e-5,1.52e-5]
qs=[18*pi*d/V*sqrt(visc**3*speed**3/(2*density*9.8)) for V,speed in zip(Vs,speeds)]
ns=[3,1,5,2];es=[q/n for q,n in zip(qs,ns)];a['23.79']={'chargeMagnitudes':qs,'electronCounts':ns,'eEstimates':es,'mean':sum(es)/4}
Vo=2*k*1e-6/(.05+.1);a['23.80']=[Vo,sqrt(2*1e-6*Vo/.001)]
cap=2*pi*eps*100e-6/log(10/9);a['23.81']=[cap*.09,.09/(9e-6*log(10/9)),cap*.11,cap*.11/e]
a['23.83']=[(head+sqrt(head*head+4*b*b))/2 for b in [1e-12,1e-13,1e-14]]
for b,r in zip([1e-12,1e-13,1e-14],a['23.83']):
 assert abs(head/r+b*b/(r*r)-1)<1e-12
a['23.84']=3e6/3
a['23.85-min-Z']=3e6*e*10e-15/(2*k*e*e)
a['23.86']=6e6/12
out=root/'qa/physics/chapter23';out.mkdir(parents=True,exist_ok=True)
(out/'exercise-calculations.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(a,ensure_ascii=False,indent=2))
