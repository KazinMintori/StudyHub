"""Independent nodal, MNA, energy, and RC checks for Chapter 26 guided practice."""

from math import exp, isclose, log


def close(actual, expected, *, rel=1e-10, abs_tol=1e-12):
    assert isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol), (
        actual,
        expected,
    )


def solve_linear(matrix, rhs):
    """Gauss-Jordan solver for a small dense system."""
    a = [list(row) + [value] for row, value in zip(matrix, rhs)]
    n = len(a)
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(a[row][col]))
        assert abs(a[pivot][col]) > 1e-14
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        a[col] = [value / scale for value in a[col]]
        for row in range(n):
            if row == col:
                continue
            factor = a[row][col]
            a[row] = [
                a[row][j] - factor * a[col][j]
                for j in range(n + 1)
            ]
    return [a[row][-1] for row in range(n)]


def nodal(edges, *, fixed=None, injections=None):
    """Solve a resistor network; injections are positive into a node."""
    fixed = dict(fixed or {})
    injections = dict(injections or {})
    nodes = set(fixed) | set(injections)
    for u, v, resistance in edges:
        assert resistance > 0
        nodes.update((u, v))
    unknown = sorted(nodes - set(fixed))
    index = {node: k for k, node in enumerate(unknown)}
    matrix = [[0.0] * len(unknown) for _ in unknown]
    rhs = [injections.get(node, 0.0) for node in unknown]
    for u, v, resistance in edges:
        g = 1.0 / resistance
        for node, other in ((u, v), (v, u)):
            if node not in index:
                continue
            i = index[node]
            matrix[i][i] += g
            if other in index:
                matrix[i][index[other]] -= g
            else:
                rhs[i] += g * fixed[other]
    result = dict(fixed)
    if unknown:
        result.update(zip(unknown, solve_linear(matrix, rhs)))
    return result


def edge_current(voltages, u, v, resistance):
    return (voltages[u] - voltages[v]) / resistance


def mna(resistors, voltage_sources, ground):
    """Modified nodal analysis; source current is positive from + to -."""
    nodes = {ground}
    for u, v, resistance in resistors:
        nodes.update((u, v))
    for positive, negative, emf in voltage_sources:
        nodes.update((positive, negative))
    unknown_nodes = sorted(nodes - {ground})
    node_index = {node: k for k, node in enumerate(unknown_nodes)}
    n, m = len(unknown_nodes), len(voltage_sources)
    matrix = [[0.0] * (n + m) for _ in range(n + m)]
    rhs = [0.0] * (n + m)

    for u, v, resistance in resistors:
        g = 1.0 / resistance
        for node, other in ((u, v), (v, u)):
            if node == ground:
                continue
            i = node_index[node]
            matrix[i][i] += g
            if other != ground:
                matrix[i][node_index[other]] -= g

    for j, (positive, negative, emf) in enumerate(voltage_sources):
        current_col = n + j
        if positive != ground:
            i = node_index[positive]
            matrix[i][current_col] += 1
            matrix[n + j][i] += 1
        if negative != ground:
            i = node_index[negative]
            matrix[i][current_col] -= 1
            matrix[n + j][i] -= 1
        rhs[n + j] = emf

    solution = solve_linear(matrix, rhs)
    voltages = {ground: 0.0}
    voltages.update(zip(unknown_nodes, solution[:n]))
    source_currents = solution[n:]
    return voltages, source_currents


# VP26.2.1: apply a 1 A test current and solve four actual Figure 26.1 graphs.
R1, R2, R3 = 1.0, 2.0, 4.0
graphs_2621 = {
    "a": [("a", "x", R1), ("x", "y", R2), ("y", "b", R3)],
    "b": [("a", "b", R1), ("a", "b", R2), ("a", "b", R3)],
    "c": [("a", "x", R1), ("x", "b", R2), ("x", "b", R3)],
    "d": [("a", "b", R1), ("a", "x", R2), ("x", "b", R3)],
}
req_2621 = {}
for name, graph in graphs_2621.items():
    v = nodal(graph, fixed={"b": 0.0}, injections={"a": 1.0})
    req_2621[name] = v["a"]
for actual, expected in zip(
    (req_2621["a"], req_2621["b"], req_2621["c"], req_2621["d"]),
    (7.0, 4 / 7, 7 / 3, 6 / 7),
):
    close(actual, expected)

# VP26.2.2: Figure 26.1d, 24 V fixed at a-b.
graph = [("a", "b", 4.0), ("a", "x", 5.0), ("x", "b", 6.0)]
v = nodal(graph, fixed={"a": 24.0, "b": 0.0})
i_r1 = edge_current(v, "a", "b", 4.0)
i_r2 = edge_current(v, "a", "x", 5.0)
i_r3 = edge_current(v, "x", "b", 6.0)
i_battery = i_r1 + i_r2
for actual, expected in zip((i_battery, i_r1, i_r2, i_r3), (90 / 11, 6, 24 / 11, 24 / 11)):
    close(actual, expected)
p_2622 = i_r1**2 * 4 + i_r2**2 * 5 + i_r3**2 * 6
close(p_2622, 24 * i_battery)
close(i_r1 + i_r2, i_battery)

# VP26.2.3: three parallel branches, independently solved by nodal voltage.
graph = [("a", "b", 7.0), ("a", "b", 8.0), ("a", "b", 9.0)]
v = nodal(graph, fixed={"a": 12.0, "b": 0.0})
branch_i_2623 = [edge_current(v, "a", "b", r) for r in (7.0, 8.0, 9.0)]
branch_p_2623 = [i * i * r for i, r in zip(branch_i_2623, (7.0, 8.0, 9.0))]
p_battery_2623 = 12.0 * sum(branch_i_2623)
for actual, expected in zip(branch_p_2623, (144 / 7, 18, 16)):
    close(actual, expected)
close(p_battery_2623, sum(branch_p_2623))

# VP26.2.4: Figure 26.1c, with the source voltage imposed at a-b.
graph = [("a", "x", 5.0), ("x", "b", 6.0), ("x", "b", 7.0)]
v = nodal(graph, fixed={"a": 9.0, "b": 0.0})
i_r1 = edge_current(v, "a", "x", 5.0)
i_r2 = edge_current(v, "x", "b", 6.0)
i_r3 = edge_current(v, "x", "b", 7.0)
p_2624 = (i_r1**2 * 5, i_r2**2 * 6, i_r3**2 * 7)
i_battery_2624 = i_r1
close(i_r2 + i_r3, i_r1)
close(9 * i_battery_2624, sum(p_2624))
for actual, expected in zip(p_2624, (5.978251375665997, 2.0800069875098264, 1.7828631321512798)):
    close(actual, expected)

# VP26.7.1: MNA on the drawn single-loop circuit after reversing the 4 V cell.
# The 12 V cell is positive on the left; the reversed 4 V cell is positive on the right.
v, source_i = mna(
    resistors=[
        ("x", "a", 3.0),
        ("x", "m12", 2.0),
        ("b", "y", 7.0),
        ("a", "m4", 4.0),
    ],
    voltage_sources=[("m12", "b", 12.0), ("y", "m4", 4.0)],
    ground="a",
)
i12_delivered = -source_i[0]
i4_delivered = -source_i[1]
i_loop = i12_delivered
v_ab = v["a"] - v["b"]
close(i12_delivered, 1.0)
close(i4_delivered, 1.0)
close(v_ab, 7.0)
close(12 * i12_delivered + 4 * i4_delivered, i_loop**2 * (3 + 2 + 7 + 4))

# VP26.7.2: node a receives both stated currents; R connects a to b.
i1, i2, r_load = 0.200, 1.35, 5.00
i_load = i1 + i2
v_ab = r_load * i_load
r1 = (8.00 - v_ab) / i1
r2 = (9.00 - v_ab) / i2
close(v_ab, 7.75)
close(r1, 1.25)
close(r2, 0.9259259259259259)
close(8.00 * i1 + 9.00 * i2, i_load**2 * r_load + i1**2 * r1 + i2**2 * r2)

# VP26.7.3: solve the modified Figure 26.12 as a nodal bridge with c=13 V,d=0.
bridge_edges = [
    ("c", "a", 1.0),  # c-a
    ("c", "b", 1.0),  # c-b
    ("a", "b", 1.0),  # a-b
    ("a", "d", 1.0),  # a-d
    ("b", "d", 3.0),  # modified b-d
]
v = nodal(bridge_edges, fixed={"c": 13.0, "d": 0.0})
currents_2673 = (
    edge_current(v, "c", "a", 1.0),
    edge_current(v, "c", "b", 1.0),
    edge_current(v, "a", "b", 1.0),
    edge_current(v, "a", "d", 1.0),
    edge_current(v, "b", "d", 3.0),
)
p_2673 = tuple(i * i * r for i, r in zip(currents_2673, (1, 1, 1, 1, 3)))
for actual, expected in zip(currents_2673, (52 / 9, 13 / 3, -13 / 9, 65 / 9, 26 / 9)):
    close(actual, expected)
for actual, expected in zip(p_2673, (33.382716049382715, 18.77777777777778, 2.0864197530864197, 52.160493827160494, 25.037037037037038)):
    close(actual, expected)
close(13 * (currents_2673[0] + currents_2673[1]), sum(p_2673))

# VP26.7.4: MNA for Figure 26.9a with ideal cells and equal R1=R2=R3=R.
emf1, emf2, resistor = 8.0, 9.0, 5.0
v, source_i = mna(
    resistors=[("left", "a", resistor), ("right", "a", resistor), ("top", "a", resistor)],
    voltage_sources=[("top", "left", emf1), ("top", "right", emf2)],
    ground="a",
)
i1, i2 = source_i
i3 = edge_current(v, "a", "top", resistor)  # arrow points upward a -> top
expected_i = (
    (emf2 - 2 * emf1) / (3 * resistor),
    (emf1 - 2 * emf2) / (3 * resistor),
    -(emf1 + emf2) / (3 * resistor),
)
for actual, expected in zip((i1, i2, i3), expected_i):
    close(actual, expected)
close(i1 + i2, i3)
source_output = -(emf1 * source_i[0] + emf2 * source_i[1])
resistor_loss = resistor * (i1**2 + i2**2 + i3**2)
close(source_output, resistor_loss)

# VP26.13.1: charging capacitor.
R, C, emf = 10.0e6, 3.20e-6, 9.00
tau = R * C
q_final = C * emf
i_initial = emf / R
q_fraction = 1 - exp(-18.0 / tau)
i_fraction = exp(-18.0 / tau)
close(tau, 32.0)
close(q_final, 28.8e-6)
close(i_initial, 0.900e-6)
close(q_fraction, 0.430217175269077)
close(i_fraction, 0.569782824730923)
close(q_fraction + i_fraction, 1.0)

# VP26.13.2: discharging capacitor.
C, q0, q_target, R = 2.20e-6, 4.20e-6, 1.20e-6, 4.00e6
tau = R * C
t_target = tau * log(q0 / q_target)
i_target = q_target / tau
close(tau, 8.80)
close(t_target, 11.02431412275924)
close(i_target, 1.3636363636363635e-7)
close(q0 * exp(-t_target / tau), q_target)

# VP26.13.3: infer the time constant from a measured charge ratio.
C, q0, q17 = 8.00e-6, 5.50e-6, 1.10e-6
tau = 17.0 / log(q0 / q17)
R = tau / C
i0, i17 = q0 / tau, q17 / tau
close(tau, 10.5626938875134)
close(R, 1320336.7359391751)
close(i0, 5.207005010816207e-7)
close(i17, 1.0414010021632415e-7)
close(q0 * exp(-17.0 / tau), q17)

# VP26.13.4: charge for 51 s, then discharge through a new resistor.
C, emf = 6.40e-6, 12.0
tau_charge = 5.00e6 * C
q_disconnect = C * emf * (1 - exp(-51.0 / tau_charge))
tau_discharge = 6.00e6 * C
q_after_70 = q_disconnect * exp(-70.0 / tau_discharge)
close(tau_charge, 32.0)
close(tau_discharge, 38.4)
close(q_disconnect, 61.19713361268235e-6)
close(q_after_70, 9.886633421016409e-6)

# Bridging Problem 26.27: series capacitance; parallel resistor/voltmeter;
# verify dU/dt both by resistor power and by differentiating U(q).
C1, C2, Q0 = 2.40e-6, 3.60e-6, 5.20e-6
R1, Rv = 655.0, 4.58e4
Ceq = 1 / (1 / C1 + 1 / C2)
Req = 1 / (1 / R1 + 1 / Rv)
V0 = Q0 / Ceq
U0 = Q0**2 / (2 * Ceq)
tau = Req * Ceq
dU0_power = -(V0**2) / Req
t_energy_e = tau / 2
U_energy_e = U0 / exp(1)
v_energy_e = V0 * exp(-t_energy_e / tau)
dU_energy_e_power = -(v_energy_e**2) / Req
q_energy_e = Q0 * exp(-t_energy_e / tau)
dU_energy_e_derivative = (q_energy_e / Ceq) * (-q_energy_e / tau)
close(Ceq, 1.44e-6)
close(Req, 645.7647185448284)
close(V0, 3.611111111111111)
close(U0, 9.388888888888889e-6)
close(tau, 0.0009299011947045528)
close(dU0_power, -0.020193304282982272)
close(t_energy_e, 0.0004649505973522764)
close(U_energy_e, U0 / exp(1))
close(dU_energy_e_power, -0.007428701495028412)
close(dU_energy_e_derivative, dU_energy_e_power)
close(-2 * U0 / (exp(1) * tau), dU_energy_e_power)
close(-2 * U0 / tau, dU0_power)

print("All Chapter 26 guided-practice nodal, MNA, RC, and energy checks passed.")
