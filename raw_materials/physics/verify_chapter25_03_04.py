"""Independent arithmetic checks for the worked examples in Ch. 25.3–25.4."""
from math import isclose

# Example 25.2: copper wire
rho = 1.72e-8
area = 8.17e-7
current = 1.67
length = 50.0
j = current / area
field = rho * j
voltage = field * length
resistance = rho * length / area
assert isclose(field, 0.03516, rel_tol=3e-4)
assert isclose(voltage, 1.758, rel_tol=3e-4)
assert isclose(resistance, 1.05263, rel_tol=1e-5)
assert isclose(voltage / current, resistance, rel_tol=2e-3)

# Example 25.3: linear resistance-temperature approximation.
R0, alpha, T0 = 1.05, 0.00393, 20.0
R_0C = R0 * (1 + alpha * (0 - T0))
R_100C = R0 * (1 + alpha * (100 - T0))
ratio = R_100C / R_0C
assert isclose(R_0C, 0.96747, rel_tol=1e-6)
assert isclose(R_100C, 1.38012, rel_tol=1e-6)
assert isclose(ratio, 1.42652, rel_tol=1e-5)

# Conceptual Example 25.4; Examples 25.5–25.7.
emf, r_internal, R_load = 12.0, 2.0, 4.0
I_open = 0.0
V_open = emf - I_open * r_internal
I_loaded = emf / (R_load + r_internal)
V_loaded = emf - I_loaded * r_internal
I_short = emf / r_internal
V_short = 0.0
assert (V_open, I_open) == (12.0, 0.0)
assert (I_loaded, V_loaded) == (2.0, 8.0)
assert (I_short, V_short) == (6.0, 0.0)

# Conceptual Example 25.6: ideal instruments.
V_a = V_loaded  # Voltmeter across load, ammeter in series.
I_a = I_loaded
V_b = emf       # Ideal voltmeter is in series, opening the circuit.
I_b = 0.0
assert (V_a, I_a, V_b, I_b) == (8.0, 2.0, 12.0, 0.0)

# Section 25.4 end check: rank (iii), (ii), (i).
I_i = 1.5 / (1.4 + 0.10)
I_ii = 3.6 / 1.8
I_iii = (12.0 - 11.0) / 0.20
assert (I_iii, I_ii, I_i) == (5.0, 2.0, 1.0)

print(f"25.2 J={j:.6g} A/m^2, E={field:.6g} V/m, V={voltage:.6g} V, R={resistance:.6g} ohm")
print(f"25.3 R(0 C)={R_0C:.6g} ohm, R(100 C)={R_100C:.6g} ohm, ratio={ratio:.6g}")
print(f"25.4 open (V,I)=({V_open:g} V,{I_open:g} A), loaded ({V_loaded:g} V,{I_loaded:g} A), short ({V_short:g} V,{I_short:g} A)")
print(f"25.4 ranking currents: (iii) {I_iii:g} A > (ii) {I_ii:g} A > (i) {I_i:g} A")
