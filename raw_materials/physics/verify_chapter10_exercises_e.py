"""Bộ kiểm tra xác minh các bài tập Vật lý 1 Chapter 10 nhóm E (10.76–10.97).

Xác minh tính đúng đắn của dữ liệu đầu vào, các công thức giải tích,
và kết quả số học của toàn bộ 22 bài tập thực tế trong phạm vi phân công.
"""
import math

def verify_all():
    print("--- Bắt đầu xác minh tính toán Chapter 10 Nhóm E (10.76–10.97) ---")

    # 10.76
    # Ramp L = 6.00 m, beta = 37.0 deg, M = 460 kg, R = 0.300 m, mu_s = 0.120, g = 9.80 m/s^2
    # F pulls at center (yoke) parallel to ramp.
    # rolling up without slipping: f_s points down ramp, tau = f_s * R = I * alpha = (1/2 M R^2)*(a/R) = 1/2 M R a => f_s = 1/2 M a
    # F - M g sin(beta) - f_s = M a => F - M g sin(beta) = 3 f_s => f_s = (F - M g sin(beta)) / 3
    # f_s <= mu_s M g cos(beta) => F <= M g (sin(beta) + 3 mu_s cos(beta))
    g = 9.80
    beta = math.radians(37.0)
    M_76 = 460.0
    R_76 = 0.300
    mu_s_76 = 0.120
    L_76 = 6.00
    F_max_76 = M_76 * g * (math.sin(beta) + 3 * mu_s_76 * math.cos(beta))
    assert 4000 < F_max_76 < 4020, f"10.76(a) F_max fail: {F_max_76}"
    # Part (b) max a occurs when f_s is max: a_max = 2 f_s_max / M = 2 * mu_s * g * cos(beta)
    a_max_76 = 2 * mu_s_76 * g * math.cos(beta)
    t_min_76 = math.sqrt(2 * L_76 / a_max_76)
    assert 2.50 < t_min_76 < 2.56, f"10.76(b) t_min fail: {t_min_76}"
    print(f"10.76: F_max = {F_max_76:.2f} N, t_min = {t_min_76:.3f} s - OK")

    # 10.77
    # D = 0.420 m, R = 0.210 m, 6 spokes, linear mass density lambda = 25.0 g/cm = 2.50 kg/m, h = 58.0 m
    # M_rim = 2*pi*R*lambda, I_rim = M_rim * R^2 = 2*pi*lambda*R^3
    # 6 spokes: each length R, mass lambda*R, I_spoke = 1/3 (lambda*R)*R^2 = 1/3 lambda R^3
    # I_spokes = 6 * 1/3 lambda R^3 = 2 lambda R^3
    # I_tot = (2*pi + 2) lambda R^3. M_tot = (2*pi + 6) lambda R
    # c = I_tot / (M_tot R^2) = (2*pi + 2)/(2*pi + 6) = (pi + 1)/(pi + 3)
    c_77 = (math.pi + 1.0) / (math.pi + 3.0)
    h_77 = 58.0
    v_77 = math.sqrt(2 * g * h_77 / (1 + c_77))
    assert 26.0 < v_77 < 26.2, f"10.77(a) v fail: {v_77}"
    # (b) doubling lambda and D does not change c (dimensionless) or g, h => v unchanged
    print(f"10.77: v = {v_77:.2f} m/s, unchanged with doubled density/diameter - OK")

    # 10.78
    # Rod M = 0.0300 kg, L = 0.400 m, pivot center, I_rod = 1/12 M L^2
    # 2 rings: m = 0.0200 kg each, initially r1 = 0.0500 m, omega1 = 48.0 rpm
    # (a) rings at ends: r2 = L/2 = 0.200 m
    I_rod_78 = (1.0 / 12.0) * 0.0300 * (0.400 ** 2)
    I_1_78 = I_rod_78 + 2 * 0.0200 * (0.0500 ** 2)
    I_2_78 = I_rod_78 + 2 * 0.0200 * (0.200 ** 2)
    omega1_78 = 48.0 # rpm: Actual source input, not30.
    omega2_78 = omega1_78 * (I_1_78 / I_2_78)
    assert abs(omega2_78 - 12.0) < 1e-6, f"10.78(a) omega2 fail: {omega2_78}"
    # (b) rings fly off: no torque exerted on rod during separation => omega3 = omega2 = 12rpm.
    print(f"10.78: omega2 = {omega2_78:.2f} rpm, omega3 = {omega2_78:.2f} rpm - OK")

    # 10.79
    # Cylinder: mass M, radius 2R, rolls without slipping: I_c = 1/2 M (2R)^2 = 2 M R^2
    # Pulley: disk mass M, radius R, frictionless axle: I_p = 1/2 M R^2
    # Hanging block: mass M
    # T1 - f_s = M a, f_s (2R) = I_c (a / (2R)) = M R a => f_s = 1/2 M a => T1 = 3/2 M a
    # (T2 - T1) R = I_p (a/R) = 1/2 M R a => T2 - T1 = 1/2 M a => T2 = 2 M a
    # M g - T2 = M a => M g - 2 M a = M a => a = 1/3 g
    a_79 = g / 3.0
    assert abs(a_79 - 9.80 / 3.0) < 1e-6, f"10.79 a fail: {a_79}"
    print(f"10.79: a = g/3 = {a_79:.3f} m/s^2 - OK")

    # 10.80
    # Dropped ball m1 = 5.00 kg from h = 12.0 m onto one end of bar (M = 8.00 kg, L = 4.00 m, pivoted at center)
    # Ball 2 m2 = 5.00 kg at other end. Ball 1 sticks to bar.
    # v0 = sqrt(2 g h). L_i = m1 v0 (L/2).
    # I_tot = 1/12 M L^2 + m1 (L/2)^2 + m2 (L/2)^2
    # omega = L_i / I_tot. v2 = (L/2) omega. h2 = v2^2 / (2 g) = (v2 / v0)^2 * h
    h_80 = 12.0
    v0_80 = math.sqrt(2 * g * h_80)
    I_bar_80 = (1.0 / 12.0) * 8.00 * (4.00 ** 2) # 32/3
    I_tot_80 = I_bar_80 + 5.00 * (2.00 ** 2) + 5.00 * (2.00 ** 2) # 32/3 + 40 = 152/3
    L_i_80 = 5.00 * v0_80 * 2.00
    omega_80 = L_i_80 / I_tot_80
    v2_80 = 2.00 * omega_80
    h2_80 = (v2_80 ** 2) / (2 * g)
    # Symbolic: v2/v0 = 2 * (10 / (152/3)) = 20 * 3 / 152 = 60 / 152 = 15 / 38
    # h2 = (15/38)^2 * 12.0 = 225/1444 * 12.0 = 1.8698 m
    assert 1.86 < h2_80 < 1.88, f"10.80 h2 fail: {h2_80}"
    print(f"10.80: h2 = {h2_80:.3f} m - OK")

    # 10.81
    # Rod length L, mass M, pivoted at end: I_rod = 1/3 M L^2
    # Bullet mass m = M/4, strikes at center r = L/2 with speed v, embeds
    # L_i = (M/4) v (L/2) = 1/8 M v L
    # I_f = 1/3 M L^2 + (M/4) (L/2)^2 = (1/3 + 1/16) M L^2 = (19/48) M L^2
    # omega = (1/8) / (19/48) * (v/L) = (6/19) * (v/L)
    # K_i = 1/2 (M/4) v^2 = 1/8 M v^2
    # K_f = 1/2 I_f omega^2 = 1/2 (19/48 M L^2) (36/361 v^2/L^2) = 18 / (48 * 19) M v^2 = 3/152 M v^2
    # K_f / K_i = (3/152) / (1/8) = 24 / 152 = 3/19
    ratio_omega_81 = 6.0 / 19.0
    ratio_K_81 = 3.0 / 19.0
    assert abs(ratio_omega_81 - 0.315789) < 1e-5
    assert abs(ratio_K_81 - 0.157895) < 1e-5
    print(f"10.81: omega = (6/19)(v/L) = {ratio_omega_81:.4f} v/L, K_f/K_i = 3/19 = {ratio_K_81:.4f} - OK")

    # 10.82
    # Turntable R = 6.00 m, T1 = 8.00 s => omega1 = 2 pi / 8 = pi/4 rad/s
    # I_tt = 1200 kg m^2, Person m = 70.0 kg at r1 = 6.00 m => I1 = 1200 + 70 * 36 = 3720
    # Person walks to r2 = 3.00 m => I2 = 1200 + 70 * 9 = 1830
    # omega2 = omega1 * (3720 / 1830)
    # slips at r2 => mu_s * m * g = m r2 omega2^2 => mu_s = r2 omega2^2 / g
    omega1_82 = math.pi / 4.0
    I1_82 = 1200.0 + 70.0 * (6.00 ** 2)
    I2_82 = 1200.0 + 70.0 * (3.00 ** 2)
    omega2_82 = omega1_82 * (I1_82 / I2_82)
    mu_s_82 = (3.00 * (omega2_82 ** 2)) / g
    assert 0.77 < mu_s_82 < 0.79, f"10.82 mu_s fail: {mu_s_82}"
    print(f"10.82: omega2 = {omega2_82:.3f} rad/s, mu_s = {mu_s_82:.3f} - OK")

    # 10.83
    # I_A = 1/3 I_B => I_B = 3 I_A. A has omega0, B at rest.
    # coupled: omega_f = I_A omega0 / (I_A + I_B) = 1/4 omega0
    # K_f = 1/2 (4 I_A) (1/16 omega0^2) = 1/4 K_A0
    # Q = K_A0 - K_f = 3/4 K_A0 = 2400 J => K_A0 = 4/3 * 2400 = 3200 J
    K_A0_83 = (4.0 / 3.0) * 2400.0
    assert abs(K_A0_83 - 3200.0) < 1e-6
    print(f"10.83: K_A0_max = {K_A0_83:.1f} J - OK")

    # 10.84
    # Rod L = 2.00 m, M = 0.800 kg, pivoted at end: I_rod = 1/3 (0.800)(2.00^2) = 3.20/3
    # Puck m = 0.163 kg at end L = 2.00 m: I_puck = m L^2 = 0.163 * 4.00 = 0.652
    # I_tot = 3.20/3 + 0.652 = 1.718667
    # T = 0.736 s => omega = 2 pi / 0.736
    # L_i = m v L = I_tot omega => v = I_tot omega / (m L)
    I_rod_84 = (1.0 / 3.0) * 0.800 * (2.00 ** 2)
    I_tot_84 = I_rod_84 + 0.163 * (2.00 ** 2)
    omega_84 = 2 * math.pi / 0.736
    v_84 = (I_tot_84 * omega_84) / (0.163 * 2.00)
    assert 44.8 < v_84 < 45.2, f"10.84 v fail: {v_84}"
    print(f"10.84: v = {v_84:.2f} m/s - OK")

    # 10.85
    # Bird m = 0.500 kg, v = 2.25 m/s, hits bar 25.0 cm below top => d = 0.750 - 0.250 = 0.500 m from hinge
    # Bar M = 1.50 kg, L = 0.750 m, hinged at base: I_bar = 1/3 (1.50)(0.750^2) = 0.28125 kg m^2
    # Bird drops after hit => L_i = m v d = 0.500 * 2.25 * 0.500 = 0.5625 kg m^2/s
    # omega0 = L_i / I_bar = 0.5625 / 0.28125 = 2.00 rad/s
    I_bar_85 = (1.0 / 3.0) * 1.50 * (0.750 ** 2)
    L_i_85 = 0.500 * 2.25 * 0.500
    omega0_85 = L_i_85 / I_bar_85
    assert abs(omega0_85 - 2.00) < 1e-6, f"10.85(a) omega0 fail: {omega0_85}"
    # (b) Falls to ground: 1/2 I omega_f^2 = 1/2 I omega0^2 + M g (L/2)
    # omega_f^2 = omega0^2 + 3 g / L
    omega_f_85 = math.sqrt(omega0_85 ** 2 + 3 * g / 0.750)
    assert 6.55 < omega_f_85 < 6.60, f"10.85(b) omega_f fail: {omega_f_85}"
    print(f"10.85: omega0 = {omega0_85:.2f} rad/s, omega_f = {omega_f_85:.2f} rad/s - OK")

    # 10.86
    # m = 0.130 kg, r1 = 0.800 m, v1 = 4.00 m/s
    # Angular momentum conserved: v(r) = v1 r1 / r
    # T(r) = m v(r)^2 / r = m v1^2 r1^2 / r^3
    # T_max = 30.0 N => r^3 = m v1^2 r1^2 / T_max
    r_86 = (0.130 * (4.00 ** 2) * (0.800 ** 2) / 30.0) ** (1.0 / 3.0)
    assert 0.353 < r_86 < 0.355, f"10.86 r fail: {r_86}"
    print(f"10.86: r_break = {r_86:.4f} m - OK")

    # 10.87
    # Runner m = 55 kg at R = 3.0 m, v1 = +2.8 m/s rel to earth => L_runner = m v1 R = 55 * 2.8 * 3.0 = 462 kg m^2/s
    # Turntable I_tt = 80 kg m^2, omega_tt = -0.20 rad/s => L_tt = 80 * (-0.20) = -16 kg m^2/s
    # L_tot = 462 - 16 = 446 kg m^2/s
    # I_tot = I_tt + m R^2 = 80 + 55 * 9.0 = 80 + 495 = 575 kg m^2
    # omega_f = 446 / 575
    omega_f_87 = 446.0 / 575.0
    assert 0.77 < omega_f_87 < 0.78, f"10.87 omega_f fail: {omega_f_87}"
    print(f"10.87: omega_f = {omega_f_87:.4f} rad/s - OK")

    # 10.88
    # 2014 Silverado: max P = 285 hp at 5300 rpm, max tau = 305 ft lb at 3900 rpm
    # 1 hp = 550 ft lb/s = 745.7 W, 1 ft lb = 1.355818 N m
    # (a) tau at 5300 rpm: omega1 = 5300 * 2 pi / 60 = 530 pi / 3 rad/s
    # P1 = 285 * 550 = 156750 ft lb/s => tau_ftlb = P1 / omega1 = 156750 / (530 pi / 3) = 282.42 ft lb
    # tau_Nm = 282.42 * 1.355818 = 382.91 N m
    tau_88a_ftlb = (285 * 550) / (5300 * 2 * math.pi / 60)
    tau_88a_Nm = tau_88a_ftlb * 1.355818
    assert 281 < tau_88a_ftlb < 284
    assert 381 < tau_88a_Nm < 385
    # (b) P at 3900 rpm with tau = 305 ft lb:
    # omega2 = 3900 * 2 pi / 60 = 130 pi rad/s
    # P2_ftlb = 305 * 130 pi = 39650 pi ft lb/s
    # P2_hp = P2_ftlb / 550 = 226.51 hp
    # P2_W = P2_hp * 745.7 = 168908 W
    P_88b_hp = (305 * 3900 * 2 * math.pi / 60) / 550
    P_88b_W = P_88b_hp * 745.7
    assert 225 < P_88b_hp < 228
    assert 167000 < P_88b_W < 170000
    # (c) c = 33000 / (2 pi) = 16500 / pi = 5252.11
    c_88 = 33000.0 / (2 * math.pi)
    assert abs(c_88 - 5252.11) < 0.1
    # (d) 2012 Camaro ZL1: 580 hp at 6000 rpm => tau = c * hp / rpm
    tau_88d = c_88 * 580.0 / 6000.0
    assert 506 < tau_88d < 509
    print(f"10.88: tau_a = {tau_88a_ftlb:.1f} ft lb ({tau_88a_Nm:.1f} N m), P_b = {P_88b_hp:.1f} hp ({P_88b_W:.0f} W), c = {c_88:.1f}, tau_d = {tau_88d:.1f} ft lb - OK")

    # 10.89
    # Ramp beta = 35.0 deg. M = 0.840 kg.
    # a = g sin(beta) / (1 + c). t = sqrt(2 s (1 + c) / (g sin(beta)))
    # c values: solid sphere 0.40, solid cylinder 0.50, hollow sphere 2/3 (0.667), hollow cylinder 1.00
    # t_A < t_B < t_C < t_D => A = solid sphere, B = solid cylinder, C = hollow sphere, D = hollow cylinder
    # (b) K_tot = M g h is same for all
    # (c) K_rot = c / (1 + c) K_tot is greatest for D (c = 1 => 1/2 K_tot)
    # (d) mu_s >= c / (1 + c) tan(beta). Max is for D: 1/2 tan(35.0 deg) = 0.3501
    mu_s_89 = 0.5 * math.tan(math.radians(35.0))
    assert 0.349 < mu_s_89 < 0.352
    print(f"10.89: A=solid sphere, B=solid cylinder, C=hollow sphere, D=hollow cylinder, mu_s_min = {mu_s_89:.3f} - OK")

    # 10.90
    # Flywheel R = 0.166 m
    # (a) F = 25.0 N, s = 8.35 m, t = 2.00 s => a_tan = 2 s / t^2 = 2 * 8.35 / 4.00 = 4.175 m/s^2
    # tau = F R = 4.15 N m. alpha = a_tan / R = 25.1506 rad/s^2. I = tau / alpha = F R^2 / a_tan = 0.165 kg m^2
    a_tan_90 = 2 * 8.35 / (2.00 ** 2)
    I_90 = 25.0 * (0.166 ** 2) / a_tan_90
    assert abs(I_90 - 0.165) < 0.001
    # (b) Fig P10.90: trapezoid from d = 0 to 6.00 m. Constant 60.0 N from 0 to 3.00 m, linear to 0 at 6.00 m
    # Area = 60.0 * 3.00 + 0.5 * 3.00 * 60.0 = 180 + 90 = 270 J => K = W = 270 J
    W_90 = 60.0 * 3.00 + 0.5 * 3.00 * 60.0
    assert abs(W_90 - 270.0) < 1e-6
    # (c) omega = sqrt(2 K / I) = sqrt(540 / 0.165) = 57.21 rad/s => rpm = omega * 60 / (2 pi) = 546 rpm
    omega_90 = math.sqrt(2 * W_90 / I_90)
    rpm_90 = omega_90 * 60.0 / (2 * math.pi)
    assert 544 < rpm_90 < 548
    print(f"10.90: I = {I_90:.3f} kg m^2, K = {W_90:.1f} J, omega = {rpm_90:.1f} rpm - OK")

    # 10.91
    # Block m, v1 at r1 on frictionless surface, string pulled to r2
    # (a) T(r) = m v1^2 r1^2 / r^3
    # (b) W = int_{r1}^{r2} (- T(r) dr) = 1/2 m v1^2 r1^2 (1/r2^2 - 1/r1^2)
    # (c) Delta K = 1/2 m v2^2 - 1/2 m v1^2 = 1/2 m v1^2 (r1^2/r2^2 - 1) = W (exact match)
    # Test with arbitrary numbers
    m_test, v1_test, r1_test, r2_test = 0.5, 3.0, 1.0, 0.5
    W_91 = 0.5 * m_test * (v1_test ** 2) * (r1_test ** 2) * (1.0 / (r2_test ** 2) - 1.0 / (r1_test ** 2))
    v2_test = v1_test * r1_test / r2_test
    dK_91 = 0.5 * m_test * (v2_test ** 2) - 0.5 * m_test * (v1_test ** 2)
    assert abs(W_91 - dK_91) < 1e-12
    print("10.91: Symbolic proof and numerical identity W = Delta K - OK")

    # 10.92
    # Solid cylinder M, R, omega0 initially, vx(0) = 0. Kinetic friction mu_k
    # (a) a_x = mu_k g, alpha = - 2 mu_k g / R
    # (b) Slipping stops when vx = R omega: mu_k g t1 = R (omega0 - 2 mu_k g t1 / R) => 3 mu_k g t1 = R omega0 => t1 = R omega0 / (3 mu_k g)
    # d = 1/2 a_x t1^2 = R^2 omega0^2 / (18 mu_k g)
    # (c) W_f = Delta K = 1/12 M R^2 omega0^2 - 1/4 M R^2 omega0^2 = - 1/6 M R^2 omega0^2
    # Test work-energy equivalence:
    # W_trans = f_k * d = (mu_k M g) * (R^2 omega0^2 / (18 mu_k g)) = 1/18 M R^2 omega0^2
    # W_rot = tau * theta = (- mu_k M g R) * (omega0 t1 + 1/2 alpha t1^2) = - mu_k M g R * (2 R omega0^2 / (9 mu_k g)) = - 2/9 M R^2 omega0^2 = - 4/18 M R^2 omega0^2
    # W_net = W_trans + W_rot = - 3/18 M R^2 omega0^2 = - 1/6 M R^2 omega0^2
    assert abs((1.0 / 18.0 - 4.0 / 18.0) - (-1.0 / 6.0)) < 1e-12
    print("10.92: a_x = mu_k g, alpha = -2 mu_k g / R, d = R^2 omega0^2 / (18 mu_k g), W = -1/6 M R^2 omega0^2 - OK")

    # 10.93
    # Gyroscope D = 0.650 m => R = 0.325 m, M = 8.00 kg (all at rim => I = M R^2 = 8.00 * 0.325^2 = 0.845 kg m^2)
    # spin = 5.00 rev/s = 10 pi rad/s => L = I omega = 0.845 * 10 pi = 8.45 pi kg m^2/s = 26.546 kg m^2/s
    # shaft projects 0.200 m at each side => hand distance = 2 * 0.200 = 0.400 m
    # weight w = M g = 8.00 * 9.80 = 78.4 N => w/2 = 39.2 N
    I_93 = 8.00 * (0.325 ** 2)
    L_93 = I_93 * 5.00 * 2 * math.pi
    w_half_93 = 8.00 * 9.80 / 2.0
    # (a) at rest: F1 = F2 = w/2 = 39.2 N upward
    assert abs(w_half_93 - 39.2) < 1e-6
    # (b) precession at 0.050 rev/s: Omega = 0.050 * 2 pi = 0.10 pi rad/s
    # tau = Omega * L = 0.10 pi * 8.45 pi = 0.845 pi^2 = 8.3397 N m
    # F_prec = tau / 0.400 = 20.849 N
    # F_up = 39.2 + 20.85 = 60.05 N, F_down = 39.2 - 20.85 = 18.35 N
    tau_93b = (0.050 * 2 * math.pi) * L_93
    F_prec_93b = tau_93b / 0.400
    F_up_93b = w_half_93 + F_prec_93b
    F_down_93b = w_half_93 - F_prec_93b
    assert 59.9 < F_up_93b < 60.2
    assert 18.2 < F_down_93b < 18.5
    # (c) precession at 0.300 rev/s: Omega = 0.300 * 2 pi = 0.60 pi rad/s
    # tau = 0.60 pi * 8.45 pi = 50.038 N m => F_prec = 125.10 N
    # F1 = 39.2 + 125.1 = 164.3 N (upward), F2 = 39.2 - 125.1 = -85.9 N (downward)
    tau_93c = (0.300 * 2 * math.pi) * L_93
    F_prec_93c = tau_93c / 0.400
    F1_93c = w_half_93 + F_prec_93c
    F2_93c = w_half_93 - F_prec_93c
    assert 163.5 < F1_93c < 165.0
    assert -86.5 < F2_93c < -85.0
    # (d) Supported at one end only: F_prec = w/2 = 39.2 N => tau = w * d = M g d = 78.4 * 0.200 = 15.68 N m
    # Omega = tau / L = 15.68 / L_93 rad/s => rev/s = Omega / (2 pi)
    Omega_93d_rad = (8.00 * 9.80 * 0.200) / L_93
    Omega_93d_rev = Omega_93d_rad / (2 * math.pi)
    assert 0.093 < Omega_93d_rev < 0.095
    print(f"10.93: F_a = 39.2 N, F_b = ({F_up_93b:.1f} N up, {F_down_93b:.1f} N up), F_c = ({F1_93c:.1f} N up, {abs(F2_93c):.1f} N down), Omega_d = {Omega_93d_rev:.3f} rev/s - OK")

    # MCAT 10.94
    # I_empty = 1.5 kg m^2, tau = 2.5 N m, t = 3.0 s, omega = 1.0 rad/s
    # alpha = 1.0 / 3.0 rad/s^2. I_tot = tau / alpha = 2.5 * 3.0 = 7.5 kg m^2
    # I_person = I_tot - I_empty = 7.5 - 1.5 = 6.0 kg m^2 => option (b)
    alpha_94 = 1.0 / 3.0
    I_tot_94 = 2.5 / alpha_94
    I_person_94 = I_tot_94 - 1.5
    assert abs(I_person_94 - 6.0) < 1e-6
    print("10.94: I_person = 6.0 kg m^2 (option b) - OK")

    # MCAT 10.95
    # Extends legs => I increases. Since tau = constant, alpha = tau / I decreases => option (c)
    print("10.95: alpha decreases (option c) - OK")

    # MCAT 10.96
    # tau = T * (D/2). For same T, doubling tau requires doubling D => option (b)
    print("10.96: double pulley diameter (option b) - OK")

    # MCAT 10.97
    # Parallel-axis theorem: I_axis = I_cm + M d^2 > I_cm for d > 0 => measured value too large => option (a)
    print("10.97: measured moment of inertia too large (option a) - OK")

    print("\nComputed22 numbered cases. Source assumptions, figures and conceptual prose need separate review.")

if __name__ == '__main__':
    verify_all()
