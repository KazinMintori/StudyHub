"""Independent physical models for source-reviewed chapter8 units 011-020."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad,solve_ivp
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/"qa/physics1-remaining/ch08-early-recomputed";OUT.mkdir(parents=True,exist_ok=True)
checks=[]
def near(name,a,b,tol=1e-9):
    assert np.allclose(a,b,rtol=tol,atol=tol),(name,a,b)
    checks.append(dict(name=name,actual=np.asarray(a).tolist(),expected=np.asarray(b).tolist()))
def yes(name,c):
    assert c,name
    checks.append(dict(name=name,passed=True))
A=781.25/1.25**2;J=quad(lambda t:A*t*t,2,3.5)[0]
near('11 actual forcecoefficient',A,500)
near('11 actual requested2to3.5second impulse',J,5812.5)
near('11 actual velocityincrease',J/2150,2.703488372093023)
yes('11 not substituted0to1.5interval',not math.isclose(J,quad(lambda t:A*t*t,0,1.5)[0]))
force=lambda t:80 if t<=12 else 80*(18-t)/6
J=quad(force,0,18,points=[12])[0]
near('12 actual impulse by integration',J,1200)
near('12 actual finalspeed',J/80,15)
near('12 actual rectangleplus triangle',80*12+.5*80*6,J)
near('13 actual pulseunit conversions',(2.50*1000)*(16-15)*.001,2.5)
for sign,expected in [(1,6.25),(-1,3.75)]:
    impulse=sign*2.5
    v=5+impulse/2
    near('13 originalvelocity preservedsign'+str(sign),v,expected)
    near('13 exact impulse changesmomentum sign'+str(sign),2*v-2*5,impulse)
    yes('13 remainsmovingright sign'+str(sign),v>0)
Jx=quad(lambda t:.28*t,0,2)[0];Jy=quad(lambda t:-.45*t*t,0,2)[0];p0=np.array([-3.,4.]);pf=p0+[Jx,Jy]
near('14 actual two forceintegrals',[Jx,Jy],[.560,-1.2])
near('14 original initialmomentum plus actualimpulse',pf,[-2.44,2.80])
near('14 mass independent momentumchange',pf-p0,[Jx,Jy])
near('15 original linearmomentum',40*20,800)
near('15 original kineticenergy',.5*40*20**2,8000)
near('15 actual signed brakingforce',(0-40*20)/5,-160)
near('15 exact stoppingimpulse',-160*5,-800)
V=-2.25*3.2/68.5
near('16 actual recoilvelocity',V,-.10510948905109489)
near('16 original stationframe momentum',68.5*V+2.25*3.2,0)
yes('16 recoil oppositetool',V<0)
ground_bullet=601-1.85;p_gas=-(.0072*ground_bullet+2.8*(-1.85))
near('17 actual muzzletoearth velocity',ground_bullet,599.15)
near('17 actual gasmomentum',p_gas,.86612)
near('17 allthree groundmomenta sumzero',.0072*ground_bullet-2.8*1.85+p_gas,0)
yes('17 gasescarry forwardmomentum',p_gas>0)
near('17 incorrect601earth assumption differs',-(.0072*601-2.8*1.85),.8528)
g=9.8;mL=625/g;mH=725/g;vH=1.5;vL=725/625*vH
near('18 actual lighter velocitymagnitude',vL,1.74)
near('18 opposite skatermomenta',mL*vL-mH*vH,0)
energy=.5*mL*vL*vL+.5*mH*vH*vH
near('18 actual createdkineticenergy',energy,179.77040816326524)
yes('18 energypositive despitezero netmomentum',energy>0)
mwater=1.75;msquid=6.5-mwater;vsquid=2.5;vwater=-msquid*vsquid/mwater
near('19 actual postexpulsionsquidmass',msquid,4.75)
near('19 actual watergroundvelocity',vwater,-6.785714285714286)
near('19 actual relativewaterspeed',abs(vwater-vsquid),9.285714285714285)
near('19 original totalmomentumzero',msquid*vsquid+mwater*vwater,0)
near('19 actual generatedkineticenergy',.5*msquid*vsquid**2+.5*mwater*vwater**2,55.13392857142857)
yes('19 do notdoublecount expelledwater',msquid+mwater==6.5)
near('20 actual catching commonvelocity',.6*10/(70+.6),.08498583569405099)
near('20 exact catchingmomentum',(70+.6)*(.6*10/70.6),.6*10)
rebound=.6*(10-(-8))/70
near('20 actual rebound personvelocity',rebound,.15428571428571428)
near('20 exact separatepersonandballmomentum',70*rebound+.6*(-8),.6*10)
yes('20 reboundtransfers moremomentum',rebound>.6*10/70.6)
report=dict(status="passed",checksCount=len(checks),checks=checks)
(OUT/"numeric-011-020.json").write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+"\n").encode("utf8"))
print("PASS 011-020:",len(checks),"independent physical checks.")
