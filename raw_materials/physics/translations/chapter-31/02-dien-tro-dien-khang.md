## 31.2. Điện trở và điện kháng

Với cùng một điện áp xoay chiều, vì sao thay điện trở bằng cuộn cảm hoặc tụ điện lại làm đổi cả độ lớn lẫn thời điểm đạt cực đại của dòng? Ta xét riêng từng phần tử khi dòng hình sin đã ổn định. Chọn dòng làm mốc pha:

$$
i(t)=I\cos\omega t.
$$

Trong các sơ đồ dưới đây, chiều dương của dòng đi ngược chiều kim đồng hồ. Điện áp trên phần tử được lấy bằng điện thế đầu a trừ điện thế đầu b.

### Điện trở trong mạch xoay chiều

Với điện trở thuần $R$, định luật Ohm áp dụng tại từng thời điểm:

$$
\begin{aligned}
v_R&=iR\\
&=IR\cos\omega t.\tag{31.6}
\end{aligned}
$$

Biên độ điện áp là

$$
V_R=IR.\tag{31.7}
$$

Do đó

$$
v_R=V_R\cos\omega t.\tag{31.8}
$$

Điện áp và dòng cùng tỉ lệ với $\cos\omega t$, nên chúng **cùng pha**. Hai đại lượng đạt cực đại, bằng không và đạt cực tiểu cùng lúc.

![Hình 31.7: Điện trở nối với nguồn xoay chiều, đồ thị điện áp và dòng cùng pha, cùng giản đồ pha tương ứng.](../img/young-31/hinh-31-07.png)

Thang đứng của dòng và điện áp trong Hình 31.7b khác nhau. Vì vậy chiều cao hai đường không thể được dùng để so trực tiếp số đo bằng ampe với số đo bằng vôn. Trong giản đồ pha, hai vector quay cùng tần số và luôn song song, cùng chiều.

### Cuộn cảm trong mạch xoay chiều

Thay điện trở bằng cuộn cảm thuần có điện cảm $L$ và điện trở bằng không. Dù không có điện trở, dòng biến thiên vẫn gây ra suất điện động tự cảm.

![Hình 31.8: Với cuộn cảm thuần, điện áp sớm pha hơn dòng một phần tư chu kỳ, tương ứng góc 90 độ.](../img/young-31/hinh-31-08.png)

Suất điện động tự cảm theo chiều dương của dòng là

$$
\mathcal E_L=-L\frac{di}{dt}.
$$

Điện áp đầu a so với đầu b có dấu ngược lại:

$$
v_L=+L\frac{di}{dt}.
$$

Chẳng hạn, khi dòng dương từ a sang b đang tăng, suất điện động cảm ứng chống lại sự tăng đó. Đầu a phải ở điện thế cao hơn đầu b để duy trì dòng tăng, nên $v_L>0$.

::: info Xác định dấu điện áp cuộn cảm
Điện áp do dấu của $di/dt$ quyết định, không chỉ do dấu của dòng. Dòng dương đang giảm cho $di/dt<0$ và $v_L<0$. Dòng âm đang tăng về độ lớn cũng cho đạo hàm âm. Dòng âm đang giảm về độ lớn cho đạo hàm dương.

Các trường hợp này đều tuân theo cùng một quy ước đầu a, đầu b. Không đổi quy ước điện áp khi dòng đổi chiều.
:::

Lấy đạo hàm dòng hình sin:

$$
\begin{aligned}
v_L&=L\frac d{dt}(I\cos\omega t)\\
&=-I\omega L\sin\omega t.\tag{31.9}
\end{aligned}
$$

Điện áp lớn nhất về độ lớn khi đồ thị dòng dốc nhất. Điện áp bằng không khi dòng ở cực đại hoặc cực tiểu. Các đỉnh điện áp xuất hiện trước các đỉnh dòng một phần tư chu kỳ.

Vì $\cos(\theta+\pi/2)=-\sin\theta$, ta viết

$$
v_L=I\omega L\cos\left(\omega t+\frac\pi2\right).\tag{31.10}
$$

Điện áp **sớm pha hơn dòng 90 độ**. Vector pha điện áp nằm trước vector pha dòng 90 độ theo chiều quay ngược kim đồng hồ.

Ta luôn mô tả pha điện áp so với dòng. Khi $i=I\cos\omega t$ và $v=V\cos(\omega t+\phi)$, $\phi$ là góc pha của điện áp so với dòng. Điện trở thuần có $\phi=0$, còn cuộn cảm thuần có $\phi=\pi/2$.

Biên độ điện áp cuộn cảm là

$$
V_L=I\omega L.\tag{31.11}
$$

Định nghĩa **cảm kháng**

$$
X_L=\omega L.\tag{31.12}
$$

Khi đó

$$
V_L=IX_L.\tag{31.13}
$$

Cảm kháng có đơn vị ôm, vì nó là tỉ số giữa biên độ điện áp và biên độ dòng.

::: warning Quan hệ biên độ khác quan hệ tức thời
Công thức $V_L=IX_L$ liên hệ hai biên độ. Không được thay bằng $v_L=iX_L$, vì điện áp và dòng lệch pha 90 độ. Quan hệ tức thời đúng là $v_L=L\,di/dt$.
:::

### Ý nghĩa của cảm kháng

Cảm kháng mô tả tác dụng của suất điện động tự cảm chống lại sự biến thiên dòng. Với cùng biên độ dòng, tăng tần số hoặc tăng điện cảm làm tăng tốc độ biến thiên từ thông và tăng biên độ điện áp cuộn.

Ngược lại, nếu giữ biên độ điện áp trên cuộn không đổi:

$$
I=\frac{V_L}{\omega L}.
$$

Tần số càng cao thì biên độ dòng càng nhỏ. Cuộn cảm có thể được dùng trong nguồn điện và mạch chống nhiễu để hạn chế tín hiệu tần số cao, đồng thời cho tần số thấp hoặc dòng một chiều đi qua. Đây là một nguyên lý của bộ lọc thông thấp, sẽ được phân tích ở Bài 31.48.

::: example Ví dụ 31.2: Cuộn cảm trong máy thu radio
Một cuộn cảm thuần trong máy thu cần biên độ dòng $250\,\mu\mathrm A$ khi điện áp trên cuộn có biên độ 3,60 V và tần số 1,60 MHz. (a) Cần cảm kháng và điện cảm bao nhiêu? (b) Giữ biên độ điện áp không đổi, tìm biên độ dòng ở 16,0 MHz và 160 kHz.

**Nhận dạng và chuẩn bị:** Các phần tử khác chỉ cung cấp điện áp hình sin cho cuộn đang xét. Dùng tỉ số biên độ để tìm $X_L$, rồi dùng $X_L=2\pi fL$ để tìm $L$.

**Lời giải:**

(a) Cảm kháng tại 1,60 MHz:

$$
\begin{aligned}
X_L&=\frac{V_L}{I}\\
&=\frac{3{,}60\,\mathrm V}{250\times10^{-6}\,\mathrm A}\\
&=1{,}44\times10^4\,\Omega\\
&=14{,}4\,\mathrm{k\Omega}.
\end{aligned}
$$

Điện cảm:

$$
\begin{aligned}
L&=\frac{X_L}{2\pi f}\\
&\approx1{,}43\times10^{-3}\,\mathrm H\\
&=1{,}43\,\mathrm{mH}.
\end{aligned}
$$

(b) Với $V_L$ và $L$ không đổi, $I$ tỉ lệ nghịch với $f$. Ở 16,0 MHz, tần số tăng 10 lần nên dòng giảm 10 lần, còn $25{,}0\,\mu\mathrm A$. Ở 160 kHz, tần số giảm 10 lần nên dòng tăng 10 lần, thành $2{,}50\,\mathrm{mA}$.

**Đánh giá:** Cuộn cảm đáp ứng bằng dòng lớn hơn khi điện áp cùng biên độ biến thiên chậm hơn. Điện kháng là tỉ số biên độ điện áp và dòng, còn cảm kháng bằng tích điện cảm với tần số góc.
:::

### Tụ điện trong mạch xoay chiều

Nối tụ có điện dung $C$ với nguồn. Gọi $q$ là điện tích bản trái, còn bản phải mang điện tích $-q$. Dòng dương làm điện tích bản trái tăng:

$$
\begin{aligned}
i&=\frac{dq}{dt},\\
i&=I\cos\omega t.
\end{aligned}
$$

![Hình 31.9: Tụ nối với nguồn xoay chiều, đồ thị điện áp và dòng cùng giản đồ pha cho thấy điện áp trễ dòng một phần tư chu kỳ.](../img/young-31/hinh-31-09.png)

::: warning Dòng qua tụ có nghĩa gì?
Điện tích không dẫn xuyên qua khe cách điện giữa hai bản. Khi tụ nạp và phóng, dòng đi vào một bản và dòng đi ra bản kia có cùng độ lớn. Giữa hai bản có dòng điện dịch tương ứng.

Cách nói “dòng xoay chiều qua tụ” mô tả sự liên tục này, không có nghĩa electron đi xuyên qua điện môi.
:::

Tích phân dòng cho điện tích. Với trạng thái xoay chiều đang xét, không có thành phần điện tích không đổi:

$$
q=\frac I\omega\sin\omega t.\tag{31.14}
$$

Hằng số tích phân bằng không là điều kiện của mô hình này. Nếu tụ có điện tích một chiều ban đầu chưa được loại bỏ, phải xét thêm thành phần đó thay vì bỏ hằng số tùy ý.

Vì $q=Cv_C$:

$$
v_C=\frac I{\omega C}\sin\omega t.\tag{31.15}
$$

Điện áp tụ tỉ lệ với điện tích, còn dòng tỉ lệ với tốc độ biến thiên điện áp:

$$
i=C\frac{dv_C}{dt}.
$$

Do đó dòng lớn nhất về độ lớn khi đường điện áp dốc nhất, và dòng bằng không khi điện áp đạt cực trị. Đỉnh điện áp đến sau đỉnh dòng một phần tư chu kỳ.

Từ $\cos(\theta-\pi/2)=\sin\theta$:

$$
v_C=\frac I{\omega C}\cos\left(\omega t-\frac\pi2\right).\tag{31.16}
$$

Điện áp **trễ pha hơn dòng 90 độ**, tức $\phi=-\pi/2$. Vector pha điện áp nằm sau vector pha dòng một phần tư vòng quay.

Biên độ điện áp là

$$
V_C=\frac I{\omega C}.\tag{31.17}
$$

Định nghĩa **dung kháng**

$$
X_C=\frac1{\omega C}.\tag{31.18}
$$

Khi đó

$$
V_C=IX_C.\tag{31.19}
$$

Đơn vị dung kháng cũng là ôm.

::: warning Điện áp và dòng trên tụ lệch pha
Quan hệ $V_C=IX_C$ chỉ liên hệ biên độ. Điện áp tức thời không bằng dòng tức thời nhân dung kháng. Muốn xét tức thời, dùng $q=Cv_C$ và $i=dq/dt$.
:::

### Ý nghĩa của dung kháng

Dung kháng giảm khi điện dung hoặc tần số tăng. Vì vậy tụ hạn chế dòng tần số thấp và chặn dòng một chiều ở trạng thái ổn định, nhưng cho dòng tần số cao đi qua dễ hơn. Đây là nguyên lý của bộ lọc thông cao ở Bài 31.47.

::: example Ví dụ 31.3: Điện trở và tụ nối tiếp
Điện trở $R=200\,\Omega$ nối tiếp tụ $C=5{,}0\,\mu\mathrm F$. Điện áp trên điện trở là

$$
\begin{aligned}
v_R&=(1{,}20\,\mathrm V)\cos\theta,\\
\theta&=(2500\,\mathrm{rad/s})t.
\end{aligned}
$$

Tìm (a) biểu thức dòng trong mạch, (b) dung kháng, (c) biểu thức điện áp trên tụ.

![Hình 31.10: Mạch điện trở và tụ nối tiếp với điện áp điện trở đã biết, dùng để xác định dòng và điện áp tụ.](../img/young-31/hinh-31-10.png)

**Nhận dạng và chuẩn bị:** Hai phần tử nối tiếp có cùng dòng tại mỗi thời điểm. Điện trở cho phép tìm dòng bằng định luật Ohm. Sau đó dùng dung kháng và độ trễ pha của tụ.

**Lời giải:**

(a) Biên độ dòng:

$$
\begin{aligned}
I&=\frac{V_R}{R}\\
&=\frac{1{,}20\,\mathrm V}{200\,\Omega}\\
&=6{,}0\times10^{-3}\,\mathrm A.
\end{aligned}
$$

Vì dòng cùng pha điện áp điện trở:

$$
i=(6{,}0\,\mathrm{mA})\cos\theta.
$$

(b) Dung kháng:

$$
\begin{aligned}
X_C&=\frac1{\omega C}\\
&=\frac1{2500(5{,}0\times10^{-6})}\,\Omega\\
&=80\,\Omega.
\end{aligned}
$$

(c) Biên độ điện áp tụ:

$$
\begin{aligned}
V_C&=IX_C\\
&=(6{,}0\times10^{-3})(80)\,\mathrm V\\
&=0{,}48\,\mathrm V.
\end{aligned}
$$

Điện áp tụ trễ dòng $\pi/2$ rad:

$$
\begin{aligned}
v_C&=(0{,}48\,\mathrm V)\cos\theta,\\
\theta&=(2500\,\mathrm{rad/s})t-\frac\pi2.
\end{aligned}
$$

**Đánh giá:** Dung kháng bằng 40% điện trở nên biên độ điện áp tụ bằng 40% biên độ điện áp điện trở. Cùng dòng không có nghĩa cùng điện áp. Hai điện áp khác cả biên độ lẫn pha.

Khi viết đối số của hàm lượng giác, cần dùng thống nhất đơn vị góc. Góc pha 90 độ đã được đổi thành $\pi/2$ rad để ghép với $\omega t$.
:::

### So sánh ba phần tử

Bảng 31.1 dưới đây dùng biên độ và mô tả pha điện áp so với dòng.

| Phần tử | Biên độ điện áp | Đại lượng mạch | Pha điện áp |
| --- | --- | --- | --- |
| Điện trở | $V_R=IR$ | $R$ | Cùng pha |
| Cuộn cảm | $V_L=IX_L$ | $X_L=\omega L$ | Sớm 90 độ |
| Tụ điện | $V_C=IX_C$ | $X_C=1/(\omega C)$ | Trễ 90 độ |

Chỉ điện trở thuần có điện áp tức thời tỉ lệ với dòng tức thời. Với cuộn cảm và tụ, độ lệch pha phải được giữ khi phân tích mạch.

![Hình 31.11: Điện trở không đổi theo tần số trong mô hình lý tưởng, cảm kháng tăng còn dung kháng giảm khi tần số góc tăng.](../img/young-31/hinh-31-11.png)

Trong giới hạn một chiều $\omega\to0$, dung kháng tiến tới vô hạn nên tụ không có dòng ở trạng thái ổn định. Cảm kháng tiến tới không, nhưng kết luận này không loại bỏ suất điện động tự cảm trong giai đoạn quá độ khi vừa đóng mạch.

Khi $\omega\to\infty$, cảm kháng tăng không giới hạn và dòng cuộn cảm giảm về không nếu giữ biên độ điện áp. Dung kháng giảm về không. Với biên độ dòng cố định, điện áp tụ giảm vì dòng đổi chiều quá nhanh để tích lũy nhiều điện tích trên bản.

### Ứng dụng: Phân chia tín hiệu trong loa

![Hình 31.12: Mạng phân tần đưa tín hiệu thấp chủ yếu đến loa trầm và tín hiệu cao chủ yếu đến loa cao, cùng đồ thị dòng hiệu dụng theo tần số.](../img/young-31/hinh-31-12.png)

Loa trầm có đường kính lớn, phụ trách âm thấp. Loa cao có đường kính nhỏ, phụ trách âm cao. Hai nhánh loa được nối song song vào ngõ ra bộ khuếch đại.

Tụ ở nhánh loa cao hạn chế thành phần tần số thấp. Cuộn cảm ở nhánh loa trầm hạn chế thành phần tần số cao. Vì vậy cùng một tín hiệu âm nhạc được phân chia cho hai loa theo khả năng đáp ứng của chúng.

### Câu hỏi tự kiểm 31.2

Một điện áp hình sin có biên độ cố định được đặt lên một phần tử. Khi tăng tần số, biên độ dòng (i) tăng, (ii) giảm hay (iii) không đổi nếu phần tử là (a) điện trở, (b) cuộn cảm, (c) tụ điện?

<details><summary>Xem đáp án và giải thích</summary>

(a) Chọn (iii), vì $I=V_R/R$ không phụ thuộc tần số trong mô hình điện trở lý tưởng.

(b) Chọn (ii), vì

$$
I=\frac{V_L}{\omega L}.
$$

(c) Chọn (i), vì

$$
I=V_C\omega C.
$$

Trong cả ba trường hợp, giữ cố định biên độ điện áp trên chính phần tử đang xét. Nếu thay đổi cả cấu trúc mạch, không thể dùng kết luận này mà bỏ qua điện áp thực tế trên từng phần tử.

</details>
