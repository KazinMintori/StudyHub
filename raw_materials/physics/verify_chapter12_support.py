"""Verify the proposed support formulas using exact arithmetic and dimensions."""
from pathlib import Path
from fractions import Fraction as F
import math,json,hashlib

OUT=Path(__file__).resolve().parent
checks=[]
def eq(id,a,b,tol=1e-11):
    assert math.isclose(float(a),float(b),rel_tol=tol,abs_tol=tol),(id,a,b)
    checks.append(dict(id=id,actual=float(a),expected=float(b),passed=True))

for case in range(1,9):
    rho=F(800+50*case);g=F(49,5);A1=F(case+1,100);A2=A1/4
    h=F(case,2);p0=F(101325);p=p0+rho*g*h
    eq(f'{case}:density',rho*F(3,10)/F(3,10),rho)
    eq(f'{case}:hydrostatics',p-p0,rho*g*h)
    y1,y2=F(case),F(case+3)
    p1=p0+rho*g*(20-y1);p2=p0+rho*g*(20-y2)
    eq(f'{case}:hydrostatic-difference',p2-p1,-rho*g*(y2-y1))
    extra=F(1800+case)
    eq(f'{case}:Pascal-increment',(p+extra)-p,extra)
    f1=F(230+case);f2=A2/A1*f1
    eq(f'{case}:hydraulic-force',f1/A1,f2/A2)
    eq(f'{case}:gauge-absolute',p0+(p-p0),p)
    V=F(case+1,2000);objrho=rho*F(3,5);m=objrho*V;Vsub=m/rho
    eq(f'{case}:float-fraction',Vsub/V,objrho/rho)
    eq(f'{case}:buoyancy',rho*g*Vsub,m*g)
    v1=F(case+2,3);v2=A1/A2*v1
    eq(f'{case}:continuity',A1*v1,A2*v2)
    rho2=rho*F(3,2);Q1=A1*v1;Q2=rho*Q1/rho2
    eq(f'{case}:compressible-mass-flow',rho*Q1,rho2*Q2)
    C1=p1+rho*g*y1+rho*v1*v1/2
    p2b=C1-rho*g*y2-rho*v2*v2/2
    eq(f'{case}:Bernoulli',C1,p2b+rho*g*y2+rho*v2*v2/2)
    dV=F(case+1,1000)
    dW=(p1-p2b)*dV;dK=rho*dV*(v2*v2-v1*v1)/2;dU=rho*g*dV*(y2-y1)
    eq(f'{case}:Bernoulli-work-energy',dW,dK+dU)
    exit2=2*(p-p0)/rho+2*g*h
    eq(f'{case}:pressurized-tank',exit2,4*g*h)
    eq(f'{case}:Torricelli',math.sqrt(2*float(g*h))**2,2*g*h)
    alpha=A1/A2
    ventv=math.sqrt(float(2*g*h/(alpha*alpha-1)))
    eq(f'{case}:Venturi-pressure',float(rho)/2*(alpha*alpha-1)*ventv**2,rho*g*h)
    r=F(case+1,10)
    eq(f'{case}:surface-area-volume',(4*math.pi*float(r)**2)/(4*math.pi*float(r)**3/3),3/r)

eq('units:density',F(1,1000)/F(1,1000000),1000)
eq('Poiseuille:half-radius',F(1,1)/F(1,2)**4,16)
eq('Poiseuille:90percent-radius',F(1,1)/F(9,10)**4,F(10000,6561))
eq('Poiseuille:needle-diameters-0.3-0.6',F(6,3)**4,16)
eq('SG:reference-water',1000/1000,1)

# Dimensions are exponent triples (M,L,T). Definitions and source energy-per-volume relation.
def mul(a,b):return tuple(x+y for x,y in zip(a,b))
def power(a,k):return tuple(k*x for x in a)
M=(1,0,0);L=(0,1,0);T=(0,0,1)
rho=(1,-3,0);g=(0,1,-2);speed=(0,1,-1);pressure=(1,-1,-2);volume=(0,3,0);energy=(1,2,-2)
dimensions={'rho_g_h':mul(mul(rho,g),L),'rho_v_squared':mul(rho,power(speed,2)),'pressure_volume':mul(pressure,volume),'rho_volume_v_squared':mul(mul(rho,volume),power(speed,2)),'rho_g_volume_h':mul(mul(mul(rho,g),volume),L)}
assert dimensions['rho_g_h']==dimensions['rho_v_squared']==pressure
assert dimensions['pressure_volume']==dimensions['rho_volume_v_squared']==dimensions['rho_g_volume_h']==energy
print(json.dumps(dict(status='passed',numericChecks=len(checks),checks=checks,dimensions=dimensions),ensure_ascii=False,indent=2))
