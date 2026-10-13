"""Reproducible Vietnamese solution diagrams and full-data regression plots."""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-29'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False})
def save(fig,name):
 fig.tight_layout();fig.savefig(OUT/f'{name}.svg',facecolor='white');plt.close(fig)
 target=OUT/f'{name}.svg'
 target.write_text('\n'.join(line.rstrip() for line in target.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 fig,ax=plt.subplots(figsize=(7.2,3.8))
 ax.plot([-.35,0,0,1,1,3,3,4,4,4.35],[0,0,-.225,-.225,0,0,.225,.225,0,0],color='#654393',lw=2.5)
 ax.axhline(0,color='#888',lw=.8);ax.set_xticks([0,1,3,4],['0','t₁','t₂','t₃']);ax.set_yticks([-.225,0,.225]);ax.set_xlabel('t');ax.set_ylabel('I (A)');ax.set_title('Dòng ngược kim đồng hồ là dương');ax.grid(alpha=.2)
 save(fig,'hinh-giai29-33')
 B,L,R,m,emf=2.4,.36,5.,.90,12.
 terminal=emf/(B*L);tau=m*R/(B*B*L*L)
 t=np.linspace(0,5*tau,400)
 fig,ax=plt.subplots(figsize=(7.2,3.8));ax.plot(t,terminal*(1-np.exp(-t/tau)),color='#654393',lw=2.5)
 ax.axhline(terminal,color='#777',ls='--',label='Tốc độ giới hạn');ax.set_xlabel('t (s)');ax.set_ylabel('v (m/s)');ax.legend(frameon=False);ax.grid(alpha=.2)
 save(fig,'hinh-giai29-54')
 fig,ax=plt.subplots(figsize=(6.8,4.2));angle=math.radians(36.9);end=.250*np.array([math.cos(angle),math.sin(angle)])
 ax.plot([0,end[0]],[0,end[1]],color='#c59338',lw=8,solid_capstyle='round')
 ax.text(-.015,-.024,'a',fontsize=16);ax.text(end[0]-.01,end[1]+.018,'b: Điện thế cao hơn',fontsize=14)
 ax.annotate('',xy=(.18,.045),xytext=(.06,.045),arrowprops={'arrowstyle':'->','lw':2,'color':'#168755'});ax.text(.11,.018,'v',color='#168755',fontsize=17)
 ax.annotate('',xy=(.25,-.06),xytext=(-.02,-.06),arrowprops={'arrowstyle':'->','color':'#555'});ax.text(.25,-.06,'x')
 ax.annotate('',xy=(-.03,.20),xytext=(-.03,-.07),arrowprops={'arrowstyle':'->','color':'#555'});ax.text(-.045,.20,'y')
 ax.set_xlim(-.08,.32);ax.set_ylim(-.09,.23);ax.set_aspect('equal');ax.axis('off');save(fig,'hinh-giai29-58')
 for num,x,y,ylabel in [
  (65,np.array([20.,16.,14.,12.,10.,8.]),np.array([6.2,4.9,4.3,3.7,3.1,2.5]),'a (cm/s²)'),
  (66,np.array([2.,4.,6.,8.,10.]),np.array([.10,.21,.31,.41,.52]),'F (N)')]:
  slope,intercept=np.polyfit(x,y,1);line=np.linspace(0,1.05*max(x),200)
  fig,ax=plt.subplots(figsize=(7.2,4.1));ax.scatter(x,y,s=52,color='#c59338',label='Số đo',zorder=3);ax.plot(line,slope*line+intercept,color='#654393',lw=2,label='Đường khớp tuyến tính')
  ax.set_xlabel('v (cm/s)');ax.set_ylabel(ylabel);ax.set_xlim(0,max(line));ax.set_ylim(bottom=0);ax.grid(alpha=.2);ax.legend(frameon=False);save(fig,f'hinh-giai29-{num}')
 print('Prepared five solution figures using the stated model and every measured data point.')
if __name__=='__main__':main()
