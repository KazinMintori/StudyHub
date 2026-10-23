"""Plot the six actual equilibrium measurements requested by exercise11.87."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
m=np.array([1.,1.5,2.,2.5,3.,4.])
x=np.array([3.50,2.83,2.50,2.32,2.16,2.00])
slope,intercept=np.polyfit(1/m,x,1)
z=np.linspace(0,1.06,150)
fig,ax=plt.subplots(figsize=(6.2,4.2),layout='constrained')
ax.scatter(1/m,x,color='#b45309',label='Sáu phép đo',zorder=3)
ax.plot(z,slope*z+intercept,color='#1d4ed8',label='Đường khớp bình phương tối thiểu')
ax.set(xlabel=r'$1/m_2$ ($\mathrm{kg}^{-1}$)',ylabel=r'$x$ (m)',xlim=(0,1.07),ylim=(1.3,3.75))
ax.grid(alpha=.25);ax.legend(fontsize=8)
out=ROOT/'docs/vat-ly-1/bai-giang/img/young-11/e-plot11-87.svg'
fig.savefig(out);plt.close(fig)
print('Saved requested source-data plot:',out)
