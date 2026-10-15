"""Supplementary plots: Every source datapoint and the three-slit intensity."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1];q=root/'qa/physics/chapter35'
data=json.loads((q/'exercises-32-60-data-checks.json').read_text())['results']
out=root/'docs/vat-ly-2/bai-giang/img/young-35';out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(7.5,4),layout='constrained')
x=np.array(data['50']['allEightSourcePoints']['inverseSlitSpacingPerMm'])
y=np.array(data['50']['allEightSourcePoints']['fringeSpacingMm']);assert len(x)==8
a,b=np.polyfit(x,y,1);xx=np.linspace(0,11,200)
ax.scatter(x,y,label='Tám điểm đo',color='#0f766e')
ax.plot(xx,a*xx+b,label='Đường khớp tuyến tính',color='#7c3aed')
ax.set(xlim=(0,11),ylim=(0,6.1),xlabel='1/d (mm⁻¹)',ylabel='Khoảng vân Δy (mm)',title='Bài35.50: Khoảng vân theo nghịch đảo khoảng khe')
ax.grid(alpha=.2);ax.legend()
fig.savefig(out/'loi-giai-35-50.svg');fig.savefig(q/'plot-35-50.png',dpi=125);plt.close(fig)
u=np.linspace(-2,2,2001);I=(1+2*np.cos(2*np.pi*u))**2/9
assert abs(I[1000]-1)<1e-12
fig,ax=plt.subplots(figsize=(7.5,4),layout='constrained')
ax.plot(u,I,color='#7c3aed')
ax.axhline(1/9,color='#be123c',ls='--',label='Cực đại phụ: I/I₀ =1/9')
ax.scatter([-1/3,1/3],[0,0],color='#0f766e',label='Hai vân tối gần tâm')
ax.set(xlabel='Độ lệch pha /2π',ylabel='Cường độ I/I₀',title='Bài35.54: Giao thoa ba khe')
ax.grid(alpha=.2);ax.legend(fontsize=10)
fig.savefig(out/'loi-giai-35-54.svg');fig.savefig(q/'plot-35-54.png',dpi=125);plt.close(fig)
for p in out.glob('loi-giai-35-*.svg'):
 s=p.read_text(encoding='utf-8');p.write_text('\n'.join(x.rstrip() for x in s.splitlines()).rstrip()+'\n',encoding='utf-8')
print('Saved two supplementary SVGs, using all eight data markers and exact three-phasor intensity.')
