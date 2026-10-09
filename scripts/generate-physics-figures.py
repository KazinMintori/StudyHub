"""Sinh hình SVG từ mô hình trong Notes Vật lý; không cần thư viện ngoài.

Chạy: python -I scripts/generate-physics-figures.py
"""
from pathlib import Path
from math import sin, cos, radians, pi, exp
from html import escape
import importlib.util
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('physics_numbers',ROOT/'raw_materials/physics/verify_numbers.py')
numbers=importlib.util.module_from_spec(spec);spec.loader.exec_module(numbers)
DATA=numbers.calculate()
INK='#1f1c2b'; PURPLE='#5a37a8'; GREEN='#1d6b45'; RULE='#dcd8e8'
def label(x,y,text,size=17,color=INK,anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(text)}</text>'
def path(points,color=PURPLE,width=3,fill='none'):
    coords=' '.join(('M' if i==0 else 'L')+f'{x:.2f},{y:.2f}' for i,(x,y) in enumerate(points))
    return f'<path d="{coords}" fill="{fill}" stroke="{color}" stroke-width="{width}"/>'
def line(x1,y1,x2,y2,color=RULE,dash=''):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.5"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def save(course,slug,folder,name,title,body,caption):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 300" width="100%" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><rect width="480" height="300" rx="12" fill="#ffffff"/><g font-family="system-ui, Segoe UI, sans-serif">'+''.join(body)+'</g></svg>\n'
    ET.fromstring(svg)
    dest=ROOT/'docs'/course/'bai-giang/img'/folder/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(svg,encoding='utf-8')
    note=ROOT/'docs'/course/'bai-giang'/(slug+'.md');text=note.read_text(encoding='utf-8')
    relative=f'img/{folder}/{name}'
    if relative not in text:
        text=text.replace('## Ví dụ tính mẫu',f'![{title}]({relative})\n\n{caption}\n\n## Ví dụ tính mẫu',1)
        note.write_text(text,encoding='utf-8')

# Projectile coordinates come from the same g, speed and angle as the example.
d=DATA['c03']; v0=20;theta=radians(30);g=9.8
points=[]
for i in range(101):
    t=d['time']*i/100;x=v0*cos(theta)*t;y=v0*sin(theta)*t-g*t*t/2
    points.append((55+370*x/d['range'],245-165*y/d['height']))
b=[label(24,31,'Ném xiên, bỏ lực cản'),line(55,245,445,245,INK),line(55,245,55,57,INK)]
for fraction in [0,0.5,1]:
    x=55+370*fraction;b+=[line(x,245,x,249,INK),label(x,270,f'{d["range"]*fraction:.1f}',anchor='middle')]
b+=[label(445,289,'x (m)',anchor='end'),label(19,66,'y (m)'),label(47,250,'0',anchor='end'),label(47,86,f'{d["height"]:.2f}',anchor='end'),line(55,80,430,80,dash='5 5'),path(points),label(240,64,'đỉnh: chỉ vận tốc đứng bằng 0',15,anchor='middle')]
save('vat-ly-1','03-chuyen-dong-khong-gian','lec-03','quy-dao.svg','Quỹ đạo ném xiên với tốc độ đầu 20 mét mỗi giây và góc 30 độ',b,'Đường cong được tính từ hai phương trình tọa độ theo cùng thời gian. Tại đỉnh, tiếp tuyến nằm ngang nhưng gia tốc vẫn hướng xuống.')

# Pressure is normalized to the same initial state. Gamma is 5/3.
b=[label(24,31,'Hai đường giãn nở từ cùng trạng thái'),line(55,245,435,245,INK),line(55,245,55,60,INK),label(22,62,'p/p₁'),label(435,282,'V/V₁',anchor='end')]
def xy(x,y):return (55+360*(x-1),245-170*y)
isothermal=[xy(1+i/100,1/(1+i/100)) for i in range(101)]
adiabatic=[xy(1+i/100,(1+i/100)**(-5/3)) for i in range(101)]
shade=[xy(1,0)]+isothermal+[xy(2,0),xy(1,0)]
b+=[path(shade,'none',0,'#eee9fb'),path(isothermal),path(adiabatic,GREEN),label(285,139,'đẳng nhiệt',16,PURPLE),label(235,217,'đoạn nhiệt thuận nghịch',15,GREEN)]
for x in [1,1.5,2]:b+=[label(xy(x,0)[0],269,str(x),anchor='middle')]
for y in [0,0.5,1]:b+=[label(47,xy(1,y)[1]+5,str(y),anchor='end')]
save('vat-ly-1','19-nguyen-ly-thu-nhat','lec-19','duong-p-v.svg','Đường đẳng nhiệt và đoạn nhiệt thuận nghịch của khí đơn nguyên tử trên đồ thị áp suất–thể tích chuẩn hóa',b,'Diện tích tô dưới đường đẳng nhiệt biểu diễn công giãn nở khi nhân lại với áp suất và thể tích ban đầu. Đường đoạn nhiệt hạ nhanh hơn vì khí nguội khi thực hiện công.')

# RC curves show fractions of asymptotic voltage and initial current.
b=[label(24,31,'Nạp tụ RC từ trạng thái chưa tích điện'),line(55,245,435,245,INK),line(55,245,55,57,INK),label(22,63,'tỷ lệ'),label(435,285,'t/τ',anchor='end')]
rc=lambda t,y:(55+72*t,245-170*y)
for t in range(6):b+=[label(rc(t,0)[0],269,str(t),anchor='middle')]
for y in [0,0.5,1]:b+=[label(47,rc(0,y)[1]+5,str(y),anchor='end'),line(55,rc(0,y)[1],420,rc(0,y)[1],dash='4 5')]
b+=[path([rc(i/40,1-exp(-i/40)) for i in range(201)]),path([rc(i/40,exp(-i/40)) for i in range(201)],GREEN),line(127,245,127,75,dash='5 5'),label(250,69,'V tụ / điện áp nguồn',16,PURPLE),label(270,221,'I / dòng ban đầu',16,GREEN),label(138,151,'t = τ',15)]
save('vat-ly-2','06-mach-dien-mot-chieu','lec-26','nap-tu-rc.svg','Điện áp tụ tăng và dòng nạp giảm theo thời gian chuẩn hóa bằng hằng số RC',b,'Ở cùng thời điểm, điện áp tụ tăng trong khi dòng nạp giảm. Đường nét đứt tại một hằng số thời gian giúp thấy tụ chưa nạp đầy.')

# Thin-lens ray geometry uses the signed image distance in the worked example.
lens_x=280;axis=160;scale=700;s=0.3;sp=DATA['c34']['image'];f=0.1
obj_x=lens_x-scale*s;img_x=lens_x+scale*sp;obj_y=80;img_y=axis+80*sp/s
b=[label(24,30,'Thấu kính hội tụ: ảnh thật ngược chiều'),line(35,axis,448,axis,INK),line(lens_x,60,lens_x,228,PURPLE),label(lens_x,253,'thấu kính',16,PURPLE,anchor='middle')]
for fx,name in [(lens_x-scale*f,'F'),(lens_x+scale*f,'F′')]:b+=[line(fx,155,fx,165,INK),label(fx,182,name,anchor='middle')]
b+=[path([(obj_x,axis),(obj_x,obj_y)],GREEN,4),path([(img_x,axis),(img_x,img_y)],GREEN,4),path([(obj_x,obj_y),(lens_x,obj_y),(img_x,img_y)],PURPLE),path([(obj_x,obj_y),(lens_x,axis),(img_x,img_y)],'#2872a0'),label(obj_x,65,'vật',16,GREEN,anchor='middle'),label(img_x,img_y+23,'ảnh',16,GREEN,anchor='middle'),label(97,286,'s = 0.30 m',16),label(326,286,'s′ = 0.15 m',16)]
save('vat-ly-2','14-quang-hinh-hoc','lec-34','tao-anh.svg','Hai tia đặc biệt tạo ảnh thật của thấu kính có tiêu cự 0.10 mét khi vật ở 0.30 mét',b,'Tia tới song song trục đi qua tiêu điểm phía sau; tia qua tâm thấu kính đi thẳng trong mô hình mỏng. Chúng gặp nhau tại ảnh có độ cao bằng một nửa và ngược chiều vật.')

# Ground-state probability density in an infinite box, normalized by L.
b=[label(24,31,'Mật độ xác suất ở mức cơ bản'),line(55,245,435,245,INK),line(55,245,55,57,INK),label(15,61,'L|ψ|²'),label(435,285,'x/L',anchor='end')]
prob=lambda x:(55+360*x,245-80*2*sin(pi*x)**2)
curve=[prob(i/200) for i in range(201)]
shade=[(145,245)]+[prob(0.25+i/200) for i in range(101)]+[(325,245),(145,245)]
b+=[path(shade,'none',0,'#eee9fb'),path(curve),line(145,245,145,60,dash='4 5'),line(325,245,325,60,dash='4 5'),label(235,57,f'phần tô: P ≈ {DATA["c40"]["center_probability"]:.3f}',16,PURPLE,anchor='middle')]
for x in [0,0.25,0.5,0.75,1]:b+=[label(prob(x)[0],269,str(x),16,anchor='middle')]
for y in [0,1,2]:b+=[label(47,245-80*y+5,str(y),anchor='end')]
save('vat-ly-2','20-ham-song-schrodinger','lec-40','mat-do-xac-suat.svg','Mật độ xác suất trạng thái cơ bản trong hộp vô hạn và xác suất trên nửa giữa hộp',b,'Trục ngang dùng vị trí chia chiều dài hộp; trục đứng dùng mật độ nhân chiều dài. Diện tích tô cho xác suất trong khoảng từ một phần tư đến ba phần tư hộp, lớn hơn một nửa vì mật độ cao ở giữa.')
print('Generated 5 SVG figures and verified XML.')
