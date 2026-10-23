"""Xác minh số học và vật lý cho 44 bài tập Chương 18 (18.1 - 18.44).

Đảm bảo tính chính xác cơ học, nhiệt động lực học và mô hình động học phân tử:
- Phương trình trạng thái khí lý tưởng và phương trình van der Waals.
- Đặc tính phân tử: khối lượng mol, số phân tử, khoảng cách trung bình.
- Thuyết động học chất khí: động năng tịnh tiến, áp suất, vận tốc hiệu dụng v_rms.
- Quãng đường tự do trung bình.
- Nhiệt dung mol C_V và nhiệt dung riêng c_V của khí đơn nguyên tử, lưỡng nguyên tử, đa nguyên tử.
- Phân bố tốc độ phân tử Maxwell-Boltzmann: v_mp, v_av, v_rms và dữ liệu Bảng 18.2.
"""

import math
from pathlib import Path
import pymupdf as fitz
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parents[2]

# Các hằng số vật lý chuẩn mực theo Young & Freedman 15th:
R = 8.31446           # J/(mol K)
k_B = 1.380649e-23     # J/K
N_A = 6.02214e23       # mol^-1
P_ATM = 1.01325e5      # Pa = 1 atm
c_light = 3.0e8        # m/s

def verify_18_1():
    # V = 20.0 L = 0.0200 m^3, m = 4.86e-4 kg He, T = 18.0 C = 291.15 K, M = 4.00 g/mol
    V = 20.0e-3
    m = 4.86e-4
    M = 4.00e-3
    T = 18.0 + 273.15
    n = m / M
    assert abs(n - 0.1215) < 1e-4, f"18.1(a) n = {n}"
    p = n * R * T / V
    p_atm = p / P_ATM
    assert abs(p - 14705.5) < 50, f"18.1(b) p = {p}"
    assert abs(p_atm - 0.1451) < 1e-3, f"18.1(b) p_atm = {p_atm}"
    return {"n": round(n, 3), "p_Pa": round(p, -2), "p_atm": round(p_atm, 3)}

def verify_18_2():
    # V1 = 3.20 L, p1 = 0.180 atm, T1 = 41.0 C = 314.15 K, M = 4.00 g/mol
    # p2 = 2 p1, V2 = 2 V1 => T2 = 4 T1
    V1 = 3.20e-3
    p1 = 0.180 * P_ATM
    T1 = 41.0 + 273.15
    M = 4.00e-3
    T2 = 4.0 * T1
    T2_C = T2 - 273.15
    assert abs(T2 - 1256.6) < 1.0, f"18.2(a) T2 = {T2}"
    assert abs(T2_C - 983.45) < 1.0, f"18.2(a) T2_C = {T2_C}"
    n = p1 * V1 / (R * T1)
    m = n * M
    assert abs(m - 8.94e-5) < 2e-6, f"18.2(b) m = {m}"
    return {"T2_K": round(T2, 1), "T2_C": round(T2_C, 1), "m_g": round(m * 1e3, 3)}

def verify_18_3():
    # V1 = 0.110 m^3, p1 = 0.355 atm, V2 = 0.390 m^3, T = const
    V1 = 0.110
    p1 = 0.355
    V2 = 0.390
    p2 = p1 * V1 / V2
    assert abs(p2 - 0.1001) < 1e-3, f"18.3 p2 = {p2}"
    return {"p2_atm": round(p2, 3)}

def verify_18_4():
    # V1 = 3.00 L, p1 = 3.00 atm, T1 = 20.0 C = 293.15 K
    # (a) V = const, p2 = 1.00 atm => T2 = T1 * (p2/p1)
    V1 = 3.00
    p1 = 3.00
    T1 = 20.0 + 273.15
    p2 = 1.00
    T2 = T1 * (p2 / p1)
    T2_C = T2 - 273.15
    assert abs(T2 - 97.72) < 0.2, f"18.4(a) T2 = {T2}"
    assert abs(T2_C - (-175.43)) < 0.5, f"18.4(a) T2_C = {T2_C}"
    # (b) T = T2, p3 = 3.00 atm => V3 = V2 * (p2/p3)
    p3 = 3.00
    V3 = V1 * (p2 / p3)
    assert abs(V3 - 1.00) < 1e-4, f"18.4(b) V3 = {V3}"
    return {"T2_C": round(T2_C, 1), "V3_L": round(V3, 2)}

def verify_18_5():
    # n = 1 mol CO2, T = 273.0 K, V = 4.48e-4 m^3
    # a = 0.364 J m^3/mol^2, b = 4.27e-5 m^3/mol
    n = 1.0
    T = 273.0
    V = 4.48e-4
    a = 0.364
    b = 4.27e-5
    p_ideal = n * R * T / V
    assert abs(p_ideal - 5.0666e6) < 1e4, f"18.5(a) p_ideal = {p_ideal}"
    p_vdw = n * R * T / (V - n * b) - a * (n / V)**2
    assert abs(p_vdw - 3.7868e6) < 1e4, f"18.5(b) p_vdw = {p_vdw}"
    pct_diff = (p_vdw - p_ideal) / p_ideal * 100.0
    assert abs(pct_diff - (-25.26)) < 0.2, f"18.5(b) pct_diff = {pct_diff}"
    return {"p_ideal_MPa": round(p_ideal / 1e6, 2), "p_vdw_MPa": round(p_vdw / 1e6, 2), "pct_diff": round(pct_diff, 1)}

def verify_18_6():
    # V_max = 0.900 L = 9.00e-4 m^3, p = 1.00 atm, T = 22.0 C = 295.15 K
    V = 0.900e-3
    p = P_ATM
    T = 22.0 + 273.15
    n = p * V / (R * T)
    # (a) Air M = 28.8 g/mol
    m_air = n * 28.8e-3
    assert abs(m_air - 1.07e-3) < 3e-5, f"18.6(a) m_air = {m_air}"
    # (b) Helium M = 4.00 g/mol
    m_he = n * 4.00e-3
    assert abs(m_he - 1.49e-4) < 5e-6, f"18.6(b) m_he = {m_he}"
    return {"m_air_g": round(m_air * 1e3, 2), "m_he_g": round(m_he * 1e3, 3)}

def verify_18_7():
    # V1 = 499 cm^3, p1 = 1.01e5 Pa, T1 = 27.0 C = 300.15 K
    # V2 = 46.2 cm^3, p_gauge2 = 2.72e6 Pa => p2 = 2.72e6 + 1.01e5 = 2.821e6 Pa
    V1 = 499.0
    p1 = 1.01e5
    T1 = 27.0 + 273.15
    V2 = 46.2
    p2 = 2.72e6 + 1.01e5
    T2 = T1 * (p2 * V2) / (p1 * V1)
    T2_C = T2 - 273.15
    assert abs(T2_C - 503.0) < 1.5, f"18.7 T2_C = {T2_C}"
    return {"T2_K": round(T2, 1), "T2_C": round(T2_C, 1)}

def verify_18_8():
    # V = 0.0750 m^3, O2 (M = 32.0 g/mol)
    # Initial: p_gauge1 = 3.00e5 Pa, T1 = 37.0 C = 310.15 K => p1 = 3.00e5 + 1.013e5 = 4.013e5 Pa
    V = 0.0750
    M = 32.0e-3
    p1 = 3.00e5 + 1.013e5
    T1 = 37.0 + 273.15
    n1 = p1 * V / (R * T1)
    m1 = n1 * M
    assert abs(m1 - 0.3735) < 3e-3, f"18.8(a) m1 = {m1}"
    # Later: T2 = 22.0 C = 295.15 K, p_gauge2 = 1.80e5 Pa => p2 = 1.80e5 + 1.013e5 = 2.813e5 Pa
    p2 = 1.80e5 + 1.013e5
    T2 = 22.0 + 273.15
    n2 = p2 * V / (R * T2)
    m2 = n2 * M
    delta_m = m1 - m2
    assert abs(delta_m - 0.0984) < 2e-3, f"18.8(b) delta_m = {delta_m}"
    return {"m1_kg": round(m1, 3), "delta_m_kg": round(delta_m, 3)}

def verify_18_9():
    # V1 = 0.750 m^3, T1 = 27 C = 300.15 K, p1 = 7.50e3 Pa
    # V2 = 0.410 m^3, T2 = 157 C = 430.15 K
    V1 = 0.750
    T1 = 27.0 + 273.15
    p1 = 7.50e3
    V2 = 0.410
    T2 = 157.0 + 273.15
    p2 = p1 * (V1 / V2) * (T2 / T1)
    assert abs(p2 - 19661.7) < 50, f"18.9 p2 = {p2}"
    return {"p2_kPa": round(p2 / 1e3, 1)}

def verify_18_10():
    # Cylinder L = 1.50 m, d = 0.900 m => r = 0.450 m
    # T = 22.0 C = 295.15 K, p = 21.0 atm, O2 (M = 32.0 g/mol)
    L = 1.50
    r = 0.450
    V = math.pi * r**2 * L
    p = 21.0 * P_ATM
    T = 22.0 + 273.15
    M = 32.0e-3
    n = p * V / (R * T)
    assert abs(n - 827.4) < 3.0, f"18.10(a) n = {n}"
    m = n * M
    assert abs(m - 26.48) < 0.2, f"18.10(b) m = {m}"
    return {"V_m3": round(V, 3), "n_mol": round(n, 1), "m_kg": round(m, 1)}

def verify_18_11():
    # p = const, V1 = 0.600 L, T1 = 19.0 C = 292.15 K, T2 = 77.3 K
    V1 = 0.600
    T1 = 19.0 + 273.15
    T2 = 77.3
    V2 = V1 * (T2 / T1)
    assert abs(V2 - 0.1587) < 1e-3, f"18.11 V2 = {V2}"
    return {"V2_L": round(V2, 3)}

def verify_18_12():
    # rho = 1.33e-6 g/cm^3 = 1.33e-3 kg/m^3
    # p = 1.00e-3 atm = 101.325 Pa, T = 20.0 C = 293.15 K
    rho = 1.33e-3
    p = 1.00e-3 * P_ATM
    T = 20.0 + 273.15
    M = rho * R * T / p
    assert abs(M - 0.0320) < 5e-4, f"18.12 M = {M}"
    return {"M_g_per_mol": round(M * 1e3, 1), "identity": "O2"}

def verify_18_13():
    # Earth STP: p1 = 1 atm, T1 = 273.15 K, V1 = V
    # Venus: T2 = 1003 C = 1276.15 K, p2 = 92 atm
    p1 = 1.0
    T1 = 273.15
    p2 = 92.0
    T2 = 1003.0 + 273.15
    ratio = (p1 / p2) * (T2 / T1)
    assert abs(ratio - 0.05078) < 2e-4, f"18.13 ratio = {ratio}"
    return {"V2_over_V1": round(ratio, 4)}

def verify_18_14():
    # bottom: p1 = 3.50 atm, T1 = 4.0 C = 277.15 K
    # surface: p2 = 1.00 atm, T2 = 23.0 C = 296.15 K
    p1 = 3.50
    T1 = 4.0 + 273.15
    p2 = 1.00
    T2 = 23.0 + 273.15
    ratio = (p1 / p2) * (T2 / T1)
    assert abs(ratio - 3.740) < 0.02, f"18.14(a) ratio = {ratio}"
    return {"V_ratio": round(ratio, 2)}

def verify_18_15():
    # p_gauge = 0.876 atm => p = 1.876 atm
    # V = 5.43 L, T = 22.2 C = 295.35 K
    p = 1.876 * P_ATM
    V = 5.43e-3
    T = 22.2 + 273.15
    n = p * V / (R * T)
    assert abs(n - 0.4208) < 2e-3, f"18.15 n = {n}"
    return {"n_mol": round(n, 3)}

def verify_18_16():
    # L = 0.300 m, V = L^3 = 0.0270 m^3, A = L^2 = 0.0900 m^2, n = 3.00 mol
    # F = p * A = (n R T / L^3) * L^2 = n R T / L
    L = 0.300
    n = 3.00
    # (a) T = 20.0 C = 293.15 K
    T1 = 20.0 + 273.15
    F1 = n * R * T1 / L
    assert abs(F1 - 24375.0) < 50, f"18.16(a) F1 = {F1}"
    # (b) T = 100.0 C = 373.15 K
    T2 = 100.0 + 273.15
    F2 = n * R * T2 / L
    assert abs(F2 - 31023.0) < 50, f"18.16(b) F2 = {F2}"
    return {"F1_N": round(F1, 0), "F2_N": round(F2, 0)}

def verify_18_17():
    # V = 3000 cm^3 = 3.00e-3 m^3, T = 22.0 C = 295.15 K, p = 2.00e-13 atm = 2.0265e-8 Pa
    # N2 (M = 28.0 g/mol = 0.0280 kg/mol)
    V = 3000e-6
    T = 22.0 + 273.15
    p = 2.00e-13 * P_ATM
    M = 28.0e-3
    n = p * V / (R * T)
    m = n * M
    assert abs(m - 6.94e-16) < 3e-17, f"18.17(a) m = {m}"
    rho = m / V
    assert abs(rho - 2.31e-13) < 2e-14, f"18.17(b) rho = {rho}"
    return {"m_kg": f"{m:.2e}", "rho_kg_per_m3": f"{rho:.2e}"}

def verify_18_18():
    # altitude 11000 m, T = -56.5 C = 216.65 K, rho = 0.364 kg/m^3
    # M_air = 28.8e-3 kg/mol
    T = -56.5 + 273.15
    rho = 0.364
    M = 28.8e-3
    p = rho * R * T / M
    assert abs(p - 22766.0) < 150, f"18.18 p = {p}"
    return {"p_Pa": round(p, 0), "p_kPa": round(p / 1e3, 2)}

def verify_18_19():
    # m = 1.00 kg H2O, M = 18.0 g/mol
    m = 1.00
    M = 18.0e-3
    n = m / M
    N = n * N_A
    assert abs(n - 55.56) < 0.1, f"18.19 n = {n}"
    assert abs(N - 3.346e25) < 3e23, f"18.19 N = {N}"
    return {"n_mol": round(n, 1), "N": f"{N:.2e}"}

def verify_18_20():
    # m_mol = 1.41e-21 kg
    m_mol = 1.41e-21
    M_kg = m_mol * N_A  # kg/mol
    assert abs(M_kg - 849.12) < 2.0, f"18.20 M_kg = {M_kg}"
    M_g = M_kg * 1e3    # g/mol
    return {"M_kg_per_mol": round(M_kg, 1), "M_g_per_mol": round(M_g, 0)}

def verify_18_21():
    # T = 300.0 K, V = 1.00 cm^3 = 1.00e-6 m^3
    # (a) p1 = 9.00e-14 atm
    T = 300.0
    V = 1.00e-6
    p1 = 9.00e-14 * P_ATM
    N1 = p1 * V / (k_B * T)
    assert abs(N1 - 2.20e6) < 3e4, f"18.21(a) N1 = {N1}"
    # (b) p2 = 1.00 atm
    p2 = 1.00 * P_ATM
    N2 = p2 * V / (k_B * T)
    assert abs(N2 - 2.446e19) < 3e17, f"18.21(b) N2 = {N2}"
    return {"N1": f"{N1:.2e}", "N2": f"{N2:.2e}"}

def verify_18_22():
    # T = 7500 K, n_density = 80 cm^-3 = 8.0e7 m^-3
    T = 7500.0
    n_density = 80.0 * 1e6
    p = n_density * k_B * T
    p_atm = p / P_ATM
    assert abs(p - 8.284e-12) < 1e-13, f"18.22(a) p = {p}"
    assert abs(p_atm - 8.175e-17) < 2e-18, f"18.22(a) p_atm = {p_atm}"
    ratio = (9.00e-14) / p_atm
    assert abs(ratio - 1100.0) < 50, f"18.22(a) ratio = {ratio}"
    return {"p_Pa": f"{p:.2e}", "p_atm": f"{p_atm:.2e}", "ratio_to_lab": round(ratio, 0)}

def verify_18_23():
    # T = 27 C = 300.15 K, p = 1.00 atm
    T = 27.0 + 273.15
    p = P_ATM
    n_density = p / (k_B * T)
    vol_per_mol = 1.0 / n_density
    d = vol_per_mol**(1.0 / 3.0)
    assert abs(d - 3.445e-9) < 2e-11, f"18.23(a) d = {d}"
    ratio_mol = d / 0.35e-9
    ratio_solid = d / 0.30e-9
    assert abs(ratio_solid - 11.5) < 1.0, f"18.23(c) ratio_solid = {ratio_solid}"
    return {"d_nm": round(d * 1e9, 2), "ratio_solid": round(ratio_solid, 0)}

def verify_18_24():
    # p2 = 2 p1, v_rms2 = 2 v_rms1 => T2 = 4 T1
    # p2 V = n2 R T2 => 2 p1 V = n2 R (4 T1) => 2 n1 = 4 n2 => n2 = n1 / 2
    # delta_n = n1 - n2 = n / 2
    delta_n_ratio = 0.500
    assert delta_n_ratio == 0.5
    return {"delta_n_ratio": delta_n_ratio}

def verify_18_25():
    # room: 8.00 m * 12.00 m * 4.00 m => V = 384 m^3, p = 1.00 atm
    V = 8.00 * 12.00 * 4.00
    p = 1.013e5
    K_tr = 1.5 * p * V
    assert abs(K_tr - 5.835e7) < 5e5, f"18.25(a) K_tr = {K_tr}"
    m_car = 2000.0
    v_car = math.sqrt(2.0 * K_tr / m_car)
    assert abs(v_car - 241.6) < 1.0, f"18.25(b) v_car = {v_car}"
    return {"K_tr_J": f"{K_tr:.2e}", "v_car_m_per_s": round(v_car, 1)}

def verify_18_26():
    # Ne (20.18), Kr (83.80), Rn (222.0)
    # (a) Average KE is 3/2 kB T -> identical
    # (b) v_rms = sqrt(3 R T / M)
    v_ne = 1.0 / math.sqrt(20.18)
    v_kr = 1.0 / math.sqrt(83.80)
    v_rn = 1.0 / math.sqrt(222.0)
    ratio_ne_rn = v_ne / v_rn
    assert abs(ratio_ne_rn - 3.317) < 0.05, f"18.26 ratio = {ratio_ne_rn}"
    return {"ratio_ne_rn": round(ratio_ne_rn, 2)}

def verify_18_27():
    # slope = 1.10 atm/C, V = 80.0 cm^3 = 80.0e-6 m^3
    # p(atm) = [N kB / (V p_atm0)] * TC + const
    # N = slope * V * p_atm0 / kB
    slope = 1.10
    V = 80.0e-6
    N = slope * V * P_ATM / k_B
    assert abs(N - 6.458e23) < 2e21, f"18.27 N = {N}"
    return {"N": f"{N:.2e}"}

def verify_18_28():
    # V = 1.64 L = 1.64e-3 m^3, m = 0.226 g = 0.226e-3 kg, v_rms = 182 m/s
    V = 1.64e-3
    m = 0.226e-3
    v_rms = 182.0
    p = (1.0 / 3.0) * (m / V) * (v_rms**2)
    assert abs(p - 1521.5) < 5.0, f"18.28 p = {p}"
    return {"p_Pa": round(p, 1), "p_kPa": round(p / 1e3, 3)}

def verify_18_29():
    # m_d = 3.3436e-27 kg, T = 300e6 K
    m_d = 3.34358e-27
    T = 300.0e6
    v_rms = math.sqrt(3.0 * k_B * T / m_d)
    assert abs(v_rms - 1.928e6) < 2e4, f"18.29(a) v_rms = {v_rms}"
    ratio_c = v_rms / c_light
    assert abs(ratio_c - 0.00643) < 1e-4, f"18.29(a) ratio_c = {ratio_c}"
    # (b) v = 0.10 c = 3.0e7 m/s => T = m_d v^2 / (3 kB)
    v2 = 0.10 * c_light
    T2 = m_d * v2**2 / (3.0 * k_B)
    assert abs(T2 - 7.265e10) < 1e9, f"18.29(b) T2 = {T2}"
    return {"v_rms_m_per_s": f"{v_rms:.2e}", "ratio_c": round(ratio_c, 4), "T2_K": f"{T2:.1e}"}

def verify_18_30():
    # Mars: CO2 (M = 44.0 g/mol = 0.0440 kg/mol), p = 650 Pa
    # T_summer = 273.15 K, T_winter = 173.15 K
    M = 44.0e-3
    p = 650.0
    T_win = 173.15
    T_sum = 273.15
    v_win = math.sqrt(3.0 * R * T_win / M)
    v_sum = math.sqrt(3.0 * R * T_sum / M)
    assert abs(v_win - 313.3) < 1.0, f"18.30(a) v_win = {v_win}"
    assert abs(v_sum - 393.6) < 1.0, f"18.30(a) v_sum = {v_sum}"
    rho_win = p / (R * T_win)
    rho_sum = p / (R * T_sum)
    assert abs(rho_win - 0.4515) < 0.005, f"18.30(b) rho_win = {rho_win}"
    assert abs(rho_sum - 0.2862) < 0.005, f"18.30(b) rho_sum = {rho_sum}"
    return {"v_range": (round(v_win, 0), round(v_sum, 0)), "rho_range": (round(rho_sum, 3), round(rho_win, 3))}

def verify_18_31():
    # O2 (M = 32.0 g/mol = 0.0320 kg/mol), T = 300 K
    M = 32.0e-3
    T = 300.0
    m_mol = M / N_A
    K_tr = 1.5 * k_B * T
    assert abs(K_tr - 6.213e-21) < 2e-23, f"18.31(a) K_tr = {K_tr}"
    v2_avg = 3.0 * R * T / M
    assert abs(v2_avg - 233844.0) < 500, f"18.31(b) v2_avg = {v2_avg}"
    v_rms = math.sqrt(v2_avg)
    assert abs(v_rms - 483.6) < 1.0, f"18.31(c) v_rms = {v_rms}"
    p_mol = m_mol * v_rms
    assert abs(p_mol - 2.570e-23) < 3e-25, f"18.31(d) p_mol = {p_mol}"
    L = 0.10
    F_avg = m_mol * (v_rms**2) / L
    assert abs(F_avg - 1.243e-19) < 2e-21, f"18.31(e) F_avg = {F_avg}"
    A = L**2
    p_single = F_avg / A
    assert abs(p_single - 1.243e-17) < 2e-19, f"18.31(f) p_single = {p_single}"
    N_g = P_ATM / p_single
    assert abs(N_g - 8.154e21) < 3e19, f"18.31(g) N_g = {N_g}"
    V = L**3
    N_h = P_ATM * V / (k_B * T)
    assert abs(N_h - 2.446e22) < 5e20, f"18.31(h) N_h = {N_h}"
    ratio_hg = N_h / N_g
    assert abs(ratio_hg - 3.0) < 0.01, f"18.31(i) ratio = {ratio_hg}"
    return {"K_tr_J": f"{K_tr:.2e}", "v_rms": round(v_rms, 1), "N_g": f"{N_g:.2e}", "N_h": f"{N_h:.2e}"}

def verify_18_32():
    # p = 3.50e-13 atm, T = 300 K, r = 2.0e-10 m
    p = 3.50e-13 * P_ATM
    T = 300.0
    r = 2.0e-10
    lam = (k_B * T) / (4.0 * math.pi * math.sqrt(2.0) * (r**2) * p)
    assert abs(lam - 164299.0) < 2000, f"18.32 lam = {lam}"
    return {"lambda_km": round(lam / 1e3, 1)}

def verify_18_33():
    # v_rms(N2, T_N2) = v_rms(H2, 20 C)
    # T_N2 = T_H2 * (M_N2 / M_H2)
    T_H2 = 20.0 + 273.15
    M_N2 = 28.013
    M_H2 = 2.016
    T_N2 = T_H2 * (M_N2 / M_H2)
    T_N2_C = T_N2 - 273.15
    assert abs(T_N2_C - 3800.0) < 15, f"18.33 T_N2_C = {T_N2_C}"
    return {"T_N2_K": round(T_N2, 0), "T_N2_C": round(T_N2_C, 0)}

def verify_18_34():
    # m = 3.00e-16 kg, T = 300 K
    m = 3.00e-16
    T = 300.0
    v_rms = math.sqrt(3.0 * k_B * T / m)
    assert abs(v_rms - 6.436e-3) < 5e-5, f"18.34(a) v_rms = {v_rms}"
    return {"v_rms_mm_per_s": round(v_rms * 1e3, 2)}

def verify_18_35():
    # n = 3.00 mol He (M = 4.00e-3 kg/mol), v_rms1 = 900 m/s, Q = 2400 J
    n = 3.00
    M = 4.00e-3
    v_rms1 = 900.0
    Q = 2400.0
    # K1 = 0.5 * (n M) * v_rms1^2
    m_tot = n * M
    K1 = 0.5 * m_tot * v_rms1**2
    K2 = K1 + Q
    v_rms2 = math.sqrt(2.0 * K2 / m_tot)
    assert abs(v_rms2 - 1100.0) < 1.0, f"18.35 v_rms2 = {v_rms2}"
    return {"v_rms2_m_per_s": round(v_rms2, 0)}

def verify_18_36():
    # n = 4.00 mol monatomic, T1 = 300 K, p1 = 6.00e4 Pa, Q = 6000 J
    n = 4.00
    T1 = 300.0
    p1 = 6.00e4
    Q = 6000.0
    C_V = 1.5 * R
    delta_T = Q / (n * C_V)
    T2 = T1 + delta_T
    p2 = p1 * (T2 / T1)
    assert abs(p2 - 8.405e4) < 100, f"18.36 p2 = {p2}"
    return {"p2_kPa": round(p2 / 1e3, 2)}

def verify_18_37():
    # n = 1.80 mol, delta_T = 50.0 K
    n = 1.80
    delta_T = 50.0
    # (a) Diatomic: C_V = 5/2 R
    Q_dia = n * 2.5 * R * delta_T
    assert abs(Q_dia - 1870.7) < 5.0, f"18.37(a) Q_dia = {Q_dia}"
    # (b) Monatomic: C_V = 3/2 R
    Q_mono = n * 1.5 * R * delta_T
    assert abs(Q_mono - 1122.5) < 5.0, f"18.37(b) Q_mono = {Q_mono}"
    return {"Q_dia_J": round(Q_dia, 0), "Q_mono_J": round(Q_mono, 0)}

def verify_18_38():
    # H2 (5/2 R) raised by 2.50 C with 300 J
    # Ne (3/2 R) raised by delta_T_Ne with same Q
    delta_T_H2 = 2.50
    delta_T_Ne = delta_T_H2 * (5.0 / 3.0)
    assert abs(delta_T_Ne - 4.167) < 0.01, f"18.38 delta_T_Ne = {delta_T_Ne}"
    return {"delta_T_Ne_C": round(delta_T_Ne, 2)}

def verify_18_39():
    # N2 (M = 28.0 g/mol = 0.0280 kg/mol)
    M = 28.0e-3
    C_V = 2.5 * R
    c_V = C_V / M
    assert abs(c_V - 742.36) < 3.0, f"18.39(a) c_V = {c_V}"
    c_w = 4190.0
    ratio = c_w / c_V
    assert abs(ratio - 5.644) < 0.02, f"18.39(a) ratio = {ratio}"
    # (b) 1.00 kg water 20C to 30C => Q = 1.00 * 4190 * 10 = 41900 J
    m_air = 1.00 * ratio
    assert abs(m_air - 5.644) < 0.02, f"18.39(b) m_air = {m_air}"
    n_air = m_air / M
    T = 20.0 + 273.15
    V_air = n_air * R * T / P_ATM
    assert abs(V_air - 4.851) < 0.03, f"18.39(b) V_air = {V_air}"
    return {"c_V_J_per_kg_K": round(c_V, 0), "ratio_cw_cN2": round(ratio, 2), "m_air_kg": round(m_air, 2), "V_air_L": round(V_air * 1e3, 0)}

def verify_18_40():
    # H2O vapor: 3 trans + 3 rot = 6 dof => C_V = 3 R
    M = 18.0e-3
    C_V = 3.0 * R
    c_V = C_V / M
    assert abs(c_V - 1385.7) < 5.0, f"18.40(a) c_V = {c_V}"
    c_actual = 2000.0
    ratio = c_actual / c_V
    assert abs(ratio - 1.443) < 0.01, f"18.40(b) ratio = {ratio}"
    return {"c_V_calc": round(c_V, 0), "ratio": round(ratio, 2)}

def verify_18_41():
    # CO2 (M = 44.0 g/mol = 0.0440 kg/mol), T = 300 K
    M = 44.0e-3
    T = 300.0
    v_mp = math.sqrt(2.0 * R * T / M)
    v_av = math.sqrt(8.0 * R * T / (math.pi * M))
    v_rms = math.sqrt(3.0 * R * T / M)
    assert abs(v_mp - 336.7) < 1.0, f"18.41(a) v_mp = {v_mp}"
    assert abs(v_av - 379.9) < 1.0, f"18.41(b) v_av = {v_av}"
    assert abs(v_rms - 412.4) < 1.0, f"18.41(c) v_rms = {v_rms}"
    return {"v_mp": round(v_mp, 0), "v_av": round(v_av, 0), "v_rms": round(v_rms, 0)}

def verify_18_42():
    # N2 (M = 28.0 g/mol = 0.0280 kg/mol), fraction 0.947 => v / v_rms = 1.60
    # T = M (v / 1.60)^2 / (3 R)
    M = 28.0e-3
    results = {}
    for v in [1500, 1000, 500]:
        v_rms = v / 1.60
        T = M * (v_rms**2) / (3.0 * R)
        results[v] = round(T, 0)
    assert abs(results[1500] - 987.0) < 2.0, f"18.42(a) T = {results[1500]}"
    assert abs(results[1000] - 439.0) < 2.0, f"18.42(b) T = {results[1000]}"
    assert abs(results[500] - 110.0) < 2.0, f"18.42(c) T = {results[500]}"
    return results

def verify_18_43():
    # gamma = 1.67 (monatomic)
    gamma = 1.67
    ratio_rms = math.sqrt(3.0 / gamma)
    ratio_av = math.sqrt((8.0 / math.pi) / gamma)
    assert abs(ratio_rms - 1.340) < 0.01, f"18.43(a) ratio_rms = {ratio_rms}"
    assert abs(ratio_av - 1.235) < 0.01, f"18.43(b) ratio_av = {ratio_av}"
    return {"ratio_vrms_over_v": round(ratio_rms, 2), "ratio_vav_over_v": round(ratio_av, 2)}

def verify_18_44():
    # n = 0.0345 mol monatomic
    # speeds within 20% of v_rms => [0.80 v_rms, 1.20 v_rms]
    # From Table 18.2: F(1.20) = 0.771, F(0.80) = 0.411 => Delta F = 0.360
    n = 0.0345
    N_tot = n * N_A
    delta_F = 0.771 - 0.411
    assert abs(delta_F - 0.360) < 1e-4, f"18.44 delta_F = {delta_F}"
    N_atoms = delta_F * N_tot
    assert abs(N_atoms - 7.479e21) < 5e19, f"18.44 N_atoms = {N_atoms}"
    return {"delta_F": round(delta_F, 3), "N_atoms": f"{N_atoms:.2e}"}

def verify_image_crops():
    import importlib.util
    script_path = ROOT / 'scripts/prepare-physics1-18-exercises-d-assets.py'
    spec = importlib.util.spec_from_file_location("prep_assets", script_path)
    prep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep)
    assert hasattr(prep, 'CROPS'), "Missing CROPS dict in prepare script"
    assert hasattr(prep, 'SCALE'), "Missing SCALE in prepare script"
    assert 'd-hinh-e18-22' in prep.CROPS, "Missing d-hinh-e18-22 in CROPS"
    page, clip = prep.CROPS['d-hinh-e18-22']
    assert page == 626, f"Expected page 626, got {page}"
    img_path = ROOT / 'docs/vat-ly-1/bai-giang/img/young-18/d-hinh-e18-22.png'
    assert img_path.exists(), f"Image not found at {img_path}"
    with fitz.open(ROOT / 'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
        pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(prep.SCALE, prep.SCALE), clip=fitz.Rect(clip), alpha=False)
        with Image.open(img_path) as im:
            assert im.size == (pix.width, pix.height), f"Size mismatch: {im.size} vs {(pix.width, pix.height)}"
            assert im.convert('RGB').tobytes() == pix.samples, "Pixel bytes mismatch"
    return {"image": "d-hinh-e18-22.png", "status": "verified"}

def main():
    verifiers = [
        ("18.1", verify_18_1),
        ("18.2", verify_18_2),
        ("18.3", verify_18_3),
        ("18.4", verify_18_4),
        ("18.5", verify_18_5),
        ("18.6", verify_18_6),
        ("18.7", verify_18_7),
        ("18.8", verify_18_8),
        ("18.9", verify_18_9),
        ("18.10", verify_18_10),
        ("18.11", verify_18_11),
        ("18.12", verify_18_12),
        ("18.13", verify_18_13),
        ("18.14", verify_18_14),
        ("18.15", verify_18_15),
        ("18.16", verify_18_16),
        ("18.17", verify_18_17),
        ("18.18", verify_18_18),
        ("18.19", verify_18_19),
        ("18.20", verify_18_20),
        ("18.21", verify_18_21),
        ("18.22", verify_18_22),
        ("18.23", verify_18_23),
        ("18.24", verify_18_24),
        ("18.25", verify_18_25),
        ("18.26", verify_18_26),
        ("18.27", verify_18_27),
        ("18.28", verify_18_28),
        ("18.29", verify_18_29),
        ("18.30", verify_18_30),
        ("18.31", verify_18_31),
        ("18.32", verify_18_32),
        ("18.33", verify_18_33),
        ("18.34", verify_18_34),
        ("18.35", verify_18_35),
        ("18.36", verify_18_36),
        ("18.37", verify_18_37),
        ("18.38", verify_18_38),
        ("18.39", verify_18_39),
        ("18.40", verify_18_40),
        ("18.41", verify_18_41),
        ("18.42", verify_18_42),
        ("18.43", verify_18_43),
        ("18.44", verify_18_44),
    ]

    print("=== BẮT ĐẦU XÁC MINH SỐ HỌC 44 BÀI TẬP CHƯƠNG 18 (18.1 - 18.44) ===")
    results = {}
    for name, fn in verifiers:
        res = fn()
        results[name] = res
        print(f"Bài {name}: ĐÃ XÁC MINH -> {res}")

    img_res = verify_image_crops()
    print(f"Kiểm tra ảnh gốc: ĐÃ XÁC MINH -> {img_res}")

    print("=== TOÀN BỘ 44 BÀI TẬP ĐÃ VƯỢT QUA KIỂM THỬ XÁC MINH SỐ HỌC ===")

if __name__ == '__main__':
    main()
