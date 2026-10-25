"""Generate only the new solution plots explicitly requested in12.85and12.87."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import subprocess,sys
root=Path(__file__).resolve().parents[1]
out=root/'qa/physics1-remaining/ch12';out.mkdir(parents=True,exist_ok=True)
assets=root/'docs/vat-ly-1/bai-giang/img/young-12'
data=json.loads(subprocess.check_output([sys.executable,'-I','-X','utf8',str(root/'raw_materials/physics/verify_chapter12_exercises_parent.py')]))['records']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'none','svg.hashsalt':'studyhub-ch12-solutions','axes.spines.top':False,'axes.spines.right':False})

def save(fig,name):
 path=assets/(name+'.svg')
 fig.savefig(path,facecolor='white',metadata={'Date':None,'Creator':'StudyHub, independently checked source data'})
 path.write_bytes(('\n'.join(line.rstrip()for line in path.read_text(encoding='utf-8').splitlines())+'\n').encode('utf-8'))
 fig.savefig(out/(name+'.png'),dpi=140,facecolor='white')
 plt.close(fig)

r=data['12.85']
fig,ax=plt.subplots(figsize=(5.4,5.0),layout='constrained')
ax.scatter(r['atomic_mass_g_mol'],r['density_g_cm3'],color='#235cc4',s=38)
offsets={'Al':(5,6),'Fe':(-23,-2),'Cu':(6,3),'Ag':(5,6),'Pb':(7,-4),'Hg':(-28,3),'Au':(-28,1),'Pt':(6,5)}
for name,x,y in zip(r['elements'],r['atomic_mass_g_mol'],r['density_g_cm3']):
 ax.annotate(name,(x,y),xytext=offsets[name],textcoords='offset points',fontsize=14)
ax.set_xlabel('Khối lượng mol M (g/mol)')
ax.set_ylabel('Khối lượng riêng ρ (g/cm³)')
ax.set_xlim(0,235);ax.set_ylim(0,24.5);ax.grid(alpha=.18)
save(fig,'solution-p12-85-density')

r=data['12.87'];x=np.array(r['pressure_atm']);R=np.array(r['range_m'])
S,B=r['fit_slope_m2_per_atm'],r['fit_intercept_m2']
assert len(x)==5 and np.allclose(np.polyfit(x,R*R,1),[S,B])
fig,(ax,legend)=plt.subplots(2,1,figsize=(5.4,5.8),layout='constrained',gridspec_kw={'height_ratios':[3.2,1.3]})
xx=np.linspace(0,4.3,200)
ax.plot(xx,S*xx+B,color='#235cc4',label='Đường khớp')
ax.scatter(x,R*R,color='#b83042',s=38,label='Năm điểm đo',zorder=3)
ax.set_xlabel('Áp suất dư (atm)');ax.set_ylabel('R² (m²)')
ax.set_xlim(0,4.3);ax.set_ylim(0,135);ax.grid(alpha=.18)
ax.legend(loc='upper left',fontsize=14)
legend.axis('off')
legend.text(.02,.98,'R² = S × áp suất dư + B\nS ≈ 25,6787 m²/atm\nB ≈ 16,3848 m²',va='top',fontsize=14,transform=legend.transAxes)
save(fig,'solution-p12-87-fit')
plt.rcParams.update({'font.size':16,'axes.labelsize':18,'axes.titlesize':17,'xtick.labelsize':16,'ytick.labelsize':16})
t=np.linspace(0,1,401);height=(1-t)**2
assert np.all(np.diff(height)<=0)and height[0]==1 and height[-1]==0
fig,ax=plt.subplots(figsize=(5.0,4.2),layout='constrained')
ax.plot(t,height,color='#4338ca',lw=3,label='y/H = (1 − t/T)²')
ax.scatter([0,1],[1,0],color='#4338ca',s=35,zorder=4)
ax.set(xlim=(-.02,1.04),ylim=(-.04,1.08),xlabel='Thời gian t',ylabel='Độ cao y',title='Mực nước khi tháo cạn')
ax.set_xticks([0,.25,.5,.75,1],['0','T/4','T/2','3T/4','T'])
ax.set_yticks([0,.25,.5,.75,1],['0','H/4','H/2','3H/4','H'])
ax.grid(alpha=.24);ax.legend(loc='upper right',frameon=True);ax.spines[['top','right']].set_visible(False)
save(fig,'bridge-12-water-height-solution')
print('Saved3verified solution plots;original textbook figures are unchanged.')
