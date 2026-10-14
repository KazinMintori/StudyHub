"""Verify all numerical calculations, formulas, and concepts in Chapter 32 Theory B (Sections 32.4-32.5, Examples 32.3-32.7, and Self-Checks).

Uses exact numerical computation and numpy discretization to ensure 100% precision.
"""
from pathlib import Path
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'qa/physics/chapter32'
OUT.mkdir(parents=True, exist_ok=True)

# Standard constants used in Young & Freedman 15th ed
c = 3.00e8          # Speed of light in vacuum (m/s)
mu0 = 4 * math.pi * 1e-7  # Permeability of free space (T*m/A)
eps0 = 8.85e-12     # Permittivity of free space (C^2/(N*m^2), rounded 3-sig-fig textbook value)
eps0_exact = 1.0 / (mu0 * c**2) # Exact theoretical permittivity for c = 3.00e8 m/s

def close(a, b, rel_tol=1e-3, abs_tol=0.0):
    assert math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol), f"Mismatch: {a} vs {b}"

assert math.isclose((3*math.pi/4)*180/math.pi,135)
examples = {}

# Example 32.3: Energy in a nonsinusoidal wave
E_32_3 = 100.0  # V/m
B_32_3 = E_32_3 / c
u_32_3 = eps0 * E_32_3**2
S_32_3 = (E_32_3 * B_32_3) / mu0
S_32_3_alt = eps0 * c * E_32_3**2

close(B_32_3, 3.33e-7, rel_tol=1e-2)
close(u_32_3, 8.85e-8, rel_tol=1e-3)
close(S_32_3, 26.5, rel_tol=1e-2)
close(S_32_3_alt, 26.5, rel_tol=1e-2)

examples['32.3'] = {
    'E_V_per_m': E_32_3,
    'B_Tesla': B_32_3,
    'u_J_per_m3': u_32_3,
    'S_W_per_m2': S_32_3,
    'S_alt_W_per_m2': S_32_3_alt
}

# Example 32.4: Energy in a sinusoidal wave
P_32_4 = 50.0e3  # W (50 kW)
R_32_4 = 100.0e3 # m (100 km)
A_hemi = 2 * math.pi * R_32_4**2
I_32_4 = P_32_4 / A_hemi
Emax_32_4 = math.sqrt(2 * mu0 * c * I_32_4)
Bmax_32_4 = Emax_32_4 / c

close(A_hemi, 6.28e10, rel_tol=1e-2)
close(I_32_4, 7.96e-7, rel_tol=1e-2)
close(Emax_32_4, 2.45e-2, rel_tol=1e-2)
close(Bmax_32_4, 8.17e-11, rel_tol=1e-2)

examples['32.4'] = {
    'P_W': P_32_4,
    'R_m': R_32_4,
    'A_hemisphere_m2': A_hemi,
    'I_W_per_m2': I_32_4,
    'Emax_V_per_m': Emax_32_4,
    'Bmax_Tesla': Bmax_32_4
}

# Example 32.5: Power and pressure from sunlight
I_32_5 = 1.4e3   # W/m^2
A_32_5 = 4.0     # m^2
P_32_5 = I_32_5 * A_32_5
prad_abs_32_5 = I_32_5 / c
F_abs_32_5 = prad_abs_32_5 * A_32_5
prad_ref_32_5 = 2 * I_32_5 / c

close(P_32_5, 5.6e3, rel_tol=1e-3)
close(prad_abs_32_5, 4.7e-6, rel_tol=0.02)
# The textbook uses rounded prad = 4.7e-6 Pa to compute F = 4.7e-6 * 4.0 = 1.88e-5 N ~ 1.9e-5 N
F_rounded = 4.7e-6 * A_32_5
close(F_rounded, 1.9e-5, rel_tol=0.02)
close(F_abs_32_5, 1.9e-5, rel_tol=0.02)
close(prad_ref_32_5, 9.4e-6, rel_tol=0.02)

examples['32.5'] = {
    'I_W_per_m2': I_32_5,
    'A_m2': A_32_5,
    'P_absorbed_W': P_32_5,
    'prad_absorbed_Pa': prad_abs_32_5,
    'F_absorbed_N': F_abs_32_5,
    'prad_reflected_Pa': prad_ref_32_5
}

# Example 32.6: Intensity in a standing wave
# S_x(x, t) = (Emax * Bmax / mu0) * sin(2kx) * sin(2wt)
# Time average of vector S over full cycle: <S_x> = 0, so I = |<S>| = 0.
t_samples = np.linspace(0, 2 * math.pi, 100001)
sin_2wt_avg = float(np.trapezoid(np.sin(2 * t_samples), t_samples) / (2 * math.pi))
close(sin_2wt_avg, 0.0, abs_tol=1e-12)

# Average of absolute magnitude: <|sin(2wt)|> = 2/pi ~ 0.6366 > 0
sin_2wt_abs_avg = float(np.trapezoid(np.abs(np.sin(2 * t_samples)), t_samples) / (2 * math.pi))
close(sin_2wt_abs_avg, 2.0 / math.pi, rel_tol=1e-3)
assert sin_2wt_abs_avg > 0.63, "Average magnitude of Poynting flux must be positive"

examples['32.6'] = {
    'sin_2wt_vector_time_average': sin_2wt_avg,
    'intensity_I_magnitude_of_average_vector': 0.0,
    'sin_2wt_magnitude_time_average': sin_2wt_abs_avg,
    'physical_distinction': 'I = |<S>| = 0 (zero net transported energy flux), but <|S_x|> > 0 reflects oscillating energy exchange between electric and magnetic forms without dissipation.'
}

# Example 32.7: Standing waves in a cavity
L_32_7 = 1.50e-2  # 1.50 cm
lambda1_32_7 = 2 * L_32_7
f1_32_7 = c / lambda1_32_7

close(lambda1_32_7, 0.030, rel_tol=1e-4)
close(f1_32_7, 1.00e10, rel_tol=1e-3)

examples['32.7'] = {
    'L_m': L_32_7,
    'lambda1_m': lambda1_32_7,
    'lambda1_cm': lambda1_32_7 * 100,
    'f1_Hz': f1_32_7,
    'f1_GHz': f1_32_7 / 1e9,
    'E_nodes_cm': [0.0, 1.50],
    'E_antinode_cm': [0.75],
    'B_nodes_cm': [0.75],
    'B_antinodes_cm': [0.0, 1.50]
}

# Self-checks verification
positions=np.array([0,.25,.5,.75])
field_squares=np.cos(2*math.pi*positions)**2
assert np.allclose(field_squares,[1,0,1,0],rtol=0,atol=1e-14)
assert np.array_equal(np.flatnonzero(field_squares>.99),[0,2])
assert np.array_equal(np.flatnonzero(field_squares<1e-14),[1,3])
selfchecks = {
    '32.4': {
        'question': 'Values of x for max/min of u and instantaneous S',
        'answers': {
            '(a) energy density maximum': ['(i) x = 0', '(iii) x = lambda/2'],
            '(b) energy density minimum': ['(ii) x = lambda/4', '(iv) x = 3*lambda/4'],
            '(c) instantaneous S magnitude maximum': ['(i) x = 0', '(iii) x = lambda/2'],
            '(d) instantaneous S magnitude minimum': ['(ii) x = lambda/4', '(iv) x = 3*lambda/4']
        }
    },
    '32.5': {
        'question': 'Is energy density zero at all times at any point in cavity?',
        'answer': 'No point has energy identically zero for all times, but energy can equal zero at an individual instant (e.g. at an electric node when B is passing through zero).'
    }
}

# Dense 2D grid for numerical Maxwell derivative assertions and energy density evaluation
k = 2 * math.pi / lambda1_32_7
omega = 2 * math.pi * f1_32_7
Emax_test = 1.0
Bmax_test = Emax_test / c

x_grid = np.linspace(0, L_32_7, 201)
t_period = 1.0 / f1_32_7
t_grid = np.linspace(0, t_period, 201)
X, T = np.meshgrid(x_grid, t_grid, indexing='ij')

# Fields on 2D grid:
# Ey(x, t) = -2 * Emax * sin(kx) * sin(wt)
# Bz(x, t) = -2 * Bmax * cos(kx) * cos(wt)
Ey = -2 * Emax_test * np.sin(k * X) * np.sin(omega * T)
Bz = -2 * Bmax_test * np.cos(k * X) * np.cos(omega * T)

# Exact partial derivatives:
dEy_dx = -2 * k * Emax_test * np.cos(k * X) * np.sin(omega * T)
dBz_dt = 2 * omega * Bmax_test * np.cos(k * X) * np.sin(omega * T)
# Faraday's Law: -dEy/dx = dBz/dt  <=>  -dEy/dx - dBz/dt = 0
faraday_residual = float(np.max(np.abs(-dEy_dx - dBz_dt)))
assert faraday_residual < 1e-12, f"Faraday residual failed: {faraday_residual}"

dBz_dx = 2 * k * Bmax_test * np.sin(k * X) * np.cos(omega * T)
dEy_dt = -2 * omega * Emax_test * np.sin(k * X) * np.cos(omega * T)
# Ampere's Law: -dBz/dx = (1/c^2) * dEy/dt = eps0_exact * mu0 * dEy/dt
ampere_exact_residual = float(np.max(np.abs(-dBz_dx - (1.0 / c**2) * dEy_dt)))
assert ampere_exact_residual < 1e-12, f"Ampere exact residual failed: {ampere_exact_residual}"

# With rounded textbook eps0 = 8.85e-12, relative difference is < 0.1%:
ampere_textbook_residual = float(np.max(np.abs(-dBz_dx - eps0 * mu0 * dEy_dt)))
assert ampere_textbook_residual < 2e-9, f"Ampere textbook residual failed: {ampere_textbook_residual}"

# Wave equation: d^2Ey/dx^2 = (1/c^2) * d^2Ey/dt^2
d2Ey_dx2 = 2 * (k**2) * Emax_test * np.sin(k * X) * np.sin(omega * T)
d2Ey_dt2 = 2 * (omega**2) * Emax_test * np.sin(k * X) * np.sin(omega * T)
wave_eq_exact_residual = float(np.max(np.abs(d2Ey_dx2 - (1.0 / c**2) * d2Ey_dt2)))
wave_eq_relative_residual = wave_eq_exact_residual / float(2 * (k**2) * Emax_test)
assert wave_eq_exact_residual < 1e-9, f"Wave equation residual failed: {wave_eq_exact_residual}"
assert wave_eq_relative_residual < 1e-12, f"Wave equation relative residual failed: {wave_eq_relative_residual}"

wave_eq_textbook_residual = float(np.max(np.abs(d2Ey_dx2 - eps0 * mu0 * d2Ey_dt2)))
wave_eq_textbook_rel_error = wave_eq_textbook_residual / float(2 * (k**2) * Emax_test)
assert wave_eq_textbook_rel_error < 1e-3, f"Wave equation textbook rel error failed: {wave_eq_textbook_rel_error}"

maxwell_numerical_assertions = {
    'faraday_law': {
        'equation': '-dEy/dx = dBz/dt',
        'max_absolute_residual': faraday_residual,
        'assert_passed': bool(faraday_residual < 1e-12)
    },
    'ampere_law': {
        'equation': '-dBz/dx = (1/c^2)*dEy/dt',
        'max_absolute_residual_exact': ampere_exact_residual,
        'max_absolute_residual_rounded_eps0': ampere_textbook_residual,
        'assert_passed': bool(ampere_exact_residual < 1e-12)
    },
    'wave_equation': {
        'equation': 'd^2Ey/dx^2 = (1/c^2)*d^2Ey/dt^2',
        'max_absolute_residual_exact': wave_eq_exact_residual,
        'relative_residual_exact': wave_eq_relative_residual,
        'max_absolute_residual_rounded_eps0': wave_eq_textbook_residual,
        'assert_passed': bool(wave_eq_exact_residual < 1e-9)
    }
}

# Energy density analysis: u(x, t) = 0.5 * eps0 * Ey^2 + 0.5 * (1/mu0) * Bz^2
u_grid = 0.5 * eps0 * (Ey**2) + 0.5 * (1.0 / mu0) * (Bz**2)

# Instantaneous zero check: At x=0 (electric node, Ey=0 for all t),
# Bz(0, t) = -2*Bmax*cos(wt). At wt = pi/2 (t = t_period/4), Bz = 0, so u(0, t) = 0!
t_quarter_idx = 50  # 50/200 = 0.25 of period
u_at_node_E_quarter_t = float(u_grid[0, t_quarter_idx])
close(u_at_node_E_quarter_t, 0.0, abs_tol=1e-12)
assert u_at_node_E_quarter_t < 1e-12, "Energy density at node must equal zero at instant wt = pi/2"

# Non-vanishing over all times check: For each spatial position x, max_t u(x, t) > 0.
max_u_over_time_per_x = np.max(u_grid, axis=1)
min_time_max_u = float(np.min(max_u_over_time_per_x))
assert min_time_max_u > 0.0, "There exists a point with energy identically zero for all times!"

energy_density_report = {
    'instantaneous_energy_can_equal_zero': True,
    'instantaneous_zero_sample': {
        'position': 'x = 0 (electric node, Ey=0 identically)',
        'time': 'wt = pi/2 (t = T/4, where Bz=0 instantaneously)',
        'u_J_per_m3': u_at_node_E_quarter_t
    },
    'point_identically_zero_for_all_times_exists': False,
    'minimum_time_maximum_u_J_per_m3': min_time_max_u,
    'conclusion': 'No point has energy identically zero for all times, but energy can equal zero at an individual instant.'
}

report = {
    'status': 'passed',
    'chapter': 32,
    'section_range': '32.4-32.5',
    'examples': examples,
    'selfchecks': selfchecks,
    'maxwell_numerical_assertions': maxwell_numerical_assertions,
    'energy_density_report': energy_density_report
}

(OUT / 'theory-b-numeric-checks.json').write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + '\n',
    encoding='utf-8'
)

print(json.dumps(report, ensure_ascii=False, indent=2))
