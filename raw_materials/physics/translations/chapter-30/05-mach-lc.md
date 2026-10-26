## 30.5. Mạch L-C

Các mạch điện R-C và R-L mà ta đã khảo sát ở các phần trước đều có một đặc điểm chung: Dòng điện, điện tích và hiệu điện thế luôn tiếp cận trạng thái dừng ổn định theo quy luật hàm mũ suy giảm. Trái lại, một mạch điện chỉ chứa một cuộn cảm $L$ và một tụ điện $C$ lại biểu hiện một phương thức hoạt động hoàn toàn mới: Hiện tượng dao động điện từ điều hòa.

Trong **mạch L-C**, điện tích trên các bản tụ điện và cường độ dòng điện qua cuộn cảm biến thiên tuần hoàn theo thời gian. Năng lượng của hệ không bị tiêu tán thành nhiệt (khi bỏ qua điện trở của dây dẫn), mà liên tục chuyển hóa qua lại giữa năng lượng điện trường trong tụ điện và năng lượng từ trường trong cuộn cảm.

---

### Cơ chế dao động trong mạch L-C

Để khảo sát trực quan quá trình dao động, ta xét mạch điện ở Hình 30.14. Ban đầu, tụ điện được nạp đến hiệu điện thế $V_m$, tích lũy điện tích cực đại $Q_m = C V_m$ với bản cực bên trái mang điện tích dương và bản cực bên phải mang điện tích âm. Tại thời điểm $t = 0$, ta đóng công tắc nối tụ điện với cuộn cảm.

![Hình 30.14: Sự biến thiên của điện tích trên tụ điện, dòng điện qua cuộn cảm và sự chuyển hóa năng lượng trong một chu kỳ dao động của mạch L-C.](../img/young-30/hinh-30-14.png)

Diễn biến của một chu kỳ dao động hoàn chỉnh diễn ra qua các giai đoạn sau:

1. **Giai đoạn (a), tại $t = 0$**:
   Tụ điện tích điện cực đại $q = Q_m$, dòng điện qua mạch bằng không ($i = 0$). Toàn bộ năng lượng của mạch được tích lũy dưới dạng năng lượng điện trường trong tụ điện:
   $$
   E = U_E = \frac{Q_m^2}{2C}
   $$

2. **Từ giai đoạn (a) sang giai đoạn (b)**:
   Tụ điện bắt đầu phóng điện qua cuộn cảm. Do xuất hiện suất điện động tự cảm chống lại sự tăng của dòng điện, cường độ dòng điện không thể tăng đột ngột mà tăng dần từ không. Dòng điện chạy ngược chiều kim đồng hồ, làm giảm điện tích trên bản cực bên trái của tụ. Điện trường trong tụ giảm dần, đồng thời từ trường trong lòng cuộn cảm mạnh lên.

3. **Giai đoạn (b), tại $t = T/4$**:
   Tụ điện phóng hết điện tích ($q = 0$), hiệu điện thế giữa hai bản tụ bằng không. Cường độ dòng điện qua cuộn cảm đạt giá trị cực đại $I_m$. Toàn bộ năng lượng của hệ lúc này chuyển hóa hoàn toàn thành năng lượng từ trường trong cuộn cảm:
   $$
   E = U_B = \frac{1}{2}L I_m^2
   $$

4. **Từ giai đoạn (b) sang giai đoạn (c)**:
   Mặc dù tụ điện đã phóng hết điện, dòng điện không thể dừng lại ngay lập tức. Suất điện động tự cảm của cuộn cảm có xu hướng duy trì dòng điện, tiếp tục đẩy điện tích dương về phía bản cực bên phải của tụ điện. Tụ điện bắt đầu được nạp điện theo chiều ngược lại, với bản phải mang điện dương và bản trái mang điện âm. Cường độ dòng điện giảm dần về không.

5. **Giai đoạn (c), tại $t = T/2$**:
   Dòng điện giảm về không ($i = 0$), tụ điện được nạp đầy hoàn toàn với cực tính đảo ngược ($q = -Q_m$). Toàn bộ năng lượng lại quay về tích lũy trong điện trường của tụ điện.

6. **Từ giai đoạn (c) sang giai đoạn (d)**:
   Tụ điện lại bắt đầu phóng điện, nhưng lần này dòng điện chạy theo chiều kim đồng hồ. Năng lượng điện trường lại chuyển hóa dần thành năng lượng từ trường trong cuộn cảm.

7. **Giai đoạn (d), tại $t = 3T/4$**:
   Điện tích trên tụ lại bằng không ($q = 0$), dòng điện theo chiều kim đồng hồ đạt giá trị cực đại $I_m$. Toàn bộ năng lượng lại nằm trong từ trường của cuộn cảm.

8. **Trở lại giai đoạn (a), tại $t = T$**:
   Dòng điện tiếp tục nạp lại cho tụ điện với bản trái dương và bản phải âm, đưa hệ trở về trạng thái ban đầu tại thời điểm $t = T$. Chu kỳ dao động mới lại tiếp diễn.

---

### Thiết lập phương trình vi phân dao động

Để mô tả định lượng dòng điện và điện tích, ta áp dụng quy tắc vòng Kirchhoff cho mạch điện ở Hình 30.15.

![Hình 30.15: Quy ước dấu của điện tích q và chiều dòng điện i khi áp dụng quy tắc vòng Kirchhoff cho mạch L-C.](../img/young-30/hinh-30-15.png)

Ta quy ước dấu một cách chặt chẽ:
- Gọi $q$ là điện tích trên bản cực bên trái của tụ điện.
- Chiều dương của dòng điện $i$ được chọn là chiều đi vào bản cực bên trái của tụ. Theo định nghĩa này:
  $$
  i = \frac{dq}{dt}
  $$
  Khi $i > 0$, điện tích $q$ trên bản cực bên trái tăng lên. Ngược lại, khi tụ điện đang phóng điện và bản cực trái mất bớt điện tích dương, dòng điện $i$ mang giá trị âm.

Chọn chiều đi vòng theo chiều kim đồng hồ quanh mạch kín. Đi qua tụ điện từ bản trái sang bản phải làm điện thế giảm một lượng $-v = -q/C$. Đi qua cuộn cảm theo chiều mũi tên làm điện thế biến thiên một lượng $-L(di/dt)$. Tổng độ biến thiên điện thế quanh vòng kín bằng không:

$$
-L\frac{di}{dt} - \frac{q}{C} = 0
$$

Vì $i = dq/dt$, ta có đạo hàm bậc hai $di/dt = d^2q/dt^2$. Thay vào phương trình (30.20) và chia hai vế cho $-L$:

$$
\frac{d^2q}{dt^2} + \frac{1}{LC}q = 0 \tag{30.20}
$$

Phương trình vi phân này có dạng hoàn toàn trùng khớp với phương trình vi phân của dao động điều hòa cơ học ở con lắc lò xo:

$$
\frac{d^2x}{dt^2} + \frac{k}{m}x = 0
$$

Trong đó:
- Li độ $x$ tương ứng với điện tích $q$ trên tụ điện.
- Vận tốc $v_x = dx/dt$ tương ứng với dòng điện $i = dq/dt$.
- Khối lượng $m$ (quán tính cơ học) tương ứng với độ tự cảm $L$ (quán tính điện từ).
- Độ cứng lò xo $k$ tương ứng với nghịch đảo của điện dung, tức $1/C$.

Nghiệm tổng quát của phương trình vi phân là:

$$
q(t) = Q\cos(\omega t + \phi) \tag{30.21}
$$

Trong đó $Q$ là điện tích cực đại trên tụ điện, $\phi$ là pha ban đầu, và tần số góc riêng của mạch dao động là:

$$
\omega = \sqrt{\frac{1}{LC}} \tag{30.22}
$$

**Kiểm tra nghiệm:** Hãy lấy hai đạo hàm của (30.21) để xác nhận nghiệm điện tích thỏa phương trình (30.20) khi tần số góc có giá trị (30.22).

<details><summary>Xem phép kiểm tra</summary>

$$
\begin{aligned}
q'' &= -\omega^2q, \\
q''+\frac q{LC} &= -\omega^2q+\frac q{LC} \\
&= 0.
\end{aligned}
$$

</details>

Tần số dao động $f$ và chu kỳ dao động $T$ được xác định bởi:

$$
f = \frac{\omega}{2\pi} = \frac{1}{2\pi\sqrt{LC}}
$$

$$
T = \frac{1}{f} = \frac{2\pi}{\omega} = 2\pi\sqrt{LC}
$$

Cường độ dòng điện tức thời trong mạch là đạo hàm theo thời gian của điện tích:

$$
\begin{aligned}
i(t) &= \frac{dq}{dt} \\
&= -\omega Q\sin(\omega t + \phi)
\end{aligned} \tag{30.23}
$$

Biên độ cực đại của dòng điện là $I_m = \omega Q$. So sánh phương trình (30.21) và (30.23), ta thấy dòng điện $i(t)$ lệch pha $\pi/2$ so với điện tích $q(t)$. Khi điện tích đạt cực đại thì dòng điện bằng không, và khi điện tích bằng không thì dòng điện đạt độ lớn cực đại.

Nếu tại thời điểm ban đầu $t = 0$, bản cực bên trái của tụ điện có điện tích cực đại $q = Q$ và dòng điện trong mạch bằng không ($i = 0$), ta suy ra pha ban đầu $\phi = 0$.

Nếu điện tích bằng không tại $t=0$ thì có thể chọn $\phi=\pm\pi/2$. Dấu cụ thể được quyết định bởi chiều dòng ban đầu.

---

### Sự tương tự cơ học và bảo toàn năng lượng

Trong cơ học, vận tốc của một vật dao động điều hòa liên hệ với li độ theo biểu thức:

$$
v_x = \pm\sqrt{\frac{k}{m}}\sqrt{A^2 - x^2} \tag{30.24}
$$

Đối với mạch L-C, vì không có điện trở làm tiêu hao năng lượng, tổng năng lượng điện trường và từ trường là một đại lượng bảo toàn:

$$
\begin{aligned}
E &= U_B + U_E \\
&= \frac{1}{2}Li^2 + \frac{q^2}{2C} \\
&= \frac{Q^2}{2C}
\end{aligned} \tag{30.25}
$$

Từ phương trình bảo toàn năng lượng (30.25), ta rút ra biểu thức xác định cường độ dòng điện $i$ theo điện tích tức thời $q$:

$$
i = \pm\sqrt{\frac{1}{LC}}\sqrt{Q^2 - q^2} \tag{30.26}
$$

Biểu thức (30.26) hoàn toàn tương ứng với hệ thức cơ học (30.24). Khi thay $q = Q\cos(\omega t + \phi)$ và $i = -\omega Q\sin(\omega t + \phi)$ vào (30.25), ta thấy tổng năng lượng luôn bằng $Q^2/(2C)$ tại mọi thời điểm nhờ hệ thức lượng giác $\sin^2\alpha + \cos^2\alpha = 1$.

**Kiểm tra quan hệ dòng, điện tích:** Hãy thế nghiệm $q(t),i(t)$ vào (30.26). Bình phương hai vế cho cùng giá trị nhờ $1-\cos^2\theta=\sin^2\theta$. Dấu của dòng sau khi lấy căn phải phù hợp dấu đạo hàm điện tích ở thời điểm xét.

![Hình: Bảng 30.1 đối chiếu chi tiết sự tương tự giữa các đại lượng cơ học của hệ con lắc lò xo và các đại lượng điện từ trong mạch dao động L-C.](../img/young-30/bang-30-01.png)

Dưới đây là bảng tổng hợp các đại lượng tương tự giữa dao động cơ và dao động điện:

| Hệ con lắc lò xo (Cơ học) | Mạch dao động L-C (Điện từ) |
| :--- | :--- |
| Li độ $x$ | Điện tích $q$ trên tụ điện |
| Vận tốc $v_x = dx/dt$ | Dòng điện $i = dq/dt$ |
| Khối lượng $m$ (đo mức quán tính) | Độ tự cảm $L$ (quán tính từ tính) |
| Độ cứng lò xo $k$ | Nghịch đảo điện dung $1/C$ |
| Động năng: $K = \frac{1}{2}m v_x^2$ | Năng lượng từ trường: $U_B = \frac{1}{2}L i^2$ |
| Thế năng đàn hồi: $U = \frac{1}{2}k x^2$ | Năng lượng điện trường: $U_E = \frac{q^2}{2C}$ |
| Cơ năng được bảo toàn | Năng lượng điện từ được bảo toàn |
| Tần số góc: $\omega = \sqrt{k/m}$ | Tần số góc: $\omega = \sqrt{1/(LC)}$ |
| Li độ $x(t)$ | Điện tích $q(t)$ |

Các biểu thức bảo toàn cơ năng và nghiệm li độ được viết riêng để đọc rõ từng số hạng:

$$
\begin{aligned}
E_m &= \frac12mv_x^2+\frac12kx^2 \\
&= \frac12kA^2, \\
x(t) &= A\cos(\omega t+\phi).
\end{aligned}
$$

Đối với mạch LC, biểu thức năng lượng ở (30.25) và nghiệm điện tích ở (30.21) đóng vai trò tương ứng.

Bảng 30.1 nêu rõ mối tương quan trực diện giữa hai hệ thống vật lý:
- Li độ $x$ của vật nặng tương ứng với điện tích tức thời $q$ trên bản tụ điện, và vận tốc tức thời $v_x = dx/dt$ tương ứng với dòng điện tức thời $i = dq/dt$.
- Khối lượng $m$ đại diện cho mức quán tính cơ học chống lại sự thay đổi vận tốc, tương ứng với độ tự cảm $L$ là quán tính từ tính chống lại sự thay đổi đột ngột của dòng điện.
- Hằng số đàn hồi của lò xo $k$ tỉ lệ thuận với lực hồi phục kéo vật về vị trí cân bằng, tương ứng với nghịch đảo điện dung $1/C$ quyết định hiệu điện thế đưa điện tích trở về trạng thái trung hòa.
- Động năng cơ học $K = \frac{1}{2}m v_x^2$ chuyển đổi qua lại với thế năng đàn hồi $U = \frac{1}{2}k x^2$, hoàn toàn tương đồng với năng lượng từ trường trong cuộn cảm $U_B = \frac{1}{2}L i^2$ chuyển hóa liên tục với năng lượng điện trường trong tụ điện $U_E = \frac{q^2}{2C}$.
- Quan hệ vận tốc–li độ ở (30.24) tương ứng với quan hệ dòng–điện tích ở (30.26). Cả hai được suy từ bảo toàn năng lượng của hệ không hao phí.

Sự tương đồng sâu sắc này là cơ sở nguyên lý của các máy tính tương tự (analog computer), cho phép giải các bài toán dao động cơ học phức tạp bằng cách thiết lập các mạch điện tương đương và đo đạc các dòng điện, điện thế tương ứng.

Sự tương tự còn mở rộng sang dao động tắt dần ở mục tiếp theo và dao động điện cưỡng bức trong mạch xoay chiều ở chương 31.

---

### Các ví dụ minh họa và câu hỏi tự kiểm

::: example Ví dụ 30.8: Khảo sát mạch dao động L-C
Một nguồn điện một chiều có hiệu điện thế $300\text{ V}$ được dùng để nạp điện cho một tụ điện có điện dung $C = 25\ \mu\text{F}$. Sau khi tụ được nạp đầy, ta ngắt tụ khỏi nguồn rồi nối hai đầu tụ với một cuộn cảm có độ tự cảm $L = 10\text{ mH}$. Điện trở của mạch là không đáng kể.
1. Tìm tần số và chu kỳ dao động của mạch.
2. Tìm điện tích trên tụ điện và cường độ dòng điện trong mạch tại thời điểm $t = 1{,}2\text{ ms}$ sau khi nối tụ với cuộn cảm.

**Nhận dạng và chuẩn bị:**
Mạch điện không có điện trở nên dao động là dao động điều hòa thuần túy. Ta tính tần số góc $\omega$ từ phương trình (30.22), từ đó suy ra tần số $f$ và chu kỳ $T$. Điện tích ban đầu cực đại của tụ là $Q = C V$. Vì tại $t = 0$ dòng điện bằng không và tụ có điện tích cực đại, pha ban đầu $\phi = 0$. Sau đó áp dụng phương trình (30.21) và (30.23) để tính $q$ và $i$ tại $t = 1{,}2\text{ ms}$.

**Lời giải:**
1. Tần số góc dao động của mạch là:
   $$
   \begin{aligned}
   \omega &= \frac{1}{\sqrt{LC}} \\
   &= \frac{1}{\sqrt{(10\text{ mH})(25\ \mu\text{F})}} \\
   &= \frac{1}{\sqrt{2{,}5 \times 10^{-7}\text{ s}^2}} \\
   &= 2{,}0 \times 10^3\text{ rad/s}
   \end{aligned}
   $$
   Tần số dao động của mạch là:
   $$
   \begin{aligned}
   f &= \frac{\omega}{2\pi} \\
   &= \frac{2{,}0 \times 10^3\text{ rad/s}}{2\pi} \\
   &\approx 318\text{ Hz} \approx 320\text{ Hz}
   \end{aligned}
   $$
   Chu kỳ dao động là:
   $$
   \begin{aligned}
   T &= \frac{1}{f} \\
   &= \frac{1}{318\text{ Hz}} \\
   &\approx 3{,}14 \times 10^{-3}\text{ s} = 3{,}1\text{ ms}
   \end{aligned}
   $$

2. Điện tích cực đại ban đầu của tụ điện:
   $$
   \begin{aligned}
   Q &= C V \\
   &= (25\ \mu\text{F})(300\text{ V}) \\
   &= 7{,}5\text{ mC}
   \end{aligned}
   $$
   Phương trình điện tích và dòng điện theo thời gian:
   $$
   \begin{aligned}
   q(t) &= Q\cos(\omega t) \\
   &= (7{,}5\text{ mC})\cos(\omega t)
   \end{aligned}
   $$
   $$
   \begin{aligned}
   I_m &= \omega Q \\
   &= (2000\text{ rad/s})(7{,}5\text{ mC}) \\
   &= 15\text{ A}
   \end{aligned}
   $$
   $$
   i(t) = -(15\text{ A})\sin(\omega t)
   $$
   Tại thời điểm $t = 1{,}2\text{ ms} = 1{,}2 \times 10^{-3}\text{ s}$, góc pha là:
   $$
   \begin{aligned}
   \omega t &= (2000\text{ rad/s})(1{,}2\text{ ms}) \\
   &= 2{,}4\text{ rad}
   \end{aligned}
   $$
   Tính các giá trị lượng giác tương ứng: Ta có $\cos(2{,}4\text{ rad}) \approx -0{,}7374$ và $\sin(2{,}4\text{ rad}) \approx 0{,}6755$.
   Thay vào phương trình ta được:
   $$
   \begin{aligned}
   q &= (7{,}5\text{ mC})(-0{,}7374) \\
   &\approx -5{,}5\text{ mC}
   \end{aligned}
   $$
   $$
   \begin{aligned}
   i &= -(15\text{ A})(0{,}6755) \\
   &\approx -10{,}1\text{ A} \approx -10\text{ A}
   \end{aligned}
   $$

**Đánh giá:**
Vì chu kỳ dao động là $T = 3{,}1\text{ ms}$, thời điểm $t = 1{,}2\text{ ms}$ tương ứng với $t \approx 0{,}38T$. Thời điểm này nằm giữa $T/4 = 0{,}25T$ (giai đoạn b) và $T/2 = 0{,}50T$ (giai đoạn c). Ở vị trí này, bản tụ bên trái mang điện tích âm đang tiếp tục nạp, và dòng điện ngược chiều kim đồng hồ đang giảm dần về không. Dấu âm của cả $q$ và $i$ hoàn toàn phù hợp với dự đoán hình học từ sơ đồ dao động.
:::

---

::: example Ví dụ 30.9: Phân bố năng lượng trong mạch L-C
Đối với mạch dao động L-C ở Ví dụ 30.8, hãy tính năng lượng từ trường và năng lượng điện trường tại hai thời điểm:
1. Tại thời điểm ban đầu $t = 0$.
2. Tại thời điểm $t = 1{,}2\text{ ms}$.

**Nhận dạng và chuẩn bị:**
Năng lượng từ trường tích trữ trong cuộn cảm là $U_B = \frac{1}{2}Li^2$, và năng lượng điện trường tích trữ trong tụ điện là $U_E = q^2/(2C)$. Sử dụng các giá trị điện tích và dòng điện đã tìm được ở Ví dụ 30.8 để tính toán và kiểm tra định luật bảo toàn năng lượng.

**Lời giải:**
1. Tại thời điểm $t = 0$, dòng điện $i = 0$ và điện tích $q = Q = 7{,}5 \times 10^{-3}\text{ C}$:
   $$
   U_B = \frac{1}{2}L i^2 = 0
   $$
   $$
   \begin{aligned}
   U_E &= \frac{Q^2}{2C} \\
   &= \frac{(7{,}5\text{ mC})^2}{2(25\ \mu\text{F})} \\
   &= \frac{56{,}25 \times 10^{-6}\,\mathrm{C^2}}{50 \times 10^{-6}\,\mathrm F} \\
   &= 1{,}125\text{ J} \approx 1{,}1\text{ J}
   \end{aligned}
   $$
   Tổng năng lượng của mạch tại $t = 0$ là $E = U_B + U_E = 1{,}125\text{ J} \approx 1{,}1\text{ J}$.

2. Tại thời điểm $t = 1{,}2\text{ ms}$, ta có $i = -10{,}13\text{ A}$ và $q = -5{,}53 \times 10^{-3}\text{ C}$:
   $$
   \begin{aligned}
   U_B &= \frac{1}{2}L i^2 \\
   &= \frac{1}{2}(10\text{ mH})(-10{,}13\text{ A})^2 \\
   &\approx 0{,}513\text{ J}
   \end{aligned}
   $$
   $$
   \begin{aligned}
   U_E &= \frac{q^2}{2C} \\
   &= \frac{(-5{,}53\text{ mC})^2}{2(25\ \mu\text{F})} \\
   &= \frac{30{,}58 \times 10^{-6}\,\mathrm{C^2}}{50 \times 10^{-6}\,\mathrm F} \\
   &\approx 0{,}612\text{ J} \approx 0{,}6\text{ J}
   \end{aligned}
   $$
   Tổng năng lượng tại thời điểm này là:
   $$
   \begin{aligned}
   E &= U_B + U_E \\
   &= 0{,}513\text{ J} + 0{,}612\text{ J} \\
   &= 1{,}125\text{ J} \approx 1{,}1\text{ J}
   \end{aligned}
   $$

**Đánh giá:**
Năng lượng điện và năng lượng từ bằng nhau tại thời điểm $t = 3T/8 = 0{,}375T$. Vì thời điểm $t = 1{,}2\text{ ms} \approx 0{,}38T$ hơi muộn hơn $0{,}375T$ một chút, năng lượng từ trường $U_B$ hơi nhỏ hơn năng lượng điện trường $U_E$. Ở mọi thời điểm, tổng năng lượng $U_B + U_E$ luôn không đổi và bằng $1{,}125\text{ J}$, đúng như định luật bảo toàn năng lượng yêu cầu.
:::

---

::: exercise Câu hỏi tự kiểm 30.5
Một cách tiếp cận trực quan để hiểu về năng lượng tích trữ trong mạch L-C là xem xét công do các phần tử mạch thực hiện lên các điện tích chuyển động qua lại:
1. Trong quá trình chuyển biến từ giai đoạn (a) sang giai đoạn (b) ở Hình 30.14, tụ điện sinh công dương hay công âm lên các điện tích chuyển động?
2. Lực mà tụ điện tác dụng lên các điện tích để thực hiện công này thuộc loại lực nào (lực điện hay lực từ)?
3. Cũng trong quá trình đó, cuộn cảm sinh công dương hay công âm lên các điện tích chuyển động?
4. Lực mà cuộn cảm tác dụng lên các điện tích thuộc loại lực nào (lực điện hay lực từ)?

<details>
<summary>Đáp án và giải thích</summary>

**Đáp án:**
1. Tụ điện sinh công dương.
2. Lực điện.
3. Cuộn cảm sinh công âm.
4. Lực điện.

**Giải thích chi tiết:**
- Trong quá trình từ (a) sang (b), tụ mất năng lượng nên sinh công dương lên các điện tích. Điện trường do điện tích tụ tạo ra đẩy dòng trong dây ngoài rời bản dương và đi về phía bản âm.
- Cùng lúc đó, dòng điện qua cuộn cảm tăng dần, năng lượng từ trường tích lũy trong cuộn cảm tăng lên. Do cuộn cảm nhận thêm năng lượng, nó sinh công âm lên dòng điện tích chuyển động.
- Mặc dù năng lượng tích trữ trong cuộn cảm là năng lượng từ trường, lực mà cuộn cảm tác dụng trực tiếp lên các điện tích chuyển động trong dây dẫn lại là lực điện. Lực điện không tĩnh này xuất phát từ suất điện động tự cảm do từ thông biến thiên gây ra trong lòng cuộn dây.

Lực từ $q\vec v\times\vec B$ vuông góc vận tốc nên không trực tiếp sinh công lên hạt tải. Sự trao đổi năng lượng trong câu hỏi này gắn với lực điện.
</details>
:::
