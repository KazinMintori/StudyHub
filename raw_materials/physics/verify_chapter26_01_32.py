"""Independent arithmetic and MNA checks for Chapter 26 Exercises 26.1–26.32.

Run with: python raw_materials/physics/verify_chapter26_01_32.py
Requires NumPy.
"""

from __future__ import annotations

from math import isclose, sqrt
import numpy as np


def mna(resistors, voltage_sources, ground="g"):
    """Solve a DC network by modified nodal analysis.

    Resistors are (name, node_a, node_b, ohms). Voltage sources are
    (name, positive_node, negative_node, volts), with V+ - V- = emf.
    A source's returned current is positive from its positive to negative node.
    """
    nodes = sorted(
        {n for _, a, b, _ in resistors for n in (a, b) if n != ground}
        | {n for _, p, q, _ in voltage_sources for n in (p, q) if n != ground}
    )
    ix = {node: i for i, node in enumerate(nodes)}
    n, m = len(nodes), len(voltage_sources)
    matrix = np.zeros((n + m, n + m), dtype=float)
    rhs = np.zeros(n + m, dtype=float)

    def add(node, row, value):
        if node != ground:
            matrix[row, ix[node]] += value

    for _, a, b, resistance in resistors:
        conductance = 1.0 / resistance
        for node, other in ((a, b), (b, a)):
            if node != ground:
                row = ix[node]
                matrix[row, row] += conductance
                if other != ground:
                    matrix[row, ix[other]] -= conductance

    for k, (_, positive, negative, emf) in enumerate(voltage_sources):
        row = n + k
        add(positive, row, 1.0)
        add(negative, row, -1.0)
        if positive != ground:
            matrix[ix[positive], row] += 1.0
        if negative != ground:
            matrix[ix[negative], row] -= 1.0
        rhs[row] = emf

    solution = np.linalg.solve(matrix, rhs)
    volts = {ground: 0.0}
    volts.update({node: solution[ix[node]] for node in nodes})
    source_currents = {
        name: solution[n + k] for k, (name, _, _, _) in enumerate(voltage_sources)
    }
    resistor_currents = {
        name: (volts[a] - volts[b]) / resistance
        for name, a, b, resistance in resistors
    }
    resistor_powers = {
        name: current * current * resistance
        for (name, _, _, resistance), current in zip(resistors, resistor_currents.values())
    }
    delivered = -sum(
        emf * source_currents[name]
        for name, _, _, emf in voltage_sources
    )
    dissipated = sum(resistor_powers.values())
    if not isclose(delivered, dissipated, rel_tol=1e-9, abs_tol=1e-9):
        raise AssertionError(f"Power imbalance: supplied={delivered}, dissipated={dissipated}")
    return volts, source_currents, resistor_currents, resistor_powers


def close(actual, expected, tol=1e-8):
    if not isclose(float(actual), float(expected), rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{actual:.12g} != {expected:.12g}")


results = {}

# 26.1: Two straight pieces R/3 and a circular piece R/3 connected at opposite ends.
results[1] = {"R_ab_over_R": 2 / 3 + 1 / 12}
close(results[1]["R_ab_over_R"], 3 / 4)

# 26.2: X, 15 ohm, 5 ohm, and 10 ohm are parallel between a and b.
known_conductance = 1 / 15 + 1 / 5 + 1 / 10
x26_2 = 1 / (1 / 2.00 - known_conductance)
results[2] = {"X_ohm": x26_2}
close(x26_2, 7.5)

# 26.3–26.5: Series, parallel, and a triangular three-resistor network.
i26_3 = sqrt(36.0 / 25.0)
emf26_3 = i26_3 * 25.0
current_after_15_ohm_added = emf26_3 / (25.0 + 15.0)
results[3] = {
    "initial_current_A": i26_3,
    "battery_emf_V": emf26_3,
    "current_after_15_ohm_added_A": current_after_15_ohm_added,
    "total_power_W": current_after_15_ohm_added**2 * (25 + 15),
}
close(i26_3, 1.2)
close(emf26_3, 30.0)
close(current_after_15_ohm_added, 0.75)
close(results[3]["total_power_W"], 22.5)

req26_4 = 1 / (1 / 42.0 + 1 / 20.0)
results[4] = {
    "Req_ohm": req26_4,
    "Itotal_A": 240 / req26_4,
    "I42_A": 240 / 42,
    "I20_A": 240 / 20,
}
close(req26_4, 420 / 31)
close(results[4]["Itotal_A"], 17.714285714285715)
close(results[4]["I42_A"] + results[4]["I20_A"], results[4]["Itotal_A"])

tri = {"ab": 1 / (1 / 15 + 1 / 30), "bc": 1 / (1 / 10 + 1 / 35), "ac": 1 / (1 / 20 + 1 / 25)}
results[5] = {
    "Iab_A": 35 / tri["ab"],
    "Ibc_A": 35 / tri["bc"],
    "Iac_A": 35 / tri["ac"],
    "Ibc_with_r3_A": 35 / (tri["bc"] + 3),
}
close(tri["ab"], 10)
close(tri["bc"], 70 / 9)
close(tri["ac"], 100 / 9)

# 26.6: MNA of the inner parallel network. The 25 ohm branch current is given.
v6, s6, i6, p6 = mna(
    [("R25", "A", "B", 25.0), ("R15", "A", "B", 15.0),
     ("R15bottom", "A", "M", 15.0), ("R10", "M", "B", 10.0)],
    [("V_inner", "B", "A", 31.25)], ground="A",
)
inner_current = -s6["V_inner"]
meter45 = inner_current * 45.0
emf6 = 31.25 + inner_current * (45.0 + 35.0)
results[6] = {
    "I25_A": i6["R25"], "I15middle_A": i6["R15"],
    "I15bottom_A": i6["R15bottom"], "I10_A": i6["R10"],
    "V45_V": meter45, "emf_V": emf6,
}
close(abs(i6["R25"]), 1.25)
close(abs(i6["R15"]), 31.25 / 15)
close(abs(i6["R10"]), 1.25)
close(-(i6["R25"] + i6["R15"] + i6["R15bottom"]), inner_current)
close(meter45, 206.25)
close(emf6, 397.9166666666667)
close(emf6 * inner_current, inner_current**2 * (45 + 35) + sum(p6.values()))

# 26.7: 25 V source with r and 18 ohm in series across the 45/15 ohm load.
v7, s7, i7, p7 = mna(
    [("Rbranch", "source", "right", 3.26 + 18.0),
     ("R45", "right", "g", 45.0), ("R15", "right", "g", 15.0)],
    [("E25", "source", "g", 25.0)],
)
results[7] = {"ammeter_A": abs(i7["Rbranch"]), "terminal_V": v7["right"]}
close(results[7]["ammeter_A"], 25 / (3.26 + 18 + 1 / (1 / 45 + 1 / 15)))

# 26.8–26.10: Parallel slope, identical resistors, and resistor power ratings.
r1_26_8 = 1 / (0.208 - 1 / 8.00)
results[8] = {"R1_ohm": r1_26_8}
close(r1_26_8, 12.048192771084338)
results[9] = {"Iparallel_A": 6.0, "Iseries_A": 1 / 6, "P_ratio_parallel_series": 36.0}
close(6 * (1 / 6), 1.0)
vmax10a = sqrt(5.0 * 15_000)
p10b = 120**2 / 9_000
imax10c = sqrt(2.0 / 150.0)
vmax10c = imax10c * (100.0 + 150.0)
results[10] = {
    "Vmax_15k_ohm_V": vmax10a, "Pmin_9k_ohm_W": p10b,
    "Vmax_series_V": vmax10c, "P100_ohm_W": imax10c**2 * 100,
    "P150_ohm_W": imax10c**2 * 150,
}
close(vmax10a, 273.8612787525831)
close(vmax10c, 28.867513459481287)

# 26.11–26.12: MNA for parallel R1/R2 in series with R3.
v11, s11, i11, p11 = mna(
    [("R1", "src", "p", 3.0), ("R2", "src", "p", 6.0), ("R3", "p", "g", 5.0)],
    [("E", "src", "g", 84.0)],
)
results[11] = {"I1_A": i11["R1"], "I2_A": i11["R2"], "I3_A": i11["R3"], "E_V": 84.0}
close(i11["R2"], 4.0)
close(i11["R1"], 8.0)
close(i11["R3"], 12.0)

v12, s12, i12, p12 = mna(
    [("R1", "src", "p", 5.0), ("R2", "src", "p", 2.5), ("R3", "p", "g", 55 / 9)],
    [("E", "src", "g", 35.0)],
)
results[12] = {"R2_ohm": 2.5, "R3_ohm": 55 / 9, "I1_A": i12["R1"], "I2_A": i12["R2"], "I3_A": i12["R3"]}
close(i12["R1"], 1.5)
close(i12["R2"], 3.0)
close(i12["R3"], 4.5)

# 26.13–26.14: Each pair on the left/right is parallel, and the pair groups are in series.
v13, s13, i13, p13 = mna(
    [("R3", "L", "C", 3), ("R6", "L", "C", 6), ("R12", "C", "R", 12), ("R4", "C", "R", 4)],
    [("E", "L", "R", 60)], ground="R",
)
results[13] = {"Req_ohm": 5, "I3_A": i13["R3"], "I6_A": i13["R6"], "I12_A": i13["R12"], "I4_A": i13["R4"]}
close(i13["R3"] + i13["R6"], 12)
close(i13["R12"] + i13["R4"], 12)

v14, s14, i14, p14 = mna(
    [("R1", "L", "C", 1), ("R7", "L", "C", 7), ("R3", "C", "R", 3), ("R5", "C", "R", 5)],
    [("E", "L", "R", 48)], ground="R",
)
results[14] = {"Req_ohm": 2.75, "I1_A": i14["R1"], "I7_A": i14["R7"], "I3_A": i14["R3"], "I5_A": i14["R5"]}
close(i14["R1"] + i14["R7"], 48 / 2.75)
close(i14["R3"] + i14["R5"], 48 / 2.75)

# 26.15: R1 is in series with three equal parallel bulbs, then R4 is removed.
v15, s15, i15, p15 = mna(
    [("R1", "src", "j", 4.5), ("R2", "j", "g", 4.5), ("R3", "j", "g", 4.5), ("R4", "j", "g", 4.5)],
    [("E", "src", "g", 9.0)],
)
v15b, s15b, i15b, p15b = mna(
    [("R1", "src", "j", 4.5), ("R2", "j", "g", 4.5), ("R3", "j", "g", 4.5)],
    [("E", "src", "g", 9.0)],
)
results[15] = {
    "initial_currents_A": {k: i15[k] for k in ("R1", "R2", "R3", "R4")},
    "initial_powers_W": p15,
    "after_R4_removed_currents_A": {k: i15b[k] for k in ("R1", "R2", "R3")},
    "after_R4_removed_powers_W": p15b,
}

# 26.16–26.18: MNA for the multi-branch resistor circuit and switch states.
v16, s16, i16, p16 = mna(
    [("R6", "top", "j", 6), ("R8", "top", "j", 8), ("R25", "j", "g", 25), ("R20", "top", "g", 20)],
    [("E", "top", "g", 199)],
)
results[16] = {"I25_A": i16["R25"], "I20_A": i16["R20"], "E_V": 199}
close(i16["R6"], 4.0)
close(i16["R25"], 7.0)
close(i16["R20"], 9.95)

v17, s17, i17, p17 = mna(
    [("R1", "p", "n", 1), ("R2", "n", "g", 2), ("R6", "p", "g", 6)],
    [("E", "p", "g", 18)],
)
results[17] = {"E_V": 18, "I6_A": i17["R6"]}
close(i17["R2"], 6.0)
close(i17["R6"], 3.0)

v18_open, s18o, i18o, p18o = mna(
    [("R2", "a", "b", 6), ("R3", "b", "g", 3)], [("E", "a", "g", 36)]
)
v18_closed, s18c, i18c, p18c = mna(
    [("R1", "a", "b", 4), ("R2", "a", "b", 6), ("R3", "b", "g", 3)],
    [("E", "a", "g", 36)],
)
results[18] = {
    "Vab_open_V": v18_open["a"] - v18_open["b"],
    "Vab_closed_V": v18_closed["a"] - v18_closed["b"],
    "open_currents_A": i18o,
    "closed_currents_A": i18c,
}
close(results[18]["Vab_open_V"], 24.0)
close(results[18]["Vab_closed_V"], 16.0)

# 26.19: 20 ohm heater in water, three parallel rows, and a 5 ohm lead resistor.
v19, s19, i19, p19 = mna(
    [("water", "src", "L", 20), ("top10a", "L", "T", 10), ("top10b", "T", "R", 10),
     ("mid10a", "L", "M", 10), ("mid10b", "M", "R", 10),
     ("low5a", "L", "N", 5), ("low5b", "N", "R", 5), ("lead5", "R", "g", 5)],
    [("E", "src", "g", 30)],
)
power_water = i19["water"] ** 2 * 20
heat_capacity_water = 0.100 * 4186.0
heat_needed = heat_capacity_water * (58.0 - 10.0)
time_heat = heat_needed / power_water
results[19] = {"I_A": i19["water"], "Pwater_W": power_water, "time_s": time_heat, "time_min": time_heat / 60}
close(i19["water"], 1.0)
close(power_water, 20.0)

# 26.20: Parallel branches; the 2 A bottom segment is the R1 branch current.
v20, s20, i20, p20 = mna(
    [("R10", "top", "g", 10), ("R2", "top", "g", 10), ("R1", "top", "g", 3.75)],
    [("E", "top", "g", 7.5)],
)
results[20] = {"R1_ohm": 3.75, "R2_ohm": 10.0, "E_V": 7.5, "I10_A": i20["R10"], "IR2_A": i20["R2"], "IR1_A": i20["R1"], "Ptotal_W": sum(p20.values())}
close(i20["R1"], 2.0)
close(sum(i20.values()), 3.5)
close(sum(p20.values()), 7.5 * 3.5)

# 26.21: Independent series and parallel bulb states.
series_current21 = 120 / (400 + 800)
parallel_currents21 = (120 / 400, 120 / 800)
results[21] = {
    "series_currents_A": (series_current21, series_current21),
    "series_powers_W": (series_current21**2 * 400, series_current21**2 * 800),
    "parallel_currents_A": parallel_currents21,
    "parallel_powers_W": (120**2 / 400, 120**2 / 800),
}

# 26.22: Three parallel branches with a 10 V ideal source setting the rails.
v22, s22, i22, p22 = mna(
    [("R30", "top", "g", 30), ("R20", "top", "mid5", 20)],
    [("E10", "top", "g", 10), ("E5", "mid5", "g", 5)],
)
results[22] = {
    "I30_A": i22["R30"], "I20_A": i22["R20"],
    "I10V_battery_A": -s22["E10"], "Vmid5_V": v22["mid5"],
}
close(i22["R30"], 1 / 3)
close(i22["R20"], 0.25)
close(-s22["E10"], 7 / 12)

# 26.23: Measured branch currents determine R, E, and the open-x current.
# V_R - V_L = -18 V from the 6 A current through the 3 ohm lower branch.
v23, s23, i23, p23 = mna(
    [("R6", "x", "R", 6), ("R3", "L", "R", 3), ("R5", "t", "R", 5)],
    [("E28", "L", "t", 28), ("E42", "L", "x", 42)],
    ground="R",
)
v23_open, s23open, i23open, p23open = mna(
    [("R5", "t", "R", 5), ("R3", "L", "R", 3)], [("E28", "L", "t", 28)], ground="R"
)
results[23] = {"IR_A": i23["R5"], "R_ohm": 5.0, "E_V": 42.0, "E_polarity_reversed": False, "IR_open_x_A": i23open["R5"]}
close(i23["R6"], -4.0)
close(i23["R3"], 6.0)
close(i23["R5"], -2.0)
close(i23open["R5"], -3.5)

# 26.24: Three parallel branches, with arrows fixing branch currents and node voltage.
# MNA checks the derived branch emfs against the observed 1 A / 1 A / 2 A currents.
v24, s24, i24, p24 = mna(
    [("top1", "a", "tp", 1), ("top6", "tn", "b", 6),
     ("mid4", "a", "mp1", 4), ("mid1", "mp1", "mp2", 1),
     ("bot1", "a", "bp", 1), ("bot2", "bn", "b", 2)],
    [("E20", "tp", "tn", 20), ("E1", "mp2", "b", 18), ("E2", "bp", "bn", 7)],
    ground="b",
)
results[24] = {"E1_V": 18.0, "E2_V": 7.0, "Vb_minus_Va_V": -13.0, "branch_currents_A": {"top": i24["top1"], "mid": i24["mid4"], "bottom": i24["bot1"]}}
close(i24["top1"], -1.0)
close(i24["mid4"], -1.0)
close(i24["bot1"], 2.0)
close(v24["a"], 13.0)

# 26.25: Bridge with two batteries and three known branch currents.
v25, s25, i25, p25 = mna(
    [("R4", "L", "g", 4), ("R3", "M", "g", 3), ("R6", "R", "g", 6), ("R9", "L", "R", 9)],
    [("E1", "L", "M", 36), ("E2", "R", "M", 54)],
)
results[25] = {"I3_A": i25["R3"], "E1_V": 36, "E2_V": 54, "R_ohm": 9}
close(i25["R4"], 3)
close(i25["R6"], 5)
close(i25["R3"], -8)
close(i25["R9"], -2)

# 26.26–26.28: Three branches between the left and right rails.
def solve_26_26(top_emf=10.0, middle_emf=5.0):
    return mna(
        [("top2", "L", "t", 2), ("top3", "a", "R", 3),
         ("mid1", "L", "m", 1), ("mid4", "b", "R", 4), ("bottom10", "L", "R", 10)],
        [("Etop", "t", "a", top_emf), ("Emid", "m", "b", middle_emf)],
    )

v26, s26, i26, p26 = solve_26_26()
v27, s27, i27, p27 = solve_26_26(top_emf=-10.0, middle_emf=5.0)
v28, s28, i28, p28 = solve_26_26(top_emf=10.0, middle_emf=15.0)
results[26] = {"branch_currents_A": i26, "Vab_V": v26["a"] - v26["b"]}
results[27] = {"branch_currents_A": i27, "Vab_V": v27["a"] - v27["b"]}
results[28] = {"branch_currents_A": i28, "Vab_V": v28["a"] - v28["b"]}
close(v26["L"] - v26["R"], 6.0)
close(i26["top2"] + i26["mid1"] + i26["bottom10"], 0.0)
close(i26["bottom10"], 0.6)
close(results[26]["Vab_V"], -3.2)
close(v27["L"] - v27["R"], -2.0)
close(i27["top2"] + i27["mid1"] + i27["bottom10"], 0.0)
close(results[27]["Vab_V"], 10.4)
close(v28["L"] - v28["R"], 10.0)
close(i28["top2"] + i28["mid1"] + i28["bottom10"], 0.0)
close(results[28]["Vab_V"], 4.0)

# 26.29: The open-switch voltmeter reading fixes the unknown series-battery emf.
# Open state: V_C=15 V, hence V_L=24 V; KCL gives I_(20+E)=-0.62 A and E=36.4 V.
emf29 = 36.4
v29_open, s29o, i29o, p29o = mna(
    [("R75", "L", "g", 75), ("R20", "L", "mid", 20), ("R30", "L", "C", 30), ("R50", "C", "g", 50)],
    [("Eunknown", "mid", "g", emf29)],
)
v29_closed, s29c, i29c, p29c = mna(
    [("R75", "L", "g", 75), ("R20", "L", "mid", 20), ("R30", "L", "C", 30), ("R50", "C", "g", 50)],
    [("Eunknown", "mid", "g", emf29), ("E25", "C", "g", 25)],
)
results[29] = {"E_V": emf29, "Vmeter_open_V": v29_open["C"], "A_closed_A": abs(i29c["R50"]), "Vmeter_closed_V": v29_closed["C"]}
close(v29_open["C"], 15.0)
close(v29_closed["C"], 25.0)
close(abs(i29c["R50"]), 0.5)

# 26.30: The ammeter gives total loop current; MNA checks the solved battery emf.
emf30 = 52.3125
v30, s30, i30, p30 = mna(
    [("R12", "src", "top", 12), ("R48", "top", "g", 48), ("R15", "mid", "g", 15)],
    [("E75", "src", "g", 75), ("Eunknown", "top", "mid", emf30)],
)
results[30] = {"E_V": emf30, "E_polarity_as_drawn": True, "Iammeter_A": -s30["E75"]}
close(-s30["E75"], 1.5)

# 26.31: 25 V source, 100 ohm lead, 15 V battery with positive terminal at b, and 75 ohm load.
v31_open, s31o, i31o, p31o = mna(
    [("R100", "src", "a", 100), ("R75", "p15", "b", 75)],
    [("E25", "src", "b", 25), ("E15", "p15", "a", 15)], ground="b",
)
v31_closed, s31c, i31c, p31c = mna(
    [("R100", "src", "a", 100), ("R75", "p15", "b", 75)],
    [("E25", "src", "b", 25), ("E15", "p15", "a", 15), ("switch", "a", "b", 0)], ground="b",
)
results[31] = {
    "Vab_open_V": v31_open["a"] - v31_open["b"],
    "Vab_closed_V": v31_closed["a"] - v31_closed["b"],
    "switch_current_A": s31c["switch"],
}
close(results[31]["Vab_open_V"], 15 / 7)
close(results[31]["Vab_closed_V"], 0.0)
close(s31c["switch"], 0.05)

# 26.32: Current arrows fix the central 2 A branch. The 25 V cell is positive at the top.
emf32 = -46.0  # Opposite the polarity marked for the unknown source.
v32, s32, i32, p32 = mna(
    [("R17", "lefttop", "A", 17), ("R13", "leftbottom", "B", 13),
     ("R6", "A", "x", 6), ("R3", "y", "B", 3),
     ("R20top", "A", "r", 20), ("R20bottom", "A", "r", 20),
     ("R19", "r", "rightbottom", 19), ("R1", "rightbottom", "B", 1)],
    [("Eunknown", "lefttop", "leftbottom", emf32), ("E25", "x", "y", 25)],
    ground="B",
)
results[32] = {
    "I6_A": i32["R6"], "I3_A": i32["R3"],
    "Ammeter_A": abs(i32["R19"]), "E_magnitude_V": abs(emf32),
    "E_positive_at_bottom": True,
}
close(i32["R6"], -2.0)
close(i32["R3"], -2.0)
close(abs(i32["R19"]), 7 / 30)
close(s32["Eunknown"], 53 / 30)

print("MNA and arithmetic checks passed for Exercises 26.1–26.32.")
for number, result in results.items():
    print(f"26.{number}: {result}")
