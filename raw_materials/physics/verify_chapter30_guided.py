from pathlib import Path
import math,json

results={}
results['VP30.4.1']={'M_H':1.30e-4/2.,'fluxLinkage_Wb':1.30e-4/2.*24.}
results['VP30.4.2']={'emfGrowing_V':48e-6*7,'emfConstant_V':0.,'emfDecreasing_V':48e-6*3}
results['VP30.4.3']={'flux_Wb':76e-6*12/465,'emf_V':76e-6*55}
results['VP30.4.4']={'L_H':3.70e-3/145,'emfAt2_V':3.70e-3/145*900}
resistance=4.90e-3*math.log(4)/80e-6
results['VP30.7.1']={'R_ohm':resistance,'I_A':.75*24/resistance}
decay=math.exp(-18*.000700/.0375)
growth=12/18*(1-decay)
fall=12/18*decay
results['VP30.7.2']={'I_A':growth,'dI_A_per_s':12/.0375*decay,'U_J':.5*.0375*growth**2}
results['VP30.7.3']={'I_A':fall,'dI_A_per_s':-12/.0375*decay,'U_J':.5*.0375*fall**2}
results['VP30.7.4']={'t_over_tau':math.log(2),'I_over_E_div_R':.5,'dI_over_E_div_L':.5}
omega=2*math.pi*445
results['VP30.10.1']={'C_F':1/(25e-6*omega**2),'Imax_A':omega*.005}
omega=1/math.sqrt(30e-6*655e-6)
results['VP30.10.2']={'firstZero_s':math.pi/(2*omega),'Imax_A':omega*.0004}
capacitance=.00530**2/.8
inductance=.8/8**2
results['VP30.10.3']={'C_F':capacitance,'L_H':inductance,'omega_rad_per_s':1/math.sqrt(capacitance*inductance)}
results['VP30.10.4']={'C_F':1/(.042*624**2),'R_ohm':2*.042*math.sqrt(624**2-208**2)}
total=.5*(6e-6)**2/(250e-6)+.5*.060*(.0004)**2
results['bridge']={'Umax_J':total,'Imax_A':math.sqrt(2*total/.060),'Vmax_V':math.sqrt(2*total/250e-6),'UatHalfI_J':total/4,'VatHalfI_V':math.sqrt(1.5*total/250e-6)}
assert math.isclose(results['VP30.10.3']['C_F'],35.1125e-6,rel_tol=1e-12)
assert math.isclose(results['VP30.10.4']['C_F'],61.1481e-6,rel_tol=1e-5)
assert math.isclose(results['VP30.7.1']['R_ohm'],84.9,rel_tol=.001)
assert math.isclose(results['bridge']['Umax_J'],7.68e-8,rel_tol=1e-12)
(Path(__file__).resolve().parents[2]/'qa/physics/chapter30/guided-data-checks.json').write_text(json.dumps({'status':'passed','sourceImageReviewed':'printed page1010, PDF1030','solutionsAuthored':True,'results':results},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Recalculated twelve variation problems and the bridge. C in VP30.10.3 and VP30.10.4 uses microfarads.')
