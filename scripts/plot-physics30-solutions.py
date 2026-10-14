"""Draw the requested inductance solution graphs from independently recalculated models."""
from pathlib import Path
import json,subprocess,sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-30'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False})
def save(fig,name):
 fig.tight_layout();target=OUT/f'{name}.svg'
 fig.savefig(target,facecolor='white');plt.close(fig)
 target.write_text('\n'.join(line.rstrip() for line in target.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 subprocess.run([sys.executable,'-X','utf8',str(ROOT/'raw_materials/physics/verify_chapter30_41_75.py')],cwd=ROOT,check=True,capture_output=True)
 results=json.loads((ROOT/'qa/physics/chapter30/problems-41-75-checks.json').read_text(encoding='utf8'))['results']
 fig,ax=plt.subplots(figsize=(7.2,3.5))
 ax.step([0,1,2,3,4,5,6],[1,-1,1,-1,1,-1,1],where='post',color='#654393',lw=2.4)
 ax.axhline(0,color='#777',lw=.8);ax.set_ylim(-1.4,1.4);ax.set_yticks([-1,0,1],['−Lk','0','+Lk'])
 ax.set_xlabel('Thời gian (đơn vị quy ước)');ax.set_ylabel('Điện áp cuộn cảm');ax.grid(alpha=.2)
 save(fig,'hinh-giai-q30-10')
 resistance=np.array([3.,4.,5.,6.,7.,8.,10.,12.]);halves=np.array([.735,.654,.589,.536,.491,.453,.393,.347])
 model=results['59'];grid=np.linspace(0,13,200)
 fig,ax=plt.subplots(figsize=(7.2,4))
 ax.scatter(resistance,1/halves,color='#c59338',s=48,label='Tám số đo',zorder=3)
 ax.plot(grid,model['slope']*grid+model['intercept'],color='#654393',label='Đường khớp tuyến tính')
 ax.set_xlabel('Điện trở ngoài (Ω)');ax.set_ylabel('1/t₁/₂ (s⁻¹)');ax.grid(alpha=.2);ax.legend(frameon=False)
 save(fig,'hinh-giai30-59')
 t=np.linspace(0,.10,400);decay=np.exp(-t/.020)
 fig,(a,b)=plt.subplots(2,1,figsize=(7.2,6),sharex=True)
 a.plot(t*1e3,.18*(1-decay),color='#654393',label='i₀');a.set_ylabel('Dòng điện (A)');a.legend(frameon=False);a.grid(alpha=.2)
 b.plot(t*1e3,9*(1-decay),color='#654393',label='v_ac');b.plot(t*1e3,27+9*decay,color='#c59338',label='v_cb')
 b.set_ylabel('Điện áp (V)');b.set_xlabel('Thời gian (ms)');b.legend(frameon=False);b.grid(alpha=.2)
 save(fig,'hinh-giai30-63')
 t=np.linspace(0,.14,400);currentR=.18*np.exp(-t/(4/150))
 fig,ax=plt.subplots(figsize=(7.2,4))
 ax.plot(t*1e3,np.full_like(t,.72),label='Qua R₀',color='#654393')
 ax.plot(t*1e3,currentR,label='Qua R',color='#c59338')
 ax.plot(t*1e3,.72-currentR,label='Qua S₂',color='#168755')
 ax.set_xlabel('Thời gian (ms)');ax.set_ylabel('Dòng điện (A)');ax.legend(frameon=False);ax.grid(alpha=.2)
 save(fig,'hinh-giai30-64')
 for number in (67,68):
  model=results[str(number)];points=np.array(model['points']);grid=np.linspace(0,4.5 if number==67 else 15,300)
  voltage=20+30*np.exp(-grid*1e-3/.0024) if number==67 else 25*(1-np.exp(-grid*1e-3/.0080))
  fig,ax=plt.subplots(figsize=(7.2,4))
  ax.scatter(points[:,0],points[:,1],s=35,color='#c59338',label='Điểm đọc từ đồ thị',zorder=3)
  ax.plot(grid,voltage,color='#654393',label='Mô hình RL')
  ax.set_xlabel('Thời gian (ms)');ax.set_ylabel('Điện áp (V)');ax.grid(alpha=.2);ax.legend(frameon=False)
  save(fig,f'hinh-giai30-{number}')
 print('Prepared six solution graphs with complete source datasets and circuit models.')
if __name__=='__main__':main()
