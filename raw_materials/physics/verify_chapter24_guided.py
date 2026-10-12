from pathlib import Path
from math import pi,exp,isclose
import json
root=Path(__file__).resolve().parents[2];eps=8.8541878128e-12;a={}
a['VP24.4.1']=[eps*2.75/.00370,1.40e-5/eps*.00370]
C=8.30e-9;A=4.5;d=eps*A/C
a['VP24.4.2']=[d,C*3000,3000/d]
C=125e-12;b=.09;r=1/(1/b+4*pi*eps/C);Q=C*355
a['VP24.4.3']=[r,Q,Q/(4*pi*r*r),-Q/(4*pi*b*b)]
a['VP24.4.4']=[exp(2*pi*eps/69e-12),8.62e-9/(69e-12)]
series=lambda *cs:1/sum(1/c for c in cs)
a['VP24.9.1']=[series(1e-6,2.5e-6,5e-6),8.5e-6,series(3.5e-6,5e-6),series(1e-6,2.5e-6)+5e-6]
a['VP24.9.2']=[(4.5e-4)**2/(2*1.5e-6),(4.5e-4)**2/(2*6e-6),.5*1.5e-6*125**2,.5*6e-6*125**2]
Cs=series(1.5e-6,4e-6);Cp=5.5e-6
a['VP24.9.3']=[.5*Cs*145**2,.5*Cp*145**2,(4e-4)**2/(2*Cs),(4e-4)**2/(2*Cp)]
sigma=1.25e-5/2.45;E=sigma/eps;u=.5*eps*E*E
a['VP24.9.4']=[sigma,E,u,u*2.45*.00140]
C0=eps*.460/.003;Q=C0*4000;K=4000/2500
a['VP24.11.1']=[C0,Q,K,K*C0,Q*(1-1/K)]
C0=eps*1.20/.00450;Q0=C0*3500;K=2.5
a['VP24.11.2']=[C0,Q0,K*C0,K*Q0,K*Q0*(1-1/K)]
Q=4.50e-6*2800
a['VP24.11.3']=[.5*Q*2800,.5*Q*1200]
a['VP24.11.4']=[.5*5.6e-6*1500**2,.5*2.85*5.6e-6*1500**2]
targets={
 'VP24.4.1':[6.58e-9,5.85e3], 'VP24.4.2':[.0048,2.49e-5,6.25e5],
 'VP24.4.3':[.0833,4.44e-8,5.09e-7,-4.36e-7], 'VP24.4.4':[2.24,125],
 'VP24.9.1':[.625e-6,8.5e-6,2.06e-6,5.71e-6],
 'VP24.9.2':[.0675,.0169,.0117,.0469], 'VP24.9.3':[.0115,.0578,.0733,.0145],
 'VP24.9.4':[5.10e-6,5.76e5,1.47,.00504],
 'VP24.11.1':[1.36e-9,5.43e-6,1.60,2.17e-9,2.04e-6],
 'VP24.11.2':[2.36e-9,8.26e-6,5.90e-9,2.07e-5,1.24e-5],
 'VP24.11.3':[17.6,7.56], 'VP24.11.4':[6.30,18.0]
}
for name,values in a.items():
 for actual,target in zip(values,targets[name]):assert isclose(actual,target,rel_tol=.008),(name,actual,target)
# Independently integrate the conducting sphere's field to infinity by u=1/r.
Q=3e-9;R=.1;U=Q*Q/(8*pi*eps*R)
energy_in_inverse_radius=Q*Q/(8*pi*eps)*(1/R)
assert isclose(U,energy_in_inverse_radius,rel_tol=1e-12)
a['bridge24-energy-coefficient']=1/(8*pi*eps)
out=root/'qa/physics/chapter24';out.mkdir(parents=True,exist_ok=True)
(out/'guided-checks.json').write_text(json.dumps({'status':'passed','groups':len(a),'checks':a},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(a,ensure_ascii=False,indent=2))
print('Passed',len(a),'guided practice and bridge checks.')
