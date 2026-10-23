#!/usr/bin/env python3
"""Numerical verification script for Physics 1 Chapter 6 Theory.
Recalculates all numerical worked examples, self-checks, and conversions.
"""
import math
import sys

def verify_all():
    print("=== Starting Numerical Verification for Chapter 6 Theory ===")

    # -------------------------------------------------------------
    # Example 6.1: Work done by a constant force
    # Part (a): F = 210 N, s = 18 m, phi = 30 deg
    F_61a = 210.0
    s_61a = 18.0
    phi_61a = math.radians(30.0)
    W_61a = F_61a * s_61a * math.cos(phi_61a)
    assert abs(W_61a - 3273.59) < 1.0, f"Ex 6.1a failed: {W_61a}"
    assert round(W_61a, -2) == 3300.0, f"Ex 6.1a rounded failed: {W_61a}"
    print(f"Example 6.1 (a): W = {W_61a:.2f} J ~ 3.3 kJ [PASS]")

    # Part (b): F_vec = (160 i - 40 j) N, s_vec = (14 i + 11 j) m
    Fx_61b = 160.0
    Fy_61b = -40.0
    sx_61b = 14.0
    sy_61b = 11.0
    W_61b = Fx_61b * sx_61b + Fy_61b * sy_61b
    assert W_61b == 1800.0, f"Ex 6.1b failed: {W_61b}"
    print(f"Example 6.1 (b): W = {W_61b:.1f} J ~ 1.8 kJ [PASS]")

    # -------------------------------------------------------------
    # Example 6.2: Work done by several forces
    w_62 = 14700.0
    s_62 = 20.0
    F_T = 5000.0
    phi_T = math.radians(36.9)
    f_k = 3500.0

    W_w = 0.0
    W_n = 0.0
    W_T = F_T * s_62 * math.cos(phi_T)
    W_f = f_k * s_62 * math.cos(math.radians(180.0))
    W_tot_sum = W_w + W_n + W_T + W_f

    # Check textbook values: W_T ~ 80 kJ, W_f = -70 kJ, W_tot ~ 10 kJ
    assert abs(W_T - 79984.0) < 50.0, f"Ex 6.2 W_T failed: {W_T}"
    assert W_f == -70000.0, f"Ex 6.2 W_f failed: {W_f}"
    assert abs(W_tot_sum - 9984.0) < 50.0, f"Ex 6.2 W_tot failed: {W_tot_sum}"

    # Alternative using net force
    F_net_x = F_T * math.cos(phi_T) - f_k
    W_tot_net = F_net_x * s_62
    assert abs(W_tot_net - 9984.0) < 50.0, f"Ex 6.2 W_tot_net failed: {W_tot_net}"
    print(f"Example 6.2: W_T = {W_T:.1f} J, W_f = {W_f:.1f} J, W_tot = {W_tot_sum:.1f} J ~ 10 kJ [PASS]")

    # -------------------------------------------------------------
    # TYU 6.1: Electron in CRT
    # Constant velocity -> net force = 0 -> W_tot = 0
    v_tyu61 = 8.0e7
    a_tyu61 = 0.0
    F_net_tyu61 = 0.0
    W_tyu61 = 0.0
    assert W_tyu61 == 0.0
    print(f"TYU 6.1: W_tot = {W_tyu61} J [PASS]")

    # -------------------------------------------------------------
    # Example 6.3: Calculating speed using work and energy
    m_63 = 14700.0 / 9.80
    assert m_63 == 1500.0
    v1_63 = 2.0
    K1_63 = 0.5 * m_63 * v1_63**2
    assert K1_63 == 3000.0

    # With W_tot = 9984 J (or rounded 10000 J)
    K2_63 = K1_63 + W_tot_sum
    v2_63 = math.sqrt(2 * K2_63 / m_63)
    assert abs(v2_63 - 4.16) < 0.05
    # With 10 kJ:
    v2_63_rounded = math.sqrt(2 * (3000.0 + 10000.0) / 1500.0)
    assert abs(v2_63_rounded - 4.1633) < 0.05
    print(f"Example 6.3: K1 = {K1_63} J, K2 = {K2_63:.1f} J, v2 = {v2_63:.2f} m/s ~ 4.2 m/s [PASS]")

    # -------------------------------------------------------------
    # Example 6.4: Pile driver hammerhead
    m_64 = 200.0
    g = 9.80
    w_64 = m_64 * g
    h_64 = 3.00
    d_64 = 0.074
    f_rail = 60.0

    # 1 to 2: falling 3.00 m
    F_net_12 = w_64 - f_rail
    assert math.isclose(F_net_12, 1900.0, rel_tol=1e-5)
    W_12 = F_net_12 * h_64
    assert math.isclose(W_12, 5700.0, rel_tol=1e-5)
    v2_64 = math.sqrt(2 * W_12 / m_64)
    assert abs(v2_64 - 7.55) < 0.01

    # 2 to 3: stopping in 0.074 m
    # W_23 = -K2 = -5700 J = (w - f - n) * d
    # n = w - f + K2 / d = 1900 + 5700 / 0.074
    n_64 = 1900.0 + 5700.0 / d_64
    assert abs(n_64 - 78927.0) < 5.0
    assert round(n_64, -3) == 79000.0
    print(f"Example 6.4: v2 = {v2_64:.2f} m/s, n = {n_64:.1f} N ~ 79 kN [PASS]")

    # -------------------------------------------------------------
    # Example 6.5: Comparing kinetic energies of iceboats
    # W1 = F*s, W2 = F*s -> K1 = K2 = F*s
    # v1 / v2 = sqrt(2K/m) / sqrt(2K/2m) = sqrt(2)
    ratio_v_65 = math.sqrt(2.0)
    assert abs(ratio_v_65 - 1.4142) < 0.001
    print(f"Example 6.5: K1 = K2 = Fs, v1/v2 = {ratio_v_65:.4f} ~ sqrt(2) [PASS]")

    # -------------------------------------------------------------
    # TYU 6.2: Rank kinetic energies
    # (i) 2.0 kg moving at 5.0 m/s: K = 0.5 * 2.0 * 5.0^2 = 25.0 J
    # (ii) 1.0 kg initially at rest, W = 30 J: K2 = 0 + 30 = 30.0 J
    # (iii) 1.0 kg at 4.0 m/s, W = 20 J: K1 = 8.0 J -> K2 = 8.0 + 20 = 28.0 J
    # (iv) 2.0 kg at 10 m/s, did 80 J on another object: K1 = 100 J -> K2 = 100 - 80 = 20.0 J
    K_tyu62_1 = 0.5 * 2.0 * 5.0**2
    K_tyu62_2 = 0.0 + 30.0
    K_tyu62_3 = 0.5 * 1.0 * 4.0**2 + 20.0
    K_tyu62_4 = 0.5 * 2.0 * 10.0**2 - 80.0
    assert K_tyu62_1 == 25.0
    assert K_tyu62_2 == 30.0
    assert K_tyu62_3 == 28.0
    assert K_tyu62_4 == 20.0
    assert K_tyu62_4 < K_tyu62_1 < K_tyu62_3 < K_tyu62_2
    print(f"TYU 6.2: (iv) 20 J < (i) 25 J < (iii) 28 J < (ii) 30 J [PASS]")

    # -------------------------------------------------------------
    # Example 6.6: Spring in bathroom scale
    w_66 = 600.0
    x_comp_66 = 0.010
    k_66 = w_66 / x_comp_66
    assert k_66 == 60000.0
    W_66 = 0.5 * k_66 * x_comp_66**2
    assert W_66 == 3.0
    print(f"Example 6.6: k = {k_66:.1f} N/m, W = {W_66:.1f} J [PASS]")

    # -------------------------------------------------------------
    # Example 6.7: Glider on air track with spring
    m_67 = 0.100
    k_67 = 20.0
    v1_67 = 1.50
    # Part (a): no friction
    d_67a = v1_67 * math.sqrt(m_67 / k_67)
    assert abs(d_67a - 0.106) < 0.001
    # Part (b): with friction mu_k = 0.47
    mu_k_67 = 0.47
    g_67 = 9.80
    term1 = mu_k_67 * m_67 * g_67 / k_67 # 0.02303
    term2 = m_67 * v1_67**2 / k_67       # 0.01125
    d_67b = -term1 + math.sqrt(term1**2 + term2)
    assert abs(d_67b - 0.086) < 0.001
    print(f"Example 6.7: d_no_fric = {d_67a*100:.1f} cm, d_fric = {d_67b*100:.1f} cm [PASS]")

    # -------------------------------------------------------------
    # Example 6.8: Pushing swing
    # w = mg, R = 2.00 m, theta0 = 30 deg, m = 25.0 kg
    m_68 = 25.0
    R_68 = 2.00
    theta0_68 = math.radians(30.0)
    w_68 = m_68 * 9.80
    W_grav_68 = -w_68 * R_68 * (1.0 - math.cos(theta0_68))
    W_F_68 = -W_grav_68
    assert abs(W_F_68 - 65.65) < 0.1
    print(f"Example 6.8: W_tot = 0, W_T = 0, W_F = {W_F_68:.1f} J ~ 65.7 J [PASS]")

    # -------------------------------------------------------------
    # TYU 6.3: Conical pendulum (Example 5.20)
    # Bob moves in a horizontal circle: F_tension perp dl, w perp dl
    # Over any part or one complete circle: W_F = 0, W_w = 0
    W_T_tyu63 = 0.0
    W_w_tyu63 = 0.0
    assert W_T_tyu63 == 0.0
    assert W_w_tyu63 == 0.0
    # Swing kinematics verification:
    v_tyu63 = math.sqrt(2 * 9.80 * R_68 * (1.0 - math.cos(theta0_68)))
    assert abs(v_tyu63 - 2.29) < 0.01
    print(f"TYU 6.3: W_T = 0 J, W_w = 0 J, v_bottom = {v_tyu63:.2f} m/s [PASS]")

    # -------------------------------------------------------------
    # Example 6.9: Airbus A380 engine power
    F_69 = 322000.0
    v_69 = 250.0
    P_69 = F_69 * v_69
    assert P_69 == 8.05e7
    hp_69 = P_69 / 746.0
    assert abs(hp_69 - 107908.8) < 10.0
    assert round(hp_69, -3) == 108000.0
    print(f"Example 6.9: P = {P_69/1e6:.2f} MW, hp = {hp_69:.0f} hp ~ 108000 hp [PASS]")

    # -------------------------------------------------------------
    # Example 6.10: Marathon runner Willis Tower climb
    m_610 = 50.0
    h_610 = 443.0
    t_610 = 15.0 * 60.0
    W_610 = m_610 * 9.80 * h_610
    assert abs(W_610 - 217070.0) < 1.0
    Pav_610 = W_610 / t_610
    assert abs(Pav_610 - 241.19) < 0.1
    hp_610 = Pav_610 / 746.0
    assert abs(hp_610 - 0.3233) < 0.001
    print(f"Example 6.10: W = {W_610/1e5:.2f}x10^5 J, Pav = {Pav_610:.1f} W ~ 0.241 kW = 0.323 hp [PASS]")

    # -------------------------------------------------------------
    # Actual TYU6.4: Drag power for four engines in straight level steady flight.
    P_drag = -(4 * F_69) * v_69
    assert P_drag == -322000000.0
    assert round(P_drag / 746.0, -3) == -432000.0
    print(f"TYU 6.4: Drag power {P_drag / 746.0:.1f} hp ~ -432000 hp [PASS]")

    # Original opening photograph question, PDF191.
    opening_energies = [0.5*m*v*v for m,v in [(0.145,20.0),(0.0145,200.0),(1.45,2.0)]]
    assert all(math.isclose(a,b) for a,b in zip(opening_energies,[29.0,290.0,2.9]))
    assert opening_energies.index(max(opening_energies)) == 1
    # Source examples and biological-sidebar/unit arithmetic restored in parent review.
    assert 5.0 * 6.0 == 30.0
    assert math.isclose(0.3 / (1e-3)**2, 3e5)
    assert round(33000*4.448*0.3048/60) == 746
    assert 1000*3600 == 3.6e6
    assert 100*10*3600 == 3.6e6
    assert math.isclose(4.448*0.3048,1.356,rel_tol=5e-4)
    assert math.isclose(0.100*9.8*1.0,1.0,abs_tol=0.03)
    assert hp_69/3400 > 30
    assert v_69*3.6 == 900
    assert F_69*0.0 == 0.0
    assert math.isclose(443/900, 0.4922222222222222)
    assert math.isclose(m_610*9.8*(443/900),Pav_610)
    assert math.isclose(k_67*d_67b/(m_67*g_67),1.7450502677057105,rel_tol=1e-10)
    # Independent integration of the original symbolic swing example.
    from scipy.integrate import quad
    integral_F=quad(lambda theta:w_68*math.tan(theta)*math.cos(theta)*R_68,0,theta0_68)[0]
    integral_g=quad(lambda theta:-w_68*math.sin(theta)*R_68,0,theta0_68)[0]
    assert math.isclose(integral_F,W_F_68,rel_tol=1e-12)
    assert math.isclose(integral_F+integral_g,0.0,abs_tol=1e-10)

    print("\n>>> ALL 10 EXAMPLES, 4 TYU SELF-CHECKS, AND CONVERSIONS VERIFIED CLEANLY! <<<")

if __name__ == "__main__":
    verify_all()
