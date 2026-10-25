"""Create a new mathematical schematic; never alters source PDF images."""
from pathlib import Path
from html import escape
import math
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-15'
OUT.mkdir(exist_ok=True)
W,H=480,930
scale=2
im=Image.new('RGB',(W*scale,H*scale),'white')
draw=ImageDraw.Draw(im)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
 '<title id="title">Chồng chất của hai xung dương</title>',
 '<desc id="desc">Năm thời điểm từ t bằng không đến sáu. Hai thành phần không âm truyền ngược chiều, tổng li độ luôn không âm và đạt 1,3 khi hai tâm trùng nhau.</desc>',
 '<rect width="480" height="930" fill="#ffffff"/>']

def line(points,color,width=2,dash=False):
    d=' '.join(('M' if i==0 else 'L')+f'{x:.2f},{y:.2f}' for i,(x,y) in enumerate(points))
    svg.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"'+(' stroke-dasharray="6 4"' if dash else '')+'/>')
    if dash:
        for i in range(0,len(points)-1,8):
            seg=points[i:min(i+5,len(points))]
            if len(seg)>1:draw.line([(round(x*scale),round(y*scale)) for x,y in seg],fill=color,width=round(width*scale))
    else:
        draw.line([(round(x*scale),round(y*scale)) for x,y in points],fill=color,width=round(width*scale))

def text(x,y,label,size=18,color='#172033',bold=False,anchor=None):
    fontpath='C:/Windows/Fonts/arialbd.ttf' if bold else 'C:/Windows/Fonts/arial.ttf'
    font=ImageFont.truetype(fontpath,size*scale)
    svg.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial, sans-serif" font-size="{size}"'+(' font-weight="700"' if bold else '')+(' text-anchor="middle"' if anchor=='middle' else '')+'>'+escape(label)+'</text>')
    box=draw.textbbox((0,0),label,font=font)
    xx=x*scale-(box[2]/2 if anchor=='middle' else 0)
    draw.text((xx,y*scale-size*scale*.95),label,fill=color,font=font)

def bump(q):
    return math.cos(math.pi*q/2)**4 if abs(q)<=1 else 0.

text(24,32,'Hai xung dương truyền ngược chiều',20,bold=True)
line([(24,55),(64,55)],'#2563eb',2,True);text(72,62,'Xung hẹp',16)
line([(242,55),(282,55)],'#d97706',2,True);text(290,62,'Xung rộng',16)
line([(24,82),(64,82)],'#0f766e',3);text(72,89,'Tổng li độ',16)

for idx,t in enumerate([0.,2.6,3.,3.4,6.]):
    top=110+idx*158
    baseline=top+120
    text(24,top+19,f't = {t:g}',18,bold=True)
    line([(45,baseline),(450,baseline)],'#9ca3af',1)
    text(453,baseline+5,'x',16)
    for x in [-4,0,4]:
        px=45+(x+5)*40.5
        line([(px,baseline-3),(px,baseline+3)],'#9ca3af',1)
        text(px,baseline+22,str(x),16,anchor='middle')
    xx=[-5+i*.01 for i in range(1001)]
    v1=[bump((x+3-t)/.5) for x in xx]
    v2=[.3*bump((x-3+t)/1.2) for x in xx]
    coords=lambda values:[(45+(x+5)*40.5,baseline-y*72) for x,y in zip(xx,values)]
    line(coords(v1),'#2563eb',2,True)
    line(coords(v2),'#d97706',2,True)
    line(coords([a+b for a,b in zip(v1,v2)]),'#0f766e',3)

text(24,925,'Đơn vị vị trí và thời gian được chọn để minh họa.',16)
svg.append('</svg>')
(OUT/'solution-selfcheck-15-6-positive-pulses.svg').write_text('\n'.join(svg)+'\n',encoding='utf8')
preview=ROOT/'qa/physics1-remaining/ch15/solution-selfcheck-15-6-positive-pulses.png'
preview.parent.mkdir(parents=True,exist_ok=True)
im.save(preview)
print(OUT/'solution-selfcheck-15-6-positive-pulses.svg')
