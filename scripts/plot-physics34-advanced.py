"""Additional solution diagrams and full-data plot; all coordinates from verified results."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1]
q=root/'qa/physics/chapter34';out=root/'docs/vat-ly-2/bai-giang/img/young-34'
r=json.loads((q/'exercises-66-111-data-checks.json').read_text())['results']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
def save(fig,n):
 fig.savefig(out/f'loi-giai-34-{n}.svg')
 fig.savefig(q/f'loi-giai-34-{n}.png',dpi=125)
 plt.close(fig)
def arrow(ax,x,y,color,label):
 ax.annotate('',(x,y),(x,0),arrowprops={'arrowstyle':'->','color':color,'lw':2})
 ax.text(x,y+(0.12 if y>=0 else -.2),label,ha='center',color=color)
#72: independently check both ray intersections.
f,s=18.,10.;sp=1/(1/f-1/s);m=-sp/s
assert abs(sp-r['72']['imageDistanceCm'])<1e-10
fig,ax=plt.subplots(figsize=(8,4),layout='constrained')
ax.axhline(0,color='#64748b',lw=.8);ax.axvline(0,color='#6d28d9',lw=2)
arrow(ax,-s,1,'#0f766e','Vật');arrow(ax,sp,m,'#be123c','Ảnh ảo')
for y0,k,c in [(1,-1/f,'#7c3aed'),(0,-1/s,'#0891b2')]:
 ax.plot([-s,0],[1,y0],color=c);ax.plot([0,22],[y0,y0+k*22],color=c)
 ax.plot([0,sp],[y0,m],color=c,ls='--')
 assert abs(y0+k*sp-m)<1e-12
# exact ray from(-10,1) toward lens with front-focus(-18,0)
lens_y=f/(f-s)
assert abs(lens_y-m)<1e-12
ax.plot([-18,-10],[0,1],color='#65a30d',ls=':')
ax.plot([-10,0],[1,lens_y],color='#65a30d')
ax.plot([0,22],[lens_y,lens_y],color='#65a30d')
ax.scatter([-f,f],[0,0],s=15,color='#6d28d9')
ax.text(-f,-.25,'F₁',ha='center');ax.text(f,-.25,'F₂',ha='center')
ax.set(xlim=(-27,24),ylim=(-2,3),xlabel='Tọa độ ngang (cm)',ylabel='Độ cao / chiều cao vật',title='Bài 34.72: Ba tia chính và ảnh ảo')
ax.grid(alpha=.15);save(fig,'72')
#73: pinhole geometry, no thinlens assumptions.
fig,ax=plt.subplots(figsize=(8,3.7),layout='constrained')
ax.axhline(0,color='#64748b',lw=.8)
for oy in [9.,-9.]:
 iy=-oy*20/150
 ax.plot([-150,0,20],[oy,0,iy],color='#7c3aed' if oy>0 else '#0891b2')
ax.plot([0,0],[-12,-.3],color='#334155',lw=3);ax.plot([0,0],[.3,12],color='#334155',lw=3)
ax.plot([20,20],[-12,12],color='#be123c',lw=3)
ax.plot([0,20],[12,12],color='#334155');ax.plot([0,20],[-12,-12],color='#334155')
ax.plot([-150,-150],[-9,9],color='#0f766e',lw=3)
ax.plot([20,20],[-1.2,1.2],color='#f59e0b',lw=6)
ax.text(-150,10,'Vật cao 18cm',ha='center');ax.text(0,13,'Lỗ kim',ha='center')
ax.text(20,-14,'Phim\nẢnh cao 2,4cm',ha='center')
ax.set(xlim=(-190,50),ylim=(-18,17),xlabel='Khoảng cách dọc trục (cm)',ylabel='Độ cao (cm)',title='Bài 34.73: Tia truyền thẳng qua lỗ kim')
save(fig,'73')
#78: alignedfrontfocalplane, tiltedplane mirror; piecewise rays satisfy lens equations.
fig,ax=plt.subplots(figsize=(8,3.8),layout='constrained')
f=22.;xm=60.;tilt=.012
ax.axhline(0,color='#64748b',lw=.8);ax.axvline(f,color='#6d28d9',lw=2)
# sketchmirror slope: x=xm+tilt*y. Reflection creates common small returningbeam angle.
ax.plot([xm-tilt*4,xm+tilt*4],[-4,4],color='#334155',lw=3)
source_y=1.2
# initial rays parallel after lens at slope-source_y/f. exact linearpropagation common reflectedslope.
k=-source_y/f
for yl,c in [(0.,'#7c3aed'),(2.,'#0891b2')]:
 ym=yl+k*(xm-f)
 k_return=-k-2*tilt
 # using physical x coordinate (dxnegative aftermirror).
 yback=ym+k_return*(f-xm)
 k_after=k_return+yback/f
 yscreen=yback+k_after*(0-f)
 ax.plot([0,f,xm],[source_y,yl,ym],color=c)
 ax.plot([xm,f,0],[ym,yback,yscreen],color=c,ls='--')
 expected=-source_y+2*f*tilt
 assert abs(yscreen-expected)<1e-12
arrow(ax,0,source_y,'#0f766e','Vật')
ax.scatter([0],[expected],color='#be123c',s=30)
ax.text(0,expected-.6,'Ảnh trên màn',ha='left',color='#be123c')
ax.text(f,3.5,'Thấu kính',ha='center');ax.text(xm,4.4,'Gương hơi nghiêng',ha='right')
ax.text(11,-3.6,'22,0cm',ha='center');ax.text(41,-3.6,'38,0cm',ha='center')
ax.text(3,3.9,'Nét liền: Lượt đi\nNét đứt: Lượt về',fontsize=10)
ax.set(xlim=(-5,65),ylim=(-4.5,5),xlabel='Tọa độ dọc trục (cm)',ylabel='Độ cao sơ đồ',title='Bài 34.78: Tự chuẩn trực, vật và màn ở cùng mặt tiêu')
save(fig,'78')
#89: two sourcepaths, realimages atsamex withoppositeheights.
fig,axes=plt.subplots(2,1,figsize=(8,6.5),layout='constrained')
sp=r['89']['directImageDistanceFromLensCm']
for i,ax in enumerate(axes):
 yobj=1. if i==0 else -1.
 m=-sp/85.;yi=m*yobj
 ax.axhline(0,color='#64748b',lw=.8);ax.axvline(0,color='#6d28d9',lw=2)
 arrow(ax,-85,yobj,'#0f766e','Nến' if i==0 else 'Ảnh qua gương')
 arrow(ax,sp,yi,'#be123c','Ảnh cuối')
 for h,k,c in [(yobj,-yobj/32,'#7c3aed'),(0,-yobj/85,'#0891b2')]:
  ax.plot([-85,0],[yobj,h],color=c)
  ax.plot([0,65],[h,h+k*65],color=c)
  assert abs(h+k*sp-yi)<1e-12
  if i==1:
   ym=yobj+(-105+85)*(h-yobj)/85
   ax.plot([-85,-105,0],[1,ym,h],color=c)
 if i==1:
  ax.axvline(-105,color='#334155',lw=2);ax.text(-105,1.45,'Gương',ha='center')
  arrow(ax,-85,1,'#9a3412','Nến')
 ax.scatter([32],[0],color='#6d28d9',s=15);ax.text(32,.15,'F₂',ha='center')
 ax.set(xlim=(-115,70),ylim=(-1.8,1.8),xlabel='Tọa độ dọc trục (cm)',ylabel='Độ cao / chiều cao nến')
 ax.set_title('Chùm trực tiếp' if i==0 else 'Chùm qua gương rồi qua kính')
save(fig,'89')
#103: allsixmeasuredpairs, trueOLS.
s=np.array([22.5,25,30,35,40,45]);sp=np.array([271.6,148.3,89.4,71.1,60.8,53.2])
x=1/s;y=1/sp;a,b=np.polyfit(x,y,1)
assert abs(-1/a-1.500106594)<1e-8
fig,ax=plt.subplots(figsize=(7,4),layout='constrained')
xx=np.linspace(.02,.047,100);ax.plot(xx,a*xx+b,label='Đường khớp tuyến tính',color='#7c3aed')
ax.scatter(x,y,color='#0f766e',label='Sáu cặp đo')
ax.set(xlabel='1/s (cm⁻¹)',ylabel='1/s′ (cm⁻¹)',title='Bài 34.103: Xác định chiết suất và bán kính')
ax.grid(alpha=.2);ax.legend();save(fig,'103')
#105: validbranchu>1 only.
u=np.linspace(1.08,7,500);v=u+u/(u-1)
assert np.all(v>=4)
fig,ax=plt.subplots(figsize=(7,4),layout='constrained')
ax.plot(u,v,color='#7c3aed');ax.axvline(1,color='#64748b',ls='--')
ax.scatter([2],[4],color='#be123c');ax.annotate('Cực tiểu (2,4)',(2,4),xytext=(3,5.8),arrowprops={'arrowstyle':'->'})
ax.set(xlim=(.8,7),ylim=(3,12),xlabel='Khoảng vật / tiêu cự: s/f',ylabel='Khoảng vật–ảnh / tiêu cự: D/f',title='Bài 34.105: Hai khoảng thật và khoảng nhỏ nhất')
ax.grid(alpha=.2);save(fig,'105')
#106: pointwisethinlensmapping, assertcollinearity.
delta=8/np.sqrt(2);xo=np.array([-45-delta,-45+delta,-45]);yo=np.array([15-delta,15+delta,15])
ss=-xo;xx=20*ss/(ss-20);yy=-xx/ss*yo
assert np.max(abs(yy-(60-2*xx)))<1e-10
assert abs(np.hypot(xx[1]-xx[0],yy[1]-yy[0])-r['106']['imageLengthCm'])<1e-8
fig,ax=plt.subplots(figsize=(8,4),layout='constrained')
ax.axhline(0,color='#64748b',lw=.8);ax.axvline(0,color='#6d28d9',lw=2)
ax.plot(xo[:2],yo[:2],color='#0f766e',lw=3,label='Bút chì')
ax.plot(xx[:2],yy[:2],color='#be123c',lw=3,label='Ảnh thật')
for j,name in enumerate(['A','B','C']):
 ax.scatter([xo[j]],[yo[j]],color='#0f766e');ax.text(xo[j]-2,yo[j]+1,name,ha='center')
 ax.scatter([xx[j]],[yy[j]],color='#be123c');ax.text(xx[j]+2,yy[j]+.8,name+'′',ha='center')
ax.plot([xo[0],0,xx[0]],[yo[0],0,yy[0]],color='#0891b2',lw=.8)
ax.plot([xo[1],0,xx[1]],[yo[1],0,yy[1]],color='#7c3aed',lw=.8)
ax.set(xlim=(-60,52),ylim=(-26,25),xlabel='Tọa độ dọc trục (cm)',ylabel='Độ cao (cm)',title='Bài 34.106: Tạo ảnh từng điểm của vật nghiêng')
ax.grid(alpha=.15);ax.legend();save(fig,'106')
print('Saved seven supplementary solution diagrams; ray intersections, six-point fit and object endpoints verified.')

# Normalize insignificant trailingXMLpathwhitespace for cleanGitdiffs.
for svg_path in out.glob('loi-giai-34-*.svg'):
    svg_text=svg_path.read_text(encoding='utf-8')
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_text.splitlines()).rstrip()+'\n',encoding='utf-8')
