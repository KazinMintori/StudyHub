"""Recalculate the actual chapter18 state examples and distribution identities."""
from pathlib import Path
import json, math
import numpy as np
from scipy.integrate import quad

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'qa/physics1-priority'
OUT.mkdir(parents=True,exist_ok=True)
R=8.314
V=R*273.15/1.013e5
n1=1.013e5*.011/(R*294)
p2=2.10e7+1.013e5
n2=p2*.011/(R*315)
H=R*273/(.0288*9.80)
co2V=.0224
ideal=R*273.15/co2V
vdw=R*273.15/(co2V-4.27e-5)-.364/co2V**2
cases={
 'opening':dict(hot_K=373.15,cold_K=298.15,speedRatio=math.sqrt(373.15/298.15)),
 '18.1':dict(n_mol=1,T_K=273.15,p_Pa=1.013e5,V_m3=V,V_L=1000*V,cubeSide_m=V**(1/3)),
 '18.2':dict(T1_K=300,p1_atm=1,p2_atm=21.7,compressionRatio=9,T2_K=300*21.7/9,T2_C_rounded=723-273),
 '18.3':dict(V_m3=.011,T1_K=294,T2_K=315,p1_Pa=1.013e5,p2Gauge_Pa=2.10e7,p2Absolute_Pa=p2,n1_mol=n1,n2_mol=n2,added_mol=n2-n1,added_kg=.0288*(n2-n1)),
 '18.4':dict(T_K=273,M_kg_mol=.0288,g_m_s2=9.8,scaleHeight_m=H,altitude_m=8848,exponent=8848/H,p_Pa=1.013e5*math.exp(-8848/H),p_atm=math.exp(-8848/H)),
 'vanDerWaals':dict(n_mol=1,T_K=273.15,V_m3=co2V,a=.364,b=4.27e-5,ideal_Pa=ideal,vdw_Pa=vdw,difference_Pa=ideal-vdw,relativeDifference=(ideal-vdw)/ideal),
 'selfcheck18.1':dict(relativeMoles=[1,2,2,.5,1]),
 'heatCapacityFactors':dict(mono=1.5*R,diatomic=2.5*R,withVibration=3.5*R,solid=3*R),
 'selfcheck18.4':dict(initialCvFactor=1.5,finalCvFactor=2.5,initialToFinalHeatingRate=2.5/1.5)
}
assert math.isclose(V*1000,22.4,rel_tol=.001)
assert math.isclose(cases['18.2']['T2_K'],723,abs_tol=.5)
assert math.isclose(cases['18.3']['added_kg'],2.54,abs_tol=.005)
assert math.isclose(cases['18.4']['p_Pa'],3.37e4,rel_tol=.001)
assert math.isclose(ideal-vdw,532,abs_tol=.5)
# Dimensionless x = v / sqrt(kT/m). Compare all table18.2 entries
# by independent numerical integration, rather than copying a lookup table.
f=lambda x:math.sqrt(2/math.pi)*x*x*math.exp(-x*x/2)
table=[(.2,.011),(.4,.077),(.6,.218),(.8,.411),(1.,.608),(1.2,.771),(1.4,.882),(1.6,.947),(1.8,.979),(2.,.993)]
fractions=[]
for multiple,published in table:
 actual=quad(f,0,multiple*math.sqrt(3),epsabs=1e-12)[0]
 assert abs(actual-published)<.00051,(multiple,actual,published)
 fractions.append(dict(vOverRms=multiple,published=published,calculated=actual))
assert math.isclose(quad(f,0,np.inf)[0],1,rel_tol=1e-12)
mean=quad(lambda x:x*f(x),0,np.inf)[0]
second=quad(lambda x:x*x*f(x),0,np.inf)[0]
assert math.isclose(mean,math.sqrt(8/math.pi),rel_tol=1e-12)
assert math.isclose(second,3,rel_tol=1e-12)
# y = epsilon/(kT). A true energy density requires the Jacobian.
h=lambda y:2/math.sqrt(math.pi)*math.sqrt(y)*math.exp(-y)
assert math.isclose(quad(h,0,np.inf,epsabs=1e-12,epsrel=1e-12)[0],1,rel_tol=1e-12)
assert math.isclose(quad(lambda y:y*h(y),0,np.inf,epsabs=1e-12,epsrel=1e-12)[0],1.5,rel_tol=1e-12)
delta=1e-5
assert h(.5)>h(.5-delta) and h(.5)>h(.5+delta)
composed=lambda y:y*math.exp(-y)
assert composed(1)>composed(1-delta) and composed(1)>composed(1+delta)
F=lambda x:quad(f,0,x)[0]
for lower,upper in [(0,1),(.5,2),(2,5)]:
 probability=quad(f,lower,upper)[0]
 assert math.isclose(probability,F(upper)-F(lower),rel_tol=1e-12)
cases['maxwell']=dict(normalization=quad(f,0,np.inf)[0],meanSpeedFactor=mean,rmsSpeedFactor=math.sqrt(second),energyDensityNormalization=quad(h,0,np.inf)[0],meanEnergyFactor=1.5,energyDensityMode=.5,composedSpeedDensityMode=1,table18_2=fractions)
result=dict(status='passed',scope='Actual examples18.1–18.4, opening, van der Waals comparison, heat-capacity factors, ten Maxwell table entries and change-of-variable identities; source and browser completeness reviewed separately.',cases=cases)
(OUT/'ch18-state-actual-cases.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(status='passed',actualExamples=4,maxwellTableEntries=len(table),addedAir_kg=cases['18.3']['added_kg'],vdwDifference_Pa=ideal-vdw)))
