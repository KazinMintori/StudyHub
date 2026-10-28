"""Execute the printed questions and worked solutions of photo paper 049.

Run from the repository root. Needs numpy, pandas, pyarrow and duckdb.
Temporary CSV/Parquet fixtures are isolated from the user's data.
"""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import hashlib
import json
import os
import re
import sys
import tempfile

import duckdb
import numpy as np
import pandas as pd
import pyarrow

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'raw_materials/xu-ly-du-lieu/exam-papers/source.json'
paper = next(e for e in json.loads(SOURCE.read_text(encoding='utf-8'))['exams'] if e['code'] == '049')
FENCE = re.compile(r'^```(python|sql)\n(.*?)^```\s*$', re.M | re.S)
expected_stdout = {9: '[8 5]', 10: '4 6', 12: '60 80', 13: '2 5 2', 14: '(3, 4) 225',
                   15: "['G5', 'G1'] 0", 22: '[1 3]'}
expected_errors = {19: TypeError, 20: AttributeError, 23: pyarrow.ArrowInvalid}
records = []


def execute(code, env):
    output = StringIO()
    with redirect_stdout(output):
        exec(compile(code, '<paper-049>', 'exec'), env)
    return output.getvalue().strip()


prior_cwd = Path.cwd()
with tempfile.TemporaryDirectory(prefix='studyhub-paper-049-') as temp:
    os.chdir(temp)
    sys.path.insert(0, temp)
    try:
        Path('raw').mkdir()
        pd.DataFrame({'trang_thai': ['ban'] * 4 + ['huy'] * 2}).to_csv('raw/ve.csv', index=False)
        Path('kho_cu.csv').write_text('ma\n00101\n103\n', encoding='utf-8')
        Path('kho_moi.csv').write_text('ma\nHN02\n', encoding='utf-8')
        Path('quy_doi.py').write_text('def nghin(x):\n    return x / 1000\n', encoding='utf-8')
        for q in paper['questions']:
            n = q['n']
            env = dict(np=np, pd=pd, duckdb=duckdb)
            if n == 11:
                env['bs'] = pd.Series(['30a-12345', '30A-123456', '130A-12345', '30A-1234'])
            if n == 18:
                env['A'] = np.arange(12).reshape(3, 4)
            if n == 20:
                env.update(bang=pd.DataFrame({'x': [1]}), bang_t10=pd.DataFrame({'x': [2]}))
            if n == 21:
                env['bc'] = pd.DataFrame({
                    'thang': ['2026-01', '2026-02', '2026-03', '2026-03', '2026-04', '2026-04'],
                    'chi_nhanh': ['Q1', 'Q1', 'Q1', 'Q7', 'Q1', 'Q7'],
                    'doanh_thu': [100, 110, 104.5, 200, 209, 190],
                    'kl': ['12 kg', '800 g', None, '0 g', '1250 g', '2 kg'],
                })
            record = dict(id=q['id'], sourceNumber=n,
                          solutionSha256=hashlib.sha256(q['solutionMarkdown'].encode()).hexdigest())
            code = '\n\n'.join(i['text'] for i in q['items'] if i['kind'] == 'code' and i.get('language', 'python') == 'python')
            if n == 17:
                cells = re.split(r'^# Ô \d[^\n]*\n', code, flags=re.M)[1:]
                changed = []
                for i, cell in enumerate(cells, 1):
                    cell_env = dict(bd=pd.DataFrame({'diem': [12, 4, 7]}))
                    execute(cell, cell_env)
                    first = cell_env['bd'].copy(deep=True)
                    execute(cell, cell_env)
                    changed.append(not first.equals(cell_env['bd']))
                assert changed == [False, False, False, True]
                record['changedOnSecondRun'] = changed
            elif code:
                try:
                    stdout = execute(code, env)
                except Exception as error:
                    assert n in expected_errors and isinstance(error, expected_errors[n]), (n, repr(error))
                    record['printedCodeError'] = type(error).__name__
                else:
                    assert n not in expected_errors, (n, 'Expected a printed-code error')
                    if n in expected_stdout:
                        assert stdout == expected_stdout[n], (n, stdout)
                    record['printedCodeStdout'] = stdout
            if n == 11:
                assert env['hop_le'].tolist() == [False, True, False, False]
                record['match'] = env['hop_le'].tolist()
            if n == 16:
                cases = ['import quy_doi.nghin\nprint(nghin(45000))',
                         'import quy_doi\nprint(nghin(45000))',
                         'from quy_doi import nghin\nprint(quy_doi.nghin(45000))']
                errors = []
                for case in cases:
                    try:
                        execute(case, {})
                    except (ImportError, NameError) as error:
                        errors.append(type(error).__name__)
                assert errors == ['ModuleNotFoundError', 'NameError', 'NameError']
                record['invalidImportErrors'] = errors
            if n == 23:
                env['cua_hang'] = pd.DataFrame({'ma': ['A', 'A', 'B'], 'ten': ['A1', 'A2', 'B1'], 'thanh_pho': ['HN', 'HN', 'DN']})
                env['don_hang'] = pd.DataFrame({'ma_don': ['DH1', 'DH2'], 'ma_shop': ['A', 'B'], 'tien': [300, 1500]})
                # Explicit registration avoids scope-dependent replacement scans in this verifier.
                con = duckdb.connect()
                for table in ['cua_hang', 'don_hang']:
                    con.register(table, env[table])
                original_total = con.sql('SELECT SUM(tong) FROM (SELECT thanh_pho, SUM(tien) AS tong FROM don_hang LEFT JOIN cua_hang ON ma_shop = ma GROUP BY thanh_pho)').fetchall()[0][0]
                assert original_total == 2100
            if n == 24:
                assert env['phi_tre'](-2) == -4000
                try:
                    env['phi_tre'](None)
                except TypeError:
                    record['noneError'] = 'TypeError'
                else:
                    raise AssertionError('phi_tre(None) must raise')
            outputs = []
            sql_results = []
            for language, snippet in FENCE.findall(q['solutionMarkdown']):
                if language == 'python':
                    outputs.append(execute(snippet, env))
                else:
                    sql_results.append(con.sql(snippet).fetchall())
            record['solutionStdout'] = outputs
            if n == 10:
                assert outputs == ['4 6']
                assert duckdb.sql("SELECT COUNT(*) FROM read_parquet('ve.parquet')").fetchall()[0][0] == 6
            if n == 16:
                assert outputs == ['45.0']
            if n == 18:
                assert outputs == ['[True, False, True, False]']
            if n == 19:
                assert outputs == ["{'D1': 82.5, 'D2': 60.0}"]
            if n == 20:
                assert env['bang']['x'].tolist() == [1, 2]
            if n == 21:
                np.testing.assert_allclose(env['bc']['kg'], [12, .8, np.nan, 0, 1.25, 2], equal_nan=True)
                np.testing.assert_allclose(env['bc']['tang'], [np.nan, .1, -.05, np.nan, 1, -.05], equal_nan=True)
                record['fixtureKg'] = env['bc']['kg'].fillna('missing').tolist()
                record['fixtureChange'] = env['bc']['tang'].fillna('missing').tolist()
            if n == 22:
                assert outputs == ['[2 3]']
            if n == 23:
                assert pd.read_parquet('kho.parquet')['ma'].tolist() == ['00101', '103', 'HN02']
                assert sql_results == [[('A', 2)], [('DH1', 'A', 300, 2, 300)]]
                record['sqlResults'] = sql_results
                record['preservedCodes'] = pd.read_parquet('kho.parquet')['ma'].tolist()
                con.close()
            if n == 24:
                assert outputs == ['[None, 0, 0, 6000]']
            if n == 25:
                assert outputs == ['69.0 119.0\n57.98%']
                assert np.isclose(env['ty_le'], 69 / 119)
            if n == 26:
                assert outputs == ['[800, 300, 300, 600, 700, 0]', "{'T2': 8.25, 'T3': 7.5}"]
            records.append(record)
            print(f'PASS {q["id"]}')
    finally:
        sys.path.remove(temp)
        os.chdir(prior_cwd)

report = dict(code='049', verifiedQuestions=len(records),
              versions=dict(python=sys.version.split()[0], numpy=np.__version__, pandas=pd.__version__,
                            pyarrow=pyarrow.__version__, duckdb=duckdb.__version__),
              questions=records)
report_file = ROOT / 'raw_materials/xu-ly-du-lieu/exam-papers/verification-049.json'
report_file.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Verified {len(records)} questions, including expected errors and corrected solutions.')
