"""Reproduce the six acoustic pipe modes as normalized amplitude envelopes."""
from pathlib import Path
import math,json,hashlib,html
ROOT=Path(__file__).resolve().parents[1]
B=ROOT/'qa/physics1-remaining/ch16/solution-regeneration';B.mkdir(parents=True,exist_ok=True)
A=ROOT/'docs/vat-ly-1/bai-giang/img/young-16';A.mkdir(exist_ok=True)
assets=[];checks=[]
def text(x,y,s,size=20,anchor='start',color='#2b2435'):
 return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}">{html.escape(s)}</text>'
for typ,indices,title in [('open',[1,2,3],'Ống hở hai đầu'),('stopped',[1,3,5],'Ống kín trái, hở phải')]:
 lines=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 660" role="img">',f'<title>{title}: Biên độ li độ và áp suất</title>','<rect width="360" height="660" fill="white"/>','<g font-family="Arial, sans-serif">',text(12,24,title,20),text(12,46,'Biên độ chuẩn hóa của hai đại lượng',18),'<path d="M14 65H42" stroke="#62409a" stroke-width="2.4"/>',text(48,70,'Li độ',20),'<path d="M158 65H186" stroke="#238994" stroke-width="2.4" stroke-dasharray="5 3"/>',text(192,70,'Áp suất',20)]
 data=[]
 for j,n in enumerate(indices):
  top=92+j*184;base=top+99;scale=62
  name='Âm cơ bản' if j==0 else 'Bồi âm thứ '+('nhất' if j==1 else 'hai')
  lines.append(text(12,top+14,f'{name} (n = {n})',20))
  def shape(x):
   phase=n*math.pi*x/1.2 if typ=='open' else n*math.pi*x/(2*1.2)
   return (abs(math.cos(phase)),abs(math.sin(phase))) if typ=='open' else (abs(math.sin(phase)),abs(math.cos(phase)))
  xs=[1.2*i/1200 for i in range(1201)];pairs=[shape(x) for x in xs]
  lines+=['<path d="M44 '+str(base)+'H338" stroke="#a39baa"/>',text(36,base+5,'0',20,'end'),text(36,base-scale+5,'1',20,'end')]
  for x,label in [(0,'0'),(.6,'0,600'),(1.2,'1,20')]:
   X=44+294*x/1.2;lines.append(f'<path d="M{X} {base-3}v6" stroke="#a39baa"/>');lines.append(text(X,base+26,label,20,'middle'))
  for q,color,dash in [(0,'#62409a',''),(1,'#238994',' stroke-dasharray="5 3"')]:
   path=' '.join(('M' if i==0 else 'L')+f'{44+294*x/1.2:.4f},{base-scale*p[q]:.4f}' for i,(x,p) in enumerate(zip(xs,pairs)))
   lines.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="2.4"{dash}/>')
  lines.append(text(338,base+48,'x (m)',20,'end'))
  checks.append({'type':typ,'harmonic':n,'left_displacement_amplitude':pairs[0][0],'left_pressure_amplitude':pairs[0][1],'right_displacement_amplitude':pairs[-1][0],'right_pressure_amplitude':pairs[-1][1],'points':len(xs),'passed':abs(pairs[-1][1])<1e-12 and (abs(pairs[0][1])<1e-12 if typ=='open' else abs(pairs[0][0])<1e-12)})
  assert checks[-1]['passed']
  data.append({'harmonic':n,'x_m':xs,'normalized_displacement_amplitude':[p[0] for p in pairs],'normalized_pressure_amplitude':[p[1] for p in pairs]})
 lines+=['</g></svg>'];p=A/f'solution-s16-23-{typ}.svg';p.write_text(''.join(lines),'utf-8')

 assets.append({'key':f'source-solution:S16.23-{typ}','output':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'generated_by':'generate_solution_figures.py','meaning':'Normalized amplitude envelopes, not simultaneous instantaneous pressure/displacement.','harmonics':indices,'original_source_crops_modified':False})
 (B/f'solution-figure-data-{typ}.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),'utf-8')

print('Generated two unchanged-geometry pipe-mode solution diagrams with readable labels.')
