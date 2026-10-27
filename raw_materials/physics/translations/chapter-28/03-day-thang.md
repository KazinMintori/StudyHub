## 28.3 Từ trường của dây dẫn thẳng mang dòng điện

Dây dẫn thẳng xuất hiện trong hầu hết thiết bị điện. Ta dùng định luật Biot–Savart để tìm từ trường do một đoạn dây hữu hạn tạo ra, rồi xét giới hạn dây dài. Phép tính này cho biết cả độ lớn lẫn hình dạng đường sức từ quanh dây.

### Dây thẳng hữu hạn

Xét dây dẫn thẳng nằm dọc trục $y$, dài $2a$, mang dòng điện $I$. Điểm đo $P$ nằm trên đường trung trực của dây, cách dây một khoảng $x$. Một phần tử có độ dài $dy$ tại tọa độ $y$ có véc-tơ $d\vec\ell=dy\,\hat\jmath$. Khoảng cách từ phần tử đến $P$ là $r=\sqrt{x^2+y^2}$.

![Hình học tính từ trường tại điểm P do từng phần tử của dây dẫn thẳng hữu hạn](../img/young-28/hinh-28-05.png)

Hình 28.5: Véc-tơ từ trường do mỗi phần tử dây đều hướng vào mặt phẳng trang giấy tại điểm P.

Góc $\phi$ giữa dòng điện và hướng từ phần tử đến $P$ thỏa mãn $\sin\phi=x/r$. Từ phương trình (28.5), độ lớn đóng góp của phần tử là:

$$
\begin{aligned}
dB &= \frac{\mu_0 I}{4\pi}\,\frac{dy\sin\phi}{r^2} \\
&= \frac{\mu_0 I}{4\pi}\,\frac{x\,dy}{(x^2+y^2)^{3/2}}.
\end{aligned} \tag{28.8}
$$

Quy tắc bàn tay phải cho thấy mọi $d\vec B$ tại điểm P đều hướng vào mặt phẳng hình. Vì vậy, ta có thể cộng các độ lớn bằng tích phân theo $y$ từ đầu dưới $-a$ đến đầu trên $a$:

$$
B = \frac{\mu_0 I}{4\pi} \int_{-a}^{a} \frac{x\,dy}{(x^2+y^2)^{3/2}}.
$$

Với $x>0$, đặt $u=y/x$, nên $dy=x\,du$. Để tách phần biến thiên khỏi biểu thức dài, đặt $f(y)=x/(x^2+y^2)^{3/2}$ và $g(u)=1/(1+u^2)^{3/2}$. Nguyên hàm của $g(u)/x$ là $G(u)=u/[x\sqrt{1+u^2}]$. Khi đổi biến và thế hai cận, ta được:

$$
\begin{aligned}
\mathcal I &= \int_{-a}^{a}f(y)\,dy, \\
\mathcal I &= G(a/x)-G(-a/x), \\
\mathcal I &= \frac{2a}{x\sqrt{x^2+a^2}}.
\end{aligned}
$$

Thế kết quả tích phân vào biểu thức của $B$, ta được từ trường tại điểm nằm trên đường trung trực:

$$
B = \frac{\mu_0 I}{4\pi} \times\frac{2a}{x\sqrt{x^2+a^2}}.
$$

### Giới hạn dây rất dài và đường sức từ

Nếu chiều dài dây lớn hơn nhiều khoảng cách đến điểm đo, thì $a\gg x$ và $\sqrt{x^2+a^2}\approx a$. Trong giới hạn $a\to\infty$, phương trình (28.8) trở thành:

$$
B = \frac{\mu_0 I}{2\pi x}. \tag{28.9}
$$

Đối xứng trục cho biết từ trường có cùng độ lớn tại mọi điểm trên một đường tròn tâm nằm trên dây, trong mặt phẳng vuông góc với dây. Ở bán kính tổng quát $r$, từ trường quanh dây thẳng dài là:

$$
B = \frac{\mu_0 I}{2\pi r}.
$$

Các đường sức là những đường tròn đồng tâm với dây. Chiều của chúng được xác định bằng quy tắc bàn tay phải: Ngón cái chỉ theo chiều dòng điện, các ngón tay khum quanh dây theo chiều đường sức.

![Các đường sức từ là những đường tròn quanh dây dẫn thẳng mang dòng điện](../img/young-28/hinh-28-06.png)

Hình 28.6: Từ trường quanh dây dẫn dài có các đường sức tròn, với chiều xác định bằng quy tắc bàn tay phải.

Đường sức điện của điện tích đường tỏa ra hoặc hướng vào điện tích. Trái lại, đường sức từ do dòng điện luôn khép kín. Điều đó phù hợp với định luật Gauss cho từ trường, theo đó tổng từ thông qua mọi mặt kín bằng không:

$$
\oint_S \vec B\cdot d\vec A = 0. \tag{28.10}
$$

Mọi đường sức từ đi vào mặt kín đều phải đi ra khỏi mặt ấy. Từ trường không có điểm bắt đầu hay kết thúc như đường sức của điện tích đơn lẻ.

::: example Ví dụ 28.3 Tìm khoảng cách đến dây dẫn
Một dây dẫn thẳng, dài mang dòng $I=1{,}0\,\mathrm A$. Tại điểm cách trục dây một khoảng $r$, từ trường có độ lớn $B=0{,}5\times10^{-4}\,\mathrm T$, xấp xỉ từ trường Trái Đất ở Pittsburgh. Tìm $r$.

Điều kiện “dài” nghĩa là chiều dài dây lớn hơn nhiều $r$, nên dùng phương trình (28.9). Hai thừa số cần dùng là:

$$
\frac{\mu_0}{2\pi}\approx2\times10^{-7}\,\frac{\mathrm{T\,m}}{\mathrm A},
$$

$$
\frac IB=2\times10^4\,\frac{\mathrm A}{\mathrm T}.
$$

Giải phương trình theo r rồi nhân hai thừa số:

$$
\begin{aligned}
r &= \frac{\mu_0 I}{2\pi B} \\
&= \frac{\mu_0}{2\pi}\,\frac{I}{B} \\
&=(2\times2)\times10^{-3}\,\mathrm m\\
&= 4{,}0\times10^{-3}\,\mathrm m \\
&= 4{,}0\,\mathrm{mm}.
\end{aligned}
$$

Kết quả cho thấy dây điện gia dụng có dòng cỡ ampe vẫn tạo từ trường yếu ngay ở khoảng cách vài milimét. Độ lớn giảm theo $1/r$, nên ở xa dây trường còn nhỏ hơn.
:::

### Ví dụ 28.4: Từ trường của hai dây

Hai dây dài song song, vuông góc mặt phẳng $xy$, mang hai dòng có cùng độ lớn $I$ nhưng ngược chiều như Hình 28.7. (a) Tìm vector trường tại $P_1$, $P_2$, $P_3$. (b) Tìm biểu thức trường tại mọi điểm trên trục $x$ ở bên phải dây 2.

![Hai dây dài song song mang dòng điện ngược chiều và bản đồ từ trường của chúng](../img/young-28/hinh-28-07.png)

Hình 28.7: Hai dây mang dòng điện bằng nhau nhưng ngược chiều. Đường sức tập trung dày hơn giữa hai dây, nơi từ trường mạnh hơn.

Xét hai dây thẳng, song song, mỗi dây mang dòng có độ lớn $I$ nhưng ngược chiều. Theo nguyên lý chồng chất, tại một điểm, ta cộng véc-tơ từ trường do dây 1 và dây 2 tạo ra:

$$
\vec B_{\mathrm{tot}} = \vec B_1+\vec B_2.
$$

Chọn gốc tọa độ tại trung điểm hai dây, đặt dây 1 tại $x=-d$ và dây 2 tại $x=+d$. Dòng điện ở dây 1 hướng ra khỏi trang giấy, còn dòng ở dây 2 hướng vào trang giấy. Các khoảng cách đến từng dây cùng quy tắc bàn tay phải xác định độ lớn và dấu của thành phần từ trường theo $y$.

- Tại $P_1$, các khoảng cách đến dây 1 và dây 2 lần lượt là $2d$ và $4d$. Từ trường do dây 1 hướng theo $-y$, còn từ trường do dây 2 hướng theo $+y$:

$$
\begin{aligned}
\vec B_1 &= -\frac{\mu_0 I}{4\pi d}\,\hat\jmath, \\
\vec B_2 &= \frac{\mu_0 I}{8\pi d}\,\hat\jmath, \\
\vec B_{\mathrm{tot}}(P_1) &= -\frac{\mu_0 I}{8\pi d}\,\hat\jmath.
\end{aligned}
$$

- Tại $P_2$, hai dây cách điểm đó đều một khoảng $d$. Cả hai từ trường hướng theo $+y$, nên cộng lại:

$$
\begin{aligned}
\vec B_1 &= \frac{\mu_0 I}{2\pi d}\,\hat\jmath, \\
\vec B_2 &= \frac{\mu_0 I}{2\pi d}\,\hat\jmath, \\
\vec B_{\mathrm{tot}}(P_2) &= \frac{\mu_0 I}{\pi d}\,\hat\jmath.
\end{aligned}
$$

- Tại $P_3$, các khoảng cách đến dây 1 và dây 2 lần lượt là $3d$ và $d$. Từ trường của hai dây hướng ngược nhau:

$$
\begin{aligned}
\vec B_1 &= \frac{\mu_0 I}{6\pi d}\,\hat\jmath, \\
\vec B_2 &= -\frac{\mu_0 I}{2\pi d}\,\hat\jmath, \\
\vec B_{\mathrm{tot}}(P_3) &= -\frac{\mu_0 I}{3\pi d}\,\hat\jmath.
\end{aligned}
$$

Ở những điểm ngoài trục $x$, hai vector trường không còn nhất thiết song song hoặc ngược chiều. Khi ấy cần cộng từng thành phần, thay vì cộng hoặc trừ trực tiếp hai độ lớn.

(b) Với điểm trên trục $x$ ở bên phải dây 2, gọi tọa độ là $x>d$. Khoảng cách đến dây 1 và dây 2 lần lượt là $x+d$ và $x-d$. Hai từ trường tiếp tục ngược chiều:

$$
\begin{aligned}
C &= \frac{1}{x+d}-\frac{1}{x-d}, \\
\vec B(x) &= \frac{\mu_0 I}{2\pi}C\,\hat\jmath, \\
\vec B(x) &= -\frac{\mu_0 I d}{\pi(x^2-d^2)}\,\hat\jmath.
\end{aligned}
$$

Khi $x\gg d$, mẫu số xấp xỉ $x^2$, nên độ lớn từ trường tổng giảm gần như $1/x^2$. Với một dây đơn, trường giảm theo $1/x$. Ở cặp dây mang dòng ngược chiều, hai đóng góp bậc $1/x$ gần triệt tiêu. Vì vậy cặp dây tín hiệu và dây hồi dòng trong cáp máy tính hoặc cáp âm thanh thường được đặt sát nhau hoặc xoắn lại để làm từ trường bên ngoài nhỏ đi.

![Cáp máy tính hoặc âm thanh dùng các dây gần nhau mang dòng ngược chiều](../img/young-28/hinh-28-08.png)

Hình 28.8: Các dòng điện ngược chiều trong cùng một cáp làm từ trường bên ngoài nhỏ đi.

### Tự kiểm tra 28.3

Một mạch đặt nằm ngang trên bàn có công tắc và la bàn ở phía trên một đoạn dây. Cần lắp pin sao cho khi đóng công tắc, kim la bàn lệch ngược chiều kim đồng hồ. Nên đặt pin theo hướng A hay B?

![Hai cách đặt pin A, B và chiều lệch của kim la bàn trong mạch](../img/young-28/tu-kiem-tra-28-03.png)

::: details Đáp án
Chọn hướng A. Khi đó dòng điện chạy theo chiều kim đồng hồ trong mạch và đi về phía nam qua đoạn dây nằm dưới la bàn. Quy tắc bàn tay phải cho từ trường của dây hướng về phía tây tại vị trí la bàn. Kết hợp với từ trường hướng bắc của Trái Đất, từ trường tổng hướng tây bắc, nên kim quay ngược chiều kim đồng hồ.
:::
