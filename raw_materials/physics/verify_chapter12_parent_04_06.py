"""Independent arithmetic and algebra for the owned Chapter12 theory proposal."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, math
import numpy as np

OUT = Path(__file__).resolve().parent
checks = []

def close(key, value, expected, tolerance=1e-10, note=''):
    value, expected = float(value), float(expected)
    assert math.isclose(value, expected, rel_tol=0, abs_tol=tolerance), (key, value, expected)
    checks.append(dict(id=key, computed=value, expected=expected, tolerance=tolerance, note=note, status='passed'))

# Example12.6: Recompute without substituting rounded intermediate speeds.
Q, rho = 9.5e-3, 850
A1, A2 = math.pi * .04**2, math.pi * .02**2
v1, v2 = Q / A1, Q / A2
close('12.6.volume_flow_m3_s', Q, .0095)
close('12.6.v1_m_s', v1, 1.890, .001)
close('12.6.mass_flow_kg_s', rho * Q, 8.075)
close('12.6.v2_m_s', v2, 7.560, .001)
close('12.6.speed_ratio', v2 / v1, 4)
close('12.4.pipe_2cm_to1cm_ratio', (2/1)**2, 4)
close('12.4.traffic_incompressible_speed_ratio', 3/1, 3)

# Source formulas12.13–18: Exact rational substitutions retain signs and units.
for i, (rho, A1, A2, vin, y1, y2, p1, dt) in enumerate([
    (F(1000), F(4), F(1), F(3,2), F(0), F(5), F(400000), F(1,100)),
    (F(850), F(5), F(2), F(7,10), F(3), F(-2), F(200000), F(1,1000)),
    (F(6,5), F(9), F(4), F(5), F(1), F(6), F(101325), F(1,50)),
]):
    gg = F(49,5)
    vout = A1 * vin / A2
    volume = A1 * vin * dt
    p2 = p1 - rho * (vout**2 - vin**2) / 2 - rho * gg * (y2-y1)
    work = p1*A1*vin*dt-p2*A2*vout*dt
    dk = rho*volume*(vout**2-vin**2)/2
    du = rho*volume*gg*(y2-y1)
    assert work == dk+du
    assert p1+rho*gg*y1+rho*vin**2/2 == p2+rho*gg*y2+rho*vout**2/2
    close(f'12.13-18.case{i}.energy_residual_J', work-dk-du, 0)
    close(f'12.13-18.case{i}.continuity_volume_residual', A1*vin*dt-A2*vout*dt, 0)

# Example12.7: The speed and height contributions must both reduce p2.
rho, g, p1, vin, dh = 1000., 9.8, 4e5, 1.5, 5.
vout = vin*(.02/.01)**2
dp_speed = rho*(vout*vout-vin*vin)/2
dp_height = rho*g*dh
p2 = p1-dp_speed-dp_height
Q = math.pi*.005**2*vout
close('12.7.v2_m_s', vout, 6)
close('12.7.pressure_drop_speed_Pa', dp_speed, 16875)
close('12.7.pressure_drop_height_Pa', dp_height, 49000)
close('12.7.p2_absolute_Pa', p2, 334125)
close('12.7.p2_atm', p2/101325, 3.3, .05)
close('12.7.p2_psi', p2/6894.757293168, 48, .5)
close('12.7.Q_m3_s', Q, .00047, .000005)
close('12.7.Q_L_s', Q*1000, .47, .005)
close('12.7.p2_water_off_Pa', p1-dp_height, 351000)

# Example12.8: A grid verifies efflux/Torricelli substitution, not a new public example.
for i, (rho, h, dp) in enumerate([(700,3,0),(850,2,30000),(1000,4,-10000)]):
    vv = 2*dp/rho+2*g*h
    assert vv > 0
    close(f'12.8.case{i}.Bernoulli_residual_Pa', dp+rho*g*h-rho*vv/2, 0, 1e-8)
    if dp == 0:
        close('12.8.Torricelli_speed_identity', math.sqrt(vv), math.sqrt(2*g*h))

# Example12.9: Both continuity and hydrostatic pressure measurements must agree.
for i, (ratio, h, rho) in enumerate([(4,.3,1000),(2,.7,850),(1.5,1.2,13600)]):
    va = math.sqrt(2*g*h/(ratio**2-1))
    vb = ratio*va
    close(f'12.9.case{i}.pressure_residual_Pa', rho*(vb*vb-va*va)/2-rho*g*h, 0, 1e-8)

# Viscous flow comparisons assume fixed viscosity, length and volume flow rate.
close('12.6.viscosity.half_radius_pressure_ratio', 1/.5**4, 16)
close('12.6.viscosity.90percent_radius_pressure_ratio', 1/.9**4, 1.5241579027587258)
close('12.6.viscosity.90percent_radius_percent_increase', (1/.9**4-1)*100, 52.4, .1)
close('selfcheck12.6.needle_pressure_ratio', (.60/.30)**4, 16)
close('12.11.stroboscope_rotation_rev_s', 1000/8, 125)
close('12.11.stroboscope_rotation_rpm', (1000/8)*60, 7500)
close('12.11.speed_unit_conversion_mph', 35/.44704, 78, .5, 'Source prints35m/s or75mi/h roughly. Teaching keeps35m/s and corrects the conversion to about78mi/h; source discrepancy is recorded privately.')

print(json.dumps(dict(status='passed',count=len(checks),checks=checks),ensure_ascii=False,indent=2))
