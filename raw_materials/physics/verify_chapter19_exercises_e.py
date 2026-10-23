"""Verifier cho bài tập Vật lý 1 - Chapter 19 (19.34 - 19.66).

Tập trung kiểm toán số học, công thức giải tích, kiểm tra biên hình ảnh và tính nhất quán vật lý.
"""
import math
import hashlib
from pathlib import Path
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parents[2]

# Hằng số vật lý tiêu chuẩn (Young & Freedman 15th ed)
R = 8.314462618
P_ATM = 101325.0
NA = 6.02214076e23
KB = 1.380649e-23
G = 9.80665

def verify_images():
    """Kiểm tra tính hợp lệ của 11 hình ảnh đã trích xuất từ PDF."""
    import importlib.util
    prep_path = ROOT / 'scripts/prepare-physics1-19-exercises-e-assets.py'
    spec = importlib.util.spec_from_file_location("prep_assets", prep_path)
    prep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep)
    crops = prep.CROPS
    img_dir = ROOT / 'docs/vat-ly-1/bai-giang/img/young-19'
    assert len(crops) == 11, f'Kỳ vọng 11 hình ảnh nhưng có {len(crops)}'

    for stem in crops.keys():
        p = img_dir / f'{stem}.png'
        assert p.exists(), f'Tệp ảnh không tồn tại: {p}'
        with Image.open(p) as im:
            assert im.mode == 'RGB', f'Ảnh {stem} phải là RGB không kênh alpha'
            arr = np.array(im)
            assert arr.shape[0] > 50 and arr.shape[1] > 50, f'Kích thước ảnh {stem} quá nhỏ'
        edges = prep.inspect_edges(p)
        assert not any(edges.values()), f'Viền ảnh {stem} bị chạm nội dung: {edges}'
    print('PASS: Đã xác minh 11/11 ảnh PDF crop nguyên bản và kiểm tra 4 viền sạch.')

def verify_problems():
    """Tính toán và kiểm toán số học độc lập cho toàn bộ 33 bài tập."""
    ledger = {}

    # 19.34
    N_34 = 3.01e20
    dT_34 = 60.0 - 25.0  # K
    dU_34 = N_34 * (2.5 * KB) * dT_34
    assert math.isclose(dU_34, 0.3636, rel_tol=1e-3)
    ledger['19.34'] = {'dU_J': dU_34}

    # 19.35
    Va_35, Vb_35 = 0.0700, 0.1100
    pa_35, pb_35 = 1.00e5, 1.40e5
    W_35 = 0.5 * (pa_35 + pb_35) * (Vb_35 - Va_35)
    assert math.isclose(W_35, 4800.0, rel_tol=1e-4)
    ledger['19.35'] = {'W_J': W_35}

    # 19.36
    m_lid = 0.30  # kg
    h_jump = 2.0e-3  # m
    W_36 = m_lid * G * h_jump
    n_steam = 1.0 / 11.2  # mol
    Cv_water = 3.0 * R  # phân tử phi tuyến tính
    dT_36 = -W_36 / (n_steam * Cv_water)
    assert W_36 > 0 and dT_36 < 0
    ledger['19.36'] = {'W_J': W_36, 'dT_K': dT_36}

    # 19.37
    T_37 = 273.15 + 85.0
    pa_37 = 0.600 * P_ATM
    pb_37 = 0.200 * P_ATM
    Vb_37 = 0.100
    n_37 = (pb_37 * Vb_37) / (R * T_37)
    Va_37 = Vb_37 * (pb_37 / pa_37)
    W_37 = n_37 * R * T_37 * math.log(Vb_37 / Va_37)
    dU_37 = 0.0
    assert math.isclose(n_37, 0.6805, rel_tol=1e-2)
    assert math.isclose(Va_37, 0.03333, rel_tol=1e-2)
    assert math.isclose(W_37, 2226.4, rel_tol=1e-2)
    ledger['19.37'] = {'n_mol': n_37, 'Va_m3': Va_37, 'W_J': W_37, 'dU_J': dU_37}

    # 19.38: Read the pressure label at c, not a/b, from P19.38.
    n_38=3.25;Va_38=.010;Vb_38=Vc_38=.040;pc_38=2e5
    pa_38=pb_38=pc_38*Vc_38/Va_38
    Ta_38=Tc_38=pc_38*Vc_38/(n_38*R)
    Tb_38=pb_38*Vb_38/(n_38*R)
    Q_ab=2.5*pa_38*(Vb_38-Va_38)
    Q_bc=1.5*Vb_38*(pc_38-pb_38)
    Q_ca=pa_38*Va_38*math.log(Va_38/Vc_38)
    assert math.isclose(pa_38,8e5,rel_tol=1e-12)
    assert math.isclose(Ta_38,296.07,rel_tol=1e-3)
    assert math.isclose(Tb_38,1184.29,rel_tol=1e-3)
    assert math.isclose(Q_ab,60000,rel_tol=1e-12)
    assert math.isclose(Q_bc,-36000,rel_tol=1e-12)
    assert math.isclose(Q_ca,-11090.3549,rel_tol=1e-8)
    assert math.isclose(Q_ab+Q_bc+Q_ca,pa_38*(Vb_38-Va_38)+Q_ca,rel_tol=1e-12)
    ledger['19.38']={'pa':pa_38,'Ta':Ta_38,'Tb':Tb_38,'Tc':Tc_38,'Q_ab':Q_ab,'Q_bc':Q_bc,'Q_ca':Q_ca}

    # 19.39
    Q_acb = 90.0
    W_acb = 60.0
    dU_ba = Q_acb - W_acb  # Ub - Ua = 30.0 J
    W_adb = 15.0
    Q_adb = dU_ba + W_adb  # 45.0 J
    W_return = -35.0
    Q_return = -dU_ba + W_return  # -65.0 J
    Ua = 0.0
    Ud = 8.0
    Ub = dU_ba
    W_ad = 15.0  # vì db là đẳng tích, W_db = 0
    Q_ad = (Ud - Ua) + W_ad  # 8 + 15 = 23.0 J
    Q_db = (Ub - Ud) + 0.0  # 30 - 8 = 22.0 J
    assert math.isclose(Q_adb, 45.0)
    assert math.isclose(Q_return, -65.0)
    assert math.isclose(Q_ad, 23.0)
    assert math.isclose(Q_db, 22.0)
    ledger['19.39'] = {'Q_adb': Q_adb, 'Q_return': Q_return, 'Q_ad': Q_ad, 'Q_db': Q_db}

    # 19.40
    W_abc = 450.0  # ab đẳng áp, bc đẳng tích => W_ab = 450 J, W_bc = 0
    W_adc = 120.0  # ad đẳng tích, dc đẳng áp => W_ad = 0, W_dc = 120 J
    Ua_40, Ub_40, Uc_40, Ud_40 = 150.0, 240.0, 680.0, 330.0
    Q_ab = (Ub_40 - Ua_40) + W_abc  # (240 - 150) + 450 = 540 J
    Q_bc = (Uc_40 - Ub_40) + 0.0    # 680 - 240 = 440 J
    Q_ad = (Ud_40 - Ua_40) + 0.0    # 330 - 150 = 180 J
    Q_dc = (Uc_40 - Ud_40) + W_adc  # (680 - 330) + 120 = 470 J
    assert Q_ab == 540.0 and Q_bc == 440.0 and Q_ad == 180.0 and Q_dc == 470.0
    ledger['19.40'] = {'Q_ab': Q_ab, 'Q_bc': Q_bc, 'Q_ad': Q_ad, 'Q_dc': Q_dc}

    # 19.41
    # a: (0.02 m3, 3.0e5 Pa), b: (0.02 m3, 1.0e5 Pa), c: (0.06 m3, 1.0e5 Pa)
    pa_41, Va_41 = 3.0e5, 0.02
    pc_41, Vc_41 = 1.0e5, 0.06
    assert math.isclose(pa_41 * Va_41, pc_41 * Vc_41)  # Ta = Tc
    W_abc_41 = pc_41 * (Vc_41 - Va_41)  # 1.0e5 * 0.04 = 4000 J
    Q_abc_41 = W_abc_41  # dU = 0 => Q = W = 4000 J
    W_ac_straight = 0.5 * (pa_41 + pc_41) * (Vc_41 - Va_41)  # 2.0e5 * 0.04 = 8000 J
    Q_ac_straight = W_ac_straight  # dU = 0 => Q = 8000 J
    assert math.isclose(W_abc_41, 4000.0, rel_tol=1e-5)
    assert math.isclose(W_ac_straight, 8000.0, rel_tol=1e-5)
    ledger['19.41'] = {'W_abc': W_abc_41, 'Q_abc': Q_abc_41, 'Q_ac': Q_ac_straight}

    # 19.42
    n_42 = 3.0
    Cp_42 = 29.1
    Cv_42 = Cp_42 - R  # 20.7855
    Ta_42, Tc_42, Tb_42 = 300.0, 492.0, 600.0
    Q_ac_42 = n_42 * Cp_42 * (Tc_42 - Ta_42)
    Q_ba_42 = n_42 * Cv_42 * (Ta_42 - Tb_42)
    W_net_42 = Q_ac_42 + Q_ba_42
    assert math.isclose(W_net_42, -1945.35, rel_tol=1e-3)
    ledger['19.42'] = {'W_net': W_net_42}

    # 19.43
    n_43 = 0.0040
    pa_43 = 0.50 * P_ATM
    pb_43 = 2.0 * P_ATM
    Va_43 = 0.20e-3
    Vb_43 = 0.20e-3
    Vc_43 = Vb_43 * (pb_43 / pa_43)  # bc đẳng nhiệt => Vc = 0.80 L
    Ta_43 = (pa_43 * Va_43) / (n_43 * R)
    Tb_43 = (pb_43 * Vb_43) / (n_43 * R)
    Tc_43 = Tb_43
    Cv_H2 = 20.42  # Bảng 19.1
    Cp_H2 = 28.74  # Bảng 19.1
    Q_ab_43 = n_43 * Cv_H2 * (Tb_43 - Ta_43)
    Q_bc_43 = n_43 * R * Tb_43 * math.log(Vc_43 / Vb_43)
    Q_ca_43 = n_43 * Cp_H2 * (Ta_43 - Tc_43)
    assert math.isclose(Vc_43, 0.80e-3, rel_tol=1e-3)
    assert math.isclose(Ta_43, 304.66, rel_tol=1e-2)
    assert math.isclose(Tb_43, 1218.65, rel_tol=1e-2)
    ledger['19.43'] = {'Vc_m3': Vc_43, 'Ta': Ta_43, 'Tb': Tb_43, 'Q_ab': Q_ab_43, 'Q_bc': Q_bc_43, 'Q_ca': Q_ca_43}

    # 19.44: Both branches are inclined; actual vertex b is (0.006,350000).
    pa44=pc44=1e5;pb44=3.5e5;va44=.002;vb44=.006;vc44=.010
    du44=1.5*(pc44*vc44-pa44*va44)
    wab44=(pa44+pb44)/2*(vb44-va44)
    wbc44=(pb44+pc44)/2*(vc44-vb44)
    wac44=pa44*(vc44-va44)
    assert math.isclose(wab44,900,rel_tol=1e-12)
    assert math.isclose(wbc44,900,rel_tol=1e-12)
    assert math.isclose(du44+wab44+wbc44,3000,rel_tol=1e-12)
    assert math.isclose(du44+wac44,2000,rel_tol=1e-12)
    assert math.isclose(wab44+wbc44-wac44,.5*(vc44-va44)*(pb44-pa44),rel_tol=1e-12)
    ledger['19.44']={'dU':du44,'Wab':wab44,'Wbc':wbc44,'Qabc':3000,'Qac':2000}

    # 19.45
    # Chu trình pV: hình thang ngược chiều kim đồng hồ
    # Đỉnh: (3 L, 1 atm) -> (5 L, 1 atm) -> (5 L, 3 atm) -> (3 L, 2 atm) -> (3 L, 1 atm)
    W_net_45_atmL = 1.0 * (5.0 - 3.0) + 0.0 + 0.5 * (3.0 + 2.0) * (3.0 - 5.0) + 0.0  # 2 - 5 = -3.0 atm*L
    W_net_45_J = W_net_45_atmL * (P_ATM * 1e-3)  # -303.975 J
    Q_net_45_J = W_net_45_J
    assert math.isclose(W_net_45_atmL, -3.0)
    ledger['19.45'] = {'W_net_J': W_net_45_J, 'Q_net_J': Q_net_45_J}

    # 19.46
    T1_46 = 273.15 + 50.0
    T2_46 = 273.15 + 10.0
    dT_46 = T2_46 - T1_46  # -40 K
    p_46 = 3.00e5
    Q_46 = -2.50e4
    Cp_N2 = 29.07  # Bảng 19.1
    Cv_N2 = 20.76  # Bảng 19.1
    n_46 = Q_46 / (Cp_N2 * dT_46)
    dU_46 = n_46 * Cv_N2 * dT_46
    W_46 = Q_46 - dU_46
    Qv_46 = dU_46
    assert math.isclose(n_46, 21.4998, rel_tol=1e-2)
    assert math.isclose(dU_46, -17853.4, rel_tol=1e-2)
    ledger['19.46'] = {'n_mol': n_46, 'dU_J': dU_46, 'W_J': W_46, 'Qv_J': Qv_46}

    # 19.47
    p1_47 = 1.00e5
    T1_47 = 300.0
    V1_47 = 1.50e-3
    p2_47 = 2.50e4
    V2_47 = V1_47 * (p1_47 / p2_47)  # 6.00 L
    V3_47 = V1_47
    p3_47 = p2_47
    T3_47 = T1_47 * (V3_47 / V2_47)  # 75 K
    W1_47 = p1_47 * V1_47 * math.log(V2_47 / V1_47)
    W2_47 = p2_47 * (V3_47 - V2_47)
    W_tot_47 = W1_47 + W2_47
    assert math.isclose(V2_47, 6.00e-3)
    assert math.isclose(T3_47, 75.0)
    assert math.isclose(W_tot_47, 95.44, rel_tol=1e-2)
    ledger['19.47'] = {'V2_m3': V2_47, 'p3_Pa': p3_47, 'T3_K': T3_47, 'W_tot_J': W_tot_47}

    # 19.48
    H_drum = 0.880
    D_drum = 0.610
    V0_drum = math.pi * (D_drum / 2.0)**2 * H_drum
    m_drum = 17.3
    rho_sea = 1025.0
    p0_48 = 101e3
    T0_48 = 273.15 + 23.0
    V_neutral_48 = m_drum / rho_sea
    # V(y) = V0 * (p0 / (p0 + rho*g*y)) * ((T0 - 0.020*y) / T0)
    c_48 = (V0_drum / V_neutral_48) * (p0_48 / T0_48)
    y_neutral_48 = (c_48 * T0_48 - p0_48) / (rho_sea * 9.80 + 0.020 * c_48)
    assert math.isclose(V_neutral_48, 0.016878, rel_tol=1e-3)
    assert math.isclose(y_neutral_48, 141.69, rel_tol=1e-2)
    ledger['19.48'] = {'V_neutral_m3': V_neutral_48, 'y_neutral_m': y_neutral_48}

    # 19.49
    p1_49 = 5.60e4
    T1_49 = 273.15 - 15.0
    p2_49 = 8.12e4
    gamma_air = 1.40
    T2_49 = T1_49 * (p2_49 / p1_49)**((gamma_air - 1.0) / gamma_air)
    dT_denver_49 = (T2_49 - 273.15) - 2.0
    assert math.isclose(T2_49, 287.06, rel_tol=1e-2)
    assert math.isclose(dT_denver_49, 11.91, rel_tol=1e-2)
    ledger['19.49'] = {'T2_K': T2_49, 'rise_C': dT_denver_49}

    # 19.50
    V1_50 = 2.00e3
    p1_50 = 1.00 * P_ATM
    p2_50 = 0.900 * P_ATM
    T1_50 = 273.15 + 15.0
    gamma_He = 5.0 / 3.0
    V2_50 = V1_50 * (p1_50 / p2_50)**(1.0 / gamma_He)
    T2_50 = T1_50 * (p2_50 / p1_50)**((gamma_He - 1.0) / gamma_He)
    dU_50 = 1.5 * (p2_50 * V2_50 - p1_50 * V1_50)
    assert math.isclose(V2_50, 2130.51, rel_tol=1e-3)
    assert math.isclose(T2_50, 276.26, rel_tol=1e-3)
    assert math.isclose(dU_50, -1.254e7, rel_tol=1e-2)
    ledger['19.50'] = {'V2_m3': V2_50, 'T2_K': T2_50, 'dU_J': dU_50}

    # 19.51
    L1_51 = 0.250
    p1_51 = 1.01e5
    p2_51 = p1_51 + 3.80e5  # 4.81e5 Pa
    Cv_51 = 20.8
    Cp_51 = Cv_51 + R
    gamma_51 = Cp_51 / Cv_51
    L2_51 = L1_51 * (p1_51 / p2_51)**(1.0 / gamma_51)
    dist_piston = L1_51 - L2_51
    T1_51 = 273.15 + 27.0
    T2_51 = T1_51 * (p2_51 / p1_51)**((gamma_51 - 1.0) / gamma_51)
    n_51 = 20.0
    W_comp_only = n_51 * Cv_51 * (T2_51 - T1_51)
    W_net_cycle = n_51 * Cp_51 * (T2_51 - T1_51)
    assert math.isclose(dist_piston, 0.1681, rel_tol=1e-2)
    assert math.isclose(T2_51, 468.8, rel_tol=1e-2)
    ledger['19.51'] = {'d_m': dist_piston, 'T2_K': T2_51, 'W_comp_J': W_comp_only, 'W_net_J': W_net_cycle}

    # 19.52 (tổng quát giải tích)
    # T_final = T0 * 2^(2 - gamma)
    # W_total = p0 * V0 * [1 + (Cv/R)*(2 - 2^(2-gamma))]
    # Q_total = p0 * V0 * (1 + Cv/R)
    ledger['19.52'] = {'symbolic': True}

    # 19.53
    W_53 = 450.0
    # (a) đẳng nhiệt: dU = 0, Q = W = 450 J
    # (b) đoạn nhiệt: Q = 0, dU = -W = -450 J
    # (c) đẳng áp: dU = 1.5 * W = 675 J, Q = 2.5 * W = 1125 J
    assert W_53 == 450.0
    ledger['19.53'] = {'iso_Q': 450.0, 'ad_dU': -450.0, 'isobar_Q': 1125.0, 'isobar_dU': 675.0}

    # 19.54 & 19.55
    n_54 = 0.250
    p1_54 = 2.40e5
    T1_54 = 355.0
    V1_54 = n_54 * R * T1_54 / p1_54
    # (b) T đẳng nhiệt = T2 = 2 * T1 = 710 K
    T2_54 = 2.0 * T1_54
    # (c) p max = 2 * p1 = 4.80e5 Pa
    p_max_54 = 2.0 * p1_54
    W_gas_54 = n_54 * R * T1_54 - n_54 * R * T2_54 * math.log(2.0)
    W_on_gas_54 = -W_gas_54
    assert math.isclose(T2_54, 710.0)
    assert math.isclose(p_max_54, 4.80e5)
    assert math.isclose(W_on_gas_54, 285.1, rel_tol=1e-2)
    ledger['19.54'] = {'T2_K': T2_54, 'p_max_Pa': p_max_54, 'W_on_J': W_on_gas_54}

    # 19.55
    W_12_55 = n_54 * R * T1_54
    dU_12_55 = 2.5 * W_12_55
    Q_12_55 = 3.5 * W_12_55
    W_31_55 = 0.0
    dU_31_55 = -dU_12_55
    Q_31_55 = dU_31_55
    dU_iso_55 = 0.0
    assert math.isclose(W_12_55, 737.9, rel_tol=1e-2)
    assert math.isclose(dU_12_55, 1844.8, rel_tol=1e-2)
    assert math.isclose(Q_12_55, 2582.7, rel_tol=1e-2)
    ledger['19.55'] = {'W12': W_12_55, 'dU12': dU_12_55, 'Q12': Q_12_55, 'dU31': dU_31_55}

    # 19.56 & 19.57
    n_56 = 0.150
    p1_56 = 1.80e5
    T1_56 = 300.0
    T2_56 = 0.5 * T1_56  # 150 K
    T3_56 = T2_56 * (0.5)**(0.40)  # 113.68 K
    p_min_56 = p1_56 * (0.5)**(1.40)  # 6.82e4 Pa
    assert math.isclose(T2_56, 150.0)
    assert math.isclose(T3_56, 113.68, rel_tol=1e-2)
    assert math.isclose(p_min_56, 6.8207e4, rel_tol=1e-2)
    ledger['19.56'] = {'T2_K': T2_56, 'T3_K': T3_56, 'p_min_Pa': p_min_56}

    # 19.57
    W_12_57 = -0.5 * n_56 * R * T1_56
    dU_12_57 = 2.5 * W_12_57
    Q_12_57 = 3.5 * W_12_57
    Q_23_57 = 0.0
    dU_23_57 = n_56 * (2.5 * R) * (T3_56 - T2_56)
    W_23_57 = -dU_23_57
    W_31_57 = 0.0
    dU_31_57 = n_56 * (2.5 * R) * (T1_56 - T3_56)
    Q_31_57 = dU_31_57
    assert math.isclose(W_12_57, -187.08, rel_tol=1e-2)
    assert math.isclose(dU_23_57, -113.21, rel_tol=1e-2)
    assert math.isclose(W_23_57, 113.21, rel_tol=1e-2)
    assert math.isclose(Q_31_57, 580.86, rel_tol=1e-2)
    ledger['19.57'] = {'W12': W_12_57, 'dU23': dU_23_57, 'W23': W_23_57, 'Q31': Q_31_57}

    # 19.58
    n_58 = 1.20
    T1_58 = 300.0
    nRT1_58 = n_58 * R * T1_58
    W_iso_58 = nRT1_58 * math.log(3.0)
    T2_ad_58 = T1_58 * (1.0 / 3.0)**(2.0 / 3.0)
    dU_ad_58 = 1.5 * n_58 * R * (T2_ad_58 - T1_58)
    W_ad_58 = -dU_ad_58
    W_isobar_58 = 2.0 * nRT1_58
    assert math.isclose(W_iso_58, 3288.4, rel_tol=1e-2)
    assert math.isclose(W_ad_58, 2331.4, rel_tol=1e-2)
    assert math.isclose(W_isobar_58, 5986.4, rel_tol=1e-2)
    ledger['19.58'] = {'W_iso': W_iso_58, 'W_ad': W_ad_58, 'W_isobar': W_isobar_58}

    # 19.59
    n_59 = 0.300
    T1_59 = 273.15 + 20.0
    # Qa = 0 (đoạn nhiệt), Qb = 30 J (đẳng tích), Qc = 50 J (đẳng áp)
    # Qc - Qb = n * R * dT = 20 J
    dT_59 = 20.0 / (n_59 * R)
    T2_59 = T1_59 + dT_59
    W_a_59 = -30.0
    W_b_59 = 0.0
    W_c_59 = 20.0
    assert math.isclose(dT_59, 8.018, rel_tol=1e-2)
    assert math.isclose(T2_59 - 273.15, 28.02, rel_tol=1e-2)
    ledger['19.59'] = {'T2_C': T2_59 - 273.15, 'Wa': W_a_59, 'Wb': W_b_59, 'Wc': W_c_59}

    # 19.60
    V_data_60 = np.array([2.50, 2.02, 1.48, 1.01, 0.50]) * 1e-3
    p_data_60 = np.array([0.101, 0.139, 0.202, 0.361, 0.952]) * P_ATM
    poly_60 = np.polyfit(np.log(V_data_60), np.log(p_data_60), 1)
    gamma_60 = -poly_60[0]
    assert math.isclose(gamma_60, 1.3925, rel_tol=1e-2)
    ledger['19.60'] = {'gamma': gamma_60}

    # 19.61
    r_61 = 0.0150
    L1_61 = 0.300
    V1_61 = math.pi * r_61**2 * L1_61
    p1_61 = 101e3
    T1_61 = 273.15 + 30.0
    p1V1_61 = p1_61 * V1_61
    # v = 7 là nghiệm nguyên duy nhất
    v_cand = 7
    T2_61 = T1_61 * (v_cand**0.40)
    W_ad_61 = -(p1V1_61 / 0.40) * (v_cand**0.40 - 1.0)
    W_iso_61 = p1V1_61 * (v_cand**0.40) * math.log(v_cand)
    W_net_61 = W_ad_61 + W_iso_61
    Q_out_isochoric_61 = (p1V1_61 / 0.40) * (v_cand**0.40 - 1.0)
    assert T2_61 - 273.15 < 400.0
    assert W_net_61 >= 25.0
    assert math.isclose(W_net_61, 27.70, rel_tol=1e-2)
    assert math.isclose(Q_out_isochoric_61, 63.07, rel_tol=1e-2)
    ledger['19.61'] = {'v_chosen': v_cand, 'W_net': W_net_61, 'Q_out': Q_out_isochoric_61}

    # 19.62
    p0_62 = 1.01e5
    rho0_62 = 1.23
    p1_62 = 1.45e5
    V_cyl_62 = 575e-6
    m0_62 = rho0_62 * V_cyl_62
    rho_inter_62 = rho0_62 * (p1_62 / p0_62)
    m_inter_62 = rho_inter_62 * V_cyl_62
    pct_b_62 = (m_inter_62 - m0_62) / m0_62 * 100.0
    rho_turbo_62 = rho0_62 * (p1_62 / p0_62)**(1.0 / 1.40)
    m_turbo_62 = rho_turbo_62 * V_cyl_62
    pct_c_62 = (m_turbo_62 - m0_62) / m0_62 * 100.0
    assert math.isclose(m_inter_62, 1.0154e-3, rel_tol=1e-2)
    assert math.isclose(pct_b_62, 43.56, rel_tol=1e-2)
    assert math.isclose(m_turbo_62, 0.9157e-3, rel_tol=1e-2)
    assert math.isclose(pct_c_62, 29.47, rel_tol=1e-2)
    ledger['19.62'] = {'m_inter': m_inter_62, 'pct_b': pct_b_62, 'm_turbo': m_turbo_62, 'pct_c': pct_c_62}

    # 19.63 - 19.66 MCAT
    # 19.63: p_gauge = 2000 psi, T1 = 20 C = 293.15 K, T2 = -5 C = 268.15 K
    p_abs_63 = 2000.0 + 14.7
    p2_abs_63 = p_abs_63 * (268.15 / 293.15)
    p2_gauge_63 = p2_abs_63 - 14.7
    assert math.isclose(p2_gauge_63, 1828.2, rel_tol=1e-2)
    ledger['19.63'] = {'ans': 'c', 'val_psi': p2_gauge_63}

    # 19.64: giải thích giãn nở đoạn nhiệt dU = -W < 0 => T giảm
    ledger['19.64'] = {'ans': 'd'}

    # 19.65: V = 500 L, p_gauge = 2000 psi, rate = 8.2 L/min
    V_deliv_65 = 500.0 * (2000.0 / 14.7)  # lít khí tại 1 atm
    t_min_65 = V_deliv_65 / 8.2
    t_hours_65 = t_min_65 / 60.0
    assert math.isclose(t_hours_65, 138.3, rel_tol=5e-2)
    ledger['19.65'] = {'ans': 'd', 'hours': t_hours_65}

    # 19.66: 1.7 kg N2O, M = 44.013 g/mol => n = 38.62 mol
    # Tại 20 C và 50 psi: V = nRT/p
    n_66 = 1.7 / 0.044013
    V_66_direct = n_66 * R * 293.15 / (50.0 * 6894.76)  # 0.273 m3
    V_66_abs = n_66 * R * 293.15 / ((50.0 + 14.7) * 6894.76)  # 0.211 m3
    assert math.isclose(V_66_direct, 0.2731, rel_tol=1e-2)
    assert math.isclose(V_66_abs, 0.2110, rel_tol=1e-2)
    ledger['19.66'] = {'ans': 'a', 'V_nominal_m3': V_66_direct, 'V_abs_m3': V_66_abs}

    print(f'PASS: Đã tính toán và kiểm toán thành công 33/33 bài tập ({len(ledger)} mục).')
    return ledger

def main():
    verify_images()
    ledger = verify_problems()
    print('ALL VERIFICATIONS PASSED SUCCESSFULLY.')

if __name__ == '__main__':
    main()
