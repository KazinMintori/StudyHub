"""Independent exact/numerical checks for the lecture simulations; no downloads."""
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]


def solve(matrix, rhs):
    a = [list(map(F, row)) + [F(v)] for row, v in zip(matrix, rhs)]
    for col in range(len(a)):
        pivot = next(i for i in range(col, len(a)) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        a[col] = [x / scale for x in a[col]]
        for i in range(len(a)):
            if i != col:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[col])]
    return [row[-1] for row in a]


def stationary(graph, teleport, beta=F(4, 5)):
    n = len(graph)
    transition = [[F(int(i in graph[j]), len(graph[j])) if graph[j] else F(1, n)
                   for j in range(n)] for i in range(n)]
    matrix = [[F(i == j) - beta * transition[i][j] for j in range(n)] for i in range(n)]
    return solve(matrix, [(1 - beta) * v for v in teleport])


graph = [[1, 2, 3], [0, 3], [0], [1, 2]]
uniform = stationary(graph, [F(1, 4)] * 4)
topic_a = stationary(graph, [1, 0, 0, 0])
topic_c = stationary(graph, [0, 0, 1, 0])
trusted_bd = stationary(graph, [0, F(1, 2), 0, F(1, 2)])
spam = [(r - t) / r for r, t in zip(uniform, trusted_bd)]
assert sum(uniform) == sum(topic_a) == sum(topic_c) == 1
assert any(s < 0 for s in spam)

js = """import {pageGraph,personalizedRank,candidateProbability} from './src/features/labs/services/data-algorithms.mjs';
console.log(JSON.stringify({uniform:personalizedRank(pageGraph,[.25,.25,.25,.25],.8,250).rank,
topicA:personalizedRank(pageGraph,[1,0,0,0],.8,250).rank,
topicC:personalizedRank(pageGraph,[0,0,1,0],.8,250).rank,
probability:candidateProbability(.8,20,5)}));"""
actual = json.loads(subprocess.check_output(['node', '--input-type=module', '-e', js], cwd=ROOT, text=True))
for key, exact in [('uniform', uniform), ('topicA', topic_a), ('topicC', topic_c)]:
    assert max(abs(x - float(y)) for x, y in zip(actual[key], exact)) < 1e-12

a, b = set('abcd'), set('bcde')
orders = list(itertools.permutations(sorted(a | b)))
collision_count = sum(next(x for x in p if x in a) == next(x for x in p if x in b) for p in orders)
assert F(collision_count, len(orders)) == F(3, 5)
assert len(set('ababa'[i:i + 2] for i in range(4))) == 2
assert 20 * 5 == 10 * 10 == 100
# Exact counterexample: an affine family can be collision-free yet not minwise.
affine_a, affine_b = {0, 1}, {1, 2}
affine_matches = [(a, b) for a in range(1, 5) for b in range(5)
                  if min((a*x+b) % 5 for x in affine_a) == min((a*x+b) % 5 for x in affine_b)]
assert affine_matches == [(1, 4), (2, 3), (2, 4), (3, 2), (3, 3), (4, 1)]
assert F(len(affine_matches), 20) == F(3, 10) != F(1, 3)
assert F(1, 1) / (1-F(17, 20)*F(1, 2)) == F(40, 23)
assert F(1, 1) / (1-F(17, 20)) == F(20, 3)
q, beta = F(3, 200000), F(17, 20)
farm = (F(1, 10000) + (1+beta*100)*q) / (1-beta**2)
assert farm == F(139, 27750)
assert F(1, 10000) / (1-beta**2) == F(1, 2775)
assert (1+beta*100)*q / (1-beta**2) == F(43, 9250)
assert 1-F(139, 100000)/farm == F(289, 400)
and_or = [1-(1-p**4)**8 for p in [F(4, 5), F(2, 5)]]
or_and = [(1-(1-p)**8)**4 for p in [F(4, 5), F(2, 5)]]
assert [round(float(x), 6) for x in and_or] == [0.985237, 0.187360]
assert [round(float(x), 6) for x in or_and] == [0.999990, 0.934489]
p = 1 - (1 - F(4, 5)**5)**20
assert abs(actual['probability'] - float(p)) < 1e-14
half = (1 - 2**(-1 / 20))**(1 / 5)
assert abs(1 - (1 - half**5)**20 - .5) < 1e-12

# A direct authority/hub example has exact dominant squared singular value 3.
# L = [[0,1,1],[0,0,1],[0,1,0]], so equal authority at B,C and hub ratio 2:1:1.
L = [[0, 1, 1], [0, 0, 1], [0, 1, 0]]
authority = [0, 1 / math.sqrt(2), 1 / math.sqrt(2)]
hub = [2 / math.sqrt(6), 1 / math.sqrt(6), 1 / math.sqrt(6)]
La = [sum(x * y for x, y in zip(row, authority)) for row in L]
Lth = [sum(L[i][j] * hub[i] for i in range(3)) for j in range(3)]
assert all(abs(x - math.sqrt(3) * y) < 1e-12 for x, y in zip(La, hub))
assert all(abs(x - math.sqrt(3) * y) < 1e-12 for x, y in zip(Lth, authority))

report = {
    'status': 'passed', 'method': 'Fraction Gaussian elimination, exhaustive permutations and cross-language numerical comparisons',
    'pagerank_uniform': list(map(str, uniform)), 'pagerank_topic_A': list(map(str, topic_a)),
    'pagerank_topic_C': list(map(str, topic_c)), 'trust_BD': list(map(str, trusted_bd)),
    'spam_mass': list(map(str, spam)), 'minhash': {'collisions': collision_count, 'permutations': len(orders), 'jaccard': '3/5'},
    'lsh_b20_r5_s08': float(p), 'lsh_half_height': half, 'lsh_heuristic': 20**(-1 / 5),
    'hits_hub': hub, 'hits_authority': authority,
    'affine_minwise_counterexample': {'matching_parameters': affine_matches, 'collision_probability': '3/10', 'jaccard': '1/3'},
    'farm_score': str(farm), 'farm_reduction': '289/400',
    'and_or': list(map(float, and_or)), 'or_and': list(map(float, or_and)),
    'source_files': ['Foundations_of_Data_Science.pdf', 'Book_3._Mining-of-Massive-Datasets.pdf']
}
output = ROOT / 'qa/data-algorithms-04-06'
output.mkdir(parents=True, exist_ok=True)
(output / 'independent-math.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
