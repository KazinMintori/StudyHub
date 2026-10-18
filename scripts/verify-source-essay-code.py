"""Run supplied essay solution snippets after their exact question setup.

Results include intentional errors, incomplete fragments and simulated fixtures.
This is execution evidence rather than an automatic grading of every essay.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import importlib.util,json,re
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('exam_code',ROOT/'scripts/verify-data-exam-code.py')
MODULE=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(MODULE)

def run(question):
    original=question['promptMarkdown']
    if question['id']=='B8-057':
        # The requested repair replaces the two faulty lines in the original
        # program. It must not reparse dates already converted incorrectly.
        original=re.sub(r'^df\["date"\] = pd\.to_datetime\(df\["date"\]\)\s*$','',original,flags=re.M)
        original=re.sub(r'^m = .*?resample\("M"\)\.size\(\)\s*$','',original,flags=re.M)
    if question['id']=='B8-MR10':
        original += '\n\n```python\nlich = pd.date_range("2027-01-01", "2027-01-02", tz="Asia/Ho_Chi_Minh", freq="D")\n```\n'
    count=len([m for m in MODULE.FENCE.finditer(original) if m[1].strip() in {'python','py'}])
    combined={**question,'promptMarkdown':original+'\n\n'+question['answerMarkdown']}
    row=MODULE.execute(combined)
    row['promptBlockCount']=count
    row['solutionBlockCount']=len([m for m in MODULE.FENCE.finditer(question['answerMarkdown']) if m[1].strip() in {'python','py'}])
    return row

if __name__=='__main__':
    questions=[q for p in sorted((ROOT/'raw_materials/xu-ly-du-lieu/exam/banks').glob('*.json')) for q in json.loads(p.read_text(encoding='utf-8'))['questions'] if q['kind']=='essay']
    with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(run,questions))
    target=ROOT/'qa/data-exam/source-essay-execution.json'
    target.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    errors=[{'id':r['id'],'errors':[{'type':b.get('errorType'),'message':b.get('error')} for b in r['blocks'][r['promptBlockCount']:] if b['status']=='raised']} for r in rows if any(b['status']=='raised' for b in r['blocks'][r['promptBlockCount']:])]
    unexpected=[row for row in errors if row['id'] not in {'B6-018','B6-040'} or any(error['type']!='HTTPError' for error in row['errors'])]
    summary={'essays':len(rows),'withSuppliedSolutionCode':sum(r['solutionBlockCount']>0 for r in rows),
      'withExecutedSolutionCode':sum(r['solutionBlockCount']>0 and len(r['blocks'])>r['promptBlockCount'] for r in rows),
      'expectedErrorQuestions':[row['id'] for row in errors if row not in unexpected], 'unexpectedSolutionErrors':unexpected}
    (target.parent/'source-essay-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    assert not unexpected, 'Inspect source-essay-execution.json for unexpected solution errors'
