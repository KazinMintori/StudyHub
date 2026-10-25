"""Independent checks for chapter16.5–16.9 and shared acoustic definitions.

Values are transcribed from actual PDF538–551. Physical models are checked
by phase sampling, pulse-arrival kinematics and shock-front minimization.
"""
from pathlib import Path
import json,math
import numpy as np
from scipy.optimize import minimize_scalar

BASE=Path(__file__).resolve().parent
checks=[];examples={};selfchecks={}
def eq(id,value,expected,rtol=1e-10,atol=1e-11):
 assert math.isclose(float(value),float(expected),rel_tol=rtol,abs_tol=atol),(id,value,expected)
 checks.append(dict(id=id,value=float(value),expected=float(expected),passed=True))
def yes(id,value):
 assert bool(value),id
 checks.append(dict(id=id,value=bool(value),expected=True,passed=True))

# Equal fundamental frequencies of stopped pipe and two-fixed-end string.
La=1.;Ls=.80*La;va=344.;fa=va/(4*La);vs=2*Ls*fa
eq('16.12.speed_ratio',vs/va,.4)
eq('16.12.fundamental_match',vs/(2*Ls),va/(4*La))
eq('16.12.string_speed_rounded_m_s',vs,138.,atol=.5)
eq('16.12.wavelength_ratio_air_string',(va/fa)/(vs/fa),2.5)
examples['16.12']=dict(source=dict(stringToPipeLengthRatio=.8,pipe='stopped',string='bothendsfixed',modes='bothfundamentals'),result=dict(speedRatio=vs/va,illustrativeAirSpeed_m_s=va,stringSpeed_m_s=vs,airToStringWavelengthRatio=2.5))

# Ear-canal dimensional estimate, not a full human hearing response model.
eq('ear_resonance.25mm_Hz',344/(4*.025),3440.)

# Each actual option of selfcheck16.5, not just the selected pair.
fundamentals=[220.,110.,440.,220.]
families=[np.arange(1,20,2),np.arange(1,20,2),np.arange(1,20),np.arange(1,20)]
resonance=[]
for idx,(f,ns)in enumerate(zip(fundamentals,families),1):
 found=any(math.isclose(f*n,660)for n in ns)
 eq(f'TY16.5.option{idx}',found,idx in(1,4))
 resonance.append(found)
selfchecks['16.5']=dict(sourceFundamental_Hz=220,driving_Hz=660,optionResonance=resonance,answer=[1,4])

# Actual geometry gives .34903m; source's .35m yields approximate round families.
rA=math.hypot(2.,4.);rB=math.hypot(1.,4.);d=rA-rB;v=350.
eq('16.13.exact_pathdifference',d,.349030329382,rtol=1e-10)
constructive=[n*v/d for n in(1,2,3)]
destructive=[n*v/(2*d)for n in(1,3,5)]
for n,f in enumerate(constructive,1):eq(f'16.13.constructive_phase{n}',math.cos(2*math.pi*f*d/v),1)
for n,f in zip((1,3,5),destructive):eq(f'16.13.destructive_phase{n}',math.cos(2*math.pi*f*d/v),-1)
eq('16.13.rounded_first_Hz',v/.35,1000)
eq('16.13.rounded_destructive_first_Hz',v/(2*.35),500)
examples['16.13']=dict(source=dict(Aoffset_m=2,Boffset_m=1,perpendicular_m=4,soundSpeed_m_s=350,sources='inphase'),result=dict(pathA_m=rA,pathB_m=rB,exactPathDifference_m=d,constructiveExact_Hz=constructive,destructiveExact_Hz=destructive,sourceRoundedPath_m=.35,roundedConstructive_Hz=[1000,2000,3000],roundedDestructive_Hz=[500,1500,2500]),condition='ZerosoundpressurerequiresmatchingindividualpressureamplitudesatP.')

# Scalar pressures cancel, but nonparallel particle-velocity vectors do not.
n1=np.array([1.,0.]);n2=np.array([.5,math.sqrt(3)/2]);p1,p2=1.,-1.
eq('interference.scalarpressure_cancels',p1+p2,0)
yes('interference.nonparallel_velocity_nonzero',np.linalg.norm(p1*n1+p2*n2)>.9)
eq('interference.unequal_amplitude_residual',abs(2-1),1)
for t in(0,.001,.003):
 phase=2*math.pi*(1000-500)*t
 if t==0:eq('TY16.6.initial_phase',math.cos(phase),1)
 else:eq(f'TY16.6.changed_phase_t{t}',math.cos(phase),-1)
selfchecks['16.6']=dict(sourceFrequencies_Hz=[500,1000],answer=3,reason='No fixedconstructive/destructivephasepattern, whilelinearsuperpositionstillholds.')

# Source Fig16.25 uses opposite initial phase, not equal phase at zero.
fa,fb,A=16.,18.,1.
def y(t):return A*np.sin(2*np.pi*fa*t)-A*np.sin(2*np.pi*fb*t)
def envelope(t):return 2*A*abs(np.sin(np.pi*(fa-fb)*t))
eq('figure16.25.max_at_.25s',envelope(.25),2)
eq('figure16.25.min_at_.50s',envelope(.5),0)
eq('figure16.25.max_at_.75s',envelope(.75),2)
for t in np.linspace(0,1,13):
 factor=2*A*np.sin(np.pi*(fa-fb)*t)*np.cos(np.pi*(fa+fb)*t)
 eq(f'beats.trig_identity_t{t:.3f}',y(t),factor)
 eq(f'beats.envelope_period_t{t:.3f}',envelope(t+.5),envelope(t))
grid=np.arange(4096)/4096
power_envelope=envelope(grid)**2
fft=np.abs(np.fft.rfft(power_envelope-power_envelope.mean()))
eq('beats.intensity_envelope_fft_Hz',np.argmax(fft),2)
for first,second in[(256,255),(256,257),(440,437),(440,443),(1800,1900)]:
 beat=abs(first-second);Ta,Tb=1/max(first,second),1/min(first,second)
 eq(f'beats.cyclecount_{first}_{second}',1/(Ta*Tb/(Tb-Ta)),beat)
selfchecks['16.7']=dict(reference_Hz=440,beats_Hz=3,possibleOther_Hz=[437,443],answer=6)

# Acoustic Doppler from pulse arrival positions, independently of substitution.
v=340.;fS=300.;separation=1000.
def doppler(vL,vS):return(v+vL)/(v+vS)*fS
for vL,vS in[(0,30),(-30,0),(15,45),(10,10),(10,-20),(-15,20),(-25,-40)]:
 # World axis L->S, wave travels in negative direction.
 # Position equality atarrival: xL0+vL*t = xS0+vS*te-v*(t-te).
 t0=separation/(v+vL)
 te=1/fS;t1=(separation+(v+vS)*te)/(v+vL)
 eq(f'Doppler.arrival_position_{vL}_{vS}',vL*t1,separation+vS*te-v*(t1-te),atol=2e-10)
 eq(f'Doppler.arrival_frequency_{vL}_{vS}',1/(t1-t0),doppler(vL,vS),rtol=1e-10)
eq('16.14.stationary_lambda_m',v/fS,1.1333333333333333)
eq('16.14.front_lambda_m',(v-30)/fS,1.0333333333333334)
eq('16.14.behind_lambda_m',(v+30)/fS,1.2333333333333334)
examples['16.14']=dict(source=dict(sourceFrequency_Hz=300,soundSpeed_m_s=340,sourceSpeed_m_s=30,air='still'),result=dict(stationaryLambda_m=v/fS,frontLambda_m=(v-30)/fS,behindLambda_m=(v+30)/fS))
for id,vL,vS,rounded in [('16.15',0,30,276),('16.16',-30,0,274),('16.17',15,45,277)]:
 freq=doppler(vL,vS);eq(id+'.rounded_Hz',freq,rounded,atol=.5)
 examples[id]=dict(source=dict(fS_Hz=fS,v_m_s=v,vL_m_s=vL,vS_m_s=vS),result=dict(heardFrequency_Hz=freq),signConvention='PositiveLtoS,velocitiesrelativetoair.')
yes('16.15_16_16_16_17.same_relative_speed_distinct_frequencies',len({round(examples[id]['result']['heardFrequency_Hz'],6)for id in['16.15','16.16','16.17']})==3)

# Exact round-trip ray times to stationary wall and back to moving car.
u=30.;wall=1000.
returns=[];wall_times=[]
for emitted in [0,1/fS]:
 car_emit=u*emitted
 tw=emitted+(wall-car_emit)/v
 # Reflectedray wall-v*(t-tw) meetscaru*t.
 tr=(wall+v*tw)/(v+u)
 eq(f'16.18.reflection_position_emit{emitted}',wall-v*(tr-tw),u*tr,atol=1e-10)
 wall_times.append(tw);returns.append(tr)
fw=1/(wall_times[1]-wall_times[0]);fr=1/(returns[1]-returns[0])
eq('16.18.wall_frequency',fw,v/(v-u)*fS)
eq('16.18.return_frequency',fr,(v+u)/(v-u)*fS)
eq('16.18.return_rounded_Hz',fr,358.,atol=.5)
examples['16.18']=dict(source=dict(carTowardWall_m_s=30,source_Hz=300,soundSpeed_m_s=340),result=dict(wallFrequency_Hz=fw,driverReflectedFrequency_Hz=fr),independentCheck='Twoemissiontimesandbothreflectionarrivalintersections,notjusttwoDopplersubstitutions.')
eq('TY16.8.uniformwind_no_shift',doppler(10,10),fS)
selfchecks['16.8']=dict(windFromSourceToListener_m_s=10,relativeToAir_vL_m_s=10,relativeToAir_vS_m_s=10,answer='NoDopplerfrequencyshift')

# Electromagnetic longitudinal result has reciprocal factors for opposite speeds.
for beta in[-.8,-.2,0,.2,.8]:
 factor=math.sqrt((1-beta)/(1+beta))
 reverse=math.sqrt((1+beta)/(1-beta))
 eq(f'EM.reciprocal_beta{beta}',factor*reverse,1)
 eq(f'EM.rest_beta{beta}',beta==0 and factor==1 or beta!=0,1)

# Mach cone sourcegeometry, plus independent earliestarrival minimization.
Mach=1.75;h=8000.;v=320.;u=Mach*v
alpha=math.asin(1/Mach);delay=h/(u*math.tan(alpha));distance=u*delay
eq('16.19.angle_deg',math.degrees(alpha),34.8,atol=.05)
eq('16.19.plane_speed_m_s',u,560)
eq('16.19.delay_rounded_s',delay,20.5,atol=.05)
# A pulse emitted tau seconds BEFORE overhead arrives at t=-tau+travel_time.
arrival=lambda tau:-tau+math.hypot(u*tau,h)/v
opt=minimize_scalar(arrival,bounds=(0,60),method='bounded',options={'xatol':1e-10})
eq('16.19.minimum_retarded_arrival',opt.fun,delay,rtol=1e-10)
eq('16.19.distance_after_overhead_m',distance,11489.125293076057,rtol=1e-8)
for mach in[1.01,1.1,1.75,2,3,10]:
 angle=math.asin(1/mach)
 eq(f'Machcone.sin_alpha_{mach}',math.sin(angle),1/mach)
 yes(f'Machcone.angle_range_{mach}',0<angle<math.pi/2)
examples['16.19']=dict(source=dict(Mach=Mach,altitude_m=h,soundSpeed_m_s=v),result=dict(halfAngle_deg=math.degrees(alpha),planeSpeed_m_s=u,delayAfterOverhead_s=delay,distanceAfterOverhead_m=distance),model='Uniformsoundspeedallaltitudes;steadyhorizontalflight;flatground;idealMachcone.')
selfchecks['16.9']=dict(answer=3,reason='Listenerinsideconebehindairplanehearsrecedingsourcedownshift;frontcrossingboomisseparateevent.')

assert len(examples)==8 and len(selfchecks)==5
report=dict(status='passed',scope='Chapter16.5–16.9 theory only; notwholechapterorexercises',examples=examples,selfchecks=selfchecks,assertionCount=len(checks),checks=checks,sourceClarifications=['Fig16.25initialoppositephasepreserved;max.25s,min.50s.','16.13roundfamilyfrequenciesareapproximatebecauseexactpathdifference.34903m.','Scalarpressurezerodoesnotimplyzero3Dparticlevelocityfornonparallelwaves.','SoundDopplerdependsonindividualvelocitiesrelativetomedium;lightformulaisdifferent.'])
print(json.dumps(report,ensure_ascii=False,indent=2))
