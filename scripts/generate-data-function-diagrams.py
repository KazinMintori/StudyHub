"""Small deterministic function diagrams designed for a 360px reading column."""
from pathlib import Path
import html,json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/xu-ly-du-lieu/bai-giang/img/function-examples'
OUT.mkdir(parents=True,exist_ok=True)
INK='#241c39';MUTED='#5e556f';PURPLE='#6846a8';TEAL='#17776d';PALE='#f0eaf8'
class Drawing:
    def __init__(self,title,height):
        self.height=height;self.parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 330 {height}" width="100%" role="img"><title>{html.escape(title)}</title><rect width="330" height="{height}" rx="16" fill="#fffdf8"/>'];self.text(18,32,title,18,weight='700')
    def text(self,x,y,value,size=16,color=INK,weight='400'):
        self.parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" font-family="system-ui,Segoe UI,sans-serif">{html.escape(str(value))}</text>')
    def table(self,y,heads,rows):
        widths=[294/len(heads)]*len(heads)
        self.parts.append(f'<rect x="18" y="{y}" width="294" height="30" rx="5" fill="{PALE}"/>')
        for r,row in enumerate([heads]+rows):
            for col,value in enumerate(row):self.text(25+sum(widths[:col]),y+21+30*r,value,16,weight='600' if r==0 else '400')
            if r:self.parts.append(f'<path d="M18 {y+30*(r+1)}h294" stroke="#ddd5e7"/>')
        return y+30*(len(rows)+1)
    def arrow(self,y,label):
        self.text(158,y+24,'↓',23,PURPLE);self.text(18,y+49,label,16,PURPLE,weight='600')
    def save(self,name):
        (OUT/name).write_text(''.join(self.parts)+'</svg>\n',encoding='utf-8',newline='\n')

d=Drawing('map: Tra từng giá trị',378)
d.table(55,['Nhãn','Mã phòng','Phí'],[['P1','NC','20'],['P2','PR','10'],['P3','X','Thiếu'],['P4','Thiếu','Thiếu']])
d.text(18,243,'Bảng tra: NC → 20, PR → 10',16,TEAL)
d.text(18,278,'Giữ nhãn và số hàng.',16,weight='600')
d.text(18,308,'X chưa có trong bảng tra.',16,MUTED)
d.text(18,338,'P4 chưa có mã để tra.',16,MUTED)
d.save('series-map.svg')

d=Drawing('apply: Hàm nhận phần nào?',515)
d.table(55,['Ngày','Bàn','Ghế'],[['T2','2','8'],['T3','5','11']])
d.arrow(158,'axis=0: Từng cột')
d.table(220,['Hàm nhận','max − min'],[['Bàn: 2, 5','3'],['Ghế: 8, 11','3']])
d.arrow(317,'axis=1: Từng hàng')
d.table(379,['Hàm nhận','max − min'],[['T2: 2, 8','6'],['T3: 5, 11','6']])
d.save('dataframe-apply.svg')

d=Drawing('concat: Nối cột, khớp nhãn',485)
d.text(18,65,'Bảng giá',16,weight='600');d.text(178,65,'Bảng phí',16,weight='600')
for x,rows in [(18,[['A','80'],['B','100']]),(178,[['B','5'],['A','20']])]:
    d.parts.append(f'<rect x="{x}" y="76" width="134" height="95" rx="8" fill="{PALE}"/>')
    for i,row in enumerate(rows):d.text(x+12,108+i*35,row[0]);d.text(x+66,108+i*35,row[1])
d.arrow(178,'concat([giá, phí], axis=1)')
d.table(249,['Nhãn','Giá','Phí'],[['A','80','20'],['B','100','5']])
d.text(18,382,'A khớp A, B khớp B.',16,TEAL,weight='600')
d.text(18,415,'Thứ tự hàng ở đầu vào khác',16,MUTED)
d.text(18,442,'nhau không làm đổi phép khớp.',16,MUTED)
d.save('concat-alignment.svg')

d=Drawing('agg và transform trả gì?',665)
d.table(55,['Hàng','Phòng','Lương'],[['0','A','10'],['1','A','20'],['2','B','30'],['3','B','50']])
d.arrow(212,'agg("mean"): Một số mỗi nhóm')
d.table(274,['Phòng','TB lương'],[['A','15'],['B','40']])
d.arrow(371,'transform("mean"): Về từng hàng')
d.table(433,['Hàng','Phòng','TB phòng'],[['0','A','15'],['1','A','15'],['2','B','40'],['3','B','40']])
d.text(18,630,'Phòng A: Hai hàng cùng nhận 15.',16,TEAL)
d.save('groupby-shape.svg')
assert (10+20)/2==15 and (30+50)/2==40
assert [max(v)-min(v) for v in [[2,5],[8,11]]]==[3,3]
assert [max(v)-min(v) for v in [[2,8],[5,11]]]==[6,6]
print(json.dumps({'figures':4,'viewBoxWidth':330,'minimumFontSize':16,'numericChecks':'passed'}))
