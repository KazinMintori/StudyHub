"""Force diagrams with actual inertial-frame vectors; originals remain untouched."""
from pathlib import Path
import hashlib,html,json,math
import numpy as np

ROOT=Path(__file__).resolve().parents[1];B=ROOT/'raw_materials/physics/translations/chapter-05';OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-05'
meta={row['key']:row for row in json.loads((B/'parent-numbered-late-solution-image-manifest.json').read_text(encoding='utf8'))['assets']}
BLUE='#2563eb';GREEN='#15803d';RED='#b91c1c';COLORS=[BLUE,GREEN,RED]
rad=math.radians
def label(text,x,y,color):
 a=text.split('_',1)
 content=html.escape(a[0])+(f'<tspan dy="5" font-size="20">{html.escape(a[1])}</tspan>' if len(a)>1 else '')
 return f'<text x="{x:.6f}" y="{y:.6f}" fill="{color}" font-size="24">{content}</text>'
def force(origin,delta,text,xy,color):return {'origin':list(origin),'delta':list(delta),'label':text,'labelPosition':list(xy),'color':color}
def draw(number,title,panels):
 key=f's5-{number}-fbd';path=OUT/('solution-'+key+'.svg')
 height=440*len(panels);s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="{height}" viewBox="0 0 360 {height}" role="img" aria-label="{html.escape(title)}">',f'<title>{html.escape(title)}</title>',f'<rect width="360" height="{height}" fill="white" rx="10"/>','<defs>']
 for color in COLORS:s.append(f'<marker id="a{color[1:]}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="{color}"/></marker>')
 s+=['</defs>','<g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#172033">']
 for i,p in enumerate(panels):
  s.extend([f'<g transform="translate(0 {440*i})">',f'<text x="180" y="28" text-anchor="middle" font-weight="600">{html.escape(p["title"])}</text>'])
  s.extend(p.get('decoration',[]))
  if 'polygon' in p:
   points=' '.join(f'{x:.6f},{y:.6f}' for x,y in p['polygon']);s.append(f'<polygon points="{points}" fill="#e2e8f0" stroke="#64748b" stroke-width="2"/>')
  else:s.append(f'<circle cx="{p["center"][0]}" cy="{p["center"][1]}" r="10" fill="#e2e8f0" stroke="#64748b"/>')
  for f in p['forces']:
   x,y=f['origin'];dx,dy=f['delta'];c=f['color'];s.append(f'<line x1="{x:.6f}" y1="{y:.6f}" x2="{x+dx:.6f}" y2="{y+dy:.6f}" stroke="{c}" stroke-width="3" marker-end="url(#a{c[1:]})"/>');s.append(label(f['label'],*f['labelPosition'],c))
  s.append('<line x1="18" y1="325" x2="342" y2="325" stroke="#cbd5e1"/>')
  for j,line in enumerate(p['legend']):s.append(f'<text x="18" y="{355+28*j}">{html.escape(line)}</text>')
  s.append('</g>')
 s+=['</g></svg>'];path.write_bytes(('\n'.join(s)+'\n').encode('utf8'))
 meta[key].update(sha256=hashlib.sha256(path.read_bytes()).hexdigest(),minimumFontUnits=20,parentReviewedGeometry=panels,generator='generate-reviewed-097-099-103.py',description=title)
def rectangle(center,t,n):return [list(center+sx*35*t+sy*25*n) for sx,sy in [(-1,-1),(1,-1),(1,1),(-1,1)]]

theta=rad(36.9);t=np.array([math.cos(theta),-math.sin(theta)]);n=np.array([-math.sin(theta),-math.cos(theta)]);center=np.array([180.,180.])
mu=.6*math.tan(theta);w=40;normalS=4*w*math.cos(theta);normalB=w*math.cos(theta)
lower=center-25*n-25*mu*.75*t;upper=center+25*n
draw(97,'Năm lực thật tác dụng lên khối A',[
 {'title':'Khối A trượt đều xuống dốc','center':list(center),'polygon':rectangle(center,t,n),'forces':[
 force(center,[0,3*w],'3w',[190,306],RED),
 force(lower,normalS*n,'n_S',[65,99],BLUE),
 force(upper,-normalB*n,'n_B',[207,214],BLUE),
 force(lower,mu*normalS*t,'f_S',[245,165],GREEN),
 force(upper,mu*normalB*t,'f_B',[187,138],GREEN)],
 'legend':['nS, fS: Lực do mặt dốc tác dụng','nB, fB: Lực do tấm ván tác dụng','Trọng lực 3w thẳng đứng xuống']}
])

ratio=(2*math.pi*.6)**2*2.5/9.8;c=[220,180];w=40
draw(99,'Ba lực trên người chơi khi sàn đã hạ',[
 {'title':'Người quay cùng hình trụ','center':c,'forces':[
 force(c,[-ratio*w,0],'n',[95,163],BLUE),
 force(c,[0,-w],'f_s',[256,138],GREEN),
 force(c,[0,w],'mg',[256,238],RED)],
 'decoration':['<line x1="245" y1="80" x2="245" y2="285" stroke="#64748b" stroke-width="4"/>','<line x1="43" y1="80" x2="43" y2="285" stroke="#94a3b8" stroke-dasharray="5 5"/>','<text x="43" y="60" text-anchor="middle">Trục</text>','<text x="299" y="60" text-anchor="middle">Thành trụ</text>'],
 'legend':['n hướng vào trục quay','Ma sát nghỉ đỡ trọng lực','fs = mg, n = mω²R']}
])

scale=4;wA=wB=25;mu=.35;T1=mu*wA;NB=wB*math.cos(theta);fr=mu*NB;T2=T1+fr+wB*math.sin(theta)
centerA=np.array([180.,170.]);centerB=np.array([180.,180.]);floor=centerB-25*n+25*mu*t
draw(103,'Giản đồ lực riêng trên hai khối A và B',[
 {'title':'Khối A trên bàn ngang','center':list(centerA),'forces':[
 force(centerA,[0,-scale*wA],'n_A',[138,65],BLUE),force(centerA,[0,scale*wA],'w_A',[192,286],RED),force(centerA,[scale*T1,0],'T_1',[225,164],BLUE),force(centerA,[-scale*T1,0],'f_A',[98,164],GREEN)],
 'legend':['T₁ kéo sang phải, ma sát cản sang trái','Phản lực nA cân bằng trọng lực wA','T₁ = fA = 8,75 N']},
 {'title':'Khối B chuyển động lên dốc','center':list(centerB),'polygon':rectangle(centerB,t,n),'forces':[
 force(centerB,[0,scale*wB],'w_B',[192,301],RED),force(floor,scale*NB*n,'n_B',[106,119],BLUE),force(centerB+35*t,scale*T2*t,'T_2',[306,77],BLUE),force(centerB-35*t,-scale*T1*t,'T_1',[83,229],BLUE),force(floor,-scale*fr*t,'f_B',[211,237],GREEN)],
 'legend':['T₂ kéo lên dốc','T₁ và ma sát fB cùng hướng xuống dốc','Trọng lực wB hướng xuống']}
])
print('Rebuilt3diagrams:5actualforces97,3actualforces99,9actualforces103. Base labels24/subscripts20; original PDFfigures untouched.')
