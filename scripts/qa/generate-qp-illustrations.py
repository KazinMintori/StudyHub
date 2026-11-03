from pathlib import Path
from lxml import etree
import pymupdf
from html import escape
out=Path('../math-ai-visual-content/docs/toan-cho-ai/bai-giang/img/lec-02');out.mkdir(parents=True,exist_ok=True)
qa=Path('qa/math-ai-visuals/qp-illustrations');qa.mkdir(parents=True,exist_ok=True)
ink='#242136';purple='#7757b9';green='#19705a';red='#b34454'
def text(x,y,label,anchor='start',size=17):return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}">{escape(label)}</text>'
def line(x,y,u,v,color='#81798e',width=1.1):return f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="{color}" stroke-width="{width}"/>'
def write(name,height,body,title):
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="{height}" viewBox="0 0 360 {height}" role="img"><title>{title}</title><rect width="360" height="{height}" rx="12" fill="white"/><g fill="{ink}" font-family="sans-serif" font-size="17">{body}</g></svg>'
 root=etree.fromstring(svg.encode())
 (out/(name+'.svg')).write_text(svg,encoding='utf-8')
 root.set('width','294');root.set('height',str(294*height/360))
 doc=pymupdf.open(stream=etree.tostring(root),filetype='svg');doc[0].get_pixmap().save(qa/(name+'.png'))
body=''
for index,(label,kind) in enumerate([('R > 0: Miền có phần trong','disk'),('R = 0: Chỉ còn một điểm','point'),('R < 0: Không có điểm nào','empty')]):
 top=index*146
 body+=text(180,top+27,label,'middle')
 body+=line(105,top+82,255,top+82)+line(180,top+44,180,top+122)
 if kind=='disk':body+=f'<ellipse cx="180" cy="{top+82}" rx="53" ry="29" fill="#eee7f7" stroke="{purple}" stroke-width="1.3"/>'
 elif kind=='point':body+=f'<circle cx="180" cy="{top+82}" r="5" fill="{green}"/>'
 else:body+=text(180,top+94,'∅','middle',38)
 body+=text(180,top+139,'(x − a)ᵀP(x − a)/2 ≤ R','middle',16)
write('qcqp-three-domains',448,body,'Ma trận xác định dương vẫn cho ba khả năng của tập mức dưới tùy vế phải')
body=text(180,28,'Hai điểm trên cùng một miền hộp','middle')
body+=f'<rect x="70" y="57" width="190" height="190" fill="#eee7f7" stroke="{purple}" stroke-width="1.2"/>'
body+=line(54,247,278,247)+line(70,43,70,266)
q=247-190*241/302
body+=f'<circle cx="260" cy="{q}" r="6" fill="{green}"/><circle cx="260" cy="247" r="6" fill="{red}"/>'
body+=text(246,q-14,'Q','end')+text(246,235,'K','end')
body+=text(60,273,'0')+text(260,273,'1','middle')+text(53,65,'1','end')
body+=text(180,307,'K = (1, 0), J = 5.30','middle')
body+=text(180,336,'Q = (1, 0.798…), J ≈ 3.377','middle')
body+=text(180,369,'Nghiệm tự do nằm ngoài khung:','middle',16)+text(180,395,'(7.173…, −5.130…)','middle',16)
write('qp-clipping-counterexample',414,body,'Kẹp tọa độ nghiệm tự do cho điểm K có sai số lớn hơn nghiệm Q thật sự của QP')
print('Generated two deterministic QP vector illustrations.')
