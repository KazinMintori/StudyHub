"""Independent source DATA, isotope and decay-chain checks for chapter43."""
from pathlib import Path
import math,json
import numpy as np
from scipy.optimize import least_squares
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parents[2];Q=ROOT/'qa/physics/chapter43'
def main():
 data={};h=6.62607015e-34;c=299792458.;e=1.602176634e-19
 # Actual source seven-column photodisintegration table, PDF1501.
 wavelength=np.array([3.50,3.75,4.00,4.25,4.50,4.75,5.00])*1e-13
 speed=np.array([11.3,10.2,9.1,8.1,7.2,6.1,4.9])*1e6
 x=1e-13/wavelength;y=(speed/1e6)**2
 slope,intercept=np.polyfit(x,y,1);slope_si=slope*.1;intercept_si=intercept*1e12
 fitted_mp=h*c/slope_si;binding=-intercept_si*fitted_mp/e/1e6
 assert 1.60e-27<fitted_mp<1.75e-27 and 2.1<binding<2.4
 data['43.68']=dict(wavelength_m=wavelength.tolist(),speed_m_s=speed.tolist(),slope_SI=slope_si,intercept_SI=intercept_si,inferredProtonMass_kg=fitted_mp,inferredDeuteronBinding_MeV=binding,predictedSpeeds=np.sqrt(np.polyval([slope,intercept],x))*1e6)
 # Actual eleven-row activity table, not an invented generic exponential.
 t=np.array([0,.5,1,1.5,2,2.5,3,4,5,6,7]);a=np.array([20000,14800,11000,8130,6020,4460,3300,1810,1000,550,300])
 decay_slope,log_initial=np.polyfit(t,np.log(a),1);lam=-decay_slope;initial=math.exp(log_initial)
 assert abs(lam-.6)<.003 and abs(initial-20000)<60
 data['43.69']=dict(time_h=t.tolist(),activity_Bq=a.tolist(),lambda_perHour=lam,halfLife_h=math.log(2)/lam,initialActivity_Bq=initial,initialN=initial/(lam/3600),N_after7h=initial*math.exp(-lam*7)/(lam/3600),fit='Unweighted least squares of ln(activity) versus hours; data are approximate')
 # Actual fifteen-row mixed-sample table. Compare models, not a straight line forced through it.
 tm=np.array([0,.5,1,1.5,2,2.5,3,4,5,6,7,8,9,10,12]);am=np.array([7500,4120,2570,1790,1350,1070,872,596,404,288,201,140,98,68,33])
 def mixture(p):return p[0]*np.exp(-p[2]*tm)+p[1]*np.exp(-p[3]*tm)
 fit=least_squares(lambda p:mixture(p)-am,[5000,2500,1.8,.36],bounds=([0,0,0,0],[np.inf,np.inf,np.inf,np.inf]),x_scale='jac',ftol=1e-13,xtol=1e-13,gtol=1e-10)
 fit_one=least_squares(lambda p:p[0]*np.exp(-p[1]*tm)-am,[7500,.7],bounds=([0,0],[np.inf,np.inf]))
 assert fit.success
 assert sum(fit.fun**2)<sum(fit_one.fun**2)/100
 components=[]
 for amp,rate in sorted(zip(fit.x[:2],fit.x[2:]),key=lambda p:p[1],reverse=True):
  assert amp>0 and rate>0
  n0=amp/(rate/3600)
  components.append(dict(initialActivity_Bq=amp,lambda_perHour=rate,halfLife_h=math.log(2)/rate,initialN=n0,N_after5h=n0*math.exp(-rate*5)))
 assert .37<components[0]['halfLife_h']<.40 and 1.85<components[1]['halfLife_h']<2.00
 data['43.70']=dict(time_h=tm.tolist(),activity_Bq=am.tolist(),components=components,twoComponentSSE=float(sum(fit.fun**2)),oneComponentSSE=float(sum(fit_one.fun**2)),predictedActivity_Bq=mixture(fit.x).tolist(),residuals_Bq=fit.fun.tolist(),note='A positive two-exponential fit supports a minimum two components. Data do not uniquely exclude further nuclides. No precision or Poisson exposure time invented.')
 # Actual31microgramsU238perkgmantle, visually confirmed, not OCR milligrams.
 n_mantle=(31e-6/238)*6.02214076e23;lambda_u=math.log(2)/(4.47e9*3.156e7)
 a_mantle=n_mantle*lambda_u;p_mantle=a_mantle*52e6*e
 uranium_power=p_mantle*(2/3)*6e24;radiogenic=uranium_power/.39
 data['43.48']=dict(uranium_g_per_kg_mantle=31e-6,nuclei_per_kg=n_mantle,lambda_s=lambda_u,activity_Bq_per_kg=a_mantle,power_W_per_kg=p_mantle,uraniumHeat_W=uranium_power,radiogenicHeat_W=radiogenic,totalHeat_W=2*radiogenic)
 assert 1e13<uranium_power<1.5e13 and 6e13<2*radiogenic<7e13
 # Actual 9.4 microCi in source, visually confirmed, not OCR milliCi.
 initial_activity=9.4e-6*3.70e10;duration=1000;half_h=45*24
 remaining_activity=initial_activity*2**(-duration/half_h);worn_g=100*84/remaining_activity
 data['43.71']=dict(initialActivity_Bq=initial_activity,activityAfter1000h_Bq=remaining_activity,wornMass_g=worn_g,wear_g_per_h=worn_g/1000,wear_microg_per_h=worn_g/1000*1e6)
 assert 40<data['43.71']['wear_microg_per_h']<50
 l1=math.log(2)/2.46e5;l2=math.log(2)/7.54e4;t_eval=2.46e5
 fraction=l1/(l2-l1)*(math.exp(-l1*t_eval)-math.exp(-l2*t_eval))
 ode=solve_ivp(lambda t,n:[-l1*n[0],l1*n[0]-l2*n[1]],[0,t_eval],[1,0],rtol=1e-11,atol=1e-13)
 assert math.isclose(ode.y[1,-1],fraction,rel_tol=1e-9)
 daughter_mass=30*(230/234)*fraction
 data['43.72']=dict(correctAtomicNumbers=[92,90,88],halfLives_y=[2.46e5,7.54e4],daughterNumberFraction=fraction,daughterMass_g=daughter_mass,odeNumberFraction=float(ode.y[1,-1]))
 assert 4<daughter_mass<7
 # Source radioactive-iodine passage: read as a hypothetical physics calculation.
 nuclei=3.7e9*(8.04*86400)/math.log(2)
 reaction_q=(122.904270+1.007825-122.905589-1.008665)*931.5
 assert reaction_q<0 and 3.6e15<nuclei<3.8e15
 data['MCAT']=dict(iodine131Nuclei=nuclei,Te123ProductionQ_MeV=reaction_q)
 # Source production-with-decay bridge, solve ODE independently.
 rate=1.5e6;lam=math.log(2)/(25*60);sat=rate/lam
 ode=solve_ivp(lambda t,n:[rate-lam*n[0]],[0,15000],[0],rtol=1e-10,atol=1e-5)
 assert math.isclose(ode.y[0,-1],sat*(1-math.exp(-lam*15000)),rel_tol=1e-9)
 data['Bridge']=dict(production_s=rate,lambda_s=lam,saturationN=sat,saturationActivity_Bq=rate,daughter='Xe128, Z54; beta-minus changes Z53 to54')
 Q.mkdir(exist_ok=True)
 for record in data.values():
  for key,value in record.items():
   if isinstance(value,np.ndarray):record[key]=value.tolist()
 (Q/'independent-end-numeric.json').write_text(json.dumps(dict(status='passed',scope='Selected source tables, wear, Bateman, MCAT and Bridge; not all110solutions acceptance',cases=data),ensure_ascii=False,indent=2),encoding='utf-8')
 print('Passed actualDATA43.68–70,9.4microCiwear,BatemanODE,iodineandproduction-decaybridge.')
if __name__=='__main__':main()
