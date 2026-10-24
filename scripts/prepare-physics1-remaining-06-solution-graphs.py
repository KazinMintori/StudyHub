"""Plot the eight original measurements and requested quadratic fit in6.91."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-06'

def main():
 d=np.array([0,.05,.10,.15,.25,.30,.35,.40])
 v=np.array([0,.85,1.11,1.24,1.26,1.14,.90,.36])
 A,B,C=np.polyfit(d,v*v,2)
 peak=-B/(2*A);vmax=np.sqrt(A*peak**2+B*peak+C)
 assert len(d)==8 and .20 not in d
 assert abs(peak-.2040285806847)<1e-10
 assert abs(vmax-1.2902632864267)<1e-10
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'none','svg.hashsalt':'studyhub-ch06','axes.spines.top':False,'axes.spines.right':False})
 fig,(ax,legend)=plt.subplots(2,1,figsize=(6.8,6.9),layout='constrained',gridspec_kw={'height_ratios':[3.5,1.5]})
 xx=np.linspace(0,.4,401)
 ax.plot(xx,A*xx*xx+B*xx+C,color='#235cc4',label='Đường khớp bậc hai')
 ax.scatter(d,v*v,color='#235cc4',label='Tám điểm đo',zorder=3)
 ax.scatter([peak],[vmax*vmax],color='#b83042',zorder=4)
 ax.axvline(peak,color='#b83042',linestyle=':',alpha=.65)
 ax.annotate('Cực đại tại d ≈ 0,204 m',(peak,vmax*vmax),xytext=(-160,-27),textcoords='offset points',fontsize=14)
 legend.axis('off')
 legend.text(.02,.95,'v² = Ad² + Bd + C\nA ≈ −39,9603 s⁻²\nB ≈ 16,3061 m/s²\nC ≈ 0,0013251 m²/s²',transform=legend.transAxes,fontsize=14,va='top')
 ax.set_xlabel('Quãng đường d (m)');ax.set_ylabel('Bình phương tốc độ v² (m²/s²)')
 ax.set_xlim(-.01,.41);ax.set_ylim(-.03,1.9);ax.grid(alpha=.18);ax.legend(fontsize=14,loc='upper right')
 OUT.mkdir(parents=True,exist_ok=True)
 path=OUT/'solution-p6-91-fit.svg'
 fig.savefig(path,facecolor='white',metadata={'Date':None,'Creator':'StudyHub, deterministic quadratic fit'})
 plt.close(fig)
 path.write_bytes(('\n'.join(line.rstrip()for line in path.read_text(encoding='utf-8').splitlines())+'\n').encode('utf-8'))
 print(json.dumps({'status':'passed','originalRows':8,'fit':[float(A),float(B),float(C)],'maximumDistance_m':float(peak),'maximumSpeed_m_s':float(vmax)},indent=2))

if __name__=='__main__':main()
