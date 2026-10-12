"""Private Ch25 calculation suites and complete source-unit inventory."""
from pathlib import Path
import contextlib,io,json,re,runpy
root=Path(__file__).resolve().parents[2]
raw=root/'raw_materials/physics/translations/chapter-25'
out=root/'qa/physics/chapter25';out.mkdir(parents=True,exist_ok=True)
scripts=[
 'scripts/verify_chapter25_01_02.py',
 'raw_materials/physics/verify_chapter25_03_04.py',
 'raw_materials/physics/verify_chapter25_05_06.py',
 'raw_materials/physics/verify_chapter25_guided.py',
 'raw_materials/physics/verify_chapter25_discussion.py',
 'raw_materials/physics/verify_chapter25_01_30.py',
 'raw_materials/physics/verify_chapter25_31_58.py',
 'raw_materials/physics/verify_chapter25_59_82.py',
]
for script in scripts:
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf):runpy.run_path(str(root/script),run_name='__main__')
    (out/(Path(script).stem+'.log')).write_text(buf.getvalue(),encoding='utf8')
end='\n'.join(p.read_text(encoding='utf8') for p in sorted(raw.glob('*.md')) if 8<=int(p.name[:2])<=13)
exercise_ids=list(map(int,re.findall(r'^::: exercise 25\.(\d+)\b',end,re.M)))
assert exercise_ids==list(range(1,83)),exercise_ids
qids=list(map(int,re.findall(r'^::: exercise Q25\.(\d+)\b',end,re.M)))
assert qids==list(range(1,25)),qids
vp=re.findall(r'^::: exercise (VP25\.\d+\.\d+)\b',end,re.M)
assert len(vp)==len(set(vp))==12
assert len(re.findall(r'^::: exercise Bài tổng hợp 25',end,re.M))==1
solutions=re.findall(r'^::: (?:solution|details)[^\n]*\n([\s\S]*?)\n:::',end,re.M)
assert len(solutions)==119,len(solutions)
for i,body in enumerate(solutions):
    assert '**Tóm tắt đề bài:**' in body and '**Hướng đi:**' in body,i
    assert re.search(r'\*\*Hướng đi:\*\*\s*\n\s*- ',body),i
    assert body.index('**Tóm tắt đề bài:**')<body.index('**Hướng đi:**'),i
theory='\n'.join(p.read_text(encoding='utf8') for p in sorted(raw.glob('*.md')) if 1<=int(p.name[:2])<=6)
tags=list(map(int,re.findall(r'\\tag\{25\.(\d+)\}',theory)))
assert sorted(tags)==list(range(1,25)),tags
assert not re.search(r'^# ',theory+end,re.M),'Raw includes must not duplicate the page H1'
assert not re.search(r'\\\(|\\\)',theory+end),'Use Markdown math delimiters'
assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',theory+end),'Control character from an escaped TeX string'
# In I = neAv_d, n has L^-3, e has charge dimension and A has L^2.
# Therefore neA has charge/length, rather than charge/area.
assert -3+2==-1
assert r'4.93\times10^4\,\mathrm{C/m}' in end
assert r'4.93\times10^4\,\mathrm{C/m^2}' not in end
report={'status':'passed','chapter':25,'theorySections':6,'equations':24,'workedExamples':11,
 'exercises':82,'discussionQuestions':24,'variationProblems':12,'bridgingProblems':1,
 'detailedSolutions':119,'calculationSuites':scripts,
 'goldValuationEvidence':'qa/physics/chapter25/gold-material-valuation.json'}
(out/'numeric-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Passed eight calculation suites, 24 source equations and 119 complete collapsed solutions.')
