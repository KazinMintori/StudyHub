from pathlib import Path
from math import pi,sqrt,sin,asin,cos,tan,log10,isclose
import json
B=Path(__file__).resolve().parent
v=344.;g=9.80;R=8.314;Mair=.0288;gamma=1.40
rows=[];assertions=[]
def add(n,inputs,results,formula):rows.append({'exercise':f'16.{n}','inputs':inputs,'results':results,'formula':formula})
def check(name,a,b,tol=1e-9):
 ok=isclose(a,b,rel_tol=tol,abs_tol=tol);assertions.append({'name':name,'actual':a,'expected':b,'pass':ok});assert ok,(name,a,b)

lp=(v-25)/400;lm=(v+25)/400
add(42,{'v':v,'source_speed':25,'f':400},{'lambda_front_m':lp,'lambda_back_m':lm,'f_front_Hz':v/lp,'f_back_Hz':v/lm},'lambda_front/back=(v-/+uS)/fS; stationary fL=v/lambda')
fa=392*(v-15)/v;fb=392*(v+15)/(v+35)
add(43,{'v':v,'f_each':392,'uA':0,'uB':35,'uL':15},{'fA_Hz':fa,'fB_Hz':fb,'beats_Hz':abs(fa-fb)},'For A ray +x: fA=f(v-uL)/v. For B ray -x: fB=f(v+uL)/(v+uB).')
add(44,{'fS_Hz':1000,'approach_speed_fraction':.5},{'source_moving_f_Hz':2000,'listener_moving_f_Hz':1500},'Source changes wavelength; listener changes encounter speed.')
u=.32-.12/1.6;back=(.32+u)*1.6
add(45,{'T_s':1.6,'wave_v_m_s':.32,'front_lambda_m':.12},{'duck_u_m_s':u,'back_lambda_m':back},'lambda_front=(v-u)T; lambda_back=(v+u)T')
add(46,{'v':v,'fS':352,'uS':30,'uL':18},{'approach_Hz':352*(v+18)/(v-30),'recede_Hz':352*(v-18)/(v+30)},'Use velocities of source and listener separately relative to still air.')
add(47,{'v':v,'fS':520,'fL':490},{'listener_speed_m_s':v*(1-490/520)},'fL=fS(v-uL)/v')
u=v*(1-260/266)
add(48,{'v':v,'stationary_horn_Hz':260,'beats_Hz':6},{'moving_horn_heard_Hz':266,'friend_u_m_s':u},'Approaching moving source has fL>260, so fL=266; u=v(1-fS/fL).')
add(49,{'v':340,'source_and_listener_ground_u':15,'fS':500},{'wave_speed_relative_listener_m_s':355,'lambda_m':355/500,'fL_Hz':500},'Backward ray: lambda=(v+uS)/fS; relative wave speed=v+uL; fL cancels when uS=uL.')
fT=2000*(v-20)/(v-30);fD=fT*(v+30)/(v+20);lam=(v+20)/fT
add(50,{'v':v,'fS':2000,'fire_u':30,'truck_u':20},{'truck_hears_Hz':fT,'driver_reflection_Hz':fD,'reflected_lambda_m':lam},'Two Doppler stages; truck moves away then acts as moving secondary source. Driver wave speed is v+30.')
check('50 reflected lambda in moving frame',(v+30)/fD,lam)
u=v*(1250-1200)/(1250+1200);fnew=1250*(v+20)/(v-20)
add(51,{'v':v,'emitted_Hz':1200,'stationary_received_Hz':1250,'new_police_u':20},{'other_car_u_m_s':u,'direction':'toward police','new_reflection_Hz':fnew},'Stationary echo ratio=(v+u)/(v-u). Keep target ground speed fixed in second experiment.')
check('51 direct two stages',1200*(v+u)/(v-20)*(v+20)/(v-u),fnew)
add(52,{'slope_per_m':1.75,'intercept_Hz':600},{'source_f_Hz':600,'sound_speed_m_s':600/1.75},'fL=fS+(fS/v)uL')
Mach=1.70;alpha=asin(1/Mach);time=1250/(Mach*v*tan(alpha))
add(53,{'Mach':Mach,'altitude_m':1250,'sound_v':v},{'cone_half_angle_deg':alpha*180/pi,'delay_s':time,'plane_horizontal_distance_at_boom_m':1250/tan(alpha)},'sin alpha=1/M; plane travels h*cot(alpha) after overhead.')
u=331/sin(58*pi/180);Mlow=u/344;alow=asin(1/Mlow)
add(54,{'angle_deg':58,'local_sound_v':331,'low_sound_v':344},{'Mach':u/331,'u_m_s':u,'u_mph':u/.44704,'low_Mach':Mlow,'low_angle_deg':alow*180/pi},'u=v/sin(alpha); speed fixed in low-altitude comparison.')
v0=sqrt(gamma*R*273/Mair)
add(55,{'gamma':gamma,'R':R,'Mair':Mair,'T0_K':273},{'v0_m_s':v0,'v20_linear_m_s':332*(1+20/546),'v20_square_root_m_s':332*sqrt(1+20/273),'v120_linear_m_s':332*(1+120/546),'v120_square_root_m_s':332*sqrt(1+120/273),'third_to_second_term_ratio_at120':120/(4*273)},'sqrt(1+x)=1+x/2-x²/8+...; x=TC/273. Approximate v0=332 used by source.')
I=1e-12*10**5.2;rho=1.20;p=sqrt(2*rho*v*I);A=p/(rho*v*2*pi*587);r=5*10**((52-30)/20)
add(56,{'r_m':5,'level_dB':52,'f_Hz':587,'rho_air':rho,'v':v},{'I_W_m2':I,'pressure_amplitude_Pa':p,'displacement_amplitude_m':A,'r_at30dB_m':r},'I=pmax²/(2rho v); pmax=rho v omega A; inverse-square intensity.')
C=gamma*R/Mair;Tbottom=298.15;Ttop=278.15;a=(Tbottom-Ttop)/300
t=2*(sqrt(Tbottom)-sqrt(Ttop))/(a*sqrt(C));vt=sqrt(C*Ttop)
add(57,{'Tsurface_C':25,'T300m_C':5,'height_m':300,'C':C},{'travel_time_s':t,'top_v_m_s':vt,'horizontal_distance_m':vt*t},'T(z)=298.15-z/15; dt=dz/sqrt(C*T(z)); horizontal top path has constant vtop.')
FA=165/2+185/4;FB=165/2+3*185/4;mu=.0055/.75;fA=sqrt(FA/mu)/(2*.75);fB=sqrt(FB/mu)/(2*.75)
add(58,{'bar_weight_N':165,'cube_weight_N':185,'cube_position_fraction':.75,'wire_L_m':.75,'wire_mass_kg':.0055},{'FA_N':FA,'FB_N':FB,'fA_Hz':fA,'fB_Hz':fB,'beats_Hz':fB-fA},'Static torques set tensions; each wire f1=sqrt(F/mu)/(2L).')
base=(1764-1372)/2;L=v/(4*base)
add(59,{'frequencies_Hz':[1372,1764],'v':v},{'pipe':'one end closed','harmonics':[7,9],'fundamental_Hz':base,'L_m':L},'Open pipe would require integer1372/392=3.5, impossible. Stopped pipe adjacent odd modes differ2f1.')
vg=1200*(2*.470);Temp=293.15*(vg/999)**2
add(60,{'f_Hz':1200,'node_distance_m':.470,'helium20C_v_m_s':999},{'lambda_m':.94,'v_m_s':vg,'temperature_K':Temp,'temperature_C':Temp-273.15},'Adjacent nodes of either pressure or displacement separated lambda/2. v²/T constant for same helium.')
D=2;lam=v/784;solve=lambda delta:(D*D-delta*delta)/(2*delta)
des=[(m,(m+.5)*lam,solve((m+.5)*lam)) for m in range(8) if (m+.5)*lam<=D]
con=[(m,m*lam,solve(m*lam)) for m in range(1,8) if m*lam<=D]
add(61,{'speaker_separation_m':2,'f_Hz':784,'v':v},{'lambda_m':lam,'destructive_m_delta_x':des,'constructive_m_delta_x':con,'destructive_free_frequency_bound_Hz':v/(2*D)},'delta=sqrt(D²+x²)-x, x=(D²-delta²)/(2delta). Finite x has0<delta<=D; threshold f<v/(2D) for including B.')
u=v*8/(2*1700+8)
add(62,{'v':v,'bat_emission_Hz':1700,'beats_Hz':8},{'bat_u_m_s':u,'reflection_Hz':1708},'Wall stationary, bat moving source+listener: fr/f=(v+u)/(v-u).')
vs=1482;u=4.95;f=18000;fr=f*(vs+u)/(vs-u)
add(63,{'water_v':vs,'sonar_f_Hz':f,'whale_u':u},{'lambda_m':vs/f,'reflection_Hz':fr,'frequency_difference_Hz':fr-f},'Two stages with moving reflector; ship stationary in water.')
delay=3.;r=v*delay;level=80;I=1e-12*10**(level/10);P=4*pi*r*r*I;dur=2
add(64,{'chosen_delay_s':delay,'chosen_level_dB':level,'chosen_duration_s':dur,'estimate_status':'explicit illustrative assumptions, not measured data'},{'r_m':r,'I_W_m2':I,'P_W':P,'E_J':P*dur},'I=I0*10^(beta/10); P=4pi r²I for explicitly stated uniform spreading; E=P duration.')
level=90;I=1e-12*10**(level/10);P=4*pi*18**2*I;dur=.50;travel=2.50;uball=18/travel;K=.7*6.4*uball**2
add(65,{'alley_L_m':18,'ball_mass_kg':6.4,'chosen_level_dB':level,'chosen_sound_duration_s':dur,'chosen_ball_travel_s':travel,'ball_model':'uniform solid sphere rolling without slipping','spreading_model':'isotropic source, reflections neglected'},{'I_W_m2':I,'P_W':P,'sound_E_J':P*dur,'ball_u_m_s':uball,'ball_K_J':K,'sound_fraction':P*dur/K},'K=1/2mv²+1/2(2/5mr²)(v/r)²=7/10mv². All estimates explicit.')
u=1500*72/(2*2e6+72)
add(66,{'v_tissue':1500,'f_Hz':2e6,'beats_Hz':72},{'heart_wall_u_m_s':u},'Stationary transducer and approaching reflector: deltaf=2f*u/(v-u), solve exactly.')
fe=80.7e3;fr=83.5e3;ub=3.9;Q=fr*(v-ub);S=fe*(v+ub);ui=v*(Q-S)/(Q+S)
add(67,{'v':v,'bat_f_Hz':fe,'reflection_Hz':fr,'bat_u':ub},{'insect_u_m_s':ui,'Q':Q,'S':S},'fr/fe=[(v+ui)/(v-ub)]*[(v+ub)/(v-ui)]; isolate ui using Q and S.')
check('67 composed Doppler',fe*(v+ui)/(v-ub)*(v+ub)/(v-ui),fr)
add(68,{'symbols':['fsiren','platform_Ap','platform_fp','v_sound'],'condition':'2pi*fp*Ap<v'}, {'u_platform_max':'2*pi*fp*Ap','fmax':'fsiren*v/(v-2*pi*fp*Ap)','fmin':'fsiren*v/(v+2*pi*fp*Ap)','locations':'equilibrium crossing upward for max; downward for min'},'Source max/min radial speeds occur at equilibrium, not turning points.')
u=2*pi*.75*(75/60);f=v/.313;beat=f*v/(v-u)-f*v/(v+u)
add(69,{'diameter_m':1.5,'rpm':75,'emitted_lambda_m':.313,'v':v,'observer_assumption':'far compared with turntable radius'}, {'rim_u_m_s':u,'source_f_Hz':f,'max_beats_Hz':beat},'Maximum opposing radial speeds approximately +/-u in far field; beat from separate Doppler source frequencies.')
Ts=[-20,0,20,40,60,80];vs=[324,337,349,361,372,383];Ys=[a*a for a in vs];meanT=sum(Ts)/6;meanY=sum(Ys)/6
s=sum((a-meanT)*(b-meanY) for a,b in zip(Ts,Ys))/sum((a-meanT)**2 for a in Ts);inter=meanY-s*meanT;M=1.4*R/s
ssr=sum((b-(s*a+inter))**2 for a,b in zip(Ts,Ys));sst=sum((b-meanY)**2 for b in Ys)
add(70,{'T_C':Ts,'v_m_s':vs,'gamma':1.40,'R':R},{'v2':Ys,'slope_m2_s2_K':s,'intercept_at0C_m2_s2':inter,'M_g_mol':M*1000,'R2':1-ssr/sst,'suggested_gas':'nitrogen, consistent with about28 g/mol'},'Plot v² against Celsius or kelvin, slope gamma R/M; free-intercept unweighted fit.')
v71=500*2*(.555-.180);gam=Mair*v71*v71/(R*(77+273.15));end=v71/(4*500)-.180
add(71,{'T_C':77,'pressure_atm':1,'f_Hz':500,'resonance_lengths_m':[.180,.555,.930],'Mair':Mair}, {'lambda_m':.750,'v_m_s':v71,'gamma':gam,'end_correction_m':end},'Successive stopped-pipe resonances differ lambda/2. Effective first quarter-wave length lambda/4 exceeds physical length.')
fs=4.568e14;fr=4.586e14;c=3e8;ratio=fr/fs;beta=(ratio*ratio-1)/(ratio*ratio+1);u=beta*c;ulow=c*(ratio-1);yr=365.25*86400;refyear=2026;age=refyear-1054;diam=2*u*age*yr;ly=c*yr;theta=(5/60)*pi/180;distly=(diam/ly)/theta;explosion_astronomical_year=1054-distly
add(72,{'c':c,'rest_f_Hz':fs,'approaching_f_Hz':fr,'observed_supernova_year':1054,'angular_diameter_arcmin':5,'explicit_reference_year':refyear,'one_year_s':yr},{'approach_u_exact_m_s':u,'approach_u_first_order_m_s':ulow,'age_since_received_flash_years':age,'diameter_m':diam,'diameter_ly':diam/ly,'distance_ly':distly,'explosion_astronomical_year':explosion_astronomical_year,'approx_explosion_BCE':1-explosion_astronomical_year},'Relativistic formula uses recession velocity sign; approaching beta=(r²-1)/(r²+1). Estimate diameter with constant expansion and common distance light travel time.')
freq=v/(2*.39);torque=(8/2+4)*g*1.56/sqrt(2);h=(torque/(4*.00140*freq**2))**(1/3);F=torque/h
add(73,{'pole_L':1.56,'pole_mass':8,'tube_L':.39,'tube_mass':4,'angle_vertical_deg':45,'wire_mu':.00140,'v':v},{'tube_f_Hz':freq,'torque_N_m':torque,'h_m':h,'wire_F_N':F,'wire_length_m':h,'wire_f_Hz':sqrt(F/.0014)/(2*h)},'Hollow tube open at both ends. Geometry45deg gives wire length h. Fh=torque; equality of wire and tube fundamentals gives h³=torque/(4mu f²).')
check('73 matched fundamentals',sqrt(F/.0014)/(2*h),freq)
D=15.;aisle=50.;lam=v/440;dmin=sqrt(D*D+aisle*aisle)-aisle;pos=lambda delta:(D*D-delta*delta)/(2*delta)
first=[(m,(m+.5)*lam,pos((m+.5)*lam)) for m in range(100) if dmin<=(m+.5)*lam<=D]
second=[(j,(j+.5)*lam/3,pos((j+.5)*lam/3)) for j in range(200) if dmin<=(j+.5)*lam/3<=D]
additional=[r for r in second if not any(isclose(r[2],q[2],abs_tol=1e-8) for q in first)]
add(74,{'D_m':D,'aisle_L_m':aisle,'tone1_Hz':440,'v':v,'second_tone':'distinct from440 Hz'}, {'lambda1_m':lam,'path_difference_range_m':[dmin,D],'tone1_minima_count':len(first),'tone1_minima_m_delta_x':first,'last_minimum_x_m':max(x[2] for x in first),'last_to_door_m':aisle-max(x[2] for x in first),'smallest_distinct_tone_Hz':1320,'tone2_minima_count':len(second),'additional_count':len(additional),'closest_additional_x_m':min(x[2] for x in additional),'additional_m_delta_x':additional},'Phase minima delta=(m+1/2)lambda. Common minima require smallest distinct odd frequency multiplier3. Coherent intensity min=(sqrtI1-sqrtI2)^2, not zero unless equal amplitudes.')
P0=40.;lam=.2;rho=1.20;bulk=rho*v*v;T=lam/v
add(75,{'pressure_amplitude_Pa':P0,'lambda_m':lam,'v':v,'rho_air':rho,'initial_displacement_at_x0':0},{'bulk_Pa':bulk,'period_s':T,'displacement_amplitude_m':P0*lam/(8*bulk),'max_particle_speed_m_s':P0/(rho*v),'max_particle_acceleration_m_s2':4*P0/(rho*lam)},'Triangular p(x,0), p(0)=40,p(.1)=-40,p(.2)=40. p=-B dy/dx, y=Y(x-vt), u=p/(rho v); acceleration piecewise, one-sided at corners.')
add(76,{'spring_mass_kg':.250,'spring_L_m':2.,'spring_k_N_m':1.50},{'v_m_s':2*sqrt(1.50/.250)},'Segment dx has spring constant kprime*L/dx; force derivative kprime*L*yxx*dx; density m/L gives v²=kprime*L²/m.')
add(77,{'depth_m':.10,'tissue_v':1540},{'round_trip_s':.20/1540,'maximum_pulses_per_s':1540/.20,'choice':'b'},'Wait for round trip, not one-way distance.')
add(78,{'path_tissue_m':.10,'frequency_MHz':1.,'attenuation_dB_per_m_MHz':-100},{'level_change_dB':-10,'intensity_ratio':10**(-10/10),'choice':'d'},'Delta beta=negative attenuation coefficient*path*frequency in MHz. Intensity factor10^(Delta beta/10). Single pass specified.')
true=.04+.02+.01;measured=.04+.02/2+.01
add(79,{'soft1_m':.04,'bone_m':.02,'soft2_m':.01,'bone_speed_factor':2,'assumed_v':1540},{'true_distance_m':true,'measured_distance_m':measured,'actual_farther_m':true-measured,'choice':'a'},'Round-trip time cancels common factor2; bone traverses in half the assumed time, causing1cm underestimate.')
add(80,{'f_Hz':1e6,'tissue_v':1540},{'lambda_m':1540/1e6,'pressure_antinode_separation_m':1540/1e6/2,'choice':'b'},'Adjacent pressure antinodes are lambda/2, not lambda/4.0.770mm rounds to listed0.75mm.')
add(81,{'tissue_attenuation_dB_m_MHz':-100,'bone_attenuation_dB_m_MHz':-500},{'choice':'d','reason':'smaller frequency reduces magnitude of negative dB attenuation for same bone path'},'Use the passage model only; no clinical extrapolation or treatment advice.')
assert len(rows)==40
assert [r['exercise'] for r in rows]==[f'16.{n}' for n in range(42,82)]
check('74 original minima count',len(first),16)
check('74 additional minima count',len(additional),34)
check('77 correct pulses',1540/.2,7700)
check('78 attenuation ratio',10**(-10/10),.1)
result={'exercises':rows,'count':len(rows),'assertions':assertions,'all_pass':all(a['pass'] for a in assertions)}
assert result['all_pass']
print(json.dumps({'status':'passed',**result},ensure_ascii=False,indent=2))
