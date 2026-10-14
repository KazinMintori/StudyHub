"""Run independent chapter30 calculations and verify full source-unit coverage."""
from pathlib import Path
import json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2]
suites=['01_03','04_06','guided','01_40','41_75']
for suite in suites:
 completed=subprocess.run([sys.executable,'-X','utf8',str(ROOT/f'raw_materials/physics/verify_chapter30_{suite}.py')],cwd=ROOT,capture_output=True,text=True,encoding='utf8')
 if completed.returncode:
  print(completed.stdout,completed.stderr);raise SystemExit(completed.returncode)
raw=ROOT/'raw_materials/physics/translations/chapter-30'
files=sorted(raw.glob('*.md'));assert len(files)==15
theory='\n'.join(p.read_text(encoding='utf8') for p in files if p.name[:2] in ('01','02','03','04','05','06'))
assert set(re.findall(r'\\tag\{(30\.\d+)\}',theory))=={f'30.{n}' for n in range(1,30)}
assert len(re.findall(r'^::: example Ví dụ 30\.',theory,re.M))==10
end='\n'.join(p.read_text(encoding='utf8') for p in files if int(p.name[:2])>=10)
numbered=re.findall(r'^::: exercise 30\.(\d+)(?:\.|\s|$)',end,re.M)
assert sorted(map(int,numbered))==list(range(1,76))
assert len(re.findall(r'^::: exercise Q30\.',end,re.M))==16
assert len(re.findall(r'^::: exercise VP30\.',end,re.M))==12
assert len(re.findall(r'^::: exercise Bài cầu nối 30$',end,re.M))==1
solutions=re.findall(r'^::: solution[^\n]*\n([\s\S]*?)\n:::',end,re.M)
assert len(solutions)==104
for body in solutions:
 assert '**Tóm tắt đề bài:**' in body and '**Hướng đi:**' in body
 assert re.search(r'^- ',body,re.M)
images=[]
for p in files:
 for link in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',p.read_text(encoding='utf8')):
  asset=ROOT/'docs/vat-ly-2/bai-giang'/link.removeprefix('../')
  assert asset.is_file(),(p.name,asset)
  images.append(asset.name)
assert len(set(images))==50
odd=re.findall(r'^- \*\*30\.(\d+)\.',(raw/'16-dap-so.md').read_text(encoding='utf8'),re.M)
assert set(map(int,odd))==set(range(1,76,2))
out=ROOT/'qa/physics/chapter30';out.mkdir(parents=True,exist_ok=True)
report={'status':'passed','numericSuites':suites,'theorySections':6,'equations':29,'examples':10,'numberedExercises':75,'discussionQuestions':16,'variationProblems':12,'bridgeProblems':1,'detailedSolutions':104,'referencedFigures':50,'oddAnswerRows':38,'explicitModelIssues':['30.53: Pulse approximation and full RLC step response differ.','30.69: Appendix opposed-connection formula conflicts with flux linkage and energy.']}
(out/'numeric-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
