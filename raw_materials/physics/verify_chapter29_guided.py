"""Independent numerical and vector checks for all chapter 29 guided variants."""
from pathlib import Path
import json,math
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
MU0=4*math.pi*1e-7
checks=[]
def close(name,value,expected,rtol=5e-4):
    assert math.isclose(value,expected,rel_tol=rtol,abs_tol=1e-15),(name,value,expected)
    checks.append({'id':name,'value':value,'expected':expected})

area=math.pi*.024**2
close('VP29.8.1/flux0',.140*area,2.5333803158548e-4)
close('VP29.8.1/flux2',-.110*area,-1.99051310531449e-4)
close('VP29.8.1/emf',.250*area/2,2.26194671058465e-4)
emf=455*math.pi*.05**2*math.cos(math.radians(20))*.003
close('VP29.8.2/emf',emf,.010074923)
close('VP29.8.2/current',emf/14.5,6.9482228e-4)
close('VP29.8.3/emf',875*.04**2*.350/3,.1633333333333)
assert -.350/3<0 # Normal Bz decreases, so the induced circulation is positive.
for t,sign in [(0,-1),(math.pi,1)]:
    assert math.copysign(1,-math.cos(t))==sign
    checks.append({'id':f'VP29.8.4/emf-sign-at-{t}','sign':sign})
v=np.array([0.,3.90,0.]);field=np.array([0.,0.,-.600])
electric=-np.cross(v,field)
assert np.allclose(electric,[2.34,0,0])
close('VP29.9.1/emf',abs(np.cross(v,field)[0])*.08,.1872)
close('VP29.9.1/electric-field',np.linalg.norm(electric),2.34)
close('VP29.9.2/current',.150*.05*2.40/.0200,.900)
lorentz=np.cross([1.50,2.00,0.],[-.120,0.,.150])
assert np.allclose(lorentz,[.300,-.225,.240])
close('VP29.9.3/potential-b-minus-a',lorentz[0]*.08,.024)
close('VP29.9.4/speed',.0600*.750/(.550**2*.190**2),4.1207856963)
close('VP29.11.1/turn-density',15e-6/(MU0*3e-4*22),1808.57889877)
close('VP29.11.1/electric-field',15e-6/(2*math.pi*.031),7.70104563348e-5)
close('VP29.11.2/electric-field',.00360*.0150/2,2.70e-5)
for letter,efield,expected in [('a',1.20e-5,-7.7720207254),('b',-1.80e-5,11.6580310881)]:
    close('VP29.11.3/'+letter,-2*math.pi*.05*efield/(MU0*965*4e-4),expected)
close('VP29.11.4/current',MU0*585*2.70e-4*(1.2*13.9)/.600,5.5180063e-6)

# The bridge answer is independent of s and d. Check by the original mass,
# resistance and force balance for several nonzero geometries.
rho_mass=8960.;rho_resistance=1.72e-8;B=.500;g=9.80
terminal=16*rho_mass*rho_resistance*g/B**2
for side,diameter in [(.05,.001),(.20,.002),(.15,.0008)]:
    wire_area=math.pi*diameter**2/4
    resistance=rho_resistance*4*side/wire_area
    mass=rho_mass*4*side*wire_area
    magnetic_force=B**2*side**2*terminal/resistance
    close(f'Bridge29/force-balance/{side}',magnetic_force,mass*g)

out=ROOT/'qa/physics/chapter29';out.mkdir(parents=True,exist_ok=True)
(out/'guided-checks.json').write_text(json.dumps({'status':'passed','variantProblems':12,'bridgeProblems':1,'checks':checks},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(f'PASS: 12 guided variants, bridge force balance, {len(checks)} numerical/vector checks.')
