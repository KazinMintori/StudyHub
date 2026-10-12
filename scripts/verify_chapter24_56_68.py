#!/usr/bin/env python3
"""Independent numerical checks for Young & Freedman Ch. 24, problems 56–68."""
from math import isclose, pi, log

EPS0 = 8.8541878128e-12

def close(actual, expected, rel=2e-9, abs_tol=1e-12):
    assert isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol), (actual, expected)

def solve_linear(a, b):
    """Gaussian elimination with partial pivoting for small nodal systems."""
    n = len(b)
    m = [list(map(float, row)) + [float(rhs)] for row, rhs in zip(a, b)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(m[row][col]))
        if abs(m[pivot][col]) < 1e-15:
            raise ValueError("Singular nodal system")
        m[col], m[pivot] = m[pivot], m[col]
        scale = m[col][col]
        m[col] = [v / scale for v in m[col]]
        for row in range(n):
            if row == col:
                continue
            factor = m[row][col]
            m[row] = [x - factor * y for x, y in zip(m[row], m[col])]
    return [m[i][-1] for i in range(n)]

# 24.56, switch open then closed. Capacities are in microfarads.
Q_top_open_uC = (3.0 * 6.0 / (3.0 + 6.0)) * 210.0
Q_bottom_open_uC = (6.0 * 3.0 / (6.0 + 3.0)) * 210.0
Vd_open = 210.0 - Q_top_open_uC / 3.0
Vc_open = 210.0 - Q_bottom_open_uC / 6.0
Vcd_open = Vc_open - Vd_open
close(Vcd_open, 70.0)
Ceq56_uF = (3.0 + 6.0) * (6.0 + 3.0) / ((3.0 + 6.0) + (6.0 + 3.0))
Vmid56 = 210.0 / 2.0
Q56_closed_uC = [3.0 * Vmid56, 6.0 * Vmid56, 6.0 * Vmid56, 3.0 * Vmid56]
Qthrough_switch_uC = 3.0 * (Vmid56 - 210.0) + 6.0 * Vmid56
close(Ceq56_uF, 4.5)
for got, want in zip(Q56_closed_uC, [315.0, 630.0, 630.0, 315.0]):
    close(got, want)
close(Qthrough_switch_uC, 315.0)

# 24.57, series charge and energy before and after isolated redistribution.
C57_uF = 1.0 / (1.0 / 8.4 + 1.0 / 8.4 + 1.0 / 4.2)
Q57_uC = C57_uF * 36.0
U57_initial_mJ = 0.5 * C57_uF * 36.0**2 / 1000.0
Q57_parallel_total_uC = 3.0 * Q57_uC
V57_parallel = Q57_parallel_total_uC / (8.4 + 8.4 + 4.2)
U57_final_mJ = 0.5 * (8.4 + 8.4 + 4.2) * V57_parallel**2 / 1000.0
close(Q57_uC, 75.6)
close(U57_initial_mJ, 1.3608)
close(Q57_parallel_total_uC, 226.8)
close(V57_parallel, 10.8)
close(U57_final_mJ, 1.22472)

# 24.58, parallel-plate cloud/ground model.
A58 = pi * (1000.0**2)
d58 = 3000.0
C58 = EPS0 * A58 / d58
Q58 = -20.0
V58 = Q58 / C58
E58 = abs(V58) / d58
U58 = Q58**2 / (2.0 * C58)
close(C58, 9.2720837954e-9)
close(V58, -2.157012430e9)
close(E58, 7.190041434e5)
close(U58, 2.157012430e10)

# 24.59, capacitance network solved from nodal equations. All capacitances in microfarads.
C1, C2 = 6.9, 4.6
edges59 = [
    ("a", "x1", C1), ("b", "y1", C1),
    ("x1", "x2", C1), ("y1", "y2", C1),
    ("x2", "x3", C1), ("y2", "y3", C1),
    ("x3", "y3", C1), ("x1", "y1", C2), ("x2", "y2", C2),
]
nodes59 = ["x1", "y1", "x2", "y2", "x3", "y3"]
ix59 = {node: i for i, node in enumerate(nodes59)}
known59 = {"a": 1.0, "b": 0.0}
mat59 = [[0.0 for _ in nodes59] for _ in nodes59]
rhs59 = [0.0 for _ in nodes59]
for u, v, cap in edges59:
    for node, other in ((u, v), (v, u)):
        if node in ix59:
            i = ix59[node]
            mat59[i][i] += cap
            if other in ix59:
                mat59[i][ix59[other]] -= cap
            else:
                rhs59[i] += cap * known59[other]
V59 = dict(zip(nodes59, solve_linear(mat59, rhs59)))
Ceq59_uF = C1 * (known59["a"] - V59["x1"])
Q59_near_terminal_uC = 420.0 * Ceq59_uF
Q59_rung_uC = 420.0 * C2 * (V59["x1"] - V59["y1"])
Vcd59 = 420.0 * (V59["x2"] - V59["y2"])
close(Ceq59_uF, 2.3)
close(Q59_near_terminal_uC, 966.0)
close(Q59_rung_uC, 644.0)
close(Vcd59, 46.6666666667)

# 24.60, conducting slab removes electric-field volume but does not touch plates.
def C60_ratio(d, a):
    return d / (d - a)
close(C60_ratio(1.0, 0.0), 1.0)
assert C60_ratio(1.0, 0.99) > 99.9

# 24.61, C1 and C2 in series, parallel with C3, then series with C4.
Ceq61_uF = 2.0 * 2.90e-3 / 48.0**2 * 1e6
Cad61_uF = 8.0 * Ceq61_uF / (8.0 - Ceq61_uF)
C3_61_uF = Cad61_uF - (4.0 * 4.0 / (4.0 + 4.0))
close(Ceq61_uF, 2.5173611111)
close(C3_61_uF, 1.6732108930)

# 24.62, coaxial capacitor energy density and integrated energy per length.
lam62, ra62, rb62, L62 = 2.3e-6, 0.01, 0.04, 0.2
u62_at_r = lam62**2 / (8.0 * pi**2 * EPS0 * (0.02**2))
UperL62_integral = lam62**2 / (4.0 * pi * EPS0) * log(rb62 / ra62)
CperL62 = 2.0 * pi * EPS0 / log(rb62 / ra62)
V62 = lam62 / CperL62
UperL62_cap = 0.5 * CperL62 * V62**2
close(UperL62_integral, UperL62_cap)
assert u62_at_r > 0.0 and L62 > 0.0

# 24.63, elastic-electrostatic equilibrium and voltage when Q and 2Q are applied.
A63, d0_63, K63, Y63 = 1.00e-4, 0.400e-3, 3.0, 0.0100e9
Q63 = 0.700e-6
s63 = d0_63 / (2.0 * K63 * EPS0 * Y63 * A63**2)
d63 = d0_63 - s63 * Q63**2
d2_63 = d0_63 - s63 * (2.0 * Q63)**2
V63 = Q63 * d63 / (K63 * EPS0 * A63)
V2_63 = 2.0 * Q63 * d2_63 / (K63 * EPS0 * A63)
close(s63, 7.529393782e7)
close(V63, 95.6888743e3)
close(V2_63, 133.0419164657e3)
assert d63 > 0.0 and d2_63 > 0.0

# 24.64, dielectric and air regions occupy half the plate area each, voltage fixed at 18 V.
A64, d64, V64, K64 = 0.12**2, 4.50e-3, 18.0, 3.40
C0_64 = EPS0 * A64 / d64
C_64 = (1.0 + K64) * C0_64 / 2.0
U_64 = 0.5 * C_64 * V64**2
U_air64 = 0.5 * C0_64 * V64**2
close(C_64, 6.2333482202e-11)
close(U_64, 1.0098024117e-8)
close(U_air64, 4.5900109622e-9)

# 24.65, constant-voltage parallel-plate capacitor and cable work.
r65, V65, d65 = 0.04, 100.0, 0.002
F65 = EPS0 * pi * r65**2 * V65**2 / (2.0 * d65**2)
Wcable65 = EPS0 * pi * r65**2 * V65**2 / (4.0 * d65)
Ui65 = EPS0 * pi * r65**2 * V65**2 / (2.0 * d65)
Uf65 = EPS0 * pi * r65**2 * V65**2 / (4.0 * d65)
close(Wcable65, Ui65 - Uf65)
assert Wcable65 > 0.0 and Uf65 < Ui65

# 24.66, area-weighted effective dielectric constant.
Kgas = 1.95
Kmethanol = 33.0
fractions = (0.25, 0.50, 0.75)
Keff_gas = [1.0 + (Kgas - 1.0) * h for h in fractions]
Keff_methanol = [1.0 + (Kmethanol - 1.0) * h for h in fractions]
for got, want in zip(Keff_gas, (1.2375, 1.475, 1.7125)):
    close(got, want)
for got, want in zip(Keff_methanol, (9.0, 17.0, 25.0)):
    close(got, want)

# 24.67, measured energy at the same applied voltage gives C_parallel and C_series.
V67 = 200.0
Cpar67_uF = 2.0 * 0.180 / V67**2 * 1e6
Cser67_uF = 2.0 * 0.0400 / V67**2 * 1e6
sum67 = Cpar67_uF
product67 = Cser67_uF * sum67
roots67 = ((sum67 + (sum67**2 - 4.0 * product67)**0.5) / 2.0,
           (sum67 - (sum67**2 - 4.0 * product67)**0.5) / 2.0)
close(Cpar67_uF, 9.0)
close(Cser67_uF, 2.0)
close(roots67[0], 6.0)
close(roots67[1], 3.0)

# 24.68, Table 24.2 materials. E is half dielectric strength; d and C0 are fixed.
C0_68, d68 = 6.00e-12, 2.50e-3
materials68 = [
    ("Polycarbonate", 2.8, 3.0e7),
    ("Polyester", 3.3, 6.0e7),
    ("Polypropylene", 2.2, 7.0e7),
    ("Polystyrene", 2.6, 2.0e7),
    ("Pyrex glass", 4.7, 1.0e7),
]
rows68 = []
for name, K, Em in materials68:
    E = Em / 2.0
    U = 0.5 * K * C0_68 * E**2 * d68**2
    Q = K * C0_68 * E * d68
    V = E * d68
    rows68.append((name, U, Q, V))
assert max(rows68, key=lambda row: row[1])[0] == "Polyester"
assert max(rows68, key=lambda row: row[2])[0] == "Polyester"
assert max(rows68, key=lambda row: row[3])[0] == "Polypropylene"
close(rows68[0][1], 0.0118125)
close(rows68[1][1], 0.0556875)
close(rows68[2][1], 0.05053125)
close(rows68[3][1], 0.004875)
close(rows68[4][1], 0.002203125)

print("24.56 Vcd_open=70.0 V, Q_switch=315 uC, Q_closed=[315,630,630,315] uC")
print("24.57 Q=75.6 uC, U_initial=1.3608 mJ, V_parallel=10.8 V, U_final=1.22472 mJ")
print(f"24.58 C={C58:.5g} F, V_cloud-ground={V58:.5g} V, E={E58:.5g} V/m, U={U58:.5g} J")
print(f"24.59 Ceq={Ceq59_uF:.5g} uF, Q_near={Q59_near_terminal_uC:.5g} uC, Q_rung={Q59_rung_uC:.5g} uC, Vcd={Vcd59:.5g} V")
print(f"24.61 C3={C3_61_uF:.5g} uF")
print(f"24.62 u(r=.02 m)={u62_at_r:.5g} J/m^3, U/L={UperL62_integral:.5g} J/m")
print(f"24.63 s={s63:.5g} m/C^2, V(Q)={V63:.5g} V, V(2Q)={V2_63:.5g} V")
print(f"24.64 C={C_64:.5g} F, U_with={U_64:.5g} J, U_air={U_air64:.5g} J")
print(f"24.65 F(d)={F65:.5g} N, W_cable={Wcable65:.5g} J, DeltaU={Uf65-Ui65:.5g} J")
print("24.66 Keff gasoline:", [round(v, 4) for v in Keff_gas], "methanol:", [round(v, 4) for v in Keff_methanol])
print(f"24.67 C1={roots67[0]:.5g} uF, C2={roots67[1]:.5g} uF")
print("24.68 rows (U J, Q C, V V):")
for row in rows68:
    print("  ", row)