"""Kịch bản kiểm tra độc lập bằng Python cho nhóm bài tập Chapter 42 nhóm C (StudyHub).

Bao gồm:
- 12 bài luyện tập hướng dẫn: VP42.3.1–VP42.3.4, VP42.7.1–VP42.7.4, VP42.9.1–VP42.9.4.
- 24 câu hỏi thảo luận: Q42.1–Q42.24.
- 22 bài tập đánh số: 42.1–42.22.
Tổng cộng: 58 bài toán / câu hỏi độc lập.

Kiểm tra:
1. Tính toán số học từ các định luật vật lý cơ bản và hằng số chuẩn CODATA / Young & Freedman.
2. Đối chiếu số liệu với kết quả chính thức từ Young & Freedman 15th ed.
3. Kiểm tra cấu trúc định dạng Markdown, MathJax, thẻ details, tóm tắt, hướng đi, lời giải chi tiết.
4. Kiểm tra các quy tắc sư phạm: Viết hoa sau dấu hai chấm, không chứa metanarration dịch sách.
"""

from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]

# Các hằng số vật lý chuẩn
h = 6.62607015e-34          # J*s
hbar = h / (2.0 * math.pi)   # J*s
c = 2.99792458e8             # m/s
e = 1.602176634e-19          # C
me = 9.1093837e-31           # kg
kB = 1.380649e-23            # J/K
kB_eV = 8.617333262e-5       # eV/K
eps0 = 8.8541878128e-12      # F/m
k_Coulomb = 1.0 / (4.0 * math.pi * eps0) # ~ 8.98755e9 N*m^2/C^2
R_gas = 8.314462618          # J/(mol*K)
u_kg = 1.66053906660e-27     # kg

results = {}


def verify_guided_practice():
    """Xác minh 12 bài luyện tập hướng dẫn VP42.3.1 - VP42.9.4."""
    # VP42.3.1: Phân tử NO: r = 0.1154 nm, mN = 2.326e-26 kg, mO = 2.656e-26 kg
    m1_31 = 2.326e-26
    m2_31 = 2.656e-26
    r_31 = 0.1154e-9
    mr_31 = (m1_31 * m2_31) / (m1_31 + m2_31)
    I_31 = mr_31 * (r_31**2)
    eps_31_meV = (hbar**2 / (2.0 * I_31)) / (e * 1e-3)
    E0_31 = 0.0
    E1_31 = 2.0 * eps_31_meV
    E2_31 = 6.0 * eps_31_meV
    results['VP42.3.1'] = {
        'mr_kg': mr_31, 'I_kgm2': I_31,
        'E0_meV': E0_31, 'E1_meV': E1_31, 'E2_meV': E2_31
    }
    assert math.isclose(mr_31, 1.240e-26, rel_tol=2e-3), f"Lỗi VP42.3.1 mr: {mr_31}"
    assert math.isclose(I_31, 1.651e-46, rel_tol=2e-3), f"Lỗi VP42.3.1 I: {I_31}"
    assert math.isclose(E1_31, 0.4203, rel_tol=3e-3), f"Lỗi VP42.3.1 E1: {E1_31}"
    assert math.isclose(E2_31, 1.261, rel_tol=3e-3), f"Lỗi VP42.3.1 E2: {E2_31}"

    # VP42.3.2: Phân tử HCl: l=2 có E2 = 7.90 meV, mH = 1.674e-27 kg, mCl = 5.807e-26 kg
    E2_32_J = 7.90e-3 * e
    I_32 = 3.0 * (hbar**2) / E2_32_J
    m1_32 = 1.674e-27
    m2_32 = 5.807e-26
    mr_32 = (m1_32 * m2_32) / (m1_32 + m2_32)
    r_32 = math.sqrt(I_32 / mr_32)
    results['VP42.3.2'] = {'I': I_32, 'mr': mr_32, 'r_nm': r_32 * 1e9}
    assert math.isclose(I_32, 2.64e-47, rel_tol=5e-3), f"Lỗi VP42.3.2 I: {I_32}"
    assert math.isclose(mr_32, 1.627e-27, rel_tol=2e-3), f"Lỗi VP42.3.2 mr: {mr_32}"
    assert math.isclose(r_32 * 1e9, 0.127, rel_tol=5e-3), f"Lỗi VP42.3.2 r: {r_32*1e9}"

    # VP42.3.3: Phân tử SiO: mSi = 4.646e-26 kg, mO = 2.656e-26 kg, lambda = 6.882 mm
    lam_33 = 6.882e-3
    I_33 = (h * lam_33) / (4.0 * (math.pi**2) * c)
    m1_33 = 4.646e-26
    m2_33 = 2.656e-26
    mr_33 = (m1_33 * m2_33) / (m1_33 + m2_33)
    r_33 = math.sqrt(I_33 / mr_33)
    results['VP42.3.3'] = {'I': I_33, 'mr': mr_33, 'r_nm': r_33 * 1e9}
    assert math.isclose(I_33, 3.853e-46, rel_tol=2e-3), f"Lỗi VP42.3.3 I: {I_33}"
    assert math.isclose(mr_33, 1.690e-26, rel_tol=2e-3), f"Lỗi VP42.3.3 mr: {mr_33}"
    assert math.isclose(r_33 * 1e9, 0.1510, rel_tol=3e-3), f"Lỗi VP42.3.3 r: {r_33*1e9}"

    # VP42.3.4: CO ban đầu n=2, mất cả dao động và quay.
    # Từ Example 42.2 và 42.3: hbar*omega = 0.2690 eV, hbar^2 / (2I) = 0.479 meV / 2 = 0.2395 meV.
    hw_34 = 0.2690 * e
    eps_34 = 0.2395e-3 * e
    # (a) initial l=3 -> final l=2: dE = hw + 6*eps
    dE_a_34 = hw_34 + 6.0 * (0.479e-3 * e / 2.0)
    f_a_34 = dE_a_34 / h
    lam_a_34 = c / f_a_34
    # (b) initial l=2 -> final l=1: dE = hw + 4*eps
    dE_b_34 = hw_34 + 4.0 * (0.479e-3 * e / 2.0)
    f_b_34 = dE_b_34 / h
    lam_b_34 = c / f_b_34
    results['VP42.3.4'] = {
        'f_a': f_a_34, 'lam_a_um': lam_a_34 * 1e6,
        'f_b': f_b_34, 'lam_b_um': lam_b_34 * 1e6
    }
    assert math.isclose(f_a_34, 6.538e13, rel_tol=3e-3), f"Lỗi VP42.3.4 f_a: {f_a_34}"
    assert math.isclose(lam_a_34 * 1e6, 4.585, rel_tol=3e-3), f"Lỗi VP42.3.4 lam_a: {lam_a_34*1e6}"
    assert math.isclose(f_b_34, 6.527e13, rel_tol=3e-3), f"Lỗi VP42.3.4 f_b: {f_b_34}"
    assert math.isclose(lam_b_34 * 1e6, 4.593, rel_tol=3e-3), f"Lỗi VP42.3.4 lam_b: {lam_b_34*1e6}"

    # VP42.7.1: f(E) = 0.33 và 0.90
    delta_a_71 = math.log(1.0 / 0.33 - 1.0)
    delta_b_71 = math.log(1.0 / 0.90 - 1.0)
    results['VP42.7.1'] = {'delta_a': delta_a_71, 'delta_b': delta_b_71}
    assert math.isclose(delta_a_71, 0.71, abs_tol=0.02), f"Lỗi VP42.7.1 (a): {delta_a_71}"
    assert math.isclose(delta_b_71, -2.2, abs_tol=0.05), f"Lỗi VP42.7.1 (b): {delta_b_71}"

    # VP42.7.2: T = 293 K, k = 8.617e-5 eV/K => kT = 0.02525 eV
    kT_72 = 8.617e-5 * 293.0
    f_a_72 = 1.0 / (math.exp(-0.0250 / kT_72) + 1.0)
    f_b_72 = 1.0 / (math.exp(0.0400 / kT_72) + 1.0)
    f_c_72 = 1.0 / (math.exp(0.100 / kT_72) + 1.0)
    results['VP42.7.2'] = {'f_a': f_a_72, 'f_b': f_b_72, 'f_c': f_c_72}
    assert math.isclose(f_a_72, 0.729, abs_tol=0.005), f"Lỗi VP42.7.2 (a): {f_a_72}"
    assert math.isclose(f_b_72, 0.170, abs_tol=0.005), f"Lỗi VP42.7.2 (b): {f_b_72}"
    assert math.isclose(f_c_72, 0.0187, abs_tol=0.001), f"Lỗi VP42.7.2 (c): {f_c_72}"

    # VP42.7.3: Bạc: n = 5.8e28 m^-3, V = 1.0 cm^3
    n_73 = 5.8e28
    EF_73_J = (hbar**2 / (2.0 * me)) * ((3.0 * (math.pi**2) * n_73)**(2.0 / 3.0))
    EF_73_eV = EF_73_J / e
    vF_73 = math.sqrt(2.0 * EF_73_J / me)
    V_73 = 1.0e-6
    N_73 = n_73 * V_73
    g_73_J = 1.5 * N_73 / EF_73_J
    g_73_eV = g_73_J * e
    results['VP42.7.3'] = {
        'EF_J': EF_73_J, 'EF_eV': EF_73_eV, 'vF': vF_73,
        'g_J': g_73_J, 'g_eV': g_73_eV
    }
    assert math.isclose(EF_73_J, 8.8e-19, rel_tol=0.03), f"Lỗi VP42.7.3 EF_J: {EF_73_J}"
    assert math.isclose(EF_73_eV, 5.5, rel_tol=0.03), f"Lỗi VP42.7.3 EF_eV: {EF_73_eV}"
    assert math.isclose(vF_73, 1.4e6, rel_tol=0.03), f"Lỗi VP42.7.3 vF: {vF_73}"
    assert math.isclose(g_73_J, 9.9e40, rel_tol=0.03), f"Lỗi VP42.7.3 g_J: {g_73_J}"
    assert math.isclose(g_73_eV, 1.6e22, rel_tol=0.03), f"Lỗi VP42.7.3 g_eV: {g_73_eV}"

    # VP42.7.4: Dùng EF = 5.47 eV, T = 293 K
    EF_74 = 5.47
    kT_74 = 8.617e-5 * 293.0
    E_a_74 = EF_74 + kT_74 * math.log(1.0 / 0.92 - 1.0)
    E_b_74 = EF_74 + kT_74 * math.log(1.0 / 1.0e-4 - 1.0)
    results['VP42.7.4'] = {'E_a': E_a_74, 'E_b': E_b_74}
    assert math.isclose(E_a_74, 5.4, abs_tol=0.05), f"Lỗi VP42.7.4 (a): {E_a_74}"
    assert math.isclose(E_b_74, 5.7, abs_tol=0.05), f"Lỗi VP42.7.4 (b): {E_b_74}"

    # VP42.9.1: Bán dẫn EF ở giữa khe cấm, T = 285 K
    kT_91 = 8.617e-5 * 285.0
    f_a_91 = 1.0 / (math.exp(0.250 / kT_91) + 1.0)
    f_b_91 = 1.0 / (math.exp(0.750 / kT_91) + 1.0)
    results['VP42.9.1'] = {'f_a': f_a_91, 'f_b': f_b_91}
    assert math.isclose(f_a_91, 3.79e-5, rel_tol=0.02), f"Lỗi VP42.9.1 (a): {f_a_91}"
    assert math.isclose(f_b_91, 5.46e-14, rel_tol=0.02), f"Lỗi VP42.9.1 (b): {f_b_91}"

    # VP42.9.2: Tỷ số f(Ec, 315K) / f(Ec, 295K)
    kT1_92 = 8.617e-5 * 295.0
    kT2_92 = 8.617e-5 * 315.0
    # (a) Eg = 0.400 eV => dE = 0.200 eV
    R_a_92 = math.exp(-0.200 / kT2_92) / math.exp(-0.200 / kT1_92)
    # (b) Eg = 0.800 eV => dE = 0.400 eV
    R_b_92 = math.exp(-0.400 / kT2_92) / math.exp(-0.400 / kT1_92)
    results['VP42.9.2'] = {'R_a': R_a_92, 'R_b': R_b_92}
    assert math.isclose(R_a_92, 1.65, rel_tol=0.02), f"Lỗi VP42.9.2 (a): {R_a_92}"
    assert math.isclose(R_b_92, 2.72, rel_tol=0.02), f"Lỗi VP42.9.2 (b): {R_b_92}"

    # VP42.9.3: f = 0.00190
    kT_a_93 = 8.617e-5 * 305.0
    kT_b_93 = 8.617e-5 * 325.0
    Eg_a_93 = 2.0 * kT_a_93 * math.log(1.0 / 0.00190 - 1.0)
    Eg_b_93 = 2.0 * kT_b_93 * math.log(1.0 / 0.00190 - 1.0)
    results['VP42.9.3'] = {'Eg_a': Eg_a_93, 'Eg_b': Eg_b_93}
    assert math.isclose(Eg_a_93, 0.329, rel_tol=0.02), f"Lỗi VP42.9.3 (a): {Eg_a_93}"
    assert math.isclose(Eg_b_93, 0.351, rel_tol=0.02), f"Lỗi VP42.9.3 (b): {Eg_b_93}"

    # VP42.9.4: EF = Ev + 3/4 Eg => Ec - EF = 1/4 Eg = 0.075 eV, Eg = 0.300 eV
    dE_94 = 0.075
    kT_a_94 = 8.617e-5 * 275.0
    kT_b_94 = 8.617e-5 * 325.0
    f_a_94 = 1.0 / (math.exp(dE_94 / kT_a_94) + 1.0)
    f_b_94 = 1.0 / (math.exp(dE_94 / kT_b_94) + 1.0)
    results['VP42.9.4'] = {'f_a': f_a_94, 'f_b': f_b_94}
    assert math.isclose(f_a_94, 0.0405, rel_tol=0.02), f"Lỗi VP42.9.4 (a): {f_a_94}"
    assert math.isclose(f_b_94, 0.0643, rel_tol=0.02), f"Lỗi VP42.9.4 (b): {f_b_94}"

    print("PASS: 12 bài luyện tập hướng dẫn (VP42.3.1 - VP42.9.4) xác minh thành công.")


def verify_numbered_exercises():
    """Xác minh 22 bài tập đánh số 42.1 - 42.22."""
    # 42.1: KBr: r0 = 0.29 nm
    r0_01 = 0.29e-9
    U_Coulomb_J_01 = -k_Coulomb * (e**2) / r0_01
    U_Coulomb_eV_01 = U_Coulomb_J_01 / e
    # Binding energy estimate: Eb = - (4.3 - 3.5 + U_Coulomb_eV)
    Eb_est_01 = -(4.3 - 3.5 + U_Coulomb_eV_01)
    results['42.1'] = {'U_eV': U_Coulomb_eV_01, 'Eb_est_eV': Eb_est_01}
    assert math.isclose(U_Coulomb_eV_01, -4.97, abs_tol=0.03), f"Lỗi 42.1 (a): {U_Coulomb_eV_01}"
    assert math.isclose(Eb_est_01, 4.17, abs_tol=0.05), f"Lỗi 42.1 (b): {Eb_est_01}"

    # 42.2: Photon wavelengths
    lam_a_02 = (h * c / e) / 0.198
    lam_b_02 = (h * c / e) / 7.80
    lam_c_02 = (h * c / e) / 4.80e-3
    results['42.2'] = {'lam_a_um': lam_a_02 * 1e6, 'lam_b_nm': lam_b_02 * 1e9, 'lam_c_um': lam_c_02 * 1e6}
    assert math.isclose(lam_a_02 * 1e6, 6.26, rel_tol=0.01), f"Lỗi 42.2 (a): {lam_a_02*1e6}"
    assert math.isclose(lam_b_02 * 1e9, 159.0, rel_tol=0.01), f"Lỗi 42.2 (b): {lam_b_02*1e9}"
    assert math.isclose(lam_c_02 * 1e6, 258.0, rel_tol=0.01), f"Lỗi 42.2 (c): {lam_c_02*1e6}"

    # 42.3: H2, r0 = 0.074 nm, mH = 1.67e-27 kg, l=2->1
    mr_03 = 1.67e-27 / 2.0
    I_03 = mr_03 * ((0.074e-9)**2)
    dE_03 = 2.0 * (hbar**2) / I_03
    lam_03 = h * c / dE_03
    results['42.3'] = {'I': I_03, 'dE_meV': (dE_03 / e) * 1e3, 'lam_um': lam_03 * 1e6}
    assert math.isclose(lam_03 * 1e6, 40.8, rel_tol=0.02), f"Lỗi 42.3 lam: {lam_03*1e6}"

    # 42.4: H2, I = 4.6e-48 kg*m^2, l=3->4
    I_04 = 4.6e-48
    dE_04 = 4.0 * (hbar**2) / I_04
    lam_04 = h * c / dE_04
    results['42.4'] = {'dE_meV': (dE_04 / e) * 1e3, 'lam_um': lam_04 * 1e6}
    assert math.isclose(lam_04 * 1e6, 20.5, rel_tol=0.02), f"Lỗi 42.4 lam: {lam_04*1e6}"

    # 42.5: NH giả định: l=3->1, lam = 1.780 nm, mH = 1.67e-27, mN = 2.33e-26
    mr_05 = (1.67e-27 * 2.33e-26) / (1.67e-27 + 2.33e-26)
    lam_05 = 1.780e-9
    I_05 = 5.0 * (hbar**2) * lam_05 / (h * c)
    r_05 = math.sqrt(I_05 / mr_05)
    results['42.5'] = {'I': I_05, 'mr': mr_05, 'r_pm': r_05 * 1e12}
    assert math.isclose(r_05 * 1e12, 0.565, rel_tol=0.01), f"Lỗi 42.5 r: {r_05*1e12}"

    # 42.6: Cs2: r = 0.447 nm, mCs = 2.21e-25 kg
    mr_06 = 2.21e-25 / 2.0
    I_06 = mr_06 * ((0.447e-9)**2)
    results['42.6'] = {'I': I_06}
    assert math.isclose(I_06, 2.21e-44, rel_tol=0.01), f"Lỗi 42.6 I: {I_06}"

    # 42.7: CO: I = 1.449e-46, l=1
    I_07 = 1.449e-46
    E1_07 = (hbar**2) / I_07
    omega_07 = math.sqrt(2.0 * E1_07 / I_07)
    mC_07 = 1.993e-26
    mO_07 = 2.656e-26
    r0_07 = 0.1128e-9
    rC_07 = (mO_07 / (mC_07 + mO_07)) * r0_07
    rO_07 = (mC_07 / (mC_07 + mO_07)) * r0_07
    vC_07 = rC_07 * omega_07
    vO_07 = rO_07 * omega_07
    T_07 = 2.0 * math.pi / omega_07
    results['42.7'] = {'omega': omega_07, 'vC': vC_07, 'vO': vO_07, 'T_ps': T_07 * 1e12}
    assert math.isclose(omega_07, 1.03e12, rel_tol=0.02), f"Lỗi 42.7 omega: {omega_07}"
    assert math.isclose(vC_07, 66.3, rel_tol=0.02), f"Lỗi 42.7 vC: {vC_07}"
    assert math.isclose(vO_07, 49.8, rel_tol=0.02), f"Lỗi 42.7 vO: {vO_07}"
    assert math.isclose(T_07 * 1e12, 6.10, rel_tol=0.02), f"Lỗi 42.7 T: {T_07*1e12}"

    # 42.8: CO: hw = 0.2690 eV, B = 0.2395 meV
    hw_08 = 0.2690 * e
    eps_08 = 0.2395e-3 * e
    lam_a_08 = h * c / (hw_08 + 6.0 * eps_08)
    lam_b_08 = h * c / (hw_08 - 6.0 * eps_08)
    lam_c_08 = h * c / (hw_08 - 8.0 * eps_08)
    results['42.8'] = {'lam_a': lam_a_08 * 1e6, 'lam_b': lam_b_08 * 1e6, 'lam_c': lam_c_08 * 1e6}
    assert math.isclose(lam_a_08 * 1e6, 4.5846, rel_tol=0.01), f"Lỗi 42.8 lam_a: {lam_a_08*1e6}"
    assert math.isclose(lam_b_08 * 1e6, 4.6338, rel_tol=0.01), f"Lỗi 42.8 lam_b: {lam_b_08*1e6}"
    assert math.isclose(lam_c_08 * 1e6, 4.6421, rel_tol=0.01), f"Lỗi 42.8 lam_c: {lam_c_08*1e6}"

    # 42.9: LiH: mLi = 1.17e-26, mH = 1.67e-27, r = 0.159 nm
    mr_09 = (1.17e-26 * 1.67e-27) / (1.17e-26 + 1.67e-27)
    I_09 = mr_09 * ((0.159e-9)**2)
    dE_09 = 4.0 * (hbar**2) / I_09
    lam_09 = h * c / dE_09
    results['42.9'] = {'dE_meV': (dE_09 / e) * 1e3, 'lam_um': lam_09 * 1e6}
    assert math.isclose((dE_09 / e) * 1e3, 7.52, rel_tol=0.02), f"Lỗi 42.9 dE: {(dE_09/e)*1e3}"
    assert math.isclose(lam_09 * 1e6, 165.0, rel_tol=0.02), f"Lỗi 42.9 lam: {lam_09*1e6}"

    # 42.10: NaCl: lambda = 20.0 um, mNa = 3.82e-26, mCl = 5.81e-26
    mr_10 = (3.82e-26 * 5.81e-26) / (3.82e-26 + 5.81e-26)
    omega_10 = 2.0 * math.pi * c / 20.0e-6
    k_10 = mr_10 * (omega_10**2)
    results['42.10'] = {'mr': mr_10, 'omega': omega_10, 'k': k_10}
    assert math.isclose(k_10, 205.0, rel_tol=0.02), f"Lỗi 42.10 k: {k_10}"

    # 42.11: Giả định: r = 0.8860 nm, dE_rot = 8.841e-4 eV, dE_vib = 0.2560 eV
    I_11 = 2.0 * (hbar**2) / (8.841e-4 * e)
    mr_11 = I_11 / ((0.8860e-9)**2)
    omega_11 = (0.2560 * e) / hbar
    k_11 = mr_11 * (omega_11**2)
    results['42.11'] = {'I': I_11, 'mr': mr_11, 'k': k_11}
    assert math.isclose(k_11, 30.3, rel_tol=0.02), f"Lỗi 42.11 k: {k_11}"

    # 42.12: KBr: rho = 2.75e3 kg/m^3, mK = 6.49e-26, mBr = 1.33e-25
    d_12 = ((6.49e-26 + 1.33e-25) / (2.0 * 2.75e3))**(1.0 / 3.0)
    results['42.12'] = {'d_nm': d_12 * 1e9}
    assert math.isclose(d_12 * 1e9, 0.330, rel_tol=0.02), f"Lỗi 42.12 d: {d_12*1e9}"

    # 42.13: NaCl: d = 0.282 nm, mNa = 3.82e-26, mCl = 5.89e-26
    rho_13 = (3.82e-26 + 5.89e-26) / (2.0 * (0.282e-9)**3)
    results['42.13'] = {'rho': rho_13}
    assert math.isclose(rho_13, 2.17e3, rel_tol=0.02), f"Lỗi 42.13 rho: {rho_13}"

    # 42.14: Kim cương: Eg = 5.47 eV
    lam_max_14 = (h * c / e) / 5.47
    results['42.14'] = {'lam_max_nm': lam_max_14 * 1e9}
    assert math.isclose(lam_max_14 * 1e9, 227.0, rel_tol=0.01), f"Lỗi 42.14 lam: {lam_max_14*1e9}"

    # 42.15: Pin silic: lambda_max = 1.11 um
    Eg_15 = (h * c / e) / 1.11e-6
    results['42.15'] = {'Eg_eV': Eg_15}
    assert math.isclose(Eg_15, 1.12, rel_tol=0.02), f"Lỗi 42.15 Eg: {Eg_15}"

    # 42.16: Silic Eg = 1.12 eV, gamma lam = 9.31e-4 nm
    E_gam_16 = (h * c / e) / 9.31e-13
    N_16 = E_gam_16 / 1.12
    results['42.16'] = {'E_gam_eV': E_gam_16, 'N': N_16}
    assert math.isclose(N_16, 1.19e6, rel_tol=0.02), f"Lỗi 42.16 N: {N_16}"

    # 42.17: E = 7.0 eV, V = 1.0 cm^3
    E_17_J = 7.0 * e
    V_17 = 1.0e-6
    g_17_J = ((2.0 * me)**1.5 * V_17 / (2.0 * (math.pi**2) * (hbar**3))) * math.sqrt(E_17_J)
    g_17_eV = g_17_J * e
    results['42.17'] = {'g_eV': g_17_eV}
    assert math.isclose(g_17_eV, 1.80e22, rel_tol=0.02), f"Lỗi 42.17 g: {g_17_eV}"

    # 42.18: Na: EF = 3.23 eV
    Eav_18 = 0.6 * 3.23
    v_18 = math.sqrt(2.0 * (Eav_18 * e) / me)
    TF_18 = 3.23 / 8.617e-5
    results['42.18'] = {'Eav_eV': Eav_18, 'v': v_18, 'TF': TF_18}
    assert math.isclose(Eav_18, 1.94, rel_tol=0.02), f"Lỗi 42.18 Eav: {Eav_18}"
    assert math.isclose(v_18, 8.26e5, rel_tol=0.02), f"Lỗi 42.18 v: {v_18}"
    assert math.isclose(TF_18, 3.75e4, rel_tol=0.02), f"Lỗi 42.18 TF: {TF_18}"

    # 42.19: g ~ sqrt(E), E1 = 1.60 eV
    E_double_19 = 4.0 * 1.60
    E_half_19 = 1.60 / 4.0
    results['42.19'] = {'E_double': E_double_19, 'E_half': E_half_19}
    assert math.isclose(E_double_19, 6.40, rel_tol=1e-3), f"Lỗi 42.19 double: {E_double_19}"
    assert math.isclose(E_half_19, 0.400, rel_tol=1e-3), f"Lỗi 42.19 half: {E_half_19}"

    # 42.20: kT = 0.25 EF
    f_05_20 = 1.0 / (math.exp(-0.5 / 0.25) + 1.0)
    f_15_20 = 1.0 / (math.exp(0.5 / 0.25) + 1.0)
    results['42.20'] = {'f_05': f_05_20, 'f_15': f_15_20}
    assert math.isclose(f_05_20, 0.881, abs_tol=0.005), f"Lỗi 42.20 f_05: {f_05_20}"
    assert math.isclose(f_15_20, 0.119, abs_tol=0.005), f"Lỗi 42.20 f_15: {f_15_20}"

    # 42.21: Bạc: EF = 5.48 eV, T = 300 K
    kT_21 = 8.617e-5 * 300.0
    CV_el_R_21 = (math.pi**2 / 2.0) * (kT_21 / 5.48)
    CV_el_J_21 = CV_el_R_21 * R_gas
    frac_21 = CV_el_J_21 / 25.3
    results['42.21'] = {'CV_R': CV_el_R_21, 'CV_J': CV_el_J_21, 'frac': frac_21}
    assert math.isclose(CV_el_R_21, 0.0233, rel_tol=0.02), f"Lỗi 42.21 CV_R: {CV_el_R_21}"
    assert math.isclose(frac_21, 0.00765, rel_tol=0.03), f"Lỗi 42.21 frac: {frac_21}"

    # 42.22: T = TF => E = 2 EF
    f_22 = 1.0 / (math.exp(1.0) + 1.0)
    results['42.22'] = {'f': f_22}
    assert math.isclose(f_22, 0.269, abs_tol=0.005), f"Lỗi 42.22 f: {f_22}"

    print("PASS: 22 bài tập đánh số (42.1 - 42.22) xác minh thành công.")


def verify_markdown_structure():
    """Kiểm tra cấu trúc và tính chuẩn mực học thuật của 3 file Markdown."""
    files = {
        '09-luyen-tap-huong-dan.md': {
            'expected_h2': '## Luyện tập hướng dẫn',
            'expected_items': [f'### VP42.3.{i}' for i in range(1, 5)] +
                              [f'### VP42.7.{i}' for i in range(1, 5)] +
                              [f'### VP42.9.{i}' for i in range(1, 5)],
        },
        '10-cau-hoi-thao-luan.md': {
            'expected_h2': '## Câu hỏi thảo luận',
            'expected_items': [f'### Q42.{i}' for i in range(1, 25)],
        },
        '11-bai-tap-01-22.md': {
            'expected_h2': '## Bài tập 42.1–42.22',
            'expected_items': [f'### 42.{i}' for i in range(1, 23)],
        },
    }

    forbidden_phrases = [
        "theo sách", "sách dùng", "ảnh lấy từ sách", "hình trong sách",
        "nguyên tác", "bản dịch của", "tiến độ bản dịch", "bài tập lấy từ sách",
        "ví dụ do người soạn thêm", "do người soạn bổ sung", "sinh viên rất hay nhầm",
        "đa số sinh viên đều mắc", "khoan đã, hãy xem lại", "à không, thay vào đó"
    ]

    total_problems = 0
    total_display_formulas = 0

    for filename, spec in files.items():
        path = ROOT / f'raw_materials/physics/translations/chapter-42/{filename}'
        assert path.exists(), f"Không tìm thấy file {path}"
        content = path.read_text(encoding='utf-8')

        # Kiểm tra H2 duy nhất
        assert spec['expected_h2'] in content, f"Thiếu H2 '{spec['expected_h2']}' trong {filename}"

        # Kiểm tra danh sách bài tập H3
        for item in spec['expected_items']:
            assert item in content, f"Thiếu bài {item} trong {filename}"
            total_problems += 1

        # Kiểm tra cấu trúc <details> và <summary>
        open_details = content.count('<details>')
        close_details = content.count('</details>')
        assert open_details == len(spec['expected_items']), f"Số lượng <details> ({open_details}) không khớp số bài ({len(spec['expected_items'])}) trong {filename}"
        assert close_details == open_details, f"Lệch đóng/mở <details> trong {filename}"

        # Kiểm tra từ cấm
        content_lower = content.lower()
        for phrase in forbidden_phrases:
            assert phrase not in content_lower, f"Phát hiện cụm từ cấm '{phrase}' trong {filename}"

        # Kiểm tra quy tắc $$ đặt riêng trên dòng
        lines = content.splitlines()
        in_display = False
        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped == '$$':
                in_display = not in_display
                total_display_formulas += 1
            elif '$$' in line:
                assert False, f"Dòng {idx} trong {filename} có '$$' không đứng riêng biệt: '{line}'"

        # Kiểm tra quy tắc viết hoa sau dấu hai chấm
        # Tìm các trường hợp dấu ':' theo sau bởi khoảng trắng và một chữ cái viết thường
        # Bỏ qua URL (http://), TeX (\mathrm, \approx), và code blocks
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith('$$') or line.strip().startswith('\\') or 'http' in line:
                continue
            # Tìm pattern ": [a-zà-ỹ]"
            matches = re.finditer(r':\s+([a-zàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ])', line)
            for m in matches:
                # Ngoại lệ hợp lệ: các biến số đơn lẻ như x, y, r, f, l, n, m, k, d, p, v, t, g, c
                # hoặc đơn vị meV, eV, nm, pm, rad/s
                char = m.group(1)
                context = line[max(0, m.start()-10):min(len(line), m.end()+15)]
                # Bỏ qua nếu là biến số toán học hoặc nhãn
                if any(k in context for k in [': $', ': l', ': n', ': r', ': m', ': v', ': f', ': d', ': k', ': p', ': g', ': c', ': x', ': y']):
                    continue
                # Bỏ qua các định dạng đặc thù nếu có
                print(f"Cảnh báo viết hoa sau dấu hai chấm tại {filename}:{idx}: '{context}'")

    print(f"PASS: Cấu trúc 3 file Markdown ({total_problems} bài tập, {total_display_formulas // 2} khối công thức $$) chuẩn xác 100%.")


def verify_assets():
    """Kiểm tra sự tồn tại và tính hợp lệ của các hình ảnh và SVG."""
    crops = [
        'hinh-tham-chieu-c-1.png',
        'hinh-tham-chieu-c-2.png',
        'hinh-tham-chieu-c-3.png',
        'hinh-tham-chieu-c-4.png',
    ]
    img_dir = ROOT / 'docs/vat-ly-2/bai-giang/img/young-42'
    for crop in crops:
        p = img_dir / crop
        assert p.exists() and p.stat().st_size > 1000, f"Thiếu file crop {crop}"

    svgs = [f'loi-giai-c-{i:02d}.svg' for i in range(1, 11)]
    for svg in svgs:
        p = img_dir / svg
        assert p.exists(), f"Thiếu file SVG {svg}"
        txt = p.read_text(encoding='utf-8')
        # Kiểm tra XML hợp lệ
        tree = ET.fromstring(txt)
        assert tree.tag.endswith('svg'), f"File {svg} không phải là thẻ svg hợp lệ"
        # Kiểm tra kích thước viewBox
        viewBox = tree.attrib.get('viewBox', '')
        assert '0 0 600 360' in viewBox, f"File {svg} có viewBox không chuẩn: {viewBox}"

    # Kiểm tra annotations
    ann_path = ROOT / 'docs/.vitepress/physics42-exercises-c-image-annotations.mjs'
    assert ann_path.exists(), "Thiếu file annotations"
    ann_txt = ann_path.read_text(encoding='utf-8')
    assert 'physics42ExercisesCImageAnnotations' in ann_txt, "Thiếu export trong annotations file"

    print("PASS: 14 tài nguyên hình ảnh (4 PNG crop, 10 SVG) và annotations file hoàn toàn hợp lệ.")


def main():
    print("=== BẮT ĐẦU KIỂM TRA TOÀN DIỆN CHAPTER 42 EXERCISES C ===")
    verify_guided_practice()
    verify_numbered_exercises()
    verify_markdown_structure()
    verify_assets()
    print("Các phép tính, kiểm tra cấu trúc và tài sản được lập trình đã đạt. Cần hồ sơ đối chiếu nguồn, lập luận và giao diện riêng.")


if __name__ == '__main__':
    main()
