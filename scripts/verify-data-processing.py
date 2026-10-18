"""Check chapter coverage and run the independently calculated course examples.

Does not build the site, fetch data, or require API keys. Optional dependencies
can be supplied through PYTHONPATH without changing the user's Python install.
"""
import ast
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'raw_materials/xu-ly-du-lieu'
NOTES = ROOT / 'docs/xu-ly-du-lieu/bai-giang'


def expand_includes(file, chain=()):
    file = file.resolve()
    assert file not in chain, f'Include cycle: {file}'
    assert file.is_relative_to(ROOT), f'Include outside repository: {file}'
    text = file.read_text(encoding='utf-8-sig')
    return re.sub(r'<!--@include:\s*([^>]+?)\s*-->',
                  lambda match: expand_includes(file.parent / match[1], chain + (file,)), text)


def inspect(entry):
    text = expand_includes(NOTES / (entry['slug'] + '.md'))
    front = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.S)
    assert front, f"Missing metadata: {entry['slug']}"
    assert f"lecture: {entry['slug']}" in front[1]
    title = re.search(r'^title:\s*(.+)$', front[1], re.M)
    assert title and title[1].strip().strip('"\'') == entry['title']
    assert re.findall(r'^## (.+)$', text, re.M)[-1] == 'Tài liệu tham khảo'
    fences = re.findall(r'^```([^\n]*)\n(.*?)^```\s*$', text, re.M | re.S)
    python_blocks = 0
    for number, (language, code) in enumerate(fences, 1):
        if language.strip() != 'python':
            continue
        # Notebook magic belongs in an ipython fence, not a Python program.
        ast.parse(code, filename=f"{entry['slug']}:block{number}")
        python_blocks += 1
    prose = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text[front.end():], flags=re.M | re.S)
    assert not re.search(r'^# ', prose, re.M), 'Duplicate H1'
    assert not re.search(r'colab\.research\.google\.com/[^\s)]*lecture-01', prose)
    # "Chế độ mở tệp" is a legitimate file-I/O term, not a course AI policy.
    banned = r'chế độ\s+đóng\s*/\s*mở|chính sách AI|được dùng AI|không dùng AI|GitHub Classroom|vấn đáp|cơ cấu điểm'
    assert not re.search(banned, prose, re.I), f"Administrative content: {entry['slug']}"
    # A URL may retain the historical slug; prose must not import administration.
    assert not re.search(r'(?<!https://)\b(?:Khoan đã|À không|Thử lại nào|ánh xạ hợp đồng)\b', prose)
    exercises = len(re.findall(r'^::: exercise\b', text, re.M))
    solutions = len(re.findall(r'^::: solution\b', text, re.M))
    assert exercises > 0 and solutions >= exercises, f"Unanswered exercise: {entry['slug']}"
    for line in prose.splitlines():
        if '$$' in line:
            assert line.strip() == '$$', f"Display math delimiter must be on its own line: {entry['slug']}: {line}"
    return {'chapter': entry['chapter'], 'lesson': entry['slug'], 'pythonBlocksParsed': python_blocks,
            'exercises': exercises, 'solutions': solutions}


def main():
    contract = json.loads((SOURCE / 'authoring-contract.json').read_text(encoding='utf-8'))
    expected = [str(i) for i in range(1, 14)] + ['A', 'B']
    assert [entry['chapter'] for entry in contract['lessons']] == expected
    inventory = json.loads((SOURCE / 'source-inventory.json').read_text(encoding='utf-8'))
    assert len([r for r in inventory['records'] if r['source'] == 'wes']) == 15
    assert len([r for r in inventory['records'] if r['source'] == 'iai']) == 13
    assert inventory['unlistedIaiLectures'] == [9]
    assert len(inventory['notebooks']) == 25
    assert not any('/lecture-01.ipynb' in r['url'] for r in inventory['notebooks'])
    for group in 'abc':
        coverage = SOURCE / f'coverage-{group}.json'
        assert coverage.is_file(), f'Missing source traceability: {coverage}'
        json.loads(coverage.read_text(encoding='utf-8-sig'))
        with tempfile.TemporaryDirectory(prefix=f'studyhub-course-{group}-') as directory:
            subprocess.run([sys.executable, str(ROOT / f'scripts/verify-data-course-{group}.py')], cwd=directory, check=True)
    for file in sorted((ROOT / 'scripts').glob('verify-data-practice-*.py')):
        subprocess.run([sys.executable, str(file)], cwd=ROOT, check=True)
    rows = [inspect(entry) for entry in contract['lessons']]
    print(json.dumps({'chapters': len(rows), 'iaiSlideExercisesInventoried': sum(len(r['exercises']) for r in inventory['records']),
                      'linkedNotebooksRead': len(inventory['notebooks']), 'lessons': rows}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    main()
