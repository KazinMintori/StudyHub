"""Record isolated execution of the supplied question code, without network access.

This is evidence, not an automatic claim that a multiple-choice key is correct.
Intentional errors and scenario-dependent snippets remain visible in the report.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import ast
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
FENCE = re.compile(r'^```([^\r\n]*)\r?\n(.*?)^```[ \t]*$', re.M | re.S)


def compact(text):
    return re.sub(r'\s+', '', re.sub(r'[*`]', '', text)).strip('.').casefold()


RUNNER = '''import json, sys, ast, io, contextlib, warnings, socket, types
from pathlib import Path
import numpy as np
import pandas as pd
import re
from io import StringIO
try:
 import duckdb
except ImportError:
 duckdb = None
import requests
def no_network(*args, **kwargs):
 raise RuntimeError("Network is disabled during question verification")
socket.create_connection = no_network
socket.socket.connect = no_network
payload = json.loads(Path("question.json").read_text(encoding="utf-8"))
scope = {"np": np, "pd": pd, "re": re, "json": json, "StringIO": StringIO,
         "Path": Path, "duckdb": duckdb, "requests": requests, "__name__": "__question__"}
if payload.get("setup"):
 exec(payload["setup"], scope)
rows = []
for index, code in enumerate(payload["blocks"]):
 out, err = io.StringIO(), io.StringIO()
 record = {"block": index + 1}
 try:
  tree = ast.parse(code)
  # Mimic the documented notebook display of the final expression.
  if tree.body and isinstance(tree.body[-1], ast.Expr):
   last = tree.body.pop()
  else:
   last = None
  with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err), warnings.catch_warnings(record=True) as captured:
   warnings.simplefilter("always")
   exec(compile(tree, "<question>", "exec"), scope)
   if last is not None:
    value = eval(compile(ast.Expression(last.value), "<last-expression>", "eval"), scope)
    if value is not None: print(repr(value))
  record.update(status="returned", warnings=[str(w.message) for w in captured])
 except Exception as exc:
  record.update(status="raised", errorType=type(exc).__name__, error=str(exc))
 record.update(stdout=out.getvalue(), stderr=err.getvalue())
 record["variables"] = {name: repr(value)[:1800] for name, value in scope.items()
   if not name.startswith("_") and name not in {"np","pd","re","json","StringIO","Path","duckdb","requests"}
   and not callable(value) and not isinstance(value, (types.ModuleType, type))}
 rows.append(record)
Path("execution.json").write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
'''


def execute(question):
    fences = list(FENCE.finditer(question['promptMarkdown']))
    blocks = [m[2] for m in fences if m[1].strip().casefold() in {'python', 'py'}]
    record = {'id': question['id'], 'sourceKey': question['correctKey'], 'blocks': []}
    if not blocks:
        record['method'] = 'No executable Python fence; requires reasoning or explicit expression check'
        return record
    # A source snippet can describe an API request without supplying an endpoint.
    if any(re.search(r'\b(?:requests\.(?:get|post)|subprocess\.|os\.(?:system|remove|rmdir)|shutil\.rmtree)', b) for b in blocks):
        record['method'] = 'Scenario inspection only; no external side effect executed'
        return record
    files = set()
    setup = ''
    prepared = {}
    identifier = question['id']
    if identifier in {'B7-R09', 'B7-R13', 'B5-035'}:
        record['method'] = 'Template or incomplete function in prompt; requires completing the requested expression before execution'
        return record
    if identifier == 'B2-025':
        prepared['ghi_chu.txt'] = 'cũ'
    if identifier == 'B2-030':
        prepared['cleaning.py'] = blocks[0]
    if identifier == 'B6-007':
        setup = 'r = requests.Response(); r.status_code = 400; r._content = b\'{"error":true,"reason":"invalid parameter"}\''
    if identifier == 'B6-MR01':
        prepared['gia.csv'] = 'gia\n' + '\n'.join(map(str,range(7))) + '\n'
    if identifier == 'B6-021':
        prepared['l.csv'] = 'id,khu,gia,host_id,loai\n' + '\n'.join(f'{i:03d},A,10,H1,R' for i in range(1,7)) + '\n'
    if identifier == 'B6-MR05':
        setup = 'd = pd.DataFrame({"gia": [10.0,20.0,30.0]})'
    if identifier == 'B6-032':
        setup = 'pd.DataFrame({"id":["001","002","003","004"],"gia":[10.0,20.0,np.nan,40.0],"khu":["A"]*4,"host_id":["H1"]*4}).to_parquet("p.parquet",index=False)'
    if identifier == 'B6-048':
        value = ast.literal_eval(ast.parse(blocks[0]).body[0].value)
        setup = 'x = '+repr(value)+'\nr = requests.Response(); r.status_code = 200'
    if identifier == 'B6-051':
        setup = 'pd.DataFrame({"listing_id":["001","001","002","003"]}).to_csv("reviews.csv.gz",index=False,compression="gzip")'
    if identifier in {'B6-018','B6-040'}:
        status = 503 if identifier == 'B6-018' else 400
        setup = f'r = requests.Response(); r.status_code = {status}; r._content = b\'{{"error":true}}\''
    if identifier in {'B6-MR04','B6-MR10'}:
        values = ['10','','','20','40','60',''] if identifier == 'B6-MR04' else ['10','','30','50','','70','110']
        prepared['gia.csv'] = 'gia\n' + '\n'.join('""' if value=='' else value for value in values) + '\n'
    if identifier == 'B6-029':
        prepared['raw/gia.csv'] = 'id,gia\n001,10\n002,20\n003,0\n004,\n'
        setup = 'Path("processed").mkdir(exist_ok=True)'
    if identifier == 'B6-038':
        setup = 'pd.DataFrame({"id":["001","002","003","004"],"price":["$12.00","$20.00","$0.00","$30.00"]}).to_csv("ban_day_du.csv.gz",index=False,compression="gzip")'
    if identifier == 'B6-047':
        setup = 'pd.DataFrame({"listing_id":["001","001","002","003"],"date":["2025-01-01","2025-01-02","2025-01-03","2025-01-04"],"diem":["4","?","5","3"]}).to_csv("reviews.csv.gz",index=False,compression="gzip")'
    if identifier == 'B6-050':
        setup = 'raw_path="weather.json"; meta_path="metadata.json"; downloaded_at="2025-10-18T12:00:00Z"; r=requests.Response(); r.status_code=200; r.url="https://example.invalid/weather"; r._content=json.dumps({"daily":{"time":["2025-01-01","2025-01-02","2025-01-03"]},"daily_units":{},"timezone":"America/Santiago"}).encode()'
    if identifier == 'B6-060':
        setup = 'w_ok = pd.DataFrame({"time":["2025-01-01","2025-01-02","2025-01-03"],"t_c":[30.0,32.0,33.0]})'
    if prepared or setup:
        record['fixtureNote'] = 'Prepared the file/response/state explicitly described in the prompt. Unspecified numeric values in format/shape scenarios use a representative small fixture.'
    for block in blocks:
        try:
            tree = ast.parse(block)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                value = node.args[0].value
                if value.endswith(('.csv', '.txt', '.json', '.jsonl', '.parquet')):
                    if Path(value).is_absolute() or re.match(r'^[A-Z]:', value):
                        record['method'] = 'Path scenario; absolute source path is not executed'
                        return record
                    files.add(value)
    with tempfile.TemporaryDirectory(prefix='studyhub-exam-') as folder:
        folder = Path(folder)
        for name, content in prepared.items():
            target = (folder/name).resolve()
            if not target.is_relative_to(folder.resolve()): raise ValueError('Fixture must remain inside temporary directory')
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding='utf-8', newline='')
        for name in files:
            target = (folder/name).resolve()
            if not target.is_relative_to(folder.resolve()):
                record['method'] = 'Path scenario; traversal outside temporary working directory is not executed'
                return record
            target.parent.mkdir(parents=True, exist_ok=True)
            extension = Path(name).suffix.removeprefix('.')
            data = [m[2] for m in fences if m[1].strip().casefold() in {extension, 'jsonl' if extension=='json' else extension}]
            if len(data) == 1:
                target.write_text(data[0], encoding='utf-8', newline='')
            elif name == 'note.txt' and 'Dữ liệu' in question['promptMarkdown']:
                target.write_text('Dữ liệu', encoding='utf-8')
        (folder/'question.json').write_text(json.dumps({'blocks': blocks, 'setup': setup}, ensure_ascii=False), encoding='utf-8')
        (folder/'run.py').write_text(RUNNER, encoding='utf-8', newline='')
        try:
            run = subprocess.run([sys.executable, str(folder/'run.py')], cwd=folder,
                env={**os.environ, 'PYTHONIOENCODING': 'utf-8', 'MPLBACKEND': 'Agg'},
                capture_output=True, text=True, encoding='utf-8', timeout=40)
        except subprocess.TimeoutExpired:
            record['method'] = 'Timed out; requires individual review'
            return record
        if not (folder/'execution.json').exists():
            record.update(method='Runner failure', runnerError=run.stderr[-1500:])
            return record
        record['method'] = 'Executed prompt fences in a fresh process and temporary folder'
        record['blocks'] = json.loads((folder/'execution.json').read_text(encoding='utf-8'))
        stdout = '\n'.join(b['stdout'].strip() for b in record['blocks']).strip()
        candidates = [choice['key'] for choice in question['options'] if stdout and compact(choice['markdown']) == compact(stdout)]
        if len(candidates) == 1:
            record['matchingOutputKey'] = candidates[0]
            record['matchesSourceKey'] = candidates[0] == question['correctKey']
        return record


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--jobs', type=int, default=3, choices=range(1,5))
    parser.add_argument('--lesson', action='append')
    parser.add_argument('--id', action='append')
    args = parser.parse_args()
    selected = [q for p in sorted((ROOT/'raw_materials/xu-ly-du-lieu/exam/banks').glob('bai-*.json'))
                if not args.lesson or p.stem.removeprefix('bai-') in args.lesson
                for q in json.loads(p.read_text(encoding='utf-8'))['questions'] if not args.id or q['id'] in args.id]
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        rows = list(pool.map(execute, selected))
    directory = ROOT/'qa/data-exam'
    directory.mkdir(parents=True, exist_ok=True)
    suffix = '-'.join(args.id or args.lesson or ['all'])
    (directory/f'code-execution-{suffix}.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
    summary = {'questions': len(rows), 'withExecutedCode': sum(bool(r['blocks']) for r in rows),
               'literalOutputMatches': sum(r.get('matchesSourceKey') is True for r in rows),
               'literalOutputKeyDifferences': [r['id'] for r in rows if r.get('matchesSourceKey') is False],
               'raisedCodeBlocks': sum(b['status']=='raised' for r in rows for b in r['blocks'])}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    assert not summary['literalOutputKeyDifferences'], summary
