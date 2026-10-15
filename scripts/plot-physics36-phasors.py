"""Supplementary solution diagrams, separate from untouched source figures."""
from pathlib import Path
import math,json,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'qa/physics/chapter36/discussion-data-checks.json').read_text(encoding='utf-8-sig'))
out=root/'docs/vat-ly-2/bai-giang/img/young-36';out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','font.size':12})
for N,stem in [(4,'loi-giai-q36-06'),(8,'loi-giai-q36-07')]:
 cases=[x for x in data['phasorCases'] if x['N']==N]
 for index,case in enumerate(cases):
  fig,ax=plt.subplots(figsize=(4.5,4.8))
  phi=case['phasePi']*math.pi;z=np.exp(1j*np.arange(N)*phi);points=np.r_[0,np.cumsum(z)];assert abs(points[-1])<1e-13
  ax.axhline(0,color='#cbd5e1',lw=.6);ax.axvline(0,color='#cbd5e1',lw=.6)
  for j in range(N):
   start=points[j];v=z[j];ax.annotate('',xy=(start.real+v.real,start.imag+v.imag),xytext=(start.real,start.imag),arrowprops=dict(arrowstyle='->',color=plt.cm.tab10(j%10),lw=2))
   mid=start+.52*v;shift=.08*(j-(N-1)/2);ax.text(mid.real+.05,mid.imag+.08+shift,str(j+1),fontsize=11,color=plt.cm.tab10(j%10))
  extent=max(np.ptp(points.real),np.ptp(points.imag),1)*1.8;cx=(min(points.real)+max(points.real))/2;cy=(min(points.imag)+max(points.imag))/2
  ax.set_xlim(cx-extent/2,cx+extent/2);ax.set_ylim(cy-extent/2,cy+extent/2)
  phase={.25:r'\pi/4',.5:r'\pi/2',.75:r'3\pi/4',1.:r'\pi',1.5:r'3\pi/2',1.75:r'7\pi/4'}[case['phasePi']]
  ax.scatter([0],[0],c='#111827',s=25,zorder=5);ax.set_aspect('equal');ax.set_title(r'$\phi='+phase+'$');ax.set_xlabel('Thành phần ngang');ax.set_ylabel('Thành phần đứng')
  fig.suptitle('Tổng '+str(N)+' vectơ pha bằng không',fontsize=14)
  fig.text(.5,.02,'Cặp khử: '+', '.join('('+str(a)+','+str(b)+')' for a,b in case['pairsOneBased']),ha='center',fontsize=10)
  fig.tight_layout(rect=(0,.04,1,.93));name=stem+'-'+chr(97+index);dest=out/(name+'.svg');fig.savefig(dest,bbox_inches='tight');fig.savefig(root/'qa/physics/chapter36'/(name+'.png'),dpi=120,bbox_inches='tight');plt.close(fig)
  text=dest.read_text(encoding='utf-8');dest.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n',encoding='utf-8')
  print(name)
