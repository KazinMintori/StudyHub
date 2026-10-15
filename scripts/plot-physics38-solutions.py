from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1];out=root/'docs/vat-ly-2/bai-giang/img/young-38';out.mkdir(parents=True,exist_ok=True)
qa=root/'qa/physics/chapter38/plot-review';qa.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'none'})
datasets=[
 ('35',1/np.array([100,120,140,160,180,200]),np.array([7.53,5.59,3.98,2.92,2.06,1.43]),r'$X=1/\lambda\ (\mathrm{nm}^{-1})$',r'$V_0\ (\mathrm{V})$',(0,.0106),(-5.5,9),'Sáu điểm đo'),
 ('37',1-np.cos(np.array([30.6,58.7,90.2,119.2,151.3])*np.pi/180),np.array([5.52,6.40,7.60,8.84,9.69]),r'$X=1-\cos\phi$',r'$\lambda\prime\ (\mathrm{pm})$',(0,2),(4.8,10.4),'Năm điểm đo'),
]
for n,x,y,xlabel,ylabel,xlim,ylim,label in datasets:
 slope,offset=np.polyfit(x,y,1);xx=np.linspace(*xlim,200);fig,ax=plt.subplots(figsize=(7.4,4.7));ax.plot(xx,slope*xx+offset,color='#5743a1',label='Đường thẳng hồi quy');ax.scatter(x,y,color='#177b8c',s=45,zorder=3,label=label);ax.set(xlim=xlim,ylim=ylim,xlabel=xlabel,ylabel=ylabel);ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.2);ax.axhline(0,color='#697888',lw=.7);ax.legend(fontsize=11);fig.tight_layout();p=out/f'loi-giai-38-{n}.svg';fig.savefig(p,facecolor='white');fig.savefig(qa/f'loi-giai-38-{n}.png',facecolor='white',dpi=130);plt.close(fig)
 p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 310" role="img" aria-labelledby="title desc">
<title id="title">Động lượng trong tán xạ Compton ngược</title><desc id="desc">Photon tới đi sang phải. Sau va chạm photon đi sang trái, electron đi sang phải. Động lượng electron bằng tổng độ lớn động lượng hai photon.</desc>
<defs><marker id="photon-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#157c94"/></marker><marker id="electron-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#bd5c18"/></marker></defs>
<rect width="720" height="310" rx="12" fill="white"/>
<g font-family="DejaVu Sans, sans-serif" fill="#24364b" font-size="20">
<text x="30" y="34">Trước va chạm</text><text x="30" y="175">Sau va chạm</text>
<line x1="60" y1="84" x2="270" y2="84" stroke="#157c94" stroke-width="4" marker-end="url(#photon-arrow)"/><text x="95" y="65">Photon tới: p</text>
<circle cx="410" cy="84" r="17" fill="#e8f2f4" stroke="#697888" stroke-width="2"/><text x="440" y="91">Electron đứng yên</text>
<line x1="270" y1="229" x2="80" y2="229" stroke="#157c94" stroke-width="4" marker-end="url(#photon-arrow)"/><text x="75" y="208">Photon cuối: −p′</text>
<circle cx="410" cy="229" r="17" fill="#fff0dd" stroke="#bd5c18" stroke-width="2"/><line x1="432" y1="229" x2="655" y2="229" stroke="#bd5c18" stroke-width="4" marker-end="url(#electron-arrow)"/><text x="450" y="208">Electron: pₑ = p + p′</text>
<text x="30" y="291" font-size="16">Sơ đồ chỉ hướng động lượng, không vẽ theo tỉ lệ độ lớn.</text></g></svg>'''
(out/'loi-giai-38-cau-noi.svg').write_text(svg+'\n',encoding='utf-8')
print('Generated two complete-data regression graphs and a recoil momentum diagram.')
