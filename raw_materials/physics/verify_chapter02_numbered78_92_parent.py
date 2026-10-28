from pathlib import Path
import math,json,hashlib
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pymupdf
ROOT=Path(__file__).resolve().parents[2];checks=[];values={};g=9.8
def ck(unit,name,actual,expected,tol=1e-9):
 assert math.isclose(actual,expected,rel_tol=tol,abs_tol=tol),(unit,name,actual,expected)
 checks.append({'unit':unit,'quantity':name,'computed':float(actual),'expected':float(expected)})
a78=16;T78=math.sqrt(2*960/(a78*(1+a78/g)));ck('2.78','maximumHeight',.5*a78*T78*T78+(a78*T78)**2/(2*g),960);values['2.78']={'engineTime':T78}
u79=50;h79=250;TH=(u79+math.sqrt(u79*u79+2*g*h79))/g;yp7=h79+u79*7-.5*g*49;vp7=u79-g*7;dt=TH-7;HP=yp7+vp7*dt-dt*dt
ck('2.79','heliGroundTime',h79+u79*TH-.5*g*TH*TH,0,1e-8);ck('2.79','heightAt7',yp7,359.9);ck('2.79','velocityAt7',vp7,-18.6);assert HP>0
values['2.79']={'maxHeight':h79+u79*u79/(2*g),'heliImpactAfterExit':TH,'PowersHeightAtCrash':HP,'afterJetTime':dt}
tf80=brentq(lambda t:t+.5*g*t*t/330-8,0,8);h80=.5*g*tf80*tf80;ck('2.80','totalDelay',tf80+h80/330,8);assert h80<.5*g*64;values['2.80']={'fallTime':tf80,'height':h80,'ignoredSoundHeight':.5*g*64}
C81=40/64;ck('2.81','finalVelocity',20-.5*C81*64,0);s81=quad(lambda t:20-.5*C81*t*t,0,8)[0];ck('2.81','distance',s81,320/3);values['2.81']={'C':C81,'distance':s81}
for H,u in[(5,10),(10,10),(10,math.sqrt(98))]:
 t=H/u;y1=u*t-.5*g*t*t;y2=H-.5*g*t*t;ck('2.82','sameHeight'+str(H)+str(u),y1,y2)
H=100/g;t=10/g;ck('2.82','meetAtPeak',10*t-.5*g*t*t,H/2)
xA=lambda t:2.6*t+1.2*t*t;xB=lambda t:2.8*t*t-.2*t**3
for t in[0,4-math.sqrt(3),4+math.sqrt(3)]:ck('2.83','samePosition'+str(t),xA(t),xB(t))
for t in[1,13/3]:ck('2.83','sameVelocity'+str(t),2.6+2.4*t,5.6*t-.6*t*t)
ck('2.83','sameAcceleration',2.4,5.6-1.2*(8/3));assert xA(.01)>xB(.01)
x84=np.arange(.5,3.01,.5);t84=np.array([.36,.51,.63,.73,.81,.89]);B84,A84=np.polyfit(t84*t84,x84,1);acc84=2*B84;u84=math.sqrt(2*acc84*1.35)
assert acc84>0;ck('2.84','bestFitCenteredResidual',float(np.sum((x84-A84-B84*t84*t84)*(t84*t84-np.mean(t84*t84)))),0)
values['2.84']={'timeReadApproximately':t84.tolist(),'positionRead':x84.tolist(),'fitPositionIntercept':A84,'fitXSlope':B84,'acceleration':acc84,'speedFrom1p35':u84,'limit':'Approximate point readings from original graphic, not exact supplied data. Unconstrained OLS x vs t^2 with intercept.'}
ck('2.85','vacuumSlope',1/(2*g),.0510204081632653)
ta=np.arange(6.);aa=np.array([5.95,5.52,5.08,4.55,3.96,3.40]);B86,A86=np.polyfit(ta,aa,1);c=(ta-ta.mean())*(aa-aa.mean());dd=(ta-ta.mean())**2
ck('2.86','OLSslope',B86,float(c.sum()/dd.sum()));ck('2.86','OLSintercept',A86,float(aa.mean()-B86*ta.mean()))
v86=lambda t:A86*t+.5*B86*t*t;s86=quad(v86,0,5)[0];ck('2.86','speed5',v86(5),23.71666666666667);ck('2.86','distance5',s86,64.63690476190476)
values['2.86']={'fitIntercept':A86,'fitSlope':B86,'tMean':ta.mean(),'aMean':aa.mean(),'N':c.sum(),'D':dd.sum(),'v5':v86(5),'distance5':s86}
tp=1.;tlo=tp*(1-1/math.sqrt(2));thi=tp*(1+1/math.sqrt(2));ck('2.87','durationRatio',(thi-tlo)/tlo,2*(1+math.sqrt(2)));ck('2.87','halfheight',tp*tlo-.5*tlo*tlo,.25)
d88=40;a88=.17;u88=5;disc=u88*u88-2*a88*d88;t1=(u88-math.sqrt(disc))/a88;t2=(u88+math.sqrt(disc))/a88
for t in[t1,t2]:ck('2.88','meetingPosition'+str(t),u88*t,d88+.5*a88*t*t)
umin=math.sqrt(2*a88*d88);ttan=umin/a88;ck('2.88','tangentPosition',umin*ttan,d88+.5*a88*ttan*ttan);ck('2.88','tangentSpeed',a88*ttan,umin);assert 3.5**2-2*a88*d88<0
values['2.88']={'firstTime':t1,'firstDistance':u88*t1,'busSpeed1':a88*t1,'secondTime':t2,'secondDistance':u88*t2,'busSpeed2':a88*t2,'minimumSpeed':umin,'tangentTime':ttan,'tangentDistance':umin*ttan,'gapAt3p5Closest':d88-3.5**2/(2*a88)}
tau=1;T89=tau+math.sqrt(40/g);u89=g*tau-.5*g*tau*tau/T89
ck('2.89','firstGroundAt20',20+u89*T89-.5*g*T89*T89,0);ck('2.89','secondGroundAt20',20-.5*g*(T89-tau)**2,0)
heights={}
for u in[6,9.5]:
 T=g*tau*tau/(2*(g*tau-u));H=.5*g*(T-tau)**2;ck('2.89','simultaneousGround'+str(u),H+u*T-.5*g*T*T,0,1e-8);heights[str(u)]=H
values['2.89']={'speedFor20':u89,'groundTimeFor20':T89,'heights':heights,'vmin':g*tau/2,'vmax':g*tau}
ck('2.90','averageAcceleration',.8/.250,3.2);ck('2.91','twoBranchCombinedArea',2*math.pi*(1/math.sqrt(2))**2/4,math.pi/4)

print('PASS',len(checks),'independent checks for2.78–2.92; graph-read2.84 approximate and2.92qualitative separate.')
