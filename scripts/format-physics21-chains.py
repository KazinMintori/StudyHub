"""Break top-level equation chains without changing any mathematical operand."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
dirs=[ROOT/'raw_materials/physics/translations/chapter-21',ROOT/'raw_materials/physics/solutions/chapter-21']

def top_equal_positions(s):
    depth=0;out=[]
    for i,c in enumerate(s):
        if c=='{':depth+=1
        elif c=='}':depth-=1
        elif c=='=' and depth==0:out.append(i)
    return out

def wrap(body):
    body=body.strip()
    if r'\begin{cases}' in body:return '\n'+body+'\n'
    tag=re.search(r'\\tag\{[^}]+\}',body)
    tagtext=tag[0] if tag else ''
    if tag:body=body.replace(tag[0],'').strip()
    aligned=r'\begin{aligned}' in body
    if aligned:
        core=body.removeprefix(r'\begin{aligned}').removesuffix(r'\end{aligned}').strip()
    else:core=body
    rows=core.split(chr(92)*2)
    new=[]
    for row in rows:
        parts=re.split(r'\\qquad\s*',row)
        for part in parts:
            positions=top_equal_positions(part)
            if not positions:
                new.append(part.strip());continue
            first=positions[0]
            if '&' not in part[:first+1]:part=part[:first]+'&'+part[first:]
            positions=top_equal_positions(part)
            if len(positions)>1:
                start=0
                for j,pos in enumerate(positions[1:]):
                    new.append(part[start:pos].strip())
                    start=pos
                new.append('&'+part[start:].strip())
            else:new.append(part.strip())
    # Repeated relation chains acquire a continuation alignment marker.
    for i in range(1,len(new)):
        if new[i].startswith('='):new[i]='&'+new[i]
    changed=(aligned or len(new)>1)
    if changed:
        result='\n'+r'\begin{aligned}'+'\n'+('\\\\\n'.join(new))+'\n'+r'\end{aligned}'
        if tagtext:result+='\n'+tagtext
        return result+'\n'
    if tagtext:body+='\n'+tagtext
    return '\n'+body+'\n'

count=0
for directory in dirs:
    for file in directory.glob('*.md'):
        text=file.read_text(encoding='utf8')
        result=re.sub(r'\$\$([\s\S]*?)\$\$',lambda m:'$$'+wrap(m[1])+'$$',text)
        if text!=result:file.write_text(result,encoding='utf8');count+=1
print('Reformatted equation chains in',count,'files.')
