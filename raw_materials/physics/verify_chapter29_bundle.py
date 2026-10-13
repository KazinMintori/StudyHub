"""Run numerical suites and assert complete source numbering and solution structure."""
from pathlib import Path
import subprocess,sys,json,re
ROOT=Path(__file__).resolve().parents[2]
folder=ROOT/'raw_materials/physics/translations/chapter-29'
SUITES=['01_04','05_08','guided','discussion','01_30','31_60','61_74']
for name in SUITES:
 result=subprocess.run([sys.executable,'-X','utf8',str(ROOT/f'raw_materials/physics/verify_chapter29_{name}.py')],cwd=ROOT,text=True,encoding='utf8',capture_output=True)
 assert result.returncode==0,(name,result.stdout,result.stderr)
 print('PASS:',name)
files=sorted(folder.glob('*.md'));assert len(files)==17,len(files)
theory='\n'.join(p.read_text(encoding='utf8') for p in files if re.match(r'0[1-8]-',p.name))
tags=list(map(int,re.findall(r'\\tag\{29\.(\d+)\}',theory)))
assert sorted(tags)==list(range(1,25)),tags
examples=list(map(int,re.findall(r'^### Ví dụ(?: khái niệm)? 29\.(\d+)',theory,re.M)))
assert sorted(examples)==list(range(1,12)),examples
end='\n'.join(p.read_text(encoding='utf8') for p in files if re.match(r'1[0-5]-',p.name))
numbered=list(map(int,re.findall(r'^::: exercise 29\.(\d+)\b',end,re.M)))
assert numbered==list(range(1,75)),numbered
questions=re.findall(r'^::: exercise Q29\.(\d+)\b',end,re.M)
assert list(map(int,questions))==list(range(1,22)),questions
variations=re.findall(r'^::: exercise VP29\.(\d+\.\d+)\b',end,re.M)
assert len(variations)==12 and len(set(variations))==12,variations
assert len(re.findall(r'^::: exercise Bài cầu nối 29\b',end,re.M))==1
solutions=re.findall(r'^::: solution[^\n]*\n([\s\S]*?)\n:::',end,re.M)
assert len(solutions)==108,len(solutions)
for index,solution in enumerate(solutions):
 assert '**Tóm tắt đề bài:**' in solution,index
 assert '**Hướng đi:**' in solution,index
 direction=solution.split('**Hướng đi:**',1)[1]
 assert re.match(r'\s*- ',direction),index
all_text='\n'.join(p.read_text(encoding='utf8') for p in files)
assert not re.search(r'(theo sách|sách dùng|bản dịch của|ảnh lấy từ sách)',all_text,re.I)
assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',all_text)
assert len(re.findall(r'^### 29\.\d+\s*$',(folder/'16-dap-so.md').read_text(encoding='utf8'),re.M))==37
figures=set(re.findall(r'(?:img/young-29/)([^)]+)',all_text))
missing=[f for f in figures if not (ROOT/'docs/vat-ly-2/bai-giang/img/young-29'/f).is_file()]
assert not missing,missing
report={'status':'passed','numericSuites':SUITES,'theorySections':8,'equations':24,'examples':11,'numberedExercises':74,'discussionQuestions':21,'variationProblems':12,'bridgeProblems':1,'detailedSolutions':108,'referencedFigures':len(figures),'oddAnswerRows':37}
out=ROOT/'qa/physics/chapter29';out.mkdir(parents=True,exist_ok=True)
(out/'numeric-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
