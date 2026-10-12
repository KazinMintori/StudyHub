"""Private source inventory and independent calculation entry point for Ch24."""
from pathlib import Path
import contextlib
import io
import json
import math
import re
import runpy

root = Path(__file__).resolve().parents[2]
raw = root / 'raw_materials/physics/translations/chapter-24'
out = root / 'qa/physics/chapter24'
out.mkdir(parents=True, exist_ok=True)
scripts = [
 'raw_materials/physics/verify_chapter24_theory.py',
 'raw_materials/physics/verify_chapter24_guided.py',
 'raw_materials/physics/verify_chapter24_discussion.py',
 'raw_materials/physics/verify_chapter24_exercises.py',
 'scripts/verify_chapter24_40_55.py',
 'scripts/verify_chapter24_56_68.py',
 'scripts/verify_chapter24_69_76.py',
]
for script in scripts:
    log = io.StringIO()
    with contextlib.redirect_stdout(log):
        runpy.run_path(str(root / script), run_name='__main__')
    (out / (Path(script).stem + '.log')).write_text(log.getvalue(), encoding='utf8')

files = sorted(raw.glob('*.md'))
source = '\n'.join(p.read_text(encoding='utf8') for p in files if 8 <= int(p.name[:2]) <= 14)
exercise_ids = list(map(int, re.findall(r'^::: exercise 24\.(\d+)\b', source, re.M)))
discussion_ids = list(map(int, re.findall(r'^::: exercise Q24\.(\d+)\b', source, re.M)))
variation_ids = re.findall(r'^::: exercise (VP24\.\d+\.\d+)\b', source, re.M)
assert exercise_ids == list(range(1, 77)), exercise_ids
assert discussion_ids == list(range(1, 22)), discussion_ids
assert len(set(variation_ids)) == len(variation_ids) == 12
assert len(re.findall(r'^::: exercise Bài tổng hợp 24', source, re.M)) == 1
solutions = re.findall(r'^::: (?:solution|details)[^\n]*\n([\s\S]*?)^:::', source, re.M)
assert len(solutions) == 110, len(solutions)
for i, body in enumerate(solutions):
    assert '**Tóm tắt đề bài:**' in body, i
    assert re.search(r'\*\*Hướng đi:\*\*\s*\n\s*- ', body), i
    assert body.index('**Tóm tắt đề bài:**') < body.index('**Hướng đi:**'), i

# New Wiki examples and answer-table values, using SI rather than rounded inputs.
eps = 8.8541878128e-12
assert math.isclose(100e-9 * 12, 1.2e-6)
assert math.isclose(.5 * 100e-9 * 12**2, 7.2e-6)
assert math.isclose(12 / 3, 4)
assert math.isclose(3 * eps * 1e12, 26.5625634384)
assert math.isclose(.5 * eps * 1e5**2, .044270939064)
assert math.isclose(20e6 * 1e-3, 20e3)
assert math.isclose(.5 * 21e-6 * 10.8**2, 1.22472e-3)
report = {
 'status': 'passed', 'chapter': 24, 'exercises': 76,
 'discussionQuestions': 21, 'variationProblems': 12,
 'bridgingProblems': 1, 'detailedSolutions': 110,
 'numericScripts': scripts, 'wikiExampleChecks': 7,
 'sourceReview': [
  'raw_materials/physics/reviews/ch24-01-39.md',
  'raw_materials/physics/reviews/ch24-40-55.md',
  'raw_materials/physics/reviews/ch24-56-68.md',
  'raw_materials/physics/reviews/ch24-69-76.md',
  'raw_materials/physics/reviews/ch24-cross-review.md',
 ],
}
(out / 'numeric-checks.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
print('Passed seven calculation suites, 110 solution structures and seven new Wiki/answer checks.')
