"""Independent calculations for original exercises12.1–12.46; no public files written."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

OUT=Path(__file__).resolve().parent
g=9.80;water=1000.;sea=1030.;blood=1060.;glycerin=1260.;mercury=13600.
records={}
def put(n,**values):records[f'12.{n}']=values
V=math.pi*(.0285/2)**2*.858;m=7800*V
put(1,volume_m3=V,mass_kg=m,weight_N=m*g)
V0=.05**3;Vhole=math.pi*.01**2*.05;V=V0-Vhole;rho=(6.30/g)/V
put(2,remaining_volume_m3=V,density_kg_m3=rho,initial_weight_N=rho*V0*g)
V=.005*.015*.030;rho=.0158/V
put(3,volume_m3=V,density_kg_m3=rho,gold_density_kg_m3=19300,percent_of_gold_density=100*rho/19300,is_gold_density=False)
sunmass=1.99e30;sunradius=6.96e8
put(4,sun_mean_density_kg_m3=sunmass/(4*math.pi*sunradius**3/3),neutron_mean_density_kg_m3=sunmass/(4*math.pi*(20e3)**3/3),mass_kg=sunmass,sun_radius_m=sunradius)
put(5,aluminum_to_lead_radius_ratio=(11300/2700)**(1/3))
V=math.pi*.25*(.035**2-.025**2)*1.5;m=8900*V
put(6,metal_volume_m3=V,mass_kg=m,weight_N=m*g)
dp=water*3.71*500
put(7,mars_gauge_Pa=dp,earth_seawater_depth_m=dp/(sea*g))
dp=blood*g*1.65;area=math.pi*.00150*.0200
put(8,head_to_feet_pressure_increase_Pa=dp,lateral_area_m2=area,integrated_outward_load_increase_N=dp*area,note='Integral of outward normal force magnitudes on cylindrical wall, not nonzero net vector around full circumference.')
put(9,threshold_height_m=5980/(1050*g),note='Threshold corresponds zero flow; positive flow needs a strictly positive excess head in ideal limiting model.')
p=600*g*.120
put(10,interface_gauge_Pa=p,bottom_gauge_Pa=p+water*g*.250)
put(11,glycerin_column_above_interface_m=.350-.120,unknown_density_kg_m3=glycerin*(.350-.120)/.350)
dp=sea*g*250
put(12,gauge_Pa=dp,window_net_force_inward_N=dp*math.pi*.15**2)
area=math.pi*(.0082/2)**2
put(13,eardrum_area_m2=area,pressure_difference_threshold_Pa=1.5/area,depth_m=1.5/(area*sea*g))
patm=980*100;pbot=patm+mercury*g*.07
put(14,bottom_absolute_Pa=pbot,depth4cm_absolute_Pa=patm+mercury*g*.04,gas_absolute_Pa=pbot-mercury*g*.03,gas_gauge_Pa=mercury*g*(.07-.03))
put(15,external_minus_internal_pressure_Pa=water*g*6.1)
put(16,lowest_lung_gauge_Pa=-water*g*1.1)
put(17,net_water_over_air_force_up_N=sea*g*30*.75,crew_downward_force_N=sea*g*30*.75-300)
height=mercury/water*.08
put(18,added_water_height_m=height,added_water_volume_m3=12e-4*height,added_water_volume_L=12e-4*height*1000)
area=math.pi*.15**2
put(19,oil_surface_gauge_Pa=45/area,added_pressure_every_depth_Pa=83/area,initial_bottom_gauge_Pa=45/area+850*g*.750)
put(20,double_surface_pressure_depth_m=1.03e5/(sea*g),quadruple_surface_pressure_depth_m=3*1.03e5/(sea*g))
put(21,diameter_ratio=math.sqrt(1520*g/125),area_ratio=1520*g/125)
dp=1200*g/(math.pi*.15**2)
put(22,required_gauge_Pa=dp,required_gauge_atm=dp/101325)
put(23,wine_barometer_height_m=mercury*.750/990)
f=.030;m=70
V=m/(sea*(1-f))
put(24,formula_total_volume='weight/(rho_sea*g*(1-f))',formula_density='rho_sea*(1-f)',illustrative_emerged_fraction=f,illustrative_weight_N=m*g,illustrative_volume_m3=V,illustrative_mean_density_kg_m3=sea*(1-f))
V=(900-20)/(water*g);m=900/g
put(25,volume_m3=V,mean_density_kg_m3=m/V)
V=(1.8*g-12.8)/(water*g)
put(26,volume_m3=V,minimum_float_density_kg_m3=1.8/V)
put(27,additional_sink_m=80/(sea*math.pi*.45**2),initial_submerged_height_m=950/(sea*math.pi*.45**2))
put(28,minimum_ice_volume_m3=65/(water-920))
V=(17.50-11.20)/(water*g)
put(29,total_volume_m3=V,density_kg_m3=17.50/(g*V))
put(30,apparatus_mean_density_kg_m3=.25*sea,caasi_submerged_fraction=.25*sea/glycerin,caasi_submerged_percent=100*.25*sea/glycerin)
put(31,immersed_tension_N=28*(1-750/1200))
B=water*g*.650;m=(B-1120)/g
put(32,buoyant_force_N=B,sphere_mass_kg=m,floating_submerged_fraction=m/(water*.650))
pupper=790*g*.015;plower=790*g*.1+water*g*.015
mass=(plower-pupper)*.1**2/g
put(33,upper_face_gauge_Pa=pupper,lower_face_gauge_Pa=plower,mass_kg=mass,density_kg_m3=mass/.1**3,oil_submerged_height_m=.085,water_submerged_height_m=.015)
V=89/(2700*g)
put(34,volume_m3=V,immersed_tension_N=89-water*g*V)
V=(39.2-28.4)/(water*g)
put(35,rock_volume_m3=V,unknown_liquid_density_kg_m3=(39.2-21.5)/(g*V))
put(36,block_density_kg_m3=water*.7,second_liquid_density_kg_m3=water*.7/.8)
V=30/370;B=water*g*.7*V
put(37,cylinder_volume_m3=V,buoyant_force_N=B,cable_tension_down_N=B-30*g)
Q=.750;v=Q/(math.pi*(.045/2)**2)
put(38,hole_speed_m_s=v,triple_diameter_speed_m_s=v/9)
put(39,pipe_Q_m3_s=math.pi*.008**2*3,exit_speed_m_s=(math.pi*.008**2*3)/(20*math.pi*.001**2))
Q=.070*3.5
put(40,volume_flow_m3_s=Q,speed_at_A0105_m_s=Q/.105,speed_at_A0047_m_s=Q/.047,discharged_volume_one_hour_m3=Q*3600)
Q=1.2
put(41,speed_at_r015_m_s=Q/(math.pi*.15**2),radius_at_v380_m=math.sqrt(Q/(math.pi*3.8)))
put(42,planet_g_m_s2=1.94e-5/(2*(9e-4)**2))
Vgal=.003785411784;Atank=math.pi*1.5**2;Ahole=math.pi*.0025**2;drop=Vgal/Atank
v=math.sqrt(2*g*2);Q=Ahole*v;duration=Vgal/Q
exact_time=Atank/Ahole*math.sqrt(2/g)*(math.sqrt(2)-math.sqrt(2-drop))
put(43,one_US_gallon_m3=Vgal,height_drop_m=drop,initial_exit_speed_m_s=v,initial_volume_flow_m3_s=Q,constant_head_collect_time_s=duration,exact_varying_head_time_s=exact_time,relative_depth_change=drop/2)
Q=220*.355e-3/60;massflow=water*Q;v1=Q/(2e-4);v2=Q/(8e-4);p1=152e3+water*(v2*v2-v1*v1)/2-water*g*1.35
put(44,mass_flow_kg_s=massflow,volume_flow_m3_s=Q,v1_m_s=v1,v2_m_s=v2,p1_gauge_Pa=p1)
put(45,exit_speed_m_s=math.sqrt(2*(3*101325/sea+g*11)))
dp=1.20e4-1.15e4;rho=1060;v1=.300;v2=math.sqrt(v1*v1+2*dp/rho)
fraction=1-v1/v2
put(46,pressure_drop_Pa=dp,blood_density_kg_m3=rho,constriction_speed_m_s=v2,open_area_fraction=v1/v2,blocked_area_percent=100*fraction)

# Independent back-substitution/quadrature catches sign/geometry mistakes.
assert len(records)==46 and set(records)=={f'12.{i}'for i in range(1,47)}
assert math.isclose(quad(lambda z: math.pi*(.0285/2)**2*7800*g,0,.858)[0],records['12.1']['weight_N'])
assert math.isclose(records['12.2']['density_kg_m3']*(V0-Vhole)*g,6.30)
assert records['12.3']['density_kg_m3']<19300
assert math.isclose(records['12.5']['aluminum_to_lead_radius_ratio']**3*2700,11300)
assert math.isclose(records['12.11']['unknown_density_kg_m3']*.35,glycerin*.23)
assert math.isclose(records['12.18']['added_water_volume_m3']/12e-4*water*g,mercury*g*.08)
for n,key,weight in [(25,'volume_m3',900-20),(29,'total_volume_m3',17.50-11.20)]:
 assert math.isclose(records[f'12.{n}'][key]*water*g,weight)
assert math.isclose(records['12.32']['buoyant_force_N'],records['12.32']['sphere_mass_kg']*g+1120)
assert math.isclose(records['12.33']['mass_kg'],790*.01*.085+water*.01*.015)
assert math.isclose(records['12.35']['unknown_liquid_density_kg_m3']/water,(39.2-21.5)/(39.2-28.4))
assert math.isclose(records['12.37']['cable_tension_down_N']+30*g,records['12.37']['buoyant_force_N'])
assert records['12.38']['hole_speed_m_s']>400 #Source reallyQ=.750m3/s,not.750L/s.
assert records['12.43']['relative_depth_change']<.001
assert abs(records['12.43']['exact_varying_head_time_s']/records['12.43']['constant_head_collect_time_s']-1)<.001
assert math.isclose(2*records['12.42']['planet_g_m_s2']*(9e-4)**2,1.94e-5)
assert math.isclose(records['12.44']['v1_m_s']*2e-4,records['12.44']['v2_m_s']*8e-4)
assert math.isclose(records['12.44']['p1_gauge_Pa']+water*g*1.35+.5*water*records['12.44']['v1_m_s']**2,152e3+.5*water*records['12.44']['v2_m_s']**2)
assert math.isclose(.5*rho*(v2*v2-v1*v1),dp)

# A second route checks selected solutions against force or mass balances.
assert math.isclose(records['12.6']['metal_volume_m3'],math.pi*(.035/2+.025/2)*(.035/2-.025/2)*1.5)
assert math.isclose(records['12.7']['mars_gauge_Pa'],records['12.7']['earth_seawater_depth_m']*sea*g)
assert math.isclose(records['12.9']['threshold_height_m']*1050*g,5980)
assert math.isclose(records['12.10']['bottom_gauge_Pa']-records['12.10']['interface_gauge_Pa'],water*g*.25)
assert math.isclose(records['12.12']['window_net_force_inward_N']/(math.pi*.15**2),records['12.12']['gauge_Pa'])
assert math.isclose(records['12.13']['depth_m']*sea*g*records['12.13']['eardrum_area_m2'],1.5)
assert math.isclose(records['12.14']['bottom_absolute_Pa']-mercury*g*.03,records['12.14']['gas_absolute_Pa'])
assert math.isclose(records['12.14']['depth4cm_absolute_Pa'],records['12.14']['gas_absolute_Pa'])
assert math.isclose(records['12.15']['external_minus_internal_pressure_Pa']/(water*g),6.1)
assert math.isclose(records['12.16']['lowest_lung_gauge_Pa']+water*g*1.1,0,abs_tol=1e-12)
assert math.isclose(records['12.17']['crew_downward_force_N']+300,records['12.17']['net_water_over_air_force_up_N'])
assert math.isclose(records['12.19']['added_pressure_every_depth_Pa']*math.pi*.15**2,83)
assert math.isclose(records['12.20']['quadruple_surface_pressure_depth_m']/records['12.20']['double_surface_pressure_depth_m'],3)
assert math.isclose(records['12.21']['diameter_ratio']**2,records['12.21']['area_ratio'])
assert math.isclose(records['12.22']['required_gauge_Pa']*math.pi*.15**2,1200*g)
assert math.isclose(records['12.23']['wine_barometer_height_m']*990,mercury*.750)
assert math.isclose(records['12.24']['illustrative_volume_m3']*(1-.03)*sea*g,70*g)
assert math.isclose(records['12.26']['minimum_float_density_kg_m3']*records['12.26']['volume_m3']*g,1.8*g)
assert math.isclose(records['12.27']['additional_sink_m']*math.pi*.45**2*sea*g,80*g)
assert math.isclose((water-920)*records['12.28']['minimum_ice_volume_m3'],65)
assert math.isclose(records['12.30']['caasi_submerged_fraction']*glycerin*5.40,records['12.30']['apparatus_mean_density_kg_m3']*5.40)
assert math.isclose(records['12.31']['immersed_tension_N']+750/1200*28,28)
assert math.isclose(records['12.34']['immersed_tension_N']+water*g*records['12.34']['volume_m3'],89)
assert math.isclose(records['12.36']['second_liquid_density_kg_m3']*.8,water*.7)
assert math.isclose(records['12.38']['hole_speed_m_s']/records['12.38']['triple_diameter_speed_m_s'],9)
assert math.isclose(records['12.39']['exit_speed_m_s']*20*math.pi*.001**2,records['12.39']['pipe_Q_m3_s'])
assert math.isclose(records['12.40']['speed_at_A0105_m_s']*.105,records['12.40']['speed_at_A0047_m_s']*.047)
assert math.isclose(math.pi*records['12.41']['radius_at_v380_m']**2*3.8,1.2)
assert math.isclose(.5*sea*records['12.45']['exit_speed_m_s']**2,3*101325+sea*g*11)

# Parameter cases exercise sign and cancellation independent of the source numbers.
for mass,rhoa,rhof in [(3.,2700.,1000.),(.7,11300.,750.),(70.,1001.,1030.)]:
 volume=mass/rhoa
 B=rhof*g*volume
 T=mass*g-B
 assert math.isclose(T/(mass*g),1-rhof/rhoa)
for r1,r2,rate in [(.04,.02,.0095),(.008,.001,.0006),(.15,.32,1.2)]:
 va=rate/(math.pi*r1*r1);vb=rate/(math.pi*r2*r2)
 assert math.isclose(va/vb,(r2/r1)**2)

report=dict(status='passed',sourcePdfPages=[408,409,410],constants=dict(g=g,water=water,seawater=sea,blood=blood,glycerin=glycerin,mercury=mercury,iron=7800,lead=11300,aluminum=2700,copper=8900,ice=920),records=records)
print(json.dumps(report,ensure_ascii=False,indent=2))
