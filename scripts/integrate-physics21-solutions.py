"""Place authored solutions immediately after each end-of-chapter prompt and figure."""
from pathlib import Path
import re,json

ROOT=Path(__file__).resolve().parents[1]
SOL=ROOT/'raw_materials/physics/solutions/chapter-21'
solutions={}
for file in sorted(SOL.glob('*.md')):
    source=file.read_text(encoding='utf8')
    entries=list(re.finditer(r'^<!-- solution: ([^ ]+) -->\s*$',source,re.M))
    for i,m in enumerate(entries):
        body=source[m.end():entries[i+1].start() if i+1<len(entries) else len(source)].strip()
        assert m[1] not in solutions,m[1]
        assert '**Tóm tắt đề bài.**' in body and '**Hướng đi:**' in body,m[1]
        solutions[m[1]]=body

count=0
for file in sorted((ROOT/'raw_materials/physics/translations/chapter-21').glob('*.md')):
    if int(file.name[:2]) not in range(9,16):continue
    text=file.read_text(encoding='utf8')
    text=re.sub(r'\n<!-- detailed-solution:[^>]+ -->\n::: solution Lời giải chi tiết\n[\s\S]*?\n:::\n','\n',text)
    inserts=[]
    for m in re.finditer(r'^::: exercise ([^\n]+)\n',text,re.M):
        idmatch=re.match(r'((?:Q|VP)?21\.\d+(?:\.\d+)?)\b',m[1])
        key=idmatch[1] if idmatch else ('bridge21' if m[1]=='Điện tích phân bố trên nửa vòng' else None)
        assert key and key in solutions,(file,key)
        closing=re.search(r'^:::\s*$',text[m.end():],re.M)
        assert closing,file
        pos=m.end()+closing.end()
        # Keep source illustrations and their authored captions ahead of the solution.
        tail=text[pos:]
        image=re.match(r'\s*(!\[[^\n]+\]\([^\n]+\))\n',tail)
        if image:
            pos+=image.end()
            caption=re.match(r'\s*(\*\*Hình[^\n]+(?:\n(?!\s*\n)[^\n]+)*)\n',text[pos:])
            if caption:pos+=caption.end()
        block=f'\n\n<!-- detailed-solution:{key} -->\n::: solution Lời giải chi tiết\n{solutions[key]}\n:::\n'
        inserts.append((pos,block));count+=1
    for pos,block in reversed(inserts):text=text[:pos]+block+text[pos:]
    file.write_text(text,encoding='utf8')
assert count==137,(count,len(solutions))
print('Integrated137 detailed solutions:101 numbered problems,23 questions,12 variations and1 bridge.')
