"""Source-specific checks for numbered gravitation problems 13.43–13.84."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad,solve_ivp

OUT=Path(__file__).resolve().parent
G=6.67e-11;ME=5.97e24;RE=6.37e6;MS=1.99e30;RS=6.96e8;c=3e8
DAY=86400.;YEAR=365.25*DAY;LY=9.46e15
results={};assertions=[]
def check(n,key,value,expected,rtol=1e-9,atol=1e-12):
 assert math.isclose(float(value),float(expected),rel_tol=rtol,abs_tol=atol),(n,key,value,expected)
 assertions.append(dict(problem=f'13.{n}',id=key,value=float(value),expected=float(expected),passed=True))
def keep(n,**r):results[str(n)]=r;return r
def circular(mu,r):return math.sqrt(mu/r),2*math.pi*math.sqrt(r**3/mu)

r=7.5*LY;M=(200e3)**2*r/G;rh=2*G*M/c**2
keep(43,r_m=r,M_kg=M,M_solar=M/MS,Rsch_m=rh,Rsch_AU=rh/1.5e11)
check(43,'force_centripetal',G*M/r**2,(200e3)**2/r)
check(43,'not_single_50_solar_star',M/MS>50,1);check(43,'horizon_fits_earth_orbit',rh<1.5e11,1)
T=27*3600;v=30e3*1e3;r=v*T/(2*math.pi);M=v*v*r/G
keep(44,r_m=r,M_kg=M,M_solar=M/MS,Rsch_m=2*G*M/c**2)
check(44,'period',2*math.pi*math.sqrt(r**3/(G*M)),T)
P=np.array([0.,0.]);positions=np.array([[0.,.5],[.5,.5],[.5,0.]]);masses=np.array([1.,2.,1.]);mp=.015
forces=[G*mp*M*(q-P)/np.linalg.norm(q-P)**3 for q,M in zip(positions,masses)]
F=np.sum(forces,axis=0);initial=np.array([-300/math.sqrt(2)]*2)
potential=lambda p:-G*sum(M/np.linalg.norm(q-p)for q,M in zip(positions,masses))
v=math.sqrt(2*(potential(initial)-potential(P)))
keep(45,Fx_N=F[0],Fy_N=F[1],F_N=np.linalg.norm(F),angle_deg=math.degrees(math.atan2(F[1],F[0])),v_m_s=v)
check(45,'force_symmetry',F[0],F[1]);check(45,'energy',.5*mp*v*v+mp*potential(P),mp*potential(initial),atol=1e-24)
check(45,'potential_gradient_x',-(potential(np.array([1e-6,0]))-potential(np.array([-1e-6,0])))/(2e-6)*mp,F[0],rtol=2e-7,atol=1e-22)
g=G*4.8e22/(1.56e6)**2;omega=math.sqrt(g/4.25)
keep(46,g_m_s2=g,omega_rad_s=omega,rpm=omega*60/(2*math.pi));check(46,'centripetal',omega**2*4.25,g)
m1=50.;m2=100.;d0=40.;d=20.;mu=m1*m2/(m1+m2);released=G*m1*m2*(1/d-1/d0);vrel=math.sqrt(2*released/mu);v1=m2*vrel/(m1+m2);v2=m1*vrel/(m1+m2)
keep(47,v50_m_s=v1,v100_m_s=v2,vrel_m_s=vrel,center50_collision_m=26.4,contact_from_initial50_m=26.6)
check(47,'momentum',m1*v1,m2*v2);check(47,'kinetic',.5*m1*v1*v1+.5*m2*v2*v2,released,atol=1e-20)
check(47,'center_of_mass_at_collision',(50*26.4+100*26.8)/150,100*40/150)
D=1.22e9;Mt=1.35e23;Msa=5.68e26;q=math.sqrt(Msa/Mt);x=D/(1+q);xo=D/(q-1)
keep(48,between_from_titan_center_m=x,between_altitude_m=x-2.575e6,outer_equal_magnitudes_m=xo)
check(48,'between_accelerations',G*Mt/x**2,G*Msa/(D-x)**2)
check(48,'outer_accelerations',G*Mt/xo**2,G*Msa/(D+xo)**2)
T=DAY;r=(G*ME*T*T/(4*math.pi**2))**(1/3);lat=math.degrees(math.acos(RE/r))
keep(49,r_m=r,altitude_m=r-RE,max_lat_deg=lat);check(49,'tangent_triangle',r*math.cos(math.radians(lat)),RE)
for R,rho in[(1e6,3000),(2e6,3000)]:
 M=rho*4*math.pi*R**3/3
 check(50,'density_period_R'+str(R),circular(G*M,R)[1],math.sqrt(3*math.pi/(G*rho)))
keep(50,period_ratio=1.)
R=150e3;rho=2500;M=4*math.pi*rho*R**3/3;ve=math.sqrt(2*G*M/R)
keep(51,R_m=R,M_kg=M,escape_m_s=ve);check(51,'escape_energy',.5*ve**2,G*M/R)
R=4.8e6;r=R+5.75e5;T=5800;mu=4*math.pi**2*r**3/T**2;g=mu/R**2
keep(52,mu_m3_s2=mu,g_m_s2=g,weight_N=85.6*g);check(52,'period',circular(mu,r)[1],T)
m=943/9.8;R=2*18850e3/math.pi;gx=915/m;omega=math.sqrt(65/(m*R));Tx=2*math.pi/omega;orb=2*math.pi*math.sqrt((R+2e6)**3/(gx*R**2))
keep(53,m_kg=m,R_m=R,g_m_s2=gx,rotation_s=Tx,rotation_h=Tx/3600,orbit_s=orb,orbit_h=orb/3600)
check(53,'equator_support',m*(gx-omega**2*R),850)
rho0=13000;drop=10000
for r in[0,.1*RE,.6*RE,RE]:
 formula=4*math.pi*(rho0*r**3/3-drop*r**4/(4*RE))
 numerical=quad(lambda z:4*math.pi*z*z*(rho0-drop*z/RE),0,r)[0]
 check(54,'shell_integral_r'+str(r),formula,numerical,atol=1e-10)
keep(54,M_total_kg=4*math.pi*RE**3*(rho0/3-drop/4),surface_g_m_s2=4*math.pi*G*RE*(rho0/3-drop/4))
g=2*1.90/.480**2;M=g*(8.60e7)**2/G;keep(55,g_m_s2=g,M_kg=M);check(55,'fall_distance',.5*g*.480**2,1.90)
g=2*12/4.8;R=2e8/(2*math.pi);M=g*R**2/G;T=circular(G*M,R+3e7)[1]
keep(56,g_m_s2=g,R_m=R,M_kg=M,orbit_s=T,orbit_h=T/3600);check(56,'flight_returns',12*4.8-.5*g*4.8**2,0)
R=4.48e6;r=R+630e3;mu=4900**2*r;g=mu/R**2;flight=12.6**2*math.sin(2*math.radians(30.8))/g
keep(57,g_m_s2=g,range_m=flight);check(57,'projectile_solution',12.6*math.cos(math.radians(30.8))*2*12.6*math.sin(math.radians(30.8))/g,flight)
muA=G*5.;muB=G*10.;x0=.4;xf=.8;xeq=1/(1+math.sqrt(2))
ph=lambda x:-muA/x-muB/(1-x)
acc=lambda x:-muA/x**2+muB/(1-x)**2
vformal=math.sqrt(2*(ph(x0)-ph(xf)))
keep(58,initial_acceleration_m_s2=acc(x0),equilibrium_x_m=xeq,potential_barrier_specific_J_kg=ph(xeq)-ph(x0),formal_unreachable_speed_m_s=vformal,requested_motion_possible=False)
check(58,'initial_left',acc(x0)<0,1);check(58,'barrier',ph(xeq)>ph(x0),1)
check(58,'equilibrium',acc(xeq),0,atol=1e-22)
check(58,'formal_energy',.5*vformal*vformal+ph(xf),ph(x0),atol=1e-22)
for r in[1,2,10]:check(59,'spherical_flux_r'+str(r),G*3/r**2*4*math.pi*r**2,4*math.pi*G*3)
keep(59,flux_factor=4*math.pi)
for a,r in[(.5,2),(3,2),(100,1)]:
 lam=2.;mp=3.;F=2*G*lam*mp*a/(r*math.sqrt(r*r+a*a))
 numerical=quad(lambda y:G*lam*mp*r/(r*r+y*y)**1.5,-a,a,epsabs=1e-20)[0]
 check(60,f'rod_integral_a{a}',F,numerical,rtol=2e-10,atol=1e-20)
 check(60,f'rod_transverse_cancellation_a{a}',quad(lambda y:G*lam*mp*y/(r*r+y*y)**1.5,-a,a)[0],0,atol=1e-20)
keep(60,flux_factor=4*math.pi)
for h in[10,1e5,RE]:
 v2=2*G*ME*h/(RE*(RE+h))
 numerical=quad(lambda z:2*G*ME/z**2,RE,RE+h)[0]
 check(61,'fall_integral_h'+str(h),v2,numerical)
keep(61,earth_scale_GM_over_R=G*ME/RE)
keep(62,work_to_low_orbit_J_kg=G*ME/(2*RE),work_low_orbit_to_infinity_J_kg=G*ME/(2*RE))
check(62,'two_stages_sum',2*results['62']['work_to_low_orbit_J_kg'],G*ME/RE)
for M,R in[(2.,3.),(1.2e30,2e10)]:
 v=math.sqrt(G*M/(4*R));T=4*math.pi*math.sqrt(R**3/(G*M))
 check(63,'centripetal_M'+str(M),M*v*v/R,G*M*M/(4*R*R),atol=1e-20)
 check(63,'energy_M'+str(M),M*v*v-G*M*M/(2*R),-G*M*M/(4*R),atol=1e-20)
keep(63,separation_is_2R=True)
T=137*DAY;va=36e3;vb=12e3;R1=va*T/(2*math.pi);R2=vb*T/(2*math.pi);tot=4*math.pi**2*(R1+R2)**3/(G*T*T);Ma=tot*vb/(va+vb);Mb=tot*va/(va+vb)
T2=7.75*3600;Mo=.67*MS;Mh=3.8*MS;D=(G*(Mo+Mh)*T2*T2/(4*math.pi**2))**(1/3);Ro=D*Mh/(Mo+Mh);Rh=D*Mo/(Mo+Mh);vo=2*math.pi*Ro/T2;vh=2*math.pi*Rh/T2
keep(64,alpha_kg=Ma,beta_kg=Mb,alpha_solar=Ma/MS,beta_solar=Mb/MS,star_radius_m=Ro,BH_radius_m=Rh,star_speed_m_s=vo,BH_speed_m_s=vh,earth_orbit_speed_m_s=2*math.pi*1.5e11/(365.3*DAY),star_radius_earth_ratio=Ro/1.5e11,BH_radius_earth_ratio=Rh/1.5e11,star_speed_earth_ratio=vo/(2*math.pi*1.5e11/(365.3*DAY)),BH_speed_earth_ratio=vh/(2*math.pi*1.5e11/(365.3*DAY)))
check(64,'center_of_mass_alpha_beta',Ma*R1,Mb*R2)
check(64,'orange_star_centripetal',vo*vo/Ro,G*Mh/D**2)
check(64,'compact_centripetal',vh*vh/Rh,G*Mo/D**2)
vi=2e4;ri=2.5e11;rf=5e10;vf=math.sqrt(vi*vi+2*G*MS*(1/rf-1/ri))
keep(65,speed_m_s=vf);check(65,'specific_energy',.5*vi*vi-G*MS/ri,.5*vf*vf-G*MS/rf)
RU=25360e3;mu=9*RU*RU;MU=mu/G;r=RU+104000e3;ao=mu/r**2;gm=G*6.6e19/(236e3)**2;tidal=mu/(r-236e3)**2-mu/r**2
keep(66,Uranus_kg=MU,orbital_accel_m_s2=ao,Miranda_g_m_s2=gm,near_surface_Uranus_differential_m_s2=tidal)
check(66,'surface_gravity_dominates_tidal',gm>tidal,1)
rp=RE+400e3;ra=RE+4000e3;a=(rp+ra)/2;T=2*math.pi*math.sqrt(a**3/(G*ME));vp=math.sqrt(G*ME*(2/rp-1/a));vapo=math.sqrt(G*ME*(2/ra-1/a));dvP=math.sqrt(2*G*ME/rp)-vp;dvA=math.sqrt(2*G*ME/ra)-vapo
keep(67,period_s=T,period_h=T/3600,speed_ratio=ra/rp,perigee_speed_m_s=vp,apogee_speed_m_s=vapo,delta_perigee_m_s=dvP,delta_apogee_m_s=dvA)
check(67,'angular_momentum',rp*vp,ra*vapo);check(67,'specific_energy',vp**2/2-G*ME/rp,vapo**2/2-G*ME/ra)
check(67,'perigee_less_deltav',dvP<dvA,1)
m=5e3;ri=7.2e6;rf=8.8e6;dk=G*ME*m/2*(1/rf-1/ri);du=-2*dk;work=du+dk
keep(68,deltaK_J=dk,deltaU_J=du,work_J=work);check(68,'energy_change',work,G*ME*m/2*(1/ri-1/rf))
m=5000;MM=6.42e23;RM=3.39e6;ri=RM+2e6;rf=RM+4e6;w=G*MM*m/2*(1/ri-1/rf)
keep(69,work_J=w);check(69,'circular_energy_difference',w,-G*MM*m/(2*rf)+G*MM*m/(2*ri))
m=848.;vi=9640.;W=-7.5e9;vf=math.sqrt(vi*vi-2*W/m);ri=G*ME/vi**2;rf=G*ME/vf**2
keep(70,formal_speed_m_s=vf,formal_initial_radius_m=ri,formal_final_radius_m=rf,external_earth_orbit_possible=False)
check(70,'work_energy_circular',-.5*m*vf**2+.5*m*vi**2,W,atol=1e-5)
check(70,'initial_radius_inside_earth',ri<RE,1)
rho0=15e3;drop=13e3;M=4*math.pi*RE**3*(rho0/3-drop/4);g=G*M/RE**2
keep(71,M_kg=M,g_m_s2=g,average_density_kg_m3=rho0-3*drop/4)
check(71,'density_shell_integral',M,quad(lambda r:4*math.pi*r*r*(rho0-drop*r/RE),0,RE)[0])
T=30000*YEAR;a=(G*MS*T*T/(4*math.pi**2))**(1/3)
keep(72,semi_major_m=a,semi_major_AU=a/1.5e11,ratio_Pluto=a/5.91e12,ratio_AlphaCentauri=a/(4.3*LY))
check(72,'Kepler_period',2*math.pi*math.sqrt(a**3/(G*MS)),T)
for a,x,M,m in[(2.,.5,3.,4.),(2.,5.,3.,4.),(2.,100.,3.,4.)]:
 F=G*M*m*x/(a*a+x*x)**1.5
 ring_quad=quad(lambda theta:G*M*m*x/(2*math.pi*(a*a+x*x)**1.5),0,2*math.pi)[0]
 check(73,f'ring_action_reaction_x{x}',F,ring_quad,atol=1e-22)
keep(73,force_direction='toward sphere, positive x for x>0')
for R in[1.,3.]:
 M=2.;m=3.;lam=M/(math.pi*R)
 Fx=quad(lambda t:G*m*lam/R*math.sin(t),0,math.pi,epsabs=1e-20)[0]
 Fy=quad(lambda t:G*m*lam/R*math.cos(t),0,math.pi,epsabs=1e-20)[0]
 check(74,'semicircle_force_R'+str(R),Fx,2*G*M*m/(math.pi*R*R),atol=1e-22)
 check(74,'semicircle_transverse_R'+str(R),Fy,0,atol=1e-22)
keep(74,force_factor_for_GMm_over_L2=2*math.pi)
vc=math.sqrt(G*ME/RE);keep(75,center_speed_m_s=vc)
check(75,'potential_derivative',G*ME*2e6/RE**3,(G*ME*(2e6+1)**2/(2*RE**3)-G*ME*(2e6-1)**2/(2*RE**3))/2,rtol=1e-9)
check(75,'surface_to_center_energy',vc*vc/2,G*ME/(2*RE))
names=['Sao Thủy','Sao Kim','Trái Đất','Sao Hỏa','Sao Mộc','Sao Thổ','Sao Thiên Vương','Sao Hải Vương']
a=np.array([57.9,108.2,149.6,227.9,778.3,1426.7,2870.7,4498.4])*1e9
td=np.array([88.,224.7,365.2,687.,4331.,10747.,30589.,59800.]);ts=td*DAY
x=np.log10(a);y=np.log10(ts);slope,intercept=np.polyfit(x,y,1);bfix=np.mean(y-1.5*x)
G76=6.674e-11;Mfree=4*math.pi**2/(G76*10**(2*intercept));Mfix=4*math.pi**2/(G76*10**(2*bfix));vestaT=1325.4*DAY;av=(10**(-bfix)*vestaT)**(2/3)
keep(76,planet_names=names,semi_major_m=a.tolist(),period_days=td.tolist(),slope=float(slope),intercept=float(intercept),fixed_slope_intercept=float(bfix),M_sun_free_fit_kg=Mfree,M_sun_fixed_fit_kg=Mfix,Vesta_semimajor_m=av,Vesta_AU=av/1.496e11,source_G=G76)
check(76,'slope_close_Kepler',slope,1.5,rtol=2e-3)
check(76,'normal_equation_residuals',float(sum(y-slope*x-intercept)),0,atol=1e-11)
check(76,'Vesta_fixed_relation',10**bfix*av**1.5,vestaT)
D=np.array([4879,12104,12756,6792,142984,120536,51118,49528])*1000;gs=np.array([3.7,8.9,9.8,3.7,23.1,9.,8.7,11.]);dens=3*gs/(2*math.pi*G*D);order=np.argsort(-dens)
keep(77,planet_names=names,diameter_m=D.tolist(),g_m_s2=gs.tolist(),density_kg_m3=dens.tolist(),density_order=[names[i]for i in order],Saturn_g_if_earth_density_m_s2=gs[2]*D[5]/D[2])
for i in range(8):check(77,'surface_reconstruction_'+str(i),2*math.pi*G*dens[i]*D[i]/3,gs[i])
masses=np.array([3.30e23,4.87e24,5.97e24,6.42e23,1.90e27,5.68e26,8.68e25,1.02e26]);orbitalR=np.array([5.79e10,1.08e11,1.50e11,2.28e11,7.78e11,1.43e12,2.87e12,4.50e12]);periods=np.array([88*DAY,224.7*DAY,365.3*DAY,687*DAY,11.86*YEAR,29.45*YEAR,84.02*YEAR,164.8*YEAR]);Ls=2*math.pi*masses*orbitalR**2/periods
spin=.4*MS*RS**2*2*math.pi/(24.6*DAY);sumL=float(sum(Ls));massP=float(sum(masses))
keep(78,planet_names=names,planet_orbital_angular_momentum=Ls.tolist(),total_orbital_angular_momentum=sumL,sun_spin_angular_momentum=spin,spin_to_planet_orbits_ratio=spin/sumL,planet_total_mass_kg=massP,sun_to_planet_mass_ratio=MS/massP)
for i in range(8):check(78,'L_MvR_'+str(i),Ls[i],masses[i]*(2*math.pi*orbitalR[i]/periods[i])*orbitalR[i])
re=1.5e11;rm=2.28e11;a=(re+rm)/2;t=math.pi*math.sqrt(a**3/(G*MS));phi=math.pi-2*math.pi*t/(687*DAY)
keep(79,transfer_s=t,transfer_days=t/DAY,Mars_lead_deg=math.degrees(phi),departure_delta_m_s=math.sqrt(G*MS*(2/re-1/a))-math.sqrt(G*MS/re),arrival_delta_m_s=math.sqrt(G*MS/rm)-math.sqrt(G*MS*(2/rm-1/a)))
check(79,'Mars_arrival_phase',phi+2*math.pi*t/(687*DAY),math.pi)
Mbh=5*MS;mu=G*Mbh;r=120e3;d=.06;m=.03;omega2=mu/r**3
Ti=m*(mu/(r-d)**2-omega2*(r-d));To=m*(omega2*(r+d)-mu/(r+d)**2);Tapprox=3*mu*m*d/r**3
keep(80,inner_tension_N=Ti,outer_tension_N=To,first_order_tension_N=Tapprox,Schwarzschild_from_mass_m=2*mu/c**2,CG_shift_two_ear_model_m=-d*((r-d)**-2-(r+d)**-2)/((r-d)**-2+(r+d)**-2))
check(80,'inner_series',Ti,Tapprox,rtol=2e-6);check(80,'outer_series',To,Tapprox,rtol=2e-6)
for a,x in[(2.,.5),(2.,2),(2.,100)]:
 M=3.;m=4.;sigma=M/(math.pi*a*a);F=2*math.pi*G*sigma*m*(1-x/math.sqrt(x*x+a*a))
 numerical=quad(lambda s:G*m*x*2*math.pi*sigma*s/(x*x+s*s)**1.5,0,a,epsabs=1e-22)[0]
 check(81,'disk_ring_integral_x'+str(x),F,numerical,rtol=1e-10,atol=1e-24)
keep(81,force_direction='toward disk for x>0')
rho_ratio=7.9/2.3**3;g_ratio=7.9/2.3**2;r_ratio=(.7*(9.5/365.3)**2)**(1/3)
keep(82,density_ratio=rho_ratio,choice='c');check(82,'composition_interval',.4<rho_ratio<.9,1)
keep(83,g_ratio=g_ratio,choice='c');check(83,'option_1p5',g_ratio,1.5,rtol=.01)
keep(84,radius_ratio=r_ratio,choice='b');check(84,'period_ratio',math.sqrt(r_ratio**3/.7),9.5/365.3)

assert set(results)==set(map(str,range(43,85)))
payload=dict(status='passed',problemCount=len(results),assertionCount=len(assertions),constants=dict(G=G,ME=ME,RE=RE,MS=MS,RS=RS,c=c,day=DAY,year=YEAR,light_year=LY),results=results,assertions=assertions,limitations=['13.58 requested rightward trajectory is impossible from rest; formal energy speed is not a reachable-state answer.','13.70 circular-orbit algebra returns a radius inside Earth; given inputs do not describe an exterior Earth orbit.','13.76 uses the explicit problem-specific G=6.674e-11; all other numerical G values use6.67e-11.'])
print(json.dumps(payload,ensure_ascii=False,indent=2))
