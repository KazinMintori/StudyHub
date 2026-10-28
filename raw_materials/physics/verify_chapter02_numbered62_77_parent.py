from pathlib import Path
import math,json,hashlib
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pymupdf
ROOT=Path(__file__).resolve().parents[2];checks=[];values={}
def ck(unit,key,actual,expected,tol=1e-9):
 assert math.isclose(actual,expected,rel_tol=tol,abs_tol=tol),(unit,key,actual,expected)
 checks.append({'unit':unit,'quantity':key,'computed':float(actual),'expected':float(expected)})
g=9.8
xp=lambda t:25*t-.05*t*t;xf=lambda t:200+15*t
t62=brentq(lambda t:xp(t)-xf(t),0,100);x62=xp(t62)
ck('2.62','firstcollisiontime',t62,(10-math.sqrt(60))/.1);ck('2.62','collisionposition',x62,xf(t62));assert t62<100
values['2.62']={'t':t62,'x':x62,'vPassenger':25-.1*t62,'laterFormalRoot':(10+math.sqrt(60))/.1}
a63=200/(.5*(100-25));ck('2.63','firstdistance',quad(lambda t:a63*t,0,5)[0],200/3);ck('2.63','seconddistance',quad(lambda t:a63*t,5,10)[0],200)
for t,want,vel in[(2,24,8),(6,24,-8),(4+2*math.sqrt(7),-24,-8*math.sqrt(7))]:
 ck('2.64','positionAt'+str(t),16*t-2*t*t,want);ck('2.64','velocityAt'+str(t),16-4*t,vel)
t65=math.sqrt(120/2.1);gap65=.5*(3.4-2.1)*t65*t65
ck('2.65','truckDistance',quad(lambda t:2.1*t,0,t65)[0],60);ck('2.65','carMeetingPosition',-gap65+.5*3.4*t65*t65,60)
values['2.65']={'t':t65,'gap':gap65,'truckSpeed':2.1*t65,'carSpeed':3.4*t65}
t66=brentq(lambda t:.48*t*t-5*t-12,0,30);u66=.96*t66
ck('2.66','catchDistance',.48*t66*t66,12+5*t66);ck('2.66','catchSpeed',u66,5+math.sqrt(48.04));values['2.66']={'t':t66,'distance':.48*t66*t66,'speed':u66,'kmph':3.6*u66}
a67=100/31.5;ck('2.67','totalDistance',.5*a67*9+(a67*3)*9,100);values['2.67']={'a':a67}
t68=math.sqrt(2);x68=quad(lambda t:4-2*t*t,0,t68)[0];ck('2.68','maximumPosition',x68,8*math.sqrt(2)/3);ck('2.68','stationaryVelocity',4-2*t68*t68,0)
t69=brentq(lambda t:quad(lambda z:8*z-4*z**3,0,t)[0],1.5,3);ck('2.69','nonzeroReturn',t69,2);ck('2.69','returnVelocity',8*t69-4*t69**3,-16);ck('2.69','returnAcceleration',8-12*t69*t69,-40)
t70=math.sqrt(2*(46-1.8)/g);ck('2.70','dropHeight',.5*g*t70*t70,44.2);values['2.70']={'fallTime':t70,'professorBeforeTargetDistance':1.2*t70}
v71=lambda t:-4+quad(lambda z:-2+3*z,0,t)[0];ck('2.71','returnPosition',quad(v71,0,4)[0],0);ck('2.71','endVelocity',v71(4),12)
for H,u in[(1,2),(20,10),(100,30)]:
 T=(u+math.sqrt(u*u+2*g*H))/g;avg=-H/T
 ck('2.72','velocityAverage'+str(H),avg,(u-math.sqrt(u*u+2*g*H))/2)
w73=(30-.5*g*1.5**2)/1.5;H73=30+w73*w73/(2*g)
ck('2.73','lateDistance',w73*1.5+.5*g*1.5**2,30);ck('2.73','dropSpeed',math.sqrt(2*g*(H73-30)),w73);values['2.73']={'speed30m':w73,'buildingHeight':H73}
w74=(1.9-.5*g*.38**2)/.38;d74=w74*w74/(2*g)
ck('2.74','windowPassDistance',w74*.38+.5*g*.38**2,1.9);ck('2.74','entrySpeedFromDrop',math.sqrt(2*g*d74),w74);values['2.74']={'entrySpeed':w74,'distanceBelowSill':d74}
u75=math.sqrt(2*35*.64);T75=(u75+math.sqrt(u75*u75+2*g*.37))/g
ck('2.75','pushDistance',.5*35*(u75/35)**2,.64);ck('2.75','headReturnHeight',2.2+u75*T75-.5*g*T75*T75,1.83);values['2.75']={'releaseSpeed':u75,'maxHeight':2.2+u75*u75/(2*g),'fromRelease':T75,'fromStartPush':T75+u75/35,'massKg':16*.45359237}
h1=.5*3.5*25**2;u1=3.5*25;a2=(132.5-u1)/10;hcut=h1+quad(lambda z:u1+a2*z,0,10)[0];U=math.sqrt(132.5**2+2*g*hcut);T76=(132.5+U)/g
ck('2.76','uniformStage2Acceleration',a2,4.5);ck('2.76','uniformStage2Distance',hcut-h1,1100);ck('2.76','groundAtEnd',hcut+132.5*T76-.5*g*T76*T76,0,1e-8)
values['2.76']={'stage1Height':h1,'stage1Speed':u1,'stage2NetAccelerationUnderUniformAssumption':a2,'cutoffHeightUnderUniformAssumption':hcut,'maxHeight':hcut+132.5**2/(2*g),'afterCutoffFlightTime':T76,'impactSpeed':U,'limit':'Stage2distance underdetermined without a velocity history; quoted numbers conditional on uniform stage2 acceleration.'}
ck('2.77','flightTimeRatio',(2*3*7/g)/(2*7/g),3);ck('2.77','peakHeightRatio',(3*7)**2/(2*g)/(7**2/(2*g)),9)

print('PASS',len(checks),'independent checks for2.62–2.77.')
