"""Independent source-transcribed calculations for the late chapter12 exercises.

Partial coverage is explicit until all12.47–12.92have been calculated.
"""
import json,math
import numpy as np
from scipy.integrate import quad
g=9.80;rho=1000.;records={}
records['12.47']={'gauge_pressure_Pa':rho*g*15.0,'assumption':'City-main speed negligible relative to tap-jet speed; no losses.'}
v=math.sqrt(2*g*14.0);area=math.pi*.006**2/4
records['12.48']={'speed_m_s':v,'volume_flow_m3_s':area*v,'volume_flow_L_s':1000*area*v}
records['12.49']={'second_speed_m_s':2.50/2,'second_gauge_pressure_Pa':1.80e4+.5*rho*(2.50**2-(2.50/2)**2)}
records['12.50']={'second_speed_m_s':3./4,'second_gauge_pressure_Pa':5e4+.5*rho*(3.**2-(3./4)**2)+rho*g*11.0}
Q=7200e-6;v1=Q/(math.pi*.04**2);v2=Q/(math.pi*.02**2)
records['12.51']={'volume_flow_m3_s':Q,'first_speed_m_s':v1,'second_speed_m_s':v2,'second_absolute_pressure_Pa':2.40e5+.5*rho*(v1*v1-v2*v2)}
records['12.52']={'pressure_ratio':(.210/.0700)**4,'new_pressure_difference_Pa':6e4*(.210/.0700)**4}
assert math.isclose(records['12.49']['second_gauge_pressure_Pa'],20343.75)
assert math.isclose(records['12.50']['second_gauge_pressure_Pa'],162018.75)
assert math.isclose(records['12.52']['pressure_ratio'],81.)
H,pg,D,d=.800,5e3,2.00,.0200
ratio=(D/d)**2;c=pg/rho
speed=math.sqrt(2*(g*H+c));open_speed=math.sqrt(2*g*H)
T=ratio*math.sqrt(2)/g*(math.sqrt(g*H+c)-math.sqrt(c))
Topen=ratio*math.sqrt(2*H/g)
assert math.isclose(T,quad(lambda y:ratio/math.sqrt(2*(g*y+c)),0,H)[0])
records['12.73']={'speed_m_s':speed,'speed_to_open_ratio':speed/open_speed,'drain_time_s':T,'open_drain_time_s':Topen,'time_to_open_ratio':T/Topen,'surface_to_hole_area_ratio':ratio}
V=4/3*math.pi*.12**3;rho_ball=.24*rho;mass=rho_ball*V
records['12.74']={'volume_m3':V,'ball_mass_kg':mass,'downward_holding_force_N':(rho-rho_ball)*g*V,'initial_upward_acceleration_m_s2':(rho/rho_ball-1)*g}
for rB,rL,rW,L in [(7800,13600,1000,.10),(700,1100,500,.20),(800,1200,600,.15)]:
 h=L*(rL-rB)/(rL-rW)
 assert 0<h<L
 assert math.isclose(rL*L**2*(L-h)+rW*L**2*h,rB*L**3)
records['12.75']={'above_volume_fraction':'1-rhoB/rhoL','water_layer_depth':'L*(rhoL-rhoB)/(rhoL-rhoW)','domain':'rhoW<=rhoB<rhoL','iron_mercury_water_depth_m':.10*(13600-7800)/(13600-1000)}
W,area,rmetal=2.5e6,60*20,7200.
rise=W/(rho*g*area);fall=W/g*(1/rho-1/rmetal)/area
records['12.76']={'rise_when_loaded_m':rise,'fall_from_loaded_state_m':fall,'level_above_original_after_sinking_m':rise-fall}
for H,h in [(3,.5),(7,3),(2,1)]:
 R=math.sqrt(2*g*h)*math.sqrt(2*(H-h)/g)
 R2=math.sqrt(2*g*(H-h))*math.sqrt(2*h/g)
 assert math.isclose(R,R2)and math.isclose(R,2*math.sqrt(h*(H-h)))
records['12.77']={'range':'2*sqrt(h*(H-h))','second_hole_height_above_bottom':'h','domain':'0<h<H'}
v=math.sqrt(2*g*.900);Q=1.20e-4*v
records['12.78']={'entry_speed_m_s':v,'volume_flow_m3_s':Q,'time_for_10L_s':.0100/Q,'correction_requires':'waterplane area and interior flooding level'}
records['12.79']={'range_ratio':(1.80/.750)**2,'new_range_m':.950*(1.80/.750)**2,'assumption':'Same feed volume flow and same nozzle height.'}
Qin,Ahole=2.40e-4,1.50e-4
h=(Qin/Ahole)**2/(2*g)
assert 0<h<.25 and math.isclose(Ahole*math.sqrt(2*g*h),Qin)
records['12.80']={'steady_depth_m':h,'hole_speed_m_s':Qin/Ahole,'outflow_at_rim_m3_s':Ahole*math.sqrt(2*g*.25)}
v3=math.sqrt(2*g*(10-2));Q=.0160*v3;v2=Q/.0480
records['12.81']={'outlet_speed_m_s':v3,'volume_flow_m3_s':Q,'point2_speed_m_s':v2,'point2_gauge_pressure_Pa':.5*rho*(v3*v3-v2*v2)}
ve=200/3.6;vr=ve*30/350;dp=.5*1.20*(ve*ve-vr*vr)
assert math.isclose(vr*350,ve*30)
records['12.82']={'rim_speed_m_s':vr,'rim_speed_km_h':vr*3.6,'rim_minus_eye_pressure_Pa':dp,'kinetic_only_height_m':ve*ve/(2*g),'other_energy_source':'Work of pressure forces, not just initial swirling kinetic energy.'}
for h1 in [.1,.4,1.0]:
 vd=math.sqrt(2*g*h1);vc=2*vd;pressure_drop=.5*rho*(vc*vc-vd*vd)
 assert math.isclose(pressure_drop/(rho*g),3*h1)
records['12.83']={'rise_above_lower_surface':'3*h1','condition':'Liquid column continuous; calculated absolute pressure nonnegative.'}
v0=1.20;y=15*v0*v0/(2*g)
for y0 in [0,.1,.4,1.5]:
 v=math.sqrt(v0*v0+2*g*y0);rr=(1+2*g*y0/v0**2)**(-.25)
 assert math.isclose(rr*rr*v,v0)
records['12.84']={'speed':'sqrt(v0^2+2*g*y)','radius':'r0*(1+2*g*y/v0^2)^(-1/4)','height_for_half_radius_m':y}
elements=['Al','Fe','Cu','Ag','Pb','Hg','Au','Pt']
atomic_mass=[26.982,55.845,63.546,107.868,207.2,200.59,196.967,195.078]
density=[2.7,7.8,8.9,10.5,11.3,13.6,19.3,21.4]
assert atomic_mass[4]>atomic_mass[5]>atomic_mass[6]>atomic_mass[7]
assert density[4]<density[5]<density[6]<density[7]
records['12.85']={'source_atomic_mass_pdf_page':1550,'elements':elements,'atomic_mass_g_mol':atomic_mass,'density_g_cm3':density,'counterexample':'Pt has smaller atomic mass but greater density than Au,Hg,Pb.'}
L=.080;h0=.030;slope=-.00072;coin_mass=.00567
rl=-coin_mass/(slope*L*L);M=rl*L*L*(L-h0)
for n in [0,5,10,15,20,25]:
 h=h0+slope*n
 assert h>0 and math.isclose(rl*L*L*(L-h),M+n*coin_mass)
records['12.86']={'source_graph_intercept_m_approx':h0,'source_graph_slope_m_per_coin_approx':slope,'quarter_mass_kg':coin_mass,'liquid_density_kg_m3_approx':rl,'block_mass_kg_approx':M,'primary_quarter_source':'https://www.usmint.gov/learn/coins-and-medals/circulating-coins/coin-specifications'}
x=np.array([.50,1,2,3,4]);R=np.array([5.4,6.5,8.2,9.7,10.9])
S,B=np.linalg.lstsq(np.column_stack([x,np.ones_like(x)]),R*R,rcond=None)[0]
drop=.500;patm=1.013e5;h=B/(4*drop);rl=4*drop*patm/(g*S)
records['12.87']={'pressure_atm':x.tolist(),'range_m':R.tolist(),'fit_slope_m2_per_atm':float(S),'fit_intercept_m2':float(B),'liquid_depth_m':float(h),'liquid_density_kg_m3':float(rl),'atm_Pa':patm,'equation':'R^2=4*drop*(h+pg/(rho*g))'}
for rho0,drop,H in [(1000,1,2),(800,2,3),(1200,.5,4)]:
 v=math.sqrt(2*g*drop);p_top=101325-rho0*g*H-rho0*v*v/2
 assert math.isclose(p_top,101325-rho0*g*(H+drop))
records['12.88']={'speed':'sqrt(2*g*h)','highest_crest':'patm/(rho*g)-h','assumption':'Ideal continuous column,zero vapor pressure bound; p_top>=0.'}
records['12.89']={'freshwater_depth_m':150*133.3/(rho*g),'choice':'b'}
A=math.pi*(1.20/2)**2;maxp=24000/A
records['12.90']={'diaphragm_area_m2':A,'maximum_pressure_difference_Pa':maxp,'maximum_pressure_difference_mmHg':maxp/133.3,'choice':'a'}
records['12.91']={'law':'F=rho_water*g*area*h','choice':'a'}
records['12.92']={'law':'h_max=F_max/(rho_water*g*area)','saltwater_depth_relation':'smaller','choice':'b'}
assert len(records)==26
print(json.dumps({'status':'partial-passed','scope':'12.47–12.52 and12.73–12.92 only;12.53–12.72 belongs to a separate review','count':len(records),'records':records},ensure_ascii=False,indent=2))
