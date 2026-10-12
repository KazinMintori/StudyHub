"""Independent numerical checks for Chapter 24 problems 69–76."""

from math import log, pi, isclose

EPS0 = 8.8541878128e-12

# 24.69: slope is read from the plotted graph in units of nJ per cm^-1.
graph_slope = 3.67e-11  # J m
voltage_69 = 24.0
area_69 = 2 * graph_slope / (EPS0 * voltage_69**2)
assert isclose(area_69, 1.4392e-2, rel_tol=2e-3)

# 24.70: air and dielectric-filled axial segments are parallel branches.
length, a, b, outer_dielectric, K = 0.100, 0.0100, 0.0400, 0.0300, 3.21
c_air = 2 * pi * EPS0 / log(b / a)
c_dielectric = 2 * pi * EPS0 / (log(outer_dielectric / a) / K + log(b / outer_dielectric))
c_zero = c_air * length
c_full = c_dielectric * length
required_c = 6.00e-9 / 1.00e3
x_70 = (required_c - c_zero) / (c_dielectric - c_air)
assert isclose(c_zero, 4.0130e-12, rel_tol=1e-4)
assert isclose(c_full, 8.8316e-12, rel_tol=1e-4)
assert isclose(x_70, 0.041236, rel_tol=1e-4)
assert 0 <= x_70 <= length

# 24.71: numerical integration checks the closed-form series-slice result.
gap, plate_area, K_end = 0.030, 0.020, 3.2
K_of_x = lambda x: 1 + (K_end - 1) * x / gap
n = 100_000
dx = gap / n
integrand_sum = sum(1 / K_of_x((i + 0.5) * dx) for i in range(n)) * dx
c_integral = EPS0 * plate_area / integrand_sum
c_closed = EPS0 * plate_area * (K_end - 1) / (gap * log(K_end))
c_limit = EPS0 * plate_area / gap
assert isclose(c_integral, c_closed, rel_tol=1e-9)
assert isclose(EPS0 * plate_area * 1e-8 / (gap * log(1 + 1e-8)), c_limit, rel_tol=1e-7)

# 24.72: differentiate C(x), compare fixed-V and fixed-Q energy changes,
# and verify that battery work reverses the misleading fixed-V inference.
plate_side, gap_72, dielectric_K, voltage_72 = 0.080, 0.0020, 3.5, 100.0
dCdx = (dielectric_K - 1) * EPS0 * plate_side / gap_72
C_before = EPS0 * plate_side**2 / gap_72 + dCdx * 0.030
step = 1e-8
dC = dCdx * step
dU_fixed_v = 0.5 * voltage_72**2 * dC
Q_fixed = C_before * voltage_72
dU_fixed_q = Q_fixed**2 / (2 * (C_before + dC)) - Q_fixed**2 / (2 * C_before)
dW_battery = voltage_72**2 * dC
dW_mechanical_external = dU_fixed_v - dW_battery
assert dU_fixed_v > 0 and dU_fixed_q < 0
assert isclose(dW_mechanical_external, -0.5 * voltage_72**2 * dC, rel_tol=1e-7)
force_72 = 0.5 * voltage_72**2 * dCdx
assert force_72 > 0

# 24.73: capacitor charge per area divided by Faraday's number.
capacitance_density = 1.0e-6  # F/cm^2
delta_vm = 0.100  # V
faraday = 1.0e5  # C/mol
na_moles_per_area = capacitance_density * delta_vm / faraday
assert isclose(na_moles_per_area, 1e-12, rel_tol=1e-12)

# 24.74: spherical sea-urchin egg, diameter 200 micrometres.
radius_cm = 100e-4  # 100 um = 0.0100 cm
surface_area_cm2 = 4 * pi * radius_cm**2
volume_l = (4 / 3) * pi * radius_cm**3 * 1e-3  # cm^3 -> L
initial_na_moles = 0.030 * volume_l
additional_na_moles = na_moles_per_area * surface_area_cm2
fractional_na_change = additional_na_moles / initial_na_moles
assert isclose(volume_l, 4.1887902e-9, rel_tol=1e-7)
assert isclose(fractional_na_change, 1e-5, rel_tol=1e-10)

# 24.75: Ca2+ carries twice the charge per ion, so half as many ions are needed.
calcium_to_sodium_count = 1 / 2
assert calcium_to_sodium_count == 0.5

# 24.76: increase in capacitor energy as Vm changes from +30 mV to -70 mV.
delta_u_per_area = 0.5 * capacitance_density * (0.070**2 - 0.030**2)
delta_u_total = delta_u_per_area * surface_area_cm2
assert isclose(delta_u_total, 2.5132741e-12, rel_tol=1e-7)

print(f"24.69: A = {area_69:.6g} m^2 ({area_69 * 1e4:.4g} cm^2)")
print(f"24.70: C(0) = {c_zero:.6g} F, C(L) = {c_full:.6g} F, x = {x_70:.6g} m")
print(f"24.71: integral/formula agree; K -> 1 gives {c_limit:.6g} F")
print(f"24.72: fixed-V dU > 0, fixed-Q dU < 0, force into capacitor = {force_72:.6g} N")
print(f"24.73: Na+ = {na_moles_per_area:.6g} mol/cm^2")
print(f"24.74: fractional concentration change = {fractional_na_change:.6g}")
print(f"24.75: Ca2+/Na+ count = {calcium_to_sodium_count:.3g}")
print(f"24.76: delta U = {delta_u_total:.6g} J")
