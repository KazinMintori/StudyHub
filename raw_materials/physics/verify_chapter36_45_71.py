"""Remaining exercises, complete data sets, moving apertures and complex-wave identities."""
from pathlib import Path
import math,cmath,json
import numpy as np
from PIL import Image
root=Path(__file__).resolve().parents[2];q=root/'qa/physics/chapter36';q.mkdir(parents=True,exist_ok=True)
sin=math.sin;cos=math.cos;asin=math.asin;tan=math.tan;atan=math.atan;pi=math.pi;deg=math.degrees;rad=math.radians
r={};c=3e8
def put(i,**data):r[str(i)]=data
def sinc2(x):return 1. if x==0 else (sin(x)/x)**2
def bisect(fn,lo,hi):
 flo=fn(lo);fhi=fn(hi);assert flo*fhi<0
 for _ in range(100):
  mid=(lo+hi)/2;fm=fn(mid)
  if flo*fm<=0:hi=mid
  else:lo=mid;flo=fm
 return (lo+hi)/2
put(45,hairDiameterUm=632.8e-9/sin(atan(.0522/2/1.25))*1e6)
moving_lambda=(344-80)/960;d=moving_lambda/(2*sin(rad(11.4)))
put(46,movingWavelengthM=moving_lambda,openingSeparationM=d,stationaryFirstMinDeg=deg(asin((344/960)/(2*d))))
lam=632.8e-9;a=.0250e-3;maxm=math.floor(a/lam);previous=asin((maxm-1)*lam/a);outer=asin(maxm*lam/a);theta=(previous+outer)/2;alpha=pi*a*sin(theta)/lam
put(47,maxDarkOrder=maxm,totalDarkFringes=2*maxm,outerMinDeg=deg(outer),previousMinDeg=deg(previous),midpointApproxMaxDeg=deg(theta),approxSidePeakWm2=8.50*sinc2(alpha))
lv=380e-9;lr=750e-9;spread=rad(27);d=math.sqrt(lv**2+((lr-lv*cos(spread))/sin(spread))**2)
assert math.isclose(deg(asin(lr/d))-deg(asin(lv/d)),27,rel_tol=1e-13)
put(48,linesPerCm=1/d/100,violetDeg=deg(asin(lv/d)),redDeg=deg(asin(lr/d)))
put(49,liquidIndex=sin(rad(38.2))/sin(rad(21.6)))
D=.035/2.80;lam=c/6e14;distance=2.75
put(50,apertureMm=D*1e3,airWavelengthNm=lam*1e9,waterFeatureMm=distance*tan(asin(1.22*(lam/1.33)/D))*1e3,airFeatureMm=distance*tan(asin(1.22*lam/D))*1e3,waterIndex=1.33)
roots=[bisect(lambda z:tan(z)-z,m*pi+1e-10,(m+.5)*pi-1e-10) for m in [1,2]]
put(51,positiveMaximaGamma=roots,positiveMinimaGamma=[pi,2*pi,3*pi],anglesForWidth12LambdaDeg=[deg(asin(1/12)),deg(asin(roots[0]/(12*pi))),deg(asin(2/12))])
half=bisect(lambda z:sinc2(z)-.5,1e-10,pi-1e-10);lam=540e-9;a=.360e-3;R=1.20
put(52,halfIntensityGamma=half,firstMinMm=R*tan(asin(lam/a))*1e3,halfIntensityPositionMm=R*tan(asin(half*lam/(pi*a)))*1e3)
alpha_al=2.4e-5;deltaT=500.;W0=.00275;R=.620;sn0=sin(atan(W0/2/R));sn1=sn0/(1+alpha_al*deltaT);W1=2*R*tan(asin(sn1))
put(53,alphaPerK=alpha_al,newWidthMm=W1*1e3,changeWidthMm=(W1-W0)*1e3,differentialApproxChangeMm=-W0*alpha_al*deltaT*1e3,direction='decrease')
beta=2.65e7/c;ratio=math.sqrt((1+beta)/(1-beta))
put(54,wavelengthRatio=ratio,galaxySecondOrderDeg=deg(asin(ratio*sin(rad(18.9)))))
put(55,limitingWavelengthNm=1/(9200*100)/3*1e9,limitingAngleDeg=90)
door=.90;v_sound=344.
put(56,assumedDoorWidthM=door,speedMps=v_sound,comparableWavelengthFrequencyHz=v_sound/door,firstMinimumAt20DegFrequencyHz=v_sound/(door*sin(rad(20))))
put(57,highestFullVisibleOrder=math.floor(1/(650e3)/(750e-9)))
lam=c/1665e6;D=77000e3;theta=asin(1.22*lam/D);feature=7.2e8*math.tan(theta)
put(58,wavelengthM=lam,angleRad=theta,smallestFeatureLy=feature,smallestFeatureKm=feature*9.46e12)
theta=rad((180-50)/2);lam=2*.091e-9*sin(theta);charge=1.602176634e-19;E=54*charge;mass=9.11e-31;speed=math.sqrt(2*E/mass);fclass=speed/lam;fphase=fclass/2
put(59,braggAngleDeg=deg(theta),electronWavelengthNm=lam*1e9,kineticEnergyJ=E,classicalSpeedMps=speed,assumedClassicalFrequencyHz=fclass,initialPlanckJs=E/fclass,nonrelativisticPhaseSpeedMps=speed/2,correctedFrequencyHz=fphase,correctedPlanckJs=E/fphase,comparisonGivenPlanckJs=6.6e-34)
lam=550e-9;D=.002;R=.25;theta=asin(1.22*lam/D);s=R*tan(theta)
put(60,object50UmResolved=False,minObjectUm=s*1e6,resolutionArcmin=deg(theta)*60,limitingEffectForGivenModel='diffraction',retinalObjectLimitUm=50)
d=632.8e-9*2.50/.00153
image=np.asarray(Image.open(root/'docs/vat-ly-2/bai-giang/img/young-36/hinh-p36-61.png').convert('RGB'))
profile=image[70:110].mean(axis=2).max(axis=0);active=profile>170;groups=[];start=None
for i,on in enumerate(np.r_[active,False]):
 if on and start is None:start=i
 if not on and start is not None:
  if i-start>=5:groups.append((start+i-1)/2)
  start=None
assert len(groups)==17,groups
step=float(np.median(np.diff(groups)));center=groups[len(groups)//2];orders=[round((x-center)/step) for x in groups]
assert orders==[-9,-8,*list(range(-6,7)),8,9],orders
put(61,slitSeparationMm=d*1e3,visibleSpotCount=len(groups),visibleNominalOrders=orders,firstMissingOrder=7,intendedFirstMinimumSlitWidthMm=d/7*1e3,possibleWidthsMm=[j*d/7*1e3 for j in range(1,7)],model='First single-slit minimum at missingorder7 selects minimumwidthd/7. Positions alone allow higher diffraction orders.')
a=np.array([.78,.91,1.04,1.82,3.12,5.20,7.80,10.40,15.60])*1e-6;w=np.array([2.68,2.09,1.73,.89,.51,.30,.20,.15,.10]);R=1.5;products=a*w;individual=a*np.sin(np.arctan(w/(2*R)));plateau=np.mean(products[-4:]);lam=plateau/(2*R)
put(62,slitWidthsUm=(a*1e6).tolist(),measuredWidthsM=w.tolist(),productsMicrometerMeters=(products*1e6).tolist(),perPointExactWavelengthNm=(individual*1e9).tolist(),plateauWavelengthNm=lam*1e9,firstAnglesDeg=[deg(asin(lam/a[0])),deg(asin(lam/a[-1]))])
xs=np.array([1.,1.5,2.,2.5]);rs=np.array([.056,.085,.116,.141]);lam=562e-9;Ds=1.22*lam/np.sin(np.arctan(rs/xs));D=float(np.mean(Ds))
put(63,individualAperturesUm=(Ds*1e6).tolist(),averageApertureUm=D*1e6,ring2RadiusCm=100*tan(asin(2.23*lam/D)),ring3RadiusCm=100*tan(asin(3.24*lam/D)))
sn=sin(atan(.224/2/.300));lam_medium=1.25e-6*sn
put(64,liquidWavelengthNm=lam_medium*1e9,liquidIndex=612e-9/lam_medium)
lam=532e-9;d=20*lam;v=lam;amax=3*lam;vanish_width=d/9;first=vanish_width/(2*v)
put(65,slitSeparationUm=d*1e6,membraneSpeedUmPerS=v*1e6,maxApertureUm=amax*1e6,firstVanishTimeS=first,closingVanishTimeS=3-first,intensityFirstOrderAt1point5sRatio=sinc2(pi*amax/d),firstOrderAngleDeg=deg(asin(lam/d)),outerNinthIntensityAt1sRatio=sinc2(pi*(2*lam)*9/d),qualification='Nineteen nominal interference orders with edges at first envelope minima do not all have approximately equal intensities.')
# Challenge66: verify the closed form against actual finite sums for a grid.
checks=0
for N in range(2,22):
 for phi in [.13,.61,1.9,2.8,4.4,6.1]:
  direct=sum(cmath.exp(1j*n*phi) for n in range(N));closed=sin(N*phi/2)/sin(phi/2)*cmath.exp(1j*(N-1)*phi/2)
  assert abs(direct-closed)<1e-12;checks+=1
put(66,finiteComplexSumChecks=checks,twoSlitFactorRelativeSingleSlit=4)
for N in range(2,31):
 for j in range(1,N):assert abs(sum(cmath.exp(2j*pi*n*j/N) for n in range(N)))<1e-11
 mid=abs(sum(cmath.exp(1j*pi*n) for n in range(N)))**2
 assert math.isclose(mid,1. if N%2 else 0.,abs_tol=1e-11)
put(67,maximumNormalizedIntensity='N²',centralWidthInPhase='4π/N',halfwayIntensityNormalizedToOneSlit={'evenN':0,'oddN':1},sourceProseCorrection='Width is proportional to1/N, not inversely proportional to1/N.')
ys=np.linspace(-.5,.5,20001)
for alpha in [0.,.4,1.7,pi,5.5,8.9]:
 delta=.73;values=np.sin(delta-2*alpha*ys);numeric=float(np.trapezoid(values,ys));exact=sin(delta)*(1 if alpha==0 else sin(alpha)/alpha)
 assert abs(numeric-exact)<1e-7
put(68,independentQuadratureCases=6,symmetricOddPartIntegral=0)
put(69,choice='d')
n_water=1.33;lam=650e-9/n_water;d=lam/(2*sin(rad(39)))
put(70,waterWavelengthNm=lam*1e9,firstOrderPlaneSpacingNm=d*1e9,secondOrderPlaneSpacingNm=2*d*1e9,intendedChoiceWithFirstOrder='a',alsoPossibleChoiceWithoutOrder='d')
put(71,choice='a',bottomToTopSpacingRatio=sin(rad(37))/sin(rad(41)))
assert len(r)==27
(q/'exercises-45-71-data-checks.json').write_text(json.dumps(dict(status='passed',numberedExercises=27,results=r),indent=2),encoding='utf-8')
print(json.dumps(r,indent=2))
