"""Execute added solution examples and compare their displayed outputs.

Incomplete fragments, intentionally failing examples and mocked API scenarios
remain in the report for review. They are not silently counted as passing code.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import hashlib
import importlib.util
import json
import re

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'raw_materials/xu-ly-du-lieu/exam'
FENCE=re.compile(r'^```([^\r\n]*)\r?\n(.*?)^```[ \t]*$',re.M|re.S)
SPEC=importlib.util.spec_from_file_location('exam_executor',ROOT/'scripts/verify-data-exam-code.py')
EXECUTOR=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(EXECUTOR)


def normalize(text):
    return '\n'.join(line.rstrip() for line in text.replace('\r\n','\n').strip().splitlines())


def check(item):
    record=EXECUTOR.execute({'id':'example-'+item['id'],'promptMarkdown':item['markdown'],'options':[],'correctKey':None})
    record['id']=item['id']
    fences=list(FENCE.finditer(item['markdown']))
    paired=[];python_index=0
    for i,fence in enumerate(fences):
        if fence[1].strip() not in {'python','py'}:continue
        expected=fences[i+1] if i+1<len(fences) and fences[i+1][1].strip() in {'text','output'} else None
        actual=record['blocks'][python_index] if python_index<len(record['blocks']) else None
        python_index+=1
        if expected is not None:
            paired.append({'block':python_index,'expected':expected[2].strip(),'actual':actual.get('stdout','').strip() if actual else None,
              'match':bool(actual and actual['status']=='returned' and normalize(expected[2])==normalize(actual['stdout']))})
    record.update(markdownSha256=item['hash'],pairedOutputs=paired)
    return record


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--jobs',type=int,default=3,choices=range(1,5));parser.add_argument('--force',action='store_true');parser.add_argument('--strict',action='store_true');args=parser.parse_args()
    target=ROOT/'qa/data-exam/detailed-code-execution.json';target.parent.mkdir(exist_ok=True,parents=True)
    prior=json.loads(target.read_text(encoding='utf-8')) if target.exists() else []
    cache={r['id']:r for r in prior};selected=[];all_ids=[]
    for p in sorted((BASE/'detailed-solutions').glob('bai-*.json')):
        for item in json.loads(p.read_text(encoding='utf-8'))['items']:
            item['hash']=hashlib.sha256(item['markdown'].encode()).hexdigest();all_ids.append(item['id'])
            if args.force or cache.get(item['id'],{}).get('markdownSha256')!=item['hash']:selected.append(item)
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for row in pool.map(check,selected):cache[row['id']]=row
    rows=[cache[qid] for qid in all_ids]
    target.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    summary={'solutions':len(rows),'newlyChecked':len(selected),'withExecutedCode':sum(bool(r['blocks']) for r in rows),
      'pairedOutputs':sum(len(r['pairedOutputs']) for r in rows),
      'outputDifferences':[{'id':r['id'],'pairs':[p for p in r['pairedOutputs'] if not p['match']]} for r in rows if any(not p['match'] for p in r['pairedOutputs'])],
      'raisedBlocks':[{'id':r['id'],'errors':[b.get('errorType') for b in r['blocks'] if b['status']=='raised']} for r in rows if any(b['status']=='raised' for b in r['blocks'])]}
    (target.parent/'detailed-code-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    if args.strict: assert not summary['outputDifferences'], 'Displayed output differs from execution; inspect detailed-code-summary.json'

if __name__=='__main__':main()
