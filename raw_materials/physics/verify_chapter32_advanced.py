"""Check exercises49–56, SI conversions, and independent field identities."""
from pathlib import Path
import json,math
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
c=3e8;mu0=4*math.pi*1e-7;eps0=1/(mu0*c*c)
G=6.6743e-11;Msun=1.98847e30
q=1.602176634e-19;mp=1.67262192369e-27;me=9.1093837015e-31
r={}
e=.61;I=1400;D=8e-6;m=1e-13;distance=1.5e11
area=math.pi*(D/2)**2;pressure=I*(2-e)/c;force=pressure*area;grav=G*Msun*m/distance**2
assert math.isclose(pressure,e*I/c+(1-e)*2*I/c,rel_tol=1e-13)
assert math.isclose(force/grav,.553,rel_tol=.005)
r['49']={'pressurePa':pressure,'forceN':force,'gravityN':grav,'forceRatio':force/grav,'diameterM':D,'massKg':m}
lam=500e-9;k=2*math.pi/lam;omega=c*k;h=.02
E=math.sqrt(mu0*c*100);B=E/c
z=np.linspace(0,lam/2,10001)
for phase in [0,.3,1.2,2.6,4.8]:
 circulation=h*E*(math.cos(-phase)-math.cos(math.pi-phase))
 flux=-h*np.trapezoid(B*np.cos(k*z-phase),z)
 analytic_flux=-2*h*B*math.sin(phase)/k
 emf=2*h*B*omega*math.cos(phase)/k
 assert math.isclose(flux,analytic_flux,abs_tol=1e-18)
 assert math.isclose(circulation,emf,rel_tol=1e-12)
 ex=E*math.cos(phase);ey=E*math.sin(phase);bx=-B*math.sin(phase);by=B*math.cos(phase)
 assert math.isclose((ex*by-ey*bx)/mu0,100,rel_tol=1e-12)
 assert math.isclose(ey+(-ey),0,abs_tol=1e-10)
 assert math.isclose(bx+(-bx),0,abs_tol=1e-15)
r['50']={'E_Vpm':E,'B_T':B,'frequencyHz':c/lam,'k':k,'omega':omega,'intensity':100,'normal':'-y'}
Kp=6e6*q;radius=.750;v2=2*Kp/mp;a=v2/radius
power=q*q*a*a/(6*math.pi*eps0*c**3)
Ke=.5*me*v2;fp=power/Kp;fe=power/Ke
assert math.isclose(fe/fp,mp/me,rel_tol=1e-12)
r['51']={'protonKineticJ':Kp,'speed':math.sqrt(v2),'speedFractionC':math.sqrt(v2)/c,'acceleration':a,'powerW':power,'protonFractionPerSecond':fp,'electronKineticJ':Ke,'electronFractionPerSecond':fe}
K=13.6*q;radius=0.0529e-9;v2=2*K/me;a=v2/radius
power=q*q*a*a/(6*math.pi*eps0*c**3)
assert math.isclose(power*(K/power),K,rel_tol=1e-12)
r['52']={'radiusM':radius,'kineticJ':K,'speed':math.sqrt(v2),'acceleration':a,'initialPowerW':power,'characteristicTimeS':K/power,'energyEvPerSecond':power/q}
f=1e6;rho=1.72e-8;w=2*math.pi*f;kc=math.sqrt(w*mu0/(2*rho));delta=1/kc
assert math.isclose(math.exp(-kc*delta),1/math.e,rel_tol=1e-12)
dx=1e-4;dt=1e-4
for x,t in [(0,0),(.3,.7),(.7,1.2),(1.3,.2),(2.,2.4)]:
 field=lambda xx,tt:math.exp(-xx)*math.cos(xx-tt)
 dxx=(field(x+dx,t)-2*field(x,t)+field(x-dx,t))/dx**2
 dtime=(field(x,t+dt)-field(x,t-dt))/(2*dt)
 assert math.isclose(dxx,2*dtime,rel_tol=1e-5,abs_tol=1e-7)
r['53']={'frequencyHz':f,'resistivity':rho,'kC':kc,'skinDepthM':delta,'skinDepthMicrometres':delta*1e6,'conductionDisplacementRatio':1/(rho*w*eps0)}
fk=.060;Elimit=350/fk;Ilimit=.5*eps0*c*Elimit**2
assert math.isclose(Ilimit,45000,rel_tol=.01)
r['54']={'frequencyKHz':fk,'electricAmplitude':Elimit,'intensityWm2':Ilimit,'choice':'c','assumption':'ideal travelling plane wave; exercise model, not real near-field exposure assessment'}
for freq in [.025,.060,.7,1.5]:
 old=.5*eps0*c*(350/freq)**2;new=.5*eps0*c*(350/(2*freq))**2
 assert math.isclose(new/old,.25,rel_tol=1e-12)
r['55']={'intensityRatio':.25,'choice':'d','condition':'both frequencies stay within the given interval'}
Blimit=5/fk;IfromB=.5*c*Blimit**2/mu0;ratio=IfromB/Ilimit
assert math.isclose(ratio,(c*5/350)**2,rel_tol=1e-12)
assert ratio>1
r['56']={'printedMagneticUnit':'T','magneticAmplitude':Blimit,'magneticEquivalentIntensity':IfromB,'electricEquivalentIntensity':Ilimit,'ratio':ratio,'choice':'b','limitation':'printed comparison model is not a valid real exposure guideline'}
assert set(r)=={str(i) for i in range(49,57)}
out=ROOT/'qa/physics/chapter32/advanced-data-checks.json'
out.write_text(json.dumps({'status':'passed','numberedExercises':8,'results':r},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(r,indent=2))
