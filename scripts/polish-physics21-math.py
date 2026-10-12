"""Authored line breaks for the expressions identified by the width audit."""
from pathlib import Path
import re
R=Path(__file__).resolve().parents[1]/'raw_materials/physics/translations/chapter-21'
patches={
'03-dinh-luat-coulomb.md':[(r'F_{1\to3}&',r'''
\begin{aligned}
F_{1\to3}&=\frac{(9.0)(1.0)(5.0)}{0.020^2}10^{-9}\,\mathrm N\\
&\approx112\,\mu\mathrm N,\\
F_{2\to3}&=\frac{(9.0)(3.0)(5.0)}{0.040^2}10^{-9}\,\mathrm N\\
&\approx84\,\mu\mathrm N.
\end{aligned}
''')],
'04-dien-truong-luc-dien.md':[(r'a_y&=',r'''
\begin{aligned}
a_y&=F_y/m=-eE/m\\
&=-\frac{(1.60)(1.00)}{9.11}\\
&\quad\times10^{16}\,\mathrm{m/s^2}\\
&=-1.76\times10^{15}\,\mathrm{m/s^2}.
\end{aligned}
'''),(r'K&=',r'''
\begin{aligned}
K&=\frac12mv^2\\
&=\frac12(9.11)(5.9)^2\\
&\quad\times10^{-19}\,\mathrm J\\
&\approx1.6\times10^{-17}\,\mathrm J.
\end{aligned}
''')],
'05-tinh-dien-truong.md':[(r'\tag{21.8}',r'''
\begin{aligned}
E_x&=\frac{kQx}{(x^2+a^2)^{3/2}},\\
\vec E&=E_x\hat{\mathbf i}.
\end{aligned}
\tag{21.8}
'''),(r'\tag{21.10}',r'''
\begin{aligned}
E_x&=\frac{2k\lambda}{x}\\
&\quad\times(1+x^2/a^2)^{-1/2},\\
\vec E&=E_x\hat{\mathbf i}.
\end{aligned}
\tag{21.10}
'''),(r'\tag{21.11}',r'''
\begin{aligned}
E_x&=\frac{\sigma x}{4\varepsilon_0}\int_{x^2}^{x^2+R^2}u^{-3/2}\,du\\
&=\frac{\sigma x}{2\varepsilon_0}\left(\frac1x-\frac1{\sqrt{x^2+R^2}}\right).
\end{aligned}
$$

$$
\begin{aligned}
E_x&=\frac{\sigma}{2\varepsilon_0}\\
&\quad-\frac{\sigma x}{2\varepsilon_0\sqrt{x^2+R^2}}.
\end{aligned}
\tag{21.11}
''')],
'07-luong-cuc-dien.md':[(r'\tag{21.17}',r'''
U=-pE\cos\varphi.
\tag{21.17}
'''),(r'E_y&=kq\left',r'''
\begin{aligned}
E_y&=\frac{kq}{(y-d/2)^2}\\
&\quad-\frac{kq}{(y+d/2)^2}\\
&=\frac{kq}{y^2}\left(1-\frac d{2y}\right)^{-2}\\
&\quad-\frac{kq}{y^2}\left(1+\frac d{2y}\right)^{-2}.
\end{aligned}
''')],
'09-luyen-tap-huong-dan.md':[(r'F_x&=-k(2.00',r'''
\begin{aligned}
F_{1x}&=-\frac{k(8.00\times10^{-18})}{0.0400^2},\\
F_{2x}&=-\frac{k(2.40\times10^{-18})}{0.0200^2},\\
F_x&=F_{1x}+F_{2x}\\
&=-98.9\,\mu\mathrm N.
\end{aligned}
'''),(r'E_y&=k\left',r'''
\begin{aligned}
E_y&=\frac{k(4.00\times10^{-9})}{0.200^2}\\
&\quad-\frac{k(5.00\times10^{-9})}{0.400^2}\\
&=618\,\mathrm{N/C}.
\end{aligned}
'''),(r'\tau&=(6.13',r'''
\begin{aligned}
pE&=(6.13)(3.00)10^{-25}\,\mathrm{N\,m},\\
\tau&=pE\sin50.0^\circ\\
&=1.41\times10^{-24}\,\mathrm{N\,m},\\
U&=-pE\cos50.0^\circ\\
&=-1.18\times10^{-24}\,\mathrm J.
\end{aligned}
''')],
'10-cau-hoi-thao-luan.md':[(r'Q&\approx10^{-5}',r'''
\begin{aligned}
Q&\approx\frac{10^{-5}e}{2m_p}\\
&=4.8\times10^2\,\mathrm C,\\
F&\approx kQ^2/5.0^2\\
&=8.2\times10^{13}\,\mathrm N.
\end{aligned}
''')],
'11-bai-tap-01-30.md':[(r'F_{2\to1}&=k(2.0',r'''
\begin{aligned}
F_{2\to1}&=kq_1q_2/(0.60)^2\\
&=0.0999\,\mathrm N,\\
F_{Q\to1}&=0.2876\,\mathrm N,\\
F_x&=-0.2876(0.40/0.50)\\
&=-0.230\,\mathrm N,\\
F_y&=0.0999+0.2876(0.30/0.50)\\
&=0.272\,\mathrm N.
\end{aligned}
'''),(r'F_x&=k(6.00',r'''
\begin{aligned}
F_x&=\frac{k(24.0\times10^{-18})}{0.200^2}\\
&\quad-\frac{k(30.0\times10^{-18})}{0.300^2}\\
&=2.40\times10^{-6}\,\mathrm N.
\end{aligned}
'''),(r'F_x&=\frac{k(1.0',r'''
\begin{aligned}
F_x&=\frac{k(1.0)(5.0+3.0)}{0.020^2}10^{-18}\\
&\approx1.8\times10^{-4}\,\mathrm N.
\end{aligned}
'''),(r'F_y&=-k(5.00',r'''
\begin{aligned}
F_y&=-\frac{k(7.50\times10^{-18})}{0.200^2}\\
&\quad-\frac{k(16.0\times10^{-18})}{0.400^2}\\
&=-2.58\,\mu\mathrm N.
\end{aligned}
'''),(r'F&=ke^2\left',r'''
\begin{aligned}
F&=ke^2\frac{10^{18}}{0.170^2}-ke^2\frac{10^{18}}{0.280^2}\\
&\quad+ke^2\frac{10^{18}}{0.190^2}-ke^2\frac{10^{18}}{0.300^2}\\
&=8.87\times10^{-9}\,\mathrm N.
\end{aligned}
'''),(r'F&=2ke^2\left',r'''
\begin{aligned}
F&=2ke^2\frac{10^{18}}{0.180^2}-2ke^2\frac{10^{18}}{0.290^2}\\
&\quad+ke^2\frac{10^{18}}{0.190^2}-ke^2\frac{10^{18}}{0.300^2}\\
&=1.26\times10^{-8}\,\mathrm N.
\end{aligned}
''')],
'12-bai-tap-31-56.md':[(r'E_A&=k\left',r'''
\begin{aligned}
E_A&=\frac{k(12.5\times10^{-9})}{0.100^2}\\
&\quad-\frac{k(6.25\times10^{-9})}{0.150^2}\\
&=8.74\times10^3\,\mathrm{N/C},\\
E_B&=\frac{k(6.25\times10^{-9})}{0.100^2}\\
&\quad+\frac{k(12.5\times10^{-9})}{0.350^2}\\
&=6.54\times10^3\,\mathrm{N/C},\\
F_A&=eE_A=1.40\times10^{-15}\,\mathrm N.
\end{aligned}
'''),(r'F&=2\frac{ke^2}',r'''
\begin{aligned}
F_0&=ke^2/(1.50\times10^{-10})^2,\\
F&=2F_0\cos32.5^\circ\\
&=1.73\times10^{-8}\,\mathrm N.
\end{aligned}
'''),(r'E_x&=k(4.00',r'''
\begin{aligned}
E_x&=k(4.00\times10^{-9})(0.600)\\
&\quad-\frac{k(6.00\times10^{-9})}{0.600^2}\\
&=-128\,\mathrm{N/C},\\
E_y&=k(4.00\times10^{-9})(0.800)\\
&=28.8\,\mathrm{N/C}.
\end{aligned}
'''),(r'F_{\mathrm{nguồn',r'''
\begin{aligned}
E_x&=\frac{kQx}{(x^2+a^2)^{3/2}}\\
&=7.0\,\mathrm{N/C},\\
F&=|q|E=1.75\times10^{-5}\,\mathrm N.
\end{aligned}
''')],
'13-bai-tong-hop-57-80.md':[(r'q_{\\',r'''
\begin{aligned}
q_{\min}&=\sqrt{mgd^2/k}\\
&\approx1.0\,\mathrm{nC},\\
N&=10q_{\min}/e\\
&\sim6\times10^{10}.
\end{aligned}
'''),(r'F_g&=Gm^2',r'''
\begin{aligned}
N&=m/m_p\approx6.0\times10^{23},\\
F_g&=Gm^2/(2R_E)^2\\
&\approx4.1\times10^{-31}\,\mathrm N,\\
F_e&=k(Ne)^2/(2R_E)^2\\
&\approx5.1\times10^5\,\mathrm N.
\end{aligned}
'''),(r'F_z(z)&',r'''
\begin{aligned}
F_z(z)&=\frac{Q\sigma}{2\varepsilon_0}\\
&\quad-\frac{Q\sigma z}{2\varepsilon_0\sqrt{z^2+R^2}}\\
&\quad-Mg,\\
\frac h{\sqrt{h^2+R^2}}&=1-\omega,\\
h&=\frac{R(1-\omega)}{\sqrt{\omega(2-\omega)}}.
\end{aligned}
''')],
'14-bai-tong-hop-81-92.md':[(r'E&=\frac{Q}{2\pi',r'''
\begin{aligned}
E&=\frac{Q}{2\pi\varepsilon_0R^2}\\
&\quad-\frac{Qx}{2\pi\varepsilon_0R^2\sqrt{x^2+R^2}}.
\end{aligned}
'''),(r'E_0&=\frac{k(2.50',r'''
\begin{aligned}
E_0&=\frac{kQ}{0.600\sqrt{0.600^2+0.600^2}},\\
E&=\sqrt2E_0=6.25\times10^4\,\mathrm{N/C},\\
F_e&=eE=1.00\times10^{-14}\,\mathrm N.
\end{aligned}
'''),(r'E_x&=\frac{\sigma x}',r'''
\begin{aligned}
E_x&=\frac{\sigma x}{2\varepsilon_0\sqrt{x^2+R_1^2}}\\
&\quad-\frac{\sigma x}{2\varepsilon_0\sqrt{x^2+R_2^2}}.
\end{aligned}
'''),(r'\lim_{x\to\infty}Ex^2',r'''
\begin{aligned}
\lim_{x\to\infty}Ex^2&=kQ,\\
Q&\approx50/k=5.6\,\mathrm{nC},\\
\lim_{x\to0}E/x&=kQ/a^3,\\
a&\approx(50/700)^{1/3}\\
&=0.41\,\mathrm m.
\end{aligned}
'''),(r'\alpha\Delta&=',r'''
\begin{aligned}
\alpha\Delta&=\sqrt{\Delta^2+R^2}-R,\\
\Delta_{\max}&=\frac{2R\alpha}{1-\alpha^2}.
\end{aligned}
'''),(r'\vec F_1&=',r'''
\begin{aligned}
F_{1x}&=\frac{kQ^2}{L^2\cos u},\\
F_{1y}&=\frac{kQ^2\sin u}{L^2\cos^2u},\\
F_{2x}&=-\frac{kQ^2}{L^2\sin u},\\
F_{2y}&=\frac{kQ^2\cos u}{L^2\sin^2u},\\
\tau_{1z}&=-\frac{kQ^2\sin u}{2L\cos^2u},\\
\tau_{2z}&=\frac{kQ^2\cos u}{2L\sin^2u}.
\end{aligned}
''')],
'15-bai-nang-cao-mcat.md':[(r'dF_{2x}&=k\lambda',r'''
\begin{aligned}
dF_{2x}&=k\lambda^2a\,dy_2\int_0^L\frac{dy_1}{[a^2+(y_2-y_1)^2]^{3/2}}.
\end{aligned}
$$

Đặt $r_0=\sqrt{a^2+y_2^2}$ và $r_L=\sqrt{a^2+(L-y_2)^2}$. Khi đó:

$$
dF_{2x}=\frac{k\lambda^2}{a}\left(\frac{y_2}{r_0}+\frac{L-y_2}{r_L}\right)dy_2.
'''),(r'U(a)&=',r'''
\begin{aligned}
U(a)&=\frac{2kQ^2L}{L^2}\ln\frac{L+\sqrt{a^2+L^2}}a\\
&\quad+\frac{2kQ^2a}{L^2}\\
&\quad-\frac{2kQ^2}{L^2}\sqrt{a^2+L^2}.
\end{aligned}
'''),(r'\begin{cases}',r'''
U_1(\theta)=QaE(\cos\theta-1).
$$

Biểu thức này áp dụng khi $0\le\theta\le\pi$. Khi $\pi\le\theta\le2\pi$:

$$
U_2=-2QaE.
$$

Khi $2\pi\le\theta\le3\pi$:

$$
U_3(\theta)=QaE(\cos\theta-3).
$$

Khi $3\pi\le\theta\le4\pi$:

$$
U_4=-4QaE.
'''),(r'E_y&=-ky_P',r'''
\begin{aligned}
E_y&=-\frac{ky_P|q_1|}{0.050^3}\\
&\quad-\frac{ky_P|q_2|}{0.120^3}\\
&=-1.17\times10^7\,\mathrm{N/C}.
\end{aligned}
'''),(r'E_x(x)&=',r'''
\begin{aligned}
E_x(x)&=\frac{kQ}{L(x+a/2)}\\
&\quad-\frac{kQ}{L(x+a/2+L)},\\
E_y&=0.
\end{aligned}
'''),(r'\int_{a/2}^{a/2+L}',r'''
\begin{aligned}
F&=\frac QL\int_{a/2}^{a/2+L}E_x(x)\,dx\\
&=\frac{kQ^2}{L^2}\ln\frac{(a+L)^2}{a(a+2L)}.
\end{aligned}
''')],
'17-dap-so-bai-le.md':[(r'\frac{|x|}{x}',r'''
\begin{aligned}
E_x&=\frac{\sigma x}{2\varepsilon_0\sqrt{x^2+R_1^2}}\\
&\quad-\frac{\sigma x}{2\varepsilon_0\sqrt{x^2+R_2^2}},\\
\vec E&=E_x\hat{\mathbf i}.
\end{aligned}
'''),(r'W_e&=',r'''
\begin{aligned}
W_e&=-\frac{q\sigma}{2\varepsilon_0}(\sqrt{\Delta^2+R^2}-R),\\
W_g&=mg\Delta,\\
\Delta_{\max}&=\frac{2R\alpha}{1-\alpha^2},\\
\frac12mv^2&=W_e+W_g.
\end{aligned}
'''),(r'dF_{2x}&=',r'''
\begin{aligned}
r_0&=\sqrt{y_2^2+a^2},\\
r_L&=\sqrt{(y_2-L)^2+a^2},\\
dF_{2x}&=\frac{k\lambda^2}{a}\left(\frac{y_2}{r_0}-\frac{y_2-L}{r_L}\right)dy_2.
\end{aligned}
'''),(r'\vec F_2&=',r'''
\begin{aligned}
F_{2x}&=\frac{2kQ^2}{L^2}\\
&\quad\times\left(\sqrt{1+(L/a)^2}-1\right),\\
\vec F_2&=F_{2x}\hat{\mathbf i}.
\end{aligned}
'''),(r'W&=\frac{Q^2}',r'''
\begin{aligned}
W&=\frac{2kQ^2}{L}\ln\frac{L+\sqrt{a^2+L^2}}a\\
&\quad+\frac{2kQ^2a}{L^2}\\
&\quad-\frac{2kQ^2}{L^2}\sqrt{a^2+L^2}.
\end{aligned}
'''),(r'E_x&=\frac{Q}{2\pi',r'''
\begin{aligned}
E_x&=\frac{2kQ}{L(2x+a)}\\
&\quad-\frac{2kQ}{L(2L+2x+a)}.
\end{aligned}
''')]
}
count=0
for name,entries in patches.items():
 p=R/name;source=p.read_text(encoding='utf8')
 for needle,new in entries:
  used=[False]
  def replace(m):
   if not used[0] and needle in m[1]:used[0]=True;return '$$\n'+new.strip()+'\n$$'
   return m[0]
  source=re.sub(r'\$\$([\s\S]*?)\$\$',replace,source)
  if used[0]:count+=1
 p.write_text(source,encoding='utf8')
print('Applied',count,'authored formula layouts.')
