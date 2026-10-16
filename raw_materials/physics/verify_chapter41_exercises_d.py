"""Kịch bản kiểm tra độc lập bằng Python cho nhóm bài tập Chapter 41 (nhóm D).

Bao gồm 52 lời giải hoàn chỉnh:
- 16 bài tập mục 41.23 - 41.38
- 16 bài tập mở rộng 41.39 - 41.54
- 15 bài toán và thử thách 41.55 - 41.69 (gồm 3 challenge 41.67 - 41.69)
- 4 bài trắc nghiệm MCAT 41.70 - 41.73 kèm đoạn văn Atoms of Unusual Size
- 1 Bài tập cầu nối (Bridging Problem: A Many-Electron Atom in a Box) kèm 8 bước Solution Guide
"""
import numpy as np
import scipy.constants as const
from scipy.optimize import curve_fit

# Các hằng số vật lý chuẩn CODATA / Young & Freedman 15th Edition
c = const.c                     # m/s
h = const.h                     # J*s
hbar = const.hbar               # J*s
e = const.e                     # C
m_e = const.m_e                 # kg
m_p = const.m_p                 # kg
eps0 = const.epsilon_0           # F/m
mu0 = const.mu_0                # N/A^2 (H/m)
mu_B = const.value('Bohr magneton') # J/T (~9.274e-24 J/T)
mu_B_eV = mu_B / e              # eV/T (~5.788e-5 eV/T)
a0 = const.value('Bohr radius') # m (~5.29177e-11 m)
R_inf = const.value('Rydberg constant')
E_Rydberg_eV = R_inf * h * c / e # eV (~13.6057 eV)
hc_eV_nm = (h * c / e) * 1e9     # eV*nm (~1239.84 eV*nm)

res = {}

# ==========================================
# 1. BÀI TẬP CẦU NỐI (Bridging Problem: A Many-Electron Atom in a Box)
# ==========================================
# Titanium (Ti, Z = 22), R_atom = 1.47e-10 m. Hộp lập phương thể tích bằng nguyên tử: L^3 = (4/3)*pi*R^3
R_Ti = 1.47e-10
V_Ti = (4.0 / 3.0) * np.pi * (R_Ti**3)
L_Ti = V_Ti**(1.0 / 3.0)

E0_Ti_J = (np.pi**2 * hbar**2) / (2.0 * m_e * L_Ti**2)
E0_Ti_eV = E0_Ti_J / e

# Mức năng lượng: E_{nx, ny, nz} = (nx^2 + ny^2 + nz^2) * E0
# Phân bố 22 electron vào các mức thấp nhất tuân theo nguyên lý loại trừ Pauli (2 e / trạng thái không gian):
# 1. (1,1,1): K=3, deg=1 -> 2 e.  E = 3 * E0
# 2. (2,1,1), (1,2,1), (1,1,2): K=6, deg=3 -> 6 e.  E = 6 * E0 (tổng tích lũy 8 e)
# 3. (2,2,1), (2,1,2), (1,2,2): K=9, deg=3 -> 6 e.  E = 9 * E0 (tổng tích lũy 14 e)
# 4. (3,1,1), (1,3,1), (1,1,3): K=11, deg=3 -> 6 e. E = 11 * E0 (tổng tích lũy 20 e)
# 5. (2,2,2): K=12, deg=1 -> 2 e. E = 12 * E0 (tổng tích lũy 22 e, vừa kín mức này!)

occupied_K = [3, 6, 9, 11, 12]
occupied_E_eV = [k * E0_Ti_eV for k in occupied_K]

# (d) Bước chuyển lấp lỗ trống mức thấp nhất từ mức cao nhất: (2,2,2) -> (1,1,1)
delta_E_bridge_eV = (12 - 3) * E0_Ti_eV
# So sánh với định luật Moseley cho photon K_alpha của Titanium (Z = 22):
# E(K_alpha) = (Z - 1)^2 * (3/4) * 13.6 eV = (21)^2 * 10.2 eV = 4498.2 eV ~ 4.50 - 4.52 keV
E_Moseley_eV = ((22 - 1)**2) * (0.75 * E_Rydberg_eV)

# Bước 8 Solution Guide: Ước lượng thế năng đẩy tĩnh điện của 2 electron cách nhau L/2:
r_sep = L_Ti / 2.0
U_coulomb_J = (1.0 / (4.0 * np.pi * eps0)) * (e**2) / r_sep
U_coulomb_eV = U_coulomb_J / e

res['bridge'] = {
    'L_m': L_Ti,
    'E0_eV': E0_Ti_eV,
    'occupied_E_eV': occupied_E_eV,
    'delta_E_eV': delta_E_bridge_eV,
    'E_Moseley_eV': E_Moseley_eV,
    'U_coulomb_eV': U_coulomb_eV
}

# ==========================================
# 2. BÀI TẬP 41.23 - 41.38
# ==========================================
# 41.23: Hydrogen 5g (l = 4), B = 0.600 T
# (a) Số mức tách: 2l + 1 = 9
# (b) Độ tách hai mức kề nhau: delta_E = mu_B * B
# (c) Độ tách mức thấp nhất đến cao nhất: 8 * mu_B * B
B_23 = 0.600
delta_E_23_eV = mu_B_eV * B_23
total_split_23_eV = 8.0 * delta_E_23_eV
res['41.23'] = {'levels': 9, 'delta_E_eV': delta_E_23_eV, 'total_split_eV': total_split_23_eV}

# 41.24: 2p -> 1s, lambda0 = 122 nm, từ trường B theo hướng +z.
# Quy tắc chọn lọc Delta m_l = 0, +-1. Initial m_l in {-1, 0, +1}, final m_l = 0.
# (a) 3 bước sóng
# (b) Cùng bước sóng: Delta m_l = 0 (m_li = 0 -> m_lf = 0)
# (c) Bước sóng dài hơn (photon năng lượng nhỏ hơn): Delta E < Delta E0 -> m_li = -1 -> m_lf = 0
# (d) Bước sóng ngắn hơn (photon năng lượng lớn hơn): Delta E > Delta E0 -> m_li = +1 -> m_lf = 0
res['41.24'] = {'wavelengths_count': 3, 'same': (0, 0), 'longer': (-1, 0), 'shorter': (1, 0)}

# 41.25: Spin electron cổ điển. R = 1.0e-17 m, S = sqrt(3/4)*hbar
S_25 = np.sqrt(0.75) * hbar
I_sphere_25 = 0.4 * m_e * (1.0e-17)**2
omega_25 = S_25 / I_sphere_25
v_equator_25 = 1.0e-17 * omega_25
v_over_c_25 = v_equator_25 / c
res['41.25'] = {'omega_rad_s': omega_25, 'v_m_s': v_equator_25, 'v_over_c': v_over_c_25}

# 41.26: Cấu trúc siêu tinh vi hydro: Delta E = 5.9e-6 eV
delta_E_26_J = 5.9e-6 * e
f_26 = delta_E_26_J / h
lam_26_m = c / f_26
B_eff_26 = 5.9e-6 / (2.0 * mu_B_eV)
res['41.26'] = {'f_Hz': f_26, 'lam_cm': lam_26_m * 100.0, 'B_eff_T': B_eff_26}

# 41.27: 1s, B = 1.45 T theo hướng -z (B_z = -1.45 T)
# U = -mu_z * B_z = -(-2 * mu_B * m_s) * (-B) = -2 * mu_B * m_s * B
# m_s = +1/2: U = -mu_B * B (thấp hơn)
# m_s = -1/2: U = +mu_B * B (cao hơn)
delta_E_27_eV = 2.0 * mu_B_eV * 1.45
res['41.27'] = {'delta_E_eV': delta_E_27_eV, 'lower_state': '+1/2'}

# 41.28: n=1, m_s = -1/2, B = 1.60 T theo hướng +z
# mu_z = -2 * mu_B * (-1/2) = +mu_B
# U = -mu_z * B = -mu_B * B
U_28_eV = -mu_B_eV * 1.60
res['41.28'] = {'U_eV': U_28_eV}

# 41.29: Neon (Z = 10): 10 bộ số lượng tử (n, l, ml, ms)
res['41.29'] = {'electron_count': 10}

# 41.30: Germanium (Z = 32): 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2
res['41.30'] = {'subshells': {'1s':2, '2s':2, '2p':6, '3s':2, '3p':6, '4s':2, '3d':10, '4p':2}}

# 41.31: Be (Z = 4, 1s2 2s2), Mg (Z = 12, [Ne]3s2), Ca (Z = 20, [Ar]4s2)
res['41.31'] = {'Be': '1s2 2s2', 'Mg': '[Ne] 3s2', 'Ca': '[Ar] 4s2'}

# 41.32: C (Z = 6, 1s2 2s2 2p2), Si (Z = 14, [Ne]3s2 3p2)
res['41.32'] = {'C': '1s2 2s2 2p2', 'Si': '[Ne] 3s2 3p2'}

# 41.33: Rubidium 5s, Z_eff = 2.771
E_ion_33_eV = (2.771**2 / 5.0**2) * 13.606
res['41.33'] = {'E_ion_eV': E_ion_33_eV}

# 41.34: Potassium (Z = 19): 4s (-4.339 eV), 4p (-2.73 eV), 4d (-0.94 eV)
Zeff_4s = 4.0 * np.sqrt(4.339 / 13.606)
Zeff_4p = 4.0 * np.sqrt(2.73 / 13.606)
Zeff_4d = 4.0 * np.sqrt(0.94 / 13.606)
assert Zeff_4s > Zeff_4p > Zeff_4d
assert np.isclose(Zeff_4s, 2.259, atol=0.01)
assert np.isclose(Zeff_4p, 1.792, atol=0.01)
assert np.isclose(Zeff_4d, 1.051, atol=0.01)
res['41.34'] = {'Zeff_4s': Zeff_4s, 'Zeff_4p': Zeff_4p, 'Zeff_4d': Zeff_4d}

# 41.35: N2+ (5 e: 1s2 2s2 2p1), P2+ (13 e: [Ne] 3s2 3p1)
# Ước lượng đơn giản Z_eff ~ Z - n_inner: N2+ có 4 e trong -> Z_eff ~ 3 -> E(2p) ~ -3^2/2^2 * 13.6 = -30.6 eV
# P2+ có 12 e trong -> Z_eff ~ 3 -> E(3p) ~ -3^2/3^2 * 13.6 = -13.6 eV
res['41.35'] = {'N2+_E_eV': -30.6, 'P2+_E_eV': -13.6}

# 41.36: E(K_alpha) = 7.46 keV = 7460 eV
# 7460 = (Z - 1)^2 * 10.2 eV -> (Z - 1)^2 = 731.37 -> Z - 1 = 27.04 -> Z = 28 (Nickel)
Z_36 = 1.0 + np.sqrt(7460.0 / 10.204)
res['41.36'] = {'Z': int(round(Z_36)), 'element': 'Ni'}

# 41.37: Ca (Z=20), Co (Z=27), Cd (Z=48)
def moseley_ka(Z):
    E_eV = (Z - 1)**2 * (0.75 * 13.606)
    f_Hz = (E_eV * e) / h
    lam_nm = hc_eV_nm / E_eV
    return E_eV / 1e3, f_Hz, lam_nm

res['41.37'] = {
    'Ca': moseley_ka(20),
    'Co': moseley_ka(27),
    'Cd': moseley_ka(48)
}

# 41.38: Tungsten (W): E_K = -69500 eV, E_L = -12000 eV, E_M = -2200 eV
delta_E_Ka_38 = -12000.0 - (-69500.0)
delta_E_Kb_38 = -2200.0 - (-69500.0)
lam_Ka_38_nm = hc_eV_nm / delta_E_Ka_38
lam_Kb_38_nm = hc_eV_nm / delta_E_Kb_38
res['41.38'] = {'lam_Ka_nm': lam_Ka_38_nm, 'lam_Kb_nm': lam_Kb_38_nm}

# ==========================================
# 3. BÀI TẬP 41.39 - 41.54
# ==========================================
# 41.39: 10 electron trong hộp lập phương.
# E_{nx,ny,nz} = (nx^2 + ny^2 + nz^2) E_0. E_{1,1,1} = 3 E_0
# 2 e ở n^2 = 3; 6 e ở n^2 = 6; 2 e còn lại ở n^2 = 9.
# Mức cao nhất là n^2 = 9, tương ứng E = 9 E_0 = 3 E_{1,1,1}.
res['41.39'] = {'highest_ratio': 3.0}

# 41.40: Hộp Lx = 0.600 nm, Ly = Lz = 1.200 nm
# E = (4 nx^2 + ny^2 + nz^2) * E0, E0 = pi^2*hbar^2 / (2*m*Ly^2)
Ly_40 = 1.200e-9
E0_40_eV = (np.pi**2 * hbar**2) / (2.0 * m_e * Ly_40**2) / e
# Bốn mức năng lượng thấp nhất và độ suy biến kể cả spin:
# 1. (1,1,1): K = 6 -> E1 = 6 * E0 ~ 1.567 eV (suy biến spin = 2)
# 2. (1,1,2), (1,2,1): K = 9 -> E2 = 9 * E0 ~ 2.350 eV (suy biến spin = 4)
# 3. (1,2,2): K = 12 -> E3 = 12 * E0 ~ 3.134 eV (suy biến spin = 2)
# 4. (1,1,3), (1,3,1): K = 14 -> E4 = 14 * E0 ~ 3.656 eV (suy biến spin = 4)
E1_40 = 6.0 * E0_40_eV
E2_40 = 9.0 * E0_40_eV
E3_40 = 12.0 * E0_40_eV
E4_40 = 14.0 * E0_40_eV
assert np.isclose(E1_40, 1.567, atol=0.01)
assert np.isclose(E2_40, 2.350, atol=0.01)
assert np.isclose(E3_40, 3.134, atol=0.01)
assert np.isclose(E4_40, 3.656, atol=0.01)
res['41.40'] = {
    'E1_eV': E1_40, 'deg1': 2, 'states1': [(1,1,1)],
    'E2_eV': E2_40, 'deg2': 4, 'states2': [(1,1,2), (1,2,1)],
    'E3_eV': E3_40, 'deg3': 2, 'states3': [(1,2,2)],
    'E4_eV': E4_40, 'deg4': 4, 'states4': [(1,1,3), (1,3,1)]
}

# 41.41: Hộp lập phương [0, L/4]^3
# (a) Phân số thể tích của khối hộp con: (L/4)^3 / L^3 = 1/64 = 0.015625
vol_frac_41 = (1.0 / 4.0)**3
assert np.isclose(vol_frac_41, 1.0 / 64.0)
# (b) Trạng thái cơ bản (1,1,1): P1 = [ (1/4) - (1/(2*pi)) ]^3
P_1D_n1 = 0.25 - (1.0 / (2.0 * np.pi))
P_41_b = P_1D_n1**3
assert np.isclose(P_41_b, 7.498e-4, rtol=0.01)
# (c) Trạng thái kích thích (2,1,1): nx = 2 cho tích phân = 1/4; ny=1, nz=1 cho P1
P_41_c = 0.25 * (P_1D_n1**2)
assert np.isclose(P_41_c, 2.063e-3, rtol=0.01)
res['41.41'] = {'vol_fraction': vol_frac_41, 'P_ground': P_41_b, 'P_exc': P_41_c}

# 41.42: Hộp Lx = Lz khác Ly. E1 = 2.24 eV, E2 = 3.47 eV, mỗi mức có độ suy biến kể cả spin là 2.
# E = C1*(nx^2 + nz^2) + C2*ny^2
# Mức cơ bản: (1,1,1) -> 2 C1 + C2 = 2.24 eV (deg spin = 2)
# Mức thứ hai: deg spin = 2 -> bắt buộc phải là (1,2,1) với E = 2 C1 + 4 C2 = 3.47 eV
# (nếu là (2,1,1) và (1,1,2) thì suy biến kể cả spin sẽ là 4, mâu thuẫn đề bài!)
C2_42 = (3.47 - 2.24) / 3.0 # = 0.410 eV
C1_42 = (2.24 - C2_42) / 2.0 # = 0.915 eV
factor_42 = (np.pi**2 * hbar**2) / (2.0 * m_e * e)
Lx_42 = np.sqrt(factor_42 / C1_42)
Ly_42 = np.sqrt(factor_42 / C2_42)
Lz_42 = Lx_42
# Mức năng lượng tiếp theo (mức thứ ba):
# Xét (2,1,1) và (1,1,2): E = 5 C1 + C2 = 5*(0.915) + 0.410 = 4.985 eV
# So với (1,3,1): E = 2 C1 + 9 C2 = 2*(0.915) + 9*(0.410) = 5.520 eV > 4.985 eV
# Do đó mức thứ 3 là 4.985 eV, gồm 2 trạng thái không gian (2,1,1) và (1,1,2),
# suy biến kể cả spin là 2 * 2 = 4!
E3_42 = 5.0 * C1_42 + C2_42
assert np.isclose(E3_42, 4.985, atol=0.01)
assert np.isclose(Lx_42 * 1e9, 0.641, atol=0.01)
assert np.isclose(Ly_42 * 1e9, 0.958, atol=0.01)
res['41.42'] = {
    'states_1': (1,1,1), 'E1_eV': 2.24, 'deg1': 2,
    'states_2': (1,2,1), 'E2_eV': 3.47, 'deg2': 2,
    'Lx_nm': Lx_42 * 1e9, 'Ly_nm': Ly_42 * 1e9, 'Lz_nm': Lz_42 * 1e9,
    'E3_eV': E3_42, 'states_3': [(2,1,1), (1,1,2)], 'deg3': 4
}

# 41.43: Hộp lập phương miền phẳng (slab) ở trạng thái cơ bản (1,1,1)
# (a) 0 < x < L/2: tích phân theo x từ 0 đến L/2 cho xác suất đúng 1/2
P_43_a = 0.500
# (b) L/4 < x < L/2: tích phân theo x cho (1/4) + (1/(2*pi)) ~ 0.40915
P_43_b = 0.25 + (1.0 / (2.0 * np.pi))
# So sánh với Example 41.1 (0 < x < L/4): P = 1/4 - 1/(2*pi) ~ 0.09085
P_43_ex41_1 = 0.25 - (1.0 / (2.0 * np.pi))
assert P_43_a == 0.5
assert np.isclose(P_43_b, 0.40915, atol=0.001)
assert np.isclose(P_43_ex41_1, 0.09085, atol=0.001)
res['41.43'] = {'P_a': P_43_a, 'P_b': P_43_b, 'P_ex41_1': P_43_ex41_1}

# 41.44: Dao động tử điều hòa đẳng hướng 3D
# E = (nx + ny + nz + 3/2)*hbar*omega
# Cơ bản: nx=ny=nz=0 -> E = 1.5 hbar*omega (deg = 1)
# Kích thích 1: nx+ny+nz=1 -> (1,0,0),(0,1,0),(0,0,1) -> E = 2.5 hbar*omega (deg = 3)
res['41.44'] = {'E0_factor': 1.5, 'E1_factor': 2.5, 'deg1': 3}

# 41.45: Dao động tử không đẳng hướng k'1 > k'2 (omega1 > omega2)
# E = (nx + ny + 1)*hbar*omega1 + (nz + 1/2)*hbar*omega2
# Cơ bản: (0,0,0) -> E = hbar*omega1 + 0.5*hbar*omega2 (deg = 1)
# Kích thích 1: (0,0,1) -> E = hbar*omega1 + 1.5*hbar*omega2 (deg = 1)
res['41.45'] = {'deg0': 1, 'deg1': 1}

# 41.46: Hộp Ly = 2 Lx, Lz = Ly/3 = (2/3) Lx.
# E = (4 nx^2 + ny^2 + 9 nz^2) * (pi^2*hbar^2 / (8*m*Lx^2))
# Cơ bản: (1,1,1) -> K = 14
# Kích thích 1: (1,2,1) -> K = 17 -> Delta K = 3 -> Delta E = 3 * (pi^2*hbar^2 / (8*m*Lx^2))
# Bậc suy biến = 1. Cực đại xác suất ở tâm: x = Lx/2, y = Ly/2 = Lx, z = Lz/2 = Lx/3.
res['41.46'] = {'delta_K': 3, 'degenerate': False}

# 41.47: Lớp n có tổng số trạng thái 2n^2.
# 50 trạng thái -> 2n^2 = 50 -> n = 5 (lớp O).
res['41.47'] = {'n': 5}

# 41.48: Sao lùn trắng R = 7000 km, M_sun = 2.0e30 kg, M_p = 1.7e-27 kg
N_e_48 = 2.0e30 / 1.7e-27
V_wd_48 = (4.0 / 3.0) * np.pi * ((7.0e6)**3)
V_e_48 = V_wd_48 / N_e_48
V_C_48 = 6.0 * V_e_48
L_C_48 = V_C_48**(1.0 / 3.0)
# 6 electron điền: (1,1,1, +-1/2) và 4 electron vào n^2 = 6
E_high_48_J = 6.0 * (np.pi**2 * hbar**2) / (2.0 * m_e * L_C_48**2)
E_high_48_eV = E_high_48_J / e
res['41.48'] = {'N_e': N_e_48, 'L_m': L_C_48, 'E_high_eV': E_high_48_eV}

# 41.49: Hydro 1s, U(r) = -e^2/(4*pi*eps0*r), E = -e^2/(8*pi*eps0*a0)
# (a) Điểm chuyển tiếp cổ điển U(r) = E -> r = 2 a0
# (b) Xác suất trong vùng cấm cổ điển r > 2 a0:
# P = \int_{2 a0}^\infty (4/a0^3) r^2 exp(-2r/a0) dr = 13 * exp(-4)
P_49 = 13.0 * np.exp(-4.0)
res['41.49'] = {'r_turn': 2.0, 'prob_forbidden': P_49}

# 41.50: Hydro 1s, P(r) = (4/a0^3) r^2 exp(-2r/a0). Cực đại tại r = a0 (bán kính Bohr n=1).
res['41.50'] = {'r_max': 1.0}

# 41.51: Hydro 2p, P(r) = (1/(24 a0^5)) r^4 exp(-r/a0). Cực đại tại r = 4 a0 (bán kính Bohr n=2).
res['41.51'] = {'r_max': 4.0}

# 41.52: Bức xạ siêu tinh vi hydro giữa proton và electron
# (a) mu_p = (e/(2*m_p))*(hbar/2) = e*hbar / (4*m_p)
mp_52 = 1.7e-27
mu_p_52 = (e * hbar) / (4.0 * mp_52)
R_p_52 = 0.85e-15
I_p_52 = mu_p_52 / (np.pi * R_p_52**2)
# (b) B tại x = 0.40 a0: B = mu0 * mu_p / (2*pi * x^3)
x_52 = 0.40 * a0
B_52 = (mu0 * mu_p_52) / (2.0 * np.pi * x_52**3)
# (c) U = mu_B * B
U_52_eV = (mu_B * B_52) / e
# (d) lambda = hc / (2 * U)
lam_52_m = (h * c) / (2.0 * mu_B * B_52)
res['41.52'] = {'I_A': I_p_52, 'B_T': B_52, 'U_eV': U_52_eV, 'lam_m': lam_52_m}

# 41.53: Cấu trúc tinh vi vạch lam hydro (n = 5 -> n = 2, 434 nm)
# (a) Số bộ (l, j): n=5 có 9 bộ; n=2 có 3 bộ
# (b) Số mức năng lượng: n=5 có 5 mức (j = 1/2, 3/2, 5/2, 7/2, 9/2); n=2 có 2 mức (j = 1/2, 3/2)
# Công thức Dirac tách mức: Delta E_{n, j} = - (13.606 eV / n^2) * (alpha^2 / n^2) * [ n/(j+1/2) - 3/4 ]
alpha_fine = const.fine_structure
def dirac_shift_eV(n, j):
    return - (13.6057 / (n**2)) * ((alpha_fine / n)**2) * (n / (j + 0.5) - 0.75)

shifts_n5 = {f'5_{int(2*j)}/2': dirac_shift_eV(5, j) for j in [0.5, 1.5, 2.5, 3.5, 4.5]}
shifts_n2 = {f'2_{int(2*j)}/2': dirac_shift_eV(2, j) for j in [0.5, 1.5]}
E0_53 = 13.6057 * (1.0/4.0 - 1.0/25.0)
lam0_53 = hc_eV_nm / E0_53

all_trans_53 = []
for l5 in range(5):
    for j5 in [l5 - 0.5, l5 + 0.5]:
        if j5 < 0.5: continue
        for l2 in range(2):
            if abs(l5 - l2) != 1: continue
            for j2 in [l2 - 0.5, l2 + 0.5]:
                if j2 < 0.5: continue
                if abs(j5 - j2) > 1: continue
                dE_trans = dirac_shift_eV(5, j5) - dirac_shift_eV(2, j2)
                lam_trans = hc_eV_nm / (E0_53 + dE_trans)
                dlam_trans = lam_trans - lam0_53
                all_trans_53.append(((l5, j5), (l2, j2), dE_trans, lam_trans, dlam_trans))

all_trans_53.sort(key=lambda x: x[3])
shortest_trans = all_trans_53[0] # ((1, 1.5), (0, 0.5)) -> dlam ~ -0.00829 nm
longest_trans = all_trans_53[-1] # ((0, 0.5), (1, 1.5)) -> dlam ~ -0.00097 nm
broadening_53 = longest_trans[3] - shortest_trans[3]
assert np.isclose(shortest_trans[4], -0.00829, atol=0.0005)
assert np.isclose(longest_trans[4], -0.00097, atol=0.0005)
assert np.isclose(broadening_53, 0.00732, atol=0.0005)
res['41.53'] = {
    'sets_n5': 9, 'sets_n2': 3,
    'levels_n5': 5, 'levels_n2': 2,
    'shifts_n5': shifts_n5, 'shifts_n2': shifts_n2,
    'shortest_dlam_nm': shortest_trans[4],
    'longest_dlam_nm': longest_trans[4],
    'broadening_nm': broadening_53
}

# 41.54: 3d -> 2p, lambda0 = 475.082 nm, B = 3.500 T
E0_54_eV = hc_eV_nm / 475.082
delta_U_54_eV = mu_B_eV * 3.500
# (c) Mức 3d ban đầu -8.50000 eV tách thành 5 mức trong từ trường:
E_3d_split_eV = [-8.50000 + ml * delta_U_54_eV for ml in [-2, -1, 0, 1, 2]]
# (d) Ba bước sóng phát xạ ứng với Delta ml = 0, +-1:
lam_54_nm_list = [hc_eV_nm / (E0_54_eV + dml * delta_U_54_eV) for dml in [1, 0, -1]]
res['41.54'] = {
    'E0_eV': E0_54_eV,
    'delta_U_eV': delta_U_54_eV,
    'E_3d_split_eV': E_3d_split_eV,
    'emitted_lambdas_nm': lam_54_nm_list
}

# ==========================================
# 4. BÀI TẬP 41.55 - 41.69
# ==========================================
# 41.55: Phân tích quang phổ Zeeman: lambda0 = 575.050 nm, Delta lambda = 0.0462 nm
B_55 = (h * c * (0.0462e-9)) / (((575.050e-9)**2) * mu_B)
assert np.isclose(B_55, 2.993, atol=0.01)
res['41.55'] = {'B_T': B_55}

# 41.56: Thí nghiệm Stern-Gerlach: L = 50.0 cm = 0.500 m, v = 375 m/s, d = 1.0 mm = 1.0e-3 m
m_Ag = 107.8682 * const.atomic_mass
grad_56 = (1.0e-3 * m_Ag * 375.0**2) / (mu_B * 0.500**2)
assert np.isclose(grad_56, 10.86, atol=0.02)
res['41.56'] = {'m_Ag_kg': m_Ag, 'grad_T_m': grad_56}

# 41.57: Quả cầu tích điện quay quanh trục z
# (a) da = 2*pi*R^2*sin(theta)*dtheta
# (b) dI = sigma*omega*R^2*sin(theta)*dtheta
# (c) dM = pi*sigma*omega*R^4*sin^3(theta)*dtheta
# (d) M = (4/3)*pi*sigma*omega*R^4 = (1/3)*Q*omega*R^2
# (e) Cầu đặc: M = (4*pi/3)*omega*\int_0^R r^4*rho(r)*dr
# (f) L = c*M_mass*R^2*omega -> g = (M/L)*(2*M_mass/Q) = (8*pi/(3*c*Q*R^2)) * \int_0^R r^4*rho(r)*dr
# (g) Cầu đồng chất: rho = Q / ((4/3)*pi*R^3), c = 2/5 -> \int r^4 dr = R^5/5 -> M = (1/5)*Q*omega*R^2 -> g = 1.0
res['41.57'] = {'g_uniform': 1.0}

# 41.58: Từ trường hiệu dụng của electron 2p (r = 4 a0, L = sqrt(2)*hbar)
v_58 = (np.sqrt(2.0) * hbar) / (m_e * (4.0 * a0))
# Proton chuyển động tròn bán kính r2 = 4 a0 tạo dòng I = e*v / (2*pi*r2)
# B tại tâm: B = mu0 * I / (2 * r2) = mu0 * e * v / (4 * pi * (4 a0)^2)
B_58 = (mu0 * e * v_58) / (4.0 * np.pi * ((4.0 * a0)**2))
res['41.58'] = {'v_m_s': v_58, 'B_T': B_58}

# 41.59: Vũ trụ spin-3/2
# (a) Hai khí hiếm nhẹ nhất: Z = 4 (1s^4) và Z = 20 (1s^4 2s^4 2p^12)
# (b) Cấu hình electron cơ bản của Natri (Z = 11): 1s^4 2s^4 2p^3
res['41.59'] = {'noble_gases': [4, 20], 'Na_config': '1s^4 2s^4 2p^3'}

# 41.60: Bước sóng lithium theo nguyên bản đề: lambda1 = 67.09608 um, lambda2 = 67.09761 um
lam1_60 = 67.09608e-6
lam2_60 = 67.09761e-6
delta_E_60_J = h * c * (1.0 / lam1_60 - 1.0 / lam2_60)
delta_E_60_eV = delta_E_60_J / e
B_eff_60 = delta_E_60_J / (2.0 * mu_B)
assert np.isclose(B_eff_60, 0.00364, atol=0.0001)
res['41.60'] = {'delta_E_eV': delta_E_60_eV, 'B_eff_T': B_eff_60}

# 41.61: Hydro n=2, l=1, ml=-1 -> n=1, l=0, ml=0. B = 2.20 T
# Delta E = E0(2p -> 1s) + (-1)*mu_B*B - 0 = 10.204 eV - mu_B*B
delta_E_61_eV = (13.606 * 0.75) - mu_B_eV * 2.20
lam_61_nm = hc_eV_nm / delta_E_61_eV
res['41.61'] = {'delta_E_eV': delta_E_61_eV, 'lam_nm': lam_61_nm}

# 41.62: Cộng hưởng spin electron (ESR)
# h*c / lambda = 2 * mu_B * B -> B = hc / (2 * mu_B * lambda)
lam_62 = 0.0420 # 4.20 cm
B_62 = (h * c) / (2.0 * mu_B * lam_62)
res['41.62'] = {'B_T': B_62}

# 41.63 (DATA): ESR với 7 cặp số liệu
B_63 = np.array([0.51, 0.74, 1.03, 1.52, 2.02, 2.48, 2.97])
lam_63_mm = np.array([21.4, 14.3, 10.7, 7.14, 5.35, 4.28, 3.57])
lam_63_m = lam_63_mm * 1e-3
f_63 = c / lam_63_m # Hz

slope_63, intercept_63 = np.polyfit(B_63, f_63, 1)
mu_z_exp_63 = slope_63 * h / 2.0
mu_z_over_muB_63 = mu_z_exp_63 / mu_B
# gyromagnetic ratio gamma = |mu_z| / |S_z| = |mu_z| / (hbar / 2)
gamma_63 = mu_z_exp_63 / (0.5 * hbar)
# gamma / (e / (2m)) = |mu_z| / mu_B
ratio_gamma_63 = gamma_63 / (e / (2.0 * m_e))
assert np.isclose(ratio_gamma_63, 2.029, atol=0.01)
res['41.63'] = {
    'slope_Hz_T': slope_63,
    'intercept_Hz': intercept_63,
    'mu_z_exp': mu_z_exp_63,
    'mu_z_over_muB': mu_z_over_muB_63,
    'g_ratio': ratio_gamma_63
}

# 41.64: Chuyển mức 3p -> 2s, j = 3/2 vs j = 1/2
delta_E_3p_split_eV = dirac_shift_eV(3, 1.5) - dirac_shift_eV(3, 0.5)
lam_Halpha_nm = hc_eV_nm / (13.606 * (1.0/4.0 - 1.0/9.0))
delta_lam_64_nm = lam_Halpha_nm * (delta_E_3p_split_eV / (13.606 * (1.0/4.0 - 1.0/9.0)))
res['41.64'] = {'delta_E_split_eV': delta_E_3p_split_eV, 'delta_lam_nm': delta_lam_64_nm}

# 41.65 (DATA): Kim loại kiềm Li, Na, K, Rb, Cs, Fr
elements_65 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
Z_65 = [3, 11, 19, 37, 55, 87]
n_65 = [2, 3, 4, 5, 6, 7]
ion_kJ_mol_65 = np.array([520.2, 495.8, 418.8, 403.0, 375.7, 380.0])
kJ_to_eV = 1e3 / (const.N_A * e)
ion_eV_65 = ion_kJ_mol_65 * kJ_to_eV
Z_eff_65 = np.array(n_65) * np.sqrt(ion_eV_65 / 13.606)
res['41.65'] = {
    'ion_eV': list(ion_eV_65),
    'Z_eff': list(Z_eff_65)
}

# 41.66 (DATA): Electron trong hộp lập phương
lam_longest_66 = 624.0e-9
L_66 = np.sqrt( (3.0 * np.pi**2 * hbar**2 * lam_longest_66) / (2.0 * m_e * h * c) )
res['41.66'] = {'L_m': L_66, 'K_final': 11, 'degeneracy_with_spin': 6}

# 41.67 (CHALLENGE): Hạt spin-3/2
S_mag_factor = np.sqrt(15.0) / 2.0
# Đo A được +1/2:
# Trạng thái B có xác suất: P(-1/2) = 0.5, P(-3/2) = 0.5, P(+1/2) = 0.0, P(+3/2) = 0.0
# Tiếp theo đo C được -3/2:
# Trạng thái B chắc chắn là -1/2: P(-1/2) = 1.0, P(khác) = 0.0
res['41.67'] = {
    'S_magnitude_factor': S_mag_factor,
    'post_A_probs': {'-1/2': 0.5, '+1/2': 0.0, '-3/2': 0.5, '+3/2': 0.0},
    'post_C_probs': {'-1/2': 1.0, '+1/2': 0.0, '-3/2': 0.0, '+3/2': 0.0}
}

# 41.68 (CHALLENGE): 2N electron trong dao động tử điều hòa 1D
res['41.68'] = {'coeff': 'N^2'}

# 41.69 (CHALLENGE): Helium quỹ đạo đối đường kính
r_69_over_a0 = 4.0 / 7.0
E_ion_total_69_eV = (49.0 / 8.0) * 13.606
diff_percent_69 = (E_ion_total_69_eV - 79.0) / 79.0 * 100.0
res['41.69'] = {
    'r_over_a0': r_69_over_a0,
    'E_ion_total_eV': E_ion_total_69_eV,
    'diff_percent': diff_percent_69
}

# ==========================================
# 5. MCAT 41.70 - 41.73
# ==========================================
r_MCAT = 1.0e-6 # 1 micrometer (1 um)
n_70 = np.sqrt(r_MCAT / a0) # ~137.47 -> chọn 140 (đáp án a)
assert np.isclose(n_70, 137.47, atol=0.1)

D_sep = 10.0 * (2.0 * r_MCAT) # 20 um = 2.0e-3 cm
density_71 = 1.0 / ((D_sep * 1e2)**3) # 1.25e8 cm^-3 -> 10^8 (đáp án b)
assert 1e8 <= density_71 <= 2e8

res['41.70'] = {'n': n_70, 'choice': '(a) 140'}
res['41.71'] = {'density_cm3': density_71, 'choice': '(b) 10^8 atoms/cm^3'}
res['41.72'] = {'L_factor': np.sqrt(6), 'choice': '(b) sqrt(6) hbar'}
res['41.73'] = {'states_count': 10, 'choice': '(d) 10'}

print('===========================================================')
print('ĐÃ TÍNH LẠI CÁC ĐẠI LƯỢNG TRONG MÔ HÌNH SỐ, CHAPTER41 D; CẦN RÀ RIÊNG VĂN BẢN, HÌNH VÀ LẬP LUẬN')
print('===========================================================')
print(f'1. Bridging Problem: L = {res["bridge"]["L_m"]*1e10:.3f} e-10 m, E_photon = {res["bridge"]["delta_E_eV"]:.1f} eV vs Moseley {res["bridge"]["E_Moseley_eV"]:.0f} eV, U_coulomb(L/2) = {res["bridge"]["U_coulomb_eV"]:.1f} eV')
print(f'2. Bài 41.63 ESR: slope = {res["41.63"]["slope_Hz_T"]:.3e} Hz/T, mu_z/mu_B = {res["41.63"]["mu_z_over_muB"]:.3f}, g = {res["41.63"]["g_ratio"]:.3f}')
print(f'3. Bài 41.65 Kiềm: Fr ion_energy = {res["41.65"]["ion_eV"][-1]:.3f} eV, Z_eff = {res["41.65"]["Z_eff"][-1]:.3f} (Fr cao hơn Cs trong bảng đã cho)')
print(f'4. Bài 41.66 Box: L = {res["41.66"]["L_m"]*1e9:.3f} nm, K_final = {res["41.66"]["K_final"]}, deg_with_spin = {res["41.66"]["degeneracy_with_spin"]}')
print(f'5. Bài 41.69 Helium: r/a0 = {res["41.69"]["r_over_a0"]:.4f}, E_ion = {res["41.69"]["E_ion_total_eV"]:.2f} eV vs 79.0 eV (lệch {res["41.69"]["diff_percent"]:.1f}%)')
print(f'6. MCAT: 41.70: {res["41.70"]["choice"]}, 41.71: {res["41.71"]["choice"]}, 41.72: {res["41.72"]["choice"]}, 41.73: {res["41.73"]["choice"]}')
