"""Reproducible data fits and spacetime construction for chapter37 solutions."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-37';out.mkdir(parents=True,exist_ok=True)
qa=root/'qa/physics/chapter37/plot-review';qa.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'none'})
def finish(fig,ax,name):
 ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.2);fig.tight_layout();fig.savefig(out/name,facecolor='white');fig.savefig(qa/Path(name).with_suffix('.png'),facecolor='white',dpi=130);plt.close(fig)
b=np.array([.70,.80,.85,.88,.90,.92,.94]);t=np.array([3.57,4.41,5.02,5.47,6.05,6.58,7.62]);x=1/(1-b*b);y=t*t;slope,offset=np.polyfit(x,y,1)
fig,ax=plt.subplots(figsize=(7.4,4.7));xx=np.linspace(0,9,150);ax.plot(xx,slope*xx+offset,color='#5743a1',label='Đường thẳng hồi quy');ax.scatter(x,y,color='#177b8c',s=45,zorder=3,label='Bảy điểm đo');ax.set(xlim=(0,9),ylim=(0,65),xlabel=r'$X=1/(1-u^2/c^2)$',ylabel=r'$Y=(\Delta t)^2\ (10^{-16}\ \mathrm{s}^2)$');ax.legend(fontsize=11);finish(fig,ax,'loi-giai-37-63.svg')
b=np.array([.60,.65,.70,.75,.80,.85]);a=np.array([20.3,17.9,14.8,11.2,8.5,5.9]);x=(1-b*b)**1.5;slope,offset=np.polyfit(x,a,1)
fig,ax=plt.subplots(figsize=(7.4,4.7));xx=np.linspace(0,.56,150);ax.plot(xx,slope*xx+offset,color='#5743a1',label='Đường thẳng hồi quy');ax.scatter(x,a,color='#177b8c',s=45,zorder=3,label='Sáu điểm đo');ax.set(xlim=(0,.56),ylim=(0,23),xlabel=r'$X=(1-v^2/c^2)^{3/2}$',ylabel=r'$a\ (10^3\ \mathrm{m/s^2})$');ax.legend(fontsize=11);finish(fig,ax,'loi-giai-37-65.svg')
b=.6;gamma=1/np.sqrt(1-b*b);L=1.;cT=1.3;M=gamma*np.array([[1,-b],[-b,1]])
points=np.array([[0,0],[-L,0],[0,cT],[-L,cT]])@M.T
fig,ax=plt.subplots(figsize=(7.4,5.1));ax.add_patch(Polygon(points[[0,1,3,2]],closed=True,facecolor='#ffea9c',edgecolor='#5743a1',lw=2));ax.scatter(points[:,0],points[:,1],color='#24364b',zorder=3)
for i,(x,y) in enumerate(points):ax.annotate(str(i+1),(x,y),xytext=(7,5),textcoords='offset points',fontsize=15)
ax.annotate('',xy=(.35,0),xytext=(-2.6,0),arrowprops={'arrowstyle':'->','color':'#24364b'});ax.annotate('',xy=(0,2.7),xytext=(0,-.2),arrowprops={'arrowstyle':'->','color':'#24364b'});ax.text(.26,-.16,"x′",fontsize=15);ax.text(.08,2.52,"ct′",fontsize=15);ax.set(xlim=(-2.5,.4),ylim=(-.25,2.75),aspect='equal');ax.set_xticks([]);ax.set_yticks([]);ax.spines[:].set_visible(False);ax.text(-2.3,2.55,'Miền các sự kiện đèn đang sáng',fontsize=12);fig.tight_layout();fig.savefig(out/'loi-giai-37-67.svg',facecolor='white');fig.savefig(qa/'loi-giai-37-67.png',facecolor='white',dpi=130);plt.close(fig)
print('Generated all7-point and6-point data graphs and Lorentz spacetime parallelogram.')
