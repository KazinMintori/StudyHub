"""Source-transcribed models for exercises13.1–13.42, not whole chapter."""
import json,math
from scipy.integrate import quad
G=6.67e-11;g=9.80;records={}
Ms=1.99e30;Me=5.97e24;Mm=7.35e22;rs=1.50e11;rm=3.84e8
ratio=Ms/Me*(rm/rs)**2
assert math.isclose(ratio,2.1845333333333334)
records['13.1']={'source_reference':'AppendixF','Sun_mass_kg':Ms,'Earth_mass_kg':Me,'Moon_mass_kg':Mm,'Earth_Sun_distance_m':rs,'Earth_Moon_distance_m':rm,'Sun_on_Moon_to_Earth_on_Moon_force_ratio':ratio}
M,m,r=70.,70.,1.
F=G*M*m/r**2
records['13.2']={'example_assumptions':{'instructor_mass_kg':M,'student_mass_kg':m,'center_distance_m':r},'attraction_N':F,'earth_force_N':m*g,'ratio_to_earth_force':F/(m*g)}
m1,m2,r0=65.,72.,20.
F=G*m1*m2/r0**2;a1=F/m1;a2=F/m2;relative_a=a1+a2
tc=math.sqrt(2*r0/relative_a)
tc_exact=quad(lambda u:2*(math.sqrt(r0)*math.cos(u))**2/math.sqrt(2*G*(m1+m2)/r0),0,math.pi/2)[0]
assert math.isclose(tc_exact/tc,math.pi/4,rel_tol=1e-12)
records['13.3']={'initial_force_N':F,'initial_accel65_m_s2':a1,'initial_accel72_m_s2':a2,'relative_initial_accel_m_s2':relative_a,'constant_accel_time_until_meeting_s':tc,'constant_accel_time_days':tc/86400,'exact_time_s_crosscheck':tc_exact,'acceleration_trend':'increasesasdistancefalls'}
records['13.4']={'formula':'G*M^2/(4*R^2)','condition':'UniformspheresradiusRjusttouch;centerseparation2R.'}
M,m,d=.260,.0100,.100
each=G*M*m/d**2
acc=2*each*(.060/.100)/m
records['13.5']={'each_attraction_N':each,'horizontal_net_N':0,'net_downward_force_N':acc*m,'initial_downward_acceleration_m_s2':acc,'source_geometry_m':{'half_base':.080,'height':.060,'equal_side':.100}}
Fleft=G*2*2/.100**2;Fright=G*2*2/.400**2
records['13.6']={'case_a_rightward_N':G*4*(1/.100**2+1/.500**2),'case_b_leftward_N':Fleft-Fright,'masses_kg':[2,2,2]}
Fmoon=G*Mm*70/(378000e3)**2
records['13.7']={'lunar_attraction_N':Fmoon,'relative_to_earth_weight':Fmoon/(70*g)}
a8=G*(12/.300**2-8/.200**2)
assert a8<0 and math.isclose(a8,-4.446666666666667e-9)
records['13.8']={'source_separation_m':.500,'distance_from8kg_m':.200,'distance_from12kg_m':.300,'signed_acceleration_toward12kg_m_s2':a8,'direction':'towards8kgmass'}
x=1/(1+math.sqrt(3))
assert math.isclose(1/x**2,3/(1-x)**2)
records['13.9']={'zero_force_position_m_from_m_toward3m':x,'axial_equilibrium':'unstable','perpendicular_equilibrium':'stable','note':'Axialdisplacementstrengthensattractiontowardsnearerend;transversedisplacementrestoring.'}
for eps in [.001,.01,.1]:
 Fminus=-1/(x-eps)**2+3/(1-x+eps)**2
 Fplus=-1/(x+eps)**2+3/(1-x-eps)**2
 assert Fminus<0<Fplus
 y=.05
 Fy=-y/(x*x+y*y)**1.5-3*y/((1-x)**2+y*y)**1.5
 assert Fy<0
x=1/(1+math.sqrt(2))
assert math.isclose(1/x**2,2/(1-x)**2)
def force10(x,L=1):
 return -x/abs(x)**3+2*(L-x)/abs(L-x)**3
for p in [-3,-.5,.2,.8,1.2,3]:
 formula=1/p**2+2/(1-p)**2 if p<0 else(-1/p**2+2/(1-p)**2 if p<1 else-1/p**2-2/(p-1)**2)
 assert math.isclose(force10(p),formula)
assert force10(-.5)>0 and force10(1.2)<0
records['13.10']={'zero_force_x_over_L':x,'piecewise_Fx_over_GmM':'+1/x²+2/(L-x)² ifx<0;-1/x²+2/(L-x)² if0<x<L;-1/x²-2/(x-L)² ifx>L','domain':'xnot0,L'}
RE=6.37e6
h11=RE*(math.sqrt(9.80/.980)-1)
assert math.isclose(9.80*(RE/(RE+h11))**2,.980,rel_tol=1e-12)
records['13.11']={'surface_g_m_s2':9.80,'target_g_m_s2':.980,'earth_radius_m':RE,'altitude_m':h11,'center_distance_m':RE+h11}
g12=g*.815/.949**2;w12=75*g12/g
assert math.isclose(g12,8.868522242369263,rel_tol=1e-12)
records['13.12']={'venus_to_earth_mass_ratio':.815,'radius_ratio':.949,'surface_g_m_s2':g12,'rock_weight_N':w12}
Mt=Me/1700;Rt=RE/8;gt=g*64/1700;rhot=Mt/(4*math.pi*Rt**3/3)
records['13.13']={'mass_kg':Mt,'radius_m':Rt,'surface_g_m_s2':gt,'mean_density_kg_m3':rhot}
Rr=764e3;gr=.265;Mr=gr*Rr**2/G;rhor=3*gr/(4*math.pi*G*Rr)
assert math.isclose(Mr/(4*math.pi*Rr**3/3),rhor,rel_tol=1e-12)
records['13.14']={'radius_m':Rr,'surface_g_m_s2':gr,'mass_kg':Mr,'mean_density_kg_m3':rhor}
records['13.15']={'radius_ratio':1.25,'same_density_g_m_s2':1.25*g,'required_density_ratio_for_same_g':.8,'corresponding_mass_ratio':.8*1.25**3}
assert math.isclose(.8*1.25**3/1.25**2,1)
Mi=8.93e22;Ri=1821e3;hi=500e3;gi=G*Mi/Ri**2;v=math.sqrt(2*gi*hi);he=v*v/(2*g)
assert math.isclose(he/hi,gi/g,rel_tol=1e-12)
records['13.16']={'Io_mass_kg':Mi,'Io_radius_m':Ri,'assumed_constant_surface_g_m_s2':gi,'Io_height_m':hi,'launch_speed_m_s':v,'earth_height_m':he,'model':'ConstantgravityonIoasexplicitlyrequested;noheightvariationofg.'}
escape17={name:math.sqrt(2*G*M/R)for name,M,R in [('Mars',6.42e23,3.39e6),('Jupiter',1.90e27,6.99e7)]}
for name,M,R in [('Mars',6.42e23,3.39e6),('Jupiter',1.90e27,6.99e7)]:
 assert math.isclose(escape17[name]**2/2,G*M/R,rel_tol=1e-12)
records['13.17']={'appendix_data_source':'PDF1553/1586','escape_speed_m_s':escape17,'model':'Fixedcentralplanet,spacecraftmassnegligible,nodragorrotation.'}
m18=629.;r18=2.87e6*1000;v18=1.20e4*1000/3600
records['13.18']={'mass_kg':m18,'earth_center_distance_m':r18,'speed_m_s':v18,'kinetic_energy_J':.5*m18*v18*v18,'potential_energy_J':-G*Me*m18/r18}
R19=3.24e6;ve19=7.65e3;g19=ve19**2/(2*R19)
records['13.19']={'planet_radius_m':R19,'escape_speed_m_s':ve19,'surface_g_m_s2':g19}
assert math.isclose(2*g19*R19,ve19**2)
h20=10e3;U0=-G*Me/RE;Uh=-G*Me/(RE+h20);fraction=(Uh-U0)/abs(U0)
assert math.isclose(fraction,h20/(RE+h20),rel_tol=1e-12)
assert math.isclose(fraction,h20/RE,rel_tol=.002)
records['13.20']={'assumed_cruise_altitude_m':h20,'fractional_increase_relative_to_abs_ground_U':fraction,'percentage_increase':100*fraction,'signed_deltaU_over_U_ground':-fraction,'potential_greater':'airplane'}
records['13.21']={'surface_U_J':-1.20e9,'planet_radius_m':5e6,'force_magnitude_N':1.20e9/5e6,'direction':'towardsplanetcenter'}
mu=G*Me
records['13.22']={'new_radius_over_rA':.5,'reason':'CircularorbitK=Gmpm/(2r).'}
records['13.23']={'kinetic_energy_J':2e6,'total_energy_J':-2e6,'potential_energy_J':-4e6}
v24=6200.;r24=mu/v24**2;T24=2*math.pi*r24/v24;a24=v24*v24/r24
records['13.24']={'speed_m_s':v24,'radius_m':r24,'period_s':T24,'period_h':T24/3600,'radial_acceleration_m_s2':a24}
def orbit(h):
 r=RE+h;v=math.sqrt(mu/r);T=2*math.pi*r/v
 assert math.isclose(4*math.pi**2*r**3/T**2,mu,rel_tol=1e-12)
 return {'altitude_m':h,'radius_m':r,'speed_m_s':v,'period_s':T,'period_h':T/3600}
records['13.25']=orbit(890e3)
records['13.26']=orbit(705e3)
v27=4800*math.sqrt(7e7/3e7)
assert math.isclose(v27**2*3e7,4800**2*7e7)
records['13.27']={'second_speed_m_s':v27,'irrelevant_satellite_masses_kg':[68,84],'planet_radius_m':9e6,'orbital_radii_m':[7e7,3e7]}
T28=86400/15.65;r28=(mu*(T28/(2*math.pi))**2)**(1/3)
records['13.28']={'revolutions_per_24h':15.65,'period_s':T28,'radius_m':r28,'altitude_m':r28-RE}
Md=1.5e15;Rd=6e3;vd=math.sqrt(G*Md/Rd);Td=2*math.pi*Rd/vd
records['13.29']={'Deimos_mass_kg':Md,'Deimos_diameter_m':12e3,'circular_surface_speed_m_s':vd,'period_s':Td,'period_h':Td/3600,'model':'IdealsmoothsphericalDeimos,neglectrotationandMars.'}
r30=5.79e10/9;T30=3.09*86400;M30=4*math.pi**2*r30**3/(G*T30**2);v30=2*math.pi*r30/T30
records['13.30']={'Mercury_orbit_radius_m':5.79e10,'planet_orbit_radius_m':r30,'period_s':T30,'star_mass_kg':M30,'star_mass_solar':M30/Ms,'orbital_speed_km_s':v30/1000}
M31=.85*Ms;r31=.11*1.50e11;v31=math.sqrt(G*M31/r31);T31=2*math.pi*r31/v31
records['13.31']={'star_mass_solar':.85,'orbital_radius_m':r31,'orbital_speed_m_s':v31,'period_s':T31,'period_days':T31/86400,'source_star_distance_light_years':57}
records['13.32']={'Charon_period_days':6.39,'Charon_radius_km':19600,'satellite_periods_days':[6.39*(r/19600)**1.5 for r in [48000,64000]]}
a33=5.91e12;e33=.249;T33=2*math.pi*math.sqrt(a33**3/(G*Ms))
records['13.33']={'semimajor_axis_m':a33,'eccentricity':e33,'period_s':T33,'period_earth_years':T33/(365.3*86400),'perihelion_m':a33*(1-e33),'aphelion_m':a33*(1+e33)}
assert math.isclose((a33*(1-e33)+a33*(1+e33))/2,a33)
r34=10.5e6*1000;T34=6.3*86400;M34=4*math.pi**2*r34**3/(G*T34**2)
records['13.34']={'orbital_radius_m':r34,'orbital_period_s':T34,'star_mass_kg':M34,'star_mass_solar':M34/Ms}
for r,T,M in [(r30,T30,M30),(r31,T31,M31),(r34,T34,M34)]:
 assert math.isclose((2*math.pi*r/T)**2/r,G*M/r**2,rel_tol=1e-12)
m35=.020
forces35=[0,G*20*m35/5**2,G*60*m35/8**2]
records['13.35']={'shell_radii_m':[4,6],'shell_masses_kg':[20,40],'probe_mass_kg':m35,'probe_radii_m':[2,5,8],'force_magnitudes_N':forces35}
M36=1000.;R36=5.;m36=2
records['13.36']={'shell_mass_kg':M36,'radius_m':R36,'probe_mass_kg':m36,'r_m':[5.01,4.99,2.72],'force_magnitudes_N':[G*M36*m36/5.01**2,0,0],'graph':'0inside;GMm/r²outside;idealzero-thicknesssurfaceonesidedlimitdiscontinuous.'}
records['13.37']={'solid_sphere_mass_kg':M36,'radius_m':R36,'probe_mass_kg':m36,'r_m':[5.01,2.50],'force_magnitudes_N':[G*M36*m36/5.01**2,G*M36*m36*2.5/R36**3],'graph':'GMmr/R³inside;GMm/r²outside;continuousatR.'}
for x,L in[(.2,.9),(1,2),(100,1)]:
 analytic=-math.log((x+L)/x)/L
 numeric=quad(lambda u:-1/(x+u)/L,0,L,epsabs=1e-12)[0]
 assert math.isclose(analytic,numeric,rel_tol=1e-12)
 h=1e-6*min(x,L)
 def pot(p):return -math.log((p+L)/p)/L
 force=-(pot(x+h)-pot(x-h))/(2*h)
 assert math.isclose(force,-1/(x*(x+L)),rel_tol=2e-7)
records['13.38']={'U':'-(GMm/L)ln((x+L)/x)','Fx':'-GMm/[x(x+L)]','domain':'x>0,L>0','far_limit':'U≈-GMm/x,Fx≈-GMm/x²'}
for x,a in[(0,1),(.2,.9),(1,2),(100,1),(-.4,1)]:
 h=1e-6
 def ur(p):return -1/math.hypot(p,a)
 field=-(ur(x+h)-ur(x-h))/(2*h)
 assert math.isclose(field,-x/(x*x+a*a)**1.5,rel_tol=2e-6,abs_tol=1e-12)
records['13.39']={'U':'-GMm/sqrt(x²+a²)','Fx':'-GMmx/(x²+a²)^(3/2)','at0':{'U':'-GMm/a','Fx':0},'far_positive_x':'U≈-GMm/x,Fx≈-GMm/x²'}
records['13.40']={'shell_field_magnitude_inside':0,'outside':'GM/r²','field_direction_outside':'radiallyinward','ideal_surface':'onesidedlimits;notrequested'}
g41=11.2;M41=1.02e26;R41=2.46e7;T41=16*3600;m41=3.;w41=2*math.pi/T41
records['13.41']={'given_polar_g_m_s2':g41,'GMR2_unrounded_m_s2':G*M41/R41**2,'polar_force_N':m41*g41,'equatorial_centripetal_accel_m_s2':w41*w41*R41,'equatorial_apparent_weight_N':m41*(g41-w41*w41*R41),'using_GMR2_equatorial_N':m41*(G*M41/R41**2-w41*w41*R41),'source_approximation':'Givenpolargravity11.2isrounded;gfromM,Rdifferslessthan0.4percent.'}
T42=24*3600;w42=2*math.pi/T42;gp=G*Me/RE**2;mass42=395/gp;eq42=395-mass42*w42*w42*RE
assert math.isclose(eq42/mass42+w42*w42*RE,gp,rel_tol=1e-12)
records['13.42']={'polar_tension_N':395.,'earth_polar_gravity_m_s2':gp,'assumed_rotation_period_s':T42,'mass_kg':mass42,'equatorial_tension_N':eq42,'polar_minus_equator_N':395-eq42,'model':'SphericalEarth,genuinegravitysameatpoleandequator;rotationchangesapparentweight.'}
assert set(records)=={f'13.{n}'for n in range(1,43)}
print(json.dumps({'status':'passed','scope':'13.1–13.42 early numbered exercises; sourcePDF442–444 andAppendixdata, notwholechapter','count':len(records),'records':records},ensure_ascii=False,indent=2))
