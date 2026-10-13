"""Independent analytic, numerical integration and data fits for the final problems."""
from pathlib import Path
import json,math
import numpy as np
ROOT=Path(__file__).resolve().parents[2];mu0=4*math.pi*1e-7;eps0=8.8541878128e-12
results={}
def put(n,**values):results[str(n)]=values
M,R,W,k,x0,B=1.20,.500,.400,90.,.100,1.
drag=B*B*W*W/R;alpha=drag/(2*M);omega0=math.sqrt(k/M);wd=math.sqrt(omega0**2-alpha**2)
C=x0*math.sqrt(1+(alpha/wd)**2)
t_first=(math.pi/2+math.atan(alpha/wd))/wd
v_first=-x0*math.exp(-alpha*t_first)*omega0**2/wd*math.sin(wd*t_first)
put(62,damping=drag,decayRate=alpha,dampedAngularFrequency=wd,frequency=wd/(2*math.pi),envelopeAt5=C*math.exp(-alpha*5),approximateEnvelopeAt5=x0*math.exp(-alpha*5),firstEquilibriumTime=t_first,speedAtFirstEquilibrium=abs(v_first),currentAtFirstEquilibrium=B*W*abs(v_first)/R)
put(63,time=math.sqrt(21e-6/(3.5e-11*3*8e3)))
factor=.250/(4*math.pi*.008**2)
put(64,fieldAt2=factor*.003,fieldAt5=factor*.012,fieldAt6=factor*.0135)
# Fit all measured data with both slope+intercept and the physical origin fit.
v65=np.array([20.,16.,14.,12.,10.,8.])*1e-2
a65=np.array([6.2,4.9,4.3,3.7,3.1,2.5])*1e-2
s65,c65=np.polyfit(v65,a65,1);s650=float(v65@a65/(v65@v65))
B65=math.sqrt(s65*.200*.800/.060**2)
put(65,slope=s65,intercept=c65,originSlope=s650,field=B65,halvingTime=math.log(2)/s65)
v66=np.array([2.,4.,6.,8.,10.])*1e-2
F66=np.array([.10,.21,.31,.41,.52])
s66,c66=np.polyfit(v66,F66,1);s660=float(v66@F66/(v66@v66))
B66=math.sqrt(s66*.004/.080**2)
put(66,slope=s66,intercept=c66,originSlope=s660,field=B66,powerAt005=s66*.050**2)
omega=4*math.pi;radius=.100;theta_end=math.pi/3;B67=1.;res67=10.
theta=(np.arange(100000)+.5)*theta_end/100000
integral=float(np.sum(-omega*B67*radius**2*np.sin(theta)*np.cos(theta))*theta_end/100000)
analytic=-.5*omega*B67*radius**2*math.sin(theta_end)**2
assert math.isclose(integral,analytic,rel_tol=1e-10)
put(67,angularSpeed=omega,surfaceSpeedCoefficient=omega*radius,emfTopToAngled=analytic,current=abs(analytic)/res67)
# Problem 68 integrate the magnetic field proportional to radius.
eta,t,a,b=2.,.4,.03,.1
displacement=eps0*2*eta*t*math.pi*a*a
field=lambda r:mu0*eps0*eta*t*r
r=(np.arange(10000)+.5)*a/10000
flux=float(np.sum(field(r))*a/10000*b)
expected_flux=.5*mu0*eps0*eta*t*b*a*a
assert math.isclose(flux,expected_flux,rel_tol=1e-13)
put(68,fluxSample=flux,emfCoefficient=.5*mu0*eps0*b*a*a)
# Problem 69 check equilibrium and power from independently evaluated force.
mass,L,res,B,phi,g=.2,.3,2.,.8,.4,9.80
terminal=res*mass*g*math.sin(phi)/(B*B*L*L*math.cos(phi)**2)
current=B*L*terminal*math.cos(phi)/res
assert math.isclose(current*B*L*math.cos(phi),mass*g*math.sin(phi),rel_tol=1e-12)
assert math.isclose(current*current*res,mass*g*terminal*math.sin(phi),rel_tol=1e-12)
put(69,terminalSample=terminal,currentSample=current,powerBalance=True)
# The two side rods each contribute (m/4)*L²/3, the far rod (m/4)*L².
put(70,inertiaCoefficient=1/4+2/12)
assert math.isclose(results['70']['inertiaCoefficient'],5/12)
put(71,answer='c');put(72,answer='b');put(73,answer='a');put(74,answer='c')
out=ROOT/'qa/physics/chapter29';out.mkdir(parents=True,exist_ok=True)
(out/'exercises61-74-checks.json').write_text(json.dumps({'status':'passed','results':results},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(results,ensure_ascii=False,indent=2))
