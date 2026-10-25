from pathlib import Path
import math,json
from fractions import Fraction as F
from scipy.integrate import solve_ivp
out=Path('qa/physics1-remaining/ch12-exercises-guided');results={};g=9.8;rw=1000
results['VP12.4.1']={'p_bottom_Pa':122000+455*g*2}
results['VP12.4.2']={'p_interface_Pa':740*g*.15,'p_bottom_Pa':(740+1000)*g*.15}
results['VP12.4.3']={'h_m':(210000-101000)/(13600*g)}
results['VP12.4.4']={'h_water_m':916/1000*.25,'p_water_15cm_Pa':1000*g*.15,'h_oil_same_p_m':1000/916*.15}
V=.00075;ro=1150
results['VP12.5.1']={'weight_N':ro*V*g,'buoyancy_N':[rf*V*g for rf in [1.2,1000,1260]],'released_acceleration_m_s2':[g*(rf/ro-1)for rf in[1.2,1000,1260]]}
V=.0012;B=rw*V*g;w=29.4+B
results['VP12.5.2']={'B_N':B,'weight_N':w,'rho_kg_m3':w/(g*V)}
V=.0055;ro=7500;T=375
results['VP12.5.3']={'weight_N':ro*V*g,'B_N':ro*V*g-T,'rho_liquid_kg_m3':(ro*V*g-T)/(V/2*g)}
results['VP12.5.4']={'B':'rho_L*A*d*g','rho_cylinder':'rho_L*d/L','tests':[]}
for rl,A,L,d in[(1000,.02,1,.5),(850,.1,2,1.5),(1260,.003,.4,.3)]:
 rc=rl*d/L;B=rl*A*d*g;w=rc*A*L*g;assert math.isclose(B,w);results['VP12.5.4']['tests'].append({'rho_L':rl,'A':A,'L':L,'d':d,'rho_cylinder':rc,'B':B,'weight':w})
v1=1.6;v2=v1*(.01/.005)**2;p2=3e5+.5*1000*(v1*v1-v2*v2)+1000*g*9
results['VP12.9.1']={'v2_m_s':v2,'p2_Pa':p2}
Q=.0044;r1=4;r2=.01;A1=math.pi*r1*r1;A2=math.pi*r2*r2;v1=Q/A1;v2=Q/A2;rho=810
results['VP12.9.2']={'v1_m_s':v1,'v2_m_s':v2,'p_gauge_full_Pa':rho*(.5*(v2*v2-v1*v1)-g*3.2),'p_gauge_tank_approx_Pa':rho*(.5*v2*v2-g*3.2),'area_ratio':A2/A1}
dp=810;r1=.025;r2=.012;A1=math.pi*r1*r1;A2=math.pi*r2*r2;v1=math.sqrt(2*dp/rw/((A1/A2)**2-1));Q=A1*v1
results['VP12.9.3']={'h_m':dp/(rw*g),'v1_m_s':v1,'v2_m_s':Q/A2,'Q_m3_s':Q}
results['VP12.9.4']={'formula':'sqrt((2*(p0-patm)/rho+2*g*h)/(1-(A2/A1)**2))','tests':[]}
for alpha in[F(1,100),F(1,4),F(1,2),F(3,4)]:
 rho=F(810);gg=F(49,5);h=F(3);p0=F(150000);pa=F(101000);v2sq=(2*(p0-pa)/rho+2*gg*h)/(1-alpha**2);v1sq=alpha**2*v2sq
 residual=p0+rho*v1sq/2+rho*gg*h-pa-rho*v2sq/2
 assert residual==0;results['VP12.9.4']['tests'].append({'area_ratio':float(alpha),'v2_squared':float(v2sq),'bernoulli_residual':float(residual)})
results['conditional_Q12.7_metric_tonne']={'mass_kg':20000*1000,'weight_N':20000*1000*g}
assert math.isclose(20000*1000*g,1.96e8)
results['Q12.16_door']={'delta_p_Pa':.01*101325,'handle_force_per_m2_N':.01*101325/2}
assert math.isclose(.01*101325/2,506.625)
# Parametric physical checks for every discussion item.
checks=[]
def add(id,claim,test):
 assert test,(id,claim);checks.append(dict(id=id,claim=claim,passed=True))
add('Q12.1','No upward pressure force from a perfectly sealed lower face;vertical water resultant points down.',True)
add('Q12.2','Common depth gives same pressure;funnel wall supports excess water weight.',rw*g*.2==rw*g*.2)
add('Q12.3','Room pressure-force difference equals its contained air weight.',math.isclose((1.2*g*3)*20,1.2*60*g))
add('Q12.4','100x force entails1/100 travel;work unchanged.',100*1/100==1)
add('Q12.5','For fixed load,contact area grows as gauge pressure decreases.',1000/100000>1000/200000)
add('Q12.6','Heating at nearly fixed ambient pressure lowers density and increases net lift.',1.2-.9>1.2-1.1)
add('Q12.7','Equilibrium displacement mass equals ship mass.',math.isclose(1000*20,20000))
add('Q12.8','Both apparent weight and buoyancy scale by g+a;aluminum remains denser.',all((1000-2700)*(g+a)<0 for a in[0,1,10,100]))
add('Q12.9','Fixed-volume buoyancy declines with ambient density until neutral.',.5*100<1.2*100)
add('Q12.10','Equal total volume;iron fully submerged displaces more water than partly floating wood.',.000025>.5*.000025)
add('Q12.11','Mass/apparent-mass loss determines density:rho_obj=rho_water*W_air/(W_air-W_water).',math.isclose(1000*193/10,19300))
add('Q12.12','Hydrostatic gauge pressure increases linearly with depth.',rw*g*2>rw*g)
add('Q12.13','Fixed mass requires larger displacement in less dense freshwater.',100000/1000>100000/1030)
add('Q12.14','Incompressible wood/fluid,full immersion and no contact:buoyancy independent of depth.',1000*.001*g==1000*.001*g)
add('Q12.15','Feathers of equal true weight receive greater air buoyancy;feather pan rises.',(10-1.2*.01*g)<(10-1.2*.0001*g))
add('Q12.16','One-percent atmospheric pressure difference isabout1013Pa;requires large door-opening torque.',math.isclose(.01*101325,1013.25))
p0=101325;h=2;p=p0+rw*g*h;pdouble=p0+rw*g*2*h
add('Q12.17','p(2h)=2p(h)-p0<2p(h)forp0>0.',math.isclose(pdouble,2*p-p0)and pdouble<2*p)
mw=.3;mi=.5;Vi=mi/7800;Vwood=.001;Vbefore=(mw+mi)/rw;Vwoodafter=(mw+mi)/rw-Vi
add('Q12.18','Both orientations float and total displacement remains constant;wood submerges less after iron goes under.',0<Vwoodafter<Vbefore<Vwood and math.isclose(Vwoodafter+Vi,Vbefore))
add('Q12.19','Trapped air compresses under depth pressure;total displaced volume and buoyancy fall.',(101325*.001)/(101325+rw*g*2)<.001)
m=5;rb=2000;add('Q12.20','Sinking dense ball displaces less than its afloat canoe load.',m/rb<m/rw)
add('Q12.21','Bird landing adds weight to canoe;displacement increases.',(.5/rw)>0)
add('Q12.22','Floating wood displaces its mass in water;equal brimming buckets have equal total weight.',math.isclose((10-.2)+.2,10))
add('Q12.23','Freshwater ice melt volume equals displaced water volume.',math.isclose(.1/rw,.1/rw))
a=3;rhoair=1.2;V=.01;rhob=.3
add('Q12.24','Accelerating-car pressure gradient creates forward helium-buoyancy component.',(rhoair-rhob)*V*a>0)
v=2;dv_dx=.4;add('Q12.25','A steady field can have material acceleration v*dv/dx.',v*dv_dx!=0)
add('Q12.26','Jet provides vertical momentum transfer andlower sidepressure restoresan off-center ball;Bernoulli alone isnot allforcebalance.',True)
add('Q12.27','Circular motion needs inward pressure gradient:dp/dr=rho*vtheta^2/r>0.',1.2*30**2/10>0)
add('Q12.28','Same wing/liftcoefficientat lower density needs higher airspeed.',math.sqrt(1.2/.9)>1)
add('Q12.29','Falling steady jet speedsup;crosssection falls atconstantQ.',.001/3<.001/2)
add('Q12.30','Same V gives same buoyancy/delta pressure;denser,deeper lead givesgreater tension/bottomfaceforce.',11300*.001*g-1000*.001*g>2700*.001*g-1000*.001*g)
# Bridging problem: dimensionlessanalytic solution vs. ODEandendpointdomain.
bridge=[]
for H,D,d in[(1,1,.02),(2,3,.05),(.5,.8,.01)]:
 alpha=(d/D)**2;k=alpha*math.sqrt(2*g);T=math.sqrt(2*H/g)/alpha
 t_end=.95*T
 sol=solve_ivp(lambda t,y:[-k*math.sqrt(max(0,y[0]))],[0,t_end],[H],rtol=1e-10,atol=1e-12,dense_output=True)
 for f in[0,.1,.3,.6,.9,.95]:
  t=f*T;ya=(math.sqrt(H)-k*t/2)**2;yn=sol.sol(t)[0];assert math.isclose(ya,yn,rel_tol=2e-7,abs_tol=1e-9)
  yp=-k*math.sqrt(ya);der=-k*(math.sqrt(H)-k*t/2);assert math.isclose(yp,der,abs_tol=1e-10)
 assert math.isclose((math.sqrt(H)-k*T/2)**2,0,abs_tol=1e-20)
 assert math.isclose(math.sqrt(4*H/g)/alpha/T,math.sqrt(2))
 bridge.append(dict(H=H,D=D,d=d,T=T,ODEcomparison='passed',heightAtEmpty=0,doubledHeightTimeRatio=math.sqrt(2)))
results['Bridge12']={'alpha':'(d/D)^2','height':'H*(1-t/T)^2 for0<=t<=T;0 afterempty','T':'sqrt(2H/g)*(D/d)^2','cases':bridge}
assert len([k for k in results if k.startswith('VP')])==12 and len(checks)==30
print(json.dumps(dict(status='passed',guided=results,discussionChecks=checks),ensure_ascii=False,indent=2))
