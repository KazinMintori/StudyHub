from pathlib import Path
import math,json
B=Path(__file__).resolve().parent
pi=math.pi;v=344.;rho=1.20;bulk=1.42e5;Iref=1e-12;R=8.314
units={};tests=[]
def add(n,inputs,model,results):units[n]={'exercise':f'16.{n}','inputs_with_units':inputs,'model':model,'results_with_units':results}
def ck(n,name,a,b,tol=1e-9):
 ok=abs(a-b)<=tol;tests.append({'exercise':f'16.{n}','name':name,'actual':a,'expected':b,'tolerance':tol,'passed':ok});assert ok,(n,name,a,b)
def pressure(f,A):return bulk*2*pi*f/v*A
def intensity(p):return p*p/(2*rho*v)
def level(I):return 10*math.log10(I/Iref)
add(1,{'f0_Hz':1000,'A0_m':1.2e-8,'p0_Pa':.03,'pain_Pa':30,'pc_Pa':.0015},'same medium p_max proportional to f*A; use supplied calibration without adding rounded material constants',{'lambda_a_m':v/1000,'A_b_m':1.2e-8*30/.03,'f_c_Hz':1000*.0015/.03,'lambda_c_m':v/(1000*.0015/.03)})
ck(1,'part c calibration',.03*(50/1000),.0015)
add(2,{'A_m':1e-6,'pmax_Pa':10,'bulk_Pa':bulk},'pmax=BkA=2pi B f A/v; upper bound on f',{'fmax_Hz':10*v/(2*pi*bulk*1e-6),'audible':True})
ck(2,'pressure at limit',pressure(units[2]['results_with_units']['fmax_Hz'],1e-6),10)
pp=[pressure(f,2e-5) for f in [150,1500,15000]]
add(3,{'A_m':2e-5,'f_Hz':[150,1500,15000],'pain_Pa':30},'pmax=B(2pi f/v)A; compare pressure amplitude, not intensity, with30Pa',{'pmax_Pa':pp,'ratio_to_pain':[p/30 for p in pp]})
ck(3,'decade in f gives decade in p',pp[1]/pp[0],10);ck(3,'second decade',pp[2]/pp[1],10)
add(4,{'whale_f_Hz':17,'sea_v_m_s':1531,'dolphin_lambda_m':.015,'whistle_Hz':25000,'bat_Hz':[39000,78000],'tumor_m':.001,'tissue_v_m_s':1550},'lambda=v/f; ultrasound image criterion lambda<=tumor diameter/4',{'whale_lambda_m':1531/17,'dolphin_f_Hz':1531/.015,'whistle_lambda_m':v/25000,'bat_lambda_min_max_m':[v/78000,v/39000],'image_fmin_Hz':1550/(.001/4)})
ck(4,'image wavelength',1550/units[4]['results_with_units']['image_fmin_Hz'],.00025)
vb=math.sqrt(9e10/8600)
add(5,{'L_m':60,'brass_Y_Pa':9e10,'brass_rho_kg_m3':8600,'air_v_m_s':344},'rod sides free: vrod=sqrt(Y/rho), not bulk-fluid formula; separate transit times',{'brass_v_m_s':vb,'t_air_s':60/v,'t_brass_s':60/vb,'delay_s':60/v-60/vb})
ck(5,'metal arrival first',int(vb>v),1)
add(6,{'liquid_rho_kg_m3':1300,'f_Hz':400,'lambda_m':8,'bar_L_m':1.5,'bar_rho_kg_m3':6400,'bar_t_s':3.9e-4},'fluid B=rho(f lambda)^2; free-sided bar Y=rho(L/t)^2',{'fluid_v_m_s':3200,'B_Pa':1300*(400*8)**2,'bar_v_m_s':1.5/3.9e-4,'Y_Pa':6400*(1.5/3.9e-4)**2})
ck(6,'fluid speed recovered',math.sqrt(units[6]['results_with_units']['B_Pa']/1300),3200)
h=1482*(22-1.2)/344;d=h+1.2
add(7,{'land_path_m':22,'air_leg_to_surface_m':1.2,'air_v_m_s':344,'water_v_m_s':1482},'simultaneous arrivals mean22/v_air=1.2/v_air+h/v_water; requested distance includes air leg',{'water_depth_m':h,'horn_diver_distance_m':d,'arrival_s':22/344})
ck(7,'equal travel times',1.2/344+h/1482,22/344)
gases=[('H2',1.41,.00202),('He',1.67,.00400),('Ar',1.67,.0399),('air',1.40,.0288)]
speeds={name:math.sqrt(gamma*R*300.15/M) for name,gamma,M in gases}
add(8,{'T_K':300.15,'R_J_mol_K':R,'gamma_M_kg_mol':gases},'ideal gas v=sqrt(gamma R T/M), kelvin and kilograms per mole; gamma values fromTable19.1',{'speed_m_s':speeds,'ratio_to_air':{k:x/speeds['air'] for k,x in speeds.items()}})
ck(8,'ordering H2>He>air>Ar',int(speeds['H2']>speeds['He']>speeds['air']>speeds['Ar']),1)
T2=295.15*(1250*.285/325)**2
add(9,{'f_Hz':1250,'v_initial_m_s':325,'T_initial_K':295.15,'lambda_target_m':.285},'same gas and oscillator: target v=f lambda, v proportional sqrt(T)',{'v_target_m_s':1250*.285,'T_target_K':T2,'T_target_C':T2-273.15})
ck(9,'wavelength at new temperature',325*math.sqrt(T2/295.15)/1250,.285)
add(10,{'v0_m_s':344,'T0_K':293.15,'dT_K':1},'v=C sqrt(T); logarithmic differentiation dv/v=dT/(2T)',{'dv_for_plus_1K_m_s':344/(2*293.15),'exact_change_for_plus_1K_m_s':344*(math.sqrt(294.15/293.15)-1)})
ck(10,'differential approximation small error',units[10]['results_with_units']['dv_for_plus_1K_m_s']-units[10]['results_with_units']['exact_change_for_plus_1K_m_s'],0,.001)
eararea=pi*(.0084/2)**2;earI=Iref*10**2;E=earI*eararea
add(11,{'ear_diameter_m':.0084,'whisper_dB':20,'mosquito_kg':2e-6,'interval_s':1},'I=Iref*10^(beta/10); energy in1s=I area*1s; kinetic energy=mv^2/2',{'area_m2':eararea,'I_W_m2':earI,'power_W':E,'energy_in_1s_J':E,'mosquito_m_s':math.sqrt(2*E/2e-6),'mosquito_mm_s':1000*math.sqrt(2*E/2e-6)})
ck(11,'mosquito kinetic energy',.5*2e-6*(units[11]['results_with_units']['mosquito_m_s'])**2,E,1e-25)
add(12,{'level_increase_dB':13},'Delta beta=10log(I2/I1), only intensity ratio is needed',{'intensity_factor':10**1.3})
ck(12,'recover dB',10*math.log10(10**1.3),13)
add(13,{'r_initial_m':15,'beta_initial_dB':20,'beta_target_dB':60},'constant isotropic source: level change=20log(r1/r2)',{'distance_m':15*10**((20-60)/20),'intensity_factor':10**4})
ck(13,'geometric intensity gain',(15/.15)**2,1e4)
add(14,{'fixed_r_m':20,'level_increase_dB':5},'at fixed radius intensity proportional source power',{'power_factor':10**.5})
ck(14,'power factor in dB',10*math.log10(10**.5),5)
p15=pressure(320,5e-6);i15=intensity(p15)
add(15,{'f_Hz':320,'A_m':5e-6,'air_rho_kg_m3':rho,'air_B_Pa':bulk},'pmax=B omega A/v; I=pmax^2/(2rho v); beta=10log(I/Iref)',{'pmax_Pa':p15,'I_W_m2':i15,'beta_dB':level(i15)})
ck(15,'intensity from displacement',.5*rho*v*(2*pi*320*5e-6)**2,i15,1e-6)
add(16,{'level_reduction_dB':30,'second_intensity_ratio':.5},'intensity reduction and dB reduction differ: ratios exponentiate, levels add',{'remaining_fraction':10**-3,'removed_fraction':1-10**-3,'level_change_if_half_dB':10*math.log10(.5)})
ck(16,'remaining plus removed',.001+.999,1)
p17=6e-5;i17=intensity(p17);a17=p17*v/(bulk*2*pi*400)
add(17,{'f_Hz':400,'pmax_Pa':p17,'T_C':20},'traveling wave intensity from pressure amplitude, particle displacement A=pmax/(Bk)',{'I_W_m2':i17,'beta_dB':level(i17),'A_m':a17})
ck(17,'pressure recovered',pressure(400,a17),p17)
add(18,{'initial_babies':4,'independent_equal_intensity':True},'independent intensities add; same extra6.02dB means multiply total intensity by4 again',{'level_increase_dB':10*math.log10(4),'final_total_babies':16,'additional_babies':12})
ck(18,'same second level increase',10*math.log10(16/4),10*math.log10(4))
add(19,{'father_r_m':.30,'mother_r_m':1.50},'inverse-square intensity; Delta beta=20log(r_mother/r_father)',{'father_minus_mother_dB':20*math.log10(1.5/.30)})
ck(19,'intensity ratio',(.30/1.5)**-2,25)
add(20,{'a_delta_dB':5,'b_ratio':100,'c_ratio':2},'logarithmic level difference is10log intensity ratio',{'a_ratio':10**.5,'b_delta_dB':20,'c_delta_dB':10*math.log10(2)})
ck(20,'ratio a',10*math.log10(10**.5),5)
i21=Iref*10**5.3;r21=3*10**((53-53/4)/20)
add(21,{'initial_radius_m':3,'initial_dB':53},'distinguish quarter intensity from quarter numerical dB value; r2=r1 sqrt(I1/I2)',{'initial_I_W_m2':i21,'quarter_I_radius_m':6,'quarter_I_extra_walk_m':3,'quarter_level_dB':53/4,'quarter_level_radius_m':r21,'quarter_level_extra_walk_m':r21-3,'quarter_level_I_W_m2':Iref*10**(53/40)})
ck(21,'quarter numerical dB level',53-20*math.log10(r21/3),53/4)
lam22=v/1710;L22=5*lam22/2
add(22,{'pattern':'ANANANANANA','frequency_Hz':1710,'air_v_m_s':344,'helium_v_m_s':999},'both displacement endpoints antinodes=>open-open;10 quarter wavelengths=>fifth harmonic',{'quarter_intervals':10,'harmonic':5,'lambda_m':lam22,'L_m':L22,'f1_air_Hz':1710/5,'f1_helium_Hz':999/(2*L22)})
ck(22,'pattern intervals',len('ANANANANANA')-1,10);ck(22,'length',L22/(lam22/4),10)
L=1.2
open_modes=[];closed_modes=[]
for n in [1,2,3]:open_modes.append({'harmonic':n,'displacement_nodes_m':[(j+.5)*L/n for j in range(n)],'pressure_nodes_m':[j*L/n for j in range(n+1)]})
for n in [1,3,5]:closed_modes.append({'harmonic':n,'displacement_nodes_m':[2*j*L/n for j in range((n+1)//2)],'pressure_nodes_m':[(2*j+1)*L/n for j in range((n+1)//2)]})
add(23,{'L_m':L,'open_both_harmonics':[1,2,3],'stopped_harmonics':[1,3,5]},'displacement nodes correspond pressure antinodes; pressure nodes correspond displacement antinodes; open end pressure node, closed end displacement node',{'open_both':open_modes,'closed_left':closed_modes})
for mode in open_modes:
 n=mode['harmonic']
 for x in mode['displacement_nodes_m']:ck(23,f'open n{n} displacement node{x}',math.cos(n*pi*x/L),0)
 for x in mode['pressure_nodes_m']:ck(23,f'open n{n} pressure node{x}',math.sin(n*pi*x/L),0)
for mode in closed_modes:
 n=mode['harmonic']
 for x in mode['displacement_nodes_m']:ck(23,f'stopped n{n} displacement node{x}',math.sin(n*pi*x/(2*L)),0)
 for x in mode['pressure_nodes_m']:ck(23,f'stopped n{n} pressure node{x}',math.cos(n*pi*x/(2*L)),0)
L24=v/(2*524)
add(24,{'f_open_Hz':524},'same length: open fundamental lambda=2L; stopped fundamental lambda=4L',{'L_m':L24,'lambda_stopped_m':4*L24,'f_stopped_Hz':v/(4*L24)})
ck(24,'frequency halved',v/(4*L24),262)
add(25,{'tract_L_m':.17,'v_m_s':344,'boundary':'one closed one open'},'closed-open resonance has odd harmonics1,3,5',{'first_three_f_Hz':[n*v/(4*.17) for n in [1,3,5]]})
ck(25,'third allowed mode index',units[25]['results_with_units']['first_three_f_Hz'][2]/units[25]['results_with_units']['first_three_f_Hz'][0],5)
add(26,{'lowest_Hz':220,'highest_Hz':1244,'v_m_s':354,'boundary':'open mouth,closed diaphragm model'},'lowest note treated as stopped-pipe fundamental; use354m/s explicitly',{'air_column_L_m':354/(4*220),'range_octaves':math.log2(1244/220)})
ck(26,'lowest frequency recovered',354/(4*units[26]['results_with_units']['air_column_L_m']),220)
add(27,{'L_m':4.88},'fundamental open-open v/(2L), stopped v/(4L)',{'open_f_Hz':v/(2*4.88),'stopped_f_Hz':v/(4*4.88)})
ck(27,'ratio',units[27]['results_with_units']['open_f_Hz']/units[27]['results_with_units']['stopped_f_Hz'],2)
add(28,{'L_m':2.5,'both_closed':True},'both ends displacement nodes: sin(kL)=0=>kL=npi; all positive integers allowed',{'lambda_first3_m':[5/n for n in [1,2,3]],'frequency_first3_Hz':[n*v/5 for n in [1,2,3]],'audible_first3':True})
ck(28,'all first three audible',int(all(20<f<20000 for f in units[28]['results_with_units']['frequency_first3_Hz'])),1)
lam29=v/1710;L29=9*lam29/4
add(29,{'pattern':'NANANANANA','frequency_Hz':1710,'v_m_s':344},'left displacement node,right antinode=>stopped-open;9 quarter-wavelength intervals=>n9, fourth overtone',{'quarter_intervals':9,'harmonic':9,'L_m':L29,'f1_Hz':1710/9})
ck(29,'pattern intervals',len('NANANANANA')-1,9)
vw=math.sqrt(4110/(.00725/.62));fw=3*vw/(2*.62);Lp=v/(4*fw)
add(30,{'wire_L_m':.62,'wire_m_kg':.00725,'tension_N':4110,'wire_mode':'second overtone=third harmonic'},'resonance matches stopped-pipe fundamental to wire third harmonic',{'wire_mu_kg_m':.00725/.62,'wire_speed_m_s':vw,'wire_third_f_Hz':fw,'pipe_length_m':Lp})
ck(30,'resonance frequencies',v/(4*Lp),fw)
add(31,{'empty_air_length_m':.14,'half_full_air_length_m':.07},'test tube is stopped pipe; water halves vibrating air length',{'empty_f_Hz':v/(4*.14),'half_full_f_Hz':v/(4*.07)})
ck(31,'frequency doubles',units[31]['results_with_units']['half_full_f_Hz']/units[31]['results_with_units']['empty_f_Hz'],2)
lam32=v/725
add(32,{'f_Hz':725,'initial_path_m':4.5,'in_phase':True},'moving A away by d increases path difference by d; destructive odd half-lambda, first nonzero constructive lambda',{'lambda_m':lam32,'first_destructive_d_m':lam32/2,'second_destructive_d_m':3*lam32/2,'first_nonzero_constructive_d_m':lam32})
ck(32,'first minimum relative phase',2*pi*(lam32/2)/lam32,pi)
add(33,{'speaker_separation_m':2,'Q_beyond_B_m':1,'in_phase':True},'path lengths3m and1m; fixed difference2m; lowest positive constructive frequency v/Delta r, destructive v/(2Delta r)',{'delta_r_m':2,'lowest_constructive_Hz':v/2,'lowest_destructive_Hz':v/4})
ck(33,'constructive path /lambda',2/(v/172),1);ck(33,'destructive path /lambda',2/(v/86),.5)
lam34=v/206;des=[1-lam34/4,1+lam34/4];cons=[1-lam34/2,1,1+lam34/2]
add(34,{'speaker_separation_m':2,'f_Hz':206,'x_domain_m':[0,2],'in_phase':True},'rA=x,rB=2-x; abs(path difference)=abs(2-2x); enumerate allowed interference orders within2m',{'lambda_m':lam34,'destructive_x_m':des,'constructive_x_m':cons,'next_destructive_delta_m':3*lam34/2})
for x in des:ck(34,f'destructive{x}',abs(2-2*x)/lam34,.5)
for x,target in zip(cons,[1,0,1]):ck(34,f'constructive{x}',abs(2-2*x)/lam34,target)
add(35,{'speaker_separation_m':12,'f_Hz':688},'between speakers, path difference changes by twice listener displacement; adjacent max to min requires lambda/2 path change',{'lambda_m':v/688,'nearest_walk_m':v/688/4})
ck(35,'distance',v/688/4,.125)
lam36=v/172;dist=[8-(2*m+1)*lam36/2 for m in range(10) if 8-(2*m+1)*lam36/2>=0]
add(36,{'distance_to_A_m':8,'f_Hz':172},'destructive path difference=(m+1/2)lambda; minimize nonnegative distance toB',{'lambda_m':lam36,'possible_B_distances_below_8_m':dist,'minimum_B_distance_m':min(dist)})
ck(36,'closest B',min(dist),1)
delta37=math.hypot(4.5,2)-4.5;base=v/delta37
add(37,{'upper_speaker_to_mic_m':4.5,'speaker_vertical_separation_m':2,'in_phase':True},'source paths from right triangle; constructive f=m v/Delta r,m>=1; destructive f=(m+1/2)v/Delta r,m>=0',{'lower_path_m':math.hypot(4.5,2),'delta_r_m':delta37,'constructive_base_Hz':base,'destructive_base_Hz':base/2})
ck(37,'minimum phase',2*pi*(base/2)*delta37/v,pi)
add(38,{'lambda_m':[.648,.652]},'beat frequency abs(f1-f2)=v abs(1/lambda1-1/lambda2)',{'frequency_Hz':[v/.648,v/.652],'beat_Hz':v*abs(1/.648-1/.652)})
ck(38,'beat from frequency difference',abs(v/.648-v/.652),units[38]['results_with_units']['beat_Hz'])
add(39,{'reference_Hz':440,'initial_beat_Hz':3,'beat_after_tightening_Hz':4},'tightening raises string frequency; continuously increasing beat means initial note above reference',{'initial_violin_Hz':443,'after_slight_tightening_Hz':444,'required_action':'loosen'})
ck(39,'initial beat',abs(443-440),3);ck(39,'after tightening',abs(444-440),4)
freq40=[v/(4*x) for x in [1.14,1.16]]
add(40,{'initial_lengths_m':[1.14,1.14],'added_length_m':.02,'boundary':'one closed one open'},'stopped-pipe fundamental v/4L; beats are absolute difference',{'fundamental_Hz':freq40,'beat_Hz':abs(freq40[0]-freq40[1])})
ck(40,'longer pipe lower pitch',int(freq40[1]<freq40[0]),1)
vsound=1240*25/(1240-1200)
add(41,{'approaching_source_m_s':25,'source_f_Hz':1200,'stationary_listener_f_Hz':1240},'source moves toward stationary listener in medium; fL=fS*v/(v-vS); solve for unknown medium speed',{'sound_speed_m_s':vsound})
ck(41,'Doppler recovery',1200*vsound/(vsound-25),1240)
assert sorted(units)==list(range(1,42))
print(json.dumps({'status':'passed','units':[units[n]for n in sorted(units)],'unitCount':len(units),'assertionCount':len(tests),'assertions':tests},ensure_ascii=False,indent=2))
