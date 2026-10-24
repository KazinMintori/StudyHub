"""Reproduce the four graphs explicitly requested by problems7.77,7.79,7.80.

The original problem figures are separate, unchanged PDF crops. The potential
sketch for7.79 uses approximate ordinates read from those original data points.
"""
from pathlib import Path
import json
import numpy as np
from scipy.interpolate import PchipInterpolator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-07'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none','svg.hashsalt':'studyhub-ch07','axes.spines.top':False,'axes.spines.right':False})
BLUE='#235cc4';RED='#b83042';GRAY='#61697a'

def canvas(xlabel,ylabel):
 fig,ax=plt.subplots(figsize=(6.4,4.3),layout='constrained')
 ax.set_xlabel(xlabel);ax.set_ylabel(ylabel)
 ax.grid(alpha=.18);ax.tick_params(labelsize=11)
 return fig,ax

def save(fig,name):
 OUT.mkdir(parents=True,exist_ok=True)
 fig.savefig(OUT/name,facecolor='white',metadata={'Date':None,'Creator':'StudyHub, deterministic Python graph'})
 svg=OUT/name
 svg.write_bytes(('\n'.join(line.rstrip()for line in svg.read_text(encoding='utf-8').splitlines())+'\n').encode('utf-8'))
 plt.close(fig)

def main():
 h=np.array([.8,2,4,6,8,10,12]);tension=np.array([265,274,298,313,330,348,371])
 slope,intercept=np.polyfit(h,tension,1)
 length=2*265/slope;hmax=(411-intercept)/slope
 assert abs(length-57.0330889)<1e-4
 fig,ax=canvas('Độ cao thả h (m)','Lực căng ở đáy T (N)')
 ax.scatter(h,tension,color=BLUE,label='Các giá trị đo',zorder=3)
 x=np.linspace(0,18,200);ax.plot(x,intercept+slope*x,color=BLUE,label='Đường khớp tuyến tính')
 ax.axhline(411,color=RED,linestyle='--',label='Giới hạn cho phép 411 N')
 ax.plot(hmax,411,'o',color=RED);ax.axvline(hmax,color=RED,linestyle=':',alpha=.6)
 ax.annotate('h ≈ 16,5 m',(hmax,411),xytext=(-83,-27),textcoords='offset points',fontsize=11)
 ax.legend(fontsize=10,loc='upper left');save(fig,'solution-p7-77-fit.svg')

 # Values read from the positive half of FigureP7.79; mirror symmetry is
 # visible in the measured data. Keep the sketch's precision explicit.
 xp=np.arange(0,1.51,.1)
 kp=np.array([.14,.145,.16,.185,.215,.25,.29,.32,.36,.38,.39,.38,.34,.27,.16,0])
 assert len(xp)==len(kp)
 xx=np.r_[-xp[:0:-1],xp];kk=np.r_[kp[:0:-1],kp]
 energy=.14;u=energy-kk
 assert np.isclose(u[np.where(np.isclose(xx,0))[0][0]],0)
 assert np.isclose(u.min(),-.25)
 curve=PchipInterpolator(xx,u);x=np.linspace(-1.5,1.5,601)
 fig,ax=canvas('Tọa độ x (m)','Thế năng U (J)')
 ax.plot(x,curve(x),color=BLUE,label='Thế năng phác từ đồ thị động năng')
 ax.scatter(xx,u,s=12,color=BLUE,zorder=3)
 ax.axhline(energy,color=GRAY,linestyle='--',label='Cơ năng ban đầu ≈ 0,14 J')
 ax.axhline(-.13,color=RED,linestyle='--',label='Cơ năng lần thả mới ≈ −0,13 J')
 ax.axhline(0,color=GRAY,linewidth=.8)
 ax.set_ylim(-.30,.20);ax.legend(fontsize=9,loc='upper center');save(fig,'solution-p7-79-potential.svg')

 xi=np.linspace(.72,8,800);potential=1/xi**2-1/xi
 fig,ax=canvas('Tọa độ không thứ nguyên ξ = x/x₀','Thế năng u = Ux₀²/α')
 ax.plot(xi,potential,color=BLUE)
 ax.axhline(0,color=GRAY,linestyle='--',label='Thả tại x₀: Cơ năng bằng 0')
 ax.axhline(-2/9,color=RED,linestyle='--',label='Thả tại 3x₀: Cơ năng −2/9')
 ax.scatter([1,1.5,2,3],[0,-2/9,-.25,-2/9],color=[GRAY,RED,BLUE,RED],zorder=3)
 ax.set_ylim(-.29,.55);ax.set_xlim(.72,8);ax.legend(fontsize=10,loc='upper right')
 save(fig,'solution-p7-80-potential.svg')

 # v*=sqrt(2α/(m*x0²)), hence v/v*=sqrt(e-u), not sqrt(2(e-u)).
 xi=np.linspace(1,8,800);speed=np.sqrt(1/xi-1/xi**2)
 xb=np.linspace(1.5,3,401);bound_speed=np.sqrt(np.maximum(0,-2/9+1/xb-1/xb**2))
 assert np.isclose(np.sqrt(1/2-1/4),.5)
 assert np.isclose(np.sqrt(-2/9+1/2-1/4),1/6)
 fig,ax=canvas('Tọa độ không thứ nguyên ξ = x/x₀','Tốc độ v/v*')
 ax.plot(xi,speed,color=BLUE,label='Thả từ nghỉ tại x₀')
 ax.plot(xb,bound_speed,color=RED,label='Thả từ nghỉ tại 3x₀')
 ax.scatter([1,2,1.5,3],[0,.5,0,0],color=[BLUE,BLUE,RED,RED],zorder=3)
 ax.set_xlim(.9,8);ax.set_ylim(-.025,.58);ax.legend(fontsize=10,loc='upper right')
 save(fig,'solution-p7-80-speed.svg')
 print(json.dumps({'status':'passed','fit_slope_N_per_m':float(slope),'fit_intercept_N':float(intercept),'L_m':float(length),'max_release_height_m':float(hmax),'graph79_precision':'Approximate readings, not a new measurement','graph80_speed_scale':'sqrt(2alpha/(m*x0^2))','graph80_normalized_maxima':[.5,1/6]},indent=2))

if __name__=='__main__':main()
