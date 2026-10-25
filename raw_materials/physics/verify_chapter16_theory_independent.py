"""Independent chapter16 source-input checks, without importing author verifiers.

Checks cover physical models and arithmetic. They do not certify health dose
outcomes, experimental sound-speed measurements, source coverage or UI layout.
"""
from pathlib import Path
import json,math,re
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar,brentq

OUT=Path(__file__).resolve().parent
checks=[];examples={};selfchecks={}
def close(name,a,b,rtol=1e-8,atol=1e-12):
 assert math.isclose(float(a),float(b),rel_tol=rtol,abs_tol=atol),(name,a,b)
 checks.append({'id':name,'actual':float(a),'expected':float(b),'passed':True})
def truth(name,value):
 assert value,name
 checks.append({'id':name,'passed':True})

# Original worked-example values are transcribed from PDF524–551, not loaded
# from author-generated answers. The numerical approaches below are separate.
p=.03;f=1000.;v=344.;B=1.42e5;k=2*math.pi*f/v
A=p/(B*k)
examples['16.1']={'wave_number_rad_m':k,'displacement_m':A,'model':'linear plane traveling sound'}
close('16.1:reported12nm',A,1.2e-8,rtol=.05)
close('16.1:recover_pressure',B*(2*math.pi*f/v)*A,.03)
ratio=43/3.2;p2=p*ratio;compressibility=45.8e-11;B2=1/compressibility;k2=2*math.pi*f/1500;A2=p2/(B2*k2)
examples['16.2']={'area_ratio':ratio,'fluid_pressure_Pa':p2,'fluid_bulk_modulus_Pa':B2,'fluid_displacement_m':A2}
close('16.2:equal_force',p*43e-6,p2*3.2e-6)
close('16.2:reported44pm',A2,4.4e-11,rtol=.01)
truth('16.2:liquid_lower_displacement_higher_pressure',A2<A and p2>p)
vw=math.sqrt(2.18e9/1000);lam=vw/262
examples['16.3']={'water_speed_m_s':vw,'wavelength_m':lam}
close('16.3:sonar5p64m',lam,5.64,rtol=.002)
close('16.3:frequency_preserved',vw/lam,262)
R=8.314;gamma=1.40;T=293.15;M=.0288;vg=math.sqrt(gamma*R*T/M)
examples['16.4']={'gas_speed_m_s':vg,'wavelength_20Hz_m':vg/20,'wavelength_20000Hz_m':vg/20000}
close('16.4:reported344',vg,344,rtol=.001)
for pressure in [.3e5,1.013e5,3e5]:
 density=pressure*M/(R*T)
 close(f'gas:pressure_cancellation:{pressure}',math.sqrt(gamma*pressure/density),vg)
rho=1.20;v=344.;I=.03**2/(2*rho*v)
examples['16.5']={'intensity_W_m2':I}
close('16.5:reported1p1microW_m2',I,1.1e-6,rtol=.01)
for amp in [3e-5,.03,30]:
 close(f'intensity:pressure_scaling:{amp}',amp**2/(2*rho*v)/I,(amp/.03)**2)
# Direct integration of pressure times particle velocity is independent of the
# author's algebraic average-sin-square implementation.
omega=2*math.pi*1000
A_consistent=.03/(rho*v*omega)
average=quad(lambda t:(.03*math.sin(omega*t))*(omega*A_consistent*math.sin(omega*t)),0,1/1000,epsabs=1e-18)[0]*1000
close('intensity:direct_PV_integral',average,I)
A20=1.2e-8*1000/20
examples['16.6']={'pressure_Pa':.03,'displacement_using_rounded_16_1_m':A20,'displacement_ratio':50}
close('16.6:reported0p60micrometre',A20,.6e-6)
for freq in [20,100,1000,20000]:
 amplitude=math.sqrt(2*I/(rho*v))/(2*math.pi*freq)
 close(f'intensity:fixed_I_fA:{freq}',freq*amplitude,math.sqrt(2*I/(rho*v))/(2*math.pi))
P=2*math.pi*20**2
examples['16.7']={'required_hemispherical_power_W':P}
close('16.7:reported2p5kW',P,2500,rtol=.01)
close('16.7:hemisphere_integral',quad(lambda th:2*math.pi*20**2*math.sin(th),0,math.pi/2)[0],P)
examples['16.8']={'I28_W_m2':1e-12*10**2.8,'I92_W_m2':1e-12*10**9.2,'health_dose_outcomes_verified':False}
for beta in [0,10,28,92,120,140]:
 intensity=1e-12*10**(beta/10)
 close(f'dB:roundtrip:{beta}',10*math.log10(intensity/1e-12),beta,atol=1e-10)
delta=10*math.log10(.25)
examples['16.9']={'level_change_dB':delta}
close('16.9:reported_minus6dB',delta,-6.0,rtol=.005)
examples['16.10']={'pressure_node_d_over_lambda':[.25,.75,1.25],'conceptual':True}
for j in range(6):
 x=(2*j+1)/4
 close(f'16.10:pressure_node:{j}',math.cos(2*math.pi*x),0,atol=1e-14)
 close(f'16.10:displacement_antinode:{j}',abs(math.sin(2*math.pi*x)),1)
Lclosed=344/(4*220);sharedf=5*220;Lopen=3*344/(2*sharedf)
examples['16.11']={'stopped_pipe_length_m':Lclosed,'shared_frequency_Hz':sharedf,'open_pipe_length_m':Lopen}
close('16.11:stopped3rdmode_is5thharmonic',344/(4*Lclosed)*5,1100)
close('16.11:open3rdharmonic',3*344/(2*Lopen),1100)
examples['16.12']={'string_to_air_wave_speed_ratio':.4,'string_length_to_pipe_ratio':.8}
close('16.12:fundamentals_equal',.4/(2*.8),1/4)
d=math.hypot(2,4)-math.hypot(1,4)
examples['16.13']={'path_difference_m':d,'constructive_fundamental_Hz':350/d,'destructive_lowest_Hz':350/(2*d)}
for n in range(1,6):
 fconstructive=n*350/d;fdestructive=(2*n-1)*350/(2*d)
 close(f'16.13:constructive_phase:{n}',math.cos(2*math.pi*fconstructive*d/350),1)
 close(f'16.13:destructive_phase:{n}',math.cos(2*math.pi*fdestructive*d/350),-1)
# Source-side phase origins and scalar/vector interference are tested directly.
for t in [.25,.75]:close(f'beats:envelope_max:{t}',abs(2*math.sin(math.pi*(18-16)*t)),2)
for t in [0,.5,1]:close(f'beats:envelope_min:{t}',abs(2*math.sin(math.pi*(18-16)*t)),0,atol=1e-14)
for t in np.linspace(0,1,17):
 direct=math.sin(2*math.pi*18*t)-math.sin(2*math.pi*16*t)
 factored=2*math.sin(math.pi*2*t)*math.cos(math.pi*34*t)
 close('beats:trig_identity:'+str(t),direct,factored,atol=1e-13)
pressure1=1.;pressure2=-1.;n1=np.array([1.,0.]);n2=np.array([0.,1.])
close('interference:pressure_cancellation',pressure1+pressure2,0)
truth('interference:nonparallel_particle_velocity_not_cancelled',np.linalg.norm(pressure1*n1+pressure2*n2)>0)

# Independently recover observed frequency from successive wavefront arrivals
# by solving ray/listener intersection equations, rather than substituting the
# textbook Doppler quotient as the numerical method.
def ray_frequency(vL,vS,c=340.,fs=300.,D=2000.):
 def arrival(te):
  sx=D+vS*te
  return brentq(lambda tr:sx-c*(tr-te)-vL*tr,te,te+30)
 t1=arrival(0);t2=arrival(1/fs)
 return 1/(t2-t1)
examples['16.14']={'static_wavelength_m':340/300,'front_wavelength_m':(340-30)/300,'rear_wavelength_m':(340+30)/300}
for pair,expected in [((0,30),300*340/370),((-30,0),300*310/340),((15,45),300*355/385)]:
 close('Doppler:ray_solution:'+str(pair),ray_frequency(*pair),expected,rtol=1e-9)
examples['16.15']={'received_Hz':ray_frequency(0,30)}
examples['16.16']={'received_Hz':ray_frequency(-30,0)}
examples['16.17']={'received_Hz':ray_frequency(15,45)}
for vs in [-80,-30,0,30,80]:
 for vl in [-60,0,60]:
  close(f'Doppler:general_ray:{vl}:{vs}',ray_frequency(vl,vs),(340+vl)/(340+vs)*300,rtol=1e-9)
for u in [-20,0,10,35]:close('Doppler:common_drift:'+str(u),ray_frequency(u,u),300,rtol=1e-9)
def echo_arrival(te,c=340.,u=30.,D=1000.):
 tw=brentq(lambda t:u*te+c*(t-te)-D,te,te+20)
 return brentq(lambda t:D-c*(t-tw)-u*t,tw,tw+20)
echo=1/(echo_arrival(1/300)-echo_arrival(0))
examples['16.18']={'wall_received_Hz':300*340/310,'echo_received_Hz':echo}
close('16.18:two_ray_intersections',echo,300*370/310,rtol=1e-10)
for u in [-.7,-.2,0,.2,.7]:
 ratio=math.sqrt((1-u)/(1+u))
 close(f'light_Doppler:rapidity:{u}',ratio,math.exp(-math.atanh(u)))
# The first arrival of a continuously supersonic moving source is the minimum
# over retarded emission time. It must agree with cone geometry.
Mach=1.75;h=8000.;c=320.;u=Mach*c
arrival=lambda te:te+math.hypot(u*te,h)/c
minimum=minimize_scalar(arrival,bounds=(-100,0),method='bounded',options={'xatol':1e-10})
alpha=math.asin(1/Mach);cone_delay=h/(u*math.tan(alpha))
examples['16.19']={'Mach_half_angle_deg':math.degrees(alpha),'delay_after_overhead_s':cone_delay,'first_arrival_by_retarded_minimum_s':minimum.fun,'distance_plane_travels_m':u*cone_delay}
close('16.19:retarded_first_arrival',minimum.fun,cone_delay)
close('16.19:reported20p5s',cone_delay,20.5,rtol=.003)

# Standing-wave boundary conditions: p=-B dy/dx. At the rigid end y=0,
# pressure is an antinode. An open end has pressure approximately zero.
for n in range(1,7):
 kn=n*math.pi
 close(f'open:pressure_end_left:{n}',math.sin(kn*0),0)
 close(f'open:pressure_end_right:{n}',math.sin(kn*1),0,atol=1e-14)
for n in [1,3,5,7,9]:
 kn=n*math.pi/2
 close(f'stopped:displacement_closed:{n}',math.sin(kn*0),0)
 close(f'stopped:pressure_open:{n}',math.cos(kn*1),0,atol=1e-14)

selfchecks['16.1']={'choice':5,'displacement_ratio':.25};close('self16.1:fixed_pressure',100/400,.25)
selfchecks['16.2']={'choice':1,'mercury_to_water_density_ratio':13.6,'mercury_speed_m_s':1451,'water_speed_m_s':1482,'bulk_modulus_ratio':13.6*(1451/1482)**2}
close('self16.2:mercury_bulk_modulus_ratio',selfchecks['16.2']['bulk_modulus_ratio'],13.0,rtol=.003)
selfchecks['16.3']={'A_ratio':math.sqrt(2),'pressure_ratio':math.sqrt(2),'B_ratio':1,'v_ratio':1,'level_change_dB':10*math.log10(2)}
close('self16.3:3dB',10*math.log10(2),3.0,rtol=.005)
selfchecks['16.4']={'choice':2,'helium_higher_frequency':True};truth('self16.4:helium_air',math.sqrt((5/3)/.004)>math.sqrt(1.4/.0288))
selfchecks['16.5']={'choices':[1,4]}
f0=[220,110,440,220];allowed=[range(1,10,2),range(1,10,2),range(1,10),range(1,10)]
truth('self16.5:modes', [i+1 for i,(fund,ns)in enumerate(zip(f0,allowed))if any(fund*n==660 for n in ns)]==[1,4])
selfchecks['16.6']={'choice':3,'different_frequencies_have_no_time_constant_phase_difference':True}
truth('self16.6:relative_phase_changes',not math.isclose(math.cos(2*math.pi*500*0),math.cos(2*math.pi*500*.001)))
selfchecks['16.7']={'choice':6,'possible_frequencies_Hz':[437,443]}
truth('self16.7:both_directions',[freq for freq in [434,437,443,446]if abs(freq-440)==3]==[437,443])
selfchecks['16.8']={'frequency_ratio':1};close('self16.8:uniform_wind',ray_frequency(10,10),300,rtol=1e-9)
selfchecks['16.9']={'choice':3,'receding_source_inside_cone_downshift':True};truth('self16.9:downshift',c/(c+u)<1)

table1=[['Air',20,344],['He',20,999],['H2',20,1330],['liquidHe',4,211],['mercury',20,1451],['water',0,1402],['water',20,1482],['water',100,1543],['Al',None,6420],['Pb',None,1960],['steel',None,5941]]
table2=[(140,100),(120,1),(95,3.2e-3),(90,1e-3),(70,1e-5),(65,3.2e-6),(50,1e-7),(40,1e-8),(20,1e-10),(10,1e-11),(0,1e-12)]
for beta,intensity in table2:close(f'table16.2:log_conversion:{beta}',1e-12*10**(beta/10),intensity,rtol=.012)
assert len(examples)==19 and len(selfchecks)==9
report={'status':'passed','scope':'Independent theory arithmetic and physical models for19examples/9selfchecks; not source/UI/deployment or health-dose certification.','exampleCount':19,'selfcheckCount':9,'assertionCount':len(checks),'examples':examples,'selfchecks':selfchecks,'sourceTable16_1':table1,'table16_1Scope':'Empirical values manually transcribed from originalPDF; not independently measured.','sourceTable16_2':table2,'checks':checks,'methods':['Direct wavefront arrival roots for Doppler','Two successive ray intersections for reflected sound','Retarded-time minimization for Mach cone arrival','Pressure-times-particle-velocity quadrature','Standing pressure/displacement boundary functions','Pressure cancellation versus vector particle velocity','Exact beat phase/trigonometric checks','Ideal gas pressure-density cancellation and relativistic rapidity identity']}
print(json.dumps(report,ensure_ascii=False,indent=2))
