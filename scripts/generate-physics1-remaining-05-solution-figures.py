from pathlib import Path
import math,json,hashlib
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'raw_materials/physics/translations/chapter-05';OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-05';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
BLUE='#2563eb';GREEN='#15803d';PURPLE='#7e22ce';INK='#172033'
def head(height,title):
 return [f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="{height}" viewBox="0 0 360 {height}" role="img" aria-label="{title}">',f'<title>{title}</title>',f'<rect width="360" height="{height}" rx="10" fill="#fff"/>','<defs>']+[f'<marker id="c{c[1:]}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7 Z" fill="{c}"/></marker>'for c in [BLUE,GREEN,PURPLE]]+['</defs>','<g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#172033">']
def arrow(p,v,color,label,offset):
 q=(p[0]+v[0],p[1]+v[1]);x,y=q[0]+offset[0],q[1]+offset[1]
 return f'<line x1="{p[0]:.5f}" y1="{p[1]:.5f}" x2="{q[0]:.5f}" y2="{q[1]:.5f}" stroke="{color}" stroke-width="3" marker-end="url(#c{color[1:]})"/><text x="{x:.5f}" y="{y:.5f}" fill="{color}">{label}</text>'
rows=[]
parts=head(360,'Các lực tác dụng lên người khi ghế nhẹ')
parts+=['<text x="180" y="30" text-anchor="middle" font-weight="600">Các lực tác dụng lên người</text>','<text x="180" y="58" text-anchor="middle">Trường hợp ghế nhẹ</text>','<rect x="112" y="146" width="136" height="24" rx="8" fill="#f1f5f9" stroke="#64748b"/>',arrow((140,146),(0,-60),BLUE,'T',(-24,30)),arrow((220,170),(0,-60),GREEN,'n',(9,-6)),arrow((180,158),(0,120),PURPLE,'mg',(10,2)),'<text x="24" y="322">T + n = mg</text>','<text x="24" y="350">T = n = mg / 2</text>','</g></svg>']
p=OUT/'solution-s-q5-1-man-fbd.svg';p.write_bytes(('\n'.join(parts)+'\n').encode('utf-8'))
rows.append({'key':'s-q5-1-man-fbd','file':'proposed-assets/'+p.name,'sha256':sha(p),'purpose':'Giản đồ ba lực tác dụng lên người khi bỏ qua trọng lượng ghế.','minimumFontUnits':20,'geometry':{'forceStarts':[[140,146],[220,170],[180,158]],'forceVectors':[[0,-60],[0,-60],[0,120]],'forceLabels':['T','n','mg'],'normalAndTensionSumEqualsWeight':True}})
parts=head(860,'Các lực ở hai biên quay của vật trong hình nón')
geometry=[];beta=math.radians(35);mu=.55;s=math.sin(beta);c=math.cos(beta)
for index,sign in enumerate([1,-1]):
 # Sign+1: friction up/outward. Sign-1: friction down/inward.
 weight=110 if sign==1 else 80;normal=weight/(c+sign*mu*s);friction=mu*normal
 origin=(150.,170.)if sign==1 else(100.,226.)
 nv=(normal*s,-normal*c);fv=(-sign*friction*c,-sign*friction*s);wv=(0.,weight)
 title='Biên quay chậm'if sign==1 else'Biên quay nhanh';subtitle='Chu kỳ lớn nhất'if sign==1 else'Chu kỳ nhỏ nhất'
 parts += [f'<g transform="translate(0 {430*index})">',f'<text x="180" y="28" text-anchor="middle" font-weight="600">{title}</text>',f'<text x="180" y="56" text-anchor="middle">{subtitle}</text>']
 a=(origin[0]-75*c,origin[1]-75*s);z=(origin[0]+150*c,origin[1]+150*s)
 parts += [f'<line x1="{a[0]:.5f}" y1="{a[1]:.5f}" x2="{z[0]:.5f}" y2="{z[1]:.5f}" stroke="#94a3b8" stroke-width="2"/>',f'<circle cx="{origin[0]}" cy="{origin[1]}" r="6" fill="#fef3c7" stroke="#d97706"/>',arrow(origin,nv,BLUE,'n',(7,-3)),arrow(origin,fv,GREEN,'fₛ',(-30,-9)if sign==1 else(7,20)),arrow(origin,wv,PURPLE,'mg',(-35,17))]
 pa=(origin[0]-40,origin[1]);pb=(origin[0]-40*c,origin[1]-40*s)
 parts += [f'<path d="M{pa[0]:.5f} {pa[1]:.5f} A40 40 0 0 1 {pb[0]:.5f} {pb[1]:.5f}" fill="none" stroke="#64748b"/>',f'<line x1="{origin[0]-48}" y1="{origin[1]}" x2="{origin[0]-5}" y2="{origin[1]}" stroke="#94a3b8" stroke-dasharray="3 3"/>',f'<text x="{origin[0]-62}" y="{origin[1]-5}">β</text>','<path d="M282 322 H323 M282 322 V281" fill="none" stroke="#64748b" stroke-width="1.5"/>','<text x="328" y="328">x</text>','<text x="274" y="275">y</text>','<line x1="24" y1="347" x2="336" y2="347" stroke="#d1d5db"/>','<text x="24" y="372">n: Phản lực pháp tuyến</text>','<text x="24" y="398">fₛ: Ma sát nghỉ</text>','<text x="24" y="424">mg: Trọng lực</text>','</g>']
 geometry.append({'signUpSlope':sign,'origin':origin,'normalVector':nv,'frictionVector':fv,'weightVector':wv,'normalUnit':[s,-c],'downSlopeUnit':[c,s],'betaIllustrationDegrees':35,'illustrativeFrictionCoefficient':mu,'forceScaleWeight':weight,'note':'Illustration parameters determine only drawing geometry. No extra numerical exercise is stated to learners.'})
parts+=['</g></svg>'];p=OUT/'solution-s-bridge-cone-fbd.svg';p.write_bytes(('\n'.join(parts)+'\n').encode('utf-8'))
rows.append({'key':'s-bridge-cone-fbd','file':'proposed-assets/'+p.name,'sha256':sha(p),'purpose':'Phản lực, trọng lực và ma sát ở hai biên trượt hữu hạn, với x hướng vào trục và y hướng lên.','minimumFontUnits':20,'panels':geometry})
print('Reproduced',len(rows),'separate solution diagrams.')
