"""Independent checks for the actual chapter14earlytheoryprose proposal."""
from pathlib import Path
import math,json
from scipy.integrate import solve_ivp

OUT=Path(__file__).resolve().parent
results={};checks=[]
def eq(id,a,b,rel=1e-10,absolute=1e-10):
 assert math.isclose(a,b,rel_tol=rel,abs_tol=absolute),(id,a,b)
 checks.append(dict(id=id,actual=float(a),expected=float(b),passed=True))

f=6.7e6;T=1/f;w=2*math.pi*f
eq('14.1:microsecondconversion',T*1e6,.14925373134328357)
results['14.1']=dict(T_s=T,T_microsecond=T*1e6,omega_rad_s=w)
k=6/.030;m=.5;A=.020;w=math.sqrt(k/m)
eq('14.2:k',k,200.)
eq('14.2:omega',w,20.)
results['14.2']=dict(k_N_m=k,omega_rad_s=w,f_Hz=w/(2*math.pi),T_s=2*math.pi/w,A_m=A)
x0=.015;v0=.40;amplitude=math.hypot(x0,v0/w);phase=math.atan2(-v0/w,x0)
eq('14.3:A',amplitude,.025)
eq('14.3:cosphi',math.cos(phase),.6)
eq('14.3:sinphi',math.sin(phase),-.8)
results['14.3']=dict(A_m=amplitude,phi_rad=phase,phi_deg=math.degrees(phase),T_s=2*math.pi/w,v_coefficient_m_s=-w*amplitude,a_coefficient_m_s2=-w*w*amplitude)
for initialx,initialv in[(.015,.4),(-.015,.4),(-.015,-.4),(.015,-.4),(0.,.4),(0.,-.4),(.02,0.),(-.02,0.)]:
 amp=math.hypot(initialx,initialv/w);phi=math.atan2(-initialv/w,initialx)
 eq('phase:reconstructx',amp*math.cos(phi),initialx)
 eq('phase:reconstructv',-w*amp*math.sin(phi),initialv)
 # Integrate NewtonODE, independentoftrigonometricconstruction.
 ode=solve_ivp(lambda t,y:[y[1],-k/m*y[0]],(0,.4),[initialx,initialv],rtol=1e-11,atol=1e-12,dense_output=True)
 for t in(.05,.13,.4):
  numeric=ode.sol(t)
  eq('SHM:ODEx',float(numeric[0]),amp*math.cos(w*t+phi),rel=1e-8,absolute=1e-10)
  eq('SHM:ODEv',float(numeric[1]),-w*amp*math.sin(w*t+phi),rel=1e-8,absolute=1e-10)
x=.010;vx=-math.sqrt(k/m)*math.sqrt(A*A-x*x);ax=-k/m*x
E=k*A*A/2;U=k*x*x/2;K=m*vx*vx/2
eq('14.4:energy',K+U,E)
eq('14.4:quarterpotential',U/E,.25)
eq('14.4:halfkineticx',(.5*k*(A/math.sqrt(2))**2)/E,.5)
results['14.4']=dict(v_max_m_s=w*A,v_min_m_s=-w*A,a_max_m_s2=w*w*A,a_min_m_s2=-w*w*A,v_at_halfA_m_s=vx,a_at_halfA_m_s2=ax,E_J=E,U_J=U,K_J=K)
cases=[]
for M,putty,kk,amp in[(1,.2,2,.3),(3,2,8,.5),(.5,.5,200,.02),(5,.1,17,.7)]:
 v1=math.sqrt(kk/M)*amp;v2=M/(M+putty)*v1;E1=kk*amp*amp/2;E2=(M+putty)*v2*v2/2
 A2=math.sqrt(2*E2/kk);newT=2*math.pi*math.sqrt((M+putty)/kk)
 eq('14.5:horizontalmomentum',M*v1,(M+putty)*v2)
 eq('14.5:energyfraction',E2/E1,M/(M+putty))
 eq('14.5:amplituderatio',A2/amp,math.sqrt(M/(M+putty)))
 eq('14.5:turningpointA',math.sqrt(2*E1/kk),amp)
 cases.append(dict(M=M,m=putty,k=kk,A1=amp,A2_equilibrium=A2,A2_turningpoint=amp,T2=newT))
results['14.5']=dict(parameterCases=cases,scope='Horizontaloscillationenergy,notverticalimpactenergy')
massperson=980/9.8;kcar=980/.028;mtotal=1000+massperson;Tcar=2*math.pi*math.sqrt(mtotal/kcar)
eq('14.6:personmass',massperson,100.)
eq('14.6:stiffness',kcar,35000.)
results['14.6']=dict(person_mass_kg=massperson,total_mass_kg=mtotal,k_N_m=kcar,T_s=Tcar,f_Hz=1/Tcar)
U0=1.68e-21;R0=3.82e-10;atomic=39.948*1.66e-27;kmol=72*U0/R0**2
fixed=math.sqrt(kmol/atomic)/(2*math.pi);mu=atomic/2;free=math.sqrt(kmol/mu)/(2*math.pi)
eq('14.7:reducedmassfactor',free/fixed,math.sqrt(2))
results['14.7']=dict(k_N_m=kmol,atomic_mass_kg=atomic,reduced_mass_kg=mu,f_fixed_atom_Hz=fixed,f_bothfree_atoms_Hz=free)
for q in(.9,.98,1.,1.02,1.2):
 # Algebraicallyequivalentqandzformsusedtokeepformulasreadable.
 z=1/q;dimensionlessForce=12*(q**13-q**7)
 eq('14.26vs14.27',dimensionlessForce,12*(z**-13-z**-7))
 delta=1e-6
 def potential(ratio):return ratio**-12-2*ratio**-6
 radial=1/q
 forceDerivative=-(potential(radial+delta)-potential(radial-delta))/(2*delta)
 eq('14.26:potentialderivative',dimensionlessForce,forceDerivative,rel=1e-7,absolute=2e-7)
for n in(-13,-7):
 u=1e-5
 truncated=1+n*u+n*(n-1)*u*u/2+n*(n-1)*(n-2)*u**3/6
 eq('14.28:binomial',truncated,(1+u)**n,rel=1e-12)
for u in(-1e-5,1e-5):
 force=12*((1+u)**-13-(1+u)**-7)
 eq('14.29:linearrestoring',force/(-72*u),1.,rel=2e-4)
selfchecks={
 '14.1':{'xSigns':['negative','positive','negative','positive','positive','zero'],'reason':'aoppositexregardlessv'},
 '14.2':{'a':{'A':'greaterthan.1','phi':'negativeprincipalbranch'},'b':{'A':'greaterthan.1','phi':'positiveprincipalbranch'}},
 '14.3':{'amplitudeChoice':3,'amplitudeFactor':math.sqrt(2),'frequencyChoice':5,'frequencyChange':1},
 '14.4':{'choice':1,'periodMars_s':10.,'staticExtensionRatio':.4}}
eq('TY14.3:doubleenergy',math.sqrt(2)**2,2.)
assert len(results)==7 and len(selfchecks)==4
report=dict(status='passed',scope='Chapter14earlytheoryproseproposal,notpublicrenderacceptance',exampleIds=list(results),examples=results,selfchecks=selfchecks,openingQuestion={'choice':1,'law':'stepfrequencyproportional1/sqrtL'},numericAssertions=len(checks),assertions=checks,privateClarifications=['Microsecondunitpreserved.','atan2phasequadrantsandA0phaseirrelevanceexplicit.','Ar2fixed/freebothretained.','Puttycollisionenergyrestrictedhorizontaloscillation.','VanDerWaalsq/u/zandbinomialP1/P2/P3areexplicitlydefinedequivalentsourceformulas.'])
print(json.dumps(report,ensure_ascii=False,indent=2))
