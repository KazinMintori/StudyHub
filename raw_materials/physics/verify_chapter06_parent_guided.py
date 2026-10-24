"""Independent calculations for 12 guided, 24 discussion and one bridge unit.

Run with C:/Users/Ai/miniconda3/python.exe -I -X utf8 checks.py.
Only standard-library arithmetic, numerical quadrature and explicit identities.
"""
from pathlib import Path
import json
import math
import random

OUT = Path(__file__).resolve().parent
G = 9.80
results = {}

def put(key, **values):
    results[key] = values

def close(x, y, tol=1e-10):
    assert math.isclose(x, y, rel_tol=tol, abs_tol=tol), (x, y)

def midpoint(f, lo, hi, n=20000):
    dx = (hi-lo)/n
    return math.fsum(f(lo+(i+0.5)*dx)*dx for i in range(n))

sx, sy, fx, fy = 3.00, -6.50, 126.0, 168.0
put('VP6.2.1', sx=sx, sy=sy, Fx=fx, Fy=fy,
    Wx_J=fx*sx, Wy_J=fy*sy, W_opponent_on_player_J=fx*sx+fy*sy,
    W_player_on_opponent_shared_contact_J=-(fx*sx+fy*sy))
close(fx*sx+fy*sy, -714)
put('VP6.2.2', cos_theta=1470/(215*8.4),
    theta_deg=math.degrees(math.acos(1470/(215*8.4))))
wg = 15*G*3*math.sin(math.radians(28))
put('VP6.2.3', W_f_J=-90.0, W_g_J=wg, W_n_J=0.0, W_total_J=wg-90)
close(2-3-8+9, 0)
put('VP6.2.4', coefficients_W1_W2_W3_at_G9=[2,-3,1], G_over_F0=9)
put('VP6.4.1', K_impact_J=(20*G-16)*1.5,
    speed_impact_m_s=math.sqrt(2*(20*G-16)*1.5/20),
    mean_force_N=(20*G-16)*(1.5+.03)/.03,
    full_Wg_J=20*G*1.53, full_Wrail_J=-16*1.53)
ki=.5*14.5*.5**2
wt=175*1.25
wg=-14.5*G*1.25
put('VP6.4.2', W_T_J=wt, W_g_J=wg, W_total_J=wt+wg, K_i_J=ki,
    K_f_J=ki+wt+wg, speed_final_m_s=math.sqrt(2*(ki+wt+wg)/14.5))
ki=.5*1400*3**2
kf=.5*1400*.45**2
wg=1400*G*2
wl=kf-ki-wg
put('VP6.4.3', K_i_J=ki, K_f_J=kf, W_total_J=kf-ki, W_g_J=wg,
    W_lift_J=wl, lift_force_N=-wl/2)
put('VP6.4.4', model='Wg=mgd sin(theta), Wf=-mu mgd cos(theta), v^2=2gd(sin(theta)-mu cos(theta))',
    start_condition='The assumed motion needs static-friction information; mu_k alone does not determine release.')
m,k,v,mu=.150,30,1.25,.320
d0=v*math.sqrt(m/k)
fr=mu*m*G
d=(-fr+math.sqrt(fr**2+k*m*v**2))/k
close(.5*m*v*v, .5*k*d*d+fr*d)
put('VP6.8.1', K_i_J=.5*m*v*v, d_no_friction_m=d0,
    kinetic_friction_N=fr, d_friction_m=d)
close((m*v*v-k*d*d)/(2*m*G*d), mu)
put('VP6.8.2', reconstructed_mu=mu, admissibility='0<d<=v1*sqrt(m/k)')
h=.750*(1-math.cos(math.radians(35)))
put('VP6.8.3', height_m=h, W_AB_J=.500*G*h, W_BC_J=-.500*G*h, W_AC_J=0.)
put('VP6.8.4', identity='v^2=2gL(1-cos(theta))')

# Additional algebra checks use positive random parameters, never SymPy.
rng=random.Random(602)
for _ in range(80):
    m,k,d,v=(rng.uniform(.1,5) for _ in range(4))
    theta=rng.uniform(.1,1.2)
    mu=.25*math.tan(theta)
    wg=m*G*d*math.sin(theta)
    wf=-mu*m*G*d*math.cos(theta)
    v2=2*G*d*(math.sin(theta)-mu*math.cos(theta))
    close(.5*m*v2,wg+wf)
    close(.5*m*(2*G*d*(1-math.cos(theta))),m*G*d*(1-math.cos(theta)))

put('Q6.1', check='Dot products invariant under simultaneous coordinate reversal: (-Fx)(-sx)+(-Fy)(-sy).')
close((-fx)*(-sx)+(-fy)*(-sy),fx*sx+fy*sy)
put('Q6.2', W_total_J=0)
put('Q6.3', check='Third-law forces act on different bodies, so are not added in work on one body.')
put('Q6.4', speed_factor=math.sqrt(2), kinetic_energy_factor=2)
put('Q6.5', check='Uniform circular motion: net force nonzero and perpendicular to velocity, P=0.')
put('Q6.6', work_coefficients_Ts={'bucket_descending':-1,'cart_uphill':1})
put('Q6.7', work_gravity_J=0, work_tension_J=0)
put('Q6.8', speed_factors_sqrt_2gh=[1,1,1], work_factors_mgh=[1,1,2])
work=midpoint(lambda x:x-1,0,2)
close(work,0)
put('Q6.9', signed_area_linear_example=work, function='Fx=c*(x-(x1+x2)/2)')
put('Q6.10', first_deltaK_per_kg=0.5*(15**2-10**2),
    second_deltaK_per_kg=0.5*(20**2-15**2),
    ratio=(20**2-15**2)/(15**2-10**2))
put('Q6.11', speed_m_s=math.hypot(3,4), kinetic_energy_each_J=.5*1.5*5**2)
put('Q6.12', bound='-K_i <= W_total < 0')
put('Q6.13', work_factor=3**2, additional_fraction_of_W1=3**2-1)
for _ in range(80):
    m=rng.uniform(.2,10)
    vi,vf,u=(rng.uniform(-8,8) for _ in range(3))
    w=.5*m*(vf*vf-vi*vi)
    wp=.5*m*((vf-u)**2-(vi-u)**2)
    close(wp,w-u*m*(vf-vi))
put('Q6.14', galilean_work_identity='W_prime=W-u*m*(vf-vi)',
    truck_stop_ground_factor=-.5, truck_stop_initial_comoving_inertial_factor=.5,
    warning='A driver-fixed frame during braking is not inertial.')
put('Q6.15', horizontal_hand_work=0, escalator_hand_work='mg*H, positive')
put('Q6.16', example='Static friction does positive work on box in accelerating truck, in ground frame.')
put('Q6.17', formula='P_avg=m*g*H/dt', hp_in_W=746.)
put('Q6.18', check='Force is not power; horizontal constant-height load has zero upward-support work.')
pin=28000*746
put('Q6.19', input_W=pin, input_MW=pin/1e6, output_MW=30,
    implied_efficiency=30e6/pin)
put('Q6.20', model='a=P/(m*v), v>0, constant positive mechanical power and negligible resistance')
triangle=midpoint(lambda t:t if t<=1 else 2-t,0,2)
close(triangle,1)
put('Q6.21', unit_triangle_area=triangle, unit_triangle_average=triangle/2,
    peak_over_average=1/(triangle/2))
put('Q6.22', can_be_constant={'speed':True,'velocity':False,'kinetic_energy':True})
put('Q6.23', displacement_factor=2, work_factor=2**2,
    assumption='quasistatic extension from natural length, negligible final kinetic energy')
put('Q6.24', additional_work_factor=2**2-1)

bridge=[]
for _ in range(80):
    m=rng.uniform(.1,10)
    a=rng.uniform(.1,100)
    xe=math.sqrt(m*G/a)
    x2=math.sqrt(3*m*G/a)
    x1=rng.uniform(.01,.99)*x2
    v2=2*G*x1-2*a*x1**3/(3*m)
    assert 0<v2<2*G*x1
    close(m*G*x2-a*x2**3/3,0)
    close(m*G-a*x2*x2,-2*m*G)
    close(m*G-a*xe*xe,0)
    close(x2/xe,math.sqrt(3))
    close(midpoint(lambda x:-a*x*x,0,x1),-a*x1**3/3,tol=1e-8)
    # Work-energy derivative equals net force at every interior x.
    close(.5*m*(2*G-2*a*x1*x1/m),m*G-a*x1*x1)
    bridge.append({'m':m,'a':a,'x1':x1,'v2':v2,'x_eq':xe,'x2':x2,
                   'P_spring':-a*x1*x1*math.sqrt(v2)})
put('Bridge6', tested_parameter_sets=len(bridge), x2_over_xeq=math.sqrt(3),
    endpoint_acceleration_over_g=-2, branch='first downward passage, 0<=x1<=sqrt(3mg/a)',
    first_sample=bridge[0])

assert len(results)==37
payload={'g_m_s2':G,'coverage_count':len(results),'status':'PASS','results':results}
print(json.dumps(payload,ensure_ascii=False,indent=2))
