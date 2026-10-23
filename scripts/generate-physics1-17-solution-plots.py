from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'qa/physics1-priority/ch17-numbered-a-values.json').read_text(encoding='utf-8'))['cases']['44']
t=[0,data['startMelting_min'],data['finishMelting_min'],500]
T=[-15,0,0,data['temperatureAt500min']]
fig,ax=plt.subplots(figsize=(6,4),layout='constrained')
ax.plot(t,T,'o-',color='#1d4ed8',lw=2)
ax.set(xlabel='Thời gian (phút)',ylabel='Nhiệt độ (°C)',xlim=(0,510),ylim=(-20,100))
ax.axhline(0,color='#6b7280',lw=.7)
ax.text(110,4,'Nóng chảy ở 0°C',ha='center',fontsize=9)
ax.grid(alpha=.25)
out=ROOT/'docs/vat-ly-1/bai-giang/img/young-17'
fig.savefig(out/'d-plot17-44.svg');plt.close(fig)
# Bridge diagram, to accompany the requested sketch.
fig,ax=plt.subplots(figsize=(7,3.2),layout='constrained');ax.set_aspect('equal');ax.axis('off')
ax.add_patch(Rectangle((.1,.1),1.2,1.3,fc='#dbeafe',ec='#1d4ed8'))
ax.add_patch(Rectangle((1.3,.55),3.2,.4,fc='#fed7aa',ec='#b45309',lw=2))
ax.plot([1.3,4.5],[.49,.49],color='#6b7280',lw=2)
ax.plot([1.3,4.5],[1.01,1.01],color='#6b7280',lw=2)
ax.plot([4.5,4.5],[.55,.95],color='#111827',lw=5)
ax.annotate('',(4.4,.75),(5.5,.75),arrowprops=dict(arrowstyle='->',color='#dc2626',lw=2))
ax.text(5.1,1.0,'Bức xạ ròng',ha='center',fontsize=10,color='#dc2626')
ax.text(.7,.75,'Hiđrô\nrắn/lỏng\n13,84 K',ha='center',va='center',fontsize=10)
ax.text(2.9,.75,'Thanh đồng, mặt bên cách nhiệt',ha='center',va='center',fontsize=8)
ax.text(5.4,1.45,'Vách bao quanh: 500 K',ha='center',fontsize=10)
ax.annotate('',(4.5,.25),(1.3,.25),arrowprops=dict(arrowstyle='<->',color='#374151'))
ax.text(2.9,.08,'L = 0,200 m',ha='center',va='top',fontsize=9)
ax.text(4.55,.35,'Đầu bôi đen, T',ha='left',fontsize=9)
ax.text(2.9,1.25,'R = 0,0250 m',ha='center',fontsize=9)
ax.set_xlim(-.1,6.6);ax.set_ylim(-.1,1.8)
fig.savefig(out/'c-bridge-radiation-conduction.svg');plt.close(fig)
print('Saved requested heating curve and bridge dimension/heat-flow diagram.')
