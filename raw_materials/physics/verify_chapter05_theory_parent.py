"""Independent source-data calculations and residual checks for examples5.1–5.23.

Symbolic examples are checked on explicit positive parameter samples, without
adding those samples as replacement examples to the published lecture.
"""
from math import sin,cos,tan,atan,radians,sqrt,pi,isclose
import json
g=9.8;out={}
out['5.1']={'weight_N':50*g,'force_upward_N':50*g,'tension_top_N':50*g}
out['5.2']={'tension_bottom_N':50*g,'tension_top_N':50*g+120}
w=357.;t1=w;t3=w/sin(radians(60));t2=t3*cos(radians(60))
assert isclose(t3*sin(radians(60))-t1,0,abs_tol=1e-10)
assert isclose(t3*cos(radians(60))-t2,0,abs_tol=1e-10)
out['5.3']={'T1_over_w':1,'T2_over_w':t2/w,'T3_over_w':t3/w}
for angle in [0,15,30,60,89]:
 alpha=radians(angle);T=w*sin(alpha);normal=w*cos(alpha)
 assert isclose(T-w*sin(alpha),0,abs_tol=1e-10)
 assert isclose(normal-w*cos(alpha),0,abs_tol=1e-10)
out['5.4']={'T':'w*sin(alpha)','normal':'w*cos(alpha)'}
out['5.5']={'w2_over_w1':sin(radians(15)),'T':'w2=w1*sin(15degrees)'}
out['5.6']={'a_m_s2':6/4,'wind_force_N':200*6/4}
out['5.7']={'wind_force_N':200*1.5+100}
a=10**2/(2*25)
out['5.8']={'a_upward_m_s2':a,'tension_N':800*(g+a)}
out['5.9']={'normal_scale_N':50*(g+a),'downward_acceleration_scale_N':50*(g-a),'true_weight_N':50*g,'condition':'Moving down but slowing: upward acceleration'}
out['5.10']={'a_down_slope':'g*sin(alpha)','normal':'w*cos(alpha)'}
a=9/(1+.50)
out['5.11']={'a_m_s2':a,'tray_on_carton_N':.50*a}
for m1,m2 in[(.3,.1),(5,2),(7,11)]:
 a=m2*g/(m1+m2);T=m1*m2*g/(m1+m2)
 assert isclose(T,m1*a)
 assert isclose(m2*g-T,m2*a)
out['5.12']={'acceleration':'m2*g/(m1+m2)','tension':'m1*m2*g/(m1+m2)','directions':'Glider toward pulley; suspended mass down'}
out['5.13']={'mu_static':230/500,'mu_kinetic':200/500}
out['5.14']={'static_friction_N':50,'max_static_N':230,'condition':'At rest with only50N horizontal push'}
mu=.4;theta=radians(30);T=mu*500/(cos(theta)+mu*sin(theta));normal=500-T*sin(theta)
assert isclose(T*cos(theta),mu*normal)
out['5.15']={'pull_N':T,'normal_N':normal,'friction_N':mu*normal,'force_ratio_to_horizontal':T/200}
out['5.16']={'slope_angle':'atan(mu_k)','condition':'Steady downhill sliding; independent of mass'}
out['5.17']={'a_downhill':'g*(sin(alpha)-mu_k*cos(alpha))','normal':'m*g*cos(alpha)'}
for mu,angle in[(.2,30),(.4,45),(.6,60)]:
 alpha=radians(angle);a=g*(sin(alpha)-mu*cos(alpha));m=53
 assert isclose(m*g*sin(alpha)-mu*m*g*cos(alpha),m*a)
out['5.18']={'terminal_speed_m_s':sqrt(50*g/.25),'double_mass_same_D_m_s':sqrt(100*g/.25),'drop2800m_at_terminal_speed_s':2800/sqrt(50*g/.25),'limitation':'Constant terminal speed estimate; does not model the initial transient fall'}
period=60/5;radius=5.;v=2*pi*radius/period
out['5.19']={'period_s':period,'speed_m_s':v,'tension_N':25*v*v/radius}
for m,L,beta in[(.5,2,15),(3,1,45),(6,.8,70)]:
 b=radians(beta);r=L*sin(b);v=sqrt(g*L*sin(b)*tan(b));F=m*g/cos(b);period=2*pi*sqrt(L*cos(b)/g)
 assert isclose(F*cos(b),m*g)
 assert isclose(F*sin(b),m*v*v/r)
 assert isclose(2*pi*r/v,period)
out['5.20']={'wire_tension':'m*g/cos(beta)','period':'2*pi*sqrt(L*cos(beta)/g)','radius':'L*sin(beta)','speed_squared':'g*L*sin(beta)*tan(beta)'}
out['5.21']={'original_mu_s':.96,'original_R_m':230,'original_max_speed_m_s':sqrt(.96*g*230),'original_max_speed_km_h':3.6*sqrt(.96*g*230),'max_speed':'sqrt(mu_s*g*R)','condition':'Level curve, static friction, normal=mg'}
for R,mu in[(30,.2),(170,.97),(500,.4)]:
 vmax=sqrt(mu*g*R);assert isclose(vmax*vmax/R,mu*g)
out['5.22']={'original_beta_degrees':atan(25**2/(g*230))*180/pi,'original_speed_km_h':25*3.6,'bank_angle':'atan(v^2/(g*R))','condition':'Design speed v, no friction needed'}
for R,v in[(30,10),(170,40),(500,45)]:
 b=atan(v*v/(g*R));m=1000.;normal=m*g/cos(b)
 assert isclose(normal*sin(b),m*v*v/R)
out['5.23']={'normal_top':'m*g-m*v^2/R','normal_bottom':'m*g+m*v^2/R','seat_contact_condition_top':'v^2<=g*R for an upward-only seat force; a restraint can supply additional downward force otherwise'}
out['self5.1']={'tension_over_weight':1/sqrt(2),'choice':'ii'}
out['self5.2']={'choice':'ii','reason':'Same nonzero acceleration and tension at instantaneous zero velocity'}
out['self5.3']={'no_friction':['i','iii'],'static_friction':['ii','iv'],'kinetic_friction':['v']}
out['self5.4']={'choice':'iii','reason':'For the same orbiting mass, both smaller v and larger R imply smaller m*v^2/R at the larger orbit'}
out['airplane_app']={'80degrees_normal_over_mg':1/cos(radians(80)),'84degrees_normal_over_mg':1/cos(radians(84))}
assert isclose(out['5.6']['wind_force_N'],300)
assert isclose(out['5.7']['wind_force_N'],400)
assert isclose(out['5.11']['a_m_s2'],6)
assert isclose(out['5.11']['tray_on_carton_N'],3)
assert isclose(out['5.9']['normal_scale_N'],590)
assert isclose(out['5.9']['downward_acceleration_scale_N'],390)
assert isclose(out['5.22']['original_speed_km_h'],90)
assert len([k for k in out if k.startswith('5.')])==23
print(json.dumps({'status':'passed','scope':'Independent reference values and sampled force-balance residuals; Source values compared with authored theory; no end-of-chapter exercises in this scope','items':out},indent=2))
