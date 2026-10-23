"""Plot the assigned Lennard–Jones function and verify its roots/derivative."""
from pathlib import Path
import math,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-18/e-lennard-jones-solution.svg'
u=lambda x:x**-12-2*x**-6
force=lambda x:12*(x**-13-x**-7)
r1=2**(-1/6);r2=1.
assert abs(u(r1))<1e-12 and u(1)==-1 and force(1)==0
for value in [.87,.95,1.1,1.7,2.2]:
 step=1e-6
 derivative=(u(value+step)-u(value-step))/(2*step)
 assert math.isclose(force(value),-derivative,rel_tol=1e-8,abs_tol=1e-8)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'path'})
fig,axes=plt.subplots(2,1,figsize=(7.2,5.8),sharex=True,layout='constrained')
x=np.linspace(.86,2.2,1400)
axes[0].plot(x,u(x),color='#6945a0',linewidth=2.2)
axes[1].plot(x,force(x),color='#a85a23',linewidth=2.2)
for ax in axes:
 ax.axhline(0,color='#777',linewidth=.8)
 ax.axvline(r1,color='#a85a23',linestyle=':',linewidth=1)
 ax.axvline(r2,color='#6945a0',linestyle='--',linewidth=1)
 ax.set_xlim(.86,2.2);ax.grid(alpha=.16)
 ax.spines[['top','right']].set_visible(False)
axes[0].set_ylim(-1.18,1.6)
axes[0].set_ylabel('Potential energy U / U0')
axes[0].scatter([r1,r2],[0,-1],color=['#a85a23','#6945a0'],s=28,zorder=4)
axes[0].annotate('r1',(r1,0),xytext=(1.12,.35),arrowprops={'arrowstyle':'-','color':'#777'},fontsize=13)
axes[0].annotate('r2 = R0',(r2,-1),xytext=(1.35,-.95),arrowprops={'arrowstyle':'-','color':'#777'},fontsize=13)
axes[1].set_ylim(-4,55)
axes[1].set_ylabel('Radial force F R0 / U0')
axes[1].set_xlabel('Separation r / R0')
axes[1].scatter([r2],[0],color='#6945a0',s=28,zorder=4)
fig.savefig(OUT,facecolor='white')
fig.savefig(ROOT/'qa/physics1-priority/ch18-lj-preview.png',facecolor='white',dpi=120)
plt.close(fig)
q=ROOT/'qa/physics1-priority'
(q/'ch18-lj-plot-ledger.json').write_text(json.dumps(dict(status='passed',sourceProblem='18.67',dimensionlessRoots=dict(zeroPotential=r1,equilibrium=r2),potentialMinimum=-1,workToSeparateInUnitsU0=1,derivativeCheckedAt=[.87,.95,1.1,1.7,2.2]),indent=2),encoding='utf-8')
print('Created a vector plot of the actual potential and force; roots and force derivative passed.')
