"""Keep a referenced diagram beside each end-of-chapter prompt using it."""
from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
captions={}
for ch in [21,22,23,24]:
 for path in (root/f'raw_materials/physics/translations/chapter-{ch}').glob('*.md'):
  for alt,src in re.findall(r'!\[([^\n]+)\]\(([^)]+)\)',path.read_text(encoding='utf8')):
   captions.setdefault(Path(src).name,alt)
added=[]
for ch,start in [(21,9),(22,7),(23,7)]:
 for path in sorted((root/f'raw_materials/physics/translations/chapter-{ch}').glob('*.md')):
  if int(path.name[:2])<start:continue
  source=path.read_text(encoding='utf8');parts=[];position=0
  matches=list(re.finditer(r'::: exercise ([^\n]+)\n([\s\S]*?)\n:::',source))
  for index,match in enumerate(matches):
   limit=matches[index+1].start() if index+1<len(matches) else len(source)
   before_solution=source[match.end():limit].split('<!-- detailed-solution:',1)[0]
   references=list(dict.fromkeys(re.findall(r'Hình\s+([EPQ]?\d+\.\d+)',match[2])))
   # This biology prompt depends on the illustration in the earlier exercise.
   if ch==23 and match[1].startswith('23.6 '):references.append('E21.18')
   insert=[]
   for ref in references:
    filename='hinh-'+ref.lower().replace('.','-')+'.png'
    refch=re.search(r'\d+',ref)[0]
    image=root/f'docs/vat-ly-2/bai-giang/img/young-{refch}/{filename}'
    if not image.exists() or filename in before_solution:continue
    alt=captions.get(filename,'Hình '+ref+': Sơ đồ cấu hình của bài toán')
    insert.append(f'![{alt}](img/young-{refch}/{filename})')
    added.append({'chapter':ch,'problem':match[1],'reference':ref,'image':str(image.relative_to(root))})
   parts.append(source[position:match.end()])
   if insert:parts.append('\n\n'+'\n\n'.join(insert))
   position=match.end()
  parts.append(source[position:])
  path.write_text(''.join(parts),encoding='utf8')
out=root/'qa/physics/exercise-figure-review.json'
out.write_text(json.dumps({'added':added,'count':len(added)},ensure_ascii=False,indent=2),encoding='utf8')
print('Placed',len(added),'referenced illustrations beside their exercise prompts.')
