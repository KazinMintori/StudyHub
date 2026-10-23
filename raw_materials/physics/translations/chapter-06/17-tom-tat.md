## Tổng kết

---

### 1. Công của một lực (Work done by a force)

Khi một lực không đổi $\vec F$ tác dụng lên một chất điểm có độ dời thẳng $\vec s$, công do lực thực hiện lên chất điểm được định nghĩa là tích vô hướng của vector lực và vector độ dời:
$$
\begin{aligned}
W &= \vec F \cdot \vec s \\
&= Fs \cos\phi
\end{aligned}
$$

Trong đó:
- $F$: Là độ lớn của lực tác dụng.
- $s$: Là độ lớn của độ dời.
- $\phi$: Là góc hợp bởi vector lực $\vec F$ và vector độ dời $\vec s$.

![Tóm tắt 6.1: Công của một lực](/vat-ly-1/bai-giang/img/young-06/r-theory-summary-01.png)

Công là một đại lượng vô hướng. Công có thể dương ($\phi < 90^\circ$), âm ($\phi > 90^\circ$) hoặc bằng không ($\phi = 90^\circ$).

Đơn vị đo của công trong hệ SI là **joule** (ký hiệu: $\mathrm{J}$):
$$
1\,\mathrm{J} = 1\,\mathrm{N \cdot m} = 1\,\mathrm{kg \cdot m^2/s^2}
$$

---

### 2. Động năng (Kinetic energy)

Động năng $K$ của một chất điểm có khối lượng $m$ chuyển động với tốc độ $v$ được định nghĩa là:
$$
K = \frac{1}{2}mv^2
$$

![Tóm tắt 6.2: Động năng](/vat-ly-1/bai-giang/img/young-06/r-theory-summary-02.png)

Động năng bằng lượng công cần thiết để gia tốc chất điểm từ trạng thái nghỉ đến tốc độ $v$. Nó cũng bằng đúng lượng công mà chất điểm có thể thực hiện lên môi trường trước khi dừng lại hoàn toàn.

Đặc điểm của động năng:
- Động năng là một đại lượng vô hướng, không có hướng trong không gian.
- Luôn luôn không âm ($K \ge 0$). Động năng bằng không khi và chỉ khi vật đứng yên ($v = 0$).
- Đơn vị của động năng trùng với đơn vị của công: Joule ($\mathrm{J}$).
- Khi nhân đôi khối lượng ($m \to 2m$), động năng tăng gấp đôi.
- Khi nhân đôi tốc độ ($v \to 2v$), động năng tăng gấp bốn lần.

---

### 3. Định lý công–động năng (The work–energy theorem)

Khi các lực tác dụng lên một chất điểm trong suốt quá trình dịch chuyển, động năng của chất điểm biến thiên một lượng đúng bằng tổng công do tất cả các ngoại lực thực hiện lên nó:
$$
W_{\mathrm{tot}} = K_2 - K_1 = \Delta K
$$

Trong đó $W_{\mathrm{tot}}$ là tổng công của mọi lực tác dụng lên chất điểm dọc theo quỹ đạo.

![Tóm tắt 6.3: Định lý công–động năng](/vat-ly-1/bai-giang/img/young-06/r-theory-summary-03.png)

Phạm vi áp dụng của định lý:
- Định lý công–động năng nghiệm đúng cho cả lực không đổi lẫn lực biến đổi theo thời gian hoặc vị trí.
- Nghiệm đúng cho cả chuyển động thẳng và chuyển động dọc theo quỹ đạo cong bất kỳ.
- Chỉ áp dụng trực tiếp cho các vật thể có thể mô hình hóa như một chất điểm đơn lẻ.

---

### 4. Công của lực biến đổi hoặc trên quỹ đạo cong (Work done by a varying force or on a curved path)

#### Chuyển động thẳng với lực biến đổi

Khi lực $F_x$ thay đổi theo vị trí trong chuyển động thẳng dọc theo trục $x$ từ $x_1$ đến $x_2$, công thực hiện được xác định bằng tích phân:
$$
W = \int_{x_1}^{x_2} F_x \, dx
$$

Về mặt hình học, công $W$ bằng đúng diện tích giới hạn dưới đồ thị $F_x$ theo $x$ giữa hai vị trí $x_1$ và $x_2$.

Đối với lò xo lý tưởng tuân theo định luật Hooke ($F_x = kx$), công cần thiết để kéo dãn lò xo từ vị trí tự nhiên $x = 0$ đến độ dãn $X$ là:
$$
W = \frac{1}{2}kX^2
$$

![Tóm tắt 6.4: Công của lực biến đổi hoặc trên quỹ đạo cong](/vat-ly-1/bai-giang/img/young-06/r-theory-summary-04.png)

#### Chuyển động dọc theo quỹ đạo cong

Khi chất điểm chuyển động theo một đường cong từ điểm $P_1$ đến điểm $P_2$, công do lực $\vec F$ thực hiện là tích phân đường dọc theo quỹ đạo:
$$
\begin{aligned}
W &= \int_{P_1}^{P_2} F \cos\phi \, dl \\
&= \int_{P_1}^{P_2} F_{\parallel} \, dl \\
&= \int_{P_1}^{P_2} \vec F \cdot d\vec l
\end{aligned}
$$

Trong đó:
- $d\vec l$: Là vector độ dời vi phân tiếp tuyến với quỹ đạo.
- $\phi$: Là góc hợp bởi vector lực $\vec F$ và vector tiếp tuyến $d\vec l$.
- $F_{\parallel} = F \cos\phi$: Là thành phần lực tiếp tuyến sinh công.

---

### 5. Công suất (Power)

Công suất là đại lượng vật lý đặc trưng cho tốc độ sinh công theo thời gian.

![Tóm tắt 6.5: Công suất](/vat-ly-1/bai-giang/img/young-06/r-theory-summary-05.png)

#### Công suất trung bình và tức thời

- **Công suất trung bình** trong khoảng thời gian $\Delta t$:
$$
P_{\mathrm{av}} = \frac{\Delta W}{\Delta t}
$$

- **Công suất tức thời** tại một thời điểm:
$$
\begin{aligned}
P &= \lim_{\Delta t \to 0} \frac{\Delta W}{\Delta t} \\
&= \frac{dW}{dt}
\end{aligned}
$$

#### Công suất biểu diễn qua lực và vận tốc

Khi lực $\vec F$ tác dụng lên một chất điểm đang chuyển động với vận tốc $\vec v$, công suất tức thời bằng tích vô hướng của lực và vận tốc:
$$
\begin{aligned}
P &= \vec F \cdot \vec v \\
&= F v \cos\phi \\
&= F_{\parallel} v
\end{aligned}
$$

#### Đơn vị đo

- Đơn vị SI của công suất là **watt** (ký hiệu: $\mathrm{W}$):
$$
1\,\mathrm{W} = 1\,\mathrm{J/s}
$$
- Đơn vị **mã lực** (ký hiệu: $\mathrm{hp}$):
$$
1\,\mathrm{hp} = 746\,\mathrm{W} = 0{,}746\,\mathrm{kW}
$$
- Đơn vị đo năng lượng **kilowatt-giờ** (ký hiệu: $\mathrm{kWh}$):
$$
\begin{aligned}
1\,\mathrm{kWh} &= 3{,}6 \times 10^6\,\mathrm{J} \\
&= 3{,}6\,\mathrm{MJ}
\end{aligned}
$$
