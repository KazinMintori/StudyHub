from pathlib import Path
import math,json,hashlib,html,numpy as np
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'raw_materials/physics/translations/chapter-03';OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-03';BLUE='#2563eb';GREEN='#15803d';RED='#be123c';PURPLE='#7e22ce';manifest=[]
g=9.8;rad=math.radians;ns='http://www.w3.org/2000/svg'
def head(height,title):
 return[f'<svg xmlns="{ns}" width="360" height="{height}" viewBox="0 0 360 {height}" role="img" aria-label="{html.escape(title)}">',f'<title>{html.escape(title)}</title>',f'<rect width="360" height="{height}" rx="10" fill="white"/>','<defs>']+[f'<marker id="m{c[1:]}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7 Z" fill="{c}"/></marker>'for c in [BLUE,GREEN,RED,PURPLE]]+['</defs>','<g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#172033">',f'<text x="180" y="28" text-anchor="middle" font-weight="600">{html.escape(title)}</text>']
def number(x):return f'{x:.3g}'.replace('.',',')
def save(n,parts,**data):
 parts+=['</g></svg>'];p=OUT/f'solution-s3-{n}.svg';p.write_bytes(('\n'.join(parts)+'\n').encode('utf8'))
 manifest.append({'key':f'solution-image:S3.{n}','file':'proposed-assets/'+p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'sourceUnit':f'3.{n}','minimumFontUnits':20,'generator':'generate-reviewed-diagrams.py',**data})
def graph_panels(n,vx,vy,tf):
 parts=head(1140,f'Bài 3.{n}: Bốn đồ thị');panels=[]
 parts.append('<text x="180" y="56" text-anchor="middle">Gốc tại điểm phóng, đơn vị SI</text>')
 for index,(label,unit,coef)in enumerate([('x','m',[0,vx]),('y','m',[0,vy,-g/2]),('vₓ','m/s',[vx]),('vᵧ','m/s',[vy,-g])]):
  times=np.linspace(0,tf,201);values=np.polynomial.polynomial.polyval(times,coef);lo=min(float(values.min()),0);hi=max(float(values.max()),0)
  if hi-lo<1e-8:hi=lo+1
  span=hi-lo;lo-=.08*span;hi+=.08*span
  y=lambda value:190-(value-lo)/(hi-lo)*140
  pts=np.column_stack((72+240*times/tf,[y(v)for v in values]));top=65+index*265
  parts +=[f'<g transform="translate(0 {top})">',f'<text x="18" y="22" font-weight="600">{label} ({unit})</text>','<path d="M72 45 V197 H322" stroke="#64748b" fill="none"/>',f'<line x1="72" y1="{y(0):.6f}" x2="322" y2="{y(0):.6f}" stroke="#94a3b8" stroke-dasharray="4 4"/>']
  yticks=[0,float(values.min()),float(values.max())];unique=[]
  for tick in yticks:
   if all(abs(y(tick)-y(q))>24 for q in unique):unique.append(tick)
  for tick in unique:parts.append(f'<text x="64" y="{y(tick)+6:.6f}" text-anchor="end">{number(tick)}</text>')
  for tick in [0,tf/2,tf]:
   x=72+240*tick/tf;parts.append(f'<line x1="{x:.6f}" y1="45" x2="{x:.6f}" y2="197" stroke="#e2e8f0"/><text x="{x:.6f}" y="223" text-anchor="middle">{number(tick)}</text>')
  parts +=[f'<polyline data-quantity="{label}" points="'+ ' '.join(f'{x:.6f},{y:.6f}'for x,y in pts)+f'" fill="none" stroke="{BLUE}" stroke-width="2.5"/>','<text x="290" y="250">t (s)</text>','</g>']
  panels.append({'quantity':label,'unit':unit,'timeEnd':tf,'coefficientsAscending':coef,'valueRange':[lo,hi],'screenX':[72,312],'screenY':[190,50],'polylineSamples':201})
 save(n,parts,diagramKind='four-time-graphs',sourceParameters={'vx':vx,'vy':vy,'g':g,'timeEnd':tf},panels=panels)
graph_panels(9,1.1,0,.480)
graph_panels(12,20,12,24/g)
graph_panels(18,12*math.cos(rad(51)),12*math.sin(rad(51)),2.08)
vx=30*math.cos(rad(33));vy=30*math.sin(rad(33));graph_panels(21,vx,vy,(vy+math.sqrt(vy*vy+2*g*15))/g)
def spatial(n,title,points,arrows,labels,legend,polyline=None,source=None):
 data=[np.array(p,dtype=float)for p in points]
 if polyline is not None:data.extend(polyline)
 for a,b,color,tag in arrows:data.extend([np.array(a),np.array(b)])
 a=np.array(data);low=a.min(axis=0);high=a.max(axis=0);center=(low+high)/2;scale=min(245/max(high[0]-low[0],1e-8),200/max(high[1]-low[1],1e-8))
 def screen(p):return np.array([180,160])+(np.array(p)-center)*[scale,-scale]
 parts=head(350+28*len(legend),title);svgArrows=[]
 if polyline is not None:
  xy=np.array([screen(p)for p in polyline]);parts.append('<polyline data-trajectory="true" points="'+' '.join(f'{x:.6f},{y:.6f}'for x,y in xy)+f'" fill="none" stroke="{BLUE}" stroke-width="2.5"/>')
 for index,(a,b,color,tag)in enumerate(arrows):
  start=screen(a);end=screen(b);parts.append(f'<line data-arrow="{index}" x1="{start[0]:.6f}" y1="{start[1]:.6f}" x2="{end[0]:.6f}" y2="{end[1]:.6f}" stroke="{color}" stroke-width="2.5" marker-end="url(#m{color[1:]})"/>');svgArrows.append({'startWorld':np.asarray(a,dtype=float).tolist(),'endWorld':np.asarray(b,dtype=float).tolist(),'color':color,'label':tag})
 boxes=[]
 for p,label in labels:
  x,y=screen(p);width=12*len(label)
  preferred={3:{'t=0':(-44,8),'t=1':(-48,-6),'t=2':(10,25)},7:{'a':(-24,-6)}}.get(n,{}).get(label)
  candidates=([preferred]if preferred else[])+[(10,-10),(10,25),(-width-10,-10),(-width-10,25),(12,8),(-width-12,8),(0,-23),(0,36)]
  for dx,dy in candidates:
   box=(x+dx,y+dy-20,x+dx+width,y+dy+5)
   if box[0]<8 or box[2]>352 or box[1]<36 or box[3]>280:continue
   if any(not(box[2]+4<q[0]or q[2]+4<box[0]or box[3]+3<q[1]or q[3]+3<box[1])for q in boxes):continue
   boxes.append(box);parts.append(f'<text x="{x+dx:.6f}" y="{y+dy:.6f}">{html.escape(label)}</text>');break
  else:raise AssertionError((n,label,'label does not fit'))
 axisx,axisy=('vₓ','vᵧ')if n in [5,6,40,43]else('x','y')
 parts+=['<path d="M270 300 H311 M270 300 V276 M307 297 L311 300 L307 303 M267 280 L270 276 L273 280" stroke="#64748b" fill="none"/>',f'<text x="316" y="306">{axisx}</text>',f'<text x="247" y="274">{axisy}</text>']
 for i,line in enumerate(legend):parts.append(f'<text x="18" y="{330+28*i}">{html.escape(line)}</text>')
 save(n,parts,diagramKind='same-scale-vectors-or-path',screenMapping={'centerWorld':center.tolist(),'centerScreen':[180,160],'scale':scale,'flipY':True},arrows=svgArrows,labelsWorld=[{'anchorWorld':np.asarray(p,dtype=float).tolist(),'text':label}for p,label in labels],worldTrajectory=[list(p)for p in polyline]if polyline is not None else None,sourceParameters=source)
times=np.linspace(0,2,201);path=np.column_stack((4+2.5*times*times,5*times));arrows=[];labels=[]
for t in [0,1,2]:
 p=np.array([4+2.5*t*t,5*t]);v=np.array([5*t,5]);end=p+.4*v;arrows.append((p,end,GREEN,'v'));labels.append((p,f't={t}'))
spatial(3,'Bài 3.3: Quỹ đạo và vận tốc',[],arrows,labels,['Tọa độ x, y tính bằng cm','Mũi tên xanh lá: Vận tốc','Độ dài mũi tên bằng 0,4 s × v','Các nhãn t có đơn vị giây'],path,{'timeEnd':2,'xCoefficients':[4,0,2.5],'yCoefficients':[0,5],'velocityScaleSeconds':.4})
path=np.column_stack((2.4*times,3-1.2*times*times));p=path[-1];v=np.array([2.4,-4.8]);a=np.array([0,-2.4]);vend=p+.3*v;aend=p+.5*a
spatial(7,'Bài 3.7: Vận tốc và gia tốc',[],[(p,vend,GREEN,'v'),(p,aend,RED,'a')],[(path[0],'t=0'),(p,'t=2'),(vend,'v'),(aend,'a')],['Tọa độ x, y tính bằng m','Mũi tên v: Hệ số 0,3 s','Mũi tên a: Hệ số 0,5 s²','Vận tốc tiếp tuyến với đường bay'],path,{'timeEnd':2,'xCoefficients':[0,2.4],'yCoefficients':[3,0,-1.2],'velocityScaleSeconds':.3,'accelerationScaleSeconds2':.5})
for n,v1,v2,legend in [(5,np.array([90,110]),np.array([-170,40]),['v₁: Lúc t = 0 s','v₂: Lúc t = 30,0 s','Tím: Hiệu v₂ − v₁','Hai trục là vₓ, vᵧ (m/s)']),(6,np.array([2.6,-1.8]),np.array([2.6,-1.8])+10*.45*np.array([math.cos(rad(31)),math.sin(rad(31))]),['v₁: Lúc t = 10,0 s','v₂: Lúc t = 20,0 s','Tím: Hiệu v₂ − v₁','Hai trục là vₓ, vᵧ (m/s)'])]:
 spatial(n,f'Bài 3.{n}: Hai vận tốc',[[0,0]],[(np.zeros(2),v1,BLUE,'v₁'),(np.zeros(2),v2,GREEN,'v₂'),(v1,v2,PURPLE,'Δv')],[(np.zeros(2),'O'),(v1,'v₁'),(v2,'v₂')],legend,source={'v1':v1.tolist(),'v2':v2.tolist()})
air=np.array([0.,-35]);wind=np.array([-10/math.sqrt(2),-10/math.sqrt(2)]);ground=air+wind
spatial(40,'Bài 3.40: Máy bay và gió',[[0,0]],[(np.zeros(2),air,PURPLE,'A'),(air,ground,GREEN,'B'),(np.zeros(2),ground,RED,'R')],[(air/2,'A'),(air+wind/2,'B'),(ground/2,'R')],['A: Máy bay so với không khí','B: Gió so với mặt đất','R: Máy bay so với mặt đất','Đông sang phải, Bắc hướng lên','Đơn vị vận tốc: m/s'],source={'air':air.tolist(),'wind':wind.tolist(),'ground':ground.tolist()})
air=np.array([-math.sqrt(320**2-80**2),80.]);wind=np.array([0.,-80]);ground=air+wind
spatial(43,'Bài 3.43: Bay về Tây',[[0,0]],[(np.zeros(2),air,PURPLE,'A'),(air,ground,GREEN,'B'),(np.zeros(2),ground,RED,'R')],[(air/2,'A'),(air+wind/2,'B'),(ground/2,'R')],['A: Máy bay so với không khí','B: Gió thổi về phía Nam','R: Đường bay theo hướng Tây','Đông sang phải, Bắc hướng lên','Đơn vị vận tốc: km/h'],source={'air':air.tolist(),'wind':wind.tolist(),'ground':ground.tolist()})
print('Reproduced',len(manifest),'separate solution diagrams.')
