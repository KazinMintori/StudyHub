"""Đối chiếu số của phụ lục nguồn. Chỉ ghi lỗi, không thay đáp án nguyên tác."""
from math import pi,sqrt,sin,cos,atan2,acos,degrees,radians
from pathlib import Path
import json,sys
if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[2]
def vec(length,angle):return [length*cos(radians(angle)),length*sin(radians(angle))]
def plus(*args):return [sum(v[i] for v in args) for i in range(len(args[0]))]
def negate(v):return [-x for x in v]
def norm(v):return sqrt(sum(x*x for x in v))
def direction(v):return degrees(atan2(v[1],v[0]))%360
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def angle(a,b):return degrees(acos(max(-1,min(1,dot(a,b)/(norm(a)*norm(b))))))
answers={
 '1.1':[5280*.3048/1000,1000/.3048],
 '1.3':.3048/299792458*1e9,
 '1.5':1e9/(365*24*3600),
 '1.7':[55*1.609/3.788,1500/(55*1.609/3.788)/45],
 '1.9':(3*(60000/19.5)/(4*pi))**(1/3),
 '1.11':[12*5.98,5.98/12,2*(12+5.98),12-5.98,12/5.98],
 '1.13':abs(pi*1e7-365.24*86400)/(365.24*86400)*100,
 '1.21':plus(vec(2.6,90),vec(4,0),vec(3.1,45)),
 '1.23':negate(plus(vec(180,180),vec(210,315),vec(280,60))),
 '1.27':[-9.60*sin(radians(32))/cos(radians(32)),9.60/cos(radians(32))],
 '1.31':[-2.2,3.25-1.5],
 '1.39':{'A':norm([-2,3,4]),'B':norm([3,1,-3]),'difference':norm([-5,2,7])},
 '1.43':[angle([-2,6],[2,-3]),angle([3,5],[10,6]),angle([-4,2],[7,14])],
 '1.49':[5.97e24/(4/3*pi*(6.37e6)**3)/1000,1.99e30/(4/3*pi*(7500e3)**3)/1000,1.99e30/(4/3*pi*(10e3)**3)/1000],
 '1.51':(3*(5.5*5.97e24)/(4*pi*1760))**(1/3)/1000,
 '1.61':12.8/(2*cos(radians(32))),
 '1.63':plus([-32,0],negate(plus(vec(23,-34),[0,46]))),
 '1.65':plus([0,20.8],[38,0],vec(18,237)),
 '1.67':plus(vec(122,328),[72,0]),
 '1.69':negate(plus([0,-825],vec(1250,120),vec(1000,32))),
 '1.71':plus([0,-10],negate(plus([12,0],vec(28,140)))),
 '1.73':norm(plus(vec(32,37),negate(vec(21,-23)))),
 '1.75':5*.8*cos(radians(120)),
 '1.77':degrees(atan2(9,-6)),
 '1.81':sqrt((12*16)**2-112**2),
 '1.83':48/(9*cos(radians(321-242))),
 '1.85':[-8,-8*5/6.5],
 '1.93':2*(3*(4.2e6*1e-18)/(4*pi))**(1/3)*1000,
}
A=[0,-8];B=vec(15,60);C=vec(12,205);D=vec(10,143)
answers['1.25']={'A':A,'B':B,'C':C,'D':D}
answers['1.29']=[plus(A,B),plus(B,A),plus(A,negate(B)),plus(B,negate(A))]
answers['1.33']=[plus(vec(2.8,60),vec(1.9,-60)),plus(vec(2.8,60),negate(vec(1.9,-60))),plus(vec(1.9,-60),negate(vec(2.8,60)))]
a=vec(3.6,70);b=vec(2.4,210)
answers['1.37']={'A':a,'B':b,'C':plus([3*x for x in a],[-4*x for x in b])}
answers['1.41']=[dot(A,B),dot(B,C),dot(A,C)]
answers['1.45']=A[0]*D[1]-A[1]*D[0]
answers['1.47']={'A':[-8,0,0],'B':[0,-2,0],'cross':[0,0,16],'magnitude_B':2}
answers['1.59']=plus([0,450],vec(600,233.1))
samples={'A':(8e-3,1.67e-6),'B':(6e-9,9.38e6*1e-18),'C':(8e-6,2.50e-3*1e-6),'D':(9e-4,2.81e3*1e-9),'E':(9e4*1e-12,1.41e-2*1e-9),'F':(6e-2*1e-6,1.25e8*1e-18)}
densities={k:m/v for k,(m,v) in samples.items()}
answers['1.87']={'densities':densities,'order':sorted(densities,key=densities.get)}
earth=[.3182,.9329,0];mars=[1.3087,-.4423,-.0414]
earth_mars=plus(mars,negate(earth))
answers['1.89']={'distances':[norm(earth),norm(mars),norm(earth_mars)],'angle':angle(negate(earth),earth_mars)}
distance=sqrt(138**2+77**2-2*138*77*cos(radians(25.6)))
answers['1.91']={'distance':distance,'angle':degrees(acos((77**2+distance**2-138**2)/(2*77*distance)))}
for key in ['1.21','1.23','1.31','1.63','1.65','1.67','1.69','1.71']:
    answers[key]={'components':answers[key],'length':norm(answers[key]),'angle_from_positive_x':direction(answers[key])}
assert answers['1.87']['order']==['D','F','B','C','A','E']
assert abs(answers['1.25']['B'][1]-12.990381)<1e-5
assert abs(answers['1.45']-(-63.89084))<1e-4
assert abs(answers['1.93']-.20)<.01
errors=[
 {'problem':'1.25','sourcePdf':1554,'printed':'B_y=13.0 cm; C_x=-10.9 cm','verified':'B_y≈13.0 m; C_x≈-10.9 m','kind':'unit mismatch'},
 {'problem':'1.47','sourcePdf':1554,'printed':'-2.0 m, -x-direction','verified':'magnitude 2.0 m; B points in -y-direction','kind':'negative magnitude and wrong direction'},
 {'problem':'1.79(b)','sourcePdf':1554,'printed':'magnitude of scalar product: -bd','verified':'absolute value bd for b,d positive','kind':'signed value printed for requested magnitude'},
]
out=ROOT/'qa/physics/translation-review/exercise-answer-audit.json'
out.write_text(json.dumps({'numericChecks':answers,'sourceDiscrepancies':errors,'notes':'Source discrepancies are reported, never silently corrected.'},ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Checked {len(answers)} numeric answer groups; reported {len(errors)} source discrepancies.')
