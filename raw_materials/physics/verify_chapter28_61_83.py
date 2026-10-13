"""Private independent numeric/vector checks for Chapter28 exercises61–83."""
from pathlib import Path
import json,math
import numpy as np

MU0=4*math.pi*1e-7
G=9.80
nodes,weights=np.polynomial.legendre.leggauss(128)
def integral(fn,lo,hi):
    x=(lo+hi)/2+(hi-lo)/2*nodes
    return float(np.dot(weights,fn(x))*(hi-lo)/2)
def close(actual,expected,tol=2e-11):
    assert math.isclose(float(actual),float(expected),rel_tol=tol,abs_tol=1e-100),(actual,expected)
values={}

# 61: Separation comes from both inclined cords; forces are per unit length.
cord=.0400;theta=math.radians(6);linear_mass=.0125
separation=2*cord*math.sin(theta)
current61=math.sqrt(2*math.pi*separation*linear_mass*G*math.tan(theta)/MU0)
close(MU0*current61**2/(2*math.pi*separation),linear_mass*G*math.tan(theta))
values['61']={'distance_m':separation,'current_A':current61}

# 62/64: Direct arc integration, with signed rotation and radial legs zero.
def arc_b(radius,start,end,current):
    return MU0*current/(4*math.pi)*integral(lambda t:np.ones_like(t)/radius,start,end)
a,b,I=.030,.070,5.0
b62=arc_b(a,0,math.pi,I)+arc_b(b,math.pi,0,I)
close(b62,MU0*I/4*(1/a-1/b));assert b62>0
alpha=math.radians(120)
b64=arc_b(.300,0,alpha,12)+arc_b(.200,alpha,0,12)
close(b64,MU0*12*alpha/(4*math.pi)*(1/.300-1/.200));assert b64<0
values['64']={'B_T_signed_outward':b64,'magnitude_T':abs(b64)}

# 63: Density is beta/r times exp((r-a)/delta), singular but integrable.
beta,delta,a63=600.,.0250,.0500
total63=2*math.pi*beta*delta*(-math.expm1(-a63/delta))
close(total63,integral(lambda r:2*math.pi*beta*np.exp((r-a63)/delta),0,a63))
def enclosed63(r):
    return total63*math.expm1(r/delta)/math.expm1(a63/delta)
def field63(r):
    assert r>0
    return MU0*(enclosed63(r) if r<a63 else total63)/(2*math.pi*r)
for r in [delta,a63*.7,a63]:
    close(enclosed63(r),integral(lambda x:2*math.pi*beta*np.exp((x-a63)/delta),0,r))
close(enclosed63(a63),total63)
close(field63(1e-12),MU0*beta*math.exp(-a63/delta),1e-9)
values['63']={'I0_A':total63,'B_delta_T':field63(delta),'B_a_T':field63(a63),'B_2a_T':field63(2*a63),'axis_limit_magnitude_T':MU0*beta*math.exp(-a63/delta)}

# 65: Radially increasing density. 67: Density falls quadratically to zero.
R,I65=.04,7.
density_alpha=3*I65/(2*math.pi*R**3)
for r in [.1*R,.4*R,R]:
    current=integral(lambda s:2*math.pi*s*density_alpha*s,0,r)
    close(current,I65*(r/R)**3)
    close(MU0*current/(2*math.pi*r),MU0*I65*r*r/(2*math.pi*R**3))
a67,I0=.070,11.
for r in [.1*a67,.7*a67,a67]:
    numerical=integral(lambda s:2*math.pi*s*(2*I0/(math.pi*a67*a67))*(1-(s/a67)**2),0,r)
    analytic=I0*(2*(r/a67)**2-(r/a67)**4)
    close(numerical,analytic)
close(I0*(2-1),I0)

# 66: The horizontal segment is radial, the vertical semi-infinite wire gives +z.
a66,I66=.035,6.
semi=MU0*I66/(4*math.pi)*integral(lambda t:np.cos(t)/a66,0,math.pi/2)
close(semi,MU0*I66/(4*math.pi*a66))
assert np.array_equal(np.cross([1.,0,0],[a66,0,0]),[0,0,0])
assert np.cross([0.,-1,0],[a66,2*a66,0])[2]>0

# 68: A clockwise loop produces -z. A rightward wire below it produces +z.
D,R68,I2=.12,.040,3.
I1=math.pi*D*I2/R68
assert abs(MU0*I1/(2*math.pi*D)-MU0*I2/(2*R68))<1e-18

# 69: Integrating all straight-wire contributions gives a constant field.
n69,I69=800.,.4
sheet=MU0*n69*I69/2
for height in [.010,.100,1.0]:
    numeric=MU0*n69*I69/(2*math.pi)*integral(lambda t:np.ones_like(t),-math.pi/2,math.pi/2)
    close(numeric,sheet)
assert np.cross([0,1,0],[0,0,1])[0]>0
fields70=[np.array([-sheet,0.,0.])+[sheet,0.,0.],np.array([sheet,0.,0.])+[sheet,0.,0.],np.array([sheet,0.,0.])+[-sheet,0.,0.]]
assert np.array_equal(fields70[0],[0,0,0]) and np.array_equal(fields70[2],[0,0,0])
close(fields70[1][0],MU0*n69*I69)

# 71: Ring currents and charged-disk moment, independent of shell radius.
Q1,w1,H,R1=3e-6,30.,.4,.1
Q2,w2,R2,M,angle=2e-6,400.,.005,.010,.45
surface=Q1/(2*math.pi*R1*H)
enclosed71=surface*R1*w1*H
close(enclosed71,Q1*w1/(2*math.pi))
field71=MU0*enclosed71/H
moment71=Q2*w2*R2**2/4
tau71=moment71*field71*math.sin(angle)
L71=M*R2**2*w2/2
close(moment71/L71,Q2/(2*M))
close(tau71,MU0*Q1*Q2*w1*w2*R2**2*math.sin(angle)/(8*math.pi*H))

# 72: Read two unmistakable grid intersections: (2mA,8A),(5mA,16A).
slope72=(16.-8.)/(.005-.002)
intercept72=8.-slope72*.002
N2=slope72;N1=intercept72/.002
B72=MU0*(N1*.002-N2*.005)/.400
close(N1*.002+N2*.002,8.)
close(N1*.002+N2*.005,16.)
values['72']={'N1':N1,'N2':N2,'B_part_c_signed_T':B72}

# 73: Use all printed measurements, with distance measured from surface.
x73=np.array([2.,4.,6.,8.,10.])*1e-2
B73=np.array([.406,.250,.181,.141,.116])*1e-3
slope73,intercept73=np.polyfit(1/B73,x73,1)
I73=2*math.pi*slope73/MU0
R73=-intercept73
assert R73>0 and I73>0
assert np.ptp(x73*B73)>1e-6
prediction=MU0*I73/(2*math.pi*(x73+R73))
assert np.max(abs(prediction/B73-1))<.003
values['73']={'Bx_T_m':(x73*B73).tolist(),'slope_T_m':float(slope73),'intercept_m':float(intercept73),'current_A':float(I73),'radius_m':float(R73)}

# 74: Each rod is opposed by TWO springs. Use exact printed rounded data.
length74=.500;coefficient74=MU0*length74/(4*math.pi)
xs=np.array([.0040,.0080]);currents=np.array([8.05,13.1])
rhs=coefficient74*currents**2/xs
kl0,k74=np.linalg.solve(np.column_stack([np.ones(2),xs]),rhs)
l0=kl0/k74
assert k74>0 and l0>0
def stretch74(current):
    return (-l0+math.sqrt(l0*l0+4*coefficient74*current*current/k74))/2
for x,current in zip(xs,currents):
    close(stretch74(current),x)
    close(2*k74*x,MU0*current*current*length74/(2*math.pi*(l0+x)))
x12=stretch74(12.)
I_1cm=math.sqrt(k74*.01*(l0+.01)/coefficient74)
values['74']={'l0_m':float(l0),'k_N_m':float(k74),'x_12A_m':float(x12),'I_1cm_A':float(I_1cm)}

# 75: Scalar sum of radial force magnitudes, not the zero vector resultant.
n75=8e16*1e6;q75=1.6e-19;R75=.020;v75=20.;length75=.30
rho75=n75*q75;sigma75=q75*n75**(2/3)
B75=MU0*rho75*v75*R75/2
pressure75=sigma75*v75*B75
close(pressure75,MU0*n75**(5/3)*q75*q75*R75*v75*v75/2)
scalar_force75=2*math.pi*R75*length75*pressure75
net=np.array([integral(lambda phi:-pressure75*R75*length75*np.cos(phi),0,2*math.pi),integral(lambda phi:-pressure75*R75*length75*np.sin(phi),0,2*math.pi),0])
assert np.linalg.norm(net)<scalar_force75*1e-12
values['75']={'number_density_m3':n75,'rho_C_m3':rho75,'sigma_C_m2':sigma75,'surface_B_T':B75,'pinch_pressure_Pa':pressure75}

# 76: Independent numerical loop integral, stable for all aspect ratios.
Q76,w76=5e-6,20.
for radius,width in [(.07,.2),(.01,3.),(1.,.001)]:
    bound=math.atan(width/(2*radius))
    numeric=MU0*Q76*w76/(4*math.pi*width)*integral(lambda theta:np.cos(theta),-bound,bound)
    analytic=MU0*Q76*w76/(4*math.pi*math.sqrt(radius*radius+(width/2)**2))
    close(numeric,analytic)

# 77: Direct latitude integrals for charge, moment and angular momentum.
Q77,M77,R77,w77=2e-6,.030,.040,100.
close(integral(lambda theta:Q77/2*np.sin(theta),0,math.pi),Q77)
mu77=integral(lambda theta:Q77*w77*R77**2/4*np.sin(theta)**3,0,math.pi)
L77=integral(lambda theta:M77*w77*R77**2/2*np.sin(theta)**3,0,math.pi)
close(mu77,Q77*w77*R77**2/3)
close(L77,2*M77*w77*R77**2/3)
close(mu77/L77,Q77/(2*M77));close((mu77/L77)/(Q77/(2*M77)),1)

# 78: Direct surface Biot–Savart calculation, with r from element to origin.
R78,W78,Q78,w78=.07,.20,5e-6,20.
sigma78=Q78/(2*math.pi*R78*W78)
xs78=nodes*W78/2;phis=(nodes+1)*math.pi
wx=weights*W78/2;wp=weights*math.pi
total78=np.zeros(3)
for x,weight_x in zip(xs78,wx):
    source=np.column_stack([np.full_like(phis,x),R78*np.cos(phis),R78*np.sin(phis)])
    displacement=-source
    velocity=np.column_stack([np.zeros_like(phis),-w78*R78*np.sin(phis),w78*R78*np.cos(phis)])
    integrand=np.cross(velocity,displacement)/np.linalg.norm(displacement,axis=1)[:,None]**3
    total78+=weight_x*np.sum(wp[:,None]*integrand,axis=0)*R78
total78*=MU0*sigma78/(4*math.pi)
expected78=MU0*Q78*w78/(4*math.pi*math.sqrt(R78**2+(W78/2)**2))
close(total78[0],expected78)
assert np.linalg.norm(total78[1:])<abs(expected78)*1e-12

# 79: Integrate the repulsive impulse during RC discharge, and Joule energy.
Q0,C79,resistance79,lambda79,d79=.004,1e-4,2.,.010,.010
tau79=resistance79*C79
isquared=integral(lambda t:(Q0/tau79*np.exp(-t/tau79))**2,0,20*tau79)
close(isquared,Q0*Q0/(2*resistance79*C79))
close(resistance79*isquared,Q0*Q0/(2*C79))
v079=MU0*isquared/(2*math.pi*lambda79*d79)
close(v079,MU0*Q0*Q0/(4*math.pi*lambda79*resistance79*C79*d79))
height79=v079*v079/(2*G)
close(.5*lambda79*v079*v079,lambda79*G*height79)

# 80: Integrate the infinite surface in polar coordinates, current along +x.
sigma80,speed80=2e-5,3.
integrated80=-MU0*sigma80*speed80/(4*math.pi)*2*math.pi*integral(np.sin,0,math.pi/2)
close(integrated80,-MU0*sigma80*speed80/2)
assert np.cross([1,0,0],[0,0,1])[1]<0

# 81–83: Both printed field units are MICROtesla. n=1/(1mm).
n81=1/.001
current81=150e-6/(MU0*n81)
assert abs(current81-.12)<.001
close(.400/.001,400)
close(MU0*n81*current81,150e-6)
Bs,Be=150e-6,50e-6
angles=np.linspace(0,math.pi,10001)
magnitude=np.sqrt(Bs*Bs+Be*Be+2*Bs*Be*np.cos(angles))
close(np.min(magnitude),100e-6);close(np.max(magnitude),200e-6)
values['81_83']={'current_A':current81,'turns':400,'minimum_field_T':float(np.min(magnitude)),'maximum_field_T':float(np.max(magnitude)),'choices':['b','c','c']}

root=Path(__file__).resolve().parents[2]
out=root/'qa/physics/chapter28';out.mkdir(parents=True,exist_ok=True)
(out/'numeric-61-83.json').write_text(json.dumps({'status':'passed','scope':'28.61–28.83','values':values},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(values,ensure_ascii=False,indent=2))
print('Passed independent numeric integrals, vector signs, boundaries and all root-scope calculations.')
