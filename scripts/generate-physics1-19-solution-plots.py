"""Reproducible solution diagrams. Original PDF figures are separate assets."""
from pathlib import Path
import json,math,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image,ImageOps,ImageDraw

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-19'
QA=ROOT/'qa/physics1-priority/ch19-solution-plots'
OUT.mkdir(exist_ok=True);QA.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':12,'axes.labelsize':13,'figure.facecolor':'white','savefig.facecolor':'white','svg.fonttype':'path'})
blue='#0068a1';orange='#b54b0f';ledger={};previews=[]
def canvas(xlabel=r'$V/V_1$',ylabel=r'$p/p_1$'):
 fig,ax=plt.subplots(figsize=(5.5,3.7),layout='constrained')
 ax.set_xlabel(xlabel);ax.set_ylabel(ylabel);ax.grid(alpha=.2)
 ax.spines[['top','right']].set_visible(False)
 return fig,ax
def path(ax,x,y,color=blue,label=None):
 ax.plot(x,y,color=color,lw=2,label=label)
 k=max(0,len(x)//2-1);j=min(len(x)-1,k+max(1,len(x)//10))
 ax.annotate('',xy=(x[j],y[j]),xytext=(x[k],y[k]),arrowprops={'arrowstyle':'->','color':color,'lw':2})
def save(n,fig,caption):
 filename=f'parent-solution-19-{n:02}.svg'
 fig.savefig(OUT/filename);fig.savefig(QA/f'19-{n:02}.png',dpi=110);plt.close(fig)
 previews.append(QA/f'19-{n:02}.png')
 raw=ROOT/'raw_materials/physics/translations/chapter-19'/('11-bai-tap-001-033.md' if n<=33 else '12-bai-tap-034-066.md')
 text=raw.read_text(encoding='utf-8')
 match=re.search(rf'^### 19\.{n}\n.*?(?=^### |\Z)',text,re.M|re.S);assert match,n
 block=match.group(0);assert '**Lời giải chi tiết:**' in block,n
 image=f'![{caption}](./img/young-19/{filename})'
 if filename not in block:block=block.replace('**Lời giải chi tiết:**','**Lời giải chi tiết:**\n\n'+image,1)
 raw.write_text(text[:match.start()]+block+text[match.end():],encoding='utf-8')

# 19.1: Initial absolute pressure is unspecified, so use normalized axes.
ratio=380.15/300.15
fig,ax=canvas();x=np.linspace(1,ratio,60);path(ax,x,np.ones_like(x))
ax.scatter([1,ratio],[1,1],color=blue);ax.text(1,1.025,'1');ax.text(ratio,1.025,'2')
ax.set_ylim(.85,1.15)
ledger['19.1']={'V2_over_V1':ratio,'constantNormalizedPressure':1}
save(1,fig,'Giản đồ lời giải 19.1: Gia nhiệt đẳng áp làm thể tích tăng, với các trục được chuẩn hóa theo trạng thái đầu.')

# 19.17: Numerical state volumes follow the supplied ideal-gas model.
R=8.314462618;pressure=101325
v1=.25*R*300.15/pressure;v2=.25*R*400.15/pressure
assert v2>v1 and math.isclose(pressure*(v2-v1),.25*R*100,rel_tol=1e-12)
fig,ax=canvas(r'$V$ (L)',r'$p$ (atm)');x=np.linspace(v1*1000,v2*1000,60);path(ax,x,np.ones_like(x))
ax.scatter([v1*1000,v2*1000],[1,1],color=blue);ax.set_ylim(.85,1.15)
ledger['19.17']={'V1_m3':v1,'V2_m3':v2,'work_J':pressure*(v2-v1)}
save(17,fig,'Giản đồ lời giải 19.17: CO₂ giãn đẳng áp ở 1 atm khi nhiệt độ tăng từ 27°C lên 127°C.')

# 19.18: Both paths start at the same normalized state.
ratio=340.15/300.15
fig,ax=canvas();t=np.linspace(0,1,60)
path(ax,np.ones_like(t),1+t*(ratio-1),label='Đẳng tích')
path(ax,1+t*(ratio-1),np.ones_like(t),orange,'Đẳng áp')
ax.scatter([1],[1],color='black');ax.legend();ax.set_xlim(.95,ratio+.05);ax.set_ylim(.95,ratio+.05)
ledger['19.18']={'temperatureRatio':ratio,'isochoricPressureRatio':ratio,'isobaricVolumeRatio':ratio}
save(18,fig,'Giản đồ lời giải 19.18: Từ cùng trạng thái đầu, đường đẳng tích đi lên còn đường đẳng áp đi sang phải.')

# 19.19: This is deliberately qualitative; no inconsistent numerical EOS state is imposed.
fig,ax=canvas(r'$V$',r'$p$');t=np.linspace(0,1,60)
path(ax,np.ones_like(t),1+.4*t,label='Giữ thể tích')
path(ax,1+.4*t,np.ones_like(t),orange,'Giữ áp suất')
ax.set_xticks([]);ax.set_yticks([]);ax.text(.97,.94,'Đầu');ax.legend(loc='upper right')
ax.set_xlim(.8,1.8);ax.set_ylim(.8,1.8)
ledger['19.19']={'kind':'qualitative paths only; no numerical pressure-volume-temperature state inferred'}
save(19,fig,'Giản đồ lời giải 19.19: Hai cách truyền nhiệt được biểu diễn định tính bằng đường đẳng tích và đường đẳng áp.')

# 19.29: Adiabatic expansion of ideal monatomic argon.
gamma=5/3;ratio=(339.15/283.15)**(1/(gamma-1))
x=np.linspace(1,ratio,100);y=x**(-gamma)
assert np.allclose(y*x**gamma,1)
assert math.isclose(y[-1]*x[-1],283.15/339.15,rel_tol=1e-12)
fig,ax=canvas();path(ax,x,y);ax.scatter([x[0],x[-1]],[y[0],y[-1]],color=blue)
ax.text(x[0],y[0]+.02,'1');ax.text(x[-1],y[-1]+.02,'2')
ledger['19.29']={'gamma':gamma,'V2_over_V1':ratio,'p2_over_p1':float(y[-1])}
save(29,fig,'Giản đồ lời giải 19.29: Argon giãn đoạn nhiệt nên thể tích tăng, trong khi áp suất và nhiệt độ giảm.')

# 19.52: Symbolic gamma is represented by one explicitly identified example curve.
gamma=1.4;fig,ax=canvas(r'$V/V_0$',r'$p/p_0$')
x=np.linspace(1,2,60);path(ax,x,np.ones_like(x),label='Đẳng áp')
x=np.linspace(2,4,100);y=(2/x)**gamma;path(ax,x,y,orange,r'Đoạn nhiệt, $\gamma=1.4$')
assert math.isclose(y[-1],2**(-gamma),rel_tol=1e-12)
ax.scatter([1,2,4],[1,1,float(y[-1])],color='black');ax.legend()
ledger['19.52']={'illustrativeGamma':gamma,'finalVolumeOverInitial':4,'finalPressureOverInitial':float(y[-1]),'generalFinalPressureRatio':'2**(-gamma)'}
save(52,fig,'Giản đồ lời giải 19.52: Giãn đẳng áp đến 2V₀ rồi giãn đoạn nhiệt đến 4V₀. Đường cong minh họa dùng γ = 1,4.')

# 19.60: Actual source table, converted to SI before taking logarithms.
volumes=np.array([2.50,2.02,1.48,1.01,.50])*1e-3
pressures=np.array([.101,.139,.202,.361,.952])*101325
logv=np.log10(volumes);logp=np.log10(pressures)
slope,intercept=np.polyfit(logv,logp,1)
residuals=logp-(slope*logv+intercept)
assert abs(float(residuals.sum()))<1e-10
assert abs(float(residuals@logv))<1e-10
assert 1.35<-slope<1.45
fig,ax=canvas(r'$\log_{10}[V/(1\,\mathrm{m^3})]$',r'$\log_{10}[p/(1\,\mathrm{Pa})]$')
ax.scatter(logv,logp,color=blue,label='Dữ liệu')
line=np.linspace(logv.min(),logv.max(),100);ax.plot(line,slope*line+intercept,color=orange,label='Đường hồi quy');ax.legend()
temperatures=295.15*pressures*volumes/(pressures[0]*volumes[0])
ledger['19.60']={'volumes_m3':volumes.tolist(),'pressures_Pa':pressures.tolist(),'slope':float(slope),'intercept':float(intercept),'gamma':float(-slope),'temperatures_K':temperatures.tolist()}
save(60,fig,'Đồ thị lời giải 19.60: Năm cặp số liệu sau khi đổi sang SI nằm gần đường thẳng trên hệ trục logarit.')

# 19.62: Follow the same parcel, so volume ratios also describe specific volume ratios.
gamma=1.4;pr=1.45e5/1.01e5;vr=pr**(-1/gamma);vc=1/pr
assert vc<vr<1 and math.isclose(pr*vc,1,rel_tol=1e-12)
fig,ax=canvas();x=np.linspace(1,vr,100);path(ax,x,x**(-gamma),label='Nén đoạn nhiệt')
x=np.linspace(vr,vc,60);path(ax,x,np.ones_like(x)*pr,orange,'Làm mát đẳng áp')
ax.scatter([1,vr,vc],[1,pr,pr],color='black')
for label,x0,y0 in [('1',1,1),('2',vr,pr),('3',vc,pr)]:ax.annotate(label,(x0,y0),xytext=(3,7),textcoords='offset points')
ax.legend(loc='lower left');ax.set_ylim(.9,1.55)
ledger['19.62']={'pressureRatio':pr,'postTurboVolumeRatio':vr,'postIntercoolerVolumeRatio':vc,'postTurboTemperature_K':288.15*pr**((gamma-1)/gamma)}
save(62,fig,'Giản đồ lời giải 19.62: Cùng một lượng khí được nén đoạn nhiệt từ 1 đến 2 rồi làm mát đẳng áp từ 2 đến 3.')

tiles=[]
for p in previews:
 image=Image.open(p).convert('RGB');thumb=ImageOps.contain(image,(440,320))
 tile=Image.new('RGB',(460,350),'white');tile.paste(thumb,((460-thumb.width)//2,20));ImageDraw.Draw(tile).text((8,3),p.stem,fill='black');tiles.append(tile)
sheet=Image.new('RGB',(1380,1050),'#eeeeee')
for i,tile in enumerate(tiles):sheet.paste(tile,((i%3)*460,(i//3)*350))
sheet.save(QA/'contact.jpg')
(QA/'numeric-ledger.json').write_text(json.dumps({'status':'passed','cases':ledger},ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Generated {len(ledger)} verified solution diagrams and retained their numerical assumptions.')
