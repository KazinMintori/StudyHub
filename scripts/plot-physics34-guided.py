"""Supplementary paraxial rays for the wine-goblet problem; original art is not replaced."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parents[1]
evidence=json.loads((root/'qa/physics/chapter34/guided-data-checks.json').read_text())
out=root/'docs/vat-ly-2/bai-giang/img/young-34'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
for key,label in [('1.0','Ly rỗng'),('1.37','Ly chứa rượu')]:
 case=evidence['goblet'][key];positions=np.array([0.,.6,7.4,8.])
 indices=[1.,1.5,float(key),1.5,1.];radii=[4.,3.4,-3.4,-4.]
 image_x=case['finalPositionFromFirstSurfaceCm']
 xlim=(-34,13) if image_x<0 else (-2,15)
 fig,ax=plt.subplots(figsize=(9.2,3.5),layout='constrained')
 ax.axhline(0,color='#64748b',lw=.8)
 ax.axvspan(0,.6,color='#c4b5fd',alpha=.8)
 ax.axvspan(.6,7.4,color='#dbeafe',alpha=.8)
 ax.axvspan(7.4,8,color='#c4b5fd',alpha=.8)
 for x in positions:ax.axvline(x,color='#6d28d9',lw=.8)
 for height,color in [(.3,'#7c3aed'),(-.3,'#0891b2')]:
  y=height;u=0.;xs=[xlim[0] if image_x>0 else -3,0.];ys=[height,height]
  for j,x in enumerate(positions):
   if j:
    y+=(x-positions[j-1])*u/indices[j]
    xs.append(float(x));ys.append(y)
   u-=(indices[j+1]-indices[j])*y/radii[j]
  xmax=xlim[1]
  xs.append(xmax);ys.append(y+(xmax-8)*u)
  ax.plot(xs,ys,color=color,lw=1.6)
  if image_x<0:
   ax.plot([image_x,8],[0,y],ls='--',color=color,lw=1.)
  assert abs(y+(image_x-8)*u)<1e-12
 ax.scatter([image_x],[0],color='#be123c',zorder=5)
 text='Ảnh ảo: 30,0 cm trước mặt đầu' if image_x<0 else 'Ảnh thật: 3,72 cm sau mặt cuối'
 ax.annotate(text,(image_x,0),xytext=(0,34),textcoords='offset points',ha='left' if image_x<0 else 'right',color='#9f1239',arrowprops={'arrowstyle':'->','color':'#9f1239'})
 ax.set(xlim=xlim,ylim=(-.7,.7),xlabel='Tọa độ dọc trục x (cm)',ylabel='Độ cao tia (cm)',title=label+' trong gần đúng cận trục')
 ax.set_xticks(sorted(set([*ax.get_xticks(),0,8])))
 ax.set_xlim(xlim)
 ax.text(.98,.03,'Trục độ cao được phóng đại. Các mặt được biểu diễn tại đỉnh.',transform=ax.transAxes,ha='right',fontsize=9)
 ax.grid(alpha=.15)
 fig.savefig(out/('loi-giai-34-cau-noi-'+('rong' if key=='1.0' else 'ruou')+'.svg'))
 plt.close(fig)
print('Plotted both paraxial bundles with independently checked final intersections.')

# Normalize insignificant trailingXMLpathwhitespace for cleanGitdiffs.
for svg_path in out.glob('loi-giai-34-*.svg'):
    svg_text=svg_path.read_text(encoding='utf-8')
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_text.splitlines()).rstrip()+'\n',encoding='utf-8')
