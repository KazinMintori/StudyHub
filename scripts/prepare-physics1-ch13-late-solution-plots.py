from pathlib import Path
import math,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Arc
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'qa/physics1-remaining/ch13/solution-previews';OUT.mkdir(parents=True,exist_ok=True)
ASSETS=ROOT/'docs/vat-ly-1/bai-giang/img/young-13';ASSETS.mkdir(exist_ok=True)
records=[]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'none','svg.hashsalt':'studyhub13late','axes.spines.top':False,'axes.spines.right':False})
def save(fig,name,description):
 path=ASSETS/(name+'.svg');fig.savefig(path,facecolor='white',metadata={'Date':None,'Creator':'StudyHub solution diagram'})
 path.write_bytes(('\n'.join(line.rstrip()for line in path.read_text(encoding='utf-8').splitlines())+'\n').encode('utf-8'))
 fig.savefig(OUT/(name+'.png'),dpi=135,facecolor='white');plt.close(fig)
 records.append({'key':name,'kind':'new-required-solution-diagram','file':'proposed-assets/'+name+'.svg','preview':'proposed-assets/'+name+'.png','sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'description':description,'minimumNominalTextSize':14,'englishLabels':[],'visualFrameReview':'pending'})

#13.49 exact tangent geometry, using the source constants and24hperiod.
G=6.67e-11;ME=5.97e24;RE=6.37e6
r=(G*ME*86400**2/(4*math.pi**2))**(1/3);q=r/RE;phi=math.acos(1/q)
P=np.array([1/q,math.sqrt(1-1/q**2)]);S=np.array([q,0.]);O=np.array([0.,0.])
assert abs(np.dot(P,S-P))<1e-12
fig,ax=plt.subplots(figsize=(6.3,3.5),layout='constrained');ax.set_aspect('equal');ax.axis('off')
ax.add_patch(Circle((0,0),1,facecolor='#dcebf8',edgecolor='#235cc4',lw=1.8))
ax.plot([0,q],[0,0],color='#616976',ls='--',lw=1.1)
ax.plot([0,P[0]],[0,P[1]],color='#235cc4',lw=1.6)
ax.plot([P[0],S[0]],[P[1],S[1]],color='#c34753',lw=2)
ax.add_patch(Arc((0,0),.9,.9,theta1=0,theta2=math.degrees(phi),color='#8a5520'))
ax.scatter([0,P[0],q],[0,P[1],0],color=['#235cc4','#c34753','#c34753'],s=30)
ax.text(-.26,-.34,'O',fontsize=14);ax.text(P[0]-.15,P[1]+.15,'P',fontsize=14);ax.text(q+.12,-.08,'S',fontsize=14)
ax.text(.60,.45,'φ ≈ 81,3°',fontsize=14,color='#80501f')
ax.text(-.65,-1.48,'Trái Đất',fontsize=14);ax.text(4.9,-.62,'Vệ tinh',fontsize=14)
ax.text(2.8,.75,'Tia giới hạn SP',fontsize=14,ha='center')
ax.text(2.9,-1.45,'Góc tại P: 90°',fontsize=14,ha='center')
ax.set(xlim=(-1.2,q+.5),ylim=(-1.7,1.6))
save(fig,'solution-p13-49-visibility','Exact tangent triangle OPS; satellite radius6.625RE, latitude81.32degrees. No source artwork replaced.')

names=['Thủy','Kim','Trái Đất','Hỏa','Mộc','Thổ','Thiên Vương','Hải Vương']
a=np.array([57.9,108.2,149.6,227.9,778.3,1426.7,2870.7,4498.4])*1e9
T=np.array([88.,224.7,365.2,687.,4331.,10747.,30589.,59800.])*86400
fig,ax=plt.subplots(figsize=(5.5,4.7),layout='constrained')
ax.scatter(a**3/1e38,T**2/1e19,s=44,color='#235cc4',zorder=3)
coef=np.dot(a**3,T**2)/np.dot(a**3,a**3);line=np.linspace(0,max(a**3),100)
ax.plot(line/1e38,coef*line/1e19,color='#a3503d',lw=1.4)
ax.set(xlabel='a³ (10³⁸ m³)',ylabel='T² (10¹⁹ s²)',xlim=(0,None),ylim=(0,None));ax.grid(alpha=.18)
ax.annotate('Bốn hành tinh trong\ngần gốc',(0,0),xytext=(.27,.43),textcoords='axes fraction',fontsize=14,arrowprops={'arrowstyle':'->'})
ax.text(.03,.95,'Tám điểm dữ liệu',transform=ax.transAxes,va='top',fontsize=14)
save(fig,'solution-p13-76-linear','All eight original a,T values; axes use explicit powers to preserve the requested linear plot.')

X=np.log10(a);Y=np.log10(T);slope,intercept=np.polyfit(X,Y,1);fixed=np.mean(Y-1.5*X)
fig,ax=plt.subplots(figsize=(6.1,5.0),layout='constrained')
line=np.linspace(X.min()-.12,X.max()+.12,100)
ax.plot(line,slope*line+intercept,label='Khớp tự do',lw=1.7,color='#235cc4')
ax.plot(line,1.5*line+fixed,'--',label='Hệ số góc 1,5',lw=1.5,color='#c25142')
ax.scatter(X,Y,s=40,color='#235cc4',zorder=3)
offsets=[(-2,-27),(-38,12),(0,-27),(0,15),(-24,15),(8,-15),(-70,14),(-93,-27)]
for x,y,name,offset in zip(X,Y,names,offsets):ax.annotate(name,(x,y),xytext=offset,textcoords='offset points',fontsize=14,arrowprops={'arrowstyle':'-','color':'#747b86','lw':.6})
ax.set(xlabel='log₁₀(a / m)',ylabel='log₁₀(T / s)',xlim=(X.min()-.18,X.max()+.13),ylim=(Y.min()-.32,Y.max()+.34));ax.grid(alpha=.18);ax.legend(loc='upper left',fontsize=14)
save(fig,'solution-p13-76-log','Original eight points, independent least squares free fit and Kepler slope1.5 fixed fit. Labels are Vietnamese planet abbreviations.')

D=np.array([4879,12104,12756,6792,142984,120536,51118,49528])*1000
g=np.array([3.7,8.9,9.8,3.7,23.1,9.,8.7,11.])
fig,ax=plt.subplots(figsize=(6.2,5.0),layout='constrained')
line=np.linspace(0,1.5e8,150)
for rho,style,color in [(1000,'--','#a95b2e'),(3000,':','#447b52'),(5500,'-.','#8c5ab8')]:
 ax.plot(line/1e6,2*math.pi*G*rho*line/3,style,color=color,lw=1.2,label=f'ρ = {rho} kg/m³')
ax.scatter(D/1e6,g,color='#235cc4',s=45,zorder=4)
offsets=[(3,-18),(-30,10),(5,25),(10,-36),(-24,14),(-18,-27),(-52,-29),(-25,11)]
for x,y,name,offset in zip(D/1e6,g,names,offsets):ax.annotate(name,(x,y),xytext=offset,textcoords='offset points',fontsize=14,arrowprops={'arrowstyle':'-','color':'#747b86','lw':.6})
ax.set(xlabel='Đường kính D (10⁶ m)',ylabel='Gia tốc g (m/s²)',xlim=(-6,156),ylim=(0,27));ax.grid(alpha=.18);ax.legend(loc='upper left',fontsize=14)
save(fig,'solution-p13-77-density','Original D,g table; different slopes indicate different average densities. Reference lines are truncated by the plotted y-range.')

print('Saved four source-parameter solution plots.')
