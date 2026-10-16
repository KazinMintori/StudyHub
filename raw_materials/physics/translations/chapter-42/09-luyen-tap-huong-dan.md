## Luyện tập hướng dẫn

Nhóm 12 bài tập sau rèn luyện phương pháp tính toán định lượng cho ba chủ đề trọng tâm của vật lý phân tử và vật lý chất rắn: Phổ dao động – quay của phân tử hai nguyên tử, mô hình khí electron tự do trong kim loại và các đặc trưng dẫn điện của chất bán dẫn.

Các hằng số vật lý sử dụng trong tính toán:
- Tốc độ ánh sáng trong chân không: $c = 3{,}00 \times 10^8\,\mathrm{m/s}$
- Hằng số Planck: $h = 6{,}626 \times 10^{-34}\,\mathrm{J\cdot s}$
- Hằng số Planck rút gọn: $\hbar=\frac{h}{2\pi}$, tức $1{,}055 \times 10^{-34}\,\mathrm{J\cdot s}$
- Điện tích nguyên tố: $e = 1{,}602 \times 10^{-19}\,\mathrm{C}$
- Khối lượng electron: $m_e = 9{,}109 \times 10^{-31}\,\mathrm{kg}$
- Hằng số Boltzmann: $k = 1{,}381 \times 10^{-23}\,\mathrm{J/K}$ (tương đương $8{,}617 \times 10^{-5}\,\mathrm{eV/K}$)
- Đơn vị khối lượng nguyên tử: $1\,\mathrm{u} = 1{,}661 \times 10^{-27}\,\mathrm{kg}$

---

### VP42.3.1

Hai hạt nhân trong phân tử nitơ monoxit ($\mathrm{NO}$) cách nhau một khoảng $0{,}1154\,\mathrm{nm}$. Khối lượng của nguyên tử nitơ phổ biến nhất là $2{,}326 \times 10^{-26}\,\mathrm{kg}$, và khối lượng của nguyên tử oxy phổ biến nhất là $2{,}656 \times 10^{-26}\,\mathrm{kg}$. Hãy xác định:
(a) Khối lượng rút gọn của phân tử $\mathrm{NO}$.
(b) Mômen quán tính của phân tử $\mathrm{NO}$.
(c) Năng lượng (tính theo đơn vị $\mathrm{meV}$) của ba mức năng lượng quay thấp nhất của phân tử $\mathrm{NO}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khoảng cách cân bằng giữa hai hạt nhân: $r=0{,}1154\,\mathrm{nm}$, tức $1{,}154 \times 10^{-10}\,\mathrm{m}$.
- Khối lượng nguyên tử nitơ: $m_1 = 2{,}326 \times 10^{-26}\,\mathrm{kg}$.
- Khối lượng nguyên tử oxy: $m_2 = 2{,}656 \times 10^{-26}\,\mathrm{kg}$.
- Cần tìm: Khối lượng rút gọn $m_r$, mômen quán tính $I$, và năng lượng ba mức quay thấp nhất ($l = 0, 1, 2$) theo $\mathrm{meV}$.

**Hướng đi:**
- Phân tử hai nguyên tử quay quanh khối tâm được quy về một chất điểm duy nhất có khối lượng rút gọn $m_r = \frac{m_1 m_2}{m_1 + m_2}$ chuyển động ở khoảng cách $r$.
- Mômen quán tính của phân tử đối với trục quay đi qua khối tâm và vuông góc với trục liên kết được xác định bởi công thức $I = m_r r^2$.
- Theo cơ học lượng tử, mômen động lượng bị lượng tử hóa dẫn đến mức năng lượng quay gián đoạn $E_l = l(l+1)\frac{\hbar^2}{2I}$ với $l = 0, 1, 2, \dots$

**Lời giải chi tiết:**

(a) Tính khối lượng rút gọn của phân tử $\mathrm{NO}$:
Với $m_1 = 2{,}326 \times 10^{-26}\,\mathrm{kg}$ và $m_2 = 2{,}656 \times 10^{-26}\,\mathrm{kg}$, tích khối lượng $m_1 m_2 \approx 6{,}178 \times 10^{-52}\,\mathrm{kg^2}$ và tổng khối lượng $m_1 + m_2 = 4{,}982 \times 10^{-26}\,\mathrm{kg}$:
$$
\begin{aligned}
m_r &= \frac{m_1 m_2}{m_1 + m_2} \\
&= \frac{6{,}178 \times 10^{-52}\,\mathrm{kg^2}}{4{,}982 \times 10^{-26}\,\mathrm{kg}} \\
&\approx 1{,}240 \times 10^{-26}\,\mathrm{kg}.
\end{aligned}
$$

(b) Tính mômen quán tính của phân tử $\mathrm{NO}$:
Sử dụng giá trị $m_r \approx 1{,}240 \times 10^{-26}\,\mathrm{kg}$ cùng khoảng cách $r=0{,}1154\,\mathrm{nm}$, tức $1{,}154 \times 10^{-10}\,\mathrm{m}$:
$$
\begin{aligned}
I &= m_r r^2 \\
&\approx 1{,}651 \times 10^{-46}\,\mathrm{kg\cdot m^2}.
\end{aligned}
$$

(c) Năng lượng của ba mức quay thấp nhất ($l = 0, 1, 2$):
Với $\hbar = 1{,}055 \times 10^{-34}\,\mathrm{J\cdot s}$ và $I \approx 1{,}651 \times 10^{-46}\,\mathrm{kg\cdot m^2}$, hệ số năng lượng đặc trưng là:
$$
\begin{aligned}
\epsilon_0 &= \frac{\hbar^2}{2I} \\
&\approx 3{,}371 \times 10^{-23}\,\mathrm{J}.
\end{aligned}
$$

Đổi sang đơn vị milielectron-volt ($\mathrm{meV}$):
$$
\begin{aligned}
\epsilon_0 &= \frac{3{,}371 \times 10^{-23}\,\mathrm{J}}{1{,}602 \times 10^{-22}\,\mathrm{J/meV}} \\
&\approx 0{,}2102\,\mathrm{meV}.
\end{aligned}
$$

Từ đó, ta tính các mức năng lượng $E_l = l(l+1)\epsilon_0$:
- Với mức $l = 0$:
$$
E_0 = 0\,\mathrm{meV}.
$$

- Với mức $l = 1$:
$$
\begin{aligned}
E_1 &= 1(2)\epsilon_0 \\
&= 2(0{,}2102\,\mathrm{meV}) \\
&\approx 0{,}4203\,\mathrm{meV}.
\end{aligned}
$$

- Với mức $l = 2$:
$$
\begin{aligned}
E_2 &= 2(3)\epsilon_0 \\
&= 6(0{,}2102\,\mathrm{meV}) \\
&\approx 1{,}261\,\mathrm{meV}.
\end{aligned}
$$

Ba mức năng lượng quay thấp nhất của phân tử $\mathrm{NO}$ lần lượt là $0\,\mathrm{meV}$, $0{,}4203\,\mathrm{meV}$ và $1{,}261\,\mathrm{meV}$.

</details>

---

### VP42.3.2

Mức năng lượng quay $l = 2$ của phân tử hiđro clorua ($\mathrm{HCl}$) có giá trị $7{,}90\,\mathrm{meV}$. Khối lượng của nguyên tử hiđro phổ biến nhất là $1{,}674 \times 10^{-27}\,\mathrm{kg}$, và khối lượng của nguyên tử clo phổ biến nhất là $5{,}807 \times 10^{-26}\,\mathrm{kg}$. Hãy xác định:
(a) Mômen quán tính của phân tử $\mathrm{HCl}$.
(b) Khối lượng rút gọn của phân tử $\mathrm{HCl}$.
(c) Khoảng cách giữa hạt nhân $\mathrm{H}$ và hạt nhân $\mathrm{Cl}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Mức năng lượng quay ứng với $l = 2$: $E_2 = 7{,}90\,\mathrm{meV}$. Đổi sang joule: $E_2 \approx 1{,}266 \times 10^{-21}\,\mathrm{J}$ (với $1\,\mathrm{eV} = 1{,}6022 \times 10^{-19}\,\mathrm{J}$).
- Khối lượng nguyên tử $\mathrm{H}$: $m_1 = 1{,}674 \times 10^{-27}\,\mathrm{kg}$.
- Khối lượng nguyên tử $\mathrm{Cl}$: $m_2 = 5{,}807 \times 10^{-26}\,\mathrm{kg}$.
- Cần tìm: Mômen quán tính $I$, khối lượng rút gọn $m_r$, và khoảng cách liên hạt nhân $r$.

**Hướng đi:**
- Năng lượng quay được lượng tử hóa theo công thức $E_l = l(l+1)\frac{\hbar^2}{2I}$. Với $l = 2$, ta có $E_2 = \frac{3\hbar^2}{I}$, cho phép giải trực tiếp mômen quán tính $I$.
- Khối lượng rút gọn của hệ hai vật điểm tính bằng $m_r = \frac{m_1 m_2}{m_1 + m_2}$.
- Khi đã biết mômen quán tính và khối lượng rút gọn, khoảng cách giữa hai hạt nhân được xác định từ hệ thức $I=m_r r^2$, suy ra $r=\sqrt{I / m_r}$.

**Lời giải chi tiết:**

(a) Xác định mômen quán tính $I$ của phân tử $\mathrm{HCl}$:
Biểu thức mức năng lượng quay tại $l = 2$ là:
$$
\begin{aligned}
E_2 &= 2(2+1)\frac{\hbar^2}{2I} \\
&= \frac{3\hbar^2}{I}.
\end{aligned}
$$

Suy ra mômen quán tính:
$$
\begin{aligned}
I &= \frac{3\hbar^2}{E_2} \\
&= \frac{3(1{,}055 \times 10^{-34}\,\mathrm{J\cdot s})^2}{1{,}266 \times 10^{-21}\,\mathrm{J}} \\
&\approx 2{,}64 \times 10^{-47}\,\mathrm{kg\cdot m^2}.
\end{aligned}
$$

(b) Xác định khối lượng rút gọn $m_r$:
Với $m_1 = 1{,}674 \times 10^{-27}\,\mathrm{kg}$ và $m_2 = 5{,}807 \times 10^{-26}\,\mathrm{kg}$, tích khối lượng $m_1 m_2 \approx 9{,}721 \times 10^{-53}\,\mathrm{kg^2}$ và tổng $m_1 + m_2 \approx 5{,}974 \times 10^{-26}\,\mathrm{kg}$:
$$
\begin{aligned}
m_r &= \frac{m_1 m_2}{m_1 + m_2} \\
&= \frac{9{,}721 \times 10^{-53}\,\mathrm{kg^2}}{5{,}974 \times 10^{-26}\,\mathrm{kg}} \\
&\approx 1{,}627 \times 10^{-27}\,\mathrm{kg}.
\end{aligned}
$$

(c) Xác định khoảng cách giữa hai hạt nhân $r$:
Từ mối liên hệ giữa mômen quán tính và khoảng cách liên hạt nhân:
$$
\begin{aligned}
r &= \sqrt{\frac{I}{m_r}} \\
&= \sqrt{\frac{2{,}64 \times 10^{-47}\,\mathrm{kg\cdot m^2}}{1{,}627 \times 10^{-27}\,\mathrm{kg}}} \\
&\approx 1{,}27 \times 10^{-10}\,\mathrm{m} \\
&= 0{,}127\,\mathrm{nm}.
\end{aligned}
$$

Khoảng cách cân bằng giữa hai hạt nhân trong phân tử $\mathrm{HCl}$ là $0{,}127\,\mathrm{nm}$.

</details>

---

### VP42.3.3

Khối lượng của nguyên tử silic phổ biến nhất là $4{,}646 \times 10^{-26}\,\mathrm{kg}$, và khối lượng của nguyên tử oxy phổ biến nhất là $2{,}656 \times 10^{-26}\,\mathrm{kg}$. Khi một phân tử silic monoxit ($\mathrm{SiO}$) thực hiện bước chuyển mức giữa hai mức năng lượng quay $l = 1$ và $l = 0$, nó phát ra một photon có bước sóng $6{,}882\,\mathrm{mm}$. Hãy xác định:
(a) Mômen quán tính của phân tử $\mathrm{SiO}$.
(b) Khối lượng rút gọn của phân tử $\mathrm{SiO}$.
(c) Khoảng cách giữa hai hạt nhân $\mathrm{Si}$ và $\mathrm{O}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng nguyên tử silic: $m_1 = 4{,}646 \times 10^{-26}\,\mathrm{kg}$.
- Khối lượng nguyên tử oxy: $m_2 = 2{,}656 \times 10^{-26}\,\mathrm{kg}$.
- Bước sóng photon phát xạ khi chuyển mức $l = 1 \to 0$: $\lambda=6{,}882\,\mathrm{mm}$, tức $6{,}882 \times 10^{-3}\,\mathrm{m}$.
- Cần tìm: Mômen quán tính $I$, khối lượng rút gọn $m_r$, và khoảng cách liên hạt nhân $r$.

**Hướng đi:**
- Khi phân tử chuyển mức từ $l = 1$ về $l = 0$, năng lượng mất đi là $\Delta E = E_1 - E_0 = \frac{\hbar^2}{I}$.
- Năng lượng này truyền trọn vẹn cho photon phát ra: $\Delta E = \frac{hc}{\lambda}$. Cân bằng hai vế giúp ta tính được mômen quán tính $I$.
- Khối lượng rút gọn $m_r$ được tính từ khối lượng hai nguyên tử.
- Khoảng cách giữa hai hạt nhân được suy ra từ công thức $r = \sqrt{I / m_r}$.

**Lời giải chi tiết:**

(a) Xác định mômen quán tính $I$:
Độ biến thiên năng lượng quay trong bước chuyển mức $l = 1 \to l = 0$ là:
$$
\begin{aligned}
\Delta E &= 1(1+1)\frac{\hbar^2}{2I} - 0 \\
&= \frac{\hbar^2}{I}.
\end{aligned}
$$

Theo định luật bảo toàn năng lượng:
$$
\frac{\hbar^2}{I} = \frac{hc}{\lambda} = \frac{2\pi \hbar c}{\lambda}.
$$

Suy ra mômen quán tính:
Tích $h\lambda \approx 4{,}560 \times 10^{-36}\,\mathrm{J\cdot s\cdot m}$ và mẫu số $4\pi^2 c \approx 1{,}184 \times 10^{10}\,\mathrm{m/s}$:
$$
\begin{aligned}
I &= \frac{h \lambda}{4\pi^2 c} \\
&= \frac{4{,}560 \times 10^{-36}\,\mathrm{J\cdot s\cdot m}}{1{,}184 \times 10^{10}\,\mathrm{m/s}} \\
&\approx 3{,}853 \times 10^{-46}\,\mathrm{kg\cdot m^2}.
\end{aligned}
$$

(b) Xác định khối lượng rút gọn $m_r$:
Với $m_1 = 4{,}646 \times 10^{-26}\,\mathrm{kg}$ và $m_2 = 2{,}656 \times 10^{-26}\,\mathrm{kg}$, tích khối lượng $m_1 m_2 \approx 1{,}234 \times 10^{-51}\,\mathrm{kg^2}$ và tổng $m_1 + m_2 = 7{,}302 \times 10^{-26}\,\mathrm{kg}$:
$$
\begin{aligned}
m_r &= \frac{m_1 m_2}{m_1 + m_2} \\
&= \frac{1{,}234 \times 10^{-51}\,\mathrm{kg^2}}{7{,}302 \times 10^{-26}\,\mathrm{kg}} \\
&\approx 1{,}690 \times 10^{-26}\,\mathrm{kg}.
\end{aligned}
$$

(c) Xác định khoảng cách giữa hai hạt nhân $r$:
Từ mối liên hệ $I = m_r r^2$, tỷ số $I / m_r \approx 2{,}280 \times 10^{-20}\,\mathrm{m^2}$:
$$
\begin{aligned}
r &= \sqrt{\frac{I}{m_r}} \\
&= \sqrt{2{,}280 \times 10^{-20}\,\mathrm{m^2}} \\
&\approx 1{,}510 \times 10^{-10}\,\mathrm{m} \\
&= 0{,}1510\,\mathrm{nm}.
\end{aligned}
$$

Khoảng cách cân bằng giữa hai hạt nhân trong phân tử $\mathrm{SiO}$ là $0{,}1510\,\mathrm{nm}$.

</details>

---

### VP42.3.4

Một phân tử $\mathrm{CO}$ ban đầu ở mức dao động $n = 2$. Nếu phân tử này đồng thời mất cả năng lượng dao động và năng lượng quay để phát ra một photon, hãy tìm bước sóng và tần số của photon phát ra nếu số lượng tử mômen động lượng ban đầu là:
(a) $l = 3$.
(b) $l = 2$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Phân tử: Cacbon monoxit ($\mathrm{CO}$).
- Khoảng cách giữa các mức năng lượng dao động kế tiếp: $\hbar\omega = 0{,}2690\,\mathrm{eV}$.
- Hằng số năng lượng quay: $\epsilon_0=\frac{\hbar^2}{2I}$, tức $0{,}2395\,\mathrm{meV}$, tức $0{,}0002395\,\mathrm{eV}$ (tương ứng khoảng cách giữa hai mức quay $l = 0$ và $l = 1$ là $2\epsilon_0 = 0{,}479\,\mathrm{meV}$).
- Trạng thái ban đầu: Mức dao động $n = 2$.
- Phân tử mất cả năng lượng dao động và quay: Bước chuyển dao động thỏa mãn quy tắc chọn lọc $\Delta n = -1$ (chuyển từ $n = 2$ xuống $n = 1$), và bước chuyển quay thỏa mãn $\Delta l = -1$ để năng lượng quay giảm.
- Cần tìm: Tần số $f$ và bước sóng $\lambda$ của photon phát ra khi:
  (a) Trạng thái quay ban đầu là $l = 3$.
  (b) Trạng thái quay ban đầu là $l = 2$.

**Hướng đi:**
- Năng lượng toàn phần của trạng thái dao động – quay trong phân tử hai nguyên tử là $E_{nl}=E_n+E_l$, với $E_n=(n+\frac12)\hbar\omega$ và $E_l=l(l+1)\hbar^2/(2I)$.
- Khi phân tử mất cả năng lượng dao động và quay, bước chuyển tương ứng với nhánh $P$ với $\Delta n = -1$ và $\Delta l = -1$.
- Năng lượng phát ra bằng hiệu năng lượng giữa trạng thái ban đầu và trạng thái cuối: $E_{ph} = \hbar\omega + \Delta E_{rot}$, với $\Delta E_{rot} = 2l\epsilon_0$.
- Tần số photon tính bằng $f = E_{ph}/h$, và bước sóng tính bằng $\lambda = c/f$.

**Lời giải chi tiết:**

(a) Trường hợp số lượng tử quay ban đầu $l = 3$:
Vì phân tử mất năng lượng quay, trạng thái quay cuối cùng là $l' = l - 1 = 2$.
Độ giảm năng lượng quay của phân tử là:
$$
\begin{aligned}
\Delta E_{rot} &= [3(4) - 2(3)]\epsilon_0 \\
&= 6\epsilon_0 \\
&= 3(2\epsilon_0) \\
&= 3(0{,}479\,\mathrm{meV}) \\
&= 1{,}437\,\mathrm{meV} \\
&= 0{,}001437\,\mathrm{eV}.
\end{aligned}
$$

Độ giảm năng lượng dao động là $\Delta E_{vib} = \hbar\omega = 0{,}2690\,\mathrm{eV}$.
Năng lượng toàn phần của photon phát ra:
Tổng năng lượng $\Delta E_{vib} = 0{,}2690\,\mathrm{eV}$ và $\Delta E_{rot} = 0{,}001437\,\mathrm{eV}$:
$$
\begin{aligned}
E_{ph} &= \Delta E_{vib} + \Delta E_{rot} \\
&= 0{,}270437\,\mathrm{eV}.
\end{aligned}
$$

Đổi sang joule với $1\,\mathrm{eV} = 1{,}6022 \times 10^{-19}\,\mathrm{J}$:
$$
E_{ph} \approx 4{,}333 \times 10^{-20}\,\mathrm{J}.
$$

Tần số của photon:
$$
\begin{aligned}
f &= \frac{E_{ph}}{h} \\
&= \frac{4{,}333 \times 10^{-20}\,\mathrm{J}}{6{,}626 \times 10^{-34}\,\mathrm{J\cdot s}} \\
&\approx 6{,}538 \times 10^{13}\,\mathrm{Hz}.
\end{aligned}
$$

Bước sóng của photon:
$$
\begin{aligned}
\lambda &= \frac{c}{f} \\
&= \frac{3{,}00 \times 10^8\,\mathrm{m/s}}{6{,}538 \times 10^{13}\,\mathrm{Hz}} \\
&\approx 4{,}585 \times 10^{-6}\,\mathrm{m} \\
&= 4{,}585\,\mu\mathrm{m}.
\end{aligned}
$$

(b) Trường hợp số lượng tử quay ban đầu $l = 2$:
Trạng thái quay cuối cùng là $l' = l - 1 = 1$.
Độ giảm năng lượng quay của phân tử là:
$$
\begin{aligned}
\Delta E_{rot} &= [2(3) - 1(2)]\epsilon_0 \\
&= 4\epsilon_0 \\
&= 2(2\epsilon_0) \\
&= 2(0{,}479\,\mathrm{meV}) \\
&= 0{,}958\,\mathrm{meV} \\
&= 0{,}000958\,\mathrm{eV}.
\end{aligned}
$$

Năng lượng photon phát ra:
Tổng năng lượng $\Delta E_{vib} = 0{,}2690\,\mathrm{eV}$ và $\Delta E_{rot} = 0{,}000958\,\mathrm{eV}$:
$$
\begin{aligned}
E_{ph} &= \Delta E_{vib} + \Delta E_{rot} \\
&= 0{,}269958\,\mathrm{eV}.
\end{aligned}
$$

Đổi sang joule với $1\,\mathrm{eV} = 1{,}6022 \times 10^{-19}\,\mathrm{J}$:
$$
E_{ph} \approx 4{,}325 \times 10^{-20}\,\mathrm{J}.
$$

Tần số của photon:
$$
\begin{aligned}
f &= \frac{E_{ph}}{h} \\
&= \frac{4{,}325 \times 10^{-20}\,\mathrm{J}}{6{,}626 \times 10^{-34}\,\mathrm{J\cdot s}} \\
&\approx 6{,}527 \times 10^{13}\,\mathrm{Hz}.
\end{aligned}
$$

Bước sóng của photon:
$$
\begin{aligned}
\lambda &= \frac{c}{f} \\
&= \frac{3{,}00 \times 10^8\,\mathrm{m/s}}{6{,}527 \times 10^{13}\,\mathrm{Hz}} \\
&\approx 4{,}593 \times 10^{-6}\,\mathrm{m} \\
&= 4{,}593\,\mu\mathrm{m}.
\end{aligned}
$$

</details>

---

### VP42.7.1

Đối với các electron tự do trong chất rắn có mức năng lượng Fermi $E_F$ tại nhiệt độ $T$, hãy tìm mức năng lượng $E$ để xác suất bị chiếm của một trạng thái tại mức năng lượng đó bằng:
(a) $0{,}33$.
(b) $0{,}90$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Năng lượng Fermi: $E_F$.
- Nhiệt độ tuyệt đối: $T$.
- Cần tìm: Biểu thức năng lượng $E$ theo $E_F$ và $kT$ sao cho xác suất chiếm mức $f(E)$ nhận các giá trị:
  (a) $f(E) = 0{,}33$.
  (b) $f(E) = 0{,}90$.

**Hướng đi:**
- Xác suất chiếm một trạng thái lượng tử có năng lượng $E$ bởi một electron tuân theo hàm phân bố Fermi–Dirac:
$$
f(E) = \frac{1}{e^{(E - E_F)/kT} + 1}.
$$
- Nghịch đảo phương trình:
$$
e^{(E - E_F)/kT} = \frac{1}{f(E)} - 1.
$$
- Lấy logarit tự nhiên hai vế giúp giải trực tiếp tỷ số $(E - E_F)/kT$.

**Lời giải chi tiết:**

(a) Với xác suất chiếm $f(E) = 0{,}33$:
Áp dụng công thức biến đổi từ hàm phân bố Fermi–Dirac:
$$
\begin{aligned}
e^{(E - E_F)/kT} &= \frac{1}{0{,}33} - 1 \\
&\approx 3{,}0303 - 1 \\
&= 2{,}0303.
\end{aligned}
$$

Lấy logarit tự nhiên hai vế:
$$
\begin{aligned}
\frac{E - E_F}{kT} &= \ln(2{,}0303) \\
&\approx +0{,}71.
\end{aligned}
$$

Suy ra mức năng lượng tương ứng:
$$
E = E_F + 0{,}71 kT.
$$

(b) Với xác suất chiếm $f(E) = 0{,}90$:
Tương tự:
$$
\begin{aligned}
e^{(E - E_F)/kT} &= \frac{1}{0{,}90} - 1 \\
&\approx 1{,}1111 - 1 \\
&= 0{,}1111.
\end{aligned}
$$

Lấy logarit tự nhiên:
$$
\begin{aligned}
\frac{E - E_F}{kT} &= \ln(0{,}1111) \\
&\approx -2{,}20.
\end{aligned}
$$

Suy ra mức năng lượng tương ứng:
$$
E = E_F - 2{,}2 kT.
$$

Như vậy, trạng thái có xác suất chiếm $0{,}33$ nằm cao hơn mức Fermi một lượng $0{,}71 kT$, trong khi trạng thái có xác suất chiếm $0{,}90$ nằm sâu dưới mức Fermi một khoảng $2{,}2 kT$.

</details>

---

### VP42.7.2

Hằng số Boltzmann có giá trị $k = 8{,}617 \times 10^{-5}\,\mathrm{eV/K}$. Đối với một khối kim loại ở nhiệt độ phòng ($293\,\mathrm{K}$), hãy tính xác suất chiếm một trạng thái electron nếu mức năng lượng của nó:
(a) Nằm dưới mức Fermi $0{,}0250\,\mathrm{eV}$.
(b) Nằm trên mức Fermi $0{,}0400\,\mathrm{eV}$.
(c) Nằm trên mức Fermi $0{,}100\,\mathrm{eV}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hằng số Boltzmann: $k = 8{,}617 \times 10^{-5}\,\mathrm{eV/K}$.
- Nhiệt độ khối kim loại: $T = 293\,\mathrm{K}$.
- Cần tính xác suất chiếm trạng thái $f(E)$ khi hiệu năng lượng $E - E_F$ nhận các giá trị:
  (a) $E - E_F = -0{,}0250\,\mathrm{eV}$.
  (b) $E - E_F = +0{,}0400\,\mathrm{eV}$.
  (c) $E - E_F = +0{,}100\,\mathrm{eV}$.

**Hướng đi:**
- Trước hết, tính năng lượng nhiệt đặc trưng $kT$ ở nhiệt độ đã cho.
- Áp dụng trực tiếp hàm phân bố Fermi–Dirac $f(E) = \frac{1}{e^{(E - E_F)/kT} + 1}$.

**Lời giải chi tiết:**

Tính năng lượng nhiệt $kT$ tại $T = 293\,\mathrm{K}$ với $k = 8{,}617 \times 10^{-5}\,\mathrm{eV/K}$:
$$
kT \approx 0{,}02525\,\mathrm{eV}.
$$

(a) Năng lượng nằm dưới mức Fermi $0{,}0250\,\mathrm{eV}$ ($E - E_F = -0{,}0250\,\mathrm{eV}$):
Số mũ trong hàm Fermi–Dirac:
$$
\begin{aligned}
\frac{E - E_F}{kT} &= \frac{-0{,}0250\,\mathrm{eV}}{0{,}02525\,\mathrm{eV}} \\
&\approx -0{,}9901.
\end{aligned}
$$

Xác suất chiếm mức:
$$
\begin{aligned}
f(E) &= \frac{1}{e^{-0{,}9901} + 1} \\
&= \frac{1}{0{,}3715 + 1} \\
&\approx 0{,}729.
\end{aligned}
$$

(b) Năng lượng nằm trên mức Fermi $0{,}0400\,\mathrm{eV}$ ($E - E_F = +0{,}0400\,\mathrm{eV}$):
Số mũ trong hàm phân bố:
$$
\begin{aligned}
\frac{E - E_F}{kT} &= \frac{+0{,}0400\,\mathrm{eV}}{0{,}02525\,\mathrm{eV}} \\
&\approx +1{,}5842.
\end{aligned}
$$

Xác suất chiếm mức:
$$
\begin{aligned}
f(E) &= \frac{1}{e^{1{,}5842} + 1} \\
&= \frac{1}{4{,}875 + 1} \\
&\approx 0{,}170.
\end{aligned}
$$

(c) Năng lượng nằm trên mức Fermi $0{,}100\,\mathrm{eV}$ ($E - E_F = +0{,}100\,\mathrm{eV}$):
Số mũ trong hàm phân bố:
$$
\begin{aligned}
\frac{E - E_F}{kT} &= \frac{+0{,}100\,\mathrm{eV}}{0{,}02525\,\mathrm{eV}} \\
&\approx +3{,}9604.
\end{aligned}
$$

Xác suất chiếm mức:
$$
\begin{aligned}
f(E) &= \frac{1}{e^{3{,}9604} + 1} \\
&= \frac{1}{52{,}48 + 1} \\
&\approx 0{,}0187.
\end{aligned}
$$

</details>

---

### VP42.7.3

Bạc chứa mật độ electron tự do là $5{,}8 \times 10^{28}\,\mathrm{m}^{-3}$. Tại nhiệt độ không độ tuyệt đối ($0\,\mathrm{K}$), hãy xác định:
(a) Năng lượng Fermi của bạc (tính theo đơn vị $\mathrm{J}$ và $\mathrm{eV}$).
(b) Tốc độ của electron có mức năng lượng này.
(c) Mật độ trạng thái (tính theo $\text{trạng thái/J}$ và $\text{trạng thái/eV}$) tại mức năng lượng Fermi cho một khối bạc có thể tích $1{,}0\,\mathrm{cm}^3$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Mật độ số hạt electron dẫn: $n = \frac{N}{V} = 5{,}8 \times 10^{28}\,\mathrm{m}^{-3}$.
- Nhiệt độ: $T = 0\,\mathrm{K}$.
- Thể tích khối bạc: $V=1{,}0\,\mathrm{cm}^3$, tức $1{,}0 \times 10^{-6}\,\mathrm{m}^3$.
- Cần tìm: Năng lượng Fermi $E_F$ (theo $\mathrm{J}$ và $\mathrm{eV}$), tốc độ Fermi $v_F$, mật độ trạng thái $g(E_F)$ theo $\text{trạng thái/J}$ và $\text{trạng thái/eV}$.

**Hướng đi:**
- Trong mô hình khí electron tự do, năng lượng Fermi tại $0\,\mathrm{K}$ liên hệ trực tiếp với mật độ hạt qua công thức $E_F = \frac{\hbar^2}{2m_e}(3\pi^2 n)^{2/3}$.
- Tốc độ Fermi liên hệ với động năng cực đại qua biểu thức phi tương đối tính $E_F=\frac{1}{2}m_e v_F^2$, suy ra $v_F=\sqrt{2E_F / m_e}$.
- Mật độ trạng thái toàn phần tại năng lượng $E_F$ cho khối có thể tích $V$ có thể tính nhanh bằng hệ thức vi tích phân $g(E_F) = \frac{3N}{2E_F}$, trong đó $N = nV$ là tổng số electron tự do.

**Lời giải chi tiết:**

(a) Năng lượng Fermi của bạc:
Tính thừa số mật độ với $n = 5{,}8 \times 10^{28}\,\mathrm{m}^{-3}$:
$$
3\pi^2 n \approx 1{,}717 \times 10^{30}\,\mathrm{m}^{-3}.
$$

Lũy thừa bậc $2/3$ của đại lượng này là $(3\pi^2 n)^{2/3} \approx 1{,}434 \times 10^{20}\,\mathrm{m}^{-2}$.

Với $\frac{\hbar^2}{2m_e} \approx 6{,}108 \times 10^{-39}\,\mathrm{J\cdot m^2}$ và $(3\pi^2 n)^{2/3} \approx 1{,}434 \times 10^{20}\,\mathrm{m}^{-2}$:
$$
\begin{aligned}
E_F &= \frac{\hbar^2}{2m_e}(3\pi^2 n)^{2/3} \\
&\approx 8{,}76 \times 10^{-19}\,\mathrm{J} \\
&\approx 8{,}8 \times 10^{-19}\,\mathrm{J}.
\end{aligned}
$$

Đổi sang đơn vị electron-volt:
$$
\begin{aligned}
E_F &= \frac{8{,}76 \times 10^{-19}\,\mathrm{J}}{1{,}602 \times 10^{-19}\,\mathrm{J/eV}} \\
&\approx 5{,}5\,\mathrm{eV}.
\end{aligned}
$$

(b) Tốc độ Fermi $v_F$:
Từ động năng của electron tại mặt Fermi:
$$
\begin{aligned}
v_F &= \sqrt{\frac{2E_F}{m_e}} \\
&= \sqrt{\frac{2(8{,}76 \times 10^{-19}\,\mathrm{J})}{9{,}109 \times 10^{-31}\,\mathrm{kg}}} \\
&\approx 1{,}39 \times 10^6\,\mathrm{m/s} \\
&\approx 1{,}4 \times 10^6\,\mathrm{m/s}.
\end{aligned}
$$

(c) Mật độ trạng thái $g(E_F)$ tại mức năng lượng Fermi:
Tổng số electron tự do trong mẫu là:
$$
N = nV = 5{,}8 \times 10^{22}.
$$

Mật độ trạng thái tại mức năng lượng Fermi với $2E_F \approx 1{,}752 \times 10^{-18}\,\mathrm{J}$:
$$
\begin{aligned}
g(E_F) &= \frac{3N}{2E_F} \\
&\approx 9{,}9 \times 10^{40}\,\mathrm{J}^{-1}.
\end{aligned}
$$

Giá trị này tương ứng với $9{,}9 \times 10^{40}\,\text{trạng thái/J}$.
Đổi sang đơn vị theo $\mathrm{eV}$ với $1\,\mathrm{eV} = 1{,}6022 \times 10^{-19}\,\mathrm{J}$:
$$
g(E_F) \approx 1{,}6 \times 10^{22}\,\mathrm{eV}^{-1}.
$$

Tương ứng với $1{,}6 \times 10^{22}\,\text{trạng thái/eV}$.

</details>

---

### VP42.7.4

Nếu tích $kT$ rất nhỏ so với năng lượng Fermi tại không độ tuyệt đối, thì năng lượng Fermi tại nhiệt độ $T$ thực tế không khác biệt đáng kể so với tại $0\,\mathrm{K}$. Sử dụng kết quả của bài trước ($E_F \approx 5{,}47\,\mathrm{eV}$ đối với bạc), hãy tìm mức năng lượng của electron (tính theo $\mathrm{eV}$) để xác suất chiếm trạng thái của electron bằng:
(a) $0{,}92$.
(b) $1{,}0 \times 10^{-4}$ đối với bạc ở nhiệt độ phòng ($293\,\mathrm{K}$).

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Năng lượng Fermi của bạc: $E_F \approx 5{,}47\,\mathrm{eV}$ (làm tròn $5{,}5\,\mathrm{eV}$).
- Nhiệt độ phòng: $T=293\,\mathrm{K}$, suy ra $kT\approx0{,}02525\,\mathrm{eV}$.
- Cần tìm mức năng lượng $E$ (theo $\mathrm{eV}$) khi:
  (a) Xác suất chiếm $f(E) = 0{,}92$.
  (b) Xác suất chiếm $f(E) = 1{,}0 \times 10^{-4}$.

**Hướng đi:**
- Dùng hệ thức rút ra từ hàm phân bố Fermi–Dirac:
$$
e^{(E - E_F)/kT} = \frac{1}{f(E)} - 1.
$$
- Lấy logarit tự nhiên hai vế giúp tìm độ lệch năng lượng $\Delta E=E - E_F$, tức $kT \ln[1/f(E) - 1]$.

**Lời giải chi tiết:**

(a) Với xác suất chiếm $f(E) = 0{,}92$:
Tính hệ số logarit:
$$
\begin{aligned}
\frac{1}{0{,}92} - 1 &\approx 0{,}08696, \\
\ln(0{,}08696) &\approx -2{,}442.
\end{aligned}
$$

Độ lệch năng lượng so với mức Fermi với $kT \approx 0{,}02525\,\mathrm{eV}$:
$$
\begin{aligned}
\Delta E &= -2{,}442 kT \\
&\approx -0{,}0617\,\mathrm{eV}.
\end{aligned}
$$

Mức năng lượng tương ứng:
$$
\begin{aligned}
E &= E_F + \Delta E \\
&= 5{,}47\,\mathrm{eV} - 0{,}0617\,\mathrm{eV} \\
&\approx 5{,}4\,\mathrm{eV}.
\end{aligned}
$$

(b) Với xác suất chiếm $f(E) = 1{,}0 \times 10^{-4}$:
Vì $f(E) \ll 1$, ta có $\frac{1}{f(E)} - 1 \approx 10^4$.
Tính hệ số logarit:
$$
\ln(10^4) \approx 9{,}210.
$$

Độ lệch năng lượng so với mức Fermi với $kT \approx 0{,}02525\,\mathrm{eV}$:
$$
\begin{aligned}
\Delta E &= 9{,}210 kT \\
&\approx +0{,}2325\,\mathrm{eV}.
\end{aligned}
$$

Mức năng lượng tương ứng:
$$
\begin{aligned}
E &= E_F + \Delta E \\
&= 5{,}47\,\mathrm{eV} + 0{,}2325\,\mathrm{eV} \\
&\approx 5{,}7\,\mathrm{eV}.
\end{aligned}
$$

</details>

---

### VP42.9.1

Đối với một chất bán dẫn nhất định, mức năng lượng Fermi nằm chính giữa khe cấm năng lượng. Nếu nhiệt độ của khối bán dẫn là $285\,\mathrm{K}$, hãy tính xác suất chiếm một trạng thái tại đáy vùng dẫn nếu độ rộng khe cấm là:
(a) $0{,}500\,\mathrm{eV}$.
(b) $1{,}50\,\mathrm{eV}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Nhiệt độ khối bán dẫn: $T = 285\,\mathrm{K}$.
- Mức Fermi nằm ở giữa khe cấm: $E_c - E_F = \frac{1}{2} E_g$.
- Cần tính xác suất chiếm trạng thái tại đáy vùng dẫn $f(E_c)$ với:
  (a) $E_g = 0{,}500\,\mathrm{eV}$, suy ra $E_c - E_F = 0{,}250\,\mathrm{eV}$.
  (b) $E_g = 1{,}50\,\mathrm{eV}$, suy ra $E_c - E_F = 0{,}750\,\mathrm{eV}$.

**Hướng đi:**
- Năng lượng nhiệt được tính bằng $kT$. Dùng $k=8{,}617\times10^{-5}\,\mathrm{eV/K}$ và $T=285\,\mathrm K$.
- Áp dụng hàm phân bố Fermi–Dirac $f(E_c)=\frac{1}{e^{(E_c - E_F)/kT} + 1}$, xấp xỉ $e^{-(E_c - E_F)/kT}$ khi $E_c - E_F \gg kT$.

**Lời giải chi tiết:**

Tính năng lượng nhiệt $kT$ tại $T = 285\,\mathrm{K}$ với $k = 8{,}617 \times 10^{-5}\,\mathrm{eV/K}$:
$$
kT \approx 0{,}02456\,\mathrm{eV}.
$$

(a) Khi bề rộng khe cấm $E_g = 0{,}500\,\mathrm{eV}$:
Độ chênh lệch năng lượng giữa đáy vùng dẫn và mức Fermi:
$$
\begin{aligned}
E_c - E_F &= \frac{E_g}{2} \\
&= \frac{0{,}500\,\mathrm{eV}}{2} \\
&= 0{,}250\,\mathrm{eV}.
\end{aligned}
$$

Tỷ số không thứ nguyên:
$$
\begin{aligned}
\frac{E_c - E_F}{kT} &= \frac{0{,}250\,\mathrm{eV}}{0{,}02456\,\mathrm{eV}} \\
&\approx 10{,}179.
\end{aligned}
$$

Xác suất chiếm trạng thái tại đáy vùng dẫn:
$$
\begin{aligned}
f(E_c) &= \frac{1}{e^{10{,}179} + 1} \\
&\approx e^{-10{,}179} \\
&\approx 3{,}79 \times 10^{-5}.
\end{aligned}
$$

(b) Khi bề rộng khe cấm $E_g = 1{,}50\,\mathrm{eV}$:
Độ chênh lệch năng lượng:
$$
\begin{aligned}
E_c - E_F &= \frac{1{,}50\,\mathrm{eV}}{2} \\
&= 0{,}750\,\mathrm{eV}.
\end{aligned}
$$

Tỷ số không thứ nguyên:
$$
\begin{aligned}
\frac{E_c - E_F}{kT} &= \frac{0{,}750\,\mathrm{eV}}{0{,}02456\,\mathrm{eV}} \\
&\approx 30{,}537.
\end{aligned}
$$

Xác suất chiếm trạng thái:
$$
\begin{aligned}
f(E_c) &= \frac{1}{e^{30{,}537} + 1} \\
&\approx e^{-30{,}537} \\
&\approx 5{,}46 \times 10^{-14}.
\end{aligned}
$$

</details>

---

### VP42.9.2

Hãy tìm tỷ số giữa xác suất chiếm một trạng thái tại đáy vùng dẫn của một chất bán dẫn ở nhiệt độ $315\,\mathrm{K}$ so với xác suất tại $295\,\mathrm{K}$ nếu khe cấm năng lượng có giá trị:
(a) $0{,}400\,\mathrm{eV}$.
(b) $0{,}800\,\mathrm{eV}$.
Giả thiết rằng mức năng lượng Fermi nằm chính giữa khe cấm năng lượng.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Mức Fermi nằm ở giữa khe cấm: $E_c - E_F = \frac{1}{2} E_g$.
- Hai nhiệt độ khảo sát: $T_1 = 295\,\mathrm{K}$ và $T_2 = 315\,\mathrm{K}$.
- Cần tìm tỷ số xác suất $R = \frac{f(E_c, T_2)}{f(E_c, T_1)}$ khi:
  (a) $E_g = 0{,}400\,\mathrm{eV}$, suy ra $E_c - E_F = 0{,}200\,\mathrm{eV}$.
  (b) $E_g = 0{,}800\,\mathrm{eV}$, suy ra $E_c - E_F = 0{,}400\,\mathrm{eV}$.

**Hướng đi:**
- Với bán dẫn thực tế ở nhiệt độ phòng, $E_c - E_F \gg kT$, số hạng $+1$ trong mẫu số của hàm Fermi–Dirac là không đáng kể, do đó ta có gần đúng Maxwell–Boltzmann rất chính xác:
$$
f(E_c, T) \approx e^{-(E_c - E_F)/kT}.
$$
- Tỷ số xác suất giữa hai nhiệt độ tính theo độ lệch số mũ:
$$
R = \frac{f(E_c, T_2)}{f(E_c, T_1)} \approx e^\Delta,
$$
với $\Delta = \frac{E_c - E_F}{k}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$.

**Lời giải chi tiết:**

Hiệu số nghịch đảo nhiệt độ với $T_1 = 295\,\mathrm{K}$ và $T_2 = 315\,\mathrm{K}$ là $\frac{1}{T_1} - \frac{1}{T_2} \approx 2{,}152 \times 10^{-4}\,\mathrm{K}^{-1}$.
Thừa số nhiệt độ $\beta = \frac{1}{k}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$:
$$
\begin{aligned}
\beta &= \frac{2{,}152 \times 10^{-4}\,\mathrm{K}^{-1}}{8{,}617 \times 10^{-5}\,\mathrm{eV/K}} \\
&\approx 2{,}497\,\mathrm{eV}^{-1}.
\end{aligned}
$$

(a) Khi $E_g = 0{,}400\,\mathrm{eV}$:
Ta có $E_c - E_F = 0{,}200\,\mathrm{eV}$.
Số mũ của tỷ số với $\beta \approx 2{,}497\,\mathrm{eV}^{-1}$:
$$
\Delta = (0{,}200\,\mathrm{eV})\beta \approx 0{,}4994.
$$

Tỷ số xác suất:
$$
\begin{aligned}
R &= e^{0{,}4994} \\
&\approx 1{,}65.
\end{aligned}
$$

(b) Khi $E_g = 0{,}800\,\mathrm{eV}$:
Ta có $E_c - E_F = 0{,}400\,\mathrm{eV}$.
Số mũ của tỷ số với $\beta \approx 2{,}497\,\mathrm{eV}^{-1}$:
$$
\Delta = (0{,}400\,\mathrm{eV})\beta \approx 0{,}9988.
$$

Tỷ số xác suất:
$$
\begin{aligned}
R &= e^{0{,}9988} \\
&\approx 2{,}72.
\end{aligned}
$$

Khe cấm càng rộng, xác suất kích thích nhiệt lên vùng dẫn càng nhạy cảm với sự gia tăng nhiệt độ.

</details>

---

### VP42.9.3

Xét một vật liệu bán dẫn có mức năng lượng Fermi nằm chính giữa khe cấm. Bề rộng khe cấm năng lượng phải bằng bao nhiêu để xác suất chiếm một trạng thái tại đáy vùng dẫn bằng $0{,}00190$ nếu nhiệt độ của khối chất là:
(a) $305\,\mathrm{K}$.
(b) $325\,\mathrm{K}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Mức Fermi ở giữa khe cấm: $E_c - E_F = \frac{1}{2} E_g$, suy ra $E_g = 2(E_c - E_F)$.
- Xác suất chiếm trạng thái đáy vùng dẫn: $f(E_c) = 0{,}00190$.
- Cần tìm bề rộng khe cấm $E_g$ tại hai nhiệt độ:
  (a) $T = 305\,\mathrm{K}$.
  (b) $T = 325\,\mathrm{K}$.

**Hướng đi:**
- Từ hàm phân bố Fermi–Dirac:
$$
f(E_c) = \frac{1}{e^{(E_c - E_F)/kT} + 1}.
$$
- Nghịch đảo phương trình:
$$
e^{(E_c - E_F)/kT} = \frac{1}{f(E_c)} - 1.
$$
- Lấy logarit tự nhiên hai vế giúp giải ra hiệu năng lượng $E_c - E_F$. Bề rộng khe cấm năng lượng bằng hai lần khoảng cách này: $E_g = 2(E_c - E_F)$.

**Lời giải chi tiết:**

Tính hệ số logarit từ xác suất đã cho:
$$
\begin{aligned}
\frac{1}{0{,}00190} - 1 &\approx 526{,}316 - 1 \\
&= 525{,}316.
\end{aligned}
$$

Lấy logarit tự nhiên:
$$
\ln(525{,}316) \approx 6{,}2640.
$$

(a) Tại nhiệt độ $T = 305\,\mathrm{K}$:
Năng lượng nhiệt với $k = 8{,}617 \times 10^{-5}\,\mathrm{eV/K}$:
$$
kT \approx 0{,}02628\,\mathrm{eV}.
$$

Khoảng cách từ mức Fermi đến đáy vùng dẫn:
$$
\begin{aligned}
E_c - E_F &= 6{,}2640 kT \\
&\approx 0{,}1646\,\mathrm{eV}.
\end{aligned}
$$

Bề rộng khe cấm năng lượng:
$$
\begin{aligned}
E_g &= 2(0{,}1646\,\mathrm{eV}) \\
&\approx 0{,}329\,\mathrm{eV}.
\end{aligned}
$$

(b) Tại nhiệt độ $T = 325\,\mathrm{K}$:
Năng lượng nhiệt với $k = 8{,}617 \times 10^{-5}\,\mathrm{eV/K}$:
$$
kT \approx 0{,}02801\,\mathrm{eV}.
$$

Khoảng cách từ mức Fermi đến đáy vùng dẫn:
$$
\begin{aligned}
E_c - E_F &= 6{,}2640 kT \\
&\approx 0{,}1754\,\mathrm{eV}.
\end{aligned}
$$

Bề rộng khe cấm năng lượng:
$$
\begin{aligned}
E_g &= 2(0{,}1754\,\mathrm{eV}) \\
&\approx 0{,}351\,\mathrm{eV}.
\end{aligned}
$$

</details>

---

### VP42.9.4

Trong một chất bán dẫn nhất định, mức năng lượng Fermi nằm phía trên đỉnh vùng hóa trị một khoảng bằng $\frac{3}{4}$ bề rộng khe cấm. Hãy tìm xác suất để một trạng thái tại đáy vùng dẫn bị chiếm nếu khe cấm có bề rộng $0{,}300\,\mathrm{eV}$ và nhiệt độ của chất bán dẫn là:
(a) $275\,\mathrm{K}$.
(b) $325\,\mathrm{K}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Bề rộng khe cấm: $E_g = 0{,}300\,\mathrm{eV}$.
- Vị trí mức Fermi: Nằm trên đỉnh vùng hóa trị một khoảng $\frac{3}{4} E_g$.
- Do đó, khoảng cách từ mức Fermi đến đáy vùng dẫn là:
$$
\begin{aligned}
E_c - E_F &= E_g - \frac{3}{4} E_g \\
&= \frac{1}{4} E_g \\
&= \frac{0{,}300\,\mathrm{eV}}{4} \\
&= 0{,}0750\,\mathrm{eV}.
\end{aligned}
$$
- Cần tính xác suất chiếm trạng thái đáy vùng dẫn $f(E_c)$ tại:
  (a) $T = 275\,\mathrm{K}$.
  (b) $T = 325\,\mathrm{K}$.

**Hướng đi:**
- Xác định năng lượng nhiệt $kT$ tương ứng với từng giá trị nhiệt độ.
- Tính số mũ $\frac{E_c - E_F}{kT}$ và thế vào hàm phân bố Fermi–Dirac đầy đủ $f(E_c) = \frac{1}{e^{(E_c - E_F)/kT} + 1}$.

**Lời giải chi tiết:**

Khoảng cách năng lượng cần xét là $E_c - E_F = 0{,}0750\,\mathrm{eV}$.

(a) Tại nhiệt độ $T = 275\,\mathrm{K}$:
Năng lượng nhiệt với $k = 8{,}617 \times 10^{-5}\,\mathrm{eV/K}$:
$$
kT \approx 0{,}02370\,\mathrm{eV}.
$$

Số mũ trong hàm Fermi–Dirac:
$$
\begin{aligned}
\frac{E_c - E_F}{kT} &= \frac{0{,}0750\,\mathrm{eV}}{0{,}02370\,\mathrm{eV}} \\
&\approx 3{,}165.
\end{aligned}
$$

Xác suất chiếm trạng thái tại đáy vùng dẫn:
$$
\begin{aligned}
f(E_c) &= \frac{1}{e^{3{,}165} + 1} \\
&= \frac{1}{23{,}69 + 1} \\
&\approx 0{,}0405.
\end{aligned}
$$

(b) Tại nhiệt độ $T = 325\,\mathrm{K}$:
Năng lượng nhiệt với $k = 8{,}617 \times 10^{-5}\,\mathrm{eV/K}$:
$$
kT \approx 0{,}02801\,\mathrm{eV}.
$$

Số mũ trong hàm Fermi–Dirac:
$$
\begin{aligned}
\frac{E_c - E_F}{kT} &= \frac{0{,}0750\,\mathrm{eV}}{0{,}02801\,\mathrm{eV}} \\
&\approx 2{,}678.
\end{aligned}
$$

Xác suất chiếm trạng thái tại đáy vùng dẫn:
$$
\begin{aligned}
f(E_c) &= \frac{1}{e^{2{,}678} + 1} \\
&= \frac{1}{14{,}55 + 1} \\
&\approx 0{,}0643.
\end{aligned}
$$

Xác suất chiếm mức tăng từ $4{,}05\%$ lên $6{,}43\%$ khi nhiệt độ tăng từ $275\,\mathrm{K}$ lên $325\,\mathrm{K}$.

</details>
