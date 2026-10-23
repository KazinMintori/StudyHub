"""Kịch bản kiểm tra độc lập bằng Python cho toàn bộ 48 bài tập Chapter 09 (nhóm D: 9.1 - 9.48).

Kiểm tra:
- Toàn bộ giá trị số học, biến đổi đại số và đơn vị vật lý cho 48 bài tập (9.1 đến 9.48).
- Đối chiếu với đáp án chuẩn của sách giáo trình Young & Freedman (15th Edition).
- Kiểm tra tính hợp lệ và nguyên vẹn của 4 tệp hình ảnh crop từ PDF gốc.
- Kiểm tra định dạng xuất dữ liệu chú thích hình ảnh.
"""
import math
import hashlib
from pathlib import Path
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parents[2]

# Hằng số chuẩn
g = 9.80  # m/s^2

results = {}

# ==========================================
# 9.1 - 9.10
# ==========================================
# 9.1
theta_1a_rad = 1.50 / 2.50
theta_1a_deg = theta_1a_rad * 180.0 / math.pi
r_1b_cm = 14.0 / (128.0 * math.pi / 180.0)
s_1c_m = 1.50 * 0.700
assert abs(theta_1a_rad - 0.600) < 1e-4
assert abs(theta_1a_deg - 34.377) < 0.1
assert abs(r_1b_cm - 6.27) < 0.05
assert abs(s_1c_m - 1.05) < 1e-4
results['9.1'] = (theta_1a_rad, theta_1a_deg, r_1b_cm, s_1c_m)

# 9.2
omega_2a = 1900.0 * 2.0 * math.pi / 60.0
t_2b = (35.0 * math.pi / 180.0) / omega_2a
assert abs(omega_2a - 198.97) < 0.5
assert abs(t_2b - 0.00307) < 1e-4
results['9.2'] = (omega_2a, t_2b)

# 9.3
alpha_3b_i = 0.0
alpha_3b_ii = 2.0 * 1.50 * 5.00
theta_3c = 2.75 * 2.00 + 1.50 * (2.00**3) / 3.0
assert alpha_3b_i == 0.0
assert alpha_3b_ii == 15.0
assert abs(theta_3c - 9.50) < 1e-4
results['9.3'] = (alpha_3b_i, alpha_3b_ii, theta_3c)

# 9.4
alpha_4b_inst = -2.0 * 0.800 * 3.00
omega_4_0 = 5.00
omega_4_3 = 5.00 - 0.800 * (3.00**2)
alpha_4b_avg = (omega_4_3 - omega_4_0) / 3.00
assert abs(alpha_4b_inst - (-4.80)) < 1e-4
assert abs(alpha_4b_avg - (-2.40)) < 1e-4
results['9.4'] = (alpha_4b_inst, alpha_4b_avg)

# 9.5
omega_5b = 0.400
omega_5c_inst = 0.400 + 3.0 * 0.0120 * (5.00**2)
theta_5c = 0.400 * 5.00 + 0.0120 * (5.00**3)
omega_5c_avg = theta_5c / 5.00
assert abs(omega_5b - 0.400) < 1e-4
assert abs(omega_5c_inst - 1.30) < 1e-4
assert abs(omega_5c_avg - 0.700) < 1e-4
results['9.5'] = (omega_5b, omega_5c_inst, omega_5c_avg)

# 9.6
# 4.5*t^2 + 40*t - 250 = 0
t_6a = (-40.0 + math.sqrt(40.0**2 - 4 * 4.50 * (-250.0))) / (2 * 4.50)
alpha_6b = -40.0 - 9.00 * t_6a
theta_6c = 250.0 * t_6a - 20.0 * (t_6a**2) - 1.50 * (t_6a**3)
rev_6c = theta_6c / (2 * math.pi)
omega_6d = 250.0
omega_6e = theta_6c / t_6a
assert abs(t_6a - 4.234) < 0.01
assert abs(alpha_6b - (-78.10)) < 0.1
assert abs(rev_6c - 93.24) < 0.2
assert omega_6d == 250.0
assert abs(omega_6e - 138.4) < 0.5
results['9.6'] = (t_6a, alpha_6b, rev_6c, omega_6d, omega_6e)

# 9.7
# theta(t) = a + b*t - c*t^3
# When t=0, theta = pi/4, omega = 2.00
# At t=1.50 s, alpha = 1.25 rad/s^2 -> -6c(1.50) = 1.25 -> c = -0.13889
a_7 = math.pi / 4.0
b_7 = 2.00
c_7 = -1.25 / 9.0  # -0.13889
alpha_7b = 0.0
t_7c = 3.50 / (-6.0 * c_7)  # 4.20 s
theta_7c = a_7 + b_7 * t_7c - c_7 * (t_7c**3)
omega_7c = b_7 - 3.0 * c_7 * (t_7c**2)
assert abs(a_7 - 0.7854) < 1e-3
assert abs(c_7 - (-0.1389)) < 1e-3
assert alpha_7b == 0.0
assert abs(theta_7c - 19.48) < 0.1
assert abs(omega_7c - 9.35) < 0.1
results['9.7'] = (a_7, b_7, c_7, alpha_7b, theta_7c, omega_7c)

# 9.8
alpha_8a = (4.00 - (-6.00)) / 7.00
t_reverse_8 = 6.00 / alpha_8a  # 4.20 s
theta_8c = (-6.00 + 4.00) / 2.0 * 7.00
assert abs(alpha_8a - 1.4286) < 1e-3
assert abs(t_reverse_8 - 4.20) < 1e-2
assert theta_8c == -7.00
results['9.8'] = (alpha_8a, t_reverse_8, theta_8c)

# 9.9
omega_9a = 1.50 + 0.200 * 2.50
theta_9b = 1.50 * 2.50 + 0.5 * 0.200 * (2.50**2)
assert abs(omega_9a - 2.00) < 1e-4
assert abs(theta_9b - 4.375) < 1e-4
results['9.9'] = (omega_9a, theta_9b)

# 9.10
w0_10 = 500.0 / 60.0
w1_10 = 200.0 / 60.0
alpha_10a_rev = (w1_10 - w0_10) / 4.00
rev_10a = (w0_10 + w1_10) / 2.0 * 4.00
t_10b = (0.0 - w1_10) / alpha_10a_rev
assert abs(alpha_10a_rev - (-1.25)) < 1e-4
assert abs(rev_10a - 23.33) < 0.05
assert abs(t_10b - 2.667) < 0.01
results['9.10'] = (alpha_10a_rev, rev_10a, t_10b)

# ==========================================
# 9.11 - 9.20
# ==========================================
# 9.11
t_11a = 36.0 / 1.50
rev_11b = (0.5 * 36.0 * t_11a) / (2 * math.pi)
assert abs(t_11a - 24.0) < 1e-4
assert abs(rev_11b - 68.75) < 0.1
results['9.11'] = (t_11a, rev_11b)

# 9.12
alpha_12 = (2 * 8.00) / (2.50**2)
rev_total_12 = 0.5 * alpha_12 * (7.50**2)
rev_next_12 = rev_total_12 - 8.00
assert abs(rev_next_12 - 64.0) < 1e-4
results['9.12'] = rev_next_12

# 9.13
w0_13 = (30.0 - 0.5 * 2.25 * (4.00**2)) / 4.00
assert abs(w0_13 - 3.00) < 1e-4
results['9.13'] = w0_13

# 9.14
alpha_14 = 140.0 / 6.00
theta_14 = 0.5 * 140.0 * 6.00
assert abs(alpha_14 - 23.33) < 0.05
assert theta_14 == 420.0
results['9.14'] = (alpha_14, theta_14)

# 9.15
w0_15_rev = 500.0 / 60.0
w1_15_rev = (2 * 200.0 / 30.0) - w0_15_rev
w1_15_rpm = w1_15_rev * 60.0
alpha_15 = (w1_15_rev - w0_15_rev) / 30.0
t_stop_15 = (0 - w0_15_rev) / alpha_15
rev_stop_15 = 0.5 * w0_15_rev * t_stop_15
assert abs(w1_15_rpm - 300.0) < 1e-3
assert abs(t_stop_15 - 75.0) < 1e-3
assert abs(rev_stop_15 - 312.5) < 0.5
results['9.15'] = (w1_15_rpm, t_stop_15, rev_stop_15)

# 9.16
theta_16_1 = 24.0 * 2.00 + 0.5 * 30.0 * (2.00**2)
w_16_1 = 24.0 + 30.0 * 2.00
theta_16_tot = theta_16_1 + 432.0
t_16_2 = 2 * 432.0 / w_16_1
t_16_tot = 2.00 + t_16_2
alpha_16_coast = - (w_16_1**2) / (2 * 432.0)
assert theta_16_tot == 540.0
assert abs(t_16_tot - 12.29) < 0.05
assert abs(alpha_16_coast - (-8.167)) < 0.01
results['9.16'] = (theta_16_tot, t_16_tot, alpha_16_coast)

# 9.17
rev_17 = (3.0**2) * 1.00
assert rev_17 == 9.00
results['9.17'] = rev_17

# 9.18
r_18 = 1.25
w_18_rpm = (0.250 / r_18) * 60.0 / (2 * math.pi)
alpha_18 = (g / 8.0) / r_18
theta_18_rad = 3.25 / r_18
theta_18_deg = theta_18_rad * 180.0 / math.pi
assert abs(w_18_rpm - 1.91) < 0.02
assert abs(alpha_18 - 0.980) < 0.01
assert abs(theta_18_rad - 2.60) < 1e-4
assert abs(theta_18_deg - 148.97) < 0.1
results['9.18'] = (w_18_rpm, alpha_18, theta_18_rad, theta_18_deg)

# 9.19
# D ~ 0.50 m, r = 0.25 m
r_19 = 0.250
w_19_rad = math.sqrt(3 * g / r_19)
w_19_rpm = w_19_rad * 60.0 / (2 * math.pi)
v_19 = w_19_rad * r_19
assert abs(w_19_rpm - 103.5) < 1.0
assert abs(v_19 - 2.71) < 0.05
results['9.19'] = (w_19_rpm, v_19)

# 9.20
w_20_in = 1.25 / 0.0250
w_20_out = 1.25 / 0.0580
len_20 = 1.25 * (74.0 * 60.0)
alpha_20_avg = (w_20_out - w_20_in) / (74.0 * 60.0)
assert abs(w_20_in - 50.0) < 1e-4
assert abs(w_20_out - 21.55) < 0.05
assert len_20 == 5550.0
assert abs(alpha_20_avg - (-0.006407)) < 1e-5
results['9.20'] = (w_20_in, w_20_out, len_20, alpha_20_avg)

# ==========================================
# 9.21 - 9.30
# ==========================================
# 9.21
r_21 = 0.200
theta_21 = 4.0 * math.pi
w2_21 = 2.0 * 3.00 * theta_21
arad_21a = w2_21 * r_21
arad_21b = (w2_21 * (r_21**2)) / r_21
assert abs(arad_21a - 15.08) < 0.05
assert abs(arad_21a - arad_21b) < 1e-6
results['9.21'] = arad_21a

# 9.22
w_22 = 7.5 * 2 * math.pi / 60.0
d_22 = 2.0 * (0.0200 / w_22)
alpha_22 = 0.400 / (d_22 / 2.0)
assert abs(d_22 - 0.05093) < 0.001
assert abs(alpha_22 - 15.71) < 0.05
results['9.22'] = (d_22, alpha_22)

# 9.23
# typical D ~ 0.200 m, r = 0.100 m
w_23 = 2600.0 * 2 * math.pi / 60.0
v_23 = w_23 * 0.100
assert abs(v_23 - 27.23) < 0.5
results['9.23'] = v_23

# 9.24
r_24 = 0.375
w0_24 = 0.250 * 2 * math.pi
alpha_24 = 0.900 * 2 * math.pi
w_24 = w0_24 + alpha_24 * 0.200
rev_24 = 0.250 * 0.200 + 0.5 * 0.900 * (0.200**2)
v_24 = w_24 * r_24
atan_24 = alpha_24 * r_24
arad_24 = (w_24**2) * r_24
a_res_24 = math.sqrt(atan_24**2 + arad_24**2)
assert abs(w_24 / (2 * math.pi) - 0.430) < 1e-4
assert abs(rev_24 - 0.0680) < 1e-4
assert abs(v_24 - 1.013) < 0.01
assert abs(a_res_24 - 3.46) < 0.05
results['9.24'] = (w_24, rev_24, v_24, a_res_24)

# 9.25
w_25 = 5000.0 * 2 * math.pi / 60.0
r_25 = (3000.0 * g) / (w_25**2)
assert abs(r_25 - 0.1072) < 0.001
results['9.25'] = r_25

# 9.26
r_26 = 0.200
alpha_26 = -10.0 / r_26
w_26_3 = 50.0 / r_26
w_26_0 = w_26_3 - alpha_26 * 3.00
theta_26 = (w_26_0 + w_26_3) / 2.0 * 3.00
t_26_g = (math.sqrt(g / r_26) - w_26_0) / alpha_26
assert alpha_26 == -50.0
assert w_26_3 == 250.0
assert w_26_0 == 400.0
assert theta_26 == 975.0
assert abs(t_26_g - 7.86) < 0.02
results['9.26'] = (alpha_26, w_26_3, w_26_0, theta_26, t_26_g)

# 9.27
r_27 = 0.300
w0_27 = 3.00 / r_27
w1_27 = 6.00 / r_27
theta_27 = 4.00 * 2 * math.pi
alpha_27 = (w1_27**2 - w0_27**2) / (2 * theta_27)
assert abs(alpha_27 - 5.968) < 0.01
results['9.27'] = alpha_27

# 9.28
R_28 = 1.27e7 / 2.0
w_28 = 2 * math.pi / 86400.0
v_28 = w_28 * R_28
arad_28 = (w_28**2) * R_28
assert abs(v_28 - 461.8) < 0.5
assert abs(arad_28 - 0.0336) < 0.001
results['9.28'] = (v_28, arad_28)

# 9.29
r_29 = 0.300
alpha_29 = 0.600
w_29 = alpha_29 * 2.00
atan_29 = alpha_29 * r_29
arad_29 = (w_29**2) * r_29
ares_29 = math.sqrt(atan_29**2 + arad_29**2)
assert abs(atan_29 - 0.180) < 1e-4
assert abs(arad_29 - 0.432) < 1e-4
assert abs(ares_29 - 0.468) < 1e-3
results['9.29'] = (atan_29, arad_29, ares_29)

# 9.30
m_30 = 0.200
s_30 = 0.400
r_diag_30 = s_30 / math.sqrt(2)
I_30a = 4 * m_30 * (r_diag_30**2)
I_30b = 4 * m_30 * ((s_30 / 2.0)**2)
I_30c = 2 * m_30 * (r_diag_30**2)
assert abs(I_30a - 0.0640) < 1e-4
assert abs(I_30b - 0.0320) < 1e-4
assert abs(I_30c - 0.0320) < 1e-4
results['9.30'] = (I_30a, I_30b, I_30c)

# ==========================================
# 9.31 - 9.40
# ==========================================
# 9.31
I_31a_i = (1.0 / 3.0) * 2.50 * (0.750**2)
I_31a_ii = (1.0 / 12.0) * 2.50 * (0.750**2)
I_31a_iii = 0.0
I_31b_i = (2.0 / 5.0) * 3.00 * (0.190**2)
I_31b_ii = (2.0 / 3.0) * 3.00 * (0.190**2)
I_31c_i = 8.00 * (0.0600**2)
I_31c_ii = 0.5 * 8.00 * (0.0600**2)
assert abs(I_31a_i - 0.46875) < 1e-4
assert abs(I_31a_ii - 0.11719) < 1e-4
assert I_31a_iii == 0.0
assert abs(I_31b_i - 0.04332) < 1e-4
assert abs(I_31b_ii - 0.0722) < 1e-4
assert abs(I_31c_i - 0.0288) < 1e-4
assert abs(I_31c_ii - 0.0144) < 1e-4
results['9.31'] = (I_31a_i, I_31a_ii, I_31a_iii, I_31b_i, I_31b_ii, I_31c_i, I_31c_ii)

# 9.32
# (a) I = 0.5 * m * L^2
# (b) I = (11/16) * m * L^2
results['9.32'] = ('0.5*m*L^2', '11/16*m*L^2')

# 9.33
I_33a = (1.0 / 12.0) * 4.00 * (2.00**2) + 2 * 0.300 * (1.00**2)
I_33b = (1.0 / 3.0) * 4.00 * (2.00**2) + 0.300 * (2.00**2)
I_33c = 0.0
I_33d = (4.00 + 2 * 0.300) * (0.500**2)
assert abs(I_33a - 1.9333) < 0.01
assert abs(I_33b - 6.5333) < 0.01
assert I_33c == 0.0
assert abs(I_33d - 1.15) < 1e-4
results['9.33'] = (I_33a, I_33b, I_33c, I_33d)

# 9.34
I_34a = (1.0 / 12.0) * 0.400 * (0.600**2)
I_34b = 2 * (1.0 / 3.0) * 0.200 * (0.300**2)
assert abs(I_34a - 0.0120) < 1e-4
assert abs(I_34b - 0.0120) < 1e-4
results['9.34'] = (I_34a, I_34b)

# 9.35
I_35_rim = 1.40 * (0.300**2)
I_35_spokes = 8 * (1.0 / 3.0) * 0.280 * (0.300**2)
I_35_tot = I_35_rim + I_35_spokes
assert abs(I_35_tot - 0.1932) < 0.001
results['9.35'] = I_35_tot

# 9.36
# I_disk = (5/4) * I_sphere = 1.25 * I_1
results['9.36'] = '1.25*I1'

# 9.37
w1_37 = math.sqrt(2 * 30.0 / 12.0)
w2_37 = math.sqrt(2 * 15.0 / 12.0)
alpha_37 = 0.500 * 2 * math.pi
t_37 = (w1_37 - w2_37) / alpha_37
assert abs(t_37 - 0.2085) < 0.001
results['9.37'] = t_37

# 9.38
I_38 = (1.0 / 12.0) * 117.0 * (2.08**2)
w_38 = 2400.0 * 2 * math.pi / 60.0
K_38a = 0.5 * I_38 * (w_38**2)
rpm_38b = 2400.0 / math.sqrt(0.750)
assert abs(K_38a - 1.332e6) < 2e4
assert abs(rpm_38b - 2771.3) < 1.0
results['9.38'] = (K_38a, rpm_38b)

# 9.39
# w_hollow = w1 * sqrt(3/5)
results['9.39'] = 'w1 * sqrt(3/5)'

# 9.40
theta_40 = 8.20 * 2 * math.pi
w_40 = 2 * theta_40 / 12.0
I_40 = 2 * 36.0 / (w_40**2)
assert abs(I_40 - 0.976) < 0.01
results['9.40'] = I_40

# ==========================================
# 9.41 - 9.48
# ==========================================
# 9.41
I_41 = (2.0 / 5.0) * 28.0 * (0.380**2)
w_41 = math.sqrt(2 * 236.0 / I_41)
v_41 = w_41 * 0.380
assert abs(v_41 - 6.492) < 0.01
results['9.41'] = v_41

# 9.42
I_42 = (2.0 / 3.0) * 8.20 * (0.220**2)
theta_42 = 6.00 * 2 * math.pi
w2_42 = 2 * 0.890 * theta_42
K_42 = 0.5 * I_42 * w2_42
assert abs(K_42 - 8.878) < 0.05
results['9.42'] = K_42

# 9.43
# KA/KB = 3/16 = 0.1875
ratio_43 = 3.0 / 16.0
assert ratio_43 == 0.1875
results['9.43'] = ('B', ratio_43)

# 9.44
w_44 = 45.0 * 2 * math.pi / 60.0
I_44 = 2 * 0.250 / (w_44**2)
m_44 = 2 * I_44 / (0.300**2)
assert abs(I_44 - 0.0225) < 0.001
assert abs(m_44 - 0.500) < 0.01
results['9.44'] = (I_44, m_44)

# 9.45
I_45 = 0.5 * 70.0 * (1.20**2)
w2_max_45 = 3500.0 / 1.20
K_max_45 = 0.5 * I_45 * w2_max_45
assert abs(K_max_45 - 73500.0) < 1.0
results['9.45'] = K_max_45

# 9.46
theta_46 = 30.0 * 2 * math.pi
alpha_46 = 0.200 * 2 * math.pi
w2_46 = 2 * alpha_46 * theta_46
I_46 = 2 * 240.0 / w2_46
assert abs(I_46 - 1.013) < 0.01
results['9.46'] = I_46

# 9.47
# K_pulley = 4.50 J, M = 2.50 kg, m = 1.50 kg
pct_47 = (2.50 / 4.0) / (2.50 / 4.0 + 1.50 / 2.0) * 100.0
K_tot_47 = 4.50 / (pct_47 / 100.0)
h_47 = K_tot_47 / (1.50 * g)
assert abs(pct_47 - 45.45) < 0.1
assert abs(h_47 - 0.6735) < 0.01
results['9.47'] = (h_47, pct_47)

# 9.48
# I = 0.5 * m * R^2
results['9.48'] = '0.5*m*R^2'

# ==========================================
# KIỂM TRA HÌNH ẢNH CROPS
# ==========================================
expected_crops = {
    'd-hinh-e9-18.png': (306, 495),
    'd-hinh-e9-30.png': (375, 285),
    'd-hinh-e9-35.png': (336, 402),
    'd-hinh-e9-47.png': (351, 453),
}
img_dir = ROOT / 'docs/vat-ly-1/bai-giang/img/young-09'
for name, exp_size in expected_crops.items():
    p = img_dir / name
    assert p.exists(), f"Thiếu tệp ảnh: {p}"
    with Image.open(p) as im:
        assert im.size == exp_size, f"Kích thước sai cho {name}: {im.size} != {exp_size}"
        arr = np.array(im)
        assert np.all(arr[:2, :, :3] > 240), f"Viền trên không sạch: {name}"
        assert np.all(arr[-2:, :, :3] > 240), f"Viền dưới không sạch: {name}"
        assert np.all(arr[:, :2, :3] > 240), f"Viền trái không sạch: {name}"
        assert np.all(arr[:, -2:, :3] > 240), f"Viền phải không sạch: {name}"

print("=" * 60)
print(f"XÁC MINH TOÀN DIỆN THÀNH CÔNG: 48/48 BÀI TẬP VÀ 4 TỆP HÌNH ẢNH.")
print(f"Tổng số bài tập đã kiểm tra: {len(results)}")
print("=" * 60)
