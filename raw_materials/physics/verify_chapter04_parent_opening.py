"""Independent recalculation of Chapter4 numerical examples and self-checks."""
from math import sin,cos,radians,hypot,atan2,degrees,isclose
import json
f3x=-250*cos(radians(53));f3y=250*sin(radians(53))
rx=50+f3x;ry=-120+f3y
assert round(f3x/10)*10==-150
assert round(f3y/10)*10==200
rounded=(-100,80)
assert round(hypot(*rounded))==128
assert round(degrees(atan2(rounded[1],rounded[0])))==141
assert rx<0<ry
assert isclose(hypot(f3x,f3y),250)
assert 20/40==.5
assert (0-2**2)/(2*1)==-2
assert isclose(.45*(-2),-.90)
assert [2/2,8/2,2/8,8/8]==[1,4,.25,1]
assert isclose(80*9.8,784)
assert isclose(80*1.62,129.6)
assert 24500/9.8==2500
assert isclose(-18300/(24500/9.8),-7.32)
assert isclose(1e-3*1e-2,1e-5)
print(json.dumps({'status':'passed','source':'Chapter4 numerical examples and self-checks','unrounded':{'F3':[f3x,f3y],'R':[rx,ry],'magnitude':hypot(rx,ry),'angle_deg':degrees(atan2(ry,rx))},'printed_intermediate_rounding':{'F3':[-150,200],'R':rounded,'magnitude':hypot(*rounded),'angle_deg':degrees(atan2(80,-100))},'additionalChecks':{'4.4_acceleration_m_s2':20/40,'4.5_acceleration_m_s2':-2,'4.5_force_N':-.9,'self4.3_acceleration_rank_values':[1,4,.25,1],'4.6_weight_earth_N':80*9.8,'4.6_weight_moon_N':80*1.62,'4.7_mass_kg':24500/9.8,'4.7_acceleration_m_s2':-18300/(24500/9.8),'dyne_in_newtons':1e-5},'note':'Example4.1 uses explicitly stated intermediate rounding. Example4.7 corrects the printed arithmetic while preserving the question data.'},indent=2))
