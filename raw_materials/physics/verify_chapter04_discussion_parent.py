"""Independent numerical checks for Chapter4 conceptual discussions."""
from math import pi,sqrt,isclose
import json
g=9.8
values={
 'Q4.11_earth_spin_acceleration_m_s2':4*pi*pi*6380e3/(24*3600)**2,
 'Q4.11_earth_orbit_acceleration_m_s2':4*pi*pi*1.496e11/(365.25*24*3600)**2,
 'Q4.16_weight_1kg_N':g,'Q4.16_weight_10kg_N':10*g,
 'Q4.19_freefall_speed10m_m_s':sqrt(2*g*10),
 'Q4.23_weight10kg_N':10*g,'Q4.23_weight20kg_N':20*g,
 'Q4.24_weight1kg_earth_lb':g/4.448221615260,
 'Q4.24_weight1kg_moon_lb':1.62/4.448221615260,
 'Q4.31_contact_N':50/(150+50)*100,
 'Q4.37_acceleration_ratio':2500/1000,
}
assert isclose(values['Q4.31_contact_N'],25)
assert isclose(values['Q4.37_acceleration_ratio'],2.5)
assert isclose(values['Q4.19_freefall_speed10m_m_s'],14)
assert .033<values['Q4.11_earth_spin_acceleration_m_s2']<.035
assert .0058<values['Q4.11_earth_orbit_acceleration_m_s2']<.0061
print(json.dumps({'status':'passed','scope':'Numerical illustrations; conceptual reasoning reviewed separately','values':values},indent=2))
