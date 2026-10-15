from math import sqrt,pi,isclose
import json
import numpy as np
c=3e8
def close(a,b):assert np.allclose(a,b,rtol=1e-10,atol=1e-12),(a,b)
r={}
b=np.array([.70,.80,.85,.88,.90,.92,.94]);t=np.array([3.57,4.41,5.02,5.47,6.05,6.58,7.62])
x=1/(1-b*b);y=t*t
slope,offset=np.polyfit(x,y,1);pred=slope*x+offset;r2=1-np.sum((pred-y)**2)/np.sum((y-y.mean())**2)
sl0=x@y/(x@x)
assert r2>.995
r['37.63']={'points':7,'slope_in_1e16_s2':slope,'offset_in_1e16_s2':offset,'R2':r2,'rest_lifetime_s':sqrt(slope)*1e-8,'zero_intercept_lifetime_s':sqrt(sl0)*1e-8,'beta_lifetime_fourfold':sqrt(15)/4}
r['37.64']={'drag_coefficient':1-1/1.333**2,'expansion':'w=c/n+(1-1/n^2)V+O(V^2/c)'}
b=np.array([.60,.65,.70,.75,.80,.85]);a=np.array([20.3,17.9,14.8,11.2,8.5,5.9])*1e3
x=(1-b*b)**1.5;slope,offset=np.polyfit(x,a,1);pred=slope*x+offset;r2=1-np.sum((pred-a)**2)/np.sum((a-a.mean())**2)
m=8e-14/slope
assert r2>.995
r['37.65']={'points':6,'slope_m_s2':slope,'offset_m_s2':offset,'R2':r2,'mass_kg':m,'acceleration_at100m_s_m_s2':8e-14*(1-(100/c)**2)**1.5/m,'zero_intercept_mass_kg':8e-14/(x@a/(x@x))}
f=np.array([7.1,5.4,6.1,8.1]);f0=np.array([9.2,8.6,7.9,8.9]);betas=(f0*f0-f*f)/(f0*f0+f*f)
r['37.66']={'betas':dict(zip('ABCD',betas.tolist())),'highest':'B','lowest':'D','B_approach_THz':f0[1]**2/f[1]}
# Lorentz boosts preserve the oriented area in the (x,ct) plane.
area_checks=[]
for b in [.2,.6,.9]:
 gamma=1/sqrt(1-b*b);M=gamma*np.array([[1,-b],[-b,1]])
 p=np.array([[0,0],[-1,0],[0,1.3],[-1,1.3]])
 transformed=p@M.T
 area=abs(np.linalg.det(np.stack([transformed[1],transformed[2]])))
 close(area,1.3);area_checks.append({'beta':b,'area':area})
r['37.67']={'area_formula':'LcT','checks':area_checks}
f0=4.568110e14;fmin=4.567710e14;fmax=4.568910e14
fc=(fmin+fmax)/2;u=c*(fc-f0)/f0;v=c*(fmax-fmin)/(2*f0);T=11*86400;R=v*T/(2*pi);G=6.67e-11;m=4*v*v*R/G
r['37.68']={'center_frequency_Hz':fc,'center_approach_m_s':u,'orbital_speed_m_s':v,'period_s':T,'radius_m':R,'mass_each_kg':m,'mass_each_solar':m/1.99e30,'radius_over_EarthSun':R/1.5e11}
M=938.3;k=493.7;W=2*M+2*k
K=(W*W-4*M*M)/(2*M);E=M+K;p=sqrt(E*E-M*M);bc=p/(E+M);gamma=1/sqrt(1-bc*bc)
close((E+M)/gamma,W)
r['37.69']={'fixed_target_threshold_MeV':K,'combined_kaon_rest_MeV':2*k,'threshold_over_kaon_rest':K/(2*k),'colliding_beams_total_K_MeV':2*k,'CM_speed_beta':bc}
checks=[]
for b in [.1,.4,.9]:
 gamma=1/sqrt(1-b*b)
 # Coefficients on A^2, AB, B^2 for spatial derivative squared minus temporal.
 Cx=np.array([1.,-b]);Ct=np.array([-b,1.])
 coef=gamma*gamma*(np.array([Cx[0]**2,2*Cx[0]*Cx[1],Cx[1]**2])-np.array([Ct[0]**2,2*Ct[0]*Ct[1],Ct[1]**2]))
 close(coef,[1,0,-1]);checks.append(dict(beta=b,lorentz_coefficients=coef.tolist(),galileo_coefficients=[1-b*b,2*b,-1]))
r['37.70']={'lorentz_operator_invariant':True,'checks':checks}
assert len(r)==8
print(json.dumps(dict(status='passed',results=r),indent=2))
