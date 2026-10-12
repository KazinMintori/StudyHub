"""Independent checks for numerical and network claims in Q26.1-Q26.21."""

from math import isclose


def close(actual, expected, *, rel_tol=1e-12, abs_tol=1e-12):
    assert isclose(actual, expected, rel_tol=rel_tol, abs_tol=abs_tol), (
        f"expected {expected}, got {actual}"
    )


# Q26.1: rated resistance, then series and parallel voltage behavior.
v_rated = 120.0
r_60 = v_rated**2 / 60.0
r_120 = v_rated**2 / 120.0
i_series_q1 = v_rated / (r_60 + r_120)
v_60_series = i_series_q1 * r_60
v_120_series = i_series_q1 * r_120
v_60_parallel = v_120_parallel = v_rated
close(r_60, 240.0)
close(r_120, 120.0)
close(v_60_series / v_120_series, 2.0)
close(v_60_series + v_120_series, v_rated)
close(v_60_parallel, v_120_parallel)

# Q26.3: adding identical bulbs changes the series load but not each
# ideal-source parallel branch voltage.
n_bulbs, bulb_r, flashlight_emf = 3, 1.0, 3.0
p_each_series = flashlight_emf**2 / (n_bulbs**2 * bulb_r)
p_each_parallel = flashlight_emf**2 / bulb_r
i_total_series = flashlight_emf / (n_bulbs * bulb_r)
i_total_parallel = n_bulbs * flashlight_emf / bulb_r
assert p_each_series < p_each_parallel
assert i_total_series < i_total_parallel

# Q26.2: rated 120 V lamps placed in series across 240 V.
r_25 = v_rated**2 / 25.0
r_200 = v_rated**2 / 200.0
i_series_q2 = 240.0 / (r_25 + r_200)
v_25 = i_series_q2 * r_25
v_200 = i_series_q2 * r_200
p_25 = i_series_q2**2 * r_25
p_200 = i_series_q2**2 * r_200
close(r_25, 576.0)
close(r_200, 72.0)
close(v_25 + v_200, 240.0)
assert v_25 > 120.0 and p_25 > 25.0
assert v_200 < 120.0 and p_200 < 200.0

# Q26.4: one bulb in parallel with a branch of two identical series bulbs.
e, bulb_r = 12.0, 1.0
i_a = e / bulb_r
i_bc_branch = e / (2.0 * bulb_r)
p_a = i_a**2 * bulb_r
p_b = i_bc_branch**2 * bulb_r
close(i_a, 2.0 * i_bc_branch)
close(p_a, 4.0 * p_b)

# Q26.5-Q26.6: unequal resistors in series and parallel.
e, r1, r2 = 12.0, 1.0, 2.0
i_series = e / (r1 + r2)
i1_series = i2_series = i_series
p1_series, p2_series = i_series**2 * r1, i_series**2 * r2
v1_series, v2_series = i_series * r1, i_series * r2
close(i1_series, i2_series)
assert p2_series > p1_series and v2_series > v1_series

i1_parallel, i2_parallel = e / r1, e / r2
p1_parallel, p2_parallel = e**2 / r1, e**2 / r2
close(i1_parallel + i2_parallel, e * (1.0 / r1 + 1.0 / r2))
close(p1_parallel, e * i1_parallel)
close(p2_parallel, e * i2_parallel)
assert i1_parallel > i2_parallel and p1_parallel > p2_parallel

# Q26.7-Q26.8: ideal source keeps the voltage across parallel branches fixed.
v_b1_before = e
v_b1_after = e
close(v_b1_before, v_b1_after)
current_three_strips = e / (bulb_r / 3.0)
current_two_strips = e / (bulb_r / 2.0)
close(current_two_strips / current_three_strips, 2.0 / 3.0)

# Q26.9: closing the switch adds a resistor branch to a parallel group,
# which is in series with a resistor and the bulb. Use equal 1-ohm elements.
e = 12.0
parallel_open = 1.0 / (1.0 / 1.0 + 1.0 / 1.0)
parallel_closed = 1.0 / (1.0 / 1.0 + 1.0 / 1.0 + 1.0 / 1.0)
i_bulb_open = e / (1.0 + parallel_open)
i_bulb_closed = e / (1.0 + parallel_closed)
close(i_bulb_closed / i_bulb_open, 9.0 / 8.0)
assert i_bulb_closed**2 > i_bulb_open**2

# Q26.10: a real battery's terminal voltage falls as the parallel load rises.
r_internal = r_bulb = r_switch_branch = 1.0
load_open = r_bulb
load_closed = 1.0 / (1.0 / r_bulb + 1.0 / r_switch_branch)
v_terminal_open = e * load_open / (r_internal + load_open)
v_terminal_closed = e * load_closed / (r_internal + load_closed)
p_bulb_open = v_terminal_open**2 / r_bulb
p_bulb_closed = v_terminal_closed**2 / r_bulb
close(v_terminal_open, 6.0)
close(v_terminal_closed, 4.0)
close(p_bulb_closed / p_bulb_open, 4.0 / 9.0)
assert p_bulb_closed < p_bulb_open

# Q26.11: ideal voltage source holds the bulb voltage fixed.
v_bulb_ideal_before = e
v_bulb_ideal_after = e
close(v_bulb_ideal_before**2 / r_bulb, v_bulb_ideal_after**2 / r_bulb)

# Q26.12: two lamps in series, one single lamp, and a switched resistor branch.
r_internal = 1.0
load_open = 1.0 / (1.0 / 2.0 + 1.0 / 1.0)
load_closed = 1.0 / (1.0 / 2.0 + 1.0 / 1.0 + 1.0 / 1.0)
v_open = e * load_open / (r_internal + load_open)
v_closed = e * load_closed / (r_internal + load_closed)
assert v_closed < v_open
assert (v_closed / 2.0) ** 2 < (v_open / 2.0) ** 2
assert v_closed**2 < v_open**2

# Q26.14 and Q26.16: an ideal switch bypasses a lamp.
p_b1_before = e**2 / (2.0**2 * bulb_r)
p_b1_after = e**2 / bulb_r
close(p_b1_after / p_b1_before, 4.0)
p_a_three_before = e**2 / (3.0**2 * bulb_r)
p_a_three_after = e**2 / (2.0**2 * bulb_r)
close(p_a_three_after / p_a_three_before, 9.0 / 4.0)

# Q26.15: for n identical cells, parallel keeps emf and divides internal r;
# series adds emf and internal resistance.
n_cells, emf_cell, r_cell = 2, 1.5, 0.5
emf_parallel = emf_cell
emf_series = n_cells * emf_cell
r_internal_parallel = r_cell / n_cells
close(emf_parallel, 1.5)
close(emf_series, 3.0)
close(r_internal_parallel, 0.25)

# Q26.18: equivalent capacitance, time constant, initial current, final charge.
capacitance, resistance, emf = 1.0e-6, 2.0e6, 12.0
c_series = capacitance / 2.0
c_parallel = 2.0 * capacitance
tau_series = resistance * c_series
tau_parallel = resistance * c_parallel
i_initial_series = emf / resistance
i_initial_parallel = emf / resistance
q_series_each = c_series * emf
q_parallel_each = capacitance * emf
close(tau_series, 1.0)
close(tau_parallel, 4.0)
close(i_initial_series, i_initial_parallel)
close(q_series_each, 6.0e-6)
close(q_parallel_each, 12.0e-6)
assert tau_series < tau_parallel

# Q26.19: symbolic SI base dimensions (M, L, T, I) for ohm and farad.
ohm_dims = (1, 2, -3, -2)
farad_dims = (-1, -2, 4, 2)
rc_dims = tuple(a + b for a, b in zip(ohm_dims, farad_dims))
assert rc_dims == (0, 0, 1, 0)

# Q26.20-Q26.21: R=tau/C and ideal final charge Q=CE independent of R.
tau_measured, known_c = 120.0, 1.0e-6
r_inferred = tau_measured / known_c
close(r_inferred, 120.0e6)
q_final_r_small = known_c * emf
q_final_r_large = known_c * emf
close(q_final_r_small, 12.0e-6)
close(q_final_r_small, q_final_r_large)  # R does not enter Q_final=C*emf

print("Discussion-question checks Q26.1-Q26.21 passed.")
print(f"Q26.2 25 W bulb: V={v_25:.3f} V, P={p_25:.3f} W; 200 W bulb: V={v_200:.3f} V, P={p_200:.3f} W")
print(f"Q26.10 representative real-battery bulb power ratio: {p_bulb_closed / p_bulb_open:.6f}")
print(f"Q26.18 time constants: series={tau_series:.3g} s, parallel={tau_parallel:.3g} s")
