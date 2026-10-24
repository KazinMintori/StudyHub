"""Read-only source-review checks, including alternative numerical algorithms."""
from pathlib import Path
import hashlib, json, math, re, subprocess, sys
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq, minimize_scalar

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / 'raw_materials/physics/translations/chapter-06/parent-12-bai-tap-050-097.md'
G = 9.8
canonical = json.loads(subprocess.check_output([sys.executable, '-I', '-X', 'utf8', str(ROOT / 'raw_materials/physics/verify_chapter06_parent_late.py')], cwd=ROOT))
assert canonical['status'] == 'passed' and len(canonical['records']) == 48
records = canonical['records']
checked = {}

def close(problem, field, value, *, rel=1e-8, absolute=1e-8):
    expected = records[problem][field]
    assert math.isclose(value, expected, rel_tol=rel, abs_tol=absolute), (problem, field, value, expected)
    checked.setdefault(problem, {})[field] = float(value)

# Integrate instantaneous friction power in time rather than just W/t.
stop = 8 / (.2 * G)
power_integral = quad(lambda t: -(.2 * 20 * G) * (8 - .2 * G * t), 0, stop)[0]
close('6.50', 'average_power_W', power_integral / stop)

# Direct quadrature cross-checks of changing forces.
close('6.58', 'work_J', quad(lambda x: -(20 + 3 * x), 0, 6.9)[0])
close('6.66', 'work_J', quad(lambda x: -12 + .3 * x * x, 0, 5)[0])

def at_five(t, state):
    return state[0] - 5
at_five.terminal = True
at_five.direction = 1
def turning(t, state):
    return state[1]
turning.direction = 1
trajectory = solve_ivp(lambda t, q: [q[1], (-12 + .3 * q[0] ** 2) / 5], (0, 30), [0, -6], events=[at_five, turning], max_step=.01, rtol=1e-10, atol=1e-12)
assert len(trajectory.y_events[0]) == len(trajectory.y_events[1]) == 1
close('6.66', 'speed_m_s', trajectory.y_events[0][0][1], rel=1e-7)
close('6.66', 'left_turn_m', trajectory.y_events[1][0][0], rel=1e-7)
checked['6.66']['method'] = 'Direct Newton ODE with initial negative velocity and two events'

distance = brentq(lambda x: G * quad(lambda u: .1 + .04 * u, 0, x)[0] - 4.5 ** 2 / 2, 0, 12.5)
close('6.67', 'stop_distance_m', distance)
close('6.68', 'stretch_work_J', quad(lambda x: 100 * x - 700 * x ** 2 + 12000 * x ** 3, 0, .05)[0])
close('6.68', 'compress_work_J', quad(lambda x: 100 * x - 700 * x ** 2 + 12000 * x ** 3, 0, -.05)[0])
spring_k = 530 / .018
close('6.70', 'spring_work_J', quad(lambda x: -spring_k * x, .018, 710 / spring_k)[0])

# Use u=1/r so the repulsive-force work is well conditioned over ten orders.
proton_work = quad(lambda u: -2.12e-26, 1 / 5, 1 / 8e-10)[0]
close('6.72', 'speed_at_8e10m_m_s', math.sqrt(3e5 ** 2 + 2 * proton_work / 1.67e-27))

optimum = minimize_scalar(lambda s: -(quad(lambda x: 400 * (.06 - x) - 6, 0, s)[0]), bounds=(0, .06), method='bounded', options={'xatol': 1e-13})
close('6.76', 'max_speed_distance_m', optimum.x, rel=1e-7)
close('6.76', 'maximum_speed_m_s', math.sqrt(2 * (-optimum.fun) / .03))

# Integrate net tangential force along the circular arc.
arc_work = quad(lambda angle: (.760 - .200 * G * math.sin(angle)) * .600, 0, math.radians(37))[0]
close('6.86', 'final_K_J', arc_work)
close('6.86', 'speed_m_s', math.sqrt(2 * arc_work / .2))
assert all(.200 * (2 * quad(lambda a: (.760 - .200 * G * math.sin(a)) * .600, 0, angle)[0] / .200) / .600 + .200 * G * math.cos(angle) > 0 for angle in np.linspace(0, math.radians(37), 101))
checked['6.86']['ropeTautOverPath'] = True

close('6.88', 'horizontal_path_work_J', quad(lambda x: 2.5 * x * 3, 0, 2)[0])
close('6.88', 'line_y15x_work_J', quad(lambda x: 2.5 * x * (1.5 * x), 0, 2)[0])
close('6.90', 'work0_to04_J', quad(lambda x: 33.55 * x ** .4871, 0, .04, epsabs=1e-12)[0])
close('6.90', 'work04_to08_J', quad(lambda x: 33.55 * x ** .4871, .04, .08, epsabs=1e-12)[0])

# Solve normal equations through lstsq instead of polyfit, retaining the eight rows.
d = np.array([0, .05, .10, .15, .25, .30, .35, .40])
v = np.array([0, .85, 1.11, 1.24, 1.26, 1.14, .90, .36])
A, B, C = np.linalg.lstsq(np.column_stack([d ** 2, d, np.ones_like(d)]), v ** 2, rcond=None)[0]
for field, value in [('fit_A_s2', A), ('fit_B_m_s2', B), ('fit_C_m2_s2', C)]:
    close('6.91', field, value)
checked['6.91']['originalEightRowsRetained'] = True

# Graph-reading uncertainty cannot reverse the ranking (±1 s around each read).
mass = np.array([50.2, 68.2, 81.8, 59.1])
times = np.array([31., 50., 45., 53.])
low, high = mass * G * 16 / (times + 1), mass * G * 16 / (times - 1)
assert low[2] > max(high[[0, 1, 3]])
assert high[3] < min(low[[0, 1, 2]])
checked['6.92'] = {'largest': 'Ricardo', 'smallest': 'Melanie', 'robustForEachTimePlusMinusOneSecond': True}

# Independently integrate the kinetic energy density of the moving spring.
M, L, end_speed = .243, .7, records['6.93']['massive_speed_m_s']
integrated = quad(lambda l: .5 * (end_speed * l / L) ** 2 * M / L, 0, L)[0]
close('6.93', 'final_spring_K_J', integrated)
for field, function in [('max_range_speed_m_s', lambda x: .3 * x * x + 3.5e5 / x ** 2), ('max_endurance_speed_m_s', lambda x: .3 * x ** 3 + 3.5e5 / x)]:
    result = minimize_scalar(function, bounds=(1, 100), method='bounded', options={'xatol': 1e-10})
    close('6.94', field, result.x, rel=1e-6)

text = SOURCE.read_text(encoding='utf-8')
headings = list(re.finditer(r'^### (6\.\d+)\b', text, re.M))
assert [h.group(1) for h in headings] == [f'6.{n}' for n in range(50, 98)]
structure = []
for i, heading in enumerate(headings):
    body = text[heading.end(): headings[i + 1].start() if i + 1 < len(headings) else len(text)]
    assert len(re.findall(r'<details\b', body)) == body.count('</details>') == 1
    assert not re.search(r'<details\b[^>]*\bopen\b', body)
    for label in ['Tóm tắt đề bài:', 'Hướng đi:', 'Lời giải:']:
        assert label in body, (heading.group(1), label)
    structure.append({'id': heading.group(1), 'line': text.count('\n', 0, heading.start()) + 1, 'oneClosedSolutionWithThreeStages': True})

report = {'status': 'passed', 'canonicalNumericRecords': 48, 'alternativeNumericalProblemCount': len(checked), 'alternativeChecks': checked, 'structure': structure, 'sourceSha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(), 'scopeLimit': 'Numeric and structure checks only. Human PDF comparison is recorded separately; no viewport/browser claim.'}
print(json.dumps(report,ensure_ascii=False,indent=2))
