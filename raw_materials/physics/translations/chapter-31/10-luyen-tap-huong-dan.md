## Luyện tập có hướng dẫn

### Điện trở, cảm kháng và dung kháng

Ôn Ví dụ 31.2 và 31.3 trước khi giải bốn bài sau. Các điện áp trên điện trở và tụ cùng một mạch nối tiếp có thể khác cả biên độ lẫn pha.

::: exercise VP31.3.1
Cuộn cảm $L=2{,}50\,\mathrm{mH}$ thuộc mạch đài dẫn đường vô tuyến hàng không hoạt động ở 108 MHz.

(a) Tìm cảm kháng. (b) Tìm biên độ dòng nếu biên độ điện áp trên cuộn là 4,20 kV.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết điện cảm, tần số và biên độ điện áp. Cần tìm $X_L$ và $I$.

**Hướng đi:**

- Dùng $X_L=2\pi fL$ vì phần tử đang xét là cuộn cảm thuần ở tần số đã biết.
- Dùng $V_L=IX_L$ để liên hệ các biên độ. Quan hệ này không đòi hỏi điện áp và dòng cùng pha.

**Lời giải:**

(a) Đổi $L$ sang henry và $f$ sang hertz:

$$
\begin{aligned}
X_L &= 2\pi fL \\
&= 2\pi(108\times10^6) \times(2{,}50\times10^{-3})\,\Omega \\
&\approx 1{,}70\times10^6\,\Omega.
\end{aligned}
$$

(b) Với điện áp biên độ $4200\,\mathrm V$:

$$
\begin{aligned}
I &= \frac{V_L}{X_L} \\
&\approx 2{,}48\times10^{-3}\,\mathrm A \\
&= 2{,}48\,\mathrm{mA}.
\end{aligned}
$$

:::

::: exercise VP31.3.2
Điện trở $R=125\,\Omega$ nối tiếp tụ $C=7{,}00\,\mu\mathrm F$. Dòng trong mạch là

$$
\begin{aligned}
i(t) &= (2{,}40\,\mathrm{mA})\cos\theta, \\
\theta &= (1{,}75\times10^3\,\mathrm{rad/s})t.
\end{aligned}
$$

Tìm (a) điện áp điện trở theo thời gian, (b) dung kháng, (c) điện áp tụ theo thời gian.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết dòng hình sin chung, điện trở và điện dung. Cần tìm $v_R$, $X_C$, $v_C$.

**Hướng đi:**

- Dùng $v_R=iR$ vì điện trở thuần có điện áp cùng pha dòng.
- Dùng $X_C=1/(\omega C)$ để tính tỉ số biên độ điện áp và dòng trên tụ.
- Giữ độ trễ $\pi/2$ của điện áp tụ để viết biểu thức tức thời, thay vì chỉ thay biên độ.

**Lời giải:**

(a) Biên độ điện áp điện trở:

$$
\begin{aligned}
V_R &= IR \\
&= (2{,}40\times10^{-3})(125)\,\mathrm V \\
&= 0{,}300\,\mathrm V.
\end{aligned}
$$

Do đó $v_R=(0{,}300\,\mathrm V)\cos\theta$.

(b) Dung kháng:

$$
\begin{aligned}
X_C &= \frac1{\omega C} \\
&\approx 81{,}6\,\Omega.
\end{aligned}
$$

(c) Biên độ $V_C=IX_C\approx0{,}196\,\mathrm V$. Điện áp:

$$
\begin{aligned}
v_C &= V_C\cos(\theta-\pi/2), \\
V_C &= 0{,}196\,\mathrm V.
\end{aligned}
$$

Trong cả hai biểu thức, $\theta$ có cùng định nghĩa như đề bài.
:::

::: exercise VP31.3.3
Điện trở $155\,\Omega$ nối tiếp tụ $8{,}00\,\mu\mathrm F$. Biên độ dòng là $4{,}00\,\mathrm{mA}$.

(a) Tìm tần số để dung kháng bằng điện trở. (b) Tại đó, tìm biên độ điện áp trên điện trở và tụ. (c) Khi điện áp điện trở cực đại, điện áp tụ bằng bao nhiêu? Khi điện áp tụ cực đại, điện áp điện trở bằng bao nhiêu?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mạch RC có dòng biên độ đã biết và điều kiện $X_C=R$.

**Hướng đi:**

- Giải $1/(2\pi fC)=R$ vì tần số cần tìm được xác định bởi sự bằng nhau của hai đại lượng đó.
- Dùng $V_R=IR$, $V_C=IX_C$ vì dòng nối tiếp chung.
- Dùng độ lệch pha 90 độ để suy điện áp tức thời khi điện áp kia đạt cực đại.

**Lời giải:**

(a)

$$
\begin{aligned}
f &= \frac1{2\pi RC} \\
&\approx 128\,\mathrm{Hz}.
\end{aligned}
$$

(b) Vì $X_C=R$, hai biên độ bằng nhau:

$$
\begin{aligned}
V_R &= IR=0{,}620\,\mathrm V, \\
V_C &= IX_C=0{,}620\,\mathrm V.
\end{aligned}
$$

(c) Chọn $v_R=V_R\cos\omega t$, khi đó $v_C=V_C\sin\omega t$. Khi cosin đạt cực đại dương, sin bằng không. Khi sin đạt cực đại dương, cosin bằng không. Hai điện áp được hỏi đều bằng không.
:::

::: exercise VP31.3.4
Điện trở $116\,\Omega$ nối tiếp một tụ chưa biết điện dung. Tần số góc nguồn là $5{,}10\times10^3\,\mathrm{rad/s}$. Biên độ điện áp điện trở là 2,45 V. Dòng đạt cực đại dương tại $t=0$.

Tìm (a) biên độ dòng, (b) dòng tại 3,50 ms, (c) điện áp cực đại trên tụ, (d) điện dung.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết $R$, $\omega$, $V_R$ và pha dòng. Chưa có điện dung hoặc điện áp nguồn.

**Hướng đi:**

- Dùng $I=V_R/R$ vì điện áp điện trở xác định biên độ dòng chung.
- Dùng cosin có pha đầu bằng không vì dòng cực đại dương tại gốc thời gian.
- Xét số dữ kiện độc lập trước khi tìm $V_C$ và $C$. Một quan hệ giữa hai ẩn chưa đủ xác định riêng từng ẩn.

**Lời giải:**

(a)

$$
\begin{aligned}
I &= \frac{2{,}45\,\mathrm V}{116\,\Omega} \\
&\approx 0{,}0211\,\mathrm A.
\end{aligned}
$$

(b) Tại 3,50 ms, pha là

$$
\omega t=17{,}85\,\mathrm{rad}.
$$

Suy ra

$$
\begin{aligned}
i &= I\cos(17{,}85) \\
&\approx 0{,}0114\,\mathrm A.
\end{aligned}
$$

(c), (d) Dữ kiện chưa xác định riêng biên độ điện áp tụ và điện dung. Ta chỉ có quan hệ

$$
\begin{aligned}
V_C &= \frac I{\omega C}, \\
C &= \frac I{\omega V_C}.
\end{aligned}
$$

Mỗi điện dung dương phù hợp với một biên độ điện áp tụ khác nhau. Cần thêm một dữ kiện độc lập, chẳng hạn điện áp nguồn hoặc điện áp tụ, để cho hai đáp số số học duy nhất. Không thể suy $V_C=V_R$ chỉ từ việc hai phần tử nối tiếp.
:::

### Mạch RLC nối tiếp

Ôn Ví dụ 31.4 và 31.5. Các bài dưới dùng mạch ba phần tử nối tiếp có cùng dòng tại mọi thời điểm.

![Hình 31.13: Mạch RLC nối tiếp và cách cộng các vector điện áp để xác định điện áp nguồn.](img/young-31/hinh-31-13.png)

::: exercise VP31.5.1
Mạch RLC nối tiếp có $R=255\,\Omega$, $L=45{,}0\,\mathrm{mH}$, $C=0{,}400\,\mu\mathrm F$ và biên độ nguồn 55,0 V. Cảm kháng bằng điện trở.

Tìm (a) tần số nguồn, (b) trở kháng, (c) biên độ dòng, (d) góc pha, (e) điện áp sớm hay trễ dòng.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết ba phần tử, biên độ nguồn và $X_L=R$. Tần số chưa biết.

**Hướng đi:**

- Dùng $\omega L=R$ vì điều kiện cảm kháng xác định tần số.
- Tính dung kháng ở chính tần số ấy rồi dùng tổng vector điện áp để tìm $Z$.
- Dùng $I=V/Z$ và dấu $X_L-X_C$ để xác định biên độ cùng chiều lệch pha.

**Lời giải:**

(a)

$$
\begin{aligned}
\omega &= \frac RL \\
&\approx 5{,}67\times10^3\,\mathrm{rad/s}, \\
f &= \frac{\omega}{2\pi}\approx902\,\mathrm{Hz}.
\end{aligned}
$$

(b) Hai điện kháng là $X_L=255\,\Omega$ và $X_C\approx441\,\Omega$. Do đó

$$
\begin{aligned}
Z &= \sqrt{R^2+(X_L-X_C)^2} \\
&\approx 316\,\Omega.
\end{aligned}
$$

(c) $I=V/Z\approx0{,}174\,\mathrm A$.

(d)

$$
\begin{aligned}
\phi &= \arctan\frac{X_L-X_C}{R} \\
&\approx -36{,}1^\circ.
\end{aligned}
$$

(e) Góc âm cho biết điện áp nguồn trễ dòng. Dung kháng lớn hơn cảm kháng, phù hợp kết luận này.
:::

::: exercise VP31.5.2
Nguồn mạch RLC nối tiếp có biên độ 20,0 V và tần số góc $5{,}40\times10^3\,\mathrm{rad/s}$. Cho $L=6{,}50\,\mathrm{mH}$, $C=0{,}600\,\mu\mathrm F$, $Z=474\,\Omega$.

Tìm (a) điện trở, (b) biên độ dòng, (c) biên độ điện áp điện trở, (d) biên độ điện áp cuộn, (e) biên độ điện áp tụ.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết $Z$, $L$, $C$, $\omega$ và $V$. Cần suy $R$ trước khi tính điện áp từng phần tử.

**Hướng đi:**

- Tính hai điện kháng từ tần số góc vì trở kháng chứa cả phần điện trở lẫn phần phản kháng.
- Giải công thức $Z^2=R^2+(X_L-X_C)^2$, chọn điện trở không âm.
- Dùng dòng chung để tìm ba biên độ điện áp.

**Lời giải:**

Hai điện kháng:

$$
\begin{aligned}
X_L &= \omega L=35{,}1\,\Omega, \\
X_C &= \frac1{\omega C}\approx309\,\Omega.
\end{aligned}
$$

(a)

$$
\begin{aligned}
R &= \sqrt{Z^2-(X_L-X_C)^2} \\
&\approx 387\,\Omega.
\end{aligned}
$$

(b) $I=V/Z\approx0{,}0422\,\mathrm A$.

(c)–(e)

$$
\begin{aligned}
V_R &= IR\approx16{,}3\,\mathrm V, \\
V_L &= IX_L\approx1{,}48\,\mathrm V, \\
V_C &= IX_C\approx13{,}0\,\mathrm V.
\end{aligned}
$$

Ba biên độ không cộng số học thành 20,0 V, vì điện áp cuộn và tụ khác pha điện áp điện trở.
:::

::: exercise VP31.5.3
Mạch RLC nối tiếp có $\omega=1{,}20\times10^4\,\mathrm{rad/s}$, $C=0{,}965\,\mu\mathrm F$ và $R=65{,}0\,\Omega$. Muốn điện áp nguồn sớm dòng 15,0 độ, tìm (a) $X_L-X_C$, (b) điện cảm cần có.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Góc pha nguồn dương 15,0 độ và các đại lượng $R$, $C$, $\omega$ đã biết.

**Hướng đi:**

- Dùng $\tan\phi=(X_L-X_C)/R$ vì yêu cầu của bài là độ lệch pha nguồn.
- Tìm $X_C$ rồi cộng điện kháng tổng để suy $X_L$. Cuối cùng dùng $L=X_L/\omega$.

**Lời giải:**

(a)

$$
\begin{aligned}
X_L-X_C &= R\tan15{,}0^\circ \\
&\approx 17{,}4\,\Omega.
\end{aligned}
$$

(b) Dung kháng:

$$
X_C=\frac1{\omega C}\approx86{,}4\,\Omega.
$$

Vì vậy

$$
\begin{aligned}
X_L &= X_C+(X_L-X_C), \\
L &= \frac{X_L}{\omega} \\
&\approx 8{,}65\,\mathrm{mH}.
\end{aligned}
$$

:::

::: exercise VP31.5.4
Mạch RLC nối tiếp có biên độ dòng 0,120 A, tần số góc $8{,}00\times10^3\,\mathrm{rad/s}$ và dòng cực đại dương tại $t=0$. Cho $R=95{,}0\,\Omega$, $L=6{,}50\,\mathrm{mH}$, $C=0{,}440\,\mu\mathrm F$.

Với điện trở, cuộn cảm và tụ, tìm (a) các biên độ điện áp, (b) các điện áp tức thời tại 0,305 ms.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết dòng chung và ba phần tử. Cần phân biệt biên độ với giá trị ở một thời điểm.

**Hướng đi:**

- Dùng $IR$, $I\omega L$ và $I/(\omega C)$ để tìm ba biên độ.
- Chọn dòng cosin pha đầu không vì dòng cực đại dương tại gốc.
- Giữ dấu âm trước sin của điện áp cuộn và dấu dương trước sin của điện áp tụ.

**Lời giải:**

(a)

$$
\begin{aligned}
V_R &= IR=11{,}4\,\mathrm V, \\
V_L &= I\omega L=6{,}24\,\mathrm V, \\
V_C &= \frac I{\omega C}\approx34{,}1\,\mathrm V.
\end{aligned}
$$

(b) Pha tại thời điểm đã cho:

$$
\theta=\omega t=2{,}44\,\mathrm{rad}.
$$

Điện áp tức thời:

$$
\begin{aligned}
v_R &= V_R\cos\theta\approx-8{,}71\,\mathrm V, \\
v_L &= -V_L\sin\theta\approx-4{,}03\,\mathrm V, \\
v_C &= V_C\sin\theta\approx22{,}0\,\mathrm V.
\end{aligned}
$$

Dòng đang có dấu âm tại thời điểm này. Dấu điện áp không thể suy chỉ từ biên độ dương.
:::

### Công suất

Ôn Ví dụ 31.6 và 31.7. Công suất được cho trên nhãn tải nhiệt là công suất trung bình, còn điện áp, dòng ở ổ cắm thường được mô tả bằng hiệu dụng.

::: exercise VP31.7.1
Lò nướng bánh lấy dòng hiệu dụng 3,95 A từ ổ điện có điện áp hiệu dụng $1{,}20\times10^2\,\mathrm V$. Tìm (a) công suất trung bình, (b) công suất tức thời lớn nhất, (c) điện trở.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tải nhiệt thuần trở có $I_{\mathrm{rms}}=3{,}95\,\mathrm A$, $V_{\mathrm{rms}}=120\,\mathrm V$.

**Hướng đi:**

- Dùng tích hai giá trị hiệu dụng vì điện áp tải thuần trở cùng pha dòng.
- Dùng công suất đỉnh gấp đôi trung bình vì tích hai hình sin cùng pha tỉ lệ cosin bình phương.
- Dùng tỉ số hiệu dụng để tìm điện trở.

**Lời giải:**

(a)

$$
\begin{aligned}
P_{\mathrm{av}} &= V_{\mathrm{rms}}I_{\mathrm{rms}} \\
&= 474\,\mathrm W.
\end{aligned}
$$

(b) $p_{\max}=2P_{\mathrm{av}}=948\,\mathrm W$.

(c)

$$
R=\frac{V_{\mathrm{rms}}}{I_{\mathrm{rms}}}\approx30{,}4\,\Omega.
$$

:::

::: exercise VP31.7.2
Mạch RLC nối tiếp có biên độ nguồn 35,0 V, $\omega=1{,}30\times10^3\,\mathrm{rad/s}$, $R=275\,\Omega$, $L=82{,}3\,\mathrm{mH}$ và $C=1{,}10\,\mu\mathrm F$.

Tìm (a) hai điện kháng, (b) góc pha, (c) hệ số công suất.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết các phần tử và tần số. Góc pha được lấy cho điện áp nguồn so với dòng.

**Hướng đi:**

- Tính $X_L$, $X_C$ để xác định phần phản kháng tổng.
- Dùng dấu $X_L-X_C$ khi lấy góc arctan, vì cosin riêng không phân biệt góc âm với góc dương.
- Lấy cosin góc pha để tìm hệ số công suất.

**Lời giải:**

(a)

$$
\begin{aligned}
X_L &= \omega L\approx107\,\Omega, \\
X_C &= \frac1{\omega C}\approx699\,\Omega.
\end{aligned}
$$

(b)

$$
\begin{aligned}
\phi &= \arctan\frac{X_L-X_C}{R} \\
&\approx -65{,}1^\circ.
\end{aligned}
$$

(c) $\cos\phi\approx0{,}421$. Góc âm nghĩa điện áp nguồn trễ dòng.
:::

::: exercise VP31.7.3
Với mạch ở VP31.7.2, tìm (a) trở kháng, (b) biên độ dòng, (c) công suất trung bình truyền cho điện trở.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dùng các dữ kiện và hai điện kháng của bài trước. Biên độ nguồn là 35,0 V.

**Hướng đi:**

- Dùng công thức trở kháng nối tiếp vì điện áp phần tử khác pha.
- Dùng tỉ số biên độ nguồn và trở kháng để tìm dòng.
- Dùng $P_R=I^2R/2$ vì $I$ là biên độ, không phải hiệu dụng.

**Lời giải:**

(a)

$$
\begin{aligned}
Z &= \sqrt{R^2+(X_L-X_C)^2} \\
&\approx 653\,\Omega.
\end{aligned}
$$

(b) $I=V/Z\approx0{,}0536\,\mathrm A$.

(c)

$$
\begin{aligned}
P_R &= \frac12I^2R \\
&\approx 0{,}395\,\mathrm W.
\end{aligned}
$$

:::

::: exercise VP31.7.4
Hệ số công suất của mạch RLC nối tiếp là 0,800. Cho $\omega=1{,}30\times10^4\,\mathrm{rad/s}$, $L=7{,}50\,\mathrm{mH}$, $C=0{,}440\,\mu\mathrm F$.

Tìm (a) cảm kháng và dung kháng, (b) góc pha, (c) điện trở.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết hệ số công suất dương và các đại lượng xác định hai điện kháng. Dấu góc pha cần được suy từ mạch.

**Hướng đi:**

- Tính hai điện kháng trước để xác định mạch thiên về cảm hay dung.
- Dùng $\cos\phi=0{,}800$ để tìm độ lớn góc, rồi chọn dấu theo $X_L-X_C$.
- Giải $\tan\phi=(X_L-X_C)/R$, không thay cosin thành góc dương một cách tự động.

**Lời giải:**

(a)

$$
\begin{aligned}
X_L &= \omega L=97{,}5\,\Omega, \\
X_C &= \frac1{\omega C}\approx175\,\Omega.
\end{aligned}
$$

(b) Dung kháng lớn hơn cảm kháng, nên góc âm:

$$
\begin{aligned}
\phi &= -\arccos(0{,}800) \\
&\approx -36{,}9^\circ.
\end{aligned}
$$

(c)

$$
\begin{aligned}
R &= \frac{X_L-X_C}{\tan\phi} \\
&\approx 103\,\Omega.
\end{aligned}
$$

Cả tử và mẫu đều âm, nên điện trở nhận được dương. Dùng giá trị chưa làm tròn của hai điện kháng khi thế số.
:::

## Bài toán cầu nối: Hai tần số cho cùng biên độ dòng

::: exercise Mạch xoay chiều ngoài cộng hưởng
Mạch RLC nối tiếp có $L=1{,}50\,\mathrm{mH}$, $R=125\,\Omega$, $C=25{,}0\,\mathrm{nF}$. Nguồn có điện áp hiệu dụng 35,0 V và thay đổi được tần số.

(a) Tìm các tần số góc làm biên độ dòng bằng một phần ba giá trị lớn nhất có thể có. (b) Tại mỗi tần số ấy, tìm biên độ dòng và biên độ điện áp trên từng phần tử, kể cả nguồn.

![Hình 31.13a: Mạch RLC nối tiếp dùng để tìm hai tần số cho cùng biên độ dòng ngoài cộng hưởng.](img/young-31/hinh-bridge31-01.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biên độ nguồn không đổi. Cần tìm hai tần số ở hai phía cộng hưởng cùng cho $I=I_{\max}/3$, rồi tìm các biên độ.

**Hướng đi:**

- Dùng $I_{\max}=V/R$ vì dòng lớn nhất ở cộng hưởng với trở kháng bằng điện trở.
- Đặt $Z=3R$ vì cùng biên độ nguồn nhưng dòng giảm ba lần.
- Giải hai phương trình điện kháng tổng bằng hai giá trị đối dấu. Chúng mô tả hai phía cộng hưởng.
- Đổi hiệu dụng nguồn sang biên độ trước khi tính dòng và điện áp biên độ.
- Tính từng điện kháng tại từng nghiệm để tìm các điện áp, rồi đối chiếu tổng vector với điện áp nguồn.

**Lời giải:**

(a) Điều kiện trở kháng:

$$
Z=3R.
$$

$$
R^2+(X_L-X_C)^2=9R^2.
$$

$$
X_L-X_C=\pm\sqrt8R.
$$

Đặt $A=\sqrt8R$. Hai phương trình theo tần số là

$$
\begin{aligned}
\omega L-\frac1{\omega C} &= \pm A, \\
L\omega^2\mp A\omega-\frac1C &= 0.
\end{aligned}
$$

Mỗi phương trình có một nghiệm dương. Hai nghiệm cần lấy:

$$
\begin{aligned}
\omega_- &= \frac{-A+\sqrt{A^2+4L/C}}{2L}, \\
\omega_+ &= \frac{A+\sqrt{A^2+4L/C}}{2L}.
\end{aligned}
$$

Thế các đại lượng SI:

$$
\begin{aligned}
\omega_- &\approx 8{,}35\times10^4\,\mathrm{rad/s}, \\
\omega_+ &\approx 3{,}19\times10^5\,\mathrm{rad/s}.
\end{aligned}
$$

(b) Biên độ nguồn:

$$
\begin{aligned}
V &= \sqrt2V_{\mathrm{rms}} \\
&\approx 49{,}5\,\mathrm V.
\end{aligned}
$$

Ở cả hai tần số, $Z=375\,\Omega$ nên

$$
\begin{aligned}
I &= \frac V{3R}\approx0{,}132\,\mathrm A, \\
V_R &= IR\approx16{,}5\,\mathrm V.
\end{aligned}
$$

Tại $\omega_-$:

$$
\begin{aligned}
X_L &\approx 125{,}3\,\Omega, \\
X_C &\approx 478{,}9\,\Omega, \\
V_L &\approx 16{,}5\,\mathrm V, \\
V_C &\approx 63{,}2\,\mathrm V.
\end{aligned}
$$

Tại $\omega_+$, hai điện kháng đổi vai:

$$
\begin{aligned}
X_L &\approx 478{,}9\,\Omega, \\
X_C &\approx 125{,}3\,\Omega, \\
V_L &\approx 63{,}2\,\mathrm V, \\
V_C &\approx 16{,}5\,\mathrm V.
\end{aligned}
$$

Điện áp nguồn có biên độ 49,5 V ở cả hai trường hợp. Một điện áp phản kháng có biên độ lớn hơn nguồn không phải mâu thuẫn. Hai điện áp cuộn và tụ ngược pha, nên phải lấy hiệu của chúng trong tổng vector.
:::
