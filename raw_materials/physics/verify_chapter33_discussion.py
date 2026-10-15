"""Check relations and illustrative models behind25 qualitative source questions.

The chosen model inputs are not measurements or extra textbook data. Human source
review is required for explanatory scope and assumptions.
"""
from pathlib import Path
import math,json,re
import numpy as np
root=Path(__file__).resolve().parents[2];out=root/'qa/physics/chapter33'
c=3e8;rad=math.radians;deg=math.degrees
snell=lambda na,nb,a:deg(math.asin(na/nb*math.sin(rad(a))))
r={}
def put(n,**kw):r[f'Q33.{n}']={'status':'passed',**kw}
#1: Deliberately overestimate a homogeneous atmospheric path, not a measured delay.
n_air=1.000293;L=1e5;delay=(n_air-1)*L/c
assert 0<delay<1e-6 and delay/(8*60)<1e-8
put(1,illustrativeConstantIndexPathM=L,delayS=delay,relativeToEightMinutes=delay/(8*60))
#2/4: A flat-layer model establishes bending sign, not actual horizon corrections.
refracted=snell(1.0001,n_air,60)
assert refracted<60 and snell(1,n_air,0)==0
put(2,bendsTowardNormal=True,verticalIncidenceUnchanged=True)
f=c/589e-9;lam_g=c/(1.52*f)
assert math.isclose(f*lam_g,c/1.52,rel_tol=1e-12)
put(3,frequencyInvariant=True,periodInvariant=True,wavelengthRatio=lam_g/589e-9)
apparent_altitude=90-snell(1,n_air,89)
assert apparent_altitude>1
put(4,flatLayerApparentAltitudeGreater=True,modelNotAnAstronomicalPrediction=True)
positions=[snell(1,n,60) for n in [n_air-.0001,n_air,n_air+.0001]]
assert max(positions)>min(positions)
put(5,timeVaryingIndexChangesApparentDirection=True)
#6: Three independently invertible angle measurements recover one index.
n=1.52;ta=40;tb=snell(1,n,ta);critical=deg(math.asin(1/n));brewster=deg(math.atan(n))
recovered=[math.sin(rad(ta))/math.sin(rad(tb)),1/math.sin(rad(critical)),math.tan(rad(brewster))]
assert all(math.isclose(x,n,rel_tol=1e-12) for x in recovered)
put(6,recoveredIndexes=recovered,speeds=[c/x for x in recovered])
#7: A finite slab has a second reflected path with displaced exit point.
thickness=.005;tg=snell(1,n,50);offset=2*thickness*math.tan(rad(tg))
assert offset>0
ca=math.cos(rad(50));cb=math.cos(rad(tg))
Rs=((ca-n*cb)/(ca+n*cb))**2;Rp=((n*ca-cb)/(n*ca+cb))**2
R=(Rs+Rp)/2
assert 0<(1-R)**2*R<R
put(7,illustrativeSlabOffsetM=offset,frontIntensity=R,firstBackReflectionIntensity=(1-R)**2*R)
critical_w=deg(math.asin(1/1.333))
assert 60>critical_w and 1.333*math.sin(rad(60))>1
mirror=np.diag([1,1,-1]);object_point=np.array([.1,.2,-.15])
assert np.allclose(mirror@object_point,[.1,.2,.15])
put(8,waterToAirCriticalDeg=critical_w,mirrorImageAcrossSurface=True)
angles=np.linspace(0,89.999,1000)
assert np.max(np.sin(np.deg2rad(angles))/n)<1
put(9,noTotalInternalReflectionAirToGlass=True)
refractions=[snell(1,index,42) for index in [1.50,1.52,1.54]]
assert len(set(refractions))==3
put(10,reflectionSameIncidenceAngle=True,dispersionChangesRefraction=True)
transmission=np.cos(np.deg2rad(np.array([0.,45.,90.])))**2
assert np.allclose(transmission,[1,.5,0],atol=1e-14)
put(11,rotatingAnalyzerTransmission=transmission.tolist())
k=np.array([0.,0.,1.]);Plong=np.outer(k,k);Ptrans=np.eye(3)-Plong
assert np.linalg.matrix_rank(Plong)==1 and np.linalg.matrix_rank(Ptrans)==2
put(12,longitudinalSubspaceDimension=1,transverseSubspaceDimension=2)
normal=np.array([0.,0.,1.]);incoming=np.array([math.sin(rad(brewster)),0,-math.cos(rad(brewster))]);s=np.cross(incoming,normal);s/=np.linalg.norm(s)
assert abs(s[2])<1e-15 and abs(s[0])<1e-15
put(13,knownHorizontalReflectionPolarization=s.tolist())
up=np.array([1,0,1])/math.sqrt(2);um=np.array([-1,0,1])/math.sqrt(2)
assert abs(float(np.dot(up,um)))<1e-15
assert math.isclose(float(np.dot(up,up)),1,rel_tol=1e-12)
put(14,opposing45DegreeAxesDotProduct=float(np.dot(up,um)),sameVehicleAxesParallel=True)
#15: A rotated retarder creates a component transmitted by crossed analyzers.
alpha=rad(45);rotation=np.array([[math.cos(alpha),-math.sin(alpha)],[math.sin(alpha),math.cos(alpha)]])
Iout=[]
for delta in [0,math.pi/2]:
 J=rotation@np.diag([1,np.exp(1j*delta)])@rotation.T
 E=J@np.array([1.,0.]);Iout.append(float(abs(E[1])**2))
 assert math.isclose(float(np.vdot(E,E).real),1,rel_tol=1e-12)
assert Iout[0]<1e-28 and math.isclose(Iout[1],.5,rel_tol=1e-12)
put(15,crossedAnalyzerIntensityForZeroAndQuarterWaveRetardance=Iout)
Ehorizontal=np.array([1.,0.]);axis_vertical=np.array([0.,1.]);axis_horizontal=np.array([1.,0.])
assert np.dot(Ehorizontal,axis_vertical)==0 and np.dot(Ehorizontal,axis_horizontal)==1
put(16,turningGlassesChangesGlareProjection=True)
phis=np.linspace(0,math.pi/2,1001);intensities=.5*np.cos(phis)**2*np.sin(phis)**2
assert math.isclose(float(np.max(intensities)),.125,rel_tol=1e-12)
assert intensities[0]==0 and abs(intensities[-1])<1e-28
put(17,maximumFractionOfUnpolarizedInput=float(np.max(intensities)),requiresIntermediateAxis=True)
assert np.allclose([np.dot(Ehorizontal,a)**2 for a in [axis_horizontal,axis_vertical]],[1,0])
put(18,antennaOrientationChangesLongitudinalWireDriving=True)
#19: Integrate the full dipole pattern; equal transverse input components lose
#equal total power, although a particular observed direction selects polarization.
u,weights=np.polynomial.legendre.leggauss(48);phi=np.linspace(0,2*math.pi,128,endpoint=False)
U,Phi=np.meshgrid(u,phi,indexing='ij');dirs=np.stack([np.sqrt(1-U*U)*np.cos(Phi),np.sqrt(1-U*U)*np.sin(Phi),U],axis=-1)
integrals=[]
for dipole in [np.array([0,1,0]),np.array([0,0,1])]:
 pattern=1-np.einsum('ijk,k->ij',dirs,dipole)**2
 val=float(np.sum(weights[:,None]*pattern)*(2*math.pi/128));integrals.append(val)
 assert math.isclose(val,8*math.pi/3,rel_tol=1e-12)
observation=np.array([0.,-1.,0.])
assert np.allclose(np.array([0,1,0])-observation*np.dot(observation,[0,1,0]),0)
assert np.allclose(np.array([0,0,1])-observation*np.dot(observation,[0,0,1]),[0,0,1])
put(19,fullSolidAngleDipolePatternIntegrals=integrals,isotropicRemovalEqual=True)
#20: East=x,North=y,Up=z; a low western sun sends its beam eastward/downward.
alt=rad(15);kin=np.array([math.cos(alt),0,-math.sin(alt)]);kout=np.array([0.,0.,-1.])
Pi=np.eye(3)-np.outer(kin,kin);Po=np.eye(3)-np.outer(kout,kout);coherency=.5*Po@Pi@Po
assert coherency[0,0]<coherency[1,1] and abs(coherency[0,1])<1e-14
put(20,minimumTransmissionAxis='east-west',feetChoices=['east','west'],illustrativeEastNorthIntensities=[float(coherency[0,0]),float(coherency[1,1])])
#21: An incoherent mixture over many polarization directions has no common axis.
ang=np.linspace(0,2*math.pi,720,endpoint=False);axes=np.column_stack([np.cos(ang),np.sin(ang)])
mean=np.einsum('ni,nj->ij',axes,axes)/len(axes)
assert np.allclose(mean,.5*np.eye(2),atol=1e-14)
put(21,uniformOrientationMixture=mean.tolist(),notAUniversalCloudPolarizationPrediction=True)
blue_red=(750/380)**4
assert blue_red>15
put(22,shortToLongWavelengthRayleighScatteringRatio=blue_red,redFilterContrastClaimConditional=True)
ratios=[]
for column in [1,2]:
 Iblue=math.exp(-column);Ired=math.exp(-column/blue_red);ratios.append(Ired/Iblue)
assert ratios[1]>ratios[0]
put(23,directBeamRedBlueRatiosInConditionalModel=ratios,noUniversalSunsetSunriseOrdering=True)
#24: Two neighboring front points advance at distinct speeds. Their forward
#normal tilts toward the slower layer.
day_tangent=np.array([1.-2.,1.]);night_tangent=np.array([2.-1.,1.])
forward_normal=lambda tangent:np.array([tangent[1],-tangent[0]])
assert forward_normal(day_tangent)[1]>0 and forward_normal(night_tangent)[1]<0
put(24,dayRayBends='up',inversionNightRayBends='down')
incoming_angle=40;vdeep=2;vshallow=1
angle_shallow=deg(math.asin(vshallow/vdeep*math.sin(rad(incoming_angle))))
assert angle_shallow<incoming_angle
put(25,refractionTowardNormalWhenSpeedDecreases=True,smallAmplitudeWaveModel=True)
text=(root/'raw_materials/physics/translations/chapter-33/11-cau-hoi-thao-luan.md').read_text(encoding='utf-8-sig')
ids=re.findall(r'^::: exercise (Q33\.\d+)$',text,re.M)
assert ids==[f'Q33.{i}' for i in range(1,26)] and set(r)==set(ids)
assert len(re.findall(r'^::: solution Lời giải chi tiết$',text,re.M))==25
out.joinpath('discussion-data-checks.json').write_text(json.dumps({'status':'passed','discussionQuestions':25,'scope':'Relations and illustrative models; semantic source review remains necessary.','results':r},ensure_ascii=False,indent=2),encoding='utf-8')
print('Checked25 discussion arguments, including full-angle dipole integrals and polarization geometry.')
