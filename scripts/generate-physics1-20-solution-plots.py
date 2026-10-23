from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'docs/vat-ly-1/bai-giang/img/young-20'
data=json.loads((ROOT/'qa/physics1-priority/ch20-numbered-parent-values.json').read_text(encoding='utf-8'))['cases']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path'})
def draw(ax,v,p,label,color):
 ax.plot(v,p,color=color,lw=2)
 k=len(v)//2;j=min(k+max(1,len(v)//20),len(v)-1)
 ax.annotate('',(v[j],p[j]),(v[k],p[k]),arrowprops=dict(arrowstyle='->',color=color,lw=2))
def finish(fig,ax,name):
 ax.grid(alpha=.25);ax.set_xlabel('Thể tích V (L)');ax.set_ylabel('Áp suất p (kPa)')
 fig.savefig(out/name);plt.close(fig)
R=8.314462618;TH=773.15;TC=data['30']['coldK'];Va=.005;Vb=Va*math.exp(500/(2*R*TH));f=(TH/TC)**1.5;Vc=Vb*f;Vd=Va*f
fig,ax=plt.subplots(figsize=(6.4,4.3),layout='constrained')
for a,b,kind,col in [(Va,Vb,'hot','#dc2626'),(Vb,Vc,'ad1','#6d28d9'),(Vc,Vd,'cold','#1d4ed8'),(Vd,Va,'ad2','#6d28d9')]:
 v=np.linspace(a,b,150)
 if kind=='hot':p=2*R*TH/v
 elif kind=='cold':p=2*R*TC/v
 elif kind=='ad1':p=(2*R*TH/Vb)*(Vb/v)**(5/3)
 else:p=(2*R*TC/Vd)*(Vd/v)**(5/3)
 draw(ax,v*1000,p/1000,kind,col)
for label,v,t in [('a',Va,TH),('b',Vb,TH),('c',Vc,TC),('d',Vd,TC)]:
 p=2*R*t/v;ax.plot(v*1000,p/1000,'ko',ms=4);ax.annotate(label,(v*1000,p/1000),xytext=({'a':(-15,7),'b':(6,-1),'c':(6,-2),'d':(-15,-10)}[label]),textcoords='offset points')
ax.text(.45,.84,'ab: Nhận nhiệt',transform=ax.transAxes,color='#dc2626');ax.text(.45,.75,'cd: Thải nhiệt',transform=ax.transAxes,color='#1d4ed8')
finish(fig,ax,'d-do-thi20-30.svg')
states=data['43']['states'];fig,ax=plt.subplots(figsize=(6.4,4.3),layout='constrained')
for i,j,kind in [(0,1,'isobar'),(1,2,'isochor'),(2,3,'isotherm'),(3,0,'isochor')]:
 a,b=states[i],states[j];v=np.linspace(a['V'],b['V'],100)
 p=a['p']*a['V']/v if kind=='isotherm' else np.linspace(a['p'],b['p'],100)
 draw(ax,v*1000,p/1000,'','#6d28d9')
for i,a in enumerate(states):
 ax.plot(a['V']*1000,a['p']/1000,'ko',ms=4);ax.annotate(str(i+1),(a['V']*1000,a['p']/1000),xytext=(7,5),textcoords='offset points')
ax.set_xlim(3.7,6.5);ax.set_ylim(95,225);finish(fig,ax,'e-do-thi20-43.svg')
s=data['47']['states'];fig,ax=plt.subplots(figsize=(6.4,4.3),layout='constrained')
for a,b,kind,col in [('a','b','ad','#6d28d9'),('b','c','iso','#dc2626'),('c','d','ad','#6d28d9'),('d','a','iso','#1d4ed8')]:
 u,w=s[a],s[b];v=np.linspace(u['V'],w['V'],120);p=u['p']*(u['V']/v)**1.4 if kind=='ad' else np.linspace(u['p'],w['p'],120)
 draw(ax,v*1000,p/1000,'',col)
for name,a in s.items():
 ax.plot(a['V']*1000,a['p']/1000,'ko',ms=4);ax.annotate(name,(a['V']*1000,a['p']/1000),xytext=({'a':(7,-8),'b':(7,0),'c':(7,0),'d':(7,4)}[name]),textcoords='offset points')
ax.text(.38,.86,'bc: Nhận nhiệt',transform=ax.transAxes,color='#dc2626');ax.text(.38,.77,'da: Thải nhiệt',transform=ax.transAxes,color='#1d4ed8')
finish(fig,ax,'e-do-thi20-47.svg')
print('Generated3 state-consistent pV solution diagrams.')
