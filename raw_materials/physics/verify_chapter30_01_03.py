"""Recompute and verify all numerical results and relationships used in Chapter 30, Sections 30.1–30.3."""
import math

mu_0 = 4.0 * math.pi * 1e-7

# ==============================================================================
# Section 30.1: Mutual Inductance
# ==============================================================================

# Example 30.1: Calculating mutual inductance of long solenoid (1) and outer coil (2)
length_301 = 0.50          # m
area_301 = 10.0 * 1e-4      # 10 cm^2 = 1.0e-3 m^2
n1_301 = 1000              # turns
n2_301 = 10                # turns

# M = mu_0 * A * N1 * N2 / l
m_301 = mu_0 * area_301 * n1_301 * n2_301 / length_301
m_301_rounded = 25e-6      # 25 microhenry as quoted in textbook

assert math.isclose(m_301, 2.513274e-5, rel_tol=1e-5)
assert math.isclose(m_301_rounded, 25e-6, rel_tol=1e-12)
print(f"Example 30.1: M = {m_301:.6e} H (~ {m_301*1e6:.1f} uH, textbook: 25 uH)")

# Example 30.2: Emf due to mutual inductance
# i2 = (2.0e6 A/s) * t
di2_dt_302 = 2.0e6         # A/s
t_302 = 3.0e-6             # 3.0 us
i2_302 = di2_dt_302 * t_302 # 6.0 A
assert math.isclose(i2_302, 6.0, rel_tol=1e-12)

# Average flux per turn through solenoid 1 using M = 25 uH:
# N1 * Phi_B1 = M * i2 => Phi_B1 = M * i2 / N1
flux_b1_302 = (m_301_rounded * i2_302) / n1_301
assert math.isclose(flux_b1_302, 1.5e-7, rel_tol=1e-12)

# Induced emf in solenoid 1:
# E1 = -M * (di2/dt)
emf1_302 = -m_301_rounded * di2_dt_302
assert math.isclose(emf1_302, -50.0, rel_tol=1e-12)
print(f"Example 30.2: i2(3 us) = {i2_302:.2f} A, Phi_B1 = {flux_b1_302:.2e} Wb, E1 = {emf1_302:.1f} V")

# Test Your Understanding 30.1
# Both N1 and l doubled: N1' = 2*N1, l' = 2*l
m_301_ratio = (2.0 * n1_301) / (2.0 * length_301)
assert math.isclose(m_301_ratio, n1_301 / length_301, rel_tol=1e-12)
print("TYU 30.1: Ratio (N1/l) unchanged -> M unchanged (Option iii)")

# ==============================================================================
# Section 30.2: Self-Inductance and Inductors
# ==============================================================================

# Example 30.3: Calculating self-inductance of toroidal solenoid
n_303 = 200
area_303 = 5.0 * 1e-4       # 5.0 cm^2 = 5.0e-4 m^2
r_303 = 0.10               # m

# L = mu_0 * N^2 * A / (2 * pi * r)
l_303 = (mu_0 * (n_303**2) * area_303) / (2.0 * math.pi * r_303)
l_303_rounded = 40e-6      # 40 uH

assert math.isclose(l_303, 40e-6, rel_tol=1e-12)
print(f"Example 30.3: L = {l_303:.6e} H = {l_303*1e6:.1f} uH")

# Example 30.4: Calculating self-induced emf
# Current increases uniformly from 0 to 6.0 A in 3.0 us
delta_i_304 = 6.0          # A
delta_t_304 = 3.0e-6       # 3.0 us (verified against source page image)
di_dt_304 = delta_i_304 / delta_t_304
assert math.isclose(di_dt_304, 2.0e6, rel_tol=1e-12)

# Magnitude of self-induced emf: |E| = L * |di/dt|
abs_emf_304 = l_303 * di_dt_304
assert math.isclose(abs_emf_304, 80.0, rel_tol=1e-12)
print(f"Example 30.4: di/dt = {di_dt_304:.2e} A/s, |E| = {abs_emf_304:.1f} V")

# Test Your Understanding 30.2
# Inductor potential difference: V_ab = L * (di/dt)
# Case (i): L = 2.0 uH, i: 1.0 A -> 2.0 A in 0.50 s
v_ab_i = 2.0e-6 * (2.0 - 1.0) / 0.50
assert math.isclose(v_ab_i, 4.0e-6, rel_tol=1e-12)

# Case (ii): L = 4.0 uH, i: 3.0 A -> 0 A in 2.0 s
v_ab_ii = 4.0e-6 * (0.0 - 3.0) / 2.0
assert math.isclose(v_ab_ii, -6.0e-6, rel_tol=1e-12)

# Case (iii): L = 1.0 uH, i = 4.0 A constant
v_ab_iii = 0.0

# Case (iv): L = 1.0 uH, i: 0 -> 4.0 A in 0.25 s
v_ab_iv = 1.0e-6 * (4.0 - 0.0) / 0.25
assert math.isclose(v_ab_iv, 16.0e-6, rel_tol=1e-12)

ranking = sorted([("i", v_ab_i), ("ii", v_ab_ii), ("iii", v_ab_iii), ("iv", v_ab_iv)],
                 key=lambda item: item[1], reverse=True)
order = [item[0] for item in ranking]
assert order == ["iv", "i", "iii", "ii"]
print(f"TYU 30.2: Ranking = {order} with V_ab values: iv={v_ab_iv*1e6:.1f} uV, i={v_ab_i*1e6:.1f} uV, iii={v_ab_iii*1e6:.1f} uV, ii={v_ab_ii*1e6:.1f} uV")

# ==============================================================================
# Section 30.3: Magnetic-Field Energy
# ==============================================================================

# MRI Magnetic energy density: B = 1.5 T in vacuum
b_mri = 1.5
u_mri = (b_mri**2) / (2.0 * mu_0)
assert math.isclose(u_mri, 8.952465e5, rel_tol=1e-4)
print(f"Section 30.3 MRI: u = {u_mri:.2e} J/m^3 (~ 9.0e5 J/m^3)")

# Example 30.5: Storing energy in an inductor
u_energy_305 = 1.00 * 1000.0 * 3600.0  # 1.00 kW*h in Joules = 3.60e6 J
current_305 = 200.0                    # A
# U = 0.5 * L * I^2 => L = 2 * U / I^2
l_305 = 2.0 * u_energy_305 / (current_305**2)
assert math.isclose(u_energy_305, 3.60e6, rel_tol=1e-12)
assert math.isclose(l_305, 180.0, rel_tol=1e-12)
print(f"Example 30.5: U = {u_energy_305:.2e} J, I = {current_305:.1f} A -> L = {l_305:.1f} H")

# Test Your Understanding 30.3
# Current reversed: I' = -I => B' = -B (changes direction)
# u' = B'^2 / (2*mu_0) = (-B)^2 / (2*mu_0) = B^2 / (2*mu_0) = u (unchanged)
b_orig = 1.2
b_rev = -b_orig
assert math.isclose((b_rev**2) / (2.0 * mu_0), (b_orig**2) / (2.0 * mu_0), rel_tol=1e-12)
print("TYU 30.3: (a) B changes direction -> Yes; (b) u proportional to B^2 -> No change")

print("\nALL CHAPTER 30.1-30.3 NUMERICAL CHECKS PASSED SUCCESSFULLY!")
