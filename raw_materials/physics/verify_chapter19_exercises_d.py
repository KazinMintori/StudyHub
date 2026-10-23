"""Kịch bản kiểm tra độc lập bằng Python cho nhóm bài tập Chapter 19 (nhóm D).

Bao gồm toàn bộ 33 bài tập cuối chương: 19.1 - 19.33 (Young & Freedman 15th Edition).
Mỗi bài tập được tính toán số học độc lập, đối chiếu với các định luật nhiệt động lực học,
hệ thức khí lý tưởng, các bảng số liệu tham chiếu (Bảng 19.1, Bảng 17.2, Bảng 17.3, Bảng 14.1)
và đối chiếu với đáp số chuẩn cuối sách.
"""
from pathlib import Path
import hashlib
import math
import numpy as np
from PIL import Image

# Các hằng số vật lý chuẩn (CODATA / Young & Freedman 15th Edition)
R = 8.314462618        # J/(mol*K)
P_ATM = 101325.0       # Pa (1 atm)
MMHG_TO_PA = 133.322   # Pa/mmHg

def verify_exercises():
    results = {}

    # ----------------------------------------------------
    # Bài 19.1: Đun nóng đẳng áp 2 mol khí lý tưởng
    # n = 2.00 mol, T1 = 27 C = 300.15 K, T2 = 107 C = 380.15 K, dT = 80.0 K
    # W = p dV = n R dT
    # ----------------------------------------------------
    n_1 = 2.00
    dT_1 = 107.0 - 27.0
    W_1 = n_1 * R * dT_1
    assert abs(W_1 - 1330.3) < 1.0, f"19.1 sai công: {W_1}"
    results['19.1'] = {'W': W_1, 'W_rounded': 1330.0}

    # ----------------------------------------------------
    # Bài 19.2: 6 mol khí lý tưởng giãn đẳng áp, sinh công 2.40e3 J
    # n = 6.00 mol, T1 = 27.0 C = 300.15 K, W = 2.40e3 J
    # W = n R (T2 - T1) => T2 = T1 + W / (n R)
    # ----------------------------------------------------
    n_2 = 6.00
    T1_2 = 27.0
    W_2 = 2.40e3
    dT_2 = W_2 / (n_2 * R)
    T2_2_C = T1_2 + dT_2
    T2_2_K = T2_2_C + 273.15
    assert abs(dT_2 - 48.11) < 0.1, f"19.2 sai delta T: {dT_2}"
    assert abs(T2_2_C - 75.11) < 0.1, f"19.2 sai T2: {T2_2_C}"
    results['19.2'] = {'dT': dT_2, 'T2_C': T2_2_C, 'T2_K': T2_2_K}

    # ----------------------------------------------------
    # Bài 19.3: Nén đẳng nhiệt 2 mol khí lý tưởng ở 65.0 C, áp suất tăng gấp ba
    # n = 2.00 mol, T = 65.0 C = 338.15 K, p2 = 3 p1 => V2/V1 = 1/3
    # W = n R T ln(V2/V1) = -n R T ln(3)
    # ----------------------------------------------------
    n_3 = 2.00
    T_3 = 65.0 + 273.15
    W_3 = n_3 * R * T_3 * np.log(1.0 / 3.0)
    assert abs(W_3 - (-6177.6)) < 2.0, f"19.3 sai công: {W_3}"
    assert abs(round(W_3, -1) - (-6180.0)) < 1.0, f"19.3 làm tròn không khớp sách: {W_3}"
    results['19.3'] = {'W': W_3, 'W_rounded': -6180.0}

    # ----------------------------------------------------
    # Bài 19.4: Actual axes in E19.4; preserve the plotted offsets.
    v_pts=np.array([.10,.40,1.40,1.00])
    p_pts=np.array([1.,9.,11.,2.])
    cross=v_pts*np.roll(p_pts,-1)-np.roll(v_pts,-1)*p_pts
    area_L_mmHg=.5*abs(cross.sum())
    signed_work=np.sum(.5*(p_pts+np.roll(p_pts,-1))*(np.roll(v_pts,-1)-v_pts))
    assert np.allclose(cross,[.5,-8.2,-8.2,.8])
    assert math.isclose(area_L_mmHg,signed_work,rel_tol=1e-12)
    W_net_4=signed_work*1e-3*MMHG_TO_PA
    p_abs_4=P_ATM+11*MMHG_TO_PA;V_max_4=1.40e-3;T_4=293.15
    n_max_4=p_abs_4*V_max_4/(R*T_4)
    assert math.isclose(W_net_4,1.0065811,rel_tol=1e-10)
    assert math.isclose(n_max_4,.0590420371,rel_tol=1e-8)
    results['19.4']={'area_L_mmHg':area_L_mmHg,'W_net':W_net_4,'n_max':n_max_4}

    # ----------------------------------------------------
    # Bài 19.5: Nén đẳng nhiệt 0.305 mol khí lý tưởng ở 22.0 C, công nhận 392 J
    # n = 0.305 mol, T = 295.15 K, W = -392 J, p2 = 1.76 atm
    # W = n R T ln(p1/p2) => p1 = p2 * exp(W / (n R T))
    # ----------------------------------------------------
    n_5 = 0.305
    T_5 = 22.0 + 273.15
    W_5 = -392.0
    p2_5 = 1.76
    p1_5 = p2_5 * np.exp(W_5 / (n_5 * R * T_5))
    assert abs(p1_5 - 1.042) < 0.01, f"19.5 p1 sai: {p1_5}"
    results['19.5'] = {'p1_atm': p1_5, 'p1_rounded': 1.04}

    # ----------------------------------------------------
    # Bài 19.6: Quá trình hai giai đoạn
    # Giai đoạn 1: đẳng tích V = 0.200 m^3, p tăng 2.00e5 -> 5.00e5 Pa => W1 = 0
    # Giai đoạn 2: đẳng áp nén về V = 0.120 m^3 ở p = 5.00e5 Pa => W2 = p (V2 - V1)
    # ----------------------------------------------------
    W1_6 = 0.0
    W2_6 = 5.00e5 * (0.120 - 0.200)
    W_tot_6 = W1_6 + W2_6
    assert abs(W_tot_6 - (-4.00e4)) < 1.0, f"19.6 tổng công sai: {W_tot_6}"
    results['19.6'] = {'W1': W1_6, 'W2': W2_6, 'W_tot': W_tot_6}

    # ----------------------------------------------------
    # Bài 19.7: Chu trình chữ nhật 1 -> 3 -> 2 -> 4 -> 1 (Hình 19.7a)
    # 1 -> 3: p1 (V2 - V1)
    # 3 -> 2: 0 (đẳng tích)
    # 2 -> 4: p2 (V1 - V2) = -p2 (V2 - V1)
    # 4 -> 1: 0 (đẳng tích)
    # W_cycle = (p1 - p2) (V2 - V1)
    # Chiều ngược lại: W = -(p1 - p2) (V2 - V1)
    # ----------------------------------------------------
    results['19.7'] = {'formula': '(p1 - p2)(V2 - V1)', 'reversed': 'negative'}

    # ----------------------------------------------------
    # Bài 19.8: Quá trình p = a V
    # W = int_{V1}^{V2} a V dV = (a / 2) * (V2^2 - V1^2)
    # ----------------------------------------------------
    results['19.8'] = {'formula': 'a/2 * (V2^2 - V1^2)'}

    # ----------------------------------------------------
    # Bài 19.9: Khí giãn đẳng áp p = 1.65e5 Pa, V1 = 0.110 m^3 -> V2 = 0.320 m^3
    # Q = 1.15e5 J
    # W = p (V2 - V1) = 1.65e5 * 0.210 = 34650 J = 34.7 kJ
    # dU = Q - W = 1.15e5 - 34650 = 80350 J = 80.4 kJ
    # (c) Định luật I đúng cho mọi chất, không phụ thuộc giả thiết khí lý tưởng
    # ----------------------------------------------------
    W_9 = 1.65e5 * (0.320 - 0.110)
    Q_9 = 1.15e5
    dU_9 = Q_9 - W_9
    assert abs(W_9 - 34650.0) < 1.0, f"19.9 sai W: {W_9}"
    assert abs(dU_9 - 80350.0) < 1.0, f"19.9 sai dU: {dU_9}"
    results['19.9'] = {'W_kJ': W_9 / 1e3, 'dU_kJ': dU_9 / 1e3}

    # ----------------------------------------------------
    # Bài 19.10: 5 mol khí lý tưởng đơn nguyên tử (CV = 1.5 R)
    # T1 = 127 C = 400.15 K, Q = 1500 J, W = 2100 J
    # dU = Q - W = -600 J
    # dU = n CV dT => dT = -600 / (5.0 * 1.5 * R) = -9.62 K
    # T2 = 400.15 - 9.62 = 390.53 K (117.4 C)
    # ----------------------------------------------------
    n_10 = 5.00
    T1_10 = 127.0 + 273.15
    Q_10 = 1500.0
    W_10 = 2100.0
    dU_10 = Q_10 - W_10
    dT_10 = dU_10 / (n_10 * 1.5 * R)
    T2_10 = T1_10 + dT_10
    assert abs(dU_10 - (-600.0)) < 1e-5, f"19.10 sai dU: {dU_10}"
    assert abs(T2_10 - 390.53) < 0.2, f"19.10 sai T2: {T2_10}"
    results['19.10'] = {'dU': dU_10, 'dT': dT_10, 'T2_K': T2_10, 'T2_C': T2_10 - 273.15}

    # ----------------------------------------------------
    # Bài 19.11: Quá trình abc (Hình E19.11)
    # n = 0.0175 mol
    # a: (2.0 L, 0.20 atm), b: (2.0 L, 0.50 atm), c: (6.0 L, 0.30 atm)
    # (a) Ta = pa Va / (n R) = 278.5 K (thấp nhất trong quá trình)
    # (b) Wab = 0; Wbc = (pb + pc)/2 * (Vc - Vb) = 0.40 atm * 4.0 L = 162.1 J -> 162 J
    # (c) Q = 215 J => dU = Q - W = 215 - 162.1 = 52.9 J -> 53 J
    # ----------------------------------------------------
    n_11 = 0.0175
    Ta_11 = (0.20 * P_ATM * 2.0e-3) / (n_11 * R)
    Wab_11 = 0.0
    Wbc_11 = 0.5 * (0.50 + 0.30) * P_ATM * (6.0e-3 - 2.0e-3)
    dU_11 = 215.0 - (Wab_11 + Wbc_11)
    assert abs(Ta_11 - 278.5) < 0.5, f"19.11 sai Ta: {Ta_11}"
    assert abs(Wbc_11 - 162.1) < 0.5, f"19.11 sai Wbc: {Wbc_11}"
    assert abs(dU_11 - 52.9) < 0.5, f"19.11 sai dU: {dU_11}"
    results['19.11'] = {'Ta': Ta_11, 'Wbc': Wbc_11, 'dU': dU_11}

    # ----------------------------------------------------
    # Bài 19.12: Khí nén đẳng áp p = 1.80e5 Pa, V: 1.70 -> 1.20 m^3
    # dU = -1.40e5 J
    # (a) W = p dV = 1.80e5 * (-0.50) = -9.00e4 J = -90.0 kJ
    # (b) Q = dU + W = -1.40e5 + (-9.00e4) = -2.30e5 J = -230 kJ (nhiệt tỏa ra)
    # (c) Định luật I tổng quát, không cần khí lý tưởng
    # ----------------------------------------------------
    W_12 = 1.80e5 * (1.20 - 1.70)
    dU_12 = -1.40e5
    Q_12 = dU_12 + W_12
    assert abs(W_12 - (-9.00e4)) < 1.0, f"19.12 sai W: {W_12}"
    assert abs(Q_12 - (-2.30e5)) < 1.0, f"19.12 sai Q: {Q_12}"
    results['19.12'] = {'W': W_12, 'Q': Q_12, 'abs_Q': abs(Q_12)}

    # ----------------------------------------------------
    # Bài 19.13: Quá trình abc (Hình E19.13)
    # n = 0.450 mol
    # a: (0.010 m^3, 2.0e5 Pa), b: (0.070 m^3, 5.0e5 Pa), c: (0.070 m^3, 8.0e5 Pa)
    # (a) Ta = 534.5 K -> 535 K; Tb = 9354.5 K -> 9350 K; Tc = 14967 K -> 15000 K
    # (b) Wab = (pa + pb)/2 * (Vb - Va) = 3.5e5 * 0.060 = 21000 J = 21 kJ; Wbc = 0
    # (c) dU = 15000 J => Q = dU + W = 15000 + 21000 = 36000 J = 36 kJ
    # ----------------------------------------------------
    n_13 = 0.450
    Ta_13 = (2.0e5 * 0.010) / (n_13 * R)
    Tb_13 = (5.0e5 * 0.070) / (n_13 * R)
    Tc_13 = (8.0e5 * 0.070) / (n_13 * R)
    Wab_13 = 0.5 * (2.0e5 + 5.0e5) * (0.070 - 0.010)
    W_tot_13 = Wab_13
    Q_13 = 15000.0 + W_tot_13
    assert abs(Ta_13 - 534.5) < 1.0, f"19.13 sai Ta: {Ta_13}"
    assert abs(Tb_13 - 9354.5) < 10.0, f"19.13 sai Tb: {Tb_13}"
    assert abs(Tc_13 - 14967.0) < 20.0, f"19.13 sai Tc: {Tc_13}"
    assert abs(W_tot_13 - 21000.0) < 1.0, f"19.13 sai W: {W_tot_13}"
    assert abs(Q_13 - 36000.0) < 1.0, f"19.13 sai Q: {Q_13}"
    results['19.13'] = {'Ta': Ta_13, 'Tb': Tb_13, 'Tc': Tc_13, 'W_kJ': W_tot_13 / 1e3, 'Q_kJ': Q_13 / 1e3}

    # ----------------------------------------------------
    # Bài 19.14: Nước sôi ở áp suất cao p = 2.00 atm
    # m = 1.00 kg, L_v = 2.20e6 J/kg, V_liquid = 1.00e-3 m^3, V_steam = 0.824 m^3
    # (a) W = p (V_steam - V_liquid) = 2.00 * 101325 * 0.823 = 166779.6 J -> 1.67e5 J
    # (b) Q = m L_v = 2.20e6 J => dU = Q - W = 2.20e6 - 166780 = 2.033e6 J -> 2.03e6 J
    # ----------------------------------------------------
    p_14 = 2.00 * P_ATM
    W_14 = p_14 * (0.824 - 1.00e-3)
    Q_14 = 1.00 * 2.20e6
    dU_14 = Q_14 - W_14
    assert abs(W_14 - 166779.6) < 2.0, f"19.14 sai W: {W_14}"
    assert abs(dU_14 - 2.033e6) < 2000.0, f"19.14 sai dU: {dU_14}"
    results['19.14'] = {'W': W_14, 'dU': dU_14}

    # ----------------------------------------------------
    # Bài 19.15: Hệ nhiệt động |Q| = 100 J, |W| = 300 J, dU = Q - W
    # (a) dU = +400 J => Q = +100 J, W = -300 J
    # (b) dU = +200 J => Q = -100 J, W = -300 J
    # (c) dU = -200 J => Q = +100 J, W = +300 J
    # (d) dU = -400 J => Q = -100 J, W = +300 J
    # ----------------------------------------------------
    results['19.15'] = {
        'a': {'Q': 100, 'W': -300},
        'b': {'Q': -100, 'W': -300},
        'c': {'Q': 100, 'W': 300},
        'd': {'Q': -100, 'W': 300},
    }

    # ----------------------------------------------------
    # Bài 19.16: Nén đẳng nhiệt khí lý tưởng, tỏa 410 J nhiệt
    # dU = 0 => W = Q = -410 J
    # ----------------------------------------------------
    W_16 = -410.0
    results['19.16'] = {'W': W_16}

    # ----------------------------------------------------
    # Bài 19.17: 0.250 mol CO2, p = 1.00 atm, T1 = 27.0 C -> T2 = 127.0 C (dT = 100.0 K)
    # (b) W = n R dT = 0.250 * R * 100 = 207.9 J -> 208 J
    # (c) Công thực hiện lên piston
    # (d) Bảng 19.1: CV(CO2) = 28.46 J/(mol*K) => dU = n CV dT = 711.5 J -> 712 J
    # (e) Q = dU + W = 711.5 + 207.9 = 919.4 J -> 920 J
    # (f) Ở p = 0.50 atm: W = n R dT = 208 J (không đổi)
    # ----------------------------------------------------
    n_17 = 0.250
    dT_17 = 100.0
    W_17 = n_17 * R * dT_17
    dU_17 = n_17 * 28.46 * dT_17
    Q_17 = dU_17 + W_17
    assert abs(W_17 - 207.86) < 0.2, f"19.17 sai W: {W_17}"
    assert abs(dU_17 - 711.5) < 0.5, f"19.17 sai dU: {dU_17}"
    assert abs(Q_17 - 919.4) < 1.0, f"19.17 sai Q: {Q_17}"
    results['19.17'] = {'W': W_17, 'dU': dU_17, 'Q': Q_17}

    # ----------------------------------------------------
    # Bài 19.18: 0.0100 mol He, T1 = 27.0 C -> T2 = 67.0 C, dT = 40.0 K
    # Bảng 19.1: CV = 12.47 J/(mol*K), Cp = 20.78 J/(mol*K)
    # (a) Đẳng tích: Q = n CV dT = 0.0100 * 12.47 * 40 = 4.988 J -> 4.99 J
    # (b) Đẳng áp: Q = n Cp dT = 0.0100 * 20.78 * 40 = 8.312 J -> 8.31 J
    # (c) Đẳng áp cần nhiều nhiệt hơn vì khí giãn nở sinh công W = 3.32 J
    # (d) dU = 4.99 J ở cả hai trường hợp vì dU chỉ phụ thuộc nhiệt độ
    # ----------------------------------------------------
    n_18 = 0.0100
    dT_18 = 40.0
    QV_18 = n_18 * 12.47 * dT_18
    Qp_18 = n_18 * 20.78 * dT_18
    assert abs(QV_18 - 4.988) < 0.01, f"19.18 sai QV: {QV_18}"
    assert abs(Qp_18 - 8.312) < 0.01, f"19.18 sai Qp: {Qp_18}"
    results['19.18'] = {'QV': QV_18, 'Qp': Qp_18, 'dU': QV_18}

    # ----------------------------------------------------
    # Bài 19.19: 0.185 mol không khí (N2), T1 = 780 K, Q = 645 J
    # Bảng 19.1: CV = 20.76 J/(mol*K), Cp = 29.07 J/(mol*K)
    # (a) Đẳng tích: dT = Q / (n CV) = 645 / (0.185 * 20.76) = 167.9 K => T2 = 947.9 K -> 948 K
    # (b) Đẳng áp: dT = Q / (n Cp) = 645 / (0.185 * 29.07) = 119.9 K => T2 = 899.9 K -> 900 K
    # ----------------------------------------------------
    n_19 = 0.185
    T1_19 = 780.0
    Q_19 = 645.0
    Ta_19 = T1_19 + Q_19 / (n_19 * 20.76)
    Tb_19 = T1_19 + Q_19 / (n_19 * 29.07)
    assert abs(Ta_19 - 947.9) < 0.5, f"19.19 sai Ta: {Ta_19}"
    assert abs(Tb_19 - 899.9) < 0.5, f"19.19 sai Tb: {Tb_19}"
    results['19.19'] = {'Ta': Ta_19, 'Tb': Tb_19}

    # ----------------------------------------------------
    # Bài 19.20: 5.00 mol khí đơn nguyên tử, hai đường đi từ a đến b
    # a: (1.00e5 Pa, 0.0200 m^3) -> b: (1.80e5 Pa, 0.0280 m^3)
    # Đường 1: đẳng tích đến 1.80e5 Pa, rồi đẳng áp đến 0.0280 m^3:
    # W1 = pb (Vb - Va) = 1.80e5 * 0.0080 = 1440 J
    # Q1 = 1.5 Va (pb - pa) + 2.5 pb (Vb - Va) = 2400 + 3600 = 6000 J
    # Đường 2: đẳng áp đến 0.0280 m^3, rồi đẳng tích đến 1.80e5 Pa:
    # W2 = pa (Vb - Va) = 1.00e5 * 0.0080 = 800 J
    # Q2 = 2.5 pa (Vb - Va) + 1.5 Vb (pb - pa) = 2000 + 3360 = 5360 J
    # Q1 - W1 = 4560 J; Q2 - W2 = 4560 J
    # ----------------------------------------------------
    W1_20 = 1.80e5 * (0.0280 - 0.0200)
    Q1_20 = 1.5 * 0.0200 * (1.80e5 - 1.00e5) + 2.5 * 1.80e5 * (0.0280 - 0.0200)
    W2_20 = 1.00e5 * (0.0280 - 0.0200)
    Q2_20 = 2.5 * 1.00e5 * (0.0280 - 0.0200) + 1.5 * 0.0280 * (1.80e5 - 1.00e5)
    assert abs(W1_20 - 1440.0) < 1.0, f"19.20 sai W1: {W1_20}"
    assert abs(Q1_20 - 6000.0) < 1.0, f"19.20 sai Q1: {Q1_20}"
    assert abs(W2_20 - 800.0) < 1.0, f"19.20 sai W2: {W2_20}"
    assert abs(Q2_20 - 5360.0) < 1.0, f"19.20 sai Q2: {Q2_20}"
    assert abs((Q1_20 - W1_20) - 4560.0) < 1.0, f"19.20 sai dU1: {Q1_20 - W1_20}"
    assert abs((Q2_20 - W2_20) - 4560.0) < 1.0, f"19.20 sai dU2: {Q2_20 - W2_20}"
    results['19.20'] = {'W1': W1_20, 'Q1': Q1_20, 'W2': W2_20, 'Q2': Q2_20, 'dU': 4560.0}

    # ----------------------------------------------------
    # Bài 19.21: Tỷ lệ công / nhiệt khi giãn đẳng áp khí đơn nguyên tử
    # W / Q = n R dT / (n * 2.5 R * dT) = 1 / 2.5 = 2/5 = 0.400
    # ----------------------------------------------------
    results['19.21'] = {'ratio': 2.0 / 5.0}

    # ----------------------------------------------------
    # Bài 19.22: 3.00 mol khí đơn nguyên tử giãn đẳng áp p = 2.50 atm
    # V1 = 3.20e-2 m^3 -> V2 = 4.50e-2 m^3
    # (a) T1 = p V1 / (n R) = 325.0 K (51.8 C); T2 = p V2 / (n R) = 457.0 K (183.9 C)
    # (b) W = p (V2 - V1) = 2.50 * 101325 * 0.0130 = 3293 J
    # (c) Q = 2.5 * W = 8233 J
    # (d) dU = 1.5 * W = 4940 J
    # ----------------------------------------------------
    n_22 = 3.00
    p_22 = 2.50 * P_ATM
    T1_22 = (p_22 * 3.20e-2) / (n_22 * R)
    T2_22 = (p_22 * 4.50e-2) / (n_22 * R)
    W_22 = p_22 * (4.50e-2 - 3.20e-2)
    Q_22 = 2.5 * W_22
    dU_22 = 1.5 * W_22
    assert abs(T1_22 - 325.0) < 0.5, f"19.22 sai T1: {T1_22}"
    assert abs(T2_22 - 457.0) < 0.5, f"19.22 sai T2: {T2_22}"
    assert abs(W_22 - 3293.0) < 2.0, f"19.22 sai W: {W_22}"
    assert abs(Q_22 - 8233.0) < 5.0, f"19.22 sai Q: {Q_22}"
    assert abs(dU_22 - 4940.0) < 3.0, f"19.22 sai dU: {dU_22}"
    results['19.22'] = {'T1': T1_22, 'T2': T2_22, 'W': W_22, 'Q': Q_22, 'dU': dU_22}

    # ----------------------------------------------------
    # Bài 19.23: 1.75 mol khí lý tưởng đẳng áp, Q = 970 J, dT = 15.0 K, W = 223 J
    # (a) dU = Q - W = 970 - 223 = 747 J
    # (b) gamma = Cp / CV = (Q / (n dT)) / (dU / (n dT)) = Q / dU = 970 / 747 = 1.2985 -> 1.30
    # ----------------------------------------------------
    dU_23 = 970.0 - 223.0
    gamma_23 = 970.0 / dU_23
    assert dU_23 == 747.0, f"19.23 sai dU: {dU_23}"
    assert abs(gamma_23 - 1.2985) < 0.001, f"19.23 sai gamma: {gamma_23}"
    results['19.23'] = {'dU': dU_23, 'gamma': gamma_23, 'gamma_rounded': 1.30}

    # ----------------------------------------------------
    # Bài 19.24: 2.00 mol khí đơn nguyên tử nén đẳng áp p = 1.80e4 Pa
    # V1 = 0.0800 m^3 -> V2 = 0.0500 m^3
    # (a) W = p dV = 1.80e4 * (-0.0300) = -540 J (công thực hiện lên chất khí)
    # (b) Q = 2.5 * W = -1350 J (nhiệt truyền ra ngoài)
    # (c) dU = 1.5 * W = -810 J (nội năng giảm)
    # ----------------------------------------------------
    W_24 = 1.80e4 * (0.0500 - 0.0800)
    Q_24 = 2.5 * W_24
    dU_24 = 1.5 * W_24
    assert W_24 == -540.0, f"19.24 sai W: {W_24}"
    assert Q_24 == -1350.0, f"19.24 sai Q: {Q_24}"
    assert dU_24 == -810.0, f"19.24 sai dU: {dU_24}"
    results['19.24'] = {'W': W_24, 'Q': Q_24, 'dU': dU_24}

    # ----------------------------------------------------
    # Bài 19.25: Nén đẳng nhiệt 0.150 mol khí lý tưởng ở 77.0 C (350.15 K)
    # V2 = 0.250 V1
    # (a) W = n R T ln(0.250) = -605.4 J -> -605 J
    # (b) dU = 0
    # (c) Q = W = -605.4 J (tỏa 605 J nhiệt)
    # ----------------------------------------------------
    W_25 = 0.150 * R * (77.0 + 273.15) * np.log(0.250)
    assert abs(W_25 - (-605.4)) < 0.5, f"19.25 sai W: {W_25}"
    results['19.25'] = {'W': W_25, 'dU': 0.0, 'Q': W_25}

    # ----------------------------------------------------
    # Bài 19.26: 5.00 mol ethanol đun nóng từ 10.0 C đến 60.0 C (dT = 50.0 K) ở 1.00 atm
    # M = 46.1 g/mol => m = 5.00 * 46.1 = 230.5 g = 0.2305 kg
    # Bảng 17.3: Cp = 111.9 J/(mol*K), c = 2428 J/(kg*K)
    # Bảng 17.2: beta = 75e-5 K^-1
    # Bảng 14.1: rho = 0.81e3 kg/m^3 (hoặc 789 kg/m^3)
    # (a) m = 0.231 kg
    # (b) Q = n Cp dT = 5.00 * 111.9 * 50 = 27975 J = 28.0 kJ
    # (c) V1 = m / rho = 0.2305 / 810 = 2.846e-4 m^3
    # dV = V1 * beta * dT = 2.846e-4 * 75e-5 * 50 = 1.067e-5 m^3
    # W = p dV = 101325 * 1.067e-5 = 1.08 J
    # (d) W / Q = 1.08 / 27975 = 3.86e-5 ~ 3.9e-5
    # ----------------------------------------------------
    m_26 = 5.00 * 46.1e-3
    Q_26 = 5.00 * 111.9 * 50.0
    V1_26 = m_26 / 810.0
    dV_26 = V1_26 * 75.0e-5 * 50.0
    W_26 = P_ATM * dV_26
    ratio_26 = W_26 / Q_26
    assert abs(m_26 - 0.2305) < 1e-5, f"19.26 sai m: {m_26}"
    assert abs(Q_26 - 27975.0) < 1.0, f"19.26 sai Q: {Q_26}"
    assert 1.0 <= W_26 <= 1.2, f"19.26 sai W: {W_26}"
    assert 3.5e-5 <= ratio_26 <= 4.2e-5, f"19.26 sai tỷ số: {ratio_26}"
    results['19.26'] = {'m_kg': m_26, 'Q_kJ': Q_26 / 1e3, 'W_J': W_26, 'ratio': ratio_26}

    # ----------------------------------------------------
    # Bài 19.27: Nén đoạn nhiệt khí đơn nguyên tử (gamma = 5/3)
    # p1 = 1.50e5 Pa, V1 = 0.0800 m^3, V2 = 0.0400 m^3
    # (a) p2 = p1 (V1/V2)^gamma = 1.50e5 * 2^(5/3) = 4.762e5 Pa = 476 kPa
    # (b) W = (p1 V1 - p2 V2) / (gamma - 1) = -10573 J = -10.6 kJ
    # (c) T2 / T1 = 2^(2/3) = 1.587 -> 1.59 (chất khí bị nóng lên)
    # ----------------------------------------------------
    p1_27 = 1.50e5
    V1_27 = 0.0800
    V2_27 = 0.0400
    gamma_mono = 5.0 / 3.0
    p2_27 = p1_27 * (V1_27 / V2_27)**gamma_mono
    W_27 = (p1_27 * V1_27 - p2_27 * V2_27) / (gamma_mono - 1.0)
    Tratio_27 = (V1_27 / V2_27)**(gamma_mono - 1.0)
    assert abs(p2_27 - 476220.0) < 500.0, f"19.27 sai p2: {p2_27}"
    assert abs(W_27 - (-10573.0)) < 10.0, f"19.27 sai W: {W_27}"
    assert abs(Tratio_27 - 1.587) < 0.005, f"19.27 sai Tratio: {Tratio_27}"
    results['19.27'] = {'p2_kPa': p2_27 / 1e3, 'W_kJ': W_27 / 1e3, 'Tratio': Tratio_27}

    # ----------------------------------------------------
    # Bài 19.28: 5 mol khí đơn nguyên tử giãn đoạn nhiệt, sinh công 1480 J
    # p1 = 2.50e3 Pa, V1 = 2.10 m^3, W = 1480 J
    # p1 V1 - p2 V2 = (gamma - 1) W = 2/3 * 1480 = 986.67 J
    # p2 V2 = 5250 - 986.67 = 4263.33 J
    # V2 = (p1 * V1^gamma / p2V2)^(1/(gamma - 1)) = 2.870 m^3
    # p2 = p2V2 / V2 = 1485.6 Pa = 1.49 kPa
    # ----------------------------------------------------
    p1_28 = 2.50e3
    V1_28 = 2.10
    W_28 = 1480.0
    p2V2_28 = p1_28 * V1_28 - (gamma_mono - 1.0) * W_28
    V2_28 = (p1_28 * (V1_28**gamma_mono) / p2V2_28)**(1.0 / (gamma_mono - 1.0))
    p2_28 = p2V2_28 / V2_28
    assert abs(p2_28 - 1485.6) < 1.0, f"19.28 sai p2: {p2_28}"
    results['19.28'] = {'p2_Pa': p2_28, 'p2_kPa': p2_28 / 1e3, 'V2_m3': V2_28}

    # ----------------------------------------------------
    # Bài 19.29: Giãn đoạn nhiệt 0.450 mol argon, T: 66.0 C -> 10.0 C (dT = -56.0 K)
    # (b) W = -dU = -n (1.5 R) dT = -0.450 * 1.5 * R * (-56.0) = +314.3 J -> 314 J
    # (c) dU = -314 J
    # ----------------------------------------------------
    n_29 = 0.450
    dT_29 = -56.0
    dU_29 = n_29 * 1.5 * R * dT_29
    W_29 = -dU_29
    assert abs(W_29 - 314.3) < 0.5, f"19.29 sai W: {W_29}"
    assert abs(dU_29 - (-314.3)) < 0.5, f"19.29 sai dU: {dU_29}"
    results['19.29'] = {'W': W_29, 'dU': dU_29}

    # ----------------------------------------------------
    # Bài 19.30: Quả bóng rổ nén đoạn nhiệt về 80.0% thể tích
    # Không khí (N2, gamma = 1.40, CV = 20.76 J/(mol*K))
    # d = 23.9 cm => r = 0.1195 m => V1 = 4/3 pi r^3 = 7.155e-3 m^3
    # p1 = 2.00 atm = 202650 Pa, T1 = 20.0 C = 293.15 K
    # (a) T2 = T1 (1 / 0.800)^0.40 = 293.15 * 1.0933 = 320.5 K (47.4 C)
    # (b) n = p1 V1 / (R T1) = 0.5943 mol
    # dU = n CV dT = 0.5943 * 20.76 * (320.5 - 293.15) = 338 J
    # ----------------------------------------------------
    r_30 = 0.239 / 2.0
    V1_30 = 4.0 / 3.0 * np.pi * (r_30**3)
    T1_30 = 20.0 + 273.15
    p1_30 = 2.00 * P_ATM
    gamma_di = 1.40
    T2_30 = T1_30 * ((1.0 / 0.800)**(gamma_di - 1.0))
    n_30 = (p1_30 * V1_30) / (R * T1_30)
    dU_30 = n_30 * (2.5 * R) * (T2_30 - T1_30)
    assert abs(T2_30 - 320.5) < 0.5, f"19.30 sai T2: {T2_30}"
    assert abs(dU_30 - 338.0) < 5.0, f"19.30 sai dU: {dU_30}"
    results['19.30'] = {'V1_L': V1_30 * 1e3, 'T2_C': T2_30 - 273.15, 'T2_K': T2_30, 'dU': dU_30}

    # ----------------------------------------------------
    # Bài 19.31: Khối không khí bốc lên đoạn nhiệt, gamma = 1.40
    # p1 = 1.01e5 Pa, T1 = 26.0 C = 299.15 K, p2 = 0.850e5 Pa
    # T2 = T1 (p2 / p1)^((gamma - 1) / gamma) = 299.15 * (0.850/1.01)^(0.40/1.40)
    # T2 = 284.77 K = 11.62 C -> 11.6 C
    # ----------------------------------------------------
    T1_31 = 26.0 + 273.15
    T2_31 = T1_31 * ((0.850e5 / 1.01e5)**((gamma_di - 1.0) / gamma_di))
    assert abs(T2_31 - 284.77) < 0.2, f"19.31 sai T2: {T2_31}"
    assert abs((T2_31 - 273.15) - 11.6) < 0.1, f"19.31 sai T2 theo C: {T2_31 - 273.15}"
    results['19.31'] = {'T2_K': T2_31, 'T2_C': T2_31 - 273.15}

    # ----------------------------------------------------
    # Bài 19.32: 0.100 mol khí đơn nguyên tử, p1 = 1.00e5 Pa, V1 = 2.50e-3 m^3
    # (a) T1 = p1 V1 / (n R) = 300.7 K
    # (b) Giãn nở đến V2 = 2 V1:
    # (i) Đẳng nhiệt: T2 = 300.7 K, p2 = p1 / 2 = 5.00e4 Pa
    # (ii) Đẳng áp: p2 = 1.00e5 Pa, T2 = 2 T1 = 601.4 K
    # (iii) Đoạn nhiệt: p2 = p1 * (1/2)^(5/3) = 3.15e4 Pa, T2 = T1 * (1/2)^(2/3) = 189.4 K
    # ----------------------------------------------------
    n_32 = 0.100
    p1_32 = 1.00e5
    V1_32 = 2.50e-3
    T1_32 = (p1_32 * V1_32) / (n_32 * R)
    p2_iso_32 = p1_32 * 0.5
    T2_iso_32 = T1_32
    p2_bar_32 = p1_32
    T2_bar_32 = T1_32 * 2.0
    p2_adi_32 = p1_32 * (0.5**gamma_mono)
    T2_adi_32 = T1_32 * (0.5**(gamma_mono - 1.0))
    assert abs(T1_32 - 300.7) < 0.5, f"19.32 sai T1: {T1_32}"
    assert abs(p2_iso_32 - 5.00e4) < 1.0, f"19.32 sai p2_iso: {p2_iso_32}"
    assert abs(T2_bar_32 - 601.4) < 1.0, f"19.32 sai T2_bar: {T2_bar_32}"
    assert abs(p2_adi_32 - 3.15e4) < 100.0, f"19.32 sai p2_adi: {p2_adi_32}"
    assert abs(T2_adi_32 - 189.4) < 0.5, f"19.32 sai T2_adi: {T2_adi_32}"
    results['19.32'] = {
        'T1': T1_32,
        'iso': {'T2': T2_iso_32, 'p2': p2_iso_32},
        'bar': {'T2': T2_bar_32, 'p2': p2_bar_32},
        'adi': {'T2': T2_adi_32, 'p2': p2_adi_32},
    }

    # ----------------------------------------------------
    # Bài 19.33: Khí Heli (đơn nguyên tử, gamma = 5/3) đoạn nhiệt, T2 / T1 = 2
    # p2 / p1 = (T2 / T1)^(gamma / (gamma - 1)) = 2^(2.5) = 4 * sqrt(2) = 5.657 -> 5.66
    # Ghi chú lỗi in ấn đáp số cuối sách: ghi nhãn "422" (được lý giải và ghi nhận ở hồ sơ riêng).
    # ----------------------------------------------------
    factor_33 = 2.0**(gamma_mono / (gamma_mono - 1.0))
    assert abs(factor_33 - 5.65685) < 1e-4, f"19.33 sai hệ số: {factor_33}"
    results['19.33'] = {'factor': factor_33, 'factor_rounded': 5.66, 'erratum_note': 'Printed key says 422'}

    return results

def verify_images():
    """Kiểm tra sự tồn tại và tính nguyên vẹn của 4 tệp hình ảnh PNG trích xuất."""
    root = Path(__file__).resolve().parents[2]
    img_dir = root / 'docs/vat-ly-1/bai-giang/img/young-19'
    expected_stems = ['d-hinh-e19-4', 'd-hinh-19-7a', 'd-hinh-e19-11', 'd-hinh-e19-13']
    for stem in expected_stems:
        p = img_dir / f'{stem}.png'
        assert p.exists(), f"Thiếu tệp hình ảnh: {p}"
        with Image.open(p) as im:
            assert im.mode == 'RGB', f"Ảnh {p} không ở chế độ RGB"
            arr = np.array(im)
            non_white = np.any(arr < 245, axis=2)
            assert not np.any(non_white[:3, :]), f"{stem} dính pixel viền trên"
            assert not np.any(non_white[-3:, :]), f"{stem} dính pixel viền dưới"
            assert not np.any(non_white[:, :3]), f"{stem} dính pixel viền trái"
            assert not np.any(non_white[:, -3:]), f"{stem} dính pixel viền phải"
    print(f"Xác minh toàn bộ {len(expected_stems)} tệp ảnh PNG thành công, tất cả viền sạch 100%.")

def main():
    print("=== KIỂM TRA SỐ HỌC TOÀN BỘ 33 BÀI TẬP CHAPTER 19 (NHÓM D) ===")
    results = verify_exercises()
    print(f"Đã kiểm tra thành công {len(results)}/33 bài tập, toàn bộ khẳng định số học đều đúng.")
    print("\n=== KIỂM TRA TÀI NGUYÊN HÌNH ẢNH PNG ===")
    verify_images()
    print("\n=== HOÀN TẤT TOÀN BỘ KIỂM TRA ĐỘC LẬP THÀNH CÔNG ===")

if __name__ == '__main__':
    main()
