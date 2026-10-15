## Luyện tập có hướng dẫn Chương 26

### Bài tập biến đổi gắn với ví dụ trọng tâm

#### Điện trở mắc nối tiếp và song song

Trước khi làm các bài sau, hãy ôn Ví dụ 26.1 và 26.2 trong Mục 26.1.

::: exercise VP26.2.1
Có ba điện trở $R_1=1{,}00\,\Omega$, $R_2=2{,}00\,\Omega$ và $R_3=4{,}00\,\Omega$. Tìm điện trở tương đương trong các cách mắc sau: (a) Hình 26.1a, (b) Hình 26.1b, (c) Hình 26.1c và (d) Hình 26.1d.

![Hình 26.1: Bốn cách mắc ba điện trở](img/young-26/hinh-26-01.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dùng cùng ba điện trở $1{,}00\,\Omega$, $2{,}00\,\Omega$ và $4{,}00\,\Omega$ cho bốn cấu hình ở Hình 26.1.

**Hướng đi:**

- Ở (a), cộng trực tiếp ba điện trở nối tiếp.
- Ở (b), cộng nghịch đảo của ba điện trở song song.
- Ở (c), rút gọn cặp $R_2$, $R_3$ song song rồi cộng nối tiếp với $R_1$.
- Ở (d), cộng nối tiếp $R_2$, $R_3$ rồi ghép nhóm ấy song song với $R_1$.

**Thực hiện:**

**(a) Ba điện trở nối tiếp.**

$$
\begin{aligned}
R_{\mathrm{eq}} &= R_1+R_2+R_3 \\
&= 1{,}00\,\Omega+2{,}00\,\Omega+4{,}00\,\Omega \\
&= 7{,}00\,\Omega.
\end{aligned}
$$

**(b) Ba điện trở song song.**

$$
\begin{aligned}
\frac{1}{R_{\mathrm{eq}}} &= \frac{1}{1{,}00\,\Omega} +\frac{1}{2{,}00\,\Omega} +\frac{1}{4{,}00\,\Omega} \\
&= 1{,}75\,\Omega^{-1}, \\
R_{\mathrm{eq}} &= 0{,}571\,\Omega.
\end{aligned}
$$

**(c) $R_1$ nối tiếp với cặp $R_2$, $R_3$ song song.**

$$
\begin{aligned}
R_{23} &= \frac{R_2R_3}{R_2+R_3} \\
&= \frac{(2{,}00\,\Omega)(4{,}00\,\Omega)}{2{,}00\,\Omega+4{,}00\,\Omega} \\
&= 1{,}33\,\Omega, \\
R_{\mathrm{eq}} &= R_1+R_{23} \\
&= 2{,}33\,\Omega.
\end{aligned}
$$

**(d) $R_1$ song song với cặp $R_2$, $R_3$ nối tiếp.**

$$
\begin{aligned}
R_{23} &= R_2+R_3 \\
&= 6{,}00\,\Omega, \\
R_{\mathrm{eq}} &= \frac{R_1R_{23}}{R_1+R_{23}} \\
&= \frac{(1{,}00)(6{,}00)}{1{,}00+6{,}00}\,\Omega \\
&= 0{,}857\,\Omega.
\end{aligned}
$$

**Đánh giá:** Kết quả ở (a) lớn hơn từng điện trở thành phần, còn kết quả ở (b) nhỏ hơn điện trở nhỏ nhất. Các cấu hình kết hợp cũng cho điện trở nằm giữa những giới hạn phù hợp của hai nhóm thành phần.
:::

::: exercise VP26.2.2
Có ba điện trở $R_1=4{,}00\,\Omega$, $R_2=5{,}00\,\Omega$ và $R_3=6{,}00\,\Omega$, mắc như Hình 26.1d. Nối hai cực của pin có suất điện động $24{,}0\,\mathrm V$ và điện trở trong không đáng kể vào hai điểm $a$, $b$. Tìm dòng điện qua (a) pin, (b) $R_1$, (c) $R_2$ và (d) $R_3$.

![Hình 26.1: Cấu hình song song giữa R₁ và cặp nối tiếp R₂, R₃](img/young-26/hinh-26-01.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nguồn lý tưởng $24{,}0\,\mathrm V$ đặt giữa $a$, $b$. Nhánh thứ nhất có $R_1=4{,}00\,\Omega$. Nhánh thứ hai có $R_2=5{,}00\,\Omega$ nối tiếp $R_3=6{,}00\,\Omega$.

**Hướng đi:**

- Tính điện trở và dòng của nhánh nối tiếp $R_2$, $R_3$.
- Vì hai nhánh mắc song song, mỗi nhánh chịu cùng hiệu điện thế $24{,}0\,\mathrm V$.
- Cộng dòng hai nhánh để tìm dòng qua pin.

**Thực hiện:** Điện trở nhánh thứ hai là:

$$
\begin{aligned}
R_{23} &= R_2+R_3 \\
&= 5{,}00\,\Omega+6{,}00\,\Omega \\
&= 11{,}00\,\Omega.
\end{aligned}
$$

Dòng qua nhánh $R_1$:

$$
\begin{aligned}
I_1 &= \frac{24{,}0\,\mathrm V}{4{,}00\,\Omega} \\
&= 6{,}00\,\mathrm A.
\end{aligned}
$$

Dòng qua nhánh nối tiếp:

$$
\begin{aligned}
I_{23} &= \frac{24{,}0\,\mathrm V}{11{,}00\,\Omega} \\
&= 2{,}18\,\mathrm A.
\end{aligned}
$$

Do $R_2$, $R_3$ nối tiếp, cùng dòng $2{,}18\,\mathrm A$ chạy qua mỗi điện trở. Dòng pin bằng tổng hai dòng nhánh:

$$
I_{\mathrm{pin}} = I_1+I_{23} = 8{,}18\,\mathrm A.
$$

**Đánh giá:** Quy tắc nút tại điểm phân nhánh cho $8{,}18\,\mathrm A=6{,}00\,\mathrm A+2{,}18\,\mathrm A$. Trong nhánh nối tiếp, dòng qua $R_2$ và $R_3$ bằng nhau.
:::

::: exercise VP26.2.3
Có ba điện trở $R_1=7{,}00\,\Omega$, $R_2=8{,}00\,\Omega$ và $R_3=9{,}00\,\Omega$, mắc như Hình 26.1b. Nối hai cực của pin có suất điện động $12{,}0\,\mathrm V$ và điện trở trong không đáng kể vào hai điểm $a$, $b$. Tìm (a) công suất đầu ra của pin và công suất đầu vào của (b) $R_1$, (c) $R_2$ và (d) $R_3$.

![Hình 26.1: Ba điện trở mắc song song](img/young-26/hinh-26-01.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Ba điện trở mắc song song với nguồn lý tưởng $12{,}0\,\mathrm V$. Vì vậy, hiệu điện thế trên từng điện trở bằng $12{,}0\,\mathrm V$.

**Hướng đi:**

- Tính công suất từng nhánh bằng $P=V^2/R$.
- Cộng công suất nhánh để tìm công suất pin cấp ra.

**Thực hiện:**

$$
\begin{aligned}
P_1 &= \frac{(12{,}0\,\mathrm V)^2}{7{,}00\,\Omega} \\
&= 20{,}6\,\mathrm W, \\
P_2 &= \frac{(12{,}0\,\mathrm V)^2}{8{,}00\,\Omega} \\
&= 18{,}0\,\mathrm W, \\
P_3 &= \frac{(12{,}0\,\mathrm V)^2}{9{,}00\,\Omega} \\
&= 16{,}0\,\mathrm W.
\end{aligned}
$$

Do đó:

$$
P_{\mathrm{pin}} = P_1+P_2+P_3 = 54{,}6\,\mathrm W.
$$

**Đánh giá:** Công suất ba nhánh cộng lại bằng công suất nguồn cấp. Nhánh có điện trở lớn nhất nhận công suất nhỏ nhất khi hiệu điện thế trên các nhánh bằng nhau.
:::

::: exercise VP26.2.4
Có ba điện trở $R_1=5{,}00\,\Omega$, $R_2=6{,}00\,\Omega$ và $R_3=7{,}00\,\Omega$, mắc như Hình 26.1c. Nối hai cực của pin có suất điện động $9{,}00\,\mathrm V$ và điện trở trong không đáng kể vào hai điểm $a$, $b$. Tìm (a) công suất đầu ra của pin và công suất đầu vào của (b) $R_1$, (c) $R_2$ và (d) $R_3$.

![Hình 26.1: Điện trở R₁ nối tiếp với cặp song song R₂, R₃](img/young-26/hinh-26-01.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nhánh $R_1$ nối tiếp với nhóm song song $R_2$, $R_3$. Nguồn đặt $9{,}00\,\mathrm V$ lên cả mạng.

**Hướng đi:**

- Rút gọn cặp song song để tìm dòng tổng, cũng là dòng qua $R_1$.
- Tìm hiệu điện thế trên nhóm song song.
- Dùng $P=I^2R$ cho $R_1$ và $P=V^2/R$ cho hai nhánh song song.

**Thực hiện:** Điện trở tương đương của cặp song song và toàn mạng là:

$$
\begin{aligned}
R_{23} &= \frac{R_2R_3}{R_2+R_3} \\
&= \frac{(6{,}00\,\Omega)(7{,}00\,\Omega)}{6{,}00\,\Omega+7{,}00\,\Omega} \\
&= \frac{42}{13}\,\Omega, \\
R_{\mathrm{eq}} &= R_1+R_{23} \\
&= \frac{107}{13}\,\Omega.
\end{aligned}
$$

Dòng qua pin và $R_1$:

$$
\begin{aligned}
I &= \frac{9{,}00\,\mathrm V}{R_{\mathrm{eq}}} \\
&= \frac{117}{107}\,\mathrm A \\
&= 1{,}09\,\mathrm A.
\end{aligned}
$$

Công suất đầu ra của pin:

$$
\begin{aligned}
P_{\mathrm{pin}} &= VI \\
&= (9{,}00\,\mathrm V)\left(\frac{117}{107}\,\mathrm A\right) \\
&= 9{,}84\,\mathrm W.
\end{aligned}
$$

Hiệu điện thế trên cặp song song:

$$
\begin{aligned}
V_{23} &= I R_{23} \\
&= \frac{378}{107}\,\mathrm V \\
&= 3{,}53\,\mathrm V.
\end{aligned}
$$

Công suất trên từng điện trở:

$$
\begin{aligned}
P_1 &= I^2R_1=5{,}98\,\mathrm W, \\
P_2 &= \frac{V_{23}^2}{R_2}=2{,}08\,\mathrm W, \\
P_3 &= \frac{V_{23}^2}{R_3}=1{,}78\,\mathrm W.
\end{aligned}
$$

**Đánh giá:** Tổng công suất ba điện trở là $9{,}84\,\mathrm W$, bằng công suất đầu ra của pin. Hai nhánh song song cùng có hiệu điện thế $3{,}53\,\mathrm V$.
:::

#### Quy tắc Kirchhoff

Trước khi làm các bài sau, hãy ôn Ví dụ 26.3–26.7 trong Mục 26.2.

::: exercise VP26.7.1
Trong mạch ở Hình 26.10a, đảo pin $4\,\mathrm V$ sao cho cực dương nằm bên phải thay vì bên trái. Tìm (a) dòng điện trong mạch, (b) hiệu điện thế $V_{ab}$ và (c) công suất đầu ra của suất điện động mỗi pin.

![Hình 26.10: Mạch một vòng có hai pin](img/young-26/hinh-26-10.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Pin $4\,\mathrm V$ được đảo cực. Khi đi theo chiều dòng điện trong mạch, cả hai suất điện động đều làm tăng điện thế.

**Hướng đi:**

- Cộng đại số hai suất điện động theo chiều dòng điện mới.
- Cộng điện trở $2\,\Omega$, $3\,\Omega$, $4\,\Omega$ và $7\,\Omega$ trong vòng.
- Dùng quy tắc vòng để tìm dòng. Sau đó cộng các độ biến thiên điện thế từ $b$ đến $a$.

**Thực hiện:** Tổng suất điện động đẩy dòng theo chiều đã chọn là:

$$
\begin{aligned}
\mathcal E_{\mathrm{tot}} &= 12\,\mathrm V+4\,\mathrm V \\
&= 16\,\mathrm V.
\end{aligned}
$$

Tổng điện trở của vòng:

$$
\begin{aligned}
R_{\mathrm{tot}} &= 2+3+4+7 \\
&= 2\,\Omega+3\,\Omega+4\,\Omega+7\,\Omega \\
&= 16\,\Omega.
\end{aligned}
$$

Vì vậy dòng điện là:

$$
\begin{aligned}
I &= \frac{\mathcal E_{\mathrm{tot}}}{R_{\mathrm{tot}}} \\
&= 1{,}00\,\mathrm A.
\end{aligned}
$$

Để tìm $V_{ab}=V_a-V_b$, đi từ $b$ qua nguồn $12\,\mathrm V$, điện trở trong $2\,\Omega$ và điện trở $3\,\Omega$ đến $a$:

$$
\begin{aligned}
V_{ab} &= 12\,\mathrm V-(1{,}00\,\mathrm A)(2\,\Omega) -(1{,}00\,\mathrm A)(3\,\Omega) \\
&= 7{,}00\,\mathrm V.
\end{aligned}
$$

Dòng đi qua cả hai suất điện động từ cực âm đến cực dương, nên cả hai đều cấp năng lượng:

$$
\begin{aligned}
P_{12\,\mathrm V} &= (12\,\mathrm V)(1{,}00\,\mathrm A) \\
&= 12{,}0\,\mathrm W, \\
P_{4\,\mathrm V} &= (4\,\mathrm V)(1{,}00\,\mathrm A) \\
&= 4{,}00\,\mathrm W.
\end{aligned}
$$

**Đánh giá:** Tổng công suất hai nguồn cấp là $16{,}0\,\mathrm W$. Bốn điện trở tỏa nhiệt tổng cộng $(1{,}00\,\mathrm A)^2(16\,\Omega)=16{,}0\,\mathrm W$.
:::

::: exercise VP26.7.2
Hình 26.6a biểu diễn hai pin có suất điện động $\mathcal E_1$, $\mathcal E_2$ mắc với điện trở $R$. Dòng $I_1$ đi qua suất điện động $\mathcal E_1$ từ điểm $c$ đến điểm $a$. Dòng $I_2$ đi qua suất điện động $\mathcal E_2$ từ điểm $b$ đến điểm $a$. Cho $\mathcal E_1=8{,}00\,\mathrm V$, $\mathcal E_2=9{,}00\,\mathrm V$, $R=5{,}00\,\Omega$, $I_1=0{,}200\,\mathrm A$ và $I_2=1{,}35\,\mathrm A$. Tìm (a) hiệu điện thế $V_{ab}$, (b) điện trở trong $r_1$ và (c) điện trở trong $r_2$.

![Hình 26.6a: Hai pin có điện trở trong cấp dòng cho điện trở ngoài](img/young-26/hinh-26-06.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai dòng điện $I_1$, $I_2$ đi vào nút $a$. Điện trở $R$ nối giữa $a$ và $b$.

**Hướng đi:**

- Áp dụng quy tắc nút tại $a$ để tìm dòng qua $R$.
- Dùng định luật Ôm trên $R$ để tìm $V_{ab}$.
- Ở mỗi pin, hiệu điện thế hai cực bằng suất điện động trừ sụt áp trên điện trở trong.

**Thực hiện:** Dòng qua $R$ bằng tổng dòng đi vào nút $a$:

$$
I_R = I_1+I_2 = 1{,}55\,\mathrm A.
$$

Điện áp trên $R$:

$$
\begin{aligned}
V_{ab} &= I_RR \\
&= (1{,}55\,\mathrm A)(5{,}00\,\Omega) \\
&= 7{,}75\,\mathrm V.
\end{aligned}
$$

Với pin thứ nhất và thứ hai, lần lượt:

$$
\begin{aligned}
V_{ab} &= \mathcal E_1-I_1r_1, \\
r_1 &= \frac{\mathcal E_1-V_{ab}}{I_1} \\
&= \frac{8{,}00\,\mathrm V-7{,}75\,\mathrm V}{0{,}200\,\mathrm A} \\
&= 1{,}25\,\Omega, \\
V_{ab} &= \mathcal E_2-I_2r_2, \\
r_2 &= \frac{\mathcal E_2-V_{ab}}{I_2} \\
&= \frac{9{,}00\,\mathrm V-7{,}75\,\mathrm V}{1{,}35\,\mathrm A} \\
&= 0{,}926\,\Omega.
\end{aligned}
$$

**Đánh giá:** Từ pin thứ nhất, điện áp hai cực là $8{,}00-(0{,}200)(1{,}25)=7{,}75\,\mathrm V$. Từ pin thứ hai cũng được $9{,}00-(1{,}35)(0{,}926)\approx7{,}75\,\mathrm V$. Hai nhánh cùng nối vào $a$, $b$ nên phải cho cùng hiệu điện thế.
:::

::: exercise VP26.7.3
Trong mạch ở Hình 26.12, thay điện trở $2\,\Omega$ giữa hai điểm $b$ và $d$ bằng điện trở $3\,\Omega$. Tìm công suất tỏa nhiệt ở (a) điện trở $1\,\Omega$ giữa $c$ và $a$, (b) điện trở $1\,\Omega$ giữa $c$ và $b$, (c) điện trở $1\,\Omega$ giữa $a$ và $b$, (d) điện trở $1\,\Omega$ giữa $a$ và $d$ và (e) điện trở $3\,\Omega$ giữa $b$ và $d$. Làm tròn mỗi kết quả đến ba chữ số có nghĩa.

![Hình 26.12: Mạng cầu gồm bốn điện trở 1 Ω và một điện trở ở nhánh dưới phải](img/young-26/hinh-26-12.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nguồn $13\,\mathrm V$ mắc vào cầu. Bốn nhánh giữ điện trở $1\,\Omega$, còn nhánh $b$–$d$ tăng từ $2\,\Omega$ lên $3\,\Omega$.

**Hướng đi:**

- Dùng quy tắc nút để biểu diễn năm dòng nhánh theo $I_1$, $I_2$, $I_3$ như Hình 26.12.
- Lập ba phương trình vòng. Giữ dấu dòng đã chọn, kể cả khi kết quả dòng có thể âm.
- Tính công suất mỗi điện trở bằng $P=I^2R$.

**Thực hiện:** Với các chiều dòng trong hình, ba phương trình vòng là:

$$
\begin{aligned}
&13\,\mathrm V - I_1(1\,\Omega) - (I_1-I_3)(1\,\Omega) = 0, \\
&-I_2(1\,\Omega) - (I_2+I_3)(3\,\Omega) + 13\,\mathrm V = 0, \\
&-I_1(1\,\Omega) - I_3(1\,\Omega) + I_2(1\,\Omega) = 0.
\end{aligned}
$$

Từ vòng giữa, $I_2=I_1+I_3$. Hai phương trình còn lại rút gọn thành:

$$
\begin{aligned}
13\,\mathrm V &= I_1(2\,\Omega)-I_3(1\,\Omega), \\
13\,\mathrm V &= I_1(4\,\Omega)+I_3(7\,\Omega).
\end{aligned}
$$

Giải hệ:

$$
\begin{aligned}
I_1 &= \frac{52}{9}\,\mathrm A=5{,}78\,\mathrm A, \\
I_2 &= \frac{13}{3}\,\mathrm A=4{,}33\,\mathrm A, \\
I_3 &= -\frac{13}{9}\,\mathrm A=-1{,}44\,\mathrm A.
\end{aligned}
$$

Dấu âm cho biết dòng giữa thực chạy từ $b$ đến $a$. Năm dòng điện qua các điện trở theo thứ tự đề bài là:

$$
\begin{aligned}
I_{ca} &= I_1=\frac{52}{9}\,\mathrm A, \\
I_{cb} &= I_2=\frac{13}{3}\,\mathrm A, \\
I_{ab} &= I_3=-\frac{13}{9}\,\mathrm A, \\
I_{ad} &= I_1-I_3=\frac{65}{9}\,\mathrm A, \\
I_{bd} &= I_2+I_3=\frac{26}{9}\,\mathrm A.
\end{aligned}
$$

Suy ra công suất tỏa nhiệt:

$$
\begin{aligned}
P_{ca} &= I_{ca}^2(1\,\Omega)=33{,}4\,\mathrm W, \\
P_{cb} &= I_{cb}^2(1\,\Omega)=18{,}8\,\mathrm W, \\
P_{ab} &= I_{ab}^2(1\,\Omega)=2{,}09\,\mathrm W, \\
P_{ad} &= I_{ad}^2(1\,\Omega)=52{,}2\,\mathrm W, \\
P_{bd} &= I_{bd}^2(3\,\Omega)=25{,}0\,\mathrm W.
\end{aligned}
$$

**Đánh giá:** Tổng dòng từ nguồn là $I_1+I_2=91/9\,\mathrm A$. Công suất nguồn cấp là $13(91/9)=131{,}4\,\mathrm W$, bằng tổng công suất tỏa nhiệt ở năm điện trở.
:::

::: exercise VP26.7.4
Trong mạch ở Hình 26.9a, cho $r_1=r_2=0$ (điện trở trong rất nhỏ) và $R_1=R_2=R_3=R$. Tìm (a) $I_1$, (b) $I_2$ và (c) $I_3$.

![Hình 26.9a: Hai nguồn cấp điện cho ba nhánh điện trở](img/young-26/hinh-26-09.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai nguồn lý tưởng có suất điện động $\mathcal E_1$, $\mathcal E_2$ cùng nối vào nút trên. Ba điện trở đều bằng $R$.

**Hướng đi:**

- Chọn nút dưới $a$ làm điện thế $0$.
- Vì các nguồn lý tưởng nối vào nút trên, dùng cực tính hình vẽ để viết điện thế hai nút ngoài theo điện thế nút trên.
- Tính ba dòng theo các hiệu điện thế trên điện trở. Sau đó kiểm tra quy tắc nút tại hai nút giữa.

**Thực hiện:** Gọi điện thế nút trên là $V$. Cực dương của cả hai nguồn hướng về nút trên, nên điện thế các nút trái và phải lần lượt là $V-\mathcal E_1$ và $V-\mathcal E_2$. Dòng điện theo chiều mũi tên trong hình:

$$
\begin{aligned}
I_1 &= \frac{V-\mathcal E_1}{R}, \\
I_2 &= \frac{V-\mathcal E_2}{R}, \\
I_3 &= \frac{0-V}{R}.
\end{aligned}
$$

Tại nút trên, $I_3=I_1+I_2$. Thay các biểu thức trên:

$$
\begin{aligned}
-V &= (V-\mathcal E_1)+(V-\mathcal E_2), \\
V &= \frac{\mathcal E_1+\mathcal E_2}{3}.
\end{aligned}
$$

Do đó:

$$
\begin{aligned}
I_1 &= \frac{\mathcal E_2-2\mathcal E_1}{3R}, \\
I_2 &= \frac{\mathcal E_1-2\mathcal E_2}{3R}, \\
I_3 &= -\frac{\mathcal E_1+\mathcal E_2}{3R}.
\end{aligned}
$$

**Đánh giá:** Thay ba biểu thức vào $I_1+I_2=I_3$ cho hai vế cùng bằng $-(\mathcal E_1+\mathcal E_2)/(3R)$. Nếu một kết quả âm, dòng thực trong nhánh ấy ngược với mũi tên đã chọn.
:::

#### Mạch RC

Trước khi làm các bài sau, hãy ôn Ví dụ 26.12 và 26.13 trong Mục 26.4.

::: exercise VP26.13.1
Nối điện trở $10{,}0\,\mathrm{M}\Omega$, tụ điện $3{,}20\,\mu\mathrm F$ và pin có suất điện động $9{,}00\,\mathrm V$ thành mạch nối tiếp. Trước khi đóng khóa tại $t=0$, tụ chưa tích điện. Tìm (a) điện tích cuối trên tụ, (b) dòng điện ban đầu, (c) hằng số thời gian, (d) phần điện tích cuối đã tích được trên tụ tại $t=18{,}0\,\mathrm s$ và (e) phần dòng điện ban đầu còn lại tại thời điểm đó.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mạch nạp có $R=10{,}0\,\mathrm{M}\Omega$, $C=3{,}20\,\mu\mathrm F$ và $\mathcal E=9{,}00\,\mathrm V$.

**Hướng đi:**

- Điện tích cuối là $Q_f=C\mathcal E$.
- Dòng ban đầu khi tụ chưa tích điện là $I_0=\mathcal E/R$.
- Hằng số thời gian là $\tau=RC$. Trong quá trình nạp, $q/Q_f=1-e^{-t/\tau}$ và $i/I_0=e^{-t/\tau}$.

**Thực hiện:**

$$
\begin{aligned}
Q_f &= (3{,}20\,\mu\mathrm F)(9{,}00\,\mathrm V) \\
&= 28{,}8\,\mu\mathrm C, \\
I_0 &= \frac{9{,}00\,\mathrm V}{10{,}0\,\mathrm{M}\Omega} \\
&= 0{,}900\,\mu\mathrm A, \\
\tau &= (10{,}0\,\mathrm{M}\Omega)(3{,}20\,\mu\mathrm F) \\
&= 32{,}0\,\mathrm s.
\end{aligned}
$$

Tại $18{,}0\,\mathrm s$:

$$
\begin{aligned}
\frac{q}{Q_f} &= 1-e^{-18{,}0/32{,}0} \\
&= 0{,}430, \\
\frac{i}{I_0} &= e^{-18{,}0/32{,}0} \\
&= 0{,}570.
\end{aligned}
$$

**Đánh giá:** Hai phần ở (d) và (e) cộng lại bằng $1$, đúng vì điện tích nạp được bằng phần hụt của dòng ban đầu theo nghiệm hàm mũ của mạch RC.
:::

::: exercise VP26.13.2
Tụ điện $2{,}20\,\mu\mathrm F$ ban đầu mang điện tích $4{,}20\,\mu\mathrm C$. Nối tụ nối tiếp với điện trở $4{,}00\,\mathrm{M}\Omega$ và một khóa đang mở. Lấy $t=0$ là thời điểm đóng khóa. (a) Sau bao lâu điện tích của tụ còn $1{,}20\,\mu\mathrm C$? (b) Khi đó dòng điện trong mạch bằng bao nhiêu?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tụ phóng điện qua điện trở. Điện tích giảm từ $Q_0=4{,}20\,\mu\mathrm C$ xuống $q=1{,}20\,\mu\mathrm C$.

**Hướng đi:**

- Tính hằng số thời gian $\tau=RC$.
- Dùng $q=Q_0e^{-t/\tau}$ để tìm $t$.
- Độ lớn dòng điện khi ấy bằng $q/\tau$.

**Thực hiện:**

$$
\begin{aligned}
\tau &= (4{,}00\,\mathrm{M}\Omega)(2{,}20\,\mu\mathrm F) \\
&= 8{,}80\,\mathrm s.
\end{aligned}
$$

Từ phương trình phóng điện:

$$
\begin{aligned}
t &= \tau\ln\left(\frac{Q_0}{q}\right) \\
&= (8{,}80\,\mathrm s)\ln\left(\frac{4{,}20}{1{,}20}\right) \\
&= 11{,}0\,\mathrm s.
\end{aligned}
$$

Dòng điện khi điện tích còn $1{,}20\,\mu\mathrm C$:

$$
\begin{aligned}
|i| &= \frac{q}{\tau} \\
&= \frac{1{,}20\,\mu\mathrm C}{8{,}80\,\mathrm s} \\
&= 0{,}136\,\mu\mathrm A.
\end{aligned}
$$

**Đánh giá:** Điện tích giảm theo $e^{-t/\tau}$, còn độ lớn dòng điện giảm theo cùng hệ số. Tại $11{,}0\,\mathrm s$, tỉ số điện tích $q/Q_0=1{,}20/4{,}20$ cũng bằng tỉ số dòng điện hiện tại với dòng ban đầu.
:::

::: exercise VP26.13.3
Nối một điện trở chưa biết nối tiếp với tụ điện $8{,}00\,\mu\mathrm F$ và khóa đang mở. Trước khi đóng khóa tại $t=0$, tụ có điện tích $5{,}50\,\mu\mathrm C$. Tại $t=17{,}0\,\mathrm s$, điện tích giảm còn $1{,}10\,\mu\mathrm C$. Tìm (a) điện trở, (b) dòng điện ngay sau khi đóng khóa và (c) dòng điện tại $t=17{,}0\,\mathrm s$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tụ phóng điện từ $Q_0=5{,}50\,\mu\mathrm C$ xuống $q=1{,}10\,\mu\mathrm C$ trong $17{,}0\,\mathrm s$. Điện dung là $8{,}00\,\mu\mathrm F$.

**Hướng đi:**

- Từ $q/Q_0=e^{-t/\tau}$, suy ra $\tau=t/\ln(Q_0/q)$.
- Tính $R=\tau/C$.
- Dùng $i_0=Q_0/\tau$ và $i(t)=q/\tau$ cho độ lớn dòng điện ở hai thời điểm.

**Thực hiện:** Hằng số thời gian:

$$
\begin{aligned}
\tau &= \frac{17{,}0\,\mathrm s}{\ln(5{,}50/1{,}10)} \\
&= 10{,}6\,\mathrm s.
\end{aligned}
$$

Điện trở:

$$
\begin{aligned}
R &= \frac{\tau}{C} \\
&= \frac{10{,}6\,\mathrm s}{8{,}00\,\mu\mathrm F} \\
&= 1{,}32\,\mathrm{M}\Omega.
\end{aligned}
$$

Dòng ban đầu và dòng tại $17{,}0\,\mathrm s$:

$$
\begin{aligned}
|i_0| &= \frac{5{,}50\,\mu\mathrm C}{10{,}6\,\mathrm s} \\
&= 0{,}521\,\mu\mathrm A, \\
|i(17{,}0\,\mathrm s)| &= \frac{1{,}10\,\mu\mathrm C}{10{,}6\,\mathrm s} \\
&= 0{,}104\,\mu\mathrm A.
\end{aligned}
$$

**Đánh giá:** Điện tích còn lại bằng một phần năm ban đầu. Dòng điện tại $17{,}0\,\mathrm s$ cũng bằng một phần năm dòng ban đầu.
:::

::: exercise VP26.13.4
Nối tụ điện $6{,}40\,\mu\mathrm F$ chưa tích điện nối tiếp với điện trở $5{,}00\,\mathrm{M}\Omega$ và pin có suất điện động $12{,}0\,\mathrm V$. Sau khi tụ nạp trong $51{,}0\,\mathrm s$, ngắt tụ khỏi mạch thứ nhất rồi nối tụ nối tiếp với một khóa đang mở và điện trở $6{,}00\,\mathrm{M}\Omega$. Tìm điện tích của tụ (a) ngay khi ngắt khỏi mạch thứ nhất và (b) sau khi khóa của mạch thứ hai đã đóng được $70{,}0\,\mathrm s$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tụ nạp qua $R_1=5{,}00\,\mathrm{M}\Omega$ trong $51{,}0\,\mathrm s$, rồi phóng qua $R_2=6{,}00\,\mathrm{M}\Omega$ trong $70{,}0\,\mathrm s$. Điện dung là $6{,}40\,\mu\mathrm F$.

**Hướng đi:**

- Tính $\tau_1=R_1C$ và điện tích cuối $Q_f=C\mathcal E$ của giai đoạn nạp.
- Dùng phương trình nạp để tìm điện tích ngay khi ngắt mạch thứ nhất.
- Điện tích đó trở thành điện tích ban đầu của giai đoạn phóng qua $R_2$.

**Thực hiện:** Hằng số thời gian khi nạp và điện tích cuối:

$$
\begin{aligned}
\tau_1 &= (5{,}00\,\mathrm{M}\Omega)(6{,}40\,\mu\mathrm F) \\
&= 32{,}0\,\mathrm s, \\
Q_f &= (6{,}40\,\mu\mathrm F)(12{,}0\,\mathrm V) \\
&= 76{,}8\,\mu\mathrm C.
\end{aligned}
$$

Sau $51{,}0\,\mathrm s$:

$$
\begin{aligned}
q_1 &= Q_f\left(1-e^{-51{,}0/\tau_1}\right) \\
&= 61{,}2\,\mu\mathrm C.
\end{aligned}
$$

Khi phóng điện qua điện trở thứ hai:

$$
\begin{aligned}
\tau_2 &= (6{,}00\,\mathrm{M}\Omega)(6{,}40\,\mu\mathrm F) \\
&= 38{,}4\,\mathrm s, \\
q_2 &= q_1e^{-70{,}0/\tau_2} \\
&= 9{,}89\,\mu\mathrm C.
\end{aligned}
$$

**Đánh giá:** Điện tích sau khi đóng khóa lần hai phải nhỏ hơn điện tích lúc ngắt khỏi mạch nạp, và $9{,}89\,\mu\mathrm C<61{,}2\,\mu\mathrm C$.
:::

Để xem bài tập được giao và các tài liệu học tập khác, truy cập Mastering Physics.

### Bài cầu nối: Hai tụ điện và hai điện trở

::: exercise Bài cầu nối 26.27
Hai tụ điện $2{,}40\,\mu\mathrm F$ và $3{,}60\,\mu\mathrm F$ mắc nối tiếp. (a) Đặt điện tích $5{,}20\,\mu\mathrm C$ lên mỗi tụ. Tính năng lượng dự trữ trong hai tụ. (b) Nối điện trở $655\,\Omega$ vào hai đầu của tổ hợp tụ, đồng thời mắc vôn kế có điện trở $4{,}58\times10^4\,\Omega$ song song với điện trở đó như Hình 26.27. Tốc độ biến thiên năng lượng dự trữ của các tụ ngay sau khi nối mạch là bao nhiêu? (c) Sau bao lâu năng lượng dự trữ giảm còn $1/e$ giá trị ban đầu? (d) Tại thời điểm tìm được ở câu (c), tốc độ biến thiên năng lượng dự trữ bằng bao nhiêu?

![Hình 26.27: Hai tụ đang tích điện phóng qua điện trở và vôn kế](img/young-26/hinh-26-27.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai tụ mắc nối tiếp có cùng điện tích đầu. Khi phóng, điện trở $655\,\Omega$ và điện trở vôn kế mắc song song cùng nhận điện áp của tổ hợp tụ.

**Hướng đi:**

- Dùng điện dung tương đương của hai tụ nối tiếp vì chúng có cùng điện tích. Cộng hai năng lượng hoặc tính từ điện dung tương đương để tìm năng lượng đầu.
- Ghép song song hai điện trở vì chúng nối cùng hai đầu tổ hợp tụ. Điện trở tương đương quyết định hằng số thời gian của quá trình phóng.
- Dùng $U=Q^2/(2C)$ và điện tích giảm theo hàm mũ để tìm thời gian năng lượng còn $1/e$. Dùng $dU/dt=-V^2/R$ để tìm tốc độ biến thiên năng lượng.

#### Nhận diện và bố trí

Hai tụ mắc nối tiếp có thể thay bằng điện dung tương đương $C_{\mathrm{eq}}$. Điện trở $655\,\Omega$ và vôn kế mắc song song, nên cũng được thay bằng một điện trở tương đương $R_{\mathrm{eq}}$. Khi đóng mạch, hai tụ phóng điện qua tổ hợp điện trở này.

1. Để tìm $C_{\mathrm{eq}}$, dùng quy tắc tụ điện mắc nối tiếp. Để tìm $R_{\mathrm{eq}}$, dùng quy tắc điện trở mắc song song.
2. Ở câu (a), dùng phương trình năng lượng của tụ điện (24.9).
3. Ở các câu (b), (c), (d), dùng phương trình năng lượng cùng các phương trình điện tích và dòng điện theo thời gian (26.16), (26.17). Tốc độ mất năng lượng của tụ bằng tốc độ tỏa nhiệt trên các điện trở.

#### Thực hiện

**Bước 4. Tìm năng lượng ban đầu.** Vì điện tích trên mỗi tụ là $Q_0=5{,}20\,\mu\mathrm C$, điện dung tương đương của cặp là:

$$
\begin{aligned}
\frac{1}{C_{\mathrm{eq}}} &= \frac{1}{2{,}40\,\mu\mathrm F} +\frac{1}{3{,}60\,\mu\mathrm F} \\
&= \frac{1}{1{,}44\,\mu\mathrm F}, \\
C_{\mathrm{eq}} &= 1{,}44\,\mu\mathrm F.
\end{aligned}
$$

Năng lượng tổng cộng của hai tụ:

$$
\begin{aligned}
U_0 &= \frac{Q_0^2}{2C_{\mathrm{eq}}} \\
&= \frac{(5{,}20\,\mu\mathrm C)^2}{2(1{,}44\,\mu\mathrm F)} \\
&= 9{,}39\,\mu\mathrm J.
\end{aligned}
$$

**Bước 5. Tìm tốc độ biến thiên năng lượng lúc $t=0$.** Điện trở tương đương của vôn kế và điện trở $655\,\Omega$ là:

$$
\begin{aligned}
\frac{1}{R_{\mathrm{eq}}} &= \frac{1}{655\,\Omega} +\frac{1}{4{,}58\times10^4\,\Omega}, \\
R_{\mathrm{eq}} &= 645{,}8\,\Omega.
\end{aligned}
$$

Ban đầu, hiệu điện thế hai đầu tổ hợp tụ là:

$$
\begin{aligned}
V_0 &= \frac{Q_0}{C_{\mathrm{eq}}} \\
&= \frac{5{,}20\,\mu\mathrm C}{1{,}44\,\mu\mathrm F} \\
&= 3{,}611\,\mathrm V.
\end{aligned}
$$

Năng lượng giảm với tốc độ bằng âm công suất tỏa nhiệt trên hai điện trở:

$$
\begin{aligned}
\left.\frac{dU}{dt}\right|_{t = 0} &= -\frac{V_0^2}{R_{\mathrm{eq}}} \\
&= -20{,}2\,\mathrm{mW}.
\end{aligned}
$$

Dấu âm cho biết năng lượng dự trữ của tụ đang giảm.

**Bước 6. Tìm thời điểm năng lượng còn $1/e$ giá trị đầu.** Điện tích giảm theo $Q(t)=Q_0e^{-t/\tau}$, trong đó $\tau=R_{\mathrm{eq}}C_{\mathrm{eq}}$. Vì $U=Q^2/(2C_{\mathrm{eq}})$, năng lượng giảm theo $U(t)=U_0e^{-2t/\tau}$. Do đó:

$$
\begin{aligned}
\tau &= R_{\mathrm{eq}}C_{\mathrm{eq}} \\
&= (645{,}8\,\Omega)(1{,}44\,\mu\mathrm F) \\
&= 0{,}9299\,\mathrm{ms}, \\
U(t) &= \frac{U_0}{e}, \\
t &= \frac{\tau}{2} \\
&= 0{,}465\,\mathrm{ms}.
\end{aligned}
$$

**Bước 7. Tìm tốc độ biến thiên năng lượng tại thời điểm đó.** Điện áp trên các điện trở đã giảm theo $e^{-t/\tau}$, nên công suất tiêu tán lúc $t=\tau/2$ bằng công suất ban đầu chia cho $e$:

$$
\begin{aligned}
\left.\frac{dU}{dt}\right|_{t = \tau/2} &= -\frac{V_0^2}{eR_{\mathrm{eq}}} \\
&= -7{,}43\,\mathrm{mW}.
\end{aligned}
$$

#### Đánh giá

**Bước 8. Kiểm tra bằng đạo hàm năng lượng.** Từ $U=Q^2/(2C_{\mathrm{eq}})$:

$$
\begin{aligned}
\frac{dU}{dt} &= \frac{Q}{C_{\mathrm{eq}}}\frac{dQ}{dt} \\
&= -\frac{Q^2}{C_{\mathrm{eq}}\tau} \\
&= -\frac{2U}{\tau}.
\end{aligned}
$$

Tại $t=\tau/2$, $U=U_0/e$, nên:

$$
\frac{dU}{dt} = -\frac{2U_0}{e\tau} = -7{,}43\,\mathrm{mW},
$$

đúng bằng kết quả tính từ công suất tiêu tán. Ban đầu cũng có $-2U_0/\tau=-20{,}2\,\mathrm{mW}$, khớp câu (b).
:::
