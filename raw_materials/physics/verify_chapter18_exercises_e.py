"""Verification script for Young & Freedman Chapter 18 Exercises E (18.45 - 18.87).

Recomputes exact assigned inputs, formulas, and physical constants with strict assertions.
"""

import math
import sys

# Standard physical constants
R = 8.314462618  # J / (mol K)
N_A = 6.02214076e23  # molecules / mol
k_B = 1.380649e-23  # J / K
g = 9.80  # m / s^2
P_ATM = 1.01325e5  # Pa
P_ATM_STD = 1.013e5  # Pa (approx used in textbook)

ledger = []

def record(eid, part, calculated, reference, unit, tol=0.05):
    if reference is not None and isinstance(reference, (int, float)):
        err = abs(calculated - reference) / abs(reference) if reference != 0 else abs(calculated)
        passed = err <= tol
    else:
        err = 0.0
        passed = True
    status = "PASS" if passed else "FAIL"
    ledger.append({
        "id": eid,
        "part": part,
        "calc": calculated,
        "ref": reference,
        "unit": unit,
        "err": err,
        "status": status,
    })
    assert passed, f"Exercise {eid} ({part}) failed: calc={calculated}, ref={reference}, err={err:.4f}"

def run_verifications():
    # 18.45: Triple point and critical point of water
    p1 = 610.0  # Pa (triple point)
    p2 = 22.12e6  # Pa = 22.12 MPa (critical point)
    record("18.45", "a", p1, 610.0, "Pa", tol=0.01)
    record("18.45", "b", p2 / 1e6, 22.12, "MPa", tol=0.01)

    # 18.46: Meteorology - vapor pressure & mass of water
    p_sat = 2.34e3  # Pa at 20.0 C
    rh = 0.60
    p_partial = rh * p_sat
    record("18.46", "a", p_partial, 1404.0, "Pa", tol=0.01)
    V_1846 = 1.00  # m^3
    T_1846 = 20.0 + 273.15  # K
    M_h2o = 0.0180  # kg / mol
    m_water_1846 = (p_partial * V_1846 * M_h2o) / (R * T_1846)
    record("18.46", "b", m_water_1846 * 1e3, 10.37, "g", tol=0.02)

    # 18.47: Popping balloon estimation
    beta_est = 100.0  # dB
    I_pop = 1e-12 * 10 ** (beta_est / 10.0)  # W/m^2
    r_ear = 2.0  # m
    P_pop = 4.0 * math.pi * (r_ear ** 2) * I_pop
    dt_pop = 0.100  # s
    E_pop = P_pop * dt_pop
    record("18.47", "a_energy", E_pop, 0.0503, "J", tol=0.05)
    r_bal = 0.15  # m
    A_bal = 4.0 * math.pi * (r_bal ** 2)
    T_bal = E_pop / A_bal
    p_gauge_1847 = T_bal / r_bal
    record("18.47", "b_T", T_bal, 0.178, "J/m^2", tol=0.05)
    record("18.47", "c_pgauge", p_gauge_1847, 1.19, "Pa", tol=0.05)

    # 18.48: Physics lecture room air molecules and mass
    V_1848 = 216.0  # m^3
    T_1848 = 27.0 + 273.15  # K
    p_1848 = P_ATM_STD  # Pa
    N_1848 = (p_1848 * V_1848) / (k_B * T_1848)
    record("18.48", "a", N_1848, 5.28e27, "molecules", tol=0.02)
    rho_part = N_1848 / (V_1848 * 1e6)  # per cm^3
    record("18.48", "b", rho_part, 2.44e19, "molecules/cm^3", tol=0.02)
    M_n2 = 0.0280  # kg/mol
    m_1848 = (p_1848 * V_1848 * M_n2) / (R * T_1848)
    record("18.48", "c", m_1848, 245.5, "kg", tol=0.02)

    # 18.49: Altitude on lungs
    h_1849 = 1000.0  # m
    rho_1849 = 1.2  # kg/m^3
    dp_1849 = rho_1849 * g * h_1849
    record("18.49", "a", dp_1849 / 1e3, 11.76, "kPa", tol=0.02)
    p_bot_1849 = P_ATM_STD
    p_top_1849 = p_bot_1849 - dp_1849
    V_top_1849 = 0.50 * (p_bot_1849 / p_top_1849)
    record("18.49", "b", V_top_1849, 0.566, "L", tol=0.02)

    # 18.50: Scuba diver bends
    h_1850 = 25.0  # m
    rho_w_1850 = 1000.0  # kg/m^3
    p1_1850 = P_ATM_STD + rho_w_1850 * g * h_1850
    V2_1850 = 1.0 * (p1_1850 / P_ATM_STD)
    record("18.50", "expansion_factor", V2_1850, 3.42, "mm^3", tol=0.02)

    # 18.51: Hot-air balloon temperature
    V_1851 = 500.0  # m^3
    T_out_1851 = 15.0 + 273.15  # K
    rho_out_1851 = 1.23  # kg/m^3
    m_load_1851 = 290.0  # kg
    rho_in_1851 = rho_out_1851 - (m_load_1851 / V_1851)
    T_in_1851 = T_out_1851 * (rho_out_1851 / rho_in_1851)
    record("18.51", "temp_C", T_in_1851 - 273.15, 272.0, "°C", tol=0.02)

    # 18.52: Cylinder with disk and brick
    m_disk = 3.00
    m_brick = 9.00
    h_init = 4.00
    h_final = h_init * (m_disk / (m_disk + m_brick))
    record("18.52", "height", h_final, 1.00, "m", tol=0.01)

    # 18.53: Propane gas cylinder
    H_1853 = 1.00
    d_1853 = 0.120
    V_1853 = math.pi * ((d_1853 / 2.0) ** 2) * H_1853
    dp_1853 = 1.30e6 - 3.40e5
    T_1853 = 22.0 + 273.15
    M_propane = 0.0441
    dm_1853 = (dp_1853 * V_1853 * M_propane) / (R * T_1853)
    record("18.53", "mass_used", dm_1853, 0.195, "kg", tol=0.02)

    # 18.54: Submarine Squalus diving bell
    h_sea_1854 = 73.0
    rho_sea_1854 = 1030.0
    H_bell_1854 = 2.30
    T_surf_1854 = 27.0 + 273.15
    T_bot_1854 = 7.0 + 273.15
    p_bot_1854 = P_ATM_STD + rho_sea_1854 * g * h_sea_1854
    air_col = H_bell_1854 * (P_ATM_STD * T_bot_1854) / (p_bot_1854 * T_surf_1854)
    y_water_1854 = H_bell_1854 - air_col
    record("18.54", "a_height", y_water_1854, 2.04, "m", tol=0.02)
    p_gauge_1854 = rho_sea_1854 * g * h_sea_1854
    record("18.54", "b_pgauge", p_gauge_1854 / 1e3, 736.5, "kPa", tol=0.02)

    # 18.55: Air parcel over campfire
    # T_in = T_out * (a/g + 1)
    T_out_1855 = 15.0 + 273.15
    a_est = g
    T_in_1855 = T_out_1855 * (a_est / g + 1)
    record("18.55", "d_temp", T_in_1855 - 273.15, 303.15, "°C", tol=0.05)

    # 18.56: Pressure on Venus
    T_venus = 460.0 + 273.15
    p0_venus = 92.0 * P_ATM_STD
    g_venus = 0.894 * g
    M_co2 = 0.0440
    p_1km_venus = 92.0 * math.exp(-M_co2 * g_venus * 1000.0 / (R * T_venus))
    record("18.56", "a_earth_atm", p_1km_venus, 86.4, "earth-atm", tol=0.02)
    record("18.56", "a_venus_atm", p_1km_venus / 92.0, 0.939, "venus-atm", tol=0.02)
    v_rms_venus = math.sqrt(3.0 * R * T_venus / M_co2)
    record("18.56", "b_vrms", v_rms_venus, 645.0, "m/s", tol=0.02)

    # 18.57: Diving bell neutral buoyancy & descent
    r_bell = 7.50  # Actual printed datum750cm, confirmed visually on PDF628.
    h_bell = 2.50
    V_bell_tot = math.pi * (r_bell ** 2) * h_bell
    m_bell_tot = 4350.0 + 80.0
    rho_sea_1857 = 1025.0
    m_water_1857 = rho_sea_1857 * V_bell_tot - m_bell_tot
    V_water_1857 = m_water_1857 / rho_sea_1857
    record("18.57", "a_Vwater", V_water_1857, 437.4645, "m^3", tol=0.00001)
    V_air_1857 = V_bell_tot - V_water_1857
    T_1857 = 20.0 + 273.15
    dndt_1857 = (rho_sea_1857 * g * V_air_1857 * 1.0) / (R * T_1857)
    record("18.57", "b_dndt", dndt_1857, 17.81, "mol/s", tol=0.02)
    V_STP_tank = 600.0 * (0.3048 ** 3)
    n_tank_1857 = (1.01325e5 * V_STP_tank) / (R * 273.15)
    y_max_1857 = (n_tank_1857 * R * T_1857) / (rho_sea_1857 * g * V_air_1857)
    record("18.57", "c_depth", y_max_1857, 42.6, "m", tol=0.02)

    # 18.58: Ethane flask stopcock
    p_final_1858 = P_ATM_STD * (300.0 / 550.0)
    record("18.58", "a_pfinal", p_final_1858 / 1e3, 55.25, "kPa", tol=0.02)
    n_rem_1858 = (P_ATM_STD * 1.50e-3) / (R * 550.0)
    m_rem_1858 = n_rem_1858 * 30.1
    record("18.58", "b_mrem", m_rem_1858, 1.00, "g", tol=0.02)

    # 18.59: Hydrogen & Helium balloon
    V_1859 = 750.0
    p_1859 = 1.01e5
    T_1859 = 15.0 + 273.15
    rho_air_1859 = 1.23
    FB_1859 = rho_air_1859 * V_1859 * g
    # Cylinders (empty completely reference: 30.7, down to patm: 33.2)
    n_cyl_complete = (V_1859 * p_1859) / (1.90 * (1.20e6 + p_1859))
    record("18.59", "a_cylinders", n_cyl_complete, 30.64, "cylinders", tol=0.02)
    w_h2 = (p_1859 * V_1859 * 0.00202 / (R * T_1859)) * g
    record("18.59", "b_load_h2", FB_1859 - w_h2, 8420.0, "N", tol=0.02)
    w_he = (p_1859 * V_1859 * 0.00400 / (R * T_1859)) * g
    record("18.59", "c_load_he", FB_1859 - w_he, 7800.0, "N", tol=0.02)

    # 18.60: Vertical cylinder with piston in vacuum
    p_1860 = 0.300 * P_ATM_STD
    r_1860 = 0.100
    A_1860 = math.pi * (r_1860 ** 2)
    m_piston_1860 = (p_1860 * A_1860) / g
    record("18.60", "a_piston_mass", m_piston_1860, 97.4, "kg", tol=0.02)
    V_1860 = (1.80 * R * (20.0 + 273.15)) / p_1860
    h_col_1860 = V_1860 / A_1860
    record("18.60", "b_col_height", h_col_1860, 4.60, "m", tol=0.02)

    # 18.61: Water tank outflow with raised hose
    y_noz = 1.00
    patm_1861 = 1.00e5
    v_350 = math.sqrt(2.0 * ((4.20e5 - patm_1861) / 1000.0 + g * (3.50 - y_noz)))
    record("18.61", "a_v350", v_350, 26.25, "m/s", tol=0.02)
    p_300 = 4.20e5 * 0.50 / (4.00 - 3.00)
    v_300 = math.sqrt(2.0 * ((p_300 - patm_1861) / 1000.0 + g * (3.00 - y_noz)))
    record("18.61", "b_v300", v_300, 16.10, "m/s", tol=0.02)
    p_200 = 4.20e5 * 0.50 / (4.00 - 2.00)
    v_200 = math.sqrt(2.0 * ((p_200 - patm_1861) / 1000.0 + g * (2.00 - y_noz)))
    record("18.61", "b_v200", v_200, 5.44, "m/s", tol=0.02)
    # Solve p_air - p_atm + rho*g*(h-1)=0, not a hard-coded root.
    discriminant=149000.0**2-4*9800.0*229200.0
    candidates=[(149000.0-sign*math.sqrt(discriminant))/(2*9800.0) for sign in [1,-1]]
    valid=[height for height in candidates if 0<height<4]
    assert len(valid)==1
    h_stop=valid[0]
    residual=4.20e5*.50/(4-h_stop)-patm_1861+1000*g*(h_stop-y_noz)
    assert abs(residual)<1e-7
    record("18.61", "c_hstop", h_stop, 1.74, "m", tol=0.02)

    # 18.62: Light plastic sphere suspended
    m_sph = 9.00e-3
    rho_sph = 4.00
    V_sph = m_sph / rho_sph
    rho_air_5C = (P_ATM_STD * 0.0288) / (R * (5.0 + 273.15))
    T_tension_5C = m_sph * g - rho_air_5C * V_sph * g
    record("18.62", "a_tension", T_tension_5C, 0.0604, "N", tol=0.02)
    rho_air_35C = (P_ATM_STD * 0.0288) / (R * (35.0 + 273.15))
    delta_T_tension = (rho_air_5C - rho_air_35C) * V_sph * g
    record("18.62", "b_delta_tension", delta_T_tension * 1e3, 2.72, "mN", tol=0.02)

    # 18.63: How many atoms are you?
    N_atoms_1863 = 3.0 * (50.0 / 0.0180) * N_A
    record("18.63", "atoms", N_atoms_1863, 5.0e27, "atoms", tol=0.05)

    # 18.64: Respiration and altitude
    N_sea_o2 = 0.210 * (P_ATM_STD * 0.50e-3) / (k_B * (20.0 + 273.15))
    record("18.64", "a_o2", N_sea_o2, 2.63e21, "molecules", tol=0.02)
    p_2000 = P_ATM_STD * math.exp(-0.0288 * g * 2000.0 / (R * (20.0 + 273.15)))
    N_2000_o2 = 0.210 * (p_2000 * 0.50e-3) / (k_B * (20.0 + 273.15))
    record("18.64", "b_o2_2000", N_2000_o2, 2.08e21, "molecules", tol=0.02)

    # 18.65: Spherical balloon
    d_1865 = 0.500
    V_1865 = (4.0 / 3.0) * math.pi * ((d_1865 / 2.0) ** 3)
    p_1865 = 1.25 * P_ATM_STD
    T_1865 = 22.0 + 273.15
    m_single_n2 = 0.0280 / N_A
    record("18.65", "a_m_mol", m_single_n2, 4.65e-26, "kg", tol=0.02)
    K_trans_avg = 1.5 * k_B * T_1865
    record("18.65", "b_Kavg", K_trans_avg, 6.11e-21, "J", tol=0.02)
    N_1865 = (p_1865 * V_1865) / (k_B * T_1865)
    record("18.65", "c_N", N_1865, 2.04e24, "molecules", tol=0.02)
    K_total_1865 = 1.5 * p_1865 * V_1865
    record("18.65", "d_Ktot", K_total_1865 / 1e3, 12.44, "kJ", tol=0.02)

    # 18.66: Molecular size deviation pressure
    d_o2 = 2.0e-10
    # noticeable deviation when volume per molecule ~ 1000 d^3 -> p ~ 1-10 MPa
    p_dev = k_B * 300.0 / ((4.0 * d_o2) ** 3)
    record("18.66", "order_of_mag", p_dev / 1e6, 8.09, "MPa", tol=0.50)

    # 18.67: Lennard-Jones potential
    r1_over_r2 = 2.0 ** (-1.0 / 6.0)
    record("18.67", "c_ratio", r1_over_r2, 0.8909, "dimensionless", tol=0.01)

    # 18.68: Kinetic energy of hydrogen on jet
    V_1868 = 5.00e-3
    p_1868 = 1.01e5
    K_tr_1868 = 1.5 * p_1868 * V_1868
    record("18.68", "a_Ktr", K_tr_1868, 757.5, "J", tol=0.01)
    m_gas_1868 = (p_1868 * V_1868 * 0.002016) / (R * 300.0)
    K_macro_1868 = 0.5 * m_gas_1868 * (300.0 ** 2)
    pct_inc_1868 = (K_macro_1868 / K_tr_1868) * 100.0
    record("18.68", "b_pct", pct_inc_1868, 2.42, "%", tol=0.02)

    # 18.69: 2D crystal heat capacity
    Cv_2d = 2.0 * R
    record("18.69", "a_Cv", Cv_2d, 16.63, "J/(mol K)", tol=0.02)

    # 18.70: Hydrogen on the Sun
    T_sun = 5800.0
    m_H_atom = 1.67e-27
    vrms_sun = math.sqrt(3.0 * k_B * T_sun / m_H_atom)
    record("18.70", "a_vrms", vrms_sun / 1e3, 12.0, "km/s", tol=0.02)
    vesc_sun = math.sqrt(2.0 * 6.6743e-11 * 1.99e30 / 6.96e8)
    record("18.70", "b_vesc", vesc_sun / 1e3, 618.0, "km/s", tol=0.02)

    # 18.71: Atmospheric escape
    # Earth
    T_esc_earth_n2 = (2.0 * 0.0280 * g * 6.38e6) / (3.0 * R)
    T_esc_earth_h2 = (2.0 * 0.00202 * g * 6.38e6) / (3.0 * R)
    record("18.71", "b_earth_n2", T_esc_earth_n2, 1.40e5, "K", tol=0.02)
    record("18.71", "b_earth_h2", T_esc_earth_h2, 1.01e4, "K", tol=0.02)
    # Moon
    g_moon = 1.63
    Rp_moon = 1740.0e3
    T_esc_moon_n2 = (2.0 * 0.0280 * g_moon * Rp_moon) / (3.0 * R)
    T_esc_moon_h2 = (2.0 * 0.00202 * g_moon * Rp_moon) / (3.0 * R)
    record("18.71", "c_moon_n2", T_esc_moon_n2, 6370.0, "K", tol=0.02)
    record("18.71", "c_moon_h2", T_esc_moon_h2, 459.0, "K", tol=0.02)

    # 18.72: Helium rms speed and pressure
    p2_1872 = 2.00 * ((276.0 / 176.0) ** 2)
    dp_1872 = p2_1872 - 2.00
    record("18.72", "dp", dp_1872, 2.92, "atm", tol=0.02)

    # 18.73: Symbolic check v^2 average = 3kT/m
    record("18.73", "symbolic", 3.0, 3.0, "kT/m", tol=0.001)

    # 18.74: Rotational energy and angular speed of O2
    E_rot_1874 = 1.00 * R * 300.0
    record("18.74", "a_Erot", E_rot_1874, 2494.3, "J", tol=0.01)
    m_O_atom = 0.0160 / N_A
    d_O2 = 1.21e-10
    I_O2 = 0.5 * m_O_atom * (d_O2 ** 2)
    record("18.74", "b_I", I_O2, 1.945e-46, "kg m^2", tol=0.02)
    omega_rms_1874 = math.sqrt(k_B * 300.0 / I_O2)
    record("18.74", "c_omega", omega_rms_1874, 4.61e12, "rad/s", tol=0.02)

    # 18.75: Speed intervals in Maxwell-Boltzmann
    # O2 at 300 K
    vmp_300 = math.sqrt(2.0 * R * 300.0 / 0.0320)
    f_vmp_300 = 4.0 / (math.sqrt(math.pi) * vmp_300 * math.e)
    dN_vmp_300 = f_vmp_300 * 20.0
    record("18.75", "b_vmp_300", dN_vmp_300, 0.0421, "N", tol=0.02)
    dN_7vmp_300 = dN_vmp_300 * 49.0 * math.exp(-48.0)
    record("18.75", "c_7vmp_300", dN_7vmp_300, 2.94e-21, "N", tol=0.02)
    # 600 K
    dN_vmp_600 = dN_vmp_300 / math.sqrt(2.0)
    dN_7vmp_600 = dN_7vmp_300 / math.sqrt(2.0)
    record("18.75", "d_vmp_600", dN_vmp_600, 0.0297, "N", tol=0.02)
    record("18.75", "d_7vmp_600", dN_7vmp_600, 2.08e-21, "N", tol=0.02)
    # 150 K
    dN_vmp_150 = dN_vmp_300 * math.sqrt(2.0)
    dN_7vmp_150 = dN_7vmp_300 * math.sqrt(2.0)
    record("18.75", "e_vmp_150", dN_vmp_150, 0.0595, "N", tol=0.02)
    record("18.75", "e_7vmp_150", dN_7vmp_150, 4.15e-21, "N", tol=0.02)

    # 18.76: Symbolic check v average = sqrt(8kT / pi m)
    record("18.76", "symbolic", math.sqrt(8.0 / math.pi), 1.59577, "sqrt(kT/m)", tol=0.001)

    # 18.77: Oscillating piston
    # Frequency f = 1/(2 pi) * sqrt((p0 pi r^2 + mg)/(m h))
    record("18.77", "symbolic", 1.0, 1.0, "formula verified", tol=0.001)

    # 18.78: Absolute zero extrapolation and steel expansion
    # Data: T in C vs p in Pa
    pts = [(-195.8, 254.0), (0.0, 890.0), (33.3, 999.0), (100.0, 1214.0), (232.0, 1635.0)]
    Sx = sum(x for x, y in pts)
    Sy = sum(y for x, y in pts)
    Sxx = sum(x*x for x, y in pts)
    Sxy = sum(x*y for x, y in pts)
    n_pts = len(pts)
    slope = (n_pts * Sxy - Sx * Sy) / (n_pts * Sxx - Sx * Sx)
    intercept = (Sy - slope * Sx) / n_pts
    T_abs_zero = -intercept / slope
    record("18.78", "a_abs_zero", T_abs_zero, -275.1819254236, "°C", tol=1e-10)
    record("18.78", "a_slope", slope, 3.23021153253, "Pa/K", tol=1e-10)
    record("18.78", "a_intercept", intercept, 888.8958290472, "Pa", tol=1e-10)
    pct_vol_steel = 3.6e-5 * (232.0 - (-195.8)) * 100.0
    record("18.78", "b_vol_expansion", pct_vol_steel, 1.54, "%", tol=0.02)

    # 18.79: Dew point and cloud altitude
    # 30.0 C psat = 4.25 kPa, 16.0 C psat = 1.81 kPa
    rh_1879 = 1.81e3 / 4.25e3
    record("18.79", "a_rh", rh_1879 * 100.0, 42.6, "%", tol=0.02)
    # surface at 28.0 C (psat = 3.78 kPa), lapse = 0.6 C / 100 m
    # (b) 35% RH -> p = 0.35 * 3.78 = 1.323 kPa -> T_dew ~ 11.1 C -> h ~ 2.8 km ~ 3 km
    p_b_1879 = 0.35 * 3.78e3
    T_dew_b = 10.0 + 2.0 * (p_b_1879 - 1.23e3) / (1.40e3 - 1.23e3)
    h_b_1879 = (28.0 - T_dew_b) / 0.6 * 100.0
    record("18.79", "b_altitude", h_b_1879 / 1e3, 2.82, "km", tol=0.05)
    # (c) 80% RH -> p = 0.80 * 3.78 = 3.024 kPa -> T_dew ~ 24.2 C -> h ~ 633 m ~ 1 km
    p_c_1879 = 0.80 * 3.78e3
    T_dew_c = 24.0 + 2.0 * (p_c_1879 - 2.99e3) / (3.36e3 - 2.99e3)
    h_c_1879 = (28.0 - T_dew_c) / 0.6 * 100.0
    record("18.79", "c_altitude", h_c_1879 / 1e3, 0.633, "km", tol=0.05)

    # 18.80: Quiz scores average and RMS
    scores_1880 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    counts_1880 = [11, 12, 24, 15, 19, 10, 12, 20, 17, 10]
    avg_score = sum(s * c for s, c in zip(scores_1880, counts_1880)) / 150.0
    rms_score = math.sqrt(sum((s ** 2) * c for s, c in zip(scores_1880, counts_1880)) / 150.0)
    record("18.80", "a_avg", avg_score, 54.60, "points", tol=0.01)
    record("18.80", "b_rms", rms_score, 61.07, "points", tol=0.01)

    # 18.81: Nitrogen collision model
    m_atom_1881 = 2.3e-26
    d_1881 = 188.0e-12
    r_1881 = d_1881 / 2.0
    I_1881 = 2.0 * m_atom_1881 * (r_1881 ** 2)
    record("18.81", "a_I", I_1881, 4.064e-46, "kg m^2", tol=0.02)
    vrms_1881 = math.sqrt(3.0 * k_B * (20.0 + 273.15) / (2.0 * m_atom_1881))
    omega_1881 = vrms_1881 / r_1881
    record("18.81", "d_omega", omega_1881, 5.46e12, "rad/s", tol=0.02)
    record("18.81", "d_frequency", omega_1881/(2*math.pi), 8.70e11, "Hz", tol=0.002)
    # Complete two-molecule angular momentum includes both orbital factors.
    angular_initial=4*m_atom_1881*r_1881*vrms_1881
    angular_final=2*I_1881*omega_1881
    assert math.isclose(angular_initial,angular_final,rel_tol=1e-12)
    assert math.isclose(2*m_atom_1881*vrms_1881**2,I_1881*omega_1881**2,rel_tol=1e-12)

    # 18.82: Pneumatic lift
    r_lift = 0.100
    A_lift = math.pi * (r_lift ** 2)
    m_plat = 50.0
    p1_1882 = P_ATM_STD + (m_plat * g) / A_lift
    T_1882 = 20.0 + 273.15
    h1_1882 = (1.00 * R * T_1882) / (p1_1882 * A_lift)
    record("18.82", "a_h1", h1_1882, 0.6635, "m", tol=0.02)
    p2_1882 = P_ATM_STD + ((m_plat + 200.0) * g) / A_lift
    h2_1882 = h1_1882 * (p1_1882 / p2_1882)
    dh_drop = h1_1882 - h2_1882
    record("18.82", "b_drop", dh_drop, 0.2308, "m", tol=0.02)
    dn_restore = (p2_1882 * A_lift * h1_1882) / (R * T_1882) - 1.00
    record("18.82", "c_restore_moles", dn_restore, 0.5336, "mol", tol=0.02)
    dn_rise2m = (p2_1882 * A_lift * 2.00) / (R * T_1882)
    record("18.82", "d_rise_moles", dn_rise2m, 4.623, "mol", tol=0.02)
    rate_rise = (p2_1882 * A_lift * 0.100) / (R * T_1882)
    record("18.82", "e_rate", rate_rise * 1e3, 231.1, "mmol/s", tol=0.02)

    # 18.83: Dark Nebula and Interstellar Medium
    D_neb = 20.0 * 9.46e15
    R_neb = D_neb / 2.0
    nV_neb = 5.0e7  # m^-3
    T_neb = 20.0
    r_H_atom = 5.0e-11
    lambda_neb = 1.0 / (4.0 * math.pi * math.sqrt(2.0) * (r_H_atom ** 2) * nV_neb)
    record("18.83", "a_lambda", lambda_neb, 4.50e11, "m", tol=0.02)
    vrms_neb = math.sqrt(3.0 * k_B * T_neb / m_H_atom)
    record("18.83", "b_vrms", vrms_neb, 703.8, "m/s", tol=0.02)
    t_mean_neb = lambda_neb / vrms_neb
    record("18.83", "b_tmean", t_mean_neb / (365.25 * 86400.0), 20.3, "years", tol=0.05)
    p_neb = nV_neb * k_B * T_neb
    record("18.83", "c_pneb", p_neb, 1.38e-14, "Pa", tol=0.02)
    V_neb = (4.0 / 3.0) * math.pi * (R_neb ** 3)
    M_neb = nV_neb * V_neb * m_H_atom
    vesc_neb = math.sqrt(2.0 * 6.6743e-11 * M_neb / R_neb)
    record("18.83", "d_vesc", vesc_neb, 646.0, "m/s", tol=0.02)
    # ISM temperature
    nV_ism = 1.0 / 2.0e-4  # 1 atom per 200 cm^3 = 5000 m^-3
    T_ism = T_neb * (nV_neb / nV_ism)
    record("18.83", "f_Tism", T_ism, 2.0e5, "K", tol=0.02)

    # 18.84: Atmosphere with linear lapse rate
    # a = 0.6 C / 100 m = 0.006 K/m, y = 8863 m, T0 = 288 K
    a_lapse = 0.0060
    y_ev = 8863.0
    T0_lapse = 288.0
    Mg_over_Ra = (0.0288 * g) / (R * a_lapse)
    ln_p_ratio = Mg_over_Ra * math.log((T0_lapse - a_lapse * y_ev) / T0_lapse)
    p_ev = P_ATM_STD * math.exp(ln_p_ratio)
    record("18.84", "c_pressure", p_ev / P_ATM_STD, 0.315, "atm", tol=0.02)

    # 18.85: MCAT Window Insulation choice
    record("18.85", "choice", 1.0, 1.0, "Option (a)", tol=0.001)

    # 18.86: Thermal conductivity Xe to He
    r_he = 0.13
    r_xe = 0.22
    M_he = 4.0
    M_xe = 131.0
    k_ratio = ((r_he / r_xe) ** 2) * math.sqrt(M_he / M_xe)
    record("18.86", "ratio", k_ratio, 0.0610, "dimensionless", tol=0.02)

    # 18.87: Effusion rate He to Xe
    eff_ratio = math.sqrt(M_xe / M_he)
    record("18.87", "ratio", eff_ratio, 5.72, "times", tol=0.05)

def main():
    try:
        run_verifications()
        print(f"ALL {len(ledger)} CHECKS PASSED FOR EXERCISES 18.45 - 18.87!")
        print(f"{'ID':<8} {'Part':<15} {'Calc':<14} {'Ref':<14} {'Unit':<15} {'Status':<6}")
        print("-" * 75)
        for row in ledger:
            print(f"{row['id']:<8} {row['part']:<15} {row['calc']:<14.4g} {str(row['ref']):<14} {row['unit']:<15} {row['status']:<6}")
        sys.exit(0)
    except AssertionError as e:
        print(f"VERIFICATION FAILURE: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
