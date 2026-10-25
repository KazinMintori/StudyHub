"""Recompute early sound theory directly from stated prompt data."""
from pathlib import Path
import json, math
from scipy.integrate import quad

HERE=Path(__file__).resolve().parent
assertions=[]
examples={}
def check(name,a,b,rel=1e-10,atol=1e-12):
 assert math.isclose(a,b,rel_tol=rel,abs_tol=atol),(name,a,b)
 assertions.append({'name':name,'actual':a,'expected':b})
def truth(name,cond):
 assert cond,name
 assertions.append({'name':name,'passed':True})

p0=.030; freq=1000; c=344; B=1.42e5
k=2*math.pi*freq/c; amp=p0/(B*k)
examples['16.1']={'k_rad_m':k,'A_m':amp}
check('16.1.reconstructed-pressure',B*k*amp,p0)
truth('16.1.source-rounded-amplitude',abs(amp-1.2e-8)<.05e-8)
area1=43e-6;area2=3.2e-6
force=p0*area1;pe=force/area2;be=1/(45.8e-11);ke=2*math.pi*freq/1500;ae=pe/(be*ke)
examples['16.2']={'force_N':force,'p_ear_Pa':pe,'B_ear_Pa':be,'k_ear_rad_m':ke,'A_ear_m':ae,'gain':area1/area2}
check('16.2.force-consistency',p0*area1,pe*area2)
check('16.2.frequency-preserved',ke*1500/(2*math.pi),freq)
truth('16.2.smaller-displacement-in-fluid',ae<amp)
wv=math.sqrt(2.18e9/1000);wl=wv/262
examples['16.3']={'speed_m_s':wv,'lambda_m':wl,'dolphin_lambda_m':1482/1e5,'ultrasound_lambda_m':1482/5e6}
check('16.3.wave-relation',wl*262,wv)
truth('16.3.longer-than-air',wl>344/262)
air=math.sqrt(1.4*8.314*(20+273.15)/.0288)
examples['16.4']={'temperature_K':293.15,'speed_m_s':air,'rounded293_speed_m_s':math.sqrt(1.4*8.314*293/.0288),'lambda20_m':air/20,'lambda20000_m':air/20000}
for pressure in [.4e5,1.013e5,2.4e5]:
 rho=pressure*.0288/(8.314*293.15)
 check('ideal-gas.pressure-cancels',math.sqrt(1.4*pressure/rho),air)
examples['self16.2']={'B_Hg_over_water':13.6*(1451/1482)**2}
truth('self16.2.mercury-larger-B',examples['self16.2']['B_Hg_over_water']>12.9)
check('air.bulk-modulus',1.4*1.013e5,1.4182e5)
check('spectrum.clarinet-period-ms',1000/233,4.291845493562231)
check('spectrum.recorder-period-ms',1000/523,1.9120458891013384)
check('self16.1.frequency-ratio',100/400,.25)
for rho,bulk,u,area,t in [(1000,2.18e9,.001,.03,.2),(1.2,1.42e5,1e-5,.01,.3)]:
 wave=math.sqrt(bulk/rho);dp=bulk*u/wave
 check('wavefront.impulse-vs-momentum',dp*area*t,rho*area*wave*t*u)
 check('wavefront.pressure-impedance',dp,rho*wave*u)

I=p0*p0/(2*1.2*344)
examples['16.5']={'I_W_m2':I,'I_at_pressure30Pa_W_m2':30**2/(2*1.2*344),'I_at_pressure3e-5Pa_W_m2':(3e-5)**2/(2*1.2*344)}
examples['16.6']={'p20_Pa':p0,'A20_from_rounded_A1000_m':1.2e-8*50,'A20_full_precision_m':amp*50,'amplitude_ratio':50}
check('16.6.constant-fA',20*amp*50,1000*amp)
truth('16.6.low-frequency-larger-displacement',amp*50>amp)
examples['16.7']={'area_hemisphere_m2':2*math.pi*20**2,'power_W':2*math.pi*20**2,'full_sphere_if_other_model_W':4*math.pi*20**2}
examples['16.8']={'I28_W_m2':1e-12*10**2.8,'I92_W_m2':1e-12*10**9.2}
examples['16.9']={'delta_dB':10*math.log10(.25),'ratio':.25}
for beta in [-10,0,10,28,65,92,120,140]:
 check('decibel.roundtrip',10*math.log10((1e-12*10**(beta/10))/1e-12),beta)
for f in [20,400,1000,20000]:
 rho=1.2;wave=344;bulk=rho*wave**2;w=2*math.pi*f;kk=w/wave;a=3e-8
 intens1=.5*bulk*w*kk*a*a
 pmax=bulk*kk*a
 check('intensity.four-forms',intens1,pmax*pmax/(2*rho*wave),atol=1e-20)
 check('intensity.displacement-form',intens1,.5*math.sqrt(rho*bulk)*w*w*a*a,atol=1e-20)
 timeavg=quad(lambda phase:(bulk*kk*a*math.sin(phase))*(w*a*math.sin(phase)),0,2*math.pi)[0]/(2*math.pi)
 check('intensity.direct-integral',timeavg,intens1,atol=1e-20)
 h=1e-5/kk;x=.23/kk;t=.31/w
 deriv=(a*math.cos(kk*(x+h)-w*t)-a*math.cos(kk*(x-h)-w*t))/(2*h)
 check('pressure.finite-difference-gradient',-bulk*deriv,bulk*kk*a*math.sin(kk*x-w*t),rel=1e-8,atol=1e-16)

table16_1=[['Air20C',344],['Helium20C',999],['Hydrogen20C',1330],['LiquidHelium4K',211],['Mercury20C',1451],['Water0C',1402],['Water20C',1482],['Water100C',1543],['Aluminum',6420],['Lead',1960],['Steel',5941]]
table16_2=[['Militaryjet30m',140,1e2],['Painthreshold',120,1],['Riveter',95,3.2e-3],['Elevatedtrain',90,1e-3],['Traffic',70,1e-5],['Conversation',65,3.2e-6],['Quietcar',50,1e-7],['Quietradio',40,1e-8],['Whisper',20,1e-10],['Leaves',10,1e-11],['Hearing1000Hz',0,1e-12]]
for name,beta,intensity in table16_2:
 check('table16.2.'+name,10*math.log10(intensity/1e-12),beta,rel=0,atol=.06)
check('self16.3.amplitude-ratio',math.sqrt(2)**2,2)
check('self16.3.delta-dB',10*math.log10(2),3.010299956639812)
truth('self16.4.helium-higher-speed',999>344)
check('self16.4.same-mode-frequency-ratio',(3*999/(2*.8))/(3*344/(2*.8)),999/344)
check('self16.4.same-pressure-temperature-density-ratio',.0288/.004,7.2)
check('power.city-order-estimate',1e7*1e-5,100.)
check('intensity.6to10fold-level-limits',10**.8,6.309573444801933)
check('intensity.10fold-level',10*math.log10(10),10.)

# A rigid boundary at x=0 gives a pressure antinode and displacement node.
# Phase relation is checked through direct derivatives, not source captions.
lam=.8;kk=2*math.pi/lam;w=2*math.pi*500
for n in range(5):
 d=(2*n+1)*lam/4
 check('16.10.pressure-node',math.cos(kk*d),0,atol=1e-13)
 check('16.10.displacement-antinode',abs(math.sin(kk*d)),1)
examples['16.10']={'distances_in_lambda':[.25,.75,1.25],'model':'Rigidwall,one-dimensionalincident/reflectedplane waves.'}
Lclosed=344/(4*220);fovertone=5*220;Lopen=3*344/(2*fovertone)
examples['16.11']={'stopped_length_m':Lclosed,'second_overtone_Hz':fovertone,'open_length_m':Lopen,'open_f1_Hz':344/(2*Lopen)}
check('16.11.same-wavelength',4*Lclosed/5,2*Lopen/3)
check('16.11.closed-f1',344/(4*Lclosed),220)
for n in range(1,9):
 L=.73;kopen=n*math.pi/L
 check('open.left-pressure-node',math.sin(kopen*0),0)
 check('open.right-pressure-node',math.sin(kopen*L),0,atol=1e-13)
 check('open.right-displacement-antinode',abs(math.cos(kopen*L)),1)
 if n%2:
  kclosed=n*math.pi/(2*L)
  check('stopped.closed-displacement-node',math.cos(kclosed*L),0,atol=1e-13)
  check('stopped.closed-pressure-antinode',abs(math.sin(kclosed*L)),1)
 else:
  truth('stopped.even-harmonic-fails-boundary',abs(math.cos(n*math.pi/2))>.9)

out={'status':'passed','checks':len(assertions),'scope':'Earlytheory16.1–16.4: 11examplesincludingconceptual16.10,4selfchecks,sourceTable16.2logconversion. EmpiricalTable16.1valuesaretranscriptionsnotexperimentalvalidation. Nohealthdoseoutcomeverified.','examples':examples,'table16_1':table16_1,'table16_2':table16_2,'assertions':assertions}
print(json.dumps(out,ensure_ascii=False,indent=2))
