"""Principal-ray sketches supplement source figures and use verified cận-trục results."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parents[1]
data=json.loads((root/'qa/physics/chapter34/exercises-01-39-data-checks.json').read_text())['results']
data.update(json.loads((root/'qa/physics/chapter34/exercises-40-65-data-checks.json').read_text())['results'])
out=root/'docs/vat-ly-2/bai-giang/img/young-34';out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
cases=[(5,'mirror',11.,16.5),(6,'mirror',-11.,16.5),(11,'mirror',16.,12.),(13,'mirror',2.5,1.25),(30,'lens',-48.,16.),(40,'lens',12.,data['40']['objectDistanceCm']),(41,'lens',-48.,data['41']['objectDistanceCm']),(42,'lens',data['42']['focalLengthCm'],16.)]
for num,kind,f,s in cases:
 sp=1/(1/f-1/s);m=-sp/s
 if num==13:assert abs(sp-data[str(num)]['imageDistanceCm'])<1e-10
 else:assert abs(sp-data[str(num)]['imageDistanceCm'])<1e-10
 image_x=-sp if kind=='mirror' else sp
 xs=[-s,image_x,-f if kind=='mirror' else f,0.]
 span=max(xs)-min(xs);xmin=min(xs)-.12*span;xmax=max(xs)+.12*span
 fig,ax=plt.subplots(figsize=(8.4,3.5),layout='constrained')
 ax.axhline(0,color='#64748b',lw=.8)
 ax.axvline(0,color='#6d28d9',lw=2)
 ax.annotate('',(-s,1),(-s,0),arrowprops={'arrowstyle':'->','lw':2,'color':'#0f766e'})
 ax.annotate('',(image_x,m),(image_x,0),arrowprops={'arrowstyle':'->','lw':2,'color':'#be123c'})
 ax.text(-s,1.08,'Vật',ha='center',color='#0f766e')
 ax.text(image_x,m+(.10 if m>0 else -.28),'Ảnh '+('thật' if sp>0 else 'ảo'),ha='center',color='#be123c')
 ax.scatter([-f if kind=='mirror' else f],[0],color='#6d28d9',s=15)
 ax.text(-f if kind=='mirror' else f,-.2,'F',ha='center',color='#6d28d9')
 # Incoming parallelray and centralray to opticalvertex.
 ax.plot([-s,0],[1,1],color='#7c3aed',lw=1.4)
 ax.plot([-s,0],[1,0],color='#0891b2',lw=1.4)
 end=xmin if kind=='mirror' else xmax
 slope1=1/f if kind=='mirror' else -1/f
 slope2=1/s if kind=='mirror' else -1/s
 ax.plot([0,end],[1,1+slope1*end],color='#7c3aed',lw=1.4)
 ax.plot([0,end],[0,slope2*end],color='#0891b2',lw=1.4)
 if sp<0:
  ax.plot([0,image_x],[1,m],ls='--',color='#7c3aed',lw=1.)
  ax.plot([0,image_x],[0,m],ls='--',color='#0891b2',lw=1.)
 assert abs(1+slope1*image_x-m)<1e-10
 assert abs(slope2*image_x-m)<1e-10
 ax.set(xlim=(xmin,xmax),ylim=(min(0,m)-.65,max(1,m)+.55),xlabel='Tọa độ dọc trục (cm)',ylabel='Độ cao / chiều cao vật',title=f'Bài 34.{num}: '+('Gương cầu' if kind=='mirror' else 'Thấu kính mỏng'))
 ax.grid(alpha=.15)
 if num in [40,41]:ax.invert_xaxis()
 note='Mặt quang học tại x = 0\nNét đứt: Đường kéo dài'
 if num in [40,41]:note+='\nÁnh sáng truyền từ phải sang trái'
 fig.suptitle(note,fontsize=10)
 fig.savefig(out/f'loi-giai-34-{num:02}-tia.svg')
 fig.savefig(root/f'qa/physics/chapter34/loi-giai-34-{num:02}-tia.png',dpi=125)
 plt.close(fig)
print('Plotted eight independently intersected principal-ray sketches.')

# Normalize insignificant trailingXMLpathwhitespace for cleanGitdiffs.
for svg_path in out.glob('loi-giai-34-*.svg'):
    svg_text=svg_path.read_text(encoding='utf-8')
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_text.splitlines()).rstrip()+'\n',encoding='utf-8')
