"""Independent calculations from PDF pp. 250–254. No production files modified."""
from pathlib import Path
import json, math, hashlib
import numpy as np
from scipy.integrate import quad

OUT = Path(__file__).resolve().parent
g = 9.80
r = {}
def save(n, **kw): r[f'7.{n}'] = kw
def close(a, b, tol=1e-9):
    assert math.isclose(a, b, rel_tol=tol, abs_tol=tol), (a, b)
sin = lambda d: math.sin(math.radians(d))
cos = lambda d: math.cos(math.radians(d))

save(43, distance_m=4/.2, friction_work_J=-2*g*4)
save(44, minimum_v_over_sqrt_gR=math.sqrt(5), normalized_top_normal=5-4-1)
m=15; k=2.00; f=.2*m*g; EB=.5*m*10**2+m*g*20
Ec=EB-f*100
x=(-f+math.sqrt(f*f+2*k*Ec))/k
close(.5*k*x*x+f*x, Ec)
save(45, spring_constant_N_per_m=k, vB_mps=math.sqrt(2*EB/m), K_first_touch_J=Ec,
     compression_m=x, spring_force_N=k*x, static_limit_N=.8*m*g,
     moves_again=k*x>.8*m*g)
t=math.sqrt(2*(70-50)/g); v=40/t
save(46, fall_time_s=t, top_v_mps=v, base_v_mps=math.sqrt(v*v+2*g*70))
save(47, spring_energy_J=.6*g*2*(sin(37)+.4*cos(37)))
m=1470/g; E=.5*m*1.8**2+(1470*sin(22)-515)*5
Flim=1470*sin(22)+515; x=2*E/Flim; k=Flim/x
close(.5*k*x*x, E)
save(48, stopping_spring_energy_J=E, spring_max_force_N=Flim, compression_m=x,
     kmax_N_per_m=k, spring_initial_touch_distance_m=5-x)
x=4400/1100; E=.5*1100*x*x-40*4-60*g*2.5
save(49, compression_m=x, spring_energy_J=.5*1100*x*x, exit_v_mps=math.sqrt(2*E/60))
save(50, initial_distance_m=.5*1500*50**2/(1500*g*sin(53)+2000-500))
save(51, impact_v_mps=math.sqrt(2*(12-4)*g*2/(12+4)))
save(52, friction_N=(8-.5*.2*4**2-.2*g*3*sin(53))/3)
save(53, bottom_v_mps=math.sqrt(2*g*2.5), bottom_tension_N=3*.3*g)
K1=60*g*65-10500; K2=K1-(.2*60*g+160)*82
save(54, bottom_K_J=K1, bottom_v_mps=math.sqrt(2*K1/60), after_snow_K_J=K2,
     after_snow_v_mps=math.sqrt(2*K2/60), drift_average_resisting_force_N=K2/2.5)
save(55, cos_alpha=2/3, angle_deg=math.degrees(math.acos(2/3)))
E=.5*.4*3**2+.5*200*.16**2; A=math.sqrt(2*E/200)
save(56, energy_J=E, vmax_mps=math.sqrt(2*E/.4), amplitude_m=A,
     compressed_speed_mps=0, max_accel_mps2=200*A/.4)
save(57, horizontal_mu=4.8**2/(2*g*3), arc_friction_work_J=.5*.2*4.8**2-.2*g*1.6)
# Independent symbolic identity, sampled over nonzero angles, rolling friction and initial speed.
for m,L,v0,aa,bb,mu in [(4,30,8,15,25,.1),(10,9,0,10,30,.3),(2,3,7,1,80,0)]:
    s=(v0*v0+2*g*L*sin(aa))/(2*g*(sin(bb)+mu*cos(bb)))
    close(.5*m*v0*v0+m*g*L*sin(aa), m*g*s*(sin(bb)+mu*cos(bb)))
save(58, symbolic_energy_residual_pass=True, formula='(v0^2+2gL sin(alpha))/(2g(sin(beta)+mu_r cos(beta)))')
a=60; b=18
U=lambda x: .5*a*x*x+b*x**3/3
work=quad(lambda x: -a*x-b*x*x, 1, .5)[0]
close(work, U(1)-U(.5))
save(59, initial_U_J=U(1), final_U_J=U(.5), speed_mps=math.sqrt(2*work/.9))
ve=math.sqrt(22.5**2-2*g*11); t=math.sqrt(2*11/g)
save(60, edge_v_mps=ve, flight_s=t, range_m=ve*t)
a=.8;x0=.2;xf=.4;m=.5
work=quad(lambda x:a/(x+x0)**2,0,xf)[0]
close(work,a/x0-a/(xf+x0))
save(61, U0_J=a/x0, Ufinal_J=a/(xf+x0), work_J=work, speed_mps=math.sqrt(2*work/m))
save(62, turning_tension_N=.2*g*cos(37), tension_25deg_N=.2*g*(3*cos(25)-2*cos(37)))
save(63, impact_v_mps=math.sqrt(1900*.045**2/.15+2*g*1.2))
for m,k in [(1,20),(.4,7),(5,120)]:
    d=m*g/k; close(.5*k*(2*d)**2,m*g*2*d)
save(64, stretch_over_equilibrium_stretch=2)
m=1.6;k=45;d=.28;f=.3*m*g
K=lambda s:.5*k*d*d-.5*k*(d-s)**2-f*s
smax=d-f/k
save(65, friction_N=f, leave_K_J=K(d), leave_v_mps=math.sqrt(2*K(d)/m),
     max_speed_position_m=smax, max_speed_remaining_compression_m=f/k,
     max_K_J=K(smax), max_v_mps=math.sqrt(2*K(smax)/m))
m=3;k=1500
xa=2*m*g/k; xb=(m*g+math.sqrt((m*g)**2+2*k*m*g*1))/k
close(.5*k*xb**2,m*g*(1+xb))
save(66, sudden_place_stretch_m=xa, dropped_stretch_m=xb)
save(67, speed_at_005_mps=math.sqrt(2*g*.05-900*.05**2/3), vmax_mps=g*math.sqrt(3/900), vmax_y_m=3*g/900)
t=math.sqrt(80/g);ve=30/t
save(68, flight_s=t, launch_v_mps=ve, friction_work_J=.5*3*ve*ve-3*g*23)
E=20*.25;K=E-.5*40*.25**2;A=math.sqrt(2*E/40)
save(69, energy_J=E, vB_mps=math.sqrt(2*K/.5), amplitude_m=A, min_back_wall_distance_m=.6-A)
m=.04;R=.5
vA2=(3.95-m*g)*R/m;vB2=(.68+m*g)*R/m
save(70, vA2_m2ps2=vA2, vB2_m2ps2=vB2, friction_work_J=.5*m*(vB2-vA2)+m*g*2*R)
save(71, top_normal_N=3.4-6*.05*g, top_normal_if_g_standard_N=3.4-6*.05*9.80665)
save(72, bottom_v_mps=math.sqrt(2*g*.8*(1-cos(45))), turning_tension_N=.12*g*cos(45), bottom_tension_N=.12*g*(3-2*cos(45)))
save(73, initial_spring_U_J=.5*1.5*7**2+1.5*g*6*(sin(30)+.5*cos(30)))
save(74, initial_energy_assumption='small positive initial x, E approximately 0; exactly x=0,v=0 stays at equilibrium',
     U4_J=-2*4**2+.3*4**3, speed4_mps=math.sqrt(2*(2*4**2-.3*4**3)/.09),
     accel4_mps2=(2*2*4-3*.3*4**2)/.09, xmax_m=2/.3)
Wa=quad(lambda y:-2.5*y**3,0,3)[0]
Wb=quad(lambda y:-2.5*3*y**2,0,3)[0]
save(75, diagonal_work_J=Wa, axes_work_J=Wb, conservative=False)
save(76, evidence='Visually read original PDF253 figure P7.76; estimates only', force_A='positive x', force_B='negative x',
     maximum_K_x_m=.75, force_C_N=0, xmax_m_approx=2.25, stable_x_m=[.75,1.9], unstable_x_m=[1.4])
h=np.array([.8,2,4,6,8,10,12]);T=np.array([265,274,298,313,330,348,371])
slope,intercept=np.polyfit(h,T,1);L=2*265/slope
residual=T-(slope*h+intercept)
save(77, data_h_m=h.tolist(),data_T_N=T.tolist(), slope_N_per_m=float(slope), intercept_N=float(intercept),
     residual_N=residual.tolist(), L_m=float(L), max_h_fit_m=float((822/2-intercept)/slope),
     max_h_physical_anchor_m=float(.8+(822/2-265)*L/(2*265)))
mu=[.15,.29,.43,.85]
hs=[16/(2*g*(1-x/math.tan(math.radians(52)))) for x in mu]
save(78, theta_deg=52, height_iron_m=hs[0],height_copper_m=hs[1],height_lead_m=hs[2],height_zinc_m=hs[3], mass_cancels=True)
# Graph ordinates read from the original; these are estimates, not formula-generated data.
save(79, evidence='Original figure has K(0) approx .14 J and K peaks approx .39 J at x=+-1 m',
     initial_E_J=.14, initial_U_minus15_J=.14, Umin_J=.14-.39,
     new_U_minus13_J=.14-.27, new_Kmax_J=.39-.27, new_xmax_m_approx=-.55,
     zeros_force_m=[-1,0,1], force_positive_intervals=[[-1.5,-1],[0,1]],
     force_negative_intervals=[[-1,0],[1,1.5]])
for a,b,m in [(1,1,1),(2,3,4),(.7,2.3,.8)]:
    x0=a/b; xm=2*x0
    U=lambda x:a/x**2-b/x
    close(U(x0),0); close(U(xm),-b*b/(4*a))
    close(2*a/xm**3-b/xm**2,0)
    E1=U(3*x0); close(E1,U(1.5*x0))
    close(E1,-2*b*b/(9*a))
    for x in [1.5*x0,2*x0,2.5*x0,3*x0]:
        close(U(x),a/x0**2*((x0/x)**2-x0/x))
        assert E1-U(x)>-1e-10
save(80, normalized_x0=1, normalized_Ux0=0, normalized_x_vmax=2,
     normalized_vmax=.5, normalized_speed_scale='sqrt(2alpha/(m*x0^2))', second_energy=-2/9,
     second_turning_points=[1.5,3], first_interval='[x0,+infinity); no finite maximum')
save(81, deflection_nm=.1*6/3, choice='c')
save(82, figure_segment_endpoint_nm=50, figure_segment_endpoint_pN=5, k_pN_per_nm=5/50, choice='b')
save(83, energy_J=.5*(.1*1e-12/1e-9)*(50e-9)**2, choice='b')
save(84, formula='P=k*v^2*t', choice='a')
assert sorted(map(lambda x:int(x.split('.')[1]),r))==list(range(43,85))
payload={'scope':'All 42 original problems 7.43–7.84, independent numerical calculations / explicit symbolic identities / visually read graph records',
         'g_mps2':g,'source_pdf_pages':[250,251,252,253,254],
         'authored_file_sha256':hashlib.sha256((OUT/'translations/chapter-07/parent-12-bai-tap-043-084.md').read_text(encoding='utf-8').encode()).hexdigest(),
         'results':r,'passed':True}
print(json.dumps({'status':'passed',**payload},ensure_ascii=False,indent=2))
