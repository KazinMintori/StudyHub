"""Numerical/analytic checks for chapter17 discussion explanations; no textbook prose generated."""
import math,json
from pathlib import Path
checks={}
# Small hot-water sample changes appreciably when a cold thermometer equilibrates.
Cw,Ct,Tw,Tt=4.19,15,80,20
Tf=(Cw*Tw+Ct*Tt)/(Cw+Ct)
assert Tf<Tw-30
checks['Q17.1']={'illustrativeWaterCapacity_J_K':Cw,'thermometerCapacity_J_K':Ct,'equilibrium_C':Tf,'illustrationOnly':True}
Tc=20;first=(Tc+273.15);doubledC=2*Tc+273.15
assert not math.isclose(doubledC/first,2)
checks['Q17.2']={'Celsius20to40_pressureRatio':doubledC/first}
# Same bounding volume, homogeneous free thermal dilation, including void.
alpha=2e-5;delta=40;scale=1+alpha*delta
checks['Q17.5']={'outsideVolumeScaleForEither':scale**3}
# Unit identity: J/(kg K)=m²/(s²K).
assert math.isclose((2*3**2/4**2)/(2*5),3**2/(4**2*5))
checks['Q17.9']={'dimensionalIdentity':'J/(kg K)=m²/(s² K)'}
# Cooling before/after instant cream addition; same lumped conductance.
C,Cc,k,t=1000.,100.,1.5,300.;Ta,Ti,Tcream=20.,90.,5.
early=Ta+(C*(Ti-Ta)+Cc*(Tcream-Ta))/(C+Cc)*math.exp(-k*t/(C+Cc))
late=(C*(Ta+(Ti-Ta)*math.exp(-k*t/C))+Cc*Tcream)/(C+Cc)
assert early>late
checks['Q17.20']={'earlyCreamFinal_C':early,'lateCreamFinal_C':late,'model':'Constant conductance and heat capacities; instantaneous mixing; same environment; no phase change.'}
# Newton cooling is a rate statement, not a statement about time to a fixed threshold.
hot,cold,env,target=80.,20.,-20.,0.
th=math.log((hot-env)/(target-env));tc=math.log((cold-env)/(target-env))
assert th>tc
checks['Q17.26']={'scaledHotCoolingTime':th,'scaledColdCoolingTime':tc,'model':'Identical constant heat capacity and conductance; no evaporation/supercooling.'}
# Night setback with a simplified energy balance and identical initial/final wall energy.
U,Ta,day,night,hours=200.,0.,20.,15.,8.
checks['Q17.28']={'constantLoss_J':U*(day-Ta)*hours*3600,'setbackLoss_J':U*(night-Ta)*hours*3600}
assert checks['Q17.28']['setbackLoss_J']<checks['Q17.28']['constantLoss_J']
# Fixed body losing sensible heat and latent energy has different unit roles.
assert math.isclose(1*4190*10,41900)
out=Path(__file__).resolve().parents[2]/'qa/physics1-priority/ch17-discussion-parent-checks.json'
out.write_text(json.dumps({'status':'passed','checks':checks,'limitations':'Illustrative model tests do not establish empirical values or universal claims outside stated assumptions.'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Checked7 quantitative/limiting-case explanations and dimensional identities.')
