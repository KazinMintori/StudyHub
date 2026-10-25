"""Independent recalculation of Chapter13 drafts from the PDF inputs.

Does not import or run either author's verification code.
"""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad,solve_ivp

OUT=Path(__file__).resolve().parent
records=[]
def check(id,value,expected,rtol=1e-10,atol=1e-12,note=''):
    ok=math.isclose(float(value),float(expected),rel_tol=rtol,abs_tol=atol)
    records.append(dict(id=id,value=float(value),expected=float(expected),rtol=rtol,atol=atol,passed=ok,note=note))
    assert ok,records[-1]
G=6.67e-11;ME=5.97e24;RE=6.37e6;MS=1.99e30;c=3e8;mu=G*ME

F=G*.01*.5/.05**2
check('ex13.1.force_N',F,1.334e-10)
check('ex13.2.small_accel',F/.01,1.334e-8)
check('ex13.2.large_accel',F/.5,2.668e-10)
check('ex13.2.acceleration_ratio',(.5)/(.01),50)
positions=np.array([[2e12,2e12],[2e12,0]])
vector=sum((G*8e30*1e30*p/np.linalg.norm(p)**3 for p in positions),start=np.zeros(2))
check('ex13.3.force_norm_N',np.linalg.norm(vector),1.866e26,rtol=.005)
check('ex13.3.force_angle_deg',math.degrees(math.atan2(vector[1],vector[0])),14.6,atol=.05)
check('ex13.3.small_star_accel',np.linalg.norm(vector)/1e30,1.87e-4,rtol=.005)
check('selfcheck13.1.accelSaturn_over_Earth',(G*MS/(10**2))/(G*MS),.01)
check('text.massEarth_from_g',9.8*RE**2/G,5.96e24,rtol=.001)
check('text.tenkm_weight_loss_fraction',1-(RE/(RE+10000))**2,.003132,atol=1e-6)
check('text.Earth_volume_m3',4*math.pi*RE**3/3,1.0826969324300024e21,rtol=1e-6)
check('text.Earth_average_density',ME/(4*math.pi*RE**3/3),5500,rtol=.003)
mass=3430/9.8;gm=G*6.42e23/(3.39e6)**2
check('ex13.4.mass_kg',mass,350)
check('ex13.4.gMars',gm,3.73,atol=.005)
check('ex13.4.weightMars_N',mass*gm,1300,rtol=.005)
for i,(mass_ratio,radius_ratio,result)in enumerate([(2,2,.5),(4,4,.25),(4,2,1),(2,4,.125)],1):
    check(f'selfcheck13.2.case{i}',mass_ratio/radius_ratio**2,result)

for j,(r1,r2)in enumerate([(RE,2*RE),(2*RE,RE),(RE,20*RE)],1):
    work,error=quad(lambda r:-mu*1000/r**2,r1,r2,epsabs=.01,epsrel=1e-12)
    check(f'eq13.8.work_integral{j}',work,mu*1000*(1/r2-1/r1),rtol=1e-12,atol=.001)
v1=math.sqrt(mu/RE);vesc=math.sqrt(2*mu/RE)
check('ex13.5.h_RE_speed',v1,7910,atol=5)
check('ex13.5.escape_speed',vesc,11200,atol=50)
check('ex13.5.threshold_energy_h_RE',v1**2/2-mu/RE,-mu/(2*RE),atol=1e-8)
check('ex13.5.escape_threshold_energy',vesc**2/2-mu/RE,0,atol=1e-8)
check('ex13.5.escape_km_h',vesc*3.6,40300,atol=50)
check('ex13.5.superescape_E_positive',(.5*(1.1*vesc)**2-mu/RE)>0,1)
for factor in[.5,1,2,10]:
    check(f'selfcheck13.3.same_g_Rfactor{factor}',math.sqrt(2*9.8*RE*factor)/math.sqrt(2*9.8*RE),math.sqrt(factor))
r=RE+340000;v=math.sqrt(mu/r);T=2*math.pi*r/v;a=mu/r**2
check('ex13.6.radius_m',r,6.71e6)
check('ex13.6.speed_m_s',v,7700,atol=5)
check('ex13.6.period_s',T,5470,atol=5)
check('ex13.6.period_min',T/60,91.2,atol=.05)
check('ex13.6.radial_accel',a,8.84,atol=.005)
E1=-mu*1000/RE;E2=-mu*1000/(2*r)
check('ex13.6.E1_J',E1,-6.25e10,rtol=.001)
check('ex13.6.E2_J',E2,-2.97e10,rtol=.001)
check('ex13.6.launch_work_J',E2-E1,3.28e10,rtol=.002)
check('ex13.6.additional_escape_work',-E2,2.97e10,rtol=.001)
check('ex13.6.initial_rotation_KE',.5*1000*410**2,8.405e7)
check('selfcheck13.4.smaller_circle_faster',math.sqrt(mu/(.99*r))>math.sqrt(mu/r),1)
check('selfcheck13.4.smaller_circle_lower_E',-mu/(2*.99*r)<-mu/(2*r),1)

year=3.156e7;pallasT=4.62*year;pallasa=(G*MS*pallasT**2/(4*math.pi**2))**(1/3)
check('ex13.8.Pallas_a',pallasa,4.15e11,atol=5e8)
rp=8.80e7*1000;ra=5.25e9*1000;ha=(rp+ra)/2;he=(ra-rp)/(ra+rp);ht=2*math.pi*math.sqrt(ha**3/(G*MS))
check('ex13.9.Halley_a_km',ha/1000,2.669e9)
check('ex13.9.Halley_e',he,.967,atol=.0005)
check('ex13.9.Halley_T_year',ht/year,75.3,atol=.05)
check('selfcheck13.5.period_ratio',4**1.5,8)
for ecc in[0,.2,.7]:
    semi=1.4;u=2.3;period=2*math.pi*math.sqrt(semi**3/u)
    rperi=semi*(1-ecc);vperi=math.sqrt(u*(1+ecc)/(semi*(1-ecc)))
    initial=[rperi,0,0,vperi,0]
    def ode(t,z):
        x,y,vx,vy,area=z;rr=math.hypot(x,y)
        return[vx,vy,-u*x/rr**3,-u*y/rr**3,(x*vy-y*vx)/2]
    sol=solve_ivp(ode,[0,period],initial,rtol=3e-12,atol=1e-13,dense_output=True)
    ts=np.linspace(0,period,101);zs=sol.sol(ts);radius=np.hypot(zs[0],zs[1]);h=zs[0]*zs[3]-zs[1]*zs[2]
    E=(zs[2]**2+zs[3]**2)/2-u/radius
    check(f'Kepler.e{ecc}.angular_momentum_error',np.max(abs(h-h[0])),0,atol=3e-9)
    check(f'Kepler.e{ecc}.energy_error',np.max(abs(E-E[0])),0,atol=3e-9)
    check(f'Kepler.e{ecc}.area_linear_error',np.max(abs(zs[4]-h[0]*ts/2)),0,atol=3e-8)
    check(f'Kepler.e{ecc}.one_period_position_error',np.linalg.norm(zs[:2,-1]-zs[:2,0]),0,atol=5e-8)
    check(f'ex13.7.e{ecc}.max_speed_at_peri',np.max(np.hypot(zs[2],zs[3])),vperi,atol=3e-8)

# Dimensionless direct angular integral, independent of the author's changed
# integration variable s, for both interior and exterior shell points.
for rr in[0,.1,.5,.9,1.1,2,7]:
    integral,_=quad(lambda phi:math.sin(phi)/math.sqrt(rr**2-2*rr*math.cos(phi)+1),0,math.pi,epsabs=1e-11,epsrel=1e-11)
    U=-integral/2
    expected=-1 if rr<1 else-1/rr
    check(f'shell.potential_r{rr}',U,expected,rtol=1e-10)
for rr in[.1,.4,.8,1,1.5,3]:
    U,_=quad(lambda ss:-3*ss**2/max(rr,ss),0,1,points=[rr]if rr<1 else None,epsabs=1e-11)
    expected=-(3-rr**2)/2 if rr<=1 else-1/rr
    check(f'uniform_sphere.potential_r{rr}',U,expected)
    eps=1e-5
    def potential(x):return-(3-x*x)/2 if x<=1 else-1/x
    force=-(potential(rr+eps)-potential(rr-eps))/(2*eps)
    expected_force=-rr if rr<=1 else-1/rr**2
    check(f'ex13.10.force_r{rr}',force,expected_force,atol=1e-5)
check('selfcheck13.6.hollow_shell_force',0,0,note='Force equals negative derivative of constant interior potential.')

omega=2*math.pi/86164;ae=omega**2*RE
check('rotation.equator_speed',omega*RE,465,atol=.5)
check('rotation.equator_delta_g',ae,.0339,atol=.00005)
check('selfcheck13.7.tenfold_rotation_delta_g',ae*100,3.39,atol=.005)
check('rotation.zero_weight_rotation_factor',math.sqrt(9.8/ae),17.0,atol=.05)
for lat in[0,15,30,45,60,75,90]:
    phi=math.radians(lat);er=np.array([math.cos(phi),math.sin(phi)])
    g0vec=-9.8*er;ar=np.array([-omega**2*RE*math.cos(phi),0]);geff=g0vec-ar
    diff=9.8-np.linalg.norm(geff)
    check(f'rotation.lat{lat}.delta_in_bound',0-1e-12<=diff<=ae+1e-12,1)
    beta=math.degrees(math.acos(np.clip(np.dot(-er,geff)/np.linalg.norm(geff),-1,1)))
    check(f'rotation.lat{lat}.tilt_below_point1degree',beta<.101,1)

RSsun=2*G*MS/c**2;sunrho=MS/(4*math.pi*(6.96e8)**3/3)
check('text.Sun_average_density',sunrho,1410,atol=5)
check('text.Sun_surfaceC',5800-273.15,5500,atol=50)
check('text.Sun_surfaceF',(5800-273.15)*1.8+32,10000,atol=50)
check('text.Sun_coreF',(1.5e7-273.15)*1.8+32,2.7e7,atol=1000)
sunescape=math.sqrt(2*G*MS/6.96e8)
check('text.Sun_escape',sunescape,6.18e5,atol=500)
check('text.Michell_same_density500R_superlight_Newton',500*sunescape>c,1)
Mbh=6e30;RS=2*G*Mbh/c**2;rhobh=Mbh/(4*math.pi*RS**3/3)
check('ex13.11.Schwarzschild_radius_m',RS,8900,atol=50)
check('ex13.11.average_density',rhobh,2e18,rtol=.03)
Mgc=8.2e36;RSgc=2*G*Mgc/c**2
check('SgrA.mass_in_Suns',Mgc/MS,4.1e6,rtol=.01)
check('SgrA.RS_from_own_mass',RSgc,1.2154e10,atol=500000)
check('SgrA.displayed_RS',RSgc,1.2e10,rtol=.02)
check('selfcheck13.8.same_mass_external_acceleration',G*MS/(1.5e11)**2,G*MS/(1.5e11)**2)
tidalStar=2*G*Mbh*2/RS**3;tidalSuper=2*G*Mgc*2/RSgc**3
check('tidal.horizon_mass_scaling',tidalStar/tidalSuper,(Mgc/Mbh)**2,rtol=1e-10)

payload=dict(status='passed',count=len(records),checks=records,methods=['PDF inputs transcribed independently; no author verification code imported.','Direct angular shell-potential quadrature and independent uniform-sphere radial layering.','Cartesian orbital ODE with energy/angular momentum/swept-area checks at101samples per orbit for3eccentricities.','Numerical scalar/unit/rounding checks and7latitude vector checks.'],modelBoundary=dict(testParticleEscape='sqrt(2GM/r) assumescentralbodyfixed. In exacttwo-body relative motion the massfactorisG(M+m).',finiteMassCounterexample=dict(mOverM=1,speedRatioExactRelativeToTestParticle=math.sqrt(2))),sourceTyposConfirmed=['PDF427:Tsubstitutionprints6.67e6instead6.71e6.','PDF427:E2substitutionprintsG6.71e-11instead6.67e-11.'],notes=['Published correctedG/rinputs are consistent with the expected results.','Source may use rounded intermediate values for last-digit differences; these are identified as rounding,notphysicsfailures.'])
print(json.dumps(payload,ensure_ascii=False,indent=2))
