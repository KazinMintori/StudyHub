"""Original12.53–12.72: independent calculations and alternate integrations."""
from pathlib import Path
import math,json
import numpy as np
from scipy.integrate import quad

OUT=Path(__file__).resolve().parent
g=9.8;rho_w=1000.;rho_sea=1030.;rho_eth=810.;rho_gly=1260.;rho_Hg=13600.
records={}
def put(n,**r):records[f'12.{n}']=r
put(53,diameter_ratio=2**.25,percent_diameter_increase=(2**.25-1)*100)
h=10920;p0=101325;p_actual=1.16e8;kappa=45.8e-11
p_inc=rho_sea*g*h
delta=p_actual-p0;volume_fraction=1-kappa*delta
rho_compressed=rho_sea/volume_fraction
put(54,incompressible_gauge_Pa=p_inc,incompressible_absolute_Pa=p0+p_inc,compressibility_Pa_inv=kappa,pressure_increase_Pa=delta,volume_fraction=volume_fraction,linear_volume_model_density_kg_m3=rho_compressed,density_increase_percent=(rho_compressed/rho_sea-1)*100,first_order_density_kg_m3=rho_sea*(1+kappa*delta),first_order_density_percent=100*kappa*delta,note='Finite bulk-strain model V≈V0(1-kappa*dp). Expanding reciprocal to first order gives5.31percent, while retaining reciprocal gives5.61percent. No hydrostatic integration withvariablekappa claimed.')
length,width,depth=5.,4.,3.
bottom=rho_w*g*depth*length*width
end=quad(lambda y:rho_w*g*y*width,0,depth)[0]
put(55,bottom_force_N=bottom,end_force_N=end,long_side_force_if_requested_N=rho_w*g*depth**2*length/2)
volume=(1.6-1.2)/((rho_w-rho_eth)*g);weight=1.2+rho_w*g*volume
put(56,rock_volume_m3=volume,rock_weight_N=weight)
W,H=4.,2.
torque=quad(lambda y:rho_w*g*W*y*(y-H/2),0,H)[0]
gate_force=quad(lambda y:rho_w*g*W*y,0,H)[0]
upper=quad(lambda y:rho_w*g*W*y*(y-H/2),0,H/2)[0]
lower=quad(lambda y:rho_w*g*W*y*(y-H/2),H/2,H)[0]
put(57,gate_force_N=gate_force,torque_about_middle_N_m=torque,upper_signed_torque_N_m=upper,lower_signed_torque_N_m=lower,center_of_pressure_depth_m=2*H/3)
V=.02**3;m=.0092;rhob=m/V;f=(rhob-rho_w)/(rho_gly-rho_w)
put(58,wood_density_kg_m3=rhob,glycerin_submerged_fraction=f,glycerin_submerged_percent=100*f,depth_in_glycerin_m=f*.02,depth_in_water_m=(1-f)*.02)
slope=.0390;intercept=.0312;A=1/(rho_w*slope);mass=intercept/slope
put(59,area_m2=A,block_mass_kg=mass,block_density_kg_m3=mass/(A*.08),maximum_coin_mass_before_top_wet_kg=(.08-intercept)/slope)
sigma=.005;rho_M=.0154;radius=3*sigma/rho_M;M=4*math.pi*radius**2*sigma
acc=g*(1.20/rho_M-1)
put(60,radius_m=radius,envelope_mass_kg=M,initial_earth_acceleration_up_m_s2=acc,initial_earth_acceleration_in_g=acc/g,big_radius_m=5*radius,big_envelope_mass_kg=25*M,big_displaced_atmosphere_mass_kg=125*M,package_mass_kg=100*M,package_weight_on_Mars_N=100*M*3.71)
ice=.180;area=math.pi*.035**2;delta_volume=ice/rho_w-ice/rho_gly
put(61,initial_displaced_glycerin_volume_m3=ice/rho_gly,melted_water_volume_m3=ice/rho_w,liquid_level_change_up_m=delta_volume/area)
oilratio=.8;initial=.25;water_left=(initial+oilratio*initial)/2;water_right=initial-water_left
put(62,water_left_height_m=water_left,water_under_oil_right_m=water_right,right_total_column_height_m=water_right+initial,equal_density_heights_m=[.25,.25],negligible_oil_density_heights_m=[.125,.375])
water_h=.15;Hgdiff=rho_w/rho_Hg*water_h
put(63,interface_gauge_Pa=rho_w*g*water_h,mercury_level_difference_m=Hgdiff,water_top_above_right_mercury_m=water_h-Hgdiff)
rho_molasses=1600.;H=17.7;D=27.4
force=quad(lambda y:rho_molasses*g*y*math.pi*D,0,H)[0]
put(64,total_outward_load_magnitude_N=force,net_vector_force_all_sidewalls_N=0,tank_volume_m3=math.pi*(D/2)**2*H)
V=40/(rho_w*.8);maxload=rho_w*V-40
put(65,block_volume_m3=V,maximum_brick_mass_kg=maxload)
V=2200.;rhoair=1.23;otherW=900+1700+3200
rhog=rhoair-otherW/(g*V)
put(66,buoyant_force_N=rhoair*g*V,total_non_gas_weight_N=otherW,heated_gas_density_kg_m3=rhog,heated_gas_mass_kg=rhog*V)
L,W,H,t=40.,22.,12.,.04;steelrho=7800.;coalrho=1500.
outer=L*W*H;inner=(L-2*t)*(W-2*t)*(H-t)
steel=outer-inner;steelmass=steel*steelrho;maxcoal=rho_w*outer-steelmass;coalvolume=maxcoal/coalrho
thinsteel=t*(L*W+2*L*H+2*W*H)
put(67,outer_displacement_limit_m3=outer,interior_capacity_m3=inner,steel_volume_m3=steel,steel_mass_kg=steelmass,max_coal_mass_kg=maxcoal,coal_volume_m3=coalvolume,coal_fits=bool(coalvolume<inner),thin_plate_approx_steel_volume_m3=thinsteel,thin_plate_approx_max_coal_mass_kg=rho_w*outer-thinsteel*steelrho,outer_dimensions_assumed=True)
Vwood=.600*.250*.080;rhoWood=700.;rhoPb=11300.;Vpb=(rho_w-rhoWood)*Vwood/(rhoPb-rho_w)
put(68,wood_volume_m3=Vwood,lead_volume_m3=Vpb,lead_mass_kg=rhoPb*Vpb)
head=.25;height=.80;jet=math.sqrt(2*g*head);fall=math.sqrt(2*height/g)
put(69,general_range_formula='2sqrt(hH)',illustrative_milk_head_m=head,illustrative_table_height_m=height,illustrative_exit_speed_m_s=jet,illustrative_fall_time_s=fall,illustrative_range_m=jet*fall)
Q=.0800;vA=Q/.05;vB=Q/.02;p=rho_eth*(vB*vB-vA*vA)/2+rho_eth*g*3
put(70,speed_A_m_s=vA,speed_B_m_s=vB,required_gauge_Pa=p)
Q=.5;H=28.;v=math.sqrt(2*g*H);area=Q/v;diam=math.sqrt(4*area/math.pi)
put(71,required_exit_speed_m_s=v,maximum_nozzle_diameter_m=diam,double_diameter_exit_speed_m_s=v/4,double_diameter_max_height_m=H/16)
beaker=1.;liquid=1.8;Dkg=3.5;Ekg=7.5;Vblock=.00380
Bkg=Ekg-beaker-liquid;blockmass=Dkg+Bkg
put(72,beaker_mass_kg=beaker,liquid_mass_kg=liquid,hanging_balance_D_kg=Dkg,platform_balance_E_kg=Ekg,buoyant_mass_equivalent_kg=Bkg,buoyant_force_N=Bkg*g,liquid_density_kg_m3=Bkg/Vblock,block_mass_kg=blockmass,final_D_kg=blockmass,final_E_kg=beaker+liquid,rejected_handoff_error='Handoff incorrectlycalledbeaker3.50kg;actualPDF411beaker1.00kgandD3.50kg.')
assert set(records)=={f'12.{n}'for n in range(53,73)}
assert math.isclose(records['12.53']['diameter_ratio']**4,2)
assert math.isclose(records['12.54']['linear_volume_model_density_kg_m3']*volume_fraction,rho_sea)
assert math.isclose(records['12.55']['end_force_N'],rho_w*g*4*3**2/2)
assert math.isclose(weight-rho_w*g*volume,1.2) and math.isclose(weight-rho_eth*g*volume,1.6)
assert math.isclose(torque,rho_w*g*4*2**3/12)
assert math.isclose(torque,gate_force*(2*2/3-2/2))
assert math.isclose(upper+lower,torque)
assert math.isclose(rho_w*(1-f)+rho_gly*f,rhob)
for coin in [0,.1,.5,1]:
 h=intercept+slope*coin
 assert math.isclose(rho_w*A*h,mass+coin)
assert math.isclose(rho_M*(4*math.pi*radius**3/3),M)
assert math.isclose(rho_M*(4*math.pi*(5*radius)**3/3),25*M+100*M)
assert math.isclose(water_left-water_right,.8*.25)
assert math.isclose(water_left+water_right,.25)
assert math.isclose(records['12.63']['interface_gauge_Pa'],rho_Hg*g*Hgdiff)
assert math.isclose(records['12.64']['total_outward_load_magnitude_N'],rho_molasses*g*17.7*math.pi*27.4*17.7/2)
assert math.isclose(rho_w*records['12.65']['block_volume_m3'],40+records['12.65']['maximum_brick_mass_kg'])
assert math.isclose(rhoair*g*V,rhog*g*V+otherW)
assert math.isclose(steelmass+maxcoal,rho_w*outer)
assert math.isclose((rhoPb-rho_w)*Vpb,(rho_w-rhoWood)*Vwood)
assert math.isclose(jet*fall,2*math.sqrt(head*height))
assert math.isclose(p+.5*rho_eth*vA*vA,.5*rho_eth*vB*vB+rho_eth*g*3)
assert math.isclose(math.pi*diam**2/4*v,Q)
assert math.isclose((v/4)**2/(2*g),H/16)
assert math.isclose(blockmass*g,Dkg*g+Bkg*g)
assert math.isclose(Ekg*g,(beaker+liquid)*g+Bkg*g)
assert math.isclose(records['12.72']['liquid_density_kg_m3']*g*Vblock,Bkg*g)
# Parameter cases validate both hydrostatic integrals and equilibrium cancellation.
for rh,gg,b,depth in [(1000,9.8,4,3),(850,3.71,2.5,1.7),(1260,9.8,3.2,5)]:
 F=quad(lambda y:rh*gg*b*y,0,depth)[0]
 tau=quad(lambda y:rh*gg*b*y*(y-depth/2),0,depth)[0]
 assert math.isclose(F,rh*gg*b*depth**2/2)
 assert math.isclose(tau,rh*gg*b*depth**3/12)
for ratio in [.1,.5,.8,1.]:
 left=(.25+ratio*.25)/2;under=.25-left
 assert math.isclose(left,under+ratio*.25)
 assert math.isclose(left+under,.25)
report=dict(status='passed',sourcePdfPages=[410,411],records=records)
print(json.dumps(report,ensure_ascii=False,indent=2))
