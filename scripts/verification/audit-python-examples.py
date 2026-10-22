"""Syntax-check Python examples without importing or executing their contents."""
import ast
import json
import sys
from pathlib import Path

directory = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('qa/markdown-audit')
fences = json.loads((directory / 'code-fences.json').read_text(encoding='utf-8'))
checked = 0
issues = []
for block in fences:
    if block['language'] not in ('python', 'py'):
        continue
    checked += 1
    try:
        ast.parse(block['code'])
    except SyntaxError as error:
        issues.append({'file': block['file'], 'line': block['line'] + (error.lineno or 1) - 1,
                       'message': error.msg, 'sample': error.text})
report = {'checked': checked, 'issues': issues}
(directory / 'python-examples.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
sys.exit(bool(issues))
