"""Scientific solution plots, reproducible from their stated formulas."""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-22';out.mkdir(parents=True,exist_ok=True)
qa=root/'qa/physics/chapter22/plots';qa.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
color='#4c47a1'
def save(fig,name):
 fig.tight_layout();fig.savefig(out/(name+'.svg'),bbox_inches='tight');fig.savefig(qa/(name+'.png'),dpi=110,bbox_inches='tight');plt.close(fig)
def graph(name,segments,boundaries,labels,title,ylabel='E (đơn vị quy ước)',xmax=6):
 fig,ax=plt.subplots(figsize=(6.5,3.6))
 for lo,hi,f in segments:
  xs=np.linspace(max(lo,.04),hi,350);ys=np.array([f(x) for x in xs]);ax.plot(xs,ys,color=color,lw=2)
 for b in boundaries:ax.axvline(b,color='#aaa',lw=.8,ls=':')
 ax.axhline(0,color='#888',lw=.7);ax.set(xlim=(0,xmax),xlabel='Khoảng cách r',ylabel=ylabel,title=title)
 endlabel={'c':'2c','d':'2d','b':'2b','2R':'6R','R':'3R'}.get(labels[-1],'')
 ax.set_xticks([0]+boundaries+[xmax],['0']+labels+[endlabel])
 ax.grid(alpha=.15)
 save(fig,name)

graph('loi-giai-22-37',[(0,1,lambda x:0),(1,2,lambda x:1/x),(2,3,lambda x:0),(3,6,lambda x:1/x)],[1,2,3],['a','b','c'],'Cáp đồng trục')
graph('loi-giai-22-38',[(.25,1,lambda x:1/x),(1,2,lambda x:0),(2,4,lambda x:2/x)],[1,2],['a','b'],'Dây trục và ống dẫn cùng điện tích dài',xmax=4)
graph('loi-giai-22-39',[(0,1,lambda x:x),(1,3,lambda x:1/x)],[1],['R'],'Trụ cách điện tích điện đều',ylabel='E / E(R)',xmax=3)
graph('loi-giai-22-40',[(0,1,lambda x:0),(1,2,lambda x:1/x**2),(2,3,lambda x:0),(3,6,lambda x:1/x**2)],[1,2,3],['a','b','c'],'Cầu dẫn trong vỏ cầu trung hòa')
graph('loi-giai-22-41',[(0,1,lambda x:0),(1,2,lambda x:1/x**2),(2,6,lambda x:2/x**2)],[1,2],['R','2R'],'Cầu dẫn và vỏ cách điện cùng Q')
fig,axes=plt.subplots(1,2,figsize=(8,3.5))
for ax,sign,title in zip(axes,[1,-1],['Độ lớn trường E','Thành phần xuyên tâm Eᵣ']):
 for lo,hi,f in [(.25,1,lambda x:1/x**2),(1,2,lambda x:0),(2,4,lambda x:sign*2/x**2)]:
  xs=np.linspace(lo,hi,200);ax.plot(xs,[f(x) for x in xs],color=color)
 ax.axhline(0,color='#999',lw=.7);ax.set(xlim=(0,4),ylim=(-1,4.5),title=title,xlabel='r');ax.set_xticks([0,1,2,4],['0','a','b','2b']);ax.grid(alpha=.15)
save(fig,'loi-giai-22-42')
for name,outer in [('loi-giai-22-43',6),('loi-giai-22-44',0)]:
 graph(name,[(0,1,lambda x:0),(1,2,lambda x:0),(2,3,lambda x:2/x**2),(3,4,lambda x:0),(4,8,lambda x:outer/x**2)],[1,2,3,4],['a','b','c','d'],'Hai vỏ cầu dẫn đồng tâm',xmax=8)

fig,ax=plt.subplots(figsize=(6.5,3.6));u=np.linspace(0,3,700);E=np.where(u<=1,4*u-3*u*u,1/np.maximum(u,.00001)**2)
ax.plot(u,E,color=color,lw=2);ax.plot([2/3],[4/3],'o',color=color);ax.annotate('Cực đại tại r = 2R/3',(2/3,4/3),xytext=(1,1.15),arrowprops={'arrowstyle':'->','color':'#777'})
ax.set(xlabel='r/R',ylabel='E / (kQ/R²)',title='Mật độ cầu giảm tuyến tính');ax.grid(alpha=.15);save(fig,'loi-giai-22-47')
fig,ax=plt.subplots(figsize=(6.5,3.6));u=np.linspace(0,2,500);E=np.where(u<=1,u*(1-u),0)
ax.plot(u,E,color=color,lw=2);ax.set(xlabel='r/R',ylabel='3ε₀E / (ρ₀R)',title='Phân bố cầu có điện tích tổng bằng không');ax.grid(alpha=.15);save(fig,'loi-giai-22-52')

rr=np.array([.01,.015,.02,.025,.03,.035,.04]);A=np.array([2.72,1.79,1.34,1.07,.902,.770,.677])*1e5;B=np.array([5.45,2.42,1.34,.861,.605,.443,.335])*1e5
fig,axes=plt.subplots(2,2,figsize=(8,6))
for row,(data,label) in enumerate([(A,'A'),(B,'B')]):
 for col,power in enumerate([1,2]):
  ax=axes[row,col];ax.plot(rr*100,data*rr**power,'o-',color=color);ax.set(title=f'Bộ {label}: '+('Er' if power==1 else 'Er²'),xlabel='r (cm)',ylabel='Er (N m/C)' if power==1 else 'Er² (N m²/C)');ax.grid(alpha=.2)
save(fig,'loi-giai-22-55')
fig,ax=plt.subplots(figsize=(6.5,3.6));u=np.linspace(0,4,500);ratio=np.exp(-2*u)*(1+2*u+2*u*u)
ax.plot(u,ratio,color=color,lw=2);ax.set(xlim=(0,4),ylim=(0,1.03),xlabel='r/a₀',ylabel='E / Eₚ',title='Điện trường trong mô hình hydrogen');ax.grid(alpha=.2);save(fig,'loi-giai-hydrogen')
print('Generated 12 scientific solution SVG plots.')
