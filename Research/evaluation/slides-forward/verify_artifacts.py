import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parent
audit_script = Path(r'C:\Users\Ai\Documents\StudyHub\Research\revised\textbook-to-course-slides\scripts\audit_spec.py')
spec_path = root / 'course-spec.json'
spec = json.loads(spec_path.read_text(encoding='utf-8'))
spec['qa_status']['structure'] = 'audit-result-in-audit-result.json'
spec_path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
command = [sys.executable, str(audit_script), str(spec_path), '--asset-root', str(root)]
result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
(root / 'audit-result.json').write_text(result.stdout, encoding='utf-8')
(root / 'audit-command.txt').write_text('Command: ' + subprocess.list2cmdline(command) + '\nExit code: ' + str(result.returncode) + '\nStderr: ' + result.stderr + '\n', encoding='utf-8')

f = lambda x: (x - 3) ** 2
df = lambda x: 2 * (x - 3)
x0 = Fraction(0)
alpha = Fraction(1, 4)
x1 = x0 - alpha * df(x0)
x2 = x1 - alpha * df(x1)
large_step_x1 = x0 - 2 * df(x0)
assert (x1, x2, f(x0), f(x1), f(x2)) == (Fraction(3, 2), Fraction(9, 4), Fraction(9), Fraction(9, 4), Fraction(9, 16))
assert large_step_x1 == 12 and f(large_step_x1) == 81
note = (root / 'study-note.md').read_text(encoding='utf-8')
for n, slide in enumerate(spec['slides'], 1):
    assert f'<a id="slide-{n}"></a>' in note
    assert slide['speaker_notes'] in note
    assert slide['study_text'] in note
    for body in slide['body']:
        if body['type'] in {'text', 'equation'}:
            assert body.get('text', body.get('latex')) in note
        elif body['type'] == 'table':
            for row in body['rows']:
                assert '| ' + ' | '.join(row) + ' |' in note
assert sum(s['estimated_minutes'] for s in spec['slides']) == 12
calculation_report = {
    'method': 'Exact rational arithmetic with Python fractions.Fraction; assertions executed.',
    'values': {'x0': str(x0), 'df_x0': str(df(x0)), 'alpha': str(alpha), 'x1': str(x1), 'df_x1': str(df(x1)), 'x2': str(x2), 'f_x0': str(f(x0)), 'f_x1': str(f(x1)), 'f_x2': str(f(x2)), 'alpha_2_x1': str(large_step_x1), 'alpha_2_f_x1': str(f(large_step_x1))},
    'slide_note_consistency': 'Exact slide text, equations, table, speaker notes and self-study text found in companion; all 8 anchors exist.',
    'core_minutes': 12,
    'render': 'Not performed by evaluation request; layout and glyphs remain unverified.'
}
(root / 'calculation-and-consistency.json').write_text(json.dumps(calculation_report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(result.stdout)
print('Audit exit code:', result.returncode)
print('Exact calculations and companion consistency assertions completed.')
raise SystemExit(result.returncode)
