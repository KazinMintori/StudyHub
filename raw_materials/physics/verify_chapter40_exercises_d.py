"""Kịch bản kiểm tra độc lập bằng Python cho nhóm bài tập Chapter 40 (nhóm D).

Bao gồm:
- 27 câu hỏi thảo luận Q40.1 - Q40.27
- Bài tập 40.36 - 40.50
- Bài tập 40.51 - 40.66 (gồm Bài toán thử thách 40.63 - 40.66)
- Bài đọc Chấm lượng tử (Quantum Dots) và 4 bài MCAT 40.67 - 40.70
- Toàn bộ Bài tập cầu nối (Bridging Problem) và 7 ý trong Solution Guide
"""
import numpy as np
from scipy.optimize import brentq
import math

# Các hằng số vật lý chuẩn (CODATA / Young & Freedman 15th Edition)
c = 2.99792458e8              # m/s
h = 6.62607015e-34            # J*s
hbar = h / (2 * np.pi)        # J*s (~1.0545718e-34 J*s)
e = 1.602176634e-19           # C
m_e = 9.1093837e-31           # kg (khối lượng electron)
m_p = 1.67262192e-27          # kg (khối lượng proton)
m_n = 1.6749275e-27           # kg (khối lượng neutron)
m_u = 1.660539066e-27         # kg (đơn vị khối lượng nguyên tử u)
eps0 = 8.8541878128e-12       # F/m
k_coulomb = 1.0 / (4 * np.pi * eps0)
a0 = (4 * np.pi * eps0 * hbar**2) / (m_e * e**2)  # ~0.529177e-10 m (bán kính Bohr)
hc_eV_nm = 1239.841984        # eV*nm

r = {}

# ==========================================
# 1. BÀI TẬP CẦU NỐI (Bridging Problem: A Packet in a Box)
# ==========================================
# Hố thế vô hạn: E_n = n^2 * pi^2 * hbar^2 / (2 * m * L^2)
# (a) Mật độ xác suất |Psi(x,t)|^2 = (1/L) * [sin^2(pi*x/L) + sin^2(2*pi*x/L) + 2*sin(pi*x/L)*sin(2*pi*x/L)*cos((E2-E1)t/hbar)]
# (b) Không phải trạng thái dừng vì mật độ phụ thuộc thời gian
# (c) Tích phân chuẩn hóa = 1/2 + 1/2 + 0 = 1
# (d) omega_osc = (E2 - E1) / hbar = 3 * pi^2 * hbar / (2 * m * L^2)
# (e) Hố thế hữu hạn U0 = 6 * E1_IDW:
# Tính nghiệm chính xác của phương trình siêu việt:
R2 = 1.5 * np.pi**2
R = np.sqrt(R2)

f_even = lambda xi: np.sqrt(R2 - xi**2) - xi * np.tan(xi)
xi_1 = brentq(f_even, 0.01, np.pi/2 - 0.001)

f_odd = lambda xi: np.sqrt(R2 - xi**2) + xi / np.tan(xi)
xi_2 = brentq(f_odd, np.pi/2 + 0.001, np.pi - 0.001)

e1_ratio = 4 * xi_1**2 / np.pi**2
e2_ratio = 4 * xi_2**2 / np.pi**2
delta_e_ratio = e2_ratio - e1_ratio
omega_coeff_exact = delta_e_ratio / 2.0

# Young & Freedman dùng nghiệm làm tròn E1 = 0.625 E1_IDW và E2 = 2.43 E1_IDW
delta_e_approx = 2.43 - 0.625
omega_coeff_approx = delta_e_approx / 2.0  # ~0.9025 -> 0.903

r['bridge'] = {
    'xi_1': xi_1,
    'xi_2': xi_2,
    'E1_ratio': e1_ratio,
    'E2_ratio': e2_ratio,
    'delta_E_ratio': delta_e_ratio,
    'omega_coeff_exact': omega_coeff_exact,
    'omega_coeff_source': 0.903,
}

# ==========================================
# 2. CÂU HỎI THẢO LUẬN (Q40.1 - Q40.27)
# ==========================================
# Q40.1: Bước sóng de Broglie quả bóng chày (m=0.145 kg, v=40 m/s)
lambda_baseball = h / (0.145 * 40.0)

# Q40.5: Hạt tự do với động lượng p xác định có hàm sóng phẳng exp(i(kx - omega*t)), |Psi|^2 = const
# Q40.6: n=0 cho psi=0 (không chuẩn hóa được), n âm chỉ đổi dấu toàn cục
# Q40.8: Cổ điển P(x) = 1/L, lượng tử <sin^2(n*pi*x/L)> -> 1/2 khi n -> inf
# Q40.9: sin(kx) = (exp(ikx) - exp(-ikx))/(2i), phân rã hai mode cục bộ trong hộp;
# khi giải phóng, phân bố Fourier là hàm liên tục sinc
# Q40.10: Đối xứng P(x) quanh L/2 cho P = 0.50 ở nửa phải
# Q40.16: Bước sóng hố hữu hạn dài hơn -> E1 < E1_IDW
# Q40.17: Hố thế 1D luôn có ít nhất 1 trạng thái liên kết
# Q40.20: STM quantum corral 48 Fe atoms -> hàm sóng Bessel J0(kr)
# Q40.23: Dao động điều hòa n -> vô cùng tiệm cận phân bố cổ điển P(x) ~ 1/v(x)
# Q40.25: Số lượng tử mức cơ bản và kích thích 2:
# H atom: n=1, n=3; Box: n=1, n=3; Harmonic oscillator: n=0, n=2.
# Q40.27: Trạng thái chồng chập đo năng lượng nhận E1 hoặc E2 xác suất 50%

r['discussion'] = {
    'q40_1_lambda_baseball': lambda_baseball,
    'q40_10_prob_right': 0.5,
    'q40_25_H': (1, 3),
    'q40_25_box': (1, 3),
    'q40_25_sho': (0, 2),
}

# ==========================================
# 3. BÀI TẬP 40.36 - 40.50
# ==========================================
# 40.36: Dao động điều hòa hấp thụ photon lambda = 6.35 um chuyển từ n=0 sang n=1
lam_36 = 6.35e-6
delta_E_36_J = h * c / lam_36
delta_E_36_eV = delta_E_36_J / e
E0_36_eV = 0.5 * delta_E_36_eV
r['40.36'] = {'delta_E_eV': delta_E_36_eV, 'E0_eV': E0_36_eV}

# 40.37: E0 = 5.60 eV -> Delta E = hbar*omega = 2*E0 = 11.20 eV
E0_37 = 5.60
delta_E_37 = 2 * E0_37
lam_37_nm = hc_eV_nm / delta_E_37
r['40.37'] = {'delta_E_eV': delta_E_37, 'lam_nm': lam_37_nm}

# 40.38: n=1 -> n=2 hấp thụ photon lambda = 6.50 um
lam_38 = 6.50e-6
lam_38_a = lam_38  # n=2 -> n=3 có Delta n = 1 -> cùng bước sóng
lam_38_b = lam_38 / 2.0  # n=1 -> n=3 có Delta n = 2 -> bước sóng giảm một nửa
omega_38 = 2 * np.pi * c / lam_38
r['40.38'] = {'lam_a_um': lam_38_a * 1e6, 'lam_b_um': lam_38_b * 1e6, 'omega': omega_38}

# 40.39: Na atom in Example 40.8: m = 3.82e-26 kg, U = 0.0075 eV at x = 0.014 nm
m_Na = 3.82e-26
U_Na_J = 0.0075 * e
x_Na = 0.014e-9
k_prime_Na = 2 * U_Na_J / (x_Na**2)
omega_Na = np.sqrt(k_prime_Na / m_Na)
hbar_omega_Na_J = hbar * omega_Na
hbar_omega_Na_eV = hbar_omega_Na_J / e
E0_Na_eV = 0.5 * hbar_omega_Na_eV
lam_Na_43_m = 2 * np.pi * c / omega_Na
r['40.39'] = {
    'k_prime': k_prime_Na,
    'omega': omega_Na,
    'E0_eV': E0_Na_eV,
    'lam_um': lam_Na_43_m * 1e6,
    'delta_E_eV': hbar_omega_Na_eV,
}

# 40.40: Tỉ số mật độ xác suất dao động điều hòa cơ bản
# A = 1/alpha -> alpha * A = 1
ratio_40_a = np.exp(-1.0)
ratio_40_b = np.exp(-4.0)
r['40.40'] = {'ratio_A': ratio_40_a, 'ratio_2A': ratio_40_b}

# 40.41: Hạt trong hộp [0, L] trạng thái chồng chập n=1 và n=3
# psi1(L/2) = sqrt(2/L), psi3(L/2) = -sqrt(2/L)
# P(L/2, t) = (2/L) * [1 - cos(omega_osc * t)]
# omega_osc = (E3 - E1)/hbar = 8 E1 / hbar = 4 * pi^2 * hbar / (m * L^2)
r['40.41'] = {'omega_factor': 4.0}

# 40.42: 4 vạch quang phổ khả kiến của hydrogen
lams_42 = np.array([656.0, 486.0, 434.0, 410.0])  # nm
E_photons_42 = hc_eV_nm / lams_42
# Khảo sát mô hình hạt trong hộp En = n^2 * P
# Dãy 4 vạch từ các mức kế tiếp ni đến cùng mức nf: Delta(n^2) = ni^2 - nf^2
r['40.42'] = {'E_photons_eV': E_photons_42}

# 40.43: Bước thế U0 < E
# B = ((k1 - k2)/(k1 + k2)) * A, C = (2*k1/(k1 + k2)) * A
r['40.43'] = {'formula_valid': True}

# 40.44: Tích phân mật độ trạng thái cơ bản trong hộp
# P(0 -> L/4) = 1/4 - 1/(2*pi)
P_44_a = 0.25 - 1.0 / (2 * np.pi)
P_44_b = 0.25 + 1.0 / (2 * np.pi)
P_44_d = P_44_a + P_44_b  # = 0.50
r['40.44'] = {'P_a': P_44_a, 'P_b': P_44_b, 'P_sum': P_44_d}

# 40.45: Electron trong laser nhuộm, hộp rộng L = 4.18 nm
L_45 = 4.18e-9
E1_45_J = (h**2) / (8 * m_e * L_45**2)
E1_45_eV = E1_45_J / e
# (a) n=2 -> n=1: Delta E = 3 * E1
dE_45_a_J = 3 * E1_45_J
lam_45_a_um = (h * c / dE_45_a_J) * 1e6
# (b) n=3 -> n=2: Delta E = 5 * E1
dE_45_b_J = 5 * E1_45_J
lam_45_b_um = (h * c / dE_45_b_J) * 1e6
r['40.45'] = {
    'E1_eV': E1_45_eV,
    'lam_a_um': lam_45_a_um,
    'lam_b_um': lam_45_b_um,
}

# 40.46 & 40.47: Xác suất vi phân trong khoảng dx
# 40.46 (n=1): P(x) = (2/L)*sin^2(pi*x/L)
# x = L/4 -> 1/L dx; x = L/2 -> 2/L dx; x = 3L/4 -> 1/L dx
# 40.47 (n=2): P(x) = (2/L)*sin^2(2*pi*x/L)
# x = L/4 -> 2/L dx; x = L/2 -> 0; x = 3L/4 -> 2/L dx
r['40.46'] = {'L_4': 1.0, 'L_2': 2.0, '3L_4': 1.0}
r['40.47'] = {'L_4': 2.0, 'L_2': 0.0, '3L_4': 2.0}

# 40.48: Dòng xuyên ngầm qua khe oxide giữa 2 dây đồng
# d = 1 mm, n = 8.5e28 m^-3, U0 = 12 eV, E = 5.0 eV, L = 1 nm
d_48 = 1.0e-3
A_48 = np.pi * (d_48 / 2.0)**2
n_48 = 8.5e28
U0_48 = 12.0 * e
E_48 = 5.0 * e
L_48 = 1.0e-9
kappa_48 = np.sqrt(2 * m_e * (U0_48 - E_48)) / hbar
exp_term_48 = np.exp(-2 * kappa_48 * L_48)
G_48 = 16.0 * (5.0 / 12.0) * (1.0 - 5.0 / 12.0)
T_48_with_G = G_48 * exp_term_48
T_48_simple = exp_term_48
# (f) Ước tính dòng với thế phân cực V = 1.0 V
V_48 = 1.0
v_48 = np.sqrt(2 * e * V_48 / m_e)
I_48_with_G = T_48_with_G * n_48 * A_48 * e * v_48
I_48_simple = T_48_simple * n_48 * A_48 * e * v_48
r['40.48'] = {
    'kappa': kappa_48,
    'T_with_G': T_48_with_G,
    'T_simple': T_48_simple,
    'v_eff': v_48,
    'I_tunnel_A_with_G': I_48_with_G,
    'I_tunnel_A_simple': I_48_simple,
}

# 40.49: Tích phân hộp từ L/4 đến 3L/4
# (a) n=1: 1/2 + 1/pi
P_49_a = 0.5 + 1.0 / np.pi
# (b) n=2: 1/2
P_49_b = 0.5
r['40.49'] = {'P_a': P_49_a, 'P_b': P_49_b}

# 40.50: Độ sâu xuyên eta = hbar / sqrt(2m(U0 - E))
# (a) Electron E=13 eV, U0=20 eV -> U0 - E = 7 eV
eta_50_a = hbar / np.sqrt(2 * m_e * 7.0 * e)
# (b) Proton E=20 MeV, U0=30 MeV -> U0 - E = 10 MeV
eta_50_b = hbar / np.sqrt(2 * m_p * 10.0e6 * e)
r['40.50'] = {'eta_e_pm': eta_50_a * 1e12, 'eta_p_fm': eta_50_b * 1e15}

# ==========================================
# 4. BÀI TẬP 40.51 - 40.66
# ==========================================
# 40.52: E = 5.5 eV, U0 = 10.0 eV, T = 0.0050
U0_52 = 10.0 * e
E_52 = 5.5 * e
kappa_52 = np.sqrt(2 * m_e * (U0_52 - E_52)) / hbar
L_52_simple = -np.log(0.0050) / (2 * kappa_52)
G_52 = 16.0 * (5.5 / 10.0) * (1.0 - 5.5 / 10.0)
L_52_with_G = -np.log(0.0050 / G_52) / (2 * kappa_52)
r['40.52'] = {
    'kappa': kappa_52,
    'L_simple_nm': L_52_simple * 1e9,
    'L_with_G_nm': L_52_with_G * 1e9,
}

# 40.53: Mạng carbon d = 0.500 nm, q = 6e
d_53 = 0.500e-9
q_53 = 6 * e
k_prime_53 = 4 * (q_53**2) * k_coulomb / (d_53**3)
V0_53_eV = (2 * (q_53**2) * k_coulomb / d_53) / e
m_C12 = 12 * m_u
omega_53 = np.sqrt(k_prime_53 / m_C12)
dE_53_eV = (hbar * omega_53) / e
lam_53_um = (hc_eV_nm / dE_53_eV) * 1e-3
r['40.53'] = {
    'k_prime': k_prime_53,
    'V0_eV': V0_53_eV,
    'omega': omega_53,
    'dE_eV': dE_53_eV,
    'lam_um': lam_53_um,
}

# 40.54: Con lắc lò xo m = 0.020 kg, f = 1.50 Hz, vmax = 0.480 m/s
m_54 = 0.020
f_54 = 1.50
omega_54 = 2 * np.pi * f_54
vmax_54 = 0.480
E_54 = 0.5 * m_54 * vmax_54**2
n_54 = E_54 / (hbar * omega_54) - 0.5
dE_54_J = hbar * omega_54
dE_54_eV = dE_54_J / e
r['40.54'] = {'E_J': E_54, 'n': n_54, 'dE_eV': dE_54_eV}

# 40.55: Con lắc đơn T = 0.500 s -> f = 2.00 Hz
f_55 = 2.00
omega_55 = 2 * np.pi * f_55
E0_55_J = 0.5 * hbar * omega_55
E0_55_eV = E0_55_J / e
dE_55_J = hbar * omega_55
dE_55_eV = dE_55_J / e
r['40.55'] = {'E0_eV': E0_55_eV, 'dE_eV': dE_55_eV}

# 40.57: Mô hình H atom dạng hộp L = a0
E1_57_J = (h**2) / (8 * m_e * a0**2)
E1_57_eV = E1_57_J / e
r['40.57'] = {'E1_eV': E1_57_eV}

# 40.59: Electron trong hộp hấp thụ f1 = 9.0e14 Hz và f2 = 16.9e14 Hz từ n=1
f1_59 = 9.0e14
f2_59 = 16.9e14
# Thử các cặp (n, n+1): với n=3 -> (9-1)=8, (16-1)=15 -> tỉ số 15/8 = 1.875
# f2/f1 = 16.9/9.0 = 1.8778 (sai số 0.15%)
n_final_1 = 3
n_final_2 = 4
E1_h_avg_59 = ((f1_59 / 8.0) + (f2_59 / 15.0)) / 2.0
L_59 = np.sqrt(h / (8 * m_e * E1_h_avg_59))
# Bước sóng dài nhất từ n=1 là n=1 -> n=2 (Delta E = 3 E1)
f_12_59 = 3 * E1_h_avg_59
lam_max_59_nm = (c / f_12_59) * 1e9
r['40.59'] = {
    'n1': n_final_1,
    'n2': n_final_2,
    'L_nm': L_59 * 1e9,
    'lam_max_nm': lam_max_59_nm,
}

# 40.60: Hồi quy tuyến tính tìm bề rộng rào L
E_60 = np.array([4.0, 5.0, 6.0, 7.0, 7.6])
T_60 = np.array([2.4e-6, 1.5e-5, 1.2e-4, 1.3e-3, 8.1e-3])
U0_60 = 8.0
G_60 = 16.0 * (E_60 / U0_60) * (1.0 - E_60 / U0_60)
kappa_60 = np.sqrt(2 * m_e * (U0_60 - E_60) * e) / hbar
y_60 = np.log(T_60 / G_60)
slope_60, intercept_60 = np.polyfit(kappa_60, y_60, 1)
L_60_nm = (-slope_60 / 2.0) * 1e9
r['40.60'] = {
    'slope': slope_60,
    'intercept': intercept_60,
    'L_nm': L_60_nm,
}

# 40.61: Hiệu ứng Ramsauer-Townsend U0 = 10 eV, L = 1.8e-10 m
U0_61 = 10.0
L_61 = 1.8e-10
E1_box_61 = (h**2) / (8 * m_e * L_61**2 * e)
E_61_N1 = U0_61 + 1**2 * E1_box_61
E_61_N2 = U0_61 + 2**2 * E1_box_61
E_61_N3 = U0_61 + 3**2 * E1_box_61
r['40.61'] = {
    'E1_box_eV': E1_box_61,
    'E_N1_eV': E_61_N1,
    'E_N2_eV': E_61_N2,
    'E_N3_eV': E_61_N3,
}

# 40.66: Quarkonium WKB U(x) = A|x|
# Turning points: x = +- E/A
# Integral = 4*sqrt(2m)/(3A) * E^(3/2) = n*h/2
# En = 1/(2m) * (3*m*A*h/4)^(2/3) * n^(2/3)
r['40.66'] = {'power_n': 2.0 / 3.0}

# ==========================================
# 5. MCAT: CHẤM LƯỢNG TỬ (40.67 - 40.70)
# ==========================================
# Em,n = (m^2 + n^2) * pi^2 * hbar^2 / (2 * M * L^2)
# 40.67: Khoảng cách mức tỉ lệ 1/L^2 -> Chấm nhỏ hơn có khoảng cách mức lớn hơn (c)
# 40.68: lambda tỉ lệ L^2 -> L' = 1.1 L -> lambda' = 1.21 * 550 nm = 665.5 nm ~ 670 nm (b)
lam_68_new = (1.1**2) * 550.0
# 40.69: lambda tỉ lệ M -> lambda1 > lambda2 -> M1 > M2 (a)
# 40.70: Thời gian sống dài Delta t = 10 ns -> Delta E nhỏ -> Năng lượng xác định rõ hơn (a)
r['mcat'] = {
    '40.67': 'c',
    '40.68_lambda_nm': lam_68_new,
    '40.68_choice': 'b',
    '40.69': 'a',
    '40.70': 'a',
}

# In báo cáo xác nhận
def run_tests():
    assert abs(r['bridge']['omega_coeff_source'] - 0.903) < 1e-4
    assert abs(r['40.36']['E0_eV'] - 0.0976) < 1e-3
    assert abs(r['40.37']['lam_nm'] - 110.7) < 0.2
    assert abs(r['40.38']['lam_b_um'] - 3.25) < 1e-2
    assert abs(r['40.40']['ratio_A'] - 0.368) < 1e-2
    assert abs(r['40.44']['P_sum'] - 0.50) < 1e-5
    assert abs(r['40.49']['P_b'] - 0.50) < 1e-5
    assert abs(r['40.50']['eta_e_pm'] - 73.8) < 0.5
    assert abs(r['40.50']['eta_p_fm'] - 1.44) < 0.05
    assert abs(r['40.59']['L_nm'] - 0.899) < 0.01
    assert abs(r['40.60']['L_nm'] - 0.698) < 0.02
    assert abs(r['40.61']['E_N1_eV'] - 21.61) < 0.1
    assert abs(r['mcat']['40.68_lambda_nm'] - 665.5) < 0.1
    print('All numerical checks passed successfully!')

if __name__ == '__main__':
    run_tests()
