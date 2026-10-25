from pathlib import Path
import json,math
B=Path(__file__).resolve().parent
pi=math.pi;g=9.80;c=3e8
rows=[];assertions=[]
def check(label,actual,expected,tol=1e-10):
 ok=math.isclose(actual,expected,rel_tol=tol,abs_tol=tol);assertions.append({'label':label,'actual':actual,'expected':expected,'passed':ok});assert ok,label
def add(n,inputs,results):rows.append({'id':f'15.{n}','source_inputs_with_units':inputs,'results':results})
add(1,{'v_m_s':344,'f_Hz':784},{'lambda_m':344/784,'T_ms':1000/784,'higher_lambda_m':344/(2*784)})
add(2,{'v_m_s':1500,'max_lambda_m':.001},{'minimum_f_Hz':1500/.001})
add(3,{'lambda_m':800000,'T_s':3600},{'v_m_s':800000/3600,'v_km_h':800})
add(4,{'highest_to_lowest_s':2.5,'vertical_distance_m':.53,'lambda_m':4.8},{'T_s':5,'v_m_s':4.8/5,'A_m':.53/2,'changed_A_m':.30/2,'changed_v_m_s':4.8/5})
add(5,{'sound_air_m_s':344,'audible_f_Hz':[20,20000],'light_lambda_m':[380e-9,750e-9],'c_m_s':c,'ultrasound_Hz':23000,'body_sound_m_s':1480},{'audible_lambda_m':[344/20000,344/20],'light_f_Hz':[c/750e-9,c/380e-9],'ultrasound_air_lambda_m':344/23000,'body_lambda_m':1480/23000})
m=.004;A=.008;w=2*pi*20
add(6,{'m_kg':m,'A_m':A,'f_Hz':20},{'amax_m_s2':w*w*A,'net_vertical_force_amplitude_N':m*w*w*A,'maximum_upward_string_force_N':m*(g+w*w*A)})
v=8;lam=.320;f=v/lam;k=2*pi/lam;w=2*pi*f;phase=k*.360+w*.150
wait=(-phase)%(2*pi)/w
add(7,{'v_m_s':v,'A_m':.0700,'lambda_m':lam,'direction':'-x','x_m':.360,'t_s':.150},{'f_Hz':f,'T_s':1/f,'k_rad_m':k,'omega_rad_s':w,'y_m':.07*math.cos(phase),'phase_rad':phase,'wait_to_next_peak_s':wait})
check('15.7:next peak',math.cos(phase+w*wait),1)
add(8,{'A_m':.0065,'lambda_m':.28,'T_s':.036},{'A_mm':6.5,'f_Hz':1/.036,'v_m_s':.28/.036,'direction':'+x'})
add(9,{'functions':['A cos(kx+omega t)','A sin(kx+omega t)','A(cos kx+cos omega t)']},{'satisfies_wave_equation':[True,True,False],'speed_relation':'v=omega/k','vy_b':'A omega cos(kx+omega t)','ay_b':'-A omega² sin(kx+omega t)'})
A=.0275;k=41;w=6.2
add(10,{'A_m':A,'k_rad_m':k,'omega_rad_s':w},{'T_s':2*pi/w,'lambda_m':2*pi/k,'f_Hz':w/(2*pi),'crest_speed_m_s':w/k,'floater_max_speed_m_s':w*A,'direction':'-x'})
add(11,{'graph':'E15.11','A_m':.004,'T_s':.040,'delta_x_m':.09,'x0_peak_s':.01,'x09_peak_s':.035,'within_one_wavelength':True},{'plus_delay_s':.025,'plus_v_m_s':.09/.025,'plus_lambda_m':.09/.025*.04,'minus_delay_s':.015,'minus_v_m_s':.09/.015,'minus_lambda_m':.09/.015*.04})
check('15.11:positive phase',.09/(.09/.025*.04),.025/.04)
add(12,{'wave':'A cos[2pi(x-vt)/lambda]'}, {'vy':'(2pi A v/lambda) sin[2pi(x-vt)/lambda]','vymax_over_v':'2pi A/lambda','equal_condition':'A=lambda/(2pi)','less_condition':'A<lambda/(2pi)','greater_condition':'A>lambda/(2pi)'})
xs=[1.5*i for i in range(9)];times=[0,.4,.8]
table=[[.300*math.cos(2*pi*(x-6*t)/12)for x in xs]for t in times]
add(13,{'A_cm':.300,'lambda_cm':12,'v_cm_s':6,'x_cm':xs,'times_s':times},{'y_cm_by_time':table,'T_s':2,'direction':'+x','shift_cm':[0,2.4,4.8]})
for j,t in enumerate(times):check('15.13:translated shape '+str(t),.3*math.cos(2*pi*(6*t-6*t)/12),.3)
add(14,{'frequency_ratio':2,'fixed_L_mu':True},{'tension_ratio':4})
mu=.048;v=math.sqrt(1.5*g/mu);v2=math.sqrt(3*g/mu)
add(15,{'f_Hz':120,'mu_kg_m':mu,'hanging_m_kg':1.5,'new_hanging_m_kg':3},{'v_m_s':v,'lambda_m':v/120,'new_v_m_s':v2,'new_lambda_m':v2/120,'factor':math.sqrt(2)})
add(16,{'L_m':2.5,'m_kg':.12,'f_Hz':40,'lambda_m':.75},{'v_m_s':30,'tension_N':(.12/2.5)*30**2})
M=54;L=3.8;t=.049;q=g*t*t/(4*L)
add(17,{'L_m':L,'hung_mass_kg':M,'travel_s':t},{'uniform_tension_mass_kg':M*g*t*t/L,'exact_variable_tension_mass_kg':4*M*q/(1-q)**2,'inferred_wire_to_load_ratio':g*t*t/L})
L=1.5;weight=.0125;k=172;w=4830;v=w/k;mu=weight/(g*L)
add(18,{'L_m':L,'wire_weight_N':weight,'A_m':.0085,'k_rad_m':k,'omega_rad_s':w,'direction_up':'+x'},{'v_m_s':v,'travel_s':L/v,'W_N':mu*v*v,'lambda_m':2*pi/k,'wavelength_count':L*k/(2*pi)})
v=.0333*625
add(19,{'L_m':.750,'m_kg':.0165,'lambda_m':.0333,'f_Hz':625},{'v_m_s':v,'tension_N':(.0165/.750)*v*v})
mu=(29.4/g)/6;Ts=[.5*g,.5*g+29.4/2,.5*g+29.4];vs=[math.sqrt(T/mu)for T in Ts]
add(20,{'L_m':6,'rope_weight_N':29.4,'hung_m_kg':.5},{'mu_kg_m':mu,'tension_bottom_middle_top_N':Ts,'speed_bottom_middle_top_m_s':vs,'endpoint_average_speed_m_s':(vs[0]+vs[2])/2})
check('15.20:middle tension average',Ts[1],(Ts[0]+Ts[2])/2)
mu=.5;force=100;A=.60;period=1;v=math.sqrt(force/mu);P=.5*mu*(2*pi/period)**2*A*A*v
add(21,{'mu_kg_m':mu,'estimated_A_m':A,'estimated_tension_N':force,'estimated_T_s':period,'estimates_not_source_data':True},{'v_m_s':v,'P_W':P,'new_power_ratio':(.5)**2*2**2})
mu=.003/.8;v=math.sqrt(25/mu);P=.5*mu*(2*pi*120)**2*.0016**2*v
add(22,{'m_kg':.003,'L_m':.8,'tension_N':25,'f_Hz':120,'A_m':.0016},{'v_m_s':v,'P_W':P,'half_amplitude_P_W':P/4})
add(23,{'tension_N':94,'v_m_s':406,'f_Hz':69,'P_W':.365},{'A_m':math.sqrt(2*.365*406/(94*(2*pi*69)**2))})
target=7.5*math.sqrt(.11/1)
add(24,{'r0_m':7.5,'I0_W_m2':.11,'target_I_W_m2':1},{'target_radius_m':target,'closer_distance_m':7.5-target})
add(25,{'I0_W_m2':10,'r0_m':30,'desired_I_W_m2':1e-6},{'minimum_radius_m':30*math.sqrt(10/1e-6),'friend_I_W_m2':1e-6/4,'sound_power_W':4*pi*30**2*10})
A=.00230;k=6.98;w=742;mu=.00338/1.35;v=w/k
add(26,{'A_m':A,'k_rad_m':k,'omega_rad_s':w,'L_m':1.35,'m_kg':.00338},{'f_Hz':w/(2*pi),'lambda_m':2*pi/k,'v_m_s':v,'direction':'-x','mu_kg_m':mu,'tension_N':mu*v*v,'P_W':.5*mu*w*w*A*A*v})
P=4*pi*4.3**2*.026
add(27,{'I0_W_m2':.026,'r0_m':4.3,'r_m':3.1,'elapsed_s':3600},{'I_W_m2':.026*(4.3/3.1)**2,'power_W':P,'energy_J':P*3600})
add(28,{'A_mm':4,'half_width_mm':4,'distance_leading_edge_to_O_mm':8,'v_mm_s':400,'times_ms':[15,20,25,30,35,40,45]}, {'initial_support_mm':[-16,-8],'initial_peak_mm':-12,'first_contact_ms':20,'peak_at_end_ms':30,'complete_reflection_ms':40,'fixed_sign':-1,'free_sign':1})
add(29,{'A_mm':5,'width_mm':20,'leading_distance_mm':10,'v_mm_s':5000,'times_ms':[1,2,3,4,5,6,7]}, {'initial_support_mm':[10,30],'first_contact_ms':2,'complete_reflection_ms':6,'fixed_sign':-1,'free_sign':1})
for n,sign in [(30,1),(31,-1)]:
 add(n,{'pulse_A_cm':1,'half_width_cm':1,'leading_gap_cm':1,'speed_cm_s':2,'rightmoving_initial_peak_cm':-1.5,'leftmoving_initial_peak_cm':1.5,'leftmoving_sign':sign,'times_s':[.25,.5,.75,1,1.25]}, {'peak_coordinates_cm':[[-1.5+2*t,1.5-2*t]for t in [.25,.5,.75,1,1.25]],'full_overlap_s':.75,'full_overlap_amplitude_cm':1+sign})
add(32,{'rightmoving_height_mm':3,'leftmoving_height_mm':-4,'width_mm':4,'gap_mm':8,'speed_mm_s':1,'times_s':[4,6,10]}, {'rightmoving_supports_mm':[[t-4,t]for t in [4,6,10]],'leftmoving_supports_mm':[[8-t,12-t]for t in [4,6,10]],'full_overlap_s':6,'full_overlap_height_mm':-1})
add(33,{'estimated_violin_L_m':.33,'violin_E5_f_Hz':659,'estimated_bass_L_m':1.10,'bass_G2_f_Hz':98,'air_speed_m_s':344,'lengths_are_estimates':True},{'violin_string_lambda_m':.66,'violin_string_v_m_s':2*.33*659,'violin_air_lambda_m':344/659,'bass_string_lambda_m':2.2,'bass_string_v_m_s':2*1.1*98,'bass_air_lambda_m':344/98})
add(34,{'adjacent_antinodes_m':.150,'antinode_A_m':.00850,'T_s':.0750},{'node_spacing_m':.15,'lambda_m':.30,'traveling_A_m':.0085/2,'wave_speed_m_s':.30/.075,'antinode_max_speed_m_s':2*pi/.075*.0085,'antinode_min_speed_m_s':0,'node_to_antinode_m':.075})
add(35,{'standing_A_m':.0025,'omega_rad_s':942,'k_rad_m':.750*pi},{'lambda_m':2*pi/(.75*pi),'node_step_m':pi/(.75*pi),'first_antinode_m':pi/(2*.75*pi),'antinode_step_m':pi/(.75*pi)})
add(36,{'L_m':1.5,'v_m_s':62,'mode_n':[1,3,4]},{'wavelengths_m':[3/n for n in [1,3,4]],'frequencies_Hz':[62*n/3 for n in [1,3,4]]})
L=.8;mu=.040/L;f=60;A=.003;v=2*L*f
add(37,{'m_kg':.040,'L_m':L,'fundamental_f_Hz':f,'antinode_A_m':A},{'v_m_s':v,'tension_N':mu*v*v,'max_transverse_speed_m_s':2*pi*f*A,'max_transverse_acceleration_m_s2':(2*pi*f)**2*A})
v=math.sqrt(800/(.003/.4));f1=v/(2*.4);n=math.floor(10000/f1)
add(38,{'tension_N':800,'L_m':.4,'m_kg':.003,'hearing_max_Hz':10000},{'v_m_s':v,'f1_Hz':f1,'highest_n':n,'highest_f_Hz':n*f1,'next_f_Hz':(n+1)*f1})
check('15.38:harmonic bracket',float(n*f1<=10000<(n+1)*f1),1)
k=3.40;w=50;A=.056;L=3*pi/k
add(39,{'standing_A_m':A,'k_rad_m':k,'omega_rad_s':w,'harmonic_n':3},{'traveling_A_m':A/2,'L_m':L,'lambda_m':2*pi/k,'f_Hz':w/(2*pi),'T_s':2*pi/w,'wave_speed_m_s':w/k,'max_transverse_speed_m_s':w*A,'eighth_k_rad_m':8*pi/L,'eighth_omega_rad_s':8*w/3,'eighth_amplitude_phase':'Not fixed by the stated data.'})
check('15.39:third-mode right node',math.sin(k*L),0)
check('15.39:eighth-mode right node',math.sin(8*pi/L*L),0)
k=32.5;w=754;A=.00444
add(40,{'standing_A_m':A,'k_rad_m':k,'omega_rad_s':w},{'traveling_A_m':A/2,'lambda_m':2*pi/k,'f_Hz':w/(2*pi),'speed_m_s':w/k,'mode_n':'Cannot infer without L or total count of loops.'})
check('15.6:Newton force balance',rows[5]['results']['maximum_upward_string_force_N']-.004*g,rows[5]['results']['net_vertical_force_amplitude_N'])
check('15.15:tension ratio speed',rows[14]['results']['new_v_m_s']**2/rows[14]['results']['v_m_s']**2,2)
wire=rows[16]['results']['exact_variable_tension_mass_kg'];mu17=wire/3.8
steps=10000;h=3.8/steps
integrand=lambda z:math.sqrt(mu17/(g*(54+mu17*z)))
integral=h/3*(integrand(0)+integrand(3.8)+4*sum(integrand(i*h)for i in range(1,steps,2))+2*sum(integrand(i*h)for i in range(2,steps,2)))
check('15.17:direct variable-tension travel integral',integral,.049)
check('15.18:force to propagation speed',math.sqrt(rows[17]['results']['W_N']/(.0125/(g*1.5))),rows[17]['results']['v_m_s'])
check('15.20:wave speeds not arithmetic mean',float(abs(rows[19]['results']['speed_bottom_middle_top_m_s'][1]-rows[19]['results']['endpoint_average_speed_m_s'])>.1),1)
# Direct average of force times transverse velocity, independent of the mean-power formula.
N=8000;f22=120;A22=.0016;v22=rows[21]['results']['v_m_s'];w22=2*pi*f22;k22=w22/v22
work_power=sum(25*A22*A22*k22*w22*math.sin(2*pi*(i+.5)/N)**2 for i in range(N))/N
check('15.22:direct transverse work-rate average',work_power,rows[21]['results']['P_W'])
check('15.23:inverse power',.5*(94/406**2)*406*(2*pi*69)**2*rows[22]['results']['A_m']**2,.365)
check('15.24:threshold radius inverse square',.11*(7.5/rows[23]['results']['target_radius_m'])**2,1)
check('15.25:target intensity inverse square',10*(30/rows[24]['results']['minimum_radius_m'])**2,1e-6)
check('15.26:power as force-work',.5*rows[25]['results']['tension_N']*(742/rows[25]['results']['v_m_s'])*742*.0023**2,rows[25]['results']['P_W'])
check('15.27:energy divided by time',rows[26]['results']['energy_J']/3600,rows[26]['results']['power_W'])
check('15.34:two traveling-wave amplitudes',2*rows[33]['results']['traveling_A_m'],.0085)
check('15.37:fundamental speed boundary',rows[36]['results']['v_m_s']/60,2*.8)
for n in range(4):
 check('15.35:node '+str(n),math.sin(.75*pi*(4*n/3)),0)
 check('15.35:antinode '+str(n),abs(math.sin(.75*pi*(4*n+2)/3)),1)
for x,t in [(.017,.003),(.11,.005),(.28,.007)]:
 check('15.40:counterpropagating decomposition '+str(x),.00222*math.cos(32.5*x-754*t)-.00222*math.cos(32.5*x+754*t),.00444*math.sin(32.5*x)*math.sin(754*t))
for fun in [math.cos,math.sin]:
 x=.31;t=.22;k=2.3;w=4.7;v=w/k;h=1e-4
 wave=lambda x,t:fun(k*x+w*t)
 xx=(wave(x+h,t)-2*wave(x,t)+wave(x-h,t))/h**2
 tt=(wave(x,t+h)-2*wave(x,t)+wave(x,t-h))/h**2
 check('15.9:finite-difference wave PDE '+fun.__name__,xx,tt/v**2,1e-6)
assert [r['id']for r in rows]==[f'15.{n}'for n in range(1,41)]
print(json.dumps({'status':'passed','units':rows,'assertionCount':len(assertions),'assertions':assertions},ensure_ascii=False,indent=2))
