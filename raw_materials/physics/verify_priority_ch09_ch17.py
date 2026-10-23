"""Independent recomputation of the actual source teaching examples in chapters9 and17.

Private QA ledgers are written under qa, never included in the lecture text.
"""
from pathlib import Path
import math,json
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2];Q=ROOT/'qa/physics1-priority'
cases={}
def save(key,**values):
 assert all(math.isfinite(v) for v in values.values() if isinstance(v,(float,int)))
 cases[key]=values
def close(a,b,rel=1e-10,abs_=1e-10):assert math.isclose(a,b,rel_tol=rel,abs_tol=abs_),(a,b)
theta=lambda t:2*t**3;omega=lambda t:6*t*t;alpha=lambda t:12*t
save('9.1',diameter_m=.36,t1_s=2,t2_s=5,theta1_rad=theta(2),theta2_rad=theta(5),arc_m=.18*(theta(5)-theta(2)),omega_average=(theta(5)-theta(2))/3,omega1=omega(2),omega2=omega(5))
close(cases['9.1']['arc_m'],42.12)
save('9.2',alpha_average=(omega(5)-omega(2))/3,alpha1=alpha(2),alpha2=alpha(5))
close(cases['9.2']['alpha_average'],42)
save('9.3',omega_rad_s=27.5-10*.300,theta_rad=27.5*.300-.5*10*.300**2,extraAngle_deg=(27.5*.300-.5*10*.300**2)*180/math.pi-360)
save('9.4',a_t_m_s2=.8*50,a_r_m_s2=.8*10**2,a_total=math.hypot(.8*50,.8*10**2),a_total_doubled_omega=math.hypot(.8*50,.8*20**2))
w=2400*2*math.pi/60;r=math.sqrt(270**2-75**2)/w
save('9.5',rpm=2400,planeSpeed_m_s=75,tipMaximum_m_s=270,radius_m=r,alpha_centripetal=w*w*r)
I1=.10*.50**2+.20*.40**2;I2=.30*.40**2
save('9.6',I_axis1=I1,I_axis2=I2,K_axis1_at4rad_s=.5*I1*4**2)
close(I1,.057);close(I2,.048)
I=.5*50*.060**2;W=9*2;w=math.sqrt(2*W/I)
save('9.7',M_kg=50,diameter_m=.120,force_N=9,distance_m=2,I_kg_m2=I,work_J=W,omega=w,cableSpeed_m_s=w*.060)
for j,(m,M,R,h) in enumerate([(1,2,.1,1),(.3,5,.2,.75),(4,1,.06,.5)]):
 v=math.sqrt(2*m*9.8*h/(m+M/2));w=v/R
 close(m*9.8*h,.5*m*v*v+.5*(.5*M*R*R)*w*w)
 save('9.8_case'+str(j+1),m=m,M=M,R=R,h=h,v=v,omega=w)
save('9.9',I_offset=.132,M_kg=3.6,d_m=.15,I_cm=.132-3.6*.15**2)
close(cases['9.9']['I_cm'],.051)
for j,(rho,L,R1,R2) in enumerate([(1200,.4,0,.1),(2700,1,.3,.7),(1000,.6,.59,.6)]):
 M=rho*math.pi*(R2**2-R1**2)*L
 integral=quad(lambda r:2*math.pi*rho*L*r**3,R1,R2)[0]
 exact=.5*M*(R1*R1+R2*R2);close(integral,exact)
 save('9.10_case'+str(j+1),rho=rho,L=L,R1=R1,R2=R2,M=M,I_integral=integral,I_exact=exact)
for j,(rho,R) in enumerate([(2700,.2),(1000,1),(7800,.05)]):
 M=4*math.pi*rho*R**3/3
 integral=quad(lambda x:.5*math.pi*rho*(R*R-x*x)**2,-R,R)[0]
 exact=.4*M*R*R;close(integral,exact)
 save('9.11_case'+str(j+1),rho=rho,R=R,M=M,I_integral=integral,I_exact=exact)
# Actual17.1 ice32F to body98.60F, not a fever problem.
C1=(32-32)*5/9;C2=(98.60-32)*5/9
save('17.1',F1=32.00,F2=98.60,C1=C1,C2=C2,K1=C1+273.15,K2=C2+273.15,deltaC=C2-C1,deltaK=C2-C1)
close(C2,37)
# Actual17.2 tape50.000m, not35m; measurement remains35.794m.
a=1.2e-5;dt=15
save('17.2',tapeLength20C_m=50,tapeLength35C_m=50*(1+a*dt),reading_m=35.794,actualDistance_m=35.794*(1+a*dt))
close(cases['17.2']['tapeLength35C_m'],50.009)
save('17.3',initial_cm3=200,deltaT=80,beta_mercury=18e-5,alpha_glass=.40e-5,overflow_cm3=(18e-5-3*.40e-5)*200*80)
stress=-7e10*2.4e-5*(22.3-17.2)
save('17.4',L_m=.10,A_m2=20e-4,Y_Pa=7e10,alpha_Kinv=2.4e-5,deltaT_K=22.3-17.2,stress_Pa=stress,forceEachWall_N=abs(stress)*20e-4)
cw=4190.;ccu=390.;cal=4.186
save('17.5',mass_kg=80,deltaT=2,Q_waterApprox_J=80*cw*2,Q_waterApprox_kcal=80*cw*2/(1000*cal),Q_bodySpecific_J=80*3480*2)
save('17.6',mass_kg=23e-6,power_W=7.4e-3,c_J_kgK=705,dT_K_s=7.4e-3/(23e-6*705),dT_K_min=60*7.4e-3/(23e-6*705))
tf=(.3*cw*70+.12*910*20)/(.3*cw+.12*910)
q1=.3*cw*(tf-70);q2=.12*910*(tf-20);close(q1+q2,0,abs_=1e-8)
save('17.7',coffee_kg=.300,cup_kg=.120,coffeeInitial_C=70,cupInitial_C=20,Tfinal_C=tf,coffeeQ_J=q1,cupQ_J=q2)
Lf=3.34e5;Lv=2.256e6;ci=2100.
mice=.25*cw*25/(ci*20+Lf)
save('17.8',cola_kg=.25,colaInitial_C=25,iceInitial_C=-20,final_C=0,ice_kg=mice)
t_if_liquid=(.1*cw*25+2*ccu*150)/(.1*cw+2*ccu)
available=2*ccu*(150-100)-.1*cw*(100-25);steam=available/Lv
assert t_if_liquid>100 and 0<steam<.1
save('17.9',copper_kg=2,copperInitial_C=150,water_kg=.10,waterInitial_C=25,liquidOnlyTrial_C=t_if_liquid,final_C_standardBoilingModel=100,steam_kg=steam,steamFraction=steam/.1,waterMassAllBoilsBoundary_kg=2*ccu*50/(cw*75+Lv))
needed=cw*80+.25*Lv
save('17.10',sensible_J=cw*80,latent_J=.25*Lv,total_J=needed,stoveFraction=.30,gasolineCombustion_J_g=46000,gasoline_g=needed/(.30*46000))
heat=.027*.8*30/.020
save('17.11',conductivity=.027,area_m2=.80,thickness_m=.020,deltaT=30,H_W=heat,meltedIce_3h_kg=heat*10800/Lf)
ks=50.2;kcu=385;A=.020**2;Ls=.1;Lcu=.2
T=(ks/Ls*100)/(ks/Ls+kcu/Lcu);H=ks*A*(100-T)/Ls
close(H,kcu*A*T/Lcu)
save('17.12',k_steel=ks,k_copper=kcu,L_steel=Ls,L_copper=Lcu,area_m2=A,junction_C=T,H_W=H)
save('17.13',steelH_W=ks*A*100/Ls,copperH_W=kcu*A*100/Lcu,totalH_W=ks*A*100/Ls+kcu*A*100/Lcu)
sig=5.67e-8
save('17.14',side_m=.10,totalTwoFaceArea_m2=.020,emissivity=.60,T_K=1073,emitted_W=.020*.60*sig*1073**4)
save('17.15',area_m2=1.2,emissivity=1,body_K=303,surroundings_K=293,emitted_W=1.2*sig*303**4,net_W=1.2*sig*(303**4-293**4))
save('17.6_selfcheck',heat_to_melt_per_kg=Lf,heat_to_warm_per_kg=cw*100,heat_to_boil_per_kg=Lv,halfEnergy_per_kg=(Lf+cw*100+Lv)/2)
assert (Lf+cw*100)<cases['17.6_selfcheck']['halfEnergy_per_kg']<(Lf+cw*100+Lv)
Q.mkdir(parents=True,exist_ok=True)
(Q/'actual-ch09-ch17-numerical-ledger.json').write_text(json.dumps(dict(status='passed',cases=cases,limitations=['Numbers alone do not certify source completeness or correct prose.','17.9 source textbook boiling calculation assumes the stated boiling model; a sealed rigid vessel requires volume/pressure data for a complete physical specification.']),ensure_ascii=False,indent=2),encoding='utf-8')
print('Passed',len(cases),'actual-source numerical cases, including11chapter9examples and15chapter17examples with independentintegrals/energychecks.')
