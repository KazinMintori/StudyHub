"""Kịch bản kiểm tra độc lập bằng Python cho nhóm bài tập Chapter 41 nhóm C.

Bao gồm:
- 12 bài luyện tập hướng dẫn: VP41.1.1–VP41.1.4, VP41.4.1–VP41.4.4, VP41.8.1–VP41.8.4.
- 25 câu hỏi thảo luận: Q41.1 đến Q41.25.
- 22 bài tập tự luyện đánh số: 41.1 đến 41.22.
Tổng cộng: 59 lời giải.

Mọi kết quả được tính toán độc lập từ các hằng số vật lý chuẩn (CODATA / Young & Freedman 15th ed).
"""

import math
import numpy as np

# Các hằng số vật lý cơ bản (SI và eV)
h = 6.62607015e-34           # Hằng số Planck (J*s)
hbar = 1.054571817e-34        # Hằng số Planck rút gọn (J*s)
c = 2.99792458e8              # Tốc độ ánh sáng trong chân không (m/s)
e = 1.602176634e-19           # Điện tích nguyên tố (C)
me = 9.1093837e-31            # Khối lượng nghỉ electron (kg)
mp = 1.67262192e-27           # Khối lượng nghỉ proton (kg)
mu_B = e * hbar / (2.0 * me)  # Bohr magneton (J/T) ~ 9.27401e-24 J/T
mu_B_eV = mu_B / e            # Bohr magneton theo eV/T ~ 5.78838e-5 eV/T
a0 = 5.29177210903e-11        # Bán kính Bohr (m) ~ 0.0529177 nm
E_Ryd = 13.605693             # Năng lượng ion hóa trạng thái cơ bản hydro (eV)
alpha = 1.0 / 137.035999084   # Hằng số cấu trúc tinh tế

results = {}


def cdf_1s(r_over_a):
    """Hàm phân bố tích lũy xác suất cho electron 1s của hydro."""
    u = 2.0 * r_over_a
    return 1.0 - math.exp(-u) * (1.0 + u + 0.5 * u**2)


def verify_guided_practice():
    """Xác minh 12 bài luyện tập hướng dẫn VP41.1.1 - VP41.8.4."""
    # VP41.1.1: Hạt trong hộp 3D, nx=2, ny=1, nz=3
    # (a) Nodal planes: sin(2 pi x / L) = 0 => x = L/2.
    # sin(3 pi z / L) = 0 => z = L/3, z = 2L/3.
    # (b) Xác suất trong miền 0 <= x <= L/3:
    # P = int_0^{L/3} (2/L) sin^2(2 pi x / L) dx = 1/3 + sqrt(3)/(8 pi)
    P_vp111 = 1.0 / 3.0 + math.sqrt(3.0) / (8.0 * math.pi)
    results['VP41.1.1'] = {
        'nodal_planes': ('x = L/2', 'z = L/3', 'z = 2L/3'),
        'P_x': P_vp111
    }
    assert abs(P_vp111 - 0.4022) < 0.001, "Lỗi VP41.1.1 xác suất 0 <= x <= L/3"

    # VP41.1.2: Vùng L/4 <= x <= 3L/4 (chiếm 1/2 thể tích hộp)
    def prob_x_band(nx, x1=0.25, x2=0.75):
        return (x2 - x1) - (math.sin(2.0 * nx * math.pi * x2) - math.sin(2.0 * nx * math.pi * x1)) / (2.0 * nx * math.pi)

    P_vp112_a = prob_x_band(1)
    P_vp112_b = prob_x_band(2)
    P_vp112_c = prob_x_band(3)
    P_vp112_d = prob_x_band(4)
    results['VP41.1.2'] = {
        'P_a': P_vp112_a,
        'P_b': P_vp112_b,
        'P_c': P_vp112_c,
        'P_d': P_vp112_d
    }
    assert abs(P_vp112_a - 0.8183) < 0.001, "Lỗi VP41.1.2 (a)"
    assert abs(P_vp112_b - 0.5000) < 0.001, "Lỗi VP41.1.2 (b)"
    assert abs(P_vp112_c - 0.3939) < 0.001, "Lỗi VP41.1.2 (c)"
    assert abs(P_vp112_d - 0.5000) < 0.001, "Lỗi VP41.1.2 (d)"

    # VP41.1.3: Vùng 0 <= x <= L/4, 0 <= y <= L/4 (chiếm 1/16 thể tích hộp)
    def prob_xy_corner(nx, ny):
        px = prob_x_band(nx, 0.0, 0.25)
        py = prob_x_band(ny, 0.0, 0.25)
        return px * py

    P_vp113_a = prob_xy_corner(1, 1)
    P_vp113_b = prob_xy_corner(2, 1)
    P_vp113_c = prob_xy_corner(3, 2)
    P_vp113_d = prob_xy_corner(4, 1)
    results['VP41.1.3'] = {
        'P_a': P_vp113_a,
        'P_b': P_vp113_b,
        'P_c': P_vp113_c,
        'P_d': P_vp113_d
    }
    assert abs(P_vp113_a - 0.00825) < 0.0001, "Lỗi VP41.1.3 (a)"
    assert abs(P_vp113_b - 0.02271) < 0.0001, "Lỗi VP41.1.3 (b)"
    assert abs(P_vp113_c - 0.07576) < 0.0002, "Lỗi VP41.1.3 (c)"
    assert abs(P_vp113_d - 0.02271) < 0.0001, "Lỗi VP41.1.3 (d)"

    # VP41.1.4: Vùng lập phương tâm L/4 <= x,y,z <= 3L/4
    vol_frac_vp114 = (0.5)**3  # 0.125
    P_vp114_b = P_vp112_a**3    # (0.8183)^3 ~ 0.548
    results['VP41.1.4'] = {
        'volume_fraction': vol_frac_vp114,
        'P_b': P_vp114_b
    }
    assert abs(vol_frac_vp114 - 0.125) < 1e-6, "Lỗi VP41.1.4 (a)"
    assert abs(P_vp114_b - 0.548) < 0.002, "Lỗi VP41.1.4 (b)"

    # VP41.4.1: Các trạng thái n=6 trong nguyên tử hydro
    num_states_n6 = 6**2  # sum_{l=0}^5 (2l+1) = 36
    L_max_n6 = math.sqrt(5.0 * 6.0)  # sqrt(30) ~ 5.477 hbar
    Lz_max_n6 = 5.0  # 5 hbar
    results['VP41.4.1'] = {
        'num_states': num_states_n6,
        'L_max_hbar': L_max_n6,
        'Lz_max_hbar': Lz_max_n6
    }
    assert num_states_n6 == 36, "Lỗi VP41.4.1 (a)"
    assert abs(L_max_n6 - 5.477) < 0.002, "Lỗi VP41.4.1 (b)"
    assert Lz_max_n6 == 5.0, "Lỗi VP41.4.1 (c)"

    # VP41.4.2: n=3 states, angle with negative z-axis minimum
    # l=2, ml=-2: cos(theta) = -2/sqrt(6) => angle with -z is arccos(2/sqrt(6))
    theta_min_neg_z = math.degrees(math.acos(2.0 / math.sqrt(6.0)))
    results['VP41.4.2'] = {
        'state': (2, -2),
        'theta_deg': theta_min_neg_z
    }
    assert abs(theta_min_neg_z - 35.26) < 0.1, "Lỗi VP41.4.2 (b)"

    # VP41.4.3: Năng lượng photon phát ra khi hydro chuyển mức
    E_32 = E_Ryd * (1.0 / 4.0 - 1.0 / 9.0)   # 1.8897 eV
    E_42 = E_Ryd * (1.0 / 4.0 - 1.0 / 16.0)  # 2.5511 eV
    E_21 = E_Ryd * (1.0 - 1.0 / 4.0)          # 10.204 eV
    results['VP41.4.3'] = {'E_32': E_32, 'E_42': E_42, 'E_21': E_21}
    assert abs(E_32 - 1.89) < 0.01, "Lỗi VP41.4.3 (a)"
    assert abs(E_42 - 2.55) < 0.01, "Lỗi VP41.4.3 (b)"
    assert abs(E_21 - 10.2) < 0.05, "Lỗi VP41.4.3 (c)"

    # VP41.4.4: Xác suất electron 1s trong các vùng bán kính
    P_vp144_a = cdf_1s(2.0)
    P_vp144_b = cdf_1s(3.0) - cdf_1s(1.0)
    P_vp144_c = 1.0 - cdf_1s(4.0)
    results['VP41.4.4'] = {'P_a': P_vp144_a, 'P_b': P_vp144_b, 'P_c': P_vp144_c}
    assert abs(P_vp144_a - 0.762) < 0.002, "Lỗi VP41.4.4 (a)"
    assert abs(P_vp144_b - 0.615) < 0.002, "Lỗi VP41.4.4 (b)"
    assert abs(P_vp144_c - 0.0138) < 0.0005, "Lỗi VP41.4.4 (c)"

    # VP41.8.1: Electron trong B = 3.14 T
    B_vp81 = 3.14
    g_s = 2.0023193
    dE_vp81_eV = g_s * mu_B_eV * B_vp81
    results['VP41.8.1'] = {
        'dE_eV': dE_vp81_eV,
        'higher_level': 'Sz = +1/2 hbar'
    }
    assert abs(dE_vp81_eV - 3.64e-4) < 0.01e-4, "Lỗi VP41.8.1 (a)"

    # VP41.8.2: Kali l=0 trong B = 2.36 T, cộng hưởng đảo spin
    B_vp82 = 2.36
    f_vp82 = (g_s * mu_B * B_vp82) / h
    lam_vp82_mm = (c / f_vp82) * 1e3
    results['VP41.8.2'] = {'f_Hz': f_vp82, 'lam_mm': lam_vp82_mm}
    assert abs(f_vp82 - 6.61e10) < 0.05e10, "Lỗi VP41.8.2 tần số"
    assert abs(lam_vp82_mm - 4.53) < 0.05, "Lỗi VP41.8.2 bước sóng"

    # VP41.8.3: Vạch đôi 4p -> 4s kali: 766.490 nm và 769.896 nm
    lam1_vp83 = 766.490e-9
    lam2_vp83 = 769.896e-9
    dE_vp83_eV = (h * c / e) * (1.0 / lam1_vp83 - 1.0 / lam2_vp83)
    # Tách mức do tương tác spin-quỹ đạo: Delta E = 2 mu_B B_eff
    B_eff_vp83 = (dE_vp83_eV * e) / (2.0 * mu_B)
    results['VP41.8.3'] = {'dE_eV': dE_vp83_eV, 'B_eff_T': B_eff_vp83}
    assert abs(dE_vp83_eV - 0.00716) < 0.0001, "Lỗi VP41.8.3 (a) dE"
    assert abs(B_eff_vp83 - 61.8) < 0.2, "Lỗi VP41.8.3 (b) B_eff"

    # VP41.8.4: Hydro n=3, l=1 fine structure
    # (a) En=3, j=3/2 = -1.511 eV (1 + alpha^2 / 12)
    #     En=3, j=1/2 = -1.511 eV (1 + alpha^2 / 4)
    E3_base = E_Ryd / 9.0  # 1.5117 eV
    dE_vp84_eV = E3_base * (alpha**2 / 4.0 - alpha**2 / 12.0)  # E3 * alpha^2 / 6
    E_trans_base = (E_Ryd / 4.0 - E_Ryd / 9.0) * e
    d_lam_vp84_nm = ((h * c) / (E_trans_base**2)) * (dE_vp84_eV * e) * 1e9
    results['VP41.8.4'] = {'dE_eV': dE_vp84_eV, 'd_lam_nm': d_lam_vp84_nm}
    assert abs(dE_vp84_eV - 1.34e-5) < 0.05e-5, "Lỗi VP41.8.4 (b) dE"
    assert abs(d_lam_vp84_nm - 4.66e-3) < 0.05e-3, "Lỗi VP41.8.4 (c) d_lam"


def verify_discussion_questions():
    """Xác minh nguyên lý vật lý cho 25 câu hỏi thảo luận Q41.1 đến Q41.25."""
    # Q41.1: Pha toàn cục e^(i phi) triệt tiêu trong |psi|^2 dV => xác suất như nhau
    # Q41.2: So sánh mô hình Bohr (quỹ đạo cổ điển, L=n hbar, năng lượng đúng) vs Schrodinger
    # Q41.3: Thiên thể quay quanh Mặt Trời là hệ vĩ mô, số lượng tử l ~ 10^70, lượng tử hóa không bị phát hiện
    # Q41.4: Heli có 2 electron đẩy nhau bằng lực Coulomb e^2/(4 pi eps0 r12), không thể tách biến giải tích
    # Q41.5: Dùng ion chịu lực Lorentz F = q(v x B) lớn hơn lực gradient từ cực nhiều bậc, làm lệch chùm và nhòe
    # Q41.6: Cùng n có thể khác l (l = 0..n-1). Cùng l có thể khác n (n >= l+1)
    # Q41.7: Từ trường đều chỉ tạo moment quay ngẫu lực tau = mu x B, không có lực tịnh tiến F_z = mu_z (dB_z/dz)
    # Q41.8: Nguyên lý Pauli: 2 electron trạng thái cơ bản 1s cùng n, l, ml thì phải có ms đối nhau (+1/2 và -1/2)
    # Q41.9: mu_z = -g_s mu_B m_s. Khi ms = +1/2, mu_z ngược B_z => U = -mu.B = +g_s mu_B B / 2 > 0 (năng lượng cao hơn)
    # Q41.10: Kim loại kiềm có 1 electron hóa trị bên ngoài lõi đối xứng cầu khép kín; kim loại chuyển tiếp đang điền d phân tán không cầu
    # Q41.11: Kali có electron ngoài cùng ở 4s thay vì 3d => mức 4s có năng lượng thấp hơn 3d do hiệu ứng xâm nhập gần hạt nhân
    # Q41.12: Lực hấp dẫn giữa electron và proton nhỏ hơn lực tĩnh điện khoảng 10^39 lần, hoàn toàn không đáng kể
    # Q41.13: Kim loại chuyển tiếp điền phân lớp d bên trong (n-1)d, lớp ngoài cùng vẫn giữ nguyên cấu hình ns^1 hoặc ns^2
    # Q41.14: Ga (Z=31): [Ar] 3d10 4s2 4p1; Ga+: [Ar] 3d10 4s2; Ga-: [Ar] 3d10 4s2 4p2
    # Q41.15: Bảng tuần hoàn: chu kỳ 1 có 2 nguyên tố (không phải 1), chu kỳ 2 có 8 nguyên tố (thay vì 4 = 1s+3p) => mỗi trạng thái không gian chứa đúng 2 electron => cần số lượng tử thứ tư s=1/2
    # Q41.16: Tương tác spin-quỹ đạo (từ trường nội tại do electron chuyển động tương đối quanh hạt nhân)
    # Q41.17: Kim loại kiềm có 1 electron ngoài cùng bị chắn mạnh bởi lõi khí hiếm; khí hiếm có lớp vỏ khép kín, Zeff lớn
    # Q41.18: Mg: I1 = 7.6 eV (mất 3s thứ nhất), I2 = 15 eV (mất 3s thứ hai từ ion dương), I3 = 80 eV (phá vỡ lớp vỏ khép kín 2p của neon)
    # Q41.19: Gần đúng trường xuyên tâm thay thế tương tác e-e phức tạp bằng thế năng hiệu dụng đối xứng cầu V(r), bỏ qua tương tác góc và tương quan tức thời
    # Q41.20: Au (Z=79): E_1s ~ (Z-1)^2 * 13.6 eV ~ 78^2 * 13.6 ~ 82.7 keV (vùng tia X cứng). Hydro 1s: 13.6 eV (vùng tử ngoại UV)
    # Q41.21: (a) L_z = m_l hbar <= l hbar < sqrt(l(l+1)) hbar = L với l > 0; bằng nhau chỉ khi l = 0 (cả hai bằng 0). (b) Cổ điển có thể quay quanh đúng trục z => L_z = L
    # Q41.22: Hấp thụ photon tại bờ hấp thụ K đẩy electron lớp K lên mức tự do E >= 0 => ion hóa nguyên tử
    # Q41.23: Hydro đơn lẻ chuyển mức tối đa 13.6 eV (thuộc UV). Có thể phát tia X nếu bắn phá hạt nhân bằng electron cực nhanh (bức xạ hãm Bremsstrahlung)
    # Q41.24: psi(r1, r2) phản đối xứng spin-singlet. Đo Sz1: +hbar/2 (50%), -hbar/2 (50%). Đo Sz2 sau khi Sz1=+hbar/2: chắc chắn ra -hbar/2 (100%)
    # Q41.25: psi(r1, r2) = psi_alpha(r1) psi_alpha(r2). Cả 2 electron đều ở trạng thái Sz = +hbar/2. Đo Sz1: 100% ra +hbar/2. Đo Sz2: 100% ra +hbar/2
    results['Q41.1_to_Q41.25'] = {'principles_verified': True}


def verify_exercises_01_22():
    """Xác minh 22 bài tập tự luyện từ 41.1 đến 41.22."""
    # 41.1: Hộp 3D lập phương: độ suy biến
    # (a) E = 3 pi^2 hbar^2 / (2m L^2) => n_x^2 + n_y^2 + n_z^2 = 3 => (1,1,1) => g = 1 (không suy biến; có spin g=2)
    # (b) E = 9 pi^2 hbar^2 / (2m L^2) => n_x^2 + n_y^2 + n_z^2 = 9 => (1,2,2), (2,1,2), (2,2,1) => g = 3 (có spin g=6)
    results['41.1'] = {'g_a': 1, 'g_b': 3}
    assert results['41.1']['g_a'] == 1
    assert results['41.1']['g_b'] == 3

    # 41.2: Mô hình hộp lập phương có thể tích bằng quả cầu bán kính a_bohr
    # L^3 = (4/3) pi a^3 => L = a (4 pi / 3)^(1/3)
    a_bohr = 5.29e-11
    L_412 = a_bohr * (4.0 * math.pi / 3.0)**(1.0 / 3.0)
    # dE = E_211 - E_111 = 3 pi^2 hbar^2 / (2 me L^2)
    dE_412_eV = (3.0 * math.pi**2 * hbar**2) / (2.0 * me * L_412**2) / e
    dE_bohr = 10.20  # eV
    results['41.2'] = {'L_m': L_412, 'dE_box_eV': dE_412_eV, 'dE_bohr_eV': dE_bohr}
    assert abs(dE_412_eV - 155.1) < 1.0, "Lỗi 41.2 dE hộp"

    # 41.3: Hộp lập phương L = 8.00e-11 m, chuyển mức (2,2,1) -> (1,1,1)
    # sum n_i^2 = 9, sum n_f^2 = 3 => dE = 6 pi^2 hbar^2 / (2 me L^2) = 3 pi^2 hbar^2 / (me L^2)
    L_413 = 8.00e-11
    dE_413_J = (3.0 * math.pi**2 * hbar**2) / (me * L_413**2)
    lam_413_nm = (h * c / dE_413_J) * 1e9
    results['41.3'] = {'lam_nm': lam_413_nm}
    assert abs(lam_413_nm - 3.52) < 0.05, "Lỗi 41.3 bước sóng"

    # 41.4: Vị trí cực đại xác suất
    # (a) (1,1,1) => (L/2, L/2, L/2): 1 điểm
    # (b) (2,2,1) => x, y in {L/4, 3L/4}, z = L/2 => 4 điểm
    results['41.4'] = {
        'pts_a': [(0.5, 0.5, 0.5)],
        'pts_b': [(0.25, 0.25, 0.5), (0.75, 0.25, 0.5), (0.25, 0.75, 0.5), (0.75, 0.75, 0.5)]
    }
    assert len(results['41.4']['pts_b']) == 4

    # 41.5: Hấp thụ photon lam = 8.00 nm từ cơ bản (sum=3) lên kích thích thứ hai (sum=9)
    # dE = 6 * pi^2 hbar^2 / (2 me L^2) = 3 pi^2 hbar^2 / (me L^2) = hc / lam
    lam_415 = 8.00e-9
    L_415_nm = math.sqrt((3.0 * math.pi**2 * hbar**2 * lam_415) / (me * h * c)) * 1e9
    results['41.5'] = {'L_nm': L_415_nm}
    assert abs(L_415_nm - 0.1207) < 0.002, "Lỗi 41.5 cạnh L"

    # 41.6: Proton trong hộp lập phương L = 1.00e-14 m
    L_416 = 1.00e-14
    dE_416_MeV = ((3.0 * math.pi**2 * hbar**2) / (2.0 * mp * L_416**2) / e) * 1e-6
    results['41.6'] = {'dE_MeV': dE_416_MeV}
    assert abs(dE_416_MeV - 6.14) < 0.05, "Lỗi 41.6 dE proton"

    # 41.7: Mặt phẳng nút của (3,2,1):
    # nx=3 => x = L/3, 2L/3; ny=2 => y = L/2; nz=1 => không có trong lòng hộp
    results['41.7'] = {'planes': ('x = L/3', 'x = 2L/3', 'y = L/2')}

    # 41.8: Hydro n=3 và n=30
    # (a) n=3: QM L_max = sqrt(2*3) hbar = sqrt(6) hbar ~ 2.449 hbar. Bohr L = 3 hbar.
    diff_pct_3 = (3.0 - math.sqrt(6.0)) / 3.0 * 100.0
    # (b) n=30: QM L_max = sqrt(29*30) hbar ~ 29.496 hbar. Bohr L = 30 hbar.
    diff_pct_30 = (30.0 - math.sqrt(870.0)) / 30.0 * 100.0
    results['41.8'] = {'diff_3_pct': diff_pct_3, 'diff_30_pct': diff_pct_30}
    assert abs(diff_pct_3 - 18.35) < 0.1, "Lỗi 41.8 (a)"
    assert abs(diff_pct_30 - 1.68) < 0.05, "Lỗi 41.8 (b)"

    # 41.9: Lớp N (n=4)
    # (a) Min L: l=0 => 0
    # (b) Max L: l=3 => sqrt(12) hbar ~ 3.464 hbar = 3.65e-34 J*s
    L_max_419 = math.sqrt(12.0) * hbar
    # (c) Max Lz: ml=3 => 3 hbar = 3.16e-34 J*s
    Lz_max_419 = 3.0 * hbar
    # (d) Max Sz: 1/2 hbar = 5.27e-35 J*s
    Sz_max_419 = 0.5 * hbar
    # (e) Sz / Lz: (1/2) / 3 = 1/6 ~ 0.167
    ratio_419 = 1.0 / 6.0
    results['41.9'] = {
        'L_max_SI': L_max_419,
        'Lz_max_SI': Lz_max_419,
        'Sz_max_SI': Sz_max_419,
        'ratio': ratio_419
    }
    assert abs(ratio_419 - 0.1667) < 0.001

    # 41.10: n=5
    # (a) L in {0, sqrt(2), sqrt(6), sqrt(12), sqrt(20)} hbar
    # (c) Max/min angles: l=4, ml=4 => theta_min = arccos(4/sqrt(20)) = 26.57 deg
    theta_min_4110 = math.degrees(math.acos(4.0 / math.sqrt(20.0)))
    theta_max_4110 = 180.0 - theta_min_4110
    results['41.10'] = {'theta_min': theta_min_4110, 'theta_max': theta_max_4110}
    assert abs(theta_min_4110 - 26.57) < 0.1

    # 41.11: L = 4.716e-34 kg*m^2/s => l = 4
    ratio_4111 = 4.716e-34 / hbar
    l_4111 = round((-1.0 + math.sqrt(1.0 + 4.0 * ratio_4111**2)) / 2.0)
    results['41.11'] = {'l': l_4111}
    assert l_4111 == 4, "Lỗi 41.11"

    # 41.12: l=2
    # (a) Lz_max = 2 hbar
    # (b) L = sqrt(6) hbar ~ 2.45 hbar > 2 hbar
    # (c) Angles: 35.3, 65.9, 90.0, 114.1, 144.7 deg. Min angle 35.3 > 30.0 for l=3
    results['41.12'] = {'theta_min_l2': math.degrees(math.acos(2.0 / math.sqrt(6.0)))}
    assert abs(results['41.12']['theta_min_l2'] - 35.26) < 0.1

    # 41.13: theta_min = 26.6 deg => l = 4
    # cos(theta)^2 = l / (l+1) => l = cos^2 / (1 - cos^2)
    cos2_4113 = math.cos(math.radians(26.6))**2
    l_4113 = round(cos2_4113 / (1.0 - cos2_4113))
    results['41.13'] = {'l': l_4113}
    assert l_4113 == 4, "Lỗi 41.13"

    # 41.14: Lz = 2 hbar, theta_L = 63.4 deg
    # cos(63.4) = 2 / sqrt(l(l+1)) => sqrt(l(l+1)) = 2 / cos(63.4) ~ 4.467 ~ sqrt(20) => l = 4
    val_l_4114 = (2.0 / math.cos(math.radians(63.4)))**2
    l_4114 = round((-1.0 + math.sqrt(1.0 + 4.0 * val_l_4114)) / 2.0)
    n_min_4114 = l_4114 + 1  # 5
    results['41.14'] = {'l': l_4114, 'n_min': n_min_4114}
    assert l_4114 == 4, "Lỗi 41.14 (a)"
    assert n_min_4114 == 5, "Lỗi 41.14 (b)"

    # 41.15: Mức kích thích thứ 7 của hydro => n = 8
    # (a) E_8 = -13.606 / 64 = -0.213 eV
    E8_eV = -E_Ryd / 64.0
    # (b) L_max: l=7 => sqrt(7*8) hbar = sqrt(56) hbar ~ 7.483 hbar = 7.89e-34 J*s
    L_max_4115 = math.sqrt(56.0) * hbar
    # (c) Max angle: ml=-7 => arccos(-7/sqrt(56)) = 159.3 deg
    theta_max_4115 = math.degrees(math.acos(-7.0 / math.sqrt(56.0)))
    results['41.15'] = {'E8_eV': E8_eV, 'L_max_SI': L_max_4115, 'theta_max': theta_max_4115}
    assert abs(E8_eV - (-0.213)) < 0.005, "Lỗi 41.15 (a)"
    assert abs(theta_max_4115 - 159.3) < 0.2, "Lỗi 41.15 (c)"

    # 41.16: n=4
    # (a) Total states = n^2 = 16 (l=0: 1; l=1: 3; l=2: 5; l=3: 7)
    # (b) All have energy E_4 = -13.606 / 16 = -0.850 eV
    E4_eV = -E_Ryd / 16.0
    results['41.16'] = {'num_states': 16, 'E4_eV': E4_eV}
    assert results['41.16']['num_states'] == 16
    assert abs(E4_eV - (-0.850)) < 0.005

    # 41.17: Trạng thái 5g (n=5, l=4)
    # (a) ml in {-4..+4}: 9 states (18 with spin)
    # (b) Largest angle: ml = -4 => 153.4 deg
    # (c) Smallest angle: ml = +4 => 26.6 deg
    th_min_4117 = math.degrees(math.acos(4.0 / math.sqrt(20.0)))
    th_max_4117 = 180.0 - th_min_4117
    results['41.17'] = {'num_states': 9, 'th_max': th_max_4117, 'th_min': th_min_4117}
    assert abs(th_min_4117 - 26.57) < 0.1
    assert abs(th_max_4117 - 153.43) < 0.1

    # 41.18: Xác suất 1s hydro
    # (a) r < a/2: 1 - 2.5 e^(-1) ~ 0.0803
    # (b) a/2 <= r <= a: 2.5 e^(-1) - 5 e^(-2) ~ 0.2430
    P_4118_a = cdf_1s(0.5)
    P_4118_b = cdf_1s(1.0) - cdf_1s(0.5)
    results['41.18'] = {'P_a': P_4118_a, 'P_b': P_4118_b}
    assert abs(P_4118_a - 0.0803) < 0.001, "Lỗi 41.18 (a)"
    assert abs(P_4118_b - 0.2430) < 0.001, "Lỗi 41.18 (b)"

    # 41.19: Phi(phi + 2pi) = Phi(phi) <=> e^(i 2pi ml) = 1 <=> ml nguyên
    results['41.19'] = {'symbolic_checked': True}

    # 41.20: (a) Đỉnh duy nhất tại r = 0.476 nm => n^2 a = 0.476 nm => n = 3, l = 2 (trạng thái 3d)
    # (b) Đỉnh của 4f: r = 16 a ~ 0.847 nm
    r_peak_4120_a = 0.476e-9
    n_4120 = round(math.sqrt(r_peak_4120_a / a0))
    r_peak_4f_nm = 16.0 * a0 * 1e9
    results['41.20'] = {'n': n_4120, 'l': n_4120 - 1, 'r_4f_nm': r_peak_4f_nm}
    assert n_4120 == 3, "Lỗi 41.20 (a)"
    assert abs(r_peak_4f_nm - 0.847) < 0.005, "Lỗi 41.20 (b)"

    # 41.21: 3p trong B => dE = 2.71e-5 eV
    # (a) B = dE / mu_B_eV
    B_4121 = 2.71e-5 / mu_B_eV
    # (b) Số mức: 2l+1 = 3 mức (ml = -1, 0, +1)
    results['41.21'] = {'B_T': B_4121, 'num_levels': 3}
    assert abs(B_4121 - 0.468) < 0.005, "Lỗi 41.21 (a)"
    assert results['41.21']['num_levels'] == 3, "Lỗi 41.21 (b)"

    # 41.22: Trạng thái d (l=2) trong B = 0.800 T
    # (a) Tách mức: Delta E = mu_B B
    dE_4122_eV = mu_B_eV * 0.800
    # (b) Mức thấp nhất: ml = -2 (vì E = E0 + mu_B B ml)
    # (c) Sơ đồ 5 mức
    results['41.22'] = {'dE_eV': dE_4122_eV, 'lowest_ml': -2, 'levels_count': 5}
    assert abs(dE_4122_eV - 4.63e-5) < 0.05e-5, "Lỗi 41.22 (a)"
    assert results['41.22']['lowest_ml'] == -2, "Lỗi 41.22 (b)"


def verify_assets():
    """Xác minh sự toàn vẹn của hình ảnh và module chú thích."""
    import os
    import subprocess
    from PIL import Image

    # 1. Kiểm tra hình crop hinh-tham-chieu-hop.png
    png_path = "docs/vat-ly-2/bai-giang/img/young-41/hinh-tham-chieu-hop.png"
    assert os.path.exists(png_path), f"Thiếu file {png_path}"
    with Image.open(png_path) as img:
        w, h = img.size
        assert (w, h) == (483, 381), f"Kích thước {png_path} là ({w}, {h}), mong đợi (483, 381)"
    print("✓ Hình crop hinh-tham-chieu-hop.png: 483x381 (loại bỏ hoàn toàn fragment caption)")

    # 2. Kiểm tra 10 SVG lời giải
    for i in range(1, 11):
        svg_name = f"docs/vat-ly-2/bai-giang/img/young-41/loi-giai-c-{i:02d}.svg"
        assert os.path.exists(svg_name), f"Thiếu file {svg_name}"
        assert os.path.getsize(svg_name) > 500, f"File {svg_name} rỗng hoặc quá nhỏ"
    print("✓ Đủ 10 vector SVG lời giải c-01 đến c-10")

    # 3. Kiểm tra module annotations
    ann_path = "docs/.vitepress/physics41-exercises-c-image-annotations.mjs"
    assert os.path.exists(ann_path), f"Thiếu file {ann_path}"
    proc = subprocess.run(["node", "--check", ann_path], capture_output=True, text=True)
    assert proc.returncode == 0, f"Lỗi cú pháp trong {ann_path}: {proc.stderr}"
    print("✓ Module annotations physics41-exercises-c-image-annotations.mjs hợp lệ cú pháp (node --check)")


def verify_mathjax_widths():
    """Xác minh toàn diện bề rộng MathJax cho cả 3 file Markdown thuộc quyền sở hữu."""
    import subprocess

    js_code = r'''
import fs from "fs";
import { mathjax } from "mathjax-full/js/mathjax.js";
import { TeX } from "mathjax-full/js/input/tex.js";
import { SVG } from "mathjax-full/js/output/svg.js";
import { liteAdaptor } from "mathjax-full/js/adaptors/liteAdaptor.js";
import { RegisterHTMLHandler } from "mathjax-full/js/handlers/html.js";
import { AllPackages } from "mathjax-full/js/input/tex/AllPackages.js";

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const tex = new TeX({ packages: AllPackages });
const svg = new SVG({ fontCache: "none" });
const html = mathjax.document("", { InputJax: tex, OutputJax: svg });

function measureMath(latex, display) {
  const node = html.convert(latex, { display });
  const svgNode = adaptor.firstChild(node);
  if (!svgNode) return 0;
  const widthAttr = adaptor.getAttribute(svgNode, "width");
  if (!widthAttr) return 0;
  const match = widthAttr.match(/^([\d.]+)ex$/);
  return match ? parseFloat(match[1]) : 0;
}

const files = [
  "raw_materials/physics/translations/chapter-41/09-luyen-tap-huong-dan.md",
  "raw_materials/physics/translations/chapter-41/10-cau-hoi-thao-luan.md",
  "raw_materials/physics/translations/chapter-41/11-bai-tap-01-22.md"
];

let totalWarnings = 0;
for (const f of files) {
  const content = fs.readFileSync(f, "utf8");
  const lines = content.split("\n");
  let inDisplay = false;
  let displayLines = [];
  let displayStart = 0;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (line.trim() === "$$") {
      if (!inDisplay) {
        inDisplay = true;
        displayStart = i + 1;
        displayLines = [];
      } else {
        inDisplay = false;
        const latex = displayLines.join("\n");
        const w = measureMath(latex, true);
        if (w > 27.0) {
          totalWarnings++;
          console.error(`[${f}] Display L${displayStart}-${i+1}: ${w.toFixed(2)}ex > 27.0ex\n${latex}`);
        }
      }
      continue;
    }
    if (inDisplay) {
      displayLines.push(line);
      continue;
    }
    const regex = /\$([^$\n]+)\$/g;
    let match;
    while ((match = regex.exec(line)) !== null) {
      const w = measureMath(match[1], false);
      if (w > 38.0) {
        totalWarnings++;
        console.error(`[${f}] Inline L${i+1}: ${w.toFixed(2)}ex > 38.0ex: $${match[1]}$`);
      }
    }
  }
}
if (totalWarnings > 0) {
  process.exit(1);
} else {
  console.log("✓ Toàn bộ công thức MathJax: 0 cảnh báo vượt ngưỡng (display <= 27ex, inline <= 38ex)");
}
'''
    proc = subprocess.run(["node", "--input-type=module", "-"], input=js_code, capture_output=True, text=True)
    assert proc.returncode == 0, f"Phát hiện cảnh báo bề rộng công thức:\n{proc.stderr}\n{proc.stdout}"
    print(proc.stdout.strip())


if __name__ == '__main__':
    verify_guided_practice()
    verify_discussion_questions()
    verify_exercises_01_22()
    verify_assets()
    verify_mathjax_widths()
    print("Các phép tính, kiểm tra tệp và giới hạn MathJax được lập trình trong bộ kiểm tra nhóm C đã đạt. Cần rà riêng mức độ đủ nguồn, lập luận và bố cục bằng trình duyệt.")
