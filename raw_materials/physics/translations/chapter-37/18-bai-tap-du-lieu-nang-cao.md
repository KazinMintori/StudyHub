## Bài tập dữ liệu và bài tập nâng cao

::: exercise 37.63

Bạn nghiên cứu một hạt không bền tại máy gia tốc thẳng. Thời gian sống trung bình $\Delta t$ được đo theo tốc độ $u$ của hạt đối với thiết bị phòng thí nghiệm:

| $u/c$ | $\Delta t$ ($10^{-8}\,\mathrm s$) |
| --- | --- |
| $0{,}70$ | $3{,}57$ |
| $0{,}80$ | $4{,}41$ |
| $0{,}85$ | $5{,}02$ |
| $0{,}88$ | $5{,}47$ |
| $0{,}90$ | $6{,}05$ |
| $0{,}92$ | $6{,}58$ |
| $0{,}94$ | $7{,}62$ |

(a) Vẽ bình phương thời gian sống theo đại lượng nghịch đảo $1-u^2/c^2$. Kiểm tra dự đoán rằng các điểm gần nằm trên một đường thẳng và dùng đường hồi quy tốt nhất để tìm thời gian sống riêng. (b) Tốc độ hạt bằng bao nhiêu theo đơn vị $c$ nếu thời gian sống trong phòng lớn gấp bốn thời gian sống riêng?

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Có bảy điểm đo tốc độ và thời gian sống. Cần biến đổi dữ liệu để nhận ra quan hệ tuyến tính từ giãn thời gian.

**Hướng đi:**

- Bình phương $\Delta t=\gamma\Delta t_0$ để thu được quan hệ giữa hai đại lượng đề yêu cầu vẽ.
- Dùng hệ số góc của đường thẳng, thay vì lấy một điểm riêng lẻ, để ước lượng thời gian sống riêng.
- Ở (b), tỉ số thời gian cho trực tiếp $\gamma=4$.

(a) Đặt

$$
X=\frac1{1-u^2/c^2}.
$$

Gọi $Y$ là bình phương thời gian sống, đo theo đơn vị $10^{-16}\,\mathrm{s^2}$. Mô hình lý tưởng cho

$$
(\Delta t)^2=(\Delta t_0)^2X.
$$

Hồi quy cả bảy điểm bằng một đường thẳng có hệ số chặn tự do cho

$$
Y\approx6{,}7086X+0{,}4226.
$$

![Lời giải 37.63: Cả bảy điểm đo sau tuyến tính hóa nằm gần đường hồi quy của bình phương thời gian sống theo bình phương hệ số Lorentz.](img/young-37/loi-giai-37-63.svg)

Hệ số xác định xấp xỉ $0{,}9981$, phù hợp với dự đoán gần tuyến tính. Hệ số góc có giá trị vật lý $6{,}7086\times10^{-16}\,\mathrm{s^2}$, nên

$$
\Delta t_0\approx2{,}59\times10^{-8}\,\mathrm s.
$$

Mô hình lý tưởng có hệ số chặn bằng không, nhưng dữ liệu đo không nằm đúng trên đường lý tưởng. Nếu buộc đường hồi quy qua gốc, kết quả là $2{,}60\times10^{-8}\,\mathrm s$. Hai cách đều cho ước lượng khoảng $2{,}6\times10^{-8}\,\mathrm s$ ở mức chính xác của dữ liệu.

(b) Điều kiện thời gian sống tăng bốn lần cho $\gamma=4$. Do đó,

$$
\frac uc=\sqrt{1-\frac1{16}}\approx0{,}968.
$$

:::

::: exercise 37.64

Armand Fizeau đo tốc độ ánh sáng trong nước chuyển động và thu được dạng gần đúng

$$
w=\frac cn+kV.
$$

Ở đây $n=1{,}333$ là chiết suất nước, $V$ là tốc độ nước cùng hướng truyền ánh sáng đối với phòng thí nghiệm, còn $k$ là hệ số kéo. Giá trị thực nghiệm được cho bằng $0{,}44$. Dùng phép biến đổi vận tốc tương đối tính để tính $k$.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Trong hệ nghỉ của nước, ánh sáng có tốc độ $c/n$. Cần khai triển đến bậc nhất theo tốc độ nước $V$ khi $V/c$ nhỏ.

**Hướng đi:**

- Dùng phép cộng vận tốc Lorentz cho ánh sáng trong môi trường chuyển động.
- Khai triển mẫu số đến bậc nhất theo $V/c$, rồi gom hệ số của $V$.

Biểu thức chính xác trong mô hình chiết suất đã cho là

$$
w=\frac{c/n+V}{1+V/(nc)}.
$$

Đặt $q=V/c$. Với $q$ nhỏ, ta có

$$
\frac1{1+q/n}\approx1-\frac qn.
$$

Sau khi nhân và bỏ các số hạng bậc hai theo $V/c$,

$$
w\approx\frac cn+\left(1-\frac1{n^2}\right)V.
$$

Vậy

$$
k=1-\frac1{n^2}\approx0{,}437.
$$

Giá trị làm tròn là $0{,}44$, phù hợp với dữ kiện thực nghiệm.

:::

::: exercise 37.65

Một hạt aerosol tích điện trong buồng chân không chịu lực điện không đổi $8{,}00\times10^{-14}\,\mathrm N$. Hạt chuyển động theo hướng lực. Gia tốc đo được theo tốc độ là

| $v/c$ | $a$ ($10^3\,\mathrm{m/s^2}$) |
| --- | --- |
| $0{,}60$ | $20{,}3$ |
| $0{,}65$ | $17{,}9$ |
| $0{,}70$ | $14{,}8$ |
| $0{,}75$ | $11{,}2$ |
| $0{,}80$ | $8{,}5$ |
| $0{,}85$ | $5{,}9$ |

(a) Chọn cách vẽ để các điểm gần nằm trên một đường thẳng. Dùng hệ số góc tìm khối lượng hạt. (b) Cùng lực ấy tạo gia tốc bao nhiêu khi tốc độ hạt bằng $100\,\mathrm{m/s}$?

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Lực cùng hướng vận tốc và có độ lớn không đổi. Có sáu điểm gia tốc theo tốc độ.

**Hướng đi:**

- Dùng $F=\gamma^3ma$ vì lực dọc vận tốc.
- Chọn hoành độ $X=(1-v^2/c^2)^{3/2}$ để có quan hệ tuyến tính $a=(F/m)X$.
- Hệ số góc cho $F/m$. Ở $100\,\mathrm{m/s}$, hệ số Lorentz gần một nên gia tốc gần bằng hệ số góc.

(a) Hồi quy sáu điểm với gia tốc tính theo đơn vị SI cho

$$
a\approx SX+b.
$$

Hai hệ số lần lượt là $S\approx4{,}0361\times10^4\,\mathrm{m/s^2}$ và $b\approx-129\,\mathrm{m/s^2}$.

![Lời giải 37.65: Sáu điểm gia tốc trở nên gần tuyến tính khi vẽ theo lũy thừa ba phần hai của một trừ bình phương tỉ số tốc độ.](img/young-37/loi-giai-37-65.svg)

Hệ số xác định xấp xỉ $0{,}9977$. Khối lượng từ hệ số góc là

$$
m=\frac FS\approx1{,}98\times10^{-18}\,\mathrm{kg}.
$$

Nếu buộc đường lý tưởng qua gốc, ước lượng là $2{,}00\times10^{-18}\,\mathrm{kg}$. Ở độ chính xác của dữ liệu, có thể báo khối lượng khoảng $2{,}0\times10^{-18}\,\mathrm{kg}$.

(b) Với tốc độ $100\,\mathrm{m/s}$, hiệu chỉnh tương đối tính không đáng kể ở các chữ số được giữ. Gia tốc bằng khoảng $4{,}04\times10^4\,\mathrm{m/s^2}$ theo khối lượng từ hồi quy tự do.

:::

::: exercise 37.66

Bạn nghiên cứu bốn nguồn bức xạ hồng ngoại và biết tần số riêng $f_0$ của mỗi nguồn. Máy thu đứng yên trên Trái Đất đo được tần số $f$:

| Nguồn | $f$ (THz) | $f_0$ (THz) |
| --- | --- | --- |
| A | $7{,}1$ | $9{,}2$ |
| B | $5{,}4$ | $8{,}6$ |
| C | $6{,}1$ | $7{,}9$ |
| D | $8{,}1$ | $8{,}9$ |

(a) Nguồn nào có tốc độ lớn nhất đối với máy thu? Tốc độ ấy bằng bao nhiêu và nguồn tiến lại gần hay rời xa? (b) Trả lời tương tự cho tốc độ nhỏ nhất. (c) Với nguồn B, nếu giữ nguyên tốc độ nhưng đổi hướng để nguồn tiến lại gần, máy thu đo tần số bao nhiêu?

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Cả bốn nguồn có $f<f_0$. Xét chuyển động dọc phương nhìn như mô hình Doppler của bài toán.

**Hướng đi:**

- Tần số giảm chỉ ra chuyển động rời xa.
- Dùng tỉ số tần số, không dùng độ chênh tần số tuyệt đối, để suy tốc độ.
- Khi đảo hướng với cùng tốc độ, hệ số Doppler trở thành nghịch đảo của hệ số cũ.

Gọi $b=u/c$ là độ lớn tỉ số tốc độ rời xa. Từ công thức Doppler,

$$
b=\frac{f_0^2-f^2}{f_0^2+f^2}.
$$

Kết quả trước làm tròn được liệt kê để so sánh:

| Nguồn | $u/c$ |
| --- | --- |
| A | $0{,}25346$ |
| B | $0{,}43445$ |
| C | $0{,}25296$ |
| D | $0{,}09391$ |

(a) Nguồn B nhanh nhất, rời xa với tốc độ khoảng $0{,}43c$.

(b) Nguồn D chậm nhất, rời xa với tốc độ khoảng $0{,}094c$. Chênh lệch suy ra giữa A và C nhỏ hơn mức chính xác mà hai chữ số dữ liệu có thể hỗ trợ, nhưng không ảnh hưởng hai cực trị B và D.

(c) Khi B tiến lại gần, tần số mới thỏa mãn

$$
f_{\rm toward}=\frac{f_0^2}{f}\approx13{,}7\,\mathrm{THz}.
$$

Theo hai chữ số có nghĩa của dữ liệu, kết quả xấp xỉ $14\,\mathrm{THz}$.

:::

::: exercise 37.67

Một ống đèn huỳnh quang dài $L$ nằm ngang phía trên cửa bán vé sân ga. Trong hệ sân ga $S$, ống nằm trên trục $x$, đầu phải ở gốc và đầu trái ở $x=-L$. Đèn sáng đồng loạt tại $t=0$, đổi từ trắng sang vàng, rồi tắt đồng loạt tại $t=T$.

![Bài 37.67: Miền chữ nhật màu vàng biểu diễn những sự kiện trên ống đèn trong thời gian nó sáng ở hệ sân ga.](img/young-37/hinh-p37-67.png)

Sự kiện 1 và 2 lần lượt là đầu phải và đầu trái lúc bật. Sự kiện 3 và 4 lần lượt là đầu phải và đầu trái lúc tắt. Một tàu chạy từ trái sang phải với tốc độ $v$. Hệ $S'$ gắn tàu có các trục cùng hướng, và sự kiện 1 là gốc $x'=t'=0$.

(a) Tìm tọa độ của bốn sự kiện trong $S'$. (b) Dựng giản đồ không thời gian tương ứng. (c) Tìm diện tích miền đèn sáng trên giản đồ $x,ct$ trong $S$. (d) Tìm diện tích miền tương ứng trong $S'$. (e) Hai diện tích có bằng nhau không?

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Bốn tọa độ trong $S$ là $(0,0)$, $(-L,0)$, $(0,T)$ và $(-L,T)$. Đặt $\beta=v/c$ và $\gamma=1/\sqrt{1-\beta^2}$.

**Hướng đi:**

- Áp dụng $x'=\gamma(x-vt)$ và $ct'=\gamma(ct-\beta x)$ cho từng sự kiện.
- Nối 1–2–4–3 theo thứ tự biên miền sáng. Biến đổi Lorentz là tuyến tính nên hình chữ nhật trở thành hình bình hành.
- Tính diện tích từ định thức hai cạnh kề trong mặt phẳng có cả hai trục cùng đơn vị chiều dài.

(a) Tọa độ là

| Sự kiện | $x'$ | $ct'$ |
| --- | --- | --- |
| 1 | $0$ | $0$ |
| 2 | $-\gamma L$ | $\gamma\beta L$ |
| 3 | $-\gamma\beta cT$ | $\gamma cT$ |
| 4 | $-\gamma(L+vT)$ | $\gamma(cT+\beta L)$ |

Chia cột cuối cho $c$ nếu cần tọa độ $t'$.

(b) Hai đường bật đèn và tắt đèn không còn nằm ngang trên giản đồ của tàu. Hai đầu đèn vẫn cùng chuyển động đều theo chiều âm của $x'$.

![Lời giải 37.67: Miền sáng trở thành hình bình hành 1–2–4–3 trong hệ tàu. Các độ nghiêng trên sơ đồ minh họa một vận tốc dương, còn tọa độ tổng quát được cho trong bảng.](img/young-37/loi-giai-37-67.svg)

(c) Trong $S$, diện tích hình chữ nhật là

$$
A=LcT.
$$

(d) Gọi hai vectơ cạnh từ sự kiện 1 đến 2 và từ 1 đến 3 lần lượt là $\vec a$ và $\vec b$. Các thành phần theo $x',ct'$ là

$$
\begin{aligned}
a_x&=-\gamma L,\\
a_t&=\gamma\beta L,\\
b_x&=-\gamma\beta cT,\\
b_t&=\gamma cT.
\end{aligned}
$$

Diện tích là độ lớn định thức:

$$
\begin{aligned}
A'&= |a_xb_t-a_tb_x|\\
&= \gamma^2LcT(1-\beta^2)\\
&= LcT.
\end{aligned}
$$

(e) Hai diện tích bằng nhau. Trong mặt phẳng $x,ct$, ma trận biến đổi Lorentz có định thức bằng một, nên bảo toàn diện tích này dù làm thay đổi hình dạng miền.

:::

::: exercise 37.68

Hai sao giống nhau, mỗi sao có khối lượng $m$, chuyển động tròn bán kính $R$ quanh khối tâm chung. Mặt phẳng quỹ đạo chứa đường nhìn từ Trái Đất. Ta có thể suy chuyển động từ dịch Doppler của vạch hydrogen, nên đây là một mô hình hệ sao đôi quang phổ.

![Bài 37.68: Hai sao cùng khối lượng ở hai phía của quỹ đạo tròn quanh khối tâm, với mặt phẳng quỹ đạo nhìn nghiêng hoàn toàn từ Trái Đất.](img/young-37/hinh-p37-68.png)

(a) Tần số hydrogen trong phòng thí nghiệm là $f_0=4{,}568110\times10^{14}\,\mathrm{Hz}$. Tần số thu từ mỗi sao biến thiên giữa $f_{\min}=4{,}567710\times10^{14}\,\mathrm{Hz}$ và $f_{\max}=4{,}568910\times10^{14}\,\mathrm{Hz}$. Tìm hướng và tốc độ chuyển động của toàn hệ đối với Trái Đất, cùng tốc độ quỹ đạo mỗi sao. Có thể dùng gần đúng Doppler tốc độ nhỏ.

(b) Một chu kỳ từ cực đại tần số đến cực tiểu rồi trở lại cực đại kéo dài $11{,}0$ ngày. Tìm $R$ và $m$ theo kilogram, theo khối lượng Mặt Trời $1{,}99\times10^{30}\,\mathrm{kg}$, và so $R$ với khoảng cách Trái Đất–Mặt Trời $1{,}50\times10^{11}\,\mathrm m$.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Hai sao có cùng khối lượng, quỹ đạo tròn và đường nhìn nằm trong mặt phẳng quỹ đạo. Gọi $U$ là tốc độ khối tâm tiến lại gần, $v$ là tốc độ quỹ đạo mỗi sao.

**Hướng đi:**

- Trung bình hai cực trị tần số cho dịch do chuyển động chung của khối tâm. Nửa khoảng biến thiên cho thành phần vận tốc quỹ đạo cực đại.
- Dùng gần đúng $\Delta f/f_0\approx u/c$ vì các tốc độ suy ra nhỏ hơn nhiều so với $c$.
- Từ $v=2\pi R/T$, tìm bán kính. Khoảng cách hai sao là $2R$, nên lực hấp dẫn dùng mẫu số $(2R)^2$.

(a) Tần số ở tâm khoảng biến thiên là

$$
f_c=\frac{f_{\max}+f_{\min}}2.
$$

Giá trị $f_c=4{,}568310\times10^{14}\,\mathrm{Hz}$ lớn hơn $f_0$. Vì vậy, khối tâm toàn hệ tiến lại gần Trái Đất. Tốc độ là

$$
\begin{aligned}
U&\approx c\frac{f_c-f_0}{f_0}\\
&\approx13{,}1\,\mathrm{km/s}.
\end{aligned}
$$

Tốc độ quỹ đạo mỗi sao bằng

$$
\begin{aligned}
v&\approx c\frac{f_{\max}-f_{\min}}{2f_0}\\
&\approx39{,}4\,\mathrm{km/s}.
\end{aligned}
$$

(b) Chu kỳ $T=11{,}0$ ngày $=950400\,\mathrm s$. Bán kính quỹ đạo là

$$
R=\frac{vT}{2\pi}\approx5{,}96\times10^9\,\mathrm m.
$$

Cân bằng lực hấp dẫn và lực hướng tâm cho mỗi sao:

$$
\frac{Gm^2}{(2R)^2}=\frac{mv^2}{R}.
$$

Suy ra, với $G=6{,}67\times10^{-11}$ theo đơn vị SI,

$$
\begin{aligned}
m&= \frac{4Rv^2}{G}\\
&\approx 5{,}55\times10^{29}\,\mathrm{kg}.
\end{aligned}
$$

Mỗi sao có khối lượng khoảng $0{,}279$ khối lượng Mặt Trời. Bán kính quỹ đạo bằng khoảng $0{,}0397$ khoảng cách Trái Đất–Mặt Trời, tức gần $4\%$.

Trong hệ thật, hai sao có thể không giống nhau, quỹ đạo có thể không tròn và mặt phẳng quỹ đạo có thể nghiêng so với đường nhìn. Khi đó phải bổ sung các thông số ấy để suy khối lượng từ vạch phổ.

:::

::: exercise 37.69

Trong vật lý năng lượng cao, va chạm của hai proton có thể tạo thêm một kaon âm và một kaon dương:

$$
p+p\to p+p+K^-+K^+.
$$

Năng lượng nghỉ mỗi proton là $938{,}3\,\mathrm{MeV}$, còn mỗi kaon là $493{,}7\,\mathrm{MeV}$.

(a) Nếu proton bia ban đầu đứng yên, động năng nhỏ nhất của proton tới để phản ứng có thể xảy ra bằng bao nhiêu? Có thể xét hệ tổng động lượng bằng không, rồi liên hệ với hệ phòng thí nghiệm bằng biến đổi Lorentz. (b) So động năng ngưỡng ấy với tổng năng lượng nghỉ hai kaon. (c) Nếu hai proton tới có vận tốc bằng nhau về độ lớn, ngược chiều, tổng động năng nhỏ nhất bằng bao nhiêu? So với năng lượng nghỉ hai kaon và giải thích lợi ích của hai chùm đối đầu.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Đặt $M=938{,}3\,\mathrm{MeV}$ và $q=493{,}7\,\mathrm{MeV}$, đều là các năng lượng nghỉ. Năng lượng nghỉ tổng trạng thái cuối là $W=2M+2q$.

**Hướng đi:**

- Ở ngưỡng, các hạt cuối không có chuyển động tương đối trong hệ khối tâm. Tổng năng lượng trong hệ ấy nhỏ nhất và bằng $W$.
- Dùng tính bất biến của bình phương năng lượng toàn hệ trừ bình phương tổng động lượng nhân $c^2$ để chuyển giữa hai hệ mà vẫn bảo toàn cả năng lượng lẫn động lượng.
- Với bia đứng yên, một phần năng lượng phải còn trong chuyển động chung của hệ cuối ở phòng thí nghiệm. Hai chùm đối đầu đối xứng loại bỏ phần chuyển động khối tâm ấy.

(a) Gọi $E$ là năng lượng toàn phần của proton tới và $p$ là động lượng của nó. Trong phòng thí nghiệm, tổng năng lượng là $E+M$ và tổng động lượng là $p$. Hệ thức cho proton tới là

$$
(pc)^2=E^2-M^2.
$$

Ở ngưỡng, bất biến toàn hệ cho

$$
W^2=(E+M)^2-(pc)^2.
$$

Thay hệ thức của proton tới vào và rút gọn:

$$
W^2=2M^2+2ME.
$$

Với $E=M+K$, động năng ngưỡng là

$$
K=\frac{W^2-4M^2}{2M}.
$$

Thay các năng lượng nghỉ đã cho, ta được

$$
K\approx2494{,}3\,\mathrm{MeV}.
$$

Trong hệ khối tâm, các vận tốc cuối cùng đều bằng không ở ngưỡng. Trong hệ phòng, cả hệ sản phẩm vẫn chuyển động. Tốc độ khối tâm ở ngưỡng xấp xỉ $0{,}7554c$, xác định từ $v_{\rm CM}/c=pc/(E+M)$.

(b) Tổng năng lượng nghỉ của hai kaon là $2q=987{,}4\,\mathrm{MeV}$. Động năng ngưỡng bia cố định lớn gấp khoảng $2{,}526$ lần giá trị ấy.

(c) Với hai chùm đối đầu đối xứng, phòng thí nghiệm cũng là hệ khối tâm. Ở ngưỡng,

$$
K_{\rm total}=2q=987{,}4\,\mathrm{MeV}.
$$

Mỗi proton cần động năng $493{,}7\,\mathrm{MeV}$. Tổng động năng đúng bằng năng lượng nghỉ của các hạt mới vì không phải dành năng lượng cho chuyển động chung của hệ cuối. Đây là lợi ích của hai chùm đối đầu trong bài toán tạo hạt.

:::

::: exercise 37.70

(a) Xét biến đổi Galileo $x'=x-vt$, $t'=t$. Trong hệ $S$, thành phần điện trường sóng điện từ trong chân không thỏa mãn phương trình sóng

$$
\frac{\partial^2E}{\partial x^2}-\frac1{c^2}\frac{\partial^2E}{\partial t^2}=0.
$$

Chứng minh phương trình đổi dạng khi chuyển sang $S'$. Cụ thể, nếu đặt $\beta=v/c$ và các đạo hàm chuẩn hóa

$$
U=\frac{\partial^2E}{\partial x'^2},
$$

$$
V=\frac1c\frac{\partial^2E}{\partial x'\partial t'},
$$

$$
W=\frac1{c^2}\frac{\partial^2E}{\partial t'^2},
$$

thì cần thu được

$$
(1-\beta^2)U+2\beta V-W=0.
$$

Dùng quy tắc đạo hàm hàm hợp để chuyển các toán tử đạo hàm. (b) Lặp lại với biến đổi Lorentz và chứng minh phương trình trong $S'$ trở lại dạng $U-W=0$. Giải thích ý nghĩa đối với tốc độ ánh sáng trong hai hệ.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Cần xét sự biến đổi toán tử sóng khi các tọa độ đổi tuyến tính. Ký hiệu $E$ ở hai hệ biểu diễn hàm sau đổi biến trong phép chứng minh này.

**Hướng đi:**

- Dùng quy tắc dây chuyền cho từng đạo hàm bậc nhất, rồi bình phương các toán tử vì các hệ số biến đổi là hằng số.
- Giữ đạo hàm hỗn hợp. Hệ số của nó là nơi thể hiện sự khác nhau giữa biến đổi Galileo và Lorentz.
- Đặt toán tử không gian $A=\partial/\partial x'$ và toán tử thời gian chuẩn hóa $B=(1/c)\partial/\partial t'$ để khai triển đủ các số hạng mà mỗi công thức vẫn gọn.

Ta có $A^2E=U$, $ABE=V$ và $B^2E=W$. Các đạo hàm hỗn hợp giao hoán khi trường đủ trơn.

(a) Với biến đổi Galileo, quy tắc dây chuyền cho

$$
\frac{\partial}{\partial x}=A,
$$

$$
\frac1c\frac{\partial}{\partial t}=B-\beta A.
$$

Gọi $Q=(B-\beta A)^2E$. Khai triển tường minh:

$$
Q=W-2\beta V+\beta^2U.
$$

Phương trình sóng ban đầu là $U-Q=0$. Đặt $\alpha=1-\beta^2$ để gom hệ số, ta được

$$
\alpha U+2\beta V-W=0.
$$

Đây là phương trình đích, với $\alpha=1-v^2/c^2$. Xuất hiện đạo hàm hỗn hợp và hệ số không gian khác một, nên phương trình không giữ nguyên dạng.

(b) Với biến đổi Lorentz,

$$
x'=\gamma(x-vt),
$$

$$
t'=\gamma(t-vx/c^2).
$$

Quy tắc dây chuyền cho

$$
\frac{\partial}{\partial x}=\gamma(A-\beta B),
$$

$$
\frac1c\frac{\partial}{\partial t}=\gamma(B-\beta A).
$$

Đặt $P=(A-\beta B)^2E$ và giữ $Q$ như trên. Khai triển hai bình phương là

$$
\begin{aligned}
P&=U-2\beta V+\beta^2W,\\
Q&=W-2\beta V+\beta^2U.
\end{aligned}
$$

Hai đạo hàm hỗn hợp triệt tiêu khi lấy hiệu:

$$
P-Q=(1-\beta^2)(U-W).
$$

Vì $\gamma^2(1-\beta^2)=1$, phương trình ban đầu trở thành

$$
\begin{aligned}
\gamma^2(P-Q)&=0\\
U-W&=0.
\end{aligned}
$$

Tức là

$$
\frac{\partial^2E}{\partial x'^2}-\frac1{c^2}\frac{\partial^2E}{\partial t'^2}=0.
$$

Hệ số vận tốc trong phương trình vẫn là $c$, nên sóng truyền trong chân không với cùng tốc độ $c$ trong hai hệ quán tính. Khi biến đổi toàn bộ trường điện từ, các thành phần điện trường và từ trường cũng phải được biến đổi nhất quán. Phép đổi biến ở đây chỉ làm rõ tính bất biến của toán tử sóng.

:::
