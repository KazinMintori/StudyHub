"""Independent calculations for Chapter 25 exercises 25.1–25.30."""
from math import pi, isclose

e = 1.602176634e-19
NA = 6.02214076e23
rho_ag = 1.47e-8
rho_cu = 1.72e-8
rho_au = 2.44e-8
rho_al = 2.75e-8
rho_ni = 100e-8
alpha_ni = 0.0004
alpha_carbon = -0.0005
n_cu = 8.5e28

out = {}

# 25.1: Current and duration. Source scan visibly reads 40 microseconds.
out[1] = 25_000 * 40e-6
assert isclose(out[1], 1.0)

# 25.2: Silver wire charge transfer and drift.
d = 2.6e-3
A = pi * (d / 2) ** 2
I = 420 / (80 * 60)
vd = I / (5.8e28 * e * A)
out[2] = (I, vd)

# 25.3: Electron rate, current density, drift speed, diameter scaling.
d = 2.05e-3
A = pi * (d / 2) ** 2
I = 5.00
out[3] = (I / e, I / A, I / (n_cu * e * A), (I / A) / 4)

# 25.4: Given J in a copper wire.
d = 1.02e-3
A = pi * (d / 2) ** 2
J = 3.20e6
out[4] = (J * A, J / (n_cu * e))

# 25.5: Given electric field in copper.
E = 0.0600
J = E / rho_cu
out[5] = (J / (n_cu * e), E * 0.200)

# 25.6: Three wires with R=1 ohm, diameter 1 mm; gold mass and price factor.
d = 1.00e-3
A = pi * (d / 2) ** 2
lengths = {"gold": A / 2.44e-8, "copper": A / rho_cu, "aluminum": A / rho_al}
gold_mass_kg = 1.93e4 * A * lengths["gold"]
out[6] = (lengths, gold_mass_kg, gold_mass_kg * 1000)  # grams; total cost = grams * unit price/gram

# 25.7: Integrate I(t) = 55 - 0.65 t^2 from 0 to 8 s.
Q = 55 * 8 - 0.65 * 8**3 / 3
out[7] = (Q, Q / 8)

# 25.8: Na+ and Cl- both contribute to conventional current in the same direction.
out[8] = ((2.68e16 + 3.92e16) * e / 1.00, "from positive electrode to negative electrode")

# 25.9: Charge from sodium ions entering 1 m of axon in 10 ms.
out[9] = (5.6e11 * e) / 0.010

# 25.10: Silver conduction electron density, one electron per atom.
n_ag = 10.5e3 / 0.108 * NA
out[10] = (n_ag, n_ag / n_cu)

# 25.11: Slope dI/d(1/d) = V A/rho.
wire_A = pi * (0.800e-3) ** 2
out[11] = 12.0 * wire_A / 600

# 25.12: E = rho I/A for copper and silver.
wire_A = pi * (2.05e-3 / 2) ** 2
out[12] = (rho_cu * 4.50 / wire_A, rho_ag * 4.50 / wire_A)

# 25.13: Rod resistivity and temperature coefficient, no thermal expansion.
rod_A = pi * (0.500e-2 / 2) ** 2
R20 = 15.0 / 18.5
R92 = 15.0 / 17.2
rho20 = R20 * rod_A / 1.50
alpha = (R92 / R20 - 1) / (92.0 - 20.0)
out[13] = (rho20, alpha)

# 25.14: Square wire, current density, field, drift speed and travel time.
wire_A = (2.3e-3) ** 2
J = 3.6 / wire_A
vd = J / (n_cu * e)
out[14] = (J, rho_cu * J, 4.0 / vd, vd)

# 25.15: Millivolt-scale drops, using the textbook's gauge diameters.
wire_A = pi * (1.628e-3 / 2) ** 2
out[15] = (0.0125 * rho_cu * 2.00 / wire_A, 0.0125 * rho_ag * 2.00 / wire_A)

# 25.16: Identify material by inferred resistivity.
wire_A = pi * (2.05e-3 / 2) ** 2
rho_wire = 0.0290 * wire_A / 6.50
out[16] = (rho_wire, "silver is closest among listed common metals")

# 25.17: E ratio at equal current.
out[17] = (rho_cu / rho_ag) * (0.500 / 0.800) ** 2

# 25.18: Stretch to 3L at constant volume and material resistivity.
out[18] = 9.0

# 25.19: Household copper wire.
wire_A = pi * (2.05e-3 / 2) ** 2
out[19] = rho_cu * 24.0 / wire_A

# 25.20: Equal R and length, rho_Cu/A_Cu = rho_Al/A_Al.
out[20] = 2.14 * (rho_cu / rho_al) ** 0.5

# 25.21: Gold wire, E given.
wire_A = pi * (0.84e-3 / 2) ** 2
J = 0.49 / rho_au
I = J * wire_A
R = rho_au * 6.4 / wire_A
out[21] = (I, 0.49 * 6.4, R)

# 25.22: Infer resistivity from V, I and geometry.
wire_A = pi * (0.654e-3) ** 2
out[22] = 4.50 * wire_A / (2.50 * 17.6)

# 25.23: Temperature coefficient table: nichrome +0.0004, graphite -0.0005.
out[23] = (
    100.00 * (1 + alpha_ni * (0.0 - 11.5)),
    0.0160 * (1 + alpha_carbon * (25.8 - 0.0)),
)

# 25.24: Carbon thermometer, reference at 4 C.
out[24] = 4.0 + (215.8 / 217.3 - 1) / alpha_carbon

# 25.25: 100 km copper cable, diameter 10.0 cm.
cable_A = pi * (0.100 / 2) ** 2
R_cable = rho_cu * 100_000 / cable_A
V_drop = 125 * R_cable
energy_hour = 125**2 * R_cable * 3600
out[25] = (R_cable, V_drop, energy_hour)

# 25.26: Terminal voltage while supplying 4 A.
out[26] = ((24.0 - 21.2) / 4.00, 21.2 / 4.00)

# 25.27: Ideal voltmeter in series opens the loop.
out[27] = (0.0, 5.0, 5.0)

# 25.28: Ideal ammeter shorts the battery terminals.
out[28] = (10.0 / 2.00, 0.0, 0.0)

# 25.29: Open-circuit emf, loaded terminal voltage, current.
emf = 3.08
I = 1.65
V_terminal = 2.97
out[29] = (emf, (emf - V_terminal) / I, V_terminal / I)

# 25.30: Both batteries have + on the left; they oppose around the loop.
I = (16.0 - 8.0) / (1.6 + 9.0 + 1.4 + 5.0)
Vab = 16.0 - I * 1.6
Vac = Vab - I * 9.0
# Set Vc=0 and record the circuit-node potentials for part (d).
Vc = 0.0
Vb = Vc - I * 9.0
Va = Vb + Vab
Vd = Vc + 8.0 + I * 1.4
out[30] = (I, "counterclockwise", Vab, Vac, {"a": Va, "b": Vb, "c": Vc, "d": Vd})

assert isclose(out[1], 1.0)
assert isclose(out[2][0], 0.0875)
assert isclose(out[7][0], 329.0666666667)
assert isclose(out[10][0], 5.86e28, rel_tol=2e-3)
assert isclose(out[13][1], 0.00105, rel_tol=5e-3)
assert isclose(out[15][0], 0.206e-3, rel_tol=2e-2)
assert isclose(out[15][1], 0.176e-3, rel_tol=2e-2)
assert isclose(out[17], 0.457, rel_tol=2e-3)
assert isclose(out[25][1], 27.4, rel_tol=3e-3)
assert isclose(out[25][2] / 1e6, 12.3, rel_tol=3e-3)
assert isclose(out[26][0], 0.700)
assert isclose(out[26][1], 5.30)
assert out[27] == (0.0, 5.0, 5.0)
assert out[28] == (5.0, 0.0, 0.0)
assert isclose(out[29][1], 0.0666666667)
assert isclose(out[29][2], 1.80)
assert isclose(out[30][0], 8 / 17)
assert out[30][1] == "counterclockwise"
assert isclose(out[30][2], 15.2470588235)
assert isclose(out[30][3], 11.0117647059)
assert isclose(out[30][4]["a"] - out[30][4]["d"], 5 * out[30][0])
assert isclose(out[30][4]["d"] - out[30][4]["c"], 8 + 1.4 * out[30][0])
assert isclose(out[30][4]["c"] - out[30][4]["b"], 9 * out[30][0])

for problem, result in out.items():
    print(f"25.{problem}: {result}")
