## Bài tổng hợp 28.61–28.75

::: exercise 28.61 ••• CP
Hai dây dài, song song được treo bằng các dây treo dài $4{,}00\,\mathrm{cm}$ từ cùng một trục như Hình P28.61. Khối lượng trên một đơn vị chiều dài của mỗi dây là $0{,}0125\,\mathrm{kg/m}$. Hai dòng điện có cùng độ lớn nhưng ngược chiều. Tìm dòng điện trong mỗi dây nếu mỗi dây treo tạo góc $6{,}00^\circ$ với phương thẳng đứng.

![Hình P28.61: Hai dây mang dòng điện ngược chiều đẩy nhau và làm các dây treo nghiêng.](img/young-28/hinh-p28-61.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Chiều dài dây treo $l=0{,}0400\,\mathrm m$, khối lượng dài $\lambda=0{,}0125\,\mathrm{kg/m}$ và góc lệch $\theta=6{,}00^\circ$. Hai dòng có độ lớn $I$.

**Hướng đi:**

- Hai dòng ngược chiều tạo lực đẩy. Dùng lực giữa hai dây dài để tính lực ngang trên một đơn vị chiều dài.
- Mỗi dây treo giữ cân bằng theo hai phương. Tỉ số lực ngang và trọng lượng bằng $\tan\theta$, giúp loại lực căng.
- Khoảng cách giữa hai dây nhận đóng góp từ cả hai phía của trục treo, nên bằng $2l\sin\theta$.

Khoảng cách giữa hai dây là:

$$
d = 2l\sin\theta = 8{,}36\times10^{-3}\,\mathrm m.
$$

Xét một đoạn dây dài $L$. Lực từ hướng ngang, trọng lực hướng xuống và lực căng có hướng dọc dây treo. Hai phương trình cân bằng cho:

$$
\begin{aligned}
T\sin\theta &= F_B, \\
T\cos\theta &= \lambda Lg, \\
\frac{F_B}{L} &= \lambda g\tan\theta.
\end{aligned}
$$

Mặt khác, lực từ trên một đơn vị chiều dài bằng:

$$
\frac{F_B}{L}=\frac{\mu_0I^2}{2\pi d}.
$$

Suy ra:

$$
\begin{aligned}
I &= \sqrt{\frac{2\pi d\lambda g\tan\theta}{\mu_0}} \\
&= 23{,}2\,\mathrm A.
\end{aligned}
$$

Mỗi dây mang dòng $23{,}2\,\mathrm A$, theo hai chiều ngược nhau như đã cho.
:::

::: exercise 28.62 •
Hai cung dây bán nguyệt trong Hình P28.62 có bán kính $a$ và $b$. Tính độ lớn và chiều của từ trường tổng do dòng điện tạo ra tại $P$.

![Hình P28.62: Hai cung bán nguyệt đồng tâm có dòng điện chạy theo hai chiều ngược nhau.](img/young-28/hinh-p28-62.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $P$ là tâm chung, $a$ là bán kính cung trong, $b>a$ là bán kính cung ngoài. Dòng trên cung trong ngược chiều kim đồng hồ, còn dòng trên cung ngoài theo chiều kim đồng hồ.

**Hướng đi:**

- Dùng từ trường tại tâm của cung tròn, vì khoảng cách từ mọi phần tử cung đến $P$ không đổi.
- Các đoạn nối theo bán kính không đóng góp, vì phần tử dây song song với vector hướng đến $P$.
- Hai cung tạo trường ngược chiều. Cung có bán kính nhỏ hơn tạo trường mạnh hơn.

Với cung góc $\alpha$, tích phân Biot–Savart cho:

$$
\begin{aligned}
B_{\mathrm{arc}} &= \frac{\mu_0I}{4\pi R}\alpha, \\
\alpha &= \pi, \\
B_{\mathrm{semicircle}} &= \frac{\mu_0I}{4R}.
\end{aligned}
$$

Trường của cung trong hướng ra khỏi trang giấy, còn trường của cung ngoài hướng vào. Do đó:

$$
B=\frac{\mu_0I}{4}\left(\frac1a-\frac1b\right).
$$

Vì $a<b$, trường tổng hướng ra khỏi trang giấy.
:::

::: exercise 28.63 •
Một trụ dẫn đặc, dài, có trục theo phương $z$. Mật độ dòng đối xứng quanh trục nhưng thay đổi theo khoảng cách $r$ đến trục:

$$
\vec J(r)=\frac{\beta}{r}e^{(r-a)/\delta}\hat k.
$$

Biểu thức này áp dụng trong trụ với $0<r\le a$. Ngoài trụ, $\vec J=0$.

Bán kính trụ là $a=5{,}00\,\mathrm{cm}$, hằng số $\beta=600\,\mathrm{A/m}$ và $\delta=2{,}50\,\mathrm{cm}$. (a) Tìm tổng dòng $I_0$ theo $\beta,\delta,a$ và tính giá trị số.

(b) Dùng định luật Ampere tìm từ trường ở $r\ge a$, biểu diễn theo $I_0$ thay vì $\beta$.

(c) Tìm dòng bao trong tiết diện tròn bán kính $r\le a$, biểu diễn theo $I_0$.

(d) Tìm từ trường trong trụ.

(e) Tính độ lớn trường ở $r=\delta$, $r=a$ và $r=2a$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $a=0{,}0500\,\mathrm m$, $\delta=0{,}0250\,\mathrm m$. Dòng theo $+z$, có mật độ $J=\beta e^{(r-a)/\delta}/r$ trong trụ.

**Hướng đi:**

- Chia tiết diện thành các vành khăn có diện tích $2\pi r\,dr$. Mật độ dòng không đều nên phải tích phân, không thể nhân một giá trị $J$ với toàn tiết diện.
- Đối xứng trụ làm trường tiếp tuyến với đường tròn đồng tâm và có độ lớn không đổi trên đường ấy. Vì vậy, tích phân Ampere trở thành $B(2\pi r)$.
- Bên ngoài dùng tổng dòng $I_0$. Bên trong chỉ dùng dòng nằm trong bán kính đường tích phân.

(a) Gọi $s$ là biến bán kính trong phép tích phân. Khi đó:

$$
\begin{aligned}
I_0 &= \int_0^a J(s)\,2\pi s\,ds \\
&= 2\pi\beta\int_0^a e^{(s-a)/\delta}\,ds \\
&= 2\pi\beta\delta(1-e^{-a/\delta}) \\
&= 81{,}5\,\mathrm A.
\end{aligned}
$$

Thừa số $1/s$ trong mật độ triệt tiêu với thừa số $s$ của diện tích vành khăn. Vì vậy tổng dòng hữu hạn dù mật độ tăng không giới hạn khi tiến đến trục.

(b) Với $r\ge a$, đường Ampere bao toàn bộ dòng:

$$
\begin{aligned}
B(2\pi r) &= \mu_0I_0, \\
\vec B(r) &= \frac{\mu_0I_0}{2\pi r}\hat\phi.
\end{aligned}
$$

Vector đơn vị $\hat\phi$ chỉ chiều đi quanh trục theo quy tắc bàn tay phải của dòng $+z$.

(c) Dòng nằm trong bán kính $r$ là:

$$
\begin{aligned}
I(r) &= 2\pi\beta\delta \left(e^{(r-a)/\delta}-e^{-a/\delta}\right), \\
I(r) &= I_0\frac{e^{r/\delta}-1}{e^{a/\delta}-1}.
\end{aligned}
$$

(d) Thay dòng bao vào định luật Ampere. Với $0<r\le a$:

$$
\vec B(r)=\frac{\mu_0I_0}{2\pi r}
\frac{e^{r/\delta}-1}{e^{a/\delta}-1}\hat\phi.
$$

Hai biểu thức trong và ngoài cho cùng giá trị tại $r=a$. Tại đúng trục $r=0$, mô hình mật độ đã cho không xác định. Không gán tùy tiện giá trị trường bằng không tại điểm ấy. Độ lớn trường có giới hạn hữu hạn khi $r$ tiến đến không, nhưng hướng $\hat\phi$ phụ thuộc hướng tiếp cận trục.

(e) Các giá trị cần tìm là:

$$
\begin{aligned}
B(\delta) &= 1{,}75\times10^{-4}\,\mathrm T, \\
B(a) &= 3{,}26\times10^{-4}\,\mathrm T, \\
B(2a) &= 1{,}63\times10^{-4}\,\mathrm T.
\end{aligned}
$$
:::

::: exercise 28.64 ••
Tính độ lớn và chiều của từ trường tại $P$ do dòng $I=12{,}0\,\mathrm A$ trong Hình P28.64. Cung $BC$ có bán kính $30{,}0\,\mathrm{cm}$, cung $DA$ có bán kính $20{,}0\,\mathrm{cm}$. $P$ là tâm cong của cả hai cung. Hai đoạn thẳng $CD$ và $AB$ đều dài $10{,}0\,\mathrm{cm}$.

![Hình P28.64: Dòng chạy trên hai cung đồng tâm góc 120 độ và hai đoạn nối theo bán kính.](img/young-28/hinh-p28-64.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $I=12{,}0\,\mathrm A$, bán kính ngoài $b=0{,}300\,\mathrm m$, bán kính trong $a=0{,}200\,\mathrm m$, góc cung $\alpha=120^\circ=2\pi/3$.

**Hướng đi:**

- Hai đoạn thẳng theo bán kính cho tích có hướng bằng không tại tâm $P$.
- Tính trường của từng cung bằng công thức cung tròn, vì mỗi cung có bán kính không đổi.
- Giữ dấu chiều trường khi cộng. Cung ngoài chạy ngược chiều kim đồng hồ, cung trong chạy theo chiều kim đồng hồ.

Chọn chiều ra khỏi trang giấy là dương. Trường của cung ngoài dương, còn trường của cung trong âm:

$$
\begin{aligned}
B_z &= \frac{\mu_0I\alpha}{4\pi} \left(\frac1b-\frac1a\right) \\
&= -4{,}19\times10^{-6}\,\mathrm T.
\end{aligned}
$$

Độ lớn là $4{,}19\,\mu\mathrm T$, hướng vào trang giấy.
:::

::: exercise 28.65 • CALC
Dây thẳng dài, tiết diện tròn bán kính $R$, mang tổng dòng $I$. Mật độ dòng thay đổi theo bán kính theo quy luật $J=\alpha r$. (a) Tìm $\alpha$ theo $I,R$ bằng điều kiện tích phân mật độ trên tiết diện bằng tổng dòng.

(b) Dùng định luật Ampere tìm độ lớn trường ở (i) $r\le R$ và (ii) $r\ge R$, biểu diễn kết quả theo $I$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $J(r)=\alpha r$, tiết diện tròn bán kính $R$, tổng dòng $I$.

**Hướng đi:**

- Tích phân $J\,dA$ trên các vành khăn để tìm tổng dòng và hằng số $\alpha$.
- Tích phân chỉ đến bán kính đường Ampere khi tính trường bên trong.
- Đối xứng trụ cho $B(2\pi r)=\mu_0I_{\mathrm{bao}}$.

(a) Tổng dòng là:

$$
\begin{aligned}
I &= \int_0^R\alpha s\,2\pi s\,ds \\
&= \frac{2\pi\alpha R^3}{3}, \\
\alpha &= \frac{3I}{2\pi R^3}.
\end{aligned}
$$

(b) Với $r\le R$, dòng bao là:

$$
\begin{aligned}
I(r) &= \frac{2\pi\alpha r^3}{3} \\
&= I\left(\frac rR\right)^3, \\
B(r) &= \frac{\mu_0Ir^2}{2\pi R^3}.
\end{aligned}
$$

Với $r\ge R$, đường tích phân bao toàn bộ dòng:

$$
B(r)=\frac{\mu_0I}{2\pi r}.
$$

Tại trục, trường bằng không. Tại $r=R$, cả hai biểu thức cho $\mu_0I/(2\pi R)$. Chiều trường đi quanh trục theo quy tắc bàn tay phải của dòng.
:::

::: exercise 28.66 • CALC
Dây trong Hình P28.66 dài vô hạn và mang dòng $I$. Tính độ lớn và chiều của từ trường tại $P$.

![Hình P28.66: Dây gấp vuông góc với dòng đi sang phải rồi đi xuống, điểm P nằm cách góc một đoạn a.](img/young-28/hinh-p28-66.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $P$ nằm trên phần kéo dài của đoạn ngang, cách góc dây một khoảng $a$. Đoạn thẳng đứng kéo dài xuống vô hạn và mang dòng đi xuống.

**Hướng đi:**

- Đoạn ngang không đóng góp, vì mọi phần tử dây và vector đến $P$ cùng phương.
- Đoạn thẳng đứng là dây bán vô hạn, không phải dây vô hạn về cả hai phía. Phải lấy đúng giới hạn tích phân.
- Tích có hướng của phần tử dòng đi xuống và vector sang phải chỉ ra khỏi trang giấy.

Gọi $s\ge0$ là khoảng cách từ góc dây xuống phần tử đang xét. Khoảng cách đến $P$ bằng $\sqrt{a^2+s^2}$, và thừa số hình học trong Biot–Savart cho:

$$
\begin{aligned}
B &= \frac{\mu_0I}{4\pi} \int_0^\infty\frac{a\,ds}{(a^2+s^2)^{3/2}} \\
&= \frac{\mu_0I}{4\pi} \left[\frac{s}{a\sqrt{a^2+s^2}}\right]_0^\infty \\
&= \frac{\mu_0I}{4\pi a}.
\end{aligned}
$$

Trường hướng ra khỏi trang giấy. Kết quả bằng một nửa trường của dây thẳng dài vô hạn cách $P$ một khoảng $a$.
:::

::: exercise 28.67 • CALC
Trụ dẫn đặc, dài, có bán kính $a$ và trục theo $z$. Mật độ dòng đối xứng trục, có dạng:

$$
\vec J(r)=\frac{2I_0}{\pi a^2}
\left(1-\frac{r^2}{a^2}\right)\hat k.
$$

Trong trụ, biểu thức áp dụng với $r\le a$. Ngoài trụ, $\vec J=0$.

(a) Chứng minh $I_0$ là tổng dòng qua tiết diện.

(b) Tìm độ lớn từ trường ở $r\ge a$.

(c) Tìm dòng bao trong tiết diện tròn đồng tâm bán kính $r\le a$.

(d) Tìm từ trường trong trụ và so sánh hai kết quả tại $r=a$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mật độ giảm từ $2I_0/(\pi a^2)$ tại trục đến không ở mặt trụ. Dòng theo $+z$.

**Hướng đi:**

- Dùng vành khăn $2\pi r\,dr$ để cộng dòng, vì $J$ phụ thuộc bán kính.
- Đường Ampere đồng tâm có trường tiếp tuyến và độ lớn không đổi.
- Dòng bao bên trong phải tính theo bán kính thực của đường tích phân.

(a) Tích phân trên toàn tiết diện:

$$
\begin{aligned}
I_{\mathrm{tot}} &= \frac{4I_0}{a^2} \int_0^a\left(s-\frac{s^3}{a^2}\right)ds \\
&= \frac{4I_0}{a^2} \left(\frac{a^2}{2}-\frac{a^2}{4}\right) \\
&= I_0.
\end{aligned}
$$

(b) Bên ngoài, tổng dòng bao là $I_0$:

$$
B(r)=\frac{\mu_0I_0}{2\pi r}.
$$

(c) Khi chỉ tích phân đến $r$:

$$
\begin{aligned}
I(r) &= \frac{4I_0}{a^2} \left(\frac{r^2}{2}-\frac{r^4}{4a^2}\right) \\
&= I_0\left(\frac{2r^2}{a^2}-\frac{r^4}{a^4}\right).
\end{aligned}
$$

(d) Từ định luật Ampere:

$$
\begin{aligned}
B(r) &= \frac{\mu_0I(r)}{2\pi r} \\
&= \frac{\mu_0I_0r}{2\pi a^2} \left(2-\frac{r^2}{a^2}\right).
\end{aligned}
$$

Biểu thức trong cho trường bằng không tại trục. Tại mặt trụ, biểu thức trong và ngoài đều cho:

$$
B(a)=\frac{\mu_0I_0}{2\pi a}.
$$

Chiều trường tuân theo quy tắc bàn tay phải quanh dòng $+z$.
:::

::: exercise 28.68 •
Vòng dây tròn bán kính $R$ mang dòng $I_2$ theo chiều kim đồng hồ như Hình P28.68. Tâm vòng cách dây thẳng dài bên dưới một khoảng $D$. Tìm độ lớn và chiều dòng $I_1$ trong dây thẳng để từ trường tổng tại tâm vòng bằng không.

![Hình P28.68: Vòng dây có dòng theo chiều kim đồng hồ đặt phía trên một dây thẳng dài.](img/young-28/hinh-p28-68.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tâm vòng cách dây thẳng một khoảng $D$, bán kính vòng $R$, dòng vòng $I_2$ theo chiều kim đồng hồ.

**Hướng đi:**

- Trường của vòng tại tâm hướng vào trang giấy. Dây thẳng phải tạo trường ra khỏi trang giấy để triệt tiêu.
- Dùng trường tại tâm vòng và trường của dây dài tại khoảng cách $D$.
- Sau khi xác định chiều đối nhau, đặt hai độ lớn bằng nhau.

Với điểm nằm phía trên dây, dòng từ trái sang phải tạo trường ra khỏi trang giấy. Do đó $I_1$ phải chạy sang phải. Điều kiện độ lớn là:

$$
\begin{aligned}
\frac{\mu_0I_1}{2\pi D} &= \frac{\mu_0I_2}{2R}, \\
I_1 &= \frac{\pi D}{R}I_2.
\end{aligned}
$$
:::

::: exercise 28.69 •
Mặt dòng điện vô hạn được tạo bởi các dây dài, tiết diện vuông, đặt sát nhau như Hình P28.69. Các dây nằm trong mặt phẳng $xy$, song song trục $y$, mỗi dây mang dòng $I$ theo $+y$. Có $n$ dây trên một đơn vị chiều dài đo theo $x$. Tìm độ lớn và chiều trường (a) ở khoảng cách $a$ phía dưới mặt dòng và (b) ở khoảng cách $a$ phía trên mặt dòng.

![Hình P28.69: Các dây song song mang dòng theo trục y tạo thành mặt dòng điện vô hạn.](img/young-28/hinh-p28-69.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mặt dòng nằm ở $z=0$, dòng theo $+y$, mật độ dây $n$ và dòng mỗi dây $I$. Hai điểm cần xét có $z=-a$ và $z=+a$.

**Hướng đi:**

- Đối xứng và chồng chất làm các thành phần vuông góc mặt triệt tiêu. Trường còn lại song song trục $x$.
- Phản xạ qua mặt dòng cho hai trường cùng độ lớn và ngược chiều.
- Dùng đường Ampere hình chữ nhật cắt qua mặt dòng để tính độ lớn từ dòng bao.

Chọn hình chữ nhật có hai cạnh dài $l$ song song $x$, một cạnh ở phía trên và một cạnh ở phía dưới mặt dòng. Hai cạnh còn lại vuông góc trường nên không đóng góp. Có $nl$ dây xuyên qua mặt chữ nhật, mỗi dây mang dòng $I$:

$$
\begin{aligned}
\oint\vec B\cdot d\vec l &= 2Bl, \\
I_{\mathrm{bao}} &= nlI, \\
2Bl &= \mu_0nlI, \\
B &= \frac{\mu_0nI}{2}.
\end{aligned}
$$

Quy tắc bàn tay phải cho trường phía trên hướng $+x$, phía dưới hướng $-x$. Vì vậy:

$$
\begin{aligned}
\vec B(z = -a) &= -\frac{\mu_0nI}{2}\hat i, \\
\vec B(z = +a) &= +\frac{\mu_0nI}{2}\hat i.
\end{aligned}
$$

Độ lớn không phụ thuộc $a$ trong mô hình mặt dòng vô hạn.
:::

::: exercise 28.70 •
Các dây dài có tiết diện vuông, đặt sát nhau tạo thành mặt dòng vô hạn với dòng hướng ra khỏi trang giấy. Mặt dòng thứ hai nằm phía dưới, song song mặt thứ nhất và cách một khoảng $d$, có dòng hướng vào trang giấy. Mỗi mặt có $n$ dây trên một đơn vị chiều dài, mỗi dây mang dòng $I$. Dùng kết quả bài 28.69 để tìm độ lớn và chiều trường tổng tại (a) $P$ phía trên mặt trên, (b) $R$ giữa hai mặt và (c) $S$ phía dưới mặt dưới.

![Hình P28.70: Hai mặt dòng vô hạn song song có dòng điện ngược chiều.](img/young-28/hinh-p28-70.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mỗi mặt tạo trường có độ lớn $B_0=\mu_0nI/2$ ở mỗi phía. Mặt trên có dòng đi ra, mặt dưới có dòng đi vào trang giấy.

**Hướng đi:**

- Xác định riêng chiều trường của từng mặt tại từng điểm bằng quy tắc bàn tay phải.
- Cộng vector, vì hai mặt không làm thay đổi dòng của nhau trong mô hình đang xét.
- Bên ngoài hai mặt, hai trường đối nhau. Ở giữa, hai trường cùng chiều.

| Điểm | Trường của mặt trên | Trường của mặt dưới | Tổng |
| --- | --- | --- | --- |
| $P$ | Sang trái | Sang phải | Bằng không |
| $R$ | Sang phải | Sang phải | Sang phải |
| $S$ | Sang phải | Sang trái | Bằng không |

Do đó:

$$
\begin{aligned}
B_P &= 0, \\
B_R &= 2B_0=\mu_0nI, \\
B_S &= 0.
\end{aligned}
$$

Trường ở $R$ hướng sang phải như mặt hình. Khoảng cách $d$ không ảnh hưởng độ lớn trong mô hình hai mặt dòng vô hạn.
:::

::: exercise 28.71 ••• CP
Vỏ trụ bán kính $R_1$, cao $H$, mang điện tích $Q_1$ và quay quanh trục với tốc độ góc $\omega_1$. Một đĩa rất nhỏ có bán kính $R_2$, khối lượng $M$ và điện tích $Q_2$ nằm bên trong, xa hai mép trụ. Tâm đĩa nằm trên trục trụ. Đĩa quay nhanh với vận tốc góc $\vec\omega_2$, trục đĩa tạo góc $\theta$ với trục trụ như Hình P28.71. Tương tác từ làm trục đĩa tiến động.

(a) Tìm độ lớn dòng bao bởi đường kín có một cạnh dọc theo trục trụ, kéo dài quá cả hai đầu trụ, còn cạnh đối diện nằm rất xa ngoài trụ.

(b) Giả sử trường đều bên trong và dùng định luật Ampere tìm trường tại tâm đĩa.

(c) Mômen từ của đĩa có độ lớn $\mu=Q_2\omega_2R_2^2/4$. Tìm độ lớn mômen lực tác dụng lên đĩa.

(d) Tìm độ lớn mômen động lượng của đĩa.

![Hình P28.71: Vỏ trụ tích điện quay tạo từ trường tác dụng mômen lên đĩa tích điện đang quay.](img/young-28/hinh-p28-71.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vỏ trụ có điện tích phân bố đều $Q_1$, chiều cao $H$, tốc độ góc $\omega_1$. Đĩa nhỏ có $Q_2,R_2,M,\omega_2$ và góc nghiêng $\theta$.

**Hướng đi:**

- Điện tích quay qua một vị trí sau mỗi chu kỳ tạo dòng điện. Tổng dòng cắt đường Ampere bằng điện tích vỏ trụ chia chu kỳ quay.
- Dùng mô hình trường đều trong trụ và trường ngoài rất nhỏ để áp dụng Ampere, giống ống dây dài.
- Đĩa là lưỡng cực từ nhỏ, nên mômen lực có độ lớn $\mu B\sin\theta$.
- Mômen động lượng của đĩa đồng chất bằng mômen quán tính $MR_2^2/2$ nhân tốc độ góc.

(a) Một vòng quay kéo dài $2\pi/\omega_1$. Dòng bao có độ lớn:

$$
I_{\mathrm{bao}}=\frac{|Q_1|\omega_1}{2\pi}.
$$

(b) Mật độ dòng mặt theo phương vòng quanh trụ là:

$$
\begin{aligned}
\sigma_1 &= \frac{Q_1}{2\pi R_1H}, \\
K &= \sigma_1R_1\omega_1 \\
&= \frac{Q_1\omega_1}{2\pi H}.
\end{aligned}
$$

Trong mô hình bỏ qua hiệu ứng mép và trường ngoài, tích phân dọc cạnh trong bằng $BH$:

$$
\begin{aligned}
BH &= \mu_0I_{\mathrm{bao}}, \\
B &= \frac{\mu_0|Q_1|\omega_1}{2\pi H}.
\end{aligned}
$$

Trường dọc trục trụ. Chiều được xác định từ chiều chuyển động của điện tích quy ước bằng quy tắc bàn tay phải. Khi dấu điện tích đảo, chiều trường đảo.

(c) Mômen từ dọc trục quay của đĩa, nên góc với từ trường là $\theta$. Vì vậy:

$$
\begin{aligned}
\tau &= \mu B\sin\theta \\
&= \frac{\mu_0|Q_1Q_2|R_2^2}{8\pi H} \times\omega_1\omega_2\sin\theta.
\end{aligned}
$$

Mômen lực vuông góc với mômen từ và trường, làm đổi hướng trục quay của đĩa.

(d) Mômen động lượng có độ lớn:

$$
L=\frac12MR_2^2\omega_2.
$$
:::

::: exercise 28.72 •• DATA
Một ống dây dài $L=40{,}0\,\mathrm{cm}$, đường kính $2{,}80\,\mathrm{cm}$ có hai cuộn được quấn sát nhau, cùng chiều, trên cùng một khuôn trụ rỗng. Cần tìm số vòng trong từng cuộn. Dòng qua cuộn 1 giữ ở $2{,}00\,\mathrm{mA}$, còn dòng $I$ qua cuộn 2 thay đổi. Hai dòng cùng chiều. Đo trường $B$ tại tâm và biểu diễn $BL/\mu_0$ theo $I$ như Hình P28.72.

(a) Giải thích vì sao các điểm gần nằm trên một đường thẳng.

(b) Dùng đồ thị để tính $N_1,N_2$.

(c) Giữ dòng cuộn 1 như trước, cho cuộn 2 mang dòng $5{,}00\,\mathrm{mA}$ theo chiều ngược lại. Tìm từ trường tại tâm.

![Hình P28.72: Đồ thị trường trong ống dây có hai cuộn theo dòng điện qua cuộn thứ hai.](img/young-28/hinh-p28-72.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $L=0{,}400\,\mathrm m$, $I_1=0{,}00200\,\mathrm A$. Trục đứng là $BL/\mu_0$ tính bằng ampere, trục ngang là $I$ tính bằng milliampere.

**Hướng đi:**

- Hai trường cùng chiều cộng đại số trong ống dây dài, nên $B=\mu_0(N_1I_1+N_2I)/L$.
- Hệ số góc theo dòng tính bằng ampere cho số vòng $N_2$. Tung độ gốc cho tích $N_1I_1$.
- Khi đảo dòng cuộn 2, giữ dấu âm của đóng góp ấy trước khi lấy độ lớn trường.

(a) Ta có:

$$
\frac{BL}{\mu_0}=N_1I_1+N_2I.
$$

Đây là quan hệ đường thẳng với $I$. Cuộn 1 tạo tung độ gốc, còn cuộn 2 quyết định hệ số góc.

(b) Đọc hai điểm tại các giao điểm lưới rõ trên đồ thị:

| $I$ (mA) | $BL/\mu_0$ (A) |
| --- | --- |
| 2,00 | 8,00 |
| 5,00 | 16,00 |

Khi đổi milliampere sang ampere, số vòng cuộn 2 là:

$$
\begin{aligned}
N_2 &= \frac{16{,}00-8{,}00}{0{,}00500-0{,}00200} \\
&\approx 2{,}67\times10^3.
\end{aligned}
$$

Dùng điểm thứ nhất để tìm cuộn 1:

$$
\begin{aligned}
N_1I_1 &= 8{,}00-N_2(0{,}00200) \\
&\approx 2{,}67\,\mathrm A, \\
N_1 &\approx 1{,}33\times10^3.
\end{aligned}
$$

Các số vòng là ước lượng từ đường thẳng trên đồ thị.

(c) Chọn trục $+z$ dọc chiều trường ban đầu. Khi dòng cuộn 2 đảo:

$$
\begin{aligned}
B_z &= \frac{\mu_0}{L} \left(N_1I_1-N_2I_2\right) \\
&= -3{,}35\times10^{-5}\,\mathrm T.
\end{aligned}
$$

Trường có độ lớn khoảng $3{,}4\times10^{-5}\,\mathrm T$ và hướng ngược trường ban đầu.
:::

::: exercise 28.73 •• DATA
Dùng teslameter dựa trên hiệu ứng Hall để đo trường gần một cáp đồng trụ dày, dài, mang dòng lớn không đổi. Đặt máy về không trước khi đo để loại trường Trái Đất. Đo độ lớn $B$ ở các khoảng cách $x$ tính từ mặt ngoài của cáp:

| $x$ (cm) | 2,0 | 4,0 | 6,0 | 8,0 | 10,0 |
| --- | --- | --- | --- | --- | --- |
| $B$ (mT) | 0,406 | 0,250 | 0,181 | 0,141 | 0,116 |

(a) Nếu nhớ trường dây tỉ lệ nghịch khoảng cách, có thể chờ đợi $Bx$ không đổi. Tính $Bx$ cho từng số đo, xét nó có không đổi không và giải thích.

(b) Vẽ đồ thị $x$ theo $1/B$ và giải thích vì sao gần là đường thẳng.

(c) Từ đồ thị, tìm dòng $I$ và bán kính $R$ của cáp.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $x$ đo từ mặt cáp, không phải từ trục. Các số đo $B$ ở bên ngoài cáp.

**Hướng đi:**

- Khoảng cách đến trục là $r=R+x$, nên phải dùng $B=\mu_0I/[2\pi(R+x)]$.
- Sắp xếp biểu thức thành quan hệ tuyến tính giữa $x$ và $1/B$ để đọc hệ số góc và tung độ gốc.
- Dùng toàn bộ các điểm để xác định một đường thẳng phù hợp với số đo.

(a) Đổi số đo sang SI trước khi nhân:

| $x$ (cm) | 2,0 | 4,0 | 6,0 | 8,0 | 10,0 |
| --- | --- | --- | --- | --- | --- |
| $Bx$ ($10^{-6}\,\mathrm{T\,m}$) | 8,12 | 10,0 | 10,86 | 11,28 | 11,60 |

Tích không cố định. Công thức tỉ lệ nghịch dùng khoảng cách $R+x$ đến trục. Chính $B(R+x)$ mới không đổi trong mô hình dây dài, còn:

$$
Bx=\frac{\mu_0I}{2\pi}\frac{x}{R+x}.
$$

(b) Sắp xếp công thức trường:

$$
x=\frac{\mu_0I}{2\pi}\frac1B-R.
$$

Vì thế đồ thị có hệ số góc dương và tung độ gốc âm.

![Đồ thị lời giải 28.73: Khoảng cách từ mặt cáp theo nghịch đảo độ lớn từ trường.](img/young-28/hinh-giai28-73-do-thi.svg)

(c) Đặt $s$ là hệ số góc và $c$ là tung độ gốc. Đường thẳng phù hợp với toàn bộ dữ liệu cho:

$$
\begin{aligned}
s &\approx 1{,}298\times10^{-5}\,\mathrm{T\,m}, \\
c &\approx -1{,}191\times10^{-2}\,\mathrm m.
\end{aligned}
$$

So sánh với biểu thức lý thuyết:

$$
\begin{aligned}
I &= \frac{2\pi s}{\mu_0} \\
&\approx 64{,}9\,\mathrm A, \\
R &= -c \\
&\approx 1{,}19\,\mathrm{cm}.
\end{aligned}
$$

Từ độ chính xác của số đo và đồ thị, có thể nêu kết quả khoảng $65\,\mathrm A$ và $1{,}2\,\mathrm{cm}$.
:::

::: exercise 28.74 ••• DATA
Hai thanh kim loại cứng, dài $0{,}50\,\mathrm m$, nằm song song trên bàn không ma sát. Hai đầu tương ứng được nối bằng hai lò xo dẫn điện giống nhau, rất nhẹ, có chiều dài tự nhiên $l_0$ và hằng số lực $k$ như Hình P28.74. Dòng $I$ chạy qua mạch gồm thanh và lò xo làm các lò xo giãn.

Khi $I=8{,}05\,\mathrm A$, mỗi lò xo giãn $x=0{,}40\,\mathrm{cm}$. Khi $I=13{,}1\,\mathrm A$, độ giãn là $0{,}80\,\mathrm{cm}$. Trong cả hai trường hợp, thanh dài hơn nhiều khoảng cách giữa hai thanh, nên có thể dùng công thức hai dây dài vô hạn. (a) Tìm $l_0,k$.

(b) Tìm độ giãn khi $I=12{,}0\,\mathrm A$.

(c) Tìm dòng cần để mỗi lò xo giãn $1{,}00\,\mathrm{cm}$.

![Hình P28.74: Hai thanh mang dòng ngược chiều được nối bởi hai lò xo dẫn điện.](img/young-28/hinh-p28-74.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Chiều dài thanh $L=0{,}50\,\mathrm m$, khoảng cách hai thanh $d=l_0+x$. Hai cặp số đo là $(8{,}05\,\mathrm A,0{,}0040\,\mathrm m)$ và $(13{,}1\,\mathrm A,0{,}0080\,\mathrm m)$.

**Hướng đi:**

- Dòng qua hai thanh ngược chiều nên tạo lực đẩy. Tính lực trên cả chiều dài $L$ bằng công thức hai dây song song.
- Mỗi thanh chịu lực kéo từ hai lò xo, mỗi lò xo có lực $kx$. Vì vậy lực phục hồi tổng là $2kx$.
- Hai số đo cung cấp hai phương trình để tìm hai ẩn $k,l_0$. Sau đó giải phương trình cân bằng cho độ giãn hoặc dòng.

Điều kiện cân bằng của một thanh là:

$$
\begin{aligned}
2kx &= \frac{\mu_0I^2L}{2\pi(l_0+x)}, \\
kx(l_0+x) &= \alpha I^2, \\
\alpha &= \frac{\mu_0L}{4\pi}.
\end{aligned}
$$

(a) Chia mỗi phương trình đo cho độ giãn tương ứng:

$$
\begin{aligned}
kl_0+kx_1 &= \frac{\alpha I_1^2}{x_1}, \\
kl_0+kx_2 &= \frac{\alpha I_2^2}{x_2}.
\end{aligned}
$$

Lấy phương trình thứ hai trừ phương trình thứ nhất:

$$
\begin{aligned}
k &= \frac{\alpha}{x_2-x_1} \left(\frac{I_2^2}{x_2}-\frac{I_1^2}{x_1}\right) \\
&= 6{,}56\times10^{-2}\,\mathrm{N/m}, \\
l_0 &= \frac{\alpha I_1^2}{kx_1}-x_1 \\
&= 8{,}34\times10^{-3}\,\mathrm m.
\end{aligned}
$$

Chiều dài tự nhiên khoảng $0{,}83\,\mathrm{cm}$, hằng số lực khoảng $0{,}066\,\mathrm{N/m}$.

(b) Viết cân bằng thành phương trình bậc hai:

$$
x^2+l_0x-\frac{\alpha I^2}{k}=0.
$$

Chọn nghiệm dương vì lò xo giãn:

$$
\begin{aligned}
x &= \frac{-l_0+\sqrt{l_0^2+4\alpha I^2/k}}2 \\
&= 7{,}10\times10^{-3}\,\mathrm m \\
&\approx 0{,}71\,\mathrm{cm}.
\end{aligned}
$$

(c) Khi $x=0{,}0100\,\mathrm m$, dòng điện là:

$$
I = \sqrt{\frac{kx(l_0+x)}{\alpha}} = 15{,}5\,\mathrm A.
$$
:::

::: exercise 28.75 ••• CP CALC
Plasma là khí chứa các hạt đã ion hóa. Khi plasma chuyển động, tương tác từ có thể tạo áp suất ép vào trong, gọi là hiệu ứng thắt dòng. Xét một ống plasma trụ bán kính $R$, dài $L$, chuyển động với vận tốc $\vec v$ dọc trục. Có $n$ ion trên một đơn vị thể tích, mỗi ion mang điện tích $q$.

(a) Tìm mật độ điện tích thể tích $\rho$ theo $n,q$.

(b) Bề dày của lớp bề mặt được lấy là $n^{-1/3}$. Tìm mật độ điện tích mặt $\sigma$.

(c) Với mật độ dòng $\vec J=\rho\vec v$, dùng Ampere tìm trường trên mặt trụ, gọi vector đơn vị theo chiều vòng quanh trụ là $\hat\phi$.

(d) Dải dòng bề mặt có bề rộng $R\,d\phi$. Tìm dòng vi phân qua dải.

(e) Tìm lực vi phân tác dụng lên dải do trường của dòng trong thể tích.

(f) Tích phân lực ép lên thành và chia diện tích thành trụ để tìm áp suất theo $n,q,R,v$.

(g) Tính áp suất khi $R=2{,}0\,\mathrm{cm}$, mật độ số ion là $8{,}0\times10^{16}\,\mathrm{ion/cm^3}$, $q=1{,}6\times10^{-19}\,\mathrm C$ và $v=20{,}0\,\mathrm{m/s}$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Plasma trụ có mật độ số $n$, điện tích mỗi ion $q$, dòng dọc trục và lớp bề mặt mỏng có bề dày $n^{-1/3}$. Cần tính riêng áp suất ép do tương tác từ.

**Hướng đi:**

- Nhân mật độ số với điện tích mỗi hạt để chuyển sang mật độ điện tích.
- Mật độ điện tích mặt bằng mật độ thể tích nhân bề dày lớp bề mặt.
- Dòng thể tích đối xứng trụ cho trường tiếp tuyến theo Ampere. Dòng trên dải bề mặt chịu lực $I\vec l\times\vec B$ hướng vào trục.
- Áp suất dùng độ lớn lực ép trên diện tích. Tổng vector của các lực hướng vào từ mọi phía bằng không, nhưng áp suất không bằng không.

(a) Mật độ điện tích thể tích là:

$$
\rho=nq.
$$

(b) Mật độ mặt của lớp bề mặt:

$$
\sigma = \rho n^{-1/3} = q n^{2/3}.
$$

(c) Chọn dòng dọc $+z$. Dòng trong tiết diện trụ bằng $J\pi R^2=nqv\pi R^2$. Do đó:

$$
\begin{aligned}
B_R(2\pi R) &= \mu_0nqv\pi R^2, \\
\vec B_R &= \frac{\mu_0nqvR}{2}\hat\phi.
\end{aligned}
$$

(d) Dòng mặt trên một đơn vị bề rộng là $\sigma v$. Nhân với bề rộng dải:

$$
dI_{\mathrm{face}}=\sigma vR\,d\phi.
$$

(e) Dải dài $L$ theo trục. Vì $\hat z\times\hat\phi=-\hat r$, lực hướng vào:

$$
d\vec F=-\sigma vRLB_R\,d\phi\,\hat r.
$$

(f) Cộng các độ lớn lực ép theo phương bán kính. Mỗi dải có diện tích $RL\,d\phi$, nên:

$$
\begin{aligned}
F_{\mathrm{comp}} &= \int_0^{2\pi}\sigma vRLB_R\,d\phi \\
&= 2\pi RL\sigma vB_R, \\
p &= \frac{F_{\mathrm{comp}}}{2\pi RL} \\
&= \sigma vB_R \\
&= \frac{\mu_0}{2}n^{5/3}q^2Rv^2.
\end{aligned}
$$

Ở đây $F_{\mathrm{comp}}$ là tổng độ lớn lực ép lên các phần thành trụ. Các hướng bán kính khác nhau triệt tiêu khi cộng vector lực, chứ không làm mất áp suất trên từng phần thành.

(g) Đổi mật độ sang đơn vị SI:

$$
\begin{aligned}
n &= 8{,}0\times10^{22}\,\mathrm{m^{-3}}, \\
R &= 0{,}020\,\mathrm m, \\
p &= 1{,}91\times10^{-5}\,\mathrm{Pa} \\
&\approx 1{,}9\times10^{-5}\,\mathrm{Pa}.
\end{aligned}
$$
:::
