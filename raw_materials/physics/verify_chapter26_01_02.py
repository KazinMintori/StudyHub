"""Independent arithmetic and sign checks for the Chapter 26.1–26.2 drafts."""

from math import isclose


def close(actual, expected, *, rel_tol=1e-12, abs_tol=1e-12):
    assert isclose(actual, expected, rel_tol=rel_tol, abs_tol=abs_tol), (
        actual,
        expected,
    )


# Example 26.1: parallel reduction and branch currents.
r_parallel = 1 / (1 / 6 + 1 / 3)
r_network = r_parallel + 4
current_total = 18 / r_network
v_parallel = current_total * r_parallel
currents_parallel = (v_parallel / 6, v_parallel / 3)
close(r_parallel, 2)
close(r_network, 6)
close(current_total, 3)
close(v_parallel, 6)
assert currents_parallel == (1, 2)
close(sum(currents_parallel), current_total)
close(1 / r_parallel, 1 / 6 + 1 / 3)

# Equal-resistance arrangements in the section 26.1 understanding check.
equivalent_rank_values = (3, 1 / 3, 3 / 2, 2 / 3)
assert sorted(range(4), key=lambda i: equivalent_rank_values[i], reverse=True) == [0, 2, 3, 1]

# Example 26.2: two identical bulbs in series and parallel, including the
# power comparison and total-power conservation for an ideal 8 V source.
r_bulb = 2
emf_bulbs = 8
i_series = emf_bulbs / (2 * r_bulb)
v_series_each = i_series * r_bulb
p_series_each = i_series**2 * r_bulb
p_series_total = 2 * p_series_each
i_parallel_each = emf_bulbs / r_bulb
p_parallel_each = i_parallel_each**2 * r_bulb
p_parallel_total = 2 * p_parallel_each
close(i_series, 2)
close(v_series_each, 4)
close(p_series_each, 8)
close(p_series_total, 16)
close(i_parallel_each, 4)
close(p_parallel_each, 32)
close(p_parallel_total, 64)
close(p_parallel_each / p_series_each, 4)
close(p_parallel_total / p_series_total, 4)
close(i_series * (2 * r_bulb), emf_bulbs)
close(i_parallel_each * r_bulb, emf_bulbs)

# Example 26.3: single-loop sign convention, terminal potential, source
# powers and resistor dissipation.
i_loop = (12 - 4) / (4 + 7 + 2 + 3)
v_ab_lower = i_loop * 7 + 4 + i_loop * 4
v_ab_upper = 12 - i_loop * 2 - i_loop * 3
p_emf_12 = 12 * i_loop
p_emf_4 = -4 * i_loop
p_resistors = i_loop**2 * (4 + 7 + 2 + 3)
close(i_loop, 0.5)
close(v_ab_lower, 9.5)
close(v_ab_upper, v_ab_lower)
close(p_emf_12, 6)
close(p_emf_4, -2)
close(p_resistors, 4)
close(p_emf_12 + p_emf_4, p_resistors)

# Example 26.4: node and loop equations, assumed polarity, and path checks.
i_source = 1 + 2
r_source = (12 - 2 * 3) / i_source
emf_battery = 1 * 1 - 2 * 3
v_ba_bulb = 2 * 3
v_ba_right_branch = 12 - i_source * r_source
v_ba_middle_branch = -emf_battery + 1 * 1
close(i_source, 3)
close(r_source, 2)
close(emf_battery, -5)
close(-i_source + 1 + 2, 0)
close(12 - i_source * r_source - 2 * 3, 0)
close(-emf_battery + 1 * 1 - 2 * 3, 0)
close(12 - i_source * r_source - 1 * 1 + emf_battery, 0)
close(v_ba_bulb, 6)
close(v_ba_right_branch, v_ba_bulb)
close(v_ba_middle_branch, v_ba_bulb)

# Example 26.5: all power terms and conservation at the circuit level.
p_supply_emf = 12 * i_source
p_supply_internal = i_source**2 * r_source
p_supply_net = p_supply_emf - p_supply_internal
p_battery_stored = -emf_battery * 1
p_battery_internal = 1**2 * 1
p_bulb = 2**2 * 3
close(p_supply_emf, 36)
close(p_supply_internal, 18)
close(p_supply_net, 18)
close(p_battery_stored, 5)
close(p_battery_internal, 1)
close(p_bulb, 12)
close(p_supply_net, p_battery_stored + p_battery_internal + p_bulb)

# Example 26.6: solve the displayed three-loop system independently.
# Unknowns are I1, I2, I3. The reduced equations are
# 2 I1 - I3 = 13; 3 I1 + 5 I3 = 13; -I1 + I2 - I3 = 0.
det = 2 * 5 - (-1 * 3)
i1 = (13 * 5 - (-1 * 13)) / det
i3 = (2 * 13 - 3 * 13) / det
i2 = i1 + i3
branch_currents = (i1, i2, i3, i1 - i3, i2 + i3)
loop_residuals = (
    13 - i1 * 1 - (i1 - i3) * 1,
    -i2 * 1 - (i2 + i3) * 2 + 13,
    -i1 * 1 - i3 * 1 + i2 * 1,
)
close(i1 * 2 - i3, 13)
close(i1 * 3 + i3 * 5, 13)
close(-i1 + i2 - i3, 0)
assert branch_currents == (6, 5, -1, 7, 4)
for residual in loop_residuals:
    close(residual, 0)
close(i1 + i2, 11)
r_bridge = 13 / (i1 + i2)
close(r_bridge, 13 / 11)
close(r_bridge, 1.2, abs_tol=0.02)  # Source rounds to 1.2 ohm.

# Example 26.7: same V_ab from the central and lower paths.
v_ab_center = -abs(i3) * 1
v_ab_lower = -(i2 + i3) * 2 + (i1 - i3) * 1
close(v_ab_center, -1)
close(v_ab_lower, v_ab_center)

# Understanding check: subtracting the two loop equations gives the
# c-b-d-a-c path, and its residual is dependent on the first two loops.
eq1 = 13 - i1 * 1 - (i1 - i3) * 1
eq2 = -i2 * 1 - (i2 + i3) * 2 + 13
dependent_loop = eq2 - eq1
path_cbdac = (
    -i2 * 1
    - (i2 + i3) * 2
    + (i1 - i3) * 1
    + i1 * 1
)
close(dependent_loop, 0)
close(path_cbdac, dependent_loop)

print("Chapter 26.1–26.2 arithmetic and Kirchhoff sign checks passed.")
