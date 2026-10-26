from pathlib import Path
import math,json,hashlib,html,numpy as np
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'raw_materials/physics/translations/chapter-03';OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-03';BLUE="#2563eb";GREEN="#15803d";RED="#be123c";PURPLE="#7e22ce";manifest=[]
g=9.8;rad=math.radians;ns="http://www.w3.org/2000/svg"
def head(height,title):
 return[f'<svg xmlns="{ns}" width="360" height="{height}" viewBox="0 0 360 {height}" role="img" aria-label="{html.escape(title)}">',f'<title>{html.escape(title)}</title>',f'<rect width="360" height="{height}" rx="10" fill="white"/>','<defs>']+[f'<marker id="m{c[1:]}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7 Z" fill="{c}"/></marker>'for c in [BLUE,GREEN,RED,PURPLE]]+['</defs>','<g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#172033">',f'<text x="180" y="28" text-anchor="middle" font-weight="600">{html.escape(title)}</text>']

def number(x):return f'{x:.0f}'if abs(x)>=1000 else f'{x:.3g}'.replace('.',',')

def save(n,parts,**data):
 parts+=['</g></svg>'];p=OUT/f'solution-s3-{n}.svg';p.write_bytes(('\n'.join(parts)+'\n').encode('utf8'))
 manifest.append({'key':f'solution-image:S3.{n}','file':'proposed-assets/'+p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'sourceUnit':f'3.{n}','minimumFontUnits':20,'generator':'generate-reviewed-diagrams.py',**data})

def graph_panels(n,vx,vy,tf,y0=0):
 parts=head(1140,f'Bài 3.{n}: Bốn đồ thị');panels=[]
 parts.append('<text x="180" y="56" text-anchor="middle">'+("Gốc tại điểm phóng, đơn vị SI"if y0==0 else"Độ cao y tính từ mặt đất")+'</text>')
 for index,(label,unit,coef)in enumerate([('x','m',[0,vx]),('y','m',[y0,vy,-g/2]),('vₓ','m/s',[vx]),('vᵧ','m/s',[vy,-g])]):
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
 save(n,parts,diagramKind='four-time-graphs',sourceParameters={'vx':vx,'vy':vy,'g':g,'timeEnd':tf,'y0':y0},panels=panels)

values=json.loads((B/'parent-numbered-late-diagram-parameters.json').read_text('utf8'))
graph_panels(51,15,10,values['3.51']['time'])
r=values['3.61'];graph_panels(61,r['vx'],r['vy'],r['flightTime'],14)

def plot(parts,top,title,xlabel,ylabel,xrange,yrange,series,points=(),xticks=None,yticks=None):
 xlo,xhi=xrange;ylo,yhi=yrange
 def coord(x,y):return[76+(x-xlo)/(xhi-xlo)*235,218-(y-ylo)/(yhi-ylo)*145]
 parts +=[f'<g transform="translate(0 {top})">',f'<text x="18" y="25" font-weight="600">{html.escape(title)}</text>',f'<text x="100" y="55">{html.escape(ylabel)}</text>','<path d="M76 67 V225 H322" stroke="#64748b" fill="none"/>']
 if xticks is None:xticks=[xlo,(xlo+xhi)/2,xhi]
 if yticks is None:yticks=[ylo,(ylo+yhi)/2,yhi]
 for x,label in [(x,number(x))if not isinstance(x,tuple)else x for x in xticks]:
  px,_=coord(x,0);parts +=[f'<line x1="{px:.6f}" y1="67" x2="{px:.6f}" y2="225" stroke="#e2e8f0"/>',f'<text x="{px:.6f}" y="250" text-anchor="middle">{html.escape(label)}</text>']
 for y in yticks:
  _,py=coord(0,y);parts +=[f'<line x1="76" y1="{py:.6f}" x2="322" y2="{py:.6f}" stroke="#e2e8f0"/>',f'<text x="68" y="{py+6:.6f}" text-anchor="end">{number(y)}</text>']
 rows=[]
 for key,color,xy in series:
  screen=[coord(x,y)for x,y in xy];parts.append(f'<polyline data-series="{key}" points="'+' '.join(f'{x:.6f},{y:.6f}'for x,y in screen)+f'" fill="none" stroke="{color}" stroke-width="2.6"/>');rows.append({'key':key,'color':color,'worldPoints':np.asarray(xy,dtype=float).tolist()})
 for i,(x,y,color,label,dx,dy)in enumerate(points):
  px,py=coord(x,y);parts.append(f'<circle data-point="{i}" cx="{px:.6f}" cy="{py:.6f}" r="3.6" fill="{color}"/>')
  if label:parts.append(f'<text x="{px+dx:.6f}" y="{py+dy:.6f}" fill="{color}">{html.escape(label)}</text>')
 parts +=[f'<text x="180" y="283" text-anchor="middle">{html.escape(xlabel)}</text>','</g>']
 return {'title':title,'xRange':list(xrange),'yRange':list(yrange),'screenX':[76,311],'screenY':[218,73],'series':rows,'points':[[float(x),float(y),label]for x,y,color,label,dx,dy in points]}

tf=values['3.62']['time'];vy=math.sqrt(20**2-6**2);tt=np.linspace(0,tf,201);yy=45+vy*tt-.5*g*tt*tt;parts=head(760,'Bài 3.62: Hai hệ quy chiếu');panels=[]
panels.append(plot(parts,40,'Trong hệ mặt đất','x (m)','y (m)',[0,36],[0,70],[('ground-path',BLUE,np.column_stack((6*tt,yy)))],[(0,45,GREEN,'A',8,-8),(6*tf,0,RED,'B',-20,-10)],xticks=[0,18,36],yticks=[0,35,70]))
panels.append(plot(parts,345,'Trong hệ người chạy',"x′ (m)",'y′ (m)',[-1,1],[0,70],[('runner-path',PURPLE,np.column_stack((np.zeros_like(tt),yy)))],[(0,45,GREEN,'A',10,7),(0,0,RED,'B',10,-5)],xticks=[-1,0,1],yticks=[0,35,70]))
parts+=['<text x="18" y="675">A: Lúc phóng, B: Lúc bắt bóng</text>','<text x="18" y="703">Hệ người chạy: x′ luôn bằng 0</text>','<text x="18" y="731">Bóng lên rồi xuống theo phương đứng</text>'];save(62,parts,diagramKind='two-reference-frames',panels=panels,sourceParameters={'vx':6,'vy':vy,'height':45,'timeEnd':tf})

vx=25*math.cos(rad(53));vy=25*math.sin(rad(53));tf=2*vy/g;tt=np.linspace(0,tf,201);parts=head(445,'Bài 3.66: Hai khoảng cách');points=[(values['3.66']['distances'][0],10,GREEN,'A',8,-12),(values['3.66']['distances'][1],10,RED,'B',-20,-12)]
panels=[plot(parts,35,'Hai lần đi qua y = 10 m','x (m)','y (m)',[0,65],[0,24],[('trajectory',BLUE,np.column_stack((vx*tt,vy*tt-.5*g*tt**2))),('fire-height',PURPLE,[[0,10],[65,10]])],points,xticks=[0,30,60],yticks=[0,10,20])]
parts+=['<text x="18" y="365">A: Khoảng 8,80 m, nước đang lên</text>','<text x="18" y="393">B: Khoảng 52,5 m, nước đang xuống</text>'];save(66,parts,diagramKind='two-target-intersections',panels=panels,sourceParameters={'vx':vx,'vy':vy,'timeEnd':tf,'targetHeight':10})

for n,x,y,xrange,yrange,xlabel,ylabel in [(76,np.sin(2*np.deg2rad(values['3.76']['angles'])),np.array(values['3.76']['ranges']),[.55,1.05],[5.5,12], 'sin(2θ₀)','R (m)'),(77,np.array(values['3.77']['height']),np.array(values['3.77']['range'])**2,[0,13],[0,720],'h (m)','R² (m²)')]:
 slope=values[f'3.{n}']['slope'];intercept=values[f'3.{n}']['intercept'];lineX=np.linspace(max(xrange[0],min(x)-.02),min(xrange[1],max(x)+.02),101)
 parts=head(430,f'Bài 3.{n}: Khớp đường thẳng');points=[(float(a),float(b),RED,'',0,0)for a,b in zip(x,y)]
 panels=[plot(parts,40,'Dữ liệu và đường hồi quy',xlabel,ylabel,xrange,yrange,[('fit',BLUE,np.column_stack((lineX,slope*lineX+intercept)))],points)]
 parts+=['<text x="18" y="365">Chấm đỏ: Các số liệu dùng khớp</text>','<text x="18" y="393">Đường xanh: Bình phương tối thiểu</text>'];save(n,parts,diagramKind='least-squares-fit',panels=panels,sourceParameters={'x':x.tolist(),'y':y.tolist(),'slope':slope,'intercept':intercept})

r=values['3.81'];v0=r['airplaneSpeed'];t1=r['dropTime'];t2=r['poweredTime'];tf=r['totalTime'];ax=r['ax'];ay=r['ay'];times=np.unique(np.r_[np.linspace(0,tf,241),t1,t1+g*t1/ay]);tau=np.maximum(0,times-t1)
rocketx=v0*times+.5*ax*tau*tau;rockety=np.where(times<=t1,-.5*g*times*times,-.5*g*t1*t1-g*t1*tau+.5*ay*tau*tau)
planeX=v0*times;planeY=np.zeros_like(times)
states=[]
for name,t,phase in [('A: Thả',0,'drop'),('B−: Trước bật',t1,'before'),('B+: Sau bật',t1,'after'),('C: Ngang độ cao',tf,'cross')]:
 tau=max(0,t-t1);rv=[v0+ax*tau,-g*t]if phase in ['drop','before']else[v0+ax*tau,-g*t1+ay*tau];ra=[0,-g]if phase in ['drop','before']else[ax,ay]
 states.append({'label':name,'time':t,'rocketVelocity':rv,'rocketAcceleration':ra,'planeVelocity':[v0,0],'planeAcceleration':[0,0]})
parts=head(1750,'Bài 3.81: Quỹ đạo và vector')
panels=[plot(parts,45,'Quỹ đạo máy bay và tên lửa','x (m), tỉ lệ khác trục y','y (m), gốc tại máy bay',[0,4400],[-250,35],[('plane-path',BLUE,np.column_stack((planeX,planeY))),('rocket-path',RED,np.column_stack((rocketx,rockety)))],[(0,0,PURPLE,'A',8,-10),(v0*t1,r['engineOnY'],PURPLE,'B',10,-8),(rocketx[-1],0,PURPLE,'C',-20,-8)],xticks=[0,2000,4000],yticks=[-200,-100,0])]
parts+=['<text x="18" y="365">Xanh: Máy bay, đỏ: Tên lửa</text>','<text x="18" y="393">A: Thả, B: Bật động cơ, C: Gặp độ cao</text>']
# Vector diagrams use the SAME spatial scale for horizontal and vertical
# components, unlike the trajectory overview, whose axis scales are labelled.
vectorPanels=[]
for index,state in enumerate(states):
 top=425+index*310;origin=np.array([65.,160.]);vscale=.4;ascale=3.;vectors=[('plane-v',BLUE,np.array(state['planeVelocity'])*vscale),('rocket-v',RED,np.array(state['rocketVelocity'])*vscale),('rocket-a',GREEN,np.array(state['rocketAcceleration'])*ascale)]
 parts +=[f'<g transform="translate(0 {top})">',f'<text x="18" y="25" font-weight="600">{html.escape(state["label"])}</text>',f'<text x="18" y="53">t = {number(state["time"])} s</text>','<path d="M55 160 H320 M65 235 V70" stroke="#cbd5e1" fill="none"/>','<text x="320" y="182">x</text>','<text x="45" y="78">y</text>']
 for key,color,delta in vectors:
  end=origin+delta*[1,-1];parts.append(f'<line data-state="{index}" data-vector="{key}" x1="65" y1="160" x2="{end[0]:.6f}" y2="{end[1]:.6f}" stroke="{color}" stroke-width="2.7" marker-end="url(#m{color[1:]})"/>')
 parts+=['<text x="18" y="263">Xanh dương: v máy bay, đỏ: v tên lửa</text>','<text x="18" y="291">Xanh lá: a tên lửa, a máy bay = 0</text>','</g>']
 vectorPanels.append({'state':state,'originScreen':origin.tolist(),'velocityScale':vscale,'accelerationScale':ascale})
parts+=['<text x="18" y="1698">Mỗi ô vector dùng cùng tỉ lệ hai trục</text>','<text x="18" y="1726">v: 0,4 đơn vị/(m/s), a: 3 đơn vị/(m/s²)</text>']
save('81a',parts,diagramKind='rocket-path-and-state-vectors',panels=panels,vectorPanels=vectorPanels,sourceParameters=r)
for suffix,quantity,plane,rocket,yrange,yticks in [('b','x',planeX,rocketx,[0,4500],[0,2000,4000]),('c','y',planeY,rockety,[-250,40],[-200,-100,0])]:
 parts=head(460,f'Bài 3.81: Đồ thị {quantity}(t)')
 panels=[plot(parts,40,'Máy bay và tên lửa','t (s)',quantity+' (m)',[0,tf+.5],yrange,[('plane-'+quantity,BLUE,np.column_stack((times,plane))),('rocket-'+quantity,RED,np.column_stack((times,rocket)))],[],xticks=[(0,'0'),(t1,number(t1)),(tf,number(tf))],yticks=yticks)]
 parts+=['<text x="18" y="365">Xanh: Máy bay, đỏ: Tên lửa</text>',f'<text x="18" y="393">Bật động cơ: t ≈ {number(t1)} s</text>',f'<text x="18" y="421">Trở lại độ cao: t ≈ {number(tf)} s</text>'];save('81'+suffix,parts,diagramKind='rocket-time-graph',panels=panels,sourceParameters=r)
print('Reproduced',len(manifest),'separate solution diagrams.')
