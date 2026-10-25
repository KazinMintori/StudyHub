"""Reproducible wave snapshots and reflection diagrams; original source images remain separate."""
from pathlib import Path
import json,math,hashlib,html
ROOT=Path(__file__).resolve().parents[1]
B=ROOT/'qa/physics1-remaining/ch15/solution-regeneration'
O=ROOT/'docs/vat-ly-1/bai-giang/img/young-15'
B.mkdir(parents=True,exist_ok=True);O.mkdir(exist_ok=True)
manifest=[];checks=[];datasets={}
def verify(label,got,expected,tol=1e-7):
 ok=abs(got-expected)<=tol;checks.append({'label':label,'actual':got,'expected':expected,'passed':ok});assert ok,label
def tri(x,center,height,half):return height*max(0,1-abs(x-center)/half)
def rect(x,left,right,height):return height if left<x<right else 0
def render(key,title,xlim,ylim,unit,times,tlabel,fn,ticks,extra=None,points=None,mirror=False):
 rowh=152;height=46+rowh*len(times);plotleft=44;plotright=338
 def X(x):return plotleft+(x-xlim[0])/(xlim[1]-xlim[0])*(plotright-plotleft)
 def text(x,y,s,size=18,anchor='start',fill='#2b2435'):
  return f'<text x="{x:.3f}" y="{y:.3f}" font-size="{size}" text-anchor="{anchor}" fill="{fill}">{html.escape(str(s))}</text>'
 svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 {height}" role="img"><title>{html.escape(title)}</title>',
 '<rect width="100%" height="100%" fill="white"/>','<g font-family="Arial, sans-serif">',text(12,23,title,18)]
 data=[]
 for j,t in enumerate(times):
  top=40+j*rowh;base=top+54;scale=34/ylim
  def Y(y):return base-y*scale
  xs=[xlim[0]+(xlim[1]-xlim[0])*i/1200 for i in range(1201)]
  if extra:
   for z in extra(t):
    for x in [z-1e-6,z,z+1e-6]:
     if xlim[0]<=x<=xlim[1]:xs.append(x)
  xs=sorted(set(xs));ys=[fn(x,t)for x in xs]
  data.append({'t':t,'x':xs,'y':ys})
  svg+=[text(12,top+8,tlabel(t)),f'<path d="M{plotleft} {base}H{plotright}" stroke="#a39baa" fill="none"/>']
  for x,label in ticks:
   svg.append(f'<path d="M{X(x):.3f} {base-3}v6" stroke="#a39baa"/>');svg.append(text(X(x),base+55,label,18,'middle'))
  for y in [-ylim,0,ylim]:svg.append(text(plotleft-7,Y(y)+5,f'{y:g}',18,'end'))
  path=' '.join(('M'if i==0 else'L')+f'{X(x):.4f},{Y(y):.4f}'for i,(x,y)in enumerate(zip(xs,ys)))
  svg.append(f'<path d="{path}" fill="none" stroke="#62409a" stroke-width="2.4" stroke-linejoin="round"/>')
  if mirror:
   path=' '.join(('M'if i==0 else'L')+f'{X(x):.4f},{Y(-y):.4f}'for i,(x,y)in enumerate(zip(xs,ys)))
   svg.append(f'<path d="{path}" fill="none" stroke="#2b8993" stroke-width="2" stroke-dasharray="5 4"/>')
  if points:
   for x in points:svg.append(f'<circle cx="{X(x):.3f}" cy="{Y(fn(x,t)):.3f}" r="3.0" fill="#ac3f73"/>')
  yunit='cm'if unit=='cm, L'else unit
  xlabel='x'if unit=='cm, L'else 'x ('+unit+')'
  if key.endswith('-fixed'):
   svg.append(f'<circle cx="{X(0):.3f}" cy="{Y(0):.3f}" r="3" fill="#2b2435"/>')
  svg.append(text(plotright,top+8,f'y ({yunit})',18,'end'))
  svg.append(text(plotright,base+79,xlabel,18,'end'))
 svg+=['</g></svg>'];file=O/('solution-'+key.lower().replace('.','-')+'.svg');file.write_text(''.join(svg),encoding='utf-8')
 manifest.append({'key':'source-solution:'+key,'output':file.relative_to(ROOT).as_posix(),'generated_by':'generate_solution_figures.py','sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'title':title,'times':times,'source_crops_modified':False})
 datasets[key]=data

render('S15.13','Dạng dây ở ba thời điểm',(0,12),.3,'cm',[0,.4,.8],lambda t:f't = {t:.3f} s',lambda x,t:.3*math.cos(2*math.pi*(x-6*t)/12),[(0,'0'),(3,'3'),(6,'6'),(9,'9'),(12,'12')],points=[1.5*i for i in range(9)])
for sign,name,title in [(-1,'fixed','Đầu cố định'),(1,'free','Đầu tự do')]:
 p=lambda u:tri(u,-12,4,4)
 fn=lambda x,t,s=sign:p(x-400*t)+s*p(-x-400*t)
 times=[.015,.020,.025,.030,.035,.040,.045]
 render('S15.28-'+name,'Xung tam giác: '+title,(-20,0),8 if sign==1 else 4,'mm',times,lambda t:f't = {t*1000:.0f} ms',fn,[(-20,'−20'),(-10,'−10'),(0,'O')],extra=lambda t:[-16+400*t,-12+400*t,-8+400*t,16-400*t,12-400*t,8-400*t])
 for t in times:
  if sign==-1:verify('28 fixed endpoint '+str(t),fn(0,t),0)
  else:verify('28 free slope '+str(t),(fn(1e-5,t)-fn(-1e-5,t))/(2e-5),0)
 verify('28 peak at O '+name,fn(0,.030),8 if sign==1 else 0)
for sign,name,title in [(-1,'fixed','Đầu cố định'),(1,'free','Đầu tự do')]:
 p=lambda u:rect(u,10,30,5)
 fn=lambda x,t,s=sign:p(x+5000*t)+s*p(-x+5000*t)
 times=[.001,.002,.003,.004,.005,.006,.007]
 render('S15.29-'+name,'Xung chữ nhật: '+title,(0,40),10 if sign==1 else 5,'mm',times,lambda t:f't = {t*1000:.0f} ms',fn,[(0,'O'),(10,'10'),(20,'20'),(30,'30'),(40,'40')],extra=lambda t:[10-5000*t,30-5000*t,5000*t-10,5000*t-30])
 for t in times:
  if sign==-1:verify('29 fixed endpoint '+str(t),fn(0,t),0)
 verify('29 total midpoint overlap '+name,fn(5,.004),10 if sign==1 else 0)
for sign,n in [(1,30),(-1,31)]:
 fn=lambda x,t,s=sign:tri(x,-1.5+2*t,1,1)+s*tri(x,1.5-2*t,1,1)
 times=[.25,.50,.75,1,1.25]
 render('S15.'+str(n),'Hai xung '+('cùng dấu'if sign==1 else'trái dấu'),(-3,3),2 if sign==1 else 1,'cm',times,lambda t:f't = {t:.3f} s',fn,[(-3,'−3'),(-1,'−1'),(0,'0'),(1,'1'),(3,'3')],extra=lambda t:[-2.5+2*t,-1.5+2*t,-.5+2*t,.5-2*t,1.5-2*t,2.5-2*t])
 verify(f'{n} full overlap',fn(0,.75),1+sign)
fn=lambda x,t:rect(x,t-4,t,3)+rect(x,8-t,12-t,-4)
render('S15.32','Hai xung chữ nhật khác độ cao',(-4,12),4,'mm',[4,6,10],lambda t:f't = {t:.2f} s',fn,[(-4,'−4'),(0,'0'),(4,'4'),(8,'8'),(12,'12')],extra=lambda t:[t-4,t,8-t,12-t])
verify('32 full overlap',fn(4,6),-1)
render('S15.39','Họa âm thứ ba: Ba bụng',(0,1),5.6,'cm, L',[0],lambda t:'Hai dạng biên đối dấu',lambda x,t:5.6*math.sin(3*math.pi*x),[(0,'0'),(1/3,'L/3'),(2/3,'2L/3'),(1,'L')],mirror=True)

(B/'solution-figure-data.json').write_text(json.dumps(datasets,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
(B/'solution-figure-checks.json').write_text(json.dumps({'status':'passed','assertions':checks,'count':len(checks)},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Generated nine unchanged-data solution diagrams;18unit labels and consistent x-axis for15.39.')
