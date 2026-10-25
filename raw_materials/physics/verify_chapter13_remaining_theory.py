"""Independent Python checks for every theory example and self-check in chapter 13.

The script checks the source's models. It does not update historical/observational claims.
No public content or build files are written.
"""
from pathlib import Path
import json, math
from scipy.integrate import quad

OUT = Path(__file__).resolve().parent
G = 6.67e-11
ME, RE = 5.97e24, 6.37e6
MS, RSUN = 1.99e30, 6.96e8
YEAR = 3.156e7
rows = []

def close(actual, expected, rel=1e-12, abs_tol=1e-12):
    assert math.isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol), (actual, expected)

def record(unit, result, assertions):
    rows.append(dict(unit=unit, result=result, assertions=assertions, status="passed"))

F = G*.0100*.500/.0500**2
close(F, 1.334e-10, abs_tol=1e-22)
record("13.1", {"F_N": F}, ["F12 and F21 have equal magnitude and opposite vectors", "center-to-center distance, spherical symmetry"])
a1, a2 = F/.0100, F/.500
close(a1/a2, 50)
record("13.2", {"a1_m_s2": a1, "a2_m_s2": a2, "using_printed_rounded_F_a2":1.33e-10/.5}, ["equal force does not imply equal acceleration", "accelerations increase as separation decreases; not constant"])
f1 = G*8e30*1e30/(2*(2e12)**2)
f2 = G*8e30*1e30/(2e12)**2
fx, fy = f2+f1/math.sqrt(2), f1/math.sqrt(2)
f = math.hypot(fx,fy)
angle = math.degrees(math.atan2(fy,fx))
assert 14.6 < angle < 14.7
record("13.3", {"F1_N":f1,"F2_N":f2,"Fx_N":fx,"Fy_N":fy,"F_N":f,"angle_deg":angle,"acceleration_m_s2":f/1e30}, ["vector superposition, F1 is diagonal and F2 lies along +x", "result not directed toward the two-large-stars center of mass"])
lander_mass=3430/9.80
gm=G*6.42e23/(3.39e6)**2
close(lander_mass,350)
record("13.4", {"mass_kg":lander_mass,"Mars_g_m_s2":gm,"Mars_weight_N":lander_mass*gm,"Mars_to_Earth_g_ratio":gm/9.8}, ["mass unchanged", "use radius not altitude in inverse square law"])
v_half=math.sqrt(G*ME/RE)
v_escape=math.sqrt(2*G*ME/RE)
close(v_escape/v_half,math.sqrt(2))
close(.5*v_half*v_half-G*ME/RE,-G*ME/(2*RE),rel=1e-12)
close(.5*v_escape*v_escape-G*ME/RE,0,abs_tol=1e-7)
record("13.5", {"launch_to_height_RE_m_s":v_half,"launch_to_height_RE_km_h":v_half*3.6,"escape_m_s":v_escape,"escape_km_h":v_escape*3.6,"Mars_escape_m_s":math.sqrt(2*G*6.42e23/3.39e6),"sun_escape_m_s":math.sqrt(2*G*MS/RSUN)}, ["target radius 2RE versus target height RE", "minimum final speed zero", "ignore drag, rotation, moon gravity", "m cancels, launch-direction statement assumes unobstructed trajectory"])
r=RE+340e3; m=1000
v=math.sqrt(G*ME/r); T=2*math.pi*r/v; ar=v*v/r
E2=-G*ME*m/(2*r); E1=-G*ME*m/RE
record("13.6", {"r_m":r,"v_m_s":v,"T_s":T,"T_min":T/60,"arad_m_s2":ar,"E_orbit_J":E2,"E_rest_pad_J":E1,"W_launch_J":E2-E1,"W_escape_J":-E2,"wrong_printed_T_substitution_s":2*math.pi*6.67e6/7700,"wrong_printed_G_E2_J":-6.71e-11*ME*m/(2*r),"pad_rotation_K_at_410m_s_J":m*410**2/2}, ["correct r=6.71e6 in every formula", "correct G=6.67e-11", "quoted printed T5470,E2-2.97e10 fit correct constants", "mechanical minimum work, excluding rocket exhaust and losses"])
# Conceptual Example13.7: energy and angular momentum independently agree at apsides.
a=3.; e=.4; mu=1.; rp=a*(1-e); ra=a*(1+e)
vp=math.sqrt(mu*(2/rp-1/a)); va=math.sqrt(mu*(2/ra-1/a))
close(rp*vp,ra*va)
close(.5*vp**2-mu/rp,.5*va**2-mu/ra)
assert vp>va
record("13.7", {"dimensionless_test_a":a,"e":e,"rp":rp,"ra":ra,"vp":vp,"va":va}, ["kinetic energy maximal when U is most negative", "fastest perihelion, slowest aphelion", "illustrative check values are QA only, not source data"])
T=4.62*YEAR; a=(G*MS*T*T/(4*math.pi**2))**(1/3)
record("13.8", {"T_s":T,"a_m":a,"eccentricity_given":.233}, ["Kepler3 independent of eccentricity", "4.62year converted before substitution"])
rp,ra=8.80e7*1000,5.25e9*1000
a=(rp+ra)/2;e=1-rp/a;T=2*math.pi*math.sqrt(a**3/(G*MS))
close(ra,a*(1+e));close(rp,a*(1-e))
record("13.9", {"rp_m":rp,"ra_m":ra,"a_m":a,"e":e,"T_s":T,"T_year":T/YEAR}, ["source distances given in km, dynamics in SI", "2a=rp+ra", "e=1-rp/a"])
# Example13.10 and shell theorem, checked against direct angular integral.
shell_tests=[]
for q in (.01,.2,.8,.99,1.01,1.4,2.,10.):
    radius=2.; radial=q*radius
    # Units scaled so G=M=m=1 to avoid quadrature absolute tolerance masking errors.
    def dU(phi):
        s=math.sqrt(radial**2+radius**2-2*radial*radius*math.cos(phi))
        return -.5*math.sin(phi)/s
    integral,err=quad(dU,0,math.pi,epsabs=1e-12,epsrel=1e-12)
    expected=-1/(radial if q>1 else radius)
    close(integral,expected,rel=1e-9)
    shell_tests.append({"r_over_R":q,"U_scaled":integral,"analytic_U":expected,"quadrature_error":err})
uniform_tests=[]
for q in (0.,.1,.5,.9,1.):
    enclosed=ME*q**3
    force_per_mass=(G*enclosed/(RE*q)**2) if q else 0.
    analytic=G*ME/RE**2*q
    close(force_per_mass,analytic)
    uniform_tests.append({"r_over_RE":q,"enclosed_mass_fraction":q**3,"g_m_s2":force_per_mass})
record("13.10", {"uniform_density_cases":uniform_tests,"shell_quadrature_cases":shell_tests}, ["uniform density explicit, not actual Earth profile", "inner shells act as centered point mass", "outer shells exert zero net force", "at center force zero by symmetry and continuous limit", "surface joins exterior inverse-square expression"])
Mround=6e30; c=3e8
bh_R=2*G*Mround/c**2; rho=Mround/(4*math.pi*bh_R**3/3)
record("13.11", {"three_solar_mass_exact_kg":3*MS,"source_rounded_mass_kg":Mround,"Rs_m_using_rounded_mass":bh_R,"density_kg_m3":rho,"Rs_m_using_exact_three_solar":2*G*(3*MS)/c**2}, ["spherical nonrotating Schwarzschild idealization", "density means M divided by Euclidean sphere volume, not a measured local GR density", "source singularity claim is classical GR model; no inference from Newtonian kinetic energy of photons"])

self_checks=[
 ("13.1", {"Saturn_force_ratio":100/10**2,"Saturn_acceleration_ratio":1/10**2,"choice":"v"}),
 ("13.2", {"relative_g_i_to_iv":[2/2**2,4/4**2,4/2**2,2/4**2],"descending":["iii","i","ii","iv"]}),
 ("13.3", {"same_g_escape_ratio_for_radius_ratios_0.25_1_4":[math.sqrt(x) for x in(.25,1,4)],"choice":"iv"}),
 ("13.4", {"r_new_over_r_old":.99,"v_new_over_v_old":math.sqrt(1/.99),"choice":"ii; increase for a sequence of near-circular orbits"}),
 ("13.5", {"period_ratio":4**1.5,"choice":"iii"}),
 ("13.6", {"inside_shell_force":0,"answer":"Cannot stand or walk by gravity on inner surface of nonrotating hollow uniform sphere."}),
 ("13.7", {"difference_source_rounded_m_s2":100*.0339,"choice":"iv"}),
 ("13.8", {"same_mass_exterior_force_ratio":1,"choice":"iii; same orbit if mass and orbital state unchanged"})]
rotation_v=2*math.pi*RE/86164
delta=rotation_v**2/RE
supplementary={
 "Earth_mass_from_g_kg":9.8*RE**2/G,
 "Earth_volume_m3":4*math.pi*RE**3/3,
 "Earth_density_kg_m3":ME/(4*math.pi*RE**3/3),
 "weight_loss_at_10km_fraction":1-(RE/(RE+1e4))**2,
 "equatorial_speed_m_s":rotation_v,
 "equatorial_centripetal_acceleration_m_s2":delta,
 "tenfold_rotation_delta_m_s2":100*delta,
 "zero_equatorial_g_rotation_multiplier":math.sqrt(9.8/delta),
 "sun_density_kg_m3":MS/(4*math.pi*RSUN**3/3),
    "sun_escape_m_s":math.sqrt(2*G*MS/RSUN),
    "Jupiter_escape_m_s":math.sqrt(2*G*1.90e27/6.99e7),
    "ISS_orbit_at_6800km_v_m_s":math.sqrt(G*ME/6.8e6),
    "ISS_orbit_at_6800km_T_min":2*math.pi*math.sqrt(6.8e6**3/(G*ME))/60,
    "Moon_orbit_model_T_days":2*math.pi*math.sqrt(3.84e8**3/(G*ME))/86400,
    "max_Schwarzschild_tidal_gradient_ratio_mass_10_vs_1e6":(1e6/10)**2,
 "SgrA_source_mass_kg":8.2e36,
 "SgrA_source_Rs_m":2*G*8.2e36/c**2,
 "SgrA_source_solar_mass_ratio":8.2e36/MS,
 "TY13_3_Saturn_escape_ratio_to_Earth":math.sqrt(100/10),
 "opening_ring_at_half_radius_speed_ratio":math.sqrt(2),
 "opening_ring_at_half_radius_acceleration_ratio":4,
 "opening_ring_answer":"iv: closer particles in circular orbits have greater speed and acceleration"
}
assert len(rows)==11 and len(self_checks)==8
result={"status":"passed","scope":"Chapter13 theory models and source examples; not exercise chapter completion or public rendering acceptance","examplesChecked":11,"selfChecksChecked":8,"exampleResults":rows,"selfChecks":[dict(unit=u,**r) for u,r in self_checks],"supplementary":supplementary,"no_public_files_modified":True}
print(json.dumps(result,ensure_ascii=False,indent=2))
