from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'qa/physics1-remaining/ch13/solution-previews';out.mkdir(parents=True,exist_ok=True)
assets=ROOT/'docs/vat-ly-1/bai-giang/img/young-13';assets.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'none','svg.hashsalt':'studyhub13parentexercises','axes.spines.top':False,'axes.spines.right':False})
def save(fig,name):
 path=assets/(name+'.svg');fig.savefig(path,facecolor='white',metadata={'Date':None,'Creator':'StudyHub verified solution diagram'})
 path.write_bytes(('\n'.join(line.rstrip()for line in path.read_text(encoding='utf-8').splitlines())+'\n').encode('utf-8'))
 fig.savefig(out/(name+'.png'),dpi=130,facecolor='white');plt.close(fig)
fig,axes=plt.subplots(2,1,figsize=(5.0,4.4),layout='constrained')
for ax,mass,direction in zip(axes,[65,72],[1,-1]):
 ax.set_xlim(-1.1,1.1);ax.set_ylim(-.65,.65);ax.axis('off')
 ax.scatter([0],[0],s=260,color='#45566b',zorder=3)
 ax.annotate('',xy=(direction*.92,0),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2.6,'color':'#235cc4'})
 ax.text(0,-.39,str(mass)+' kg',ha='center',fontsize=14)
 ax.text(direction*.5,.22,'F',ha='center',fontsize=14)
axes[0].set_title('Hai sơ đồ lực riêng',fontsize=14)
axes[1].text(0,-.62,'Hai lực có cùng độ lớn.',ha='center',fontsize=14)
save(fig,'solution-e13-3-forces')
fig,ax=plt.subplots(figsize=(5.2,4.9),layout='constrained')
u0=1/(1+np.sqrt(2))
for interval in [np.linspace(-2,-.015,900),np.linspace(.015,.985,900),np.linspace(1.015,3,900)]:
 f=-interval/abs(interval)**3+2*(1-interval)/abs(1-interval)**3
 ax.plot(interval,f,color='#235cc4',lw=2)
ax.axvline(0,color='#ab5260',ls='--',lw=1.2);ax.axvline(1,color='#ab5260',ls='--',lw=1.2)
ax.axhline(0,color='#606773',lw=.8)
ax.scatter([u0],[0],color='#b83042',zorder=4)
ax.annotate('Cân bằng\nu ≈ 0,414',(u0,0),xytext=(-1.8,-35),textcoords='data',fontsize=14,arrowprops={'arrowstyle':'->','color':'#b83042'})
ax.set(xlim=(-2,3),ylim=(-50,50),xlabel='Vị trí u = x/L',ylabel='Thành phần lực f = Fₓ/F₀')
ax.grid(alpha=.16)
save(fig,'solution-e13-10-force')
for solid,n in [(False,36),(True,37)]:
 fig,ax=plt.subplots(figsize=(5.1,4.0),layout='constrained')
 u=np.linspace(0,1,101);v=np.linspace(1,4,300)
 ax.plot(u,u if solid else np.zeros_like(u),color='#235cc4',lw=2.2)
 ax.plot(v,1/v**2,color='#235cc4',lw=2.2)
 if solid:ax.scatter([1],[1],color='#235cc4',zorder=5)
 else:
  ax.scatter([1,1],[0,1],facecolors='white',edgecolors='#235cc4',zorder=5,s=65,linewidths=1.5)
 ax.axvline(1,color='#999999',ls='--',lw=.8)
 ax.set(xlim=(0,4),ylim=(-.05,1.15),xlabel='Khoảng cách u = r/R',ylabel='Độ lớn lực F/F₀')
 ax.text(1.2,.88,'F₀ = GMm/R²',fontsize=14)
 ax.grid(alpha=.15)
 save(fig,f'solution-e13-{n}-'+('solid'if solid else'shell'))
fig,ax=plt.subplots(figsize=(4.7,3.8),layout='constrained');ax.axis('off');ax.set(xlim=(-1.1,1.2),ylim=(-1.3,1.3))
ax.scatter([0],[0],s=250,color='#45566b',zorder=5)
ax.annotate('',xy=(0,-1.05),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2.4,'color':'#235cc4'})
ax.annotate('',xy=(0,.87),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2.4,'color':'#b05a29'})
ax.text(.12,-.75,'mg',fontsize=14);ax.text(.12,.65,'Tₑ',fontsize=14)
ax.annotate('',xy=(-.65,-1.05),xytext=(-.65,0),arrowprops={'arrowstyle':'->','lw':1.5,'linestyle':'--','color':'#555555'})
ax.text(-1.05,-.53,'a',fontsize=14);ax.text(0,-1.25,'Về tâm Trái Đất',ha='center',fontsize=14)
ax.text(0,1.12,'Hai lực và gia tốc riêng',ha='center',fontsize=14)
save(fig,'solution-e13-42-forces')
print('Saved five required new solution diagrams; original source figures remain separate.')
