"""Independent numerical checks for Chapter 26 sections 26.3 and 26.4.

Run with: python raw_materials/physics/verify_chapter26_03_04.py
"""

from __future__ import annotations

import math


def simpson(function, start: float, stop: float, intervals: int = 20_000) -> float:
    """Composite Simpson integration with an even number of intervals."""
    if intervals % 2:
        raise ValueError("Simpson integration needs an even interval count")
    step = (stop - start) / intervals
    total = function(start) + function(stop)
    total += 4 * sum(function(start + k * step) for k in range(1, intervals, 2))
    total += 2 * sum(function(start + k * step) for k in range(2, intervals, 2))
    return total * step / 3


def close(actual: float, expected: float, *, rel_tol: float = 1e-9) -> None:
    if not math.isclose(actual, expected, rel_tol=rel_tol, abs_tol=1e-14):
        raise AssertionError(f"{actual:.12g} != {expected:.12g}")


# Galvanometer conversions in Examples 26.8 and 26.9.
ifull = 1.00e-3
coil_resistance = 20.0
ammeter_range = 50.0e-3
full_scale_voltage = ifull * coil_resistance
shunt_resistance = full_scale_voltage / (ammeter_range - ifull)
ammeter_resistance = 1 / (1 / coil_resistance + 1 / shunt_resistance)
shunt_current = ammeter_range - ifull

voltmeter_range = 10.0
series_resistance = voltmeter_range / ifull - coil_resistance
voltmeter_resistance = series_resistance + coil_resistance

close(full_scale_voltage, 0.0200)
close(shunt_resistance, 0.40816326530612246)
close(ammeter_resistance, 0.400)
close(shunt_current, 49.0e-3)
close(series_resistance, 9980.0)
close(voltmeter_resistance, 10_000.0)

# Ammeter-voltmeter measurement arrangements in Examples 26.10 and 26.11.
meter_voltage = 12.0
ammeter_reading = 0.100
ammeter_internal_resistance = 2.00
voltmeter_internal_resistance = 10_000.0

resistor_voltage_a = meter_voltage - ammeter_reading * ammeter_internal_resistance
resistance_a = resistor_voltage_a / ammeter_reading
power_a = resistor_voltage_a * ammeter_reading
close(resistor_voltage_a, 11.8)
close(resistance_a, 118.0)
close(power_a, 1.18)
close(ammeter_reading**2 * resistance_a, power_a)

voltmeter_current = meter_voltage / voltmeter_internal_resistance
resistor_current_b = ammeter_reading - voltmeter_current
resistance_b = meter_voltage / resistor_current_b
power_b = meter_voltage * resistor_current_b
close(voltmeter_current, 1.20e-3)
close(resistor_current_b, 0.0988)
close(resistance_b, 121.4574898785425)
close(power_b, 1.1856)

# RC charging and discharging examples.
emf = 12.0
resistance = 10.0e6
capacitance = 1.0e-6
tau = resistance * capacitance
initial_current = emf / resistance
final_charge = capacitance * emf
charge_fraction_46s = 1 - math.exp(-46.0 / tau)
current_fraction_46s = math.exp(-46.0 / tau)

initial_discharge_charge = 5.0e-6
target_charge_fraction = 0.50e-6 / initial_discharge_charge
target_discharge_time = -tau * math.log(target_charge_fraction)
target_discharge_current = -(initial_discharge_charge / tau) * target_charge_fraction

close(tau, 10.0)
close(initial_current, 1.2e-6)
close(final_charge, 12.0e-6)
close(charge_fraction_46s, 0.9899481642553665)
close(current_fraction_46s, 0.010051835744633504)
close(target_discharge_time, 23.02585092994046)
close(target_discharge_current, -5.0e-8)
close(math.exp(-1) ** 2, 1 / math.e**2)

# Independently integrate charge and energy over 40 time constants.
# The remaining exponential tail is below 5e-18 of its initial scale.
end_time = 40 * tau


def charging_current(time: float) -> float:
    return initial_current * math.exp(-time / tau)


def charging_charge(time: float) -> float:
    return final_charge * (1 - math.exp(-time / tau))


charge_from_source = simpson(charging_current, 0.0, end_time)
source_energy = simpson(lambda time: emf * charging_current(time), 0.0, end_time)
resistor_energy = simpson(
    lambda time: charging_current(time) ** 2 * resistance, 0.0, end_time
)
stored_energy_at_end = charging_charge(end_time) ** 2 / (2 * capacitance)
full_charge_energy = final_charge**2 / (2 * capacitance)

close(charge_from_source, charging_charge(end_time), rel_tol=1e-10)
close(source_energy, resistor_energy + stored_energy_at_end, rel_tol=1e-10)
close(resistor_energy, full_charge_energy, rel_tol=1e-10)
close(stored_energy_at_end, full_charge_energy, rel_tol=1e-10)


def discharging_current(time: float) -> float:
    return -(initial_discharge_charge / tau) * math.exp(-time / tau)


discharged_charge = -simpson(discharging_current, 0.0, end_time)
discharged_energy = simpson(
    lambda time: discharging_current(time) ** 2 * resistance, 0.0, end_time
)
initial_stored_energy = initial_discharge_charge**2 / (2 * capacitance)
close(discharged_charge, initial_discharge_charge, rel_tol=1e-10)
close(discharged_energy, initial_stored_energy, rel_tol=1e-10)

print("Chapter 26.3 and 26.4 calculations verified.")
print(f"Ammeter shunt: {shunt_resistance:.6f} ohm, equivalent R: {ammeter_resistance:.3f} ohm")
print(f"Voltmeter series resistor: {series_resistance:.0f} ohm")
print(f"Meter corrections: R_a={resistance_a:.1f} ohm, P_a={power_a:.2f} W; R_b={resistance_b:.1f} ohm, P_b={power_b:.2f} W")
print(f"RC charging: tau={tau:.1f} s, q/Qf at 46 s={charge_fraction_46s:.6f}, i/I0={current_fraction_46s:.6f}")
print(f"RC discharging: t(q=0.10 Q0)={target_discharge_time:.3f} s, i={target_discharge_current:.3g} A")
print(f"Numerical charging balance: source={source_energy:.9g} J, resistor={resistor_energy:.9g} J, capacitor={stored_energy_at_end:.9g} J")
print(f"Numerical discharge: charge removed={discharged_charge:.9g} C, heat={discharged_energy:.9g} J, initial energy={initial_stored_energy:.9g} J")
