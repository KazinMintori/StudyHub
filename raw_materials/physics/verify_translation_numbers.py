"""Tính lại kết quả số của các ví dụ nguyên tác đã dịch."""
from math import sin, cos, acos, atan, atan2, sqrt, radians, degrees
import json
import sys
if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
values={
 'example-1.1-speed-ms':763.0*1.609*1000/3600,
 'example-1.2-volume-cm3':1.84*2.54**3,
 'example-1.2-volume-m3':1.84*2.54**3/100**3,
 'section-1.5-diameter-low':56.47-0.02,
 'section-1.5-diameter-high':56.47+0.02,
 'section-1.5-relative-uncertainty':0.02/56.47,
 'section-1.5-percent-uncertainty':0.02/56.47*100,
 'section-1.5-product':3.1416*2.34*0.58,
 'section-1.5-sum':123.62+8.9,
 'table-1.2-quotient':0.745*2.2/3.885,
 'table-1.2-large-product':1.32578e7*4.11e-3,
 'table-1.2-sum':27.153+138.2-11.74,
 'section-1.5-pi-measured':424/135,
 'section-1.5-ratio':525/311,
 'example-1.3-rest-energy':9.11e-31*(2.99792458e8)**2,
 'question-1.5-density':1.80/6.0e-4,
 'example-1.4-gold-estimate-kg':2*(1e9/100)/1000,
 'example-1.4-volume-estimate':2e4/1e4,
 'example-1.5-distance-km':sqrt(1**2+2**2),
 'example-1.5-angle':degrees(atan(2)),
 'example-1.6-Dx':3*cos(radians(-45)),
 'example-1.6-Dy':3*sin(radians(-45)),
 'example-1.6-Ex':4.50*cos(radians(53)),
 'example-1.6-Ey':4.50*sin(radians(53)),
 'example-1.8-length':sqrt(8**2+11**2+(-10)**2),
 'question-1.9-length':sqrt(3**2+5**2+2**2),
 'example-1.9-dot':4*5*cos(radians(77)),
 'example-1.9-dot-from-rounded-components':2.407*(-3.214)+3.195*3.830,
 'example-1.10-dot':2*(-4)+3*2+1*(-1),
 'example-1.10-angle':degrees(acos(-3/sqrt(14*21))),
 'example-1.11-cross-length':6*4*sin(radians(30)),
 'summary-pi':0.424/(2*0.06750),
}
vectors=[(72.4*cos(radians(58)),72.4*sin(radians(58))),
 (57.3*cos(radians(216)),57.3*sin(radians(216))),(0,-17.8)]
rx=sum(v[0] for v in vectors);ry=sum(v[1] for v in vectors)
values.update({'example-1.7-components':vectors,'example-1.7-Rx':rx,'example-1.7-Ry':ry,
 'example-1.7-length':sqrt(rx*rx+ry*ry),'example-1.7-angle':degrees(atan2(ry,rx))})
assert f'{values["example-1.1-speed-ms"]:.4g}'=='341'
assert f'{values["example-1.2-volume-cm3"]:.3g}'=='30.2'
assert f'{values["example-1.3-rest-energy"]:.3g}'=='8.19e-14'
assert f'{values["example-1.5-distance-km"]:.3g}'=='2.24'
assert f'{values["example-1.7-length"]:.3g}'=='12.7'
assert round(values['example-1.7-angle'])==129
assert f'{values["example-1.8-length"]:.3g}'=='16.9'
assert abs(values['example-1.9-dot']-4.50)<0.005
assert values['example-1.10-dot']==-3
assert abs(values['example-1.11-cross-length']-12)<1e-12
assert f'{values["summary-pi"]:.3g}'=='3.14'
values['opening-north-speed']=15*sin(radians(37))
values['opening-north-displacement']=2*15*sin(radians(37))
values['VP1.7.1-angle']=(degrees(atan2(-ry,-rx))+360)%360
sx=vectors[0][0]-vectors[1][0];sy=vectors[0][1]-vectors[1][1]+vectors[2][1]
values['VP1.7.2']={'length':sqrt(sx*sx+sy*sy),'angle':degrees(atan2(sy,sx))}
tx=rx;ty=ry+vectors[2][1]
values['VP1.7.3']={'x':tx,'y':ty,'length':sqrt(tx*tx+ty*ty),'angle':(degrees(atan2(ty,tx))+360)%360}
dx=38*cos(radians(127))-vectors[0][0];dy=38*sin(radians(127))-vectors[0][1]
values['VP1.7.4']={'length':sqrt(dx*dx+dy*dy),'angle':(degrees(atan2(dy,dx))+360)%360}
values['VP1.10.1-dot']=5*6.4*cos(radians(110+36.9))
cv=(6.50*cos(radians(55)),6.50*sin(radians(55)))
vp_dot=cv[0]*4.80+cv[1]*(-8.40)
values['VP1.10.2']={'dot':vp_dot,'angle':degrees(acos(vp_dot/(6.5*sqrt(4.8**2+8.4**2))))}
values['VP1.10.3-angle']=degrees(acos((-5*2.5+3*4)/(sqrt(34)*sqrt(2.5**2+4**2+1.5**2))))
fy=(26-(-12)*4)/5
values['VP1.10.4']={'Fy':fy,'angle':degrees(acos(26/(sqrt(12**2+fy**2)*sqrt(4**2+5**2))))}
weight=425/cos(radians(35))
values['bridging']={'weight':weight,'work':weight*1.5*sin(radians(35))}
assert f'{values["opening-north-displacement"]:.2g}'=='18'
assert round(values['VP1.7.1-angle'])==309
assert f'{values["VP1.7.2"]["length"]:.3g}'=='115'
assert f'{values["VP1.7.4"]["length"]:.3g}'=='68.7'
assert round(values['VP1.10.3-angle'])==91
values['chapter2-dragster-displacement']=277-19
values['chapter2-dragster-average']=(277-19)/(4-1)
values['chapter2-truck-average']=(19-277)/(25-16)
values['chapter2-swim-speed']=100.0/46.91
values['example-2.1-positions']=[20+5*t*t for t in [1,2,1.1,1.01,1.001]]
values['example-2.1-average']=(40-25)/(2-1)
values['example-2.1-short-averages']=[((20+5*(1+dt)**2)-25)/dt for dt in [0.1,0.01,0.001]]
values['example-2.2-accelerations']=[(1.2-.8)/2,(1.2-1.6)/2,(-1-(-.4))/2,(-.8-(-1.6))/2]
values['example-2.3-velocities']=[60+.5*t*t for t in [1,3,1.1]]
values['example-2.3-average-acceleration']=(64.5-60.5)/2
values['example-2.3-short-averages']=[((60+.5*(1+dt)**2)-60.5)/dt for dt in [.1,.01,.001]]
assert values['chapter2-dragster-average']==86
assert [round(x,5) for x in values['example-2.1-short-averages']]==[10.5,10.05,10.005]
assert [round(x,5) for x in values['example-2.2-accelerations']]==[.2,-.2,-.3,.4]
assert [round(x,5) for x in values['example-2.3-short-averages']]==[1.05,1.005,1.0005]
values['example-2.4']={'x-at-2':5+15*2+.5*4*2**2,'v-at-2':15+4*2,
 'time-at-v25':(25-15)/4,'x-at-v25':5+(25**2-15**2)/(2*4)}
values['example-2.5']={'catch-time':2*15/3,'officer-speed':3*(2*15/3),
 'motorist-displacement':15*(2*15/3),'officer-displacement':.5*3*(2*15/3)**2}
assert values['example-2.4']=={'x-at-2':43,'v-at-2':23,'time-at-v25':2.5,'x-at-v25':55}
assert values['example-2.5']['officer-displacement']==values['example-2.5']['motorist-displacement']==150
values['example-2.6']=[{'t':t,'y':-.5*9.8*t*t,'vy':-9.8*t} for t in [1,2,3]]
values['example-2.7']={'at-1':{'y':15-4.9,'vy':15-9.8},'at-4':{'y':15*4-4.9*4**2,'vy':15-9.8*4},
 'speed-at-y5':sqrt(15**2-2*9.8*5),'max-height':15**2/(2*9.8),'time-at-top':15/9.8}
values['example-2.8']={'at-minus5':[(15+sign*sqrt(15**2-2*9.8*(-5)))/9.8 for sign in [1,-1]],
 'at-plus5':[(15+sign*sqrt(15**2-2*9.8*5))/9.8 for sign in [1,-1]],'discriminant-at-plus15':15**2-2*9.8*15}
values['example-2.9']={'time-at-max':2/.1,'max-v':10+2*20-.5*.1*20**2,
 'position-at-max':50+10*20+.5*2*20**2-(.1/6)*20**3,'stopping-time':(2+sqrt(2**2+4*.05*10))/(2*.05)}
assert f'{values["example-2.7"]["max-height"]:.3g}'=='11.5'
assert f'{values["example-2.8"]["at-minus5"][0]:.3g}'=='3.36'
assert values['example-2.8']['discriminant-at-plus15']<0
assert values['example-2.9']['max-v']==30
assert round(values['example-2.9']['position-at-max'])==517
assert f'{values["example-2.9"]["stopping-time"]:.3g}'=='44.5'
print(json.dumps(dict(status='passed',sourceExamples=list(range(1,12)),values=values),ensure_ascii=False,indent=2))
