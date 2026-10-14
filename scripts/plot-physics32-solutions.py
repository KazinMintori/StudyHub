"""Plot all10 measured standing-wave points with both least-squares models."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'qa/physics/chapter32/exercises-data-checks.json').read_text())['results']['48']
f=np.array(data['frequenciesHz']);d=np.array(data['distanceM'])
x=1e9/f;y=d*100
assert len(x)==len(y)==10
free_m,free_b=np.polyfit(x,y,1)
zero_m=np.dot(x,y)/np.dot(x,x)
assert abs(free_m*2e7-data['speedFreeFit'])<1e-4
assert abs(zero_m*2e7-data['speedOriginFit'])<1e-4
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'axes.labelsize':14,'axes.titlesize':14,
                     'xtick.labelsize':14,'ytick.labelsize':14,'legend.fontsize':14,
                     'svg.fonttype':'none','svg.hashsalt':'studyhub-physics32'})
fig,ax=plt.subplots(figsize=(9,6.5),constrained_layout=True)
grid=np.linspace(0,1.05,250)
ax.scatter(x,y,s=65,color='#6947a7',zorder=3,label='10 điểm đo')
ax.plot(grid,free_m*grid+free_b,lw=2,color='#236aac',label='Khớp cả hệ số góc và tung độ gốc')
ax.plot(grid,zero_m*grid,lw=2,ls='--',color='#b24758',label='Khớp với tung độ gốc bằng 0')
ax.set_xlabel('Nghịch đảo tần số 1/f (ns)')
ax.set_ylabel('Khoảng cách hai bụng d (cm)')
ax.set_title('Khoảng cách bụng tỉ lệ với nghịch đảo tần số')
ax.set_xlim(0,1.05);ax.set_ylim(0,16.5);ax.grid(alpha=.25);ax.legend(loc='upper left')
out=ROOT/'docs/vat-ly-2/bai-giang/img/young-32';out.mkdir(parents=True,exist_ok=True)
fig.savefig(out/'hinh-giai32-48.svg',bbox_inches='tight',facecolor='white',metadata={'Date':None})
fig.savefig(ROOT/'qa/physics/chapter32/solution48-plot-review.png',dpi=140,bbox_inches='tight',facecolor='white')
plt.close(fig)
p=out/'hinh-giai32-48.svg'
p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n',encoding='utf8')
print('Plotted all10 source measurements and two explicitly distinguished fits.')
