"""Solution-only plots: Original data and force/motion models for16.70/73/75."""
from pathlib import Path
import math
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-16';OUT.mkdir(exist_ok=True)
def start(w,h):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img"><rect width="100%" height="100%" fill="white"/><g font-family="Segoe UI,Arial,sans-serif" fill="#17212b" font-size="20">'
def line(x1,y1,x2,y2,color='#344054',width=1.5):return f'<path d="M{x1:.4f} {y1:.4f}L{x2:.4f} {y2:.4f}" stroke="{color}" stroke-width="{width}" fill="none"/>'
def text(x,y,value,anchor='middle',size=20,color='#17212b'):return f'<text x="{x:.4f}" y="{y:.4f}" text-anchor="{anchor}" font-size="{size}" fill="{color}">{value}</text>'
def save(name,s):
 (OUT/name).write_bytes((s+'</g></svg>\n').encode('utf-8'))
def plot(name,xs,ys,xmin,xmax,ymin,ymax,xticks,yticks,xlabel,ylabel,connect=True,fit=None):
 left,right,top,bottom=65,340,52,265
 X=lambda x:left+(x-xmin)/(xmax-xmin)*(right-left)
 Y=lambda y:bottom-(y-ymin)/(ymax-ymin)*(bottom-top)
 s=start(360,335)+text(12,25,ylabel,'start')
 for x,label in xticks:s+=line(X(x),top,X(x),bottom,'#e4e7ec',1)+text(X(x),292,label)
 for y,label in yticks:s+=line(left,Y(y),right,Y(y),'#e4e7ec',1)+text(left-10,Y(y)+6,label,'end')
 s+=line(left,bottom,right+5,bottom)+line(left,top-5,left,bottom)+text(right,326,xlabel,'end')
 if fit is not None:s+=line(X(xmin),Y(fit(xmin)),X(xmax),Y(fit(xmax)),'#2458a6',2)
 if connect:s+='<polyline fill="none" stroke="#2458a6" stroke-width="2.8" points="'+' '.join(f'{X(x):.4f},{Y(y):.4f}'for x,y in zip(xs,ys))+'"/>'
 else:
  for x,y in zip(xs,ys):s+=f'<circle cx="{X(x):.4f}" cy="{Y(y):.4f}" r="4.5" fill="#007c78"/>'
 save(name,s)
temps=np.array([-20.,0,20,40,60,80]);speeds=np.array([324.,337,349,361,372,383]);ys=speeds**2
slope,intercept=np.linalg.lstsq(np.column_stack([temps,np.ones(6)]),ys,rcond=None)[0]
plot('solution-s16-70-fit.svg',temps,ys/1000,-25,85,100,152,[(x,str(int(x)))for x in temps],[(x,str(x))for x in [100,110,120,130,140,150]],'T (°C)','v² (10³ m²/s²)',False,lambda x:(slope*x+intercept)/1000)
# Pole and loads: All real forces are located at their actual application points.
s=start(360,430)
s+=line(50,340,50,40,'#a8b2c0',6)+line(50,340,280,110,'#b5712c',6)
s+=line(280,110,280,180)+line(267,180,293,180,'#344054',7)+text(304,190,'Ống','start')
s+=line(50,250,140,250,'#98a2b3',2)
def arrow(x,y,dx,dy,color):
 length=math.hypot(dx,dy);ux,uy=dx/length,dy/length;ex,ey=x+dx,y+dy
 return line(x,y,ex,ey,color,3)+f'<polygon points="{ex},{ey} {ex-11*ux-5*uy},{ey-11*uy+5*ux} {ex-11*ux+5*uy},{ey-11*uy-5*ux}" fill="{color}"/>'
s+=arrow(140,250,-72,0,'#2458a6')+text(92,233,'F')
s+=arrow(165,225,0,75,'#b42318')+text(182,290,'mₚg','start')
s+=arrow(280,110,0,68,'#b42318')+text(298,132,'mₜg','start')
s+=arrow(50,340,72,0,'#007c78')+text(104,365,'Rₓ')
s+=arrow(50,340,0,-75,'#007c78')+text(30,294,'Rᵧ')
s+=line(15,340,15,250,'#65778d',1)+line(8,340,23,340)+line(8,250,23,250)+text(12,240,'h')
s+=text(76,315,'45°','start')+text(50,390,'Trục quay','start')
save('solution-s16-73-forces.svg',s)
speed=344.;rho=1.2;B=rho*speed**2;lam=.2;T=lam/speed
def pressure(x):
 q=x%lam
 return 40-800*q if q<=.1 else-120+800*q
def disp(x):
 q=x%lam
 return(-40*q+400*q*q)/B if q<=.1 else(-400*q*q+120*q-8)/B
times=np.linspace(0,2*T,801);positions=np.linspace(0,.4,801)
tt=[(i*T*1000/2,label)for i,label in enumerate(['0','T/2','T','3T/2','2T'])]
plot('solution-s16-75-pressure-time.svg',times*1000,[pressure(-speed*t)for t in times],0,2*T*1000,-45,45,tt,[(-40,'−40'),(0,'0'),(40,'40')],'t, T = 0,5814 ms','p (Pa)')
plot('solution-s16-75-displacement-space.svg',positions,[disp(x)*1e6 for x in positions],0,.4,-8,8,[(x,str(x).replace('.',','))for x in [0,.1,.2,.3,.4]],[(-7.0421,'−7,04'),(0,'0'),(7.0421,'7,04')],'x (m)','y (µm)')
plot('solution-s16-75-displacement-time.svg',times*1000,[disp(-speed*t)*1e6 for t in times],0,2*T*1000,-8,8,tt,[(-7.0421,'−7,04'),(0,'0'),(7.0421,'7,04')],'t, T = 0,5814 ms','y (µm)')
print('Generated five compact solution diagrams; original source image content unchanged.')
