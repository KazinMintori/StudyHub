"""Numerical checks for translated Young & Freedman sections 25.5–25.6."""

from math import isclose

# Example 25.8: 12 V source, 2 ohm internal resistance, 4 ohm load, 2 A.
emf, r_internal, r_load, current = 12.0, 2.0, 4.0, 2.0
v_terminal = emf - current * r_internal
chemical_to_electrical = emf * current
internal_heat = current**2 * r_internal
source_output = v_terminal * current
load_heat = current**2 * r_load
assert isclose(v_terminal, 8.0)
assert isclose(chemical_to_electrical, 24.0)
assert isclose(internal_heat, 8.0)
assert isclose(source_output, 16.0)
assert isclose(load_heat, 16.0)
assert isclose(chemical_to_electrical, internal_heat + load_heat)

# Example 25.9: replace the 4 ohm load with 8 ohm.
r_load_9 = 8.0
current_9 = emf / (r_load_9 + r_internal)
v_load_9 = current_9 * r_load_9
load_power_9 = current_9**2 * r_load_9
chemical_9 = emf * current_9
internal_9 = current_9**2 * r_internal
output_9 = v_load_9 * current_9
assert isclose(current_9, 1.2)
assert isclose(v_load_9, 9.6)
assert isclose(load_power_9, 11.52)
assert isclose(chemical_9, 14.4)
assert isclose(internal_9, 2.88)
assert isclose(output_9, load_power_9)
assert isclose(chemical_9, internal_9 + load_power_9)

# Example 25.10: short circuit, zero external resistance.
current_short = emf / r_internal
chemical_short = emf * current_short
internal_short = current_short**2 * r_internal
terminal_short = emf - current_short * r_internal
output_short = terminal_short * current_short
assert isclose(current_short, 6.0)
assert isclose(chemical_short, 72.0)
assert isclose(internal_short, 72.0)
assert isclose(terminal_short, 0.0)
assert isclose(output_short, 0.0)

# Strategy 25.1: rank net battery powers for the three check circuits.
rank_i = (1.5 - 1.0 * 0.10) * 1.0
rank_ii = 3.6 * 2.0
rank_iii = 11.0 * ((12.0 - 11.0) / 0.20)
assert isclose(rank_i, 1.4)
assert isclose(rank_ii, 7.2)
assert isclose(rank_iii, 55.0)
assert rank_iii > rank_ii > rank_i

# Example 25.11: mean free time and reciprocal collision rate in copper.
mass_e = 9.11e-31
electron_density = 8.5e28
charge_e = 1.60e-19
resistivity_copper = 1.72e-8
tau = mass_e / (electron_density * charge_e**2 * resistivity_copper)
collision_rate = 1.0 / tau
assert isclose(tau, 2.4e-14, rel_tol=0.02)
assert isclose(collision_rate, 4.108e13, rel_tol=0.002)

print(f"25.8: source chemical conversion {chemical_to_electrical:.4g} W, "
      f"internal loss {internal_heat:.4g} W, output/load {source_output:.4g} W")
print(f"25.9: I={current_9:.4g} A, Vload={v_load_9:.4g} V, "
      f"load={load_power_9:.4g} W, chemical={chemical_9:.4g} W, internal={internal_9:.4g} W")
print(f"25.10: Ishort={current_short:.4g} A, chemical/internal={chemical_short:.4g} W, output={output_short:.4g} W")
print(f"25.5 check: battery powers rank {rank_iii:.4g} > {rank_ii:.4g} > {rank_i:.4g} W")
print(f"25.11: tau={tau:.4g} s, collision rate={collision_rate:.4g} s^-1")
