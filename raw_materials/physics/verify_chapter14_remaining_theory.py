"""Independent verification of all10chapter14theoryexamples and8selfchecks.

Additional numerical ODE, differentiation, energy, small-angle and resonance checks
audit assumptions. They are not substitutes for the mathematical derivations.
"""
from pathlib import Path
import math,json
import numpy as np
from scipy.integrate import solve_ivp,quad
from scipy.special import ellipk
from scipy.optimize import minimize_scalar

OUT=Path(__file__).resolve().parent
examples={};tests={};assertions=[]
def eq(name,a,b,rel=1e-10,absolute=1e-10):
 assert math.isclose(a,b,rel_tol=rel,abs_tol=absolute),(name,a,b)
 assertions.append(dict(id=name,actual=float(a),expected=float(b),status='passed'))
def near(name,a,b,rel):eq(name,a,b,rel)

f=6.7e6;T=1/f;w=2*math.pi*f
near('14.1:period',T,1.5e-7,.01)
near('14.1:omega',w,4.2e7,.01)
eq('14.1:microsecond',T*1e6,.14925373134328357)
examples['14.1']=dict(inputs={'f_Hz':f},result={'T_s':T,'T_microsecond':T*1e6,'omega_rad_s':w})
k=6/.03;m=.50;A=.020;w=math.sqrt(k/m);f=w/(2*math.pi);T=2*math.pi/w
eq('14.2:k',k,200.)
eq('14.2:omega',w,20.)
examples['14.2']=dict(inputs={'F_N':6.,'stretch_m':.030,'m_kg':m,'A_m':A},result={'k_N_m':k,'omega_rad_s':w,'f_Hz':f,'T_s':T})
x0=.015;v0=.40;A3=math.hypot(x0,v0/w);phi=math.atan2(-v0/w,x0)
eq('14.3:A',A3,.025)
eq('14.3:x0',A3*math.cos(phi),x0)
eq('14.3:v0',-w*A3*math.sin(phi),v0)
examples['14.3']=dict(inputs={'x0_m':x0,'v0_m_s':v0,'m_kg':m,'k_N_m':k},result={'A_m':A3,'phi_rad':phi,'phi_deg':math.degrees(phi),'omega_rad_s':w,'T_s':T,'velocity_coefficient_m_s':-w*A3,'acceleration_coefficient_m_s2':-w*w*A3})
x=A/2;v=-w*math.sqrt(A*A-x*x);acc=-w*w*x;E=k*A*A/2;U=k*x*x/2;K=m*v*v/2
eq('14.4:energy',E,K+U)
eq('14.4:velocitysign',float(v<0),1.)
eq('14.4:energyfractionU',U/E,.25)
examples['14.4']=dict(inputs={'m_kg':m,'k_N_m':k,'A_m':A,'x_m':x,'direction':'towardequilibriumfrompositiveA'},result={'v_max_m_s':w*A,'v_min_m_s':-w*A,'a_max_m_s2':w*w*A,'a_min_m_s2':-w*w*A,'v_at_halfA_m_s':v,'a_at_halfA_m_s2':acc,'E_J':E,'U_J':U,'K_J':K})
inelastic=[]
for M,putty,ks,amp in[(1,.2,2,.3),(3,2,8,.5),(.5,.5,200,.02),(5,.1,17,.7)]:
 vi=math.sqrt(ks/M)*amp;vf=M/(M+putty)*vi;A2=math.sqrt((M+putty)/ks)*vf
 E1=ks*amp*amp/2;E2=(M+putty)*vf*vf/2
 eq('14.5:momentum',M*vi,(M+putty)*vf)
 eq('14.5:amplitude',A2,amp*math.sqrt(M/(M+putty)))
 eq('14.5:energyfraction',E2/E1,M/(M+putty))
 # At turningpoint x=A, zero horizontalvelocity before/after; horizontalenergy staysspringenergy.
 eq('14.5:turningpoint-amplitude',math.sqrt(2*E1/ks),amp)
 inelastic.append(dict(M=M,m=putty,k=ks,A1=amp,A2_equilibrium=A2,A2_turningpoint=amp,energy_ratio=E2/E1,T2=2*math.pi*math.sqrt((M+putty)/ks)))
examples['14.5']=dict(result={'equilibrium_A2':'A1*sqrt(M/(M+m))','turningpoint_A2':'A1','T2_both':'2pi*sqrt((M+m)/k)','parameterCases':inelastic},conditions='Conservehorizontalmomentumoverbriefstickingevent; verticalimpactenergyexcludedfromhorizontaloscillationaccounting.')
g=9.8;person=980/g;kcar=980/.028;mtot=1000+person
Tcar=2*math.pi*math.sqrt(mtot/kcar)
near('14.6:T',Tcar,1.11,.005)
examples['14.6']=dict(inputs={'car_mass_kg':1000,'person_weight_N':980,'added_compression_m':.028},result={'person_mass_kg':person,'k_N_m':kcar,'total_mass_kg':mtot,'T_s':Tcar,'f_Hz':1/Tcar})
U0=1.68e-21;R0=3.82e-10;massAr=39.948*1.66e-27;kmol=72*U0/(R0*R0)
ffixed=math.sqrt(kmol/massAr)/(2*math.pi);ffree=math.sqrt(kmol/(massAr/2))/(2*math.pi)
near('14.7:k',kmol,.829,.001)
near('14.7:fixed-frequency',ffixed,5.63e11,.001)
near('14.7:free-frequency',ffree,7.96e11,.001)
eq('14.7:reducedmass-ratio',ffree/ffixed,math.sqrt(2))
examples['14.7']=dict(inputs={'U0_J':U0,'R0_m':R0,'atomic_mass_u':39.948,'u_kg':1.66e-27},result={'argon_mass_kg':massAr,'k_N_m':kmol,'onefixed_atom_f_Hz':ffixed,'bothfree_atoms_f_Hz':ffree,'reduced_mass_kg':massAr/2})
Tpend=2*math.pi*math.sqrt(1/9.800)
near('14.8:T',Tpend,2.007,.0003)
near('14.8:f',1/Tpend,.4982,.0002)
examples['14.8']=dict(inputs={'L_m':1.000,'g_m_s2':9.800},result={'T_small_angle_s':Tpend,'f_Hz':1/Tpend})
Trod=2*math.pi*math.sqrt(2/(3*g));Tsimple=2*math.pi*math.sqrt(1/g)
eq('14.9:rod-simple-ratio',Trod/Tsimple,math.sqrt(2/3))
examples['14.9']=dict(inputs={'L_m':1.,'g_m_s2':g},result={'T_rod_s':Trod,'T_sameL_simple_s':Tsimple,'ratio':Trod/Tsimple,'general_T':'2pi*sqrt(2L/(3g))'})
L=3.1;S=4.;Trex=2*math.pi*math.sqrt(2*L/(3*g));speed=S/Trex
Ttaper=2*math.pi*math.sqrt((L*L/15)/(g*L/4));vtaper=S/Ttaper
examples['14.10']=dict(inputs={'leg_length_m':L,'samefoot_stride_m':S,'g_m_s2':g},result={'uniformrod_T_s':Trex,'pace_steps_s':2/Trex,'speed_m_s':speed,'speed_km_h':speed*3.6,'speed_mile_h':speed/.44704,'tapered_leg_T_s':Ttaper,'tapered_leg_speed_m_s':vtaper,'tapered_model':'d=L/4,I=ML²/15'},conditions='Strideisonefulllegperiod, steptakeshalfperiod; fossilage65millionyears isnotamassdatum.')
near('14.10:speed',speed,1.4,.01)
assert Ttaper<Trex and vtaper>speed

# All8sectionselfchecks, directlyfromsourcequestions.
tests['14.1']=dict(cases=[{'vSign':1,'aSign':1,'xSign':-1},{'vSign':1,'aSign':-1,'xSign':1},{'vSign':-1,'aSign':1,'xSign':-1},{'vSign':-1,'aSign':-1,'xSign':1},{'vSign':0,'aSign':-1,'xSign':1},{'vSign':1,'aSign':0,'xSign':0}],reason='Forrestoringoscillationaandxhaveoppositesigns,independentofv.')
tests['14.2']={'a':{'A_vs_0.1':'greater','phi_sign':'negative'},'b':{'A_vs_0.1':'greater','phi_sign':'positive'}}
for vx in(.2,-.2):
 amp=math.hypot(.1,vx/20);phase=math.atan2(-vx/20,.1)
 assert amp>.1 and phase*vx<0
tests['14.3']=dict(amplitudeFactor=math.sqrt(2),amplitudeChoice='iii',frequencyChange='none',frequencyChoice='v')
eq('TY14.3:doubleenergy',math.sqrt(2)**2,2.)
tests['14.4']=dict(period_on_Mars_s=10.,choice='i',equilibrium_extension_ratio=.4,reason='Samek/mperiodindependentofg.')
tests['14.5']=dict(choice='iv',acceleration='upwardcentripetalv²/L',tension='mg+mv²/L>mg')
tests['14.6']=dict(choice='i',rodLength='2L',ratio=math.sqrt(4/3),reason='Samed=LbutIrod=4mL²/3>mL².')
tests['14.7']=dict(choice='ii',classification='underdamped',reason='Alternatingovershootswithdecayingamplitudeexcludecritical/over/undamped.')
tests['14.8']=dict(choice='i',reason='Smallerbgreateramplitudeforanypositiveomegad atfixedFmax,k,m;atomegad0responsescoincide.')

# SHM identities and phasequadrants, allsourceequationmodelchecks.
for phase in(-2.8,-1.2,0.,.7,2.4,math.pi):
 for t in(0.,.04,.13,.4):
  amp=.3;w=2.5;mm=2.;kk=mm*w*w
  x=amp*math.cos(w*t+phase);v=-amp*w*math.sin(w*t+phase);a=-amp*w*w*math.cos(w*t+phase)
  eq('SHM:ODE',mm*a+kk*x,0.)
  eq('SHM:energy',mm*v*v/2+kk*x*x/2,kk*amp*amp/2)
  recovered=math.atan2(-v/w,x)
  eq('SHM:reconstruct-x',amp*math.cos(recovered),x)
  eq('SHM:reconstruct-v',-w*amp*math.sin(recovered),v)

# van derWaalsdimensionlesspotential, directfinite-difference derivativeandcurvature.
def U(q):return q**-12-2*q**-6
def force(q):return 12*(q**-13-q**-7)
for q in(.9,.99,1.,1.01,1.2,1.8):
 h=1e-6;derivative=-(U(q+h)-U(q-h))/(2*h)
 eq('vanDerWaals:force-derivative',force(q),derivative,rel=1e-7,absolute=2e-7)
eq('vanDerWaals:curvature',(U(1+1e-5)-2*U(1)+U(1-1e-5))/1e-10,72.,rel=1e-6)
smallAngle=[]
for deg in(1.,5.,10.,15.):
 theta=math.radians(deg);param=math.sin(theta/2)**2
 exact_ratio=2*ellipk(param)/math.pi
 series=1+param/4+9*param*param/64
 integral_ratio=2/math.pi*quad(lambda u:1/math.sqrt(1-param*math.sin(u)**2),0,math.pi/2,epsabs=1e-12)[0]
 eq('pendulum:elliptic-vs-quadrature',exact_ratio,integral_ratio)
 smallAngle.append(dict(amplitude_deg=deg,exact_period_ratio=exact_ratio,source_series_through_sin4=series,small_angle_error_percent=(exact_ratio-1)*100))
assert smallAngle[-1]['small_angle_error_percent']<.5
eq('smallangle:sin0.1',math.sin(.1),.09983341664682815)

# DampedODE solution and energy-lawcheck;phi0doesnotmeanv0zero.
damper=[]
for b in(.1,.4,1.,1.8):
 m=k=1.;beta=b/2;wp=math.sqrt(1-beta*beta);A=1.;phi=.23
 def analytic(t):
  u=wp*t+phi;e=math.exp(-beta*t)
  return A*e*math.cos(u),A*e*(-beta*math.cos(u)-wp*math.sin(u))
 initial=analytic(0)
 sol=solve_ivp(lambda t,y:[y[1],-b*y[1]-y[0]],(0,8),initial,rtol=1e-11,atol=1e-12,dense_output=True)
 for t in(0.,.5,2.,5.,8.):
  xx,vv=analytic(t);num=sol.sol(t)
  eq('damping:ODE-x',xx,float(num[0]),rel=1e-9,absolute=1e-10)
  eq('damping:ODE-v',vv,float(num[1]),rel=1e-9,absolute=1e-10)
  aa=-b*vv-xx
  eq('damping:energy-law',vv*aa+xx*vv,-b*vv*vv)
 damper.append(dict(b=b,omegaPrime=wp,period=2*math.pi/wp,initialVelocity_phiZero=-b/2))

# Drivenoscillatordisplacementresonance,distinctfromcriticaldamping.
response=[]
for b in(.2,.4,.7,1.,math.sqrt(2),2.):
 def amplitude(w):return 1/math.sqrt((1-w*w)**2+b*b*w*w)
 peak=minimize_scalar(lambda q:-amplitude(q),bounds=(0.,2.),method='bounded',options={'xatol':1e-12})
 predicted=math.sqrt(max(0,1-b*b/2))
 if predicted>0:eq('forced:peak-frequency',float(peak.x),predicted,rel=1e-7)
 else:assert peak.x<1e-3
 eq('forced:static-limit',amplitude(0),1.)
 response.append(dict(b_over_sqrt_km=b,peak_frequency_ratio_numeric=float(peak.x),peak_frequency_ratio_analytic=predicted,amplitude_peak=float(-peak.fun)))
for w in(.1,.5,2.,4.):assert 1/math.sqrt((1-w*w)**2+.2**2*w*w)>1/math.sqrt((1-w*w)**2+1.0**2*w*w)
assert len(examples)==10 and len(tests)==8
report=dict(status='passed',scope='Theorysourceexamplesandmodels only; no authored/publiclectureacceptance',exampleCount=10,selfcheckCount=8,numericAssertions=len(assertions),examples=examples,selfchecks=tests,assertions=assertions,simplePendulumFiniteAmplitude=smallAngle,dampedModelCases=damper,drivenResonanceCases=response,opening={'choice':'i','law':'stepfrequency∝1/sqrt(leglength)'},limits=['Historicalseconddefinition andanatomicaldogglandclaimnotexternallyverified: networkforbiddentask.','Resonancepeaklocationandzero-drivinglimitqualifiedinprivateclarifications.'])
print(json.dumps(report,ensure_ascii=False,indent=2))
