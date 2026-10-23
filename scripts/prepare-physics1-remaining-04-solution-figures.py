"""Figures explicitly requested by the Newton exercise solutions.

These supplement, never replace, the exact original statement illustrations.
Run with Python-I. All numerical data are original measurements.
"""
from pathlib import Path
from math import isclose
import xml.sax.saxutils as xml
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-04'
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none','svg.hashsalt':'studyhub-newton-source-data'})
F=np.array([250,300,350,400,450,500.],dtype=float)
t=np.array([3.3,2.2,1.7,1.5,1.3,1.2])
a=16/t**2
mass,intercept=np.polyfit(a,F,1)
assert isclose(mass,25.58219287684,rel_tol=1e-10)
fig,ax=plt.subplots(figsize=(7.2,4.6),layout='constrained')
ax.scatter(a,F,s=50,color='#4338ca',label='Số đo')
grid=np.linspace(0,12,200)
ax.plot(grid,mass*grid+intercept,color='#0f766e',label='Đường thẳng khớp')
ax.set(xlabel='Gia tốc a (m/s²)',ylabel='Lực kéo F (N)',xlim=(0,12),ylim=(180,530))
ax.grid(alpha=.22);ax.legend()
fig.savefig(OUT/'parent-solution-4-53.svg',metadata={'Date':None})
plt.close(fig)
mass=np.array([8,11,15,20.])
distance=np.array([8.22,10.75,9.45,7.10])
time=np.array([2.8,3.2,3,2.6])
force=2*mass*distance/time**2
slope=np.dot(mass,force)/np.dot(mass,mass)
assert isclose(slope,2.099991978269365,rel_tol=1e-10)
fig,ax=plt.subplots(figsize=(7.2,4.6),layout='constrained')
ax.scatter(mass,force,s=50,color='#4338ca',label='Giá trị từ phép đo')
grid=np.linspace(0,22,200)
ax.plot(grid,slope*grid,color='#0f766e',label='Đường khớp qua gốc')
ax.set(xlabel='Tổng khối lượng m (kg)',ylabel='Độ lớn lực cản f (N)',xlim=(0,22),ylim=(0,48))
ax.grid(alpha=.22);ax.legend()
fig.savefig(OUT/'parent-solution-4-54.svg',metadata={'Date':None})
plt.close(fig)

def text(x,y,label,size=16,anchor='middle'):
 return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}">{xml.escape(label)}</text>'
def diagram(name,width,height,title,panels):
 items=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{xml.escape(title)}</title><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#4338ca"/></marker></defs><rect width="100%" height="100%" fill="#fff"/><g font-family="DejaVu Sans,Arial,sans-serif" fill="#172033">']
 for panel in panels:
  cx,cy,label,arrows=panel
  items.append(text(cx,cy-110,label,17))
  items.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="#172033"/>')
  for dx,dy,label in arrows:
   endx,endy=cx+dx,cy+dy
   items.append(f'<line x1="{cx}" y1="{cy}" x2="{endx}" y2="{endy}" stroke="#4338ca" stroke-width="2.5" marker-end="url(#arrow)"/>')
   if dx>0:tx,ty,anchor=endx+7,endy-8,'start'
   elif dx<0:tx,ty,anchor=endx-7,endy-8,'end'
   elif dy<0:tx,ty,anchor=endx+12,endy+8,'start'
   else:tx,ty,anchor=endx+12,endy-4,'start'
   items.append(text(tx,ty,label,16,anchor))
 items.append('</g></svg>')
 (OUT/name).write_text(''.join(items),encoding='utf-8')
diagram('parent-solution-4-37.svg',340,530,'Hai sơ đồ lực riêng cho hai thùng',[
 (145,140,'Thùng 4,00 kg',[(0,-70,'n₄'),(0,70,'4g'),(85,0,'T')]),
 (145,405,'Thùng 6,00 kg',[(0,-70,'n₆'),(0,70,'6g'),(90,0,'F'),(-65,0,'T')])
])
diagram('parent-solution-4-42.svg',310,270,'Sơ đồ lực của thang máy',[
 (130,140,'Thang máy và tải',[(0,-75,'T'),(0,75,'mg')])
])
diagram('parent-solution-4-46.svg',340,810,'Ba sơ đồ lực trong hệ hai khối và dây có khối lượng',[
 (145,140,'Khối trên 6,00 kg',[(0,-95,'200 N'),(0,60,'6g'),(0,100,'T trên')]),
 (145,410,'Dây 4,00 kg',[(0,-95,'T trên'),(0,60,'4g'),(0,100,'T dưới')]),
 (145,680,'Khối dưới 5,00 kg',[(0,-95,'T dưới'),(0,80,'5g')])
])
print('Saved five requested solution figures with independently checked data')
diagram('parent-solution-4-8.svg',340,530,'Sơ đồ lực của người trong câu a và gói hàng trong câu b',[
 (145,140,'Người đứng trên cân',[(0,-75,'N'),(0,75,'mg')]),
 (145,405,'Gói hàng treo bằng dây',[(0,-75,'T'),(0,75,'mₚg')])
])
diagram('parent-solution-4-26.svg',340,530,'Sơ đồ lực khối A trong hai trường hợp',[
 (145,140,'(a) Bàn không ma sát',[(0,-75,'n'),(0,75,'mₐg'),(80,0,'f')]),
 (145,405,'(b) Lực kéo cân bằng lực cản',[(0,-75,'n'),(0,75,'mₐg')])
])
diagram('parent-solution-4-27.svg',340,530,'Sơ đồ lực của hai kiện hàng tiếp xúc',[
 (145,140,'Kiện A',[(0,-75,'nₐ'),(0,75,'mₐg'),(90,0,'F'),(-70,0,'C')]),
 (145,405,'Kiện B',[(0,-75,'nᵦ'),(0,75,'mᵦg'),(75,0,'C')])
])
diagram('parent-solution-4-29.svg',340,530,'Sơ đồ lực quả cầu trong tàu chạy đều và tăng tốc',[
 (145,140,'(a) Tàu chạy thẳng đều',[(0,-75,'T'),(0,75,'mg')]),
 (145,405,'(b) Tàu tăng tốc về phía đông',[(35,-80,'T'),(0,75,'mg')])
])
diagram('parent-solution-4-30.svg',340,270,'Sơ đồ lực chiếc ghế trượt sang phải',[
 (145,140,'Ghế trượt trên sàn',[(0,-75,'n'),(0,75,'mg'),(64,48,'F'),(-75,0,'f')])
])
diagram('parent-solution-q4-30.svg',340,530,'Các lực ngoài tác dụng lên mỗi người khi kéo co',[
 (145,140,'Người A',[(0,-75,'nₐ'),(0,75,'mₐg'),(75,0,'T'),(-90,0,'fₐ')]),
 (145,405,'Người B',[(0,-75,'nᵦ'),(0,75,'mᵦg'),(-75,0,'T'),(90,0,'fᵦ')])
])
diagram('parent-solution-bridge.svg',340,1080,'Sơ đồ lực toàn chuỗi và từng mắt xích',[
 (145,140,'Toàn bộ chuỗi',[(0,-85,'F'),(0,85,'3mg')]),
 (145,405,'Mắt trên',[(0,-85,'F'),(0,55,'mg'),(0,100,'F₂₁')]),
 (145,675,'Mắt giữa',[(0,-85,'F₁₂'),(0,55,'mg'),(0,100,'F₃₂')]),
 (145,945,'Mắt dưới',[(0,-85,'F₂₃'),(0,85,'mg')])
])
print('Saved seven additional requested free-body diagrams')
for svg in OUT.glob('parent-solution-*.svg'):
 svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
