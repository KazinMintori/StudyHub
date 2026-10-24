"""Independent calculations for all48 chapter6 late exercises6.50–6.97."""
import math,json

g=9.80
hp=746.0
records={}

m,v,mu=20.,8.,.200
friction=mu*m*g
time=v/(mu*g)
work=-m*v*v/2
power=work/time
assert math.isclose(power,-156.8)
assert math.isclose(power,-friction*v/2)
records['6.50']={'friction_N':friction,'stop_time_s':time,'work_J':work,'average_power_W':power}

height=50*.3048
mass_assumed=70.
time=mass_assumed*g*height/500
assert math.isclose(time,20.90928)
records['6.51']={'illustrative_mass_kg':mass_assumed,'height_m':height,'climb_time_s':time,'assumption':'Replace mass with a class estimate; this is not a measured population mean.'}

climb_power=700*g*2.5
records['6.52']={'climb_power_W':climb_power,'fraction':climb_power/75000,'percent':100*climb_power/75000}
assert math.isclose(records['6.52']['fraction'],.22866666666666666)

work_one=30*g*.90
rate_a=(.50*hp)*60/work_one
rate_b=100*60/work_one
records['6.53']={'work_per_crate_J':work_one,'rate_a_per_min':rate_a,'rate_b_per_min':rate_b}
assert math.isclose(rate_a,84.58049886621315)

speed=20/16
motor_power=40*hp
max_count=math.floor((motor_power/(g*speed)-600)/65)
required=lambda n:(600+65*n)*g*speed
assert max_count==28 and required(28)<=motor_power<required(29)
records['6.54']={'speed_m_s':speed,'motor_power_W':motor_power,'passengers':max_count,'power_for28_W':required(28),'power_for29_W':required(29)}

speed=12/3.6
theta=math.radians(15)
power=50*70*g*speed*math.sin(theta)
height=300*math.sin(theta)
duration=300/speed
assert math.isclose(power,50*70*g*height/duration)
records['6.55']={'rope_speed_m_s':speed,'height_m':height,'travel_time_s':duration,'lifting_power_W':power}

power=(-8)*3.20+3*2.20
assert math.isclose(power,-19)
records['6.56']={'Fx_N':-8,'Fy_N':3,'vx_m_s':3.2,'vy_m_s':2.2,'power_W':power}

force=2*.010*g
work_one=force*.010
power=100*work_one
assert math.isclose(power,.196)
records['6.57']={'mass_kg':.010,'average_downstroke_force_N':force,'work_per_downstroke_J':work_one,'power_W':power,'source_check':'Mass is10g in the rendered original; original odd answer0.20W is consistent.'}

distance=6.9
work=-20*distance-3*distance**2/2
assert math.isclose(work,-209.415)
records['6.58']={'Fx':'-(20+3x) N for x in metres','distance_m':distance,'work_J':work}


theta=math.radians(32);m=20;d=3.8;force=160;mu=.3
Wpull=force*d;Wg=-m*g*d*math.sin(theta);Wf=-mu*m*g*math.cos(theta)*d;Wtotal=Wpull+Wg+Wf
records['6.59']={'pull_work_J':Wpull,'gravity_work_J':Wg,'normal_work_J':0,'friction_work_J':Wf,'total_work_J':Wtotal,'final_speed_m_s':math.sqrt(2*Wtotal/m)}
for angle,T,M in [(30,2,3),(70,4,6)]:
 a=math.radians(angle);v0=g*T/(2*math.sin(a));work=M*g*g*T*T/(8*math.sin(a)**2)
 assert math.isclose(work,M*v0*v0/2)
 assert math.isclose(M*g*g*(2*T)**2/(8*math.sin(a)**2),4*work)
records['6.60']={'formula':'M*g^2*T^2/(8sin(alpha0)^2)','double_time_ratio':4,'sampled_cases':2}
Wf1=.5*5*25-5*g*2;mu=-Wf1/(5*g*2/math.tan(math.radians(60)))
Wf2=-mu*5*g*2/math.tan(math.radians(50))
records['6.61']={'friction_work_60_J':Wf1,'inferred_mu':mu,'friction_work_50_J':Wf2,'magnitude_change':'increases; a printed decreases answer conflicts with both geometry and numeric partc'}
for theta in [20,30,50,60]:
 a=math.radians(theta);m,mu,h=2.3,.17,3.8;distance=h/math.sin(a)
 assert math.isclose(-mu*m*g*h/math.tan(a),-mu*m*g*math.cos(a)*distance)
records['6.62']={'work':'-mu_k*m*g*h*cot(alpha)','decreasing_angle':'larger negative work magnitude at fixed h','domain':'0<alpha<90degrees; block actually slides downward'}
w1,w2,d=20,12,.750
no_a=w2*g/(w1+w2);a=(w2-.325*w1)*g/(w1+w2)
assert w2>.5*w1
records['6.63']={'no_friction':{'a_m_s2':no_a,'table_block_work_J':w1/g*no_a*d,'hanging_block_work_J':w2/g*no_a*d},'with_friction':{'a_m_s2':a,'table_block_work_J':w1/g*a*d,'hanging_block_work_J':w2/g*a*d,'static_max_N':10,'hanging_weight_N':12}}
m,d,mu=5,2.8,.31;a=math.radians(24)
Wf=-mu*m*g*math.cos(a)*d;Wg=m*g*math.sin(a)*d;total=Wf+Wg
records['6.64']={'friction_work_J':Wf,'gravity_work_J':Wg,'normal_work_J':0,'total_work_J':total,'final_speed_m_s':math.sqrt(2.2**2+2*total/m)}
v=math.sqrt(2*8/5);a=v/.010
records['6.65']={'threshold_energy_J':8,'head_mass_kg':5,'speed_m_s':v,'speed_mph':v/0.44704,'average_acceleration_m_s2':a,'average_acceleration_g':a/g,'average_head_force_N':5*a}
W=-12*5+.3*5**3/3;K=.5*5*6**2+W
records['6.66']={'work_J':W,'final_K_J':K,'speed_m_s':math.sqrt(2*K/5),'direction_at_x5':'positive, after an initial excursion and leftward turning point'}
# K(x)=90-12x+0.1x^3. Only its negative root is a turning point.
lo,hi=-20.,-6.
for _ in range(100):
 mid=(lo+hi)/2
 if 90-12*mid+.1*mid**3>0:hi=mid
 else:lo=mid
turn=(lo+hi)/2;assert math.isclose(90-12*turn+.1*turn**3,0,abs_tol=1e-10)
records['6.66']['left_turn_m']=turn
slope=(.6-.1)/12.5
stop=(-.1+math.sqrt(.1**2+slope*4.5**2/g))/slope
assert math.isclose(g*(.1*stop+slope*stop*stop/2),4.5**2/2)
records['6.67']={'coefficient_slope_per_m':slope,'stop_distance_m':stop,'mu_at_stop':.1+slope*stop,'constant_mu_stop_m':4.5**2/(2*.1*g)}
k,b,c=100,700,12000
work=lambda x:k*x*x/2-b*x**3/3+c*x**4/4
records['6.68']={'stretch_work_J':work(.05),'compress_work_J':work(-.05),'easier':'stretch'}
records['6.69']={'half_work_speed_ratio':1/math.sqrt(2),'half_speed_work_ratio':.25}
k=530/.018;xi=.018;xf=710/k
records['6.70']={'k_N_per_m':k,'initial_compression_m':xi,'final_compression_m':xf,'spring_work_J':-k*(xf*xf-xi*xi)/2}
m=.060;v1=.70;r1=.40;v2=2.80;r2=.10
records['6.71']={'initial_tension_N':m*v1*v1/r1,'final_tension_N':m*v2*v2/r2,'work_J':m*(v2*v2-v1*v1)/2}
m=1.67e-27;v0=3e5;alpha=2.12e-26;ri=5.;rf=8e-10
K0=m*v0*v0/2;K=K0+alpha*(1/ri-1/rf);rmin=1/(1/ri+K0/alpha)
assert K>0
records['6.72']={'initial_K_J':K0,'speed_at_8e10m_m_s':math.sqrt(2*K/m),'rmin_m':rmin,'return_speed_m_s':v0}
records['6.73']={'minimum_spring_k_N_m':1200*.65**2/.090**2,'condition':'k>=minimum for compression<=0.090m'}
net=.5*80*(1.5**2-5**2);pedal=net+80*g*5.2
records['6.74']={'net_work_J':net,'gravity_work_J':-80*g*5.2,'pedal_work_J':pedal}
m,k,x,mu=2.5,250,.25,.3
Wspring=.5*k*x*x;distance=Wspring/(mu*m*g)
assert distance>x
records['6.75']={'initial_spring_energy_J':Wspring,'friction_N':mu*m*g,'total_distance_m':distance,'compression_m':x}
k,x,m,fr=400,.06,.03,6.
K0=k*x*x/2;Kexit=K0-fr*x;travel=x-fr/k
Kmax=K0-k*(x-travel)**2/2-fr*travel
assert math.isclose(k*(x-travel),fr)
records['6.76']={'no_friction_exit_speed_m_s':math.sqrt(2*K0/m),'with_friction_exit_speed_m_s':math.sqrt(2*Kexit/m),'max_speed_distance_m':travel,'max_speed_compression_m':x-travel,'maximum_speed_m_s':math.sqrt(2*Kmax/m)}


m,k,F,mu,x=4,130,82,.4,.8
K=F*x-.5*k*x*x-mu*m*g*x
records['6.77']={'K_J':K,'speed_m_s':math.sqrt(2*K/m),'a_towards_wall_m_s2':(F-k*x-mu*m*g)/m}
m,k,F,x=2,76,54,.4;K=F*x-k*x*x/2
records['6.78']={'speed_m_s':math.sqrt(2*K/m),'acceleration_away_from_post_m_s2':(F-k*x)/m}
records['6.79']={'max_compression_m':6*math.sqrt(5/500),'max_initial_speed_m_s':.15*math.sqrt(500/5)}
Wpush=600*2.5*math.cos(math.pi/6);Wg=-85*g*2.5*.5;K=.5*85*2**2+Wpush+Wg
records['6.80']={'push_work_J':Wpush,'gravity_work_J':Wg,'final_K_J':K,'final_speed_m_s':math.sqrt(2*K/85)}
K0=.5*14*.9**2;d=2
f=(6*g*d+K0)/d
records['6.81']={'initial_system_K_J':K0,'friction_N':f,'mu_k':f/(8*g)}
W=(6*g-.25*8*g)*1.5
records['6.82']={'net_work_J':W,'speed_m_s':math.sqrt(2*W/14)}
records['6.83']={'distance_m':(3**2-1.65**2)/(2*.25*g)}
records['6.84']={'bird_power_W':[10*.070,25*.070],'bird_work_per_beat_J':[10*.070/10,25*.070/10],'human_required_W':[10*70,25*70],'available_steady_W':500,'peak_1400W_not_sustained':True}
Wlift=800*g*14;Wkin=.5*800*18**2
records['6.85']={'lift_work_per_min_J':Wlift,'kinetic_work_per_min_J':Wkin,'power_W':(Wlift+Wkin)/60}
angle=math.radians(37);K=.760*.600*angle-.200*g*.600*(1-math.cos(angle))
records['6.86']={'applied_work_J':.760*.600*angle,'gravity_work_J':-.200*g*.600*(1-math.cos(angle)),'final_K_J':K,'speed_m_s':math.sqrt(2*K/.2)}
T=37.;m1=8.;m2=6.;d=.8
Wg=m2*g*d;WT2=-T*d;K2=Wg+WT2;v=math.sqrt(2*K2/m2);K1=.5*m1*v*v;WT1=T*d;Wf=K1-WT1
records['6.87']={'hanging_gravity_J':Wg,'hanging_tension_J':WT2,'hanging_net_work_J':K2,'speed_m_s':v,'table_net_work_J':K1,'table_tension_J':WT1,'table_friction_J':Wf,'system_net_work_J':K1+K2,'system_gravity_J':Wg,'system_tension_J':0}
assert math.isclose(K1+K2,Wg+Wf)
alpha=2.5
records['6.88']={'horizontal_path_work_J':alpha*3*2**2/2,'vertical_path_work_J':0,'line_y15x_work_J':alpha*1.5*2**3/3,'same_endpoints_path_dependence':True}
volume=7500e-3;mass=volume*1.05e3;work=mass*g*1.63
records['6.89']={'volume_m3':volume,'mass_kg':mass,'work_per_day_J':work,'power_W':work/(24*3600)}
coefficient,exponent=33.55,.4871
integral=lambda x:coefficient*x**(exponent+1)/(exponent+1)
W1=integral(.04);W2=integral(.08)-integral(.04)
records['6.90']={'force_fit':'F[N]=33.55*(x[m])^0.4871','keff_fit_coefficient':coefficient*exponent,'keff_exponent':exponent-1,'work0_to04_J':W1,'work04_to08_J':W2,'speed_after04_travel_from08_m_s':math.sqrt(2*W2/.3)}
import numpy as np
D=np.array([0,.05,.10,.15,.25,.30,.35,.40]);V=np.array([0,.85,1.11,1.24,1.26,1.14,.90,.36])
A,B,C=np.polyfit(D,V**2,2);dmax=-B/(2*A);vmax=math.sqrt(A*dmax*dmax+B*dmax+C);m=.300;x0=.400;k=-m*A;mu=(2*k*x0-m*B)/(2*m*g)
records['6.91']={'d_m':D.tolist(),'v_m_s':V.tolist(),'fit_A_s2':float(A),'fit_B_m_s2':float(B),'fit_C_m2_s2':float(C),'dmax_m':float(dmax),'vmax_m_s':float(vmax),'k_N_m':float(k),'mu_k':float(mu),'fit_residual_m2_s2':(V**2-(A*D**2+B*D+C)).tolist()}
# Approximate bar heights read directly from the original graph, not invented exact measurements.
times=[31,50,45,53];masses=[50.2,68.2,81.8,59.1];names=['Tatiana','Bill','Ricardo','Melanie']
powers=[m*g*16/t for m,t in zip(masses,times)]
records['6.92']={'graph_times_s_approx':dict(zip(names,times)),'power_W_approx':dict(zip(names,powers)),'max':'Ricardo','min':'Melanie','Chang_time_s':62.3*g*16/746}
M,m,k,X=.243,.053,3200,.025
E=.5*k*X*X;v_massless=math.sqrt(2*E/m);v_massive=math.sqrt(2*E/(m+M/3))
Kball=.5*m*v_massive*v_massive;Kspring=M*v_massive*v_massive/6
assert math.isclose(Kball+Kspring,E)
for L,M,v in [(2,.243,4),(1.3,.7,2.1)]:
 # Analytic integral M*v²/(2L³)*int(l² dl) = Mv²/6.
 assert math.isclose(M*v*v/(2*L**3)*(L**3/3),M*v*v/6)
records['6.93']={'spring_K_formula':'M*v^2/6','initial_spring_energy_J':E,'massless_speed_m_s':v_massless,'massive_speed_m_s':v_massive,'final_ball_K_J':Kball,'final_spring_K_J':Kspring}
alpha,beta=.30,3.5e5
vrange=(beta/alpha)**.25;vendurance=(beta/(3*alpha))**.25
assert math.isclose(2*alpha*vrange-2*beta/vrange**3,0,abs_tol=1e-9)
assert math.isclose(3*alpha*vendurance**2-beta/vendurance**2,0,abs_tol=1e-9)
records['6.94']={'max_range_speed_m_s':vrange,'max_range_speed_km_h':3.6*vrange,'max_endurance_speed_m_s':vendurance,'max_endurance_speed_km_h':3.6*vendurance,'assumption':'Fixed mechanical energy available for a fuel amount; efficiency not speed dependent in this model.'}
records['6.95']={'biking_to_walking_energy_ratio':1/3,'choice':'a'}
v=5/3.6;grade=.05;vy=v*grade/math.sqrt(1+grade**2);P=300+70*g*vy
records['6.96']={'vertical_speed_m_s':vy,'required_power_W':P,'choice':'c'}
records['6.97']={'kinetic_energy_ratio':(15/5)**2,'choice':'d'}
assert set(records)=={f'6.{i}'for i in range(50,98)}
print(json.dumps({'status':'passed','scope':'Independent numerical and symbolic checks for all48late problems6.50–6.97','sourcePDFPages':[216,217,218,219,220],'records':records},ensure_ascii=False,indent=2))
