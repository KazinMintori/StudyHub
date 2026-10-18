"""Cross-check selected mechanisms with independent implementations.

These are targeted second-method checks, not a claim that every key was proved.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime
from fractions import Fraction
import itertools,json,math,re
import numpy as np
import pandas as pd
import duckdb

ROOT=Path(__file__).resolve().parents[1]
BANK={q['id']:q for p in (ROOT/'raw_materials/xu-ly-du-lieu/exam/banks').glob('*.json') for q in json.loads(p.read_text(encoding='utf-8'))['questions']}
FENCE=re.compile(r'^```python\s*\n(.*?)^```[ \t]*$',re.M|re.S)
RESULTS=[]
def source_scope(qid):
 scope={'np':np,'pd':pd,'re':re,'json':json}
 for block in FENCE.findall(BANK[qid]['promptMarkdown']):exec(block,scope)
 return scope

def record(qid,method,result):RESULTS.append({'id':qid,'method':method,'result':str(result),'sourceKey':BANK[qid]['correctKey']})

# NumPy multiplication against ordinary Python arithmetic, including int8 wrap.
s=source_scope('B3-002');assert s['y'].tolist()==[int(v)*2 for v in s['x']]
assert s['y'].dtype==np.int32;record('B3-002','Python element loop vs NumPy ufunc',(s['y'].tolist(),str(s['y'].dtype)))
s=source_scope('B3-016');wrapped=[(int(v)*2+128)%256-128 for v in s['x']]
assert s['a'].tolist()==wrapped and s['b'].tolist()==[int(v)*2 for v in s['x']]
record('B3-016','Modular integer arithmetic vs fixed-width array',wrapped)
s=source_scope('B3-018');offset_p=[(row*4+col)*4 for row in range(3) for col in [0,2]];offset_q=[(row*4+col)*4 for row in range(3) for col in [1,2]]
assert len(set(np.diff(offset_p)))==1 and len(set(np.diff(offset_q)))>1
assert np.shares_memory(s['A'],s['P']) and not np.shares_memory(s['A'],s['Q'])
record('B3-018','Enumerated source byte offsets vs actual memory sharing',(offset_p,offset_q))
s=source_scope('B3-028');offsets=[(row*4+col)*4 for col in [1,3] for row in [0,2]]
span=max(offsets)+4-min(offsets);assert s['V'].shape==(2,2) and s['V'].strides==(8,32) and span==44
assert s['V'].nbytes==16 and np.shares_memory(s['A'],s['V'])
record('B3-028','Coordinate-to-offset arithmetic vs ndarray strides',(offsets,span))

# Group means and label alignment against explicit dictionaries/lists.
s=source_scope('B5-003');groups={key:[float(v) for k,v in zip(s['d']['khu'],s['d']['gia']) if k==key and not pd.isna(v)] for key in ['A','B']}
expected={key:sum(values)/len(values) for key,values in groups.items()};assert s['t'].to_dict()==expected
record('B5-003','Explicit per-group list reduction vs pandas groupby',expected)
s=source_scope('B5-006');old=s['cu'].to_dict();new=s['moi'].to_dict();missing=sorted(set(old)^set(new))
assert sorted(s['r'][s['r'].isna()].index)==missing==['C','D']
record('B5-006','Dictionary key union/missing operands vs pandas alignment',missing)

# SQL left join cardinality independently enumerated and checked via pandas.
s=source_scope('B6-015');l=s['l'];t=s['t'];pairs=[]
for left in l.to_dict('records'):
 matches=[right for right in t.to_dict('records') if left['khu']==right['khu']]
 pairs.extend((left['id'],right['phi']) for right in matches)
 if not matches:pairs.append((left['id'],None))
actual=duckdb.sql('SELECT l.id,t.phi FROM l LEFT JOIN t ON l.khu=t.khu').fetchall()
assert Counter(actual)==Counter(pairs) and len(actual)==len(l.merge(t,on='khu',how='left'))==6
record('B6-015','Nested-loop join vs DuckDB SQL vs pandas merge',pairs)

# Calendar parsing by the standard library independently of pandas.
s=source_scope('B8-007');bad=[]
for label,value in s['raw'].items():
 if pd.isna(value):continue
 try:datetime.strptime(value,'%d/%m/%Y')
 except ValueError:bad.append(label)
assert bad==s['bad'][s['bad']].index.tolist()==['R3']
record('B8-007','datetime.strptime vs pandas to_datetime/coerce',bad)
s=source_scope('B8-005');manual=sum(s['s'].tolist()[-3:])/3;assert manual==s['t'].iloc[-1]==18
record('B8-005','Plain list window mean vs rolling',manual)
s=source_scope('B8-014');last=s['s'].tolist()[-3:];valid=[v for v in last if not math.isnan(v)]
assert len(valid)<3 and math.isnan(s['t'].iloc[-1]);record('B8-014','Explicit valid-observation count vs min_periods',len(valid))

# Regex grammar contrasted with a different string algorithm on many inputs.
s={'re':re};exec('\n'.join(FENCE.findall(BANK['B7-R17']['answerMarkdown'])),s)
alphabet=[' ','\t','A','B','\u00a0','\v','\f'];count=0
for length in range(5):
 for chars in itertools.product(alphabet,repeat=length):
  value=''.join(chars);assert s['cat_dau_cuoi'](value)==value.strip(' \t');count+=1
record('B7-R17','Regex capture vs explicit ASCII-space/tab strip',f'{count} exhaustive small strings')

# Weighted means compared using exact rational arithmetic.
q=source_scope('B5-046')
# The exact 5/2/1 host sizes and20/80/140 means are stated in the prompt.
assert Fraction(5*20+2*80+140,8)==50 and Fraction(20+80+140,3)==80
record('B5-046','Exact Fraction arithmetic for host/listing denominators',(Fraction(7,8),Fraction(2,3),80,50))

out=ROOT/'qa/data-exam/cross-method-checks.json';out.write_text(json.dumps(RESULTS,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'PASS {len(RESULTS)} targeted cross-method checks; these supplement source execution and review, not all-key proof.')
