## Luyện tập hướng dẫn

Phần này cung cấp lời giải chi tiết cho 12 bài tập thuộc mục Luyện tập hướng dẫn (Key Example Variation Problems) của Chương 40. Các bài toán tập trung vào ba chủ đề nền tảng: Giếng thế một chiều sâu vô hạn, giếng thế vuông hữu hạn và hiện tượng xuyên ngầm qua rào thế.

Mọi biến đổi đều tuân thủ các hằng số vật lý tiêu chuẩn:
- Hằng số Planck: $h = 6{,}626 \times 10^{-34}\,\mathrm{J\cdot s}$
- Hằng số Planck rút gọn: $\hbar = \frac{h}{2\pi} = 1{,}055 \times 10^{-34}\,\mathrm{J\cdot s}$
- Khối lượng electron: $m_e = 9{,}109 \times 10^{-31}\,\mathrm{kg}$
- Khối lượng proton: $m_p = 1{,}673 \times 10^{-27}\,\mathrm{kg}$
- Điện tích nguyên tố: $e = 1{,}602 \times 10^{-19}\,\mathrm{C}$
- Tốc độ ánh sáng: $c = 3{,}00 \times 10^8\,\mathrm{m/s}$

---

### VP40.4.1

Mức năng lượng thấp nhất của một electron bị giam trong giếng thế một chiều sâu vô hạn là $2{,}00 \times 10^{-19}\,\mathrm{J}$. Hãy xác định:
(a) Bề rộng của giếng thế.
(b) Năng lượng của các mức $n = 2$ và $n = 3$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hạt: Electron ($m_e = 9{,}109 \times 10^{-31}\,\mathrm{kg}$).
- Năng lượng trạng thái cơ bản ($n = 1$): $E_1 = 2{,}00 \times 10^{-19}\,\mathrm{J}$.
- Cần tìm: Bề rộng $L$ của giếng thế và các năng lượng $E_2, E_3$.

**Hướng đi:**
- Mức năng lượng của hạt trong giếng thế một chiều sâu vô hạn tuân theo công thức lượng tử hóa $E_n = \frac{n^2 h^2}{8mL^2} = n^2 E_1$.
- Từ giá trị $E_1$ đã cho, ta giải phương trình để suy ra trực tiếp bề rộng $L$.
- Năng lượng của các trạng thái kích thích tỷ lệ với bình phương số lượng tử chính $n^2$.

**Lời giải chi tiết:**

(a) Xác định bề rộng giếng thế $L$:
Từ biểu thức năng lượng trạng thái cơ bản ($n = 1$):
$$
E_1 = \frac{h^2}{8m_e L^2}
$$

Suy ra bề rộng giếng:
Tính mẫu số $\sqrt{8m_e E_1} \approx 1{,}207 \times 10^{-24}\,\mathrm{kg\cdot m/s}$, ta có:
$$
\begin{aligned}
L &= \frac{h}{\sqrt{8m_e E_1}} \\
&\approx \frac{6{,}626 \times 10^{-34}}{1{,}207 \times 10^{-24}} \\
&\approx 5{,}49 \times 10^{-10}\,\mathrm{m} \\
&= 0{,}549\,\mathrm{nm}.
\end{aligned}
$$

(b) Năng lượng của các mức $n = 2$ và $n = 3$:
Áp dụng quy tắc tỷ lệ $E_n = n^2 E_1$:
$$
\begin{aligned}
E_2 &= 4 E_1 \\
&= 4(2{,}00 \times 10^{-19}\,\mathrm{J}) \\
&= 8{,}00 \times 10^{-19}\,\mathrm{J}.
\end{aligned}
$$
$$
\begin{aligned}
E_3 &= 9 E_1 \\
&= 9(2{,}00 \times 10^{-19}\,\mathrm{J}) \\
&= 1{,}80 \times 10^{-18}\,\mathrm{J}.
\end{aligned}
$$

Đổi sang electron-volt để thuận tiện đối chiếu:
$E_1 \approx 1{,}25\,\mathrm{eV}$, $E_2 \approx 4{,}99\,\mathrm{eV}$, và $E_3 \approx 11{,}23\,\mathrm{eV}$.

</details>

---

### VP40.4.2

Một proton ($m_p = 1{,}67 \times 10^{-27}\,\mathrm{kg}$) bị giam trong giếng thế một chiều sâu vô hạn có bề rộng $5{,}00 \times 10^{-15}\,\mathrm{m}$ (kích thước điển hình của hạt nhân nguyên tử). Hãy tìm độ chênh lệch năng lượng giữa:
(a) Mức $n = 2$ và mức $n = 1$.
(b) Mức $n = 3$ và mức $n = 2$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hạt: Proton ($m_p = 1{,}67 \times 10^{-27}\,\mathrm{kg}$).
- Bề rộng giếng: $L = 5{,}00 \times 10^{-15}\,\mathrm{m} = 5{,}00\,\mathrm{fm}$.
- Cần tìm: $\Delta E_{21} = E_2 - E_1$ và $\Delta E_{32} = E_3 - E_2$.

**Hướng đi:**
- Năng lượng mức $n$ là $E_n = n^2 E_1$ với $E_1 = \frac{h^2}{8m_p L^2}$.
- Hiệu năng lượng giữa hai mức kế tiếp được tính qua hiệu hai bình phương: $\Delta E = (n_f^2 - n_i^2) E_1$.
- Do khối lượng proton lớn hơn electron gần 2000 lần nhưng kích thước giếng cấp độ femtomet rất nhỏ, năng lượng giam giữ nằm ở thang mega electron-volt ($\mathrm{MeV}$).

**Lời giải chi tiết:**

Tính năng lượng mức cơ bản $E_1$:
Tính riêng tử số và mẫu số:
$$
h^2 \approx 4{,}390 \times 10^{-67}\,\mathrm{J^2\cdot s^2},
$$
$$
\begin{aligned}
D&=8m_pL^2\\
&\approx3{,}340\times10^{-55}\,\mathrm{kg\,m^2}.
\end{aligned}
$$
Suy ra:
$$
\begin{aligned}
E_1 &= \frac{h^2}{8m_p L^2} \\
&\approx \frac{4{,}390 \times 10^{-67}}{3{,}340 \times 10^{-55}} \\
&\approx 1{,}314 \times 10^{-12}\,\mathrm{J}.
\end{aligned}
$$

(a) Hiệu năng lượng giữa mức $n = 2$ và mức $n = 1$:
$$
\begin{aligned}
\Delta E_{21} &= E_2 - E_1 \\
&= 3 E_1 \\
&= 3(1{,}314 \times 10^{-12}\,\mathrm{J}) \\
&\approx 3{,}94 \times 10^{-12}\,\mathrm{J}.
\end{aligned}
$$
Đổi sang đơn vị $\mathrm{MeV}$:
Dùng hệ số đổi đơn vị $1\,\mathrm{MeV}\approx1{,}602\times10^{-13}\,\mathrm J$, ta được

$$
\Delta E_{21}\approx24{,}6\,\mathrm{MeV}.
$$

(b) Hiệu năng lượng giữa mức $n = 3$ và mức $n = 2$:
$$
\begin{aligned}
\Delta E_{32} &= E_3 - E_2 \\
&= 5 E_1 \\
&= 5(1{,}314 \times 10^{-12}\,\mathrm{J}) \\
&\approx 6{,}57 \times 10^{-12}\,\mathrm{J}.
\end{aligned}
$$
Đổi sang đơn vị $\mathrm{MeV}$:
Đổi kết quả từ joule sang megaelectron-volt bằng cùng hệ số:

$$
\Delta E_{32}\approx41{,}0\,\mathrm{MeV}.
$$

</details>

---

### VP40.4.3

Một photon phát ra khi electron trong giếng thế một chiều sâu vô hạn chuyển từ mức năng lượng $n = 2$ xuống mức $n = 1$. Bước sóng của photon này là $655\,\mathrm{nm}$. Hãy xác định:
(a) Năng lượng của photon này.
(b) Bề rộng của giếng thế.
(c) Bước sóng của photon phát ra khi electron chuyển từ mức $n = 3$ xuống mức $n = 2$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hạt: Electron ($m_e = 9{,}109 \times 10^{-31}\,\mathrm{kg}$).
- Bước sóng chuyển mức $2 \to 1$: $\lambda_{21} = 655\,\mathrm{nm} = 655 \times 10^{-9}\,\mathrm{m}$.
- Cần tìm: Năng lượng photon $E_{\mathrm{ph}}$, bề rộng giếng $L$, và bước sóng chuyển mức $\lambda_{32}$.

**Hướng đi:**
- Năng lượng photon liên hệ với bước sóng qua hệ thức Planck $E_{\mathrm{ph}} = \frac{hc}{\lambda}$.
- Theo định luật bảo toàn năng lượng, năng lượng photon bằng hiệu năng lượng hai mức $\Delta E_{21} = 3 E_1$. Từ đó ta suy ra $E_1$ và bề rộng $L$.
- Chuyển mức $3 \to 2$ có hiệu năng lượng $\Delta E_{32} = 5 E_1 = \frac{5}{3} \Delta E_{21}$. Vì bước sóng tỷ lệ nghịch với năng lượng photon, ta có $\lambda_{32} = \frac{3}{5} \lambda_{21}$.

**Lời giải chi tiết:**

(a) Năng lượng của photon phát ra trong chuyển mức $2 \to 1$:
Với tích $hc \approx 1{,}988 \times 10^{-25}\,\mathrm{J\cdot m}$:
$$
\begin{aligned}
E_{\mathrm{ph}} &= \frac{hc}{\lambda_{21}} \\
&\approx \frac{1{,}988 \times 10^{-25}}{655 \times 10^{-9}} \\
&\approx 3{,}03 \times 10^{-19}\,\mathrm{J} \\
&\approx 1{,}89\,\mathrm{eV}.
\end{aligned}
$$

(b) Bề rộng của giếng thế $L$:
Vì $\Delta E_{21} = E_2 - E_1 = 3 E_1 = E_{\mathrm{ph}}$, ta có:
$$
\begin{aligned}
E_1 &= \frac{E_{\mathrm{ph}}}{3} \\
&\approx \frac{3{,}035 \times 10^{-19}\,\mathrm{J}}{3} \\
&\approx 1{,}012 \times 10^{-19}\,\mathrm{J}.
\end{aligned}
$$

Mặt khác, $E_1 = \frac{h^2}{8m_e L^2}$, do đó:
Tính mẫu số $\sqrt{8m_e E_1} \approx 8{,}584 \times 10^{-25}\,\mathrm{kg\cdot m/s}$:
$$
\begin{aligned}
L &= \frac{h}{\sqrt{8m_e E_1}} \\
&\approx \frac{6{,}626 \times 10^{-34}}{8{,}584 \times 10^{-25}} \\
&\approx 7{,}72 \times 10^{-10}\,\mathrm{m} \\
&= 0{,}772\,\mathrm{nm}.
\end{aligned}
$$

(c) Bước sóng phát ra khi electron chuyển từ mức $n = 3$ xuống mức $n = 2$:
Hiệu năng lượng của chuyển mức này là:
$$
\begin{aligned}
\Delta E_{32} &= E_3 - E_2 \\
&= 5 E_1 \\
&= \frac{5}{3}\Delta E_{21}.
\end{aligned}
$$

Do bước sóng tỷ lệ nghịch với năng lượng photon:
$$
\begin{aligned}
\lambda_{32} &= \frac{3}{5}\lambda_{21} \\
&= \frac{3}{5}(655\,\mathrm{nm}) \\
&= 393\,\mathrm{nm}.
\end{aligned}
$$

Photon này thuộc dải tử ngoại gần, có bước sóng ngắn hơn và mang năng lượng lớn hơn so với photon dải ánh sáng đỏ nhìn thấy ở chuyển mức $2 \to 1$.

</details>

---

### VP40.4.4

Một hàm sóng của một hạt có năng lượng $E$ trong giếng thế một chiều sâu vô hạn ($0 \le x \le L$) được viết dưới dạng:
$$
\psi(x) = A \cos(k x + \phi),
$$
trong đó số sóng $k$ được định nghĩa:
$$
k = \frac{\sqrt{2mE}}{\hbar}.
$$
(a) Hãy tìm đạo hàm cấp hai của $\psi(x)$ và chứng minh rằng hàm này thỏa mãn phương trình Schrödinger độc lập với thời gian trong giếng thế.
(b) Sử dụng điều kiện biên tại $x = 0$ để xác định giá trị của pha ban đầu $\phi$.
(c) Sử dụng điều kiện biên tại $x = L$ để xác định các giá trị cho phép của năng lượng $E$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hàm sóng đề xuất: $\psi(x) = A \cos(kx + \phi)$ với $k = \frac{\sqrt{2mE}}{\hbar}$.
- Điều kiện thế: $U(x) = 0$ trong khoảng $0 < x < L$, và $U(x) = \infty$ tại $x \le 0$ hoặc $x \ge L$.
- Cần chứng minh: $\psi(x)$ nghiệm đúng phương trình Schrödinger và xác định $\phi$ cùng các mức năng lượng dừng $E_n$.

**Hướng đi:**
- Lấy đạo hàm cấp hai theo biến tọa độ $x$, so sánh với phương trình Schrödinger độc lập với thời gian $-\frac{\hbar^2}{2m} \frac{d^2\psi}{dx^2} + U(x)\psi = E\psi$.
- Điều kiện thành giếng cứng đòi hỏi hàm sóng phải triệt tiêu tại các biên: $\psi(0) = 0$ và $\psi(L) = 0$.

**Lời giải chi tiết:**

(a) Đạo hàm cấp hai và phương trình Schrödinger:
Đặt $k = \frac{\sqrt{2mE}}{\hbar}$. Đạo hàm cấp một của hàm sóng theo $x$:
$$
\frac{d\psi}{dx} = -k A \sin(kx + \phi).
$$

Đạo hàm cấp hai:
$$
\begin{aligned}
\frac{d^2\psi}{dx^2} &= -k^2 A \cos(kx + \phi) \\
&= -k^2 \psi(x).
\end{aligned}
$$

Thay $k^2 = \frac{2mE}{\hbar^2}$ vào biểu thức:
$$
\frac{d^2\psi}{dx^2} = -\frac{2mE}{\hbar^2}\psi(x).
$$
Biến đổi tương đương sang dạng phương trình Schrödinger độc lập với thời gian:
$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi(x).
$$
Trong lòng giếng thế, thế năng $U(x) = 0$, phương trình trên chính là phương trình Schrödinger độc lập với thời gian. Như vậy hàm sóng đã cho thỏa mãn phương trình vi phân.

(b) Xác định pha ban đầu $\phi$ từ điều kiện biên tại $x = 0$:
Thành giếng vô hạn tại $x = 0$ buộc xác suất tìm hạt tại biên bằng 0:
$$
\psi(0) = A \cos\phi = 0.
$$
Do $A \ne 0$, ta suy ra:
$$
\phi = \pm \frac{\pi}{2} + m\pi \quad (m \in \mathbb{Z}).
$$
Chọn nghiệm thuận tiện $\phi = -\frac{\pi}{2}$, khi đó hàm sóng trở thành dạng hàm $\sin$ quen thuộc:
$$
\begin{aligned}
\psi(x) &= A \cos\left(kx - \frac{\pi}{2}\right) \\
&= A \sin(kx).
\end{aligned}
$$

(c) Xác định năng lượng $E$ từ điều kiện biên tại $x = L$:
Áp dụng điều kiện triệt tiêu tại thành giếng bên phải:
$$
\psi(L) = A \sin(kL) = 0.
$$
Để hàm sóng không đồng nhất bằng không, ta phải có:
$$
kL = n\pi \implies k = \frac{n\pi}{L},
$$
với $n = 1, 2, 3, \dots$

Thay trở lại định nghĩa của $k$:
$$
\frac{\sqrt{2mE}}{\hbar} = \frac{n\pi}{L}.
$$
Bình phương hai vế và giải ra năng lượng $E$:
$$
\begin{aligned}
E_n &= \frac{n^2 \pi^2 \hbar^2}{2mL^2} \\
&= \frac{n^2 h^2}{8mL^2},
\end{aligned}
$$
với $n = 1, 2, 3, \dots$
Đây chính là biểu thức năng lượng lượng tử hóa chuẩn mực của hạt trong giếng thế một chiều sâu vô hạn.

</details>

---

### VP40.6.1

Một electron bị giam trong giếng thế có bề rộng $0{,}350\,\mathrm{nm}$.
(a) Tìm năng lượng trạng thái cơ bản $E_{1\text{-IDW}}$ nếu giếng thế sâu vô hạn.
Nếu thay vào đó độ sâu $U_0$ của giếng thế bằng sáu lần giá trị của $E_{1\text{-IDW}}$, hãy tìm:
(b) Năng lượng trạng thái cơ bản của electron trong giếng hữu hạn này.
(c) Năng lượng tối thiểu cần thiết để giải phóng electron ra khỏi giếng thế (năng lượng liên kết).

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hạt: Electron ($m_e = 9{,}109 \times 10^{-31}\,\mathrm{kg}$).
- Bề rộng giếng: $L = 0{,}350\,\mathrm{nm} = 3{,}50 \times 10^{-10}\,\mathrm{m}$.
- Độ sâu giếng hữu hạn: $U_0 = 6 E_{1\text{-IDW}}$.
- Cần tìm: $E_{1\text{-IDW}}$, năng lượng mức cơ bản $E_1$ của giếng hữu hạn, và năng lượng bứt electron $E_{\mathrm{free}} = U_0 - E_1$.

**Hướng đi:**
- Năng lượng giếng vô hạn tính qua công thức chuẩn $E_{1\text{-IDW}} = \frac{h^2}{8m_e L^2}$.
- Khi thành giếng có độ cao hữu hạn $U_0 = 6 E_{1\text{-IDW}}$, hàm sóng xuyên một phần ra ngoài vùng thế cấm, khiến bước sóng hiệu dụng dài hơn và mức năng lượng bị kéo tụt xuống. Theo lý thuyết giải tích giếng thế hữu hạn, mức cơ bản đạt $E_1 \approx 0{,}625 E_{1\text{-IDW}}$.
- Năng lượng ion hóa (giải phóng hạt) là độ chênh lệch giữa đỉnh giếng $U_0$ và mức liên kết $E_1$.

**Lời giải chi tiết:**

(a) Năng lượng trạng thái cơ bản của giếng sâu vô hạn:
Tính mẫu số $8m_e L^2 \approx 8{,}927 \times 10^{-49}\,\mathrm{kg\cdot m^2}$:
$$
\begin{aligned}
E_{1\text{-IDW}} &= \frac{h^2}{8m_e L^2} \\
&\approx \frac{4{,}390 \times 10^{-67}}{8{,}927 \times 10^{-49}} \\
&\approx 4{,}92 \times 10^{-19}\,\mathrm{J} \\
&\approx 3{,}07\,\mathrm{eV}.
\end{aligned}
$$

(b) Năng lượng trạng thái cơ bản trong giếng hữu hạn $U_0 = 6 E_{1\text{-IDW}}$:
Độ sâu của giếng thế:
$$
\begin{aligned}
U_0 &= 6 E_{1\text{-IDW}} \\
&= 6(4{,}923 \times 10^{-19}\,\mathrm{J}) \\
&\approx 2{,}95 \times 10^{-18}\;\mathrm{J} \\
&\approx 18{,}43\,\mathrm{eV}.
\end{aligned}
$$

Đối với giếng thế đối xứng có độ sâu $U_0 = 6 E_{1\text{-IDW}}$, nghiệm của phương trình siêu việt cho mức liên kết thứ nhất có giá trị:
$$
E_1 = 0{,}625 E_{1\text{-IDW}}.
$$
Do đó:
$$
\begin{aligned}
E_1&=0{,}625E_{1\text{-IDW}}\\
&\approx3{,}08\times10^{-19}\,\mathrm J\\
&\approx1{,}92\,\mathrm{eV}.
\end{aligned}
$$

(c) Năng lượng tối thiểu để giải phóng electron:
Electron muốn thoát ra khỏi giếng cần được cung cấp năng lượng ít nhất bằng độ sâu còn lại tới miệng giếng:
$$
\begin{aligned}
E_{\rm free}&=U_0-E_1\\
&=5{,}375E_{1\text{-IDW}}\\
&\approx2{,}65\times10^{-18}\,\mathrm J\\
&\approx16{,}51\,\mathrm{eV}.
\end{aligned}
$$

</details>

---

### VP40.6.2

Một giếng thế hữu hạn có độ sâu $U_0$ gấp 6 lần năng lượng trạng thái cơ bản $E_{1\text{-IDW}}$ của electron trong giếng sâu vô hạn có cùng bề rộng. Photon phát ra khi electron trong giếng hữu hạn này chuyển mức từ $n = 3$ xuống mức $n = 2$ có năng lượng $2{,}50 \times 10^{-19}\,\mathrm{J}$. Hãy xác định:
(a) Giá trị của $E_{1\text{-IDW}}$.
(b) Giá trị độ sâu $U_0$ của giếng thế.
(c) Bề rộng $L$ của giếng thế.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Độ sâu giếng: $U_0 = 6 E_{1\text{-IDW}}$.
- Năng lượng photon phát ra khi chuyển từ $n = 3 \to 2$: $\Delta E_{32} = 2{,}50 \times 10^{-19}\,\mathrm{J}$.
- Cần tìm: $E_{1\text{-IDW}}$, $U_0$, và bề rộng giếng $L$.

**Hướng đi:**
- Với giếng thế $U_0 = 6 E_{1\text{-IDW}}$, các mức năng lượng liên kết có giá trị: $E_1 \approx 0{,}625 E_{1\text{-IDW}}$, $E_2 \approx 2{,}43 E_{1\text{-IDW}}$, và $E_3 \approx 5{,}09 E_{1\text{-IDW}}$.
- Hiệu năng lượng của chuyển mức bức xạ là $\Delta E_{32} = E_3 - E_2 = 2{,}66 E_{1\text{-IDW}}$.
- Từ đó ta suy ra $E_{1\text{-IDW}}$, tính được $U_0 = 6 E_{1\text{-IDW}}$, và giải phương trình tìm bề rộng $L$.

**Lời giải chi tiết:**

(a) Xác định giá trị $E_{1\text{-IDW}}$:
Độ chênh lệch năng lượng giữa mức $n = 3$ và $n = 2$:
Hai hệ số mức năng lượng chênh nhau $5{,}09-2{,}43=2{,}66$. Vì vậy,

$$
\begin{aligned}
\Delta E_{32}&=E_3-E_2\\
&=2{,}66E_{1\text{-IDW}}.
\end{aligned}
$$

Theo giả thiết, photon mang năng lượng bằng đúng khoảng cách này:
$$
\begin{aligned}
E_{1\text{-IDW}} &= \frac{\Delta E_{32}}{2{,}66} \\
&= \frac{2{,}50 \times 10^{-19}\,\mathrm{J}}{2{,}66} \\
&\approx 9{,}40 \times 10^{-20}\,\mathrm{J} \\
&\approx 0{,}587\,\mathrm{eV}.
\end{aligned}
$$

(b) Độ sâu $U_0$ của giếng thế:
$$
\begin{aligned}
U_0 &= 6 E_{1\text{-IDW}} \\
&= 6(9{,}398 \times 10^{-20}\,\mathrm{J}) \\
&\approx 5{,}64 \times 10^{-19}\,\mathrm{J} \\
&\approx 3{,}52\,\mathrm{eV}.
\end{aligned}
$$

(c) Bề rộng $L$ của giếng thế:
Sử dụng biểu thức định nghĩa của $E_{1\text{-IDW}}$ đối với electron:
$$
E_{1\text{-IDW}} = \frac{h^2}{8m_e L^2}.
$$

Suy ra:
Tính mẫu số $\sqrt{8m_e E_{1\text{-IDW}}} \approx 8{,}275 \times 10^{-25}\,\mathrm{kg\cdot m/s}$:
$$
\begin{aligned}
L &= \frac{h}{\sqrt{8m_e E_{1\text{-IDW}}}} \\
&\approx \frac{6{,}626 \times 10^{-34}}{8{,}275 \times 10^{-25}} \\
&\approx 8{,}01 \times 10^{-10}\,\mathrm{m} \\
&= 0{,}801\,\mathrm{nm}.
\end{aligned}
$$

</details>

---

### VP40.6.3

Một electron trong giếng thế hữu hạn chỉ có thể phát ra photon có một trong ba bước sóng phân biệt khi nó chuyển từ một mức năng lượng cao xuống mức năng lượng thấp hơn. Độ sâu của giếng thế này gấp 6 lần năng lượng trạng thái cơ bản $E_{1\text{-IDW}}$ của electron trong giếng sâu vô hạn có cùng bề rộng.
(a) Nếu bước sóng ngắn nhất trong ba bước sóng là $355\,\mathrm{nm}$, hãy xác định các số lượng tử $n$ của mức ban đầu và mức kết thúc đối với chuyển dịch này.
(b) Tìm hai bước sóng còn lại và chỉ rõ các số lượng tử $n$ của mức ban đầu và mức kết thúc cho mỗi chuyển dịch tương ứng.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Độ sâu giếng: $U_0 = 6 E_{1\text{-IDW}}$.
- Hệ chỉ có đúng 3 vạch phổ phát xạ riêng biệt.
- Bước sóng ngắn nhất: $\lambda_{\mathrm{min}} = 355\,\mathrm{nm}$.
- Cần tìm: Các số lượng tử mức đầu - cuối cho cả ba chuyển mức và hai bước sóng còn lại.

**Hướng đi:**
- Một hệ phát ra đúng 3 vạch phổ chuyển dịch chứng tỏ hệ có đúng 3 mức năng lượng liên kết ($n = 1, 2, 3$). Số bước sóng phát xạ có thể có là $C_3^2 = 3$.
- Ba chuyển dịch gồm: $3 \to 1$, $3 \to 2$, và $2 \to 1$.
- Bước sóng ngắn nhất ứng với độ chênh lệch năng lượng lớn nhất, tức là bước nhảy từ mức cao nhất $n = 3$ xuống trạng thái cơ bản $n = 1$.
- Các bước sóng tỷ lệ nghịch với khoảng cách năng lượng tương ứng.

**Lời giải chi tiết:**

(a) Xác định chuyển mức ứng với bước sóng ngắn nhất:
Với giếng thế $U_0 = 6 E_{1\text{-IDW}}$, ba mức năng lượng liên kết là:
- Mức $n = 1$: $E_1 = 0{,}625 E_{1\text{-IDW}}$
- Mức $n = 2$: $E_2 = 2{,}43 E_{1\text{-IDW}}$
- Mức $n = 3$: $E_3 = 5{,}09 E_{1\text{-IDW}}$

Khoảng cách năng lượng giữa các cặp mức:
Hiệu năng lượng của ba chuyển mức tương ứng:
$$
\begin{aligned}
&\Delta E_{31} = 4{,}465 E_{1\text{-IDW}}, \\
&\Delta E_{32} = 2{,}660 E_{1\text{-IDW}}, \\
&\Delta E_{21} = 1{,}805 E_{1\text{-IDW}}.
\end{aligned}
$$

Vì $\Delta E_{31}$ có giá trị lớn nhất, bước sóng phát ra sẽ ngắn nhất:
$$
\lambda_{\mathrm{min}} = \lambda_{31} = 355\,\mathrm{nm}.
$$
Như vậy: Số lượng tử ban đầu là $n_i = 3$, số lượng tử kết thúc là $n_f = 1$.

(b) Xác định hai bước sóng còn lại:
Sử dụng mối liên hệ tỷ lệ nghịch $\lambda = \frac{hc}{\Delta E}$:
- Chuyển mức từ $n = 3$ xuống $n = 2$:
$$
\begin{aligned}
\lambda_{32} &= \lambda_{31}\frac{\Delta E_{31}}{\Delta E_{32}} \\
&= (355\,\mathrm{nm})\frac{4{,}465}{2{,}660} \\
&\approx 596\,\mathrm{nm}.
\end{aligned}
$$
Chuyển dịch này xảy ra giữa $n_i = 3 \to n_f = 2$, phát ra photon ánh sáng vàng-cam nhìn thấy.

- Chuyển mức từ $n = 2$ xuống $n = 1$:
$$
\begin{aligned}
\lambda_{21} &= \lambda_{31}\frac{\Delta E_{31}}{\Delta E_{21}} \\
&= (355\,\mathrm{nm})\frac{4{,}465}{1{,}805} \\
&\approx 878\,\mathrm{nm}.
\end{aligned}
$$
Chuyển dịch này xảy ra giữa $n_i = 2 \to n_f = 1$, phát ra bức xạ thuộc vùng hồng ngoại gần.

</details>

---

### VP40.6.4

Một electron ở trong một giếng thế một chiều có bề rộng $0{,}400\,\mathrm{nm}$.
(a) Tìm năng lượng trạng thái cơ bản $E_{1\text{-IDW}}$ của electron (theo đơn vị $\mathrm{eV}$) nếu giếng thế sâu vô hạn.
(b) Nếu độ sâu của giếng thế chỉ là $0{,}015\,\mathrm{eV}$, nhỏ hơn rất nhiều so với $E_{1\text{-IDW}}$, giếng chỉ có duy nhất một trạng thái liên kết. Hãy xác định năng lượng (theo đơn vị $\mathrm{eV}$) của trạng thái liên kết này.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Giếng rộng $L=0{,}400\,\mathrm{nm}$. Tính năng lượng cơ bản của hộp vô hạn, rồi tìm mức liên kết duy nhất khi độ sâu chỉ còn $U_0=0{,}015\,\mathrm{eV}$. Mốc thế năng bằng không tại đáy giếng.

**Hướng đi:**

- Dùng năng lượng hộp vô hạn để giải phần (a), vì hai vách buộc hàm sóng có nút tại hai đầu.
- Với giếng hữu hạn rất nông, giữ đuôi hàm sóng ngoài giếng và nối hàm cùng đạo hàm tại biên. Những tỉ số mức của một giếng sâu hơn không áp dụng cho độ sâu này.
- Chọn nghiệm chẵn cơ bản và giải phương trình nối bằng biến không thứ nguyên. Cách này xác định trực tiếp mức dưới ngưỡng thoát mà không cần giả sử mức là một tỉ lệ cố định của độ sâu.

(a) Ký hiệu năng lượng cơ bản của hộp vô hạn là $E_\infty$. Với khối lượng electron,

$$
\begin{aligned}
E_\infty&=\frac{h^2}{8m_eL^2}\\
&\approx3{,}765\times10^{-19}\,\mathrm J\\
&\approx2{,}350\,\mathrm{eV}.
\end{aligned}
$$

Vậy năng lượng cơ bản cần tìm trong phần (a) bằng khoảng $2{,}35\,\mathrm{eV}$.

(b) Đặt gốc tọa độ phụ tại tâm giếng để dùng tính đối xứng của trạng thái cơ bản. Bên trong, nghiệm chẵn có dạng cosin. Đặt

$$
\begin{aligned}
&z=\frac{kL}{2},\\
&z_0=\frac{L\sqrt{2m_eU_0}}{2\hbar}.
\end{aligned}
$$

Số sóng trong giếng và hằng số suy giảm ngoài giếng là

$$
\begin{aligned}
&k=\frac{\sqrt{2m_eE}}{\hbar},\\
&\kappa=\frac{\sqrt{2m_e(U_0-E)}}{\hbar}.
\end{aligned}
$$

Nối đạo hàm với hàm cosin tại một mép cho

$$
k\tan\frac{kL}{2}=\kappa.
$$

Nhân với $L/2$ rồi dùng các biến đã đặt:

$$
z\tan z=\sqrt{z_0^2-z^2}.
$$

Với các dữ kiện trên, $z_0\approx0{,}1255$. Nghiệm cơ bản nằm trong khoảng $0<z<z_0$. Giải phương trình nối và đổi lại năng lượng bằng

$$
E=U_0\left(\frac{z}{z_0}\right)^2
$$

cho kết quả

$$
E\approx0{,}01477\,\mathrm{eV}.
$$

Năng lượng liên kết so với ngưỡng ngoài là

$$
\begin{aligned}
U_0-E&\approx0{,}000231\,\mathrm{eV}\\
&=0{,}231\,\mathrm{meV}.
\end{aligned}
$$

Mức nằm sát miệng giếng, còn năng lượng cần thêm để thoát rất nhỏ. Hàm sóng có đuôi dài bên ngoài, phù hợp với việc một giếng rất nông chỉ giữ hạt yếu. Giá trị $E$ được tính từ đáy giếng, không được nhầm với năng lượng liên kết $U_0-E$.

</details>

---

### VP40.7.1

Một electron có năng lượng $3{,}75\,\mathrm{eV}$ tiến tới gặp một rào thế vuông cao $6{,}10\,\mathrm{eV}$. Hãy tính xác suất electron xuyên ngầm qua rào thế nếu bề rộng của rào là:
(a) $0{,}750\,\mathrm{nm}$.
(b) $0{,}500\,\mathrm{nm}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Năng lượng electron: $E = 3{,}75\,\mathrm{eV}$.
- Chiều cao rào thế: $U_0 = 6{,}10\,\mathrm{eV}$.
- Bề rộng rào: (a) $L = 0{,}750\,\mathrm{nm}$, (b) $L = 0{,}500\,\mathrm{nm}$.
- Cần tìm: Hệ số truyền qua (xác suất xuyên ngầm) $T$.

**Hướng đi:**
- Vì năng lượng hạt nhỏ hơn chiều cao rào ($E < U_0$), hạt chuyển động trong vùng thế cấm cổ điển. Theo cơ học lượng tử, hàm sóng suy giảm hàm mũ trong rào với hệ số suy giảm $\kappa = \frac{\sqrt{2m_e(U_0 - E)}}{\hbar}$.
- Khi rào đủ dày hoặc xác suất xuyên ngầm nhỏ ($2\kappa L \gg 1$), hệ số truyền qua được tính bằng công thức xấp xỉ chuẩn: $T = G e^{-2\kappa L}$, trong đó thừa số tiền hàm mũ là $G = 16 \frac{E}{U_0} \left(1 - \frac{E}{U_0}\right)$.

**Lời giải chi tiết:**

Tính độ hụt năng lượng dưới đỉnh rào:
$$
\begin{aligned}
U_0-E&=(6{,}10-3{,}75)\,\mathrm{eV}\\
&=2{,}35\,\mathrm{eV}\\
&\approx3{,}765\times10^{-19}\,\mathrm J.
\end{aligned}
$$

Hệ số suy giảm hàm sóng $\kappa$:
Tính tử số:
Đặt $q$ là tử số trong biểu thức của $\kappa$:

$$
\begin{aligned}
q&=\sqrt{2m_e(U_0-E)}\\
&\approx 8{,}281 \times 10^{-25}\,\mathrm{kg\cdot m/s}.
\end{aligned}
$$
$$
\begin{aligned}
\kappa &= \frac{\sqrt{2m_e(U_0 - E)}}{\hbar} \\
&\approx \frac{8{,}281 \times 10^{-25}}{1{,}055 \times 10^{-34}} \\
&\approx 7{,}85 \times 10^9\,\mathrm{m}^{-1} \\
&= 7{,}85\,\mathrm{nm}^{-1}.
\end{aligned}
$$

Thừa số tiền hàm mũ $G$:
$$
\frac{E}{U_0} = \frac{3{,}75}{6{,}10} \approx 0{,}6148.
$$
$$
\begin{aligned}
G&=16(0{,}6148)(0{,}3852)\\
&\approx3{,}79.
\end{aligned}
$$

(a) Khi bề rộng rào $L = 0{,}750\,\mathrm{nm}$:
Số mũ suy giảm:
$$
\begin{aligned}
2\kappa L&\approx2(7{,}85)(0{,}750)\\
&\approx11{,}77.
\end{aligned}
$$

Hệ số truyền qua:
$$
\begin{aligned}
T_a &= G e^{-2\kappa L} \\
&\approx 3{,}79 \times e^{-11{,}77} \\
&\approx 2{,}90 \times 10^{-5}.
\end{aligned}
$$

(b) Khi bề rộng rào $L = 0{,}500\,\mathrm{nm}$:
Số mũ suy giảm:
$$
\begin{aligned}
2\kappa L&\approx2(7{,}85)(0{,}500)\\
&\approx7{,}85.
\end{aligned}
$$

Hệ số truyền qua:
$$
\begin{aligned}
T_b &= G e^{-2\kappa L} \\
&\approx 3{,}79 \times e^{-7{,}85} \\
&\approx 1{,}47 \times 10^{-3}.
\end{aligned}
$$

Nhận xét: Khi bề rộng rào giảm đi $33\%$ (từ $0{,}75\,\mathrm{nm}$ xuống $0{,}50\,\mathrm{nm}$), xác suất truyền qua tăng vọt hơn 50 lần. Hiện tượng này minh chứng độ nhạy cực cao của hiệu ứng xuyên ngầm đối với khoảng cách, vốn là nguyên lý hoạt động của kính hiển vi quét xuyên hầm (STM).

</details>

---

### VP40.7.2

Một electron có năng lượng $3{,}50\,\mathrm{eV}$ tiến tới gặp một rào thế vuông cao $4{,}00\,\mathrm{eV}$.
(a) Tìm xác suất electron xuyên ngầm qua rào thế nếu bề rộng rào là $0{,}800\,\mathrm{nm}$.
(b) Xác định bề rộng rào thế cần thiết để xác suất xuyên ngầm tăng gấp đôi giá trị tìm được ở câu (a).

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Năng lượng electron: $E = 3{,}50\,\mathrm{eV}$.
- Chiều cao rào thế: $U_0 = 4{,}00\,\mathrm{eV}$.
- Bề rộng ban đầu: $L_1 = 0{,}800\,\mathrm{nm}$.
- Cần tìm: Xác suất $T_1$ và bề rộng $L_2$ để $T_2 = 2T_1$.

**Hướng đi:**
- Tính hệ số suy giảm $\kappa$ và hệ số tiền hàm mũ $G$, sau đó dùng công thức $T = G e^{-2\kappa L}$ để tính $T_1$.
- Để xác suất tăng gấp đôi, tỷ số truyền qua thỏa mãn $e^{-2\kappa L_2} = 2 e^{-2\kappa L_1}$. Lấy logarit tự nhiên hai vế giúp ta xác định trực tiếp độ thu hẹp bề rộng rào $\Delta L = L_1 - L_2 = \frac{\ln 2}{2\kappa}$.

**Lời giải chi tiết:**

Độ hụt năng lượng dưới đỉnh rào:
$$
\begin{aligned}
U_0-E&=(4{,}00-3{,}50)\,\mathrm{eV}\\
&=0{,}50\,\mathrm{eV}\\
&\approx8{,}01\times10^{-20}\,\mathrm J.
\end{aligned}
$$

Hệ số suy giảm $\kappa$:
Tính tử số:
Đặt $q$ là tử số trong biểu thức của $\kappa$:

$$
\begin{aligned}
q&=\sqrt{2m_e(U_0-E)}\\
&\approx 3{,}820 \times 10^{-25}\,\mathrm{kg\cdot m/s}.
\end{aligned}
$$
$$
\begin{aligned}
\kappa &= \frac{\sqrt{2m_e(U_0 - E)}}{\hbar} \\
&\approx \frac{3{,}820 \times 10^{-25}}{1{,}055 \times 10^{-34}} \\
&\approx 3{,}62 \times 10^9\,\mathrm{m}^{-1} \\
&= 3{,}62\,\mathrm{nm}^{-1}.
\end{aligned}
$$

Thừa số tiền hàm mũ $G$:
$$
\frac{E}{U_0} = \frac{3{,}50}{4{,}00} = 0{,}875.
$$
$$
\begin{aligned}
G &= 16(0{,}875)(1 - 0{,}875) \\
&= 16(0{,}875)(0{,}125) \\
&= 1{,}75.
\end{aligned}
$$

(a) Xác suất xuyên ngầm với $L_1 = 0{,}800\,\mathrm{nm}$:
Số mũ suy giảm:
$$
\begin{aligned}
2\kappa L_1&\approx2(3{,}623)(0{,}800)\\
&\approx5{,}797.
\end{aligned}
$$

Hệ số truyền qua:
$$
\begin{aligned}
T_1 &= G e^{-2\kappa L_1} \\
&\approx 1{,}75 \times e^{-5{,}797} \\
&\approx 5{,}33 \times 10^{-3}.
\end{aligned}
$$

(b) Bề rộng rào $L_2$ để xác suất tăng gấp đôi ($T_2 = 2T_1$):
Từ hệ thức tỷ số:
$$
\begin{aligned}
\frac{T_2}{T_1} &= \frac{G e^{-2\kappa L_2}}{G e^{-2\kappa L_1}} \\
&= e^{-2\kappa(L_2 - L_1)} \\
&= 2.
\end{aligned}
$$

Lấy logarit tự nhiên hai vế:
$$
-2\kappa(L_2 - L_1) = \ln 2,
$$
Suy ra:
$$
L_1 - L_2 = \frac{\ln 2}{2\kappa}.
$$

Thay số:
$$
\begin{aligned}
\Delta L &= \frac{\ln 2}{2(3{,}623\,\mathrm{nm}^{-1})} \\
&\approx \frac{0{,}6931}{7{,}246\,\mathrm{nm}^{-1}} \\
&\approx 0{,}0957\,\mathrm{nm}.
\end{aligned}
$$

Bề rộng rào mới:
$$
\begin{aligned}
L_2 &= L_1 - \Delta L \\
&= 0{,}800\,\mathrm{nm} - 0{,}0957\,\mathrm{nm} \\
&\approx 0{,}704\,\mathrm{nm}.
\end{aligned}
$$

Chỉ cần thu hẹp rào thế đi khoảng $0{,}096\,\mathrm{nm}$ (chưa bằng đường kính một nguyên tử hydro), dòng hạt xuyên hầm đã tăng lên gấp đôi.

</details>

---

### VP40.7.3

Một rào thế vuông cao $5{,}00\,\mathrm{eV}$ và có bề rộng $0{,}900\,\mathrm{nm}$. Hãy tìm xác suất để một electron xuyên ngầm qua rào thế này nếu năng lượng ban đầu của nó là:
(a) $4{,}00\,\mathrm{eV}$.
(b) $4{,}30\,\mathrm{eV}$.
(c) $4{,}60\,\mathrm{eV}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Chiều cao rào thế: $U_0 = 5{,}00\,\mathrm{eV}$.
- Bề rộng rào thế: $L = 0{,}900\,\mathrm{nm} = 9{,}00 \times 10^{-10}\,\mathrm{m}$.
- Năng lượng electron: (a) $4{,}00\,\mathrm{eV}$, (b) $4{,}30\,\mathrm{eV}$, (c) $4{,}60\,\mathrm{eV}$.
- Cần tìm: Hệ số truyền qua $T$ cho từng trường hợp.

**Hướng đi:**
- Với mỗi giá trị năng lượng $E$, ta tính độ hụt năng lượng $U_0 - E$, suy ra hệ số suy giảm $\kappa = \frac{\sqrt{2m_e(U_0 - E)}}{\hbar}$ và hệ số tiền hàm mũ $G = 16 \frac{E}{U_0} \left(1 - \frac{E}{U_0}\right)$.
- Sau đó tính hệ số truyền qua bằng công thức $T = G e^{-2\kappa L}$.

**Lời giải chi tiết:**

(a) Trường hợp $E = 4{,}00\,\mathrm{eV}$:
- Độ hụt: $U_0 - E = 1{,}00\,\mathrm{eV} = 1{,}602 \times 10^{-19}\,\mathrm{J}$.
- Hệ số $\kappa$:
Tính tử số:
Đặt $q$ là tử số trong biểu thức của $\kappa$:

$$
\begin{aligned}
q&=\sqrt{2m_e(U_0-E)}\\
&\approx 5{,}404 \times 10^{-25}\,\mathrm{kg\cdot m/s}.
\end{aligned}
$$
$$
\begin{aligned}
\kappa &= \frac{\sqrt{2m_e(U_0 - E)}}{\hbar} \\
&\approx \frac{5{,}404 \times 10^{-25}}{1{,}055 \times 10^{-34}} \\
&\approx 5{,}124 \times 10^9\,\mathrm{m}^{-1} \\
&= 5{,}124\,\mathrm{nm}^{-1}.
\end{aligned}
$$
- Hệ số tiền hàm mũ:
$$
\begin{aligned}
G &= 16(0{,}80)(1 - 0{,}80) \\
&= 16(0{,}80)(0{,}20) \\
&= 2{,}56.
\end{aligned}
$$
- Số mũ suy giảm: $2\kappa L = 2 \times 5{,}124 \times 0{,}900 \approx 9{,}223$.
- Xác suất xuyên ngầm:
$$
\begin{aligned}
T_a &= 2{,}56 \times e^{-9{,}223} \\
&\approx 2{,}54 \times 10^{-4}.
\end{aligned}
$$

(b) Trường hợp $E = 4{,}30\,\mathrm{eV}$:
- Độ hụt: $U_0 - E = 0{,}70\,\mathrm{eV} = 1{,}121 \times 10^{-19}\,\mathrm{J}$.
- Hệ số $\kappa$:
Tính tử số:
Đặt $q$ là tử số trong biểu thức của $\kappa$:

$$
\begin{aligned}
q&=\sqrt{2m_e(U_0-E)}\\
&\approx 4{,}521 \times 10^{-25}\,\mathrm{kg\cdot m/s}.
\end{aligned}
$$
$$
\begin{aligned}
\kappa &= \frac{\sqrt{2m_e(U_0 - E)}}{\hbar} \\
&\approx \frac{4{,}521 \times 10^{-25}}{1{,}055 \times 10^{-34}} \\
&\approx 4{,}287 \times 10^9\,\mathrm{m}^{-1} \\
&= 4{,}287\,\mathrm{nm}^{-1}.
\end{aligned}
$$
- Hệ số tiền hàm mũ:
$$
\begin{aligned}
G &= 16(0{,}86)(1 - 0{,}86) \\
&= 16(0{,}86)(0{,}14) \\
&\approx 1{,}926.
\end{aligned}
$$
- Số mũ suy giảm: $2\kappa L = 2 \times 4{,}287 \times 0{,}900 \approx 7{,}716$.
- Xác suất xuyên ngầm:
$$
\begin{aligned}
T_b &= 1{,}926 \times e^{-7{,}716} \\
&\approx 8{,}59 \times 10^{-4}.
\end{aligned}
$$

(c) Trường hợp $E = 4{,}60\,\mathrm{eV}$:
- Độ hụt: $U_0 - E = 0{,}40\,\mathrm{eV} = 6{,}409 \times 10^{-20}\,\mathrm{J}$.
- Hệ số $\kappa$:
Tính tử số:
Đặt $q$ là tử số trong biểu thức của $\kappa$:

$$
\begin{aligned}
q&=\sqrt{2m_e(U_0-E)}\\
&\approx 3{,}418 \times 10^{-25}\,\mathrm{kg\cdot m/s}.
\end{aligned}
$$
$$
\begin{aligned}
\kappa &= \frac{\sqrt{2m_e(U_0 - E)}}{\hbar} \\
&\approx \frac{3{,}418 \times 10^{-25}}{1{,}055 \times 10^{-34}} \\
&\approx 3{,}241 \times 10^9\,\mathrm{m}^{-1} \\
&= 3{,}241\,\mathrm{nm}^{-1}.
\end{aligned}
$$
- Hệ số tiền hàm mũ:
$$
\begin{aligned}
G &= 16(0{,}92)(1 - 0{,}92) \\
&= 16(0{,}92)(0{,}08) \\
&\approx 1{,}178.
\end{aligned}
$$
- Số mũ suy giảm: $2\kappa L = 2 \times 3{,}241 \times 0{,}900 \approx 5{,}833$.
- Xác suất xuyên ngầm:
$$
\begin{aligned}
T_c &= 1{,}178 \times e^{-5{,}833} \\
&\approx 3{,}46 \times 10^{-3}.
\end{aligned}
$$

Nhận xét: Khi năng lượng hạt tiến gần đến đỉnh rào (độ hụt giảm từ $1{,}00\,\mathrm{eV}$ xuống $0{,}40\,\mathrm{eV}$), xác suất truyền qua tăng hơn 13 lần.

</details>

---

### VP40.7.4

Xác suất để một electron có năng lượng $3{,}00\,\mathrm{eV}$ xuyên ngầm qua một rào thế vuông cao $5{,}00\,\mathrm{eV}$ là $1/417$. Hãy xác định bề rộng của rào thế này.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Năng lượng electron: $E = 3{,}00\,\mathrm{eV}$.
- Chiều cao rào thế: $U_0 = 5{,}00\,\mathrm{eV}$.
- Xác suất truyền qua: $T = \frac{1}{417} \approx 2{,}398 \times 10^{-3}$.
- Cần tìm: Bề rộng $L$ của rào thế.

**Hướng đi:**
- Xác định hệ số suy giảm $\kappa$ và hệ số tiền hàm mũ $G$ từ các thông số năng lượng.
- Từ công thức $T = G e^{-2\kappa L}$, ta giải phương trình mũ để tìm bề rộng $L = \frac{1}{2\kappa} \ln\left(\frac{G}{T}\right)$.

**Lời giải chi tiết:**

Độ hụt năng lượng dưới đỉnh rào:
$$
\begin{aligned}
U_0-E&=(5{,}00-3{,}00)\,\mathrm{eV}\\
&=2{,}00\,\mathrm{eV}\\
&\approx3{,}204\times10^{-19}\,\mathrm J.
\end{aligned}
$$

Hệ số suy giảm $\kappa$:
Tính tử số:
Đặt $q$ là tử số trong biểu thức của $\kappa$:

$$
\begin{aligned}
q&=\sqrt{2m_e(U_0-E)}\\
&\approx 7{,}641 \times 10^{-25}\,\mathrm{kg\cdot m/s}.
\end{aligned}
$$
$$
\begin{aligned}
\kappa &= \frac{\sqrt{2m_e(U_0 - E)}}{\hbar} \\
&\approx \frac{7{,}641 \times 10^{-25}}{1{,}055 \times 10^{-34}} \\
&\approx 7{,}245 \times 10^9\,\mathrm{m}^{-1} \\
&= 7{,}245\,\mathrm{nm}^{-1}.
\end{aligned}
$$

Hệ số tiền hàm mũ $G$:
$$
\frac{E}{U_0} = \frac{3{,}00}{5{,}00} = 0{,}60.
$$
$$
\begin{aligned}
G &= 16(0{,}60)(1 - 0{,}60) \\
&= 16(0{,}60)(0{,}40) \\
&= 3{,}84.
\end{aligned}
$$

Thiết lập phương trình truyền qua:
$$
T = G e^{-2\kappa L},
$$
Suy ra:
$$
e^{2\kappa L} = \frac{G}{T}.
$$
Lấy logarit tự nhiên hai vế:
$$
2\kappa L = \ln\left(\frac{G}{T}\right).
$$

Thay các giá trị số:
$$
\begin{aligned}
\frac{G}{T} &= 3{,}84 \times 417 \\
&= 1601{,}28.
\end{aligned}
$$
$$
2\kappa L = \ln(1601{,}28) \approx 7{,}379.
$$

Suy ra bề rộng của rào thế:
$$
\begin{aligned}
L &= \frac{7{,}379}{2(7{,}245\,\mathrm{nm}^{-1})} \\
&\approx 0{,}509\,\mathrm{nm}.
\end{aligned}
$$

Kết quả thu được hoàn toàn tương thích với điều kiện áp dụng của công thức xấp xỉ vì $2\kappa L \approx 7{,}38 > 1$ và $T \approx 0{,}0024 \ll 1$.

</details>
