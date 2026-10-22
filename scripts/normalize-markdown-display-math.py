"""Normalize display delimiters without touching fenced code or mathematical content."""
from pathlib import Path
import json
import re
import sys

directory = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('qa/markdown-audit')
audit = json.loads((directory/'markdown-audit.json').read_text(encoding='utf-8'))
paths = {Path(item['file']) for item in audit['issues'] if item['kind'] in ('prose-in-math', 'nested-math-delimiter')}
paths.update(Path('docs/wiki').rglob('*.md'))
records=[]
for path in sorted(paths):
    source=path.read_text(encoding='utf-8'); lines=source.splitlines(keepends=True)
    result=[]; indent=None; fence=None; changes=0
    for line in lines:
        delimiter=re.match(r'^\s*(`{3,}|~{3,})',line)
        if delimiter:
            mark=delimiter.group(1)
            if fence is None: fence=mark
            elif mark[0]==fence[0] and len(mark)>=len(fence): fence=None
            result.append(line);continue
        if fence: result.append(line);continue
        stripped=line.strip(); spaces=len(line)-len(line.lstrip(' '))
        single=re.fullmatch(r'\s*\$\$(.+)\$\$\s*',line)
        if single and indent is None:
            pad=' '*spaces
            result.extend([pad+'$$\n',pad+single.group(1).strip()+'\n',pad+'$$\n']);changes+=1;continue
        if stripped=='$$':
            if indent is None: indent=spaces;result.append(line)
            else:
                result.append(' '*indent+'$$\n')
                changes+=spaces!=indent
                indent=None
        elif indent is not None and stripped and spaces<indent:
            result.append(' '*(indent-spaces)+line);changes+=1
        else: result.append(line)
    if indent is not None:
        records.append({'file':str(path),'status':'unpaired-delimiter-not-modified'});continue
    if changes:
        path.write_text(''.join(result),encoding='utf-8',newline='')
        records.append({'file':str(path),'changes':changes})
(directory/'display-format-changes.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Normalized {sum("changes" in x for x in records)} files; unpaired: {sum("status" in x for x in records)}')
