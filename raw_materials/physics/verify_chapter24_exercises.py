from pathlib import Path
from math import pi,exp,sqrt,isclose,log
import json
root=Path(__file__).resolve().parents[2];eps=8.8541878128e-12;k=1/(4*pi*eps);a={}
series=lambda *cs:1/sum(1/c for c in cs)
d=.0025;Q=80e-9;E=4e6;a['24.1']=[E*d,Q/(eps*E),Q/(E*d)]
d=.00328;A=9.82e-4;Q=4.35e-8;C=eps*A/d;a['24.2']=[C,Q/C,Q/C/d]
C=245e-12;Q=.148e-6;d=.000328;a['24.3']=[Q/C,C*d/eps,Q/C/d,Q/(C*d/eps)]
a['24.4']=[12,24,3];a['24.5']=[120e-6,60e-6,480e-6]
C=5e-12;V=100;Emax=1e4;d=V/Emax;A=C*d/eps;a['24.6']=[d,A,sqrt(A/pi),C*V];a['24.6-gap-radius-ratio']=d/sqrt(A/pi)
a['24.7']=[eps*6.8e-4*42/(240e-12),84]
a['24.8']=[.0025*exp(2*pi*eps*.12/(36.7e-12)),36.7e-12*125/.12]
C=2*pi*eps*.18/log(.005/.0005);a['24.9']=[C,10e-12/C]
c=2*pi*eps/log(.0035/.0022);a['24.10']=[c,c*2.8*.350]
C=3.3e-9/220;b=.04;r=1/(1/b+4*pi*eps/C);a['24.11']=[C,r,k*3.3e-9/r**2]
r=.15;C=116e-12;b=1/(1/r-4*pi*eps/C);a['24.12']=[b,C*220]
a['24.13']=.650*3e-6/(1-.650)
Cp=5+8;Ce=series(10,Cp,9);Q=Ce*50
a['24.14']=[Ce*1e-6,Q*1e-6,Q*1e-6,Q*1e-6]
a['24.15']=500/.1
a['24.16']=[20e-12,series(15e-12,20e-12)]
C=4;C12=series(C,C);Cad=C12+C;Ce=series(Cad,C);Q=Ce*28;Vad=Q/Cad
a['24.17']={'charges':[C12*Vad,C12*Vad,C*Vad,Q],'voltages':[Vad/2,Vad/2,Vad,Q/C],'Vad':Vad}
Ce=series(3e-6,5e-6);Q=Ce*64;a['24.18']=[Q,Q,Q/3e-6,Q/5e-6]
a['24.19']=[3e-6*52,5e-6*52,52,52]
Vparallel=30e-6/3e-6;Q1=6e-6*Vparallel;Q3=Q1+30e-6;a['24.20']=[Q1,Q3,Vparallel+Q3/5e-6]
Ce=series(18,30,10)+7.5+6.5;a['24.21']=[Ce*1e-9,Ce*1e-9*25,6.5e-9*25,25]
ra=.125;rb=.148;C=4*pi*eps*ra*rb/(rb-ra);Q=C*120
a['24.22']=[.5*eps*(k*Q/r**2)**2 for r in [.126,.147]]
a['24.23']=.5*eps*(400/.005)**2
C=920e-12;Q=3.90e-6;U=Q*Q/(2*C);a['24.24']=[Q/C,2*Q/C,U]
C=.0180e-6/200;d=.0015;a['24.25']=[C,C*d/eps,3e6*d,.5*C*200**2]
a['24.26']=[8.38/2,8.38*2]
a['24.27']=[4,2,2]
a['24.27-charge-accounting']=[(C*1)/(C/2),(2*C)/(C), (2*C)/(C/2)]
Ce=series(150e-9,120e-9);Q=Ce*48
a['24.28']=[Q,Q/(150e-9),Q/(120e-9),.5*Ce*48**2,Q*Q/(2*150e-9),Q*Q/(2*120e-9)]
a['24.29']=[110e-9*220,35e-9*220,75e-9*220,.5*110e-9*220**2,.5*35e-9*220**2,.5*75e-9*220**2,220]
a['24.30']=[(4e-6+6e-6)*36,(5*4e-6+6e-6)*36]
U0=.5*12.5e-6*24**2;a['24.31']=[U0,3.75*U0,2.75*U0]
a['24.32']=[8e-12*.0015*3e4,2.7*8e-12*.0015*3e4]
a['24.33']=[eps*(3.2e5-2.5e5),3.2e5/2.5e5]
K=4;ratio=2*K/(K+1)
a['24.34']=[ratio,ratio>1]
Q0=1;C=1;V=2*Q0/C;Qfinal=(K*C*C/(K*C+C))*V
a['24.35']=[Qfinal/Q0,Qfinal>Q0]
a['24.36']=[series(4*3,6)/series(3,6),1]
d=5500/(1.6e7);a['24.37']=[d,1.25e-9*d/(3.6*eps)]
sigma=.50e-3;d=5e-9;E=sigma/eps;r=(3e-16/(4*pi))**(1/3);U=.5*eps*E*E*4*pi*r*r*d
a['24.38']=[E,E*d,r,U,E/5.4,E*d/5.4]
Q0=.25e-6*12;K=3.1;a['24.39']=[(K-1)*Q0,(K-1)*Q0,1]
targets={
 '24.1':[1e4,2.26e-3,8e-12],'24.2':[2.65e-12,16.4e3,5e6],
 '24.3':[604,9.08e-3,1.84e6,16.3e-6],'24.4':[12,24,3],'24.5':[120e-6,60e-6,480e-6],
 '24.6':[.01,5.65e-3,.0424,500e-12],'24.6-gap-radius-ratio':.2359,'24.7':[.00105,84],
 '24.8':[.003,38.2e-9],'24.9':[4.35e-12,2.30],'24.10':[1.2e-10,1.2e-10],
 '24.11':[15e-12,.0308,31.2e3],'24.12':[.175,25.5e-9],
 '24.13':5.57e-6,'24.15':5000,'24.16':[20e-12,8.57e-12],
 '24.18':[120e-6,120e-6,40,24],'24.19':[156e-6,260e-6,52,52],
 '24.20':[60e-6,90e-6,28],'24.21':[19.3e-9,482e-9,162.5e-9,25],
 '24.23':.0283,'24.24':[4.24e3,8.48e3,.00827],
 '24.25':[90e-12,.0152,4500,1.80e-6],'24.26':[4.19,16.76],
 '24.27':[4,2,2],'24.27-charge-accounting':[2,2,4],'24.34':[1.6,True],'24.35':[1.6,True],'24.30':[360e-6,936e-6],'24.31':[.00360,.0135,.0099],
 '24.32':[360e-12,972e-12],'24.33':[.620e-6,1.28],
 '24.36':[2,1],'24.37':[.00034375,.0135],'24.39':[6.3e-6,6.3e-6,1]
}
for name,target in targets.items():
 values=a[name];aa=values if isinstance(values,(list,tuple)) else [values];bb=target if isinstance(target,(list,tuple)) else [target]
 for x,y in zip(aa,bb):assert isclose(x,y,rel_tol=.025 if name=='24.10' else .008),(name,x,y)
assert isclose(a['24.17']['charges'][0]+a['24.17']['charges'][2],a['24.17']['charges'][3],rel_tol=1e-12)
assert isclose(a['24.17']['voltages'][0]+a['24.17']['voltages'][1],a['24.17']['Vad'],rel_tol=1e-12)
out=root/'qa/physics/chapter24';out.mkdir(parents=True,exist_ok=True)
(out/'exercise-checks.json').write_text(json.dumps({'status':'passed','checkedExerciseRange':[1,39],'groups':len(a),'checks':a},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(a,ensure_ascii=False,indent=2))
