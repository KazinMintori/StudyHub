"""Private bridge analysis diagram plus exact reuse specification for Fig13.18."""
from pathlib import Path
import math,json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pymupdf

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-13';OUT.mkdir(exist_ok=True)
PREVIEW=ROOT/'qa/physics1-remaining/ch13/solution-previews';PREVIEW.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'studyhub-ch13-bridge-orbit','font.family':'DejaVu Sans','font.size':20})
fig,ax=plt.subplots(figsize=(5.0,5.8),facecolor='white')
e=.55;a=1.;b=math.sqrt(1-e*e);t=np.linspace(0,2*math.pi,800)
ax.plot(a*np.cos(t),b*np.sin(t),color='#3759a7',lw=2.5)
ax.plot([-1.13,1.13],[0,0],color='#9aa7b4',lw=1,zorder=0)
ax.scatter([0,e,1,-1],[0,0,0,0],s=[20,130,40,40],c=['#465669','#dc9a24','#594b9c','#594b9c'],zorder=5)
ax.text(0,.07,'O',ha='center',va='bottom',fontsize=20)
ax.text(e,.12,'S',ha='center',va='bottom',fontsize=20,color='#9a6512')
ax.text(-1.04,.10,'A',ha='right',va='bottom',fontsize=20)
ax.text(1.04,-.10,'P',ha='left',va='top',fontsize=20)
style=dict(arrowstyle='-|>',color='#ae3f61',lw=2.3,mutation_scale=20)
ax.annotate('',xy=(1,.60),xytext=(1,.025),arrowprops=style)
ax.text(1.06,.49,'vₚ',color='#ae3f61',fontsize=20,ha='left')
ax.annotate('',xy=(-1,-.60),xytext=(-1,-.025),arrowprops=style)
ax.text(-1.06,-.47,'vₐ',color='#ae3f61',fontsize=20,ha='right')
for x in(0,e,1):ax.plot([x,x],[.03,1.28],ls=(0,(3,4)),lw=.8,color='#a8b3be',zorder=0)
def dim(x1,x2,y,label,labelY):
 ax.annotate('',xy=(x2,y),xytext=(x1,y),arrowprops=dict(arrowstyle='<->',lw=1.3,color='#3e5367',mutation_scale=12))
 ax.text((x1+x2)/2,labelY,label,ha='center',va='center',fontsize=20,color='#273e51',bbox=dict(facecolor='white',edgecolor='none',pad=1))
dim(0,1,1.25,'a',1.25)
dim(0,e,1.01,'ea',1.01)
for x in(-1,e,1):ax.plot([x,x],[-.02,-1.30],ls=(0,(3,4)),lw=.8,color='#a8b3be',zorder=0)
dim(e,1,-.98,'rₚ',-1.04)
dim(-1,e,-1.28,'rₐ',-1.28)
ax.set_xlim(-1.65,1.72);ax.set_ylim(-1.47,1.44);ax.set_aspect('equal');ax.axis('off')
fig.subplots_adjust(left=.02,right=.98,bottom=.02,top=.98)
stem=OUT/'solution-bridge-13-orbit'
fig.savefig(stem.with_suffix('.svg'),bbox_inches='tight',pad_inches=.13,metadata={'Date':None,'Creator':'StudyHub solution diagram'})
svg=stem.with_suffix('.svg')
svg.write_bytes(('\n'.join(line.rstrip()for line in svg.read_text(encoding='utf-8').splitlines())+'\n').encode('utf-8'))
fig.savefig(PREVIEW/(stem.stem+'.png'),dpi=160,bbox_inches='tight',pad_inches=.13)
plt.close(fig)

print('Saved the required bridge analysis sketch.')
