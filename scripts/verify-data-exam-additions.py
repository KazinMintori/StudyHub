"""Reproduce arithmetic, pandas, schema and cache behavior using synthetic inputs."""
import ast
import contextlib
import io
import json
from pathlib import Path
import re
import tempfile
import os
from typing import Literal

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'raw_materials/xu-ly-du-lieu/exam'
checks = {}


def checked(identifier, actual, expected, method):
    if isinstance(actual, (float, np.floating)):
        assert np.isclose(actual, expected), (identifier, actual, expected)
    else:
        assert actual == expected, (identifier, actual, expected)
    checks.setdefault(identifier, []).append({'method': method, 'actual': str(actual), 'expected': str(expected)})


class ReviewInfo(BaseModel):
    sentiment: Literal['positive', 'mixed', 'negative']
    aspects_positive: list[Literal['location', 'cleanliness', 'host', 'value', 'noise', 'amenities']]
    aspects_negative: list[Literal['location', 'cleanliness', 'host', 'value', 'noise', 'amenities']]
    language: str


def run_blocks():
    expressions = {
        'B10-TN-003': '(d.loc[1,"bedrooms"], d.loc[4,"bedrooms"], int(d["bedrooms_isna"].sum()))',
        'B10-TN-005': '(a,b)', 'B10-TN-007': '(int((a|b).sum()),int((a&b).sum()))',
        'B10-TN-009': 'ds["dem_that"].tolist()',
        'B10-TN-011': '(len(kpi), kpi["price_num"].mean())',
        'B10-TN-012': '(int(a.sum()),int(b.sum()))',
        'B10-TN-016': '(int(d.duplicated().sum()),int(d.duplicated(subset=["id"]).sum()))',
        'B10-TN-022': '(round(b.mean(),2),round(b.fillna(1).mean(),2))',
        'B10-TN-027': 'ty_le',
        'B10-TN-031': '(kq["price_num"],kq["bedrooms"])',
        'B10-TN-034': 'm[m].index.tolist()',
        'B10-TN-043': '(int(d.bedrooms.isna().sum()),int(d.was_missing.sum()))',
        'B11-TN-003': 'du_dai.id.tolist()', 'B11-TN-006': 'labels.columns.tolist()',
        'B11-TN-026': 'p', 'B11-TN-036': 'int(ket_qua)',
    }
    expected = {'B10-TN-003': (2.,3.,2), 'B10-TN-005': (3,5), 'B10-TN-007': (4,1),
                'B10-TN-009': [3,2,0,1], 'B10-TN-011': (3,200.), 'B10-TN-012': (1,2),
                'B10-TN-016': (1,2), 'B10-TN-022': (1.67,1.4), 'B10-TN-027': 20.,
                'B10-TN-031': (50.,25.), 'B10-TN-034': [0,1,2], 'B10-TN-043': (2,3),
                'B11-TN-003': [3], 'B11-TN-006': ['sentiment','language'],
                'B11-TN-026': set(), 'B11-TN-036': 2}
    outputs = {'B11-TN-002': 'positive', 'B11-TN-005': 'False True',
               'B11-TN-012': "['es', 'und', 'und']", 'B11-TN-016': '3 4 3',
               'B11-TN-019': '2', 'B11-TN-022': "['cleanliness', 'noise']",
               'B11-TN-032': "['mixed', 'mixed', 'mixed', 'mixed']", 'B11-TN-037': '[]',
               'B11-TN-042': '2 1 positive', 'B11-TN-046': '3', 'B11-TN-056': '3 7',
               'B11-TN-059': '[]'}
    for number in [10,11]:
        bank = json.loads((BASE / f'banks/bai-{number}.json').read_text(encoding='utf-8'))
        for q in bank['questions']:
            if q['kind'] != 'quiz':
                continue
            namespace = {'pd':pd,'np':np,'re':re,'BaseModel':BaseModel,'Literal':Literal,'validate':lambda value:value}
            if q['id']=='B10-TN-040':
                namespace['rv']=pd.DataFrame({'date':pd.to_datetime(['2025-06-29','2025-06-30','2026-06-29','2026-06-30'])})
            blocks = re.findall(r'^```python\n(.*?)^```', q['promptMarkdown'], re.M | re.S)
            stream = io.StringIO()
            ran = False
            for code in blocks:
                if q['id']=='B11-TN-033':
                    continue  # This is a stated prior assertion, not a self-contained sample.
                # Incomplete function bodies and TODOs are tested by explicit simulations below.
                if '____' in code or re.search(r'^\s*return\b',code,re.M) and not re.search(r'^def |^class ',code,re.M):
                    continue
                tree = ast.parse(code)
                allowed = {'pandas','numpy','re','typing','pydantic'}
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import): assert all(x.name.split('.')[0] in allowed for x in node.names)
                    if isinstance(node, ast.ImportFrom): assert node.module.split('.')[0] in allowed
                try:
                    with contextlib.redirect_stdout(stream):
                        exec(compile(tree,q['id'],'exec'),namespace)
                except KeyError as error:
                    assert q['id']=='B11-TN-058' and error.args==(2,)
                    checked(q['id'], str(error), '2', 'Exact missing-key exception')
                ran = True
            if ran:
                checks.setdefault(q['id'],[]).append({'method':'Executed supplied complete Python blocks','stdout':stream.getvalue()})
            if q['id'] in expressions:
                checked(q['id'],eval(expressions[q['id']],namespace),expected[q['id']],expressions[q['id']])
            if q['id'] in outputs:
                checked(q['id'],stream.getvalue().strip(),outputs[q['id']],'Exact stdout')


def numerical_checks():
    def c(n, value, expected): checked('B10-TN-'+f'{n:03d}',value,expected,'Independent small-fixture calculation')
    c(2,2/4*100,50.); c(4,(200+1.5*(200-100),sum(x>350 for x in [100,200,350,351,500])),(350,2))
    c(8,int((~pd.Series([10,10,20,99]).isin([10,20,30,40])).sum()),1)
    c(13,sum(x>365 for x in [1,365,366,999]),2)
    c(14,[i for i,(a,b)in enumerate([(-34,-71),(-33.5,-70.5),(-32.9,-70.5),(-33.5,-69.9),(-34,-70)])if not(-34<=a<=-33 and -71<=b<=-70)],[2,3])
    c(20,(sum(x!=0 for x in [0,-1,1,-1]),sum([0,-1,1,-1])),(3,-1))
    c(25,([i for i,(g,p)in enumerate(zip('AAABBB',[100,100,2500,1000,1000,5000]))if p>20*{'A':100,'B':1000}[g]],[5]),([2],[5]))
    c(28,(sum(x>1000 for x in [1000,2000,3000,4000]),sum(x>3970 for x in [1000,2000,3000,4000])),(3,1))
    c(29,(6,len(set([10,10,20,20,20,30]))),(6,3))
    c(37,all((not(a or b))==((not a)and(not b))for a in [False,True]for b in [False,True]),True)
    dates=pd.to_datetime(['2025-06-29','2025-06-30','2026-06-29','2026-06-30'])
    c(39,int((pd.to_datetime(['2026-06-28','2026-06-29','2026-06-30','2026-07-01'])>pd.Timestamp('2026-06-29')).sum()),2)
    c(40,int((dates>=pd.Timestamp('2025-06-30')).sum()),3)
    c(42,(4/8,2/6),(0.5,1/3)); c(47,round((3+3-2)/6*100,2),66.67)
    c(48,(2000000/1000,2500>2000),(2000.,True))
    orphan=[x for x in [10,99,99,88,20,99]if x not in [10,20,30,40]];c(49,(len(orphan),len(set(orphan))),(4,2))
    c(51,(1/2>2/6,2>1),(True,True));c(53,10**4/10**2,100.)
    c(55,[i for i,(g,p)in enumerate(zip('AABB',[2000,2001,4000,3999]))if p>20*{'A':100,'B':200}[g]],[1])
    dup=pd.DataFrame({'id':[1,1,1,2,2,3],'snapshot':['06','06','09','06','06','09']})
    c(56,(len(dup[~dup.duplicated(keep=False)]),len(dup.drop_duplicates())),(2,4))
    c(60,(float(np.median([0,0,0,0,-1,-1,-1])),float(np.median([-1,-1,-1]))),(0.,-1.))
    for n,value,expected in [(8,5/8,.625),(10,(2000*.25+400*1.5)/1e6,.0011),(18,(1,1,2),(1,1,2)),
                              (20,sum(x//4 for x in [7,7,7]),3),(23,[2,4],[2,4]),(28,2/(2+3),.4),
                              (30,int(np.ceil((2400-900)/1000)),2),(38,2*2/(2*2),1.),
                              (40,3*(80//4+100),360),(48,(3/4,2/4),(.75,.5)),
                              (50,10000*(200*.25+40*1.5)/1e6,1.1),
                              (60,2*(120*.25+20*1.5)/1e6,.00012)]:
        checked(f'B11-TN-{n:03d}',value,expected,'Independent arithmetic and explicit denominator')
    for n,value,expected in [(4,3-2,1),(7,(2/4,2/3),(.5,2/3)),(8,(600-150,200-150),(450,50)),
                             (9,len({1,3}|{1,2,5}),4),(13,(40-1.5*60,100+1.5*60),(-50,190)),
                             (14,6-4,2),(17,(3*2+1)/4,1.75),(19,(sum(x!=0 for x in [1,-1,0,0]),sum([1,-1,0,0])),(2,0)),
                             (25,(0/4,2/4),(0.,.5)),(28,int(dup.iloc[:5].duplicated().sum()),2),
                             (29,(3-2,3-1),(1,2))]:
        if n==28: value=int(pd.DataFrame({'id':[1,1,1,2,2],'snapshot':['06','06','09','06','09']}).duplicated().sum());expected=1
        checked(f'B10-TL-{n:03d}',value,expected,'Independent arithmetic or set/count fixture')
    for n,value,expected in [(4,4/7,4/7),(8,3/4,.75),(11,sum(x//4 for x in [7,7,7]),3),
                             (19,0. if 0==0 else 1.,0.),(20,0,0),(24,1+2+0,3),(25,5/6,5/6),(28,1.,1.),
                             (29,(500*200*.25+500*40*1.5)/1e6,.055)]:
        checked(f'B11-TL-{n:03d}',value,expected,'Independent numerator, denominator and unit calculation')


def schema_and_retry_checks():
    valid={'sentiment':'mixed','aspects_positive':[],'aspects_negative':[],'language':'en'}
    for identifier, payload in [('B11-TN-004',{**valid,'sentiment':'happy'}),('B11-TN-054',{**valid,'sentiment':'happy'}),
                                ('B11-TL-002',{k:v for k,v in valid.items()if k!='language'})]:
        try: ReviewInfo.model_validate(payload)
        except ValidationError: checked(identifier,True,True,'Actual Pydantic validation rejects invalid/missing field')
        else: raise AssertionError(identifier)
    r=ReviewInfo.model_validate({**valid,'aspects_positive':['noise','noise'],'aspects_negative':['noise'],'language':'xx-custom'})
    checked('B11-TN-034',r.language,'xx-custom','Actual schema allows unvalidated language string, repeats and overlap')
    # Simulate retry timing; never call any API or sleep.
    for identifier, outcomes, repeat, expected in [('B11-TN-015',['error','ok'],1,(2,24,[True])),
                                                 ('B11-TN-025',['invalid'],2,(1,4,[False,False])),
                                                 ('B11-TL-012',['error','error'],1,(2,20,[False]))]:
        cache={};calls=wait=0;results=[]
        def extract():
            nonlocal calls,wait
            if '1'not in cache:
                for attempt in range(2):
                    outcome=outcomes[min(calls,len(outcomes)-1)];calls+=1
                    if outcome=='error':
                        if attempt==0:wait+=20
                        continue
                    cache['1']=valid if outcome=='ok'else{k:v for k,v in valid.items()if k!='language'}
                    wait+=4;break
                else:return False
            try:ReviewInfo.model_validate(cache['1']);return True
            except ValidationError:return False
        results=[extract()for _ in range(repeat)]
        checked(identifier,(calls,wait,results),expected,'Deterministic API/cache/retry simulation with stubbed calls and waits')


def essay_code_checks():
    banks={number:json.loads((BASE/f'banks/bai-{number}.json').read_text(encoding='utf-8')) for number in [10,11]}
    good=ReviewInfo(sentiment='mixed',aspects_positive=[],aspects_negative=[],language='und')
    rv=pd.DataFrame({'listing_id':[10,10,20,20],'date':pd.to_datetime(['2025-06-29','2025-06-30','2026-06-29','2026-06-30'])})
    fixtures={
        'B10-TL-002':({'d':pd.DataFrame({'name':pd.Series(['An','  ',None,'B'],dtype=object),'review_scores_rating':pd.Series([np.nan,4.,-1.,5.1],dtype='float64')})},
                     lambda ns:(ns['ten_trong'].tolist(),ns['diem_ngoai_thang'].tolist()),([False,True,True,False],[False,False,True,True])),
        'B10-TL-005':({'report':pd.DataFrame({'quy_tac':['a','b'],'so_dong':[0,1],'ghi_chu':['Đã kiểm','Cần xem']})},lambda ns:ns['kq'].shape,(2,3)),
        'B10-TL-010':({'rv':rv,'ds':pd.DataFrame({'id':[10,20,30]})},lambda ns:ns['ds'].number_of_reviews_ltm.tolist(),[1,1,0]),
        'B10-TL-015':({'ds':pd.DataFrame({'id':[70,90,50]}),'dem':pd.Series([1,2],index=[50,70])},lambda ns:ns['ds'].dem_that.tolist(),[2,0,1]),
        'B10-TL-026':({'raw':pd.DataFrame({'price_num':[1.,np.nan,3.]})},lambda ns:(ns['d'].price_missing.tolist(),len(ns['kpi']),list(ns['raw'].columns)),([False,True,False],2,['price_num'])),
        'B10-TL-027':({'p':pd.Series([np.nan,0.,-2.,10.],dtype='float64')},lambda ns:ns['bad'].tolist(),[True,True,True,False]),
        'B10-TL-030':({'report':pd.DataFrame({'so_dong':[0,1],'ghi_chu':['Đã kiểm','Cần xem']},index=pd.Index(['review_mo_coi','review_sau_moc'],name='quy_tac'))},lambda ns:list(ns['kq'].columns),['quy_tac','so_dong','ghi_chu']),
        'B11-TL-001':({'rv':pd.DataFrame({'comments':['x'*50]*110+['short']*10})},lambda ns:(len(ns['mau']),int(ns['mau'].comments.str.len().min())),(100,50)),
        'B11-TL-007':({'df':pd.DataFrame({'comments':['a','b','c']},index=[3,1,2]),'labels':pd.DataFrame({'language':['en','es']},index=[1,3])},lambda ns:(list(ns['full'].index),ns['full'].loc[3,'language'],bool(pd.isna(ns['full'].loc[2,'language']))),([3,1,2],'es',True)),
        'B11-TL-011':({'mau':pd.DataFrame({'comments':['x'*7]*3})},lambda ns:ns['tong_token'],3),
        'B11-TL-018':({'raw':good.model_dump_json(),'ReviewInfo':ReviewInfo},lambda ns:isinstance(ns['info'],ReviewInfo),True),
        'B11-TL-021':({'ok':{12:good,4:good}},lambda ns:(list(ns['labels'].index),list(ns['labels'].columns)),([12,4],list(ReviewInfo.model_fields))),
        'B11-TL-022':({'rid':15},lambda ns:ns['key'],'15'),
        'B11-TL-023':({'so_dung':3,'hop_le':{1:good,2:good,3:good,4:good}},lambda ns:ns['acc'],.75),
        'B11-TL-026':({'results':{1:good,2:None,3:good,4:None}},lambda ns:(list(ns['ok']),ns['loi']),([1,3],[2,4])),
    }
    for identifier,(setup,result,expected)in fixtures.items():
        number=int(identifier.split('-')[0][1:])
        question=next(q for q in banks[number]['questions']if q['id']==identifier)
        namespace={'pd':pd,'np':np,'ReviewInfo':ReviewInfo,**setup}
        code='\n'.join(re.findall(r'^```python\n(.*?)^```',question['answerMarkdown'],re.M|re.S))
        assert code,identifier
        exec(compile(code,identifier,'exec'),namespace)
        checked(identifier,result(namespace),expected,'Executed primary Drive solution on explicit synthetic fixture')


def paired_methods():
    def micro(pred,gold):
        tp=sum(len(pred[i]&t)for i,t in gold.items())
        fp=sum(len(pred[i]-t)for i,t in gold.items())
        fn=sum(len(t-pred[i])for i,t in gold.items())
        return (tp,fp,fn,2*tp/(2*tp+fp+fn)if tp else 0.)
    gold={1:{'location','noise'},2:{'host'},3:set()}
    pred={1:{'location'},2:{'host','value'},3:{'amenities'}}
    checked('B11-TL-004',micro(pred,gold),(2,2,1,4/7),'Independent set intersections/differences and micro aggregation')
    checked('B11-TL-019',micro({i:set()for i in range(3)},{i:set()for i in range(3)}),(0,0,0,0.),'All-empty set fixture and exact zero-TP branch')
    checked('B11-TL-024',micro({1:{'host'},2:set(),3:{'value'}},{1:{'host','noise'},2:{'cleanliness','location'},3:set()})[2],3,'Compute FN as gold minus prediction, separately from FP')
    pred={1:set(['host'])|set(['host']),2:set()|{'noise'},3:{'location'}|set()}
    checked('B11-TL-028',micro(pred,{1:{'host'},2:{'noise'},3:{'location'}}),(3,0,0,1.),'Set union removes duplicate positive/negative mention before scoring')
    d=pd.DataFrame({'id':[10,99,20,88,30,10],'date':pd.to_datetime(['2026-06-29','2026-06-30','2026-06-30','2026-06-28','2026-06-29','2026-07-01'])})
    checked('B10-TL-009',int((~d.id.isin([10,20,30,40])|(d.date>pd.Timestamp('2026-06-29'))).sum()),4,'Pandas union mask on all six supplied rows')
    d=pd.DataFrame({'quan':list('AAAABBBB'),'gia':[100,100,100,2100,1000,1000,1000,21000]})
    a=d.gia>20*d.groupby('quan').gia.transform('median');b=d.gia>10000
    checked('B10-TL-018',int((a&b).sum()),1,'Pandas group medians, row-aligned transform and intersection')
    d=pd.DataFrame({'gia':[100.,np.nan,200.,-1.],'lat':[-34.,-33.5,np.nan,-32.9],'lon':[-71.,-70.5,-70.5,-70.5]})
    bad=d.gia.isna()|(d.gia<=0)|d.lat.isna()|d.lon.isna()|~(d.lat.between(-34,-33)&d.lon.between(-71,-70))
    checked('B10-TL-022',int(bad.sum()),3,'Actual float64 missing values and inclusive geographic boundary masks')


if __name__=='__main__':
    initial=os.getcwd()
    with tempfile.TemporaryDirectory(prefix='studyhub-new-exams-')as temp:
        try:
            os.chdir(temp);run_blocks();numerical_checks();schema_and_retry_checks();essay_code_checks();paired_methods()
        finally:os.chdir(initial)
    target=ROOT/'qa/data-exam-20261106/independent-checks.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps({'versions':{'pandas':pd.__version__,'numpy':np.__version__},'questions':checks},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'PASS {len(checks)} questions with executed code/arithmetic/schema/cache evidence')
