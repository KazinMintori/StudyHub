"""Generate the requested solution graphs and phase diagrams in Vietnamese."""
from pathlib import Path
import math,re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-31'
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'axes.labelsize':14,
                     'axes.titlesize':14,'xtick.labelsize':14,'ytick.labelsize':14,
                     'legend.fontsize':14,'svg.fonttype':'none','svg.hashsalt':'studyhub-physics31'})
PURPLE='#6947a7';BLUE='#236aac';RED='#b24758';GREEN='#33784c'
def save(fig,name):
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',facecolor='white',metadata={'Date':None})
 plt.close(fig)
 p=OUT/(name+'.svg')
 p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n',encoding='utf8')
def arrow(ax,start,end,color,label=None,where=None):
 ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','lw':2.5,'color':color})
 if label:ax.text(*(where or end),label,color=color,fontsize=14)

w=np.linspace(.01,2000,8001)
V,R,L,C=100,200,2,.50e-6
X=w*L-1/(w*C);Z=np.hypot(R,X);I=V/Z;P=.5*I**2*R
assert math.isclose(1/math.sqrt(L*C),1000)
assert math.isclose(V**2/(2*R),25)
fig,axes=plt.subplots(2,1,figsize=(9,7),sharex=True,constrained_layout=True)
axes[0].plot(w,P,color=PURPLE,lw=2.2);axes[0].set_ylabel('Công suất P (W)')
axes[1].plot(w,I,color=BLUE,lw=2.2);axes[1].set_ylabel('Biên độ dòng I (A)')
axes[1].set_xlabel('Tần số góc ω (rad/s)')
for ax in axes:ax.axvline(1000,color='#777777',ls='--');ax.grid(alpha=.25);ax.set_xlim(0,2000)
axes[0].set_title('Cùng tần số đỉnh, công suất tỉ lệ bình phương biên độ dòng')
save(fig,'hinh-giai31-49')

VL=I*w*L;VC=I/(w*C)
loss=R*R*C/L
wL=1000/math.sqrt(1-loss/2);wC=1000*math.sqrt(1-loss/2)
assert wC<1000<wL
fig,axes=plt.subplots(2,1,figsize=(9,7),constrained_layout=True)
for ax in axes:
 ax.plot(w,VL,color=RED,lw=2,label='Điện áp cuộn cảm')
 ax.plot(w,VC,color=BLUE,lw=2,label='Điện áp tụ')
 ax.axvline(1000,color='#777777',ls='--')
 ax.set_ylabel('Biên độ điện áp (V)');ax.grid(alpha=.25)
axes[0].set_xlim(0,2000);axes[0].legend(loc='upper right')
axes[0].set_title('Hai điện áp bằng nhau tại cộng hưởng dòng')
axes[1].set_xlim(965,1035);axes[1].set_ylim(800,1020)
axes[1].set_xlabel('Tần số góc ω (rad/s)')
for omega,color,text,shift in [(wC,BLUE,'Đỉnh điện áp tụ',-24),(wL,RED,'Đỉnh điện áp cuộn',5)]:
 z=math.hypot(R,omega*L-1/(omega*C))
 voltage=V/z*(1/(omega*C) if color==BLUE else omega*L)
 axes[1].plot(omega,voltage,'o',color=color)
 axes[1].annotate(text,xy=(omega,voltage),xytext=(omega+shift,920 if color==BLUE else 960),
                  arrowprops={'arrowstyle':'->','color':color},color=color)
save(fig,'hinh-giai31-50')

# Exercise31.12: The current arrow uses its own scale and only gives the phase.
R,L,w,V=200,.4,250,30
Z=math.hypot(R,w*L);I=V/Z;VR,VL=I*R,I*w*L
assert math.isclose(VR*VR+VL*VL,V*V)
fig,ax=plt.subplots(figsize=(8,5),constrained_layout=True)
arrow(ax,(0,0),(VR,0),RED,r'$V_R=26{,}8\,\mathrm{V}$',(11,-1.8))
arrow(ax,(0,0),(0,VL),BLUE,r'$V_L=13{,}4\,\mathrm{V}$',(1,11.5))
arrow(ax,(0,0),(VR,VL),PURPLE,r'$V=30{,}0\,\mathrm{V}$',(20,14.4))
ax.plot([VR,VR],[0,VL],ls='--',color='#777777')
ax.plot([0,VR],[VL,VL],ls='--',color='#777777')
arrow(ax,(0,-4),(10,-4),GREEN,'I (Mốc pha, thang riêng)',(11,-4.6))
angle=math.atan2(VL,VR)
t=np.linspace(0,angle,40);ax.plot(5*np.cos(t),5*np.sin(t),color='#777777')
ax.text(5.3,1.5,r'$\phi=26{,}6^\circ$',fontsize=14)
ax.set_aspect('equal');ax.set_xlim(-3,33);ax.set_ylim(-7,18)
ax.axis('off');ax.set_title('Điện áp nguồn sớm dòng trong mạch RL')
save(fig,'hinh-giai31-12')

fig,axes=plt.subplots(1,2,figsize=(12,6),constrained_layout=True)
for ax,IC,IL,title in [(axes[0],3,1,'Dòng tổng sớm điện áp'),(axes[1],1,3,'Dòng tổng trễ điện áp')]:
 IR=3
 arrow(ax,(0,0),(IR,0),RED,r'$I_R$',(1.5,-.35))
 arrow(ax,(0,0),(0,IC),BLUE,r'$I_C$',(.15,IC))
 arrow(ax,(0,0),(0,-IL),GREEN,r'$I_L$',(.15,-IL))
 arrow(ax,(0,0),(IR,IC-IL),PURPLE,'I',(IR+.1,IC-IL))
 ax.plot([IR,IR],[0,IC-IL],ls='--',color='#777777')
 ax.plot([0,IR],[IC-IL,IC-IL],ls='--',color='#777777')
 ax.text(.8,3.5,'Điện áp là mốc pha',fontsize=14)
 ax.set_title(title);ax.set_xlim(-.8,4);ax.set_ylim(-3.8,4.1);ax.set_aspect('equal');ax.axis('off')
save(fig,'hinh-giai31-54')

fig,ax=plt.subplots(figsize=(9,7),constrained_layout=True)
for n in range(10):
 y=9-n;color=BLUE if n%2==0 else RED
 ax.plot([1,5],[y,y],color=color,lw=6,solid_capstyle='butt')
 rod=.4 if n%2==0 else 5.6
 ax.plot([rod,1 if n%2==0 else 5],[y,y],color=color,lw=1.5)
 if n<9:ax.text(6.0,y-.65,'Khe '+str(n+1),fontsize=14)
ax.plot([.4,.4],[1,9],color=BLUE,lw=2)
ax.plot([5.6,5.6],[0,8],color=RED,lw=2)
ax.text(.1,10,'Nhóm A: Năm bản',color=BLUE,fontsize=14)
ax.text(4.2,10,'Nhóm B: Năm bản',color=RED,fontsize=14)
ax.text(1.0,-1.2,'Mỗi khe đối diện có khoảng cách g/2',fontsize=14)
ax.set_xlim(-.2,8);ax.set_ylim(-1.7,10.7);ax.axis('off')
ax.set_title('Mười bản đan xen tạo chín khe chịu cùng hiệu điện thế')
save(fig,'hinh-giai31-53-khe')
print('Generated five Vietnamese solution graphs and phase/plate diagrams.')
