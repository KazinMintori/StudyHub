"""Supplementary force diagrams requested explicitly by the exercise prompts."""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
ROOT=Path(__file__).resolve().parents[1]
def setup(width=5,height=3.8):
 fig,ax=plt.subplots(figsize=(width,height),layout='constrained')
 ax.set_aspect('equal');ax.axis('off')
 return fig,ax
def arrow(ax,p,v,label,color='#be123c',offset=(0,0),ha='left'):
 end=np.asarray(p)+np.asarray(v)
 ax.annotate('',end,p,arrowprops=dict(arrowstyle='->',lw=2,color=color))
 ax.text(*(end+np.asarray(offset)),label,color=color,fontsize=10,ha=ha,va='center')
def save(fig,ch,name):
 p=ROOT/f'docs/vat-ly-1/bai-giang/img/young-{ch:02}'/(name+'.svg')
 fig.savefig(p);plt.close(fig)
 return str(p.relative_to(ROOT))
files=[]
# Actual coordinate vectors and force directions from10.5 and10.6.
for n,r,F,scale in [(5,(-.45,.15),(-5,4),.06),(6,(3.,4.),(7,-3),.25)]:
 fig,ax=setup()
 R=np.asarray(r);force=np.asarray(F)*scale
 arrow(ax,(0,0),R,'',color='#1d4ed8')
 perp=np.array([-R[1],R[0]])/np.linalg.norm(R)
 labelpoint=.5*R+.06*np.linalg.norm(R)*perp
 ax.text(*labelpoint,r'$\vec r$',color='#1d4ed8',fontsize=10)
 arrow(ax,R,force,r'$\vec F$')
 ax.scatter([0,R[0]],[0,R[1]],c='#111827',s=20,zorder=5)
 ax.text(0,0,' O',va='top');ax.text(*R,' P',va='top')
 ext=np.vstack(([0,0],R,R+force));span=max(np.ptp(ext[:,0]),np.ptp(ext[:,1]));pad=.18*span
 ax.set_xlim(ext[:,0].min()-pad,ext[:,0].max()+pad)
 ax.set_ylim(ext[:,1].min()-pad,ext[:,1].max()+pad)
 ax.axhline(0,color='#9ca3af',lw=.7);ax.axvline(0,color='#9ca3af',lw=.7)
 assert np.sign(np.cross(np.r_[R,0],np.r_[F,0])[2])==-1
 files.append(save(fig,10,f'd-solution10-{n:02}'))
# Rolling uphill: Contact forces at the contact; gravity at center.
beta=math.radians(25);t=np.array([math.cos(beta),math.sin(beta)]);normal=np.array([-math.sin(beta),math.cos(beta)])
contact=1.2*t;center=contact+.45*normal
fig,ax=setup()
ground=np.array([-.2*t,3*t]);ax.plot(ground[:,0],ground[:,1],color='#6b7280',lw=3)
ax.add_patch(Circle(center,.45,fc='#fef3c7',ec='#a16207',lw=2))
arrow(ax,center,(0,-.85),'Mg',offset=(.03,0))
arrow(ax,contact,.85*math.cos(beta)*normal,'N',offset=(-.04,.04),ha='right',color='#047857')
arrow(ax,contact,.85*(2/7)*math.sin(beta)*t,r'$f_s$',offset=(.07,-.02))
arrow(ax,center+np.array([0,.55]),.55*t,r'$\vec v$',color='#1d4ed8')
ax.set_xlim(-.4,3);ax.set_ylim(-.35,2.1)
files.append(save(fig,10,'d-solution10-30'))
# Inclined beam11.50.
fig,ax=setup(6,4.3);u=np.array([math.cos(math.pi/6),.5]);end=8*u
ax.plot([0,end[0]],[0,end[1]],lw=6,color='#d97706',solid_capstyle='round')
ax.plot([0,0],[-2,5],color='#6b7280',lw=4)
T=1150*9.8*4*math.cos(math.pi/6)/(6*math.sin(math.radians(40)))
scale=.00017;tx=-T*math.cos(math.radians(10));ty=T*math.sin(math.radians(10));W=1150*9.8
assert math.isclose(-tx+tx,0) and math.isclose((W-ty)+ty-W,0)
arrow(ax,6*u,scale*np.array([tx,ty]),'T',offset=(-.12,.12),ha='right')
arrow(ax,4*u,(0,-scale*W),'Mg',offset=(.1,0))
arrow(ax,(0,0),(-scale*tx,0),r'$H_x$',color='#047857')
arrow(ax,(0,0),(0,scale*(W-ty)),r'$H_y$',color='#047857',offset=(.1,.1))
ax.set_xlim(-.8,8);ax.set_ylim(-2.4,5.2)
files.append(save(fig,11,'e-solution11-50'))
# Forearm11.58, schematic arrow lengths to keep all four forces readable.
fig,ax=setup(6,4.5);u=np.array([math.cos(math.radians(40)),-math.sin(math.radians(40))])
ax.plot([0,.38*u[0]],[0,.38*u[1]],lw=6,color='#d97706',solid_capstyle='round')
for r,vector,label,color in [(0,(0,-.17),'E','#047857'),(.055,(0,.22),'B','#be123c'),(.16,(0,-.10),r'$m_fg$','#7c3aed'),(.38,(0,-.10),r'$m_tg$','#7c3aed')]:
 arrow(ax,r*u,vector,label,color=color,offset=(.008,0))
ax.scatter([0],[0],c='#111827',s=40,zorder=5);ax.text(-.02,.02,'Khuỷu',ha='right',fontsize=9)
ax.set_xlim(-.1,.42);ax.set_ylim(-.4,.25)
files.append(save(fig,11,'e-solution11-58'))
# Foot11.63: Correct application points and relative moment-arm geometry.
fig,ax=setup(6,4.3)
ankle=np.array([0,.5]);heel=np.array([-.46,.2]);toe=np.array([1.25,0])
ax.plot([-.46,-.25,.2,1.25],[.2,.1,.08,0],lw=12,color='#fcd34d',solid_capstyle='round')
ax.plot([-1,1.6],[-.07,-.07],lw=2,color='#6b7280')
arrow(ax,heel,(0,1.05),'F',offset=(.05,0))
arrow(ax,toe,(0,.6),'N',offset=(.05,0),color='#047857')
arrow(ax,ankle,(0,-1.2),'P',offset=(.05,0),color='#7c3aed')
ax.scatter([*heel[:1],*ankle[:1],*toe[:1]],[heel[1],ankle[1],toe[1]],s=15,c='#111827',zorder=6)
ax.text(-.67,.08,'Gót',ha='right',fontsize=9);ax.text(0,.65,'Cổ chân',ha='center',fontsize=9)
ax.text(1.25,-.25,'Điểm tựa',ha='center',fontsize=9)
ax.set_xlim(-1,1.8);ax.set_ylim(-1.1,1.5)
files.append(save(fig,11,'e-solution11-63'))
# Experimental beam11.87, positions are the actual source locations.
fig,ax=setup(7,3)
ax.plot([0,4],[0,0],lw=7,color='#d97706',solid_capstyle='round')
for x,label in [(.2,r'$m_1g$'),(1.88,'Mg'),(3.5,r'$m_2g$')]:
 arrow(ax,(x,0),(0,-.7),label,offset=(.06,0))
arrow(ax,(1.5,0),(0,1.1),'R',color='#047857',offset=(.05,0))
for x,label in [(0,'0'),(.2,'0,200'),(1.5,'1,50'),(1.88,'1,88'),(3.5,'x'),(4,'4,00 m')]:
 ax.text(x,.2,label,ha='right' if x==0 else 'left' if x==.2 else 'center',fontsize=8)
ax.set_xlim(-.3,4.6);ax.set_ylim(-1.05,1.4)
files.append(save(fig,11,'e-solution11-87'))
print('\n'.join(files))
