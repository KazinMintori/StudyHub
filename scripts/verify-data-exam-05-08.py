"""Exact-source assertions for selected questions and all 20 regex items.

Schema coverage is reported separately from executable assertions. No self-key
comparison is counted as evidence that code was executed.
"""
from pathlib import Path
import ast
import contextlib
import importlib.util
import io
import json
import re
import sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'raw_materials/xu-ly-du-lieu/exam'
FENCE = re.compile(r'^```(?:python|py)\s*\n(.*?)^```[ \t]*$', re.M | re.S)
QUESTIONS = {q['id']:q for n in range(5,9) for q in json.loads((DATA/f'banks/bai-{n:02}.json').read_text(encoding='utf-8'))['questions']}
RESULTS = []


def code(text):
    return '\n\n'.join(FENCE.findall(text))


def scope_for(question, answer=False):
    scope = {'re':re,'np':np,'pd':pd,'json':json}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(code(question['promptMarkdown']),scope)
        if answer: exec(code(question['answerMarkdown']),scope)
    return scope


def literal(option):
    text = option['markdown'].strip().strip('`')
    try: return ast.literal_eval(text)
    except (ValueError,SyntaxError): return text


def matched_key(question, value):
    matches = [o['key'] for o in question['options'] if literal(o)==value]
    assert len(matches)==1,(question['id'],value,matches)
    return matches[0]


def log(qid, result, computed_key=None):
    q=QUESTIONS[qid]
    if q['kind']=='quiz': assert computed_key==q['correctKey'],(qid,computed_key,q['correctKey'])
    RESULTS.append({'id':qid,'method':'exact_source_assertion','result':repr(result),'computedKey':computed_key})


def verify_regex():
    essay_cases={
      4:('hop_le',[' Apa','Boc','Dna','AnaX',None],[False,True,False,False,False]),
      6:('hop_le',['aac','ab','aabccc','aa'],[True,False,True,False]),
      8:('hop_le',['7.abc','7.\tabc','7.\nabc','7. abc ',None],[False,True,True,False,False]),
      10:('lay_so',['bedrooms only','A 0BR','Modern 2BR2BA','Home 2 bedroom'],[None,'0',None,'2']),
      12:('hop_le',['12,345e-2','12,34e2','1E+','+001.5',None],[True,False,False,True,False]),
      14:('ten_goc',['Lan.01+lab@data-site.edu.vn','a..b@site.vn','a+@site.vn',None],['Lan.01',None,None,None]),
      16:('lay_anh',['scene.02-night.png','a..jpg','a.JPG',None,'a.jpg.tmp'],[('scene.02-night','png'),None,None,None,None]),
      17:('cat_dau_cuoi',['  A  B\t',' \t','',None,'\u00a0X\u00a0'],['A  B','','',None,'\u00a0X\u00a0'])
    }
    for number in range(1,21):
        qid=f'B7-R{number:02}';q=QUESTIONS[qid]
        if number in essay_cases:
            function,inputs,expected=essay_cases[number]
            scope=scope_for(q,answer=True);actual=[scope[function](v) for v in inputs]
            assert actual==expected,(qid,actual,expected)
            log(qid,actual);continue
        if number in (1,9):
            accepted=[]
            for choice in q['options']:
                body=code(q['promptMarkdown'])
                if number==1:
                    body=body.replace('# return ...',choice['markdown'].strip('`'))
                    source=body;name='lay_ma';inputs=[None,'A000 B7','none'];expected=[None,'000',None]
                else:
                    source='def candidate(text):\n'+ '\n'.join('    '+line for line in body.splitlines())+'\n    '+choice['markdown'].strip('`')
                    name='candidate';inputs=[None,'fileB_08.pdf','file.pdf','fileB_08.PDF'];expected=[None,'fileB_08',None,None]
                try:
                    scope={'re':re};exec(source,scope);actual=[scope[name](v) for v in inputs]
                    if actual==expected:accepted.append(choice['key'])
                except (IndexError,TypeError): pass
            assert len(accepted)==1,(qid,accepted)
            log(qid,expected,accepted[0]);continue
        if number==2:
            xs=['  A.','?=+.','abc.','abcd','abc','ab\n.','é你A.'];expected=[True,True,True,False,False,False,True]
            accepted=[o['key'] for o in q['options'] if [re.fullmatch(literal(o),v) is not None for v in xs]==expected]
            assert len(accepted)==1;log(qid,expected,accepted[0]);continue
        if number==3:
            bad=[o['key'] for o in q['options'] if (re.fullmatch(r'c|m|fan',o['markdown']) is not None)!=(o['markdown'] in {'can','man','fan'})]
            assert len(bad)==1;log(qid,'can is wrongly rejected',bad[0]);continue
        if number==13:
            xs=['305-555-1234','(305)-555-1234','1 (305) 555-1234','(305-555-1234','305)-555-1234','+1 305 555 1234']
            expected=[True,True,True,False,False,False];accepted=[]
            for o in q['options']:
                scope={'AREA':literal(o)};exec(code(q['promptMarkdown']),scope)
                if [re.fullmatch(scope['p'],v) is not None for v in xs]==expected:accepted.append(o['key'])
            assert len(accepted)==1;log(qid,expected,accepted[0]);continue
        scope=scope_for(q)
        if number in (5,7):actual=[re.fullmatch(scope['p'],v) is not None for v in scope['xs']]
        elif number==11:actual=[i for i,v in enumerate(scope['xs']) if re.fullmatch(scope['p'],v)]
        elif number==15:
            text=re.sub(r'<!--[\s\S]*?-->','',scope['text']);actual=re.search(scope['p'],text).group(1)
            assert actual=='my-card'
        elif number==18:actual=scope['r']
        elif number==19:actual=re.fullmatch(scope['p'],scope['text']).groups()
        elif number==20:
            actual=[]
            for value in scope['xs']:
                match=re.fullmatch(scope['p'],value) if value is not None else None
                actual.append((match.group(1) or '/') if match else None)
        else:raise AssertionError(qid)
        log(qid,actual,matched_key(q,actual))


def verify_five_regressions():
    spec=importlib.util.spec_from_file_location('exam_execution',ROOT/'scripts/verify-data-exam-code.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    cases={'B6-016':('ValueError','B'),'B6-036':('ValueError','C'),'B7-014':('TypeError','B')}
    for qid,(error,key) in cases.items():
        record=module.execute(QUESTIONS[qid]);errors=[b.get('errorType') for b in record['blocks'] if b['status']=='raised']
        assert errors==[error],(qid,record)
        choices=[o['key'] for o in QUESTIONS[qid]['options'] if error in o['markdown']]
        assert choices==[key];log(qid,error,choices[0])
    for qid,expected,value in [('B6-031','True 0','D'),('B8-007',"['R3']",'D')]:
        record=module.execute(QUESTIONS[qid]);actual='\n'.join(b['stdout'].strip() for b in record['blocks']).strip()
        assert actual==expected,(qid,record);log(qid,actual,value)


def main():
    assert len(QUESTIONS)==296
    for n in range(5,9):
        reviews=json.loads((DATA/f'reviews/bai-{n:02}.json').read_text(encoding='utf-8'))['items']
        expected={qid for qid in QUESTIONS if qid.startswith(f'B{n}-')}
        assert len(reviews)==len(expected) and {item['id'] for item in reviews}==expected
        for item in reviews:
            assert item['verification']['method'] and item['verification']['evidence']
            assert set(item['optionExplanations'])==(set('ABCD') if QUESTIONS[item['id']]['kind']=='quiz' else set())
    verify_regex();verify_five_regressions()
    assert len(RESULTS)==25 and len({r['id'] for r in RESULTS})==25
    out=ROOT/'qa/data-exam';out.mkdir(parents=True,exist_ok=True)
    report={'reviewSchemaCount':296,'exactQuestionAssertions':25,'regexQuestions':20,'results':RESULTS,
      'limitation':'Only the 25 listed questions are asserted by this suite. Remaining question execution evidence is produced separately by verify-data-exam-code.py; schema coverage is not a correctness proof.'}
    (out/'exact-verification-05-08.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS 296 review records; 25 exact-source question assertions, including all 20 regex items. No self-key comparisons counted.')

if __name__=='__main__':main()
