"""Draw the three source-correct collision states with a common velocity scale."""
from pathlib import Path
import html,math
ROOT=Path(__file__).resolve().parents[1]
vb=[2*math.cos(math.radians(19)),2*math.sin(math.radians(19))]
vc=[(1.8*3-1.8*vb[0])/1.2,-1.8*vb[1]/1.2]
states=[('Trước va chạm thứ nhất',[[4,0],[2,0],[0,0]]),('Sau va chạm thứ nhất',[[1,0],[3,0],[0,0]]),('Sau va chạm thứ hai',[[1,0],vb,vc])]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="360" height="980" viewBox="0 0 360 980" role="img" aria-label="Ba trạng thái và vector vận tốc của hệ ba quả cầu">','<title>Ba trạng thái và vector vận tốc của hệ ba quả cầu</title>','<rect width="360" height="980" rx="10" fill="white"/>','<defs><marker id="a" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#2563eb"/></marker></defs>','<g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#172033">']
for index,(title,velocities) in enumerate(states):
 top=index*300;parts.append(f'<g transform="translate(0 {top})"><text x="18" y="30" font-weight="600">{html.escape(title)}</text>')
 for row,(name,velocity) in enumerate(zip(['A','B','C'],velocities)):
  x,y=100,90+75*row;dx,dy=30*velocity[0],-30*velocity[1]
  parts +=[f'<text x="28" y="{y+6}">{name}</text>',f'<circle cx="{x}" cy="{y}" r="10" fill="#e2e8f0" stroke="#64748b"/>']
  if math.hypot(*velocity)>0:parts.append(f'<line data-state="{index}" data-object="{name}" x1="{x}" y1="{y}" x2="{x+dx:.6f}" y2="{y+dy:.6f}" stroke="#2563eb" stroke-width="2.8" marker-end="url(#a)"/>')
  else:parts.append(f'<text x="120" y="{y+6}">Đứng yên</text>')
 parts+=['<path d="M270 260 H311 M270 260 V225" stroke="#64748b" fill="none"/>','<text x="317" y="267">x</text>','<text x="252" y="220">y</text>','</g>']
parts+=['<text x="18" y="925">Mũi tên: Vector vận tốc, cùng tỉ lệ</text>','<text x="18" y="953">Vị trí các hàng chỉ để nhận diện vật</text>','</g></svg>']
(ROOT/'docs/vat-ly-1/bai-giang/img/young-08/solution-s8-bridge-three-states.svg').write_bytes(('\n'.join(parts)+'\n').encode('utf8'))
print('Reproduced the nine object states and seven actual velocity arrows.')
