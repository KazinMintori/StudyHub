"""Actual-source numerical checks for exercises17.1–60."""
from pathlib import Path
import math,json
g=9.8;cw=4190.;ci=2100.;cal=4.186;Btu=1055.;Lf=334e3;Lv=2256e3
cAl=910.;cCu=390.;cFe=470.;cPb=130.;cAg=234.
aSt=1.2e-5;aAl=2.4e-5;aCu=1.7e-5;aBr=2e-5
bEt=75e-5;bSt=3.6e-5;bCu=5.1e-5
kCu=385.;kBr=109.;kSt=50.2
out={}
def save(number,**values):
 assert all(math.isfinite(x) for x in values.values()),number
 out[str(number)]=values
F=lambda C:1.8*C+32
C=lambda F:(F-32)/1.8
save(1,Fa=F(-62.8),Fb=F(56.7),Fc=F(31.1))
save(2,aC=310-273.15,aF=F(310-273.15),bK=40+273.15,bF=F(40),cKelvinDifference=7,cFDifference=7*1.8,d4K=277.15,d4F=F(4),dMinus160K=113.15,dMinus160F=F(-160),eC=C(105),eK=C(105)+273.15)
save(3,aDeltaC=(45-(-4))/1.8,bDeltaC=(-56-44)/1.8)
save(4,FKoffset=273.15-32/1.8,KFoffset=32-1.8*273.15)
save(5,deltaF=-18,deltaC=-10)
# Equality of the numerical scale readings.
fEqC=-40.;kEqF=(273.15-32/1.8)/(1-1/1.8)
save(6,CequalsF=fEqC,KequalsF=kEqF)
save(7,pressure_atm=1.35*195/273.16,roundedCO2Reference_K=195)
save(8,aC=400-273.15,aF=F(400-273.15),bC=95-273.15,bF=F(95-273.15),cC=1.55e7-273.15,cF=F(1.55e7-273.15))
slope=(6.5e4-4.8e4)/(100-.01)
save(9,linearSlope_Pa_C=slope,zeroPressureC=.01-4.8e4/slope,idealTriplePressure=6.5e4*273.16/373.15)
save(10,pressure_mmHg=325*373.15/273.16)
save(11,deltaL=aSt*1410*23)
save(12,deltaT=.471/(aSt*1671),finalC=15.5+.471/(aSt*1671))
save(13,hotDiameter_cm=1.9*(1+2.6e-5*28),coldDiameter_cm=1.9*(1+2.6e-5*(-73)))
save(14,warmDiameter_mm=4.5/(1+aAl*(-101)))
save(15,finalC=20+.0015/bCu)
V=2*pi*27.5**3/3 if (pi:=math.pi) else 0
save(16,initialV=V,additionalV=3*aAl*V*50)
save(17,glassBeta=18e-5-8.95/(1000*55))
save(18,extraV_m3=1.9*(bEt-bSt)*14)
A=pi*(.0135/2)**2;scale=1+aSt*150
save(19,initialArea_m2=A,finalArea_m2=A*scale**2,linearizedFinalArea_m2=A*(1+2*aSt*150))
save(20,firstOrderAreaCoefficientOverAlpha=2)
save(21,gap_m=aSt*12*42,compressionStress_Pa=-2e11*aSt*42)
save(22,tensileF=9e10*aBr*110*pi*(.016/2)**2)
save(23,LAlOverLInvar=2*.09e-5*3/aAl)
Q=.320*cw*60;save(24,Q=Q,time=Q/200)
save(25,Q=(1.1*cAl+1.8*cw)*65)
q=.5*1.3e-3*1020*57
save(26,perBreathQ=q,hourlyQ=q*20*60)
save(27,modelTime_s=70*3480*7/1200)
save(28,power_W=(9.46/60)*cw*(49-10))
save(29,c=1.25e4/((28.4/g)*18))
Q=.5*25000*15.5**2;ma=65*20*12*1.20
save(30,trainEnergy=Q,airMass=ma,airDeltaT=Q/(ma*1020))
save(31,waterDeltaT=g*225/cw)
save(32,nailDeltaT=10*.60*.5*1.8*7.8**2/(.008*cAl))
save(33,waterDeltaT=.5*.015*(865**2-534**2)/(13.5*cw))
save(34,hotWaterMass=.750*(75-10)/(100-75))
c=1*cw*2/(.5*(100-22));save(35,cMetal=c)
save(36,modelIceMass=70*3480*(37-32)/Lf)
save(37,waterMass=1.2*cFe*(650-120)/(cw*(100-15)+Lv))
hot=.750*cPb*255;latent=.018*Lf
Tf=(hot-latent)/(.750*cPb+.100*cCu+(.160+.018)*cw)
assert hot>latent and 0<Tf<100
save(38,Tfinal=Tf,availableFromLeadTo0=hot,iceMeltingQ=latent)
Tf=(.5*cCu*20+.170*cw*20+.250*cFe*85)/(.5*cCu+.170*cw+.250*cFe)
save(39,Tfinal=Tf)
save(40,hotWaterMass=.2*(ci*40+Lf+cw*28)/(cw*(80-28)))
save(41,copperInitialC=(2*ci*20+.8*Lf)/(6*cCu))
Q=.290*(cw*18+Lf);save(42,removedQ=Q,calories=Q/cal,Btu=Q/Btu)
Q=.018*(ci*10+Lf+cw*100+Lv);save(43,addedQ=Q,calories=Q/cal,Btu=Q/Btu)
m=.55;Pmin=800;t1=m*ci*15/Pmin;t2=t1+m*Lf/Pmin;Tf=(Pmin*500-m*ci*15-m*Lf)/(m*cw)
save(44,startMelting_min=t1,finishMelting_min=t2,temperatureAt500min=Tf,startsBoiling_min=t2+m*cw*100/Pmin)
save(45,speed=math.sqrt(2*(cPb*(327.3-25)+24.5e3)))
Qw=.025*cw*(100-34);Qs=Qw+.025*Lv
save(46,steamQ=Qs,waterQ=Qw,ratio=Qs/Qw)
save(47,evaporatedMass=400*3480*6/2.42e6,volume_L=400*3480*6/2.42e6)
mass=70*3480/2.42e6
save(48,evaporatedMass=mass,volume_cm3=mass*1000,canFraction=mass*1000/355)
Q=.01*.5*2.6e15*(32000)**2;mass=Q/(cw*90+Lv)
save(49,depositedQ=Q,vaporizedMass=mass,lakeMassFraction=mass/2e15)
c=(.15*cCu+.2*cw)*(26.1-19)/(.085*(100-26.1))
save(50,sampleC=c)
save(51,iceMass=.25*cw*(75-40)/(ci*20+Lf+cw*40))
save(52,iceMass=4*cAg*750/Lf)
save(53,liquidC=.027*(Lf+cw*14)/(.280*(30-14)))
Rb=.300/kBr;Rc=.800/kCu;H=.005*100/(Rb+Rc);T=H*Rc/.005
save(54,junctionC=T,heatCurrent=H,iceMass5min=H*300/Lf)
save(55,unknownK=kCu*(1/.710-1))
H=.0085*Lf/600
save(56,H=H,k=H*.60/(1.25e-4*100))
Rw=.03/.080;Rs=.022/.027;flux=(19-(-10))/(Rw+Rs);T=-10+flux*Rw
save(57,flux=flux,junctionC=T)
save(58,H=.040*1.4*(175-35)/.04,power=.040*1.4*(175-35)/.04)
save(59,glassK=.8,woodKLower=.04,woodKUpper=.12,copperK=385)
H=kCu*4e-4*(100-65);length=kSt*4e-4*65/H
save(60,H=H,steelLength=length)
assert len(out)==60
# Independent energy/magnitude checks for actual case data.
assert out['9']['zeroPressureC']<-270 and not math.isclose(out['9']['zeroPressureC'],-273.15)
assert out['21']['compressionStress_Pa']<0
assert out['44']['finishMelting_min']<500<out['44']['startsBoiling_min']
assert out['46']['steamQ']>8*out['46']['waterQ']
assert math.isclose(kBr*.005*(100-out['54']['junctionC'])/.3,out['54']['heatCurrent'])
assert -10<out['57']['junctionC']<19
assert math.isclose(kSt*4e-4*65/out['60']['steelLength'],out['60']['H'])
r=Path(__file__).resolve().parents[2]
p=r/'qa/physics1-priority/ch17-numbered-a-values.json'
p.write_text(json.dumps(dict(status='passed',cases=out,limitations=['Educational numerical models retain the problem assumptions; historical rankings and clinical storage/treatment statements are not presented as current guidance.','17.7 uses the explicitly rounded195K reference from the source scale diagram.']),ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
