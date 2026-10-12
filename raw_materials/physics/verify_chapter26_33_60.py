"""Independent numerical checks for Chapter 26 exercises 26.33-26.60."""

from math import isclose, log, sqrt


def close(actual, expected, *, rel_tol=2e-10, abs_tol=1e-12):
    assert isclose(actual, expected, rel_tol=rel_tol, abs_tol=abs_tol), (
        f"expected {expected}, got {actual}"
    )


def solve_linear(matrix, rhs):
    """Solve a small dense system with Gaussian elimination and pivoting."""
    a = [list(map(float, row)) + [float(value)] for row, value in zip(matrix, rhs)]
    n = len(a)
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(a[row][col]))
        if abs(a[pivot][col]) < 1e-14:
            raise ValueError("singular circuit equations")
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        a[col] = [value / scale for value in a[col]]
        for row in range(n):
            if row == col:
                continue
            factor = a[row][col]
            a[row] = [x - factor * y for x, y in zip(a[row], a[col])]
    return [a[row][-1] for row in range(n)]


def nodal_solution(node_count, branches):
    """Nodal solution for series-resistor/ideal-emf branches.

    Each branch tuple is (u, v, resistance, voltage_drop_u_to_v). Ground is None.
    Positive source voltage means the source's positive terminal is at u.
    """
    matrix = [[0.0] * node_count for _ in range(node_count)]
    rhs = [0.0] * node_count
    for u, v, resistance, voltage_drop in branches:
        conductance = 1.0 / resistance
        if u is not None:
            matrix[u][u] += conductance
            if v is not None:
                matrix[u][v] -= conductance
            rhs[u] += voltage_drop * conductance
        if v is not None:
            matrix[v][v] += conductance
            if u is not None:
                matrix[v][u] -= conductance
            rhs[v] -= voltage_drop * conductance
    return solve_linear(matrix, rhs)


# 26.33: galvanometer conversions.
rg, ig = 25.0, 500e-6
ammeter_range = 20e-3
shunt_33 = ig * rg / (ammeter_range - ig)
voltmeter_range = 500e-3
series_33 = voltmeter_range / ig - rg
close(shunt_33, 0.6410256410256411)
close(series_33, 975.0)

# 26.34: add resistance in the coil arm so the available shunt can carry 20 A.
rg, ig, shunt_34, total_current = 9.36, 0.0224, 0.0250, 20.0
series_34 = (total_current - ig) * shunt_34 / ig - rg
close(series_34, 12.936428571428571)
close(ig * (rg + series_34), (total_current - ig) * shunt_34)

# 26.35: voltmeter loading a 5 kOhm resistor in a 6 kOhm + 5 kOhm divider.
r_top, r_load, r_meter, v_source = 6e3, 5e3, 10e3, 50.0
r_parallel = 1.0 / (1.0 / r_load + 1.0 / r_meter)
v_measured = v_source * r_parallel / (r_top + r_parallel)
v_true = v_source * r_load / (r_top + r_load)
error_percent = 100.0 * (v_true - v_measured) / v_true
close(v_measured, 17.857142857142858)
close(v_true, 22.727272727272727)
close(error_percent, 21.428571428571427)

# 26.36: T_half = R C ln(2); the graph slope is 5.00 microfarads.
slope_36 = 5.00e-6
c_36 = slope_36 / log(2.0)
close(c_36, 7.213475204444817e-6)

# 26.37: capacitor voltage decays from 12.0 V to 3.0 V in 4.00 s.
r_37, t_37, v0_37, v_37 = 3.40e6, 4.00, 12.0, 3.0
tau_37 = t_37 / log(v0_37 / v_37)
c_37 = tau_37 / r_37
close(tau_37, 2.8853900817779268)
close(c_37, 8.486441416993902e-7)

# 26.38: charging at V_C = 8.00 V.
e_38, c_38, r_38, vc_38 = 36.0, 5e-6, 120.0, 8.0
tau_38 = r_38 * c_38
i_38 = (e_38 - vc_38) / r_38
t_38 = -tau_38 * log(1.0 - vc_38 / e_38)
power_cap_38 = vc_38 * i_38
close(i_38, 7.0 / 30.0)
close(t_38, 0.00015078865696854365)
close(power_cap_38, 28.0 / 15.0)

# 26.39: values at t=0+ and at the final steady state.
e_39, r_39, c_39 = 245.0, 7.50e3, 4.60e-6
i_initial_39 = e_39 / r_39
q_final_39 = c_39 * e_39
close(i_initial_39, 0.03266666666666666)
close(q_final_39, 1.127e-3)

# 26.40: use the instantaneous resistor drop and capacitor voltage.
r_40, c_40, current_40, q_40 = 12.0, 5e-6, 3.0, 40e-6
vc_40 = q_40 / c_40
e_40 = current_40 * r_40 + vc_40
tau_40 = r_40 * c_40
t_40 = -tau_40 * log(1.0 - q_40 / (c_40 * e_40))
p_cap_40 = vc_40 * current_40
p_battery_40 = e_40 * current_40
close(e_40, 44.0)
close(t_40, 12.040241727729076e-6)
close(p_cap_40, 24.0)
close(p_battery_40, 132.0)
close(p_cap_40 + current_40**2 * r_40, p_battery_40)

# 26.41: two initially equal-voltage capacitors in parallel discharge through
# the 50-ohm and 30-ohm resistors in series.
c_41 = (15.0 + 20.0) * 1e-6
r_41 = 50.0 + 30.0
tau_41 = r_41 * c_41
t_41 = tau_41 * log(45.0 / 10.0)
i_41 = 10.0 / r_41
close(tau_41, 2.8e-3)
close(t_41, 4.211416710973567e-3)
close(i_41, 0.125)

# 26.42: charge and current at the five requested times.
e_42, c_42, r_42 = 60.0, 12.4e-6, 0.895e6
tau_42 = r_42 * c_42
times_42 = [0.0, 5.0, 10.0, 20.0, 100.0]
q_42 = [c_42 * e_42 * (1.0 - __import__("math").exp(-t / tau_42)) for t in times_42]
i_42 = [(e_42 / r_42) * __import__("math").exp(-t / tau_42) for t in times_42]
plot_times_42 = [0.0, 5.0, 10.0, 15.0, 20.0]
q_plot_42 = [c_42 * e_42 * (1.0 - __import__("math").exp(-t / tau_42)) for t in plot_times_42]
i_plot_42 = [(e_42 / r_42) * __import__("math").exp(-t / tau_42) for t in plot_times_42]
close(tau_42, 11.098)
close(q_42[0], 0.0)
assert q_42[-1] < c_42 * e_42
assert c_42 * e_42 - q_42[-1] < 1e-7
close(i_42[0], e_42 / r_42)
close(q_plot_42[3] * 1e6, 551.4326133727332)
close(i_plot_42[3] * 1e6, 17.35153961319759)

# 26.43: q = C(E - iR) at the stated current.
e_43, r_43, c_43, i_43 = 120.0, 80.0, 4.00e-6, 0.900
q_43 = c_43 * (e_43 - i_43 * r_43)
close(q_43, 192e-6)

# 26.44: equivalent capacitances and time constants for two equal capacitors.
c_44, r_44 = 1.0, 1.0
tau_series_44 = r_44 * c_44 / 2.0
tau_parallel_44 = r_44 * 2.0 * c_44
t_one_percent_series = tau_series_44 * log(100.0)
t_one_percent_parallel = tau_parallel_44 * log(100.0)
assert t_one_percent_series < t_one_percent_parallel

# 26.45: three initially equal-charge capacitors discharge in series.
q0_45, c_values_45, r_45 = 3.50e-9, [20e-12, 10e-12, 15e-12], 25.0
c_eq_45 = 1.0 / sum(1.0 / c for c in c_values_45)
i0_45 = q0_45 / (r_45 * c_eq_45)
i_45 = i0_45 * sqrt(0.20)
close(c_eq_45, 4.615384615384615e-12)
close(i0_45, 30.333333333333332)
close(i_45, 13.565479063498723)

# 26.46: charging current when q = Q_max/4.
e_46, r_46, c_46 = 10.0, 12.0, 1.50e-6
i_max_46 = e_46 / r_46
i_quarter_charge_46 = i_max_46 * (1.0 - 0.25)
close(i_max_46, 5.0 / 6.0)
close(i_quarter_charge_46, 0.625)
assert not isclose(i_quarter_charge_46, i_max_46 / 4.0)

# 26.47: initially uncharged capacitors act as shorts; at steady state they
# act as opens. Capacitor 15 uF bypasses the left 25-ohm resistor. The 10 uF
# capacitor bypasses the upper right 25-ohm resistor, leaving the lower 25.
r_initial_47 = 15.0 + 75.0 + 1.0 / (1.0 / 25.0 + 1.0 / 50.0)
r_final_47 = 15.0 + 25.0 + 75.0 + 25.0 + 25.0
i_initial_47 = 100.0 / r_initial_47
i_final_47 = 100.0 / r_final_47
close(r_initial_47, 320.0 / 3.0)
close(r_final_47, 165.0)
close(i_initial_47, 0.9375)
close(i_final_47, 100.0 / 165.0)

# 26.48: charge halves at ln(2) tau; energy halves when charge is 1/sqrt(2).
tau_48 = 225.0 * 12e-6
t_half_charge_48 = tau_48 * log(2.0)
t_half_energy_48 = tau_48 * log(sqrt(2.0))
close(t_half_charge_48, 1.8714973875118525e-3)
close(t_half_energy_48, t_half_charge_48 / 2.0)

# 26.49: charge after 3.00 ms determines R; then find the 99% time.
c_49, e_49, q_3ms_49, t_49 = 5.90e-6, 28.0, 110e-6, 3e-3
q_final_49 = c_49 * e_49
tau_49 = -t_49 / log(1.0 - q_3ms_49 / q_final_49)
r_49 = tau_49 / c_49
t_99_49 = -tau_49 * log(0.01)
close(q_final_49, 165.2e-6)
close(r_49, 463.4, rel_tol=1e-3)
close(t_99_49, tau_49 * log(100.0))

# 26.50: discharge to the current specified in the problem.
c_50, e_50, r_50, i_50 = 6e-6, 50.0, 185.0, 0.180
q0_50 = c_50 * e_50
i0_50 = e_50 / r_50
q_50 = i_50 * r_50 * c_50
t_50 = r_50 * c_50 * log(i0_50 / i_50)
close(q0_50, 300e-6)
close(q_50, 199.8e-6)
close(t_50, 0.45117682537034034e-3)

# 26.51: heater and dryer power levels on a 120 V, 20 A circuit.
breaker_51, v_51, heater_51 = 20.0, 120.0, 1500.0
dryer_levels_51 = [600.0, 900.0, 1200.0, 1500.0]
total_currents_51 = [(heater_51 + p) / v_51 for p in dryer_levels_51]
assert total_currents_51[0] < breaker_51
close(total_currents_51[1], breaker_51)
assert total_currents_51[2] > breaker_51

# 26.52: dryer current, hot resistance, and hourly cost.
p_52, v_52, price_52 = 4100.0, 240.0, 0.11
i_52 = p_52 / v_52
r_52 = v_52**2 / p_52
cost_52 = (p_52 / 1000.0) * price_52
close(i_52, 17.083333333333332)
close(r_52, 57600.0 / 4100.0)
close(cost_52, 0.451)

# 26.53: integrate charging power symbolically using tau = R*C.
# E*i integrates to C*E^2, while i^2*R integrates to C*E^2/2.
fraction_stored_53 = 0.5
fraction_dissipated_53 = 0.5
close(fraction_stored_53 + fraction_dissipated_53, 1.0)

# 26.54: R1 and R2 are series in one branch, in parallel with R3, then R4.
e_54, power_54, r4_54 = 48.0, 295.0, 3.0
r12_54 = 4.0 + 4.0
r_parallel_54 = e_54**2 / power_54 - r4_54
r3_54 = 1.0 / (1.0 / r_parallel_54 - 1.0 / r12_54)
close(r3_54, 12.063761955366633)

# 26.55: Figure 26.6a has E1, E2 with positive terminals at the top, each
# with 2-ohm internal resistance, in parallel with R=20 ohm.
v_top_55 = (24.0 / 2.0 + 36.0 / 2.0) / (1.0 / 2.0 + 1.0 / 2.0 + 1.0 / 20.0)
i1_55 = (v_top_55 - 24.0) / 2.0
i2_55 = (v_top_55 - 36.0) / 2.0
ir_55 = v_top_55 / 20.0
close(v_top_55, 200.0 / 7.0)
close(i1_55, 16.0 / 7.0)
close(i2_55, -26.0 / 7.0)
close(ir_55, 10.0 / 7.0)
close(i1_55 + i2_55 + ir_55, 0.0)

# 26.56: two equal resistors in parallel, in series with the third resistor.
r_56 = 2.4
current_limit_56 = sqrt(48.0 / r_56)
power_total_56 = current_limit_56**2 * (r_56 + r_56 / 2.0)
close(power_total_56, 72.0)
close((current_limit_56 / 2.0) ** 2 * r_56, 12.0)

# 26.57: nodal solve for the three top/bottom branches and side resistors.
# All three branch emfs have their positive terminal on the left.
# Node order: top-left, a, top-right, right midpoint, bottom-right. Ground=bottom-left.
branches_57_open = [
    (0, 2, 1.0, 12.0),
    (0, 1, 2.0, 0.0),
    (1, None, 2.0, 0.0),
    (2, 3, 1.0, 0.0),
    (3, 4, 2.0, 0.0),
    (None, 4, 1.0, 8.0),
]
nodes_57_open = nodal_solution(5, branches_57_open)
v_a_57 = nodes_57_open[1]
v_right_mid_57 = nodes_57_open[3]
v_b_57 = v_right_mid_57 + 10.0
v_ab_57 = v_a_57 - v_b_57
close(v_ab_57, 2.0 / 9.0)

# Short a-b: the middle branch (1-ohm, 10-V source, 3-ohm) is active.
branches_57_short = [
    (0, 2, 1.0, 12.0),
    (0, 1, 2.0, 0.0),
    (1, None, 2.0, 0.0),
    (2, 3, 1.0, 0.0),
    (3, 4, 2.0, 0.0),
    (None, 4, 1.0, 8.0),
    (1, 3, 4.0, 10.0),
]
nodes_57_short = nodal_solution(5, branches_57_short)
i12_battery_57 = (nodes_57_short[0] - nodes_57_short[2] - 12.0) / 1.0
close(i12_battery_57, -13.0 / 28.0)

# 26.58: three parallel branches (20, 10, 20 ohm) are in series with 15,10,5 ohm.
r_network_58 = 1.0 / (1.0 / 20.0 + 1.0 / 10.0 + 1.0 / 20.0)
r_total_58 = 15.0 + r_network_58 + 10.0 + 5.0
i_total_58 = 45.0 / r_total_58
v_network_58 = i_total_58 * r_network_58
p_ice_58 = v_network_58**2 / 20.0
melt_g_s_58 = p_ice_58 / (3.34e5) * 1000.0
close(r_network_58, 5.0)
close(r_total_58, 35.0)
close(p_ice_58, 2.066326530612245)
close(melt_g_s_58, 0.006186606379078577)

# 26.59: nodal solution for the resistor network with oriented cell sources.
# Positive terminal of the 12-V source is at the left; 9-V source is at right.
# Node order L, M; ground=right.
branches_59 = [
    (0, 1, 5.0, 0.0),
    (1, None, 8.0, 0.0),
    (0, None, 10.0, 0.0),
    (0, 1, 1.0, 12.0),
    (1, None, 1.0, -9.0),
]
nodes_59 = nodal_solution(2, branches_59)
v_l_59, v_m_59 = nodes_59
i2_59 = -(v_l_59 - v_m_59 - 12.0) / 1.0
i1_59 = (v_m_59 - (-9.0)) / 1.0
i3_59 = v_l_59 / 10.0
close(i1_59, 0.8483412322274884)
close(i2_59, 2.142180094786731)
close(i3_59, 0.17061611374407581)

# 26.60: solve branch KCL for the unknown emf, positive terminal at top.
v_load_60 = 1.80 * 7.0
i_left_60 = (v_load_60 - 24.0) / 3.0
i_right_60 = 1.80
i_mid_60 = -(i_left_60 + i_right_60)
e_60 = v_load_60 - 2.0 * i_mid_60
close(v_load_60, 12.6)
close(i_left_60, -3.8)
close(i_mid_60, 2.0)
close(e_60, 8.6)

print("Chapter 26 exercises 26.33-26.60 checks passed.")
print(f"26.33 shunt={shunt_33:.6g} ohm, voltmeter series resistor={series_33:.6g} ohm")
print(f"26.36 C={c_36 * 1e6:.6g} microfarad; 26.37 tau={tau_37:.6g} s")
print(f"26.47 ammeter: initial={i_initial_47:.6g} A, steady={i_final_47:.6g} A")
print(f"26.55 I1={i1_55:.6g} A down, I2={i2_55:.6g} A down, IR={ir_55:.6g} A down")
print(f"26.57 Vab={v_ab_57:.6g} V open; I12V={i12_battery_57:.6g} A left-to-right when a-b shorted")
print(f"26.58 melt rate={melt_g_s_58:.6g} g/s; 26.59 I1={i1_59:.6g} A, I2={i2_59:.6g} A, I3={i3_59:.6g} A")
print(f"26.60 required emf={e_60:.6g} V")
