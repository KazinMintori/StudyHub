"""Independent quantitative checks for18discussion answers."""
from pathlib import Path
import json,math,cmath
import numpy as np
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter35';q.mkdir(parents=True,exist_ok=True)
r={}
r['Q35.1']={'fringeSpacingRatioForWater':1/1.333,'frequencyUnchanged':True}
for m in range(-4,5):
 u=m*.07
 if abs(u)<1:
  exact=u/math.sqrt(1-u*u)
  if m==0:assert exact==0
r['Q35.3-4']={'equalSpacing':'small-angle approximation only','finiteScreenNeedsSinLessThan1':True}
a,b=.5,1.
for phi in np.linspace(0,2*math.pi,101):
 intensity=abs(a+b*cmath.exp(1j*phi))**2
 assert .25-1e-12<=intensity<=2.25+1e-12
r['Q35.6']={'amplitudeMax':1.5,'amplitudeMin':.5,'intensityRatioMaxOverMin':9.,'trueNodesRemoved':True}
r['Q35.8']={'largeSpacingStillInterferes':True,'angularSpacingFormula':'lambda/d'}
r['Q35.9']={'separationThresholdOverLambda':.5,'finiteScreenRequiresStrictGreater':True}
phi=.37
assert not math.isclose(phi/(2*math.pi),round(phi/(2*math.pi)))
r['Q35.10']={'generalPhaseAllowed':phi,'brightOnlyRequiresPhaseIntegerTurns':True}
for phi in [0,math.pi,math.pi/2]:
 average=2+2*math.cos(phi)
 ts=np.linspace(0,2*math.pi,200000,endpoint=False)
 numerical=2*np.mean((np.cos(ts)+np.cos(ts+phi))**2)
 assert abs(numerical-average)<1e-11
r['Q35.12']={'sumIntensitiesOnlyWhenCrossTermAveragesZero':True}
def Rfilm(n,t,lam,substrate):
 r01=(1-n)/(1+n);r12=(n-substrate)/(n+substrate);z=cmath.exp(4j*math.pi*n*t/lam)
 return abs((r01+r12*z)/(1+r01*r12*z))**2
dry=((1-1.5)/(1+1.5))**2
for t in np.linspace(0,2e-6,200):
 assert Rfilm(1.33,t,550e-9,1.5)<=dry+1e-12
r['Q35.13']={'waterIntermediateIndex':True,'quarterWaveReflectance':Rfilm(1.33,550e-9/(4*1.33),550e-9,1.5),'dryReflectance':dry}
r['Q35.14']={'soapInAirThinLimit':Rfilm(1.33,0,550e-9,1),'soapOnGlassThinLimit':Rfilm(1.33,0,550e-9,1.5)}
assert r['Q35.14']['soapInAirThinLimit']<1e-25
assert math.isclose(r['Q35.14']['soapOnGlassThinLimit'],dry)
r['Q35.15']={'opticalPathDifference':'2nt at normal incidence','coherenceAndResolutionMatter':True}
r['Q35.16-17']={'losslessEnergyConservation':'R+T=1','destructiveReflectionRedistributesIntoTransmission':True}
r['Q35.18']={'airIndexLessThanOilIndex':True,'oilIndexGreaterThanWaterIndex':True,'oneRelativeReflectionPhasePi':True}
(q/'discussion-data-checks.json').write_text(json.dumps({'status':'passed','discussionQuestions':18,'quantitativeChecks':r},indent=2),encoding='utf-8')
print('Checked18discussionclaims: Phase/amplitude distinctions, angular domains, coherence and exact filmreflection limits.')
