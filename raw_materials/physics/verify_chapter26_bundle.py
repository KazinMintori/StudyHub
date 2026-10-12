"""Private source inventory and calculation checks for Chapter26."""
from pathlib import Path
import contextlib,io,json,re,runpy
root=Path(__file__).resolve().parents[2]
raw=root/'raw_materials/physics/translations/chapter-26'
out=root/'qa/physics/chapter26';out.mkdir(parents=True,exist_ok=True)
scripts=['verify_chapter26_01_02.py','verify_chapter26_03_04.py','verify_chapter26_05.py','verify_chapter26_guided.py','verify_chapter26_discussion.py','verify_chapter26_01_32.py','verify_chapter26_33_60.py','verify_chapter26_61_88.py','verify_chapter26_advanced_cross.py']
for script in scripts:
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf):runpy.run_path(str(root/'raw_materials/physics'/script),run_name='__main__')
    (out/(Path(script).stem+'.log')).write_text(buf.getvalue(),encoding='utf8')
end='\n'.join(p.read_text(encoding='utf8') for p in sorted(raw.glob('*.md')) if 7<=int(p.name[:2])<=12)
exercise_ids=list(map(int,re.findall(r'^::: exercise 26\.(\d+)\b',end,re.M)))
assert exercise_ids==list(range(1,89)),exercise_ids
qids=list(map(int,re.findall(r'^::: exercise Q26\.(\d+)\b',end,re.M)))
assert qids==list(range(1,22)),qids
vp=re.findall(r'^::: exercise (VP26\.\d+\.\d+)\b',end,re.M)
assert len(vp)==len(set(vp))==12
assert len(re.findall(r'^::: exercise Bài cầu nối 26\.27',end,re.M))==1
solutions=re.findall(r'^::: (?:solution|details)[^\n]*\n([\s\S]*?)\n:::',end,re.M)
assert len(solutions)==122,len(solutions)
for i,body in enumerate(solutions):
    assert '**Tóm tắt đề bài:**' in body and '**Hướng đi:**' in body,i
    assert re.search(r'\*\*Hướng đi:\*\*\s*\n\s*- ',body),i
    assert body.index('**Tóm tắt đề bài:**')<body.index('**Hướng đi:**'),i
theory='\n'.join(p.read_text(encoding='utf8') for p in sorted(raw.glob('*.md')) if 1<=int(p.name[:2])<=5)
tags=list(map(int,re.findall(r'\\tag\{26\.(\d+)\}',theory)))
assert sorted(tags)==list(range(1,19)),tags
assert set(re.findall(r'Ví dụ 26\.(\d+)',theory))==set(map(str,range(1,15)))
all_text='\n'.join(p.read_text(encoding='utf8') for p in raw.glob('*.md'))
assert not re.search(r'^# ',all_text,re.M),'No duplicate H1'
assert not re.search(r'(?m)^.*[^\s$].*\$\$|^\$\$[^\n]',all_text),'Display delimiters must have separate lines'
assert not re.search(r'(?<!\\)\\[()]',all_text),'No unsupported math delimiters'
assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',all_text),'No control characters'
report={'status':'passed','detailedSolutions':122,'exercises':88,'discussion':21,'guidedVariations':12,'bridge':1,'equationTags':tags,'calculationSuites':scripts,'scope':'Source-unit inventory plus independent numeric suites. Browser/caption verification is recorded separately.'}
(out/'numeric-checks.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print('Passed nine calculation suites, 18 source equations and 122 complete collapsed solutions.')
