"""Independent numerical checks for exercises 24.40–24.55."""
from math import isclose, pi, sqrt
import numpy as np

EPS0 = 8.8541878128e-12
KCOULOMB = 1 / (4 * pi * EPS0)
G = 9.80


def near(name, actual, expected, rel=2e-9, abs_tol=1e-24):
    if not isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol):
        raise AssertionError(f"{name}: {actual} != {expected}")


def solve_floating_nodes(unknowns, fixed, capacitors):
    """Solve zero-net-charge node equations; C values may use any common unit."""
    index = {name: i for i, name in enumerate(unknowns)}
    matrix = np.zeros((len(unknowns), len(unknowns)), dtype=float)
    rhs = np.zeros(len(unknowns), dtype=float)
    for first, second, capacitance in capacitors:
        for node, other in ((first, second), (second, first)):
            if node not in index:
                continue
            row = index[node]
            matrix[row, row] += capacitance
            if other in index:
                matrix[row, index[other]] -= capacitance
            else:
                rhs[row] += capacitance * fixed[other]
    return np.linalg.solve(matrix, rhs)


# 24.40: Dielectric energy density, then solve U = eps*A*E*V/2.
K, dielectric_strength = 2.6, 2.0e7
E40, V40, U40 = 0.80 * dielectric_strength, 500.0, 0.200e-3
u40 = 0.5 * K * EPS0 * E40**2
A40 = 2 * U40 / (K * EPS0 * E40 * V40)
near("24.40 energy density", u40, 2.9466737041e3)
near("24.40 plate area", A40, 2.17194051418e-3)

# 24.41: Source stays connected, so V stays fixed and U scales with C.
C41, U041, deltaU41 = 360e-9, 1.85e-5, 2.32e-5
V41 = sqrt(2 * U041 / C41)
K41 = (U041 + deltaU41) / U041
near("24.41 voltage", V41, 10.1379375505)
near("24.41 dielectric constant", K41, 2.25405405405)

# 24.42: Source stays connected, so V and plate field stay fixed.
C042, radius42, Q042, Q142 = 12.5e-12, 0.0300, 25e-12, 45e-12
A42 = pi * radius42**2
d42 = EPS0 * A42 / C042
V42 = Q042 / C042
K42 = Q142 / Q042
E42 = V42 / d42
near("24.42 dielectric constant", K42, 1.8)
near("24.42 voltage before and after", V42, 2.0)
near("24.42 plate field before and after", E42, 9.98616865807e2)

# 24.43: Gauss pillbox gives E=Q/(K eps0 A), then V=Ed and C=Q/V.
Q43, K43, A43, d43 = 7.3e-6, 3.4, 0.018, 0.0012
E43 = Q43 / (K43 * EPS0 * A43)
V43 = E43 * d43
C43 = Q43 / V43
near("24.43 capacitance from Gauss", C43, K43 * EPS0 * A43 / d43)

# 24.44: Initially V fixed. After disconnecting and removing Teflon, Q is fixed.
A44, d44, K44, V44 = 0.0225, 1e-3, 2.1, 12.0
C44 = K44 * EPS0 * A44 / d44
Q44 = C44 * V44
E144 = V44 / d44
E244 = Q44 / (EPS0 * A44)
near("24.44 plate charge", Q44, 5.02032448986e-9)
near("24.44 field with Teflon", E144, 1.2e4)
near("24.44 field after removal", E244, 2.52e4)

# 24.45: Stored electrical energy supplies the light at 95% efficiency.
P45, t45, efficiency45, V45 = 2.70e5, 1 / 675, 0.95, 125.0
U45 = P45 * t45 / efficiency45
C45 = 2 * U45 / V45**2
near("24.45 stored energy", U45, 421.052631579)
near("24.45 capacitance", C45, 0.0538947368421)

# 24.46: Disconnecting the battery fixes Q while plate spacing doubles.
A46, d146, V146 = 0.12**2, 3.7e-3, 12.0
C146 = EPS0 * A46 / d146
Q46 = C146 * V146
E146 = V146 / d146
U146 = 0.5 * C146 * V146**2
d246 = 2 * d146
C246 = EPS0 * A46 / d246
V246 = Q46 / C246
E246 = V246 / d246
U246 = Q46**2 / (2 * C246)
near("24.46 initial capacitance", C146, 34.4595417579e-12)
near("24.46 initial charge", Q46, 4.13514501095e-10)
near("24.46 initial field", E146, 3243.24324324)
near("24.46 initial energy", U146, 2.48108700657e-9)
near("24.46 final field", E246, E146)
near("24.46 final voltage", V246, 24.0)
near("24.46 final energy", U246, 4.96217401314e-9)

# 24.47: A detectable increase of 0.250 pF determines the required gap change.
A47, d047, deltaC47 = 42e-6, 0.700e-3, 0.250e-12
C047 = EPS0 * A47 / d047
d147 = EPS0 * A47 / (C047 + deltaC47)
press47 = d047 - d147
near("24.47 initial capacitance", C047, 0.531251268768e-12)
near("24.47 key travel", press47, 0.223999636219e-3)

# 24.48: Capacitance per cm² and field from the stated resting voltage.
K48, thickness48, voltage48 = 10.0, 7.5e-9, 85e-3
C48_per_cm2 = K48 * EPS0 / thickness48 * 1e-4
E48 = voltage48 / thickness48
near("24.48 capacitance per cm2", C48_per_cm2, 1.18055837504e-6)
near("24.48 membrane field", E48, 1.13333333333e7)

# 24.49: Isolated two-capacitor system conserves charge, not stored energy.
C149, V149, C249 = 20e-6, 800.0, 10e-6
Q149 = C149 * V149
Vf49 = Q149 / (C149 + C249)
Ui49 = 0.5 * C149 * V149**2
Uf49 = 0.5 * (C149 + C249) * Vf49**2
near("24.49 original charge", Q149, 0.016)
near("24.49 final voltage", Vf49, 533.333333333)
near("24.49 final energy", Uf49, 4.26666666667)
near("24.49 energy decrease", Ui49 - Uf49, 2.13333333333)

# 24.50: A conducting sphere relative to infinity has C=4 pi eps0 R.
# R=2.0 m is an explicit order-of-magnitude model for a car-sized object.
R50, V50 = 2.0, 100e6
C50 = 4 * pi * EPS0 * R50
Q50 = C50 * V50
near("24.50 capacitance at R=2 m", C50, 2.22530011090e-10)
near("24.50 charge at R=2 m", Q50, 2.22530011090e-2)

# 24.51: C8.60 and C4.80 are in series with the bridge.
# The bridge is C3.50 in parallel with (C6.20 in series with C11.8).
C851, C4851, C6251, C11851, C3551 = 8.60, 4.80, 6.20, 11.8, 3.50
Ctop51 = C6251 * C11851 / (C6251 + C11851)
Cbridge51 = Ctop51 + C3551
Ceq51 = 1 / (1 / C851 + 1 / C4851 + 1 / Cbridge51)
Qseries51 = Ceq51 * 1e-6 * 12.0
Uall51 = 0.5 * Ceq51 * 1e-6 * 12.0**2
U4851 = Qseries51**2 / (2 * C4851 * 1e-6)
near("24.51 bridge equivalent", Cbridge51, 7.56444444444)
near("24.51 equivalent capacitance", Ceq51, 2.18909480664)
near("24.51 series charge", Qseries51, 26.2691376796e-6)
near("24.51 total energy", Uall51, 157.614826078e-6)
near("24.51 energy in 4.80 uF", U4851, 71.8820410866e-6)
nodes51 = solve_floating_nodes(
    ["n1", "n2", "mid"], {"a": 12.0, "b": 0.0},
    [("a", "n1", C851), ("n1", "n2", C4851),
     ("n2", "mid", C6251), ("mid", "b", C11851),
     ("n2", "b", C3551)],
)
near("24.51 nodal 4.80 uF energy", 0.5 * C4851 * 1e-6 * (nodes51[0] - nodes51[1])**2, U4851)

# 24.52: C1 and C2 are series, in parallel with C3, then series C4.
C152, C252, C352, C452, Vad52 = 6.0, 3.0, 4.0, 8.0, 40.0
Qseries52 = (C152 * C252 / (C152 + C252)) * Vad52
Q352 = C352 * Vad52
Q452 = Qseries52 + Q352
V452 = Q452 / C452
Vab52 = Vad52 + V452
V152, V252 = Qseries52 / C152, Qseries52 / C252
near("24.52 C1 voltage", V152, 13.3333333333)
near("24.52 C2 voltage", V252, 26.6666666667)
near("24.52 series charge", Qseries52, 80.0)
near("24.52 C3 charge", Q352, 160.0)
near("24.52 C4 voltage", V452, 30.0)
near("24.52 floating-node charge balance", Q452, 240.0)
near("24.52 applied voltage", Vab52, 70.0)
matrix52 = np.array([
    [1.0, -1.0, 0.0],
    [-C152, -C252, C152 + C252],
    [-C352, C252 + C352 + C452, -C252],
])
rhs52 = np.array([Vad52, 0.0, 0.0])
Va52, Vd52, Vm52 = np.linalg.solve(matrix52, rhs52)
near("24.52 numpy C1 voltage", Va52 - Vm52, V152)
near("24.52 numpy C2 voltage", Vm52 - Vd52, V252)
near("24.52 numpy C4 voltage", Vd52, V452)

# 24.53: C1, a middle network, and C5 are in series.
C153, C253, C353, C453, C553, Vab53 = 8.4, 4.2, 4.2, 4.2, 8.4, 220.0
Cseries34 = C353 * C453 / (C353 + C453)
Cxy53 = C253 + Cseries34
Ceq53 = 1 / (1 / C153 + 1 / Cxy53 + 1 / C553)
Qline53 = Ceq53 * Vab53
V153, Vxy53, V553 = Qline53 / C153, Qline53 / Cxy53, Qline53 / C553
Q253 = C253 * Vxy53
Qseries34 = Cseries34 * Vxy53
V353, V453 = Qseries34 / C353, Qseries34 / C453
near("24.53 equivalent capacitance", Ceq53, 2.52)
near("24.53 line charge", Qline53, 554.4)
near("24.53 voltage on C1 and C5", V153, 66.0)
near("24.53 voltage on C2", Vxy53, 88.0)
near("24.53 charge on C2", Q253, 369.6)
near("24.53 charge on C3 and C4", Qseries34, 184.8)
near("24.53 voltage on C3 and C4", V353, 44.0)
near("24.53 total voltage", V153 + Vxy53 + V553, Vab53)
nodes53 = solve_floating_nodes(
    ["X", "Y", "R"], {"a": Vab53, "b": 0.0},
    [("a", "X", C153), ("b", "Y", C553), ("X", "Y", C253),
     ("X", "R", C353), ("R", "Y", C453)],
)
near("24.53 numpy C2 voltage", nodes53[0] - nodes53[1], Vxy53)
near("24.53 numpy C3 voltage", nodes53[0] - nodes53[2], V353)
near("24.53 numpy C4 voltage", nodes53[2] - nodes53[1], V453)

# 24.54: Explicit estimates L=10 cm, N=100 standing hairs, head radius 10 cm.
# The source's force model gives 2mg = k Q²/(N L²).
L54, N54, radius54 = 0.10, 100.0, 0.10
linear_mass54 = 65e-9 / 0.01  # 65 micrograms per centimetre, in kg/m
m54 = linear_mass54 * L54
Qhead54 = sqrt(2 * m54 * G * N54 * L54**2 / KCOULOMB)
Chead54 = 4 * pi * EPS0 * radius54
Vhead54 = Qhead54 / Chead54
near("24.54 hair linear mass", linear_mass54, 6.5e-6)
near("24.54 one hair mass", m54, 6.5e-7)
near("24.54 head charge estimate", Qhead54, 3.76499159447e-8)
near("24.54 head capacitance estimate", Chead54, 1.11265005545e-11)
near("24.54 head potential estimate", Vhead54, 3383.80569527)

# 24.55: C1 and C2 are parallel between a-d, in series with C3 from d-b.
C155, Q155, Vab55, Q355 = 3.00, 150e-6, 150.0, 450e-6
V155 = Q155 / (C155 * 1e-6)
Vdb55 = Vab55 - V155
C355 = Q355 / Vdb55
Q255 = Q355 - Q155
C255 = Q255 / V155
near("24.55 voltage across C1", V155, 50.0)
near("24.55 charge on C2", Q255, 300e-6)
near("24.55 capacitance C2", C255, 6.0e-6)
near("24.55 voltage across C3", Vdb55, 100.0)
near("24.55 capacitance C3", C355, 4.50e-6)
Vd55 = solve_floating_nodes(
    ["d"], {"a": Vab55, "b": 0.0},
    [("a", "d", 3.0), ("a", "d", C255 * 1e6), ("d", "b", C355 * 1e6)],
)[0]
near("24.55 numpy node d", Vd55, Vdb55)

print("All independent checks passed for Exercises 24.40-24.55.")
