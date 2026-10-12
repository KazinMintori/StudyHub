"""Make source equation chains fit a mobile line without shortening reasoning."""
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]/'raw_materials/physics/translations/chapter-23'
for name in ['01-the-nang-dien.md','02-dien-the.md']:
 p=root/name;source=p.read_text(encoding='utf8')
 def fix(m):
  body=m[1]
  tag=re.search(r'\\tag\{23\.(\d+)\}',body)
  if not tag:return m[0]
  n=int(tag[1])
  if n in [1,3,4,6,8,12,13,17,18]:
   core=re.sub(r'\\tag\{[^}]+\}','',body).strip()
   core=core.replace(r'\begin{aligned}','').replace(r'\end{aligned}','').strip()
   rows=core.split('\\\\')
   out=[]
   for row in rows:
    row=row.strip().replace('&','')
    if not row:continue
    if '=' in row and not row.startswith('='):
     left,right=row.split('=',1)
     out.extend(['&'+left.strip(), '&='+right.strip()])
    else:out.append('&'+row)
   return '$$\n'+r'\begin{aligned}'+'\n'+('\\\\\n'.join(out))+'\n'+r'\end{aligned}'+'\n'+tag[0]+'\n$$'
  if n in [10,15]:
   coefficient='kq_0' if n==10 else 'k'
   variable='U' if n==10 else 'V'
   formula=rf'''\begin{{aligned}}
{variable}&={coefficient}\frac{{q_1}}{{r_1}}
+{coefficient}\frac{{q_2}}{{r_2}}\\
&\quad+\cdots+{coefficient}\frac{{q_n}}{{r_n}}.
\end{{aligned}}'''
   return '$$\n'+formula+'\n$$\n\nVới chỉ số i chạy từ 1 đến n, viết gọn thành:\n\n$$\n'+rf'{variable}={coefficient}\sum_{{i=1}}^{{n}}\frac{{q_i}}{{r_i}}.'+'\n'+tag[0]+'\n$$'
  if n==11:
   return '$$\n'+r'U=k\sum_{\substack{1\le i<j\\j\le n}}\frac{q_iq_j}{r_{ij}}.'+'\n'+tag[0]+'\n$$'
  return m[0]
 source=re.sub(r'\$\$([\s\S]*?)\$\$',fix,source)
 p.write_text(source,encoding='utf8')
print('Reflowed long numbered equations for chapter23.')
