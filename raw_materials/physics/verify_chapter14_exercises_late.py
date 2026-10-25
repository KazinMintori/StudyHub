"""Independent numerical and model checks for 14.49–14.96. Writes only this QA directory."""
from pathlib import Path
import math, json, hashlib
import numpy as np

BASE = Path(__file__).resolve().parent
g, pi = 9.80, math.pi
R = {}
def put(n, **kw): R[f'14.{n}'] = kw
def close(a,b): assert math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-10), (a,b)

# General formulas are checked on explicit nondegenerate parameter choices.
theta,L,m = .6,1.2,.7
alpha=theta/2
v2=2*g*L*(math.cos(alpha)-math.cos(theta))
S=m*(g*math.cos(alpha)+v2/L)
close(S-m*g*math.cos(alpha),m*v2/L)
put(49,sample_theta_rad=theta,sample_v_half=math.sqrt(v2),sample_S_half=S,
       exact=True,radial_acceleration_at_release=0)
put(50,radius_m=g*2**2/(8*pi*pi))
put(51,TB_over_TA=math.sqrt(8/9))
Iw=1.8*g*.250*(.940/(2*pi))**2
put(52,I_kg_m2=Iw,Omega_exact=math.sqrt(2*1.8*g*.250*(1-math.cos(.4))/Iw),
       Omega_small_angle=.4*2*pi/.940,
       small_angle_relative_error_pct=100*(.4/math.sqrt(2*(1-math.cos(.4)))-1))
put(53,TB_over_TA=math.sqrt(1.1))
put(54,T_s=2*pi*math.sqrt(5*.050/(3*g)))
put(55,omega_d_over_omega=math.sqrt(3)/2)
put(56,b_kg_s=2*.0500/5*math.log(.300/.100))
put(57,f_Hz=math.sqrt(2.5/.3-(.9/(2*.3))**2)/(2*pi),bc_kg_s=2*math.sqrt(.3*2.5))
put(58,E0_J=.5*225*.07**2,E1_J=.5*225*.06**2,E4_J=.5*225*.03**2,
       loss_J=.5*225*(.06**2-.03**2),turning_times_s=[0,1,2,3,4],graph_reading=True)
put(59,Aa_over_A1=1/3,Ab_over_A1=2)
put(60,A_resonant_02=5,A_resonant_04=2.5,A_half_02=1/math.sqrt(.75**2+.1**2),
       A_half_04=1/math.sqrt(.75**2+.2**2),ratio02=math.sqrt(.75**2+.1**2)/.2,
       ratio04=math.sqrt(.75**2+.2**2)/.4)
put(61,v_ratio=2*math.sqrt(9*4),a_ratio=2*9*4)
put(62,t_s=.300/(2*pi)*math.acos(-.015/.0600))
put(63,x_m=-.600*math.sin(2*pi*.480/1.200))
kcar=250*g/.0400
ml=kcar*(1.92/(2*pi))**2
put(64,k_N_m=kcar,loaded_mass_kg=ml,empty_mass_kg=ml-250,T_empty_s=2*pi*math.sqrt((ml-250)/kcar))
put(65,k2_over_k1=16,v2_over_v1=2)
put(66,sample_Amax=.35*(2+1)*g/100)
put(67,k_N_m=8.62/.120**2)
put(68,T_s=2*pi*math.sqrt(4.50/150),mu_s=150*.088/(4.5*g))
w=math.sqrt(185/1.775);y=g/w**2
put(69,omega=w,y_detach_m=y,height_above_A_m=.15+y,t_s=math.acos(-y/.15)/w,
       v_m_s=w*math.sqrt(.15**2-y**2))
close(w*w*y,g)
put(70,v_after=1,omega=math.sqrt(170/20),f_Hz=math.sqrt(170/20)/(2*pi),
       A_m=math.sqrt(20/170),T_s=2*pi*math.sqrt(20/170),return_s=pi*math.sqrt(20/170))
put(71,extension_m=1/1.5,stretched_length_m=4/1.5,L0_m=3/1.5)
put(72,sample_M=2,sample_A=.01,sample_rho=1000,sample_h=.5,
       sample_equilibrium_depth=2/(1000*.01),sample_T=2*pi*math.sqrt(2/(1000*.01*g)))
# Four sides: each I_cm = (m/4)L²/12 + (m/4)(L/2)², so total mL²/3.
close(4*(1/4/12+1/4/4),1/3)
put(73,Icm_over_mL2=1/3,Ip_over_mL2=5/6,d_over_L=1/math.sqrt(2),
       frequency_coefficient=math.sqrt(3*math.sqrt(2)/5)/(2*pi))
A=math.sqrt(2*.2/10);x0=-math.sqrt(2*.140/10)
phi=2*pi-math.acos(x0/A)
put(74,E_J=.2,A_m=A,U_half_A_J=.5*10*(A/2)**2,x_equal_abs_m=A/math.sqrt(2),
       x0_m=x0,v0_m_s=math.sqrt(2*.06/.2),phi_rad=phi,phi_equivalent_rad=phi-2*pi,
       omega=math.sqrt(10/.2))
close(A*math.cos(phi),x0)
assert -A*math.sqrt(10/.2)*math.sin(phi)>0
T=2*pi*math.sqrt(7/450)
put(75,T_half_s=T,dT_dt=-T*.002/(2*7),T_min_s=2*pi*math.sqrt(2/450),
       half_time_s=5/.002,mass_change_timescale_s=7/.002)
mp=1.67262192369e-27;f=7e13;E=5e-20
km=mp*(2*pi*f)**2;Am=math.sqrt(2*E/km)
put(76,proton_mass_kg=mp,k_N_m=km,vmax_m_s=math.sqrt(2*E/mp),A_m=Am,A_over_bond=Am/1.6e-10)
w=2*pi/4.2
put(77,vmax_m_s=w*.100,a_above_m_s2=-w*w*.050,travel_s=4.2/6,shortening_m=g/w**2)
put(78,Icm_kg_m2=.320*.400*g/(4*pi*pi),uniform_I=.400*.8**2/12)
vfall=math.sqrt(2*g*.40);vp=2.2*vfall/2.4;w=math.sqrt(400/2.4);shift=2.2*g/400
put(79,v_impact=vfall,v_after=vp,eq_shift_m=shift,A_m=math.sqrt(shift**2+(vp/w)**2),T_s=2*pi/w)
k=40/.250;mm=k/(2*pi)**2
put(80,k_N_m=k,m_kg=mm,x_m=.05*math.sin(2*pi*.35),v_m_s=.05*2*pi*math.cos(2*pi*.35),
       spring_force_N=mm*g+k*.030)
put(81,boarding_time_s=3.5/3)
put(82,T_earth_s=2*pi*math.sqrt(6.371e6/g),assumed_radius_m=6.371e6)
v=.008*280/1
put(83,v_after=v,omega=v/.150,T_s=2*pi*.150/v)
put(84,meff_kg=(14/5)*.800,T_s=2*pi*math.sqrt(((14/5)*.8)/160))
v0=math.sqrt(2*g*.1);v1=2*v0/5;angle=math.acos(1-v1*v1/(2*g*.5))
put(85,v_before=v0,v_after=v1,theta_rad=angle,theta_deg=math.degrees(angle),
       f_small_Hz=math.sqrt(g/.5)/(2*pi))
put(86,L_m=18/(34*.60))
put(87,sample_T=2*pi*math.sqrt(2/(3*100)))
put(88,d_over_L=1/(2*math.sqrt(2)),Ip_over_mL2=2/3,
       frequency_coefficient=math.sqrt(3/(2*math.sqrt(2)))/(2*pi))
w=2*pi/1.6
put(89,T_s=1.6,f_Hz=1/1.6,omega=w,A_cm=20/w,amax_cm_s2=w*20,m_kg=75/w**2,
       positive_A_times=[.4,2.0],negative_A_times=[1.2],acceleration_max_times=[.4,1.2,2.0],
       source_last_tick_should_be=1.8,source_last_tick_printed=1.6)
masses=np.array([.1,.2,.3,.4,.5]);period=np.array([8.7,10.5,12.2,13.9,15.1])/10
slope,intercept=np.polyfit(masses,period**2,1);k=4*pi*pi/slope;meff=intercept/slope
T=math.sqrt(slope*.450+intercept)
put(90,masses_kg=masses.tolist(),T2_s2=(period**2).tolist(),slope_s2_kg=slope,
       intercept_s2=intercept,k_N_m=k,meff_kg=meff,fraction_spring_mass=meff/.250,
       T450_s=T,f450_Hz=1/T,omega450=2*pi/T)
Ls=np.array([12,10,8,6,5,4,3,2.5,2.3]);Ts=np.array([6.96,6.36,5.70,4.95,4.54,4.08,3.60,3.35,3.27]);T0=2*pi*np.sqrt(Ls/g)
sl,ic=np.polyfit(Ls[:5],Ts[:5]**2,1)
ratios=Ts/T0
# Linear interpolation of T/T0 versus L between the bracketing data points.
target=1.05
Ltarget=3+(target-ratios[6])*(2.5-3)/(ratios[7]-ratios[6])
theta_target=math.asin(2/Ltarget)
# Exact finite-amplitude correction via arithmetic-geometric mean.
def ratio_exact(theta):
    a,b=1.,math.cos(theta/2)
    for _ in range(20): a,b=(a+b)/2,math.sqrt(a*b)
    return 1/a
def theta_for_ratio(target):
    lo,hi=0,pi-1e-8
    for _ in range(80):
        mid=(lo+hi)/2
        if ratio_exact(mid)<target: lo=mid
        else: hi=mid
    return (lo+hi)/2
put(91,L_m=Ls.tolist(),T_s=Ts.tolist(),ratios=ratios.tolist(),fit_slope=sl,fit_intercept=ic,
       expected_slope=4*pi*pi/g,L_at_ratio_105=Ltarget,theta_est_deg=math.degrees(theta_target),
       theta_exact_ratio105_deg=math.degrees(theta_for_ratio(1.05)),
       theta_exact_relative_T_error5_deg=math.degrees(theta_for_ratio(1/.95)),ratio_definition='(T-T0)/T0 = 0.05')
put(92,sample_parallel=3+7,sample_series=3*7/(3+7),f1_over_f2=1/math.sqrt(2))
put(93,effective_mass_over_M=1/3,kinetic_coefficient=1/6)
m=1000/(2*pi*100e3)**2
put(94,m_kg=m,m_ng=m/1e-12,m_microgram=m/1e-9,choice='c')
put(95,E_J=.5*1000*(.050e-9)**2,choice='a')
put(96,ratio_as_printed=math.sqrt(1005/1000),change_pct=100*(math.sqrt(1005/1000)-1),
       attractive_softening_alternative_pct=100*(math.sqrt(995/1000)-1),choice_nearest='b',
       source_sign_inconsistency=True)
assert len(R)==48
assert all(f'14.{i}' in R for i in range(49,97))
print(json.dumps({'status':'passed','exerciseCount':len(R),'results':R},ensure_ascii=False,indent=2))
