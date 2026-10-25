"""Solution snapshots and regression plot, with unchanged physical data."""
from pathlib import Path
import math,json
ROOT=Path(__file__).resolve().parents[1]
O=ROOT/'docs/vat-ly-1/bai-giang/img/young-15';O.mkdir(exist_ok=True)
DATA=[(.0260,559,48.1),(.0260,249,31.9),(.0374,365,32.0),(.0374,207,24.2),(.0482,262,23.8)]
mass=[m/1000 for mu,m,d in DATA]
ordinates=[mu*.1*(d/100)**2 for mu,m,d in DATA]
xbar=sum(mass)/5;ybar=sum(ordinates)/5
slope=sum((x-xbar)*(y-ybar)for x,y in zip(mass,ordinates))/sum((x-xbar)**2 for x in mass)
MODEL={'y_kgm':ordinates,'slope_m':slope,'intercept_kgm':ybar-slope*xbar}
def open_svg(w,h):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%"><rect width="100%" height="100%" fill="white"/><g font-family="Segoe UI, sans-serif" font-size="20" fill="#17212b">'
def line(x1,y1,x2,y2,c='#98a2b3',sw=1):return f'<path d="M{x1:.3f} {y1:.3f}L{x2:.3f} {y2:.3f}" fill="none" stroke="{c}" stroke-width="{sw}"/>'
def txt(x,y,t,c='#17212b',anchor='start'):return f'<text x="{x:.3f}" y="{y:.3f}" fill="{c}" text-anchor="{anchor}">{t}</text>'
X=lambda x:65+x/10*270
Y=lambda y:260-y/.75*100
s=open_svg(360,420)
for x in range(11):
 s+=line(X(x),160,X(x),360,'#e4e7ec')
 if x%2==0:s+=txt(X(x),388,str(x),anchor='middle')
for y in [-.75,0,.75]:s+=line(65,Y(y),335,Y(y),'#e4e7ec')+txt(55,Y(y)+5,str(y).replace('.',','),anchor='end')
s+=line(65,Y(0),345,Y(0),'#344054',2)+line(65,145,65,365,'#344054',2)+txt(335,414,'x (cm)',anchor='end')+txt(12,138,'y (cm)')
for i,(t,c) in enumerate([(0,'#2458a6'),(.0005,'#007c78'),(.001,'#b42318')]):
 pts=[(X(x/20),Y(.75*math.cos(.4*math.pi*(x/20)+250*math.pi*t))) for x in range(201)]
 s+=f'<polyline fill="none" stroke="{c}" stroke-width="2.5" points="'+ ' '.join(f'{x:.3f},{y:.3f}' for x,y in pts)+'"/>'
 s+=line(25,25+i*28,60,25+i*28,c,3)+txt(70,30+i*28,('t = '+str(t).replace('.',',')+' s'),c)
s+=txt(20,115,'Truyền sang trái')+'</g></svg>'; (O/'solution-15-46-snapshots.svg').write_text(s,encoding='utf-8')
# Regression graph in original physical axes; displayed y scaled by 10^4 for readable ticks.
N=MODEL;xs=[.559,.249,.365,.207,.262];ys=N['y_kgm'];a=N['slope_m'];b=N['intercept_kgm']
s=open_svg(360,340);X=lambda x:65+x/.6*270;Y=lambda y:270-y/.00065*210
for x in [0,.1,.2,.3,.4,.5,.6]:s+=line(X(x),60,X(x),270,'#e4e7ec')+txt(X(x),296,str(x).replace('.',','),anchor='middle')
for n in range(7):y=n*.0001;s+=line(65,Y(y),335,Y(y),'#e4e7ec')+txt(53,Y(y)+5,str(n),anchor='end')
s+=line(65,270,345,270,'#344054',2)+line(65,45,65,270,'#344054',2)+txt(335,330,'M (kg)',anchor='end')+txt(12,25,'μd² (10⁻⁴ kg m)')
s+=line(X(.01),Y(a*.01+b),X(.59),Y(a*.59+b),'#2458a6',2.5)
for x,y in zip(xs,ys):s+=f'<circle cx="{X(x):.3f}" cy="{Y(y):.3f}" r="4.5" fill="#007c78"/>'
s+='</g></svg>';(O/'solution-15-73-regression.svg').write_text(s,encoding='utf-8')

print('Generated two compact20unit-labelled solution plots.')
