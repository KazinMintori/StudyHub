"""Separate solution diagrams; never changes original textbook image crops."""
from pathlib import Path
import math,json,hashlib,html
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
B=ROOT/'raw_materials/physics/translations/chapter-01'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-01';OUT.mkdir(exist_ok=True)
polar=lambda r,t:np.array([r*math.cos(math.radians(t)),r*math.sin(math.radians(t))])
ZERO=np.zeros(2);BLUE='#2563eb';GREEN='#15803d';RED='#be123c';PURPLE='#7e22ce'
def segment(start,delta,label,color,offset=(0,-10)):
 return {'start':np.asarray(start).tolist(),'delta':np.asarray(delta).tolist(),'label':label,'color':color,'labelOffset':list(offset)}
def path_vectors(deltas):
 start=ZERO.copy();rows=[]
 for i,v in enumerate(deltas):rows.append(segment(start,v,'d'+str(i+1),[BLUE,GREEN,RED,PURPLE][i],(-18,-10)));start=start+v
 return rows,start
def panel(title,vectors,legend,projection=None):return {'title':title,'vectors':vectors,'legend':legend,'projection':projection.tolist()if projection is not None else None}
def addition(title,a,b,result_label,legend):
 return panel(title,[segment(ZERO,a,'A',BLUE,(-18,0)),segment(a,b,'B',GREEN,(8,-8)),segment(ZERO,a+b,result_label,PURPLE,(8,12))],legend)
route,end=path_vectors([np.array([0.,2.6]),np.array([4.,0.]),polar(3.1,45)])
cave,cave_end=path_vectors([np.array([-180.,0]),polar(210,315),polar(280,60)])
cave.append(segment(cave_end,-cave_end,'d4',PURPLE,(-20,-10)))
drive,drive_end=path_vectors([np.array([0.,3.25]),np.array([-2.2,0]),np.array([0.,-1.5])])
A=polar(8,-90);V=polar(15,60)
a=polar(2.8,60);b=polar(1.9,-60)
specs=[
 ('S1.21','s1-21-scale-diagram.svg',[panel('Ba chặng đường và độ dời',route+[segment(ZERO,end,'R',PURPLE,(10,7))],['d1: 2,6 km về bắc','d2: 4,0 km về đông','d3: 3,1 km, góc 45°'])]),
 ('S1.22','s1-22-scale-diagram.svg',[
   addition('(a): A + B',A,V,'A+B',['A hướng xuống, B chếch lên','Tổng hướng đông bắc']),
   panel('(b): A − B',[segment(ZERO,A,'A',BLUE,(-24,0)),segment(A,-V,'−B',GREEN,(-28,0)),segment(ZERO,A-V,'A−B',PURPLE,(12,-5))],['Đặt −B tại ngọn A','Hiệu hướng tây nam']),
   panel('(c): −A − B',[segment(ZERO,-A,'−A',BLUE,(-25,0)),segment(-A,-V,'−B',GREEN,(-25,0)),segment(ZERO,-A-V,'−A−B',PURPLE,(4,18))],['Vector đối của A+B','Độ lớn giữ nguyên']),
   panel('(d): B − A',[segment(ZERO,V,'B',BLUE,(8,-7)),segment(V,-A,'−A',GREEN,(12,0)),segment(ZERO,V-A,'B−A',PURPLE,(-65,0))],['Vector đối của A−B','Hiệu hướng đông bắc'])]),
 ('S1.23','s1-23-closed-route.svg',[panel('Bốn độ dời khép kín',cave,['d1: 180 m về tây','d2: 210 m, d3: 280 m','d4 trở về đúng điểm đầu'])]),
 ('S1.28','s1-28-addition-diagram.svg',[panel('Độ dời và hai thành phần',route+[segment(ZERO,end,'R',PURPLE,(10,7))],['Rₓ ≈ 6,19 km','Rᵧ ≈ 4,79 km','R ≈ 7,8 km'],projection=end)]),
 ('S1.31','s1-31-drive-route.svg',[panel('Độ dời về phía tây bắc',drive+[segment(ZERO,drive_end,'R',PURPLE,(2,20))],['d1: 3,25 km về bắc','d2: 2,20 km về tây','d3: 1,50 km về nam'])]),
 ('S1.33','s1-33-vector-diagrams.svg',[
   addition('(a): A + B',a,b,'A+B',['Hai thành phần y trái dấu','Tổng nghiêng ít so với +x']),
   panel('(b): A − B',[segment(ZERO,a,'A',BLUE,(-18,0)),segment(a,-b,'−B',GREEN,(8,0)),segment(ZERO,a-b,'A−B',PURPLE,(-65,0))],['Hai đóng góp y cùng dương','Hiệu gần hướng thẳng đứng']),
   panel('(c): B − A',[segment(ZERO,b,'B',BLUE,(8,-10)),segment(b,-a,'−A',GREEN,(8,0)),segment(ZERO,b-a,'B−A',PURPLE,(-65,0))],['Vector đối của A−B','Độ lớn bằng nhau'])]),
 ('S1.36','s1-36-vector-difference.svg',[panel('Vector A, B và hiệu A−B',[
   segment(ZERO,[4,7],'A',BLUE,(12,0)),segment(ZERO,[5,-2],'B',GREEN,(7,20)),segment(ZERO,[-1,9],'A−B',PURPLE,(-70,0))],['A = (4, 7), B = (5, −2)','A−B = (−1, 9)','Hiệu nằm ở phần tư II'])])
]
def render_panels(panels):
 height=415*len(panels)
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="{height}" viewBox="0 0 360 {height}" role="img" aria-label="Sơ đồ vector có cùng tỷ lệ trên hai trục">','<rect width="360" height="100%" rx="10" fill="#fff"/>','<defs>']
 for color in [BLUE,GREEN,RED,PURPLE]:parts.append(f'<marker id="c{color[1:]}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{color}"/></marker>')
 parts.append('</defs><g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#172033">')
 for index,p in enumerate(panels):
  top=415*index
  parts.append(f'<g transform="translate(0 {top})"><text x="180" y="28" text-anchor="middle" font-weight="600">{html.escape(p["title"])}</text>')
  points=[ZERO]
  for row in p['vectors']:points.extend([np.array(row['start']),np.array(row['start'])+row['delta']])
  if p['projection']is not None:points.extend([np.array([p['projection'][0],0]),np.array([0,p['projection'][1]])])
  pts=np.array(points);lo=pts.min(axis=0);hi=pts.max(axis=0);span=hi-lo
  scale=min(236/max(span[0],1e-10),218/max(span[1],1e-10))
  center=(lo+hi)/2
  def xy(v):return np.array([180+(v[0]-center[0])*scale,177-(v[1]-center[1])*scale])
  if p['projection']is not None:
   e=np.array(p['projection']);ep=xy(e)
   for v in [[e[0],0],[0,e[1]]]:
    tp=xy(v);parts.append(f'<line x1="{ep[0]:.4f}" y1="{ep[1]:.4f}" x2="{tp[0]:.4f}" y2="{tp[1]:.4f}" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 4"/>')
  for row in p['vectors']:
   start=np.array(row['start']);end=start+row['delta'];u=xy(start);v=xy(end);mid=(u+v)/2+row['labelOffset']
   parts.append(f'<line x1="{u[0]:.4f}" y1="{u[1]:.4f}" x2="{v[0]:.4f}" y2="{v[1]:.4f}" stroke="{row["color"]}" stroke-width="2.5" marker-end="url(#c{row["color"][1:]})"/>')
   parts.append(f'<text x="{mid[0]:.4f}" y="{mid[1]:.4f}" fill="{row["color"]}" paint-order="stroke" stroke="#fff" stroke-width="4" stroke-linejoin="round">{html.escape(row["label"])}</text>')
  o=xy(ZERO);parts.append(f'<circle cx="{o[0]:.4f}" cy="{o[1]:.4f}" r="3" fill="#172033"/><text x="{o[0]-17:.4f}" y="{o[1]+22:.4f}">O</text>')
  parts.append('<line x1="24" y1="311" x2="336" y2="311" stroke="#cbd5e1"/>')
  for j,line in enumerate(p['legend']):parts.append(f'<text x="24" y="{340+26*j}">{html.escape(line)}</text>')
  parts.append('</g>')
 parts.append('</g></svg>')
 return '\n'.join(parts)+'\n'
manifest=[]
for key,name,panels in specs:
 p=OUT/('solution-'+name);p.write_text(render_panels(panels),encoding='utf-8')
 manifest.append({'key':'solution-image:'+key,'output':'proposed-assets/'+name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'description':'Sơ đồ lời giải độc lập cho bài'+key[1:]+'.','generator':'generate-reviewed-solution-diagrams.py','panels':panels,'minimumFontUnits':20})
earlyManifest=manifest

sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
theta=math.radians(35);c=math.cos(theta);s=math.sin(theta)
O=(218.,133.);F=(0.,145.)
ex=(-c,s);ey=(-s,-c)
fx=tuple(145*s*v for v in ex);fy=tuple(-145*c*v for v in ey)
plus=lambda u,v:(u[0]+v[0],u[1]+v[1])
X=plus(O,fx);Y=plus(O,fy);W=plus(O,F)
axisx=plus(O,tuple(120*v for v in ex));axisy=plus(O,tuple(93*v for v in ey))
def line(a,b,color,width=2,dash='',marker=False):
 return f'<line x1="{a[0]:.4f}" y1="{a[1]:.4f}" x2="{b[0]:.4f}" y2="{b[1]:.4f}" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"'if dash else'')+(f' marker-end="url(#{color[1:]})"'if marker else'')+'/>'
svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 408" role="img" aria-labelledby="title desc">','<title id="title">Phân tích trọng lượng trên mái nghiêng 35 độ</title>','<desc id="desc">Trục x hướng xuống dốc về bên trái. Trục y vuông góc mái hướng ra ngoài về phía trên bên trái. Thành phần Fx hướng xuống dốc, Fy hướng vào mái xuống bên phải. Tổng hai thành phần là trọng lực thẳng đứng xuống.</desc>','<rect width="360" height="408" rx="12" fill="#fff"/>','<defs>']
for color in ['#2563eb','#15803d','#9333ea']:
 svg.append(f'<marker id="{color[1:]}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{color}"/></marker>')
svg+=['</defs>','<g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#172033">','<text x="180" y="28" text-anchor="middle" font-weight="600">Phân tích trọng lượng</text>','<text x="180" y="54" text-anchor="middle">Trên mái nghiêng 35°</text>',line(O,axisx,'#2563eb',1.7,'4 4',True),line(O,axisy,'#2563eb',1.7,'4 4',True),line(X,W,'#94a3b8',1.5,'4 4'),line(Y,W,'#94a3b8',1.5,'4 4'),line(O,X,'#15803d',3,marker=True),line(O,Y,'#15803d',3,marker=True),line(O,W,'#9333ea',3.2,marker=True),'<circle cx="218" cy="133" r="3.5" fill="#172033"/>','<text x="83" y="211" fill="#2563eb">+x</text>','<text x="133" y="85" fill="#2563eb">+y</text>','<text x="114" y="166" fill="#15803d">Fₓ</text>','<text x="297" y="223" fill="#15803d">Fᵧ</text>','<text x="228" y="286" fill="#9333ea">F</text>']
r=48;pa=plus(O,(r*math.sin(theta),r*math.cos(theta)));pb=plus(O,(0,r))
svg+=[f'<path d="M{pa[0]:.4f} {pa[1]:.4f} A48 48 0 0 1 {pb[0]:.4f} {pb[1]:.4f}" fill="none" stroke="#9333ea" stroke-width="1.5"/>','<text x="234" y="199" fill="#9333ea">35°</text>','<line x1="24" y1="309" x2="336" y2="309" stroke="#d1d5db"/>','<text x="24" y="338">Fₓ = F sin 35°</text>','<text x="24" y="366">Fᵧ = −F cos 35°</text>','<text x="24" y="394">|Fᵧ| ≤ 425 N</text>','</g></svg>']
p=OUT/'solution-s-bridge-roof-fbd.svg';p.write_text('\n'.join(svg)+'\n',encoding='utf-8')
manifest=[{'key':'s-bridge-roof-fbd','file':'proposed-assets/s-bridge-roof-fbd.svg','sha256':sha(p),'purpose':'Phân tích trọng lực theo hai trục vuông góc gắn với mái nghiêng.','sourceFigureUnchanged':True,'geometry':{'origin':O,'xUnitScreen':ex,'yUnitScreen':ey,'FxScreen':fx,'FyScreen':fy,'FScreen':F,'thetaDegrees':35,'svgTextMinimum':20},'generator':'generate-reviewed-assets.py'}]

allRows=earlyManifest+manifest
for row in allRows:
 key=row['key'].removeprefix('solution-image:')
 filename=(row.get('output')or row.get('file')).split('/')[-1]
 row['publicFile']='docs/vat-ly-1/bai-giang/img/young-01/solution-'+filename
 row['sha256']=sha(ROOT/row['publicFile'])
 row['generator']='scripts/generate-physics1-remaining-01-solution-figures.py'
 row.pop('output',None);row.pop('file',None)
(B/'parent-solution-image-manifest.json').write_text(json.dumps({'status':'reproducible-reviewed-figures','sourceUnits':[21,22,23,28,31,33,36,'bridge'],'assets':allRows},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Generated',len(allRows),'reviewed standalone solution diagrams; original textbook images unchanged.')
