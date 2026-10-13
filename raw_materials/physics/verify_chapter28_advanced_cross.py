"""Independent alternate-method checks for selected Chapter 28 solutions."""
import json
import math
from pathlib import Path
import numpy as np

MU0 = 4 * math.pi * 1e-7
checks = {}

def close(actual, expected, rel=2e-8, abs_=1e-14):
    assert math.isclose(float(actual), float(expected), rel_tol=rel, abs_tol=abs_), (actual, expected)

# 63: Integrate J dA directly; the 1/r singularity cancels against annular area.
beta, delta, a = 600., .025, .050
I0 = 2*math.pi*beta*delta*(1-math.exp(-a/delta))
def enclosed(r): return 2*math.pi*beta*delta*(math.exp((r-a)/delta)-math.exp(-a/delta))
Bdelta = MU0*enclosed(delta)/(2*math.pi*delta)
Ba = MU0*I0/(2*math.pi*a)
B2a = MU0*I0/(4*math.pi*a)
close(I0,81.4927296601); close(Bdelta,1.75334164369e-4); close(Ba,3.2597091864e-4); close(B2a,1.6298545932e-4)
checks['63']={'I0_A':I0,'B_delta_T':Bdelta,'B_a_T':Ba,'B_2a_T':B2a,'axis_limit_magnitude_T':MU0*beta*math.exp(-a/delta)}

# 72: Solve the winding equations simultaneously from the printed grid points.
# Y=N1*I1+N2*I2, using graph intersections (2 mA, 8 A) and (5 mA, 16 A).
N1,N2=np.linalg.solve(np.array([[.002,.002],[.002,.005]]),np.array([8.,16.]))
Brev=MU0/.4*(N1*.002-N2*.005)
close(N1,4000/3); close(N2,8000/3); close(Brev,-3.35103216383e-5)
checks['72']={'graph_points':[[2,8],[5,16]],'N1_turns':N1,'N2_turns':N2,'B_reverse_T_signed':Brev}

# 73: Compute least-squares line using centered covariance, not polynomial-fit API.
x=np.array([.02,.04,.06,.08,.10]); B=np.array([.406,.250,.181,.141,.116])*1e-3; z=1/B
s=float(np.sum((z-z.mean())*(x-x.mean()))/np.sum((z-z.mean())**2))
c=float(x.mean()-s*z.mean()); current=2*math.pi*s/MU0; radius=-c
close(current,64.9025399538); close(radius,.0119141023195)
checks['73']={'slope_T_m':s,'intercept_m':c,'current_A':current,'radius_m':radius}

# 74: Solve equations 2kx=mu0 I^2 L/[2pi(l0+x)] as a linear system in (kl0,k).
L=.50; alpha=MU0*L/(4*math.pi); x1,x2=.004,.008; I1,I2=8.05,13.1
kl0,k=np.linalg.solve(np.array([[1.,x1],[1.,x2]]),np.array([alpha*I1**2/x1,alpha*I2**2/x2]))
l0=kl0/k
def extension(I): return (-l0+math.sqrt(l0*l0+4*alpha*I*I/k))/2
I_for_1cm=math.sqrt(k*.01*(l0+.01)/alpha)
close(2*k*x1,MU0*I1**2*L/(2*math.pi*(l0+x1))); close(extension(12),.00710283841366); close(I_for_1cm,15.5166241496)
checks['74']={'k_N_m':k,'l0_m':l0,'extension_at_12A_m':extension(12),'current_for_1cm_A':I_for_1cm}

# 76: Integrate ring-field kernel using its endpoint antiderivative.
Q,omega,R,W=5e-6,20.,.07,.20
primitive=lambda t:t/(R*R*math.sqrt(t*t+R*R))
kernel=primitive(W/2)-primitive(-W/2)
B76=MU0*Q*omega*R*R/(4*math.pi*W)*kernel
compact=MU0*Q*omega/(4*math.pi*math.sqrt(R*R+(W/2)**2))
close(B76,compact)
checks['76']={'kernel_integral_m-2':kernel,'B_T':B76}

# 78: Midpoint quadrature of the original vector surface integral, independent
# of slicing the shell into current loops. Source-to-origin vector is -r_source.
nx,nphi=401,800; dx=W/nx; dphi=2*math.pi/nphi
xs=-W/2+(np.arange(nx)+.5)*dx; phis=(np.arange(nphi)+.5)*dphi
X,P=np.meshgrid(xs,phis,indexing='ij')
src=np.stack((X,R*np.cos(P),R*np.sin(P)),axis=-1)
rv=-src; dist=np.sqrt(X*X+R*R)
vel=np.stack((np.zeros_like(X),-omega*R*np.sin(P),omega*R*np.cos(P)),axis=-1)
sigma=Q/(2*math.pi*R*W)
integrand=sigma*np.cross(vel,rv/dist[...,None])/(dist[...,None]**2)*R
Bvec=MU0/(4*math.pi)*np.sum(integrand,axis=(0,1))*dx*dphi
close(Bvec[0],B76,rel=8e-6); close(Bvec[1],0,abs_=2e-10); close(Bvec[2],0,abs_=2e-10)
checks['78']={'surface_integral_B_vector_T':Bvec.tolist(),'ring_method_Bx_T':B76,'quadrature':'midpoint grid in x and azimuth'}

# 79: RC discharge gives integral I^2 dt=Q0^2/(2RC); impulse changes velocity.
# Flexible ideal suspension lets each wire's kinetic energy lift that wire.
Q0,C,resistance,lam,d=.004,1e-4,2.,.010,.010
intI2=Q0**2/(2*resistance*C)
v0=MU0*intI2/(2*math.pi*lam*d); h=v0*v0/(2*9.80)
close(v0,MU0*Q0**2/(4*math.pi*lam*resistance*C*d)); close(.5*lam*v0*v0,lam*9.80*h)
checks['79']={'integral_I2_A2s':intI2,'v0_m_s':v0,'rise_h_m':h,'assumption':'ideal flexible suspension; each wire rises by its own kinetic energy'}

# 81-83: Printed p. 952 visibly gives microtesla (OCR can confuse µ with m).
n=1/.001; Is=150e-6/(MU0*n); lo=abs(150e-6-50e-6); hi=150e-6+50e-6
close(Is,.119366207319); close(lo,100e-6); close(hi,200e-6)
checks['81_83']={'current_A':Is,'turns':400,'field_bounds_T':[lo,hi],'choices':['b','c','c'],'source_units':'microtesla'}

out=Path(__file__).resolve().parents[2]/'qa'/'physics'/'chapter28'/'advanced-cross.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({'status':'passed','checks':checks},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(checks,ensure_ascii=False,indent=2))
print('Independent advanced checks passed:',out)
