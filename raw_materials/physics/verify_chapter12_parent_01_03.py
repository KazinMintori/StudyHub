from pathlib import Path
import json,math
out=Path('qa/physics1-remaining/ch12-author-a')
r=[]
def add(id,value,expected,tol=1e-10):
 assert abs(value-expected)<=tol,(id,value,expected)
 r.append(dict(id=id,value=value,expected=expected,tolerance=tol))
g=9.8;rho_air=1.2;rho_water=1000;V=4*5*3
add('example12.1.V_m3',V,60);add('example12.1.m_air_kg',rho_air*V,72);add('example12.1.w_air_N',rho_air*V*g,705.6)
add('example12.1.m_water_kg',rho_water*V,60000);add('example12.1.w_water_N',rho_water*V*g,588000);add('example12.1.mass_ratio',rho_water/rho_air,2500/3)
add('example12.1.w_air_lbf',rho_air*V*g/4.4482216152605,160,5)
add('example12.1.w_water_short_ton_force',rho_water*V*g/4.4482216152605/2000,66,.5)
for i,(m,v,expected) in enumerate([(4,.0016,2500),(8,.0016,5000),(8,.0032,2500),(2560,.640,4000),(2560,1.28,2000)],1):add(f'selfcheck12.1.rho{i}',m/v,expected)
A=4*5;p_atm=101300;force=p_atm*A
add('example12.2.A_m2',A,20);add('example12.2.force_N',force,2026000);add('example12.2.short_ton_force',force/4.4482216152605/2000,230,5)
add('fluid.air_3m_delta_p_Pa',1.2*g*3,35.28);add('fluid.air_3m_delta_p_atm',1.2*g*3/101325,.0003481865284974094,1e-12)
add('units.g_cm3_to_kg_m3',.001/.000001,1000)
add('units.atm_psi',101325/6894.757293168,14.69594877551422,1e-10)
add('units.tire_gauge_Pa',32*6894.757293168,220632.233381376)
add('units.tire_absolute_psi',32+14.7,46.7)
add('units.tire_absolute_Pa',32*6894.757293168+101325,321957.233381376)
add('relative_density.aluminum',2700/1000,2.7)
pg=1000*g*12;pa=101000+pg
add('example12.3.gauge_Pa',pg,117600);add('example12.3.absolute_Pa',pa,218600)
add('example12.3.absolute_atm',pa/101325,2.16,.005)
add('example12.3.gauge_atm',pg/101325,1.16,.005)
add('example12.3.absolute_psi',pa/6894.757293168,31.7,.05)
add('example12.3.displayed_absolute_psi',219000/6894.757293168,31.8,.05)
add('example12.3.gauge_psi',pg/6894.757293168,17.1,.05)
add('example12.4.h_oil_over_h_water',1000/850,20/17)
for ratio in [1/2,1,2,4]:
 ho=1000/850*ratio;add(f'example12.4.pressure_balance_hwater_{ratio}',850*g*ho,1000*g*ratio,1e-10)
Vg=15/19300;Bw=1030*Vg*g;Ba=1.2*Vg*g
add('example12.5.statue_V_m3',Vg,.0007772020725388601,1e-15)
add('example12.5.weight_N',15*g,147);add('example12.5.B_seawater_N',Bw,7.845077720207254)
add('example12.5.T_seawater_N',147-Bw,139.1549222797927)
add('example12.5.B_air_N',Ba,.009139896373056996,1e-14)
add('example12.5.T_air_N',147-Ba,146.99086010362695)
add('example12.5.B_using_rounded_V_N',1030*7.77e-4*g,7.843038,1e-12)
add('selfcheck12.3.delta_reading_N',Bw,7.845077720207254)
for rad in [.001,.01,1,3]:add(f'surface_tension.S_over_V_r_{rad}',4*math.pi*rad**2/(4/3*math.pi*rad**3),3/rad,1e-10)
# Exact rational identities for the hydrostatic, manometer and hydraulic steps.
from fractions import Fraction as F
for j,(rho,h,a1,a2,p0) in enumerate([(1000,12,1,20,101000),(850,3,2,50,101325),(F(6,5),3,1,5,101325)],1):
 rho,h,a1,a2,p0=map(F,(rho,h,a1,a2,p0));gg=F(49,5)
 p_bottom=p0+rho*gg*h
 add(f'hydrostatic.force_balance_case{j}',p_bottom*a1-p0*a1-rho*gg*a1*h,0)
 F1=200;F2=F1*a2/a1;add(f'hydraulic.pressure_equality_case{j}',F1/a1-F2/a2,0)
 y1=F(2);y2=y1+h;p=p0+rho*gg*(y2-y1)
 add(f'manometer.equal_base_pressure_case{j}',p+rho*gg*y1-p0-rho*gg*y2,0)
report=dict(status='passed',checks=r,count=len(r),conceptualChecks=[dict(id='opening',answer='v',why='Average density m/V determines comparison with displaced-fluid weight.'),dict(id='selfcheck12.2',answer='ii',why='At unchangedh andg,lowermercurydensitymeansloweratmosphericpressure.'),dict(id='selfcheck12.3',answer='i',why='The statue exerts the downward reaction of the buoyant force onto the water.')])
print(json.dumps(report,ensure_ascii=False,indent=2,default=float))
