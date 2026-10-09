"""Tính lại đáp số nguyên tác chương 2; không sinh lời giải vào trang học."""
from math import sqrt, isclose
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
g = 9.8
checks = {}


def check(key, actual, printed, tolerance=0.006):
    if isinstance(actual, (tuple, list)):
        assert len(actual) == len(printed), key
        for a, b in zip(actual, printed):
            assert isclose(a, b, rel_tol=tolerance, abs_tol=0.0006), (key, a, b)
    else:
        assert isclose(actual, printed, rel_tol=tolerance, abs_tol=0.0006), (key, actual, printed)
    checks[key] = {"calculated": actual, "printed": printed}


check('VP2.5.1', [2*18/8, 18*2*18/8], [4.5, 81])
check('VP2.5.2', [2*30/12.5, 30*12.5], [4.8, 375])
t = 2*(30-20)/1.8
check('VP2.5.3', [t, 20*t, 30-1.8*t], [11.1, 222, 10])
check('VP2.7.1', [12*.3-.5*g*.3**2, 12-g*.3, 12*2.6-.5*g*2.6**2, 12-g*2.6], [3.16, 9.06, -1.92, -13.5])
check('VP2.7.2', [-8*1.5-.5*g*1.5**2, -8-g*1.5, -sqrt(8**2+2*g*8)], [-23, -22.7, -14.9])
v0 = sqrt(.5**2+2*g*4)
check('VP2.7.3', [v0, (v0-.5)/g], [8.87, .854])
check('VP2.8.1', [(12-sqrt(12**2-2*g*4))/g, (12+sqrt(12**2-2*g*4))/g, (12+sqrt(12**2+2*g*4))/g], [.398, 2.05, 2.75])
check('VP2.8.2', (-9+sqrt(9**2+2*g*5))/g, .447)
check('VP2.8.3a', [(5.5-sqrt(5.5**2-2*g*1.3))/g, (5.5+sqrt(5.5**2-2*g*1.3))/g], [.338, .784])
assert 5.5**2-2*g*1.8 < 0
check('bridging', .5*g*(1/(1-1/sqrt(2)))**2, 57.1)

check('2.1', 6.25*4, 25)
check('2.3', 105*(1+50/60)/70*60-110, 55)
check('2.5', [20/64,100/64], [.313,1.56])
check('2.7', [(2.4*10**2-.12*10**3)/10, 0, 2*2.4*5-3*.12*5**2, 2*2.4*10-3*.12*10**2, 2*2.4/(3*.12)], [12,0,15,12,13.3])
check('2.9', [7/3,7/3,7/3,1/3], [2.33,2.33,2.33,.33], .012)
check('2.11', [20/3,20/3,0,-40,-40,-40,0], [6.7,6.7,0,-40,-40,-40,0])
ts=[(2-sqrt(4-4*.0625*10))/(2*.0625),(2+sqrt(4-4*.0625*10))/(2*.0625),(2+sqrt(4+4*.0625*10))/(2*.0625)]
check('2.13', [2,50,-.125,16,32,*[value for t in ts for value in [t,2-.125*t]]], [2,50,-.125,16,32,6.20,1.23,25.8,-1.23,36.4,-2.55])
check('2.15', [.1*25/5,0,2*.1*5],[.5,0,1])
t=(9.6/.6)**.25
check('2.17', [2.17,9.6,2.17+4.8*t*t-.1*t**6,9.6-3*t**4], [2.17,9.6,15,-38.4])
check('2.19', [2*70/6-15,(15-(2*70/6-15))/6], [8.33,1.11])
check('2.21',[45**2/(2*1.5),2*1.5/45],[675,.0667])
check('2.23',(105/3.6)**2/(2*250),1.70)
check('2.25',.5*60*g*.036**2,.38)
check('2.27', [5000**2/(2*4),5000**2/(2*4)/g,5000/(5000**2/(2*4))*1000], [3.1e6,3.2e5,1.6],.012)
check('2.29',[0,(45-20)/4,-45/4,20*5,20*5+(20+45)*4/2,20*5+(20+45)*4/2+45*4/2],[0,6.3,-11.2,100,230,320],.009)
check('2.31',[sqrt(2*g*.44),2*sqrt(2*g*.44)/g],[2.94,.600])
check('2.33',2*8.2/g,1.67)
check('2.35',[.5*.379*g*(8.5/2)**2,.379*g*8.5/2],[33.5,15.8])
check('2.39',sqrt(2*.176/g),.190)
v=sqrt(2*2.25*525)
check('2.41',[525+v*v/(2*g),(v+sqrt(v*v+2*g*525))/g,sqrt(v*v+2*g*525)],[646,16.4,112])
check('2.43',.5*g*(3.6/2)**2,15.9)
check('2.45',g*(1.75/18.6)**2,.0868)
check('2.47',sqrt((g*6/2)**2+2*g*28),37.6)
t=(325*6/2.8)**(1/3)
check('2.49',[2.8*10**3/6,.5*2.8*t*t],[467,110])
t=1.5/.12
check('2.51',.5*1.5*t*t-.12*t**3/3,39.1)
check('2.53',[10,50/(2+40/10),100/(2+90/10),200/(2+190/10)],[10,8.33,9.09,9.52])
check('2.55',33/(1/3.5-1/6.5),250,.015)
check('2.57',[(1000-63)/4.75,1000/5.9],[197,169])
a=3**2/(2*8)
check('2.59',[sqrt(2*a*16),sqrt(2*16/a)],[4.24,7.54])
check('2.61',[(4+12)*10/2+12*2/2]*2,[92,92])
check('2.63',200/3,67)
t=sqrt(2*60/2.1)
check('2.65',[t,.5*(3.4-2.1)*t*t,3.4*t,2.1*t],[7.56,37.2,25.7,15.9])
check('2.67',100/(.5*3**2+3*9),3.2,.01)
check('2.69',[sqrt(2*8/4),8*2-4*2**3,8-12*2**2],[2,-16,-40])
check('2.71',[(4**2-.5*4**3)/4,-4-2*4+1.5*4**2],[-4,12])
v=(30-.5*g*1.5**2)/1.5
check('2.73',30+v*v/(2*g),38.2)
v=sqrt(2*35*.64)
check('2.75',[v,2.2+v*v/(2*g),(v+sqrt(v*v+2*g*(2.2-1.83)))/g],[6.69,4.49,1.42])
check('2.77',[10/3,3**2],[3.3,9],.015)
T=(50+sqrt(50**2+2*g*250))/g
y=250+50*7-.5*g*7**2;v=50-g*7;dt=T-7
check('2.79',[250+50**2/(2*g),y+v*dt-dt**2],[380,184],.008)
check('2.81',[2*20/8**2,20*8-(2*20/8**2)*8**3/6],[.625,107])
check('2.83',[(1.6-sqrt(1.6**2-4*.2*2.6))/(2*.2),(1.6+sqrt(1.6**2-4*.2*2.6))/(2*.2),1,13/3,(5.6-2.4)/1.2],[2.27,5.73,1,4.33,2.67])
check('2.85',1/(2*g),.0510)
check('2.87',2/sqrt(2)/(1-1/sqrt(2)),4.8,.008)
t=1+sqrt(2*20/g)
v0=g*(t-.5)/t
heights=[.5*g*(.5*g/(g-v)-1)**2 for v in [6,9.5]]
check('2.89-a-verified',v0,8.17764733845052)
check('2.89-bcd',[*heights,g,g/2],[.411,1150,9.8,4.9])

# Đáp án đại số và các điều kiện nghiệm được kiểm bằng các giá trị thử.
for at,ac,vc in [(2,1,5),(1.2,3.4,10)]:
    t=2*vc/(at+ac)
    assert isclose(.5*at*t*t,vc*t-.5*ac*t*t)
    assert isclose(.5*at*t*t,2*at*vc**2/(at+ac)**2)
for H in [1,3,10]:
    v0=sqrt(2*g*H)
    assert isclose(sqrt(v0*v0-2*g*H/2)/v0,1/sqrt(2))
    assert isclose((v0*v0-(v0/2)**2)/(2*g),3*H/4)
for v0 in [5,12,20]:
    for t,h in [(v0/g,v0*v0/(2*g)),(v0/(2*g),3*v0*v0/(8*g)),(3*v0/(2*g),3*v0*v0/(8*g))]:
        assert isclose(v0*t-.5*g*t*t,h)

check('2.90',.8/.250,3.2)
check('2.91-area-ratio',(1/sqrt(2))**2*2,1)
text='\n'.join(p.read_text(encoding='utf8') for p in sorted((ROOT/'raw_materials/physics/translations/chapter-02').glob('*.md')))
for n in range(1,93):
    assert re.search(rf'^::: exercise 2\.{n}(?: |\n)',text,re.M), f'Missing exercise 2.{n}'
for n in range(1,23):
    assert re.search(rf'^::: exercise Q2\.{n}\n',text,re.M), f'Missing Q2.{n}'
for section in [5,7,8]:
    for n in range(1,5):
        assert text.count(f'::: exercise VP2.{section}.{n}\n')==1

report={"chapter":2,"status":"passed","numericGroups":len(checks),"checks":checks,
        "sourceErrors":[{"location":"2.7(c), appendix A-9","printed":"13.3 m/s","correction":"13.3 s"},
                        {"location":"2.69(b), appendix A-9","printed":"negative acceleration magnitude","correction":"signed ax=-40 m/s²; magnitude40 m/s² toward-x"},
                        {"location":"2.52(c)","printed":"ay,vy","correction":"ax,vx for the motion along x"},
                        {"location":"Figure2.28","printed":"area under x-t graph","correction":"area under ax-t graph"},
                        {"location":"2.89(a), appendix A-9","printed":"8.3 m/s","correction":"8.18 m/s with g=9.80 m/s²"}]}
out=ROOT/'qa/physics/chapter2-completion/numeric-checks.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(f'Passed {len(checks)} numeric groups, algebraic answer checks, 92 exercises, 22 questions and 12 variation problems.')
