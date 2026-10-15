"""Verified numerical graphs required by the exercise solutions."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1];q=root/'qa/physics/chapter36';out=root/'docs/vat-ly-2/bai-giang/img/young-36';out.mkdir(parents=True,exist_ok=True)
d=json.loads((q/'exercises-45-71-data-checks.json').read_text(encoding='utf-8-sig'))['results']
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','font.size':12})
def save(fig,name):
 fig.tight_layout();path=out/(name+'.svg');fig.savefig(path,bbox_inches='tight');fig.savefig(q/(name+'.png'),dpi=120,bbox_inches='tight');plt.close(fig)
 text=path.read_text(encoding='utf-8');path.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n',encoding='utf-8')
fig,axs=plt.subplots(2,1,figsize=(6,7.5))
for m,ax,zero in zip([1,2],axs,d['51']['positiveMaximaGamma']):
 x=np.linspace(m*math.pi+.001,(m+.5)*math.pi-.05,900);y=np.tan(x)-x
 ax.plot(x,y,color='#2563eb',label=r'$\tan\gamma-\gamma$');ax.axhline(0,color='#64748b',lw=1);ax.scatter([zero],[0],color='#dc2626',zorder=3)
 ax.annotate(r'$\gamma\approx'+f'{zero:.6f}'+'$',xy=(zero,0),xytext=(m*math.pi+.12,8),arrowprops=dict(arrowstyle='->',color='#dc2626'),fontsize=12)
 ax.set_ylim(-10,15);ax.set_xlabel(r'$\gamma$ (rad)');ax.set_ylabel('Giá trị hàm');ax.grid(alpha=.2);ax.set_title('Nghiệm dương thứ '+str(m));ax.legend(loc='upper left')
save(fig,'loi-giai-36-51')
fig,ax=plt.subplots(figsize=(6.4,4.4));a=np.array(d['62']['slitWidthsUm']);products=np.array(d['62']['productsMicrometerMeters'])
assert len(a)==len(products)==9
ax.scatter(a,products,color='#2563eb',s=45,zorder=3,label='Chín cặp số đo');ax.plot(a,products,color='#93c5fd',lw=1);ax.axhline(1.56,color='#dc2626',ls='--',label='Giới hạn góc nhỏ: 1,56')
ax.set_xlabel(r'Bề rộng khe $a$ ($\mu\mathrm{m}$)');ax.set_ylabel(r'Tích $aw$ ($10^{-6}\,\mathrm{m^2}$)');ax.set_title('Bài 36.62: Tích bề rộng khe và bề rộng vân');ax.grid(alpha=.2);ax.legend();save(fig,'loi-giai-36-62')
print('Prepared root-isolation graph and full nine-point data graph.')
