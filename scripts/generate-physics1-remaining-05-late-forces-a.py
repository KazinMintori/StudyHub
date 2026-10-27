from pathlib import Path
import json,math,hashlib,html
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'raw_materials/physics/translations/chapter-05';OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-05'
meta={row['key']:row for row in json.loads((B/'parent-numbered-late-solution-image-manifest.json').read_text(encoding='utf8'))['assets']}
assert isinstance(meta,dict)
BLUE='#2563eb';GREEN='#15803d';PURPLE='#7e22ce';rows=[]
def arrow(origin,delta,color,label,offset):
 end=[origin[0]+delta[0],origin[1]+delta[1]]
 return f'<line x1="{origin[0]:.6f}" y1="{origin[1]:.6f}" x2="{end[0]:.6f}" y2="{end[1]:.6f}" stroke="{color}" stroke-width="3" marker-end="url(#m{color[1:]})"/><text x="{end[0]+offset[0]:.6f}" y="{end[1]+offset[1]:.6f}" fill="{color}">{html.escape(label)}</text>'
def draw(key,title,panels):
 height=len(panels)*390;parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="{height}" viewBox="0 0 360 {height}" role="img" aria-label="{html.escape(title)}">',f'<title>{html.escape(title)}</title>',f'<rect width="360" height="{height}" rx="10" fill="white"/>','<defs>']
 for c in [BLUE,GREEN,PURPLE]:parts.append(f'<marker id="m{c[1:]}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="{c}"/></marker>')
 parts+=['</defs>','<g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#172033">']
 for i,p in enumerate(panels):
  parts +=[f'<g transform="translate(0 {390*i})">',f'<text x="180" y="28" text-anchor="middle" font-weight="600">{html.escape(p["title"])}</text>','<circle cx="180" cy="160" r="10" fill="#e2e8f0" stroke="#64748b"/>']
  for force in p['forces']:parts.append(arrow(force['origin'],force['delta'],force['color'],force['label'],force['offset']))
  parts+=['<line x1="20" y1="315" x2="340" y2="315" stroke="#cbd5e1"/>']
  for j,line in enumerate(p['legend']):parts.append(f'<text x="18" y="{343+27*j}">{html.escape(line)}</text>')
  parts.append('</g>')
 parts+=['</g></svg>'];path=OUT/('solution-'+key+'.svg');path.write_bytes(('\n'.join(parts)+'\n').encode('utf8'))
 meta[key]={**meta[key],'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'minimumFontUnits':20,'parentReviewedGeometry':panels,'generator':'generate-reviewed-force-subset.py'};rows.append(key)
def F(delta,color,label,offset=(10,0),origin=(180,160)):return{'origin':list(origin),'delta':list(delta),'color':color,'label':label,'offset':list(offset)}
draw('s5-62-fbd','Lực trên từng bộ phận của hệ ròng rọc',[
 {'title':'Ròng rọc dưới','forces':[F([0,-60],BLUE,'T',(-25,0),(135,160)),F([0,-60],BLUE,'T',(10,0),(225,160)),F([0,120],PURPLE,'T₂')],'legend':['Hai lực T kéo lên, T₂ kéo xuống','2T = T₂ = w']},
 {'title':'Ròng rọc trên','forces':[F([0,60],BLUE,'T',(-25,20),(135,160)),F([0,60],BLUE,'T',(10,20),(225,160)),F([0,-120],GREEN,'T₁',(-36,20))],'legend':['Hai nhánh dây kéo ròng rọc xuống','T₁ = 2T = w']},
 {'title':'Vật nặng','forces':[F([0,-90],GREEN,'T₂',(-35,0)),F([0,90],PURPLE,'w')],'legend':['T₂ kéo lên, trọng lượng kéo xuống','T₂ = w, F = T = w / 2']}
])
weight=110.;normal=[-weight*math.tan(math.radians(35)),-weight];tension=[-normal[0],0]
draw('s5-64-fbd','Ba lực trên quả cầu giữ bằng dây ngang',[
 {'title':'Quả cầu trên mặt dốc nhẵn','forces':[F(normal,BLUE,'n',(-25,25)),F(tension,GREEN,'T',(5,-10)),F([0,weight],PURPLE,'mg')],'legend':['n: Lên trái, T: Sang phải, mg: Xuống','T − n sin 35° = 0']}
])
draw('s5-67-fbd','Lực tác dụng lên người khi hít xà',[
 {'title':'Gia tốc hướng lên','forces':[F([0,-100*(1+1.2/9.8)],GREEN,'F',(-25,20)),F([0,100],PURPLE,'w')],'legend':['Lực nâng lớn hơn trọng lượng','F − w = ma, F ≈ 763 N']},
 {'title':'Đi lên nhưng gia tốc hướng xuống','forces':[F([0,-100*(1-1.2/9.8)],GREEN,'F',(-25,0)),F([0,100],PURPLE,'w')],'legend':['Lực nâng nhỏ hơn trọng lượng','F − w = −ma, F ≈ 597 N']}
])
print('Rebuiltactualforcearrowsfor',rows,'withoutchanginganysourcePNG.')
