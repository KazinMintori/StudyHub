from pathlib import Path
import json,os
import numpy as np
root=Path(__file__).resolve().parents[1]
qa=root/'qa/physics/chapter25';qa.mkdir(parents=True,exist_ok=True)
os.environ.setdefault('MPLCONFIGDIR',str(root/'qa/physics/mpl-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
out=root/'docs/vat-ly-2/bai-giang/img/young-25';out.mkdir(parents=True,exist_ok=True)
I=np.array([.5,1.,2.,4.]);VA=np.array([2.55,3.11,3.77,4.58]);VB=np.array([1.94,3.88,7.76,15.52])
coef=np.polyfit(I,VA,2)
x=np.linspace(.5,4.,300)
f=np.polyval(coef,x)
roots=np.roots(coef-np.array([0,0,4.]))
I4=float(next(r for r in roots if .5<r<4))
assert np.isclose(4*I4,9.3596,rtol=1e-5)
assert np.allclose(VB/I,3.88)
def chart(name,yA,yB,curveA,curveB,ylabel):
    fig,ax=plt.subplots(figsize=(6.0,4.1),layout='constrained')
    ax.plot(x,curveA,color='#6348a8',linestyle='--',label='A: Đường gần đúng')
    ax.plot(x,curveB,color='#176b55',linestyle='-',label='B: Quan hệ tuyến tính')
    ax.scatter(I,yA,color='#6348a8',marker='o',s=42,label='Dữ liệu A',zorder=3)
    ax.scatter(I,yB,color='#176b55',marker='s',s=40,label='Dữ liệu B',zorder=3)
    ax.set(xlabel='Dòng điện I (A)',ylabel=ylabel,xlim=(.35,4.15))
    ax.grid(alpha=.25);ax.legend(fontsize=9.5,loc='best')
    if name=='hinh-giai25-73-dien-ap':
        ax.axhline(4,color='#676767',linewidth=.8,linestyle=':')
        ax.plot([I4,I4],[0,4],color='#676767',linewidth=.8,linestyle=':')
        ax.annotate('I ≈ 2,34 A khi V = 4,00 V',xy=(I4,4),xytext=(1.1,7.0),
                    arrowprops={'arrowstyle':'->','color':'#676767'},fontsize=9.5)
    fig.savefig(out/(name+'.svg'))
    svg_path=out/(name+'.svg')
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
    fig.savefig(qa/(name+'.png'),dpi=140)
    plt.close(fig)
chart('hinh-giai25-73-dien-ap',VA,VB,f,3.88*x,'Hiệu điện thế V (V)')
chart('hinh-giai25-73-dien-tro',VA/I,VB/I,f/x,np.ones_like(x)*3.88,'Điện trở R (Ω)')
(qa/'exercise73-plot-checks.json').write_text(json.dumps({'status':'passed','dataI':I.tolist(),'dataVA':VA.tolist(),
 'dataVB':VB.tolist(),'quadraticCoefficients':coef.tolist(),'interpolatedCurrentAt4V':I4,'powerAat4V':4*I4,
 'powerBat4V':16/3.88,'scope':'Local smooth quadratic fit on the measured range, not a physical law outside it'},indent=2)+'\n',encoding='utf8')
print('Created both required graphs for25.73; checked local fit and power values.')
