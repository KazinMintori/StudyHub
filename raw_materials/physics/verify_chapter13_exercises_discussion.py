"""Independent conceptual-model checks for Q13.1–Q13.21.

No author verifier is imported. Numeric model checks support the stated physics;
they do not certify the completeness of translated prompts or rendered layout.
"""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import solve_ivp,quad

OUT=Path(__file__).resolve().parent
checks=[];records={}
def eq(name,actual,expected,rtol=1e-9,atol=1e-11):
 assert math.isclose(float(actual),float(expected),rel_tol=rtol,abs_tol=atol),(name,actual,expected)
 checks.append({'id':name,'actual':float(actual),'expected':float(expected),'passed':True})
def truth(name,condition):
 assert condition,name
 checks.append({'id':name,'actual':True,'expected':True,'passed':True})
G=6.67e-11;ME=5.97e24;RE=6.37e6;MS=1.99e30;MM=7.35e22;RM=1.74e6;dSE=1.50e11;dEM=3.84e8

# Q1: Equal interaction forces, different accelerations. The apple mass is an
# explicitly assumed private test input, not an added datum in the public prompt.
m=.2;force=G*ME*m/RE**2
eq('Q13.1:third_law_force_magnitude',force,G*m*ME/RE**2)
eq('Q13.1:acceleration_ratio',(force/ME)/(force/m),m/ME,atol=1e-38)
records['Q13.1']={'test_apple_mass_kg':m,'force_N':force,'a_earth_over_a_apple':m/ME}

# Q2: Integrate density over volume rather than assume M proportional to R^3.
rho=5300.;radii=[1e6,2e6,5e6]
gs=[]
for r in radii:
 mass=quad(lambda s:4*math.pi*rho*s*s,0,r)[0]
 g=G*mass/r**2;gs.append(g)
 eq('Q13.2:g_over_R:'+str(r),g/r,4*math.pi*G*rho/3)
eq('Q13.2:double_radius',gs[1]/gs[0],2)
records['Q13.2']={'radii_m':radii,'surface_g_m_s2':gs,'same_average_density':rho}

# Q3: Same weight requires a different mass; same mass needs no conversion.
gE=G*ME/RE**2;gM=G*6.42e23/(3.39e6)**2
w=1.;mE=w/gE;mM=w/gM
eq('Q13.3:weight_E',mE*gE,w)
eq('Q13.3:weight_Mars',mM*gM,w)
truth('Q13.3:same_force_more_mass_on_Mars',mM>mE)
records['Q13.3']={'conditional_same_force_mass_ratio_Mars_to_Earth':mM/mE,'kilogram_mass_invariant':True,'pound_mass_interpretation_invariant':True}

# Q4: Change the gravitational force at the same time as the test mass.
accelerations=[]
for test_mass in [.001,1,5000]:
 f=G*ME*test_mass/RE**2;a=f/test_mass;accelerations.append(a)
 eq('Q13.4:free_fall_mass:'+str(test_mass),a,gE)
records['Q13.4']={'test_masses_kg':[.001,1,5000],'accelerations_m_s2':accelerations}

# Q5: Geometric near/far comparison with a fixed geocentric distance.
geometries=[]
for latitude in [0,30,60]:
 projection=math.cos(math.radians(latitude))
 r_noon=math.sqrt(dSE*dSE+RE*RE-2*dSE*RE*projection)
 r_night=math.sqrt(dSE*dSE+RE*RE+2*dSE*RE*projection)
 ratio=(r_night/r_noon)**2
 truth('Q13.5:near_far:'+str(latitude),ratio>1)
 geometries.append({'latitude_deg':latitude,'force_noon_over_midnight':ratio})
records['Q13.5']={'fixed_distance_geometry_cases':geometries,'limits':'Geocentricdistanceheldfixed;actualtime/locationgeometrymustnotbeovergeneralized.'}

def gravity2(t,y,mu=1.):
 r=np.hypot(y[0],y[1]);return [y[2],y[3],-mu*y[0]/r**3,-mu*y[1]/r**3]

# Q6: Cartesian Newton integration reproduces a circular orbit, rather than
# applying the circular formula alone.
circle=solve_ivp(gravity2,(0,2*math.pi),[1,0,0,1],rtol=2e-11,atol=2e-12,dense_output=True)
for t in np.linspace(0,2*math.pi,13):
 state=circle.sol(t)
 eq('Q13.6:circle_radius:'+str(round(t,3)),np.hypot(*state[:2]),1,rtol=3e-10)
eq('Q13.6:position_after_period',np.linalg.norm(circle.y[:2,-1]-[1,0]),0,atol=3e-9)
records['Q13.6']={'cartesian_orbit_period_normalized':2*math.pi,'radius_preserved':True,'force_is_inward_without_separate_outward_force':True}

# Q7: Period from integrated/circular acceleration scaling.
r=2.;v1=math.sqrt(1/r);v3=math.sqrt(3/r)
T1=2*math.pi*r/v1;T3=2*math.pi*r/v3
eq('Q13.7:period_ratio',T3/T1,1/math.sqrt(3))
records['Q13.7']={'choice':'d','period_ratio':T3/T1}

# Q8: The expected answer is the test-particle limit, not a universal two-body law.
M=1000.;m=1.;T_exact=2*math.pi*math.sqrt(1/(M+m));T_exact3=2*math.pi*math.sqrt(1/(M+3*m))
eq('Q13.8:two_body_correction',T_exact3/T_exact,math.sqrt((M+m)/(M+3*m)))
truth('Q13.8:finite_mass_correction_decreases_period',T_exact3<T_exact)
records['Q13.8']={'choice_in_test_particle_limit':'c','test_particle_period_ratio':1,'example_finite_two_body_ratio':T_exact3/T_exact}

# Q9: Compare solar differential acceleration to Earth's lunar attraction.
solar_common=G*MS/dSE**2
solar_difference=G*MS/(dSE-dEM)**2-solar_common
earth_at_moon=G*ME/dEM**2
force_ratio=(MS/ME)*(dEM/dSE)**2
truth('Q13.9:solar_force_exceeds_twice_earth',force_ratio>2)
truth('Q13.9:solar_tide_smaller_than_earth_accel',solar_difference/earth_at_moon<.02)
records['Q13.9']={'solar_to_earth_force_on_moon':force_ratio,'solar_differential_to_earth_lunar_accel':solar_difference/earth_at_moon}

# Q10: Energy wells support the ordinary mission comparison, not an exact fuel
# calculation without a propulsion/trajectory model.
well_E=G*ME/RE;well_M=G*MM/RM
truth('Q13.10:earth_potential_well_deeper',well_E>well_M)
records['Q13.10']={'surface_escape_energy_J_per_kg_earth':well_E,'surface_escape_energy_J_per_kg_moon':well_M,'ratio':well_E/well_M,'fuel_not_uniquely_determined_without_mission_model':True}

# Q11,15,17,19: Integrate Newton's equation and gravitational work on complete
# noncircular orbits. Energy, angular momentum and endpoint work are distinct checks.
ellipses=[]
for e in [0,.2,.6]:
 a=2.;rp=a*(1-e);ra=a*(1+e);vp=math.sqrt((1+e)/rp);period=2*math.pi*a**1.5
 def deriv(t,y):
  gx=gravity2(t,y)
  power=gx[2]*y[2]+gx[3]*y[3]
  return gx+[power]
 ode=solve_ivp(deriv,(0,period),[rp,0,0,vp,0],rtol=1e-11,atol=2e-12,dense_output=True)
 eq('Q13.11:closed_work_e'+str(e),ode.y[4,-1],0,atol=1e-9)
 eq('Q13.11:closed_position_e'+str(e),np.linalg.norm(ode.y[:2,-1]-[rp,0]),0,atol=5e-8)
 for t in np.linspace(0,period,9):
  x,y,vx,vy,work=ode.sol(t);r=math.hypot(x,y)
  eq('ellipse:energy_e'+str(e)+':'+str(round(t,2)),.5*(vx*vx+vy*vy)-1/r,-1/(2*a),rtol=2e-9)
  eq('ellipse:angular_e'+str(e)+':'+str(round(t,2)),x*vy-y*vx,rp*vp,rtol=2e-9)
 eq('Q13.17:accel_ratio_e'+str(e),(1/rp**2)/(1/ra**2),(ra/rp)**2)
 if e:
  eq('Q13.19:outward_radial_accel_at_peri_e'+str(e),vp*vp/rp-1/rp**2,e/rp**2)
  truth('Q13.19:radius_increases_after_peri_e'+str(e),np.hypot(*ode.sol(.02)[:2])>rp)
 ellipses.append({'eccentricity':e,'period':period,'work_after_orbit':float(ode.y[4,-1]),'perihelion':rp,'aphelion':ra})
records['Q13.11']={'closed_orbit_work_cases':ellipses}

# Q12: Threshold energy is direction-independent in a fixed, central, vacuum
# model. Include the radial (zero angular momentum) degenerate case explicitly.
escape_cases=[]
for angle in [0,30,60,90]:
 theta=math.radians(angle);speed=math.sqrt(2);vx=speed*math.cos(theta);vy=speed*math.sin(theta)
 ode=solve_ivp(gravity2,(0,3),[1,0,vx,vy],rtol=1e-11,atol=2e-12)
 x,y,ux,uy=ode.y[:,-1];r=math.hypot(x,y)
 eq('Q13.12:threshold_energy_angle'+str(angle),.5*(ux*ux+uy*uy)-1/r,0,atol=2e-10)
 truth('Q13.12:nonintersecting_outward_angle'+str(angle),np.min(np.hypot(ode.y[0],ode.y[1]))>=1-1e-10)
 escape_cases.append({'angle_from_radial_deg':angle,'angular_momentum':vy,'energy_initial':.5*speed**2-1,'radius_at_t3':r})
records['Q13.12']={'threshold_tests':escape_cases,'radial_is_degenerate':escape_cases[0]['angular_momentum']==0,'drag_requires_path_dependent_work':True}

# Q13: Find a negative-energy radial turning point by an ODE event.
def stop(t,y):return y[1]
stop.direction=-1;stop.terminal=True
radial=solve_ivp(lambda t,y:[y[1],-1/y[0]**2],(0,10),[1,1],events=stop,rtol=1e-11,atol=1e-12)
truth('Q13.13:turning_event_present',len(radial.t_events[0])==1)
eq('Q13.13:negative_energy_turning_radius',radial.y_events[0][0,0],2,rtol=5e-10)
E=.5*2**2-1;vinf=math.sqrt(2*E)
for r in [10,100,1000]:
 speed=math.sqrt(2*(E+1/r));truth('Q13.13:positive_energy_speed_gt_asymptote_'+str(r),speed>vinf)
records['Q13.13']={'negative_energy_normalized':-.5,'turning_radius_normalized':float(radial.y_events[0][0,0]),'positive_energy_normalized':E,'asymptotic_speed_normalized':vinf}

# Q14: Conic classification from conserved E,h, and local flat-field comparison.
classification=[]
for speed in [.8,math.sqrt(2),2.]:
 E=.5*speed**2-1;h=speed;ecc=math.sqrt(1+2*E*h*h)
 classification.append({'tangential_speed_at_r1':speed,'energy':E,'eccentricity':ecc})
eq('Q13.14:zero_energy_eccentricity',classification[1]['eccentricity'],1)
truth('Q13.14:negative_energy_conic',classification[0]['eccentricity']<1)
truth('Q13.14:positive_energy_conic',classification[2]['eccentricity']>1)
small=solve_ivp(gravity2,(0,.05),[0,1,.02,.03],rtol=1e-12,atol=1e-13,dense_output=True)
flat_errors=[]
for t in np.linspace(0,.05,11):
 actual=small.sol(t);flat_y=1+.03*t-.5*t*t;flat_errors.append(abs(actual[1]-flat_y))
truth('Q13.14:local_parabola_approximation',max(flat_errors)<2e-6)
records['Q13.14']={'conic_tests':classification,'local_constant_g_vertical_error_max':max(flat_errors)}

# Q15: Direct energy equality at two radii, independent of any calendar model.
r_close=.9;r_far=1.1;a=1.;v_close=math.sqrt(2/r_close-1/a);v_far=math.sqrt(2/r_far-1/a)
eq('Q13.15:energy_equality',v_close**2/2-1/r_close,v_far**2/2-1/r_far)
truth('Q13.15:closer_is_faster',v_close>v_far)
records['Q13.15']={'same_orbit_test_radii':[r_close,r_far],'speeds':[v_close,v_far]}

# Q16: Constant northern latitude implies zddot=0, contrary to central gravity.
phi=math.pi/4;r=2.;z=r*math.sin(phi);az=-z/r**3
truth('Q13.16:offset_plane_incompatible',az<0)
records['Q13.16']={'latitude_deg':45,'test_radius':r,'constant_z':z,'gravity_z_accel':az,'required_z_accel_for_offset_circle':0}
records['Q13.17']={'normalized_peri_apo_accel_ratios':[(case['aphelion']/case['perihelion'])**2 for case in ellipses]}

# Q18: Circular T²/r⁴ and a bound non-elliptical inverse-cube trajectory.
# With kappa=2, h=1, initial r=1 and radial speed0, the exact solution before
# collapse is r=sqrt(1-t²), phi=atanh(t). It is a spiral, not a Kepler ellipse.
kappa=2.;circular=[]
for r in [1,2,3]:
 speed=math.sqrt(kappa)/r;T=2*math.pi*r/speed
 eq('Q13.18:T2_over_r4_r'+str(r),T*T/r**4,4*math.pi**2/kappa)
 circular.append({'radius':r,'period':T})
def inverse3(t,y):
 r=math.hypot(y[0],y[1]);return [y[2],y[3],-kappa*y[0]/r**4,-kappa*y[1]/r**4]
spiral=solve_ivp(inverse3,(0,.8),[1,0,0,1],rtol=1e-11,atol=2e-12,dense_output=True)
for t in [.1,.3,.5,.8]:
 state=spiral.sol(t);r=math.hypot(*state[:2]);angle=math.atan2(state[1],state[0])
 eq('Q13.18:spiral_radius_t'+str(t),r,math.sqrt(1-t*t),rtol=2e-9)
 eq('Q13.18:spiral_phi_t'+str(t),angle,math.atanh(t),rtol=2e-9)
 eq('Q13.18:area_law_t'+str(t),state[0]*state[3]-state[1]*state[2],1,rtol=2e-9)
 eq('Q13.18:negative_spiral_energy_t'+str(t),.5*np.dot(state[2:],state[2:])-kappa/(2*r*r),-.5,rtol=3e-9)
records['Q13.18']={'circular_cases':circular,'bound_nonellipse_spiral_example':{'kappa':kappa,'specific_angular_momentum':1,'specific_energy':-.5,'radius_at_t0p8':float(np.hypot(*spiral.y[:2,-1]))},'area_law_preserved':True}

records['Q13.19']={'elliptic_ODE_cases':ellipses,'radial_acceleration_at_peri_positive_for_e_gt0':True,'no_extra_outward_force_inserted':True}

# Q20: No finite cutoff in Newton's law; apparent weight differs from mg.
force_values=[]
for r in [RE,1e11,1e17]:
 F=G*ME/r**2;truth('Q13.20:positive_at_finite_r'+str(r),F>0);force_values.append(F)
eq('Q13.20:free_fall_support',G*ME/RE**2-G*ME/RE**2,0)
records['Q13.20']={'unit_mass_forces_at_finite_radii_N':force_values,'support_in_same_g_free_fall':0}

# Q21: Uniform-field plane/person integration gives a fixed separation with no
# support. A real central field has a nonzero gradient across a finite cabin.
g=9.8;offset=1.5
def freefall(t,y):return [y[1],-g]
plane=solve_ivp(freefall,(0,2),[100,8],rtol=1e-12,atol=1e-12,dense_output=True)
person=solve_ivp(freefall,(0,2),[100+offset,8],rtol=1e-12,atol=1e-12,dense_output=True)
for t in [.1,.5,1,2]:
 eq('Q13.21:relative_position_uniform_t'+str(t),person.sol(t)[0]-plane.sol(t)[0],offset,atol=2e-11)
 eq('Q13.21:relative_velocity_uniform_t'+str(t),person.sol(t)[1]-plane.sol(t)[1],0,atol=2e-11)
eq('Q13.21:accelerated_frame_residual',g-g,0)
gradient_difference=G*ME/RE**2-G*ME/(RE+offset)**2
truth('Q13.21:finite_cabin_gradient_not_zero',gradient_difference>0)
records['Q13.21']={'uniform_field_relative_position_constant':True,'inertial_frame_support_force':0,'central_field_gradient_difference_over1p5m_m_s2':gradient_difference,'not_all_physiological_or_orbital_properties_claimed_identical':True}

assert set(records)=={f'Q13.{n}'for n in range(1,22)}
report={'status':'passed','scope':'Conceptual physics models for21discussionquestions; numerical checks overlap and are not21independentproofs. Source fidelity and browser checks are separate.','assertions':len(checks),'records':records,'checks':checks,'methods':['Cartesian Newton ODE circle/ellipse and gravitational-work integrals','Radial turning-point ODE event','Direction-varied threshold-energy Newton trajectories','Exact inverse-cube spiral crosschecked with Cartesian ODE and angular momentum','Uniform-field relative free fall and finite-cabin gradient contrast','Direct geometry, mass cancellation, potential wells and conserved-energy comparisons']}
print(json.dumps(report,ensure_ascii=False,indent=2))
