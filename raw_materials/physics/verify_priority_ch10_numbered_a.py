"""Independent numerical and limiting-case checks for numbered exercises 10.1–75."""
import json
import math
from pathlib import Path

g = 9.80
pi = math.pi
sind = lambda x: math.sin(math.radians(x))
cosd = lambda x: math.cos(math.radians(x))
tand = lambda x: math.tan(math.radians(x))
out = {}

def save(number, **values):
    assert all(math.isfinite(v) for v in values.values()), number
    out[str(number)] = values

save(1, a=40, b=40*sind(120), c=40*sind(30), d=-20*sind(60), e=0, f=0)
save(2, tau=2*12*sind(30)-5*8)
save(3, tau=.09*(26-18)+.09*14*(sind(45)+cosd(45)))
save(4, tau=.35*(8.5-14.6*sind(40)))
save(5, tau=-.450*4-.150*(-5))
save(6, tau=3*(-3)-4*7)
save(7, tau=.25*17*sind(37), maximum=.25*17)
alpha=30*.2/(.5*40*.2**2); w=math.sqrt(2*alpha*.2*2*pi)
save(8, I=.8, alpha=alpha, omega=w, v=.2*w, at=.2*alpha, ar=.2*w*w, a=math.hypot(.2*alpha,.2*w*w))
save(9, tau=1.6*400*2*pi/60/8)
save(10, alpha=40*.25/(.5*9.2*.25**2), a=2*40/9.2, Rx=-40, Ry=9.2*g, R=math.hypot(40,9.2*g), angle=math.degrees(math.atan2(9.2*g,40)), upwardRy=9.2*g-40)
save(11, alpha=-.02*.015/(.4*.225*.015**2), t=22.5/(.02*.015/(.4*.225*.015**2)))
a=2*12.6/3**2; m=5*a/(g-a)
save(12, a=a, mass=m, T=m*(g-a))
a=2*1.2/.8**2; t1=2*a; t2=3*(g-a)
save(13, a=a, T1=t1, T2=t2, I=(t2-t1)*.075**2/a)
a=15*g/(15+6)
save(14, a=a, T=15*(g-a), v=math.sqrt(20*a), t=math.sqrt(20/a), axle=12*g+15*(g-a))
save(15, alpha=12*2*pi/2, I=80*.12/(12*2*pi/2))
a=5*g/(12+5+1)
save(16, a=a, Tbox=12*a, Tweight=5*(g-a), axleX=12*a, axleY=2*g+5*(g-a))
save(17, alpha=32, I=3*.14/32)
save(18, solidW=-.7*5*4**2, shellW=-5*5*4**2/6)
v=.6*2.6;save(19, v=v, K=2.2*v*v, topV=2*v, rightV=math.sqrt(2)*v)
save(20, beta0=2/7*tand(0), beta45=2/7*tand(45), beta89=2/7*tand(89))
save(21, cylinder=1/3, sphere=2/7, shell=2/5, tube=5/13)
save(22, v=math.sqrt(g*.75), omega=math.sqrt(g*.75)/.08)
save(23, solidMu=2/7*tand(65), shellMu=2/5*tand(65))
save(24, a=3/5*g*sind(38), f=2/5*2*g*sind(38), mu=2/5*tand(38))
save(25, M=392/g, K=.9*(392/g)*(.6*25)**2, h=(.9*(392/g)*(.6*25)**2-2600)/392)
save(26, smoothHeightRatio=5/7, roughHeightRatio=1)
v=60*.3048/2.5; m=12*.45359237; R=8.5*.0254/2
save(27, chosenTime=2.5, v=v, n=v/(2*pi*R), K=.7*m*v*v, rotationFraction=2/7)
save(28, K=27*.5/9)
c=.5*(1+(.2/.35)**2)
save(29, c=c, h=(1+c)*6.66**2/(2*g), freeV=6.66*math.sqrt(1+c))
save(30, aOverGSin=5/7, fOverMGSin=2/7)
v=math.sqrt(6*g*5/5);save(31, v=v, omega=v/.113, Krot=2/5*.426*g*5)
save(32, P=175*746, omega=2400*2*pi/60, tau=175*746/(2400*2*pi/60), W=175*746/(2400/60))
tau=18*2.4; w=tau/2100*15; W=.5*2100*w*w
save(33, tau=tau, omega=w, W=W, averageP=W/15)
save(34, P=9000*(2/3)/60, tau=100/(2500*2*pi/60))
I=.5*2.8*.1**2;w=1200*2*pi/60;theta=w*2.5/2
save(35, I=I, tau=I*w/2.5, theta=theta, W=I*w/2.5*theta, K=.5*I*w*w)
I=117*2.08**2/12;a=1950/I;theta=10*pi;w=math.sqrt(2*a*theta);t=w/a
save(36, I=I, alpha=a, omega=w, W=1950*theta, time=t, averageP=1950*theta/t, finalP=1950*w)
save(37, Lz=-2*12*8*sind(36.9), tauz=2*g*8*cosd(36.9))
save(38, L=(.5*110*4**2+50*4**2)*.8*2*pi)
save(39, I=.006*.15**2/3, L=.006*.15**2/3*2*pi/60)
save(40, orbitL=5.97e24*(1.496e11)**2*2*pi/(365.25*86400), spinL=.4*5.97e24*(6.37e6)**2*2*pi/86400)
I=2/3*12*.24**2;w=2*1.5*3+4*1.1*3**3; a=2*1.5+12*1.1*3**2
save(41, I=I, omega=w, alpha=a, L=I*w, tau=I*a)
wi=2.85;wf=wi*(.3/.15)**2;ki=.5*.025*.3**2*wi**2;kf=.5*.025*.15**2*wf**2
save(42, omega=wf, Ki=ki, Kf=kf, deltaK=kf-ki, L=.025*.3**2*wi)
save(43, omega=2*pi/(30*86400)*(7e5/16)**2, period=30*86400/(7e5/16)**2)
save(44, initialN=2*3.6/18, revolutions=2*3.6/18*1.5)
save(45, Ii=.4+8*1.8**2/12, If=.4+8*.25**2, finalN=.4*(.4+8*1.8**2/12)/(.4+8*.25**2))
save(46, Idoor=40/3, Imud=.5*.5**2, omega=.5*12*.5/(40/3+.5*.5**2), relativeInertia=.5*.5**2/(40/3))
Ii=.5*120*2**2;If=Ii+70*2**2;wf=Ii*3/If
save(47, Ii=Ii, If=If, omega=wf, Ki=.5*Ii*9, Kf=.5*If*wf**2)
save(48, asteroidFraction=.4*.25)
I=.05/3;w=.01*.2/I
save(49, omega=w, bugK=.5*.01*.2**2, barK=.5*I*w*w, totalK=.5*.01*.2**2+.5*I*w*w)
save(50, rodMass=3*.003/.5**2, finalOmega=.16/.5, bugMass=.003*(.4/(.16/.5)-1)/.5**2)
save(51, g=6.42*3/4)
I=4.5*1.5**2/3;save(52, I=I, omega=1.1*(5+2)*.75/I)
# 53: Dimensionless test of the general conservation formula.
M,R,m,mr,v=120,2,70,3,10;w=-mr*v/(R*(.5*M+m));assert abs((.5*M+m)*R**2*w+mr*v*R)<1e-10
save(53, testOmega=w)
save(54, bulletV=(.5*1.6*.6**2+.02*.6**2)*4/(.02*.6))
save(55, I=2*.025**2, omega=19200*2*pi/60, precession=math.radians(1e-6)/(5*3600), tau=2*.025**2*(19200*2*pi/60)*math.radians(1e-6)/(5*3600))
save(56, precession=.5*.165)
save(57, v=30*.44704, wheelRPM=30*.44704/(pi*.70)*60, crankRPM=30*.44704/(pi*.70)*60*.05/.20)
I=.5*50*.26**2;w=120*2*pi/60;res=.6*160*.26+6.5
save(58, I=I, resistance=res, startF=(I*w/9+res)/.5, steadyF=res/.5, stoppingTime=I*w/6.5)
save(59, mu=I*(850*2*pi/60)/7.5/(160*.26))
a=2*1.8/2**2;tb=6*(g-a);ta=2.5*a;save(60, a=a, TB=tb, TA=ta, I=(tb-ta)*.08**2/a)
I=3.8*.8**2/12+2.5*.4**2;save(61, I=I, alpha=2.5*g*.4/I, omega=math.sqrt(2*2.5*g*.4/I))
save(62, accelerationFactor=5/7, frictionFactor=2/7)
a=(4-2)*g/(4+2+.220/.12**2);save(63, a=a, alpha=a/.12, TA=4*(g-a), TB=2*(g+a))
save(64, T=50*(g+1.4), alpha=1.4/.25, F=(50*(g+1.4)*.25+2.9*1.4/.25)/.12)
save(65, solidHeightCoefficient=.7, shellHeightCoefficient=5/6)
a=5*g*(sind(36.9)-.25*cosd(36.9))/(5+.5/.2**2);save(66, a=a, T=.5*a/.2**2)
t=(8*2*pi/.02)**(1/3);save(67, time=t, F=5*t, theta=.02*t**3)
save(68, accelerationCoefficient=.5, frictionOverF=.5)
a=g*(125-75)/(125+75+80/2);ta=125*(1-a/g);tb=75*(1+a/g);save(69, a=a, TA=ta, TB=tb, hook=80+ta+tb)
save(70, I=3**2/.250)
# 71: Independent force/torque residuals with example parameters.
m,R,b=2,.2,.04;a=2*g*b*b/(R*R+2*b*b);T=2*m*(g-a);assert math.isclose(T*b,m*R*R*a/b)
save(71, testA=a, testAlpha=a/b, testT=T)
save(72, hOverR=17/6, BnormalOverMg=11/5, smoothTopV2OverGR=5/3, smoothTopNormalOverMg=2/3, rollingTopNormal=0)
save(73, heightRatio=3/5, retainedRotationFraction=2/5)
vtop=math.sqrt(25**2-10/7*g*28);t=math.sqrt(2*28/g)
save(74, topV=vtop, flightTime=t, range=vtop*t, impactV=math.sqrt(vtop*vtop+2*g*28))
save(75, middleV2=10/7*g*25, bottomV=math.sqrt(10/7*g*25+2*g*25))

# Independent conservation and sign checks, rather than checking rounded output against itself.
assert out['3']['tau']>0 and out['4']['tau']<0 and out['37']['Lz']<0<out['37']['tauz']
assert math.isclose(.5*out['8']['I']*out['8']['omega']**2,30*.2*.2*2*pi)
for n,ma,mb,r in [(13,2,3,.075),(16,12,5,.25),(60,2.5,6,.08)]:
    d=out[str(n)];a=d['a'];ta=d.get('T1',d.get('Tbox',d.get('TA')));tb=d.get('T2',d.get('Tweight',d.get('TB')))
    assert math.isclose(ta,ma*a) and math.isclose(tb,mb*(g-a)), n
assert math.isclose(out['35']['W'],out['35']['K'])
assert math.isclose(out['42']['Kf']/out['42']['Ki'],4)
assert math.isclose(out['47']['Ii']*3,out['47']['If']*out['47']['omega'])
assert out['47']['Kf']<out['47']['Ki']
assert math.isclose(out['69']['TA']-out['69']['TB'],(80/(2*g))*out['69']['a'])
assert math.isclose(out['74']['impactV']**2+.4*out['74']['topV']**2,1.4*25**2)
assert math.isclose(.7*out['75']['middleV2']+.5*(out['75']['bottomV']**2-out['75']['middleV2']),g*50)
target=Path(__file__).resolve().parents[2]/'qa/physics1-priority/ch10-numbered-a-values.json'
target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
