"""Private source inventory and calculation checks for Chapter28."""
from pathlib import Path
import contextlib,io,json,re,runpy
root=Path(__file__).resolve().parents[2]
raw=root/'raw_materials/physics/translations/chapter-28'
out=root/'qa/physics/chapter28';out.mkdir(parents=True,exist_ok=True)
names=['01_04','05_08','guided','discussion','01_30','31_60','61_83','advanced_cross']
if (root/'raw_materials/physics/verify_chapter28_basic_cross.py').exists():names.append('basic_cross')
scripts=['verify_chapter28_'+name+'.py' for name in names]
for script in scripts:
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf):runpy.run_path(str(root/'raw_materials/physics'/script),run_name='__main__')
    (out/(Path(script).stem+'.log')).write_text(buf.getvalue(),encoding='utf8')
end='\n'.join(p.read_text(encoding='utf8') for p in sorted(raw.glob('*.md')) if 10<=int(p.name[:2])<=15)
exercise_ids=list(map(int,re.findall(r'^::: exercise 28\.(\d+)\b',end,re.M)))
assert exercise_ids==list(range(1,84)),exercise_ids
qids=list(map(int,re.findall(r'^::: exercise Q28\.(\d+)\b',end,re.M)))
assert qids==list(range(1,21)),qids
vp=re.findall(r'^::: exercise (VP28\.\d+\.\d+)\b',end,re.M)
assert len(vp)==len(set(vp))==12
assert len(re.findall(r'^::: exercise Bài cầu nối 28\b',end,re.M))==1
solutions=re.findall(r'^::: (?:solution|details)[^\n]*\n([\s\S]*?)\n:::',end,re.M)
assert len(solutions)==116,len(solutions)
for i,body in enumerate(solutions):
    assert '**Tóm tắt đề bài:**' in body and '**Hướng đi:**' in body,i
    assert re.search(r'\*\*Hướng đi:\*\*\s*\n\s*- ',body),i
    assert body.index('**Tóm tắt đề bài:**')<body.index('**Hướng đi:**'),i
theory='\n'.join(p.read_text(encoding='utf8') for p in sorted(raw.glob('*.md')) if 1<=int(p.name[:2])<=8)
tags=list(map(int,re.findall(r'\\tag\{28\.(\d+)\}',theory)))
assert sorted(set(tags))==list(range(1,33)),tags
assert {n for n in tags if tags.count(n)>1}=={9},'Only the recalled long-wire equation is repeated'
assert set(re.findall(r'Ví dụ 28\.(\d+)',theory))==set(map(str,range(1,13)))
all_text='\n'.join(p.read_text(encoding='utf8') for p in raw.glob('*.md'))
assert not re.search(r'^# ',all_text,re.M),'No duplicate H1'
assert not re.search(r'(?m)^.*[^\s$].*\$\$|^\$\$[^\n]',all_text),'Display delimiters must have separate lines'
assert not re.search(r'(?<!\\)\\[()]',all_text),'No unsupported math delimiters'
assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',all_text),'No control characters'
answers=(raw/'16-dap-so.md').read_text(encoding='utf8')
odd=[int(n) for n in re.findall(r'^\| 28\.(\d+)\s*\|',answers,re.M)]
assert set(odd)==set(range(1,84,2))|{82},odd
assert len(re.findall(r'^\| VP28\.',answers,re.M))==12
pngs=list((root/'docs/vat-ly-2/bai-giang/img/young-28').glob('*.png'))
assert len(pngs)==83,len(pngs)
report={'status':'passed','detailedSolutions':116,'exercises':83,'discussion':20,'guidedVariations':12,'bridge':1,'equationTags':tags,'sourcePngs':83,'calculationSuites':scripts,'scope':'Source-unit inventory, all answer-key entries and independent numeric suites. Browser/caption verification is recorded separately.'}
(out/'numeric-checks.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print('Passed',len(scripts),'calculation suites,32 source equations and116 complete collapsed solutions.')
