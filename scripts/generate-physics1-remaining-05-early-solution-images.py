"""Reproduce reviewed chapter5 early solution images from canonical geometry."""
from pathlib import Path
import hashlib,html,json,math
ROOT=Path(__file__).resolve().parents[1]
B=ROOT
meta=json.loads((ROOT/'raw_materials/physics/translations/chapter-05/parent-numbered-early-solution-image-manifest.json').read_text(encoding='utf8'))
rows={r['key']:{**r,'output':r['publicFile']} for r in meta['assets']}
BLUE='#2563eb';RED='#b91c1c'
def draw(number, title, panels):
    key = f'solution-image:s5.{number}-fbd'
    row = rows.get(key, dict(key=key, output=f'docs/vat-ly-1/bai-giang/img/young-05/solution-s5-{number}-fbd.svg'))
    p = B / row['output']
    height = 390 * len(panels)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="{height}" viewBox="0 0 360 {height}" role="img" aria-label="{html.escape(title)}">',
         f'<title>{html.escape(title)}</title>',
         f'<rect width="360" height="{height}" fill="white" rx="10"/>', '<defs>']
    for color in [BLUE, RED]:
        s.append(f'<marker id="a{color[1:]}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="{color}"/></marker>')
    s += ['</defs>', '<g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#172033">']
    for i, panel in enumerate(panels):
        s += [f'<g transform="translate(0 {390*i})">',
              f'<text x="180" y="28" text-anchor="middle" font-weight="600">{html.escape(panel["title"])}</text>']
        for x, y, r in panel['bodies']:
            s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#e2e8f0" stroke="#64748b" stroke-width="2"/>')
        for f in panel['forces']:
            x, y = f['origin']
            dx, dy = f['delta']
            c = f['color']
            lx, ly = f['labelPosition']
            parts = f['label'].split('_', 1)
            label = html.escape(parts[0])
            if len(parts) > 1:
                label += f'<tspan dy="5" font-style="normal" font-size="20">{html.escape(parts[1])}</tspan>'
            s += [f'<line x1="{x:.6f}" y1="{y:.6f}" x2="{x+dx:.6f}" y2="{y+dy:.6f}" stroke="{c}" stroke-width="3" marker-end="url(#a{c[1:]})"/>',
                  f'<text x="{lx}" y="{ly}" fill="{c}" font-size="24" font-style="italic">{label}</text>']
        s.append('<line x1="18" y1="315" x2="342" y2="315" stroke="#cbd5e1"/>')
        for j, line in enumerate(panel['legend']):
            s.append(f'<text x="18" y="{344+28*j}">{html.escape(line)}</text>')
        s.append('</g>')
    s += ['</g></svg>']
    p.write_bytes(('\n'.join(s) + '\n').encode('utf8'))
    row.update(sha256=hashlib.sha256(p.read_bytes()).hexdigest(), title=title,
               minimumFontUnits=20, parentReviewedGeometry=panels,
               generator=Path(__file__).name)
    if key not in rows:
        meta['assets'].append(row)
        rows[key] = row

for row in meta['assets']:
    if 'parentReviewedGeometry' in row:
        number=int(row['key'].split('s5.')[1].split('-')[0])
        draw(number,row['title'],row['parentReviewedGeometry'])
name=rows['solution-image:s5.24-graph']['publicFile']
title='Đồ thị ma sát khi tổng trọng lượng tăng lên 270 N'
x=lambda p:60+244*p/300
y=lambda f:335-250*f/180
static=[[0,0],[150,150]]
drop=[[150,150],[150,100]]
kinetic=[[150,100],[300,100]]
s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="480" viewBox="0 0 360 480" role="img" aria-label="{title}">',
   f'<title>{title}</title>','<rect width="360" height="480" rx="10" fill="white"/>',
   '<g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#172033">',
   '<text x="180" y="28" text-anchor="middle" font-weight="600">Tổng trọng lượng 270 N</text>',
   '<text x="18" y="60">f (N)</text>']
for f in [50,100,150]:
    s += [f'<line x1="60" y1="{y(f):.6f}" x2="304" y2="{y(f):.6f}" stroke="#cbd5e1"/>',
          f'<text x="52" y="{y(f)+7:.6f}" text-anchor="end">{f}</text>']
for p in [0,75,150,225,300]:
    s += [f'<line x1="{x(p):.6f}" y1="335" x2="{x(p):.6f}" y2="342" stroke="#334155"/>',
          f'<text x="{x(p):.6f}" y="369" text-anchor="middle">{p}</text>']
s += ['<path d="M60 75V335H320" fill="none" stroke="#334155" stroke-width="2"/>',
      '<text x="270" y="406">P (N)</text>']
for kind,data,color,dash in [('static',static,'#2563eb',''),('transition',drop,'#64748b',' stroke-dasharray="5 4"'),('kinetic',kinetic,'#b91c1c','')]:
    points=' '.join(f'{x(p):.6f},{y(f):.6f}' for p,f in data)
    s.append(f'<polyline data-series="{kind}" points="{points}" fill="none" stroke="{color}" stroke-width="3"{dash}/>')
s += ['<text x="18" y="440" fill="#2563eb">Ma sát nghỉ tới 150 N</text>',
      '<text x="18" y="468" fill="#b91c1c">Ma sát trượt bằng 100 N</text>','</g></svg>']
(B/name).write_bytes(('\n'.join(s)+'\n').encode('utf8'))

print('Reproduced16canonical solution images:15force diagrams and1answer graph.')
