"""Independent residuals, numerical integrals and derivatives. Private QA only."""
from pathlib import Path
from math import sqrt,log,pi,sin,cos,tan,isclose
import runpy,json

root=Path(__file__).resolve().parents[2]
v=runpy.run_path(str(root/'raw_materials/physics/verify_chapter21.py'))
k,eps,e=v['k'],v['eps'],v['e']
simpson,field,force=v['simpson'],v['field'],v['force']
checks={}
def verify(name,actual,expected,tol=1e-6):
    a=actual if isinstance(actual,(list,tuple)) else [actual]
    b=expected if isinstance(expected,(list,tuple)) else [expected]
    for x,y in zip(a,b):
        assert isclose(x,y,rel_tol=tol,abs_tol=max(abs(y)*tol,1e-17)),(name,x,y)
    checks[name]={'actual':actual,'expected':expected}

# Finite source fields are integrated directly, rather than evaluated from the
# same closed form as the teaching solution.
Q,q,L,a=2e-9,3e-9,.7,.2
Fx=force([(Q,0,0),(Q,L,0),(Q,0,L)],(L,L),Q)
verify('21.57-square-corner',sqrt(sum(x*x for x in Fx)),k*Q*Q/L**2*(sqrt(2)+.5))
q3=-4*Q/9
for name,p,charge,sources in [
 ('Q',(0,0),Q,[(4*Q,L,0),(q3,L/3,0)]),
 ('4Q',(L,0),4*Q,[(Q,0,0),(q3,L/3,0)]),
 ('q',(L/3,0),q3,[(Q,0,0),(4*Q,L,0)])]:
 verify('21.69-'+name,force(sources,p,charge),(0,0))
F=force([(q,0,0),(q,L,0),(q,0,L)],(L/2,L/2),-3*q)
verify('21.71-center',sqrt(sum(x*x for x in F)),6*k*q*q/L**2)
F=force([(q,0,0),(q,L,0),(q,0,L)],(L,L),-3*q)
verify('21.71-corner',sqrt(sum(x*x for x in F)),3*k*q*q/L**2*(sqrt(2)+.5))

x=a+.3
verify('21.79-rod',simpson(lambda t:k*Q/a/(x-t)**2,0,a),k*Q/(x*(x-a)))
Ex=simpson(lambda y:k*Q/a*x/(x*x+y*y)**1.5,0,a)
Ey=simpson(lambda y:-k*Q/a*y/(x*x+y*y)**1.5,0,a)
verify('21.80-components',(Ex,Ey),(k*Q/(x*sqrt(x*x+a*a)),k*Q/a*(1/sqrt(x*x+a*a)-1/x)))
for trig in [cos,sin]:
 verify('21.83-'+trig.__name__,simpson(lambda t:2*k*Q/(pi*a*a)*trig(t),0,pi/2),2*k*Q/(pi*a*a))
verify('21.84-semicircle',simpson(lambda t:-2*k*Q/(pi*a*a)*cos(t),pi/2,pi)+simpson(lambda t:2*k*Q/(pi*a*a)*cos(t),0,pi/2),4*k*Q/(pi*a*a))
sigma,R1,R2=2e-9,.3,.8
for x in [-.2,.001,.4]:
 integral=simpson(lambda r:2*pi*k*sigma*r*x/(x*x+r*r)**1.5,R1,R2)
 exact=sigma*x/(2*eps)*(1/sqrt(x*x+R1*R1)-1/sqrt(x*x+R2*R2))
 verify('21.87-annulus-'+str(x),integral,exact)
q,m=2e-9,.005;h=1e-6
annulus=lambda x:sigma*x/(2*eps)*(1/sqrt(x*x+R1*R1)-1/sqrt(x*x+R2*R2))
verify('21.87-restoring-gradient',q*(annulus(h)-annulus(-h))/(2*h),q*sigma/(2*eps)*(1/R1-1/R2))

# The turning point is checked by integrating the electric force and gravity.
sigma,R,q,m=1e-5,.1,1e-6,.025;g=9.8
mmax=q*sigma/(2*eps*g);alpha=m/mmax
delta=2*R*alpha/(1-alpha*alpha)
work=simpson(lambda z:m*g-q*sigma/(2*eps)*z/sqrt(z*z+R*R),0,delta)
verify('21.91-turning-energy',work,0,1e-5)
verify('21.91-critical-mass',mmax,.0577,.003)

# Small oscillation stiffness from a numerical derivative of the exact torque.
Q,L,M=2e-9,.7,.02
torque=lambda t:k*Q*Q/L*(cos(t/2)/sin(t/2)**2-sin(t/2)/cos(t/2)**2)
derivative=(torque(pi/2+h)-torque(pi/2-h))/(2*h)
verify('21.92-stiffness',-derivative,3*sqrt(2)*k*Q*Q/L)

# Two parallel rods: nested force integration and a separate energy integration.
Q,L,a=10e-6,.5,.1;lam=Q/L
Fnum=simpson(lambda y2:simpson(lambda y1:k*lam*lam*a/(a*a+(y2-y1)**2)**1.5,0,L,200),0,L,200)
Fexact=2*k*Q*Q/L**2*(sqrt(1+(L/a)**2)-1)
verify('21.93-force-double-integral',Fnum,Fexact,1e-6)
Unum=simpson(lambda y2:simpson(lambda y1:k*lam*lam/sqrt(a*a+(y2-y1)**2),0,L,200),0,L,200)
U=lambda d:2*k*Q*Q/L**2*(L*log((L+sqrt(d*d+L*L))/d)+d-sqrt(d*d+L*L))
verify('21.93-energy-double-integral',Unum,U(a),1e-6)
verify('21.93-force-energy-derivative',-(U(a+h)-U(a-h))/(2*h),Fexact,1e-6)
verify('21.93-relative-speed',2*sqrt(Unum/.5),6.55,.001)

# Same-axis rods, integrated over both independent source coordinates.
Q,L,a=2e-9,.7,.2
Fnum=simpson(lambda x:simpson(lambda u:k*(Q/L)**2/(x-u)**2,-a/2-L,-a/2,300),a/2,a/2+L,300)
verify('21.97-double-integral',Fnum,k*Q*Q/L**2*log((a+L)**2/(a*(a+2*L))),1e-7)

computed=json.loads((root/'qa/physics/chapter21/answers-computed.json').read_text(encoding='utf8'))
targets={'21.2':[2,1.25e19],'21.6':760,'21.8':[7.25e24,5.27e15,7.26e-10],
 '21.12':[1.09e-5,.6],'21.16':-.144,'21.18':[8.87e-9,8.24e-8],'21.19':1.26e-8,
 '21.20':[32.6,1e4],'21.22':[719,1.94],'21.24':[1e12,5.69,1.02e11],
 '21.26':[385,2020],'21.28':1.79e6,'21.30':[6.33e5,1.59e4],
 '21.42':[8.97e-12,32.3,284],'21.46':.556e-9,'21.48':2.30,
 '21.50':[3.03e4,3.45e4],'21.52':[8e-24,.39],'21.54':6.58e-13,
 '21.58':-3.27,'21.61-angle':39.5,'21.62-horizontal':468,'21.62-downward':770,
 '21.66':[6.91e23,1.11e5,2.75e23],'21.68':[1.05e-9,-2.55e-9],
 '21.72':[6.18e-8,-6.18e-8],'21.74':2.96e3,'21.76':[.174,.0734],
 '21.78':2.18e3,'21.88':[6.6e-13,4.1e6,1.6e-13],'21.90':[5.56e-9,.415],
 '21.95':[.844e-6,56.2]}
for name,expected in targets.items():verify(name,computed[name],expected,.03)
out=root/'qa/physics/chapter21/advanced-checks.json'
out.write_text(json.dumps({'status':'passed','groups':len(checks),'checks':checks},ensure_ascii=False,indent=2),encoding='utf8')
print('Passed',len(checks),'additional numeric and analytical checks.')
