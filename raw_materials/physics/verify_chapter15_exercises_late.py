from pathlib import Path
import math,json,hashlib,statistics
B=Path(__file__).resolve().parent;P=math.pi;g=9.8;rows={}
def add(n,**kw):rows[f'15.{n}']=kw
def fit(x,y):
 xm=statistics.mean(x);ym=statistics.mean(y);s=sum((a-xm)*(b-ym) for a,b in zip(x,y))/sum((a-xm)**2 for a in x);return s,ym-s*xm
add(41,length_m=3*.08,node_distance_fourth_m=3*.08/4)
L=.75;mass=.00875;f3=344/.765;v=2*L*f3/3;add(42,f_third_Hz=f3,speed_ms=v,tension_N=mass/L*v*v,f_fund_Hz=f3/3)
add(43,x_bridge_m=.6*440/587,length_required_G4_m=.6*440/392)
add(44,omega='2*pi*f',relative_standing_amplitudes=[0,2,math.sqrt(2)],relative_vmax_to_Aomega=[0,2,math.sqrt(2)],relative_amax_to_Aomega2=[0,2,math.sqrt(2)],half_period_non_nodes='1/(2*f)',node_time='not defined: no distinct extreme displacements')
omega=8.5e4/3;A=3/omega;add(45,omega_rads=omega,A_m=A,wave_speed_ms=.4*omega/(2*P))
A=.0075;k=40*P;omega=250*P;v=omega/k;mu=.05
add(46,A_m=A,k_radm=k,omega_rads=omega,period_s=2*P/omega,f_Hz=omega/(2*P),wavelength_m=2*P/k,v_ms=v,tension_N=mu*v*v,power_W=.5*mu*omega**2*A**2*v,phases_rad=[0,omega*.0005,omega*.001],left_shifts_m=[0,-v*.0005,-v*.001])
A=.0025;v=36;lam=1.8;k=2*P/lam;omega=v*k;x=1.35;t=.0625;phase=k*x-omega*t
add(47,f_Hz=v/lam,omega_rads=omega,k_radm=k,phase_at135_rad=k*x,vmax_ms=A*omega,y_f_m=A*math.cos(phase),vy_f_ms=A*omega*math.sin(phase))
mu=.290/(g*1.25);TA=1750*2/3;TB=1750/3;ta=1.25*math.sqrt(mu/TA);tb=1.25*math.sqrt(mu/TB)
add(48,tension_A_N=TA,tension_B_N=TB,mu_kgm=mu,time_A_s=ta,time_B_s=tb,delay_s=tb-ta,first='A')
add(49,wire_mass_kg=g/(4*2*20.4),tension_slope_Nkg=g)
add(50,threshold='g*mu*lambda^2/(4*pi^2*F)',normal_force='m*(g-omega^2*y)',condition='A>=g/omega^2; just zero at crest at equality')
mu=14.5e-9/.02;v=math.sqrt(.4*g/mu);t=.0267;Lapprox=v*t;Lexact=Lapprox+g*t*t/4
add(51,spare_mass_kg=14.5e-9,mu_kgm=mu,speed_bottom_ms=v,length_approx_m=Lapprox,wire_mass_kg=mu*Lapprox,wire_weight_to_load_ratio=mu*Lapprox/.4,exact_gravity_length_m=Lexact,relative_length_correction_percent=100*(Lexact/Lapprox-1))
L=.35;m=.008;f1=262;f2=466;v=2*L*f1;T=m/L*v*v;mu=m/L;x=L*(1-f1/277)
add(52,tension_N=T,string2_mass_kg=m*(f1/f2)**2,fret_from_upper_m=x,shortened_length_m=L-x,string2_after_fret_Hz=f2*277/f1)
T=235/(2*math.tan(math.radians(57)));mu=.732/5;v=math.sqrt(T/mu);f=6*v/(2*5)
add(53,tension_N=T,wire_speed_ms=v,sound_frequency_Hz=f,sound_wavelength_m=344/f)
gplanet=g*(.039/.0685)**2;add(54,g_planet_ms2=gplanet,mass_planet_kg=gplanet*(7.2e7)**2/6.67e-11)
add(55,fund_Hz=630-525,length_m=384/(2*(630-525)),harmonic_numbers=[5,6])
add(56,v_ms=2*.8/.00730,relation='n=(2*L/v)*f-1 for n interior nodes')
Lbar=1.8;TCu=638*.9/1.4;TAl=638-TCu;S=P*(.280e-3)**2
add(57,tension_Al_N=TAl,tension_Cu_N=TCu,area_m2=S,fund_Al_Hz=math.sqrt(TAl/(2700*S))/(2*.6),fund_Cu_Hz=math.sqrt(TCu/(8900*S))/(2*.6),density_Al=2700,density_Cu=8900)
lam=4*.15;f=260/lam;omega=2*P*f;add(58,lambda_m=lam,f_Hz=f,vmax_antinode_ms=.0018*omega,vmax_at075_ms=.0018*math.sin(2*P*.075/lam)*omega)
L=3*.0628;T=2*.00840;f=1/T;v=2*.0628*f;mu=5/v**2;add(59,length_m=L,period_s=T,v_ms=v,mass_kg=mu*L)
S=P*(1.024e-3)**2/4;Y=11e10;L=1.2;dL=400*L/(Y*S)
add(60,area_m2=S,lambda3_m=2*L/3,delta_length_m=dL,delta_lambda3_m=2*dL/3,delta_lambda_exact_if120_loaded_m=2/3*(400*L/(Y*S+100)),Y_copper_Pa=Y)
mu=.006/8;v=30;lam=.2;omega=2*P*v/lam;A=math.sqrt(2*50/(mu*omega**2*v));add(61,mu_kgm=mu,omega_rads=omega,A_m=A,kA=2*P*A/lam,power_double_speed_W=50*8)
dt=60/5000;T=8*dt;f=1/T;lam=.5;v=lam*f;mu=1/v**2;add(62,flash_interval_s=dt,T_s=T,f_Hz=f,lambda_m=lam,harmonic=2,v_ms=v,speed_P_pos1_ms=0,speed_P_pos3_ms=.015*2*P*f,mass_kg=mu*.5)
N=101;mass=N*.001;L=1.5;mu=mass/L;T=28.8*(1.5-1.005);v=math.sqrt(T/mu);f=4*v/(2*L);omega=2*P*f;A13=7.54/omega;nodebeads=[1,26,51,76,101];speed30=7.54*abs(math.sin(4*P*29/100)/math.sin(4*P*12/100))
add(63,bead_count=N,total_mass_kg=mass,mu_kgm=mu,tension_N=T,v_ms=v,f_Hz=f,motionless_beads=nodebeads,A13_m=A13,position_n='(n-1)*1.50/100 m for 1<=n<=101',speed30_ms=speed30,antinode_amplitude_m=A13/abs(math.sin(4*P*12/100)))
L=2.2;mu=.003/L;v=math.sqrt(330/mu);omega=P*v/L;add(64,v_ms=v,omega_rads=omega,A_antinode_m=9/omega,amax_ms2=9*omega)
L=2.5;A=.035;omega=28/A;f=omega/(2*P);v=L*f;mu=90/v**2;add(65,omega_rads=omega,v_ms=v,mass_kg=mu*L,amax_ms2=omega*28)
omega=8.4e3/3.8;A=3.8/omega;v=omega*.386/P;add(66,omega_rads=omega,A_standing_m=A,v_ms=v)
S=P*(.00114)**2/4;mu=7800*S;v=311*.55;add(67,mu_kgm=mu,v_ms=v,tension_N=mu*v*v,rho_steel_kgm3=7800)
lam=192/240;k=2*P/lam;omega=2*P*240;amps=[.004*abs(math.sin(k*x)) for x in [.4,.2,.1]];amps[0]=0
add(68,wavelength_m=lam,string_length_m=3*lam/2,amplitudes_m=amps,half_period_s=1/(2*240),vmax_ms=[a*omega for a in amps],amax_ms2=[a*omega**2 for a in amps],node_has_no_extreme_to_extreme_trip=True)
add(69,rho_liquid_kgm3=3200*(1-(28/42)**2))
mu=.0001/.1;T=1;v=math.sqrt(T/mu);add(70,assumed_tension_N=T,mu_kgm=mu,v_ms=v,f_estimate_Hz=v/(2*.1),estimate_not_measurement=True)
mu=.0144/.6;T=mu*(2*.6*65.4)**2;add(71,tension_N=T,increase_percent=100*((73.4/65.4)**2-1))
S=900/7e8;r=math.sqrt(S/P);L=.004/(7800*S);v=math.sqrt(900/(7800*S));add(72,area_min_m2=S,radius_min_m=r,length_max_m=L,v_ms=v,f_for_part_a_string_Hz=v/(2*L),global_fund_frequency_max_if_geometry_free='unbounded; fixing part(a) geometry is necessary')
mu=[.0260*.1,.0260*.1,.0374*.1,.0374*.1,.0482*.1];M=[.559,.249,.365,.207,.262];d=[.481,.319,.320,.242,.238];ys=[u*x*x for u,x in zip(mu,d)];s,c=fit(M,ys);f=math.sqrt(g/(4*s));need=4*mu[0]*f*f*.24**2/g
add(73,y_kgm=ys,slope_m=s,intercept_kgm=c,f_Hz=f,mass_for_A24cm_kg=need,fixed_nodes='d=L/n for positive integer n')
L=25.5*.0254;freqs=[82.4,196,329.6];mus=[78/(2*L*f)**2 for f in freqs];add(74,scale_length_m=L,mu_kgm=mus,mu_gcm=[u*10 for u in mus],replacement_tension_N=78*(196/82.4)**2)
s=.00031;mu=.0035;A=.004;v=s/(2*P**2*mu*A*A);omega=math.sqrt(2*10/(mu*v*A*A));add(75,graph_slope_WperHz2_approx=s,v_ms_approx=v,omega_for10W_rads_approx=omega,graph_reading_is_approximate=True)
W=1;L=4;F=81;M=4;A=.1;f=1;v=math.sqrt(F*L/M);omega=2*P*f;k=omega/v;Pavg=.5*F*k*omega*A*A
add(76,v_ms=v,k_radm=k,Pavg_W=Pavg,E_per_second_J=Pavg,power_instantaneous='F*k*omega*A^2*cos(k*x-omega*t)^2',scope='right-going component, reflected wave needs separate treatment')
S=P*(.02)**2/4;T0=(120-1000*.08)*g;a=(1.1-1000*S)*g;L=100;time=2*math.sqrt(1.1)/a*(math.sqrt(T0+a*L)-math.sqrt(T0))
add(77,T0_N=T0,area_m2=S,tension_gradient_Nm=a,Ttop_N=T0+a*L,v_bottom_ms=math.sqrt(T0/1.1),v_top_ms=math.sqrt((T0+a*L)/1.1),signal_time_s=time)
add(78,wavelength_cm=375/125,option='d')
add(79,option='b',wave='A*sin(2*pi*f*(t-z/v))',propagation='positive z; products in c/d are standing waves')
add(80,option='c',wavelength_cm_approx=3,wave_speed_proportional_frequency=True)
assert len(rows)==40 and list(rows)==[f'15.{n}' for n in range(41,81)]
assert rows['15.51']['length_approx_m']>60
assert abs(rows['15.47']['y_f_m']+.0025)<1e-12 and abs(rows['15.47']['vy_f_ms'])<1e-12
assert abs(rows['15.77']['signal_time_s']-(sum(100/100000/math.sqrt((T0+a*(i+.5)*100/100000)/1.1) for i in range(100000))))<1e-9
print(json.dumps({'status':'passed','units':rows,'unitCount':len(rows)},ensure_ascii=False,indent=2))
