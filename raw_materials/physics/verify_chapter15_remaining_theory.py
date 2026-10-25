"""Chapter15 THEORY source arithmetic and nontrivial equation checks; private QA."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad

OUT=Path(__file__).resolve().parent
checks=[]
def check(id,actual,expected,atol=1e-10,note=''):
    actual,expected=float(actual),float(expected)
    assert math.isclose(actual,expected,rel_tol=0,abs_tol=atol),(id,actual,expected)
    checks.append(dict(id=id,computed=actual,expected=expected,tolerance=atol,note=note,status='passed'))

examples={}
speed=344.;freq=262.
lam=speed/freq;highfreq=4*freq;highlam=speed/highfreq
examples['15.1']=dict(pdfPages=[488],speed_m_s=speed,f_Hz=freq,wavelength_m=lam,high_C_frequency_Hz=highfreq,high_C_wavelength_m=highlam)
check('15.1.lambda',lam,1.31,.005)
check('15.1.highC.f',highfreq,1048)
check('15.1.highC.lambda',highlam,.328,.0005)
check('15.1.sound_ft_s',speed/.3048,1130,2)

A,f,v=.075,2.,12.
omega=2*math.pi*f;T=1/f;wavelength=v/f;k=2*math.pi/wavelength
examples['15.2']=dict(pdfPages=[492],A_m=A,f_Hz=f,omega_rad_s=omega,T_s=T,wavelength_m=wavelength,k_rad_m=k,wave='A*cos(k*x-omega*t)',origin_motion='A*cos(omega*t)',at3m_motion='-A*cos(omega*t)')
for id,value,expected,tol in [('omega',omega,12.6,.05),('period',T,.5,1e-12),('lambda',wavelength,6,1e-12),('k',k,1.05,.005)]:
    check('15.2.'+id,value,expected,tol)
for t in [0,.02,.1,.2,.3]:
    check(f'15.2.halfwave_phase.t{t}',A*math.cos(k*3-omega*t),-A*math.cos(omega*t),1e-12)
check('15.2.origin_velocity_t0',-A*omega*math.sin(0),0)

mass,L,load,g=2.,80.,20.,9.8
mu=mass/L;force=load*g;v=math.sqrt(force/mu);wavelength=v/2
top=math.sqrt((load+mass)*g/mu)
examples['15.3']=dict(pdfPages=[497,498],rope_mass_kg=mass,L_m=L,load_mass_kg=load,mu_kg_m=mu,tension_ignoring_rope_weight_N=force,v_approx_m_s=v,wavelength_approx_m=wavelength,cycles_approx=L/wavelength,v_top_with_rope_weight_m_s=top)
check('15.3.mu',mu,.025)
check('15.3.F',force,196)
check('15.3.v',v,88.5,.05)
check('15.3.lambda',wavelength,44.3,.05)
check('15.3.cycles',L/wavelength,1.81,.005)
check('15.3.v_top',top,92.9,.05)

mu,force,A,f=.250,36.,.075,2.
omega=2*math.pi*f
Pmax=math.sqrt(mu*force)*omega**2*A**2;Pavg=Pmax/2;smallA=.00750
examples['15.4']=dict(pdfPages=[499,500],mu_kg_m=mu,tension_N=force,A_m=A,f_Hz=f,Pmax_W=Pmax,Pavg_W=Pavg,small_A_m=smallA,small_average_power_W=Pavg*(smallA/A)**2)
check('15.4.Pmax',Pmax,2.66,.005)
check('15.4.Pavg',Pavg,1.33,.005)
check('15.4.smallP',Pavg*(smallA/A)**2,.0133,.00005)
check('15.4.wave_speed',math.sqrt(force/mu),12)
period=1/f
mean=quad(lambda t:Pmax*math.sin(-omega*t)**2,0,period)[0]/period
check('15.4.period_integral_mean',mean,Pavg,1e-12)

r1,I1,I2=15.,.250,.010
r2=r1*math.sqrt(I1/I2)
examples['15.5']=dict(pdfPages=[500],r1_m=r1,I1_W_m2=I1,I2_W_m2=I2,r2_m=r2)
check('15.5.r2',r2,75)
check('15.5.intensity_ratio',I1/I2,(r2/r1)**2)

A_inc,f,v=.000750,440.,143.
A_SW=2*A_inc;omega=2*math.pi*f;k=omega/v;wavelength=v/f
vmax=omega*A_SW;amax=omega**2*A_SW
examples['15.6']=dict(pdfPages=[506],incoming_A_m=A_inc,standing_A_m=A_SW,f_Hz=f,v_m_s=v,omega_rad_s=omega,k_rad_m=k,wavelength_m=wavelength,first_nodes_m=[j*wavelength/2 for j in range(4)],first_antinodes_m=[(2*j+1)*wavelength/4 for j in range(3)],vmax_m_s=vmax,amax_m_s2=amax,amax_in_g=amax/9.8)
check('15.6.omega',omega,2760,5)
check('15.6.k',k,19.3,.05)
check('15.6.lambda',wavelength,.325)
check('15.6.vmax',vmax,4.15,.005)
check('15.6.amax',amax,1.15e4,50)
check('15.6.accel_g',amax/9.8,1170,1)
check('15.6.velocity_kmh',vmax*3.6,15,.1)
check('15.6.velocity_mph',vmax/.44704,9.3,.05)

L,mu,f1=5.,.0400,20.
force=4*mu*L**2*f1**2
examples['15.7']=dict(pdfPages=[509],length_m=L,mu_kg_m=mu,fundamental_Hz=f1,tension_N=force,second_harmonic_Hz=2*f1,second_harmonic_wavelength_m=L,second_overtone_is_harmonic_n=3,second_overtone_Hz=3*f1,second_overtone_wavelength_m=2*L/3,string_speed_m_s=2*L*f1)
check('15.7.tension',force,1600)
check('15.7.pounds_force',force/4.4482216152605,360,1)
check('15.7.f2',2*f1,40)
check('15.7.lambda2',L,5)
check('15.7.f3',3*f1,60)
check('15.7.lambda3',2*L/3,3.33,.005)

sound=344;string_speed=200;f=20
examples['15.8']=dict(pdfPages=[510],sound_speed_m_s=sound,sound_frequency_Hz=f,sound_wavelength_m=sound/f,string_frequency_Hz=f,string_wavelength_m=10,string_speed_m_s=string_speed,speed_and_wavelength_ratio=sound/string_speed)
check('15.8.lambda_sound',sound/f,17.2)
check('15.8.lambda_ratio',(sound/f)/10,1.72)

selfchecks={}
selfchecks['15.1']=dict(pdfPages=[486],answer='(i), transverse',reason='Propagationhorizontal,spectatordisplacementvertical.')
selfchecks['15.2']=dict(pdfPages=[489],answer='(iv),samev,halff',reason='Fixedmediumwavevelocity;lambda doubled.')
check('self15.2.frequency_factor',1/2,.5)
# Figure15.8 initiallyA/Cat-A,Bat+A. Use normalizedperiodT=1 andamplitudeA=1.
times={'a':2/8,'b':4/8,'c':5/8};om=2*math.pi
vA=om*math.sin(om*times['a']);aB=-om*om*math.cos(om*times['b'])
yC=-math.cos(om*times['c']);vC=om*math.sin(om*times['c']);aC=-om*om*yC
check('self15.3.Amaxup',vA,om)
check('self15.3.Bmaxup_accel',aB,om*om)
assert yC>0 and vC<0 and aC<0
selfchecks['15.3']=dict(pdfPages=[494],answers_in_T=times,C_displacement=yC,C_velocity=vC,C_acceleration=aC)
selfchecks['15.4']=dict(pdfPages=[498],answer='(ii),thinneststring',reason='Lowestmuatnearlysametensiongivesgreatestsqrt(F/mu).')
relative=[math.sqrt(F/10)*(A/1)**2 for F,A in [(10,1),(40,1),(10,4),(20,2)]]
selfchecks['15.5']=dict(pdfPages=[501],source_frequency_Hz=10,source_tensions_N=[10,40,10,20],source_amplitudes_mm=[1,1,4,2],powers_relative_to_i=relative,rank=['iii','iv','ii','i'])
assert np.argsort(relative).tolist()==[0,1,3,2]
selfchecks['15.6']=dict(pdfPages=[502],question_figure='15.22',answer='Constructpositivepulseoverlapsbyalgebraicsuperposition.',source_answer_graphic_issue='Printed3answerpanelscontainnegativepulsewherequestionhas2positivepulses. Do not acceptasanswerwithoutcorrection.')
xx=np.linspace(-10,10,4001)
for time in [-2,0,2]:
    one=np.exp(-((xx-time)/.25)**2)
    two=.25*np.exp(-((xx+time)/1.2)**2)
    assert np.min(one+two)>=0
check('self15.6.nonnegative_plus_nonnegative_min',min(np.min(np.exp(-((xx-t)/.25)**2)+.25*np.exp(-((xx+t)/1.2)**2))for t in[-2,0,2]),0,1e-10,note='Algebraicnonnegativitysupportsvisualsourceerratum;notpixelclassification.')
oldnodes=[j*.325/2 for j in range(8)]
newspacing=.325/4
for x in oldnodes:check(f'self15.7.oldnode{x}',x/newspacing,round(x/newspacing),1e-12)
selfchecks['15.7']=dict(pdfPages=[506],answer='Alloldnodesremain;oneextranodebetweeneacholdpair.',old_spacing_m=.325/2,new_spacing_m=.325/4)
for n in range(1,17):
    amplitude_at_mid=math.sin(n*math.pi/2)
    if n%2==0:check(f'self15.8.even_n{n}_midnode',amplitude_at_mid,0,1e-12)
    else:check(f'self15.8.odd_n{n}_mid_nonzero',abs(amplitude_at_mid),1,1e-12)
selfchecks['15.8']=dict(pdfPages=[510],forbidden_modes='n=1,3,5,...',allowed_modes='evennonly',reason='TouchingL/2requirespersistentnode,sin(n*pi/2)=0.')

# Trig/PDE/energy identities tested on several nontrivialparametergrids.
identity_cases=[]
for A,k,v in [(.075,1.0471975512,12),(.0015,19.333,143),(.2,2.3,4.1)]:
    om=k*v
    for x,t in [(.13,.07),(.31,.12),(.57,.19)]:
        phase=k*x-om*t
        y=A*math.cos(phase)
        yt=A*om*math.sin(phase)
        ytt=-A*om**2*math.cos(phase)
        yx=-A*k*math.sin(phase)
        yxx=-A*k*k*math.cos(phase)
        check(f'PDE.{A}.{x}.{t}',yxx-ytt/v**2,0,1e-10)
        check(f'SHM.{A}.{x}.{t}',ytt+om**2*y,0,1e-10)
        combined=-A*math.cos(k*x+om*t)+A*math.cos(k*x-om*t)
        check(f'standing_trig.{A}.{x}.{t}',combined,2*A*math.sin(k*x)*math.sin(om*t),1e-11)
        mu=.03;F=mu*v*v
        flux=-F*yx*yt
        expected=math.sqrt(mu*F)*om**2*A*A*math.sin(phase)**2
        check(f'energy_flux.{A}.{x}.{t}',flux,expected,1e-9)
        identity_cases.append(dict(A=A,k=k,v=v,x=x,t=t,wavePDE=True,standingTrig=True,powerIdentity=True))

for x in [.1,.27,.41]:
    ASW=.02;k=3.;v=5.;om=k*v;F=.03*v*v;period=2*math.pi/om
    flux=lambda t:-F*(ASW*k*math.cos(k*x)*math.sin(om*t))*(ASW*om*math.sin(k*x)*math.cos(om*t))
    mean=quad(flux,0,period)[0]/period
    check(f'standing_mean_power.x{x}',mean,0,1e-12)

# Arbitraryshape andlinearity: travelingGaussian/sinusoidallbothsatisfylinearPDE.
for z in [-1.2,-.3,.1,.7]:
    base_second=(4*z*z-2)*math.exp(-z*z)
    for speed in [1.3,4.]:
        check(f'GaussianPDE.{z}.{speed}',base_second-(speed*speed*base_second)/(speed*speed),0,1e-12)

# Fourier coefficients oftheoriginaltriangularpluckatL/4 (Figure15.28).
L=1.;pluck=.25
profile=lambda x:x/pluck if x<=pluck else (L-x)/(L-pluck)
bn=[]
for n in [1,2,3]:
    coefficient=2/L*(quad(lambda x:profile(x)*math.sin(n*math.pi*x/L),0,pluck)[0]+quad(lambda x:profile(x)*math.sin(n*math.pi*x/L),pluck,L)[0])
    bn.append(coefficient)
check('Fig15.28.b2_over_b1',bn[1]/bn[0],1/(2*math.sqrt(2)))
check('Fig15.28.b3_over_b1',bn[2]/bn[0],1/9)

check('application.duck.km_h',.7*3.6,2.5,.05)
check('application.duck.mi_h',.7/.44704,1.6,.05)
check('power.amplitude_doubled_ratio',2**2,4)
check('power.frequency_doubled_ratio',2**2,4)

report=dict(status='passed',checksCount=len(checks),checks=checks,examples=examples,selfchecks=selfchecks,identityCases=identity_cases,FourierTriangleCoefficients=bn,openerAnswer='(iii),amplitudeandfrequency:PavgproportionalA²omega²withfixedmedium',scope='SourceTHEORYonly,PDF484–511;notauthoringorcompletioncertification.')
print(json.dumps(report,ensure_ascii=False,indent=2))
