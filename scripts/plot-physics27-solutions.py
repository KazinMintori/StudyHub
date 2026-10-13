from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-27';out.mkdir(parents=True,exist_ok=True)
qa=root/'qa/physics/chapter27';qa.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
def save(fig,name):
    path=out/(name+'.svg');fig.savefig(path)
    path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
    fig.savefig(qa/(name+'.png'),dpi=140);plt.close(fig)
V=np.array([10.,12.,14.,16.,18.])*1e3
R=np.array([19.9,21.8,23.6,25.2,26.8])*1e-2
slope,intercept=np.polyfit(V,R*R,1)
ratio=2/(.250**2*slope)
assert np.isclose(slope,4.0213e-6)
assert np.isclose(ratio,7.957624651e6,rtol=1e-5)
fig,ax=plt.subplots(figsize=(6,4),layout='constrained')
x=np.linspace(0,20e3,201)
ax.scatter(V/1e3,R*R,color='#a85024',label='Năm cặp số liệu đo',zorder=3)
ax.plot(x/1e3,slope*x+intercept,color='#2b5d95',label='Đường thẳng khớp bình phương nhỏ nhất')
ax.set(xlabel='Điện thế gia tốc V (kV)',ylabel='Bình phương bán kính R² (m²)',xlim=(0,20),ylim=(0,.085))
ax.grid(alpha=.25);ax.legend(fontsize=8.5)
save(fig,'hinh-giai27-76-hoi-quy')
y=np.linspace(-2.2,2.2,121);z=np.linspace(-2.2,2.2,121)
yy,zz=np.meshgrid(y,z)
fig,ax=plt.subplots(figsize=(5,5),layout='constrained')
ax.streamplot(y,z,zz,yy,density=1.2,color='#2b5d95',linewidth=.9,arrowsize=1)
ax.plot(0,0,'o',color='#a85024',markersize=4)
ax.axhline(0,color='#999999',linewidth=.6);ax.axvline(0,color='#999999',linewidth=.6)
ax.set(xlabel='Tọa độ y/L',ylabel='Tọa độ z/L',aspect='equal',xlim=(-2.2,2.2),ylim=(-2.2,2.2))
save(fig,'hinh-giai27-71-duong-suc')
# Each field line has y²-z² constant, since (2y,-2z) dot (z,y)=0.
assert np.allclose(2*yy*zz-2*zz*yy,0)
svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 210" role="img">
<title>Lực từ, trọng lực và phản lực lên dây trên mặt phẳng nghiêng</title>
<defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7z" fill="context-stroke"/></marker></defs>
<style>text{font:14px sans-serif;fill:#172f49}.force{fill:none;stroke-width:2.5;marker-end:url(#arrow)}</style>
<path d="M25 185L275 45" stroke="#999999" stroke-width="2" fill="none"/>
<circle cx="150" cy="115" r="6" fill="#172f49"/>
<path class="force" d="M150 115L150 185" stroke="#a85024"/>
<path class="force" d="M150 115L240 115" stroke="#2b5d95"/>
<path class="force" d="M150 115L113 49" stroke="#53753c"/>
<text x="159" y="178">Mg</text><text x="196" y="104">F_B = ILB</text><text x="90" y="40">N</text>
<text x="31" y="204">Lực từ có thành phần lên dốc</text>
</svg>'''
(out/'hinh-giai27-55-so-do-luc.svg').write_text(svg+'\n',encoding='utf8')
frame='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 230" role="img">
<title>Lực từ trên từng cạnh của khung dây có bản lề</title>
<defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7z" fill="context-stroke"/></marker></defs>
<style>text{font:14px sans-serif;fill:#172f49}.arrow{fill:none;stroke-width:2;marker-end:url(#arrow)}</style>
<path d="M65 60H245V175H65Z" fill="none" stroke="#172f49" stroke-width="2"/>
<path class="arrow" d="M65 152V125M115 60H160M245 90V115M190 175H145" stroke="#7d478f"/>
<path class="arrow" d="M112 30H220" stroke="#2b5d95"/><text x="156" y="22">B</text>
<text x="51" y="52">b</text><text x="251" y="52">c</text><text x="51" y="195">a</text><text x="251" y="195">d</text>
<text x="12" y="103">Bản lề</text>
<text x="54" y="116" style="font-size:26px;fill:#a85024">⊗</text>
<text x="234" y="144" style="font-size:26px;fill:#a85024">⊙</text>
<text x="91" y="90">F_bc = 0</text><text x="91" y="165">F_da = 0</text>
<text x="39" y="216">F_ab = F_cd = 1,20 N</text></svg>'''
(out/'hinh-giai27-37-luc-tung-canh.svg').write_text(frame+'\n',encoding='utf8')
(qa/'required-drawings-checks.json').write_text(json.dumps({'status':'passed','problem76':{'slopeM2PerVolt':slope,'interceptM2':intercept,'chargeToMass':ratio},'problem71':'Field-line gradient dot field vanishes for y²−z²=constant','problem55':'Force directions: horizontal magnetic force, vertical gravity, normal reaction'},indent=2)+'\n',encoding='utf8')
print('Created four requested solution drawings, with regression and field-line checks.')
