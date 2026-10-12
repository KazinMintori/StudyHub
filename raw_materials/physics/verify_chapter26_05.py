"""Recompute numerical results used in the Chapter 26.5 translation."""

from math import isclose


def close(actual, expected, *, rel_tol=1e-12, abs_tol=1e-12):
    assert isclose(actual, expected, rel_tol=rel_tol, abs_tol=abs_tol), (
        f"expected {expected}, got {actual}"
    )


# Household examples at 120 V.
v_house = 120.0
i_bulb = 100.0 / v_house
r_bulb = v_house**2 / 100.0
i_waffle = 1500.0 / v_house
r_waffle = v_house**2 / 1500.0
close(i_bulb, 0.8333333333333334)
close(r_bulb, 144.0)
close(i_waffle, 12.5)
close(r_waffle, 9.6)

# The 20 A to 40 A breaker comparison in the section check.
wire_heating_ratio = (40.0 / 20.0) ** 2
close(wire_heating_ratio, 4.0)

# Example 26.14: three parallel appliances on a nominal 120 V, 20 A circuit.
loads = {"toaster": 1800.0, "frying_pan": 1300.0, "lamp": 100.0}
currents = {name: power / v_house for name, power in loads.items()}
resistances = {name: v_house**2 / power for name, power in loads.items()}
total_current = sum(currents.values())
equivalent_current = sum(loads.values()) / v_house
equivalent_resistance = 1.0 / sum(1.0 / resistance for resistance in resistances.values())
close(currents["toaster"], 15.0)
close(resistances["toaster"], 8.0)
close(currents["frying_pan"], 10.833333333333334)
close(resistances["frying_pan"], 120.0**2 / 1300.0)
close(currents["lamp"], 0.8333333333333334)
close(resistances["lamp"], 144.0)
close(total_current, 26.666666666666668)
close(equivalent_current, total_current)
close(v_house / equivalent_resistance, total_current)
assert total_current > 20.0

# Energy and cost example for a 1500 W appliance operating for one hour.
energy_kwh = (1500.0 / 1000.0) * 1.0
energy_j = 1500.0 * 3600.0
cost_dollars = energy_kwh * 0.10
close(energy_kwh, 1.5)
close(energy_j, 5.4e6)
close(cost_dollars, 0.15)

# Same power requires more current at the lower automotive voltage.
i_headlight = 100.0 / 13.0
close(i_headlight, 7.6923076923076925)
close(120.0 - (-120.0), 240.0)

print("Chapter 26.5 arithmetic checks passed.")
print(f"100 W lamp at 120 V: I={i_bulb:.6f} A, R={r_bulb:.1f} ohm")
print(f"1500 W appliance at 120 V: I={i_waffle:.1f} A, R={r_waffle:.1f} ohm")
print(f"Example 26.14 total current: {total_current:.6f} A")
print(f"40 A versus 20 A wire heating ratio at fixed R: {wire_heating_ratio:.1f}")
print(f"1500 W for one hour: {energy_kwh:.1f} kWh = {energy_j:.3g} J, cost=${cost_dollars:.2f}")
print(f"100 W headlight at 13 V: I={i_headlight:.6f} A")
