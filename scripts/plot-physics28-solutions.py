"""Reproducible drawings requested in Chapter28 exercises58 and73."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-28';out.mkdir(parents=True,exist_ok=True)
qa=root/'qa/physics/chapter28';qa.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
def save(fig,stem):
    p=out/(stem+'.svg');fig.savefig(p)
    p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
    fig.savefig(qa/(stem+'.png'),dpi=140);plt.close(fig)

# 58: Fields at P=(a,0); upper wire out, lower wire into the plane.
fig,ax=plt.subplots(figsize=(6,4),layout='constrained')
ax.axhline(0,color='#888888',linewidth=.8);ax.axvline(0,color='#888888',linewidth=.8)
ax.scatter([0,0],[1,-1],s=180,facecolors='white',edgecolors='#754591',linewidths=2,zorder=3)
ax.plot(0,1,'o',color='#754591',markersize=4,zorder=4)
ax.plot(0,-1,'x',color='#754591',markersize=8,zorder=4)
ax.text(-.92,1.10,'Dòng đi ra');ax.text(-.98,-1.37,'Dòng đi vào')
ax.text(.12,1.05,'y = a');ax.text(.12,-1.10,'y = −a')
ax.scatter([1],[0],s=25,color='#172f49',zorder=4);ax.text(.92,-.27,'P')
for dx,dy,color,label in [(1,1,'#a85024','Trường dây trên'),(1,-1,'#53753c','Trường dây dưới'),(2,0,'#2b5d95','Trường tổng')]:
    ax.annotate('',xy=(1+.65*dx,.65*dy),xytext=(1,0),arrowprops={'arrowstyle':'->','lw':2,'color':color})
    ax.text(1+.65*dx,.65*dy+(.08 if dy>=0 else -.18),label,color=color,ha='center',fontsize=9)
ax.set(xlim=(-1.15,3.25),ylim=(-1.6,1.6),aspect='equal',xlabel='Tọa độ x/a',ylabel='Tọa độ y/a')
ax.set_xticks([0,1,2,3]);ax.set_yticks([-1,0,1])
save(fig,'hinh-giai28-58-vecto-truong')
for x in [-3,-1,0,1,3]:
    top=np.array([1.,x]);bottom=np.array([1.,-x])
    assert np.allclose(top+bottom,[2,0])

u=np.linspace(-4,4,401);normalized=1/(1+u*u)
fig,ax=plt.subplots(figsize=(6,4),layout='constrained')
ax.plot(u,normalized,color='#2b5d95',lw=2)
ax.scatter([-2,-1,0,1,2],[.2,.5,1,.5,.2],color='#a85024',zorder=3)
ax.set(xlabel='Tọa độ x/a',ylabel='Tỉ số B(x)/B(0)',xlim=(-4,4),ylim=(0,1.08))
ax.grid(alpha=.25)
save(fig,'hinh-giai28-58-do-thi')
assert np.argmax(normalized)==200 and np.isclose(normalized[200],1)

# 73: x is distance from the surface, B in tesla, use all five points.
x=np.array([2,4,6,8,10.])*1e-2;B=np.array([.406,.250,.181,.141,.116])*1e-3
slope,intercept=np.polyfit(1/B,x,1)
mu0=4*math.pi*1e-7;current=2*math.pi*slope/mu0;radius=-intercept
assert np.isclose(current,64.90254) and np.isclose(radius,.0119141023)
fig,ax=plt.subplots(figsize=(6,4),layout='constrained')
xx=np.linspace(0,9000,201)
ax.scatter((1/B)/1000,x*100,color='#a85024',label='Năm cặp số liệu',zorder=3)
ax.plot(xx/1000,(slope*xx+intercept)*100,color='#2b5d95',label='Đường thẳng phù hợp với số đo')
ax.axhline(0,color='#888888',linewidth=.8)
ax.set(xlabel='Nghịch đảo từ trường 1/B (10³ T⁻¹)',ylabel='Khoảng cách từ mặt cáp x (cm)',xlim=(0,9),ylim=(-1.7,11.5))
ax.grid(alpha=.25);ax.legend(fontsize=8.5)
save(fig,'hinh-giai28-73-do-thi')
core='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 220" role="img">
<title>Ống dây có lõi thép: Trường dòng ngoài, từ hóa và trường tổng cùng hướng</title>
<defs><marker id="arrow28" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7z" fill="context-stroke"/></marker></defs>
<style>text{font:15px sans-serif;fill:#172f49}.vector{fill:none;stroke-width:2.5;marker-end:url(#arrow28)}</style>
<rect x="37" y="55" width="268" height="114" rx="18" fill="#e7ece2" stroke="#53753c" stroke-width="1.5"/>
<g fill="none" stroke="#754591" stroke-width="1.5">
<ellipse cx="51" cy="112" rx="9" ry="75"/><ellipse cx="77" cy="112" rx="9" ry="75"/><ellipse cx="103" cy="112" rx="9" ry="75"/><ellipse cx="129" cy="112" rx="9" ry="75"/><ellipse cx="155" cy="112" rx="9" ry="75"/><ellipse cx="181" cy="112" rx="9" ry="75"/><ellipse cx="207" cy="112" rx="9" ry="75"/><ellipse cx="233" cy="112" rx="9" ry="75"/><ellipse cx="259" cy="112" rx="9" ry="75"/><ellipse cx="285" cy="112" rx="9" ry="75"/>
</g>
<rect x="89" y="59" width="167" height="105" fill="#e7ece2"/>
<path class="vector" d="M107 79H232" stroke="#2b5d95"/><text x="80" y="84">B₀</text>
<path class="vector" d="M107 111H232" stroke="#53753c"/><text x="80" y="116">M</text>
<path class="vector" d="M107 143H232" stroke="#a85024"/><text x="80" y="148">B</text>
<text x="120" y="23">Ống dây có lõi thép</text>
<text x="38" y="211">Các mũi tên chỉ biểu diễn chiều vector.</text>
</svg>'''
(out/'hinh-giai28-47-loi-thep.svg').write_text(core+'\n',encoding='utf8')
(qa/'solution-drawings.json').write_text(json.dumps({'status':'passed','drawings':4,'problem47':'Positive susceptibility makes M, B0 and B parallel in the stated linear-core model. Arrows show direction only.','problem58':'Individual vector fields add along +x; normalized B is1/(1+(x/a)^2).','problem73':{'current_A':current,'radius_m':radius,'slope_T_m':slope,'intercept_m':intercept}},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Generated and checked four required solution drawings.')
