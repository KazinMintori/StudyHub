"""Recalculate and verify source data of Exercises 31.1–31.36."""
from pathlib import Path
import math
import json

results = {}

def put(n, **kwargs):
    results[str(n)] = kwargs

# 31.1: I_max = 1.50 A
I_max_1 = 1.50
I_rms_1 = I_max_1 / math.sqrt(2.0)
put(1, I_rms_A=I_rms_1)
assert math.isclose(I_rms_1, 1.06, rel_tol=0.01)

# 31.2: V = 45.0 V
V_2 = 45.0
V_rms_2 = V_2 / math.sqrt(2.0)
V_av_2 = 0.0
put(2, V_rms_V=V_rms_2, V_av_V=V_av_2)
assert math.isclose(V_rms_2, 31.8, rel_tol=0.01)

# 31.3: L = 9.50 mH, V = 45.0 V, I = 3.90 A
L_3 = 9.50e-3
V_3 = 45.0
I_3 = 3.90
XL_3 = V_3 / I_3
f_3 = XL_3 / (2.0 * math.pi * L_3)
put(3, phi_deg=90.0, lead_lag='lead', f_Hz=f_3)
assert math.isclose(f_3, 193.0, rel_tol=0.01)

# 31.4: V = 60.0 V, f = 80.0 Hz, I = 5.30 A
V_4 = 60.0
f_4 = 80.0
I_4 = 5.30
XC_4 = V_4 / I_4
C_4 = 1.0 / (2.0 * math.pi * f_4 * XC_4)
put(4, phi_deg=-90.0, lead_lag='lag', C_F=C_4)
assert math.isclose(C_4, 1.76e-4, rel_tol=0.01)

# 31.5: L = 3.00 H, XL = 120 ohm, C = 4.00 uF, XC = 120 ohm, f = 80.0 Hz
f_5 = 80.0
XL_5a = 2.0 * math.pi * f_5 * 3.00
L_5b = 120.0 / (2.0 * math.pi * f_5)
XC_5c = 1.0 / (2.0 * math.pi * f_5 * 4.00e-6)
C_5d = 1.0 / (2.0 * math.pi * f_5 * 120.0)
put(5, XL_a_ohm=XL_5a, L_b_H=L_5b, XC_c_ohm=XC_5c, C_d_F=C_5d)
assert math.isclose(XL_5a, 1510.0, rel_tol=0.01)
assert math.isclose(L_5b, 0.239, rel_tol=0.01)
assert math.isclose(XC_5c, 497.0, rel_tol=0.01)
assert math.isclose(C_5d, 16.6e-6, rel_tol=0.01)

# 31.6: L = 5.00 mH, C = 3.50 uF
L_6 = 5.00e-3
C_6 = 3.50e-6
omega_6 = 1.0 / math.sqrt(L_6 * C_6)
X_6 = omega_6 * L_6
put(6, omega_rad_per_s=omega_6, X_ohm=X_6)
assert math.isclose(omega_6, 7559.0, rel_tol=0.01)
assert math.isclose(X_6, 37.8, rel_tol=0.01)

# 31.7: L = 0.450 H, C = 2.50 uF, f = 60.0 Hz and 600 Hz
L_7 = 0.450
C_7 = 2.50e-6
XL_7_60 = 2.0 * math.pi * 60.0 * L_7
XL_7_600 = 2.0 * math.pi * 600.0 * L_7
XC_7_60 = 1.0 / (2.0 * math.pi * 60.0 * C_7)
XC_7_600 = 1.0 / (2.0 * math.pi * 600.0 * C_7)
f_7_res = 1.0 / (2.0 * math.pi * math.sqrt(L_7 * C_7))
put(7, XL_60_ohm=XL_7_60, XL_600_ohm=XL_7_600, XC_60_ohm=XC_7_60, XC_600_ohm=XC_7_600, f_res_Hz=f_7_res)
assert math.isclose(XL_7_60, 170.0, rel_tol=0.01)
assert math.isclose(XL_7_600, 1700.0, rel_tol=0.01)
assert math.isclose(XC_7_60, 1060.0, rel_tol=0.01)
assert math.isclose(XC_7_600, 106.0, rel_tol=0.01)
assert math.isclose(f_7_res, 150.0, rel_tol=0.01)

# 31.8: L = 0.450 mH, I = 1.80 mA, V = 12.0 V
L_8 = 0.450e-3
I_8 = 1.80e-3
V_8 = 12.0
f_8 = (V_8 / I_8) / (2.0 * math.pi * L_8)
put(8, f_Hz=f_8)
assert math.isclose(f_8, 2.36e6, rel_tol=0.01)

# 31.9: L = 0.180 H, R = 90.0 ohm, vL = -(12.0 V) sin((480 rad/s) t)
L_9 = 0.180
R_9 = 90.0
omega_9 = 480.0
VL_9 = 12.0
I_9 = VL_9 / (omega_9 * L_9)
VR_9 = I_9 * R_9
t_9 = 2.00e-3
vR_2ms_9 = VR_9 * math.cos(omega_9 * t_9)
put(9, VR_amp_V=VR_9, vR_2ms_V=vR_2ms_9)
assert math.isclose(VR_9, 12.5, rel_tol=0.01)
assert math.isclose(vR_2ms_9, 7.17, rel_tol=0.01)

# 31.10: R = 250 ohm, C = 4.80 uF, vC = (7.60 V) sin((120 rad/s) t)
R_10 = 250.0
C_10 = 4.80e-6
omega_10 = 120.0
VC_10 = 7.60
XC_10 = 1.0 / (omega_10 * C_10)
VR_10 = (VC_10 / XC_10) * R_10
put(10, XC_ohm=XC_10, VR_amp_V=VR_10)
assert math.isclose(XC_10, 1736.0, rel_tol=0.01)
assert math.isclose(VR_10, 1.09, rel_tol=0.01)

# 31.11: R = 150 ohm, L = 0.250 H, vR = (3.80 V) cos((720 rad/s) t)
R_11 = 150.0
L_11 = 0.250
omega_11 = 720.0
VR_11 = 3.80
I_11 = VR_11 / R_11
XL_11 = omega_11 * L_11
VL_11 = I_11 * XL_11
put(11, I_amp_A=I_11, XL_ohm=XL_11, VL_amp_V=VL_11)
assert math.isclose(I_11, 0.0253, rel_tol=0.01)
assert math.isclose(XL_11, 180.0, rel_tol=0.01)
assert math.isclose(VL_11, 4.56, rel_tol=0.01)

# 31.12: R = 200 ohm, L = 0.400 H, V = 30.0 V, omega = 250 rad/s
R_12 = 200.0
L_12 = 0.400
omega_12 = 250.0
V_12 = 30.0
XL_12 = omega_12 * L_12
Z_12 = math.sqrt(R_12**2 + XL_12**2)
I_12 = V_12 / Z_12
VR_12 = I_12 * R_12
VL_12 = I_12 * XL_12
phi_12 = math.degrees(math.atan(XL_12 / R_12))
put(12, Z_ohm=Z_12, I_A=I_12, VR_V=VR_12, VL_V=VL_12, phi_deg=phi_12)
assert math.isclose(Z_12, 224.0, rel_tol=0.01)
assert math.isclose(I_12, 0.134, rel_tol=0.01)
assert math.isclose(phi_12, 26.6, rel_tol=0.01)

# 31.13: Same as 31.12 + C = 6.00 uF
C_13 = 6.00e-6
XC_13 = 1.0 / (omega_12 * C_13)
Z_13 = math.sqrt(R_12**2 + (XL_12 - XC_13)**2)
I_13 = V_12 / Z_13
phi_13 = math.degrees(math.atan((XL_12 - XC_13) / R_12))
VR_13 = I_13 * R_12
VL_13 = I_13 * XL_12
VC_13 = I_13 * XC_13
put(13, Z_ohm=Z_13, I_A=I_13, phi_deg=phi_13, VR_V=VR_13, VL_V=VL_13, VC_V=VC_13)
assert math.isclose(Z_13, 601.0, rel_tol=0.01)
assert math.isclose(I_13, 0.0499, rel_tol=0.01)
assert math.isclose(phi_13, -70.6, rel_tol=0.01)
assert math.isclose(VR_13, 9.98, rel_tol=0.01)
assert math.isclose(VL_13, 4.99, rel_tol=0.01)
assert math.isclose(VC_13, 33.3, rel_tol=0.01)

# 31.14: R = 200 ohm, L = 0.900 H, C = 6.00 uF, V = 30.0 V, omega = 250 rad/s
L_14 = 0.900
XL_14 = omega_12 * L_14
XC_14 = 1.0 / (omega_12 * C_13)
Z_14 = math.sqrt(R_12**2 + (XL_14 - XC_14)**2)
I_14 = V_12 / Z_14
VR_14 = I_14 * R_12
VL_14 = I_14 * XL_14
VC_14 = I_14 * XC_14
put(14, VR_V=VR_14, VL_V=VL_14, VC_V=VC_14, V_sum=VR_14+VL_14+VC_14)
assert math.isclose(VR_14, 12.4, rel_tol=0.01)
assert math.isclose(VL_14, 13.9, rel_tol=0.01)
assert math.isclose(VC_14, 41.2, rel_tol=0.01)

# 31.15: VR_rms = 30.0 V, VC_rms = 90.0 V, VL_rms = 50.0 V
Vrms_15 = math.sqrt(30.0**2 + (50.0 - 90.0)**2)
put(15, Vrms_V=Vrms_15)
assert math.isclose(Vrms_15, 50.0, rel_tol=1e-4)

# 31.16: VL = 180 V, VC = 120 V, VR = 160 V, vL = 80.0 V
vC_16 = - (120.0 / 180.0) * 80.0
vR_16 = 160.0 * math.sqrt(1.0 - (80.0 / 180.0)**2)
put(16, vC_V=vC_16, vR_mag_V=vR_16)
assert math.isclose(vC_16, -53.3, rel_tol=0.01)
assert math.isclose(vR_16, 143.3, rel_tol=0.01)

# 31.17: V = 240 V, VL = 310 V, VC = 180 V
diff_17 = 310.0 - 180.0
VR_17 = math.sqrt(240.0**2 - diff_17**2)
phi_17 = math.degrees(math.atan(diff_17 / VR_17))
put(17, VR_V=VR_17, phi_deg=phi_17)
assert math.isclose(phi_17, 32.8, rel_tol=0.01)

# 31.18: R = 300 ohm, V = 500 V, Pav = 286 W
R_18 = 300.0
V_18 = 500.0
Pav_18 = 286.0
I_18 = math.sqrt(2.0 * Pav_18 / R_18)
Z_18 = V_18 / I_18
XL_18 = math.sqrt(Z_18**2 - R_18**2)
VL_18 = I_18 * XL_18
pf_18 = R_18 / Z_18
put(18, Z_ohm=Z_18, VL_V=VL_18, pf=pf_18)
assert math.isclose(Z_18, 362.0, rel_tol=0.01)
assert math.isclose(VL_18, 280.0, rel_tol=0.01)
assert math.isclose(pf_18, 0.828, rel_tol=0.01)

# 31.19: Vrms = 120 V, Pav = 20.0 W
pmax_19 = 2.0 * 20.0
Irms_19 = 20.0 / 120.0
R_19 = 120.0**2 / 20.0
put(19, pmax_W=pmax_19, Irms_A=Irms_19, R_ohm=R_19)
assert math.isclose(pmax_19, 40.0, rel_tol=1e-4)
assert math.isclose(Irms_19, 0.167, rel_tol=0.01)
assert math.isclose(R_19, 720.0, rel_tol=1e-4)

# 31.20: L = 20.0 mH, C = 140 nF, R = 350 ohm, Vrms = 120 V, f = 1.25 kHz
omega_20 = 2.0 * math.pi * 1250.0
XL_20 = omega_20 * 0.0200
XC_20 = 1.0 / (omega_20 * 140e-9)
Z_20 = math.sqrt(350.0**2 + (XL_20 - XC_20)**2)
Irms_20 = 120.0 / Z_20
Pav_20 = Irms_20**2 * 350.0
put(20, P_gen_W=Pav_20, P_res_W=Pav_20)
assert math.isclose(Pav_20, 7.32, rel_tol=0.01)

# 31.21: V = 120 V, phi = 53.1 deg, Pav = 80.0 W
V_21 = 120.0
phi_21 = math.radians(53.1)
Pav_21 = 80.0
R_21 = (V_21 * math.cos(phi_21))**2 / (2.0 * Pav_21)
put(21, R_ohm=R_21)
assert math.isclose(R_21, 32.4, rel_tol=0.01)

# 31.22: V = 900 V, omega = 20.0 rad/s, VC = 500 V, R = 300 ohm
VR_22 = math.sqrt(900.0**2 - 500.0**2)
I_22 = VR_22 / 300.0
XC_22 = 500.0 / I_22
C_22 = 1.0 / (20.0 * XC_22)
Pav_22 = 0.5 * I_22**2 * 300.0
put(22, VR_V=VR_22, C_F=C_22, Pav_W=Pav_22)
assert math.isclose(VR_22, 748.0, rel_tol=0.01)
assert math.isclose(C_22, 2.49e-4, rel_tol=0.01)
assert math.isclose(Pav_22, 933.0, rel_tol=0.01)

# 31.23: L = 0.120 H, R = 240 ohm, C = 7.30 uF, Irms = 0.450 A, f = 400 Hz
omega_23 = 2.0 * math.pi * 400.0
XL_23 = omega_23 * 0.120
XC_23 = 1.0 / (omega_23 * 7.30e-6)
phi_23_rad = math.atan((XL_23 - XC_23) / 240.0)
phi_23_deg = math.degrees(phi_23_rad)
pf_23 = math.cos(phi_23_rad)
Z_23 = math.sqrt(240.0**2 + (XL_23 - XC_23)**2)
Vrms_23 = 0.450 * Z_23
Pav_23 = 0.450**2 * 240.0
put(23, phi_deg=phi_23_deg, pf=pf_23, Z_ohm=Z_23, Vrms_V=Vrms_23, Pav_W=Pav_23)
assert math.isclose(phi_23_deg, 45.8, rel_tol=0.01)
assert math.isclose(pf_23, 0.697, rel_tol=0.01)
assert math.isclose(Z_23, 344.0, rel_tol=0.01)
assert math.isclose(Vrms_23, 155.0, rel_tol=0.01)
assert math.isclose(Pav_23, 48.6, rel_tol=0.01)

# 31.24: f = 120 Hz, Vrms = 80.0 V, R = 75.0 ohm, Z = 105 ohm
Pav_24 = (80.0 / 105.0)**2 * 75.0
put(24, Pav_W=Pav_24)
assert math.isclose(Pav_24, 43.5, rel_tol=0.01)

# 31.25: R = 250 ohm, L = 15 mH, C = 3.5 uF, V = 45 V, omega = 360 rad/s
omega_25 = 360.0
XL_25 = omega_25 * 0.015
XC_25 = 1.0 / (omega_25 * 3.5e-6)
Z_25 = math.sqrt(250.0**2 + (XL_25 - XC_25)**2)
pf_25 = 250.0 / Z_25
Pav_25 = 0.5 * (45.0 / Z_25)**2 * 250.0
put(25, pf=pf_25, Pav_W=Pav_25)
assert math.isclose(pf_25, 0.302, rel_tol=0.01)
assert math.isclose(Pav_25, 0.370, rel_tol=0.01)

# 31.26: Resonance: XC = 200 ohm, VC = 600 V, R = 300 ohm
V_26 = (600.0 / 200.0) * 300.0
put(26, V_V=V_26)
assert math.isclose(V_26, 900.0, rel_tol=1e-4)

# 31.27: R = 200 ohm, L = 0.400 H, C = 5.00 uF, V = 3.00 V
omega_27 = 1.0 / math.sqrt(0.400 * 5.00e-6)
f_27 = omega_27 / (2.0 * math.pi)
I_27_res = 3.00 / 200.0
XL_27_b = 400.0 * 0.400
XC_27_b = 1.0 / (400.0 * 5.00e-6)
Z_27_b = math.sqrt(200.0**2 + (XL_27_b - XC_27_b)**2)
I_27_b = 3.00 / Z_27_b
put(27, f_res_Hz=f_27, I_res_A=I_27_res, I_400_A=I_27_b)
assert math.isclose(f_27, 113.0, rel_tol=0.01)
assert math.isclose(I_27_res, 0.0150, rel_tol=1e-4)
assert math.isclose(I_27_b, 7.61e-3, rel_tol=0.01)

# 31.28: R = 175 ohm, C = 12.5 uF, L = 8.00 mH, V = 25.0 V
omega_0_28 = 1.0 / math.sqrt(8.00e-3 * 12.5e-6)
I_28_max = 25.0 / 175.0
vL_half_28 = (I_28_max * omega_0_28 * 8.00e-3) * math.sqrt(3.0) / 2.0
put(28, omega_0_rad_per_s=omega_0_28, Z_ohm=175.0, I_max_A=I_28_max, v_source_half_V=12.5, vR_half_V=12.5, vL_half_mag_V=vL_half_28)
assert math.isclose(omega_0_28, 3162.0, rel_tol=0.01)
assert math.isclose(I_28_max, 0.143, rel_tol=0.01)
assert math.isclose(vL_half_28, 3.13, rel_tol=0.01)

# 31.29: R = 300 ohm, L = 0.400 H, C = 6.00e-8 F, I = 0.500 A at resonance
V_29 = 0.500 * 300.0
omega_29 = 1.0 / math.sqrt(0.400 * 6.00e-8)
VL_29 = 0.500 * omega_29 * 0.400
Pav_29 = 0.5 * 0.500 * V_29
put(29, V_V=V_29, VR_V=V_29, VL_V=VL_29, VC_V=VL_29, Pav_W=Pav_29)
assert math.isclose(V_29, 150.0, rel_tol=1e-4)
assert math.isclose(VL_29, 1290.0, rel_tol=0.01)
assert math.isclose(Pav_29, 37.5, rel_tol=1e-4)

# 31.30: V = 120 V, omega = 50.0 rad/s, R = 400 ohm, L = 3.00 H
C_30 = 1.0 / (50.0**2 * 3.00)
VL_30 = (120.0 / 400.0) * (50.0 * 3.00)
put(30, C_F=C_30, VL_V=VL_30)
assert math.isclose(C_30, 1.33e-4, rel_tol=0.01)
assert math.isclose(VL_30, 45.0, rel_tol=1e-4)

# 31.31: R = 150 ohm, L = 0.750 H, C = 0.0180 uF, V = 150 V at resonance
Pav_31 = 0.5 * 150.0**2 / 150.0
put(31, pf=1.00, Pav_W=Pav_31, Pav_new_W=Pav_31)
assert math.isclose(Pav_31, 75.0, rel_tol=1e-4)

# 31.32: R = 400 ohm, L = 0.600 H, C = 5.00e-8 F, V = 80.0 V at resonance
Pav_32 = 0.5 * 80.0**2 / 400.0
put(32, Pav_W=Pav_32)
assert math.isclose(Pav_32, 8.00, rel_tol=1e-4)

# 31.33: L = 0.280 H, C = 4.00 uF, V = 120 V, I = 1.70 A at resonance
omega_33 = 1.0 / math.sqrt(0.280 * 4.00e-6)
R_33 = 120.0 / 1.70
VL_33 = 1.70 * omega_33 * 0.280
put(33, omega_0_rad_per_s=omega_33, R_ohm=R_33, VL_V=VL_33)
assert math.isclose(omega_33, 945.0, rel_tol=0.01)
assert math.isclose(R_33, 70.6, rel_tol=0.01)
assert math.isclose(VL_33, 450.0, rel_tol=0.01)

# 31.34: 1600 W at 120 V (rms), line 240 V
I1_34 = 1600.0 / 240.0
R_app_34 = 240.0**2 / 1600.0
put(34, I1_A=I1_34, R_app_ohm=R_app_34)
assert math.isclose(I1_34, 6.67, rel_tol=0.01)
assert math.isclose(R_app_34, 36.0, rel_tol=1e-4)

# 31.35: V1 = 120 V, V2 = 12.0 V, R2 = 5.00 ohm
N_ratio_35 = 120.0 / 12.0
I2_35 = 12.0 / 5.00
Pav_35 = 12.0 * I2_35
R_eff_35 = N_ratio_35**2 * 5.00
put(35, N1_div_N2=N_ratio_35, I2_A=I2_35, Pav_W=Pav_35, R_eff_ohm=R_eff_35)
assert math.isclose(N_ratio_35, 10.0, rel_tol=1e-4)
assert math.isclose(I2_35, 2.40, rel_tol=1e-4)
assert math.isclose(Pav_35, 28.8, rel_tol=1e-4)
assert math.isclose(R_eff_35, 500.0, rel_tol=1e-4)

# 31.36: V1 = 120 V, V2 = 13000 V, I2 = 8.50 mA
N_ratio_36 = 13000.0 / 120.0
Pav_36 = 13000.0 * 8.50e-3
I1_36 = N_ratio_36 * 8.50e-3
put(36, N2_div_N1=N_ratio_36, Pav_W=Pav_36, I1_A=I1_36)
assert math.isclose(N_ratio_36, 108.33, rel_tol=0.01)
assert math.isclose(Pav_36, 110.5, rel_tol=0.01)
assert math.isclose(I1_36, 0.921, rel_tol=0.01)


# Independently sample instantaneous voltages, signs and energy accounting.
phi_14 = math.atan2(XL_14-XC_14,R_12)
t_14 = .020
vR_14 = VR_14*math.cos(omega_12*t_14)
vL_14 = -VL_14*math.sin(omega_12*t_14)
vC_14 = VC_14*math.sin(omega_12*t_14)
v_14 = V_12*math.cos(omega_12*t_14+phi_14)
assert math.isclose(vR_14,3.5103838227434454,abs_tol=1e-12)
assert math.isclose(vL_14,13.350268339278156,abs_tol=1e-12)
assert math.isclose(vC_14,-39.55635063489824,abs_tol=1e-12)
assert math.isclose(v_14,-22.69569847287664,abs_tol=1e-12)
assert math.isclose(vR_14+vL_14+vC_14,v_14,abs_tol=1e-12)
results['14'].update(phaseOrigin='current',v_source_V=v_14,vR_V=vR_14,vL_V=vL_14,vC_V=vC_14)
for sign in [-1,1]:
    vR_signed = sign*vR_16
    assert math.isclose((vR_signed/160)**2+(80/180)**2,1,abs_tol=1e-12)
results['16']['vR_possible_V']=[-vR_16,vR_16]
for angle in [-math.pi/3,math.pi/3]:
    current=I_28_max*math.cos(angle)
    vL=-I_28_max*omega_0_28*8e-3*math.sin(angle)
    vC=I_28_max/(omega_0_28*12.5e-6)*math.sin(angle)
    assert math.isclose(current,I_28_max/2,abs_tol=1e-12)
    assert math.isclose(vL+vC,0,abs_tol=1e-12)
results['28']['vL_possible_V']=[-vL_half_28,vL_half_28]
assert len(results)==36

# Write output report
qa_dir = Path(__file__).resolve().parents[2] / 'qa/physics/chapter31'
qa_dir.mkdir(parents=True, exist_ok=True)
qa_file = qa_dir / 'exercises-01-36-data-checks.json'
qa_data = {
    'status': 'passed',
    'sourcePagesReviewed': 'printed pages 1042–1044 (PDF1062–1064), supplied PDF checked visually',
    'results': results
}
qa_file.write_text(json.dumps(qa_data, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
print('Recalculated all 36 exercises (31.1–31.36) successfully.')
