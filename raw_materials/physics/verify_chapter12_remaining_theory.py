"""Independent Chapter 12 source arithmetic and algebra, private QA only."""
from pathlib import Path
import json
import math
from fractions import Fraction as Frac

OUT = Path(__file__).resolve().parent
results = []
def check(key, pages, actual, expected, tolerance=1e-10, note=''):
    actual, expected = float(actual), float(expected)
    passed = abs(actual-expected) <= tolerance
    results.append(dict(id=key, pdfPages=pages, computed=actual, expected=expected, tolerance=tolerance, passed=passed, note=note))
    if not passed:
        raise AssertionError(results[-1])

g = 9.8
lbf_N = 4.4482216152605
psi_Pa = 6894.757293168
atm_Pa = 101325
check('units.g_per_cm3_to_kg_per_m3',[387],1e-3/1e-6,1000)
check('units.bar_Pa',[388],1e5,100000)
check('units.millibar_Pa',[388],1e5/1000,100)
check('units.atm_psi',[388],atm_Pa/psi_Pa,14.70,0.005)
check('units.atm_bar',[388],atm_Pa/1e5,1.013,0.0005)
check('density.aluminum_specific_gravity',[387],2700/1000,2.7)
V=4.0*5.0*3.0
check('example12.1.room_volume_m3',[387],V,60)
check('example12.1.air_mass_kg',[387],1.2*V,72)
check('example12.1.air_weight_N',[387],1.2*V*g,700,10,'Unrounded value is 705.6 N; source reports 700 N to two significant figures.')
check('example12.1.air_weight_lbf',[387],1.2*V*g/lbf_N,160,5)
check('example12.1.water_mass_kg',[387],1000*V,60000)
check('example12.1.water_weight_N',[387],1000*V*g,590000,5000)
check('example12.1.water_weight_lbf',[387],1000*V*g/lbf_N,130000,5000)
check('example12.1.water_weight_short_ton',[387],1000*V*g/lbf_N/2000,66,0.5,'Source tons are US short tons, not metric tonnes.')
for i,(m,vol,expected) in enumerate([(4,.0016,2500),(8,.0016,5000),(8,.0032,2500),(2560,.640,4000),(2560,1.28,2000)],1):
    check(f'selfcheck12.1.object{i}_rho',[388],m/vol,expected,1e-8)
check('example12.2.floor_area_m2',[389],4*5,20)
F=1.013e5*20
check('example12.2.normal_force_N',[389],F,2.0e6,50000)
check('example12.2.normal_force_lbf',[389],F/lbf_N,4.6e5,5000)
check('example12.2.normal_force_short_ton',[389],F/lbf_N/2000,230,5)
check('text.air_floor_ceiling_pressure_Pa',[390],1.2*g*3,35,0.5)
check('text.air_floor_ceiling_pressure_atm',[390],1.2*g*3/atm_Pa,.00035,.000005)
check('text.tire_32psi_gauge_kPa',[390],32*psi_Pa/1000,220,5)
check('text.tire_absolute_psi',[390],32+14.7,47,.5)
check('text.tire_absolute_kPa',[390],32*psi_Pa/1000+atm_Pa/1000,320,5)
gauge=1000*9.8*12
absolute=1.01e5+gauge
check('example12.3.gauge_Pa',[391],gauge,1.18e5,500)
check('example12.3.absolute_Pa',[391],absolute,2.19e5,500)
check('example12.3.absolute_atm',[391],absolute/atm_Pa,2.16,.005)
check('example12.3.gauge_atm',[391],gauge/atm_Pa,1.16,.005)
check('example12.3.absolute_psi_from_displayed_Pa',[391],2.19e5/psi_Pa,31.8,.05,'The printed psi conversion uses the already rounded pressure 2.19e5 Pa. Unrounded 218600 Pa is 31.705 psi.')
check('example12.3.gauge_psi',[391],gauge/psi_Pa,17.1,.05)
check('example12.4.oil_to_water_height_ratio',[392],1000/850,20/17)
statue_V=15/19300
Bsw=1030*statue_V*g
Bair=1.2*statue_V*g
check('example12.5.statue_volume_m3',[394],statue_V,7.77e-4,5e-7)
check('example12.5.statue_weight_N',[394],15*g,147)
check('example12.5.buoyancy_seawater_N_full_precision',[394],Bsw,7.845077720207254,1e-12)
check('example12.5.buoyancy_seawater_N_source_rounded_volume',[394],1030*7.77e-4*g,7.84,.005,'The source substitutes its rounded volume 7.77e-4 m3. Full-precision volume gives 7.84507772 N, which rounds to 7.85 N at three significant figures.')
check('example12.5.tension_seawater_N',[394],15*g-Bsw,139,.5)
check('example12.5.buoyancy_air_N',[394],Bair,.0091,.00005)
check('example12.5.tension_air_N',[394],15*g-Bair,147,.5)
check('selfcheck12.3.scale_increase_N',[395],1030*7.77e-4*g,7.84,.005,'The answer reuses the example displayed buoyancy 7.84 N.')
for r in [.25,.5,1,2,10]:
    check(f'identity.sphere_surface_to_volume.r{r}',[395],4*math.pi*r**2/((4/3)*math.pi*r**3),3/r)
check('text.pipe_2cm_to_1cm_speed_ratio',[397],(2/1)**2,4)
Q=9.5e-3
v1=Q/(math.pi*.04**2)
v2=Q/(math.pi*.02**2)
check('example12.6.Q_m3_per_s',[397],Q,.0095)
check('example12.6.v1_m_per_s',[397],v1,1.9,.05)
check('example12.6.mass_flow_kg_per_s',[397],850*Q,8.1,.05)
check('example12.6.v2_m_per_s',[397],v2,7.6,.05)
check('example12.6.speed_ratio',[397],v2/v1,4)
check('selfcheck12.4.incompressible_required_speed_ratio',[398],3/1,3)
v_home1=1.5
v_home2=(2/1)**2*v_home1
dp_speed=.5*1000*(v_home2**2-v_home1**2)
dp_height=1000*g*5
p_home2=4e5-dp_speed-dp_height
check('example12.7.v2_m_per_s',[400],v_home2,6)
check('example12.7.speed_pressure_loss_Pa',[400],dp_speed,16875)
check('example12.7.height_pressure_loss_Pa',[400],dp_height,49000)
check('example12.7.p2_Pa',[400],p_home2,3.3e5,5000)
check('example12.7.p2_atm',[400],p_home2/atm_Pa,3.3,.05)
check('example12.7.p2_psi',[400],p_home2/psi_Pa,48,.5)
check('example12.7.Q_m3_per_s',[400],math.pi*.005**2*v_home2,4.7e-4,.05e-4)
check('example12.7.Q_L_per_s',[400],math.pi*.005**2*v_home2*1000,.47,.005)
check('example12.7.water_off_p2_Pa',[400],4e5-dp_height,3.5e5,5000)

# Exact rational substitutions check the stated identities on a grid. These are
# verification cases, not a claim of a computer-algebra proof.
for j,(rho,gg,h,A1,A2,vv1,p1,y1,y2,dv) in enumerate([
    (1000,Frac(49,5),3,4,1,2,200000,0,5,Frac(1,10)),
    (850,Frac(49,5),2,9,4,3,150000,-2,4,Frac(1,100)),
    (Frac(6,5),Frac(49,5),1,10,3,5,101325,3,7,Frac(1,2)),
    (13600,Frac(981,100),Frac(1,100),8,3,Frac(1,5),300000,-1,2,Frac(1,1000)),
],1):
    rho,gg,h,A1,A2,vv1,p1,y1,y2,dv=map(Frac,(rho,gg,h,A1,A2,vv1,p1,y1,y2,dv))
    patm=Frac(101325); p0=patm+Frac(10000); vv2=A1/A2*vv1
    check(f'identity12.4.hydrostatic_force_balance.case{j}',[389],p1*A1-(p1-rho*gg*h)*A1-rho*gg*A1*h,0)
    check(f'identity12.7.hydraulic_force_ratio.case{j}',[390],((A2/A1)*p1*A1)/A2-p1,0)
    p_man=patm+rho*gg*(y2-y1)
    check(f'identity12.8.manometer.case{j}',[391],p_man+rho*gg*y1-patm-rho*gg*y2,0)
    p2=p1-rho*(vv2**2-vv1**2)/2-rho*gg*(y2-y1)
    W=(p1-p2)*dv
    dK=rho*dv*(vv2**2-vv1**2)/2
    dU=rho*dv*gg*(y2-y1)
    check(f'identity12.16.energy_per_volume.case{j}',[399],(W-dK-dU)/dv,0)
    check(f'identity12.17.bernoulli.case{j}',[399],p1+rho*gg*y1+rho*vv1**2/2-p2-rho*gg*y2-rho*vv2**2/2,0)
    p2_static=p1-rho*gg*(y2-y1)
    check(f'identity12.17.static_limit.case{j}',[399],p1+rho*gg*y1-p2_static-rho*gg*y2,0)
    vout2=2*(p0-patm)/rho+2*gg*h
    check(f'example12.8.bernoulli_efflux.case{j}',[400,401],p0+rho*gg*h-patm-rho*vout2/2,0)
    torricelli_v2=2*gg*h
    check(f'example12.8.torricelli.case{j}',[401],patm+rho*gg*h-patm-rho*torricelli_v2/2,0)
    venturi_v1_sq=2*gg*h/((A1/A2)**2-1)
    check(f'example12.9.venturi.case{j}',[401],rho*venturi_v1_sq*((A1/A2)**2-1)/2-rho*gg*h,0)
    check(f'continuity12.12.mass_conservation.case{j}',[397],rho*A1*vv1-rho*A2*vv2,0)
check('viscosity.radius_halved_pressure_ratio',[403],(1/.5)**4,16)
check('viscosity.radius_0_90_pressure_ratio',[403],(1/.9)**4,1.52,.005)
check('viscosity.radius_0_90_pressure_increase_percent',[403],((1/.9)**4-1)*100,52,.5)
check('example12.11.approx_75mph_to_m_per_s',[404],75*1609.344/3600,33.528,1e-10,'Source says near 35 m/s or 75 mi/h. This is a coarse approximation; exact 35 m/s is 78.29 mi/h. Preserve SI value or flag the loose conversion.')
check('figure12.31.strobe_rotation_rev_per_s',[404],1000/8,125)
check('figure12.31.strobe_rotation_rpm',[404],1000/8*60,7500)
check('selfcheck12.6.needle_pressure_ratio',[404],(.60/.30)**4,16)

qualitative = [
 dict(id='opening',pdfPages=[386,393],result='Choice v: Larger average density m/V explains why the manta ray must sustain upward force. A swim bladder lowers average density of the fish.'),
 dict(id='selfcheck12.1',pdfPages=[388],result='ii > iv > i = iii > v'),
 dict(id='selfcheck12.2',pdfPages=[393],result='ii: Warmer mercury has lower density; at unchanged h and g, p_atm = rho*g*h decreases.'),
 dict(id='selfcheck12.3',pdfPages=[395],result='i: The scale reading increases by 7.84 N; the statue exerts the equal downward reaction to its buoyant force on the water.'),
 dict(id='selfcheck12.4',pdfPages=[398],result='ii: Traffic behaves as a compressible analogue. Actual car spacing and throughput change; incompressible narrowing to one-third area would require triple speed.'),
 dict(id='selfcheck12.5',pdfPages=[402],result='ii: The pressure difference produces the net force that accelerates the fluid. This is the causal Newton-law explanation.'),
 dict(id='selfcheck12.6',pdfPages=[404],result='iv: 16 times the pressure difference at equal length and volume flow rate.')
]
payload = dict(status='pass',checks=results,checkCount=len(results),qualitativeChecks=qualitative,
 uncertainties=[
  dict(id='example12.5.rounding',note='Source buoyancy 7.84 N uses its rounded volume 7.77e-4 m3; full-precision volume gives 7.84507772 N (7.85 N to three significant figures). Tension is 139 N in either convention. Selfcheck12.3 reuses 7.84 N.'),
  dict(id='example12.3.rounding',note='31.8 psi corresponds to converting displayed rounded 2.19e5 Pa. Avoid presenting all intermediate rounded values as simultaneous exact equalities.'),
  dict(id='example12.8.velocity_typo',note='PDF400 says y1 is essentially zero immediately after y1=h. The intended symbol is v1, the small free-surface speed, because A1 is much larger than A2. Keep y1=h and v1 approximately zero.'),
  dict(id='example12.11.speed_conversion',note='The source approximate pair 35 m/s and 75 mi/h is loose by about 4.4%. No physical conclusion depends on it.'),
  dict(id='example12.1.tons',note='66 tons and 230 tons in US customary weight conversions are US short tons, not 1000 kg metric tonnes.')
 ])
print(json.dumps(payload,ensure_ascii=False,indent=2))
