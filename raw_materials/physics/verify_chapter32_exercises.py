"""Independent computations for48 source exercises, including missing-data models."""
from pathlib import Path
import json,math
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
c=3.00e8;mu0=4*math.pi*1e-7;eps0=1/(mu0*c*c)
G=6.6743e-11;Mearth=5.9722e24;Rearth=6.371e6;Msun=1.98847e30
r={}
def put(n,**data):r[str(n)]={'status':'passed',**data}
def fields(I):
 E=math.sqrt(2*I/(eps0*c));B=E/c
 assert math.isclose(.5*E*B/mu0,I,rel_tol=1e-12)
 return E,B
def fromE(E):return .5*eps0*c*E*E
put(1,timeMoonS=384000e3/c,distanceSiriusKm=c*8.61*365.25*86400/1e3,yearDays=365.25)
cross=lambda a,b:np.cross(a,b).tolist()
put(2,directions=[cross([1,0,0],[0,1,0]),cross([0,-1,0],[1,0,0]),cross([0,0,1],[-1,0,0]),cross([0,1,0],[0,0,-1])])
put(3,magneticT=4/c,direction=[0,1,0])
put(4,directions=[cross([1,0,0],[0,-1,0]),cross([0,1,0],[1,0,0]),cross([0,0,-1],[-1,0,0]),cross([1,0,0],[0,0,-1])])
put(5,frequencyHz=c/1e-10,periodS=1e-10/c,waveNumber=2*math.pi/1e-10)
put(6,UVAfrequencyHz=[c/400e-9,c/320e-9],UVBfrequencyHz=[c/320e-9,c/280e-9],
    UVAwaveNumber=[2*math.pi/400e-9,2*math.pi/320e-9],UVBwaveNumber=[2*math.pi/320e-9,2*math.pi/280e-9],
    biologyCorrection='UVB drives skin vitaminD synthesis')
put(7,frequencyHz=[c/5e3,c/5e-6,c/5e-9],wavelengthM=[c/6.5e21,c/590e3])
put(8,frequencyHz=c/435e-9,BmaxT=2.7e-3/c,k=2*math.pi/435e-9,omega=2*math.pi*c/435e-9,
    propagation='-z',electricDirection='+x',magneticDirection='-y',phase='kz+omega*t')
put(9,propagation='+y',wavelengthM=2*math.pi*c/12.65e12,BmaxT=3.10e5/c,k=12.65e12/c,
    electricDirection='+z',magneticDirection='+x')
put(10,speed=5.97e15/1.99e7,Emax=375,Bmax=375/(5.97e15/1.99e7),
    frequencyHz=5.97e15/(2*math.pi),wavelengthM=2*math.pi/1.99e7,periodS=2*math.pi/5.97e15,
    visible=False,propagation='-x')
put(11,wavelengthM=c/830e3,k=2*math.pi*830e3/c,omega=2*math.pi*830e3,Emax=c*4.82e-11)
v=c/math.sqrt(3.64*5.18)
put(12,speed=v,wavelengthM=v/65,Bmax=7.2e-3/v)
put(13,glassWavelengthM=2.17e8/5.7e14,airWavelengthM=c/5.7e14,index=c/2.17e8,dielectric=(c/2.17e8)**2)
P,dt,N,D=2e12,4e-9,100,5e-6
I=P/N/(math.pi*(D/2)**2);E,B=fields(I)
put(14,energyPerCellJ=P*dt/N,intensity=I,Emax=E,Bmax=B,diameterM=D)
I=.05*75/(4*math.pi*.03**2);E,B=fields(I)
put(15,intensity=I,Emax=E,Bmax=B)
put(16,energyJ=eps0*c*.04**2*.5*30)
put(17,powerW=4*math.pi*(2e10)**2*5e3)
E,B=fields(1400)
put(18,Emax=E,Bmax=B,powerW=1400*4*math.pi*(1.5e11)**2)
put(19,powerW=2*math.pi*eps0*c*75**2)
I=fromE(.054)
put(20,frequencyHz=c/.354,Bmax=.054/c,intensity=I)
I=60/(4*math.pi*5**2);E,B=fields(I)
put(21,intensity=I,Emax=E,Bmax=B)
I=777e3/(2*math.pi*5000**2);E,B=fields(I)
put(22,intensity=I,pressurePa=2*I/c,Emax=E,Bmax=B,energyDensity=I/c,
    electricFraction=.5,magneticFraction=.5)
I=100;area=math.pi*(1.5e-3/2)**2;E,B=fields(I)
put(23,modelMaxPowerW=I*area,Emax=E,Bmax=B,energyPerSecondJ=I*area,thresholdWcm2=I/1e4,
    limitation='hypothetical threshold model; not a general laser viewing safety criterion')
put(24,absorbingPressure=2500/c,reflectingPressure=5000/c,
    absorbingAtm=2500/c/101325,reflectingAtm=5000/c/101325,momentumDensity=2500/c**2)
I=.5e-3/(math.pi*(.5e-3)**2);E,B=fields(I)
put(25,intensity=I,Emax=E,Bmax=B,energyDensity=I/c)
coefficient=600*math.pi*(8e-3)**2*9.8*c/2
put(26,powerPerThicknessWm=coefficient,thickness='not specified in printed source',
    powerForOneMmW=coefficient*.001,doubleRadiusFactor=4,formula='P=rho*pi*Rdisk^2*h*g*c/2')
width=5*.122/2;newwidth=width+.05
put(27,widthM=width,frequencyHz=c/.122,longerFrequencyHz=5*c/(2*newwidth))
put(28,nodalDistanceM=c/75e6/2,nearestElectricMagneticNodeM=c/75e6/4)
n=1.25/(1.5-1.25)
assert math.isclose(n,5)
assert math.isclose(n*.015,(n+1)*.0125)
put(29,lowerMode=round(n),cavityWidthM=n*.015)
# Differentiate two coupled fields with arbitrary phase and verify the in-phase result.
theta=np.linspace(0,2*math.pi,1000)
Em,Bm,k,w=3.,3./c,2.,2.*c
assert np.allclose(-k*Em*np.sin(theta),-w*Bm*np.sin(theta))
assert np.allclose(-k*Bm*np.sin(theta),-mu0*eps0*w*Em*np.sin(theta))
put(30,phase=0,amplitudeRatio=c,assumptions='positive nonzero amplitudes and omega=ck')
area=math.pi*(510e-6/2)**2;I=.250/area;E,B=fields(I)
put(31,energyJ=.250*1.5e-3,pressureAirPa=I/c,wavelengthInEyeM=810e-9/1.34,frequencyHz=c/810e-9,
    EmaxAir=E,BmaxAir=B,EmaxMedium=E/math.sqrt(1.34),BmaxMedium=B*math.sqrt(1.34),
    mediumAssumption='nonmagnetic transparent medium, unchanged transmitted intensity',spotDiameterM=510e-6)
#32.32 is a parameterized estimate, not measured data.
waterM=.237;deltaT=100-20;cp=4186;heat=waterM*cp*deltaT
time=120;cupD=.08;A=math.pi*(cupD/2)**2;power=heat/time;I=2*power/A;E,B=fields(I)
put(32,assumedRoomTemperatureC=20,assumedTimeS=time,assumedCupDiameterM=cupD,heatJ=heat,
    absorbedPowerW=power,intensity=I,Emax=E,assumptions='explicit illustrative estimates, not measured values')
I=25e3/(4*math.pi*(575e3)**2);E,B=fields(I)
put(33,intensity=I,Emax=E,Bmax=B,forceN=I*.15*.40/c)
#32.34 assumes two specified flux levels per half-cycle, then a crude energy-flow model.
radius=.02;deltaFlux=.01*math.pi*radius**2;rate=deltaFlux/.25
e=rate/(2*math.pi*radius)
# Eq32.28 is S=E cross B/mu0, not the far-field E^2 formula.
meanB=.005
Smodel=e*meanB/mu0;Pmodel=Smodel*2*math.pi*radius*.10
put(34,fluxChangeRate=rate,inducedElectricVpm=e,meanMagneticT=meanB,
    approximatePoynting=Smodel,powerW=Pmodel,
    assumptions='half-cycle change between specified flux levels; multiply approximate mean E and B; uniform cylindrical band',
    limitation='near-field quasi-static model does not determine actual radiated power; E=cB is inapplicable')
Rsun=6.96e8
I1=3.9e26/(4*math.pi*Rsun**2);I2=4*I1
put(35,surfaceIntensity=I1,halfRadiusIntensity=I2,surfacePressure=I1/c,halfRadiusPressure=I2/c,
    surfaceRadiationGasRatio=I1/c/1e4,halfRadiusRadiationGasRatio=I2/c/4.7e13,
    assumptions='all specified luminosity travels radially through each sphere without scattering')
I=5.8e-3/(math.pi*(2.5e-3/2)**2);E,B=fields(I)
put(36,Emax=E,Bmax=B,electricMeanEnergyDensity=I/(2*c),magneticMeanEnergyDensity=I/(2*c),beamEnergyJ=5.8e-3/c)
I=fromE(1.25);A=.015**2;length=1.;mass=.004
torque=(2*I/c-I/c)*A*length/2;inertia=2*mass*(length/2)**2
put(37,intensity=I,netTorqueNm=torque,momentOfInertia=inertia,angularAcceleration=torque/inertia)
put(38,Emax=3.50*10/.20)
#32.39 checks independent surface flux against Joule loss.
a,rho,current,l=.001,1.7e-8,2.,.30
ef=rho*current/(math.pi*a*a);bf=mu0*current/(2*math.pi*a)
sf=ef*bf/mu0;flux=sf*2*math.pi*a*l;joule=current**2*rho*l/(math.pi*a*a)
assert math.isclose(flux,joule,rel_tol=1e-12)
put(39,electricFormula='rho*I/(pi*a^2), axial',magneticFormula='mu0*I/(2*pi*a), azimuthal',
    poyntingFormula='rho*I^2/(2*pi^2*a^3), radial inward',powerFormula='I^2*rho*l/(pi*a^2)',testSurfacePowerW=flux,testJouleW=joule)
I=.0275;E,B=fields(I);w=2*math.pi*c/6.90
put(40,magneticAmplitude=B,inducedEmf=math.pi*.075**2*w*B)
lam=c/110e6
put(41,nodalDistanceM=lam/2,cavityLengthM=8*lam/2)
I=100;E,B=fields(I);f=4e6;w=2*math.pi*f;k=w/c;N=50;a=.1;L=78e-6;R=100.
correction=math.sin(k*a/2)/(k*a/2)
emf=N*a*a*w*B*correction
cap=1/(w*w*L);irms=emf/(math.sqrt(2)*R)
assert math.isclose(w*L,1/(w*cap),rel_tol=1e-12)
put(42,fluxAmplitudeWb=2*N*a*B/k*math.sin(k*a/2),signedFlux='negative cos(omega*t) for normal+x',
    emfAmplitudeV=emf,capacitanceF=cap,rmsCurrentA=irms,finiteApertureCorrection=correction,inductanceH=L,frequencyHz=f)
T=12*3600.;orbital=(G*Mearth*T*T/(4*math.pi**2))**(1/3);height=orbital-Rearth
I=25/(2*math.pi*height**2);E,B=fields(I)
put(43,orbitRadiusM=orbital,altitudeM=height,intensityPerFrequency=I,Emax=E,Bmax=B,
    travelTimeS=height/c,pressurePa=I/c,wavelengthM=c/1575.42e6,absorbingForceN=I/c*.015**2)
area=2*math.pi*c*G*Msun*10000/3.9e26
put(44,sailAreaM2=area,sailAreaKm2=area/1e6,reflecting=True,distanceIndependent=True)
Rlimit=3*3.9e26/(16*math.pi*c*G*Msun*3000)
put(45,radiusLimitM=Rlimit,forceRatio='Rlimit/Rparticle',distanceIndependent=True)
Ia=2.6/(math.pi*(2.6e-3/2)**2);Ib=fromE(480);Ic=.5*c/mu0*(8.7e-6)**2
Id=6e-8*c/(2*math.pi*(1.8e-3/2)**2);Ie=c*3e-7
intensities={'A':Ia,'B':Ib,'C':Ic,'D':Id,'E':Ie}
put(46,intensities=intensities,ascending=sorted(intensities,key=intensities.get))
put(47,speedFromSlope=2*1.33e-3/eps0,model='I=(eps0*c/2)*Emax^2')
f=np.array([1,1.5,2,2.5,3,3.5,4,5,6,8])*1e9
d=np.array([15.2,9.7,7.7,5.8,5.2,4.1,3.8,3.1,2.3,1.7])*.01
x=1/f
slope,intercept=np.polyfit(x,d,1)
constrained=float(np.dot(x,d)/np.dot(x,x))
assert np.isfinite(slope) and slope>0 and len(x)==10
put(48,speedFreeFit=2*slope,interceptM=intercept,speedOriginFit=2*constrained,points=10,
    frequenciesHz=f.tolist(),distanceM=d.tolist(),xAxis='1/f',yAxis='d',model='d=(c/2)*(1/f)')
assert set(r)=={str(i) for i in range(1,49)}
# Independent inverse relations and sampled identities catch sign/factor errors.
assert np.allclose(r['2']['directions'],[[0,0,1],[0,0,1],[0,-1,0],[-1,0,0]])
assert np.allclose(r['4']['directions'],[[0,0,-1],[0,0,-1],[0,1,0],[0,1,0]])
assert math.isclose(r['1']['timeMoonS']*c,384000e3,rel_tol=1e-12)
assert math.isclose(r['5']['frequencyHz']*1e-10,c,rel_tol=1e-12)
assert math.isclose(r['7']['frequencyHz'][1],6e13,rel_tol=1e-12)
assert math.isclose(r['12']['speed']**2*3.64*5.18,c*c,rel_tol=1e-12)
assert math.isclose(r['14']['energyPerCellJ']*100,2e12*4e-9,rel_tol=1e-12)
assert math.isclose(r['16']['energyJ']/(.5*30),eps0*c*.04**2,rel_tol=1e-12)
assert math.isclose(r['19']['powerW']/(4*math.pi*10**2),fromE(75/10),rel_tol=1e-12)
assert math.isclose(r['26']['doubleRadiusFactor'],(2*8e-3)**2/(8e-3)**2,rel_tol=1e-12)
assert math.isclose(r['27']['longerFrequencyHz']*2*(.305+.05)/c,5,rel_tol=1e-12)
# Flux integration over the square antenna independently checks the finite-aperture formula.
wave=r['42'];w42=2*math.pi*wave['frequencyHz'];k42=w42/c;a42=.1;N42=50
B42=math.sqrt(2*mu0*100/c)
z42=np.linspace(-a42/2,a42/2,10001)
for phase42 in [0,.2,1.3,2.8]:
 numeric_flux=N42*a42*np.trapezoid(-B42*np.cos(k42*z42-phase42),z42)
 analytic_flux=-wave['fluxAmplitudeWb']*math.cos(phase42)
 assert math.isclose(numeric_flux,analytic_flux,abs_tol=1e-15)
 expected_emf=-wave['emfAmplitudeV']*math.sin(phase42)
 numeric_emf=-N42*a42*np.trapezoid(-B42*w42*np.sin(k42*z42-phase42),z42)
 assert math.isclose(numeric_emf,expected_emf,abs_tol=1e-8)
assert math.isclose(wave['rmsCurrentA']**2*100,.5*(wave['emfAmplitudeV']/100)**2*100,rel_tol=1e-12)
orbit=r['43']['orbitRadiusM']
assert math.isclose(G*Mearth/orbit**2,4*math.pi**2*orbit/(12*3600)**2,rel_tol=1e-12)
# The sail force and dust-force balance are checked at three unrelated distances.
for distance_test in [7e10,1.5e11,4e11]:
 intensity_test=3.9e26/(4*math.pi*distance_test**2)
 sail_force=2*intensity_test*r['44']['sailAreaM2']/c
 gravity_force=G*Msun*10000/distance_test**2
 assert math.isclose(sail_force,gravity_force,rel_tol=1e-12)
 dustR=r['45']['radiusLimitM']
 mass_test=3000*4*math.pi*dustR**3/3
 rad_force=intensity_test*math.pi*dustR**2/c
 grav_force=G*Msun*mass_test/distance_test**2
 assert math.isclose(rad_force,grav_force,rel_tol=1e-12)
# Refit in scaled units with a separate linear algebra method.
scaled_x=1e9/f;cm_y=d*100
design=np.column_stack([scaled_x,np.ones(10)])
alternate_coeff=np.linalg.lstsq(design,cm_y,rcond=None)[0]
assert math.isclose(2*alternate_coeff[0]*1e7,r['48']['speedFreeFit'],rel_tol=1e-12)
assert math.isclose(alternate_coeff[1]*.01,r['48']['interceptM'],rel_tol=1e-12)
for key,value in r.items():
 assert value['status']=='passed'
out=ROOT/'qa/physics/chapter32/exercises-data-checks.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({'status':'passed','numberedExercises':48,'constants':{'c':c,'mu0':mu0,'eps0':eps0,'G':G},'results':r},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Computed48 exercises with explicit model conditions, missing thickness and all10 measured points.')
