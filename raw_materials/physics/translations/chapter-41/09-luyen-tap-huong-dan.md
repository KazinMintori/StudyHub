## Luyện tập hướng dẫn

Nhóm 12 bài luyện tập sau củng cố kỹ năng giải các bài toán trọng tâm của cơ học lượng tử trong không gian ba chiều: Hạt trong hộp thế lập phương, hàm sóng và lượng tử hóa mômen động lượng của nguyên tử hydro, cùng các hiệu ứng spin và cấu trúc tinh tế.

Trong các phép tính, sử dụng các hằng số vật lý tiêu chuẩn:
$$
\begin{aligned}
&h = 6{,}626 \times 10^{-34}\,\mathrm{J\cdot s}, \\
&\hbar \approx 1{,}055 \times 10^{-34}\,\mathrm{J\cdot s}, \\
&c = 3{,}00 \times 10^8\,\mathrm{m/s}, \\
&e = 1{,}602 \times 10^{-19}\,\mathrm{C}, \\
&m_e = 9{,}109 \times 10^{-31}\,\mathrm{kg}, \\
&a = 5{,}292 \times 10^{-11}\,\mathrm{m}, \\
&\mu_B \approx 9{,}274 \times 10^{-24}\,\mathrm{J/T}, \\
&\mu_B \approx 5{,}788 \times 10^{-5}\,\mathrm{eV/T}, \\
&\alpha \approx 1/137{,}04.
\end{aligned}
$$

---

### VP41.1.1

Một hạt chuyển động trong hộp thế ba chiều có kích thước các cạnh bằng nhau và bằng $L$ như mô tả ở Hình 41.1 đang ở trạng thái lượng tử có các số lượng tử $n_X = 2$, $n_Y = 1$, $n_Z = 3$. Hãy xác định:
(a) Các mặt phẳng bên trong hộp (khác với các vách hộp) mà tại đó hàm phân bố xác suất tìm thấy hạt triệt tiêu.
(b) Xác suất để tìm thấy hạt ở vị trí bất kỳ trong miền không gian xác định bởi $0 \le x \le L/3$.

![Hình 41.1: Hạt bị giam trong hộp thế lập phương ba chiều có cạnh L với các thành tại x = 0, x = L, y = 0, y = L, z = 0 và z = L.](./img/young-41/hinh-tham-chieu-hop.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hộp thế lập phương ba chiều cạnh $L$, hạt ở trạng thái $(n_X, n_Y, n_Z) = (2, 1, 3)$.
- Cần tìm: (a) Các mặt phẳng nút bên trong lòng hộp; (b) Xác suất tìm thấy hạt trong miền $0 \le x \le L/3$.

**Hướng đi:**
- Hàm sóng dừng trong hộp lập phương ba chiều là tích tách biến của ba hàm sóng một chiều:
$$
\psi(x, y, z) = X(x)Y(y)Z(z)
$$
- Mật độ xác suất $|\psi|^2$ triệt tiêu khi một trong ba thành phần tọa độ triệt tiêu, tạo thành các mặt phẳng nút song song với các vách hộp.
- Vì ba biến số độc lập, xác suất tìm thấy hạt trong một khoảng tọa độ $x$ được tính bằng tích phân của $|X_{n_X}(x)|^2$ trên đoạn đó, trong khi tích phân theo $y$ và $z$ trên toàn bộ bề rộng $[0, L]$ đều chuẩn hóa bằng 1.

**Lời giải chi tiết:**

(a) Xác định các mặt phẳng nút bên trong hộp:
Hàm sóng dừng của hạt trong hộp lập phương có dạng tích tách biến $\psi(x, y, z) = X_2(x) Y_1(y) Z_3(z)$ với:
$$
\begin{aligned}
&X_2(x) = \sqrt{\frac{2}{L}}\sin\frac{2\pi x}{L}, \\
&Y_1(y) = \sqrt{\frac{2}{L}}\sin\frac{\pi y}{L}, \\
&Z_3(z) = \sqrt{\frac{2}{L}}\sin\frac{3\pi z}{L}.
\end{aligned}
$$

Hàm mật độ xác suất $|\psi(x, y, z)|^2 = 0$ khi một trong ba thừa số hình sin triệt tiêu tại các điểm bên trong hộp ($0 < x, y, z < L$):
- Đối với phương $x$: Điểm nút thỏa mãn $\sin(2\pi x/L) = 0$, cho $2\pi x/L = \pi$, suy ra mặt phẳng:
$$
x = \frac{L}{2}
$$
- Đối với phương $y$: Thừa số $\sin(\pi y/L)$ chỉ triệt tiêu tại hai mép vách $y = 0$ và $y = L$, do đó không có mặt phẳng nút nào nằm bên trong lòng hộp.
- Đối với phương $z$: Điểm nút thỏa mãn $\sin(3\pi z/L) = 0$, cho $3\pi z/L = \pi$ hoặc $2\pi$, suy ra hai mặt phẳng:
$$
\begin{aligned}
&z = \frac{L}{3}, \\
&z = \frac{2L}{3}.
\end{aligned}
$$

Vậy các mặt phẳng nút bên trong hộp là:
$$
\begin{aligned}
&x = \frac{L}{2}, \\
&z = \frac{L}{3}, \quad z = \frac{2L}{3}.
\end{aligned}
$$

(b) Tính xác suất hạt nằm trong miền $0 \le x \le L/3$:
Do hàm sóng chuẩn hóa độc lập theo từng phương:
$$
\begin{aligned}
&\int_0^L |Y_1(y)|^2\,\mathrm{d}y = 1, \\
&\int_0^L |Z_3(z)|^2\,\mathrm{d}z = 1.
\end{aligned}
$$

Đặt biến số không thứ nguyên $u = x/L$ với $\mathrm{d}u = \mathrm{d}x/L$, xác suất cần tìm quy về tích phân một chiều:
$$
P = \int_0^{1/3} 2\sin^2(2\pi u)\,\mathrm{d}u
$$

Sử dụng công thức hạ bậc $\sin^2\theta = \frac{1 - \cos(2\theta)}{2}$:
$$
\begin{aligned}
P &= \int_0^{1/3} [1 - \cos(4\pi u)]\,\mathrm{d}u \\
&= \left[ u - \frac{\sin(4\pi u)}{4\pi} \right]_0^{1/3} \\
&= \frac{1}{3} - \frac{\sin(4\pi/3)}{4\pi}
\end{aligned}
$$

Vì $\sin(4\pi/3) = -\frac{\sqrt{3}}{2}$, ta thu được:
$$
\begin{aligned}
P &= \frac{1}{3} + \frac{\sqrt{3}}{8\pi} \\
&\approx 0{,}3333 + 0{,}0689 \\
&\approx 0{,}402
\end{aligned}
$$

![Hình minh họa: Phân bố xác suất và mặt phẳng nút của trạng thái n_x = 2.](./img/young-41/loi-giai-c-01.svg)

</details>

---

### VP41.1.2

Một nửa thể tích của hộp thế ba chiều cạnh $L$ nằm trong vùng không gian $L/4 \le x \le 3L/4$. Hãy tính xác suất để tìm thấy hạt trong vùng này nếu hạt ở các trạng thái lượng tử sau:
(a) $n_X = 1$, $n_Y = 1$, $n_Z = 1$.
(b) $n_X = 2$, $n_Y = 1$, $n_Z = 2$.
(c) $n_X = 3$, $n_Y = 2$, $n_Z = 3$.
(d) $n_X = 4$, $n_Y = 1$, $n_Z = 1$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hộp thế ba chiều cạnh $L$, miền khảo sát: $L/4 \le x \le 3L/4$, $0 \le y \le L$, $0 \le z \le L$.
- Cần tính xác suất $P$ đối với các bộ số lượng tử: (a) $(1,1,1)$; (b) $(2,1,2)$; (c) $(3,2,3)$; (d) $(4,1,1)$.

**Hướng đi:**
- Giới hạn tích phân của $y$ và $z$ bao trọn toàn bộ hộp $[0, L]$, do đó tích phân theo $y$ và $z$ bằng 1.
- Xác suất chỉ phụ thuộc vào số lượng tử $n_X$ theo công thức tích phân dọc theo trục $x$:
$$
\begin{aligned}
&P(n_X) = \int_{L/4}^{3L/4} |X(x)|^2\,\mathrm{d}x, \\
&|X(x)|^2 = \frac{2}{L}\sin^2\left(\frac{n_X\pi x}{L}\right).
\end{aligned}
$$
- Đặt ẩn phụ $u = x/L$, chuyển về tích phân trên đoạn $[1/4, 3/4]$.

**Lời giải chi tiết:**

Đặt biến số không thứ nguyên $u = x/L$, hàm nguyên hàm có dạng:
$$
\begin{aligned}
&F(u) = u - \frac{\sin(2n_X\pi u)}{2n_X\pi}, \\
&P(n_X) = F(3/4) - F(1/4).
\end{aligned}
$$

(a) Với trạng thái $n_X = 1$:
$$
\begin{aligned}
P(1) &= \frac{1}{2} - \frac{(-1) - (1)}{2\pi} \\
&= \frac{1}{2} + \frac{1}{\pi} \\
&\approx 0{,}500 + 0{,}318 \\
&= 0{,}818
\end{aligned}
$$

(b) Với trạng thái $n_X = 2$:
$$
\begin{aligned}
P(2) &= \frac{1}{2} - \frac{0 - 0}{4\pi} \\
&= \frac{1}{2} \\
&= 0{,}500
\end{aligned}
$$

(c) Với trạng thái $n_X = 3$:
$$
\begin{aligned}
P(3) &= \frac{1}{2} - \frac{1 - (-1)}{6\pi} \\
&= \frac{1}{2} - \frac{1}{3\pi} \\
&\approx 0{,}500 - 0{,}106 \\
&= 0{,}394
\end{aligned}
$$

(d) Với trạng thái $n_X = 4$:
$$
\begin{aligned}
P(4) &= \frac{1}{2} - \frac{0 - 0}{8\pi} \\
&= \frac{1}{2} \\
&= 0{,}500
\end{aligned}
$$

</details>

---

### VP41.1.3

Miền không gian xác định bởi $0 \le x \le L/4$, $0 \le y \le L/4$ và $0 \le z \le L$ chiếm tỷ lệ thể tích bằng $1/16 = 0{,}0625$ của hộp thế lập phương ba chiều cạnh $L$. Hãy xác định xác suất tìm thấy hạt trong miền này đối với các trạng thái sau:
(a) $n_X = 1$, $n_Y = 1$, $n_Z = 1$.
(b) $n_X = 2$, $n_Y = 1$, $n_Z = 2$.
(c) $n_X = 3$, $n_Y = 2$, $n_Z = 3$.
(d) $n_X = 4$, $n_Y = 1$, $n_Z = 1$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Miền thể tích góc: $0 \le x \le L/4$, $0 \le y \le L/4$, $0 \le z \le L$.
- Cần tính xác suất $P = P_x(n_X) \cdot P_y(n_Y)$ cho bốn trạng thái cho trước.

**Hướng đi:**
- Xác suất được phân rã thành tích của hai xác suất thành phần theo $x$ và $y$:
$$
\begin{aligned}
&P = P_x \cdot P_y, \\
&P_x = I(n_X), \quad P_y = I(n_Y).
\end{aligned}
$$
- Tích phân một chiều $I(n) = \int_0^{1/4} 2\sin^2(n\pi u)\,\mathrm{d}u$:
$$
\begin{aligned}
&I(n) = \frac{1}{4} - \frac{S_n}{2n\pi}, \\
&S_n = \sin(n\pi/2).
\end{aligned}
$$

**Lời giải chi tiết:**

Tính giá trị $I(n)$ cho các số lượng tử $n = 1, 2, 3, 4$:
- Với $n = 1$:
$$
\begin{aligned}
I(1) &= \frac{1}{4} - \frac{1}{2\pi} \\
&\approx 0{,}09085
\end{aligned}
$$
- Với $n = 2$:
$$
I(2) = \frac{1}{4} = 0{,}2500
$$
- Với $n = 3$:
$$
\begin{aligned}
I(3) &= \frac{1}{4} + \frac{1}{6\pi} \\
&\approx 0{,}30305
\end{aligned}
$$
- Với $n = 4$:
$$
I(4) = \frac{1}{4} = 0{,}2500
$$

Áp dụng cho từng trạng thái:

(a) Trạng thái $(n_X, n_Y, n_Z) = (1, 1, 1)$:
$$
\begin{aligned}
P &= I(1) \cdot I(1) \\
&\approx (0{,}09085)^2 \\
&\approx 8{,}25 \times 10^{-3}
\end{aligned}
$$

(b) Trạng thái $(n_X, n_Y, n_Z) = (2, 1, 2)$:
$$
\begin{aligned}
P &= I(2) \cdot I(1) \\
&\approx 0{,}2500 \times 0{,}09085 \\
&\approx 0{,}0227
\end{aligned}
$$

(c) Trạng thái $(n_X, n_Y, n_Z) = (3, 2, 3)$:
$$
\begin{aligned}
P &= I(3) \cdot I(2) \\
&\approx 0{,}30305 \times 0{,}2500 \\
&\approx 0{,}0758
\end{aligned}
$$

(d) Trạng thái $(n_X, n_Y, n_Z) = (4, 1, 1)$:
$$
\begin{aligned}
P &= I(4) \cdot I(1) \\
&\approx 0{,}2500 \times 0{,}09085 \\
&\approx 0{,}0227
\end{aligned}
$$

</details>

---

### VP41.1.4

Xét miền không gian hình lập phương nằm ở tâm của hộp thế ba chiều cạnh $L$, được giới hạn bởi $L/4 \le x \le 3L/4$, $L/4 \le y \le 3L/4$, $L/4 \le z \le 3L/4$.
(a) Thể tích của miền lập phương này chiếm bao nhiêu phần tổng thể tích của toàn bộ hộp thế?
(b) Nếu một hạt trong hộp đang ở trạng thái cơ bản $n_X = 1$, $n_Y = 1$, $n_Z = 1$, hãy tính xác suất để tìm thấy hạt ở vị trí bất kỳ bên trong miền lập phương ở tâm này.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Miền khối lập phương tâm: Mỗi cạnh có bề rộng $\Delta x = \Delta y = \Delta z = L/2$.
- Cần tính: (a) Tỷ lệ thể tích; (b) Xác suất ở trạng thái cơ bản $(1, 1, 1)$.

**Hướng đi:**
- Thể tích khối lập phương ở tâm là $(\Delta L)^3 = (L/2)^3$.
- Do tính tách biến và đối xứng hoàn toàn giữa ba trục, xác suất toàn phần trong khối lập phương là tích lập phương của xác suất một chiều: $P = [P_x(1)]^3$.

**Lời giải chi tiết:**

(a) Xác định tỷ lệ thể tích:
Thể tích của toàn bộ hộp là $V_{\text{hộp}} = L^3$. Bề rộng mỗi cạnh của miền lập phương ở tâm là:
$$
\begin{aligned}
&L_x = \frac{3L}{4} - \frac{L}{4} = \frac{L}{2}, \\
&V_{\text{tâm}} = L_x^3 = \frac{L^3}{8}.
\end{aligned}
$$

Phân số thể tích là:
$$
\frac{V_{\text{tâm}}}{V_{\text{hộp}}} = \frac{1}{8} = 0{,}125
$$

(b) Tính xác suất hạt ở trạng thái cơ bản nằm trong miền lập phương tâm:
Hàm sóng trạng thái cơ bản phụ thuộc ba tọa độ. Ký hiệu gọn hàm này là $\psi_{111}$, ta có:

$$
\psi_{111}=X_1(x)Y_1(y)Z_1(z).
$$

Trong đó:
$$
X_1(x) = \sqrt{\frac{2}{L}}\sin\frac{\pi x}{L}
$$
và tương tự cho các biến $y, z$.

Tích phân xác suất theo mỗi phương chính là kết quả $P(1)$ đã tính ở Bài VP41.1.2:
$$
\begin{aligned}
&P_x = P_y = P_z = P(1), \\
&P(1) \approx 0{,}8183.
\end{aligned}
$$

Vì ba phương tọa độ hoàn toàn độc lập và có cùng số lượng tử $n = 1$:
$$
\begin{aligned}
P &= P_x \cdot P_y \cdot P_z \\
&= (P_x)^3 \\
&\approx (0{,}8183)^3 \\
&\approx 0{,}548
\end{aligned}
$$

Xác suất tìm thấy hạt trong miền trung tâm chiếm hơn $54{,}8\%$, lớn hơn rất nhiều so với tỷ lệ thể tích hình học $12{,}5\%$, do hàm sóng trạng thái cơ bản tập trung mật độ cực đại tại tâm hộp.

</details>

---

### VP41.4.1

Xét các trạng thái lượng tử có số lượng tử chính $n = 6$ của nguyên tử hydro.
(a) Có bao nhiêu trạng thái $(l, m_l)$ phân biệt ứng với mức này?
(b) Tính độ lớn cực đại của mômen động lượng quỹ đạo $L$ theo đơn vị $\hbar$.
(c) Tính giá trị cực đại của thành phần $z$ của mômen động lượng quỹ đạo theo đơn vị $\hbar$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Mức năng lượng $n = 6$ của nguyên tử hydro.
- Cần tìm: (a) Số trạng thái $(l, m_l)$ khác nhau; (b) Giá trị lớn nhất của $L$; (c) Giá trị lớn nhất của $L_z$.

**Hướng đi:**
- Với số lượng tử chính $n$, số lượng tử quỹ đạo $l$ nhận các giá trị nguyên từ $0$ đến $n - 1$.
- Với mỗi giá trị $l$, số lượng tử từ quỹ đạo $m_l$ nhận $2l + 1$ giá trị từ $-l$ đến $+l$. Tổng số trạng thái quỹ đạo bằng $\sum_{l=0}^{n-1} (2l+1) = n^2$.
- Độ lớn mômen động lượng quỹ đạo được lượng tử hóa theo hệ thức $L = \sqrt{l(l+1)}\hbar$, đạt cực đại khi $l = l_{\max} = n - 1$.
- Thành phần hình chiếu trên trục $z$ là $L_z = m_l\hbar$, đạt cực đại khi $m_l = l_{\max}$.

**Lời giải chi tiết:**

(a) Tổng số trạng thái $(l, m_l)$ phân biệt:
Với $n = 6$, số lượng tử quỹ đạo $l$ nhận các giá trị $l \in \{0, 1, 2, 3, 4, 5\}$. Tổng số trạng thái là:
$$
\begin{aligned}
N &= \sum_{l=0}^5 (2l + 1) \\
&= 1 + 3 + 5 + 7 + 9 + 11 \\
&= 6^2 \\
&= 36
\end{aligned}
$$

(b) Độ lớn cực đại của mômen động lượng quỹ đạo $L$:
Giá trị lớn nhất của $l$ là $l_{\max} = n - 1 = 5$. Khi đó:
$$
\begin{aligned}
L_{\max} &= \sqrt{l_{\max}(l_{\max} + 1)}\,\hbar \\
&= \sqrt{5(5 + 1)}\,\hbar \\
&= \sqrt{30}\,\hbar \\
&\approx 5{,}477\,\hbar
\end{aligned}
$$

(c) Giá trị cực đại của thành phần hình chiếu $L_z$:
Hình chiếu $L_z$ đạt cực đại khi số lượng tử từ nhận giá trị lớn nhất:
$$
m_{l,\max} = l_{\max} = 5
$$
Suy ra:
$$
L_{z,\max} = m_{l,\max}\hbar = 5\,\hbar
$$

</details>

---

### VP41.4.2

(a) Hãy liệt kê tất cả các tổ hợp giá trị có thể có của $l$ và $m_l$ đối với các trạng thái có $n = 3$ của nguyên tử hydro.
(b) Trong các trạng thái trên, trạng thái nào có góc hợp bởi vector mômen động lượng quỹ đạo $\vec{L}$ và chiều âm của trục $z$ đạt giá trị nhỏ nhất, và góc đó bằng bao nhiêu độ?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Mức năng lượng $n = 3$ của nguyên tử hydro.
- Cần làm: (a) Liệt kê toàn bộ các cặp $(l, m_l)$; (b) Xác định trạng thái có góc nhỏ nhất so với trục $-z$ và tính góc đó.

**Hướng đi:**
- Với $n = 3$, các giá trị cho phép của $l$ là $0, 1, 2$. Với mỗi $l$, $m_l \in \{-l, \dots, l\}$.
- Góc $\theta$ giữa vector $\vec{L}$ và chiều dương trục $+z$ tuân theo hệ thức:
$$
\cos\theta = \frac{L_z}{L} = \frac{m_l}{\sqrt{l(l+1)}}
$$
- Góc $\phi$ giữa $\vec{L}$ và chiều âm trục $-z$ liên hệ bởi $\phi = 180^\circ - \theta$, do đó:
$$
\cos\phi = \frac{-m_l}{\sqrt{l(l+1)}}
$$
- Để góc $\phi$ nhỏ nhất, $\cos\phi$ phải đạt cực đại dương, nghĩa là chọn $m_l = -l$ với giá trị $l$ lớn nhất.

**Lời giải chi tiết:**

(a) Liệt kê tất cả các tổ hợp $(l, m_l)$ cho $n = 3$:
- Phân lớp $l = 0$ ($3s$): Gồm 1 trạng thái:
  $(l, m_l) = (0, 0)$.
- Phân lớp $l = 1$ ($3p$): Gồm 3 trạng thái:
  $(1, 1)$, $(1, 0)$, $(1, -1)$.
- Phân lớp $l = 2$ ($3d$): Gồm 5 trạng thái:
  $(2, 2)$, $(2, 1)$, $(2, 0)$, $(2, -1)$, $(2, -2)$.

Tổng cộng có đúng $1 + 3 + 5 = 9 = 3^2$ trạng thái lượng tử quỹ đạo.

(b) Tìm góc nhỏ nhất hợp với chiều âm trục $z$:
Với trạng thái $l = 0$, $L = 0$ nên hướng của vector mômen động lượng không xác định.
Xét các trạng thái có $l > 0$:
- Với $l = 1$: Vector hướng gần chiều âm trục $z$ nhất khi $m_l = -1$:
$$
\begin{aligned}
\cos\phi &= \frac{1}{\sqrt{2}}, \\
\phi &= 45{,}0^\circ.
\end{aligned}
$$
- Với $l = 2$: Vector hướng gần chiều âm trục $z$ nhất khi $m_l = -2$:
$$
\cos\phi = \frac{2}{\sqrt{6}} = \sqrt{\frac{2}{3}}
$$
Suy ra:
$$
\begin{aligned}
\phi_{\min} &= \arccos\sqrt{2/3} \\
&\approx 35{,}3^\circ.
\end{aligned}
$$

Vậy trạng thái có góc nhỏ nhất hợp với chiều âm trục $z$ là $(l, m_l) = (2, -2)$ với góc bằng $35{,}3^\circ$.

![Hình minh họa: Các hướng lượng tử hóa của vector mômen động lượng l = 2.](./img/young-41/loi-giai-c-02.svg)

</details>

---

### VP41.4.3

Một photon được phát ra khi nguyên tử hydro chuyển mức từ một trạng thái có mức năng lượng cao về mức năng lượng thấp hơn. Hãy tính năng lượng của photon phát ra theo đơn vị electron-volt ($\mathrm{eV}$) đối với mỗi bước chuyển sau:
(a) Từ trạng thái $n = 3, l = 2, m_l = -2$ về trạng thái $n = 2, l = 1, m_l = -1$.
(b) Từ trạng thái $n = 4, l = 2, m_l = 1$ về trạng thái $n = 2, l = 1, m_l = 0$.
(c) Từ trạng thái $n = 2, l = 1, m_l = 1$ về trạng thái $n = 1, l = 0, m_l = 0$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Tính năng lượng photon $E_{\text{ph}}$ cho ba bước chuyển quang phổ trong nguyên tử hydro khi không có từ trường ngoài.

**Hướng đi:**
- Khi bỏ qua tương tác spin-quỹ đạo và không có từ trường ngoài, mức năng lượng của nguyên tử hydro chỉ phụ thuộc duy nhất vào số lượng tử chính $n$:
$$
E_n = -\frac{13{,}606\,\mathrm{eV}}{n^2}
$$
- Năng lượng của photon phát ra bằng hiệu năng lượng giữa hai mức với $E_0 = 13{,}606\,\mathrm{eV}$:
$$
E_{\text{ph}} = E_0\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right)
$$

**Lời giải chi tiết:**

(a) Chuyển mức từ $n = 3$ về $n = 2$:
$$
\begin{aligned}
E_{\text{ph}} &= E_0 \left(\frac{1}{4} - \frac{1}{9}\right) \\
&= E_0 \cdot \frac{5}{36} \\
&\approx 1{,}89\,\mathrm{eV}
\end{aligned}
$$

(b) Chuyển mức từ $n = 4$ về $n = 2$:
$$
\begin{aligned}
E_{\text{ph}} &= E_0 \left(\frac{1}{4} - \frac{1}{16}\right) \\
&= E_0 \cdot \frac{3}{16} \\
&\approx 2{,}55\,\mathrm{eV}
\end{aligned}
$$

(c) Chuyển mức từ $n = 2$ về $n = 1$:
$$
\begin{aligned}
E_{\text{ph}} &= E_0 \left(1 - \frac{1}{4}\right) \\
&= E_0 \cdot \frac{3}{4} \\
&\approx 10{,}2\,\mathrm{eV}
\end{aligned}
$$

</details>

---

### VP41.4.4

Hàm sóng của electron ở trạng thái cơ bản $1s$ của nguyên tử hydro có dạng:
$$
\psi_{1s}(r) = \frac{1}{\sqrt{\pi a^3}} e^{-r/a}
$$
trong đó $r$ là khoảng cách từ electron đến hạt nhân và $a$ là bán kính Bohr. Hãy tính xác suất để tìm thấy electron trong các miền không gian sau:
(a) $0 \le r \le 2a$.
(b) $a \le r \le 3a$.
(c) $r \ge 4a$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Trạng thái $1s$ hydro có hàm sóng đối xứng cầu:
$$
\psi_{1s}(r) = \frac{1}{\sqrt{\pi a^3}} e^{-r/a}
$$
- Cần tính xác suất $P$ trong các khoảng bán kính: (a) $[0, 2a]$; (b) $[a, 3a]$; (c) $[4a, \infty)$.

**Hướng đi:**
- Phần tử thể tích vi phân trong tọa độ cầu đối với hàm đối xứng cầu là $\mathrm{d}V = 4\pi r^2\,\mathrm{d}r$.
- Hàm phân bố xác suất xuyên tâm là:
$$
\begin{aligned}
&P(r) = 4\pi r^2 |\psi_{1s}(r)|^2, \\
&P(r) = \frac{4r^2}{a^3}e^{-2r/a}.
\end{aligned}
$$
- Đặt biến không thứ nguyên $u = \frac{2r}{a}$, hàm phân bố tích lũy $F(r) = \int_0^r P(r')\,\mathrm{d}r'$ là:
$$
\begin{aligned}
&u = \frac{2r}{a}, \\
&F(r) = 1 - e^{-u} Q(u), \\
&Q(u) = 1 + u + \frac{u^2}{2}.
\end{aligned}
$$

**Lời giải chi tiết:**

Công thức xác suất tích lũy khi tích phân từ $0$ đến bán kính $r_0$:
$$
\begin{aligned}
&F(r_0) = 1 - e^{-u_0} Q(u_0), \\
&Q(u_0) = 1 + u_0 + \frac{u_0^2}{2}.
\end{aligned}
$$

(a) Xác suất trong miền $0 \le r \le 2a$:
Với $r = 2a$, ta có $u_0 = 4$:
$$
\begin{aligned}
P(r \le 2a) &= 1 - 13e^{-4} \\
&\approx 1 - 0{,}2381 \\
&= 0{,}762
\end{aligned}
$$

(b) Xác suất trong miền $a \le r \le 3a$:
Tính giá trị tại hai cận $r = a$ ($u = 2$) và $r = 3a$ ($u = 6$):
- Tại $r = a$:
$$
\begin{aligned}
F(a) &= 1 - 5e^{-2} \\
&\approx 0{,}3233
\end{aligned}
$$
- Tại $r = 3a$:
$$
\begin{aligned}
F(3a) &= 1 - 25e^{-6} \\
&\approx 0{,}9380
\end{aligned}
$$

Xác suất trong miền giữa hai bán kính là:
$$
\begin{aligned}
P &= F(3a) - F(a) \\
&= 5e^{-2} - 25e^{-6} \\
&\approx 0{,}615
\end{aligned}
$$

(c) Xác suất trong miền $r \ge 4a$:
Với $r = 4a$, ta có $u = 8$:
$$
\begin{aligned}
P(r \ge 4a) &= 1 - F(4a) \\
&= 41e^{-8} \\
&\approx 0{,}0138
\end{aligned}
$$

![Hình minh họa: Phân bố xác suất xuyên tâm của trạng thái 1s.](./img/young-41/loi-giai-c-03.svg)

</details>

---

### VP41.8.1

Một electron cô lập được đặt trong từ trường đều $\vec{B} = (3{,}14\,\mathrm{T})\hat{k}$.
(a) Tính độ chênh lệch năng lượng giữa hai trạng thái spin $S_z = +\frac{1}{2}\hbar$ và $S_z = -\frac{1}{2}\hbar$ của electron theo đơn vị electron-volt ($\mathrm{eV}$).
(b) Trạng thái spin nào có mức năng lượng cao hơn?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Electron cô lập trong từ trường $B_z = 3{,}14\,\mathrm{T}$.
- Cần tìm: (a) Độ tách mức năng lượng $\Delta U$; (b) Xác định trạng thái có năng lượng cao hơn.

**Hướng đi:**
- Mômen từ spin của electron liên hệ với vector spin bởi hệ thức:
$$
\vec{\mu}_s = -g_s \mu_B \frac{\vec{S}}{\hbar}
$$
trong đó thừa số Landé $g_s \approx 2{,}00232 \approx 2{,}00$.
- Thế năng tương tác từ là:
$$
\begin{aligned}
&U = -\vec{\mu}_s \cdot \vec{B}, \\
&U = g_s \mu_B B_z m_s.
\end{aligned}
$$
- Với $m_s = +1/2$, mômen từ ngược hướng từ trường làm thế năng dương (cao hơn). Với $m_s = -1/2$, mômen từ cùng hướng từ trường làm thế năng âm (thấp hơn).

**Lời giải chi tiết:**

(a) Tính độ chênh lệch năng lượng $\Delta U$:
Thế năng tương tác từ của hai trạng thái spin:
$$
U(m_s) = g_s \mu_B B m_s
$$

Hiệu năng lượng giữa hai mức $m_s = +1/2$ và $m_s = -1/2$:
$$
\begin{aligned}
\Delta U &= U(+1/2) - U(-1/2) \\
&= g_s \mu_B B
\end{aligned}
$$

Thay các giá trị số với $g_s \approx 2{,}00232$, $B = 3{,}14\,\mathrm{T}$ và $\mu_B \approx 5{,}788 \times 10^{-5}\,\mathrm{eV/T}$:
$$
\begin{aligned}
\mu_B B &\approx 1{,}817 \times 10^{-4}\,\mathrm{eV}, \\
\Delta U &= g_s (\mu_B B) \\
&\approx 3{,}64 \times 10^{-4}\,\mathrm{eV}
\end{aligned}
$$

(b) Xác định trạng thái có năng lượng cao hơn:
Do electron mang điện tích âm, vector mômen từ spin $\vec{\mu}_s$ hướng ngược chiều với vector mômen động lượng spin $\vec{S}$.
Khi $S_z = +\frac{1}{2}\hbar$ ("spin hướng lên"), hình chiếu mômen từ là $\mu_{sz} < 0$ (ngược hướng từ trường $\vec{B}$). Tương tác đẩy này dẫn đến thế năng $U = -\vec{\mu}_s \cdot \vec{B} > 0$.
Do đó, trạng thái $S_z = +\frac{1}{2}\hbar$ có mức năng lượng cao hơn trạng thái $S_z = -\frac{1}{2}\hbar$.

</details>

---

### VP41.8.2

Electron ngoài cùng của nguyên tử kali ($\mathrm{K}$) ở trạng thái có số lượng tử quỹ đạo $l = 0$. Đặt nguyên tử kali vào trong từ trường đều có độ lớn $2{,}36\,\mathrm{T}$ và chiếu chùm bức xạ điện từ đơn sắc vào hệ. Bức xạ này cần có tần số và bước sóng bằng bao nhiêu để gây ra hiện tượng cộng hưởng chuyển mức giữa hai trạng thái spin-up và spin-down của electron ngoài cùng?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Nguyên tử kali có electron ngoài cùng ở phân lớp $4s$ ($l = 0$).
- Từ trường ngoài: $B = 2{,}36\,\mathrm{T}$.
- Cần tìm: Tần số $f$ và bước sóng $\lambda$ của bức xạ điện từ gây đảo spin electron.

**Hướng đi:**
- Vì electron ở trạng thái $l = 0$, mômen từ quỹ đạo triệt tiêu $\vec{\mu}_l = \vec{0}$, do đó hiện tượng tách mức hoàn toàn do mômen từ spin tạo nên (hiệu ứng cộng hưởng thuận từ electron, EPR).
- Độ chênh lệch năng lượng giữa hai trạng thái spin là $\Delta E = g_s \mu_B B$.
- Điều kiện hấp thụ cộng hưởng photon:
$$
f = \frac{\Delta E}{h} = \frac{g_s \mu_B B}{h}
$$
và bước sóng tương ứng là $\lambda = \frac{c}{f}$.

**Lời giải chi tiết:**

Tính hiệu năng lượng giữa hai trạng thái spin:
$$
\Delta E = g_s \mu_B B
$$

Tần số của photon kích thích:
$$
\begin{aligned}
\Delta E &= g_s \mu_B B \\
&\approx 4{,}38 \times 10^{-23}\,\mathrm{J}, \\
f &= \frac{\Delta E}{h} \\
&\approx 6{,}61 \times 10^{10}\,\mathrm{Hz} \\
&= 66{,}1\,\mathrm{GHz}
\end{aligned}
$$

Bước sóng của bức xạ điện từ tương ứng:
$$
\begin{aligned}
\lambda &= \frac{c}{f} \\
&= \frac{3{,}00 \times 10^8\,\mathrm{m/s}}{6{,}614 \times 10^{10}\,\mathrm{Hz}} \\
&\approx 4{,}53 \times 10^{-3}\,\mathrm{m} \\
&= 4{,}53\,\mathrm{mm}
\end{aligned}
$$

Bức xạ này thuộc dải sóng vi ba (microwave).

</details>

---

### VP41.8.3

Khi electron ngoài cùng của nguyên tử kali chuyển mức từ mức $4p$ về mức $4s$, bước sóng của photon phát ra có thể nhận một trong hai giá trị là $766{,}490\,\mathrm{nm}$ hoặc $769{,}896\,\mathrm{nm}$ tùy thuộc vào định hướng spin ban đầu của electron. Hãy xác định:
(a) Độ chênh lệch năng lượng giữa hai mức năng lượng thành phần của phân lớp $4p$.
(b) Độ lớn của từ trường hiệu dụng mà electron cảm nhận được ở phân lớp $4p$ do tương tác spin-quỹ đạo.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Bước chuyển $4p \to 4s$ trong kali phát ra vạch đôi có bước sóng $\lambda_1 = 766{,}490\,\mathrm{nm}$ và $\lambda_2 = 769{,}896\,\mathrm{nm}$.
- Cần tìm: (a) Độ tách mức $\Delta E$ của trạng thái $4p$; (b) Từ trường hiệu dụng $B_{\text{eff}}$.

**Hướng đi:**
- Mức $4s$ có $l = 0$ nên không bị tách bởi tương tác spin-quỹ đạo ($j = 1/2$).
- Mức $4p$ có $l = 1$, tách thành hai mức cấu trúc tinh tế $4p_{3/2}$ ($j = 3/2$) và $4p_{1/2}$ ($j = 1/2$).
- Hiệu năng lượng của hai photon phát ra bằng chính độ tách năng lượng $\Delta E$ giữa hai mức $4p$:
$$
\Delta E = hc\left(\frac{1}{\lambda_1} - \frac{1}{\lambda_2}\right)
$$
- Tương tác spin-quỹ đạo có thể xem như tương tác của mômen từ spin electron $\vec{\mu}_s$ với từ trường nội tại hiệu dụng $\vec{B}_{\text{eff}}$, dẫn đến độ tách năng lượng giữa spin song song và phản song song là $\Delta E = 2\mu_B B_{\text{eff}}$.

**Lời giải chi tiết:**

(a) Tính độ chênh lệch năng lượng giữa hai mức $4p$:
Năng lượng của hai photon phát ra:
$$
E_1 = \frac{hc}{\lambda_1}, \quad E_2 = \frac{hc}{\lambda_2}
$$

Sử dụng giá trị tích hằng số $hc \approx 1239{,}84\,\mathrm{eV\cdot nm}$:
$$
\begin{aligned}
&E_1 = \frac{hc}{\lambda_1} \approx 1{,}61756\,\mathrm{eV}, \\
&E_2 = \frac{hc}{\lambda_2} \approx 1{,}61040\,\mathrm{eV}.
\end{aligned}
$$

Độ chênh lệch năng lượng giữa hai mức $4p$ là:
$$
\begin{aligned}
\Delta E &= E_1 - E_2 \\
&\approx 7{,}16 \times 10^{-3}\,\mathrm{eV}
\end{aligned}
$$

(b) Tính từ trường nội tại hiệu dụng $B_{\text{eff}}$:
Độ tách mức năng lượng do mômen từ spin đảo hướng trong từ trường hiệu dụng:
$$
B_{\text{eff}} = \frac{\Delta E}{2\mu_B}
$$

Đổi độ chênh lệch năng lượng sang đơn vị joule với $e \approx 1{,}602 \times 10^{-19}\,\mathrm{C}$:
$$
\begin{aligned}
\Delta E &\approx (7{,}156 \times 10^{-3}) \times e \\
&\approx 1{,}146 \times 10^{-21}\,\mathrm{J}
\end{aligned}
$$

Thay giá trị Bohr magneton $\mu_B \approx 9{,}274 \times 10^{-24}\,\mathrm{J/T}$:
$$
\begin{aligned}
B_{\text{eff}} &= \frac{1{,}146 \times 10^{-21}}{2 \times (9{,}274 \times 10^{-24})} \\
&\approx 61{,}8\,\mathrm{T}
\end{aligned}
$$

Từ trường nội tại do chuyển động tương đối của hạt nhân xung quanh electron có độ lớn lớn, lên đến gần $62\,\mathrm{T}$.

![Hình minh họa: Sơ đồ mức cấu trúc tinh tế của phân lớp 4p nguyên tử kali.](./img/young-41/loi-giai-c-04.svg)

</details>

---

### VP41.8.4

(a) Biểu diễn theo hằng số cấu trúc tinh tế $\alpha$ năng lượng của trạng thái electron trong nguyên tử hydro có $n = 3, l = 1, j = 3/2$ và năng lượng của trạng thái có $n = 3, l = 1, j = 1/2$.
(b) Tính độ chênh lệch giữa hai mức năng lượng trên theo đơn vị electron-volt ($\mathrm{eV}$). Trạng thái nào có mức năng lượng cao hơn?
(c) Tính độ chênh lệch bước sóng của hai photon phát ra khi electron chuyển mức từ mỗi trạng thái ở câu (a) về trạng thái $n = 2, l = 0, j = 1/2$. Trạng thái ban đầu nào cho photon có bước sóng dài hơn?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Mức $n = 3, l = 1$ tách thành hai mức $j = 3/2$ và $j = 1/2$ do cấu trúc tinh tế.
- Cần tìm: (a) Biểu thức $E$ theo $\alpha$; (b) Độ tách mức $\Delta E$ và so sánh; (c) Chênh lệch bước sóng $\Delta\lambda$ khi chuyển về $n = 2, l = 0, j = 1/2$.

**Hướng đi:**
- Công thức hiệu chỉnh cấu trúc tinh tế đối với nguyên tử hydro:
$$
\begin{aligned}
&f(n, j) = \frac{n}{j + 1/2} - \frac{3}{4}, \\
&E_{n,j} = E_n \left[ 1 + \frac{\alpha^2}{n^2} f(n, j) \right]
\end{aligned}
$$
trong đó:
$$
E_n = -\frac{13{,}606\,\mathrm{eV}}{n^2}
$$
- Với $n = 3$, mức năng lượng chưa hiệu chỉnh là:
$$
\begin{aligned}
E_3 &= -\frac{13{,}606\,\mathrm{eV}}{9} \\
&\approx -1{,}511\,\mathrm{eV}
\end{aligned}
$$
- Lưu ý rằng $E_3 < 0$, do đó số hạng trong ngoặc vuông càng lớn thì năng lượng $E_{n,j}$ càng âm (nghĩa là mức năng lượng càng thấp). Mức có $j$ lớn hơn sẽ có năng lượng cao hơn (ít âm hơn).
- Độ chênh lệch bước sóng liên hệ qua vi phân:
$$
\Delta\lambda \approx \frac{hc}{(\Delta E_{\text{chuyển}})^2}\Delta E
$$

**Lời giải chi tiết:**

(a) Biểu thức năng lượng theo $\alpha$:
- Với trạng thái $n = 3, j = 3/2$: Thừa số trong ngoặc:
$$
\begin{aligned}
\frac{n}{j + 1/2} - \frac{3}{4} &= \frac{3}{2} - \frac{3}{4} \\
&= \frac{3}{4}
\end{aligned}
$$
Thừa số hiệu chỉnh là:
$$
\frac{\alpha^2}{3^2} \cdot \frac{3}{4} = \frac{\alpha^2}{12}
$$
Do đó:
$$
E_{3,\, 3/2} = E_3\left(1 + \frac{\alpha^2}{12}\right)
$$

- Với trạng thái $n = 3, j = 1/2$: Thừa số trong ngoặc:
$$
\begin{aligned}
\frac{n}{j + 1/2} - \frac{3}{4} &= 3 - \frac{3}{4} \\
&= \frac{9}{4}
\end{aligned}
$$
Thừa số hiệu chỉnh là:
$$
\frac{\alpha^2}{3^2} \cdot \frac{9}{4} = \frac{\alpha^2}{4}
$$
Do đó:
$$
E_{3,\, 1/2} = E_3\left(1 + \frac{\alpha^2}{4}\right)
$$

(b) Tính độ chênh lệch năng lượng $\Delta E$:
$$
\begin{aligned}
\Delta E &= E_{3,\, 3/2} - E_{3,\, 1/2} \\
&= |E_3|\left(\frac{\alpha^2}{4} - \frac{\alpha^2}{12}\right) \\
&= |E_3| \cdot \frac{\alpha^2}{6}
\end{aligned}
$$

Thay giá trị $\alpha \approx \frac{1}{137{,}04}$ và $|E_3| \approx 1{,}511\,\mathrm{eV}$:
$$
\begin{aligned}
\Delta E &= 1{,}511\,\mathrm{eV} \times \frac{\alpha^2}{6} \\
&\approx 1{,}34 \times 10^{-5}\,\mathrm{eV}
\end{aligned}
$$

Vì số hạng hiệu chỉnh âm ít hơn, trạng thái $j = 3/2$ có mức năng lượng cao hơn trạng thái $j = 1/2$.

(c) Tính chênh lệch bước sóng $\Delta\lambda$:
Năng lượng của mức cuối $n = 2, l = 0, j = 1/2$ có giá trị xấp xỉ:
$$
\begin{aligned}
E_2 &\approx -\frac{13{,}606\,\mathrm{eV}}{4} \\
&\approx -3{,}401\,\mathrm{eV}
\end{aligned}
$$

Năng lượng chuyển mức cơ sở là:
$$
\begin{aligned}
\Delta E_{\text{chuyển}} &= E_3 - E_2 \\
&\approx 1{,}890\,\mathrm{eV}
\end{aligned}
$$

Chênh lệch bước sóng giữa hai vạch quang phổ phát ra:
$$
\begin{aligned}
\Delta\lambda &\approx \frac{hc}{\Delta E_{\text{chuyển}}^2} \Delta E \\
&\approx 4{,}66 \times 10^{-3}\,\mathrm{nm}
\end{aligned}
$$

Trạng thái ban đầu $j = 1/2$ có mức năng lượng thấp hơn, do đó năng lượng phát xạ photon nhỏ hơn và cho bước sóng dài hơn.

![Hình minh họa: Cấu trúc tinh tế của các mức hydro và các chuyển mức phát xạ.](./img/young-41/loi-giai-c-05.svg)

</details>
