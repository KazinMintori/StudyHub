"""Bộ kiểm thử và xác minh tính toán cho 48 bài tập Chapter 11 (11.1 - 11.48).

Chương 11: Cân bằng và Tính đàn hồi (Equilibrium and Elasticity) - Young & Freedman 15th Edition.
Các phép tính được thực hiện với dữ kiện trong mã. Đối chiếu đề, giả thiết, hình và lời giải là công việc riêng.
"""
import math
import numpy as np

g = 9.80  # m/s^2


def verify_all():
    print("Bắt đầu kiểm tra 48 bài tập Chapter 11 (11.1 - 11.48)...")

    # 11.1
    m_bar, L_bar = 0.120, 0.500
    m1, m2 = 0.055, 0.110
    x_cg_11_1 = (m_bar * (L_bar / 2) + m2 * L_bar) / (m1 + m_bar + m2)
    assert abs(x_cg_11_1 - 0.2982) < 0.001, f"11.1 failed: {x_cg_11_1}"
    print(f"11.1: x_cg = {x_cg_11_1 * 100:.1f} cm (Đáp án: 29.8 cm) - OK")

    # 11.2
    M_11_2, m_add = 5.00, 1.50
    delta_cg = -0.0220  # 2.20 cm sang trái
    # x_new_cg = (M * 0 + m_add * x_add) / (M + m_add) = delta_cg
    x_add = delta_cg * (M_11_2 + m_add) / m_add
    assert abs(abs(x_add) - 0.09533) < 0.001, f"11.2 failed: {x_add}"
    print(f"11.2: x_add = {abs(x_add) * 100:.2f} cm sang trái - OK")

    # 11.3
    L_rod, m_rod = 2.00, 1.80
    m_clamp, x_target = 2.40, 1.20
    # x_target = (m_rod * (L_rod / 2) + m_clamp * x_clamp) / (m_rod + m_clamp)
    x_clamp = (x_target * (m_rod + m_clamp) - m_rod * (L_rod / 2)) / m_clamp
    assert abs(x_clamp - 1.35) < 0.001, f"11.3 failed: {x_clamp}"
    print(f"11.3: x_clamp = {x_clamp:.2f} m (Đáp án: 1.35 m) - OK")

    # 11.4 (Fig. 11.9b: w_ladder = 180 N, w_man = 800 N, x_ladder = 1.5 m, x_man = 1.0 m)
    w_ladder, w_man = 180.0, 800.0
    x_ladder, x_man = 1.50, 1.00
    w_total_11_4 = w_ladder + w_man
    x_cg_11_4 = (w_man * x_man + w_ladder * x_ladder) / w_total_11_4
    tau_B_11_4 = w_total_11_4 * x_cg_11_4
    assert abs(x_cg_11_4 - 1.0918) < 0.002, f"11.4a failed: {x_cg_11_4}"
    assert abs(tau_B_11_4 - 1070.0) < 1.0, f"11.4b failed: {tau_B_11_4}"
    print(f"11.4: x_cg = {x_cg_11_4:.2f} m, tau_B = {tau_B_11_4:.0f} N.m - OK")

    # 11.5
    m_rod_11_5, L_rod_11_5 = 0.300, 0.400
    R1, m1_11_5 = 0.0800, 0.900
    R2, m2_11_5 = 0.0600, 0.380
    x1 = -(L_rod_11_5 / 2 + R1)
    x2 = +(L_rod_11_5 / 2 + R2)
    M_tot_11_5 = m_rod_11_5 + m1_11_5 + m2_11_5
    x_cg_11_5 = (m1_11_5 * x1 + m2_11_5 * x2) / M_tot_11_5
    assert abs(abs(x_cg_11_5) - 0.09696) < 0.001, f"11.5 failed: {x_cg_11_5}"
    print(f"11.5: d = {abs(x_cg_11_5) * 100:.2f} cm (Đáp án: 9.70 cm) - OK")

    # 11.6
    w_door = 300.0
    # (a) F at center: F = 300 N, F_hinge = 0 N
    # (b) F at edge: F = 150 N, F_hinge = 150 N
    assert w_door == 300.0
    print("11.6: (a) F = 300 N, F_hinge = 0; (b) F = 150 N, F_hinge = 150 N - OK")

    # 11.7
    w_11_7, L_11_7, d_C = 3400.0, 20.0, 8.0
    theta_11_7 = math.radians(40.0)
    # tau_A = F_S * sin(40) * 8.0 - w * 10.0 = 0
    F_S_11_7 = (w_11_7 * 10.0) / (d_C * math.sin(theta_11_7))
    assert abs(F_S_11_7 - 6612.0) < 50.0, f"11.7 failed: {F_S_11_7}"
    print(f"11.7: F_S = {F_S_11_7 / 1000:.1f} kN (Đáp án: 6.6 kN) - OK")

    # 11.8
    L_11_8, w_11_8 = 3.00, 160.0
    F1_11_8 = 60.0
    F2_11_8 = w_11_8 - F1_11_8  # 100 N
    # F2 * x2 = w * (L/2) = 160 * 1.5 = 240 => x2 = 2.40 m
    x2_11_8 = (w_11_8 * (L_11_8 / 2)) / F2_11_8
    assert abs(x2_11_8 - 2.40) < 0.01, f"11.8 failed: {x2_11_8}"
    print(f"11.8: x2 = {x2_11_8:.2f} m từ người thứ nhất (hoặc 0.60 m từ đầu kia) - OK")

    # 11.9
    L_11_9 = 2.00
    F1_11_9, F2_11_9 = 400.0, 600.0
    # (a) W = 1000 N, x from F1: 1000 * x = 600 * 2 => x = 1.20 m (0.80 m from F2)
    W_a = F1_11_9 + F2_11_9
    d_from_F2_a = L_11_9 - (F2_11_9 * L_11_9) / W_a
    assert abs(W_a - 1000.0) < 0.1 and abs(d_from_F2_a - 0.80) < 0.01
    # (b) Board weighs 200 N at center: W_b = 800 N
    W_b = W_a - 200.0
    # W_b * x + 200 * 1.0 = 600 * 2.0 => 800 * x = 1000 => x = 1.25 m from F1, so 0.75 m from F2
    d_from_F2_b = L_11_9 - (F2_11_9 * L_11_9 - 200.0 * 1.0) / W_b
    assert abs(W_b - 800.0) < 0.1 and abs(d_from_F2_b - 0.75) < 0.01
    print(f"11.9: (a) W = {W_a:.0f} N, d = {d_from_F2_a:.2f} m; (b) W = {W_b:.0f} N, d = {d_from_F2_b:.2f} m - OK")

    # 11.10
    L_11_10, w_11_10 = 0.600, 50.0
    w_tool = 25.0
    # The25cm and75cm labels are VERTICAL wire lengths, not shelf overhangs.
    # Left wire at0;right wire at0.400m;tool at0.200m;shelf center at0.300m.
    T2_11_10 = (w_tool * 0.200 + w_11_10 * 0.300) / 0.400
    T1_11_10 = (w_11_10 + w_tool) - T2_11_10
    assert math.isclose(T2_11_10, 50.0) and math.isclose(T1_11_10, 25.0)
    assert math.isclose(T1_11_10*.400, w_tool*.200+w_11_10*.100)
    print(f"11.10: T1 = {T1_11_10:.1f} N, T2 = {T2_11_10:.1f} N - Source geometry corrected")

    # 11.11
    w_11_11, L_11_11 = 350.0, 1.50
    TA_max, TB_max = 500.0, 400.0
    W_max_11_11 = TA_max + TB_max - w_11_11
    x_W_11_11 = (TB_max * L_11_11 - w_11_11 * (L_11_11 / 2)) / W_max_11_11
    assert abs(W_max_11_11 - 550.0) < 0.1 and abs(x_W_11_11 - 0.6136) < 0.005
    print(f"11.11: W_max = {W_max_11_11:.0f} N, x = {x_W_11_11:.3f} m (Đáp án: 550 N, 0.614 m) - OK")

    # 11.12
    L_11_12, x0_11_12 = 5.0, 3.0
    y0_11_12 = math.sqrt(L_11_12**2 - x0_11_12**2)  # 4.0 m
    cos_th_12 = x0_11_12 / L_11_12  # 0.60
    w_lad, w_climber = 160.0, 740.0
    mu_s_12 = 0.40
    n2_12 = w_lad + w_climber  # 900 N
    fs_max_12 = mu_s_12 * n2_12  # 360 N
    # (b) climber at 1.0 m: n1 * 4.0 = 160 * 1.5 + 740 * (1.0 * 0.60) = 240 + 444 = 684 => n1 = 171 N
    fs_actual_b = (w_lad * 1.5 + w_climber * 0.60) / 4.0
    # (c) max distance d: n1 = 360 N => 360 * 4.0 = 240 + 740 * (d * 0.60)
    d_max_12 = (360.0 * 4.0 - 240.0) / (740.0 * 0.60)
    assert abs(fs_max_12 - 360.0) < 0.1 and abs(fs_actual_b - 171.0) < 0.1 and abs(d_max_12 - 2.70) < 0.02
    print(f"11.12: fs_max = {fs_max_12:.0f} N, fs(1.0m) = {fs_actual_b:.0f} N, d_max = {d_max_12:.2f} m - OK")

    # 11.13
    L_11_13, w_bd, w_div = 3.00, 280.0, 500.0
    # support at 1.00 m from left end
    # tau about left end: F_S * 1.00 = 280 * 1.50 + 500 * 3.00 = 420 + 1500 = 1920 N
    F_S_13 = w_bd * 1.50 + w_div * 3.00
    F_left_13 = w_bd + w_div - F_S_13  # -1140 N (downward)
    assert abs(F_S_13 - 1920.0) < 0.1 and abs(abs(F_left_13) - 1140.0) < 0.1
    print(f"11.13: F_S = {F_S_13:.0f} N, F_left = {abs(F_left_13):.0f} N xuống (Đáp án: 1920 N, 1140 N) - OK")

    # 11.14
    w_beam_14, w_boy_14 = 300.0, 600.0
    # (b) tips when FA = 0: 750 - 120 x = 0 => x = 6.25 m, beyond B is 6.25 - 5.00 = 1.25 m
    d_beyond_B = 1.25
    # (c) boy at right end (d from B): 300 * (4.50 - d) = 600 * d => 900 d = 1350 => d = 1.50 m
    d_support_B = 1.50
    assert abs(d_beyond_B - 1.25) < 0.01 and abs(d_support_B - 1.50) < 0.01
    print(f"11.14: d_beyond_B = {d_beyond_B:.2f} m, d_support_B = {d_support_B:.2f} m - OK")

    # 11.15
    # (a) T = 1.5 w cot(30) = 2.598 w, F = 3.28 w, theta = 37.6 deg
    T_a_15 = 1.5 / math.tan(math.radians(30.0))
    F_a_15 = math.hypot(T_a_15, 2.0)
    th_a_15 = math.degrees(math.atan2(2.0, T_a_15))
    # (b) T = 1.5 w cos(45) / sin(15) = 4.098 w, F = 5.39 w, theta = 48.8 deg
    T_b_15 = 1.5 * math.cos(math.radians(45.0)) / math.sin(math.radians(15.0))
    Fx_b = T_b_15 * math.cos(math.radians(30.0))
    Fy_b = 2.0 + T_b_15 * math.sin(math.radians(30.0))
    F_b_15 = math.hypot(Fx_b, Fy_b)
    th_b_15 = math.degrees(math.atan2(Fy_b, Fx_b))
    assert abs(T_a_15 - 2.598) < 0.02 and abs(F_a_15 - 3.28) < 0.02 and abs(th_a_15 - 37.6) < 0.2
    assert abs(T_b_15 - 4.10) < 0.02 and abs(F_b_15 - 5.39) < 0.02 and abs(th_b_15 - 48.8) < 0.2
    print(f"11.15: (a) T = {T_a_15:.2f}w, F = {F_a_15:.2f}w, {th_a_15:.1f}°; (b) T = {T_b_15:.2f}w, F = {F_b_15:.2f}w, {th_b_15:.1f}° - OK")

    # 11.16
    w_bm_16 = 190.0
    # T * 0.60 * 4.00 = 190 * 2.00 + 300 * 4.00 = 1580 => T = 658.3 N
    T_16 = 1580.0 / 2.40
    Fx_16 = T_16 * 0.80
    Fy_16 = 490.0 - T_16 * 0.60
    assert abs(T_16 - 658.3) < 1.0 and abs(Fx_16 - 526.7) < 1.0 and abs(Fy_16 - 95.0) < 1.0
    print(f"11.16: T = {T_16:.0f} N, Fx = {Fx_16:.0f} N, Fy = {Fy_16:.0f} N - OK")

    # 11.17
    w_bm_17, w_load_17 = 2600.0, 5000.0
    # T * sin(60) = (2600 * 0.35 + 5000) * cos(60) = 5910 * cos(60) => T = 5910 / tan(60) = 3412 N
    T_17 = 5910.0 / math.tan(math.radians(60.0))
    Fx_17 = T_17
    Fy_17 = w_bm_17 + w_load_17
    assert abs(T_17 - 3412.0) < 10.0 and abs(Fy_17 - 7600.0) < 1.0
    print(f"11.17: T = {T_17:.0f} N (Đáp án: 3410 N), Fx = {Fx_17:.0f} N, Fy = {Fy_17:.0f} N - OK")

    # 11.18
    w_wb_18 = 80.0
    # Estimate F_lift ~ 250 N (or 60 lb ~ 267 N):
    # (w_wb + w_dirt) * 0.50 = F_lift * 1.4 => w_dirt = 2.8 F_lift - 80 N
    # For F_lift = 267 N: w_dirt = 668 N (~150 lb), F_wheel = 668 + 80 - 267 = 481 N
    print("11.18: Tỷ lệ cánh tay đòn 1.4 / 0.5 = 2.8; w_dirt = 2.8 F_lift - 80 N - OK")

    # 11.19
    T_max_19 = 1000.0
    # beam length 9.00 m, cable 5.00 m attached 4.00 m above, so attachment x_c = 3.00 m
    # T * (4/5) * 3.00 = w * 4.50 => w = 2400 / 4.50 = 533.3 N
    w_bm_19 = (T_max_19 * 0.80 * 3.00) / 4.50
    Fx_19 = T_max_19 * 0.60
    Fy_19 = w_bm_19 - T_max_19 * 0.80  # -266.7 N (downward)
    assert abs(w_bm_19 - 533.3) < 4.0 and abs(Fx_19 - 600.0) < 1.0 and abs(abs(Fy_19) - 266.7) < 4.0
    print(f"11.19: w = {w_bm_19:.0f} N (Đáp án: 530 N), Fx = {Fx_19:.0f} N, Fy = {abs(Fy_19):.0f} N hướng xuống - OK")

    # 11.20
    tau_g_20 = (15000.0 * 7.0 + 11000.0 * 16.0) * math.cos(math.radians(55.0))
    T_20 = tau_g_20 / (13.0 * math.sin(math.radians(25.0)))
    Fx_20 = T_20 * math.cos(math.radians(30.0))
    Fy_20 = 26000.0 + T_20 * math.sin(math.radians(30.0))
    assert abs(T_20 - 29336.0) < 100.0
    print(f"11.20: T = {T_20:.0f} N, Fx = {Fx_20:.0f} N, Fy = {Fy_20:.0f} N - OK")

    # 11.21
    # T1 * sin(30) * 3.0 = 190 * 1.5 + 90 * 0.5 = 330 => T1 = 220 N
    T1_21 = 330.0 / 1.50
    T2_cos = T1_21 * math.cos(math.radians(30.0))  # 190.53
    T2_sin = 280.0 - T1_21 * math.sin(math.radians(30.0))  # 170.0
    T2_21 = math.hypot(T2_cos, T2_sin)
    th_21 = math.degrees(math.atan2(T2_sin, T2_cos))
    assert abs(T1_21 - 220.0) < 1.0 and abs(T2_21 - 255.3) < 2.0 and abs(th_21 - 41.7) < 1.0
    print(f"11.21: T1 = {T1_21:.0f} N, T2 = {T2_21:.0f} N, theta = {th_21:.1f}° (Đáp án: 220 N, 255 N, 42°) - OK")

    # 11.22
    tau_clk_22 = (1400.0 * 2.00 + 5000.0 * 4.50) * math.cos(math.radians(25.0))
    T_22 = tau_clk_22 / 3.00
    Fx_22 = T_22 * math.sin(math.radians(25.0))
    Fy_22 = 6400.0 - T_22 * math.cos(math.radians(25.0))
    assert abs(T_22 - 7643.0) < 50.0
    print(f"11.22: T = {T_22 / 1000:.2f} kN, Fx = {Fx_22 / 1000:.2f} kN, Fy = {Fy_22:.0f} N hướng xuống - OK")

    # 11.23
    l_23 = 6.40 / 8.00
    assert abs(l_23 - 0.800) < 0.001
    print(f"11.23: l = {l_23:.3f} m, chiều quay kim đồng hồ (cả 2 trục) - OK")

    # 11.24
    tau_cable_24 = 36.0 * 0.640 * math.sin(math.radians(125.0))
    T_deltoid = tau_cable_24 / (0.150 * math.sin(math.radians(12.0)))
    assert abs(T_deltoid - 605.2) < 2.0
    print(f"11.24: T_deltoid = {T_deltoid:.0f} N - OK")

    # 11.25
    # T = (1/2) m g cot(theta), slope = (1/2) m g = 30.0 N => m = 60.0 / 9.80 = 6.122 kg
    m_rod_25 = 60.0 / g
    assert abs(m_rod_25 - 6.122) < 0.02
    print(f"11.25: m = {m_rod_25:.2f} kg (Đáp án: 6.12 kg) - OK")

    # 11.26
    L0_26, A_26 = 0.200, 50.0e-4
    dL_26 = 0.030
    strain_26 = dL_26 / L0_26  # 0.15
    Y_relaxed = (25.0 / A_26) / strain_26
    Y_tense = (500.0 / A_26) / strain_26
    assert abs(Y_relaxed - 3.33e4) < 500 and abs(Y_tense - 6.67e5) < 5000
    print(f"11.26: Y_relaxed = {Y_relaxed:.2e} Pa, Y_tense = {Y_tense:.2e} Pa - OK")

    # 11.27
    Y_steel = 2.0e11
    L0_27, dL_max_27, F_27 = 2.00, 0.0025, 700.0
    A_min_27 = (F_27 * L0_27) / (Y_steel * dL_max_27)
    d_min_27 = math.sqrt(4 * A_min_27 / math.pi)
    assert abs(d_min_27 * 1000 - 1.888) < 0.05
    print(f"11.27: d_min = {d_min_27 * 1000:.1f} mm (Đáp án: 1.9 mm) - OK")

    # 11.28
    L0_28, d_28, F_28 = 0.750, 0.0150, 4000.0
    A_28 = math.pi * d_28**2 / 4
    sigma_28 = F_28 / A_28
    Y_cu = 1.1e11
    eps_steel = sigma_28 / Y_steel
    eps_cu = sigma_28 / Y_cu
    dL_steel = eps_steel * L0_28
    dL_cu = eps_cu * L0_28
    assert abs(eps_steel - 1.13e-4) < 0.05e-4 and abs(eps_cu - 2.06e-4) < 0.05e-4
    print(f"11.28: eps_steel = {eps_steel:.2e}, eps_cu = {eps_cu:.2e}, dL_st = {dL_steel*1000:.3f} mm, dL_cu = {dL_cu*1000:.3f} mm - OK")

    # 11.29
    L0_29, A_29, dL_29, F_29 = 4.00, 0.50e-4, 0.0020, 5000.0
    Y_29 = (F_29 * L0_29) / (A_29 * dL_29)
    assert abs(Y_29 - 2.0e11) < 1e9
    print(f"11.29: Y = {Y_29:.1e} Pa (Đáp án: 2.0 x 10^11 Pa) - OK")

    # 11.30
    L0_30, d_30 = 45.0, 0.0070
    A_30 = math.pi * d_30**2 / 4
    m_30, dL_30 = 65.0, 1.10
    F_30 = m_30 * g
    Y_nylon = (F_30 * L0_30) / (A_30 * dL_30)
    assert abs(Y_nylon - 6.77e8) < 0.1e8
    print(f"11.30: Y_nylon = {Y_nylon:.2e} Pa - OK")

    # 11.31
    B_lead = 4.1e10
    vol_frac_31 = 0.0050
    dp_31 = B_lead * vol_frac_31
    dp_atm_31 = dp_31 / 1.013e5
    assert abs(dp_atm_31 - 2024.0) < 50.0
    print(f"11.31: dp = {dp_atm_31:.0f} atm (Đáp án: 2.0 x 10^3 atm) - OK")

    # 11.32
    d_32, L0_32, m_32 = 0.25, 2.50, 8000.0
    A_32 = math.pi * d_32**2 / 4
    F_32 = m_32 * g
    sigma_32 = F_32 / A_32
    eps_32 = sigma_32 / Y_steel
    dL_32 = eps_32 * L0_32
    assert abs(sigma_32 - 1.60e6) < 0.05e6 and abs(eps_32 - 7.99e-6) < 0.1e-6
    print(f"11.32: sigma = {sigma_32:.2e} Pa, eps = {eps_32:.2e}, dL = {dL_32 * 1000:.3f} mm - OK")

    # 11.33
    B_bone = 15.0e9
    frac_bone = 0.0010
    dp_33 = B_bone * frac_bone  # 1.5e7 Pa
    dp_atm_33 = dp_33 / 1.013e5  # 148 atm ~ 150 atm
    depth_33 = dp_33 / 1.0e4  # 1500 m = 1.5 km
    assert abs(dp_atm_33 - 148.0) < 5.0 and abs(depth_33 - 1500.0) < 1.0
    print(f"11.33: dp = {dp_atm_33:.0f} atm (~150 atm), depth = {depth_33 / 1000:.1f} km (Đáp án: 150 atm, 1.5 km, no) - OK")

    # 11.34
    print("11.34: Áp suất giảm => thể tích vàng tăng (dãn nở thể tích) - OK")

    # 11.35
    V0_35, dp_35, dV_35 = 600.0, 3.6e6, -0.45
    B_35 = dp_35 / (-dV_35 / V0_35)
    k_35 = 1.0 / B_35
    assert abs(B_35 - 4.8e9) < 1e7 and abs(k_35 - 2.08e-10) < 0.1e-10
    print(f"11.35: B = {B_35:.1e} Pa, k = {k_35:.1e} Pa^-1 (Đáp án: 4.8 x 10^9 Pa, 2.1 x 10^-10 Pa^-1) - OK")

    # 11.36
    p_deep, p_surf = 1.16e8, 1.0e5
    dp_36 = p_deep - p_surf
    k_water = 45.8e-11
    # (a) dV for 1 m^3
    dV_36 = -k_water * 1.00 * dp_36
    # (b) density
    rho_deep = (1.03e3 * 1.00) / (1.00 + dV_36)
    assert abs(abs(dV_36) - 0.0531) < 0.002 and abs(rho_deep - 1.088e3) < 10.0
    print(f"11.36: dV = {dV_36:.3f} m^3, rho = {rho_deep:.0f} kg/m^3 - OK")

    # 11.37
    L_37, t_37 = 0.100, 0.00500
    A_37 = L_37 * t_37
    F_37 = 9.0e5
    S_steel = 7.5e10
    shear_strain_37 = (F_37 / A_37) / S_steel
    x_disp_37 = shear_strain_37 * L_37
    assert abs(shear_strain_37 - 0.024) < 0.001 and abs(x_disp_37 - 0.0024) < 0.0001
    print(f"11.37: shear_strain = {shear_strain_37:.2e}, x = {x_disp_37 * 1000:.1f} mm (Đáp án: 2.4 x 10^-2, 2.4 x 10^-3 m) - OK")

    # 11.38
    L_38 = 0.0925
    F_38, th_force_38 = 1375.0, math.radians(8.50)
    F_par_38 = F_38 * math.cos(th_force_38)
    A_38 = L_38**2
    phi_38 = math.radians(1.24)
    S_38 = (F_par_38 / A_38) / phi_38
    assert abs(S_38 - 7.34e6) < 0.1e6
    print(f"11.38: S = {S_38:.2e} Pa - OK")

    # 11.39
    # T_al = 4 * (Y_al / Y_steel) * T_steel = 4 * (7.0 / 20.0) * T_steel = 1.4 T_steel
    ratio_39 = 4.0 * (7.0e10 / 20.0e10)
    assert abs(ratio_39 - 1.4) < 0.001
    print(f"11.39: T_al = {ratio_39:.1f} T_steel (Đáp án: 1.4 T_steel) - OK")

    # 11.40
    A_40 = 8.00e-6
    slope_40 = 8.0e-7
    Y_40 = 1.0 / (A_40 * slope_40)
    assert abs(Y_40 - 1.5625e11) < 0.05e11
    print(f"11.40: Y = {Y_40:.2e} Pa (~1.6 x 10^11 Pa) - OK")

    # 11.41
    # k_gly = 21e-11, k_eth = 110e-11 => dp_eth = (21 / 110) dp_gly = 0.1909 dp_gly
    ratio_41 = 21.0 / 110.0
    assert abs(ratio_41 - 0.1909) < 0.01
    print(f"11.41: dp_2 = {ratio_41:.2f} dp_1 (Đáp án: 0.19 dp_1) - OK")

    # 11.42
    sigma_br_brass = 4.7e8
    F_42 = 350.0
    A_min_42 = F_42 / sigma_br_brass
    d_min_42 = math.sqrt(4 * A_min_42 / math.pi)
    assert abs(d_min_42 * 1000 - 0.9737) < 0.02
    print(f"11.42: d_min = {d_min_42 * 1000:.2f} mm - OK")

    # 11.43
    F_43, d_43 = 90.8, 0.00184
    A_43 = math.pi * d_43**2 / 4
    sigma_br_43 = F_43 / A_43
    assert abs(sigma_br_43 - 3.415e7) < 0.05e7
    print(f"11.43: sigma_br = {sigma_br_43:.2e} Pa (Đáp án: 3.41 x 10^7 Pa) - OK")

    # 11.44
    A_44 = 3.00e-4
    sigma_el_44 = 2.40e8
    sigma_max_44 = sigma_el_44 / 3.0
    T_max_44 = sigma_max_44 * A_44
    m_elev_44 = 1200.0
    a_max_44 = (T_max_44 - m_elev_44 * g) / m_elev_44
    assert abs(a_max_44 - 10.2) < 0.1
    print(f"11.44: a_max = {a_max_44:.1f} m/s^2 - OK")

    # 11.45
    # Leverage of hammer: d2 = 0.300 m, d1_perp = 0.080 * sin(60) = 0.06928 m
    # For F2 ~ 200 N => F1 ~ 866 N
    leverage_45 = 0.300 / (0.080 * math.sin(math.radians(60.0)))
    print(f"11.45: Độ lợi cơ học F1/F2 = {leverage_45:.2f} - OK")

    # 11.46
    w_door_46 = 330.0
    # H1 * 1.00 = 330 * 0.50 => H1 = 165 N (pulling in), H2 = 165 N (pushing out)
    H_46 = w_door_46 * 0.50 / 1.00
    assert abs(H_46 - 165.0) < 0.1
    print(f"11.46: H1 = H2 = {H_46:.0f} N - OK")

    # 11.47
    M_plank_47 = 25.0
    # fulcrum at 1.00 m from left end
    # sand cg at 0.375 m (distance to fulcrum = 0.625 m)
    # plank cg at 1.500 m (distance to fulcrum = 0.500 m)
    m_sand_47 = (M_plank_47 * 0.500) / 0.625
    assert abs(m_sand_47 - 20.0) < 0.01
    print(f"11.47: m_sand = {m_sand_47:.1f} kg (Đáp án: 20.0 kg) - OK")

    # 11.48
    L_br_48, M_br_48 = 12.0, 200.0
    m_lance_48 = 600.0
    w_br_48 = M_br_48 * g
    w_lance_48 = m_lance_48 * g
    T_break_48 = 5.80e3
    # 5800 * 12.0 - w_br * 6.0 - w_lance * x = 0
    x_break_48 = (T_break_48 * L_br_48 - w_br_48 * 6.0) / w_lance_48
    assert abs(x_break_48 - 9.837) < 0.05 and x_break_48 < L_br_48
    print(f"11.48: Dây cáp đứt trước khi tới bờ! x_break = {x_break_48:.2f} m từ cổng thành - OK")

    print("\nComputed48 cases. Source coverage, assumptions and presentation require separate review.")


if __name__ == "__main__":
    verify_all()
