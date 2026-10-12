"""Independent numerical and nodal checks for Chapter 25 problems 31–58."""

from math import isclose, pi, sqrt

import numpy as np


def close(actual, expected, rel=2e-3, abs_tol=1e-12):
    assert isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol), (actual, expected)


# Nodal solution for Fig. E25.30. Nodes are a, b, c, with d as ground.
# Each battery is modeled as an ideal emf in series with its internal resistance.
def solve_e2530(top_emf_ab):
    rt, rb = 1.6, 1.4
    Rleft, Rright = 5.0, 9.0
    bottom_emf_dc = 8.0  # positive terminal is at d, negative terminal at c
    matrix = np.array(
        [
            [1 / Rleft + 1 / rt, -1 / rt, 0.0],
            [-1 / rt, 1 / rt + 1 / Rright, -1 / Rright],
            [0.0, -1 / Rright, 1 / Rright + 1 / rb],
        ],
        dtype=float,
    )
    rhs = np.array(
        [top_emf_ab / rt, -top_emf_ab / rt, -bottom_emf_dc / rb],
        dtype=float,
    )
    va, vb, vc = np.linalg.solve(matrix, rhs)
    i_top_a_to_b = (va - vb - top_emf_ab) / rt
    i_bottom_d_to_c = (0.0 - vc - bottom_emf_dc) / rb
    i_left_a_to_d = va / Rleft
    i_right_c_to_b = (vc - vb) / Rright
    close(i_top_a_to_b + i_left_a_to_d, 0.0, rel=1e-10)
    close(i_bottom_d_to_c, i_left_a_to_d, rel=1e-10)
    close(i_right_c_to_b, i_bottom_d_to_c, rel=1e-10)
    return va, vb, vc, i_top_a_to_b, i_bottom_d_to_c


# Problems 25.31 and 25.39: original and reversed polarities.
va, vb, vc, i_top_original, i_bottom_original = solve_e2530(+16.0)
close(i_top_original, -8 / 17)
close(i_bottom_original, 8 / 17)
close(va - vb, 16.0 - (8 / 17) * 1.6)
close(va - vc, 16.0 - (8 / 17) * 1.6 - (8 / 17) * 9.0)

va_rev, vb_rev, vc_rev, i_top_reversed, _ = solve_e2530(-16.0)
close(i_top_reversed, 24 / 17)
close(va_rev - vb_rev, -16.0 + (24 / 17) * 1.6)
assert i_top_reversed > 0  # current flows clockwise through the top branch

# 25.32–25.38.
i_32 = 27.0 / 9.0
r_32 = (30.0 - 27.0) / i_32
close(r_32, 1.0)

roots_33 = np.roots([7.0, -150.0, 63.0])
assert np.allclose(sorted(roots_33), [3 / 7, 21.0], rtol=1e-12)

r_34 = 1.5**2 / 0.0625
close((12.6**2) / r_34, 4.41)
close(sqrt(5.0 * r_34), sqrt(180.0))

close(120**2 / 100, 144.0)
close(120**2 / 60, 240.0)
close(100 / 120, 5 / 6)
close(60 / 120, 0.5)
close((220.0**2) / (120.0**2 / 75.0), 252.0833333333)
close(120.0**2 / (220.0**2 / 100.0), 29.7520661157)
close(120.0 / (220.0**2 / 100.0), 120 / 484)
close(9.0 * 0.13 * 30 * 60, 2106.0)

# Fig. E25.26 provides a 4.00 A current.
close((24.0 - 21.2) / 4.0, 0.70)
close(21.2 / 4.0, 5.30)

# 25.27 ideal voltmeter draws no current; the 2-ohm load is in series with r.
i_27 = 5.0 / (2.0 + 0.5)
close(i_27, 2.0)
close(i_27 * 2.0, 4.0)

# 25.28 the ideal ammeter shorts the battery terminals.
close(10.0 / 2.0, 5.0)
close(0.0 / 4.0, 0.0)

i_29 = 1.65
emf_29 = 3.08
terminal_29 = 2.97
close((emf_29 - terminal_29) / i_29, 0.0666666667)
close(terminal_29 / i_29, 1.8)

# 25.33/25.39: power flow around the original two-source loop.
i_39 = 8 / 17
p_load_39 = i_39**2 * (5.0 + 9.0)
p_16_terminal_out = i_39 * (16.0 - i_39 * 1.6)
p_8_terminal_in = 8.0 * i_39 + i_39**2 * 1.4
close(p_load_39, 3.10034602076)
close(p_16_terminal_out, p_load_39 + p_8_terminal_in)

# Problems 25.33–25.58: direct independent calculations.
close(500.0 * 0.080, 40.0)
close(40.0 * 0.010, 0.4)
close(25.0 * 12.0, 300.0)
close(300.0 * 0.003, 0.9)
close(3.15e4 / (3.70 * 5.25 * 3600), 0.4507, rel=1e-3)

energy_battery = 12.0 * 60.0 * 3600.0
close(energy_battery, 2.592e6)
gas_volume_l = energy_battery / 4.6e7 / 900.0 * 1000.0
close(gas_volume_l, 0.06260869565)
close(energy_battery / 450.0 / 3600.0, 1.6)

i_44 = sqrt(96.0 / 12.0)
close(i_44 * (12.0 + 2.0), 39.59797975)
close(3.5 / (25.0 + 3.5) * 100.0, 12.28070175)

p_46 = 3.0**2 / 17.0
close(p_46, 9 / 17)
close(p_46 * 5.0 * 3600.0, 9529.4117647)
close((sqrt(2.0) - 1) * 17.0, 7.04163056)

current_47 = 12.0 / (1.0 + 5.0)
close(current_47 * 12.0, 24.0)
close(current_47**2 * 1.0, 4.0)
close(current_47**2 * 5.0, 20.0)

r_48 = 120.0**2 / 540.0
close(r_48, 26.66666667)
close(540.0 / 120.0, 4.5)
close(110.0**2 / r_48, 453.75)

# 25.49 Drude model and density comparison against the source Example 25.11.
m_e, e = 9.11e-31, 1.60e-19
tau_si = m_e / (1.0e16 * e**2 * 2300.0)
tau_cu = 2.4e-14
rho_ratio = (8.5e28 * tau_cu) / (1.0e16 * tau_si)
close(tau_si, 1.54e-12)
close(rho_ratio, 1.32e11, rel=0.01)
close(2300.0 / 1.72e-8, 1.34e11, rel=0.02)

# Unit conversions and symbolic estimates in 25.50–25.52.
assert 1.0e-3 * 3600.0 == 3.6  # 1 mAh is 3.6 coulombs
assert 3600.0 / 4190.0 < 1.0
close(4190.0 * 25.0 / 5400.0, 19.39814815)
close(220.0**2 / (4190.0 * 25.0 / 5400.0), 2495.086)

# 25.51 conductor.
d_51, L_51, R_51 = 2.50e-3, 14.0, 0.104
A_51 = pi * d_51**2 / 4.0
rho_51 = R_51 * A_51 / L_51
J_51 = 1.28 / rho_51
I_51 = J_51 * A_51
v_51 = J_51 / (8.5e28 * e)
close(rho_51, 3.64e-8)
close(I_51, 172.0)
close(v_51, 2.58e-3)

# 25.53 resistance per length, from two loaded battery readings.
x_53 = (12.6 / 4.2 - 12.6 / 7.0) / 20.0
close(x_53, 0.0600)

# 25.54 limits and 25.55 serial wire segments.
close(15.0 / 4.0, 3.75)
rho_cu = 1.72e-8
i_55 = 2.5e-3
A1 = pi * (1.60e-3) ** 2 / 4.0
A2 = pi * (0.80e-3) ** 2 / 4.0
E1 = rho_cu * i_55 / A1
E2 = rho_cu * i_55 / A2
V55 = E1 * 1.20 + E2 * 1.80
close(E1, 2.14e-5)
close(E2, 8.55e-5)
close(V55, 1.80e-4)

# 25.56 constant-voltage tungsten element.
close(480.0 * (1.0 + 0.0045 * (80.0 - 20.0)) / (1.0 + 0.0045 * (150.0 - 20.0)), 384.6056782)

# 25.57 lightning pulse and 25.58 two load resistances.
delta_t_57 = (25000.0**2 * 1000.0 * 40e-6) / (75.0 * 4190.0)
close(delta_t_57, 79.6, rel=0.01)
assert 37.0 + delta_t_57 > 100.0  # the lumped liquid-water model reaches boiling first
roots_58 = np.roots([1.0, -1.0, 0.16])
assert np.allclose(sorted(roots_58), [0.2, 0.8], rtol=1e-12)

print(f"E25.30 nodal currents: original I(loop)={8/17:.6f} A counterclockwise; reversed I={24/17:.6f} A clockwise")
print(f"25.31 V_ab={va_rev-vb_rev:.6f} V; 25.39 load={p_load_39:.4f} W, 16-V terminal output={p_16_terminal_out:.4f} W, 8-V terminal input={p_8_terminal_in:.4f} W")
print(f"25.43 U={energy_battery:.4g} J, gasoline={gas_volume_l:.5g} L, charging time={1.6:.3g} h")
print(f"25.49 tau_Si={tau_si:.4g} s; rho_Si/rho_Cu≈{rho_ratio:.4g}")
print(f"25.51 rho={rho_51:.4g} ohm m, I={I_51:.4g} A, drift speed={v_51:.4g} m/s")
print(f"25.55 E_large={E1:.4g} V/m, E_small={E2:.4g} V/m, V_total={V55:.4g} V")
print(f"25.57 lumped-water temperature rise={delta_t_57:.4g} K; final model temperature={37.0+delta_t_57:.4g} C; 25.58 R={sorted(roots_58)} ohm")
print("All numerical, current-direction, and power-balance checks for Problems 25.31–25.58 passed.")
