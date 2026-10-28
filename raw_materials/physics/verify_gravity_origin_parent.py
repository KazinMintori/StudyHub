import math
m=.145;g=9.8;initialSpeed=20.;rise=initialSpeed**2/(2*g)
assert math.isclose(rise,20.408163265306122)
assert math.isclose((m*initialSpeed**2/2+m*g*5)/(m*g),rise+5)
assert math.isclose(m*g*(rise+5)-m*g*5,m*initialSpeed**2/2)
for v1,v2,y1,y2,otherWork in[(20,0,0,rise,0),(0,4,1,3,m*8+m*g*2)]:
 assert math.isclose(m*(v1*v1/2+g*y1)+otherWork,m*(v2*v2/2+g*y2),abs_tol=1e-9)
print('PASS5assertions: Origin shift and equivalent energy balances, with and without nongravitational work.')
