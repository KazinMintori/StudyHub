"""Independent checks of selected semantics, not an all-bank accuracy estimate."""
import json, sys, re, calendar, warnings
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timedelta, timezone
import numpy as np
import pandas as pd
import duckdb
import importlib.metadata as metadata
import inspect
from io import StringIO

root = Path(__file__).resolve().parents[1]
banks = {q['id']:q for p in (root/'raw_materials/xu-ly-du-lieu/exam/banks').glob('*.json') for q in json.loads(p.read_text(encoding='utf8'))['questions']}
rows = []
def scope(qid):
    ns = {'np':np,'pd':pd,'re':re}
    for code in re.findall(r'^```python\n(.*?)^```',banks[qid]['promptMarkdown'],re.M|re.S):
        exec(code,ns)
    return ns
def record(qid,result,method):
    rows.append(dict(id=qid,derived=result,method=method))

left=['A','A'];right=['A','A','A']
assert sum(a==b for a in left for b in right)==6
assert len(pd.DataFrame({'k':left}).merge(pd.DataFrame({'k':right}),on='k'))==6
record('B1-001','B remains correct; matched multiplicities 2 and 3 produce 6 pairs','Explicit pair enumeration vs pandas merge; duplicate-key relationships need a stated intended grain')
assert [Fraction(n,10)*100 for n in [6,3,1]]==[60,30,10]
record('B1-026','A: 60%, 30%, 10%; a 100% sum does not identify swapped groups','Independent exact Fraction proportions from given group counts')
pytz=[r for r in metadata.requires('pandas') if r.startswith('pytz')]
assert pd.__version__.startswith('3.') and all('extra ==' in r for r in pytz)
record('B1-015',{'derivedKey':'D','pandasVersion':pd.__version__,'pytzRequirements':pytz},'Installed package metadata shows optional extras, not universal core dependencies; no package installation performed')
assert 'squeeze' not in inspect.signature(pd.read_csv).parameters
one=pd.read_csv(StringIO('id,price\n101,50000\n'),usecols=['id'])
assert isinstance(one,pd.DataFrame) and isinstance(one['id'],pd.Series)
record('B4-003','B remains correct; read_csv has no squeeze argument in pandas3, one selected column remains a DataFrame','Public function signature and exact one-column CSV fixture')

s=scope('B4-052')
manual=[(v<50,v>=50) for v in [20.,50.,80.,float('nan')]]
assert (s['p'],s['q'],s['p']+s['q'])==(0.25,0.5,0.75)
assert tuple(sum(x[i] for x in manual)/4 for i in [0,1])==(s['p'],s['q'])
record('B4-052','B: 0.25, 0.5, 0.75','Python scalar comparisons/count denominator vs pandas boolean means')

data=[('P','A',20),('P','A',40),('Q','A',80),('R','B',30),('R','B',50),('R','B',70)]
keep=[(ix,x) for ix,x in zip([10,20,30,40,50,60],data) if len({v[0] for v in data if v[1]==x[1]})>=2]
manual={ix:Fraction(x[2])-sum(Fraction(v[2]) for _,v in keep if v[0]==x[0])/sum(v[0]==x[0] for _,v in keep) for ix,x in keep}
d=pd.DataFrame(data,columns=['id','khu','gia'],index=[10,20,30,40,50,60])
du=d.loc[d.groupby('khu')['id'].transform('nunique').ge(2)].copy()
du['lech']=du['gia']-du.groupby('id')['gia'].transform('mean')
assert du['lech'].to_dict()=={ix:float(v) for ix,v in manual.items()}=={10:-10.,20:10.,30:0.}
record('B5-019',str(manual),'Explicit group sets and Fraction means vs pandas transform alignment')

weighted=sum(Fraction(n)*m for n,m in [(5,20),(2,80),(1,140)])/8
assert weighted==50 and sum(map(Fraction,[20,80,140]))/3==80
record('B5-046','A: 7/8, 2/3, 80, 50','Exact rational weighted sum from host counts')

d=pd.DataFrame({'gia':[0.,10.,np.nan,100.]})
result=duckdb.sql('SELECT MEDIAN(gia),AVG(gia),COUNT(gia) FROM d').fetchone()
valid=sorted(v for v in d['gia'] if not pd.isna(v))
assert result==(valid[1],sum(valid)/len(valid),len(valid))==(10.,110/3,3)
record('B6-044','A: 10, 110/3, 3','Sorted valid Python values and ordinary average vs DuckDB aggregates')

s=scope('B7-053')
assert pd.isna(s['a'].iloc[1]) and not s['b'].iloc[1] and not s['c'].iloc[1]
record('B7-053','C: Missing, False, False','Exact source across three pandas string/missing policies')

s=scope('B8-029')
values=s['s'].tolist()
manual=[sum(values[i-6:i+1])/7 for i in [6,7]]
actual=s['s'].rolling(7,min_periods=7,center=False).mean()
assert actual.iloc[:6].isna().all() and actual.iloc[6:].tolist()==manual
assert actual.idxmax()==pd.Timestamp('2026-11-07') and s['s'].idxmax()==pd.Timestamp('2026-11-01')
record('B8-029',{'lastTwo':manual,'maxDay':'2026-11-07','originalMax':'2026-11-01'},'Plain seven-element window sums vs pandas rolling; no universal lag or forecast follows')

assert Fraction(280+580,28+29)==Fraction(860,57)
assert calendar.monthrange(2023,2)[1]+calendar.monthrange(2024,2)[1]==57
record('B8-034','C: 860/57','Exact pooled numerator/denominator with independent calendar lengths')
assert round(float((Fraction(294,310)-1)*100),1)==-5.2
assert (Fraction(294,28)/Fraction(310,31)-1)*100==5
record('B8-037','B: Total -5.2%, daily rate +5.0%','Exact Fraction changes of totals and calendar-normalized rates')

s=scope('B8-060')
manual=[datetime.strptime(x,'%Y-%m-%d %H:%M').replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=7))) for x in s['raw']]
chosen=[i+1 for i,x in enumerate(manual) if x.date()==datetime(2027,1,1).date()]
tz=pd.to_datetime(s['raw'],utc=True).dt.tz_convert('Asia/Ho_Chi_Minh')
actual=(tz.ge(pd.Timestamp('2027-01-01',tz='Asia/Ho_Chi_Minh'))&tz.lt(pd.Timestamp('2027-01-02',tz='Asia/Ho_Chi_Minh')))
assert chosen==[i+1 for i,x in enumerate(actual) if x]==[2,3,4]
assert manual[1].weekday()==4
record('B8-060',{'keptOneBased':[2,3,4],'dailyRate':3,'secondRow':'Friday 2027-01-01 00:00 +07:00'},'Standard datetime fixed UTC+7 vs pandas timezone conversion and half-open bounds')

with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter('always')
    parsed=pd.to_datetime(pd.Series(['05/13/2026']),dayfirst=True,errors='coerce')
assert parsed.iloc[0]==pd.Timestamp('2026-05-13') and any(issubclass(w.category,UserWarning) for w in caught)
strict=pd.to_datetime(pd.Series(['05/13/2026']),format='%d/%m/%Y',errors='coerce')
assert pd.isna(strict.iloc[0])
record('B8-051',{'derivedKey':'C','warnings':[str(w.message) for w in caught]},'Exact parsing with recorded warnings vs explicit source format')
for a,b in [(5,0),(5.0,0.0)]:
    try: a/b
    except ZeroDivisionError: pass
    else: raise AssertionError('Expected Python scalar division error')
changes=pd.Series([0,0,5,10]).pct_change(fill_method=None)
assert changes.iloc[:2].isna().all() and np.isposinf(changes.iloc[2]) and changes.iloc[3]==1.
record('B8-055','A remains correct; Python scalar division raises ZeroDivisionError, unlike this pandas result','Python scalar operations vs pandas pct_change')
assert (np.array([20000],dtype=np.int16)*2).tolist()==[-25536]
record('B3-016','A remains correct; int16 can overflow for other inputs','Counterexample 20000*2 exceeds 32767; no hardware register width inference')
reversed_df=pd.DataFrame({'x':[1,2,3]}).iloc[::-1]
assert reversed_df.head(2)['x'].tolist()==[3,2]
record('B4-022','C remains correct; head follows current row order','Reversed DataFrame order, not physical address order')
dtype=pd.StringDtype(storage='python')
assert dtype.storage=='python'
record('B7-056','D remains correct; StringDtype alone does not imply Arrow storage','Construct explicit python string storage; performance requires measured operation/backend')

left_keys=['A']; right_keys=['A','B','B']
left_rows=pd.DataFrame({'k':left_keys}); right_rows=pd.DataFrame({'k':right_keys})
assert not right_rows['k'].is_unique
joined=left_rows.merge(right_rows,how='left',on='k')
assert len(joined)==len(left_rows)==sum(max(1,sum(k==other for other in right_keys)) for k in left_keys)==1
record('B6-015','C remains correct; globally unique right keys sufficient, not necessary','Unmatched duplicated B keys leave one A row unchanged; nested-loop cardinality and pandas merge')
native=duckdb.sql("SELECT count(v), count(*) FILTER (WHERE v IS NULL), isnan(avg(v)) FROM (VALUES (0.0),(10.0),(CAST('NaN' AS DOUBLE)),(100.0)) t(v)").fetchone()
d=pd.DataFrame({'gia':[0.,10.,np.nan,100.]})
imported=duckdb.sql('SELECT count(gia), count(*) FILTER (WHERE gia IS NULL), avg(gia) FROM d').fetchone()
assert native==(4,0,True) and imported==(3,1,110/3)
record('B6-044',{'derivedKey':'A','nativeNan':native,'pandasImportedNan':imported},'Native SQL NaN vs pandas-import null; SQL NULL is not universally identical to NaN')

out={'environment':{'python':sys.version,'numpy':np.__version__,'pandas':pd.__version__,'duckdb':duckdb.__version__},'checks':rows}
target=root/'qa/data-exam-second-review/root-results.json'
target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(f'{len(rows)} independent checks passed; evidence saved')
