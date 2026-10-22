"""Execute the exact teaching snippets in isolated folders and record typed output."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse,hashlib,json,os,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
RUNNER=r'''
import builtins,contextlib,datetime,io,json,math,os,socket,sys,warnings
import numpy as np
import pandas as pd
os.environ['MPLBACKEND']='Agg'
def no_network(*args,**kwargs):raise RuntimeError('Teaching examples do not access the network')
socket.create_connection=no_network
socket.socket.connect=no_network
records=[]
original_print=builtins.print
def scalar(value):
 if value is None or value is pd.NA or value is pd.NaT:return None
 if isinstance(value,(np.integer,np.floating,np.bool_)):value=value.item()
 if isinstance(value,float) and not math.isfinite(value):return str(value) if math.isinf(value) else None
 if isinstance(value,(str,int,float,bool)):return value
 if isinstance(value,(datetime.datetime,datetime.date,pd.Timestamp)):return str(value)
 if isinstance(value,tuple):return ', '.join(str(scalar(x)) for x in value)
 if isinstance(value,(list,np.ndarray)):return json.dumps([scalar(x) for x in value],ensure_ascii=False)
 return str(value)
def frame_output(frame):
 frame=frame.copy(deep=True)
 if isinstance(frame,pd.Series):frame=frame.to_frame(name=frame.name or 'Giá trị')
 data=[]
 indexed=not isinstance(frame.index,pd.RangeIndex) or frame.index.start!=0 or frame.index.step!=1
 multi=isinstance(frame.index,pd.MultiIndex)
 index_names=[name or f'Chỉ mục {i+1}' for i,name in enumerate(frame.index.names)] if multi else [frame.index.name or 'Chỉ mục']
 names=[str(x) for x in frame.columns]
 if indexed:names=index_names+names
 for key,row in frame.iterrows():
  cells=[scalar(v) for v in row.tolist()]
  keys=[scalar(k) for k in key] if multi else [scalar(key)]
  data.append((keys if indexed else [])+cells)
 return {'kind':'table','columns':names,'rows':data}
def json_output(value):
 if isinstance(value,list) and value and all(isinstance(x,dict) for x in value):
  return [frame_output(pd.DataFrame(value))]
 if isinstance(value,dict):
  flat={k:v for k,v in value.items() if not isinstance(v,dict) and not (isinstance(v,list) and v and isinstance(v[0],dict))}
  out=[{'kind':'table','columns':['Trường','Giá trị'],'rows':[[k,scalar(v)] for k,v in flat.items()]}] if flat else []
  for key,child in value.items():
   if key not in flat:out.extend([{'kind':'text','text':key+':\n'},*json_output(child)])
  return out
 return [{'kind':'text','text':json.dumps(value,ensure_ascii=False)}]
def record_print(*args,**kwargs):
 original_print(*args,**kwargs)
 if kwargs.get('file') is not None and kwargs['file'] is not sys.stdout:return
 if len(args)==1:
  arg=args[0]
  if isinstance(arg,(pd.DataFrame,pd.Series)):
   records.append(frame_output(arg))
   return
  if isinstance(arg,str):
   try:parsed=json.loads(arg)
   except (ValueError,TypeError):parsed=None
   if isinstance(parsed,(dict,list)):
    records.extend(json_output(parsed))
    return
 buffer=io.StringIO()
 original_print(*args,**{**kwargs,'file':buffer})
 records.append({'kind':'text','text':buffer.getvalue()})
with open('input.json',encoding='utf-8') as source:
 payload=json.load(source)
saved_figures=[]
if 'matplotlib' in payload['code'] or 'plt.' in payload['code']:
 from matplotlib.figure import Figure
 original_savefig=Figure.savefig
 def remember_savefig(figure,*args,**kwargs):
  if all(figure is not other for other in saved_figures):saved_figures.append(figure)
  return original_savefig(figure,*args,**kwargs)
 Figure.savefig=remember_savefig
scope={'__name__':'__example__','print':record_print}
stdout=io.StringIO()
with contextlib.redirect_stdout(stdout),warnings.catch_warnings(record=True) as caught:
 warnings.simplefilter('always')
 exec(compile(payload['code'],'<teaching-example>','exec'),scope)
figures=[]
if 'matplotlib.pyplot' in sys.modules:
 import matplotlib.pyplot as plt
 from matplotlib.figure import Figure
 for number in plt.get_fignums():
  figure=plt.figure(number)
  if all(figure is not other for other in saved_figures):saved_figures.append(figure)
 for figure in saved_figures:
  buffer=io.StringIO()
  globals().get('original_savefig',Figure.savefig)(figure,buffer,format='svg',bbox_inches='tight',metadata={'Date':None})
  figures.append(buffer.getvalue())
result={'stdout':stdout.getvalue(),'outputs':records,'figures':figures,'warnings':[str(w.message) for w in caught],'versions':{'python':sys.version.split()[0],'pandas':pd.__version__,'numpy':np.__version__}}
from pathlib import Path
Path('result.json').write_text(json.dumps(result,ensure_ascii=False,allow_nan=False),encoding='utf-8')
'''

def execute(item):
    entry={**item,'codeSha256':hashlib.sha256(item['code'].encode()).hexdigest()}
    with tempfile.TemporaryDirectory(prefix='studyhub-example-') as folder:
        target=Path(folder)
        (target/'input.json').write_text(json.dumps({'code':item['code']},ensure_ascii=False),encoding='utf-8')
        (target/'runner.py').write_text(RUNNER,encoding='utf-8')
        try:
            run=subprocess.run([sys.executable,str(target/'runner.py')],cwd=target,capture_output=True,text=True,encoding='utf-8',timeout=60,env={**os.environ,'PYTHONIOENCODING':'utf-8','MPLBACKEND':'Agg'})
        except subprocess.TimeoutExpired:
            return {**entry,'status':'timeout'}
        if run.returncode or not (target/'result.json').exists():return {**entry,'status':'failed','error':run.stderr[-3500:]}
        return {**entry,'status':'passed',**json.loads((target/'result.json').read_text(encoding='utf-8'))}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--jobs',type=int,default=3)
    args=parser.parse_args()
    paths=sorted(p for p in args.manifest.glob('*.json') if p.name!='verified-results.json') if args.manifest.is_dir() else [args.manifest]
    examples=[]
    for path in paths:
        source=json.loads(path.read_text(encoding='utf-8'))
        examples.extend(source['examples'] if 'examples' in source else [{**s,'slug':source['slug'],'id':s.get('id',f"{source['slug']}-{i+1}")} for i,s in enumerate(source['sections'])])
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:results=list(pool.map(execute,examples))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    bad=[{'id':r['id'],'status':r['status'],'error':r.get('error','')} for r in results if r['status']!='passed']
    print(json.dumps({'examples':len(results),'passed':len(results)-len(bad),'failures':bad},ensure_ascii=True,indent=2))
    raise SystemExit(bool(bad))
