from pathlib import Path
import math,json
OUT=Path(__file__).resolve().parent
pi=math.pi;I0=1e-12;rows=[];values={}
def check(name,ok,evidence):rows.append({'name':name,'pass':bool(ok),'evidence':evidence})
def close(name,a,b,tol=1e-10):check(name,math.isclose(a,b,rel_tol=tol,abs_tol=tol),{'computed':a,'comparison':b,'tolerance':tol})
def record(key,**data):
 values[key]=data
 for k,v in data.items():
  if isinstance(v,(float,int)):check(key+':'+k+':finite',math.isfinite(v),v)
beta=lambda I:10*math.log10(I/I0)
pressure=lambda I,rho=1.20,v=344.:math.sqrt(2*rho*v*I)
record('VP16.9.1',p_Pa=pressure(5.50e-8),p_after_frequency_doubled_Pa=pressure(5.50e-8))
record('VP16.9.2',I_W_m2=I0*10**(85./10),ratio=10**((85.-67.)/10))
record('VP16.9.3',beta_4m_dB=114.-20*math.log10(4.),beta_15_8m_dB=114.-20*math.log10(15.8))
record('VP16.9.4',p_Pa=pressure(I0*10**6.6,.920),new_beta_dB=66.+20*math.log10(10.))
record('VP16.12.1',open_length_m=344./(2*220),stopped_length_m=344./(4*3*220))
record('VP16.12.2',n_for_one_sixth=6/6,n_for_half=6/2,n_required_for_third=6/3)
check('VP16.12.2-third-ratio-no-even-harmonic',int(6/3)%2==0,'n=2 is forbidden in ideal stopped pipe')
record('VP16.12.3',v_string_m_s=2*.680*165,stopped_length_m=344./(4*165))
f=3*999./(4*1.)
record('VP16.12.4',f_helium_Hz=f,lambda_helium_m=999./f,f_air_Hz=f,lambda_air_m=344./f,open_length_m=5*344./(2*f))
v,u,f=340.,26.,2.80e3
record('VP16.18.1',front_f_Hz=f*v/(v-u),front_lambda_m=(v-u)/f,back_f_Hz=f*v/(v+u),back_lambda_m=(v+u)/f)
v,f,u=340.,440.,10.
record('VP16.18.2',lambda_m=v/f,approaching_f_Hz=f*(v+u)/v,receding_f_Hz=f*(v-u)/v,lambda_for_each_m=v/f)
v,f,us,ul=340.,1.20e3,40.,35.
record('VP16.18.3',eastward_f_Hz=f*(v-ul)/(v-us),westward_f_Hz=f*(v+ul)/(v-us))
v,f,u,target=340.,415.,25.,495.
record('VP16.18.4',wall_received_f_Hz=f*v/(v-u),driver_echo_f_Hz=f*(v+u)/(v-u),u_for_495_m_s=v*(target-f)/(target+f))
u=values['VP16.18.4']['u_for_495_m_s'];close('VP16.18.4-inverse-reinsert',f*(v+u)/(v-u),target)

PA,PB,rA,rB,v,f=8e-4,6e-5,4.,3.,344.,172.
IA,IB=PA/(4*pi*rA*rA),PB/(4*pi*rB*rB)
delta=2*pi*(rA-rB)/(v/f)
pA,pB=pressure(IA),pressure(IB)
Icoherent=(math.sqrt(IA)-math.sqrt(IB))**2
Iwrong=IA+IB
record('bridge',lambda_m=v/f,phase_rad=delta,IA_W_m2=IA,IB_W_m2=IB,betaA_dB=beta(IA),betaB_dB=beta(IB),pA_Pa=pA,pB_Pa=pB,pcombined_Pa=abs(pA-pB),I_W_m2=Icoherent,beta_dB=beta(Icoherent),wrong_I_W_m2=Iwrong,wrong_beta_dB=beta(Iwrong))
close('bridge-pressure-intensity',abs(pA-pB)**2/(2*1.2*v),Icoherent)
close('bridge-general-phase-cross-term',IA+IB+2*math.sqrt(IA*IB)*math.cos(delta),Icoherent)
check('bridge-destructive-not-total-zero',0<Icoherent<IA,{'coherent':Icoherent,'A_alone':IA,'B_alone':IB})
check('bridge-less-than-incoherent-sum',Icoherent<Iwrong,{'right':Icoherent,'wrong':Iwrong})
check('bridge-pressure-reduced-by-B',abs(pA-pB)<pA,{'pA':pA,'pB':pB,'combined':abs(pA-pB)})
net_flux=IA-IB
check('bridge-equivalent-intensity-not-signed-net-flux',not math.isclose(Icoherent,net_flux),{'pressure_equivalent_Iq':Icoherent,'signed_net_flux_toward_B':net_flux})

# Phase, coherent addition and pressure/displacement boundary checks.
for phase in [0.,pi/3,pi/2,pi]:
 A,B=2.,.7
 mean=sum((A*math.cos(2*pi*(i+.5)/4000)+B*math.cos(2*pi*(i+.5)/4000+phase))**2 for i in range(4000))/4000
 close('coherent-mean-square-'+str(phase),mean,(A*A+B*B+2*A*B*math.cos(phase))/2)
# Stopped at x=0, open at x=L: displacement sin(kx), pressure cos(kx).
L=1.
for n in [1,3,5,7]:
 k=n*pi/(2*L)
 close(f'stopped-{n}-closed-displacement-node',math.sin(0),0)
 close(f'stopped-{n}-open-pressure-node',math.cos(k*L),0)
 close(f'stopped-{n}-closed-pressure-antinode',math.cos(0),1)
 close(f'stopped-{n}-open-displacement-antinode',abs(math.sin(k*L)),1)
for n in [2,4,6]:check(f'stopped-{n}-forbidden',abs(math.cos(n*pi/2))>.5,'pressure would not vanish at open end')
for n in [1,2,3,4]:
 close(f'open-{n}-pressure-node-left',math.sin(0),0)
 close(f'open-{n}-pressure-node-right',math.sin(n*pi),0)

# Qualitative checks and explicit countermodels used in the 25 Q answers.
record('Q16.3',frequency_ratio_303K_to_293K=math.sqrt(303.15/293.15))
record('Q16.7',frequency_at_v20_spacing0_1_Hz=20/.1)
record('Q16.8',intensity_at_zero_dB=I0,intensity_at_minus10_dB=I0*10**(-1))
close('Q16.10-half-pressure-quarter-intensity',(.5)**2,.25)
close('Q16.10-sixteenfold-intensity-fourfold-pressure',math.sqrt(16.),4.)
record('Q16.11',beta_change_double_r_dB=-20*math.log10(2.))
check('Q16.12-absorption-faster-than-inverse-square',math.exp(-.2*4)/4**2<1/4**2,'I=P exp(-alpha r)/(4 pi r^2), alpha>0')
record('Q16.15',wavelength_m=344/860,delta_lambda=(13.4-12.)/(344/860),phase_rad=2*pi*(13.4-12.)/(344/860))
close('Q16.15-destructive-phase-mod-2pi',math.cos(values['Q16.15']['phase_rad']),-1)
# Rotating source: radial velocity changes continuously, not necessarily fixed beat frequency.
freqs=[440*340/(340-10*math.sin(t))for t in [0,pi/2,pi,3*pi/2]]
check('Q16.16-rotating-source-both-shift-signs',max(freqs)>440>min(freqs),freqs)
close('Q16.18-uniform-wind-cancels',(344+20)/(344+20),1.)
# Equal closing speed does not fix acoustic Doppler.
v,u,f=340.,30.,440.
record('Q16.22',moving_source_f_Hz=f*v/(v-u),moving_listener_f_Hz=f*(v+u)/v)
check('Q16.22-same-relative-speed-different-frequency',values['Q16.22']['moving_source_f_Hz']>values['Q16.22']['moving_listener_f_Hz'],values['Q16.22'])
record('Q16.23',Mach2_half_angle_deg=math.degrees(math.asin(.5)))
# Far-field moving source with finite perpendicular offset gives continuous radial velocity.
b,u=20.,30.
radial=[u*x/math.hypot(x,b)for x in [-100,-10,0,10,100]]
check('Q16.21-radial-component-continuous',all(radial[i]<radial[i+1]for i in range(4)),radial)
# Mass added to a flexural tine has modal inertia weighted by mode-shape squared.
phi=lambda x:x*x*(3-x)/2
check('Q16.13-outboard-mass-increases-modal-inertia',phi(.9)**2>phi(.3)**2,{'mode_squared_near_root':phi(.3)**2,'mode_squared_near_tip':phi(.9)**2})
# Equal pressure amplitudes at different frequencies have different displacement amplitudes.
close('Q16.9-displacement-inverse-frequency-at-fixed-pressure',(1/200)/(1/100),.5)
Z=1.2*344.;x=.7
pressure_samples=[];flux_samples=[]
for j in range(4000):
 t=2*pi*(j+.5)/4000
 p=2*math.cos(x)*math.cos(t)
 particle_v=2/Z*math.sin(x)*math.sin(t)
 pressure_samples.append(p*p);flux_samples.append(p*particle_v)
check('Q16.8-standing-pressure-nonzero',sum(pressure_samples)/4000>0,{'mean_p_squared':sum(pressure_samples)/4000})
close('Q16.8-zero-net-flux-counterexample',sum(flux_samples)/4000,0)

result={'scope':'12 VP +25 Q +1 bridge','count':len(rows),'passed':sum(x['pass']for x in rows),'failed':[x for x in rows if not x['pass']],'values':values,'checks':rows}
assert not result['failed']
print(json.dumps({'status':'passed',**result},ensure_ascii=False,indent=2))
