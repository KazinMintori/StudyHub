"""Reproducible scientific SVG figures and numerical checks for the Wiki atlas."""
from pathlib import Path
from fractions import Fraction as F
from math import log2, sqrt
from collections import deque
from html import escape
import json

OUT = Path('docs/wiki/img/atlas')
OUT.mkdir(parents=True, exist_ok=True)
INK, MUTED, PURPLE, BLUE, GREEN, RED = '#27233a', '#625b76', '#6540ad', '#2f5fd0', '#176b46', '#b42318'

def text(x,y,label,size=28,color=INK,anchor='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{color}">{escape(str(label))}</text>'
def line(x1,y1,x2,y2,color=MUTED,width=3,dash='',arrow=False):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arrow)"' if arrow else '')+'/>'
def rect(x,y,w,h,fill='#eee9fb',stroke=PURPLE):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
def circle(x,y,label,fill='#eee9fb'):
    return f'<circle cx="{x}" cy="{y}" r="31" fill="{fill}" stroke="{PURPLE}" stroke-width="3"/>'+text(x,y+10,label)
def save(name,title,body,height=400):
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(title)}. Các nhãn và ví dụ được giải thích trong bài.</desc>
<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="none" stroke="context-stroke" stroke-width="1.5"/></marker></defs>
<rect width="600" height="{height}" fill="#fff" rx="16"/>
<g font-family="'Be Vietnam Pro','Segoe UI',sans-serif">{body}</g></svg>'''
    (OUT/f'{name}.svg').write_text(svg,encoding='utf-8')

# 1. Vector addition, coordinates map x -> 80+90x, y -> 330-65y.
o=(80,330); a=(350,265); b=(170,135); s=(440,70)
body=line(45,330,540,330)+line(80,365,80,35)
body+=line(*o,*a,BLUE,4,arrow=True)+line(*o,*b,GREEN,4,arrow=True)+line(*o,*s,PURPLE,5,arrow=True)
body+=line(*a,*s,GREEN,3,'8 6')+line(*b,*s,BLUE,3,'8 6')
body+=text(400,310,'u = (3, 1)',color=BLUE)+text(130,100,'v = (1, 3)',color=GREEN)+text(415,40,'u + v = (4, 4)',26,PURPLE)
save('vector','Cộng hai vector bằng quy tắc hình bình hành',body)

# 2. Diagonal linear transformation: square -> rectangle.
body=rect(55,110,120,120,'#e8eefc',BLUE)+rect(310,110,240,120,'#eee9fb',PURPLE)
body+=line(200,170,285,170,PURPLE,4,arrow=True)+text(115,85,'Trước')+text(430,85,'Sau')
body+=text(125,295,'(x, y)')+text(435,295,'(2x, y)')+text(300,360,'Kéo giãn theo một trục',28)
save('matrix','Ma trận đường chéo kéo giãn hình vuông theo một trục',body)

# 3. Tangent and secants of x^2, physical coordinates 80+90x, 330-35x^2.
pts=' '.join(f'{80+90*x:.2f},{330-35*x*x:.2f}' for x in [j/50 for j in range(176)])
body=line(45,330,550,330)+line(80,360,80,35)+f'<polyline points="{pts}" fill="none" stroke="{BLUE}" stroke-width="4"/>'
body+=line(161,344,359,36,PURPLE,4)+circle(260,190,'P')+text(435,90,'y = x²',30,BLUE)+text(415,250,'Độ dốc tại P',26,PURPLE)+text(300,380,'Tiếp tuyến là xấp xỉ cục bộ',26)
save('derivative','Tiếp tuyến của đồ thị hàm bình phương tại điểm có hoành độ 2',body)

# 4. Elliptical contours x^2+2y^2, gradient at (1,1) parallel to (2,4).
body=line(80,290,545,290)+line(220,355,220,35)
for r in [0.8,1.3,1.8,2.3]:
    body+=f'<ellipse cx="220" cy="290" rx="{80*r:.1f}" ry="{80*r/sqrt(2):.1f}" fill="none" stroke="#b6a4db" stroke-width="2"/>'
body+=line(300,210,370,70,PURPLE,5,arrow=True)+circle(300,210,'P')+text(430,50,'∇f(P) = (2, 4)',26,PURPLE)+text(455,340,'Đường mức',26,MUTED)
save('gradient','Gradient vuông góc với đường mức và hướng về giá trị tăng',body)

# 5. Chord lies above x^2 on interval [-1,2].
pts=' '.join(f'{250+90*x:.2f},{315-45*x*x:.2f}' for x in [-1.8+j/40 for j in range(165)])
body=line(45,315,550,315)+line(250,350,250,35)+f'<polyline points="{pts}" fill="none" stroke="{BLUE}" stroke-width="4"/>'
body+=line(160,270,430,135,PURPLE,4)+line(295,303.75,295,202.5,GREEN,4,'5 5')
body+=circle(160,270,'A')+circle(430,135,'B')+text(140,80,'Dây cung',28,PURPLE)+text(430,345,'Đồ thị lồi',28,BLUE)
save('convex','Đồ thị hàm lồi nằm dưới dây cung nối hai điểm',body)

# 6. Natural frequency view of conditional probability.
body=rect(30,55,540,275,'#f5f4f9','#dcd8e8')+rect(50,85,180,215,'#e8eefc',BLUE)+rect(250,85,300,215,'#eee9fb',PURPLE)
body+=text(140,130,'Nhóm A')+text(400,130,'Nhóm khác')+text(140,200,'20 mẫu')+text(400,200,'80 mẫu')
body+=text(140,265,'18 đạt',28,GREEN)+text(400,265,'16 đạt',28,GREEN)+text(300,375,'Trong 34 mẫu đạt: 18 thuộc A',26)
save('bayes','Phân loại 100 mẫu thành hai nhóm và quan sát kết quả đạt',body)

# 7. Same center, different spread.
body=text(150,55,'Ít phân tán')+text(450,55,'Phân tán hơn')
for start,values in [(25,[4,5,6]),(325,[0,5,10])]:
    body+=line(start,260,start+250,260)+line(start+125,120,start+125,190,PURPLE,3,'6 5')+line(start+125,270,start+125,300,PURPLE,3,'6 5')
    for val in values:
        x=start+25+20*val
        body+=f'<circle cx="{x}" cy="205" r="8" fill="{BLUE}"/>'+text(x,240,val,26)
    body+=text(start+125,345,'Trung bình 5',26,PURPLE)
save('variance','Hai nhóm có cùng trung bình nhưng độ phân tán khác nhau',body)

# 8. Queue vs stack, three items and unambiguous exit.
body=text(150,45,'Hàng đợi')+text(450,45,'Ngăn xếp')
for j,label in enumerate(['A','B','C']):
    body+=rect(50+68*j,130,60,80)+text(80+68*j,180,label)
    body+=rect(400,250-75*j,100,65)+text(450,294-75*j,label)
body+=line(70,245,70,325,BLUE,4,arrow=True)+text(120,365,'A ra trước',26,BLUE)
body+=line(520,140,565,85,GREEN,4,arrow=True)+text(450,365,'C ra trước',26,GREEN)
save('queue-stack','Cùng thêm A rồi B rồi C, hàng đợi lấy A còn ngăn xếp lấy C',body)

# 9. Weighted graph: direct vs two hops.
nodes={'A':(100,190),'B':(300,75),'C':(500,190),'D':(300,315)}
edges=[('A','B','1'),('B','C','1'),('A','C','9'),('A','D','2'),('D','C','3')]
body=''
for u,v,w in edges:
    x1,y1=nodes[u];x2,y2=nodes[v];body+=line(x1,y1,x2,y2,BLUE,3);body+=text((x1+x2)/2,(y1+y2)/2-12,w,28,RED)
for label,(x,y) in nodes.items():body+=circle(x,y,label)
save('graph','Đường một cạnh có trọng số 9 còn đường hai cạnh qua B có trọng số 2',body)

# The spanning tree contains exactly AB, BC and AD.
body=''
for u,v in [('A','B'),('B','C'),('A','D')]:
    body+=line(*nodes[u],*nodes[v],BLUE,4)
for label,(x,y) in nodes.items():body+=circle(x,y,label)
body+=text(300,385,'4 đỉnh · 3 cạnh · Không chu trình',26)
save('tree','Cây khung nối đủ bốn đỉnh bằng các cạnh AB, BC và AD',body)

# Restrict the same saddle function to two directions through the origin.
body=''
for center,sign,label in [(150,6,'g(t, t) = 6t²'),(450,-2,'g(t, −t) = −2t²')]:
    body+=line(center-110,240,center+110,240)+line(center,320,center,65)
    pts=' '.join(f'{center+80*t:.2f},{240-25*sign*t*t:.2f}' for t in [-1+j/50 for j in range(101)])
    body+=f'<polyline points="{pts}" fill="none" stroke="{BLUE if sign>0 else RED}" stroke-width="4"/>'+text(center,45,label,26)
body+=text(300,375,'Cùng một điểm, hai dấu độ cong',26)
save('hessian','Một hàm yên ngựa cong lên theo hướng này và cong xuống theo hướng khác',body)

# 10. Hash collision handled by chaining.
body=text(135,50,'Khóa')+text(430,50,'Ô băm')
for row,(key,bucket) in enumerate([(2,2),(6,2),(9,1)]):
    y=105+100*row;body+=rect(60,y-30,120,60)+text(120,y+10,key)+line(195,y,320,210 if bucket==2 else 110,PURPLE,3,arrow=True)
body+=rect(340,75,210,70)+text(445,120,'1: 9')+rect(340,175,210,70)+text(445,220,'2: 2 → 6')+text(300,375,'h(k) = k mod 4',28,PURPLE)
save('hash','Hai khóa 2 và 6 cùng băm vào ô 2 nhưng vẫn được lưu riêng',body)

# 11. A finite-state transducer changes state after each 1.
body=circle(170,210,'q₀')+circle(430,210,'q₁')
body+=line(210,180,390,180,PURPLE,4,arrow=True)+line(390,245,210,245,BLUE,4,arrow=True)
body+=text(300,150,'Đọc 1',28,PURPLE)+text(300,290,'Đọc 1',28,BLUE)+text(170,350,'Số 1 chẵn',26)+text(430,350,'Số 1 lẻ',26)
save('states','Máy hai trạng thái theo dõi tính chẵn lẻ của số ký hiệu 1',body)

# 12. Shannon entropy values, calculated from probabilities.
body=line(70,320,550,320)+text(300,45,'Độ bất định của một bit',28)
for x,p,label in [(125,0,'Chắc chắn'),(300,0.5,'Cân bằng'),(475,0.9,'Lệch')]:
    h=0 if p==0 else -p*log2(p)-(1-p)*log2(1-p)
    body+=rect(x-45,320-210*h,90,max(3,210*h),'#eee9fb',PURPLE)+text(x,350,label,24)+text(x,95 if p==0.5 else 170,f'{h:.2f}'.replace('.',',')+' bit',24,PURPLE)
save('entropy','Entropy nhị phân bằng 0 khi chắc chắn và đạt 1 bit khi cân bằng',body)

# Independent numerical checks for examples used in authored pages.
assert (3+1,1+3)==(4,4)
assert (1*2+2*1,0*2+3*1)==(4,3)
assert 3*1+4*(-1)==-1
assert sqrt(3**2+4**2)==5
assert F(18,34)==F(9,17)
assert F(1,4)*0+F(1,2)*2+F(1,4)*4==2
assert F(1,4)*4+F(1,4)*4==2
assert F(sum((v-5)**2 for v in [4,5,6]),3)==F(2,3)
assert F(sum((v-5)**2 for v in [0,5,10]),3)==F(50,3)
q=deque(['A','B','C']); assert q.popleft()=='A'
s=['A','B','C']; assert s.pop()=='C'
assert 2%4==6%4==2 and 9%4==1
assert abs((-F(1,2)*log2(F(1,2))*2)-1)<1e-12
assert (2*2-(-1),2*(-1)-4)==(5,-6)
assert 3*4+4*(-3)==0
assert abs(F(201,100)**2-F(404,100))==F(1,10000)
assert F(8,10)**2+2*F(6,10)**2==F(136,100)
assert (-1)**2+2*(-3)**2==19
assert sum([2,4,4,2])==12 and 2-4-4+2==-4
assert F(-1+2,2)**2==F(1,4) and F(1+4,2)==F(5,2)
assert F(1,4)!=F(1,2)**3  # Pairwise independence need not imply joint independence.
assert 1+1==2 < 2+3==5 < 9
assert [n+2 for n in [60,64,67]]==[62,66,69]
assert sum(int(c) for c in '1011')%2==1
assert abs(-.9*log2(.9)-.1*log2(.1)-.4689955935892812)<1e-12
assert F(6,2)==3 and 1+3*2==7 and 2*3==6
print(f'Generated {len(list(OUT.glob("*.svg")))} SVG figures; all numerical checks passed')
