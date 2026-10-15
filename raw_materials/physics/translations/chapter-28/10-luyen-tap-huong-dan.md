## Luyện tập có hướng dẫn

### Mục 28.2: Từ trường của điện tích chuyển động và phần tử dòng điện

Hãy ôn Ví dụ 28.1 và Ví dụ 28.2 trước khi làm bốn bài dưới đây.

::: exercise VP28.2.1
Một proton có điện tích $+1{,}60\times10^{-19}\,\mathrm C$ ở gốc tọa độ $(x=y=z=0)$, chuyển động với tốc độ $2{,}00\times10^5\,\mathrm{m/s}$ theo chiều $+x$. Tìm véc-tơ từ trường do proton tạo ra tại các điểm sau.

(a) $x=0$, $y=1{,}00\,\mathrm{mm}$, $z=0$.

(b) $x=0$, $y=0$, $z=2{,}00\,\mathrm{mm}$.

(c) $x=1{,}00\,\mathrm{mm}$, $y=0$, $z=0$.

(d) $x=1{,}00\,\mathrm{mm}$, $y=1{,}00\,\mathrm{mm}$, $z=0$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $q=+1{,}60\times10^{-19}\,\mathrm C$, $\vec v=(2{,}00\times10^5)\hat i\,\mathrm{m/s}$. Các véc-tơ từ nguồn proton đến bốn điểm lần lượt là $1{,}00\,\mathrm{mm}\,\hat j$, $2{,}00\,\mathrm{mm}\,\hat k$, $1{,}00\,\mathrm{mm}\,\hat i$ và $1{,}00\,\mathrm{mm}(\hat i+\hat j)$.

**Hướng đi:**

- Dùng $\vec B=(\mu_0/4\pi)q\,\vec v\times\hat r/r^2$, trong đó $\hat r$ hướng từ điện tích tới điểm đo.
- Xác định hướng bằng tích có hướng trước, rồi thay độ lớn $r$ vào biểu thức. Khi điểm nằm trên đường chuyển động, tích có hướng bằng không.

**Các bước giải:**

(a) Với $\vec r=1{,}00\times10^{-3}\hat j\,\mathrm m$, ta có $\hat i\times\hat j=\hat k$:

$$
\begin{aligned}
\vec B &= 10^{-7}\frac{qv}{r^2}\hat k \\
&= 3{,}20\times10^{-15}\,\hat k\,\mathrm T.
\end{aligned}
$$

(b) Hướng $\vec r$ là $+z$, còn $\hat i\times\hat k=-\hat j$:

$$
\vec B=-8{,}00\times10^{-16}\,\hat j\,\mathrm T.
$$

(c) Điểm nằm trên đường chuyển động, vì vậy $\vec v\times\hat r=0$ và $\vec B=0$.

(d) Ở đây $r=\sqrt2\times10^{-3}\,\mathrm m$ và $\vec v\times\hat r$ hướng $+z$. Do đó

$$
\vec B=1{,}13\times10^{-15}\,\hat k\,\mathrm T.
$$
:::

::: exercise VP28.2.2
Một proton có điện tích $+1{,}60\times10^{-19}\,\mathrm C$ và một electron có điện tích $-1{,}60\times10^{-19}\,\mathrm C$ cùng chuyển động trong mặt phẳng $xy$ với tốc độ $4{,}20\times10^5\,\mathrm{m/s}$. Proton chuyển động theo $+y$ trên đường $x=0$, còn electron chuyển động theo $-y$ trên đường $x=+2{,}00\,\mathrm{mm}$. Tại thời điểm chúng ở gần nhau nhất, tìm độ lớn và hướng của lực từ (a) proton tác dụng lên electron và (b) electron tác dụng lên proton.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai hạt cách nhau $d=2{,}00\times10^{-3}\,\mathrm m$, có cùng tốc độ $v=4{,}20\times10^5\,\mathrm{m/s}$ và điện tích có độ lớn $e=1{,}60\times10^{-19}\,\mathrm C$.

**Hướng đi:**

- Tính từ trường của một điện tích chuyển động tại vị trí hạt kia, rồi dùng $\vec F=q\vec v\times\vec B$.
- Giữ dấu điện tích trong tích có hướng để xác định mỗi lực. Hai lực trong cấu hình này hướng vào nhau vì hai hạt nằm ngang lệch vị trí nhưng chuyển động ngược chiều.

**Các bước giải:**

(a) Từ proton đến electron, véc-tơ vị trí hướng $+x$. Vì $\hat j\times\hat i=-\hat k$, từ trường tại electron hướng $-z$. Electron chuyển động theo $-y$, nên $\vec v_e\times\vec B_p$ hướng $+x$. Điện tích âm đảo chiều lực về $-x$, tức hướng về proton.

$$
\begin{aligned}
F &= \frac{\mu_0}{4\pi}\frac{e^2v^2}{d^2} \\
&= 1{,}13\times10^{-28}\,\mathrm N.
\end{aligned}
$$

(b) Từ trường do electron tại proton hướng $+z$. Với proton chuyển động theo $+y$, lực hướng $+x$, tức về phía electron. Độ lớn vẫn là $1{,}13\times10^{-28}\,\mathrm N$. Hai lực từ đều hướng vào nhau, nên chúng hút nhau.
:::

::: exercise VP28.2.3
Một đoạn dây dài $2{,}00\,\mathrm{mm}$, đặt đối xứng quanh gốc tọa độ, mang dòng điện $6{,}00\,\mathrm A$ theo chiều $+y$. Từ trường của đoạn dây được đo tại điểm $x=3{,}00\,\mathrm m$, $y=4{,}00\,\mathrm m$, $z=0$. Tìm (a) véc-tơ đơn vị từ đoạn dây tới điểm đo và (b) từ trường tại điểm đó.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $I=6{,}00\,\mathrm A$, $d\vec l=(2{,}00\times10^{-3}\,\mathrm m)\hat j$, $\vec r=(3{,}00\hat i+4{,}00\hat j)\,\mathrm m$.

**Hướng đi:**

- Chuẩn hóa véc-tơ vị trí bằng độ dài $r=\sqrt{3^2+4^2}\,\mathrm m$.
- Dùng định luật Biot–Savart cho phần tử dòng điện. Hướng trường do $d\vec l\times\hat r$ quyết định.

**Các bước giải:**

(a)

$$
\hat r=0{,}600\hat i+0{,}800\hat j.
$$

(b) Vì $\hat j\times\hat r=-0{,}600\hat k$, trường hướng $-z$:

$$
\begin{aligned}
B &= 10^{-7}\frac{I\,d l\sin\theta}{r^2} \\
&= \frac{7{,}20\times10^{-10}}{25{,}0} \\
&= 2{,}88\times10^{-11}\,\mathrm T.
\end{aligned}
$$

Tích có hướng $d\vec l\times\hat r$ hướng $-z$, nên $\vec B=-B\hat k$.
:::

::: exercise VP28.2.4
Một đoạn dây dài $8{,}00\,\mathrm{mm}$ đặt tại gốc tọa độ, mang dòng điện $4{,}00\,\mathrm A$ theo chiều $+z$. Đoạn dây tác dụng lực từ lên electron có điện tích $-1{,}60\times10^{-19}\,\mathrm C$ ở điểm $x=1{,}25\,\mathrm m$, $y=z=0$. Electron chuyển động với tốc độ $3{,}00\times10^5\,\mathrm{m/s}$ theo chiều $-x$. Tìm lực từ này.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $I=4{,}00\,\mathrm A$, $d l=8{,}00\times10^{-3}\,\mathrm m$ theo $+z$, còn electron ở trên trục $+x$ và có vận tốc theo $-x$.

**Hướng đi:**

- Trước hết tìm từ trường của đoạn dây tại electron bằng tích có hướng $d\vec l\times\hat r$.
- Sau đó dùng $\vec F=q\vec v\times\vec B$. Dấu âm của điện tích sẽ đảo chiều lực trên hạt.

**Các bước giải:**

Tại điểm trên trục $+x$, $\hat k\times\hat i=\hat j$, do đó

$$
\vec B=2{,}048\times10^{-9}\,\hat j\,\mathrm T.
$$

Vì $(-\hat i)\times\hat j=-\hat k$ và electron mang điện âm, lực hướng $+z$:

$$
\vec F = |q|vB\,\hat k = 9{,}83\times10^{-23}\,\hat k\,\mathrm N.
$$
:::

### Mục 28.4: Lực giữa các dây dẫn song song

Hãy ôn Ví dụ 28.3, 28.4 và 28.5 trước khi giải nhóm bài này.

::: exercise VP28.5.1
Một dây dẫn thẳng dài phải mang dòng điện bao nhiêu để từ trường do dây tạo ra tại điểm cách trục dây $1{,}40\,\mathrm{cm}$ có độ lớn $3{,}20\times10^{-5}\,\mathrm T$?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $r=1{,}40\times10^{-2}\,\mathrm m$ và $B=3{,}20\times10^{-5}\,\mathrm T$.

**Hướng đi:**

- Dùng $B=\mu_0 I/(2\pi r)$ vì dây thẳng đủ dài so với khoảng cách đo, rồi giải theo $I$.

**Các bước giải:**

$$
I = \frac{2\pi rB}{\mu_0} = 2{,}24\,\mathrm A.
$$
:::

::: exercise VP28.5.2
Hai dây dẫn thẳng dài cùng vuông góc với mặt phẳng $xy$. Dây 1 đi qua $x=0$, $y=+1{,}00\,\mathrm{cm}$, $z=0$ và mang dòng $1{,}00\,\mathrm A$ theo $+z$. Dây 2 đi qua $x=0$, $y=-1{,}00\,\mathrm{cm}$, $z=0$ và mang dòng $4{,}00\,\mathrm A$ cũng theo $+z$. Tìm từ trường tổng hợp tại các điểm sau.

(a) $(0,0,0)$.

(b) $(0,+2{,}00\,\mathrm{cm},0)$.

(c) $(0,-2{,}00\,\mathrm{cm},0)$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai dây mang dòng cùng chiều $+z$, nằm tại $y=\pm0{,}0100\,\mathrm m$.

**Hướng đi:**

- Từ trường quanh mỗi dây có độ lớn $B=\mu_0I/(2\pi r)$.
- Dùng quy tắc bàn tay phải để cộng véc-tơ. Ở giữa hai dây, hai trường ngược chiều, còn ở ngoài cả hai dây, chúng cùng chiều.

**Các bước giải:**

(a) Tại gốc, dây trên tạo trường $+x$ có độ lớn $20{,}0\,\mu\mathrm T$, dây dưới tạo trường $-x$ có độ lớn $80{,}0\,\mu\mathrm T$:

$$
\vec B_{\mathrm{net}}=-60{,}0\,\mu\mathrm T\,\hat i.
$$

(b) Điểm ở trên cả hai dây. Cả hai trường hướng $-x$, với khoảng cách lần lượt $1{,}00\,\mathrm{cm}$ và $3{,}00\,\mathrm{cm}$:

$$
\vec B_{\mathrm{net}}=-46{,}7\,\mu\mathrm T\,\hat i.
$$

(c) Điểm ở dưới cả hai dây. Hai trường hướng $+x$, với khoảng cách lần lượt $3{,}00\,\mathrm{cm}$ và $1{,}00\,\mathrm{cm}$:

$$
\vec B_{\mathrm{net}}=+86{,}7\,\mu\mathrm T\,\hat i.
$$
:::

::: exercise VP28.5.3
Một dây thẳng dài mang dòng $2{,}00\,\mathrm A$. Dây thứ hai giống hệt, song song và cách dây thứ nhất $3{,}00\,\mathrm{cm}$. Từ trường tại điểm chính giữa hai dây có độ lớn $4{,}00\times10^{-5}\,\mathrm T$. Tìm dòng điện trong dây thứ hai nếu nó (a) cùng chiều hoặc (b) ngược chiều với dòng điện thứ nhất.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai dây cách nhau $3{,}00\,\mathrm{cm}$, nên điểm giữa cách mỗi dây $1{,}50\,\mathrm{cm}$. Dòng dây thứ nhất là $2{,}00\,\mathrm A$.

**Hướng đi:**

- Ở điểm giữa, hai trường triệt tiêu một phần nếu dòng cùng chiều và cộng lại nếu dòng ngược chiều.
- Mỗi ampe tạo trường $\mu_0/(2\pi r)=1{,}333\times10^{-5}\,\mathrm{T/A}$ tại điểm đó.

**Các bước giải:**

(a) Với dòng cùng chiều, các véc-tơ trường đối nhau:

$$
\begin{aligned}
|2{,}00-I_2| &= 3{,}00 \\
I_2 &= 5{,}00\,\mathrm A.
\end{aligned}
$$

Nghiệm âm tương ứng với dòng ngược chiều, không thuộc trường hợp (a).

(b) Với dòng ngược chiều, hai trường cùng hướng:

$$
\begin{aligned}
2{,}00+I_2 &= 3{,}00 \\
I_2 &= 1{,}00\,\mathrm A.
\end{aligned}
$$
:::

::: exercise VP28.5.4
Hai dây siêu dẫn thẳng song song cách nhau $0{,}900\,\mathrm m$, đều thẳng đứng. Một dây mang dòng $1{,}30\times10^4\,\mathrm A$ hướng lên và chịu lực từ trên đơn vị chiều dài $95{,}0\,\mathrm{N/m}$ hút về phía dây kia. Tìm độ lớn và hướng dòng điện trong dây còn lại.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $r=0{,}900\,\mathrm m$, $I_1=1{,}30\times10^4\,\mathrm A$ hướng lên, $F/L=95{,}0\,\mathrm{N/m}$.

**Hướng đi:**

- Dùng lực trên một đơn vị chiều dài giữa hai dây dài. Vì lực hút nên hai dòng cùng chiều.

**Các bước giải:**

$$
\begin{aligned}
I_2 &= \frac{(F/L)2\pi r}{\mu_0 I_1} \\
&= 3{,}29\times10^4\,\mathrm A.
\end{aligned}
$$

Dòng điện thứ hai hướng lên.
:::

### Mục 28.7: Các ứng dụng của định luật Ampere

Hãy ôn Ví dụ 28.8, 28.9 và 28.10 trước khi giải các bài sau.

::: exercise VP28.10.1
Một dây dẫn hình trụ đặc bán kính $4{,}50\,\mathrm{cm}$ mang dòng $2{,}00\,\mathrm A$ phân bố đều trên tiết diện. Tìm độ lớn từ trường tại các khoảng cách tới trục dây sau.

(a) $2{,}50\,\mathrm{cm}$.

(b) $4{,}50\,\mathrm{cm}$.

(c) $6{,}00\,\mathrm{cm}$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Bán kính dây $R=0{,}0450\,\mathrm m$, dòng tổng $I=2{,}00\,\mathrm A$.

**Hướng đi:**

- Bên trong dây, mật độ dòng đều nên dòng bao bởi đường tròn bán kính $r$ bằng $I(r^2/R^2)$.
- Bên ngoài, dòng bao là toàn bộ $I$. Dùng định luật Ampere cho đường tròn đồng tâm.

**Các bước giải:**

(a) $r<R$:

$$
B = \frac{\mu_0 I r}{2\pi R^2} = 4{,}94\times10^{-6}\,\mathrm T.
$$

(b) Tại mặt dây, $B=\mu_0I/(2\pi R)=8{,}89\times10^{-6}\,\mathrm T$.

(c) $r>R$:

$$
B=\frac{\mu_0I}{2\pi r}=6{,}67\times10^{-6}\,\mathrm T.
$$
:::

::: exercise VP28.10.2
Một ống trụ dài rỗng có bán kính trong $R_1$ và bán kính ngoài $R_2$ mang dòng theo chiều dài ống. Dòng phân bố đều trên tiết diện và có mật độ dòng $J$. (a) Tìm độ lớn từ trường $B$ theo khoảng cách $r$ tới trục cho điểm trong khoang rỗng $(r<R_1)$, trong phần vật liệu $(R_1<r<R_2)$ và bên ngoài ống $(r>R_2)$. (b) Tại giá trị $r$ nào thì $B$ lớn nhất?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dòng chỉ phân bố trong vành trụ $R_1<r<R_2$ với mật độ đều $J$.

**Hướng đi:**

- Chọn đường Ampere tròn đồng tâm vì đối xứng trụ làm $B$ không đổi trên đường đó và tiếp tuyến với đường.
- Tính dòng bao riêng cho từng miền, rồi dùng $B(2\pi r)=\mu_0I_{\mathrm{encl}}$.

**Các bước giải:**

Trong khoang rỗng không có dòng bao, nên

$$
B=0\qquad(r<R_1).
$$

Trong vật liệu, diện tích vành khăn được bao là:

$$
\begin{aligned}
A_{\mathrm{encl}} &= \pi(r^2-R_1^2), \\
I_{\mathrm{encl}} &= J A_{\mathrm{encl}}.
\end{aligned}
$$

Từ định luật Ampere:

$$
\begin{aligned}
B &= \frac{\mu_0 I_{\mathrm{encl}}}{2\pi r} \\
&= \frac{\mu_0 J A_{\mathrm{encl}}}{2\pi r}.
\end{aligned}
$$

Bên ngoài, với $r>R_2$, dòng bao là tổng dòng $J\pi(R_2^2-R_1^2)$:

$$
B=\frac{\mu_0J}{2r}(R_2^2-R_1^2).
$$

Trong vật liệu, $B$ tăng theo $r$. Bên ngoài, $B$ giảm theo $1/r$. Vì vậy $B$ lớn nhất tại bề mặt ngoài $r=R_2$.
:::

::: exercise VP28.10.3
Một ống dây rất dài, quấn sít, có $8{,}00\times10^3$ vòng trên mỗi mét. Dòng điện cần thiết là bao nhiêu để từ trường bên trong ống dây có độ lớn $0{,}0320\,\mathrm T$?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $n=8{,}00\times10^3\,\mathrm{m^{-1}}$, $B=0{,}0320\,\mathrm T$.

**Hướng đi:**

- Ở gần tâm một ống dây dài, $B=\mu_0 nI$. Giải biểu thức này theo $I$.

**Các bước giải:**

$$
I = \frac{B}{\mu_0n} = 3{,}18\,\mathrm A.
$$
:::

::: exercise VP28.10.4
Một dây đồng mang dòng $0{,}840\,\mathrm A$ được quấn quanh lõi hình xuyến rỗng, tạo thành một ống dây hình xuyến. Bán kính trong và ngoài của lõi lần lượt là $6{,}00\,\mathrm{cm}$ và $8{,}00\,\mathrm{cm}$. (a) Cần bao nhiêu vòng dây để từ trường tại khoảng cách $7{,}00\,\mathrm{cm}$ từ trục hình xuyến có độ lớn $2{,}00\times10^{-3}\,\mathrm T$? (b) Với số vòng này, tìm độ lớn lớn nhất và nhỏ nhất của từ trường trong lõi.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $I=0{,}840\,\mathrm A$, $r=0{,}0700\,\mathrm m$, $B=2{,}00\times10^{-3}\,\mathrm T$, $r_{\mathrm{trong}}=0{,}0600\,\mathrm m$, $r_{\mathrm{ngoài}}=0{,}0800\,\mathrm m$.

**Hướng đi:**

- Trong lõi hình xuyến, $B=\mu_0NI/(2\pi r)$.
- Suy ra $N$ từ điểm đã cho, rồi thay bán kính trong và ngoài để lấy giá trị biên. Trường mạnh hơn ở bán kính nhỏ.

**Các bước giải:**

(a)

$$
\begin{aligned}
N &= \frac{2\pi rB}{\mu_0 I} \\
&\approx 833\text{ vòng}.
\end{aligned}
$$

(b) Đặt $r_1=0{,}0600\,\mathrm m$ và $r_2=0{,}0800\,\mathrm m$ lần lượt là bán kính trong và ngoài. Khi đó:

$$
\begin{aligned}
B_{\max} &= \frac{\mu_0NI}{2\pi r_1} \\
&= 2{,}33\times10^{-3}\,\mathrm T, \\
B_{\min} &= \frac{\mu_0NI}{2\pi r_2} \\
&= 1{,}75\times10^{-3}\,\mathrm T.
\end{aligned}
$$
:::

### Bài toán cầu nối: Từ trường của đĩa điện môi tích điện đang quay

::: exercise Bài cầu nối 28

Một đĩa điện môi mỏng bán kính $a$ có tổng điện tích $+Q$ phân bố đều trên mặt đĩa. Đĩa quay $n$ vòng mỗi giây quanh trục vuông góc với mặt đĩa và đi qua tâm. Tìm từ trường tại tâm.

![Bài toán cầu nối: Đĩa tích điện quay tạo từ trường tại tâm, có thể chia thành các vòng vành khăn vi phân.](img/young-28/hinh-bridge28-30.png)

**Nhận diện và thiết lập**

1. Xem đĩa quay như tập hợp các vòng tròn đồng tâm. Mỗi vòng tạo từ trường tại tâm đĩa như một vòng dây mang dòng.
2. Dùng kết quả của mục 28.5 cho một vòng rồi tích phân theo bán kính.

**Thực hiện**

3. Tìm điện tích trên một vành khăn có bán kính trong $r$ và bán kính ngoài $r+dr$.
4. Từ thời gian để vành khăn quay hết một vòng, suy ra dòng điện tương đương của vành khăn.
5. Dùng công thức trường tại tâm của vòng tròn để tìm đóng góp $dB$.
6. Tích phân các vành khăn từ $r=0$ đến $r=a$.

**Đánh giá**

7. Kiểm tra đơn vị của kết quả.
8. So sánh với trường hợp toàn bộ điện tích nằm ở vành ngoài, $r=a$. Trường hợp nào tạo trường mạnh hơn tại tâm?

:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện tích mặt đều $\sigma=Q/(\pi a^2)$, tốc độ quay $n$ vòng mỗi giây.

**Hướng đi:**

- Chia đĩa thành vành khăn bán kính $r$, bề rộng $dr$, rồi tìm điện tích vi phân $dQ$.
- Một vành khăn quay hết vòng trong $1/n$ giây, nên tạo dòng $dI=n\,dQ$. Dùng trường tại tâm của vòng dòng bán kính $r$.
- Cộng liên tục các đóng góp từ tâm đến mép đĩa.

**Các bước giải:**

Vành khăn vi phân có diện tích $dA=2\pi r\,dr$, nên

$$
dQ=\sigma dA=2\pi\sigma r\,dr.
$$

Trong thời gian $1/n$, lượng điện tích $dQ$ đi qua một mặt cắt của vòng. Vì vậy dòng tương đương là

$$
dI=\frac{dQ}{1/n}=2\pi n\sigma r\,dr.
$$

Từ trường do vòng nhỏ tại tâm hướng theo trục quay, theo quy tắc bàn tay phải. Độ lớn là

$$
dB=\frac{\mu_0dI}{2r}=\mu_0\pi n\sigma\,dr.
$$

Tích phân trên toàn đĩa:

$$
\begin{aligned}
B &= \int_0^a dB \\
&= \mu_0\pi n\sigma\int_0^a dr \\
&= \mu_0\pi n\sigma a \\
&= \frac{\mu_0 nQ}{a}.
\end{aligned}
$$

Hướng từ trường theo chiều trục xác định bằng quy tắc bàn tay phải quanh chiều quay. Đơn vị $\mu_0nQ/a$ là tesla. Nếu cùng điện tích $Q$ tập trung ở vành ngoài, dòng là $nQ$ và trường tâm chỉ bằng $\mu_0nQ/(2a)$, tức bằng một nửa trường của đĩa tích điện đều.
:::
