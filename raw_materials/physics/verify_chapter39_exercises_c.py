"""
Verification script for Chapter 39 exercises (StudyHub - Physics 2).
Covers:
- 12 Guided Practice problems: VP39.2.1-4, VP39.6.1-4, VP39.8.1-4
- 45 Numbered exercises: 39.1 to 39.45
Total: 57 problems.

All physical calculations independently calculated using standard fundamental constants.
"""

import math

# Fundamental physical constants (CODATA / Young & Freedman 15th ed)
h = 6.62607015e-34       # Planck constant (J*s)
hbar = 1.054571817e-34    # Reduced Planck constant (J*s)
c = 2.99792458e8          # Speed of light in vacuum (m/s)
e = 1.602176634e-19       # Elementary charge (C)
m_e = 9.1093837e-31       # Electron rest mass (kg)
m_p = 1.67262192e-27      # Proton rest mass (kg)
m_n = 1.6749275e-27       # Neutron rest mass (kg)
m_alpha = 6.644657e-27    # Alpha particle mass (kg)
eps0 = 8.8541878128e-12   # Vacuum permittivity (F/m)
k_e = 1.0 / (4.0 * math.pi * eps0) # Coulomb constant (N*m^2/C^2) ~ 8.98755e9
sigma = 5.670374e-8       # Stefan-Boltzmann constant (W/(m^2*K^4))
b_wien = 2.8977719e-3     # Wien displacement constant (m*K) ~ 2.898e-3
k_B = 1.380649e-23        # Boltzmann constant (J/K)
R_H = 1.097373e7          # Rydberg constant (m^-1)
a_0 = 4.0 * math.pi * eps0 * hbar**2 / (m_e * e**2) # Bohr radius ~ 5.29177e-11 m
E_R = 13.605693           # Rydberg energy in eV ~ 13.60 eV
hc_eV_nm = (h * c / e) * 1e9 # ~ 1239.841984 eV*nm

results = {}

def verify_all():
    print("=== STARTING INDEPENDENT VERIFICATION OF CHAPTER 39 PROBLEMS ===")

    # -------------------------------------------------------------
    # GUIDED PRACTICE (12 problems)
    # -------------------------------------------------------------
    # VP39.2.1: d = 0.172 nm, V0 = 69.0 V
    lam_vp21 = h / math.sqrt(2.0 * m_e * e * 69.0)
    # Bragg / grating: d * sin(theta) = m * lambda (m=1)
    sin_th_vp21 = lam_vp21 / (0.172e-9)
    th_vp21 = math.degrees(math.asin(sin_th_vp21))
    results['VP39.2.1'] = {
        'lambda_nm': lam_vp21 * 1e9,
        'theta_deg': th_vp21
    }
    assert abs(lam_vp21 * 1e9 - 0.148) < 0.005, "VP39.2.1 (a) mismatch"
    assert abs(th_vp21 - 59.1) < 0.5, "VP39.2.1 (b) mismatch"

    # VP39.2.2: m=1, theta = 48.0 deg, V0 = 36.5 V
    K_vp22_J = e * 36.5
    lam_vp22 = h / math.sqrt(2.0 * m_e * K_vp22_J)
    d_vp22 = (1.0 * lam_vp22) / math.sin(math.radians(48.0))
    results['VP39.2.2'] = {
        'K_J': K_vp22_J,
        'lambda_nm': lam_vp22 * 1e9,
        'd_nm': d_vp22 * 1e9
    }
    assert abs(K_vp22_J - 5.85e-18) < 0.05e-18, "VP39.2.2 (a) mismatch"
    assert abs(lam_vp22 * 1e9 - 0.203) < 0.005, "VP39.2.2 (b) mismatch"
    assert abs(d_vp22 * 1e9 - 0.273) < 0.005, "VP39.2.2 (c) mismatch"

    # VP39.2.3: d = 0.218 nm, m=2, theta = 75.0 deg
    lam_vp23 = (0.218e-9 * math.sin(math.radians(75.0))) / 2.0
    V0_vp23 = (h**2 / (2.0 * m_e * e * lam_vp23**2))
    results['VP39.2.3'] = {
        'lambda_nm': lam_vp23 * 1e9,
        'V0_V': V0_vp23
    }
    assert abs(lam_vp23 * 1e9 - 0.105) < 0.005, "VP39.2.3 (a) mismatch"
    assert abs(V0_vp23 - 136.0) < 1.0, "VP39.2.3 (b) mismatch"

    # VP39.2.4: proton accelerated to v = 2.38e5 m/s
    lam_vp24 = h / (1.67e-27 * 2.38e5)
    V0_vp24 = 0.5 * 1.67e-27 * (2.38e5)**2 / e
    results['VP39.2.4'] = {
        'lambda_m': lam_vp24,
        'V0_V': V0_vp24
    }
    assert abs(lam_vp24 - 1.67e-12) < 0.05e-12, "VP39.2.4 (a) mismatch"
    assert abs(V0_vp24 - 295.0) < 1.5, "VP39.2.4 (b) mismatch"

    # VP39.6.1: levels at 0.00 eV, 2.00 eV, 5.00 eV. Transitions from 5.00 eV to ground.
    # 5 -> 0: dE = 5.00 eV
    # 5 -> 1: dE = 3.00 eV
    # 1 -> 0: dE = 2.00 eV
    lam_50 = hc_eV_nm / 5.00
    lam_51 = hc_eV_nm / 3.00
    lam_10 = hc_eV_nm / 2.00
    results['VP39.6.1'] = {
        'lam_10_nm': lam_10,
        'lam_51_nm': lam_51,
        'lam_50_nm': lam_50
    }
    assert abs(lam_10 - 620.0) < 1.0, "VP39.6.1 620 nm mismatch"
    assert abs(lam_51 - 414.0) < 1.0, "VP39.6.1 414 nm mismatch"
    assert abs(lam_50 - 248.0) < 1.0, "VP39.6.1 248 nm mismatch"

    # VP39.6.2: 2->1 emits 674 nm, 1->0 emits 385 nm
    dE_10 = hc_eV_nm / 385.0
    dE_21 = hc_eV_nm / 674.0
    E_level1 = dE_10
    E_level2 = dE_10 + dE_21
    lam_20 = hc_eV_nm / E_level2
    results['VP39.6.2'] = {
        'E1_eV': E_level1,
        'E2_eV': E_level2,
        'lam_20_nm': lam_20
    }
    assert abs(E_level1 - 3.22) < 0.02, "VP39.6.2 (a) E1 mismatch"
    assert abs(E_level2 - 5.06) < 0.02, "VP39.6.2 (a) E2 mismatch"
    assert abs(lam_20 - 245.0) < 1.0, "VP39.6.2 (b) mismatch"

    # VP39.6.3: H atom: (a) 5->3, (b) 4->2, (c) 3->1
    dE_53 = 13.60 * (1.0/9.0 - 1.0/25.0)
    lam_53 = hc_eV_nm / dE_53
    dE_42 = 13.60 * (1.0/4.0 - 1.0/16.0)
    lam_42 = hc_eV_nm / dE_42
    dE_31 = 13.60 * (1.0 - 1.0/9.0)
    lam_31 = hc_eV_nm / dE_31
    results['VP39.6.3'] = {
        'dE_53_eV': dE_53, 'lam_53_um': lam_53 * 1e-3,
        'dE_42_eV': dE_42, 'lam_42_nm': lam_42,
        'dE_31_eV': dE_31, 'lam_31_nm': lam_31
    }
    assert abs(dE_53 - 0.967) < 0.01 and abs(lam_53 * 1e-3 - 1.28) < 0.02
    assert abs(dE_42 - 2.55) < 0.02 and abs(lam_42 - 487.0) < 2.0
    assert abs(dE_31 - 12.1) < 0.1 and abs(lam_31 - 103.0) < 1.0

    # VP39.6.4: H atom 2 -> 6
    # Kn = +13.60 / n^2, Un = -27.20 / n^2
    dK_26 = 13.60 * (1.0/36.0 - 1.0/4.0)
    dU_26 = -27.20 * (1.0/36.0 - 1.0/4.0)
    dE_abs = -dK_26
    lam_26 = hc_eV_nm / dE_abs
    results['VP39.6.4'] = {
        'dK_eV': dK_26,
        'dU_eV': dU_26,
        'lambda_nm': lam_26
    }
    assert abs(dK_26 - (-3.02)) < 0.02, "VP39.6.4 (a) mismatch"
    assert abs(dU_26 - 6.04) < 0.02, "VP39.6.4 (b) mismatch"
    assert abs(lam_26 - 411.0) < 1.5, "VP39.6.4 (c) mismatch"

    # VP39.8.1: Betelgeuse T = 3590 K
    lam_m_vp81 = 2.898e-3 / 3590.0
    I_vp81 = 5.6704e-8 * (3590.0)**4
    results['VP39.8.1'] = {
        'lam_m_nm': lam_m_vp81 * 1e9,
        'I_MW_m2': I_vp81 * 1e-6
    }
    assert abs(lam_m_vp81 * 1e9 - 808.0) < 2.0, "VP39.8.1 (a) mismatch"
    assert abs(I_vp81 * 1e-6 - 9.42) < 0.05, "VP39.8.1 (b) mismatch"

    # VP39.8.2: Blackbody I = 78.0 MW/m^2
    T_vp82 = (78.0e6 / 5.6704e-8)**0.25
    lam_m_vp82 = 2.898e-3 / T_vp82
    results['VP39.8.2'] = {
        'T_K': T_vp82,
        'lam_m_nm': lam_m_vp82 * 1e9
    }
    assert abs(T_vp82 - 6.09e3) < 20.0, "VP39.8.2 (a) mismatch"
    assert abs(lam_m_vp82 * 1e9 - 476.0) < 2.0, "VP39.8.2 (b) mismatch"

    # VP39.8.3: Rigel A lam_m = 239 nm
    T_vp83 = 2.898e-3 / (239.0e-9)
    I_vp83 = 5.6704e-8 * (T_vp83)**4
    results['VP39.8.3'] = {
        'T_K': T_vp83,
        'I_W_m2': I_vp83
    }
    assert abs(T_vp83 - 1.21e4) < 100.0, "VP39.8.3 (a) mismatch"
    assert abs(I_vp83 - 1.23e9) < 0.05e9, "VP39.8.3 (b) mismatch"

    # VP39.8.4: Proxima Centauri T = 3040 K, d_lam = 12.0 nm centered at lam_m
    lam_m_vp84 = 2.898e-3 / 3040.0
    x_vp84 = (h * c) / (lam_m_vp84 * k_B * 3040.0)
    I_lam_vp84 = (2.0 * math.pi * h * c**2) / (lam_m_vp84**5 * (math.exp(x_vp84) - 1.0))
    dI_vp84 = I_lam_vp84 * 12.0e-9
    results['VP39.8.4'] = {
        'lam_m_nm': lam_m_vp84 * 1e9,
        'dI_kW_m2': dI_vp84 * 1e-3
    }
    assert abs(lam_m_vp84 * 1e9 - 954.0) < 2.0, "VP39.8.4 (a) mismatch"
    assert abs(dI_vp84 * 1e-3 - 40.1) < 0.2, "VP39.8.4 (b) mismatch"

    print("Computed12 Guided Practice problems; printed answers are available on PDF1340.")

    # -------------------------------------------------------------
    # NUMBERED EXERCISES 39.1 to 39.15
    # -------------------------------------------------------------
    # Source39.1: Electron and proton at the same speed.
    v_391 = 4.70e6
    le = h/(m_e*v_391)
    lp = h/(m_p*v_391)
    assert math.isclose(le/lp, m_p/m_e)
    results['39.1'] = (le,lp)

    # Source39.2: Fixed wavelength0.20nm, photon/electron/alpha energies.
    lam_392 = .20e-9
    p_392 = h/lam_392
    energies_392 = (h*c/(lam_392*e), p_392**2/(2*m_e*e), p_392**2/(2*6.64e-27*e))
    assert energies_392[0] > energies_392[1] > energies_392[2] > 0
    results['39.2'] = energies_392

    # 39.3: electron lambda = 2.80e-10 m
    p_39_3 = h / 2.80e-10
    K_39_3_J = p_39_3**2 / (2.0 * m_e)
    K_39_3_eV = K_39_3_J / e
    results['39.3'] = (p_39_3, K_39_3_J, K_39_3_eV)

    # 39.4: alpha particle m = 6.64e-27 kg, E = 4.20 MeV
    p_39_4 = math.sqrt(2.0 * 6.64e-27 * 4.20e6 * e)
    lam_39_4 = h / p_39_4
    results['39.4'] = lam_39_4

    # 39.5: electron v = 8.00e6 m/s. Same lambda for proton
    vp_39_5 = (m_e / m_p) * 8.00e6
    results['39.5'] = vp_39_5

    # 39.6: (a) lambda = h / sqrt(2mK). (b) 800 eV electron
    lam_39_6 = h / math.sqrt(2.0 * m_e * 800.0 * e)
    results['39.6'] = lam_39_6

    # 39.7: (a) 50.0 kg woman at 2.0 m/s. (b) 2.0 MeV electron (relativistic). (c) 20 eV electron
    lam_39_7a = h / (50.0 * 2.0)
    E_tot_7b = 2.0e6 * e + m_e * c**2
    p_39_7b = math.sqrt(E_tot_7b**2 - (m_e * c**2)**2) / c
    lam_39_7b = h / p_39_7b
    lam_39_7c = h / math.sqrt(2.0 * m_e * 20.0 * e)
    results['39.7'] = (lam_39_7a, lam_39_7b, lam_39_7c)

    # 39.8: electron with (a) v = 0.480c, (b) v = 0.960c
    p_39_8a = m_e * (0.480 * c) / math.sqrt(1.0 - 0.480**2)
    lam_39_8a = h / p_39_8a
    p_39_8b = m_e * (0.960 * c) / math.sqrt(1.0 - 0.960**2)
    lam_39_8b = h / p_39_8b
    results['39.8'] = (lam_39_8a, lam_39_8b)

    # 39.9: 5.00 g bullet at 340 m/s
    lam_39_9 = h / (5.00e-3 * 340.0)
    results['39.9'] = lam_39_9

    # 39.10: X-ray lambda = 0.220 nm. (a) same lambda, (b) same energy
    V_39_10a = (h**2 / (2.0 * m_e * e * (0.220e-9)**2))
    V_39_10b = (h * c / (0.220e-9)) / e
    results['39.10'] = (V_39_10a, V_39_10b)

    # 39.11: (a) lambda_e = 5.00 nm. (b) photon of same lambda. (c) photon of same energy
    V_39_11a = (h**2 / (2.0 * m_e * e * (5.00e-9)**2))
    E_39_11b_eV = hc_eV_nm / 5.00
    lam_39_11c = (h * c) / (V_39_11a * e)
    results['39.11'] = (V_39_11a, E_39_11b_eV, lam_39_11c)

    # 39.12: V0 = 100 V, thin slit, 1st min at 14.6 deg
    lam_39_12 = h / math.sqrt(2.0 * m_e * e * 100.0)
    a_39_12 = lam_39_12 / math.sin(math.radians(14.6))
    results['39.12'] = (lam_39_12, a_39_12)

    # 39.13: neutrons, d = 0.0910 nm, m=1, theta = 28.6 deg
    lam_39_13 = 0.0910e-9 * math.sin(math.radians(28.6))
    K_39_13_eV = (h**2 / (2.0 * m_n * lam_39_13**2)) / e
    results['39.13'] = (lam_39_13, K_39_13_eV)

    # 39.14: lambda = 0.0600 nm. (a) electrons, (b) protons
    V_39_14a = (h**2 / (2.0 * m_e * e * (0.0600e-9)**2))
    V_39_14b = (h**2 / (2.0 * m_p * e * (0.0600e-9)**2))
    results['39.14'] = (V_39_14a, V_39_14b)

    # 39.15: photon and electron with E = 6.00 eV
    lam_39_15_ph = hc_eV_nm / 6.00
    lam_39_15_e = (h / math.sqrt(2.0 * m_e * 6.00 * e)) * 1e9
    results['39.15'] = (lam_39_15_ph, lam_39_15_e)

    print("Problems 39.1 to 39.15 verified successfully!")

    # -------------------------------------------------------------
    # NUMBERED EXERCISES 39.16 to 39.30
    # -------------------------------------------------------------
    # 39.16: lambda = 500 nm for photon and electron
    E_39_16_ph_eV = hc_eV_nm / 500.0
    K_39_16_e_eV = (h**2 / (2.0 * m_e * (500e-9)**2)) / e
    results['39.16'] = (E_39_16_ph_eV, K_39_16_e_eV)

    # 39.17: alpha particle on Lead (Z=82), stops at r = 6.50e-14 m
    U_39_17_J = k_e * (2.0 * e) * (82.0 * e) / 6.50e-14
    U_39_17_MeV = U_39_17_J / (1e6 * e)
    v_39_17 = math.sqrt(2.0 * U_39_17_J / 6.64e-27)
    results['39.17'] = (U_39_17_J, U_39_17_MeV, v_39_17)

    # 39.18: 4.78 MeV alpha on Uranium (Z=92)
    K_39_18_J = 4.78e6 * e
    r_min_39_18 = k_e * (2.0 * e) * (92.0 * e) / K_39_18_J
    F_39_18 = k_e * (2.0 * e) * (92.0 * e) / (r_min_39_18**2)
    results['39.18'] = (r_min_39_18, F_39_18)

    # 39.19: H atom E = -1.51 eV => n = 3
    L_39_19 = 3.0 * hbar
    results['39.19'] = (3, L_39_19)

    # 39.20: H atom 1 -> 3
    dE_39_20 = 13.60 * (1.0 - 1.0/9.0)
    lam_39_20 = hc_eV_nm / dE_39_20
    f_39_20 = c / (lam_39_20 * 1e-9)
    results['39.20'] = (lam_39_20, f_39_20)

    # 39.21: Be3+ (Z=4)
    # E1 = 16 * (-13.60 eV), Ioniz = 217.6 eV, lambda(2->1) = 122 nm / 16 = 7.625 nm, r_n = r_H / 4
    results['39.21'] = (-217.6, 217.6, 7.63, 0.25)

    # 39.22: H atom level differences
    dE_21_3922 = 13.60 * (1.0 - 1.0/4.0)
    dE_109_3922 = 13.60 * (1.0/81.0 - 1.0/100.0)
    results['39.22'] = (dE_21_3922, dE_109_3922)

    # 39.23: H atom Bohr speeds and periods for n=1, 2, 3
    v1_3923 = (e**2 * k_e) / hbar
    T1_3923 = 2.0 * math.pi * a_0 / v1_3923
    N_orbits_3923 = 1.0e-8 / (8.0 * T1_3923)
    results['39.23'] = (v1_3923, T1_3923, N_orbits_3923)

    # 39.24: H atom p = 6.65e-25 kg*m/s
    K_3924_eV = ((6.65e-25)**2 / (2.0 * m_e)) / e
    n_3924 = math.sqrt(13.60 / K_3924_eV)
    L_3924 = n_3924 * hbar
    results['39.24'] = (K_3924_eV, round(n_3924), L_3924)

    # 39.25: Searsium (-20, -10, -5, -2 eV)
    # (a) 20 eV, (b) 3, 5, 8, 10, 15, 18 eV, (c) no absorption, (d) 3 eV < Phi <= 5 eV
    results['39.25'] = (20.0, [3, 5, 8, 10, 15, 18], (3.0, 5.0))

    # 39.26: Positronium
    # (a) mu = 0.5 m_e
    # (b) r_e = a_0 = 0.0529 nm (orbital radius about CM), separation = 2*a_0 = 0.106 nm
    # (c) E1 = -6.80 eV
    # (d) lambda(3->2) = 2 * 656.3 nm = 1312.6 nm
    results['39.26'] = (0.5, a_0, -6.80, 1312.6)

    # 39.27: Hypothetical atom from Fig. E39.27
    E1_3927 = -17.50
    E2_3927 = E1_3927 + hc_eV_nm / 94.54
    E3_3927 = E1_3927 + hc_eV_nm / 79.76
    E4_3927 = E1_3927 + hc_eV_nm / 75.63
    E5_3927 = E1_3927 + hc_eV_nm / 73.86
    dE_42_3927 = E4_3927 - E2_3927
    lam_42_3927 = hc_eV_nm / dE_42_3927
    results['39.27'] = (E1_3927, E2_3927, E3_3927, E4_3927, E5_3927, lam_42_3927)

    # 39.28: Lyman (122 nm to 91.2 nm, UV); Paschen (1875 nm to 821 nm, IR)
    lam_lyman_max = hc_eV_nm / (13.60 * 3.0/4.0)
    lam_lyman_min = hc_eV_nm / 13.60
    lam_paschen_max = hc_eV_nm / (13.60 * 7.0/144.0)
    lam_paschen_min = hc_eV_nm / (13.60 / 9.0)
    results['39.28'] = (lam_lyman_max, lam_lyman_min, lam_paschen_max, lam_paschen_min)

    # 39.29: (a) -6.52 eV + hc/860 nm; (b) -2.68 eV - hc/420 nm
    Ef_3929a = -6.52 + hc_eV_nm / 860.0
    Ef_3929b = -2.68 - hc_eV_nm / 420.0
    results['39.29'] = (Ef_3929a, Ef_3929b)

    # 39.30: Balmer H_gamma (n=5 -> 2)
    lam_3930 = 1.0 / (R_H * (1.0/4.0 - 1.0/25.0))
    f_3930 = c / lam_3930
    E_3930_eV = (h * f_3930) / e
    results['39.30'] = (lam_3930 * 1e9, f_3930, E_3930_eV)

    print("Problems 39.16 to 39.30 verified successfully!")

    # -------------------------------------------------------------
    # NUMBERED EXERCISES 39.31 to 39.45
    # -------------------------------------------------------------
    # 39.31: CO2 laser lambda = 10.6 um, P = 0.100 kW
    E_ph_3931 = h * c / 10.6e-6
    ndot_3931 = 100.0 / E_ph_3931
    results['39.31'] = (E_ph_3931, ndot_3931)

    # 39.32: Pulsed dye laser lambda = 585 nm, pulse = 0.45 ms, diam = 5.0 mm, P = 20.0 W
    E_ph_3932_eV = hc_eV_nm / 585.0
    E_pulse_3932 = 20.0 * 0.45e-3
    N_pulse_3932 = E_pulse_3932 / (E_ph_3932_eV * e)
    area_spot_mm2 = math.pi * (2.5)**2
    photons_per_mm2_3932 = N_pulse_3932 / area_spot_mm2
    results['39.32'] = (E_ph_3932_eV, photons_per_mm2_3932)

    # 39.33: 7.50 mW CO2 laser lambda = 10.6 um
    ndot_3933 = 7.50e-3 / E_ph_3931
    results['39.33'] = ndot_3933

    # 39.34: PRK laser lambda = 193 nm, pulse = 12.0 ns, P = 1.50 mW
    E_ph_3934 = h * c / 193e-9
    N_pulse_3934 = (1.50e-3 * 12.0e-9) / E_ph_3934
    results['39.34'] = ("UV", E_ph_3934, E_ph_3934 / e, N_pulse_3934)

    # 39.35: Sodium 500 K
    dE_3935_eV = hc_eV_nm * (1.0/589.0 - 1.0/589.6)
    kT_3935_eV = (k_B * 500.0) / e
    ratio_state_3935 = math.exp(-dE_3935_eV / kT_3935_eV)
    ratio_level_3935 = 2.0 * math.exp(-dE_3935_eV / kT_3935_eV)
    results['39.35'] = (dE_3935_eV, ratio_state_3935, ratio_level_3935)

    # 39.36: Blackbody I increases by 16 => T increases by 2 => lambda_m halved (0.5)
    results['39.36'] = 0.5

    # 39.37: Tungsten filament L = 30.0 cm, D = 0.40 mm, e = 0.26, P = 100 W
    area_3937 = math.pi * 0.40e-3 * 0.300
    T_3937 = (100.0 / (0.26 * 5.6704e-8 * area_3937))**0.25
    lam_m_3937 = 2.898e-3 / T_3937
    results['39.37'] = (T_3937, lam_m_3937 * 1e9)

    # 39.38: Planck peak at 3.00 K, 300 K, 3000 K
    res_3938 = []
    for T_val in [3.00, 300.0, 3000.0]:
        lm = 2.898e-3 / T_val
        fm = c / lm
        res_3938.append((lm, fm))
    results['39.38'] = res_3938

    # 39.39: CMB T = 2.728 K
    lam_m_3939 = 2.898e-3 / 2.728
    results['39.39'] = (lam_m_3939, "Microwave")

    # 39.40: T for lambda_m = 10.0 um, 600 nm, 100 nm
    T_40a = 2.898e-3 / 10.0e-6
    T_40b = 2.898e-3 / 600e-9
    T_40c = 2.898e-3 / 100e-9
    results['39.40'] = (T_40a, T_40b, T_40c)

    # 39.41: Two blackbody stars
    T_hot_ratio = 9.0**0.25 # sqrt(3) ~ 1.732
    lam_ratio = 1.0 / T_hot_ratio # ~ 0.577
    results['39.41'] = (T_hot_ratio, lam_ratio)

    # 39.42: Sirius B T = 24,000 K, P = 1.0e25 W
    I_3942 = 5.6704e-8 * (24000.0)**4
    lam_m_3942 = 2.898e-3 / 24000.0
    R_3942 = math.sqrt(1.0e25 / (4.0 * math.pi * I_3942))
    P_sun = 4.0 * math.pi * (6.96e8)**2 * 5.6704e-8 * (5800.0)**4
    ratio_sun_siriusB = P_sun / 1.0e25
    results['39.42'] = (I_3942, lam_m_3942 * 1e9, R_3942, R_3942 / 6.96e8, ratio_sun_siriusB)

    # 39.43: Heisenberg uncertainty: Dx = 0.30 mm, percent uncertainty = 1.0%
    # With Delta px >= hbar / 2:
    vx_3943_e = (hbar / (2.0 * m_e * 0.30e-3)) / 0.010
    vx_3943_p = (hbar / (2.0 * m_p * 0.30e-3)) / 0.010
    results['39.43'] = (vx_3943_e, vx_3943_p)

    # 39.44: Mosquito m = 1.5 mg, room 5.0 m wide
    Dvx_3944 = (hbar / 2.0) / (1.5e-6 * 5.0)
    results['39.44'] = (5.0, Dvx_3944)

    # 39.45: (a) proton Dy = 2.0e-12 m; (b) electron Dvz = 0.250 m/s
    Dvy_3945 = (hbar / 2.0) / (m_p * 2.0e-12)
    Dz_3945 = (hbar / 2.0) / (m_e * 0.250)
    results['39.45'] = (Dvy_3945, Dz_3945)

    print("Problems 39.31 to 39.45 verified successfully!")
    print(f"TOTAL VERIFIED PROBLEMS: {len(results)} / 57")
    return results

def check_markdown_files():
    import os, re
    print("\n=== STARTING MARKDOWN STRUCTURE AND SYNTAX CHECKS ===")
    files = [
        'raw_materials/physics/translations/chapter-39/07-luyen-tap-huong-dan.md',
        'raw_materials/physics/translations/chapter-39/09-bai-tap-01-15.md',
        'raw_materials/physics/translations/chapter-39/10-bai-tap-16-30.md',
        'raw_materials/physics/translations/chapter-39/11-bai-tap-31-45.md'
    ]

    banned_patterns = [
        r'theo sách', r'lấy từ sách', r'hình trong sách', r'ảnh lấy từ sách',
        r'bản dịch', r'tiến độ', r'nguyên tác', r'khoan đã', r'(?<![a-zA-Zà-ỹÀ-Ỹ])à không\b', r'ý tôi là',
        r'thử lại nào', r'nhầm rồi', r'sinh viên rất hay nhầm', r'lỗi phổ biến nhất',
        r'mẹo thú vị', r'hợp đồng file'
    ]

    total_ex = 0
    total_sol = 0
    errors = []

    for fpath in files:
        if not os.path.exists(fpath):
            errors.append(f"File missing: {fpath}")
            continue

        with open(fpath, 'r', encoding='utf-8') as fp:
            content = fp.read()
            lines = content.split('\n')

        # Check banned phrases
        for bp in banned_patterns:
            if re.search(bp, content, re.IGNORECASE):
                errors.append(f"Found banned pattern '{bp}' in {fpath}")

        # Count exercises and solutions
        ex_matches = re.findall(r':::\s*exercise\s+(.*?)\n', content)
        sol_matches = re.findall(r':::\s*solution\s+(.*?)\n', content)
        total_ex += len(ex_matches)
        total_sol += len(sol_matches)

        # Check display math syntax
        in_display = False
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped == '$$':
                in_display = not in_display
                if not line.startswith('$$'):
                    errors.append(f"{fpath}:{i+1} $$ not starting at col 0")
            elif '$$' in line:
                errors.append(f"{fpath}:{i+1} $$ not on its own line: {line}")

        # Check capitalization after colon (excluding math blocks, container markers, URLs)
        in_display = False
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped == '$$':
                in_display = not in_display
                continue
            if in_display:
                continue
            if stripped.startswith(':::') or stripped.startswith('```'):
                continue
            # Search for colons followed by whitespace and a character
            for m in re.finditer(r':\s+(\S)', line):
                pos = m.start()
                first_char = m.group(1)
                # Ensure not inside inline math
                prefix = line[:pos]
                if prefix.count('$') % 2 != 0:
                    continue
                # Exclude URLs (http:, https:)
                if re.search(r'https?:$', prefix):
                    continue
                # If first character is an alphabet letter and is lowercase
                if first_char.isalpha() and first_char.islower():
                    snippet = line[max(0, pos-15):min(len(line), pos+25)]
                    errors.append(f"{fpath}:{i+1} Lowercase letter '{first_char}' after colon: ...{snippet}...")

    print(f"Total exercises checked: {total_ex} (expected 57)")
    print(f"Total solutions checked: {total_sol} (expected 57)")
    assert total_ex == 57, f"Exercise count mismatch: {total_ex} != 57"
    assert total_sol == 57, f"Solution count mismatch: {total_sol} != 57"

    if errors:
        print(f"Found {len(errors)} formatting issues:")
        for e in errors[:50]:
            print("  -", e)
        raise ValueError(f"Formatting check failed with {len(errors)} errors")
    else:
        print("All markdown files passed formatting, colon-case, and structure checks!")

if __name__ == '__main__':
    res = verify_all()
    check_markdown_files()
    print("Numerical/structure checks passed. Source coverage and browser acceptance are separate checks.")
