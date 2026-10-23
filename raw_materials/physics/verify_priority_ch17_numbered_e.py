"""Actual numerical and analytical checks for source exercises17.61–119."""
from pathlib import Path
import math,json
import numpy as np
from scipy.integrate import quad
g=9.8;pi=math.pi;sig=5.670374419e-8
cw,ci,cCu,cFe,cAl=4190.,2100.,390.,470.,910.
Lf,Lv=334000.,2256000.
aSt,aBr,aCu=1.2e-5,2e-5,1.7e-5
kSt,kCu,kBr,kAir=50.2,385.,109.,.024
C=lambda x:x+273.15
out={}
def save(n,**v):
 assert all(math.isfinite(x) for x in v.values()),n
 out[str(n)]=v
H=.390*Lv/180
save(61,H=H,bottomC=100+H*.0085/(kSt*.150))
A=190*.5/(kSt*300);save(62,area=A,diameter=math.sqrt(4*A/pi))
A=1.4*2.5;Rglass=.0052/.8;Rpaper=.000750/.050
save(63,bareHeatCurrent=A*39.5/Rglass,paperHeatCurrent=A*39.5/(Rglass+Rpaper))
save(64,flux273=sig*273**4,flux2730=sig*2730**4)
save(65,area=150/(.35*sig*2450**4))
save(66,power=.35*sig*4*pi*.015**2*(3000**4-290**4))
R1=math.sqrt(2.7e32/(4*pi*sig*11000**4));R2=math.sqrt(2.1e23/(4*pi*sig*10000**4))
save(67,RigelRadius=R1,ProcyonBRadius=R2,RigelOverEarth=R1/6.37e6,RigelOverSun=R1/6.96e8,RigelOverAU=R1/1.5e11,ProcyonOverEarth=R2/6.37e6,ProcyonOverSun=R2/6.96e8,ProcyonOverAU=R2/1.5e11)
# Diagram-based approximate parabola, with coefficients stated as estimates from figure17.12.
A=1.00003;B=7.5e-6
vals={str(t):2*B*(t-4)/(A+B*(t-4)**2) for t in [1,4,7,10]}
save(68,parabolaA_cm3=A,parabolaB_cm3_C2=B,**{'beta'+t:value for t,value in vals.items()})
save(69,contactC=20+.002/(aSt*10.5+aBr*.35))
mass=.0025;L=.4;rho=7800;mu=mass/L;T1=(2*L*440)**2*mu;T2=(2*L*460)**2*mu;A=mass/(rho*L)
save(70,T1=T1,T2=T2,area=A,finalC=20-(T2-T1)/(2e11*A*aSt))
#71: Recovering heat capacity fromQ,rho,beta and measured volume change.
rho,beta,V,c,dt=800,7e-4,.002,2000,15
Q=rho*V*c*dt;dv=beta*V*dt;assert math.isclose(Q*beta/(rho*dv),c)
save(71,dimensionfulTestRecoveredC=Q*beta/(rho*dv))
ratio=math.sqrt(1+aCu*200)
save(72,periodIncreasePercent=(ratio-1)*100,firstOrderPercent=.5*aCu*200*100)
save(73,waterBoil_M=(100+39)/396*100,tenM_inC=39.6)
s=1+aCu*40
save(74,frequencyChange=440*(s**(-.5)-1),waveSpeedChangePercent=(math.sqrt(s)-1)*100,wavelengthChangePercent=(s-1)*100)
save(75,spillC=22+.03/(.97*6.8e-4-2.7e-5))
save(76,trueLength=25.970*(1+aSt*(5-20)))
aa=.065/(30*100);ab=.035/(30*100);LA=(.058/100-ab*30)/(aa-ab)
save(77,alphaA=aa,alphaB=ab,lengthA_cm=LA,lengthB_cm=30-LA)
R=.05;rho=8900;m=rho*4*pi*R**3/3;A=4*pi*R**2;H=sig*A*300**4
save(78,time_s=m*cCu/H,fractionalHeatCurrentChange=(299/300)**4-1,initialPower=H)
save(79,steelTensileStress=2e11*(aBr-aSt)*120)
# General equation79a and wave-speed coefficient80, checked with actual dimensionful test parameters.
Y,rho,alpha,dt,s1=2e11,7800,1.2e-5,5,8e7
s2=s1-Y*alpha*dt;v1=math.sqrt(s1/rho);v2=math.sqrt(s2/rho)
assert math.isclose(rho*(v1*v1-v2*v2)/(Y*dt),alpha)
save(80,recoveredAlpha=rho*(v1*v1-v2*v2)/(Y*dt))
ring=2.5;shaft=2.502
save(81,ringWarmC=20+(shaft/ring-1)/aSt,slipOffC=20+(shaft-ring)/(ring*aSt-shaft*aBr))
Ekcal=(2+17)*4+7*9;E=Ekcal*4186
save(82,energy_kcal=Ekcal,exerciseTime_min=Ekcal/510*60,speed_m_s=math.sqrt(2*E/60),speed_km_h=math.sqrt(2*E/60)*3.6)
save(83,liquidC=2.15*cw/(90*.05))
Qiron=.1*cFe*(745-100);Qwater=.085*cw*(100-20);vap=(Qiron-Qwater)/Lv
assert 0<vap<.085
save(84,finalC=100,ironMass=.1,waterRemaining=.085-vap,vaporizedWater=vap)
n,k,theta,T1,T2=1.5,1940,281,10,40
Q=n*k*(T2**4-T1**4)/(4*theta**3)
assert math.isclose(Q,quad(lambda T:n*k*T**3/theta**3,T1,T2)[0])
save(85,Q=Q,averageMolarC=Q/(n*(T2-T1)),C40=k*T2**3/theta**3)
D,L=.15,.50;A=pi*D*L+pi*D**2/2
save(86,estimatedDiameter=D,estimatedLength=L,totalSurfaceArea=A,netRadiation=sig*A*(C(700)**4-C(20)**4))
Q=140*100*50*60;Ca=3200*1.2*1020
save(87,lectureQ=Q,lectureAirRise=Q/Ca,examAirRise=2.8*Q/Ca)
n=3;T1=C(27);T2=C(227);a=29.5;b=8.20e-3
Q=n*(a*(T2-T1)+b*(T2**2-T1**2)/2)
assert math.isclose(Q,quad(lambda T:n*(a+b*T),T1,T2)[0])
save(88,Q=Q)
H=.80*500;mass=H*3600/2.42e6
save(89,evaporated_kg_h=mass,bottles750ml_h=mass/.75)
dT=H*3600/(70*3480)
save(90,bodyRise=dT,equivalentFinal_F=98.6+1.8*dT)
save(91,reactionHeat_J_kg=cw*80+.5*19**2,sensiblePart=cw*80,sprayKineticPart=.5*19**2)
P=.7*25*30*2*pi/60
save(92,usefulPower=P,meltTime_s=3*Lf/P,additionalWarmTime_s=9*cw*10.5/P)
Qwarm=.600*ci*22;Qwater=1.5*cw*28;melt=(Qwater-Qwarm)/Lf
assert 0<melt<.6
save(93,finalC=0,remainingIce=.6-melt,meltedMass=melt)
Cwarm=2*cw+.257*cAl
Tf=(Cwarm*20-.120*(ci*15+Lf))/(Cwarm+.120*cw)
assert 0<Tf<20
save(94,finalC=Tf)
ms,mi,mc=.035,.095,.446
Tf=(ms*(Lv+cw*100)-mi*Lf)/(mc*cCu+(ms+mi)*cw)
assert 0<Tf<100
save(95,finalC=Tf,iceMass=0,liquidMass=ms+mi,steamMass=0)
added=(.884-.450)*Lf/(Lf+ci*15);freeze=.884-.450-added
assert added>0 and freeze>0 and math.isclose(added*ci*15,freeze*Lf)
save(96,addedIce=added,originalWaterFreezing=freeze)
cond=.2*cw*(100-50)/Lv
assert 0<cond<.04
save(97,finalC=100,steamMass=.04-cond,liquidMass=.2+cond)
# Thin-layer approximation used for initial model, plus spherical check to quantify geometry sensitivity.
A=4*pi*.75**2;Tj=31-50*.04/(.20*A);Lair=.024*A*(Tj-2.7)/50
Rf=(1/.71-1/.75)/(4*pi*.20);Tjs=31-50*Rf
rout=1/(1/.75-4*pi*.024*(Tjs-2.7)/50)
save(98,thinLayerBoundaryC=Tj,thinLayerAirThickness=Lair,sphericalBoundaryC=Tjs,sphericalAirThickness=rout-.75)
A=2*.95;Rwood=(.05+.018)/.12;Rg=(.0045+.120)/.8
H0=A*28/Rwood;Hw=(A-.25)*28/Rwood+.25*28/Rg
save(99,solidDoorHeat=H0,windowDoorHeat=Hw,increaseFactor=Hw/H0)
#100: Basic scalar thermal-stress approximation; full multiaxial model needsPoisson's ratio.
r,d,mu,Y,alpha,T,M=.02,.1,.4,7e10,2e-5,30,2
p=Y*alpha*T;maxm=2*pi*r*d*mu*p/g-M
assert math.isclose(mu*p*2*pi*r*d,(M+maxm)*g)
save(100,testMaxContainerMass=maxm,testPressure=p)
Rsingle=.0042/.8+.15;Rdouble=2*.0042/.8+.007/.024+.15
save(101,singleToDoubleHeatRatio=Rdouble/Rsingle)
gc=kCu/.13;gb=kBr/.18;gs=kSt/.24;T=100*gc/(gc+gb+gs);A=2e-4
hc=gc*A*(100-T);hb=gb*A*T;hs=gs*A*T
assert math.isclose(hc,hb+hs)
save(102,junctionC=T,copperCurrent=hc,brassCurrent=hb,steelCurrent=hs)
met=.8*1300;rad=sig*1.85*(C(40)**4-C(33)**4);H=met+rad
save(103,metabolicHeat=met,netRadiationGain=rad,totalHeat=H,evaporation_kg_min=H*60/2.42e6,bottles750ml_halfHour=H*1800/2.42e6/.75)
H=sig*2*(C(30)**4-C(18)**4)
save(104,netRadiation=H,basalPower=H/.8)
rhoi=917.;ki=1.6
t25=rhoi*Lf*.25**2/(2*ki*10);t40=rhoi*Lf*40**2/(2*ki*10)
save(105,time25cm_s=t25,time25cm_days=t25/86400,time40m_years=t40/(365.25*86400))
flux=1500*(1.5e11/6.96e8)**2
save(106,surfaceFlux=flux,surfaceT=(flux/sig)**.25)
R=.09/2;L=.25;A=2*pi*R*L+2*pi*R**2;H=.2*sig*A*(77.3**4-4.22**4)
save(107,area=A,heatCurrent=H,boiloff_kg_h=H*3600/2.09e4)
A=4*pi*.032**2;eps=.660/(sig*A*(C(41)**4-C(30)**4));P82=eps*sig*A*(C(82)**4-C(30)**4)
save(108,emissivity=eps,power82=P82,ratio=P82/.660)
save(109,meltingT_C=10,latentHeat=10000*1.5/.5,cSolid=10000*1/(.5*15),cLiquid=10000*1.5/(.5*30))
#110: Solve the two independent energy balances rather than average final temperatures.
A=np.array([[.5*(58.1-20),.2*(58.1-20)],[1*(49.3-20),.2*(49.3-20)]])
b=np.array([.5*cw*(80-58.1),.5*cw*(80-49.3)])
cl,cc=np.linalg.solve(A,b);assert np.allclose(A@np.array([cl,cc]),b)
save(110,liquidC=float(cl),cupC=float(cc))
H=(.300-.191)*Lf/(45*60);ka=H*.4/(2.5e-4*100);kb=ka*(100-62.4)/62.4
save(111,measuredHeatCurrent=H,kA=ka,kB=kb,actualCompositeLength_m=.8)
save(112,propaneDuration_min=18*25.6e6*.30/(.5*Lf),propaneDuration_h=18*25.6e6*.30/(.5*Lf)/60)
#113: Frustum resistance integral, including unequalR and equalR limit.
k,L,R1,R2=100.,.5,.02,.06
res=quad(lambda x:1/(k*pi*(R1+(R2-R1)*x/L)**2),0,L)[0]
assert math.isclose(res,L/(k*pi*R1*R2))
save(113,testResistance=res,closedFormResistance=L/(k*pi*R1*R2))
A=1.5;conv=54/3600*A*(47-36);sun=1400*A;rad=sig*A*(C(47)**4-C(36)**4);H=280+conv+sun+rad
Ac=.45;Hc=280+(conv+sun+rad)*Ac/A
save(114,metabolic=280,convection=conv,solar=sun,environmentNetRadiation=rad,totalHeat=H,evaporation_L_h=H*3600/2.42e6,protectedHeat=Hc,protectedEvaporation_L_h=Hc*3600/2.42e6)
#115: Cylindrical thermal resistances in series, with actualr andk.
R1=math.log(.04/.02)/(.04*2*pi*2);R2=math.log(.06/.04)/(.027*2*pi*2);H=(140-15)/(R1+R2);Tj=140-H*R1
assert math.isclose(H,(Tj-15)/R2)
# General logarithmic heat-flow integral checked separately.
a,b,k,L=.02,.06,.04,2
res=quad(lambda rad:1/(2*pi*k*L*rad),a,b)[0]
assert math.isclose(res,math.log(b/a)/(2*pi*k*L))
save(115,junctionC=Tj,heatCurrent=H,testIntegralResistance=res)
Q=.035*(4500*(22-(-20))+2.8e5+2000*((-20)-(77-273.15)))
save(116,removedQ=Q,option=2)
#117: Sourcegraph has solidc below tabular2000 over most of77Kto253K.
slope=(2000-1100)/180
qactual=.035*quad(lambda tc:1100+slope*(tc+200),77-273.15,-20)[0]
qconstant=.035*2000*((-20)-(77-273.15))
assert qactual<qconstant
save(117,illustrativeGraphSolidHeat=qactual,tabularSolidHeat=qconstant,shorterTime=1)
save(118,thicknessFactor=4)
save(119,roomLeakRaisesMeasuredHeatCapacity=1)
assert list(out)==[str(n) for n in range(61,120)]
root=Path(__file__).resolve().parents[2];p=root/'qa/physics1-priority/ch17-numbered-e-values.json'
p.write_text(json.dumps({'status':'passed','cases':out,'limitations':['68 coefficients and117 heat-capacity slope are approximate readings of the original graphs, not exact measured constants.','98 thin-layer and spherical models are explicitly distinguished.','100 scalar thermal-stress model omits lateral strain coupling; a full multiaxial solution requires additional material data.','105 ignores later boundary-condition changes;114 uses the exposed-area radiation model specified in the problem.','111 contains a printed80.0m composite-length typo; two40cm bars give0.800m.']},ensure_ascii=False,indent=2),encoding='utf-8')
print('Checked59 actual-source exercises; values and model limitations saved to',p)
for n in [68,70,75,84,93,95,96,97,98,105,108,109,110,111,114,115,116]:print(n,out[str(n)])
