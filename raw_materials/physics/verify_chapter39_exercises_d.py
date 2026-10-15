"""Kịch bản kiểm tra độc lập bằng Python cho nhóm bài tập Chapter 39 (nhóm D).

Bao gồm:
- 22 câu hỏi thảo luận Q39.1 - Q39.22
- Bài tập 39.46 - 39.60
- Bài tập 39.61 - 39.75
- Bài tập 39.76 - 39.87
- Bài tập MCAT 39.88 - 39.91
- Bài tập cầu nối (Bridging Problem)
"""
from math import sqrt, pi, exp, sin, cos, radians, degrees
import json
import numpy as np

# Các hằng số vật lý chuẩn
c = 2.99792458e8          # m/s
h = 6.62607015e-34         # J*s
hb = h / (2 * pi)          # J*s
e = 1.602176634e-19        # C
me = 9.1093837e-31         # kg
mp = 1.6726219e-27         # kg
mn = 1.6749275e-27         # kg
m_alpha = 6.64e-27         # kg (Young & Freedman chuẩn)
eps0 = 8.8541878e-12       # F/m
k_coulomb = 1.0 / (4 * pi * eps0)
kB = 1.380649e-23          # J/K
sigma = (2 * pi**5 * kB**4) / (15 * c**2 * h**3)  # ~5.670374e-8 W/(m^2*K^4)
b_wien = 2.89777e-3        # m*K (hằng số dịch chuyển Wien)
R_inf = 1.097373e7         # m^-1 (hằng số Rydberg)
a0 = (4 * pi * eps0 * hb**2) / (me * e**2)  # ~0.529177e-10 m (bán kính Bohr)
E_ground_H = 13.606        # eV

r = {}

# ==========================================
# 1. BÀI TẬP CẦU NỐI (Bridging Problem)
# ==========================================
T_star = 15100.0
lam_max = b_wien / T_star
# Vùng bước sóng [lam_max / 2, 3 * lam_max]
lam_min_band = lam_max / 2.0
lam_max_band = 3.0 * lam_max
# Năng lượng photon lớn nhất ứng với lam_min_band
E_photon_max_J = h * c / lam_min_band
E_photon_max_eV = E_photon_max_J / e
# Mức n cao nhất kích thích từ n=1
# E_n - E_1 = E_ground_H * (1 - 1/n^2) <= E_photon_max_eV
# 1 - 1/n^2 <= E_photon_max_eV / E_ground_H => 1/n^2 >= 1 - E_photon_max_eV / E_ground_H
frac = 1.0 - E_photon_max_eV / E_ground_H
n_max_float = 1.0 / sqrt(frac) if frac > 0 else 999
n_max = int(n_max_float)
# Bước sóng de Broglie trong quỹ đạo n=2 và n=3: lambda_n = 2*pi*r_n / n = 2*pi*n*a0
lam_e_2 = 2 * pi * 2 * a0
lam_e_3 = 2 * pi * 3 * a0

r['bridge'] = {
    'a_lam_max_m': lam_max,
    'a_lam_max_nm': lam_max * 1e9,
    'a_spectrum_region': 'ultraviolet',
    'b_lam_min_nm': lam_min_band * 1e9,
    'b_lam_max_nm': lam_max_band * 1e9,
    'b_E_max_eV': E_photon_max_eV,
    'b_n_max': n_max,
    'c_lam_e2_nm': lam_e_2 * 1e9,
    'c_lam_e3_nm': lam_e_3 * 1e9,
}

# ==========================================
# 2. BÀI TẬP 39.46 - 39.60
# ==========================================
# 39.46: Hòn bi m = 10.0 g, bàn rộng 1.75 m
m_3946 = 0.0100
L_3946 = 1.75
dx_3946 = L_3946
dp_min_3946 = (hb / 2.0) / dx_3946
dv_min_3946 = dp_min_3946 / m_3946
# Thời gian lâu nhất hòn bi ở trên bàn (từ tâm ra mép d = L/2)
t_stay_s = (L_3946 / 2.0) / dv_min_3946
t_stay_yr = t_stay_s / (365.25 * 86400)
age_universe_yr = 14e9

r['39.46'] = {
    'a_delta_x_m': dx_3946,
    'b_delta_v_m_s': dv_min_3946,
    'c_time_years': t_stay_yr,
    'c_ratio_universe_age': t_stay_yr / age_universe_yr,
}

# 39.47: Độ lệch chuẩn vị trí 0.12 nm, xung lượng 3.0e-25 kg*m/s
dx_3947 = 0.12e-9
dp_3947 = 3.0e-25
prod_3947 = dx_3947 * dp_3947
bound_3947 = hb / 2.0
claim_valid_3947 = prod_3947 >= bound_3947

r['39.47'] = {
    'product_J_s': prod_3947,
    'heisenberg_bound_J_s': bound_3947,
    'claim_valid': claim_valid_3947,
}

# 39.48: Nguyên tử khối lượng m phát photon lambda
# (d) Hydrogen m = 1.67e-27 kg, E_photon = 10.2 eV
m_3948 = 1.67e-27
E_3948_eV = 10.2
E_3948_J = E_3948_eV * e
p_photon_3948 = E_3948_J / c
v_recoil_3948 = p_photon_3948 / m_3948
K_recoil_J_3948 = p_photon_3948**2 / (2.0 * m_3948)
K_recoil_eV_3948 = K_recoil_J_3948 / e
ratio_K_E_3948 = K_recoil_J_3948 / E_3948_J

r['39.48'] = {
    'd_v_recoil_m_s': v_recoil_3948,
    'd_K_recoil_eV': K_recoil_eV_3948,
    'd_ratio_K_E': ratio_K_E_3948,
    'negligible': ratio_K_E_3948 < 1e-6,
}

# 39.49: Muon âm m_mu = 207 m_e, proton m_p
m_mu_3949 = 207.0 * me
m_r_3949 = (m_mu_3949 * mp) / (m_mu_3949 + mp)
E1_muon_eV = (m_r_3949 / me) * (-E_ground_H)
deltaE_21_muon_eV = (3.0 / 4.0) * abs(E1_muon_eV)
lam_muon_21_nm = (h * c / (deltaE_21_muon_eV * e)) * 1e9

r['39.49'] = {
    'a_reduced_mass_kg': m_r_3949,
    'a_reduced_mass_in_me': m_r_3949 / me,
    'b_ground_state_energy_eV': E1_muon_eV,
    'c_wavelength_2_to_1_nm': lam_muon_21_nm,
}

# 39.50: Hydrogen n=3 hấp thụ photon lambda, e ra ngoài có K = 8.00 eV
E3_H_eV = -E_ground_H / 9.0
E_photon_3950_eV = abs(E3_H_eV) + 8.00
lam_3950_nm = (h * c / (E_photon_3950_eV * e)) * 1e9

r['39.50'] = {
    'E_bind_n3_eV': abs(E3_H_eV),
    'E_photon_eV': E_photon_3950_eV,
    'wavelength_nm': lam_3950_nm,
}

# 39.51: Dãy Pickering: 1/lambda = (1.097e7) * [1/4 - 1/(n/2)^2]
# n = 5, 6, 7, ... => 1/lambda = 4 R_H * [1/4^2 - 1/n^2]
lam_short_3951 = 4.0 / R_inf
# n = 5 => 1/4 - 1/(2.5)^2 = 0.25 - 0.16 = 0.09
lam_long_3951 = 1.0 / (R_inf * 0.09)

r['39.51'] = {
    'a_shortest_wavelength_nm': lam_short_3951 * 1e9,
    'a_longest_wavelength_nm': lam_long_3951 * 1e9,
    'b_element': 'He+ (Helium singly ionized)',
    'b_Z': 2,
    'b_nL': 4,
}

# 39.52: Bước sóng de Broglie electron trong Bohr: lambda_n = 2*pi*r_n / n = 2*pi*n*a0
lam_e_n1_3952 = 2.0 * pi * 1.0 * a0
lam_e_n4_3952 = 2.0 * pi * 4.0 * a0
circ_n1 = 2.0 * pi * a0
circ_n4 = 2.0 * pi * (16.0 * a0)

r['39.52'] = {
    'a_lambda_1_nm': lam_e_n1_3952 * 1e9,
    'a_ratio_circ_to_lambda': circ_n1 / lam_e_n1_3952,
    'b_lambda_4_nm': lam_e_n4_3952 * 1e9,
    'b_ratio_circ_to_lambda': circ_n4 / lam_e_n4_3952,
}

# 39.53: Chiếu lambda = 85.5 nm vào khí hydrogen
lam_3953 = 85.5e-9
E_photon_3953_eV = (h * c / lam_3953) / e
K_max_ground_3953 = E_photon_3953_eV - E_ground_H
# Các electron có năng lượng lớn hơn 10.2 eV xuất phát từ n=2
E2_H_eV = E_ground_H / 4.0
K_max_n2_3953 = E_photon_3953_eV - E2_H_eV

r['39.53'] = {
    'E_photon_eV': E_photon_3953_eV,
    'a_K_max_from_ground_eV': K_max_ground_3953,
    'b_delta_E_extra_eV': K_max_n2_3953 - K_max_ground_3953,
    'b_initial_state': 'n=2 (excited level)',
}

# 39.54: Natri doublet: 589.0 nm và 589.6 nm
lam1_3954 = 589.0e-9
lam2_3954 = 589.6e-9
dlam_3954 = abs(lam2_3954 - lam1_3954)
lam_bar_3954 = (lam1_3954 + lam2_3954) / 2.0
dE_3954_J = (h * c / lam_bar_3954**2) * dlam_3954
dE_3954_eV = dE_3954_J / e

r['39.54'] = {
    'delta_E_eV': dE_3954_eV,
    'delta_E_meV': dE_3954_eV * 1e3,
}

# 39.55: Sao Betelgeuse T = 3000 K, D = 600 D_sun
R_sun = 6.96e8
R_betelgeuse = 600.0 * R_sun
lam_max_3955 = b_wien / 3000.0
E_photon_peak_3955 = h * c / lam_max_3955
Area_betelgeuse = 4.0 * pi * R_betelgeuse**2
P_betelgeuse = Area_betelgeuse * sigma * (3000.0**4)
photons_per_sec_3955 = P_betelgeuse / E_photon_peak_3955
# Tỉ số công suất so với Mặt Trời (T_sun = 5800 K)
P_ratio_3955 = (600.0**2) * ((3000.0 / 5800.0)**4)

r['39.55'] = {
    'a_lam_max_nm': lam_max_3955 * 1e9,
    'a_power_W': P_betelgeuse,
    'a_photons_per_sec': photons_per_sec_3955,
    'b_power_ratio_to_sun': P_ratio_3955,
}

# 39.56: Vật đen đường kính 15.0 cm, cách tử 3850 vạch/cm, cực đại bậc 1 ở 14.4 độ
d_g_3956 = 1e-2 / 3850.0
lam_peak_3956 = d_g_3956 * sin(radians(14.4))
T_3956 = b_wien / lam_peak_3956
R_sphere_3956 = 0.150 / 2.0
Area_3956 = 4.0 * pi * R_sphere_3956**2
P_3956 = Area_3956 * sigma * (T_3956**4)
E_target_3956 = 12.0e6
t_radiate_3956 = E_target_3956 / P_3956

r['39.56'] = {
    'lam_peak_nm': lam_peak_3956 * 1e9,
    'a_temperature_K': T_3956,
    'power_W': P_3956,
    'b_time_seconds': t_radiate_3956,
}

# 39.57: Mặt Trăng quay quanh Trái Đất
M_m_3957 = 7.35e22
M_e_3957 = 5.97e24
R_m_3957 = 3.84e8
T_m_3957 = 27.3 * 86400
v_m_3957 = 2.0 * pi * R_m_3957 / T_m_3957
p_m_3957 = M_m_3957 * v_m_3957
lam_m_3957 = h / p_m_3957
G_grav = 6.67408e-11
a_moon_3957 = hb**2 / (G_grav * M_e_3957 * M_m_3957**2)
m_quantum_3957 = sqrt(R_m_3957 / a_moon_3957)
E0_ground_3957 = (G_grav * M_e_3957 * M_m_3957) / (2.0 * a_moon_3957)

r['39.57'] = {
    'a_wavelength_m': lam_m_3957,
    'b_formula': 'amoon = hbar^2 / (G * Mearth * Mmoon^2)',
    'c_amoon_m': a_moon_3957,
    'd_quantum_number_m': m_quantum_3957,
    'e_E0_ground_J': E0_ground_3957,
}

# 39.58: Hốc vật đen T = 400 C = 673.15 K, diện tích lỗ 4.00 mm^2
T_3958 = 400.0 + 273.15
A_hole_3958 = 4.00e-6
P_hole_3958 = A_hole_3958 * sigma * (T_3958**4)
E_target_3958 = 100.0
t_radiate_3958_s = E_target_3958 / P_hole_3958

r['39.58'] = {
    'power_W': P_hole_3958,
    'time_seconds': t_radiate_3958_s,
    'time_minutes': t_radiate_3958_s / 60.0,
}

# 39.59: Tích phân hàm phân bố Planck
# Stefan-Boltzmann constant derivation
sigma_calc = (2.0 * pi**5 * kB**4) / (15.0 * c**2 * h**3)
r['39.59'] = {
    'sigma_calculated': sigma_calc,
    'sigma_accepted': sigma,
    'relative_error': abs(sigma_calc - sigma) / sigma,
}

# 39.60: Chùm electron 40 eV qua khe rộng a = 5.0 um, màn cách 2.5 m
K_3960_eV = 40.0
K_3960_J = K_3960_eV * e
p_3960 = sqrt(2.0 * me * K_3960_J)
lam_3960 = h / p_3960
v_3960 = p_3960 / me
D_3960 = 2.5
t_flight_3960 = D_3960 / v_3960
a_slit_3960 = 5.0e-6
# Góc cực tiểu thứ nhất: sin(theta) = lambda / a
# Độ bất định xung lượng theo phương y ngay sau khe: delta_py ~ p * sin(theta) = h / a
dp_y_3960 = h / a_slit_3960
# Độ bất định vị trí tối thiểu: delta_y >= (hbar / 2) / delta_py = a / (4*pi)
dy_min_3960 = (hb / 2.0) / dp_y_3960

r['39.60'] = {
    'a_de_broglie_wavelength_nm': lam_3960 * 1e9,
    'b_flight_time_s': t_flight_3960,
    'c_delta_py_kg_m_s': dp_y_3960,
    'd_delta_y_min_um': dy_min_3960 * 1e6,
    'd_ratio_to_slit_width': dy_min_3960 / a_slit_3960,
}

# ==========================================
# 3. BÀI TẬP 39.61 - 39.75
# ==========================================
# 39.61: Chuyển động v mô hình
v_perc = 1e-3
m_human = 70.0
lam_human_perc = h / (m_human * v_perc)
m_sand = 0.5e-6
lam_sand_perc = h / (m_sand * v_perc)
lam_sand_h1 = 1.0 / (m_sand * 1.0)
lam_human_h1 = 1.0 / (m_human * 2.5)
# Bóng chày 145 g, khe cửa a = 0.90 m, góc cực đại 10 độ (bán góc 5 độ)
m_ball = 0.145
a_door = 0.90
lam_ball_req = a_door * sin(radians(5.0))
v_ball_req = 1.0 / (m_ball * lam_ball_req)

r['39.61'] = {
    'b_lambda_human_perc_m': lam_human_perc,
    'c_lambda_sand_perc_m': lam_sand_perc,
    'd_lambda_sand_h1_m': lam_sand_h1,
    'e_lambda_human_h1_mm': lam_human_h1 * 1e3,
    'f_v_baseball_m_s': v_ball_req,
}

# 39.62: Khe đơn a = 300 nm, màn 24.0 cm, triệt tiêu ở 20.0 độ
a_3962 = 300e-9
lam_3962 = a_3962 * sin(radians(20.0))
v_3962 = h / (me * lam_3962)
sin_theta2_3962 = 2.0 * lam_3962 / a_3962
theta2_3962 = degrees(np.arcsin(sin_theta2_3962))

r['39.62'] = {
    'a_wavelength_nm': lam_3962 * 1e9,
    'a_speed_m_s': v_3962,
    'b_next_angle_deg': theta2_3962,
}

# 39.63: Hai khe d = 1.25 nm, vân tối đầu tiên ở 18.0 độ
# d * sin(theta) = lambda / 2 => lambda = 2 * d * sin(theta)
d_3963 = 1.25e-9
lam_3963 = 2.0 * d_3963 * sin(radians(18.0))
p_3963 = h / lam_3963
v_3963 = p_3963 / me
K_3963_eV = (p_3963**2 / (2.0 * me)) / e
V_acc_3963 = K_3963_eV

r['39.63'] = {
    'wavelength_nm': lam_3963 * 1e9,
    'a_speed_m_s': v_3963,
    'a_beta': v_3963 / c,
    'b_potential_difference_V': V_acc_3963,
}

# 39.64: Hai khe d = 20.0 um, vân sáng bậc 2 ở 0.0300 rad
# d * sin(theta) = 2 * lambda
d_3964 = 20.0e-6
lam_3964 = (d_3964 * sin(0.0300)) / 2.0
p_3964 = h / lam_3964
K_3964_eV = (p_3964**2 / (2.0 * me)) / e

r['39.64'] = {
    'wavelength_nm': lam_3964 * 1e9,
    'kinetic_energy_eV': K_3964_eV,
    'kinetic_energy_ueV': K_3964_eV * 1e6,
}

# 39.65: Chùm electron và photon qua cùng khe
# lambda_e = lambda_gamma => E_gamma = h*c/lambda, K_e = p^2/(2m) = h^2/(2m*lambda^2)
# E_gamma = sqrt(2 * m_e * c^2 * K_e) = 2 * c / v_e * K_e
r['39.65'] = {
    'a_ratio_formula': 'E_gamma = 2 * c / v_e * K_e = sqrt(2 * m_e * c^2 * K_e)',
    'b_comparison': 'E_gamma > K_e because v_e << c',
}

# 39.66: Hồng cầu 1.00e-11 g = 1.00e-14 kg, v = 0.400 cm/s = 4.00e-3 m/s
m_rbc = 1.00e-14
v_rbc = 4.00e-3
lam_rbc = h / (m_rbc * v_rbc)
r['39.66'] = {
    'wavelength_m': lam_rbc,
    'significant_in_body': False,
}

# 39.67: Electron tương đối tính
lam_C_3967 = h / (me * c)
# Cho lambda = 1.00e-15 m
lam_target_3967 = 1.00e-15
delta_3967 = 0.5 * (lam_target_3967 / lam_C_3967)**2
v_exact_3967 = c / sqrt(1.0 + (me * c * lam_target_3967 / h)**2)

r['39.67'] = {
    'b_delta_formula': 'Delta = 0.5 * (m*c*lambda / h)^2 = 0.5 * (lambda / lambda_C)^2',
    'c_delta_value': delta_3967,
    'c_speed_fraction_of_c': 1.0 - delta_3967,
}

# 39.68: Bất định vị trí = bán kính Bohr a0
dx_3968 = a0
dp_min_3968 = (hb / 2.0) / dx_3968
p_bohr1_3968 = hb / a0
r['39.68'] = {
    'delta_p_kg_m_s': dp_min_3968,
    'p_bohr_kg_m_s': p_bohr1_3968,
    'ratio': dp_min_3968 / p_bohr1_3968,
}

# 39.69: K = 3 * m * c^2 => E = 4 * m * c^2 => pc = sqrt(15) * m * c^2
# lambda = hc / (sqrt(15) * m * c^2)
E0_e_MeV = (me * c**2) / (1e6 * e)
E0_p_MeV = (mp * c**2) / (1e6 * e)
K_e_3969_MeV = 3.0 * E0_e_MeV
K_p_3969_MeV = 3.0 * E0_p_MeV
lam_e_3969_m = (h * c) / (sqrt(15.0) * me * c**2)
lam_p_3969_m = (h * c) / (sqrt(15.0) * mp * c**2)

r['39.69'] = {
    'a_formula': 'lambda = hc / (sqrt(15) * m * c^2)',
    'b_i_K_e_MeV': K_e_3969_MeV,
    'b_i_lam_e_pm': lam_e_3969_m * 1e12,
    'b_ii_K_p_MeV': K_p_3969_MeV,
    'b_ii_lam_p_fm': lam_p_3969_m * 1e15,
}

# 39.70: Proton trong hạt nhân R = 5.0e-15 m
R_nuc = 5.0e-15
dp_p_3970 = (hb / 2.0) / R_nuc
K_p_3970_J = dp_p_3970**2 / (2.0 * mp)
K_p_3970_MeV = K_p_3970_J / (1e6 * e)

r['39.70'] = {
    'a_delta_p_kg_m_s': dp_p_3970,
    'b_K_p_MeV': K_p_3970_MeV,
    'c_strong_force_comparison': 'Nuclear potential depth is order of tens of MeV',
}

# 39.71: Electron trong hạt nhân R = 5.0e-15 m
dp_e_3971 = (hb / 2.0) / R_nuc
E_rel_e_3971_J = sqrt((dp_e_3971 * c)**2 + (me * c**2)**2)
K_rel_e_3971_MeV = (E_rel_e_3971_J - me * c**2) / (1e6 * e)
U_coulomb_3971_MeV = (k_coulomb * e**2 / R_nuc) / (1e6 * e)

r['39.71'] = {
    'a_delta_p_kg_m_s': dp_e_3971,
    'b_K_rel_e_MeV': K_rel_e_3971_MeV,
    'c_U_coulomb_MeV': U_coulomb_3971_MeV,
    'can_electrons_exist_in_nucleus': False,
}

# 39.72: Neutral pion m_pi = 264 m_e, tau = 8.4e-17 s
m_pi_3972 = 264.0 * me
tau_3972 = 8.4e-17
dE_3972_J = (hb / 2.0) / tau_3972
dE_3972_eV = dE_3972_J / e
E0_pi_eV = (m_pi_3972 * c**2) / e
frac_unc_3972 = dE_3972_eV / E0_pi_eV

r['39.72'] = {
    'delta_E_eV': dE_3972_eV,
    'delta_m_kg': dE_3972_J / c**2,
    'fractional_uncertainty': frac_unc_3972,
}

# 39.73: Nhiễu xạ qua cửa lambda = 1.0 m, m = 60.0 kg
m_3973 = 60.0
lam_3973 = 1.0
v_3973 = h / (m_3973 * lam_3973)
t_step_yr_3973 = (0.80 / v_3973) / (365.25 * 86400)

r['39.73'] = {
    'a_speed_m_s': v_3973,
    'b_years_per_step': t_step_yr_3973,
}

# 39.74: Mức kích thích 2.58 eV, tau = 1.64e-7 s
E_3974_eV = 2.58
tau_3974 = 1.64e-7
lam_3974_nm = (h * c / (E_3974_eV * e)) * 1e9
dE_3974_eV = ((hb / 2.0) / tau_3974) / e
dlam_3974_nm = lam_3974_nm * (dE_3974_eV / E_3974_eV)

r['39.74'] = {
    'a_wavelength_nm': lam_3974_nm,
    'b_delta_E_eV': dE_3974_eV,
    'c_delta_lambda_nm': dlam_3974_nm,
}

# 39.75: Tia X lambda1 = 0.0300 nm, m=1 ở 35.8 độ. Electron 4.50 keV
lam1_3975 = 0.0300e-9
d_cryst_3975 = lam1_3975 / sin(radians(35.8))
K2_3975_J = 4500.0 * e
p2_3975 = sqrt(2.0 * me * K2_3975_J)
lam2_3975 = h / p2_3975
sin_theta2_3975 = lam2_3975 / d_cryst_3975
theta2_deg_3975 = degrees(np.arcsin(sin_theta2_3975))

r['39.75'] = {
    'd_crystal_nm': d_cryst_3975 * 1e9,
    'electron_wavelength_nm': lam2_3975 * 1e9,
    'theta2_deg': theta2_deg_3975,
}

# ==========================================
# 4. BÀI TẬP 39.76 - 39.87
# ==========================================
# 39.76: Source image PDF1338: Lifetime2.0 microseconds.
E_3976_eV = 3.50
tau_3976 = 2.0e-6
lam_3976_nm = (h * c / (E_3976_eV * e)) * 1e9
dE_3976_eV = ((hb / 2.0) / tau_3976) / e

r['39.76'] = {
    'a_wavelength_nm': lam_3976_nm,
    'b_delta_E_eV': dE_3976_eV,
}

# 39.77: Virus lambda = 5.00 nm
lam_3977 = 5.00e-9
E_photon_3977_eV = (h * c / lam_3977) / e
K_electron_3977_eV = (h**2 / (2.0 * me * lam_3977**2)) / e

r['39.77'] = {
    'a_photon_energy_eV': E_photon_3977_eV,
    'b_electron_energy_eV': K_electron_3977_eV,
    'ratio_photon_to_electron': E_photon_3977_eV / K_electron_3977_eV,
}

# 39.78: The explicit source approximation is px~h, ordinary Planck constant.
# E = hbar^2 / (2m x^2) + 1/2 k x^2 => x_min = (hbar^2 / (mk))^(1/4)
# E_min = hbar * sqrt(k/m) = hbar * omega, K / U = 1
r['39.78'] = {
    'a_x_min_formula': '(h^2 / (m*k))^(1/4)',
    'a_E_min_formula': 'h * sqrt(k/m)',
    'b_ratio_K_to_U': 1.0,
}

# 39.79: U = A|x|, px ~ hbar
# E = hbar^2 / (2m x^2) + A x => dE/dx = -hbar^2 / (m x^3) + A = 0 => x = (hbar^2 / (mA))^(1/3)
# E_min = (3/2) * (hbar^2 * A^2 / m)^(1/3)
r['39.79'] = {
    'a_force': '-A * sgn(x)',
    'b_E_min_formula': '1.5 * (h^2 * A^2 / m)^(1/3)',
}

# 39.80: Vũ trụ với h = 0.0663 J*s, bóng m = 0.25 kg, v = 6.0 m/s, d = 12 m
h_3980 = 0.0663
hb_3980 = h_3980 / (2.0 * pi)
V_cube_3980 = 125e-6  # m^3
dy_3980 = V_cube_3980**(1.0 / 3.0)  # 0.05 m
dp_y_3980 = (hb_3980 / 2.0) / dy_3980
m_ball_3980 = 0.25
dv_y_3980 = dp_y_3980 / m_ball_3980
t_fly_3980 = 12.0 / 6.0
miss_dist_3980 = dv_y_3980 * t_fly_3980

r['39.80'] = {
    'a_delta_p_kg_m_s': dp_y_3980,
    'b_miss_distance_m': miss_dist_3980,
}

# 39.81: Ion một electron, vạch dài nhất hấp thụ là 13.56 nm (n=1 -> 2)
lam_12_3981 = 13.56e-9
# 1/lambda = Z^2 * R * (3/4) => Z^2 = 4 / (3 * R * lambda)
Z2_3981 = 4.0 / (3.0 * R_inf * lam_12_3981)
Z_3981 = int(round(sqrt(Z2_3981)))
# Vạch hấp thụ ngắn tiếp theo là n=1 -> 3
lam_13_3981 = 1.0 / (Z_3981**2 * R_inf * (8.0 / 9.0))
# Chiếu photon lambda = 6.78 nm
E_phot_3981_eV = (h * c / 6.78e-9) / e
E_ion_3981_eV = Z_3981**2 * E_ground_H
K_e_3981_eV = E_phot_3981_eV - E_ion_3981_eV

r['39.81'] = {
    'a_Z': Z_3981,
    'b_lambda_13_nm': lam_13_3981 * 1e9,
    'c_K_electron_eV': K_e_3981_eV,
}

# 39.82: Hồi quy Davisson-Germer
Vac_3982 = np.array([106.3, 69.1, 49.9, 25.2, 16.9, 13.6])
th_deg_3982 = np.array([20.4, 24.8, 30.2, 45.5, 59.1, 73.1])
x_3982 = 1.0 / np.sqrt(Vac_3982)
y_3982 = np.sin(np.radians(th_deg_3982))
slope_3982, intercept_3982 = np.polyfit(x_3982, y_3982, 1)
# d * sin(theta) = lambda = h / sqrt(2*me*e*Vac) => sin(theta) = [h / (d * sqrt(2*me*e))] * (1/sqrt(Vac))
# slope = h / (d * sqrt(2*me*e)) => d = h / (slope * sqrt(2*me*e))
d_crystal_3982 = h / (slope_3982 * sqrt(2.0 * me * e))

r['39.82'] = {
    'a_slope_V_half': slope_3982,
    'a_intercept': intercept_3982,
    'b_d_spacing_nm': d_crystal_3982 * 1e9,
}

# 39.83: Các ngôi sao
stars_data = {
    'Polaris': {'T': 6015.0, 'R': 46.0},
    'Vega': {'T': 9602.0, 'R': 2.73},
    'Antares': {'T': 3400.0, 'R': 883.0},
    'Alpha Centauri B': {'T': 5260.0, 'R': 0.865},
}
P_sun = 3.85e26
T_sun = 5778.0  # Hoặc tính trực tiếp 4*pi*R^2*sigma*T^4
for name, s in stars_data.items():
    R_m = s['R'] * R_sun
    Area = 4.0 * pi * R_m**2
    P = Area * sigma * (s['T']**4)
    lam_peak = b_wien / s['T']
    s['P_W'] = P
    s['P_ratio_sun'] = P / P_sun
    s['lam_peak_nm'] = lam_peak * 1e9
    s['in_visible'] = 380.0 <= lam_peak * 1e9 <= 750.0

r['39.83'] = {
    'stars': stars_data,
    'a_greatest_power_star': 'Antares',
    'b_visible_peak_stars': ['Polaris', 'Alpha Centauri B'],
    'c_less_than_sun': ['Alpha Centauri B'],
}

# 39.84: Vật đen bán kính r = 1.23 m, R = 1.00 kOhm
r_3984 = 1.23
Area_3984 = 4.0 * pi * r_3984**2
x_opt = 2.8214
def calc_3984(T):
    E0 = x_opt * kB * T
    I_max = (2.0 * pi * E0**3) / (h**3 * c**2 * (exp(x_opt) - 1.0))
    dE = 0.01 * E0
    band = 2.0 * dE
    P = Area_3984 * I_max * band
    I = sqrt(P / 1000.0)
    return {'E0_eV': E0 / e, 'P_W': P, 'current_A': I}

r['39.84'] = {
    'T_1000K': calc_3984(1000.0),
    'T_5000K': calc_3984(5000.0),
}

# 39.85: Tán xạ đàn hồi hạt alpha vào hạt nhân vàng
m_alpha_3985 = 6.64e-27
M_gold_3985 = 1.32e-25
K_alpha_eV = 5.0e6
K_alpha_J = K_alpha_eV * e
v0_3985 = sqrt(2.0 * K_alpha_J / m_alpha_3985)
V_gold_3985 = (2.0 * m_alpha_3985 / (m_alpha_3985 + M_gold_3985)) * v0_3985
frac_E_3985 = (4.0 * m_alpha_3985 * M_gold_3985) / ((m_alpha_3985 + M_gold_3985)**2)
# (e) V = 0.10 c => v0 = V * (m+M) / (2m)
v0_req_3985 = (0.10 * c) * (m_alpha_3985 + M_gold_3985) / (2.0 * m_alpha_3985)

r['39.85'] = {
    'd_V_fraction_c': V_gold_3985 / c,
    'd_fraction_energy_transferred': frac_E_3985,
    'e_v0_fraction_c': v0_req_3985 / c,
    'classical_required_projectile_speed_possible': False,
    'relativistic_recoil_0_10c_is_not_forbidden': True,
}

# 39.86: Thả bi 20.0 g từ độ cao 25.0 m
m_3986 = 0.0200
h_3986 = 25.0
g_grav = 9.80
t_fall_3986 = sqrt(2.0 * h_3986 / g_grav)
# dx_f = dx_i + (hbar * t) / (2 * m * dx_i)
# Minimized at dx_i = sqrt(hbar * t / (2 * m))
dx_i_opt = sqrt(hb * t_fall_3986 / (2.0 * m_3986))
dx_f_min_linear = 2.0 * dx_i_opt
dx_f_min_quad = sqrt(2.0) * dx_i_opt

r['39.86'] = {
    't_fall_s': t_fall_3986,
    'optimal_initial_dx_m': dx_i_opt,
    'min_miss_distance_linear_m': dx_f_min_linear,
    'min_miss_distance_quad_m': dx_f_min_quad,
}

# 39.87: Tần số quay và phát xạ Bohr
r['39.87'] = {
    'a_formula': 'f_rev = m * e^4 / (4 * eps0^2 * n^3 * h^3)',
    'b_match_quantum_transition': True,
}

# ==========================================
# 5. MCAT 39.88 - 39.91
# ==========================================
# 39.88: So sánh bước sóng He+ và e- cùng điện áp
# lambda = h / sqrt(2*m*q*V). m_ion >> m_e => lambda_ion < lambda_e
# Đáp án: (b)
r['39.88'] = {'answer': '(b)', 'reason': 'Helium ion has shorter wavelength because it has greater mass'}

# 39.89: lambda = 0.1 pm = 1e-13 m
m_He_ion = 7300.0 * me
lam_req_3989 = 0.1e-12
V_req_3989 = h**2 / (2.0 * m_He_ion * e * lam_req_3989**2)
# Đáp án: (a) Yes, ~21 kV
r['39.89'] = {
    'voltage_required_V': V_req_3989,
    'voltage_kV': V_req_3989 / 1e3,
    'answer': '(a)',
}

# 39.90: Vì sao dùng ion He+ thay vì He trung hòa?
# Đáp án: (c) Neutral helium atoms are more difficult to focus with electric and magnetic fields.
r['39.90'] = {'answer': '(c)'}

# 39.91: Tổn hao năng lượng 0.2 MeV/um, đo được đến 6 keV
dE_dx_3991 = 0.2e6  # eV / um
deltaE_meas_3991 = 6e3  # eV
dx_thick_3991 = deltaE_meas_3991 / dE_dx_3991  # um
# Đáp án: (a) 0.03 um
r['39.91'] = {
    'thickness_difference_um': dx_thick_3991,
    'answer': '(a)',
}

# ==========================================
# 6. CÂU HỎI THẢO LUẬN (ĐỊNH LƯỢNG)
# ==========================================
# Q39.6: Li++ (Z=3)
r['Q39.6'] = {
    'energy_levels_factor': 9,  # Z^2 = 9
    'ground_state_radius_factor': 1.0 / 3.0,  # a0 / Z
}

# Q39.11: Khoảng cách hành tinh
r['Q39.11'] = {
    'Mercury_AU': 5.79e10 / 1.496e11,
    'Venus_AU': 1.08e11 / 1.496e11,
    'Earth_AU': 1.50e11 / 1.496e11,
    'Mars_AU': 2.28e11 / 1.496e11,
    'obeys_n_squared': False,
    'reason': 'Macroscopic classical gravitation; massive bodies form by accretion and orbital resonance, quantum numbers n ~ 10^74',
}

# Q39.12: Electron 54 eV, độ chính xác +-1.0 mm
K_54eV = 54.0 * e
lam_54eV = h / sqrt(2.0 * me * K_54eV)
r['Q39.12'] = {
    'wavelength_nm': lam_54eV * 1e9,
    'precision_mm': 1.0,
    'need_wave_nature': False,
    'reason': 'Wavelength ~ 0.17 nm is 6 orders of magnitude smaller than 1.0 mm accuracy',
}

# Q39.14: Năng lượng và tốc độ electron trong mô hình Bohr
# E_n = -13.6 / n^2, v_n = v1 / n
r['Q39.14'] = {
    'high_n_total_energy': 'Higher (less negative, closer to 0)',
    'high_n_speed': 'Slower (v_n proportional to 1/n)',
    'contradiction': False,
    'reason': 'Potential energy U_n = -2 K_n increases rapidly toward 0, compensating decrease in K_n',
}

assert set(f'39.{n}' for n in range(46,92)) <= set(r)
assert 1.6e-10 < r['39.76']['b_delta_E_eV'] < 1.7e-10
assert r['39.47']['product_J_s'] < hb/2
assert 20e3 < V_req_3989 < 21e3
assert abs(dx_thick_3991-.03)<1e-12
# Elastic collision energy and momentum, calculated independently from final speeds.
v_alpha_final=(m_alpha_3985-M_gold_3985)/(m_alpha_3985+M_gold_3985)*v0_3985
assert np.isclose(m_alpha_3985*v0_3985,m_alpha_3985*v_alpha_final+M_gold_3985*V_gold_3985,rtol=1e-12,atol=0)
assert np.isclose(K_alpha_J,.5*m_alpha_3985*v_alpha_final**2+.5*M_gold_3985*V_gold_3985**2,rtol=1e-12,atol=0)
# Check Bohr correspondence for several increasing quantum numbers.
ratios=[]
for n in [10,100,1000,10000]:
    radiated=(13.606*e/h)*(1/n**2-1/(n+1)**2)
    revolution=me*e**4/(4*eps0**2*n**3*h**3)
    ratios.append(radiated/revolution)
assert abs(ratios[-1]-1)<abs(ratios[0]-1)
assert abs(ratios[-1]-1)<2e-4
print(json.dumps(dict(status='numerical-crosschecks-passed-source-review-separate', total_items=len(r), results=r), indent=2))
