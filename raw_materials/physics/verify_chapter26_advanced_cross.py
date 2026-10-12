"""Independent spot checks for advanced Chapter 26 exercises and P26.85 units."""
from math import log, sqrt


def solve_2(a, b, c, d, e, f):
    det = a * d - b * c
    return (e * d - b * f) / det, (a * f - e * c) / det


def close(actual, expected, tol=1e-8):
    assert abs(actual - expected) <= tol * max(1.0, abs(expected)), (actual, expected)


# P26.62: nodal analysis checks the bridge currents and source power.
vl62, vr62 = solve_2(2.5, -1.0, -1.0, 2.5, 14.0, 7.0)
i62 = ((14 - vl62), vl62 / 2, (14 - vr62) / 2, vr62, vl62 - vr62)
close(vl62, 8.0)
close(vr62, 6.0)
close(sum(i62[:2]), 10.0)
close(sum(i62[2:4]), 10.0)
close(sum(i * i * r for i, r in zip(i62, (1, 2, 2, 1, 1))), 140.0)

# P26.63: preserve the source drawing's emf polarity as the sign convention.
r_upper = 1 / (1 / 30 + 1 / 60 + 1 / 60 + 1 / 30)
v_bottom = -5 - 2 * r_upper - 2 * 5 - 10
i20 = v_bottom / 20
i15 = 2 - i20
emf63 = v_bottom - 15 * i15
close(emf63, -108.75)
close(60 / ((2 * r_upper / 30) ** 2 * 10), 13.5)

# P26.67: open-switch divider and closed-switch nodal solution.
close(36 * 3 / 9 - 36 * 6 / 9, -12)
va67, vb67 = solve_2(1 / 6 + 1 / 3 + 1 / 3, -1 / 3,
                     -1 / 3, 1 / 3 + 1 / 6 + 1 / 3, 6, 12)
close(va67, 108 / 7)
close(vb67, 144 / 7)
close((vb67 - va67) / 3, 12 / 7)
close(36 / ((36 - va67) / 6 + (36 - vb67) / 3), 4.2)

# P26.68: the same applied voltage makes the power ratio nine.
close(45 * 9, 405)

# P26.70: capacitor short at t=0+ and open at long time.
i1_70 = 42 / (8 + 1 / (1 / 6 + 1 / 3))
vbranch70 = 42 - 8 * i1_70
close(i1_70, 4.2)
close(vbranch70 / 6, 1.4)
close(vbranch70 / 3, 2.8)
close(4e-6 * 42 * 6 / (8 + 6), 72e-6)

# P26.71: charge continuity at insertion and energy balance after recharging.
eps0 = 8.8541878128e-12
c0 = eps0 * (0.02**2) / 0.003
q0 = 10 * c0
v_insert = q0 / (12 * c0)
i_insert = (10 - v_insert) / 10
u_insert = 0.5 * 12 * c0 * v_insert**2
u_final = 0.5 * 12 * c0 * 10**2
energy_battery = 10 * (12 * c0 * 10 - q0)
energy_resistor = 0.5 * 12 * c0 * (10 - v_insert) ** 2
close(i_insert, 11 / 12)
close(u_insert, 4.92e-12, tol=1e-2)
close(energy_battery, (u_final - u_insert) + energy_resistor)

# P26.75: conserve charge on the conductor formed by joining the two midpoints.
vb75 = (6 * 18 - 54) / 9
close(vb75, 6)
close(6 * (18 - vb75), 72)
close(3 * vb75, 18)

# P26.82: charge/discharge time constants and cycle frequency.
rc = 10e3 * 10e-6
period = rc * (4 * log(2) + 0.8 * log(3.5))
close(1 / period, 2.65, tol=2e-3)

# P26.83: positive self-similar ladder root.
r1, r2 = 6.4e3, 8e8
rt = r1 + sqrt(r1**2 + 2 * r1 * r2)
close(rt, 3.2064e6, tol=2e-4)

# P26.85: the source figure/text uses 1.0 μm per segment, so 2.0 mm is 2000 segments.
beta = 2 * r1 * (rt + r2) / (rt * r2)
segments = 2e-3 / 1e-6
remain = (1 + beta) ** -segments
close(segments, 2000)
close(beta, 4.01e-3, tol=2e-3)
close(remain, 3.3546e-4, tol=2e-4)
r2_myelin = 3.3e12
rt_myelin = r1 + sqrt(r1**2 + 2 * r1 * r2_myelin)
beta_myelin = 2 * r1 * (rt_myelin + r2_myelin) / (rt_myelin * r2_myelin)
remain_myelin = (1 + beta_myelin) ** -segments
close(rt_myelin, 2.055e8, tol=2e-3)
close(remain_myelin, 0.88289, tol=2e-4)

print("PASS: independent spot checks for P26.62–26.85")
print(f"P26.63: emf={emf63:.2f} V in drawn polarity; heating time={13.5:.1f} s")
print(f"P26.85 unmyelinated: RT={rt:.5g} ohm, beta={beta:.5g}, n={segments:.0f}, remaining={remain:.6g}, decrease={1-remain:.5%}")
print(f"P26.85 myelinated: RT={rt_myelin:.5g} ohm, beta={beta_myelin:.5g}, remaining={remain_myelin:.5g}, decrease={1-remain_myelin:.5%}")
