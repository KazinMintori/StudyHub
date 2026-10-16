"""Trích xuất hình ảnh cho nhóm bài tập Chapter 40 nhóm D."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.constants import m_e, hbar, e
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'hinh-q40-26': (1373, (505, 570, 616, 662)),
    'hinh-p40-48': (1376, (140, 480, 298, 572)),
    'hinh-p40-58': (1377, (224, 392, 334, 474)),
}
SCALE = 3
OUT = ROOT / 'docs/vat-ly-2/bai-giang/img/young-40'

def prepare_solution_plots():
    """Reproduce added explanatory plots; never modify source figure pixels."""
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'none',
                         'svg.hashsalt':'StudyHub-physics40'})
    preview=ROOT/'qa/physics/chapter40/plot-previews'
    preview.mkdir(parents=True,exist_ok=True)
    def save(fig,name):
        svg=OUT/(name+'.svg')
        fig.savefig(svg,bbox_inches='tight',facecolor='white',metadata={'Date':None})
        svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
        fig.savefig(preview/(name+'.png'),dpi=110,bbox_inches='tight',facecolor='white')
        plt.close(fig)

    x=np.linspace(-4,4,501)
    fig,ax=plt.subplots(figsize=(7,4))
    ax.plot(x,np.exp(-abs(x)),color='#2563eb',lw=2)
    ax.set(xlabel='Tọa độ kx',ylabel='Hàm sóng ψ',title='Hàm liên tục có đỉnh nhọn tại gốc')
    ax.axvline(0,color='#64748b',lw=.8)
    ax.grid(alpha=.2);save(fig,'loi-giai-40-51')

    u=np.linspace(-.92,.92,501)
    fig,ax=plt.subplots(figsize=(8,4.6))
    ax.plot(u,1/(1-u*u),label='Thế năng',color='#2563eb',lw=2)
    ax.plot(u,1+u*u,'--',label='Gần đúng điều hòa',color='#b45309',lw=2)
    ax.set(xlabel='Độ lệch tương đối x/d',ylabel='Thế năng V(x)/V(0)',ylim=(.8,7))
    ax.axvline(-1,color='#64748b',ls=':');ax.axvline(1,color='#64748b',ls=':')
    ax.legend(fontsize=14);ax.grid(alpha=.2);save(fig,'loi-giai-40-53')

    energy=np.array([4.,5.,6.,7.,7.6]);T=np.array([2.4e-6,1.5e-5,1.2e-4,1.3e-3,8.1e-3])
    G=16*(energy/8)*(1-energy/8)
    kappa=np.sqrt(2*m_e*(8-energy)*e)/hbar
    X=kappa/1e10;Y=np.log(T/G)
    slope,intercept=np.polyfit(X,Y,1)
    fig,ax=plt.subplots(figsize=(7,4.5))
    grid=np.linspace(.25,1.1,100)
    ax.plot(grid,slope*grid+intercept,label='Đường thẳng khớp',color='#2563eb',lw=2)
    ax.scatter(X,Y,label='Năm điểm số liệu',color='#b45309',s=48,zorder=3)
    ax.set(xlabel='κ / (10¹⁰ m⁻¹)',ylabel='ln(T/G)')
    ax.legend(fontsize=14);ax.grid(alpha=.2);save(fig,'loi-giai-40-60')

    # Dimensionless example: hbar²/(2mB²)=1, A/B=1/2, U0=60.
    # Eigenvectors solve the finite-difference Schrödinger equation, including
    # both hard-wall nodes. An arbitrary Bezier curve would not do this.
    count=1400;dx=1/(count+1);x=np.arange(1,count+1)*dx
    potential=np.where(x<.5,0.,60.)
    energies,vectors=eigh_tridiagonal(2/dx**2+potential,
                                    -np.ones(count-1)/dx**2,
                                    select='i',select_range=(0,2))
    assert energies[0]<60<energies[2]
    fig,axes=plt.subplots(2,1,figsize=(7,7),sharex=True,layout='constrained')
    xx=np.r_[0,x,1]
    for ax,n in zip(axes,[0,2]):
        wave=vectors[:,n]/np.sqrt(dx)
        if wave[0]<0:wave=-wave
        wave=np.r_[0,wave,0]
        ax.plot(xx,wave,lw=2,color='#2563eb',label='Hàm sóng')
        ax.axhline(0,color='#64748b',lw=.7)
        ax.axvline(.5,color='#64748b',ls=':',lw=1)
        ax.axvline(0,color='#0f172a',lw=2);ax.axvline(1,color='#0f172a',lw=2)
        ax.step([0,.5,1],[0,.35,.35],where='post',color='#b45309',
                ls='--',lw=1.7,label='Bậc thế (thang phụ)')
        relation='<' if energies[n]<60 else '>'
        ax.set(ylabel='Hàm sóng ψ',title=f'E{n+1} {relation} U₀,  E{n+1}/U₀ = {energies[n]/60:.3f}')
        ax.grid(alpha=.15)
    axes[0].legend(fontsize=12,loc='lower left')
    axes[1].set(xlabel='Tọa độ x/B',xticks=[0,.5,1],xticklabels=['0','A/B = 0,5','1'])
    save(fig,'loi-giai-q40-26')

    x=np.linspace(0,1,501)
    a=np.sin(np.pi*x);b=np.sin(2*np.pi*x)
    fig,axes=plt.subplots(2,2,figsize=(9,6.5),sharex=True,sharey=True,layout='constrained')
    for ax,phase,title in zip(axes.flat,[0,np.pi/2,np.pi,3*np.pi/2],
                             ['t = 0','t = T/4','t = T/2','t = 3T/4']):
        density=a*a+b*b+2*a*b*np.cos(phase)
        assert abs(np.trapezoid(density,x)-1)<1e-5
        ax.plot(x,density,lw=2,color='#2563eb')
        ax.fill_between(x,density,alpha=.1,color='#2563eb')
        ax.set(title=title,xlabel='x/L',ylabel='L |Ψ|²',ylim=(0,3.3))
        ax.grid(alpha=.2)
    save(fig,'loi-giai-cau-noi')

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    with fitz.open(ROOT / 'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
        for stem, (page, clip) in CROPS.items():
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=fitz.Rect(clip), alpha=False)
            p = OUT / (stem + '.png')
            pix.save(p)
            with Image.open(p) as im:
                assert im.size == (pix.width, pix.height) and im.convert('RGB').tobytes() == pix.samples
            sha = hashlib.sha256(p.read_bytes()).hexdigest()
            rows.append(dict(stem=stem, pdfPage=page, clip=clip, scale=SCALE, pixelMatch=True, sha256=sha, size=(pix.width, pix.height)))
    print(f'Extracted {len(rows)} figures successfully:')
    for r in rows:
        print(r)
    prepare_solution_plots()
    print('Reproduced five solution plots from numerical functions and source data.')

if __name__ == '__main__':
    main()
