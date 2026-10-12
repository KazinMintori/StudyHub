from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
paths=list((root/'raw_materials/physics/translations/chapter-21').glob('*.md'))+list((root/'raw_materials/physics/translations/chapter-22').glob('*.md'))
paths+=list((root/'raw_materials/physics/translations/chapter-23').glob('*.md'))
paths += [root/'docs/wiki'/f'{name}.md' for name in ['dien-thong','dinh-luat-gauss','mat-gauss','che-chan-tinh-dien']]
for p in paths:
    if not p.exists():continue
    text=p.read_text(encoding='utf8')
    parts=re.split(r'(\$\$[\s\S]*?\$\$|\$[^\n$]+\$)',text)
    for i in range(0,len(parts),2):
        parts[i]=parts[i].replace('ε₀',r'$\varepsilon_0$')
    p.write_text(''.join(parts),encoding='utf8')
for name in ['physics-gauss-foundations.mjs','physics-gauss-course.mjs']:
    p=root/'docs/.vitepress'/name
    text=p.read_text(encoding='utf8').replace('ε₀',r'$\\varepsilon_0$')
    p.write_text(text,encoding='utf8')

issues=[]
for p in paths:
    if not p.exists():continue
    text=p.read_text(encoding='utf8')
    clean=re.sub(r'^---\n[\s\S]*?\n---\n','',text)
    clean=re.sub(r'<!--[\s\S]*?-->|\$\$[\s\S]*?\$\$|\$[^\n$]+\$', '∎',clean)
    for n,line in enumerate(clean.splitlines(),1):
        if line.startswith(':::'):continue
        if any(m[1].islower() for m in re.finditer(r':(?:\*\*|\s|\*)+([^\W\d_])',line)):
            issues.append(f'{p.name}:{n}: {line}')
out=root/'qa/physics/language-audit.txt';out.write_text('\n'.join(issues),encoding='utf8')
print('Colon capitalization candidates:',len(issues))
print('\n'.join(issues[:30]))
