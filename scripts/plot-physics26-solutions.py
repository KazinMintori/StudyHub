from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-26'
qa=root/'qa/physics/chapter26'
out.mkdir(parents=True,exist_ok=True)
qa.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
R=0.895e6; C=12.4e-6; emf=60.0; tau=R*C
t=np.linspace(0,20,401); points=np.array([0,5,10,20,100])
q=lambda z:C*emf*(-np.expm1(-z/tau))*1e6
i=lambda z:emf/R*np.exp(-z/tau)*1e6
assert np.isclose(tau,11.098)
assert np.isclose(q(20),621.3,atol=.1)
assert np.isclose(i(100),.00819,atol=.00001)
for name,fn,ylabel in [('hinh-giai26-42-dien-tich',q,'Điện tích q (µC)'),('hinh-giai26-42-dong-dien',i,'Dòng điện i (µA)')]:
    fig,ax=plt.subplots(figsize=(6,4),layout='constrained')
    ax.plot(t,fn(t),color='#2b5d95',linewidth=2,label='Quá trình nạp tụ')
    ax.scatter(points[:4],fn(points[:4]),color='#a85024',zorder=3,label='Thời điểm trong đề')
    ax.set(xlabel='Thời gian t (s)',ylabel=ylabel,xlim=(0,20),ylim=(0,750 if fn is q else 70))
    ax.grid(alpha=.25);ax.legend(fontsize=9)
    path=out/(name+'.svg');fig.savefig(path)
    path.write_text('\n'.join(line.rstrip() for line in path.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
    fig.savefig(qa/(name+'.png'),dpi=140);plt.close(fig)
svg_head='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 160" role="img"><style>text{font:14px sans-serif;fill:#172f49}path,line,circle,rect{stroke:#172f49;stroke-width:2;fill:white}</style>'
ammeter=svg_head+'''<title>Điện trở rẽ song song cuộn điện kế</title>
<path d="M15 80H65V40H130M170 40H235V80H285M65 80V120H120M180 120H235V80" fill="none"/>
<circle cx="150" cy="40" r="20"/><text x="145" y="45">G</text>
<rect x="120" y="108" width="60" height="24"/><text x="136" y="151">R_sh</text>
<text x="12" y="102">a</text><text x="277" y="102">b</text>
<text x="82" y="17">Cuộn điện kế R_G</text></svg>'''
voltmeter=svg_head+'''<title>Điện trở phụ nối tiếp cuộn điện kế</title>
<path d="M15 80H70M130 80H185M225 80H285" fill="none"/>
<rect x="70" y="68" width="60" height="24"/><circle cx="205" cy="80" r="20"/>
<text x="200" y="85">G</text><text x="90" y="116">R_s</text>
<text x="12" y="103">a</text><text x="277" y="103">b</text>
<text x="142" y="40">Cuộn điện kế R_G</text></svg>'''
for name,svg in [('hinh-giai26-33-ampe-ke',ammeter),('hinh-giai26-33-von-ke',voltmeter)]:
    (out/(name+'.svg')).write_text(svg+'\n',encoding='utf8')
(qa/'solution-plots-checks.json').write_text(json.dumps({'status':'passed','tauSeconds':tau,'timeSeconds':points.tolist(),'chargeMicroCoulombs':q(points).tolist(),'currentMicroAmperes':i(points).tolist()},indent=2)+'\n',encoding='utf8')
print('Created two verified charging plots and two meter circuit illustrations.')

# Exercise26.79 explicitly requests q(i), including slope and intercept.
i_data=np.array([56.0,48.0,40.0,32.0,24.0])
q_data=np.array([10.1,19.8,30.2,40.0,49.9])
slope,intercept=np.polyfit(i_data,q_data,1)
assert np.isclose(slope,-1.2475)
assert np.isclose(intercept,79.9)
fig,ax=plt.subplots(figsize=(6,4),layout='constrained')
xx=np.linspace(0,65,300)
ax.plot(xx,slope*xx+intercept,color='#2b5d95',label='Đường thẳng khớp toàn bộ số liệu')
ax.scatter(i_data,q_data,color='#a85024',label='Số liệu đo',zorder=3)
ax.set(xlabel='Dòng điện i (mA)',ylabel='Điện tích q (µC)',xlim=(0,65),ylim=(0,85))
ax.grid(alpha=.25);ax.legend(fontsize=9)
path=out/'hinh-giai26-79-dien-tich-dong-dien.svg';fig.savefig(path)
path.write_text('\n'.join(line.rstrip() for line in path.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
fig.savefig(qa/'hinh-giai26-79-dien-tich-dong-dien.png',dpi=140);plt.close(fig)
(qa/'exercise79-plot-checks.json').write_text(json.dumps({'status':'passed','currentMilliAmperes':i_data.tolist(),'chargeMicroCoulombs':q_data.tolist(),'slopeMicroCoulombsPerMilliAmpere':slope,'interceptMicroCoulombs':intercept},indent=2)+'\n',encoding='utf8')
print('Created and verified required q(i) plot for26.79.')
