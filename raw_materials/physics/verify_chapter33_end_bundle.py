"""Source inventory and numerical evidence for all 102 chapter-end solutions.

This is an editorial acceptance check, not a replacement for source or browser review.
"""
from pathlib import Path
import json,re

root=Path(__file__).resolve().parents[2]
out=root/'qa/physics/chapter33'
raw=root/'raw_materials/physics/translations/chapter-33'
files=sorted(p for p in raw.glob('*.md') if 10<=int(p.name[:2])<=15)
text='\n'.join(p.read_text(encoding='utf-8-sig') for p in files)
prompts=re.findall(r'^::: exercise (.+)$',text,re.M)
solutions=re.findall(r'^::: solution (.+)$',text,re.M)
inventory=json.loads((out/'full-source-inventory.json').read_text(encoding='utf-8-sig'))
expected=set(inventory['numberedExercises']+inventory['discussion']+inventory['guidedPractice'])
assert len(expected)==101
assert expected<=set(prompts), sorted(expected-set(prompts))
assert len(prompts)==len(set(prompts))==102
assert len(solutions)==102
assert len(set(prompts)-expected)==1, 'Exactly one bridging problem is required'
for p in files:
 for block in re.findall(r'^::: solution[^\n]*\n(.*?)^:::',p.read_text(encoding='utf-8-sig'),re.M|re.S):
  assert '**Tóm tắt đề bài:**' in block,p
  assert '**Hướng đi:**' in block,p
  assert re.search(r'^- ',block,re.M),p
evidence=['guided-data-checks.json','discussion-data-checks.json','exercises-01-35-data-checks.json','exercises-36-64-data-checks.json']
for name in evidence:
 result=json.loads((out/name).read_text(encoding='utf-8-sig'))
 assert result.get('status')=='passed',name
math=json.loads((out/'end-math-review.json').read_text(encoding='utf-8-sig'))
assert not math['findings']
result={'status':'passed','numberedExercises':64,'discussionQuestions':25,'guidedPractice':12,'bridgingProblems':1,
 'endSolutions':102,'files':[p.relative_to(root).as_posix() for p in files],
 'numericEvidence':evidence,'mathEvidence':'end-math-review.json',
 'mathDisplayExpressions':math['display'],'mathInlineExpressions':math['inline'],
 'renderStatus':'pending','theoryReview':'pending-final-agy-and-parent-audit'}
(out/'end-content-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'authoring-progress.json').write_text(json.dumps({
 'status':'all-end-solutions-authored-under-final-review','chapter':33,'fullChapterEndSolutionsExpected':102,
 'authoredEndSolutions':102,'theoryStatus':'AGY A/B final corrective call3 running, acceptance pending',
 'supportStatus':'11 slides, eight Cheatsheet groups,14 new Wiki plus Snell revision authored, integration pending',
 'numericEvidence':'qa/physics/chapter33/end-content-checks.json','renderStatus':'pending','publication':'not-published'
},ensure_ascii=False,indent=2),encoding='utf-8')
print('Verified source identifiers and detailed-solution structure for all102 chapter-end problems.')
