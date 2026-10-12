from pathlib import Path
import re

folder=Path(__file__).resolve().parents[1]/'raw_materials/physics/translations/chapter-21'
for p in folder.glob('*.md'):
    source=p.read_text(encoding='utf8')
    for m in re.finditer(r'\$\$([\s\S]*?)\$\$',source):
        body=m[1];depth=0;i=0
        while i<len(body):
            if body[i:i+2]=='\\\\':
                if depth>0:
                    print(p.name,source[:m.start()+i].count('\n')+1,repr(body[max(0,i-30):i+45]))
                i+=2;continue
            if body[i]=='{' and (i==0 or body[i-1]!='\\'):depth+=1
            if body[i]=='}' and (i==0 or body[i-1]!='\\'):depth-=1
            i+=1
