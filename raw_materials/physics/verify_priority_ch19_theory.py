"""Actual source examples in chapter19, with independently checked identities."""
from pathlib import Path
import math,json
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2];Q=ROOT/'qa/physics1-priority';Q.mkdir(parents=True,exist_ok=True)
cases={}
def close(a,b,rel=1e-10):assert math.isclose(a,b,rel_tol=rel,abs_tol=1e-10),(a,b)
# 19.1 is symbolic. Test both expansion and compression against integration.
for j,(n,T,V1,V2) in enumerate([(1,300,.01,.03),(.4,450,.02,.005),(2,280,.4,.8)]):
 integral=quad(lambda V:n*8.314*T/V,V1,V2)[0]
 exact=n*8.314*T*math.log(V2/V1);close(integral,exact)
 cases[f'19.1_property_{j+1}']=dict(n=n,T=T,V1=V1,V2=V2,W=integral)
food=900*4186;height=food/(60*9.8)
cases['19.2']=dict(food_kcal=900,mass_kg=60,energy_J=food,idealHeight_m=height,mechanicalFraction=.25,modelHeight_m=.25*height)
close(.25*food+(.75*food),food)
cases['19.3']=dict(cycleDeltaU_J=0,W_J=-500,Q_J=-500,reverseW_J=500)
Qab=150;Wab=0;Qbd=600;Wbd=8e4*(5e-3-2e-3)
deltaU=Qab+Qbd-Wab-Wbd;Wacd=3e4*(5e-3-2e-3);Qacd=deltaU+Wacd
close(Wbd,240);close(deltaU,510);close(Wacd,90);close(Qacd,600)
cases['19.4']=dict(Qab=Qab,Wab=Wab,deltaUab=Qab-Wab,Qbd=Qbd,Wbd=Wbd,deltaUbd=Qbd-Wbd,Qabd=Qab+Qbd,Wabd=Wbd,deltaUabd=deltaU,Wacd=Wacd,Qacd=Qacd,deltaUacd=deltaU)
W=1.013e5*(1671-1)*1e-6;heat=.001*2.256e6
cases['19.5']=dict(mass_kg=.001,V1_m3=1e-6,V2_m3=1671e-6,pressure_Pa=1.013e5,W_J=W,Q_J=heat,deltaU_J=heat-W)
R=8.314;n=2500;gamma=1.4;T1=35;T2=26;CV=R/(gamma-1)
DU=n*CV*(T2-T1)
cases['19.6']=dict(n_mol=n,T1_C=T1,T2_C=T2,gamma=gamma,CV_J_mol_K=CV,deltaU_J=DU,W_J=n*R*(T2-T1),Q_J=n*(CV+R)*(T2-T1))
close(DU,-467662.5)
ratio=15;T1=300;p1=1.01e5;V1=.001
T2=T1*ratio**(gamma-1);p2=p1*ratio**gamma;V2=V1/ratio
work=(p1*V1-p2*V2)/(gamma-1)
n=p1*V1/(R*T1)
close(work,n*R/(gamma-1)*(T1-T2))
cases['19.7']=dict(compressionRatio=ratio,T1_K=T1,p1_Pa=p1,V1_m3=V1,T2_K=T2,T2_C_sourceRounded=T2-273,p2_Pa=p2,V2_m3=V2,work_J=work,n_mol=n)
# Using separately rounded CV20.8 versus gamma1.400 gives a rounding difference.
cases['19.7']['workUsingRoundedCV20_8_J']=n*20.8*(T1-T2)
assert work<0 and T2>T1 and p2>p1*ratio
cases['selfcheck19.7']=dict(n_mol=10,deltaT_K=-10,monatomicHeatRemoved_J=10*1.5*R*10,diatomicHeatRemoved_J=10*2.5*R*10)
cases['selfcheck19.8']=dict(isothermalPressureFactor=2,monatomicAdiabaticFactor=2**(5/3),diatomicAdiabaticFactor=2**1.4)
assert 2**(5/3)>2**1.4>2
cases['summary']=dict(Q_J=150,W_J=100,deltaU_J=150-100)
rows=[
 ('He',12.47,20.78,8.31,1.67),('Ar',12.47,20.78,8.31,1.67),
 ('H2',20.42,28.74,8.32,1.41),('N2',20.76,29.07,8.31,1.40),
 ('O2',20.85,29.17,8.32,1.40),('CO',20.85,29.16,8.31,1.40),
 ('CO2',28.46,36.94,8.48,1.30),('SO2',31.39,40.37,8.98,1.29),
 ('H2S',25.95,34.60,8.65,1.33)
]
for name,cv,cp,difference,gamma in rows:
 close(cp-cv,difference)
 assert abs(cp/cv-gamma)<.0051,(name,cp/cv,gamma)
cases['table19.1']=rows
(Q/'ch19-table19-1-verified.json').write_text(json.dumps(dict(status='passed',source='PDF647',rows=rows),ensure_ascii=False,indent=2),encoding='utf-8')
(Q/'ch19-theory-numerical-ledger.json').write_text(json.dumps(dict(status='passed',scope='Actual teaching examples and explicit symbolic property tests; source prose and browser are separate checks',cases=cases),ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(status='passed',cases=len(cases),example19_6=cases['19.6'],example19_7=cases['19.7']),ensure_ascii=False))
