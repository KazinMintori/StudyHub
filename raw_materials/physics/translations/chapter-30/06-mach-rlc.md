## 30.6. Mạch RLC nối tiếp

Trong mạch LC lý tưởng, ta bỏ qua điện trở. Cuộn dây và dây nối thông thường có điện trở, nên năng lượng điện từ có thể chuyển thành nội năng vật liệu qua công suất nhiệt $i^2R$. Ngoại lệ dây siêu dẫn đã được xét ở phần vật liệu. Điện trở trong mạch đóng vai trò tương tự lực cản trong dao động cơ học.

Xét một mạch điện gồm một cuộn cảm có độ tự cảm $L$, một điện trở thuần $R$ và một tụ điện có điện dung $C$ mắc nối tiếp nhau, tạo thành **mạch dao động nối tiếp L-R-C**.

![Hình 30.17: Sơ đồ mạch điện dao động nối tiếp L-R-C với khóa chuyển mạch nạp điện cho tụ và phóng điện qua điện trở cùng cuộn cảm.](../img/young-30/hinh-30-17.png)

Khi khóa chuyển mạch $S$ ở Hình 30.17 được gạt lên tiếp điểm $d$, nguồn điện một chiều có suất điện động $\mathcal E$ sẽ nạp điện cho tụ điện. Khi khóa $S$ duy trì ở vị trí này đủ lâu, tụ điện tích điện đến giá trị cực đại $Q = C\mathcal E$ và mọi dao động ban đầu tắt hẳn.

Tại thời điểm $t = 0$, ta chuyển khóa $S$ sang tiếp điểm $a$, ngắt hẳn nguồn điện ra khỏi mạch và đưa tụ điện vào mạch kín nối tiếp với điện trở $R$ và cuộn cảm $L$. Tụ điện bắt đầu phóng điện qua điện trở và cuộn cảm. Tuy nhiên, do điện trở tiêu tán năng lượng với công suất tức thời $i^2 R$, năng lượng từ trường mà cuộn cảm thu nhận được khi tụ phóng hết điện sẽ nhỏ hơn năng lượng điện trường ban đầu của tụ điện. Tương tự, khi dòng điện giảm về không và nạp điện ngược lại cho tụ, năng lượng điện trường thu hồi được tiếp tục suy giảm hơn nữa sau mỗi chu kỳ dao động.

Tùy thuộc vào độ lớn của điện trở thuần $R$, quá trình suy giảm năng lượng sẽ diễn ra theo các chế độ khác nhau:
1. **Chế độ dao động tắt dần (Underdamped)**: Khi $R$ nhỏ, điện tích và dòng vẫn đổi chiều lặp lại, với biên độ giảm theo hàm mũ như Hình 30.16a.
2. **Chế độ tắt dần tới hạn (Critically damped)**: Khi $R$ đạt ngưỡng tới hạn, mạch không còn dao động. Với tụ ban đầu tích điện và dòng đầu bằng không như hình, điện tích trở về không nhanh hơn trường hợp quá tắt dần mà không đổi dấu.
3. **Chế độ quá tắt dần (Overdamped)**: Khi điện trở $R$ lớn hơn giá trị tới hạn, mạch hoàn toàn không dao động, điện tích trên tụ giảm chậm chạp dần về không như ở Hình 30.16c.

![Hình 30.16: Đồ thị điện tích trên tụ điện theo thời gian trong mạch dao động nối tiếp L-R-C ở ba chế độ suy giảm khác nhau.](../img/young-30/hinh-30-16.png)

---

### Thiết lập phương trình vi phân

Để khảo sát định lượng diễn biến điện tích $q$ và dòng điện $i$ theo thời gian trong mạch L-R-C nối tiếp, ta áp dụng quy tắc vòng Kirchhoff cho mạch kín $abcda$ ở Hình 30.17 sau khi khóa $S$ đã gạt sang tiếp điểm $a$.

Quy ước chiều dương của điện tích $q$ và dòng điện $i$ được chọn hoàn toàn nhất quán với khảo sát mạch L-C: Bản cực bên trái tích điện dương $+q$, bản cực bên phải tích điện âm $-q$, và dòng điện tức thời qua mạch được định nghĩa là $i = dq/dt$. Khi tụ điện bắt đầu phóng điện, điện tích $q$ giảm ($dq/dt < 0$), do đó dòng điện ban đầu mang giá trị âm, tức là chảy ngược chiều kim đồng hồ quanh vòng kín.

Bắt đầu từ điểm $a$ và đi thuận chiều kim đồng hồ qua $b$, $c$, $d$ rồi trở về $a$:
- Đi qua điện trở $R$ theo chiều dòng điện $i$, thế điện giảm một lượng $iR$, đóng góp số hạng $-iR$.
- Đi qua cuộn cảm $L$ theo chiều dòng điện $i$, suất điện động tự cảm đóng góp số hạng $-L(di/dt)$.
- Đi từ bản âm sang bản dương của tụ điện, thế điện tăng thêm $q/C$, hay khi đi từ bản dương sang bản âm theo chiều vòng kín, độ biến thiên điện thế là $-q/C$.

Tổng độ biến thiên điện thế quanh vòng kín bằng không:

$$
-iR - L\frac{di}{dt} - \frac{q}{C} = 0
$$

Thay dòng điện $i = dq/dt$ và đạo hàm bậc nhất của dòng điện $di/dt = d^2q/dt^2$ vào phương trình trên, ta được:

$$
-L\frac{d^2q}{dt^2} - R\frac{dq}{dt} - \frac{q}{C} = 0
$$

Chia cả hai vế của phương trình cho $-L$ và sắp xếp lại theo thứ tự đạo hàm giảm dần, ta thu được **phương trình vi phân mô tả mạch dao động L-R-C nối tiếp**:

$$
\frac{d^2q}{dt^2} + \frac{R}{L}\frac{dq}{dt} + \frac{1}{LC}q = 0 \tag{30.27}
$$

Khi không có điện trở thuần ($R = 0$), phương trình (30.27) thu gọn về phương trình vi phân bậc hai của mạch dao động LC lý tưởng:

$$
\frac{d^2q}{dt^2} + \frac{1}{LC}q = 0
$$

Phương trình (30.27) có dạng toán học hoàn toàn trùng khớp với phương trình dao động cơ học tắt dần của con lắc lò xo chịu lực cản nhớt:

$$
\frac{d^2x}{dt^2} + \frac{b}{m}\frac{dx}{dt} + \frac{k}{m}x = 0
$$

Cụ thể, li độ cơ học $x$ tương ứng với điện tích $q$, còn vận tốc $v_x = dx/dt$ tương ứng với cường độ dòng điện $i = dq/dt$. Đồng thời, khối lượng $m$ tương ứng với độ tự cảm $L$, hệ số cản nhớt $b$ tương ứng với điện trở thuần $R$, và độ cứng lò xo $k$ tương ứng với nghịch đảo điện dung $1/C$.

---

### Các chế độ suy giảm

Nghiệm của phương trình vi phân tuyến tính thuần nhất bậc hai (30.27) phụ thuộc quyết định vào dấu của biệt thức đặc trưng, tức là mối tương quan định lượng giữa $R^2$ và $4L/C$.

### 1. Chế độ dao động tắt dần (Underdamped)

Khi điện trở thuần thỏa mãn điều kiện $R^2 < 4L/C$, nghiệm tổng quát của phương trình (30.27) có dạng:

$$
q(t) = A e^{-(R/2L)t} \times \cos(\omega' t + \phi) \tag{30.28}
$$

Các hằng số $A$ và $\phi$ được xác định từ điện tích và dòng ban đầu. $A$ là hệ số của bao biên độ ở mốc đầu, không nhất thiết bằng $q(0)$. Với $\alpha=R/(2L)$,

$$
\begin{aligned}
q(0) &= A\cos\phi, \\
i(0) &= -\alpha q(0) -\omega'A\sin\phi.
\end{aligned}
$$

Tần số góc của dao động tắt dần $\omega'$ trong phương trình (30.28) được xác định bởi:

$$
\omega' = \sqrt{\frac{1}{LC} - \frac{R^2}{4L^2}} \tag{30.29}
$$

**Kiểm tra nghiệm:** Hãy lấy hai đạo hàm của (30.28), rồi thế vào (30.27).

<details><summary>Xem quan hệ dùng để kiểm tra</summary>

Đặt $\alpha=R/(2L)$. Đạo hàm của nghiệm cho

$$
\begin{aligned}
q'' &= -2\alpha q' -(\alpha^2+\omega'^2)q, \\
\alpha^2+\omega'^2 &= \frac1{LC}.
\end{aligned}
$$

Vì $2\alpha=R/L$, hai hệ thức này cho đúng phương trình (30.27).

</details>

Quan sát phương trình (30.28) và (30.29), ta rút ra các nhận xét vật lý quan trọng:
- Hàm số $q(t)$ biểu diễn một dao động điều hòa hình sin với biên độ suy giảm theo hàm mũ $A(t) = A e^{-(R/2L)t}$.
- Thừa số suy giảm theo thời gian là $e^{-(R/2L)t}$. Cần lưu ý rằng số mũ ở đây chứa hệ số $R/(2L)$, khác với số mũ $e^{-(R/L)t}$ trong quá trình tăng và giảm dòng của mạch R-L thuần túy đã khảo sát ở bài trước.
- Khi điện trở thuần $R = 0$, tần số góc $\omega'$ trở về đúng tần số góc dao động riêng của mạch LC lý tưởng $\omega = 1/\sqrt{LC}$, và phương trình (30.28) trở về phương trình dao động điều hòa $q(t) = Q\cos(\omega t + \phi)$.
- Khi điện trở $R > 0$, số hạng $R^2/(4L^2)$ làm giảm đại lượng dưới dấu căn, do đó tần số góc dao động tắt dần $\omega'$ luôn nhỏ hơn tần số góc riêng $\omega$ của mạch không có điện trở. Điện trở $R$ càng lớn thì tần số góc $\omega'$ càng nhỏ và chu kỳ dao động càng kéo dài.

### 2. Chế độ tắt dần tới hạn (Critically damped)

Khi điện trở thuần đạt đúng giá trị tới hạn sao cho:

$$
R^2 = \frac{4L}{C} \iff R = 2\sqrt{\frac{L}{C}}
$$

Biểu thức dưới căn trong (30.29) bằng không. Nghiệm không còn phần dao động hình sin, mà có dạng:

$$
q(t) = (C_1 + C_2 t)e^{-(R/2L)t}
$$

Với tụ ban đầu tích điện và dòng đầu bằng không như đồ thị, điện tích trở về không nhanh hơn trường hợp quá tắt dần mà không dao động. Với điều kiện đầu khác, nghiệm có thể đổi dấu một lần. Điều đó không phải dao động lặp lại.

### 3. Chế độ quá tắt dần (Overdamped)

Khi điện trở thuần rất lớn, vượt quá ngưỡng tới hạn ($R^2 > 4L/C$), đại lượng dưới dấu căn trong phương trình (30.29) trở nên âm. Nghiệm của phương trình vi phân không còn chứa thành phần hàm lượng giác mà phân rã thành tổng của hai hàm mũ thực giảm dần:

$$
q(t) = C_1 e^{-\alpha_1 t} + C_2 e^{-\alpha_2 t}
$$

Ở đây $\alpha_1,\alpha_2$ là hai tốc độ suy giảm dương. Nghiệm đặc trưng của phương trình vi phân là $-\alpha_1$ và $-\alpha_2$. Có thể viết

$$
\begin{aligned}
\gamma &= \frac{R}{2L}, \\
\delta &= \sqrt{\gamma^2-\frac1{LC}}, \\
\alpha_1 &= \gamma-\delta, \\
\alpha_2 &= \gamma+\delta.
\end{aligned}
$$

Các hệ số $C_1,C_2$ trong nghiệm được quyết định bởi điều kiện đầu. Hệ không dao động lặp lại, dù một điều kiện đầu thích hợp có thể làm điện tích đổi dấu một lần.

Phép tương tự với dao động cơ tắt dần được giữ đầy đủ khi thay $x$ bằng $q$, $m$ bằng $L$, $k$ bằng $1/C$ và hệ số cản $b$ bằng $R$. Điều kiện tới hạn của hệ cơ là $b^2=4km$, tương ứng với $R^2=4L/C$ của mạch điện.

Các ứng dụng của RLC còn mở rộng khi mắc thêm nguồn suất điện động biến thiên hình sin. Khi ấy mạch có dao động cưỡng bức và các hiệu ứng cộng hưởng, tương tự hệ cơ có ngoại lực tuần hoàn. Đó là nội dung mạch xoay chiều ở chương tiếp theo.

---

### Ví dụ minh họa

::: example Ví dụ 30.10: Điện trở làm tần số dao động giảm một nửa

Cần mắc thêm một điện trở thuần $R$ bằng bao nhiêu (tính theo độ tự cảm $L$ và điện dung $C$) để mạch dao động nối tiếp L-R-C có tần số dao động bằng một nửa tần số dao động khi không có điện trở?

**Nhận diện và thiết lập bài toán:**

Bài toán yêu cầu khảo sát mạch dao động nối tiếp L-R-C ở chế độ dao động tắt dần.
Mục tiêu là tìm giá trị điện trở thuần $R$ để tần số góc $\omega'$ của mạch có điện trở bằng một nửa tần số góc riêng $\omega$ của mạch LC lý tưởng khi chưa mắc điện trở:

$$
\omega' = \frac{1}{2}\omega
$$

Tần số góc dao động tắt dần của mạch L-R-C được xác định bởi phương trình (30.29):

$$
\omega' = \sqrt{\frac{1}{LC} - \frac{R^2}{4L^2}}
$$

Tần số góc riêng của mạch khi không có điện trở thuần ($R = 0$) được xác định bởi phương trình (30.22):

$$
\omega = \sqrt{\frac{1}{LC}}
$$

**Các bước tính toán:**

Thiết lập đẳng thức $\omega' = \omega/2$ từ hai biểu thức trên:

$$
\sqrt{\frac{1}{LC} - \frac{R^2}{4L^2}} = \frac{1}{2}\sqrt{\frac{1}{LC}}
$$

Bình phương cả hai vế của phương trình:

$$
\frac{1}{LC} - \frac{R^2}{4L^2} = \frac{1}{4LC}
$$

Chuyển các số hạng và cô lập số hạng chứa điện trở $R$:

$$
\begin{aligned}
\frac{R^2}{4L^2} &= \frac{1}{LC} - \frac{1}{4LC} \\
\frac{R^2}{4L^2} &= \frac{3}{4LC}
\end{aligned}
$$

Nhân cả hai vế với $4L^2$:

$$
R^2 = 4L^2 \times \frac{3}{4LC} = \frac{3L}{C}
$$

Lấy căn bậc hai hai vế, ta tìm được giá trị điện trở thuần cần tìm:

$$
R = \sqrt{\frac{3L}{C}}
$$

Xét một ví dụ bằng số cụ thể với mạch điện ở Ví dụ 30.8, trong đó độ tự cảm $L = 10\text{ mH} = 10 \times 10^{-3}\text{ H}$ và điện dung $C = 25\ \mu\text{F} = 25 \times 10^{-6}\text{ F}$:

$$
\begin{aligned}
R &= \sqrt{\frac{3 \times 10 \times 10^{-3}\text{ H}}{25 \times 10^{-6}\text{ F}}} \\
&= \sqrt{1200\ \Omega^2} \\
&\approx 34{,}64\ \Omega \approx 35\ \Omega
\end{aligned}
$$

Khi mắc thêm điện trở $R \approx 35\ \Omega$ vào mạch của Ví dụ 30.8, tần số dao động của mạch sẽ giảm đi một nửa, từ $f = 320\text{ Hz}$ xuống còn $f' = 160\text{ Hz}$.

**Đánh giá:**

Giá trị điện trở tới hạn để mạch chuyển sang chế độ tắt dần tới hạn là $R_{\text{th}} = \sqrt{4L/C} = 2\sqrt{L/C} = 40\ \Omega$. Giá trị điện trở $R = \sqrt{3L/C} \approx 34{,}64\ \Omega$ nhỏ hơn điện trở tới hạn $40\ \Omega$, điều này hoàn toàn phù hợp vì mạch cần nằm trong chế độ dao động tắt dần để duy trì tính dao động tuần hoàn.

Mạch RLC tương tự hệ lò xo–vật nặng có lực cản. Khi $R$ tăng, tần số dao động giảm. Khi điện trở đạt hoặc vượt $R_{\text{th}}=2\sqrt{L/C}$, hệ không còn dao động lặp lại.
:::

---

### Câu hỏi tự kiểm 30.6

Một mạch dao động nối tiếp L-R-C chứa một điện trở thuần $R = 2{,}0\ \Omega$. Tại thời điểm ban đầu $t = 0$, điện tích trên tụ điện là $2{,}0\ \mu\text{C}$. Trong các trường hợp giá trị của độ tự cảm $L$ và điện dung $C$ sau đây, trường hợp nào làm cho điện tích trên tụ điện **không dao động**?

- (i) $L = 3{,}0\ \mu\text{H}$, $C = 6{,}0\ \mu\text{F}$
- (ii) $L = 6{,}0\ \mu\text{H}$, $C = 3{,}0\ \mu\text{F}$
- (iii) $L = 3{,}0\ \mu\text{H}$, $C = 3{,}0\ \mu\text{F}$

::: details Đáp án và giải thích chi tiết
**Đáp án đúng**: Các trường hợp (i) và (iii).

**Phân tích và lập luận chi tiết**:

Điện tích trên tụ điện không dao động khi hệ thống rơi vào chế độ tắt dần tới hạn hoặc quá tắt dần, tức là điều kiện:

$$
R^2 \ge \frac{4L}{C}
$$

Trong cả ba trường hợp, bình phương điện trở thuần của mạch đều bằng:

$$
R^2 = (2{,}0\ \Omega)^2 = 4{,}0\ \Omega^2
$$

Bây giờ ta tính giá trị của đại lượng $4L/C$ cho từng trường hợp:

- **Trường hợp (i)**: Với $L = 3{,}0\ \mu\text{H}$ và $C = 6{,}0\ \mu\text{F}$:
  $$
\begin{aligned}
\frac{4L}{C} &= \frac{4(3{,}0\ \mu\text{H})}{6{,}0\ \mu\text{F}} \\
&= 2{,}0\ \Omega^2
\end{aligned}
$$
  Vì $R^2 = 4{,}0\ \Omega^2 > 4L/C = 2{,}0\ \Omega^2$, mạch rơi vào **chế độ quá tắt dần (Overdamped)**. Điện tích trên tụ giảm dần về không mà không dao động. Do đó trường hợp (i) thỏa mãn.

- **Trường hợp (ii)**: Với $L = 6{,}0\ \mu\text{H}$ và $C = 3{,}0\ \mu\text{F}$:
  $$
\begin{aligned}
\frac{4L}{C} &= \frac{4(6{,}0\ \mu\text{H})}{3{,}0\ \mu\text{F}} \\
&= 8{,}0\ \Omega^2
\end{aligned}
$$
  Vì $R^2 = 4{,}0\ \Omega^2 < 4L/C = 8{,}0\ \Omega^2$, mạch rơi vào **chế độ dao động tắt dần (Underdamped)**. Điện tích trên tụ vẫn dao động đổi chiều quanh vị trí cân bằng với biên độ giảm dần. Do đó trường hợp (ii) không thỏa mãn.

- **Trường hợp (iii)**: Với $L = 3{,}0\ \mu\text{H}$ và $C = 3{,}0\ \mu\text{F}$:
  $$
\begin{aligned}
\frac{4L}{C} &= \frac{4(3{,}0\ \mu\text{H})}{3{,}0\ \mu\text{F}} \\
&= 4{,}0\ \Omega^2
\end{aligned}
$$
  Vì $R^2 = 4{,}0\ \Omega^2 = 4L/C$, mạch rơi vào **chế độ tắt dần tới hạn (Critically damped)**. Điện tích trên tụ giảm nhanh về không mà không đổi chiều dao động. Do đó trường hợp (iii) thỏa mãn.

Kết luận: Các bộ thông số (i) và (iii) làm cho điện tích trên tụ điện không dao động.
:::
