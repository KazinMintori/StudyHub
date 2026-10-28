from pathlib import Path
import math,json
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2];checks=[]
def check(unit,name,value,expected,tol=1e-10):
 assert math.isclose(value,expected,rel_tol=tol,abs_tol=tol),(unit,name,value,expected)
 checks.append({'id':unit,'quantity':name,'computed':value,'expected':expected})
check('2.1','positive displacement',6.25*4,25)
check('2.2','return velocity',-5150e3/(13.5*86400),-4.415294924554184);check('2.2','wholeepisode netdisplacement',0,0)
check('2.3','original distance km',105*(1+50/60),192.5)
check('2.3','newtime minutes',192.5/70*60,165);check('2.3','extra minutes',165-110,55)
check('2.4','total time',200/5+280/4,110)
check('2.4','average speed',480/110,48/11);check('2.4','average velocity',(200-280)/110,-8/11)
check('2.5','average velocity',(60-40)/(28+36),.3125);check('2.5','average speed',(60+40)/(28+36),1.5625)
x=lambda t:1.5*t*t-.05*t**3
v=lambda t:3*t-.15*t*t
check('2.6','x2',x(2),5.6);check('2.6','x4',x(4),20.8)
for (a,b,want)in[(0,2,2.8),(0,4,5.2),(2,4,7.6)]:
 check('2.6','interval'+str((a,b)),quad(v,a,b)[0]/(b-a),want)
x=lambda t:2.4*t*t-.12*t**3;v=lambda t:4.8*t-.36*t*t
check('2.7','average0to10',(x(10)-x(0))/10,12)
for t,want in[(0,0),(5,15),(10,12)]:check('2.7','instantaneous at'+str(t),v(t),want)
stop=4.8/.36;check('2.7','rest-root',v(stop),0)
check('2.8','instantaneous at8',12.4-3*.045*8**2,3.76)
for tail in[3,-3]:
 displacement=quad(lambda t:2,0,2)[0]+quad(lambda t:tail,2,3)[0]
 distance=quad(lambda t:abs(2),0,2)[0]+quad(lambda t:abs(tail),2,3)[0]
 check('2.9','displacement tail'+str(tail),displacement,7 if tail>0 else 1)
 check('2.9','distance tail'+str(tail),distance,7)
check('2.11','A/B slope',(40-20)/3,20/3);check('2.11','D/E/F slope',(0-40)/(6-5),-40)
for a,b,va,vb,want in[(0,10,0,60/3.6,5/3),(30,40,60/3.6,0,-5/3),(10,30,60/3.6,60/3.6,0),(0,40,0,0,0)]:
 check('2.12','mean interval'+str((a,b)),(vb-va)/(b-a),want)

print('PASS',len(checks),'independent checks for2.1–2.12.')
