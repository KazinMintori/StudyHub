"""Restore natural equation lines now that numbering has its own HTML column."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]/'raw_materials/physics/translations/chapter-23'
equations={
 1:r'''\begin{aligned}
W_{a\to b}&=\int_a^b\vec F\cdot d\vec\ell\\
&=\int_a^bF\cos\varphi\,d\ell
\end{aligned}''',
 3:r'K_a+U_a=K_b+U_b',
 4:r'''\begin{aligned}
W_{a\to b}&=Fd\\
&=q_0Ed
\end{aligned}''',
 6:r'''\begin{aligned}
W_{a\to b}&=-\Delta U\\
&=-q_0E(y_b-y_a)\\
&=q_0E(y_a-y_b)
\end{aligned}''',
 8:r'''\begin{aligned}
W_{a\to b}&=kqq_0\int_{r_a}^{r_b}\frac{dr}{r^2}\\
&=kqq_0\left(\frac1{r_a}-\frac1{r_b}\right)
\end{aligned}''',
 12:r'''\begin{aligned}
V&=U/q_0\\
U&=q_0V
\end{aligned}''',
 13:r'''\begin{aligned}
\frac{W_{a\to b}}{q_0}&=-\frac{U_b-U_a}{q_0}\\
&=V_a-V_b
\end{aligned}''',
 17:r'''\begin{aligned}
W_{a\to b}&=q_0\int_a^b\vec E\cdot d\vec\ell\\
V_a-V_b&=\int_a^b\vec E\cdot d\vec\ell\\
&=\int_a^bE_\parallel\,d\ell
\end{aligned}''',
 18:r'V_a-V_b=-\int_b^a\vec E\cdot d\vec\ell'
}
changed=set()
for path in root.glob('*.md'):
 text=path.read_text(encoding='utf8')
 def rewrite(match):
  number=int(match[1])
  if number not in equations:return match[0]
  changed.add(number)
  return '$$\n'+equations[number]+'\n'+r'\tag{23.'+str(number)+'}\n$$'
 text=re.sub(r'\$\$\s*[^$]*?\\tag\{23\.(\d+)\}\s*\$\$',rewrite,text)
 path.write_text(text,encoding='utf8')
assert changed==set(equations),changed
print('Refined',len(changed),'numbered equations without removing any relation.')
