"""Source-based numerical/model checks for all62 exercises in chapter20."""
from pathlib import Path
import math,json
import numpy as np
from scipy.integrate import quad
R=8.314462618;g=9.8;atm=101325.;cw=4190.;ci=2100.;Lf=334000.;Lv=2256000.;sig=5.670374419e-8
K=lambda t:t+273.15
out={}
def save(n,**v):
 assert all(math.isfinite(x) for x in v.values()),n
 out[str(n)]=v
def segment(p1,v1,p2,v2,kind,cv):
 du=cv*(p2*v2-p1*v1)
 if kind=='isochoric':w=0
 elif kind=='isobaric':assert math.isclose(p1,p2);w=p1*(v2-v1)
 elif kind=='isothermal':assert math.isclose(p1*v1,p2*v2);w=p1*v1*math.log(v2/v1);du=0
 elif kind=='adiabatic':w=-du
 elif kind=='linear':w=(p1+p2)/2*(v2-v1)
 else:raise ValueError(kind)
 return dict(Q=du+w,W=w,deltaU=du)
save(1,Qhot=2200+4300,efficiency=2200/6500)
save(2,W=9000-6400,efficiency=(9000-6400)/9000)
save(3,efficiency=3700/16100,Qcold=16100-3700,fuel_g=16100/46000,power_W=3700*60,power_hp=3700*60/746)
save(4,QhotRate=180e3/.28,QcoldRate=180e3/.28-180e3)
va,vb=.002,.009;pb=pc=1.5*atm;pa=pb*(vb/va)**1.4
segs={'ab':segment(pa,va,pb,vb,'adiabatic',2.5),'bc':segment(pb,vb,pc,va,'isobaric',2.5),'ca':segment(pc,va,pa,va,'isochoric',2.5)}
W=sum(s['W'] for s in segs.values());Qin=segs['ca']['Q'];Qout=-segs['bc']['Q']
assert math.isclose(W,Qin-Qout)
out['5']=dict(pa_Pa=pa,pa_atm=pa/atm,segments=segs,Qin=Qin,Qout=Qout,W=W,efficiency=W/Qin)
save(6,totalW=8000-.018*Lf)
eta=.63;save(7,compressionRatio=(1/(1-eta))**(1/.4),Qhot=12600/eta,Qcold=12600/eta-12600)
eta=1-9.5**(-.4);save(8,efficiency=eta,Qcold=10000*(1-eta))
e1=1-8.8**(-.4);e2=1-9.6**(-.4)
save(9,SLKeff=e1,Vipereff=e2,efficiencyIncrease=e2-e1,percentagePointIncrease=100*(e2-e1))
q=1.8*(cw*25+Lf+ci*5);w=q/2.4;save(10,Qcold=q,electricEnergy=w,roomHeat=q+w)
save(11,time_s=12*cw*(31-5)/(2.25*135))
save(12,workPerCycle=31000/2.10,Qhot=31000+31000/2.10)
th=72/.125;save(13,hotK=th,coldK=th-72)
qh=6450;qc=qh*300/520;save(14,Qcold=qc,W=qh-qc,efficiency=1-300/520)
save(15,W=550-335,coldK=620*335/550,efficiency=1-335/550)
qc=85*Lf;w=qc*(K(24)-K(0))/K(0);save(16,Qhot=qc+w,W=w)
save(17,Qhot=25000/.66,hotK=K(20)/(1-.66))
power=730e3/(365*5);cop=K(-5)/(K(20)-K(-5))
save(18,operatingPower_W=power,CarnotCOP=cop,maxIce0_kg_h=power*3600*cop/(cw*20+Lf),iceMinus5_kg_h=power*3600*cop/(cw*20+Lf+ci*5))
qc=415;w=qc*(320-270)/270;save(19,Qhot=qc+w,inputPower=w*165/60,COP=270/50)
qc=.04*Lf;save(20,W=qc*(373.15-273.15)/273.15)
save(21,coldA_K=1.16*180/1.3)
tf=(195*30+5*100)/200;ds=195*cw*math.log(K(tf)/K(30))+5*cw*math.log(K(tf)/K(100))
assert ds>0
save(22,finalC=tf,totalEntropy=ds)
q=.35*Lf;si=q/K(0);sh=-q/K(25);save(23,iceEntropy=si,sourceEntropy=sh,totalEntropy=si+sh)
sw=.25*cw*math.log(K(20)/K(85));sa=.25*cw*(85-20)/K(20);save(24,waterEntropy=sw,airEntropy=sa,totalEntropy=sw+sa)
save(25,gasEntropy=-1850/K(20))
save(26,heliumEntropy=-.130*20900/4.216)
save(27,vaporizationEntropy=Lv/K(100),meltingEntropy=Lf/K(0),ratio=(Lv/K(100))/(Lf/K(0)))
save(28,entropy=2*R*math.log(3),multiplicityLogRatioOverN=math.log(3))
save(29,entropy=.1*R*math.log(425/.0024))
W=15*g*2;eta=W/500;tc=K(500)*(1-eta)
save(30,W=W,coldK=tc,efficiency=eta,Qcold=500-W,pMax=2*R*K(500)/.005)
w=250*(1-K(100)/K(500));cycles=math.ceil(500*g*100/w)
save(31,Qcold=250*K(100)/K(500),workPerCycle=w,minimumIntegerCycles=cycles)
save(32,internalEntropyProductionRate=64*(1/K(30)-1/K(37)))
save(33,W=.22*410,Qcold=.78*410,coldK=K(135)*.78,worldEntropy=0,pumpedWaterMass=.22*410/(g*35))
n=.350;p1=atm;T1=300;T2=600;v1=n*R*T1/p1;p2=n*R*T2/v1
v3=v1*(p2/p1)**(1/1.4);T3=p1*v3/(n*R)
segs={'12':segment(p1,v1,p2,v1,'isochoric',2.5),'23':segment(p2,v1,p1,v3,'adiabatic',2.5),'31':segment(p1,v3,p1,v1,'isobaric',2.5)}
w=sum(s['W'] for s in segs.values());qin=segs['12']['Q']
assert math.isclose(sum(s['deltaU'] for s in segs.values()),0,abs_tol=1e-9)
out['34']=dict(v1=v1,v2=v1,v3=v3,p1=p1,p2=p2,p3=p1,T3exactAdiabatic=T3,sourceRoundedT3=492,segments=segs,W=w,netQ=sum(s['Q'] for s in segs.values()),efficiency=w/qin,CarnotEfficiency=1-T1/T2)
q=2.5*9.3*4186*.8;save(35,heatEnergy=q,internalEntropyTransport=q*(1/K(30)-1/K(37)))
save(36,W_over_p0V0=1,Qin_over_p0V0=9.5,efficiency=2/19)
segs={'ab':segment(2e5,.010,4e5,.005,'isothermal',2.5),'bc':segment(4e5,.005,4e5,.010,'isobaric',2.5),'ca':segment(4e5,.010,2e5,.010,'isochoric',2.5)}
w=sum(x['W'] for x in segs.values());qin=segs['bc']['Q']
out['37']=dict(Ta=2000/R,Tb=2000/R,Tc=4000/R,segments=segs,W=w,netQ=sum(x['Q'] for x in segs.values()),efficiency=w/qin)
mi=.0002*917;mw=.0002*1000;tf=K(22.2);t0=K(0);q=mi*Lf+(mi+mw)*cw*22.2
sm=mi*Lf/t0+(mi+mw)*cw*math.log(tf/t0);sa=-q/tf
save(38,chosenIceVolume_L=.2,chosenLiquidVolume_L=.2,iceMass=mi,waterMass=mw,mixtureEntropy=sm,airEntropy=sa,totalEntropy=sm+sa)
n=2;th=K(327);ta=th/3;nr=n*R
qin=nr*(1.5*(th-ta)+th*math.log(3));qout=nr*2.5*(th-ta);w=qin-qout
save(39,Ta=ta,Tb=th,Tc=th,Qin=qin,Qout=qout,W=w,efficiency=w/qin,CarnotEfficiency=1-ta/th)
eta=1-K(30)/K(37);w=2.5*g*1.2;qh=w/eta
save(40,efficiency=eta,requiredPotentialEnergy=w,Qhot=qh,candyBars=qh/(.8*350*4186))
eta=1-K(6)/K(27);qh=210e3/eta;qc=qh-210e3;mdot=qc/(cw*(10-6))
save(41,efficiency=eta,QhotRate=qh,QcoldRate=qc,coldFlow_kg_h=mdot*3600,coldFlow_L_h=mdot*3600)
segs={'ab':segment(3e5,.5,3e5,.8,'isobaric',1.5),'bc':segment(3e5,.8,1e5,.8,'isochoric',1.5),'ca':segment(1e5,.8,3e5,.5,'linear',1.5)}
w=sum(v['W'] for v in segs.values())
# For ca, instantaneous heat changes sign; distinguish net branchQ fromQin.
slope=(3e5-1e5)/(.5-.8);intercept=1e5-slope*.8
dq_dv=lambda v:2.5*(intercept+slope*v)+1.5*v*slope
vzero=-2.5*intercept/(4*slope)
qcaPos=quad(lambda v:max(-dq_dv(v),0),.5,.8)[0]
qcaNeg=quad(lambda v:max(dq_dv(v),0),.5,.8)[0]
qin=segs['ab']['Q']+qcaPos;qout=-segs['bc']['Q']+qcaNeg
assert math.isclose(qin-qout,w,rel_tol=1e-12)
out['42']=dict(segments=segs,W=w,netQ=sum(x['Q'] for x in segs.values()),deltaU=0,caHeatSignChangeVolume=vzero,caPositiveHeat=qcaPos,caRejectedHeat=qcaNeg,Qin=qin,Qout=qout,efficiency=w/qin,netBranchShortcutEfficiency=w/(segs['ab']['Q']+segs['ca']['Q']))
nr=2*atm*.004/300
states=[(2*atm,.004,300),(2*atm,.006,450),(nr*250/.006,.006,250),(nr*250/.004,.004,250)]
segs={}
for name,(i,j,kind) in zip(['12','23','34','41'],[(0,1,'isobaric'),(1,2,'isochoric'),(2,3,'isothermal'),(3,0,'isochoric')]):
 a,b=states[i],states[j];segs[name]=segment(a[0],a[1],b[0],b[1],kind,2.5)
w=sum(s['W'] for s in segs.values());qin=sum(max(s['Q'],0) for s in segs.values())
out['43']=dict(states=[dict(p=p,V=v,T=t) for p,v,t in states],segments=segs,W=w,efficiency=w/qin,CarnotEfficiency=1-250/450)
qh=1e9/.4;qc=qh-1e9;mass=qc/(cw*.5)
save(44,QhotRate=qh,coal_kg_day=qh*86400/2.65e7,QcoldRate=qc,riverVolume_m3_s=mass/1000,riverEntropyRate=mass*cw*math.log(K(18.5)/K(18)))
#45 cascade check with arbitrary actual temperatures.
th,tm,tc,qh=600,450,300,1000
w1=qh*(1-tm/th);qin2=qh-w1;w2=qin2*(1-tc/tm);assert math.isclose((w1+w2)/qh,1-tc/th)
save(45,testCompositeEfficiency=(w1+w2)/qh)
mpg=30;heatRate=(40/mpg)*120e6/3600;workRate=.2*heatRate
save(46,chosenMileage_mpg=mpg,combustionEnergyPer4StrokeCycle=heatRate/(3000/120),outputPower=workRate,outputHorsepower=workRate/746)
r=10.6;D=.0825;stroke=.0864;displacement=pi*D*D/4*stroke if (pi:=math.pi) else 0
va=displacement/(1-1/r);vb=va/r;pa=8.5e4;ta=300;nr=pa*va/ta;n=nr/R
tb=ta*r**.4;pb=pa*r**1.4;tc=tb+200/(n*20.5);pc=pb*tc/tb;td=tc/r**.4;pd=pa*td/ta
qc=200/r**.4;w=200-qc
out['47']=dict(displacement=displacement,n=n,states={'a':dict(p=pa,V=va,T=ta),'b':dict(p=pb,V=vb,T=tb),'c':dict(p=pc,V=vb,T=tc),'d':dict(p=pd,V=va,T=td)},W=w,Qcold=qc,efficiency=w/200,CarnotEfficiency=1-ta/tc,RimpliedByGivenCvGamma=.4*20.5)
vol=4*3*2.5;n=vol/.0224;N=n*6.02214076e23
save(48,chosenRoomVolume=vol,moles=n,molecules=N,approxEntropy=1.380649e-23*N*math.log(N))
pa=.7*atm;va=.03;vb=.1;pb=pa*va/vb;pc=pa
segs={'ab':segment(pa,va,pb,vb,'isothermal',2.5),'bc':segment(pb,vb,pc,vb,'isochoric',2.5),'ca':segment(pc,vb,pa,va,'isobaric',2.5)}
win=-sum(v['W'] for v in segs.values());qabs=sum(max(v['Q'],0) for v in segs.values())
out['49']=dict(segments=segs,workInput=win,totalAbsorbedHeat=qabs,cycleHeatAbsorptionCOP=qabs/win,isothermalOnlyRatio=segs['ab']['Q']/win,Ta=pa*va/(.85*R),Tc=pc*vb/(.85*R))
h=sig*1.85*(K(30)**4-K(20)**4);save(50,netHeatRate=h,airEntropyRate=h/K(20))
#51 exact derivative and concavity tests using physical heat capacities.
c1,c2,t1,t2=100,200,280,350;teq=(c1*t1+c2*t2)/(c1+c2)
second=-c1/teq**2-c1**2/(c2*teq**2);assert second<0
save(51,testEquilibriumK=teq,secondDerivativeAtEquilibrium=second)
q=.25*cw*(78-20);sw=.25*cw*math.log(K(78)/K(20));sh=-q/K(120)
save(52,waterEntropy=sw,idealSourceEntropy=sh,totalEntropy=sw+sh,Q=q)
protos={}
for label,tc,th,claim in [('A',47,177,.21),('B',17,197,.35),('C',-33,247,.56),('D',37,137,.20)]:
 em=1-K(tc)/K(th);protos[label]=dict(Carnot=em,claimed=claim,possible=claim<=em,ratio=claim/em)
out['53']=protos
eerFactor=3600/1055;cop=K((80-32)/1.8)/(K((95-32)/1.8)-K((80-32)/1.8))
cost=lambda eer:1.9e10/(eer/eerFactor)/3.6e6*.153
save(54,EERperCOP=eerFactor,CarnotCOP=cop,CarnotEER=cop*eerFactor,annualCostEER10point9=cost(10.9),annualCostEER14point6=cost(14.6),annualSavings=cost(10.9)-cost(14.6))
def rectangle(ta,tb,tc,td):
 qin=1.5*(tb-ta)+2.5*(tc-tb);w=(tc-tb)+(ta-td)
 return w/qin
save(55,efficiency=rectangle(250,300,380,316.7),doubleMolesEfficiency=rectangle(250,300,380,316.7),doubleRightVolumesEfficiency=rectangle(250,300,760,633.4),limitingEfficiency=1/15)
save(56,power_W=1*R*(K(100)-K(20))*math.log(10)*100,expansionWork=R*K(100)*math.log(10),compressionWork=-R*K(20)*math.log(10))
th=123*2**.3;eta=1-123/th;vc=4*pi*.08**3/3;ambient=20300*vc*123/(th*(54*vc))
save(57,combustionK=th,ambientPressure=ambient,efficiency=eta,Qhot_J_min=1000/eta,Qcold_J_min=1000/eta-1000)
ta,tc,gamma,r=300,950,1.4,21.;tb=ta*r**(gamma-1);cut=tc/tb;td=tc*(cut/r)**(gamma-1)
formal=1-(td-ta)/(gamma*(tc-tb))
save(58,Tb=tb,cutoffRatio=cut,Td=td,formalAlgebraicRatio=formal,positiveHeatInputExists=0,maximumRForHeating=(tc/ta)**(1/(gamma-1)))
save(59,requiredColdC=K(27)*(1-.065)-273.15,sourceGraphDepthChoice_m=400)
save(60,ammoniaEntropyRate=(10e6/.065)/K(27))
save(61,hotAndColdReservoirEntropyMagnitudesEqual=1,workingSubstanceCycleEntropy=0)
save(62,actualEfficiency=10/(10+165))
assert list(out)==[str(n) for n in range(1,63)]
root=Path(__file__).resolve().parents[2];p=root/'qa/physics1-priority/ch20-numbered-parent-values.json'
p.write_text(json.dumps({'status':'passed','cases':out,'limitations':['42 heat changes sign during straightca; true total absorbedheat differs from positive net-branch shortcut.','47 givenCv andgamma are rounded and not exactly consistent with the exact gas constant.','49 COP defined as total heat absorbed over the drawn cycle; assigning a single cold reservoir requires extra thermal-contact information.','52 treats the constant-temperature element as an ideal heat source; electrical supply and detailed element state require a different system boundary.','55 measured temperatures are rounded and not exactly consistent with a geometrically exact rectangle.','58 suppliedTa,Tc,gamma,r implyTb>Tc, so the stated numerical data do not define a positive-heat-input Diesel cycle.','All clinical/food-energy/price contexts are fixed educational input assumptions, not current real-world advice.']},ensure_ascii=False,indent=2),encoding='utf-8')
print('Checked62 source-numbered exercises, actual cycle integrals and model limitations.')
for n in [5,34,37,39,42,47,49,54,55,57,58,59]:print(n,out[str(n)])
