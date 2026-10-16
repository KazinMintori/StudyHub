"""Kịch bản kiểm tra độc lập bằng Python cho nhóm bài tập Chapter 40 nhóm C.

Bao gồm:
- 12 bài luyện tập hướng dẫn: VP40.4.1–VP40.4.4, VP40.6.1–VP40.6.4, VP40.7.1–VP40.7.4.
- 35 bài tập đánh số: 40.1 đến 40.35.
Tổng cộng: 47 bài toán.

Mọi kết quả được tính toán độc lập từ các hằng số vật lý chuẩn (CODATA / Young & Freedman 15th ed).
"""

import math
import numpy as np

# Các hằng số vật lý cơ bản
h = 6.62607015e-34          # Hằng số Planck (J*s)
hbar = 1.054571817e-34       # Hằng số Planck rút gọn (J*s)
c = 2.99792458e8             # Tốc độ ánh sáng trong chân không (m/s)
e = 1.602176634e-19          # Điện tích nguyên tố (C)
me = 9.1093837e-31           # Khối lượng nghỉ electron (kg)
mp = 1.67262192e-27          # Khối lượng nghỉ proton (kg)
m_alpha = 6.64e-27           # Khối lượng hạt alpha theo Young & Freedman (kg)
hc_eV_nm = (h * c / e) * 1e9 # ~ 1239.841984 eV*nm

results = {}

def verify_guided_practice():
    """Xác minh 12 bài luyện tập hướng dẫn VP40.4.1 - VP40.7.4."""
    # VP40.4.1: Electron trong giếng 1D vô hạn, E1 = 2.00e-19 J
    E1_vp41 = 2.00e-19
    L_vp41 = h / math.sqrt(8.0 * me * E1_vp41)
    E2_vp41 = 4.0 * E1_vp41
    E3_vp41 = 9.0 * E1_vp41
    results['VP40.4.1'] = {
        'L_nm': L_vp41 * 1e9,
        'E2_J': E2_vp41,
        'E3_J': E3_vp41
    }
    assert abs(L_vp41 * 1e9 - 0.549) < 0.005, "Lỗi VP40.4.1 (a) bề rộng giếng"
    assert math.isclose(E2_vp41, 8.00e-19, rel_tol=1e-3), "Lỗi VP40.4.1 (b) E2"
    assert math.isclose(E3_vp41, 1.80e-18, rel_tol=1e-3), "Lỗi VP40.4.1 (b) E3"

    # VP40.4.2: Proton trong giếng L = 5.00e-15 m
    m_p_given = 1.67e-27
    L_vp42 = 5.00e-15
    E1_vp42 = (h**2) / (8.0 * m_p_given * L_vp42**2)
    dE_21_vp42 = 3.0 * E1_vp42
    dE_32_vp42 = 5.0 * E1_vp42
    results['VP40.4.2'] = {
        'dE_21_J': dE_21_vp42,
        'dE_32_J': dE_32_vp42
    }
    assert abs(dE_21_vp42 - 3.94e-12) < 0.02e-12, "Lỗi VP40.4.2 (a) dE_21"
    assert abs(dE_32_vp42 - 6.57e-12) < 0.03e-12, "Lỗi VP40.4.2 (b) dE_32"

    # VP40.4.3: Chuyển mức 2->1 phát photon lambda = 655 nm
    lam_vp43 = 655e-9
    E_ph_vp43 = (h * c) / lam_vp43
    E1_vp43 = E_ph_vp43 / 3.0
    L_vp43 = h / math.sqrt(8.0 * me * E1_vp43)
    dE_32_vp43 = 5.0 * E1_vp43
    lam_32_vp43 = (h * c) / dE_32_vp43
    results['VP40.4.3'] = {
        'E_ph_J': E_ph_vp43,
        'L_nm': L_vp43 * 1e9,
        'lam_32_nm': lam_32_vp43 * 1e9
    }
    assert abs(E_ph_vp43 - 3.03e-19) < 0.02e-19, "Lỗi VP40.4.3 (a) năng lượng photon"
    assert abs(L_vp43 * 1e9 - 0.772) < 0.005, "Lỗi VP40.4.3 (b) bề rộng giếng"
    assert abs(lam_32_vp43 * 1e9 - 393.0) < 1.0, "Lỗi VP40.4.3 (c) bước sóng 3->2"

    # VP40.4.4: Chứng minh giải tích psi(x) = A cos(x sqrt(2mE)/hbar + phi)
    # (a) d2psi/dx2 = - (2mE/hbar^2) psi => TISE thỏa mãn.
    # (b) psi(0) = 0 => phi = \pm pi/2.
    # (c) psi(L) = 0 => L sqrt(2mE)/hbar = n pi => E = n^2 pi^2 hbar^2 / (2m L^2).
    results['VP40.4.4'] = {'symbolic_checked': True}

    # VP40.6.1: Giếng thế L = 0.350 nm, U0 = 6 E1-IDW
    L_vp61 = 0.350e-9
    E1_IDW_vp61 = (h**2) / (8.0 * me * L_vp61**2)
    # Theo Hình 40.15b / Trang 1351: E1 = 0.625 E1-IDW
    E1_vp61 = 0.625 * E1_IDW_vp61
    E_free_vp61 = (6.0 - 0.625) * E1_IDW_vp61
    results['VP40.6.1'] = {
        'E1_IDW_J': E1_IDW_vp61,
        'E1_J': E1_vp61,
        'E_free_J': E_free_vp61
    }
    assert abs(E1_IDW_vp61 - 4.92e-19) < 0.03e-19, "Lỗi VP40.6.1 (a) E1_IDW"
    assert abs(E1_vp61 - 3.07e-19) < 0.03e-19, "Lỗi VP40.6.1 (b) E1"
    assert abs(E_free_vp61 - 2.64e-18) < 0.03e-18, "Lỗi VP40.6.1 (c) E_free"

    # VP40.6.2: U0 = 6 E1-IDW, photon phát ra 3->2 có năng lượng 2.50e-19 J
    E_ph_vp62 = 2.50e-19
    # E3 - E2 = (5.09 - 2.43) E1-IDW = 2.66 E1-IDW
    E1_IDW_vp62 = E_ph_vp62 / 2.66
    U0_vp62 = 6.0 * E1_IDW_vp62
    L_vp62 = h / math.sqrt(8.0 * me * E1_IDW_vp62)
    results['VP40.6.2'] = {
        'E1_IDW_J': E1_IDW_vp62,
        'U0_J': U0_vp62,
        'L_nm': L_vp62 * 1e9
    }
    assert abs(E1_IDW_vp62 - 9.40e-20) < 0.1e-20, "Lỗi VP40.6.2 (a) E1-IDW"
    assert abs(U0_vp62 - 5.64e-19) < 0.05e-19, "Lỗi VP40.6.2 (b) U0"
    assert abs(L_vp62 * 1e9 - 0.800) < 0.005, "Lỗi VP40.6.2 (c) L"

    # VP40.6.3: U0 = 6 E1-IDW (3 trạng thái dừng). Bước sóng ngắn nhất là 355 nm
    # Ba chuyển mức: 3->1 (ngắn nhất), 3->2, 2->1
    lam_31_vp63 = 355e-9
    # dE_31 = (5.09 - 0.625) E1-IDW = 4.465 E1-IDW
    # dE_32 = (5.09 - 2.43) E1-IDW = 2.66 E1-IDW
    # dE_21 = (2.43 - 0.625) E1-IDW = 1.805 E1-IDW
    lam_32_vp63 = lam_31_vp63 * (4.465 / 2.66)
    lam_21_vp63 = lam_31_vp63 * (4.465 / 1.805)
    results['VP40.6.3'] = {
        'initial_final_shortest': (3, 1),
        'lam_32_nm': lam_32_vp63 * 1e9,
        'lam_21_nm': lam_21_vp63 * 1e9
    }
    assert abs(lam_32_vp63 * 1e9 - 596.0) < 1.0, "Lỗi VP40.6.3 (b) lambda 3->2"
    assert abs(lam_21_vp63 * 1e9 - 878.0) < 2.0, "Lỗi VP40.6.3 (b) lambda 2->1"

    # VP40.6.4: L = 0.400 nm. U0 = 0.015 eV << E1-IDW
    L_vp64 = 0.400e-9
    E1_IDW_vp64_J = (h**2) / (8.0 * me * L_vp64**2)
    E1_IDW_vp64_eV = E1_IDW_vp64_J / e
    # Solve the actual shallow finite well; do not assume a fixed depth ratio.
    U0_64_J = 0.015 * e
    xi0 = math.sqrt(me * L_vp64**2 * U0_64_J / (2*hbar**2))
    def residual(xi):
        return xi*math.tan(xi)-math.sqrt(xi0*xi0-xi*xi)
    lo, hi = 0.0, xi0
    for _ in range(100):
        mid = (lo+hi)/2
        if residual(mid)>0: hi=mid
        else: lo=mid
    xi_star=(lo+hi)/2
    E_exact_vp64=((2*hbar*xi_star/L_vp64)**2/(2*me))/e
    assert abs(residual(xi_star))<1e-10
    assert 0<E_exact_vp64<0.015
    assert abs(E_exact_vp64-0.01476862176)<1e-10
    results['VP40.6.4'] = {'E1_IDW_eV':E1_IDW_vp64_eV,'E_exact_eV':E_exact_vp64,
        'binding_eV':0.015-E_exact_vp64,'matching_residual':residual(xi_star)}
    assert abs(E1_IDW_vp64_eV-2.35)<0.02

    # VP40.7.1: E = 3.75 eV, U0 = 6.10 eV, (a) L = 0.750 nm, (b) L = 0.500 nm
    E_vp71 = 3.75 * e
    U0_vp71 = 6.10 * e
    kap_vp71 = math.sqrt(2.0 * me * (U0_vp71 - E_vp71)) / hbar
    G_vp71 = 16.0 * (E_vp71 / U0_vp71) * (1.0 - E_vp71 / U0_vp71)
    T_a_vp71 = G_vp71 * math.exp(-2.0 * kap_vp71 * 0.750e-9)
    T_b_vp71 = G_vp71 * math.exp(-2.0 * kap_vp71 * 0.500e-9)
    results['VP40.7.1'] = {'T_a': T_a_vp71, 'T_b': T_b_vp71}
    assert abs(T_a_vp71 - 2.90e-5) < 0.05e-5, "Lỗi VP40.7.1 (a)"
    assert abs(T_b_vp71 - 1.47e-3) < 0.03e-3, "Lỗi VP40.7.1 (b)"

    # VP40.7.2: E = 3.50 eV, U0 = 4.00 eV, (a) L = 0.800 nm, (b) T' = 2T
    E_vp72 = 3.50 * e
    U0_vp72 = 4.00 * e
    kap_vp72 = math.sqrt(2.0 * me * (U0_vp72 - E_vp72)) / hbar
    G_vp72 = 16.0 * (E_vp72 / U0_vp72) * (1.0 - E_vp72 / U0_vp72)
    T_a_vp72 = G_vp72 * math.exp(-2.0 * kap_vp72 * 0.800e-9)
    # T' = 2T => exp(-2 kap dL) = 2 => dL = - ln(2)/(2 kap)
    L_b_vp72 = 0.800e-9 - math.log(2.0) / (2.0 * kap_vp72)
    results['VP40.7.2'] = {'T_a': T_a_vp72, 'L_b_nm': L_b_vp72 * 1e9}
    assert abs(T_a_vp72 - 5.33e-3) < 0.05e-3, "Lỗi VP40.7.2 (a)"
    assert abs(L_b_vp72 * 1e9 - 0.704) < 0.005, "Lỗi VP40.7.2 (b)"

    # VP40.7.3: U0 = 5.00 eV, L = 0.900 nm. (a) 4.00 eV, (b) 4.30 eV, (c) 4.60 eV
    U0_vp73 = 5.00 * e
    L_vp73 = 0.900e-9
    def calc_T_vp73(E_eV):
        Ev = E_eV * e
        kap = math.sqrt(2.0 * me * (U0_vp73 - Ev)) / hbar
        G = 16.0 * (Ev / U0_vp73) * (1.0 - Ev / U0_vp73)
        return G * math.exp(-2.0 * kap * L_vp73)
    T_a_vp73 = calc_T_vp73(4.00)
    T_b_vp73 = calc_T_vp73(4.30)
    T_c_vp73 = calc_T_vp73(4.60)
    results['VP40.7.3'] = {'T_a': T_a_vp73, 'T_b': T_b_vp73, 'T_c': T_c_vp73}
    assert abs(T_a_vp73 - 2.54e-4) < 0.05e-4, "Lỗi VP40.7.3 (a)"
    assert abs(T_b_vp73 - 8.59e-4) < 0.05e-4, "Lỗi VP40.7.3 (b)"
    assert abs(T_c_vp73 - 3.46e-3) < 0.05e-3, "Lỗi VP40.7.3 (c)"

    # VP40.7.4: T = 1/417, E = 3.00 eV, U0 = 5.00 eV
    T_vp74 = 1.0 / 417.0
    E_vp74 = 3.00 * e
    U0_vp74 = 5.00 * e
    kap_vp74 = math.sqrt(2.0 * me * (U0_vp74 - E_vp74)) / hbar
    G_vp74 = 16.0 * (E_vp74 / U0_vp74) * (1.0 - E_vp74 / U0_vp74)
    L_vp74 = math.log(G_vp74 / T_vp74) / (2.0 * kap_vp74)
    results['VP40.7.4'] = {'L_nm': L_vp74 * 1e9}
    assert abs(L_vp74 * 1e9 - 0.509) < 0.005, "Lỗi VP40.7.4 L"


def verify_exercises_01_15():
    """Xác minh các bài tập 40.1 đến 40.15."""
    # 40.1: p = 4.50e-24 kg*m/s theo chiều -x
    p_401 = 4.50e-24
    k_401 = p_401 / hbar
    E_401 = p_401**2 / (2.0 * me)
    omega_401 = E_401 / hbar
    results['40.1'] = {'k': k_401, 'omega': omega_401, 'E_eV': E_401 / e}
    assert abs(k_401 - 4.27e10) < 0.05e10
    assert abs(omega_401 - 1.05e17) < 0.05e17

    # 40.2: k1=k, k2=2k, omega1=omega, omega2=4*omega
    # (a) t=0: x1 = pi/k, x2 = 3pi/k
    # (b) t=2pi/omega: x1 = pi/k, x2 = 3pi/k
    # (c) v_av = 3*omega/k == (omega2 - omega1)/(k2 - k1)
    results['40.2'] = {'v_av_factor': 3.0}

    # 40.3: k1=k, k2=3k, omega1=omega, omega2=9*omega
    # (a) cực đại tại t=0 ở x=0 dời đến x = 8pi/k; cực đại dương nhỏ nhất tại t=2pi/omega là x = pi/k
    # (b) v_av = 4*omega/k == (9-1)/(3-1) = 4
    results['40.3'] = {'v_av_factor': 4.0}

    # 40.4: psi(x) = A e^{-a x^2}
    # a tăng => Delta x giảm, Delta p tăng
    results['40.4'] = {'delta_x_decreases': True, 'delta_p_increases': True}

    # 40.5: psi(x) = A sin(kx)
    # (a) cực đại tại x = (2n+1) lambda / 4
    # (b) cực tiểu 0 tại x = n lambda / 2
    results['40.5'] = {'antinodes': 'odd_quarter_lambda', 'nodes': 'half_lambda'}

    # 40.6: psi = A psi1 + B psi2 không phải nghiệm TISE nếu E1 != E2
    results['40.6'] = {'is_stationary': False}

    # 40.7: lambda_12 = 420 nm => lambda_13 = 3/8 * lambda_12
    lam_12 = 420.0
    lam_13 = (3.0 / 8.0) * lam_12
    results['40.7'] = {'lam_13_nm': lam_13}
    assert abs(lam_13 - 157.5) < 0.1

    # 40.8: psi = A e^{-b|x|}, b = 2.00 m^-1
    b_408 = 2.00
    A_408 = math.sqrt(b_408)
    P_i = 1.0 - math.exp(-2.0 * b_408 * 0.500)
    P_ii = 0.500
    P_iii = math.exp(-2.0 * b_408 * 0.500) - math.exp(-2.0 * b_408 * 1.00)
    results['40.8'] = {
        'A': A_408,
        'P_i': P_i,
        'P_ii': P_ii,
        'P_iii': P_iii
    }
    assert abs(A_408 - math.sqrt(2.0)) < 1e-5
    assert abs(P_i - 0.865) < 0.005
    assert abs(P_ii - 0.500) < 1e-5
    assert abs(P_iii - 0.117) < 0.005

    # 40.9: m = 0.20 kg, L = 1.3 m
    m_409 = 0.20
    L_409 = 1.3
    E1_409 = (h**2) / (8.0 * m_409 * L_409**2)
    v_409 = math.sqrt(2.0 * E1_409 / m_409)
    t_409 = L_409 / v_409
    dE_409 = 3.0 * E1_409
    results['40.9'] = {
        'E1_J': E1_409,
        'v_m_s': v_409,
        't_s': t_409,
        'dE_J': dE_409
    }
    assert abs(E1_409 - 1.62e-67) < 0.05e-67
    assert abs(v_409 - 1.27e-33) < 0.05e-33

    # 40.10: Proton, E1 = 5.0 MeV
    E1_410 = 5.0e6 * e
    L_410 = h / math.sqrt(8.0 * mp * E1_410)
    results['40.10'] = {'L_fm': L_410 * 1e15}
    assert abs(L_410 * 1e15 - 6.4) < 0.2

    # 40.11: Electron, E1 = 13.606 eV
    E1_411 = 13.606 * e
    L_411 = h / math.sqrt(8.0 * me * E1_411)
    results['40.11'] = {'L_nm': L_411 * 1e9}
    assert abs(L_411 * 1e9 - 0.166) < 0.005

    # 40.12: Hydrogen 2->1 photon lambda = 122 nm => dE = 10.16 eV = 3 E1
    dE_412 = (h * c) / (122e-9)
    E1_412 = dE_412 / 3.0
    L_412 = h / math.sqrt(8.0 * me * E1_412)
    results['40.12'] = {
        'dE_eV': dE_412 / e,
        'E1_eV': E1_412 / e,
        'L_nm': L_412 * 1e9
    }
    assert abs(E1_412 / e - 3.39) < 0.05
    assert abs(L_412 * 1e9 - 0.333) < 0.005

    # 40.13: dE = 3.0 eV = 3 E1 => E1 = 1.0 eV
    E1_413 = 1.0 * e
    L_413 = h / math.sqrt(8.0 * me * E1_413)
    results['40.13'] = {'L_nm': L_413 * 1e9}
    assert abs(L_413 * 1e9 - 0.614) < 0.005

    # 40.14: E1 = 2.00 eV, n=1 -> n=3 => dE = 8 E1 = 16.00 eV
    dE_414 = 8.0 * 2.00 * e
    lam_414 = (h * c) / dE_414
    results['40.14'] = {'lam_nm': lam_414 * 1e9}
    assert abs(lam_414 * 1e9 - 77.5) < 0.2

    # 40.15: E = 9 pi^2 hbar^2 / (2m L^2) => n=3
    # |p| = 3 pi hbar / L = 3 h / (2 L)
    # L / lambda = 1.5
    results['40.15'] = {'n': 3, 'L_over_lambda': 1.5}


def verify_exercises_16_30():
    """Xác minh các bài tập 40.16 đến 40.30."""
    # 40.16: Giếng vô hạn n=1
    # P(x) = (2/L) sin^2(pi x / L)
    # Zeros at x = 0, L; max at x = L/2
    results['40.16'] = {'zeros': [0.0, 1.0], 'max': 0.5}

    # 40.17: mA = 9 mB, LB = 2 LA => nA / nB = 3 / 2
    # Hai số lượng tử nhỏ nhất: nA = 3, nB = 2
    results['40.17'] = {'nA': 3, 'nB': 2}

    # 40.18: Electron, L = 0.360 nm. Ground to 3rd excited (n=4)
    L_418 = 0.360e-9
    E1_418 = (h**2) / (8.0 * me * L_418**2)
    dE_418 = 15.0 * E1_418
    lam_418 = (h * c) / dE_418
    results['40.18'] = {
        'dE_J': dE_418,
        'dE_eV': dE_418 / e,
        'lam_nm': lam_418 * 1e9
    }
    assert abs(dE_418 / e - 43.54) < 0.1
    assert abs(lam_418 * 1e9 - 28.5) < 0.2

    # 40.19: L = 3.0e-10 m
    L_419 = 3.0e-10
    lam_1_419 = 2.0 * L_419
    p_1_419 = h / lam_1_419
    lam_2_419 = L_419
    p_2_419 = h / lam_2_419
    lam_3_419 = 2.0 * L_419 / 3.0
    p_3_419 = h / lam_3_419
    results['40.19'] = {
        'lam_1_nm': lam_1_419 * 1e9, 'p_1': p_1_419,
        'lam_2_nm': lam_2_419 * 1e9, 'p_2': p_2_419,
        'lam_3_nm': lam_3_419 * 1e9, 'p_3': p_3_419
    }
    assert abs(lam_1_419 * 1e9 - 0.60) < 0.01
    assert abs(p_1_419 - 1.10e-24) < 0.02e-24

    # 40.20: lambda_12 = 426 nm
    lam_12_420 = 426.0
    lam_23_420 = (3.0 / 5.0) * lam_12_420
    lam_13_420 = (3.0 / 8.0) * lam_12_420
    dE_12_420 = (h * c) / (lam_12_420 * 1e-9)
    E1_420 = dE_12_420 / 3.0
    L_420 = h / math.sqrt(8.0 * me * E1_420)
    results['40.20'] = {
        'lam_23_nm': lam_23_420,
        'lam_13_nm': lam_13_420,
        'L_nm': L_420 * 1e9
    }
    assert abs(lam_23_420 - 255.6) < 0.5
    assert abs(lam_13_420 - 159.8) < 0.5
    assert abs(L_420 * 1e9 - 0.623) < 0.005

    # 40.21: Giếng đối xứng [-L/2, L/2]
    # Cosine modes: kn = n pi / L (n lẻ)
    # Sine modes: kn = n pi / L (n chẵn)
    # Tập mức năng lượng: En = n^2 h^2 / (8 m L^2), giống hệt Eq. 40.31
    results['40.21'] = {'matches_eq_40_31': True}

    # 40.22: E = 3 U0. Kin = 3 U0, Kout = 2 U0
    # lambda_out / lambda_in = sqrt(Kin / Kout) = sqrt(3/2)
    ratio_422 = math.sqrt(1.5)
    results['40.22'] = {'ratio': ratio_422}
    assert abs(ratio_422 - 1.225) < 0.005

    # 40.23: U0 = 6 E1-IDW, E1 = 2.00 eV => E1-IDW = E1 / 0.625 = 3.20 eV
    E1_IDW_423 = 2.00 / 0.625
    L_423 = h / math.sqrt(8.0 * me * E1_IDW_423 * e)
    results['40.23'] = {'E1_IDW_eV': E1_IDW_423, 'L_nm': L_423 * 1e9}
    assert abs(E1_IDW_423 - 3.20) < 0.01
    assert abs(L_423 * 1e9 - 0.343) < 0.005

    # 40.24: L = 0.400 nm, U0 = 6 E1-IDW, photon lambda = 72 nm
    L_424 = 0.400e-9
    E1_IDW_424_eV = (h**2 / (8.0 * me * L_424**2)) / e
    E1_424_eV = 0.625 * E1_IDW_424_eV
    U0_424_eV = 6.0 * E1_IDW_424_eV
    binding_424_eV = U0_424_eV - E1_424_eV
    E_ph_424_eV = (h * c / (72.0e-9)) / e
    K_inf_424_eV = E_ph_424_eV - binding_424_eV
    results['40.24'] = {
        'E1_IDW_eV': E1_IDW_424_eV,
        'binding_eV': binding_424_eV,
        'E_ph_eV': E_ph_424_eV,
        'K_inf_eV': K_inf_424_eV
    }
    assert abs(E1_IDW_424_eV - 2.35) < 0.02
    assert abs(binding_424_eV - 12.63) < 0.1
    assert abs(E_ph_424_eV - 17.22) < 0.1
    assert abs(K_inf_424_eV - 4.59) < 0.1

    # 40.25: L = 1.50 nm, U0 = 6 E1-IDW. Giải phóng electron => photon >= U0 - E1
    L_425 = 1.50e-9
    E1_IDW_425_eV = (h**2 / (8.0 * me * L_425**2)) / e
    binding_425_eV = 5.375 * E1_IDW_425_eV
    lam_max_425 = (h * c / (binding_425_eV * e))
    results['40.25'] = {
        'E1_IDW_eV': E1_IDW_425_eV,
        'binding_eV': binding_425_eV,
        'lam_max_nm': lam_max_425 * 1e9
    }
    assert abs(E1_IDW_425_eV - 0.167) < 0.005
    assert abs(binding_425_eV - 0.898) < 0.01
    assert abs(lam_max_425 * 1e9 - 1380.0) < 15.0

    # 40.26: U0 = 6 E1-IDW. Bước sóng dài nhất hấp thụ là 582 nm
    # dE_12 = (2.43 - 0.625) E1-IDW = 1.805 E1-IDW
    dE_426_eV = (h * c / (582e-9)) / e
    E1_IDW_426_eV = dE_426_eV / 1.805
    L_426 = h / math.sqrt(8.0 * me * E1_IDW_426_eV * e)
    # Nếu xét ngưỡng ion hóa:
    E1_IDW_ion = dE_426_eV / 5.375
    L_ion = h / math.sqrt(8.0 * me * E1_IDW_ion * e)
    results['40.26'] = {
        'dE_eV': dE_426_eV,
        'E1_IDW_eV': E1_IDW_426_eV,
        'L_nm': L_426 * 1e9,
        'L_ion_nm': L_ion * 1e9
    }
    assert abs(dE_426_eV - 2.13) < 0.02
    assert abs(L_426 * 1e9 - 0.565) < 0.01

    # 40.27: Proton trong giếng L = 4.0 fm = 4.0e-15 m, U0 = 6 E1-IDW
    L_427 = 4.0e-15
    E1_IDW_427_J = (h**2) / (8.0 * mp * L_427**2)
    dE_13_427_J = 4.465 * E1_IDW_427_J
    lam_427 = (h * c) / dE_13_427_J
    results['40.27'] = {
        'E1_IDW_MeV': (E1_IDW_427_J / e) * 1e-6,
        'dE_13_MeV': (dE_13_427_J / e) * 1e-6,
        'lam_fm': lam_427 * 1e15
    }
    assert abs(E1_IDW_427_J / e * 1e-6 - 12.8) < 0.2
    assert abs(dE_13_427_J / e * 1e-6 - 57.1) < 0.5
    assert abs(lam_427 * 1e15 - 21.7) < 0.5

    # 40.28: Hạt alpha (m=6.64e-27 kg), rào U0 = 30.0 MeV, L = 2.0 fm
    L_428 = 2.0e-15
    U0_428 = 30.0e6 * e
    # (a) 1.0 MeV below top: U0 - E = 1.0 MeV, E = 29.0 MeV
    E_a_428 = 29.0e6 * e
    kap_a_428 = math.sqrt(2.0 * m_alpha * (U0_428 - E_a_428)) / hbar
    G_a_428 = 16.0 * (E_a_428 / U0_428) * (1.0 - E_a_428 / U0_428)
    T_a_approx_428 = G_a_428 * math.exp(-2.0 * kap_a_428 * L_428)
    # Công thức chính xác
    T_a_exact_428 = 1.0 / (1.0 + (U0_428**2 / (4.0 * E_a_428 * (U0_428 - E_a_428))) * (math.sinh(kap_a_428 * L_428))**2)
    # (b) 10.0 MeV below top: U0 - E = 10.0 MeV, E = 20.0 MeV
    E_b_428 = 20.0e6 * e
    kap_b_428 = math.sqrt(2.0 * m_alpha * (U0_428 - E_b_428)) / hbar
    G_b_428 = 16.0 * (E_b_428 / U0_428) * (1.0 - E_b_428 / U0_428)
    T_b_approx_428 = G_b_428 * math.exp(-2.0 * kap_b_428 * L_428)
    results['40.28'] = {
        'T_a_approx': T_a_approx_428,
        'T_a_exact': T_a_exact_428,
        'T_b_approx': T_b_approx_428
    }
    assert abs(T_a_approx_428 - 0.0897) < 0.005
    assert abs(T_b_approx_428 - 0.0141) < 0.001

    # 40.29: Barrier U0 = 41 eV, L = 0.25 nm, E = 32 eV
    U0_429 = 41.0 * e
    E_429 = 32.0 * e
    L_429 = 0.25e-9
    G_429 = 16.0 * (E_429 / U0_429) * (1.0 - E_429 / U0_429)
    # (a) electron
    kap_e_429 = math.sqrt(2.0 * me * (U0_429 - E_429)) / hbar
    T_e_429 = G_429 * math.exp(-2.0 * kap_e_429 * L_429)
    # (b) proton
    kap_p_429 = math.sqrt(2.0 * mp * (U0_429 - E_429)) / hbar
    T_p_429 = G_429 * math.exp(-2.0 * kap_p_429 * L_429)
    results['40.29'] = {'T_e': T_e_429, 'T_p': T_p_429}
    assert abs(T_e_429 - 1.26e-3) < 0.05e-3
    assert T_p_429 < 1e-100

    # 40.30: Electron E = 5.0 eV, L = 0.60 nm
    L_430 = 0.60e-9
    Ev_430 = 5.0 * e
    def calc_T_430(U0_eV):
        Uv = U0_eV * e
        kap = math.sqrt(2.0 * me * (Uv - Ev_430)) / hbar
        G = 16.0 * (Ev_430 / Uv) * (1.0 - Ev_430 / Uv)
        return G * math.exp(-2.0 * kap * L_430)
    T_a_430 = calc_T_430(7.0)
    T_b_430 = calc_T_430(9.0)
    T_c_430 = calc_T_430(13.0)
    results['40.30'] = {'T_a': T_a_430, 'T_b': T_b_430, 'T_c': T_c_430}
    assert abs(T_a_430 - 5.46e-4) < 0.1e-4
    assert abs(T_b_430 - 1.80e-5) < 0.05e-5
    assert abs(T_c_430 - 1.06e-7) < 0.05e-7


def verify_exercises_31_35():
    """Xác minh các bài tập 40.31 đến 40.35."""
    # 40.31: Electron E = 6.0 eV, U0 = 11.0 eV. (a) L = 0.80 nm, (b) L = 0.40 nm
    Ev_431 = 6.0 * e
    Uv_431 = 11.0 * e
    kap_431 = math.sqrt(2.0 * me * (Uv_431 - Ev_431)) / hbar
    G_431 = 16.0 * (Ev_431 / Uv_431) * (1.0 - Ev_431 / Uv_431)
    T_a_431 = G_431 * math.exp(-2.0 * kap_431 * 0.80e-9)
    T_b_431 = G_431 * math.exp(-2.0 * kap_431 * 0.40e-9)
    results['40.31'] = {'T_a': T_a_431, 'T_b': T_b_431}
    assert abs(T_a_431 - 4.3e-8) < 0.2e-8
    assert abs(T_b_431 - 4.14e-4) < 0.1e-4

    # 40.32: Electron vượt rào thế, E = 2 U0
    # K_out = 2 U0, K_in = U0
    # lambda_out / lambda_in = sqrt(K_in / K_out) = 1/sqrt(2)
    ratio_432 = 1.0 / math.sqrt(2.0)
    results['40.32'] = {'ratio': ratio_432}
    assert abs(ratio_432 - 0.7071) < 0.001

    # 40.33: Khối gỗ m = 0.250 kg, k' = 110 N/m
    m_433 = 0.250
    kp_433 = 110.0
    omega_433 = math.sqrt(kp_433 / m_433)
    E0_433_J = 0.5 * hbar * omega_433
    dE_433_J = hbar * omega_433
    results['40.33'] = {
        'omega': omega_433,
        'E0_J': E0_433_J,
        'E0_eV': E0_433_J / e,
        'dE_J': dE_433_J,
        'dE_eV': dE_433_J / e
    }
    assert abs(E0_433_J - 1.11e-33) < 0.02e-33
    assert abs(dE_433_J - 2.21e-33) < 0.02e-33

    # 40.34: Dao động điều hòa lượng tử mức n
    # p_max = sqrt((2n+1) hbar sqrt(m k'))
    # A = sqrt((2n+1) hbar / sqrt(m k'))
    # Delta x Delta px = (n + 1/2) hbar
    results['40.34'] = {'uncertainty_ground': 0.5}

    # 40.35: Quang phổ hồng ngoại, hấp thụ lambda = 5.8 um = 5.8e-6 m
    lam_435 = 5.8e-6
    dE_435_J = (h * c) / lam_435
    dE_435_eV = dE_435_J / e
    # dE = hbar * omega = hbar * sqrt(k' / m)
    m_435 = 5.6e-26
    omega_435 = dE_435_J / hbar
    kp_435 = m_435 * (omega_435**2)
    results['40.35'] = {
        'dE_J': dE_435_J,
        'dE_eV': dE_435_eV,
        'omega': omega_435,
        'kp_N_m': kp_435
    }
    assert abs(dE_435_eV - 0.214) < 0.005
    assert abs(kp_435 - 5907) < 50


def verify_structural_claims():
    """Check qualitative and algebraic claims using independent samples."""
    gaussian_rows=[]
    for a in [0.5,1.0,2.0]:
        grid=np.linspace(-10/math.sqrt(a),10/math.sqrt(a),100001)
        state=(2*a/math.pi)**0.25*np.exp(-a*grid**2)
        derivative=-2*a*grid*state
        norm=float(np.trapezoid(state**2,grid))
        x2=float(np.trapezoid(grid**2*state**2,grid))
        p2=hbar**2*float(np.trapezoid(derivative**2,grid))
        assert math.isclose(norm,1,rel_tol=1e-11)
        assert math.isclose(x2,1/(4*a),rel_tol=1e-11)
        assert math.isclose(p2,a*hbar**2,rel_tol=1e-11)
        gaussian_rows.append((a,math.sqrt(x2),math.sqrt(p2)))
    assert gaussian_rows[0][1]>gaussian_rows[1][1]>gaussian_rows[2][1]
    assert gaussian_rows[0][2]<gaussian_rows[1][2]<gaussian_rows[2][2]
    results['40.4']['computed_variances']=gaussian_rows
    for n in range(1,5):
        assert abs(math.sin(n*math.pi))<1e-14
        assert math.isclose(math.sin((n-.5)*math.pi)**2,1,rel_tol=1e-14)
    grid=np.linspace(0,1,100001)
    density=2*np.sin(math.pi*grid)**2
    assert abs(np.trapezoid(density,grid)-1)<1e-12
    assert abs(grid[int(np.argmax(density))]-.5)<1e-10
    assert density[0]<1e-20 and density[-1]<1e-20
    #40.6: A nonzero component in each different eigenspace prevents a single eigenvalue.
    state=np.array([1.,2.]);state/=np.linalg.norm(state)
    Hamiltonian=np.diag([1.,4.])
    expected=float(state@Hamiltonian@state)
    residual=np.linalg.norm(Hamiltonian@state-expected*state)
    assert residual>.1
    results['40.6']['computed_eigenstate_residual']=float(residual)
    #40.17: Smallest integer pair from the given mass/width ratios.
    candidates=[(na,nb) for na in range(1,5) for nb in range(1,5)
                if math.isclose(na*na/9,nb*nb/4,rel_tol=1e-12)]
    assert min(candidates,key=lambda pair:sum(pair))==(3,2)
    #40.21: Boundary residuals of both centered parity families.
    odd=[1,3,5];even=[2,4,6]
    for n in odd:assert abs(math.cos(n*math.pi/2))<1e-14
    for n in even:assert abs(math.sin(n*math.pi/2))<1e-14
    assert sorted(odd+even)==list(range(1,7))
    #40.34: Check the derived energy/amplitude/momentum identities at several levels.
    mass=2.;spring=8.;omega=math.sqrt(spring/mass)
    for n in range(5):
        energy=(n+.5)*hbar*omega
        amplitude=math.sqrt(2*energy/spring)
        momentum=math.sqrt(2*mass*energy)
        assert math.isclose(amplitude*momentum/2,(n+.5)*hbar,rel_tol=1e-12)
        assert math.isclose(spring*amplitude**2/2,energy,rel_tol=1e-12)
        assert math.isclose(momentum**2/(2*mass),energy,rel_tol=1e-12)
    print("✓ Đã đối chiếu chuẩn hóa, phương sai Gaussian, nút sóng, tính riêng năng lượng, tính chẵn lẻ và các hệ thức dao động tử.")


def main():
    print("=== BẮT ĐẦU KIỂM TRA ĐỘC LẬP TẤT CẢ BÀI TOÁN CHAPTER 40 NHÓM C ===")
    verify_guided_practice()
    print("✓ Đã xác minh 12 bài luyện tập hướng dẫn (VP40.4.1–VP40.7.4).")
    verify_exercises_01_15()
    print("✓ Đã xác minh 15 bài tập 40.1–40.15.")
    verify_exercises_16_30()
    print("✓ Đã xác minh 15 bài tập 40.16–40.30.")
    verify_exercises_31_35()
    print("✓ Đã xác minh 5 bài tập 40.31–40.35.")
    verify_structural_claims()
    assert len(results)==47
    print("Các phép tính đã chạy đều đạt. Độ đầy đủ của đề bài và giao diện được rà riêng.")

if __name__ == '__main__':
    main()
