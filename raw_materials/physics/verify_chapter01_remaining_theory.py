"""Independent source-data checks for the chapter-1 theory proposal.

Run from any cwd. Stdlib only. The source units refer to PDF page numbers,
not zero-based PyMuPDF indices. No site or public source file is modified.
"""
from pathlib import Path
import math
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
FRAGMENTS = HERE / 'translations' / 'chapter-01'
records = []


def close(actual, expected, rel=1e-10, abs_tol=1e-10):
    assert math.isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol), (actual, expected)


def record(unit, pdf_page, data, result):
    records.append({'unit': unit, 'pdf_page': pdf_page,
                    'source_data': data, 'result': result, 'passed': True})


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]


def norm(a):
    return math.sqrt(dot(a, a))


def polar(r, degrees):
    t = math.radians(degrees)
    return [r*math.cos(t), r*math.sin(t)]


# Opening question: speed, duration and angle are read from PDF21.
north = 15 * 2.0 * math.sin(math.radians(37))
close(north, 18.05445069456145)
assert round(north) == 18
record('Opening question', 21, {'km/h': 15, 'h': 2, 'deg_north_of_east': 37},
       {'north_km': north, 'choice': 'iii'})

# All eleven original worked examples; do not use values copied from verifier output.
speed = 763.0 * 1.609 * 1000 / 3600
assert format(speed, '.4g') == '341'
record('Example1.1', 27, {'mi/h': 763.0, 'km/mi': 1.609, 's/h': 3600},
       {'m/s': speed, 'display': '341.0'})

volume = 1.84 * 2.54**3
close(volume, 30.15219776)
assert format(volume, '.3g') == '30.2'
assert format(volume*1e-6, '.3g') == '3.02e-05'
record('Example1.2', 27, {'in3': 1.84, 'cm/in': 2.54},
       {'cm3': volume, 'm3': volume*1e-6})

energy = 9.11e-31 * 299792458**2
close(energy, 8.187659678070528e-14, abs_tol=1e-26)
assert format(energy, '.3g') == '8.19e-14'
record('Example1.3', 29, {'kg': 9.11e-31, 'm/s': 299792458},
       {'J': energy, 'relative_to_1e-19J': energy/1e-19})

mass_approx = 2 * 1e7 / 1000
volume_approx = mass_approx / 1e4
assert mass_approx == 20000 and volume_approx == 2
diamonds = 1e9 / 500000
assert diamonds == 2000 and diamonds/1000 == 2
record('Example1.4', 30, {'USD': 1e9, 'USD/oz_assumed': 1400, 'g/oz_approx': 30,
       'g_per_100USD_approx': 2, 'density_kg/m3_approx': 1e4,
       'diamond_g': 1, 'diamond_carat': 5, 'USD_per_diamond': 500000},
       {'gold_kg_approx': mass_approx, 'gold_m3_approx': volume_approx,
        'diamond_count': diamonds, 'diamond_kg': diamonds/1000})

distance = math.hypot(1, 2)
angle = math.degrees(math.atan2(2, 1))
assert round(distance, 2) == 2.24 and round(angle, 1) == 63.4
record('Example1.5', 33, {'north_km': 1, 'east_km': 2},
       {'km': distance, 'deg_east_of_north': angle})

d = polar(3, -45)
e = polar(4.5, 90-37)
assert [round(x, 1) for x in d] == [2.1, -2.1]
assert [round(x, 2) for x in e] == [2.71, 3.59]
record('Example1.6', 35, {'D_m': 3, 'alpha_deg': 45, 'E_m': 4.5, 'beta_deg': 37},
       {'D_xy_m': d, 'E_xy_m': e})

a, b, c = polar(72.4, 58), polar(57.3, 216), [0, -17.8]
r = [a[i]+b[i]+c[i] for i in range(2)]
r_angle = math.degrees(math.atan2(r[1], r[0]))
assert [round(x, 2) for x in r] == [-7.99, 9.92]
assert round(norm(r), 1) == 12.7 and round(r_angle) == 129
record('Example1.7', [37, 38], {'A_m': 72.4, 'A_deg_east_of_north': 32,
       'B_m': 57.3, 'B_deg_south_of_west': 36, 'C_m_due_south': 17.8},
       {'R_xy_m': r, 'R_m': norm(r), 'theta_deg': r_angle,
        'deg_west_of_north': r_angle-90})

d, e = [6, 3, -1], [4, -5, 8]
f = [2*d[i]-e[i] for i in range(3)]
assert f == [8, 11, -10] and round(norm(f), 1) == 16.9
record('Example1.8', 39, {'D_m': d, 'E_m': e, 'F': '2D-E'},
       {'F_m': f, 'magnitude_m': norm(f)})

a, b = polar(4, 53), polar(5, 130)
geometric = 4 * 5 * math.cos(math.radians(130-53))
close(dot(a, b), geometric)
assert format(geometric, '.3g') == '4.5'
record('Example1.9', 41, {'A': 4, 'A_deg': 53, 'B': 5, 'B_deg': 130},
       {'phi_deg': 77, 'geometric': geometric, 'components': dot(a, b)})

a, b = [2, 3, 1], [-4, 2, -1]
cos_phi = dot(a, b) / (norm(a)*norm(b))
phi = math.degrees(math.acos(cos_phi))
assert dot(a, b) == -3 and round(phi) == 100
record('Example1.10', 41, {'A': a, 'B': b},
       {'dot': dot(a, b), 'A_magnitude': norm(a), 'B_magnitude': norm(b),
        'cos_phi': cos_phi, 'phi_deg': phi})

a, b = [6, 0, 0], [4*math.cos(math.pi/6), 4*math.sin(math.pi/6), 0]
c = cross(a, b)
close(c[2], 12)
close(norm(c), 6*4*math.sin(math.pi/6))
record('Example1.11', 44, {'A': 6, 'B': 4, 'phi_deg': 30}, {'cross': c, 'magnitude': norm(c)})

# Six immediate self-checks. 1.6 and 1.8 are not omitted as non-numerical items.
rho = 1.8/6e-4
close(rho, 3000)
assert format(rho, '.1e') == '3.0e+03'
record('Selfcheck1.5', 29, {'kg': 1.8, 'm3': 6e-4},
       {'density': rho, 'display': '3.0e3 kg/m3', 'choice': 'ii'})
assert 30*10000 == 300000
record('Selfcheck1.6', 30, {'assumed_teeth_per_person': 30, 'assumed_students': 10000},
       {'illustrative_teeth': 300000, 'unique_answer': False})
choices = [9, 7, 5, 1, 0, -1]
possible = [i+1 for i, x in enumerate(choices) if abs(3-4) <= x <= 3+4]
assert possible == [2, 3, 4]
record('Selfcheck1.7', 34, {'S_m': 3, 'T_m': 4, 'candidate_lengths': choices},
       {'allowed_interval_m': [1, 7], 'choices': possible})
a, b = [1, 0], [0, 1]
assert norm(a) == norm(b) and a != b
record('Selfcheck1.8', 38, {'same_norm_counterexample': [a, b]},
       {'a': 'Yes', 'b': 'No: equal components give equal vectors and norms'})
vectors = [[3, 5, -2], [-3, 5, -2], [3, -5, -2], [3, 5, 2]]
assert [dot(a, a) for a in vectors] == [38]*4
record('Selfcheck1.9', 39, {'vectors': vectors}, {'squared_norms': [38]*4, 'ranking': 'all_equal'})
results = {deg: {'dot': 6*math.cos(math.radians(deg)),
                 'cross_magnitude': 6*math.sin(math.radians(deg))} for deg in [0, 90, 180]}
close(results[90]['dot'], 0)
close(results[0]['cross_magnitude'], 0)
close(results[180]['cross_magnitude'], 0)
close(results[0]['dot'], 6)
close(results[180]['dot'], -6)
close(results[90]['cross_magnitude'], 6)
record('Selfcheck1.10', 44, {'A': 2, 'B': 3, 'candidate_degrees': [0, 90, 180]},
       {'table': results, 'choices_a_b_c_d_e': ['ii', 'i/iii', 'i', 'iii', 'ii']})

# Source-data arithmetic outside worked examples, including the corrected Table1.2.
close(1.32578e7*4.11e-3, 54489.558)
assert format(1.32578e7*4.11e-3, '.3g') == '5.45e+04'
close(0.745*2.2/3.885, 0.4218790218790219)
assert round(27.153+138.2-11.74, 1) == 153.6
assert round(3.1416*2.34*0.58, 1) == 4.3
assert round(123.62+8.9, 1) == 132.5
record('Table1.2', 28, {'multiplication_factors': [1.32578e7, 4.11e-3]},
       {'product': 54489.558, 'rounded': 54500, 'other_rows_passed': True})

# Check all nine basis products and their use in both decompositions on a
# deterministic range of nontrivial vectors, including zero/parallel cases.
units = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
for i, u in enumerate(units):
    for j, v in enumerate(units):
        assert dot(u, v) == int(i == j)
        assert dot(cross(u, v), u) == dot(cross(u, v), v) == 0
cases = [[2, 3, 1], [-4, 2, -1], [0, 0, 0], [1, 0, 0], [0.5, -3, 7], [-2, -3, -1]]
for a in cases:
    for b in cases:
        products = [[a[i]*b[j]*dot(units[i], units[j]) for j in range(3)] for i in range(3)]
        assert sum(map(sum, products)) == dot(a, b)
        expanded = [0., 0., 0.]
        for i in range(3):
            for j in range(3):
                uv = cross(units[i], units[j])
                for k in range(3):
                    expanded[k] += a[i]*b[j]*uv[k]
        assert expanded == cross(a, b)
        assert cross(a, b) == [-x for x in cross(b, a)]
record('Equations1.18/1.23', [40, 43], {'basis_products_each': 9, 'vector_pair_cases': 36},
       {'dot_expansion': 'passed', 'cross_expansion': 'passed', 'anticommutation': 'passed'})

# atan branches and c in (0,1), c<0, c=0.
for ax, ay in [(2, 1), (-2, 1), (-2, -2), (2, -1), (0, 3), (0, -3)]:
    if ax:
        alpha = math.degrees(math.atan(ay/ax))
        theta = alpha if ax > 0 else alpha+180
    else:
        theta = 90 if ay > 0 else 270
    close(theta % 360, math.degrees(math.atan2(ay, ax)) % 360)
for scalar in [0.5, -2, 0]:
    a = [3, -4, 2]
    result = [scalar*x for x in a]
    close(norm(result), abs(scalar)*norm(a))
record('Component conditions', [33, 36], {'quadrants_and_axes': 6, 'scalar_values': [0.5, -2, 0]},
       {'passed': True, 'zero_vector_direction': 'undefined'})

# Structural requirements of the staged files, not a claim of integrated QA.
files = [FRAGMENTS/name for name in ['00-mo-dau.md', '01-ban-chat-vat-ly.md', '02-giai-bai-toan.md', '03-chuan-va-don-vi.md', '04-su-dung-doi-don-vi.md', '05-do-bat-dinh-chu-so.md', '06-uoc-luong.md', '07-vector-cong-vector.md', '08-thanh-phan-vector.md', '09-vector-don-vi.md', '10-tich-vector.md', '11-tom-tat.md']]
assert len(files) == 12
texts = {p.name: p.read_text(encoding='utf8') for p in files}
joined = '\n'.join(texts.values())
assert re.findall(r'\(1\.(\d+)\)', joined)
present = {int(x) for x in re.findall(r'\(1\.(\d+)\)', joined) if 1<=int(x)<=25}
assert present == set(range(1, 26)), present
assert len(re.findall(r'^::: exercise Ví dụ 1\.', joined, re.M)) == 11
assert len(re.findall(r'^::: exercise Câu hỏi tự kiểm tra 1\.', joined, re.M)) == 6
assert len(re.findall(r'!\[[^\n]*\]\([^\n]+\.png\)', joined)) == 42
for name, text in texts.items():
    assert not re.search(r'(?m)^\s*\$\$.+|.+\$\$\s*$', text), name
    assert text.count('$$') % 2 == 0, name
    assert not re.search(r'(?<!\\)\\(?:vert|Vert)\{\}', text), name
summary = texts['11-tom-tat.md']
assert 'Hình 1.3' not in summary
assert summary.count('tom-tat-') == 6

result = {'status': 'passed', 'scope': 'Source-data and expansion checks for chapter-1 theory. Browser and source-figure audits are separate gates.',
          'numerical_units': len(records), 'records': records,
          'file_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
print(json.dumps(result, ensure_ascii=False, indent=2))
