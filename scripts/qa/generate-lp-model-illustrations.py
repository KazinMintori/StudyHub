"""Deterministic vector illustrations of the checked LP examples."""
from pathlib import Path
import math
import pymupdf

out=Path('../math-ai-visual-content/docs/toan-cho-ai/bai-giang/img/lec-02');out.mkdir(parents=True,exist_ok=True)
qa=Path('qa/math-ai-visuals/lp-model-illustrations');qa.mkdir(parents=True,exist_ok=True)
ink='#242136';purple='#7757b9';green='#19705a';orange='#a25b12'
def svg(width,height,body,title):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img"><title>{title}</title><rect width="{width}" height="{height}" fill="white"/><g fill="{ink}" font-family="sans-serif" font-size="17">{body}</g></svg>'
def line(x,y,u,v,color=ink,width=1.2,extra=''):
 return f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="{color}" stroke-width="{width}" {extra}/>'
def text(x,y,label,anchor='start',size=17):
 return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}">{label}</text>'
def write(name,data):
 p=out/(name+'.svg');p.write_text(data,encoding='utf-8')
 from lxml import etree
 element=etree.fromstring(data.encode())
 element.set('width','294');element.set('height',str(294*float(element.get('viewBox').split()[3])/360))
 root=etree.tostring(element,encoding='unicode')
 doc=pymupdf.open(stream=root.encode(),filetype='svg')
 doc[0].get_pixmap().save(qa/(name+'.png'))
def point(x,y):return [40+50*x,244-28*y]
body=line(25,244,335,244)+line(40,27,40,255)
for color,fn in [(purple,lambda x:3-x),(orange,lambda x:x/2),(green,lambda x:2*x-5)]:
 # Clip each mathematical affine line to the displayed y range [0,7].
 samples=[point(i/100,fn(i/100)) for i in range(0,581) if 0<=fn(i/100)<=7]
 body+=f'<polyline points="{" ".join(f"{x:.3f},{y:.3f}" for x,y in samples)}" fill="none" stroke="{color}" stroke-width="1.3"/>'
samples=[point(i/100,max(3-i/100,i/200,2*i/100-5)) for i in range(0,581)]
body+=f'<polyline points="{" ".join(f"{x:.3f},{y:.3f}" for x,y in samples)}" fill="none" stroke="{ink}" stroke-width="2"/>'
x,y=point(2,1);body+=f'<circle cx="{x}" cy="{y}" r="5" fill="{purple}"/>'
body+=text(x+12,y-9,'(2, 1)')+text(337,266,'x')+text(49,26,'f')
body+=text(180,290,'Đường đậm là giá trị lớn nhất',anchor='middle',size=16)
write('piecewise-affine-envelope',svg(360,310,body,'Ba hàm affine và đường bao lồi có đáy tại x bằng hai, f bằng một'))

def clip(poly,a,b):
 result=[]
 for p,q in zip(poly,poly[1:]+poly[:1]):
  v=sum(x*y for x,y in zip(a,p))-b;w=sum(x*y for x,y in zip(a,q))-b
  if v<=1e-10:result.append(p)
  if v*w<0:
   t=v/(v-w);result.append([p[i]+t*(q[i]-p[i]) for i in range(2)])
 return result
def project(x,y,z):
 a,b=map(math.radians,[32,28]);u=(x-.5)*math.cos(a)-(y-.5)*math.sin(a);v=(x-.5)*math.sin(a)+(y-.5)*math.cos(a)
 return [180+62*u,189-62*(.85*z*math.cos(b)-v*math.sin(b))]
planes=[([1,1],-2),([-1,0],0),([0,-1],0)]
body=''
for index,(a,b) in enumerate(planes):
 poly=[[-1,-1],[2,-1],[2,2],[-1,2]]
 for j,(d,e) in enumerate(planes):
  if index!=j:poly=clip(poly,[d[i]-a[i] for i in range(2)],b-e)
 points=[project(x,y,a[0]*x+a[1]*y+b) for x,y in poly]
 body+=f'<polygon points="{" ".join(f"{x:.3f},{y:.3f}" for x,y in points)}" fill="{["#eee7f7","#e4f2ec","#fff0d8"][index]}" stroke="{[purple,green,orange][index]}" stroke-width="1.2"/>'
point3=project(2/3,2/3,-2/3)
body+=f'<circle cx="{point3[0]}" cy="{point3[1]}" r="5" fill="{purple}"/>'
body+=text(point3[0]+13,point3[1]+24,'Đáy: −2/3',size=16)
origin=project(-1,-1,-1)
for end,label,dx,dy in [([2.25,-1,-1],'x₁',8,18),([-1,2.25,-1],'x₂',-22,18),([-1,-1,2.4],'f',10,0)]:
 q=project(*end);body+=line(*origin,*q,color='#81798e',width=1)+text(q[0]+dx,q[1]+dy,label)
body+=text(180,316,'Đồ thị là mặt trên của ba mặt phẳng',anchor='middle',size=16)
write('piecewise-affine-surface',svg(360,340,body,'Ba mảnh affine tạo đồ thị lồi trong R3, đáy tại hai phần ba, hai phần ba, âm hai phần ba'))

body=''
for y,title,caption in [(32,'Giai đoạn 1','Sản xuất 4, đáp ứng nhu cầu 2'),(267,'Giai đoạn 2','Sản xuất 1, đáp ứng nhu cầu 3')]:
 body+=f'<rect x="30" y="{y}" width="300" height="77" rx="8" fill="#f5f1fb" stroke="{purple}" stroke-width="1.3"/>'
 body+=text(180,y+29,title,anchor='middle')+text(180,y+57,caption,anchor='middle',size=16)
body+=line(180,109,180,166,color=green,width=1.5)+line(180,218,180,265,color=green,width=1.5)
body+=f'<path d="M175,157 l5,9 5,-9 M175,256 l5,9 5,-9" fill="none" stroke="{green}" stroke-width="1.5"/>'
body+=f'<rect x="90" y="167" width="180" height="51" rx="8" fill="#e4f2ec" stroke="{green}" stroke-width="1.3"/>'
body+=text(180,198,'Tồn kho s₁ = 2',anchor='middle')
body+=text(180,375,'Tồn đầu kỳ 1 và cuối kỳ 2 đều bằng 0',anchor='middle',size=16)
body+=text(180,402,'Tổng chi phí tối ưu: 8 đơn vị',anchor='middle',size=17)
write('two-period-inventory',svg(360,425,body,'Hai giai đoạn sản xuất, hai đơn vị tồn kho chuyển sang kỳ hai và tổng chi phí tám đơn vị'))
print('Generated three exact SVG diagrams and 294 px review PNGs; browser font/layout QA remains separate.')
