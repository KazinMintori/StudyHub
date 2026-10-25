"""Source-first Chapter15 VP/Q/bridge calculations. No authored values imported."""
from pathlib import Path
import json,math
QA=Path(r'C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-remaining/ch15-exercises-guided')
records={}; checks=[]
def put(u,**values): records[u]=values
def ck(u,name,condition,**values):
    checks.append(dict(unit=u,name=name,passed=bool(condition),values=values))
    assert condition,(u,name,values)
def eq(u,name,a,b,tol=1e-10): ck(u,name,math.isclose(a,b,rel_tol=tol,abs_tol=1e-11),actual=a,expected=b)
pi=math.pi
u='VP15.3.1'; T=5.10; lam=30.5; A=1.00
put(u,T=T,A=A,lambda_=lam,f=1/T,v=lam/T,omega=2*pi/T,k=2*pi/lam)
eq(u,'phase-speed',records[u]['omega']/records[u]['k'],records[u]['v'])
u='VP15.3.2'; v=245.; f=125.; lam=3.
put(u,T=1/f,lambda_a=v/f,f_b=v/lam,omega_b=2*pi*v/lam)
eq(u,'a-dispersion',f*records[u]['lambda_a'],v); eq(u,'b-dispersion',records[u]['f_b']*lam,v)
u='VP15.3.3'; mu=.0650; F=800.; f=25.; A=.005; v=math.sqrt(F/mu); w=2*pi*f; k=w/v; x=2.50
put(u,v=v,lambda_=v/f,omega=w,k=k,x=x,phaseDelay=k*x,A=A)
y=lambda xx,t:A*math.cos(k*xx-w*t)
eq(u,'driven-end-initial-displacement',y(0,0),A); eq(u,'driven-end-initial-transverse-velocity',A*w*math.sin(0),0)
for t in [.001,.02,.06]: eq(u,'phase-travels-positive-x-'+str(t),y(v*t,t),A)
eq(u,'retarded-boundary-value',y(x,.09),y(0,.09-x/v))
u='VP15.3.4'; F=25.; f=45.; d=.400; lam=2*d; v=f*lam
put(u,lambda_=lam,v=v,mu=F/v**2)
eq(u,'nearest-opposite-phase',2*pi*d/lam,pi)
u='VP15.5.1'; F=600.; L=50.; m=2.50; T=.575; A=.0300; mu=m/L; w=2*pi/T; v=math.sqrt(F/mu); P=.5*mu*v*w*w*A*A
put(u,mu=mu,v=v,omega=w,Pavg=P,Pmax=2*P)
u='VP15.5.2'; mu=5.55e-4; F=185.; f=256.; Pmax=5.20; w=2*pi*f; v=math.sqrt(F/mu); A=math.sqrt(Pmax/(mu*v*w*w))
put(u,v=v,omega=w,A=A,Pavg=Pmax/2)
eq(u,'maximum-not-mean-power',mu*v*w*w*A*A,Pmax)
u='VP15.5.3'; P=8.; r=2.; I=.045
put(u,I=P/(4*pi*r*r),r=math.sqrt(P/(4*pi*I)))
u='VP15.5.4'; radius=.005; P=2.50e-6; r=1.50; I=P/(4*pi*r*r); area=pi*radius**2
put(u,I=I,area=area,powerAtOneMembrane=I*area,energyInOneSecond=I*area)
eq(u,'geometrical-fraction',I*area/P,radius**2/(4*r*r))
u='VP15.8.1'; node=.125; f=256.; B=1.40e-3; lam=2*node; w=2*pi*f
put(u,lambda_=lam,v=f*lam,B=B,omega=w,vymax=w*B,aymax=w*w*B,componentAmplitude=B/2)
eq(u,'standing-amplitude-is-antinode-amplitude',2*records[u]['componentAmplitude'],B)
u='VP15.8.2'; f1=196.; mu=2.29e-3; L=.641; v=2*L*f1
put(u,v=v,F=mu*v*v)
u='VP15.8.3'; L=3.; v=96.; F=175.; n=5; lam=2*L/n
put(u,lambda_=lam,f=v/lam,mu=F/v**2)
eq(u,'five-half-wavelengths-fit',5*lam/2,L)
u='VP15.8.4'; L=.500; mu=1.17e-3; f2=512.; f1=f2/2; v=f2*L; c=344.
put(u,f1=f1,vString=v,F=mu*v*v,lambdaSound=c/f1)
eq(u,'second-harmonic',2*f1,f2)
# Models and counterexamples for every discussion question.
u='Q15.1'; F=25.; mu=.01; v=math.sqrt(F/mu); f1=5.; f2=10.
put(u,v=v,lambda1=v/f1,lambda2=v/f2)
eq(u,'different-frequencies-same-speed',f1*(v/f1),f2*(v/f2))
ck(u,'same-frequency-forces-same-wavelength',v/f1==v/f1)
ck(u,'amplitude-independent-in-linear-string-model',math.sqrt(F/mu)==v)
u='Q15.2'; timeRatio=6/2; forceRatio=1/timeRatio**2
put(u,newTensionOverF=forceRatio); eq(u,'tripled-time-at-one-ninth-tension',1/math.sqrt(forceRatio),3)
u='Q15.3'; F=20.; mu=.02; A=.01; w=10.; k=w/math.sqrt(F/mu)
put(u,kineticMaxDensity=.5*mu*(A*w)**2,potentialMaxDensity=.5*F*(A*k)**2)
eq(u,'traveling-wave-equal-kinetic-and-elastic-density',records[u]['kineticMaxDensity'],records[u]['potentialMaxDensity'])
u='Q15.4'; aRatio=.6
put(u,amplitudeRatio=aRatio,energyFluxRatio=aRatio**2); ck(u,'amplitude-reduction-lowers-energy-flux',aRatio**2<1)
u='Q15.5'; F=8.; mu=.02
put(u,v=math.sqrt(F/mu)); eq(u,'linear-transport-speed-independent-of-amplitude',math.sqrt(F/mu),20.)
u='Q15.6'; g=9.8; depths=[4.,1.]
put(u,depths=depths,shallowWaterSpeeds=[math.sqrt(g*h) for h in depths]); ck(u,'shallower-wave-slower',math.sqrt(g*depths[1])<math.sqrt(g*depths[0]))
ck(u,'crest-deeper-column-faster-than-trough-in-shallow-water-model',math.sqrt(g*(1+.2))>math.sqrt(g*(1-.2)))
u='Q15.7'; E=1.e8; rho=1000.
put(u,longitudinalSpeedExample=math.sqrt(E/rho)); ck(u,'positive-longitudinal-restoring-elasticity',E>0 and rho>0)
u='Q15.8'; A=.02; w=10.; v=20.; samples=[abs(A*w*math.sin(p)) for p in [0,pi/2,pi]]
put(u,constantWaveSpeed=v,variableParticleSpeeds=samples); ck(u,'particle-and-wave-speeds-distinct',samples[0]==0 and samples[1]>0 and v>max(samples))
u='Q15.9'; muThin=.001; muThick=.004; F=40.; L=.4; vThin=math.sqrt(F/muThin); vThick=math.sqrt(F/muThick)
put(u,thinToThickSpeed=vThin/vThick,thinToThickFundamental=(vThin/(2*L))/(vThick/(2*L)))
ck(u,'thin-string-faster-higher-at-equal-LF',vThin>vThick)
u='Q15.10'; C=3.; N=10000; avg=sum(C*math.sin(2*pi*i/N)**2 for i in range(N))/N
put(u,Pmean=avg,Pmax=C); eq(u,'positive-average-of-square',avg,C/2)
# Direction is signed, not power destruction.
eq(u,'negative-x-wave-has-negative-oriented-flux',-avg,-C/2)
u='Q15.11'; F=30.; mu1=.003; mu2=.012; f=20.; v1=math.sqrt(F/mu1); v2=math.sqrt(F/mu2)
put(u,speed1=v1,speed2=v2,frequencyBoth=f,lambda1=v1/f,lambda2=v2/f)
eq(u,'frequency-continuity',v1/records[u]['lambda1'],v2/records[u]['lambda2'])
ck(u,'denser-side-slower-shorter-wavelength',v2<v1 and records[u]['lambda2']<records[u]['lambda1'])
u='Q15.12'; g=9.8; mu=.1; z=[.1,.4,.9]; speeds=[math.sqrt(g*s) for s in z]
put(u,positionsAboveBottom=z,speeds=speeds); ck(u,'speed-increases-upward',all(a<b for a,b in zip(speeds,speeds[1:])))
for s in z: eq(u,'weight-below-determines-tension-'+str(s),mu*speeds[z.index(s)]**2,mu*g*s)
u='Q15.13'; F=20.; A=.01; w=15.; k=3.; x=.13; t=.08; phi=k*x-w*t; yx=-k*A*math.sin(phi); yt=w*A*math.sin(phi); P=-F*yx*yt
put(u,localParticleVelocity=yt,localPowerAlongString=P); ck(u,'transverse-work-transmits-positive-longitudinal-energy-flux',P>0)
u='Q15.14'; F=20.; B=.02; k=pi; w=math.sqrt(F/.1)*k
flux=lambda x,t:F*B*B*k*w*math.sin(k*x)*math.cos(k*x)*math.sin(w*t)*math.cos(w*t)
nodeFlux=[flux(0,t) for t in [.02,.04,.06]]; interior=[flux(.25,t) for t in [pi/(4*w),3*pi/(4*w)]]
put(u,nodeFluxes=nodeFlux,interiorFluxes=interior)
ck(u,'node-transfer-identically-zero',all(p==0 for p in nodeFlux))
ck(u,'standing-wave-local-transfer-not-identically-zero',interior[0]>0 and interior[1]<0)
avg=sum(flux(.25,2*pi*i/(10000*w)) for i in range(10000))/10000
eq(u,'standing-wave-time-average-flux-zero',avg,0)
u='Q15.15'; A=2.; B=1.; w1=3.; w2=4.; v=5.; k1=w1/v; k2=w2/v
put(u,unequalAmplitudeEnvelopeMin=abs(A-B),unequalAmplitudeEnvelopeMax=A+B,differentFrequencyPatternSpeed=(w1-w2)/(k1+k2))
ck(u,'unequal-amplitudes-have-no-fixed-nodes',abs(A-B)>0)
ck(u,'unequal-frequencies-drift',records[u]['differentFrequencyPatternSpeed']!=0)
ck(u,'equal-case-can-have-standing-nodes',abs(A-A)==0)
u='Q15.16'; L0=.10; springK=20.; mass=.005; lengths=[.12,.18]
ff=lambda L:.5*math.sqrt(springK*(L-L0)/(mass*L))
put(u,model='Hookean tension k(L-L0), fixed band mass; not an empirical rubber law',lengths=lengths,modelFrequencies=[ff(L) for L in lengths])
ck(u,'increased-length-can-increase-frequency-if-tension-rises',ff(lengths[1])>ff(lengths[0]))
constantTension=1.; freqConst=lambda L:.5*math.sqrt(constantTension/(mass*L))
ck(u,'length-change-alone-does-not-fix-observed-trend',freqConst(lengths[1])<freqConst(lengths[0]))
u='Q15.17'; forceRatios=[4.,16.]
put(u,oneOctaveTensionRatio=4,twoOctavesTensionRatio=16)
eq(u,'one-octave-frequency',math.sqrt(forceRatios[0]),2); eq(u,'two-octaves-frequency',math.sqrt(forceRatios[1]),4)
u='Q15.18'; middleShapes={str(n):math.sin(n*pi/2) for n in range(1,7)}
put(u,middleModeDisplacements=middleShapes,lowestAllowedHarmonic=2)
ck(u,'touch-suppresses-odd-modes',all(abs(math.sin(n*pi/2))>.99 for n in [1,3,5]))
ck(u,'even-modes-have-central-node',all(abs(math.sin(n*pi/2))<1e-12 for n in [2,4,6]))
u='Q15.19'; k=2.; w=3.; t=.17; x=0
horizontal=math.sin(k*x)*math.sin(w*t); vertical=math.cos(k*x)*math.cos(w*t)
put(u,wallHorizontalDisplacement=horizontal,wallVerticalDisplacement=vertical)
ck(u,'rigid-wall-horizontal-node-vertical-antinode',horizontal==0 and abs(math.cos(k*x))==1 and vertical!=0)
u='Q15.20'; v=100.; Lshort=.3; Llong=.6
put(u,shortToLongFundamentalRatio=(v/(2*Lshort))/(v/(2*Llong)))
eq(u,'longer-string-lower-frequency',records[u]['shortToLongFundamentalRatio'],2)
u='Q15.21'; L=.6; shorter=.45; v=120.
put(u,frequencyRatio=(v/(2*shorter))/(v/(2*L)))
ck(u,'fret-shortens-length-and-raises-pitch',shorter<L and records[u]['frequencyRatio']>1)
u='BR15'; L=1.7; m=.3; omega=4.; mu=m/L
F=lambda r:.5*mu*omega**2*(L*L-r*r)
v=lambda r:omega*math.sqrt(max(0,L*L-r*r)/2)
for frac in [0,.2,.6,.9,1.]:
    r=frac*L; mout=mu*(L-r); rcm=(L+r)/2
    eq(u,'whole-outer-portion-force-'+str(frac),F(r),mout*omega**2*rcm)
    eq(u,'wave-speed-'+str(frac),mu*v(r)**2,F(r))
    if frac<1:
        h=L*1e-6
        numerical=(F(r+h)-F(r-h))/(2*h)
        eq(u,'differential-force-'+str(frac),numerical,-mu*omega**2*r,tol=1e-8)
ck(u,'maxima-at-held-end-minima-at-free-end',F(0)>F(L) and F(L)==0 and v(0)>v(L) and v(L)==0)
# r=L sin(theta) regularizes the integrable free-end singularity.
N=10000; dt=pi/(2*N); total=0.
for i in range(N):
    theta=(i+.5)*dt; r=L*math.sin(theta); drdtheta=L*math.cos(theta)
    total+=(drdtheta/v(r))*dt
expected=pi/(math.sqrt(2)*omega)
put(u,Lsample=L,mSample=m,omegaSample=omega,FatAnchor=F(0),vAtAnchor=v(0),transitTimeQuadrature=total,transitTimeFormula=expected)
eq(u,'endpoint-regularized-transit-quadrature',total,expected,tol=1e-7)
ck(u,'units-time-only-inverse-omega',expected>0)
for L2,m2 in [(L*2,m),(L,m*2),(L/2,m*3)]:
    mu2=m2/L2; wavet=lambda r:math.sqrt((.5*mu2*omega**2*(L2**2-r*r))/mu2)
    midpoint=L2/2
    eq(u,'mass-length-cancel-in-scaled-integrand-'+str((L2,m2)),L2/wavet(midpoint),math.sqrt(2)/(omega*math.sqrt(1-.5**2)))
eq('VP15.5.1','average-power-coefficient',2*records['VP15.5.1']['Pavg']/(records['VP15.5.1']['omega']**2*.03**2),math.sqrt(.05*600))
eq('VP15.5.3','inverse-square-power',records['VP15.5.3']['I']*4*pi*2**2,8.)
eq('VP15.5.3','inverse-square-distance',8/(4*pi*records['VP15.5.3']['r']**2),.045)
eq('VP15.8.2','tension-wave-speed',records['VP15.8.2']['F']/records['VP15.8.2']['v']**2,2.29e-3)
# Additional field checks use analytic derivatives and independent differences.
u='VP15.3.3'; A=.005; w=50*pi; k=records[u]['k']; speed=records[u]['v']
for time in [.007,.013,.031]:
    eq(u,'negative-direction-phase-counterexample-'+str(time),A*math.cos(k*(-speed*time)+w*time),A)
    ck(u,'wrong-sign-does-not-follow-positive-wave-'+str(time),not math.isclose(A*math.cos(k*(speed*time)+w*time),A,abs_tol=1e-7))
u='Q15.10'; F=24.; mu=.03; speed=math.sqrt(F/mu); A=.012; k=1.7; w=k*speed
for direction in [1,-1]:
    x=.37; time=.023; phi=k*x-direction*w*time
    yx=-A*k*math.sin(phi); yt=direction*A*w*math.sin(phi)
    flux=-F*yx*yt
    expected=direction*F*k*w*A*A*math.sin(phi)**2
    eq(u,'signed-flux-from-derivatives-'+str(direction),flux,expected)
    ck(u,'flux-follows-wave-direction-'+str(direction),flux*direction>0)
eq(u,'doubling-amplitude-quadruples-power',(2*A)**2/A**2,4)
u='Q15.14'; F=24.; mu=.03; B=.018; k=1.7; w=k*math.sqrt(F/mu)
def field_u(x,time):
    yt=-B*w*math.sin(k*x)*math.sin(w*time)
    yx=B*k*math.cos(k*x)*math.cos(w*time)
    return .5*mu*yt*yt+.5*F*yx*yx
def field_P(x,time):
    yt=-B*w*math.sin(k*x)*math.sin(w*time)
    yx=B*k*math.cos(k*x)*math.cos(w*time)
    return -F*yx*yt
for x,time in [(.31,.017),(.61,.031),(.93,.047)]:
    h=1e-6
    derivative_u=(field_u(x,time+h)-field_u(x,time-h))/(2*h)
    derivative_P=(field_P(x+h,time)-field_P(x-h,time))/(2*h)
    ck(u,'local-energy-continuity-'+str((x,time)),abs(derivative_u+derivative_P)<1e-7,energyDerivative=derivative_u,fluxDerivative=derivative_P)
u='VP15.8.1'; B=records[u]['B']; w=records[u]['omega']; A=B/2
for phase in [0,.7,1.8]:
    # Opposite traveling waves sum to standing antinode displacement2A cos(phase).
    eq(u,'antinode-normalization-'+str(phase),A*math.cos(phase)+A*math.cos(phase),B*math.cos(phase))
u='BR15'; omega=records[u]['omegaSample']
eq(u,'transit-inverse-angular-speed',pi/(math.sqrt(2)*(2*omega)),records[u]['transitTimeFormula']/2)

# Check every displayed numerical result against independently computed values.
rounded={
 'VP15.3.1':{'f':.196,'v':5.98,'omega':1.23,'k':.206},
 'VP15.3.2':{'T':.008,'lambda_a':1.96,'f_b':81.7,'omega_b':513.},
 'VP15.3.3':{'v':111.,'lambda_':4.44,'k':1.41590,'phaseDelay':3.53974,'A':.005},
 'VP15.3.4':{'lambda_':.800,'v':36.,'mu':.0193},
 'VP15.5.1':{'omega':10.9,'mu':.0500,'Pavg':.294},
 'VP15.5.2':{'A':.00250,'Pavg':2.60},
 'VP15.5.3':{'I':.159,'r':3.8},
 'VP15.5.4':{'area':7.85e-5,'I':8.84e-8,'powerAtOneMembrane':6.94e-12,'energyInOneSecond':6.94e-12},
 'VP15.8.1':{'lambda_':.250,'v':64.,'vymax':2.25,'aymax':3.62e3},
 'VP15.8.2':{'v':251.,'F':145.},
 'VP15.8.3':{'lambda_':1.20,'f':80.,'mu':.0190},
 'VP15.8.4':{'f1':256.,'vString':256.,'F':76.7,'lambdaSound':1.34}}
for unit,values in rounded.items():
    for key,target in values.items():
        tolerance=.012 if unit=='VP15.5.3' and key=='r' else .004
        ck(unit,'draft-rounded-'+key,math.isclose(records[unit][key],target,rel_tol=tolerance),computed=records[unit][key],draft=target,relativeTolerance=tolerance)

assert len(records)==34 and len({c['unit'] for c in checks})==34
result={'status':'passed','unitCount':34,'assertions':len(checks),'values':records,'checks':checks,'notes':'Qualitative counterexamples are model calculations. No empirical rubber-band experiment, structural test or audio measurement is claimed.'}
print(json.dumps(result,ensure_ascii=False,indent=2))
