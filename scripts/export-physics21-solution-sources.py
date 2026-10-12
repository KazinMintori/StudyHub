"""Keep the private solution sources identical to the reviewed rendered text."""
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
blocks={}
for p in (root/'raw_materials/physics/translations/chapter-21').glob('*.md'):
    for m in re.finditer(r'<!-- detailed-solution:([^>]+) -->\s*::: solution[^\n]*\n([\s\S]*?)\n:::',p.read_text(encoding='utf8')):
        assert m[1] not in blocks,m[1]
        blocks[m[1]]=m[2].strip()
assert len(blocks)==137,len(blocks)
for p in (root/'raw_materials/physics/solutions/chapter-21').glob('*.md'):
    text=p.read_text(encoding='utf8')
    matches=list(re.finditer(r'<!-- solution: ([^>]+) -->',text))
    out=[]
    for i,m in enumerate(matches):
        key=m[1]
        assert key in blocks,key
        out.append(m[0]+'\n\n'+blocks[key]+'\n')
    p.write_text('\n'.join(out),encoding='utf8')
print('Exported 137 reviewed solutions to reusable authoring sources.')
