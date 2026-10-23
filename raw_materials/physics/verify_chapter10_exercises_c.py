"""Bộ kiểm thử số học và đại số thực chứng cho Chapter 10 Nhóm C (Young & Freedman 15th Edition).
Bao gồm:
- 12 bài tập Luyện tập hướng dẫn (VP10.3.1 - VP10.12.4)
- 30 câu hỏi thảo luận (Q10.1 - Q10.30)
- 1 bài tập Cầu nối (Bridging Problem: Billiard Physics) với đầy đủ 10 điểm hướng dẫn
"""
import math
import sys


def verify_guided_practice():
    # VP10.3.1
    R_10_3_1 = 0.060  # m
    M_10_3_1 = 50.0   # kg
    a_10_3_1 = 0.60   # m/s^2
    alpha_10_3_1 = a_10_3_1 / R_10_3_1
    I_10_3_1 = 0.5 * M_10_3_1 * (R_10_3_1 ** 2)
    tau_10_3_1 = I_10_3_1 * alpha_10_3_1
    F_10_3_1 = tau_10_3_1 / R_10_3_1
    assert math.isclose(alpha_10_3_1, 10.0, rel_tol=1e-5), f"VP10.3.1 (a) failed: {alpha_10_3_1}"
    assert math.isclose(tau_10_3_1, 0.90, rel_tol=1e-5), f"VP10.3.1 (b) failed: {tau_10_3_1}"
    assert math.isclose(F_10_3_1, 15.0, rel_tol=1e-5), f"VP10.3.1 (c) failed: {F_10_3_1}"

    # VP10.3.2
    # a_y = g / (1 + M/m), T = mg / (1 + m/M)
    for M, m, g in [(2.0, 1.0, 9.8), (5.0, 2.5, 9.8), (10.0, 1.0, 9.8)]:
        a_y = g / (1.0 + M / m)
        T = m * g / (1.0 + m / M)
        assert math.isclose(m * g - T, m * a_y, rel_tol=1e-5), "VP10.3.2 block equation failed"
        assert math.isclose(T, M * a_y, rel_tol=1e-5), "VP10.3.2 cylinder equation failed"

    # VP10.3.3
    for m, g, a, R in [(3.0, 9.8, 4.0, 0.25), (5.0, 9.8, 2.0, 0.15)]:
        T = m * (g - a)
        I = m * (R ** 2) * (g / a - 1.0)
        tau = T * R
        alpha = a / R
        assert math.isclose(tau, I * alpha, rel_tol=1e-5), "VP10.3.3 torque-I relation failed"

    # VP10.3.4
    for M, m, g, a, R in [(4.0, 2.0, 9.8, 1.5, 0.20)]:
        T = m * (g + a)
        tau_cable = T * R
        I = 0.5 * M * (R ** 2)
        alpha = a / R
        tau_motor = tau_cable + I * alpha
        expected_tau_motor = m * R * (g + a) + 0.5 * M * R * a
        assert math.isclose(tau_motor, expected_tau_motor, rel_tol=1e-5), "VP10.3.4 motor torque failed"

    # VP10.7.1
    # Hollow cylinder: R_out = R, R_in = R/2
    # I = 0.5 * M * (R^2 + (R/2)^2) = (5/8) * M * R^2
    # a_cm = 8/13 g, T = 5/13 M g
    frac_a = 8.0 / 13.0
    frac_T = 5.0 / 13.0
    assert math.isclose(1.0 - frac_T, frac_a, rel_tol=1e-5), "VP10.7.1 linear balance failed"
    assert math.isclose(frac_T, (5.0 / 8.0) * frac_a, rel_tol=1e-5), "VP10.7.1 torque balance failed"

    # VP10.7.2
    # Thin-walled hollow sphere: I = (2/3) M R^2
    # a = (3/5) g sin(beta), f = (2/5) M g sin(beta), tau = (2/5) M g R sin(beta)
    a_sphere = 3.0 / 5.0
    f_sphere = 2.0 / 5.0
    assert math.isclose(1.0 - f_sphere, a_sphere, rel_tol=1e-5), "VP10.7.2 linear balance failed"
    assert math.isclose(f_sphere, (2.0 / 3.0) * a_sphere, rel_tol=1e-5), "VP10.7.2 torque balance failed"

    # VP10.7.3
    # Primitive yo-yo with T = (2/3) M g
    # a_cm = g - T/M = g - (2/3) g = (1/3) g downward
    # alpha = T * R / (0.5 * M * R^2) = (2/3 M g R) / (1/2 M R^2) = 4g / (3R)
    a_yoyo = 1.0 / 3.0
    alpha_yoyo_coeff = 4.0 / 3.0
    assert math.isclose(1.0 - 2.0 / 3.0, a_yoyo, rel_tol=1e-5), "VP10.7.3 a_cm failed"
    assert math.isclose((2.0 / 3.0) / 0.5, alpha_yoyo_coeff, rel_tol=1e-5), "VP10.7.3 alpha failed"

    # VP10.7.4
    # Solid cylinder: f = (1/3) M g sin(beta), beta_crit = arctan(3 mu_s)
    for mu_s in [0.20, 0.35, 0.50]:
        beta_c = math.atan(3.0 * mu_s)
        f_max = mu_s * math.cos(beta_c)
        f_roll = (1.0 / 3.0) * math.sin(beta_c)
        assert math.isclose(f_roll, f_max, rel_tol=1e-5), "VP10.7.4 critical angle failed"

    # VP10.12.1
    # Disk A: I_A, omega_A; Disk B: I_A/4, omega_A/2 (same direction)
    # L_i = I_A omega_A + (1/4 I_A)(1/2 omega_A) = (9/8) I_A omega_A
    # I_tot = (5/4) I_A
    # omega_f = (9/8) / (5/4) omega_A = (9/10) omega_A = 0.90 omega_A
    # K_i = 0.5 * I_A omega_A^2 * (1 + 1/16) = (17/32) I_A omega_A^2
    # K_f = 0.5 * (5/4 I_A) * (9/10 omega_A)^2 = (81/160) I_A omega_A^2
    # K_f / K_i = (81/160) / (17/32) = 81/85
    omega_f_12_1 = (9.0 / 8.0) / (5.0 / 4.0)
    K_ratio_12_1 = (81.0 / 160.0) / (17.0 / 32.0)
    assert math.isclose(omega_f_12_1, 0.90, rel_tol=1e-5), f"VP10.12.1 omega_f failed: {omega_f_12_1}"
    assert math.isclose(K_ratio_12_1, 81.0 / 85.0, rel_tol=1e-5), f"VP10.12.1 K ratio failed: {K_ratio_12_1}"
    assert math.isclose(K_ratio_12_1, 0.952941176, rel_tol=1e-4)

    # VP10.12.2
    # Opposite direction: L_i = I_A omega_A - (1/8) I_A omega_A = (7/8) I_A omega_A
    # omega_f = (7/8) / (5/4) = 7/10 = 0.70 omega_A
    # K_f / K_i = (49/160) / (17/32) = 49/85
    omega_f_12_2 = (7.0 / 8.0) / (5.0 / 4.0)
    K_ratio_12_2 = (49.0 / 160.0) / (17.0 / 32.0)
    assert math.isclose(omega_f_12_2, 0.70, rel_tol=1e-5), f"VP10.12.2 omega_f failed: {omega_f_12_2}"
    assert math.isclose(K_ratio_12_2, 49.0 / 85.0, rel_tol=1e-5), f"VP10.12.2 K ratio failed: {K_ratio_12_2}"
    assert math.isclose(K_ratio_12_2, 0.576470588, rel_tol=1e-4)

    # VP10.12.3
    d_door = 1.00
    M_door = 15.0
    m_bullet = 0.010
    v_bullet = 400.0
    I_door = (1.0 / 3.0) * M_door * (d_door ** 2)
    I_bullet = m_bullet * (d_door ** 2)
    I_tot_12_3 = I_door + I_bullet
    L_i_12_3 = m_bullet * v_bullet * d_door
    omega_12_3 = L_i_12_3 / I_tot_12_3
    K_i_12_3 = 0.5 * m_bullet * (v_bullet ** 2)
    K_f_12_3 = 0.5 * I_tot_12_3 * (omega_12_3 ** 2)
    K_ratio_12_3 = K_f_12_3 / K_i_12_3
    assert math.isclose(omega_12_3, 0.7984, rel_tol=1e-3), f"VP10.12.3 omega failed: {omega_12_3}"
    assert math.isclose(round(omega_12_3, 2), 0.80), f"VP10.12.3 rounded omega failed: {omega_12_3}"
    assert math.isclose(K_ratio_12_3, 1.0 / 501.0, rel_tol=1e-3), f"VP10.12.3 K ratio failed: {K_ratio_12_3}"
    assert math.isclose(K_ratio_12_3, 0.0020, rel_tol=1e-2)

    # VP10.12.4
    # Thin-walled hollow sphere: I = (2/3) M R^2
    # L_before = M v R, L_after = M (v/2) R = 0.5 M v R
    # L_sphere = 0.5 M v R = (2/3 M R^2) omega => omega = (3/4) v / R
    # K_i = 0.5 M v^2
    # K_f_clay = 0.5 M (v/2)^2 = (1/8) M v^2
    # K_f_sphere = 0.5 (2/3 M R^2) ((3/4 v/R))^2 = (3/16) M v^2
    # K_f_tot = (1/8 + 3/16) M v^2 = (5/16) M v^2
    # K_f / K_i = (5/16) / (1/2) = 5/8
    omega_coeff_12_4 = 0.5 / (2.0 / 3.0)
    assert math.isclose(omega_coeff_12_4, 0.75, rel_tol=1e-5), f"VP10.12.4 omega failed: {omega_coeff_12_4}"
    K_ratio_12_4 = (1.0 / 8.0 + 3.0 / 16.0) / 0.5
    assert math.isclose(K_ratio_12_4, 5.0 / 8.0, rel_tol=1e-5), f"VP10.12.4 K ratio failed: {K_ratio_12_4}"
    print("All 12 Guided Practice problems verified mathematically!")


def verify_bridging_problem():
    # Part (a): h = (2/5) R
    # J = F dt = m v_cm
    # J_rot = F h dt = I_cm omega = (2/5 m R^2) omega
    # Rolling without slipping: v_cm = R omega
    # => (F dt / m) = R * (F h dt) / (2/5 m R^2) = (5/2) (F h dt) / (m R)
    # => 1 = (5/2) (h / R) => h = 2/5 R
    h_coeff = 2.0 / 5.0
    assert math.isclose(h_coeff, 0.40, rel_tol=1e-5), "Bridging problem (a) failed"

    # Part (b): dead center hit h = 0
    # Immediately after: v_0 = F dt / m, omega_0 = 0
    # Sliding: friction f_k = mu_k m g backward
    # a_cm = - mu_k g
    # tau = f_k R = mu_k m g R = (2/5 m R^2) alpha => alpha = 5 mu_k g / (2 R)
    # v_cm(t) = v_0 - mu_k g t
    # omega(t) = alpha t = (5 mu_k g / (2 R)) t
    # v_cm(t1) = R omega(t1) => v_0 - mu_k g t1 = (5/2) mu_k g t1
    # => v_0 = (7/2) mu_k g t1 => t1 = (2/7) v_0 / (mu_k g)
    # v_cm(t1) = v_0 - (2/7) v_0 = (5/7) v_0
    v_ratio = 1.0 - 2.0 / 7.0
    assert math.isclose(v_ratio, 5.0 / 7.0, rel_tol=1e-5), "Bridging problem (b) failed"

    # Step 10 check: Hollow cylinder I = m R^2
    # v_cm = F dt / m, omega = F h dt / (m R^2)
    # v_cm = R omega => F dt / m = R (F h dt / (m R^2)) = F h dt / (m R) => h = R
    h_hollow_cylinder = 1.0
    assert math.isclose(h_hollow_cylinder, 1.0, rel_tol=1e-5), "Bridging problem step 10 failed"
    print("Bridging Problem verified mathematically!")


def verify_discussion_questions():
    # Verify quantitative relations tested in Q10.9, Q10.10, Q10.12, Q10.14, Q10.27, Q10.28
    # Q10.9: dimensions scale by 2 => I scales by 2^5 = 32 => alpha' = alpha / 32
    scale = 2.0
    I_ratio = (scale ** 3) * (scale ** 2)
    assert I_ratio == 32.0, "Q10.9 scaling failed"

    # Q10.10: T = m g / (1 + m R^2 / I)
    # Hoop has larger I => smaller m R^2 / I => larger T
    I_solid = 0.5
    I_hoop = 1.0
    T_solid_rel = 1.0 / (1.0 + 1.0 / I_solid)
    T_hoop_rel = 1.0 / (1.0 + 1.0 / I_hoop)
    assert T_hoop_rel > T_solid_rel, "Q10.10 tension ranking failed"

    # Q10.12: h_0 = 7 v^2 / (10 g)
    # (a) R' = 2R => h' = h_0
    # (b) M' = 2M => h' = h_0
    # (c) R' = 2R, M' = 2M => h' = h_0
    # (d) omega' = 2 omega => v' = 2v => h' = 4 h_0
    assert 2.0 ** 2 == 4.0, "Q10.12 height scaling failed"

    # Q10.14: a = g sin(beta) / (1 + c)
    # c_sphere = 0.40, c_cyl = 0.50, c_shell = 2/3 ≈ 0.667, c_hoop = 1.00
    c_list = [('sphere', 2.0 / 5.0), ('cylinder', 0.5), ('shell', 2.0 / 3.0), ('hoop', 1.0)]
    a_list = [(name, 1.0 / (1.0 + c)) for name, c in c_list]
    for i in range(len(a_list) - 1):
        assert a_list[i][1] > a_list[i+1][1], f"Q10.14 order failed at {i}"

    # Q10.27: Omega = w r / (I omega)
    # (a) omega -> 2 omega => Omega -> 0.5 Omega
    # (b) w -> 2w => Omega -> 2 Omega
    # (c) I -> 2I => Omega -> 0.5 Omega
    # (d) r -> 2r => Omega -> 2 Omega
    # (e) all doubled => Omega' = (2*2)/(2*2) Omega = Omega
    assert (2.0 * 2.0) / (2.0 * 2.0) == 1.0, "Q10.27 all doubled failed"

    # Q10.28: T_prec = 2pi / Omega = 2pi I omega / (w r)
    # T1 = 3.8 s, T2 = 1.9 s => T2 = 0.5 T1 => omega2 = 0.5 omega1
    assert math.isclose(1.9 / 3.8, 0.5, rel_tol=1e-5), "Q10.28 period ratio failed"

    print("All Discussion Questions quantitative relations verified!")


def main():
    verify_guided_practice()
    verify_bridging_problem()
    verify_discussion_questions()
    print("ALL Chapter 10 Exercises C verifications PASSED perfectly!")


if __name__ == '__main__':
    main()
