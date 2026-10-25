"""Reproducible solution-only diagrams for14.49,14.74,14.90,14.91.
Original source figures are extracted by a different script.
"""
from pathlib import Path
import math
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-14'
OUT.mkdir(exist_ok=True)
def svg_open(w,h):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%"><rect width="100%" height="100%" fill="white"/><defs><marker id="arr" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto-start-reverse"><path d="M0 0L7 3.5L0 7" fill="context-stroke"/></marker></defs><g font-family="Segoe UI, sans-serif" font-size="20" fill="#17212b">'
def line(x1,y1,x2,y2,col='#344054',arrow=False,width=2):
 s=f'<path d="M{x1:.3f} {y1:.3f}L{x2:.3f} {y2:.3f}" fill="none" stroke="{col}" stroke-width="{width}"/>'
 if arrow:
  dx,dy=x2-x1,y2-y1;length=math.hypot(dx,dy)
  if length:
   ux,uy=dx/length,dy/length;bx,by=x2-8*ux,y2-8*uy
   s+=f'<polygon points="{x2:.3f},{y2:.3f} {bx-3.3*uy:.3f},{by+3.3*ux:.3f} {bx+3.3*uy:.3f},{by-3.3*ux:.3f}" fill="{col}"/>'
 return s
def txt(x,y,s,col='#17212b',anchor='start'):
 return f'<text x="{x:.3f}" y="{y:.3f}" fill="{col}" text-anchor="{anchor}">{s}</text>'
def save(name,s): (OUT/name).write_text(s+'</g></svg>',encoding='utf-8')

s=svg_open(360,650)+txt(90,22,'Lực',anchor='middle')+txt(265,22,'Gia tốc',anchor='middle')
th=.7
for i,a in enumerate([th,th/2,0]):
    top=40+i*200
    s+=txt(8,top+12,['(a) α = θ','(b) α = θ/2','(c) α = 0'][i])
    ca,sa=math.cos(a),math.sin(a)
    vr=2*(ca-math.cos(th));tension=ca+vr
    for px in [60,240]:
        py=top+32; bx=px+80*sa;by=py+80*ca
        s+=line(px,py,bx,by,'#98a2b3',width=3)
        s+=f'<circle cx="{px}" cy="{py}" r="3" fill="#344054"/><circle cx="{bx}" cy="{by}" r="5" fill="#c46c2c"/>'
        if px==60:
            s+=line(bx,by,bx,by+43,'#b42318',True)+txt(bx+7,by+43,'mg','#b42318')
            tx=bx-43*tension*sa;ty=by-43*tension*ca
            s+=line(bx,by,tx,ty,'#2458a6',True)+txt(tx-8,ty-5,'S','#2458a6')
        else:
            # a/g = -sin(alpha)e_t - 2(cos alpha-cos theta)e_r
            ax=-sa*ca-vr*sa;ay=sa*sa-vr*ca
            ex=bx+55*ax;ey=by+55*ay
            s+=line(bx,by,ex,ey,'#007c78',True)+txt(ex+6,ey-6,'a','#007c78')

save('solution-14-49-forces.svg',s)

# Potential energy: both axes have 50 SVG units per 0.05 SI unit,
# preserving the requested equal centimetre intervals in the two coordinate directions.
s=svg_open(360,300);ox,oy,scale=180,240,400
for j in range(-6,7):
 x=ox+j*20;s+=line(x,oy,x,60,'#e4e7ec',width=1)
for j in range(10):
 y=oy-j*20;s+=line(60,y,300,y,'#e4e7ec',width=1)
for x in[-.3,-.15,0,.15,.3]:
 s+=txt(ox+scale*x,268,f'{x:.2g}'.replace('.',','),anchor='middle')
for u in[0,.15,.3,.45]:
 s+=txt(52,oy-scale*u+6,f'{u:.2g}'.replace('.',','),anchor='end')
s+=line(50,oy,326,oy,arrow=True)+line(ox,oy,ox,35,arrow=True)
s+=txt(325,293,'x (m)',anchor='end')+txt(194,25,'U (J)')
pts=[(ox+scale*x,oy-scale*5*x*x)for x in np.linspace(-.3,.3,241)]
s+='<polyline fill="none" stroke="#2458a6" stroke-width="3" points="'+' '.join(f'{x:.3f},{y:.3f}'for x,y in pts)+'"/>'
s+=line(60,oy-80,300,oy-80,'#b42318')+txt(65,oy-95,'E = 0,200 J','#b42318')
save('solution-14-74-potential.svg',s)

def chart(name,xs,ys,xmin,xmax,ymin,ymax,xlabel,ylabel,fit=None,ref=None,xticks=None,yticks=None,connect=False):
 w,h=360,320;left,top,right,bottom=70,45,340,250
 X=lambda v:left+(v-xmin)/(xmax-xmin)*(right-left)
 Y=lambda v:bottom-(v-ymin)/(ymax-ymin)*(bottom-top)
 s=svg_open(w,h)
 for z in (xticks if xticks is not None else np.linspace(xmin,xmax,6)):
  s+=line(X(z),top,X(z),bottom,'#e4e7ec',width=1)+txt(X(z),bottom+26,f'{z:.2g}'.replace('.',','),anchor='middle')
 for z in (yticks if yticks is not None else np.linspace(ymin,ymax,6)):
  s+=line(left,Y(z),right,Y(z),'#e4e7ec',width=1)+txt(left-8,Y(z)+6,f'{z:.3g}'.replace('.',','),anchor='end')
 s+=line(left,bottom,right+10,bottom,arrow=True)+line(left,bottom,left,top-10,arrow=True)
 s+=txt(right,308,xlabel,anchor='end')+txt(12,25,ylabel)
 if fit:
  a,b=fit;s+=line(X(xmin),Y(a*xmin+b),X(xmax),Y(a*xmax+b),'#2458a6')
 if ref is not None:s+=line(left,Y(ref),right,Y(ref),'#b42318')
 if connect:
  points=sorted(zip(xs,ys))
  s+='<polyline fill="none" stroke="#007c78" stroke-width="1.5" points="'+' '.join(f'{X(x):.3f},{Y(y):.3f}' for x,y in points)+'"/>'
 for x,y in zip(xs,ys):s+=f'<circle cx="{X(x):.3f}" cy="{Y(y):.3f}" r="4.5" fill="#007c78"/>'
 save(name,s)
m=np.array([.1,.2,.3,.4,.5]);T=np.array([8.7,10.5,12.2,13.9,15.1])/10
chart('solution-14-90-regression.svg',m,T*T,0,.55,0,2.6,'m (kg)','T² (s²)',tuple(np.polyfit(m,T*T,1)),xticks=[0,.1,.2,.3,.4,.5],yticks=[0,.5,1,1.5,2,2.5])
L=np.array([12,10,8,6,5,4,3,2.5,2.3]);T=np.array([6.96,6.36,5.70,4.95,4.54,4.08,3.60,3.35,3.27])
chart('solution-14-91-five.svg',L[:5],T[:5]**2,0,13,0,55,'L (m)','T² (s²)',tuple(np.polyfit(L[:5],T[:5]**2,1)),xticks=[0,2,4,6,8,10,12],yticks=[0,10,20,30,40,50])
chart('solution-14-91-all.svg',L,T*T,0,13,0,55,'L (m)','T² (s²)',tuple(np.polyfit(L[:5],T[:5]**2,1)),xticks=[0,2,4,6,8,10,12],yticks=[0,10,20,30,40,50])
chart('solution-14-91-ratio.svg',L,T/(2*math.pi*np.sqrt(L/9.8)),2,12,1,1.08,'L (m)','T/T₀',ref=1.05,yticks=[1,1.02,1.04,1.05,1.06,1.08],connect=True)

print('Saved six solution diagrams with compact canvases and20unit labels.')
