"""Recompute source-based results and physical invariants for exercises 14.1–14.48.
This is a calculation/structure audit, not independent source or viewport review.
Run from any cwd with Python -I -Xutf8.
"""
from pathlib import Path
import math,json,re,hashlib
R=Path(__file__).resolve().parent
S={'14.1': {'f_a_Hz': 466, 'T_b_us': 50.0, 'omega_c_rad_s': [2700000000000000.0, 4700000000000000.0], 'f_d_MHz': 5.0}, '14.2': {'A_m': 0.12, 'opposite_extreme_s': 0.8}, '14.3': {'cycles': 440, 'seconds': 0.5}, '14.4': {'graph': 'E14.4', 'A_cm': 10, 'min_s': 5, 'max_s': 13}, '14.5': {'f_Hz': 4, 'A_cm': 1.8, 'from_m': 0, 'to_cm': -1.8}, '14.6': {'estimated_L_m': 2, 'assumption': 'small-angle; push once per full cycle'}, '14.7': {'m_kg': 2.4, 'graph': 'E14.7', 'A_cm': 3, 'max_s': [0.2, 1.0]}, '14.8': {'m_kg': 0.2, 'successive_equilibrium_s': 2.6}, '14.9': {'k_N_m': 120, 'f_Hz': 6}, '14.10': {'m_kg': 0.75, 'f_Hz': 1.75, 'delta_m_kg': 0.22}, '14.11': {'T_s': 0.9, 'A_m': 0.32, 'initial_rest': True}, '14.12': {'x_m': 0.28, 'a_m_s2': -5.3}, '14.13': {'m_kg': 2, 'k_N_m': 300, 'x0_m': 0, 'v0_m_s': -12}, '14.14': {'m_kg': 2, 'k_N_m': 300, 'x0_m': 0.2, 'v0_m_s': -4}, '14.15': {'x0_over_A': 1, 'v0': 0}, '14.16': {'A1_m': 0.09, 'A2_m': 0.18, 'opposite_extreme_s': 2.7}, '14.17': {'chair_kg': 42.5, 'T_empty_s': 1.3, 'T_loaded_s': 2.54}, '14.18': {'m_kg': 0.4, 'a_m_s2': -1.8, 'x_m': 0.3}, '14.19': {'k_N_cm': 2.5, 'graph': 'E14.19', 'T_s': 0.2, 'amax_m_s2': 12}, '14.20': {'m_kg': 0.5, 'vmax_cm_s': 3.6, 'omega_rad_s': 4.71, 'phase_rad': -1.5707963267948966}, '14.21': {'m_kg': 1.5, 'A_cm': 7.4, 'omega_rad_s': 4.16, 'phase_rad': -2.42, 't_s': 1}, '14.22': {'sliver_length_nm': 30, 'mS_g': 2.1e-16, 'fS_Hz': 2000000000000000.0, 'fSV_Hz': 287000000000000.0}, '14.23': {'v_equals_minus_jerk_times_s2': 0.04}, '14.24': {'graph': 'E14.4', 'A_m': 0.1, 'T_s': 16}, '14.25': {'A_m': 0.165, 'vmax_m_s': 3.9}, '14.26': {'A_m': 0.25, 'T_s': 3.2, 'x_m': 0.16}, '14.27': {'m_kg': 0.15, 'k_N_m': 300, 'x_m': 0.012, 'speed_m_s': 0.4}, '14.28': {'symbolic': 'E=.5*k*A^2, U=.5*k*x^2'}, '14.29': {'m_kg': 0.5, 'k_N_m': 450, 'A_m': 0.04, 'x_m': -0.015}, '14.30': {'symbolic': 'SHM average speed full cycle'}, '14.31': {'speed_fraction': 0.5}, '14.32': {'m_kg': 0.3, 'x_m': 0.24, 'a_m_s2': -12, 'v_m_s': 4}, '14.33': {'x_m': 0.6, 'v_m_s': 2.2, 'a_m_s2': -8.4}, '14.34': {'U_equals_K': True}, '14.35': {'m_kg': 2, 'k_N_m': 315, 'x_m': 0.2, 'v_m_s': -4}, '14.36': {'m_kg': 65, 'stretch_m': 0.18, 'A_cm': 5}, '14.37': {'m_g': 175, 'k_N_m': 155, 'speed_m_s': 0.815, 'x_cm': 3}, '14.38': {'M_kg': 6.5, 'diameter_cm': 24, 'force_N': 4.23, 'angle_deg': 3.34}, '14.39': {'m_kg': 4, 'A_m': 0.05, 'top_unstretched': True}, '14.40': {'m_kg': 0.002, 'R_cm': 2.2, 'T_s': 1}, '14.41': {'ticks_per_s': 4, 'tick_fraction_period': 0.5, 'R_cm': 0.55, 'm_g': 0.9}, '14.42': {'kappa_N_m_rad': 0.45, 'cycles': 165, 'seconds': 265}, '14.43': {'L_m': 0.24, 'theta_deg': [3.5, 1.75]}, '14.44': {'relative_error': 0.02, 'retained_correction': 'sin(theta/2)^2/4'}, '14.45': {'mass_kg': 2.35, 'L_m': 1.5}, '14.46': {'Tearth_s': 1.6, 'gMars_m_s2': 3.71}, '14.47': {'L_cm': 50, 'cycles': 100, 'seconds': 136}, '14.48': {'graph': 'E14.48', 'A_deg': 6, 'maxima_s': [0, 1.6]}}
pi=math.pi;g=9.8;RESULTS={};TESTS=[]
def p(n):return S[f'14.{n}']
def add(n,**kw):RESULTS[f'14.{n}']={'source_inputs':p(n),'computed':kw}
def close(n,name,a,b,rtol=1e-10,atol=1e-12):
 ok=math.isclose(a,b,rel_tol=rtol,abs_tol=atol)
 TESTS.append({'exercise':f'14.{n}','test':name,'actual':a,'expected':b,'passed':ok})
 if not ok:raise AssertionError((n,name,a,b))
def condition(n,name,c):
 TESTS.append({'exercise':f'14.{n}','test':name,'passed':bool(c)})
 if not c:raise AssertionError((n,name))
s=p(1);fa=s['f_a_Hz'];tb=s['T_b_us']*1e-6;wlo,whi=s['omega_c_rad_s'];fd=s['f_d_MHz']*1e6
add(1,Ta=1/fa,wa=2*pi*fa,fb=1/tb,wb=2*pi/tb,Tc_min=2*pi/whi,Tc_max=2*pi/wlo,fc_min=wlo/(2*pi),fc_max=whi/(2*pi),Td=1/fd,wd=2*pi*fd)
close(1,'frequency-period inverse',RESULTS['14.1']['computed']['fb']*tb,1)
close(1,'angular phase per cycle',RESULTS['14.1']['computed']['wd']/fd,2*pi)
s=p(2);T=2*s['opposite_extreme_s'];add(2,A=s['A_m'],T=T,f=1/T);close(2,'opposite extreme phase',math.cos(2*pi/T*s['opposite_extreme_s']),-1)
s=p(3);f=s['cycles']/s['seconds'];add(3,f=f,omega=2*pi*f,T=1/f);close(3,'cycles reproduce duration',s['cycles']/f,s['seconds'])
s=p(4);T=2*(s['max_s']-s['min_s']);add(4,A=s['A_cm']/100,T=T,f=1/T,omega=2*pi/T);close(4,'half-cycle extrema gap',T/2,8)
s=p(5);T=1/s['f_Hz'];add(5,T=T,direct_s=T/4,initial_positive_s=3*T/4);close(5,'negative-going zero to negative extreme',-math.sin(2*pi/T*(T/4)),-1)
s=p(6);T=2*pi*math.sqrt(s['estimated_L_m']/g);add(6,T=T);close(6,'small-angle pendulum inverse',g*(T/(2*pi))**2,s['estimated_L_m'])
s=p(7);T=s['max_s'][1]-s['max_s'][0];w=2*pi/T;k=s['m_kg']*w*w;add(7,T=T,f=1/T,omega=w,A=s['A_cm']/100,k=k);close(7,'Newton restoring relation',k/s['m_kg'],w*w)
s=p(8);T=2*s['successive_equilibrium_s'];k=s['m_kg']*(2*pi/T)**2;add(8,T=T,k=k);close(8,'next equilibrium has reversed velocity',math.cos(2*pi/T*s['successive_equilibrium_s']),-1)
s=p(9);w=2*pi*s['f_Hz'];m=s['k_N_m']/w**2;add(9,T=1/s['f_Hz'],omega=w,m=m);close(9,'recovered stiffness',m*w*w,s['k_N_m'])
s=p(10);m=s['m_kg'];dm=s['delta_m_kg'];f=s['f_Hz'];fa=f*math.sqrt(m/(m+dm));fr=f*math.sqrt(m/(m-dm));add(10,f_added=fa,f_removed=fr);close(10,'same stiffness after adding mass',fa**2*(m+dm),f*f*m);condition(10,'frequency ordering',fa<f<fr)
s=p(11);T=s['T_s'];add(11,ta=T/6,tb=T/12);close(11,'half-amplitude at first endpoint',math.cos(2*pi/T*(T/6)),.5);close(11,'zero after both intervals',math.cos(2*pi/T*(T/6+T/12)),0)
s=p(12);w=math.sqrt(-s['a_m_s2']/s['x_m']);add(12,omega=w,f=w/(2*pi));close(12,'measured acceleration',-w*w*s['x_m'],s['a_m_s2'])
for n in [13,14]:
 s=p(n);w=math.sqrt(s['k_N_m']/s['m_kg']);x=s['x0_m'];v=s['v0_m_s'];A=math.hypot(x,v/w);phi=math.atan2(-v/w,x)
 add(n,omega=w,A=A,phi=phi,x_reconstructed=A*math.cos(phi),v_reconstructed=-w*A*math.sin(phi))
 close(n,'initial position and correct quadrant',A*math.cos(phi),x);close(n,'initial velocity and correct quadrant',-w*A*math.sin(phi),v)
add(15,t_xhalf_over_T=1/6,t_vhalf_over_T=1/12,v_at_xhalf_over_vmax=math.sqrt(3)/2);close(15,'first half displacement',math.cos(pi/3),.5);close(15,'first half speed',math.sin(pi/6),.5)
s=p(16);T=2*s['opposite_extreme_s'];add(16,T=T,ta=T/2,tb=T/6);close(16,'new starting position',s['A2_m']*math.cos(pi/3),s['A1_m']);close(16,'new ending position',s['A2_m']*math.cos(2*pi/3),-s['A1_m'])
s=p(17);M=s['chair_kg'];T0=s['T_empty_s'];T1=s['T_loaded_s'];m=M*((T1/T0)**2-1);add(17,astronaut_kg=m);close(17,'loaded period reconstruction',T0*math.sqrt((M+m)/M),T1)
s=p(18);w=math.sqrt(-s['a_m_s2']/s['x_m']);add(18,T=2*pi/w);close(18,'measured acceleration',-w*w*s['x_m'],s['a_m_s2'])
s=p(19);k=s['k_N_cm']*100;w=2*pi/s['T_s'];m=k/w**2;A=s['amax_m_s2']/w**2;add(19,k_N_m=k,omega=w,m=m,A=A,Fmax=k*A);close(19,'force via spring and Newton',k*A,m*s['amax_m_s2'])
s=p(20);w=s['omega_rad_s'];V=s['vmax_cm_s']/100;m=s['m_kg'];add(20,T=2*pi/w,A=V/w,amax=w*V,k=m*w*w);close(20,'speed amplitude reconstructed',(V/w)*w,V)
s=p(21);w=s['omega_rad_s'];A=s['A_cm']/100;m=s['m_kg'];t=s['t_s'];phi=s['phase_rad'];x=A*math.cos(w*t+phi);v=-w*A*math.sin(w*t+phi);a=-w*w*x
add(21,T=2*pi/w,k=m*w*w,vmax=w*A,Fmax=m*w*w*A,x1=x,v1=v,speed1=abs(v),a1=a,F1=m*a)
h=1e-5;v_fd=(A*math.cos(w*(t+h)+phi)-A*math.cos(w*(t-h)+phi))/(2*h)
close(21,'velocity from centered finite difference',v_fd,v,rtol=1e-8);close(21,'force sign and magnitude',m*a,-m*w*w*x)
s=p(22);ms=s['mS_g'];fs=s['fS_Hz'];fv=s['fSV_Hz'];mv=ms*((fs/fv)**2-1);add(22,mass_g=mv,mass_fg=mv/1e-15,reconstructed_ratio=math.sqrt(ms/(ms+mv)),ratio=fv/fs);close(22,'frequency ratio reconstructed',math.sqrt(ms/(ms+mv)),fv/fs)
s=p(23);q=s['v_equals_minus_jerk_times_s2'];w=math.sqrt(1/q);add(23,omega=w,T=2*pi/w);z=.37;v=-w*math.sin(w*z);j=w**3*math.sin(w*z);close(23,'velocity-jerk proportionality',v,-q*j)
s=p(24);w=2*pi/s['T_s'];A=s['A_m'];add(24,vmax=w*A,amax=w*w*A);close(24,'acceleration-speed amplitude ratio',(w*w*A)/(w*A),w)
s=p(25);a=s['vmax_m_s']**2/s['A_m'];add(25,amax=a);close(25,'recover maximum speed',math.sqrt(a*s['A_m']),s['vmax_m_s'])
s=p(26);w=2*pi/s['T_s'];x=s['x_m'];A=s['A_m'];v=w*math.sqrt(A*A-x*x);add(26,speed=v,a=-w*w*x);close(26,'normalized energy conservation',v*v+w*w*x*x,w*w*A*A)
s=p(27);m=s['m_kg'];k=s['k_N_m'];E=(m*s['speed_m_s']**2+k*s['x_m']**2)/2;A=math.sqrt(2*E/k);V=math.sqrt(2*E/m);add(27,E=E,A=A,vmax=V);close(27,'energy at turning point',k*A*A/2,E);close(27,'energy at equilibrium',m*V*V/2,E)
add(28,x_over_A=1/math.sqrt(2),speed_over_omega_A=1/math.sqrt(2),occurrences=4,delta_t_over_T=.25,Kfraction_at_halfA=.75,Ufraction_at_halfA=.25);close(28,'equal energy fractions',math.cos(pi/4)**2,.5);close(28,'fractions sum',.75+.25,1)
s=p(29);m=s['m_kg'];k=s['k_N_m'];A=s['A_m'];x=s['x_m'];w=math.sqrt(k/m);v=w*math.sqrt(A*A-x*x);a=-w*w*x;E=k*A*A/2;add(29,omega=w,vmax=w*A,speed=v,amax=w*w*A,a=a,E=E);close(29,'energy in measured state',(m*v*v+k*x*x)/2,E);condition(29,'force points toward equilibrium',a*x<0)
add(30,average_over_vmax=2/pi,time_above_half_fraction=2/3,time_below_half_fraction=1/3)
N=60000;phases=[2*pi*(i+.5)/N for i in range(N)];avg=sum(abs(math.sin(q)) for q in phases)/N;above=sum(abs(math.sin(q))>.5 for q in phases)/N
close(30,'numerical full-cycle speed integral',avg,2/pi,rtol=1e-8);close(30,'sampled time above half maximum',above,2/3,rtol=1e-4)
s=p(31);u=math.sqrt(1-s['speed_fraction']**2);add(31,distance_over_A=u);close(31,'energy fractions',u*u+s['speed_fraction']**2,1);condition(31,'distance exceeds half amplitude',u>.5)
s=p(32);m=s['m_kg'];x=s['x_m'];a=s['a_m_s2'];v=s['v_m_s'];w=math.sqrt(-a/x);A=math.hypot(x,v/w);add(32,k=m*w*w,omega=w,A=A,vmax=w*A,amax=w*w*A);close(32,'energy of measured state',w*w*A*A,w*w*x*x+v*v);close(32,'acceleration reconstructed',-w*w*x,a)
s=p(33);x=s['x_m'];v=s['v_m_s'];w=math.sqrt(-s['a_m_s2']/x);A=math.hypot(x,v/w);add(33,omega=w,A=A,farther=A-x);condition(33,'next turning point farther right',A>x and v>0);close(33,'energy at next stop',w*w*A*A,w*w*x*x+v*v)
u=1/math.sqrt(2);add(34,distance_over_A=u);close(34,'equal potential and kinetic fractions',u*u,1-u*u)
s=p(35);m=s['m_kg'];k=s['k_N_m'];x=s['x_m'];v=s['v_m_s'];A=math.sqrt(x*x+m*v*v/k);a=k*A/m;add(35,A=A,amax=a,Fmax=k*A);close(35,'energy in initial state',k*A*A,k*x*x+m*v*v);close(35,'maximum force from Newton',m*a,k*A)
s=p(36);m=s['m_kg'];d=s['stretch_m'];A=s['A_cm']/100;k=m*g/d;w=math.sqrt(k/m);add(36,k=k,T=2*pi/w,vmax=w*A);close(36,'static equilibrium stretch',k*d,m*g);close(36,'gravity cancels at new origin',m*g-k*d,0)
s=p(37);m=s['m_g']/1000;k=s['k_N_m'];x=s['x_cm']/100;v=s['speed_m_s'];w=math.sqrt(k/m);A=math.hypot(x,v/w);V=w*A;add(37,omega=w,A=A,vmax=V);close(37,'energy conservation',m*V*V,m*v*v+k*x*x)
s=p(38);M=s['M_kg'];r=s['diameter_cm']/200;theta=math.radians(s['angle_deg']);kap=s['force_N']*r/theta;I=M*r*r/2;w=math.sqrt(kap/I);add(38,R=r,theta=theta,I=I,kappa=kap,omega=w,f=w/(2*pi),T=2*pi/w);close(38,'holding torque',kap*theta,s['force_N']*r);close(38,'frequency reconstructs period',w*(2*pi/w),2*pi)
s=p(39);m=s['m_kg'];A=s['A_m'];k=m*g/A;Et=m*g*2*A;Eb=.5*k*(2*A)**2;Us=.5*k*A*A;Ug=m*g*A;K=Et-Us-Ug
add(39,k=k,top_Us=0,top_K=0,top_Ug=Et,top_E=Et,bottom_Us=Eb,bottom_K=0,bottom_Ug=0,equilibrium_Us=Us,equilibrium_K=K,equilibrium_Ug=Ug)
close(39,'static stretch equals amplitude',k*A,m*g);close(39,'energy at bottom',Eb,Et);close(39,'energy at equilibrium',Us+K+Ug,Et);close(39,'oscillation energy about equilibrium',K,k*A*A/2)
s=p(40);r=s['R_cm']/100;I=s['m_kg']*r*r/2;kap=I*(2*pi/s['T_s'])**2;add(40,I=I,kappa=kap);close(40,'reconstructed torsional period',2*pi*math.sqrt(I/kap),s['T_s'])
s=p(41);T=1/(s['ticks_per_s']*s['tick_fraction_period']);I=s['m_g']/1000*(s['R_cm']/100)**2;kap=I*(2*pi/T)**2;add(41,T=T,I=I,kappa=kap);close(41,'half-period tick interval',T*.5,1/s['ticks_per_s'])
s=p(42);T=s['seconds']/s['cycles'];I=s['kappa_N_m_rad']*(T/(2*pi))**2;add(42,T=T,I=I);close(42,'duration reconstructed',2*pi*math.sqrt(I/s['kappa_N_m_rad'])*s['cycles'],s['seconds'])
s=p(43);T=2*pi*math.sqrt(s['L_m']/g);add(43,T=T,ta=T/4,tb=T/4);close(43,'quarter-cycle reaches equilibrium',math.cos(2*pi/T*(T/4)),0)
s=p(44);e=s['relative_error'];th0=2*math.asin(math.sqrt(4*e));delta=e/(1-e);th=2*math.asin(math.sqrt(4*delta));add(44,theta_deg_normalized_T0=math.degrees(th0),theta_deg_normalized_T=math.degrees(th));d=math.sin(th/2)**2/4;close(44,'error relative to corrected period',d/(1+d),e);close(44,'error relative to approximation',math.sin(th0/2)**2/4,e)
s=p(45);f=math.sqrt(g/s['L_m'])/(2*pi);add(45,f=f,T=1/f);close(45,'length reconstructed from frequency',g/(2*pi*f)**2,s['L_m'])
s=p(46);TM=s['Tearth_s']*math.sqrt(g/s['gMars_m_s2']);add(46,TMars=TM);close(46,'same pendulum length on both planets',s['gMars_m_s2']*TM*TM,g*s['Tearth_s']**2)
s=p(47);T=s['seconds']/s['cycles'];gg=4*pi*pi*(s['L_cm']/100)/T**2;add(47,T=T,g=gg);close(47,'measured time reconstructed',2*pi*math.sqrt((s['L_cm']/100)/gg)*s['cycles'],s['seconds'])
s=p(48);T=s['maxima_s'][1]-s['maxima_s'][0];L=g*(T/(2*pi))**2;add(48,T=T,f=1/T,omega=2*pi/T,A_rad=math.radians(s['A_deg']),L=L,mass_identifiable=False);close(48,'pendulum length reproduces graph period',2*pi*math.sqrt(L/g),T)
for mass in [.1,1,100]:close(48,f'gravity torque divided by inertia at mass {mass}',(mass*g*L)/(mass*L**2),(2*pi/T)**2)
# Spot-check the displayed rounded answer set for every exercise. This does not parse every numeral in prose.
rounded={1:('Ta',.00215),2:('T',1.60),3:('omega',5530),4:('T',16),5:('direct_s',.0625),6:('T',2.8),7:('k',148),8:('k',.292),9:('m',.0844),10:('f_added',1.54),11:('ta',.150),12:('f',.692),13:('A',.980),14:('A',.383),15:('t_xhalf_over_T',1/6),16:('tb',.900),17:('astronaut_kg',120),18:('T',2.57),19:('m',.253),20:('A',.00764),21:('x1',-.0125),22:('mass_fg',9.99),23:('T',1.26),24:('vmax',.0393),25:('amax',92.2),26:('speed',.377),27:('E',.0336),28:('x_over_A',.7071),29:('E',.360),30:('average_over_vmax',.637),31:('distance_over_A',.866),32:('A',.614),33:('farther',.240),34:('distance_over_A',.707),35:('Fmax',119),36:('k',3540),37:('A',.0406),38:('kappa',8.71),39:('top_E',3.92),40:('kappa',1.91e-5),41:('kappa',4.3e-6),42:('I',.0294),43:('ta',.246),44:('theta_deg_normalized_T',33.2),45:('f',.407),46:('TMars',2.60),47:('g',10.7),48:('L',.635)}
for n,(field,expected) in rounded.items():close(n,'displayed principal rounded answer',RESULTS[f'14.{n}']['computed'][field],expected,rtol=.02,atol=1e-12)
print(json.dumps({'status':'passed','exerciseCount':len(RESULTS),'assertionCount':len(TESTS),'results':RESULTS,'checks':TESTS},ensure_ascii=False,indent=2))
