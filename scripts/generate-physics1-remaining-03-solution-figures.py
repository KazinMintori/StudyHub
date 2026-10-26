"""Reproduce seven reviewed native solution diagrams for chapter3.

Original textbook images are prepared separately and never changed here.
"""
from pathlib import Path
import json,hashlib,math
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'raw_materials/physics/translations/chapter-03'
assets=ROOT/'docs/vat-ly-1/bai-giang/img/young-03'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def svg(body):return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" width="100%"><rect width="360" height="250" fill="#fffdf7"/><defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#374151"/></marker></defs><g font-family="Segoe UI, sans-serif" font-size="20" fill="#17212b">'+body+'</g></svg>'
solutions=[]
def save(key,body,description,model):
 dst=assets/('solution-'+key+'.svg');dst.write_bytes(svg(body).encode('utf-8'))
 solutions.append(dict(key=key,publicFile=dst.relative_to(ROOT).as_posix(),sha256=sha(dst),purpose=description,model=model,generator="scripts/generate-physics1-remaining-03-solution-figures.py",minimumFontUnits=20))
body='<text x="24" y="32">Gia tốc ngược chiều vận tốc</text>'
for y,start,end,label in [(78,70,300,'v₁'),(135,70,220,'v₂'),(195,220,140,'Δv, a')]:
 tipbase=end-10 if end>start else end+10
 body+=f'<line x1="{start}" y1="{y}" x2="{end}" y2="{y}" stroke="#2458a6" stroke-width="4"/><polygon points="{end},{y} {tipbase},{y-6} {tipbase},{y+6}" fill="#2458a6"/><text x="24" y="{y+5}">{label}</text>'
body+='<text x="60" y="232">Cùng một trục, tốc độ giảm</text>'
save('s-q3-2-antiparallel',body,'Phác họa vận tốc sau ngắn hơn vận tốc trước, gia tốc và độ biến thiên vận tốc ngược chiều chuyển động.','v1=230 units; v2=150 units; dv=-80 units; same x axis; finite interval before stop.')
panels=[('x','x / X',lambda t:t,0,2.15),('y','y / Y',lambda t:t-.5*t*t,0,.55),('vx','vₓ / U',lambda t:1,0,1.2),('vy','vᵧ / V',lambda t:1-t,-1.2,1.2),('ax','aₓ / g',lambda t:0,-1.2,1.2),('ay','aᵧ / g',lambda t:-1,-1.2,1.2)]
for name,label,f,lo,hi in panels:
 X=lambda t:64+125*t
 Y=lambda val:205-(val-lo)/(hi-lo)*140
 zero=Y(0)
 body=f'<text x="24" y="30">{label}</text><line x1="64" y1="{zero:.3f}" x2="330" y2="{zero:.3f}" stroke="#374151" marker-end="url(#arrow)"/><line x1="64" y1="220" x2="64" y2="50" stroke="#374151" marker-end="url(#arrow)"/>'
 for t in [0,1,2]:
  body+=f'<line x1="{X(t)}" y1="{zero-4}" x2="{X(t)}" y2="{zero+4}" stroke="#374151"/><text x="{X(t)-5}" y="{zero+22}">{t}</text>'
 body+='<text x="300" y="244">t / T</text>'
 for val in sorted(set([lo if lo==-1.2 else 0,1 if hi>1 else .5])):
  if val==lo and val<0:val=-1
  if lo<=val<=hi:body+=f'<text x="24" y="{Y(val)+5:.3f}">{val:g}</text>'
 points=' '.join(f'{X(i/100):.3f},{Y(f(i/100)):.3f}' for i in range(201))
 body+=f'<polyline points="{points}" fill="none" stroke="#007c78" stroke-width="3.5"/>'
 if name in ['y','vy']:body+=f'<line x1="{X(1)}" y1="55" x2="{X(1)}" y2="210" stroke="#9a4c11" stroke-dasharray="4 4"/><text x="175" y="48">Đỉnh</text>'
 save('s-q3-7-'+name,body,'Đồ thị chuẩn hóa '+label+' theo t/T cho chuyển động ném xiên.',dict(domain=[0,2],sampleCount=201,ordinate=label,normalization='T=V/g, X=UT, Y=VT; U=v0 cos(alpha), V=v0 sin(alpha)',formula={'x':'tau','y':'tau-tau^2/2','vx':'1','vy':'1-tau','ax':'0','ay':'-1'}[name]))

(HERE/'parent-solution-image-manifest.json').write_text(json.dumps({'assets':solutions},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Generated',len(solutions),'reviewed solution diagrams with20unit text; original images unchanged.')
