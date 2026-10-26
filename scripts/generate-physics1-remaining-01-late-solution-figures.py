from pathlib import Path
import math,json,hashlib,html,textwrap
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-01'
BLUE='#2563eb';GREEN='#15803d';ORANGE='#c2410c';INK='#172033'
def v(m,d):return[m*math.cos(math.radians(d)),m*math.sin(math.radians(d))]
def plus(a,b):return[a[0]+b[0],a[1]+b[1]]
def seq(ds):
 pts=[[0.,0.]]
 for d in ds:pts.append(plus(pts[-1],d))
 return pts
def closed(ds):
 pts=seq(ds);return pts+[[0.,0.]]
def regular(n,ds,closedRoute=False):
 points=closed(ds)if closedRoute else seq(ds)
 # Shared start/end have a single label at the start.
 names=[str(i)for i in range(len(points))]
 if closedRoute:names[-1]=''
 segments=[(i,i+1,BLUE if i<len(ds)else ORANGE)for i in range(len(points)-1)]
 if not closedRoute:segments.append((0,len(points)-1,ORANGE))
 return {'n':n,'title':'Giản đồ chuyển dời','points':points,'names':names,'segments':segments,'legend':['Số: Các điểm trên đường đi','Xanh: Các chặng đã cho','Cam: Vector cần xác định'],'axes':['Đông','Bắc']}
drawings=[]
drawings.append(regular(57,[v(180,180),v(210,315),v(280,60)],True))
drawings.append(regular(60,[[2,0],v(3.5,-45),[5.8-2-3.5/math.sqrt(2),3.5/math.sqrt(2)]]))
drawings[-1]['segments']=[(0,1,BLUE),(1,2,BLUE),(2,3,ORANGE),(0,3,GREEN)]
drawings[-1]['legend']=['0: Xuất phát, 3: Điểm đến','Xanh dương: Hai chặng đầu','Cam: Chặng thứ ba','Xanh lá: Tổng chuyển dời']
drawings.append(regular(62,[v(147,5),v(106,-77),v(166,-145)],True))
drawings[-1]['legend']=['0: Lincoln','1: Clarinda','2: St. Joseph','3: Manhattan','Cam: Chặng bay trở về']
drawings.append(regular(64,[v(40,45),v(80,120),v(50,-90)],True))
drawings[-1]['segments'].append((0,3,GREEN));drawings[-1]['legend']=['0: Nơi trú ẩn','Xanh dương: Ba chặng đầu','Xanh lá: Vector tổng','Cam: Chặng trở về']
drawings.append(regular(69,[v(825,-90),v(1250,120),v(1000,32)],True))
drawings[-1]['legend']=['0: Cây sồi, 3: Kho báu','Xanh: Đường tới kho báu','Cam: Đường thẳng trở về']
drawings.append({'n':72,'title':'Ricardo và Jane','points':[[0,0],v(26,150),v(16,210)],'names':['O','R','J'],'segments':[(0,1,BLUE),(0,2,GREEN),(1,2,ORANGE)],'legend':['O: Gốc tại cây','R: Ricardo, J: Jane','Cam: Từ Ricardo tới Jane'],'axes':['Đông','Bắc']})
drawings.append({'n':79,'title':'Hai vector khi c = 0','points':[[0,0],[3,-2],[0,2]],'names':['O','A','B'],'segments':[(0,1,BLUE),(0,2,GREEN)],'legend':['A = (a, −b), B = (0, d)','Hai trục trong hình: x, z','A × B: Hướng −y','−y: Ra khỏi mặt phẳng','Độ dài chỉ để minh họa'],'axes':['x','z'],'illustrationOnly':True})
drawings.append({'n':89,'title':'Vị trí trong Hệ Mặt Trời','points':[[0,0],[.3182,.9329],[1.3087,-.4423]],'names':['S','E','M'],'segments':[(0,1,BLUE),(0,2,GREEN),(1,2,ORANGE)],'legend':['S: Mặt Trời','E: Trái Đất, M: Sao Hỏa','Hình chiếu lên mặt phẳng xy','z(E) = 0 AU','z(M) = −0,0414 AU'],'axes':['x','y'],'sourceZ':[0,0,-.0414]})
drawings.append({'n':90,'title':'Đường chạy và đường ném','points':[[1,-5],[10,-5],[10,6],[4,10],[16,28],[0,-7],[0,0]],'names':['P₀','P₁','P₂','P₃','P₄','Q','O'],'segments':[(0,1,BLUE),(1,2,BLUE),(2,3,BLUE),(3,4,BLUE),(5,4,ORANGE)],'legend':['O: Gốc tại bóng ban đầu','P₀: Vị trí người nhận lúc đầu','P₁–P₄: Bốn chặng chạy','Q: Tiền vệ sau khi lùi','Cam: Vector ném Q tới P₄','Đơn vị tọa độ: Yard'],'axes':['Phải','Dọc sân']})
drawings.append({'n':91,'title':'Tam giác ba ngôi sao','points':[[0,0],[77,0],v(138,25.6)],'names':['S','M','A'],'segments':[(0,1,BLUE),(0,2,GREEN),(1,2,ORANGE)],'legend':['S: Mặt Trời, M: Merak','A: Alkaid','SM = 77 ly, SA = 138 ly','Góc tại S: 25,6°','Góc tại M: Khoảng 128,5°'],'axes':None})
manifest=[]
for d in drawings:
 pts=d['points'];xlo=min(p[0]for p in pts);xhi=max(p[0]for p in pts);ylo=min(p[1]for p in pts);yhi=max(p[1]for p in pts)
 scale=min(255/max(xhi-xlo,1e-8),205/max(yhi-ylo,1e-8));cx=(xhi+xlo)/2;cy=(yhi+ylo)/2
 screen=lambda p:[180+(p[0]-cx)*scale,155-(p[1]-cy)*scale]
 height=352+28*len(d['legend']);parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="{height}" viewBox="0 0 360 {height}" role="img" aria-label="{html.escape(d["title"])}">',f'<title>{html.escape(d["title"])}</title>',f'<rect width="360" height="{height}" fill="white" rx="10"/>','<defs>']
 for c in [BLUE,GREEN,ORANGE]:parts.append(f'<marker id="m{c[1:]}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7 Z" fill="{c}"/></marker>')
 parts+=['</defs>','<g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#172033">',f'<text x="180" y="29" text-anchor="middle" font-weight="600">{html.escape(d["title"])}</text>']
 actualSegments=[]
 for i,j,color in d['segments']:
  a=screen(pts[i]);b=screen(pts[j]);parts.append(f'<line data-from="{i}" data-to="{j}" x1="{a[0]:.6f}" y1="{a[1]:.6f}" x2="{b[0]:.6f}" y2="{b[1]:.6f}" stroke="{color}" stroke-width="2.5" marker-end="url(#m{color[1:]})"/>');actualSegments.append({'from':i,'to':j,'color':color})
 boxes=[]
 for idx,(p,name)in enumerate(zip(pts,d['names'])):
  if not name:continue
  x,y=screen(p);parts.append(f'<circle cx="{x:.6f}" cy="{y:.6f}" r="3.5" fill="{INK}"/>')
  width=12*len(name)
  for dx,dy in [(9,-10),(9,25),(-width-9,-10),(-width-9,25),(12,8),(-width-12,8),(0,-22),(0,36)]:
   box=(x+dx,y+dy-20,x+dx+width,y+dy+5)
   if box[0]<8 or box[2]>352 or box[1]<35 or box[3]>284:continue
   if any(not(box[2]+4<q[0]or q[2]+4<box[0]or box[3]+3<q[1]or q[3]+3<box[1])for q in boxes):continue
   boxes.append(box);parts.append(f'<text x="{x+dx:.6f}" y="{y+dy:.6f}" data-point="{idx}">{html.escape(name)}</text>');break
  else:raise AssertionError(('No uncluttered label position',d['n'],name))
 if d['axes']:
  horizontal,vertical=d['axes'];parts+=['<path d="M260 310 H305 M260 310 V282" stroke="#64748b" fill="none"/>',f'<text x="310" y="316">{html.escape(horizontal)}</text>',f'<text x="247" y="276">{html.escape(vertical)}</text>']
 for i,line in enumerate(d['legend']):parts.append(f'<text x="18" y="{350+28*i}">{html.escape(line)}</text>')
 parts+=['</g></svg>'];path=OUT/f'solution-p1-{d["n"]}.svg';path.write_bytes(('\n'.join(parts)+'\n').encode('utf8'))
 manifest.append({'key':f'S1-{d["n"]}','file':'proposed-assets/'+path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'minimumFontUnits':20,'generator':'generate-reviewed-diagrams.py','sourceUnit':f'1.{d["n"]}','worldPoints':pts,'pointNames':d['names'],'segments':actualSegments,'screenMapping':{'scale':scale,'centerWorld':[cx,cy],'centerScreen':[180,155],'flipY':True},'scope':d.get('illustrationOnly',False)and'symbolicillustrationonly'or'same-scalephysicalvectors','sourceZ':d.get('sourceZ')})
print('Reproduced',len(manifest),'separate solution diagrams.')
