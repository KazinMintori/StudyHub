"""Match each source equation to its first theoretical statement, once only."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
raw=root/'raw_materials/physics/translations/chapter-25'
files={i:next(raw.glob(f'{i:02d}-*.md')) for i in range(1,7)}
def tag_block(text,needle,number):
    if rf'\tag{{25.{number}}}' in text:return text
    candidates=[m for m in re.finditer(r'\$\$([\s\S]*?)\$\$',text) if needle in m[1]]
    assert candidates,(number,needle)
    m=candidates[0];body=m[1].rstrip()
    # MathJax can display the tag beside an aligned block; the site extracts it
    # into an accessible HTML number for narrow phone layouts.
    replacement='$$'+body+'\n'+rf'\tag{{25.{number}}}'+'\n$$'
    return text[:m.start()]+replacement+text[m.end():]

s=files[1].read_text(encoding='utf8')
combined=r'''\begin{aligned}
I&=n|q|v_dA,\\
J&=\frac IA=n|q|v_d.
\end{aligned}'''
if combined in s:
    s=s.replace(combined,r'''\begin{aligned}
I&=\frac{dQ}{dt}\\
&=n|q|v_dA.
\end{aligned}
\tag{25.2}
$$

$$
\begin{aligned}
J&=\frac IA\\
&=n|q|v_d.
\end{aligned}
\tag{25.3}''',1)
for needle,n in [(r'I&=\frac{dQ}{dt}.',1),(r'\vec J&=nq\vec v_d.',4)]:s=tag_block(s,needle,n)
assert r'\tag{25.2}' in s and r'\tag{25.3}' in s
files[1].write_text(s,encoding='utf8')
s=files[2].read_text(encoding='utf8')
for needle,n in [(r'\rho&=\frac EJ.',5),(r'\rho(T)&=',6)]:s=tag_block(s,needle,n)
files[2].write_text(s,encoding='utf8')
s=files[3].read_text(encoding='utf8')
for needle,n in [(r'\vec E=\rho\vec J.',7),(r'\frac{V}{L}&=',8),(r'R=\frac{V}{I}.',9),(r'R=\rho\frac{L}{A}.',10),(r'V=IR.',11),(r'R(T)&=',12)]:s=tag_block(s,needle,n)
files[3].write_text(s,encoding='utf8')
s=files[4].read_text(encoding='utf8')
needle=r'\mathcal E&=IR.'
if needle in s:s=s.replace(needle,r'\mathcal E&=IR,\\'+'\n'+r'I&=\frac{\mathcal E}{R}.',1)
for needle,n in [(r'W_{\mathrm n}&=',13),(r'I&=\frac{\mathcal E}{R}.',14),(r'V_{ab}=\mathcal E-Ir.',15),(r'I&=\frac{\mathcal E}{R+r}.',16)]:s=tag_block(s,needle,n)
files[4].write_text(s,encoding='utf8')
s=files[5].read_text(encoding='utf8')
for needle,n in [(r'P&=\frac{V_{ab}\,dQ}{dt}',17),(r'P&=V_{ab}I\\',18),(r'P_{\mathrm{ra}}&=',19),(r'P_{\mathrm{vào}}&=',20)]:s=tag_block(s,needle,n)
files[5].write_text(s,encoding='utf8')
s=files[6].read_text(encoding='utf8')
if r'\tag{25.21}' not in s:
    # Remove an incomplete insertion left by an interrupted authoring run.
    start=s.find('Để nối mô hình với các đại lượng đo được')
    end=s.find('Xét một khoảng thời gian',start)
    if start>=0 and end>start:s=s[:start]+s[end:]
    old='$$\n'+r'\rho=\frac{E}{J}.'+'\n$$'
    if old in s:s=s.replace(old,'',1)
    introduction=r'''Để nối mô hình với các đại lượng đo được, dùng định nghĩa điện trở suất và mật độ dòng điện:

$$
\rho=\frac EJ.
\tag{25.21}
$$

$$
\vec J=nq\vec v_d.
\tag{25.22}
$$

n là số electron tự do trong một đơn vị thể tích và q = −e là điện tích mỗi electron.

'''
    target='Xét một khoảng thời gian'
    assert target in s
    s=s.replace(target,introduction+target,1)
for needle,n in [(r'\vec v_d=\frac{q\tau}{m}\vec E.',23),(r'\rho=\frac{m}{ne^2\tau}.',24)]:s=tag_block(s,needle,n)
files[6].write_text(s,encoding='utf8')
for i in [3,4]:
    p=files[i];s=p.read_text(encoding='utf8')
    if s.startswith('# '):s=re.sub(r'^(#+) ',r'\1# ',s,flags=re.M)
    p.write_text(s,encoding='utf8')
tags=[int(n) for p in files.values() for n in re.findall(r'\\tag\{25\.(\d+)\}',p.read_text(encoding='utf8'))]
assert sorted(tags)==list(range(1,25)),tags
print('Numbered all 24 source equations exactly once; raw section headings avoid duplicate page H1.')
