## 31.5. Cộng hưởng trong mạch xoay chiều

Máy thu radio nhận nhiều tín hiệu cùng lúc. Vì sao chỉnh núm dò đài lại làm một tín hiệu được đáp ứng mạnh hơn những tín hiệu khác? Một mạch RLC có thể cho dòng lớn nhất tại một tần số xác định.

Một tín hiệu tạo dòng cùng tần số với nó trong mạch thu. Tuy nhiên, biên độ dòng phụ thuộc trở kháng tại tần số ấy. Mạch được chỉnh để tín hiệu mong muốn có đáp ứng lớn, còn các tín hiệu khác tạo dòng nhỏ hơn.

### Thay đổi tần số nguồn

Giữ biên độ điện áp nguồn $V$ không đổi và thay đổi tần số góc. Với mạch RLC nối tiếp:

$$
\begin{aligned}
I&=\frac VZ,\\
Z&=\sqrt{R^2+(X_L-X_C)^2},\\
X_L&=\omega L,\\
X_C&=\frac1{\omega C}.
\end{aligned}
$$

![Hình 31.18: Trở kháng đạt cực tiểu và biên độ dòng đạt cực đại khi cảm kháng bằng dung kháng, đồng thời góc pha đổi dấu qua cộng hưởng.](../img/young-31/hinh-31-18.png)

Hình 31.18 dùng thang tần số góc logarit để biểu diễn một khoảng tần số rộng. Khi tần số tăng, cảm kháng tăng còn dung kháng giảm. Có một tần số dương làm hai điện kháng bằng nhau.

Tại đó, $X_L-X_C=0$ và trở kháng nhỏ nhất bằng $R$. Với $R>0$, dòng đạt biên độ lớn nhất $V/R$. Sự xuất hiện đỉnh đáp ứng này gọi là **cộng hưởng**.

### Tần số cộng hưởng

Gọi $\omega_0$ là tần số góc cộng hưởng. Điều kiện hai điện kháng bằng nhau cho

$$
\begin{aligned}
\omega_0L&=\frac1{\omega_0C},\\
\omega_0^2LC&=1.
\end{aligned}
$$

Do đó

$$
\omega_0=\frac1{\sqrt{LC}}.\tag{31.32}
$$

Tần số theo hertz là

$$
f_0=\frac{\omega_0}{2\pi}.
$$

Tần số này bằng tần số dao động riêng của mạch LC không có điện trở. Ở đây ta đang nói về cực đại biên độ dòng khi giữ biên độ điện áp nguồn không đổi. Không đồng nhất nó với mọi cực đại điện áp trên một phần tử hoặc với tần số dao động tự do đã tắt dần.

### Điện áp tại cộng hưởng

Dòng qua cuộn cảm và tụ luôn bằng nhau vì chúng nối tiếp. Hai điện áp lệch pha nhau 180 độ. Tại cộng hưởng, hai biên độ bằng nhau vì $X_L=X_C$.

Vì vậy chúng không chỉ có cùng độ lớn mà còn triệt tiêu tại từng thời điểm:

$$
\begin{aligned}
v_L+v_C&=0,\\
v_{bd}&=0,\\
v_R&=v.
\end{aligned}
$$

Điện áp nguồn bằng điện áp điện trở. Xét từ hai đầu nguồn, mạch có trở kháng và pha như điện trở thuần. Điều này không có nghĩa năng lượng điện trường và từ trường biến mất hoặc điện áp từng phần tử bằng không.

Khi tần số thấp hơn cộng hưởng, $X_C>X_L$, mạch có góc pha âm và điện áp trễ dòng. Khi tần số cao hơn cộng hưởng, $X_L>X_C$, góc pha dương và điện áp sớm dòng. Tại cộng hưởng, điện áp nguồn và dòng cùng pha.

### Chỉnh tần số và độ rộng đáp ứng

Thay đổi $L$ hoặc $C$ làm đổi tần số cộng hưởng. Trong một kiểu máy thu, núm dò đài thay đổi diện tích chồng lên nhau của các bản tụ. Một cách khác là dịch lõi ferrite vào hoặc ra khỏi cuộn dây để thay điện cảm.

![Hình 31.19: Các đường đáp ứng dòng với ba điện trở khác nhau, cho thấy điện trở nhỏ tạo đỉnh cộng hưởng cao và hẹp hơn.](../img/young-31/hinh-31-19.png)

Trong Hình 31.19, nguồn có biên độ 100 V, $L=2{,}0\,\mathrm H$ và $C=0{,}50\,\mu\mathrm F$. Cả ba đường đều có

$$
\omega_0=1000\,\mathrm{rad/s}.
$$

Với $R=200\,\Omega$, $500\,\Omega$ và $2000\,\Omega$, biên độ dòng tại đỉnh lần lượt là 0,50 A, 0,20 A và 0,050 A.

Xa cộng hưởng, một điện kháng lớn chi phối trở kháng nên các đường gần nhau hơn. Gần cộng hưởng, hai điện kháng gần triệt tiêu và điện trở quyết định độ cao, độ rộng của đỉnh. Điện trở nhỏ cho đỉnh cao, hẹp. Điện trở lớn cho đỉnh thấp, rộng.

Đỉnh hẹp giúp phân biệt hai đài ở các tần số gần nhau. Nhưng nếu quá hẹp, mạch có thể loại cả những thành phần mang thông tin của tín hiệu mong muốn, chẳng hạn các thành phần tương ứng âm cao trong nhạc.

Mối liên hệ với tắt dần cũng rõ ở đây. Điện trở nhỏ tương ứng tắt dần yếu và đáp ứng nhọn. Điện trở lớn tương ứng tắt dần mạnh và đáp ứng rộng. Cộng hưởng cũng có ở mạch song song, như Bài 31.54 và 31.55, nhưng cần phân tích đúng cách nối.

Hiện tượng tương tự xuất hiện trong cơ học và âm học. Dao động cưỡng bức có thể đạt biên độ lớn khi tần số lực kích thích gần một tần số riêng của hệ, tương tự dòng tăng mạnh trong mạch được kích thích gần cộng hưởng.

::: example Ví dụ 31.8: Chỉnh đài radio
Mạch RLC nối tiếp có $R=500\,\Omega$, $L=0{,}40\,\mathrm{mH}$ và $C=100\,\mathrm{pF}$. Nguồn thay đổi được tần số và giữ điện áp hiệu dụng 1,0 V.

Tìm (a) tần số cộng hưởng, (b) cảm kháng, dung kháng và trở kháng tại cộng hưởng, (c) dòng hiệu dụng, (d) điện áp hiệu dụng trên mỗi phần tử.

![Hình 31.20: Mạch dò đài tại cộng hưởng với các đồng hồ lý tưởng chỉ dòng và điện áp hiệu dụng.](../img/young-31/hinh-31-20.png)

**Nhận dạng và chuẩn bị:** Dùng điều kiện $X_L=X_C$ để tìm tần số. Tại cộng hưởng, $Z=R$. Các đồng hồ lý tưởng không làm đổi mạch và đều chỉ giá trị hiệu dụng.

**Lời giải:**

(a) Tần số góc và tần số:

$$
\begin{aligned}
\omega_0&=\frac1{\sqrt{LC}}\\
&=5{,}0\times10^6\,\mathrm{rad/s},\\
f_0&=\frac{\omega_0}{2\pi}\\
&\approx8{,}0\times10^5\,\mathrm{Hz}\\
&=800\,\mathrm{kHz}.
\end{aligned}
$$

Đây là tần số ở phần thấp của dải AM được xét trong ví dụ.

(b) Hai điện kháng:

$$
\begin{aligned}
X_L&=\omega_0L=2000\,\Omega,\\
X_C&=\frac1{\omega_0C}=2000\,\Omega.
\end{aligned}
$$

Chúng bằng nhau, nên $Z=R=500\,\Omega$.

(c) Dòng hiệu dụng:

$$
\begin{aligned}
I_{\mathrm{rms}}&=\frac{V_{\mathrm{rms}}}{R}\\
&=\frac{1{,}0\,\mathrm V}{500\,\Omega}\\
&=2{,}0\,\mathrm{mA}.
\end{aligned}
$$

(d) Điện áp hiệu dụng từng phần tử:

$$
\begin{aligned}
V_{R,\mathrm{rms}}&=I_{\mathrm{rms}}R=1{,}0\,\mathrm V,\\
V_{L,\mathrm{rms}}&=I_{\mathrm{rms}}X_L=4{,}0\,\mathrm V,\\
V_{C,\mathrm{rms}}&=I_{\mathrm{rms}}X_C=4{,}0\,\mathrm V.
\end{aligned}
$$

**Đánh giá:** Điện áp cuộn và tụ cùng hiệu dụng 4,0 V nhưng ngược pha, nên điện áp tức thời tổng qua hai phần tử bằng không. Điện áp hiệu dụng nguồn chỉ 1,0 V dù từng phần tử phản kháng có điện áp hiệu dụng lớn hơn.
:::

### Câu hỏi tự kiểm 31.5

Tần số cộng hưởng của mạch RLC nối tiếp đổi thế nào nếu đưa các bản tụ lại gần nhau? (i) Tăng. (ii) Giảm. (iii) Không đổi.

<details><summary>Xem đáp án và giải thích</summary>

Chọn (ii). Với diện tích bản và điện môi giữ nguyên, giảm khoảng cách bản làm điện dung tăng. Từ

$$
f_0=\frac1{2\pi\sqrt{LC}}:
$$

điện dung tăng làm tần số cộng hưởng giảm.

</details>
