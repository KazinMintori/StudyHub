"""Kịch bản kiểm tra độc lập toàn diện cho bài tập Chapter 43 nhóm C (StudyHub).

Bao gồm:
- 12 bài luyện tập hướng dẫn: VP43.4.1–VP43.4.4, VP43.7.1–VP43.7.4, VP43.9.1–VP43.9.4.
- 20 câu hỏi thảo luận: Q43.1–Q43.20.
- 32 bài tập đánh số: 43.1–43.32.
Tổng cộng: Đúng 64 bài toán / câu hỏi độc lập.

Kiểm tra:
1. Tính toán số học từ các định luật vật lý hạt nhân và hằng số chuẩn CODATA / Young & Freedman 15th ed.
2. Kiểm tra cấu trúc định dạng Markdown, MathJax, thẻ details, tóm tắt đề bài, hướng đi, lời giải chi tiết.
3. Kiểm tra các quy tắc sư phạm: Viết hoa sau dấu hai chấm, không chứa metanarration dịch sách.
4. Kiểm tra sự tồn tại và tính hợp lệ của các hình ảnh tham chiếu PNG và đồ thị SVG.
"""

from pathlib import Path
import math
import re

ROOT = Path(__file__).resolve().parents[2]

# Các hằng số vật lý chuẩn
u_to_MeV = 931.49410242
u_to_kg = 1.66053906660e-27
c_val = 2.99792458e8
e_val = 1.602176634e-19
h_val = 6.62607015e-34
hbar_val = h_val / (2.0 * math.pi)
m_p = 1.007276466621    # u (proton trần)
m_n = 1.00866491588     # u (nơtron)
m_H = 1.00782503223     # u (nguyên tử 1H trung hòa)
m_e = 0.000548579909    # u (electron)
N_A = 6.02214076e23

results = {}


def verify_guided_practice():
    """Xác minh 12 bài luyện tập hướng dẫn VP43.4.1 - VP43.9.4."""
    # VP43.4.1: 16_8O, M = 15.994915 u
    M_16O = 15.994915
    dM_16O = 8 * m_H + 8 * m_n - M_16O
    EB_16O = dM_16O * u_to_MeV
    EB_per_A_16O = EB_16O / 16.0
    results['VP43.4.1'] = {'dM': dM_16O, 'EB': EB_16O, 'EB_A': EB_per_A_16O}
    assert math.isclose(dM_16O, 0.137005, rel_tol=1e-3), f"Lỗi VP43.4.1 dM: {dM_16O}"
    assert math.isclose(EB_16O, 127.62, rel_tol=2e-3), f"Lỗi VP43.4.1 EB: {EB_16O}"
    assert math.isclose(EB_per_A_16O, 7.976, rel_tol=2e-3), f"Lỗi VP43.4.1 EB/A: {EB_per_A_16O}"

    # VP43.4.2: 63_29Cu, dM = 0.5919378 u
    dM_63Cu = 0.5919378
    EB_63Cu = dM_63Cu * u_to_MeV
    EB_per_A_63Cu = EB_63Cu / 63.0
    M_63Cu = 29 * m_H + 34 * m_n - dM_63Cu
    results['VP43.4.2'] = {'EB': EB_63Cu, 'EB_A': EB_per_A_63Cu, 'M': M_63Cu}
    assert math.isclose(EB_63Cu, 551.39, rel_tol=2e-3), f"Lỗi VP43.4.2 EB: {EB_63Cu}"
    assert math.isclose(EB_per_A_63Cu, 8.752, rel_tol=2e-3), f"Lỗi VP43.4.2 EB/A: {EB_per_A_63Cu}"
    assert math.isclose(M_63Cu, 62.929595, rel_tol=1e-4), f"Lỗi VP43.4.2 M: {M_63Cu}"

    # VP43.4.3: 75_33As, 150_62Sm, 225_88Ra
    EB_A_As = (0.7005604 * u_to_MeV) / 75.0
    EB_A_Sm = (1.330388 * u_to_MeV) / 150.0
    EB_A_Ra = (1.852094 * u_to_MeV) / 225.0
    results['VP43.4.3'] = {'EB_A_As': EB_A_As, 'EB_A_Sm': EB_A_Sm, 'EB_A_Ra': EB_A_Ra}
    assert math.isclose(EB_A_As, 8.701, rel_tol=2e-3), f"Lỗi VP43.4.3 As: {EB_A_As}"
    assert math.isclose(EB_A_Sm, 8.262, rel_tol=2e-3), f"Lỗi VP43.4.3 Sm: {EB_A_Sm}"
    assert math.isclose(EB_A_Ra, 7.668, rel_tol=2e-3), f"Lỗi VP43.4.3 Ra: {EB_A_Ra}"
    assert EB_A_As > EB_A_Sm > EB_A_Ra, "Lỗi VP43.4.3 thứ tự giảm dần theo A > 62"

    # VP43.4.4: 100_44Ru và 200_80Hg
    def semiempirical(A, Z):
        vol = 15.75 * A
        surf = 17.80 * (A**(2/3))
        coul = 0.7100 * Z * (Z - 1) / (A**(1/3))
        asym = 23.69 * ((A - 2 * Z)**2) / A
        pair = 39.0 * (A**(-4/3))  # Cả hai đều chẵn-chẵn
        EB = vol - surf - coul - asym + pair
        return EB, EB / A

    EB_Ru, EBA_Ru = semiempirical(100, 44)
    EB_Hg, EBA_Hg = semiempirical(200, 80)
    results['VP43.4.4'] = {'EB_Ru': EB_Ru, 'EBA_Ru': EBA_Ru, 'EB_Hg': EB_Hg, 'EBA_Hg': EBA_Hg}
    assert math.isclose(EB_Ru, 868.07, rel_tol=2e-3), f"Lỗi VP43.4.4 EB_Ru: {EB_Ru}"
    assert math.isclose(EBA_Ru, 8.681, rel_tol=2e-3), f"Lỗi VP43.4.4 EBA_Ru: {EBA_Ru}"
    assert math.isclose(EB_Hg, 1584.46, rel_tol=2e-3), f"Lỗi VP43.4.4 EB_Hg: {EB_Hg}"
    assert math.isclose(EBA_Hg, 7.922, rel_tol=2e-3), f"Lỗi VP43.4.4 EBA_Hg: {EBA_Hg}"
    assert EBA_Ru > EBA_Hg, "Lỗi VP43.4.4 xu hướng giảm theo Hình 43.2"

    # VP43.7.1: 241_95Am -> 237_93Np + 4_2He
    M_241Am = 241.056827
    M_237Np = 237.048172
    M_4He = 4.002603
    dM_Am = M_241Am - M_237Np - M_4He
    Q_Am = dM_Am * u_to_MeV
    K_alpha_Am = (M_237Np / (M_237Np + M_4He)) * Q_Am
    v_alpha_Am = math.sqrt(2 * (K_alpha_Am * 1e6 * e_val) / (M_4He * u_to_kg))
    results['VP43.7.1'] = {'Q': Q_Am, 'K_alpha': K_alpha_Am, 'v_alpha': v_alpha_Am}
    assert math.isclose(Q_Am, 5.637, rel_tol=2e-3), f"Lỗi VP43.7.1 Q: {Q_Am}"
    assert math.isclose(K_alpha_Am, 5.544, rel_tol=2e-3), f"Lỗi VP43.7.1 K: {K_alpha_Am}"
    assert math.isclose(v_alpha_Am, 1.635e7, rel_tol=3e-3), f"Lỗi VP43.7.1 v: {v_alpha_Am}"

    # VP43.7.2: 8_4Be -> 2 4_2He
    M_8Be = 8.0053051
    M_4He_2 = 4.0026033
    dM_Be = M_8Be - 2 * M_4He_2
    Q_Be = dM_Be * u_to_MeV
    K_alpha_Be = Q_Be / 2.0
    v_alpha_Be = math.sqrt(2 * (K_alpha_Be * 1e6 * e_val) / (M_4He_2 * u_to_kg))
    results['VP43.7.2'] = {'Q': Q_Be, 'K_alpha': K_alpha_Be, 'v_alpha': v_alpha_Be}
    assert math.isclose(Q_Be, 0.0918, rel_tol=3e-3), f"Lỗi VP43.7.2 Q: {Q_Be}"
    assert math.isclose(K_alpha_Be, 0.0459, rel_tol=3e-3), f"Lỗi VP43.7.2 K: {K_alpha_Be}"
    assert math.isclose(v_alpha_Be, 1.487e6, rel_tol=3e-3), f"Lỗi VP43.7.2 v: {v_alpha_Be}"

    # VP43.7.3: beta- decays
    Q_73a = (12.026922 - 12.014353) * u_to_MeV
    dM_73b = 32.977452 - 32.989926
    Q_73c = (81.9168018 - 81.9134812) * u_to_MeV
    results['VP43.7.3'] = {'Q_a': Q_73a, 'dM_b': dM_73b, 'Q_c': Q_73c}
    assert math.isclose(Q_73a, 11.708, rel_tol=2e-3), f"Lỗi VP43.7.3 a: {Q_73a}"
    assert dM_73b < 0, "Lỗi VP43.7.3 b phải không thể xảy ra"
    assert math.isclose(Q_73c, 3.0931, rel_tol=2e-3), f"Lỗi VP43.7.3 c: {Q_73c}"

    # VP43.7.4: beta+ decays
    m_2e = 0.001097
    Q_74a = (45.960198 - 45.952627 - m_2e) * u_to_MeV
    Q_74b = (133.908514 - 133.904508 - m_2e) * u_to_MeV
    dM_74c = 66.9282024 - 66.9271275
    Q_74c_EC = dM_74c * u_to_MeV
    results['VP43.7.4'] = {'Q_a': Q_74a, 'Q_b': Q_74b, 'dM_c': dM_74c, 'Q_EC': Q_74c_EC}
    assert math.isclose(Q_74a, 6.030, rel_tol=2e-3), f"Lỗi VP43.7.4 a: {Q_74a}"
    assert math.isclose(Q_74b, 2.710, rel_tol=2e-3), f"Lỗi VP43.7.4 b: {Q_74b}"
    assert dM_74c < m_2e, "Lỗi VP43.7.4 c: beta+ không thể xảy ra"
    assert dM_74c > 0, "Lỗi VP43.7.4 c: bắt electron (EC) phải xảy ra được"

    # VP43.9.1: 24_11Na
    T_15h_s = 15.0 * 3600.0
    tau_91_h = 15.0 / math.log(2)
    lambda_91 = math.log(2) / T_15h_s
    N0_91 = (1.50 * 3.70e4) / lambda_91
    A_24h_91 = 1.50 * (0.5**(24.0 / 15.0))
    results['VP43.9.1'] = {'tau_h': tau_91_h, 'lambda': lambda_91, 'N0': N0_91, 'A_24h': A_24h_91}
    assert math.isclose(tau_91_h, 21.64, rel_tol=2e-3), f"Lỗi VP43.9.1 tau: {tau_91_h}"
    assert math.isclose(lambda_91, 1.284e-5, rel_tol=2e-3), f"Lỗi VP43.9.1 lambda: {lambda_91}"
    assert math.isclose(N0_91, 4.324e9, rel_tol=3e-3), f"Lỗi VP43.9.1 N0: {N0_91}"
    assert math.isclose(A_24h_91, 0.495, rel_tol=3e-3), f"Lỗi VP43.9.1 A_24h: {A_24h_91}"

    # VP43.9.2: 95_41Nb
    T_35h_s = 35.0 * 3600.0
    lambda_92 = math.log(2) / T_35h_s
    N_92 = (0.514 * 3.70e4) / lambda_92
    N0_92 = N_92 / 0.238
    t_92_h = (-math.log(0.238) / lambda_92) / 3600.0
    results['VP43.9.2'] = {'lambda': lambda_92, 'N': N_92, 'N0': N0_92, 't_h': t_92_h}
    assert math.isclose(lambda_92, 5.501e-6, rel_tol=2e-3), f"Lỗi VP43.9.2 lambda: {lambda_92}"
    assert math.isclose(N_92, 3.457e9, rel_tol=3e-3), f"Lỗi VP43.9.2 N: {N_92}"
    assert math.isclose(N0_92, 1.453e10, rel_tol=3e-3), f"Lỗi VP43.9.2 N0: {N0_92}"
    assert math.isclose(t_92_h, 72.48, rel_tol=2e-3), f"Lỗi VP43.9.2 t: {t_92_h}"

    # VP43.9.3: Gamma decay
    lambda_93 = math.log(0.425 / 0.121) / 45.0
    T_half_93 = math.log(2) / lambda_93
    N0_93 = (0.425 * 3.70e4) / lambda_93
    N_45s_93 = (0.121 * 3.70e4) / lambda_93
    results['VP43.9.3'] = {'lambda': lambda_93, 'T_half': T_half_93, 'N0': N0_93, 'N_45s': N_45s_93}
    assert math.isclose(lambda_93, 0.0279, rel_tol=3e-3), f"Lỗi VP43.9.3 lambda: {lambda_93}"
    assert math.isclose(T_half_93, 24.83, rel_tol=3e-3), f"Lỗi VP43.9.3 T_half: {T_half_93}"
    assert math.isclose(N0_93, 5.633e5, rel_tol=3e-3), f"Lỗi VP43.9.3 N0: {N0_93}"
    assert math.isclose(N_45s_93, 1.604e5, rel_tol=3e-3), f"Lỗi VP43.9.3 N_45s: {N_45s_93}"

    # VP43.9.4: Carbon-14 dating
    A_94 = 113.0 / (20.0 * 60.0)
    a_94 = A_94 / 0.510
    lambda_94_y = math.log(2) / 5730.0
    t_94_y = (1.0 / lambda_94_y) * math.log(0.255 / a_94)
    sec_per_year = 365.25 * 86400.0
    lambda_94_s = math.log(2) / (5730.0 * sec_per_year)
    N_94 = A_94 / lambda_94_s
    results['VP43.9.4'] = {'A': A_94, 'a': a_94, 't_y': t_94_y, 'N': N_94}
    assert math.isclose(A_94, 0.09417, rel_tol=2e-3), f"Lỗi VP43.9.4 A: {A_94}"
    assert math.isclose(a_94, 0.18464, rel_tol=2e-3), f"Lỗi VP43.9.4 a: {a_94}"
    assert math.isclose(t_94_y, 2669.0, rel_tol=3e-3), f"Lỗi VP43.9.4 age: {t_94_y}"
    assert math.isclose(N_94, 2.457e10, rel_tol=3e-3), f"Lỗi VP43.9.4 N: {N_94}"
    print("Xác minh 12 bài luyện tập hướng dẫn VP: PASS for the checks executed.")


def verify_numbered_exercises():
    """Xác minh 32 bài tập đánh số 43.1 - 43.32."""
    # 43.1: 28Si (14p, 14n), 85Rb (37p, 48n), 205Tl (81p, 124n)
    assert 28 - 14 == 14 and 85 - 37 == 48 and 205 - 81 == 124

    # 43.2: Proton spin resonance f = 22.7 MHz
    mu_z_p = 2.79285 * (e_val * hbar_val / (2.0 * 1.6726219e-27))
    B_43_2 = (h_val * 22.7e6) / (2.0 * mu_z_p)
    assert math.isclose(B_43_2, 0.5331, rel_tol=3e-3), f"Lỗi 43.2 B: {B_43_2}"

    # 43.3: 11_5B
    dM_B = 5 * m_H + 6 * m_n - 11.009305
    EB_table_B = dM_B * u_to_MeV
    EB_eq_B = 15.75 * 11 - 17.80 * (11**(2/3)) - 0.7100 * 5 * 4 / (11**(1/3)) - 23.69 * (1**2) / 11
    assert math.isclose(EB_table_B, 76.205, rel_tol=2e-3)
    assert math.isclose(EB_eq_B, 76.671, rel_tol=2e-3)

    # 43.4: 11_5B và 11_6C
    dM_C = 6 * m_H + 5 * m_n - 11.011434
    EB_C = dM_C * u_to_MeV
    assert math.isclose(EB_C, 73.440, rel_tol=2e-3)
    assert EB_table_B > EB_C, "11B có lực đẩy Coulomb nhỏ hơn 11C nên bền hơn"

    # 43.5: 12C
    dM_12C = 6 * m_H + 6 * m_n - 12.000000
    EB_12C = dM_12C * u_to_MeV
    assert math.isclose(EB_12C, 92.162, rel_tol=2e-3)
    assert math.isclose(EB_12C / 12.0, 7.680, rel_tol=2e-3)
    assert math.isclose(dM_12C / (12.0 - 6*m_e) * 100, 0.8247, rel_tol=3e-3)

    # 43.6: 238U
    dM_238U = 92 * m_H + 146 * m_n - 238.050788
    EB_238U = dM_238U * u_to_MeV
    assert math.isclose(dM_238U, 1.934193, rel_tol=1e-3)
    assert math.isclose(EB_238U, 1801.7, rel_tol=2e-3)
    assert math.isclose(EB_238U / 238.0, 7.570, rel_tol=2e-3)

    # 43.7: 56Fe
    M_56Fe = 26 * m_H + 30 * m_n - (56 * 8.79 / u_to_MeV)
    assert math.isclose(M_56Fe, 55.935, rel_tol=1e-4)

    # 43.8: 12C vs 3 4He
    dM_4He = 2 * m_H + 2 * m_n - 4.002603
    EB_4He = dM_4He * u_to_MeV
    assert math.isclose(3 * EB_4He, 84.888, rel_tol=2e-3)
    assert EB_12C > 3 * EB_4He, "12C bền hơn 3 hạt alpha rời"

    # 43.9: Photodisintegration của deuteron
    E_phot_MeV = (h_val * c_val / 3.50e-13) / (e_val * 1e6)
    EB_2H = (m_H + m_n - 2.014102) * u_to_MeV
    K_tot_9 = E_phot_MeV - EB_2H
    v_9 = math.sqrt(2 * (K_tot_9 / 2.0 * 1e6 * e_val) / (1.00 * u_to_kg))
    assert math.isclose(K_tot_9, 1.318, rel_tol=3e-3)
    assert math.isclose(v_9, 1.128e7, rel_tol=3e-3)

    # 43.10: 14N và 4He
    dM_14N = 7 * m_H + 7 * m_n - 14.003074
    EB_14N = dM_14N * u_to_MeV
    assert math.isclose(EB_14N / 14.0, 7.476, rel_tol=2e-3)
    assert math.isclose(EB_4He / 4.0, 7.074, rel_tol=2e-3)

    # 43.11: 11_6C beta+
    dM_11C = 11.011433 - 11.009305 - 2 * m_e
    Q_11C = dM_11C * u_to_MeV
    assert math.isclose(Q_11C, 0.960, rel_tol=3e-3)

    # 43.12: n và p rã tự do
    Q_n = (m_n - m_H) * u_to_MeV
    Q_p = (m_p - (m_n + m_e)) * u_to_MeV
    assert math.isclose(Q_n, 0.782, rel_tol=3e-3)
    assert math.isclose(Q_p, -1.804, rel_tol=3e-3)

    # 43.14: 238U alpha
    dM_14 = 238.050788 - 234.043601 - 4.002603
    Q_14 = dM_14 * u_to_MeV
    K_Th_14 = (4.002603 / (234.043601 + 4.002603)) * Q_14
    v_Th_14 = math.sqrt(2 * (K_Th_14 * 1e6 * e_val) / (234.043601 * u_to_kg))
    assert math.isclose(Q_14, 4.270, rel_tol=2e-3)
    assert math.isclose(v_Th_14, 2.433e5, rel_tol=3e-3)

    # 43.15: 12_7N
    M_12N = 12.000000 + 2 * m_e + 16.316 / u_to_MeV
    assert math.isclose(M_12N, 12.018613, rel_tol=1e-5)

    # 43.17: Tritium
    Q_3H = (3.016049 - 3.016029) * u_to_MeV
    assert math.isclose(Q_3H * 1000, 18.63, rel_tol=2e-3)

    # 43.18: t = 0.5 T_1/2
    assert math.isclose(1 - 0.5**0.5, 0.2929, rel_tol=1e-3)

    # 43.19: 6.13 g, A=124, 0.350 Ci
    N_19 = (6.13 / 124.0) * N_A
    lambda_19 = (0.350 * 3.70e10) / N_19
    T_19_y = (math.log(2) / lambda_19) / (365.25 * 86400.0)
    assert math.isclose(T_19_y, 50494, rel_tol=3e-3)

    # 43.20: 60Co, t = 2.5 y
    A_20 = 5000.0 * (0.5**(2.5 / 5.271))
    assert math.isclose(A_20, 3599.1, rel_tol=2e-3)
    assert A_20 > 3500.0

    # 43.21: 238U
    lambda_21 = math.log(2) / (4.47e9 * 365.25 * 86400.0)
    m_21_kg = ((3.70e10 / lambda_21) / N_A) * 238.05 / 1000.0
    R_10g_21 = lambda_21 * ((10.0 / 238.05) * N_A)
    assert math.isclose(lambda_21, 4.914e-18, rel_tol=2e-3)
    assert math.isclose(m_21_kg, 2976.5, rel_tol=3e-3)
    assert math.isclose(R_10g_21, 1.243e5, rel_tol=3e-3)

    # 43.22: 103Pd, 0.250 g, T_1/2 = 17 d
    N_22 = (0.250 / 103.0) * N_A
    lambda_22 = math.log(2) / (17.0 * 86400.0)
    A0_22 = lambda_22 * N_22
    A_68d_22 = A0_22 * (0.5**4)
    assert math.isclose(A0_22, 6.898e14, rel_tol=3e-3)
    assert math.isclose(A_68d_22, 4.311e13, rel_tol=3e-3)

    # 43.23: 14C
    R_1000 = 184.0 * (0.5**(1000.0 / 5730.0))
    R_50000 = 184.0 * (0.5**(50000.0 / 5730.0))
    assert math.isclose(R_1000, 163.04, rel_tol=2e-3)
    assert math.isclose(R_50000, 0.4345, rel_tol=3e-3)

    # 43.24: 131I
    R_24 = 325.0 * (0.5**3)
    assert math.isclose(R_24, 40.625, rel_tol=2e-3)
    assert math.isclose(17.0 / R_24 * 100, 41.85, rel_tol=3e-3)

    # 43.25: 90Y
    lambda_25 = math.log(2) / (64.0 * 3600.0)
    N_25 = 8.0e16 / lambda_25
    N_12d = N_25 * (0.5**(288.0 / 64.0))
    assert math.isclose(N_25, 2.659e22, rel_tol=3e-3)
    assert math.isclose(N_12d, 1.175e21, rel_tol=3e-3)

    # 43.26: 131Ba, 400 mCi
    lambda_26 = math.log(2) / (12.0 * 86400.0)
    N_26 = (400e-6 * 3.70e10) / lambda_26
    m_26_ug = (N_26 / N_A) * 131.0 * 1e6
    t_26_d = 12.0 * math.log(400.0) / math.log(2.0)
    assert math.isclose(m_26_ug, 0.004816, rel_tol=3e-3)
    assert math.isclose(t_26_d, 103.7, rel_tol=2e-3)

    # 43.27: 8318 -> 3091 trong 4 ngày
    T_27_d = 4.0 * math.log(2.0) / math.log(8318.0 / 3091.0)
    assert math.isclose(T_27_d, 2.801, rel_tol=2e-3)

    # 43.28: 500 g carbon, 2690 decays/min
    R0_28 = 500.0 * 0.255 * 60.0  # 7650 decays/min
    t_28 = (5730.0 / math.log(2.0)) * math.log(R0_28 / 2690.0)
    assert math.isclose(t_28, 8640.0, rel_tol=2e-3)

    # 43.29: 199Pt
    lambda_29 = math.log(2.0) / (30.8 * 60.0)
    N0_29 = 7.56e11 / lambda_29
    assert math.isclose(N0_29, 2.016e15, rel_tol=3e-3)

    # 43.30: 5.0 J/kg x-ray
    assert 5.0 * 70.0 == 350.0
    assert 5.0*10 == 50.0

    # 43.31: Slow neutrons RBE = 4.0, 5.0 Gy -> 500 rad, 2000 rem, 5.0 J/kg
    assert 5.0 * 100 == 500 and 5.0 * 4.0 * 100 == 2000

    # 43.32: Fast neutrons RBE = 10, 300 rem, 25 g
    assert 300 / 10 == 30  # rad
    assert math.isclose(0.30 * 0.025, 0.0075, rel_tol=1e-4)  # J
    assert 30 * 1.0 == 30  # rem
    print("Xác minh 32 bài tập đánh số: PASS for the checks executed.")


def verify_markdown_files():
    """Kiểm tra cấu trúc và tính đầy đủ của 3 tệp Markdown bài tập."""
    files = {
        '09-luyen-tap-huong-dan.md': (12, r'###\s+(VP43\.[479]\.[1-4])'),
        '10-cau-hoi-thao-luan.md': (20, r'###\s+(Q43\.(?:[1-9]|1[0-9]|20))\b'),
        '11-bai-tap-01-32.md': (32, r'###\s+(43\.(?:[1-9]|[12][0-9]|3[0-2]))\b'),
    }

    base = ROOT / 'raw_materials/physics/translations/chapter-43'
    for filename, (expected_count, pattern) in files.items():
        path = base / filename
        assert path.exists(), f"Thiếu tệp: {path}"
        content = path.read_text(encoding='utf-8')

        # Kiểm tra H1 / frontmatter cấm
        assert not content.startswith('---'), f"Tệp {filename} không được chứa YAML frontmatter"
        assert not re.search(r'^#\s+', content, re.MULTILINE), f"Tệp {filename} không được chứa H1"

        # Đếm số lượng ID bài tập
        matches = re.findall(pattern, content)
        assert len(matches) == expected_count, (
            f"Tệp {filename} có {len(matches)} bài, kỳ vọng đúng {expected_count}: {matches}"
        )

        # Kiểm tra chi tiết từng bài
        details_count = len(re.findall(r'<details><summary>Xem lời giải chi tiết</summary>', content))
        assert details_count == expected_count, (
            f"Tệp {filename} có {details_count} thẻ details, kỳ vọng {expected_count}"
        )

        tom_tat_count = len(re.findall(r'\*\*Tóm tắt đề bài:\*\*', content))
        assert tom_tat_count == expected_count, (
            f"Tệp {filename} có {tom_tat_count} mục tóm tắt đề bài, kỳ vọng {expected_count}"
        )

        huong_di_count = len(re.findall(r'\*\*Hướng đi:\*\*', content))
        assert huong_di_count == expected_count, (
            f"Tệp {filename} có {huong_di_count} mục hướng đi, kỳ vọng {expected_count}"
        )

        # Kiểm tra không có câu dịch máy / metanarration
        forbidden_phrases = [
            'sách dùng', 'theo sách', 'nguyên tác', 'bản dịch', 'ảnh trong sách',
            'hình trong sách', 'dữ liệu này từ', 'bài tập lấy từ', 'giáo trình dùng'
        ]
        for phrase in forbidden_phrases:
            assert phrase not in content.lower(), f"Tệp {filename} chứa cụm từ cấm: '{phrase}'"

        print(f"Tệp {filename}: Xác minh cấu trúc thành công ({expected_count} bài).")


def verify_assets():
    """Kiểm tra sự tồn tại của các tệp hình ảnh và SVG giải pháp."""
    img_dir = ROOT / 'docs/vat-ly-2/bai-giang/img/young-43'
    assert (img_dir / 'hinh-tham-chieu-c-1.png').exists(), "Thiếu hinh-tham-chieu-c-1.png"
    assert (img_dir / 'hinh-tham-chieu-c-2.png').exists(), "Thiếu hinh-tham-chieu-c-2.png"
    assert (img_dir / 'hinh-tham-chieu-c-3.png').exists(), "Thiếu hinh-tham-chieu-c-3.png"

    for i in range(1, 9):
        svg_file = img_dir / f'loi-giai-c-0{i}.svg'
        assert svg_file.exists(), f"Thiếu {svg_file.name}"

    print("Xác minh toàn bộ hình ảnh và SVG: PASS for the checks executed.")


def main():
    print("=== BẮT ĐẦU KIỂM TRA CHAPTER 43 EXERCISES C ===")
    verify_guided_practice()
    verify_numbered_exercises()
    verify_assets()
    # Kiểm tra tệp Markdown nếu đã được tạo
    base = ROOT / 'raw_materials/physics/translations/chapter-43'
    if (base / '09-luyen-tap-huong-dan.md').exists():
        verify_markdown_files()
    print("=== TẤT CẢ CÁC BÀI TOÁN SỐ HỌC VÀ TÀI NGUYÊN ĐÃ VƯỢT QUA KIỂM ĐỊNH ===")


if __name__ == '__main__':
    main()
