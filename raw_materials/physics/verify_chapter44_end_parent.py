"""Independent calculations using actual chapter44 end-problem inputs.

The JSON is a private numerical ledger, not a substitute for source/solution review.
"""
from pathlib import Path
import math,json,re
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
e=1.602176634e-19;c=299792458.;h=6.62607015e-34;u=931.494
mp=1.67262192369e-27;NA=6.02214076e23;out={}
def save(key,**data):
 assert all(np.all(np.isfinite(v)) for v in data.values() if isinstance(v,(float,int)) or isinstance(v,(list,np.ndarray)) and np.asarray(v).dtype.kind in 'fiu')
 out[key]=data
def beta(r):return (r*r-1)/(r*r+1)
def threshold(m,M,F):return (F*F-(m+M)**2)/(2*M)
def two(M,a,b):
 ea=(M*M+a*a-b*b)/(2*M);eb=M-ea
 assert math.isclose(ea*ea-a*a,eb*eb-b*b,abs_tol=1e-8)
 return ea-a,eb-b
for key,m,q,B,R in [('VP44.1.1',mp,e,.6,.8),('VP44.1.4',6.64e-27,2*e,None,.65)]:
 if B is None:B=2*math.pi*m*5.8e6/q
 w=q*B/m;v=w*R;save(key,B_T=B,f_Hz=w/(2*math.pi),K_MeV=.5*m*v*v/e/1e6,beta=v/c)
save('VP44.1.2',R_m=1.67e-27*6e6/(e*.460),omega=e*.460/1.67e-27)
B=math.sqrt(2*1.67e-27*80e3*e)/(e*.057)
save('VP44.1.3',B_T=B,f_Hz=e*B/(2*math.pi*1.67e-27))
for key,m,M,F in [('VP44.3.1',938,938,2*938+958),('VP44.3.2',938,938,938+1232),('VP44.3.3',140,938,1232)]:save(key,CM_MeV=F,Klab_MeV=threshold(m,M,F))
cm=math.sqrt(2*.938**2+2*.938*7000);save('VP44.3.4',CM_GeV=cm,Xmax_GeV=cm-2*.938)
save('VP44.9.1',z=725/656.3-1,beta=beta(725/656.3))
save('VP44.9.2',lambda_nm=396.9*math.sqrt((1+.0711)/(1-.0711)),z=math.sqrt((1+.0711)/(1-.0711))-1)
save('VP44.9.3',distances_pc=[v*c/68000*1e6 for v in [.0992,.0711]])
save('VP44.9.4',v_m_s=beta(666/615)*c,distance_pc=beta(666/615)*c/68000*1e6)
save('44.1',energy_J=800*c*c,ratio_US=800*c*c/1e20)
save('44.2',lambda_max_m=h*c/(207*.511e6*e),beta_half_lambda=math.sqrt(.75))
save('44.3',Q_MeV=(273-207)*.511)
save('44.4',photon_MeV=[938.3,1558.3],lambda_m=[h*c/(x*1e6*e) for x in [938.3,1558.3]],frequency_Hz=[x*1e6*e/h for x in [938.3,1558.3]])
q=(1.008665+10.012937-7.016003-4.002603)*u;k=q*7.016003/(7.016003+4.002603)
save('44.5',Q_MeV=q,Kalpha_MeV=k,v_alpha=math.sqrt(2*k*1e6*e/(4.002603*1.6605390666e-27)))
save('44.6',range_m=197.3269804/783*1e-15)
save('44.7',K_fixed_GeV=threshold(.938,.938,2000),K_beam_GeV=1000-.938)
save('44.8',CM_GeV=math.sqrt(2*.000511**2+2*.000511*30),beam_GeV=math.sqrt(2*.000511**2+2*.000511*30)/2)
v=2*math.pi*9e6*.320;save('44.9',B_T=2*math.pi*3.344e-27*9e6/e,v=v,K_MeV=.5*3.344e-27*v*v/e/1e6)
save('44.10',p_for_radius15cm=e*.4*.15,p_for_diameter15cm=e*.4*.075)
save('44.11',E_fixed_GeV=(16**2-2*3.728**2)/(2*3.728),E_each_GeV=8)
v=e*1.3*.11/mp;save('44.12',K_MeV=.5*mp*v*v/e/1e6,beta=v/c,f=e*1.3/(2*math.pi*mp))
g=1000/.9383;save('44.13',beta=math.sqrt(1-1/g**2),omega_classical=e*4/mp,omega_rel=e*4/mp/g)
save('44.14',K_each_MeV=547.9/2,E_each_MeV=938.3+547.9/2)
save('44.15',K_colliding_MeV=938.3,K_fixed_MeV=6*938.3)
for key,Q in [('44.16',1672-1322-135),('44.17',493.7-139.6-135),('44.18',105.7-.511),('44.20',1672-1116-493.7),('44.21',1189.4-938.3-135),('44.28',9460-2*1777)]:save(key,Q_MeV=Q)
save('44.19',mass_kg=91.2e9*e/c**2,mass_ratio=91.2/.9383)
save('44.22',baryon_change=[-1,-2,0,0])
save('44.23',delta_Le=[2,0,-1,-2],delta_Lmu=[-2,0,0,0],delta_Ltau=[0,0,0,0])
save('44.24',strangeness_change=[-1,-1,0,0])
quarks={'u':np.array([2/3,1/3,0,0]),'d':np.array([-1/3,1/3,0,0]),'s':np.array([-1/3,1/3,-1,0]),'c':np.array([2/3,1/3,0,1]),'b':np.array([-1/3,1/3,0,0])}
for key,states in [('44.25',[['u','d','s'],['c','-u'],['d','d','d'],['d','-c']]),('44.26',[['u','u','s'],['c','-s'],['-d','-d','-u'],['-c','b']]),('44.27',[['u','-s'],['-d','-d','-s'],['u','s','s']])]:
 save(key,Q_B_S_C=[sum(((-1 if x.startswith('-') else 1)*quarks[x[-1]] for x in state),np.zeros(4)).tolist() for state in states])
assert np.allclose(out['44.25']['Q_B_S_C'][3],[-1,0,0,-1])
save('44.29',ratio=125/.9383)
save('44.30',beta=beta(658.5/590),v=beta(658.5/590)*c,distance_pc=beta(658.5/590)*c/68000*1e6)
v=2.2e-18*5210e6*9.461e15;b=v/c;save('44.31',v=v,redshift_ratio=math.sqrt((1+b)/(1-b)))
b=beta(1.7);save('44.32',beta=b,v=b*c,distance_m=b*c/2.2e-18)
save('44.33',Q_MeV=938.272+.511-939.565)
save('44.34',Q_MeV=(3*4.002603-12)*u)
save('44.35',Q_MeV=(12+4.002603-15.994915)*u)
F=8.9875517923e9*(2*e/3)**2/(.5e-15)**2;k=F/(.5e-15);k_mev_fm2=k*1e-30/e/1e6
save('44.36',F_N=F,k_N_m=k,k_MeV_fm2=k_mev_fm2,U_MeV=.5*k_mev_fm2*.5**2,pair_MeV=4.6,pair_distance_fm=math.sqrt(2*4.6/k_mev_fm2))
save('44.37',Q_MeV=139.6-.511,neededPions=.5/((139.6-.511)*1e6*e),H_Sv=50*1.5,H_rem=50*1.5*100)
save('44.38',K_MeV=h*c/(.720e-15)/e/1e6-938.3)
save('44.39',crossings_s=1/25e-9,colliding_fraction=20/115e9,collisions_s=20/25e-9,density_beam_per_mm3=115e9/(math.pi*(.020/2)**2*300),density_matter_per_mm3=1000/mp/1e9)
save('44.40',threshold_MeV=threshold(139.6,938.3,1192.6+497.7))
save('44.41',missing_quantum_Q_B_S_Le_Lmu_Ltau=[[1,0,1,0,0,0],[-1,0,0,0,0,0],[2,1,0,0,0,0],[1,0,0,0,-1,0]])
save('44.42',Q_3neutral=547.9-3*135,Q_charged=547.9-2*139.6-135)
save('44.43',uncertainty_time_s=6.582119569e-22/(2*4.4),natural_width_tau_s=6.582119569e-22/4.4)
save('44.44',uncertainty_MeV=6.582119569e-22/(2*7.6e-21),natural_width_MeV=6.582119569e-22/7.6e-21,fraction_uncertainty=6.582119569e-22/(2*7.6e-21)/3096.9)
decays=(1000/18.015)*NA*2*math.log(2)/1e18;D=decays*(938.272+.511)*1e6*e
save('44.45',decays_per_kg_yr=decays,D_Gy=D,D_rad=D*100,H_rem=D*100)
save('44.46',K_each_MeV=(1019.4-2*493.7)/2,three_body_Q=1019.4-2*493.7-135)
g=6000/105.7;b=math.sqrt(1-1/g**2);mean=b*c*g*2.2e-6
save('44.47',gamma=g,beta=b,nonrel_distance_m=b*c*2.2e-6,contracted15km_m=15000/g,meanDistance_m=mean,meanBeyondGround_m=mean-15000,survivalToGround=math.exp(-15000/mean))
kl,kp=two(1322,1116,139.6);save('44.48',Ktotal=kl+kp,K_lambda=kl,K_pion=kp,fraction_lambda=kl/(kl+kp),fraction_pion=kp/(kl+kp))
M=1197.;E=M+180;p=math.sqrt(E*E-M*M);epi=(M*M+139.6**2-939.6**2)/(2*E);ppi=math.sqrt(epi*epi-139.6**2)
save('44.49',K_neutron=E-epi-939.6,angle_deg=math.degrees(math.atan2(-ppi,p)))
E=497.7+225;p=math.sqrt(E*E-497.7**2);epi=E/2;ppi=math.sqrt(epi*epi-139.6**2)
save('44.50',K_pion=epi-139.6,theta_deg=math.degrees(math.acos(p/(2*ppi))))
B=np.array([.1,.2,.3,.4]);K=np.array([.068,.270,.608,1.080]);slope,intercept=np.polyfit(B*B,K,1)
save('44.51',B_T=B.tolist(),K_MeV=K.tolist(),slope_MeV_T2=slope,intercept_MeV=intercept,R_m=math.sqrt(2*mp*slope*1e6*e)/e,K025_MeV=slope*.25**2+intercept,omega040=e*.4/mp)
save('44.52',restMasses_MeV=[1197,1232,1315,1672],productK_MeV=[1197-939.6-139.6,1232-938.3-139.6,1315-1116-135,1672-1116-493.7])
save('44.53',quark_states=['uuu','uud','udd','ddd','uus','uds','dds','uss','dss','sss'],mass_sequence_MeV=[1232,1385,1530],omega_estimate_MeV=1530+((1385-1232)+(1530-1385))/2)
km,knu=two(493.7,105.7,0);emu=km+105.7
save('44.54',E_mu=emu,E_nu=knu,beta=knu/emu,Q=493.7-105.7)
year=3.156e7;R=500+.001*4*year;ratio=math.exp(.001/.00635*math.pi/3);dt=R*(ratio-1)/.001
save('44.55',R_emission_m=R,D_emission_m=R*math.pi/3,H_s=.001/R,V_m_s=.001*math.pi/3,flight_s=dt,flight_yr=dt/year,R_arrival_m=R*ratio,lambda_received_nm=ratio)
for i,(m,M,b0) in enumerate([(1,1,.8),(.5,2,.6),(.1057,.9383,.99),(.9383,.9383,.999),(.000511,.9383,.9999)]):
 g=1/math.sqrt(1-b0*b0);Et=g*m+M;p=g*m*b0;bc=p/Et;gc=1/math.sqrt(1-bc*bc)
 assert abs(gc*(p-bc*Et))<1e-11
 assert math.isclose(gc*(Et-bc*p),math.sqrt(m*m+M*M+2*M*g*m),rel_tol=1e-10)
 save(f'44.56_case{i+1}',m=m,M=M,beta0=b0,betaCM=bc,energyCM=gc*(Et-bc*p))
save('44.57',photon_MeV=.511)
save('44.58',delay_s=.06/c)
save('44.59',transmitted_fraction=math.exp(-.1*20))
kn,kpi=two(1116,939.6,135);save('Bridge',K_neutron=kn,K_pion=kpi,neutron_fraction=kn/(kn+kpi),pion_fraction=kpi/(kn+kpi),photonObserved_MeV=135/2*.12)
assert math.isclose(out['44.36']['F_N'],410.1471204,rel_tol=.001)
assert .37<out['44.51']['R_m']<.38
assert .6<out['44.45']['H_rem']<.8
q=ROOT/'qa/physics/chapter44';q.mkdir(parents=True,exist_ok=True)
(q/'end-parent-numeric.json').write_text(json.dumps(dict(status='passed',cases=out),ensure_ascii=False,indent=2),encoding='utf-8')
print('Actual chapter44 numerical ledger:',len(out),'cases; source/prose/browser review remains separate.')
