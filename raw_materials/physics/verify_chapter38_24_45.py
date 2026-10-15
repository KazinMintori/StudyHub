from math import sqrt,pi,cos,sin,acos,degrees,isclose
import json
import numpy as np
h=6.626e-34;c=2.998e8;e=1.602e-19;me=9.109e-31;mp=1.673e-27;hb=h/(2*pi);lc=h/(me*c);Ee=me*c*c
def g(b):return 1/sqrt((1-b)*(1+b))
def close(a,b):assert np.allclose(a,b,rtol=1e-10,atol=0),(a,b)
r={}
N=.1*120/(h*5e14);r['38.24']={'a_photons_s':N,'b_distance_m':sqrt(N/(4*pi*1e15))}
Q=2e-9*(4190*(100-33)+2.256e6);r['38.25']={'mass_kg':2e-9,'pulse_duration_s':450e-6,'a_energy_J':Q,'b_power_W':Q/(450e-6),'c_photons_pulse':Q/(h*c/(585e-9))}
E=h*c/(124e-9);N=2.5/E;r['38.26']={'a_work_function_eV':E/e-4.16,'b_photoelectrons_s':N,'c_half_power_s':N/2,'d_half_wavelength_s':N/2}
I=1.;A=20.;H=2.5;P=I*A;Eroom=P*H/c;E=h*c/(500e-9)
r['38.27']={'assumed_intensity_W_m2':I,'assumed_area_m2':A,'assumed_height_m':H,'c_transit_s':H/c,'d_power_W':P,'e_room_energy_J':Eroom,'f_photon_J':E,'g_photons_in_room':Eroom/E}
lam=.098e-9;sc=lam+2*lc;r['38.28']={'electron_momentum':h/lam+h/sc}
lam=.105e-9;angle=pi/3;sc=lam+lc*(1-cos(angle));px=h/lam-h/sc*cos(angle);py=-h/sc*sin(angle)
r['38.29']={'momentum_kg_m_s':sqrt(px*px+py*py),'angle_degree_opposite_photon_side':degrees(np.arctan2(abs(py),px))}
Cal=25.;At=.5;Ein=Cal*4186;P=800*At;Eff=.05;Ep=h*c/(600e-9);N=Eff*P/Ep;per=N*.5/10
r['38.30']={'assumed_tomato_Cal':Cal,'a_energy_J':Ein,'assumed_leaf_area_m2':At,'c_incident_power_W':P,'d_photosynthesis_photons_s':N,'e_per_tomato_photons_s':per,'f_photons_energy_content':Ein/Ep,'g_days_12h_sun':(Ein/Ep)/per/(12*3600)}
li=h*c/(1e6*e);dl=(500e-9-li)/1e26;angle=sqrt(2*dl/lc);year=365.25*86400
r['38.31']={'a_mean_shift_m':dl,'b_angle_deg':degrees(angle),'c_mean_free_path_m':c*1e6*year/1e26,'model_not_exact_transport':True}
restMeV=.511;gamma=1+5.11/restMeV;b=sqrt(1-1/gamma**2);co=sqrt((gamma-1)/(gamma+1))
r['38.32']={'d_gamma':gamma,'d_photon_MeV':(gamma+1)*restMeV/2,'d_each_angle_deg':degrees(acos(co)),'e_perpendicular_gamma':3,'e_positron_beta':sqrt(8)/3,'f_CM_beta_for_d':gamma*b/(gamma+1),'formula_CM_beta':'gamma*beta/(gamma+1)'}
K=h*c/(.1100e-9)-h*c/(.1132e-9);gamma=1+K/Ee
r['38.33']={'a_K_J':K,'a_speed_m_s':c*sqrt(1-1/gamma**2),'b_stopping_photon_wavelength_m':h*c/K}
sc=5.10e-12;v=1.8e8;K=(g(v/c)-1)*Ee;lam=h*c/(h*c/sc+K);angle=degrees(acos(1-(sc-lam)/lc))
r['38.34']={'c_incident_wavelength_m':lam,'c_scatter_angle_deg':angle}
lamnm=np.array([100,120,140,160,180,200]);V=np.array([7.53,5.59,3.98,2.92,2.06,1.43]);x=1/lamnm;slope,intercept=np.polyfit(x,V,1);S=slope*1e-9;hp=S*e/c;phi=-intercept
r['38.35']={'a_slope_V_nm':slope,'a_intercept_V':intercept,'b_h_J_s':hp,'b_work_function_eV':phi,'c_threshold_nm':slope/phi,'d_wavelength_K10eV_nm':slope/(10+phi),'points':6}
work={'Aluminum':4.3,'Carbon':5.,'Copper':4.7,'Gold':5.1,'Nickel':5.1,'Silicon':4.8,'Silver':4.3,'Sodium':2.7};E=h*c/(270e-9)/e;active=[k for k,v in work.items() if E>v];K=(E-2.7)*e
r['38.36']={'a_materials':active,'b_best':'Sodium','b_max_speed_m_s':sqrt(2*K/me),'c_gold_threshold_m':h*c/(5.1*e),'d_sodium_K_eV':5.1-2.7}
angles=np.array([30.6,58.7,90.2,119.2,151.3]);sc=np.array([5.52,6.40,7.60,8.84,9.69]);X=1-np.cos(angles*pi/180);slope,intercept=np.polyfit(X,sc,1)
r['38.37']={'a_slope_pm':slope,'a_intercept_pm':intercept,'b_Compton_pm':slope,'c_incident_pm':intercept,'points':5}
# Literal figure labels: a has anode-positive bias, b retarding bias. The
# quantitative sequence in the text only works if those switch names are swapped.
R=334.;Vstop=15*R/(1000+R);Phi=h*c/(140e-9)/e-Vstop;i=.00371
Vc=(i-.015)/(1/R+.001);Ires=Vc/R;Vsnew=h*c/(65e-9)/e-Phi;Rcut=1000*Vsnew/(15-Vsnew)
r['38.38']={'literal_a_bias_V_at3200ohm':15*3200/4200,'literal_figure_text_consistent':False,'conditional_swapped_labels':{'a_VAC_V':-15*3200/4200,'b_VAC_V':-Vstop,'c_work_function_eV':Phi,'d_I_R_rightward_A':Ires,'e_VAC_V':-Vc,'f_cutoff_R_ohm':Rcut}}
assert abs((Vc+15)/1000+Vc/R-i)<1e-15
ratio=me/mp
def recoil(gamma,b,phi):
 d=2*ratio*gamma*(1-b*cos(phi));aa=1-d;assert 0<aa<1
 B=(1-aa*aa)/(1+aa*aa);gm=g(B);Egamma=((gm-1)*mp+2*gamma*me)*c*c
 close(Egamma/c,gm*mp*B*c+2*gamma*me*b*c*cos(phi))
 return dict(exact_beta=B,exact_speed_km_s=B*c/1000,first_order_beta=d,incident_photon_MeV=Egamma/(1e6*e))
gamma=5e6*e/Ee;b=sqrt(1-1/gamma**2)
r['38.39']={'f_pair_at_rest':recoil(1,0,0),'g_each_5MeV_phi60':recoil(gamma,b,pi/3),'stationary_target_possible':False}
E=10e9*e;lam=10.6e-6;q=sqrt(E*E-Ee*Ee);lp=Ee*Ee*lam/(E+q)**2+2*h*c/(E+q);Ep=h*c/lp
r['38.40']={'b_scattered_wavelength_m':lp,'c_photon_energy_MeV':Ep/(1e6*e),'region':'gamma','approx_wavelength_m':h*c/E*(1+Ee*Ee*lam/(4*h*c*E))}
masscell=1e-3/1e8;dose=70/35;Ecell=dose*masscell
r['38.41']={'cell_mass_kg':masscell,'energy_cell_J':Ecell,'energy_cell_MeV_using_prompt_conversion':Ecell*6e18/1e6,'answer':'c'}
r['38.42']={'maximum_ionizations':4e6/40,'answer':'d'}
Eprime=4/(1+2*4/.511)
r['38.43']={'remaining_photon_MeV':Eprime,'electron_max_MeV':4-Eprime,'answer':'a'}
r['38.44']={'answer':'c','condition':'Within the two-process plot supplied by the passage.'}
r['38.45']={'answer':'b'}
assert len(r)==22
print(json.dumps(dict(status='passed',results=r),indent=2))
