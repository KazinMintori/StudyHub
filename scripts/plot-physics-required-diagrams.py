from pathlib import Path
import os
root=Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR',str(root/'qa/physics/mpl-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from math import sqrt,pi,cos,sin

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
def save(fig,chapter,name):
 out=root/f'docs/vat-ly-2/bai-giang/img/young-{chapter}'
 qa=root/f'qa/physics/chapter{chapter}/plots';qa.mkdir(parents=True,exist_ok=True)
 fig.tight_layout();fig.savefig(out/(name+'.svg'),bbox_inches='tight');fig.savefig(qa/(name+'.png'),dpi=110,bbox_inches='tight');plt.close(fig)
def arrow(ax,p,v,label,color='#b1446e'):
 end=(p[0]+v[0],p[1]+v[1]);ax.annotate('',xy=end,xytext=p,arrowprops={'arrowstyle':'->','color':color,'lw':2})
 ax.text(end[0]+.02,end[1]+.02,label,color=color,fontsize=10)
def square(ax,charges,target,label):
 ax.plot([0,1,1,0,0],[0,0,1,1,0],':',color='#aaa')
 for p in charges:ax.plot(*p,'o',color='#4c47a1');ax.text(p[0]-.04,p[1]-.12,'q',ha='center',color='#4c47a1')
 ax.plot(*target,'o',color='#ee8a53');ax.text(target[0]-.06,target[1]-.14,label,ha='center')
 ax.set_aspect('equal');ax.set(xlim=(-.55,1.85),ylim=(-.55,1.85));ax.axis('off')

fig,ax=plt.subplots(figsize=(5,5));target=(1,1);square(ax,[(0,0),(1,0),(0,1)],target,'+Q')
arrow(ax,target,(.55,0),'F₁');arrow(ax,target,(0,.55),'F₂');arrow(ax,target,(.55/(2*sqrt(2)),.55/(2*sqrt(2))),'F₃')
ax.set_title('Bài 21.57: Lực lên một điện tích ở đỉnh');save(fig,21,'loi-giai-21-57')
fig,axes=plt.subplots(1,2,figsize=(8,4));charges=[(0,0),(1,0),(0,1)]
for ax,target,mode in [(axes[0],(.5,.5),'Tại tâm'),(axes[1],(1,1),'Tại đỉnh trống')]:
 square(ax,charges,target,'−3q')
 for i,p in enumerate(charges):
  dx,dy=p[0]-target[0],p[1]-target[1];r=sqrt(dx*dx+dy*dy)
  length=.34 if target==(.5,.5) else .5/(r*r)
  arrow(ax,target,(length*dx/r,length*dy/r),f'F{i+1}')
 ax.set_title(mode)
save(fig,21,'loi-giai-21-71')

fig,ax=plt.subplots(figsize=(6,6));ax.set_aspect('equal')
levels=[500,400,300,200,100,0];radii=[.012,.0145454545,.0184615385,.0252631579,.04,.096]
colors=plt.cm.viridis([i/5 for i in range(6)])
for level,radius,color in zip(levels,radii,colors):ax.add_patch(Circle((0,0),radius*100,fill=False,color=color,lw=1.5,label=f'{level} V: r = {radius*100:.2f} cm'))
for t in [i*pi/4 for i in range(8)]:
 for lo,hi in [(.013,.035),(.043,.085)]:
  ax.annotate('',xy=(hi*100*cos(t),hi*100*sin(t)),xytext=(lo*100*cos(t),lo*100*sin(t)),arrowprops={'arrowstyle':'->','color':'#b1446e','lw':1.3})
ax.set(xlim=(-10.2,10.2),ylim=(-10.2,10.2),xlabel='x (cm)',ylabel='y (cm)',title='Mặt cắt đẳng thế và đường sức xuyên tâm')
ax.legend(loc='upper left',bbox_to_anchor=(1.02,1),fontsize=9);ax.grid(alpha=.12)
save(fig,23,'loi-giai-23-45')

fig,ax=plt.subplots(figsize=(5,5));square(ax,[(0,0),(1,1)],(0,1),'q₀ < 0')
ax.plot(.5,.5,'x',color='#555');ax.text(.5,.58,'B',ha='center');ax.text(-.1,1,'A')
arrow(ax,(0,1),(.52,0),'F₂');arrow(ax,(0,1),(0,-.52),'F₁');arrow(ax,(0,1),(.48,-.48),'F tổng',color='#2d887f')
ax.set_title('Bài 23.54: Hai lực hút vuông góc');save(fig,23,'loi-giai-23-54')
print('Prepared the four required free-body/equipotential diagrams.')
