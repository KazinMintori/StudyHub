"""Source Guided Practice and bridge: angles, wavelengths, polarization, and inverse checks."""
from pathlib import Path
import math,json
import numpy as np
root=Path(__file__).resolve().parents[2];out=root/'qa/physics/chapter33';out.mkdir(parents=True,exist_ok=True)
c=3e8;rad=math.radians;deg=math.degrees
snell=lambda na,nb,a:deg(math.asin(na/nb*math.sin(rad(a))))
r={}
r['VP33.2.1']={'reflection':70,'refraction':snell(1,1.8,70)}
n=1.33*math.sin(rad(55))/math.sin(rad(37))
r['VP33.2.2']={'nGlass':n,'speed':c/n}
n=635/508
r['VP33.2.3']={'nLiquid':n,'refraction':snell(1,n,35),'frequencyAir':c/635e-9,'frequencyLiquid':c/635e-9}
r['VP33.2.4']={'incidence':snell(1.309,1.36,85),'wavelengthRatio':1.36/1.309}
r['VP33.5.1']={'intensity':255*math.cos(rad(15))**2}
r['VP33.5.2']={'firstIntensity':27,'axisAngle':deg(math.acos(math.sqrt(19/27)))}
r['VP33.5.3']={'firstIntensity':60*math.cos(rad(25))**2,'secondIntensity':60*math.cos(rad(25))**4,'withoutFirstIntensity':60*math.cos(rad(50))**2}
r['VP33.5.4']={'ratio':.5+math.cos(rad(30))**2}
r['VP33.6.1']={'brewster':deg(math.atan(1.73)),'transmission':'partially polarized'}
r['VP33.6.2']={'nGlass':math.tan(rad(57)),'refraction':33}
r['VP33.6.3']={'sNoZeroReflectionAngle':True,'pBrewster':deg(math.atan(1.66))}
r['VP33.6.4']={'brewster':36.5,'nGlass':1.33/math.tan(rad(36.5))}
nw=1.333;ng=nw/math.sin(rad(59.2))
r['bridge']={'waterIndexTable33_1':nw,'criticalAngle':59.2,'nGlass':ng,'speed':c/ng,'waterSpeed':c/nw}
assert len(r)==13
assert math.isclose(1.8*math.sin(rad(r['VP33.2.1']['refraction'])),math.sin(rad(70)),rel_tol=1e-12)
assert math.isclose(r['VP33.2.2']['nGlass']*math.sin(rad(37)),1.33*math.sin(rad(55)),rel_tol=1e-12)
assert math.isclose(r['VP33.2.3']['frequencyAir']*635e-9,c,rel_tol=1e-12)
assert math.isclose(r['VP33.2.3']['frequencyLiquid']*508e-9,c/1.25,rel_tol=1e-12)
assert math.isclose(1.36*math.sin(rad(r['VP33.2.4']['incidence'])),1.309*math.sin(rad(85)),rel_tol=1e-12)
assert math.isclose(27*math.cos(rad(r['VP33.5.2']['axisAngle']))**2,19,rel_tol=1e-12)
assert math.isclose(r['VP33.5.4']['ratio'],1.25,rel_tol=1e-12)
# Independent Jones-vector projections check both sequential polarizers.
initial=np.array([1.,0.]);first=np.array([math.cos(rad(25)),math.sin(rad(25))]);second=np.array([math.cos(rad(50)),math.sin(rad(50))])
first_E=np.dot(initial,first)*first;second_E=np.dot(first_E,second)*second
assert math.isclose(60*np.dot(second_E,second_E),r['VP33.5.3']['secondIntensity'],rel_tol=1e-12)
# Fresnel reflectances independently distinguish s/p and transmitted polarization.
def reflectance(na,nb,angle):
 theta=rad(angle);trans=rad(snell(na,nb,angle));ca=math.cos(theta);cb=math.cos(trans)
 return ((na*ca-nb*cb)/(na*ca+nb*cb))**2,((nb*ca-na*cb)/(nb*ca+na*cb))**2
Rs,Rp=reflectance(1,1.73,r['VP33.6.1']['brewster'])
assert Rs>0 and Rp<1e-28 and 0<1-Rs<1-Rp
for angle in np.linspace(0,89.99,300):assert reflectance(1,1.66,float(angle))[0]>0
assert reflectance(1,1.66,r['VP33.6.3']['pBrewster'])[1]<1e-28
assert math.isclose(r['VP33.6.4']['nGlass']*math.sin(rad(36.5)),1.33*math.sin(rad(53.5)),rel_tol=1e-12)
assert math.isclose(math.sin(rad(59.2)),nw/ng,rel_tol=1e-12)
assert r['bridge']['speed']<r['bridge']['waterSpeed']
out.joinpath('guided-data-checks.json').write_text(json.dumps({'status':'passed','guidedProblems':12,'bridgingProblems':1,'results':r},ensure_ascii=False,indent=2),encoding='utf-8')
print('Verified12 Guided Practice problems and1 bridge, including independent Jones/Fresnel checks.')
