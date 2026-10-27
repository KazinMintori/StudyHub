"""Answer plots from every actual source datum; original tables stay separate."""
from pathlib import Path
import hashlib,html,json
import numpy as np

ROOT=Path(__file__).resolve().parents[1];B=ROOT/'raw_materials/physics/translations/chapter-05';OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-05'
meta={row['key']:row for row in json.loads((B/'parent-numbered-late-solution-image-manifest.json').read_text(encoding='utf8'))['assets']}
BLUE='#2563eb';PURPLE='#7e22ce'
def fmt(v):return f'{v:g}'.replace('.',',')
def plot(panel):
 x0,x1,y0,y1=65.,330.,70.,270.;xmin,xmax=panel['xRange'];ymin,ymax=panel['yRange']
 X=lambda x:x0+(x-xmin)/(xmax-xmin)*(x1-x0)
 Y=lambda y:y1-(y-ymin)/(ymax-ymin)*(y1-y0)
 out=[f'<text x="180" y="28" text-anchor="middle" font-weight="600">{html.escape(panel["title"])}</text>',f'<text x="70" y="58">{html.escape(panel["ylabel"])}</text>']
 for y in panel['yTicks']:
  yy=Y(y);out.extend([f'<line x1="{x0}" y1="{yy:.6f}" x2="{x1}" y2="{yy:.6f}" stroke="#e2e8f0"/>',f'<text x="55" y="{yy+7:.6f}" text-anchor="end">{fmt(y)}</text>'])
 for x in panel['xTicks']:
  xx=X(x);out.extend([f'<line x1="{xx:.6f}" y1="{y0}" x2="{xx:.6f}" y2="{y1}" stroke="#e2e8f0"/>',f'<text x="{xx:.6f}" y="300" text-anchor="middle">{fmt(x)}</text>'])
 out.extend([f'<line class="x-axis" x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="#475569" stroke-width="2"/>',f'<line class="y-axis" x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="#475569" stroke-width="2"/>',f'<text x="197.5" y="330" text-anchor="middle">{html.escape(panel["xlabel"])}</text>'])
 points=[];lineData=[]
 for x in np.linspace(xmin,xmax,61):
  y=panel['intercept']+panel['slope']*x
  assert ymin-1e-9<=y<=ymax+1e-9
  points.append(f'{X(x):.6f},{Y(y):.6f}');lineData.append([float(x),float(y)])
 out.append(f'<polyline class="fit-line" points="{" ".join(points)}" fill="none" stroke="{PURPLE}" stroke-width="2.5"/>')
 drawn=[]
 for x,y in panel['data']:
  cx,cy=X(x),Y(y);out.append(f'<circle class="data-point" cx="{cx:.6f}" cy="{cy:.6f}" r="4.5" fill="{BLUE}" stroke="white" stroke-width="1.5"/>');drawn.append({'data':[float(x),float(y)],'svg':[cx,cy]})
 out.extend([f'<text x="18" y="370">Chấm: {html.escape(panel["pointsLegend"])}</text>',f'<text x="18" y="402">Đường: {html.escape(panel["fitLegend"])}</text>'])
 return out,{'plotRectangle':[x0,y0,x1,y1],'data':drawn,'fitSamples':lineData,**panel}
def draw(number,title,panels):
 key=f's5-{number}-graph';p=OUT/('solution-'+key+'.svg')
 height=450*len(panels);out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="{height}" viewBox="0 0 360 {height}" role="img" aria-label="{html.escape(title)}">',f'<title>{html.escape(title)}</title>',f'<rect width="360" height="{height}" fill="white" rx="10"/>','<g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#172033">'];records=[]
 for i,panel in enumerate(panels):
  content,record=plot(panel);records.append(record);out.append(f'<g class="plot-panel" transform="translate(0 {450*i})">');out.extend(content);out.append('</g>')
 out.extend(['</g></svg>']);p.write_bytes(('\n'.join(out)+'\n').encode('utf8'))
 meta[key].update(sha256=hashlib.sha256(p.read_bytes()).hexdigest(),minimumFontUnits=20,parentReviewedPlot=records,generator='generate-reviewed-110-111.py',description=title)

v=np.array([6.,8.,10.,12.,14.,16.]);N=np.array([8100.,7690.,7050.,6100.,5200.,4200.]);slope,intercept=np.polyfit(v*v,N,1)
draw(110,'Sáu lần đo lực ép tại đỉnh đồi và đường khớp tuyến tính',[
 {'title':'Ô tô tại đỉnh đồi','xlabel':'v² (m²/s²)','ylabel':'n (N)','xRange':[0,300],'yRange':[3000,9000],'xTicks':[0,100,200,300],'yTicks':[3000,5000,7000,9000],'data':[[float(x),float(y)] for x,y in zip(v*v,N)],'intercept':float(intercept),'slope':float(slope),'pointsLegend':'Sáu số đo','fitLegend':'Khớp tuyến tính'}
])
d=np.array([.25,.375,.5,.625,.75,.875,1.]);x=d*d;breaking=np.array([24.4,54.3,95.2,149.,212.,286.,372.]);safe=np.array([4.89,10.9,19.,29.7,42.3,57.4,74.3]);KB=float((x@breaking)/(x@x));KS=float((x@safe)/(x@x))
draw(111,'Kiểm tra cả độ bền đứt và tải an toàn theo bình phương đường kính',[
 {'title':'Độ bền đứt theo d²','xlabel':'d² (in²)','ylabel':'B (kN)','xRange':[0,1.05],'yRange':[0,400],'xTicks':[0,.25,.5,.75,1.],'yTicks':[0,100,200,300,400],'data':[[float(a),float(b)] for a,b in zip(x,breaking)],'intercept':0.,'slope':KB,'pointsLegend':'Bảy cỡ cáp','fitLegend':'Khớp qua gốc'},
 {'title':'Tải an toàn theo d²','xlabel':'d² (in²)','ylabel':'S (kN)','xRange':[0,1.05],'yRange':[0,80],'xTicks':[0,.25,.5,.75,1.],'yTicks':[0,20,40,60,80],'data':[[float(a),float(b)] for a,b in zip(x,safe)],'intercept':0.,'slope':KS,'pointsLegend':'Bảy cỡ cáp','fitLegend':'Khớp qua gốc'}
])
print('Rebuilt110with6actualsourcepoints,111with7breaking+7safeactualsourcepoints;183actualfitpolyline samples; no original table changed.')
