## Luyện tập có hướng dẫn

### Hỗ cảm và tự cảm

Ôn các Ví dụ 30.1–30.4 trước khi giải bốn bài sau. Từ thông qua một vòng và từ thông móc vòng qua cả cuộn là hai đại lượng cần phân biệt.

::: exercise VP30.4.1
Một ống dây dài, gọi là cuộn 1, được bao quanh ở giữa bởi cuộn 2 ngắn hơn như Hình 30.3. Tại một thời điểm, dòng cuộn 1 bằng $24{,}0\,\mathrm A$ và tăng với tốc độ $2{,}00\,\mathrm{A/s}$. Suất điện động cảm ứng trong cuộn 2 có độ lớn $1{,}30\times10^{-4}\,\mathrm V$.

(a) Tìm hỗ cảm của hai cuộn. (b) Tìm tổng từ thông do cuộn 1 tạo ra móc qua tất cả các vòng của cuộn 2 tại thời điểm đó.

![Hình 30.3: Cuộn ngắn bao quanh phần giữa của ống dây dài.](img/young-30/hinh-30-03.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết dòng nguồn, tốc độ tăng dòng và suất điện động ở cuộn nhận. Cần tìm $M$ và từ thông móc vòng.

**Hướng đi:**

- Dùng $|\mathcal E_2|=M|di_1/dt|$ vì hình học hai cuộn không thay đổi.
- Dùng $N_2\Phi_{B2}=Mi_1$ để tính từ thông của toàn cuộn, không chia thêm cho số vòng chưa biết.

(a) Hỗ cảm là

$$
\begin{aligned}
M &= \frac{1{,}30\times10^{-4}}{2{,}00} \\
&= 6{,}50\times10^{-5}\,\mathrm H.
\end{aligned}
$$

(b) Từ thông móc vòng bằng

$$
\begin{aligned}
N_2\Phi_{B2} &= Mi_1 \\
&= 1{,}56\times10^{-3}\,\mathrm{Wb}.
\end{aligned}
$$

Đây là tổng từ thông tính trên tất cả các vòng. Không thể suy ra từ thông riêng một vòng nếu chưa biết $N_2$.
:::

::: exercise VP30.4.2
Hai cuộn có hỗ cảm $48{,}0\,\mu\mathrm H$. Tìm độ lớn suất điện động trong cuộn 2 khi dòng cuộn 1 (a) bằng $35{,}0\,\mathrm A$ và tăng $7{,}00\,\mathrm{A/s}$, (b) bằng $28{,}0\,\mathrm A$ và không đổi, (c) bằng $26{,}0\,\mathrm A$ và giảm $3{,}00\,\mathrm{A/s}$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $M=48{,}0\times10^{-6}\,\mathrm H$. Ba trạng thái có tốc độ biến thiên dòng khác nhau.

**Hướng đi:**

- Dùng độ lớn đạo hàm dòng trong định luật hỗ cảm. Giá trị dòng tức thời không trực tiếp quyết định suất điện động.
- Trường hợp dòng không đổi có đạo hàm bằng không dù dòng khác không.

Với $|\mathcal E_2|=M|di_1/dt|$, ta được

$$
\begin{aligned}
|\mathcal E_{2a}| &= 3{,}36\times10^{-4}\,\mathrm V, \\
|\mathcal E_{2b}| &= 0, \\
|\mathcal E_{2c}| &= 1{,}44\times10^{-4}\,\mathrm V.
\end{aligned}
$$

Nếu giữ một quy ước chiều cuộn cố định, suất điện động ở (a) và (c) có dấu ngược nhau vì đạo hàm dòng đổi dấu. Đề chỉ yêu cầu độ lớn.
:::

::: exercise VP30.4.3
Một ống dây hình xuyến có tự cảm $76{,}0\,\mu\mathrm H$ và 465 vòng. (a) Tìm từ thông qua mỗi vòng khi dòng bằng $12{,}0\,\mathrm A$. (b) Tìm độ lớn suất điện động tự cảm khi dòng bằng $12{,}0\,\mathrm A$ và giảm với tốc độ $55{,}0\,\mathrm{A/s}$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết tự cảm, số vòng, dòng và tốc độ giảm dòng. Cần từ thông mỗi vòng và suất điện động.

**Hướng đi:**

- Từ $N\Phi_B=Li$, chia cho $N$ vì câu (a) hỏi một vòng.
- Dùng $|\mathcal E_L|=L|di/dt|$ cho câu (b).

$$
\begin{aligned}
\Phi_B &= \frac{Li}{N} \\
&= 1{,}96\times10^{-6}\,\mathrm{Wb}, \\
|\mathcal E_L| &= 4{,}18\times10^{-3}\,\mathrm V.
\end{aligned}
$$

Suất điện động có chiều duy trì dòng cũ vì dòng đang giảm. Số vòng đã được tính vào $L$, nên không nhân $N$ một lần nữa khi tính suất điện động.
:::

::: exercise VP30.4.4
Một cuộn mang dòng $25{,}0\,\mathrm A$, đang tăng với tốc độ $145\,\mathrm{A/s}$, có suất điện động tự cảm độ lớn $3{,}70\,\mathrm{mV}$. (a) Tìm tự cảm. (b) Tìm độ lớn và chiều suất điện động tại $t=2{,}00\,\mathrm s$ nếu dòng biến thiên theo

$$
i(t)=(225\,\mathrm{A/s^2})t^2.
$$
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xác định $L$ từ một trạng thái, rồi dùng cùng cuộn cho dòng biến thiên theo bình phương thời gian.

**Hướng đi:**

- Tỉ số suất điện động và tốc độ biến thiên dòng cho tự cảm, không cần dùng giá trị 25,0 A.
- Lấy đạo hàm hàm dòng mới để tính suất điện động tại thời điểm yêu cầu.

(a) Tự cảm bằng

$$
\begin{aligned}
L &= \frac{3{,}70\times10^{-3}}{145} \\
&= 25{,}5\,\mu\mathrm H.
\end{aligned}
$$

(b) Tốc độ tăng dòng tại 2,00 s là

$$
\begin{aligned}
\frac{di}{dt} &= (450\,\mathrm{A/s^2})t, \\
\left.\frac{di}{dt}\right|_{2{,}00\,\mathrm s} &= 900\,\mathrm{A/s}.
\end{aligned}
$$

Do đó $|\mathcal E_L|=23{,}0\,\mathrm{mV}$. Dòng đang tăng theo chiều dương, nên suất điện động tự cảm có chiều ngược dòng đó.
:::

### Dòng tăng và giảm trong mạch RL

Ôn các Ví dụ 30.6–30.7. Các bài VP30.7.1–VP30.7.3 cùng dùng sơ đồ dưới đây. Đóng $S_1$, mở $S_2$ để dòng tăng từ nguồn. Mở $S_1$, đóng $S_2$ để cuộn cảm phóng năng lượng qua điện trở.

![Hình 30.11: Hai cách chuyển công tắc để dòng tăng trong mạch có nguồn hoặc suy giảm trong vòng điện trở và cuộn cảm.](img/young-30/hinh-30-11.png)

::: exercise VP30.7.1
Trong mạch Hình 30.11, $L=4{,}90\,\mathrm{mH}$ và $\mathcal E=24{,}0\,\mathrm V$. Ban đầu hai công tắc mở. Muốn dòng đạt 75,0% giá trị cực đại sau $80{,}0\,\mu\mathrm s$ kể từ khi đóng $S_1$, cần (a) điện trở bao nhiêu và (b) dòng khi đó bằng bao nhiêu?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dòng tăng từ không, với $i/I_\infty=0{,}750$ tại thời điểm đã cho. Cần $R$ và $i$.

**Hướng đi:**

- Dùng nghiệm dòng tăng RL để xác định tốc độ tiến đến trạng thái ổn định.
- Sau khi tìm $R$, tính $I_\infty=\mathcal E/R$, rồi lấy 75,0%.

$$
\begin{aligned}
0{,}750 &= 1-e^{-Rt/L}, \\
\frac{Rt}{L} &= \ln4, \\
R &= \frac{L\ln4}{t} \\
&= 84{,}9\,\Omega.
\end{aligned}
$$

Dòng tại thời điểm yêu cầu là

$$
i=0{,}750\frac{\mathcal E}{R}
=0{,}212\,\mathrm A.
$$
:::

::: exercise VP30.7.2
Trong Hình 30.11, $\mathcal E=12{,}0\,\mathrm V$, $R=18{,}0\,\Omega$ và $L=37{,}5\,\mathrm{mH}$. Ban đầu hai công tắc mở. Đóng $S_1$ tại $t=0$. Tại $t=0{,}700\,\mathrm{ms}$, tìm (a) dòng, (b) tốc độ biến thiên dòng, (c) năng lượng trong cuộn cảm.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mạch RL được nối nguồn từ trạng thái không dòng. Tính ba đại lượng ở cùng một thời điểm.

**Hướng đi:**

- Dùng nghiệm dòng tăng vì nguồn vẫn trong mạch.
- Lấy đạo hàm nghiệm đó để xác định tốc độ tăng, rồi dùng năng lượng từ trường của cuộn.

Với $\tau=L/R$, các biểu thức là

$$
\begin{aligned}
i &= \frac{\mathcal E}{R}(1-e^{-t/\tau}), \\
\frac{di}{dt} &= \frac{\mathcal E}{L}e^{-t/\tau}, \\
U_B &= \frac12Li^2.
\end{aligned}
$$

Thay dữ kiện, ta được

$$
\begin{aligned}
i &= 0{,}190\,\mathrm A, \\
\frac{di}{dt} &= +229\,\mathrm{A/s}, \\
U_B &= 6{,}79\times10^{-4}\,\mathrm J.
\end{aligned}
$$

Dấu dương của đạo hàm phù hợp với dòng đang tiến từ không đến giá trị ổn định.
:::

::: exercise VP30.7.3
Giữ các giá trị $\mathcal E$, $R$, $L$ của bài VP30.7.2. Lần này $S_1$ đã đóng rất lâu, còn $S_2$ mở. Tại $t=0$, mở $S_1$ đồng thời đóng $S_2$. Tại $t=0{,}700\,\mathrm{ms}$, tìm (a) dòng, (b) tốc độ biến thiên dòng, (c) năng lượng trong cuộn cảm.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dòng đầu bằng $I_0=\mathcal E/R$, rồi suy giảm trong vòng RL không có nguồn.

**Hướng đi:**

- Giữ dòng liên tục khi chuyển công tắc để xác định $I_0$.
- Dùng nghiệm suy giảm, khác với nghiệm dòng tăng của bài trước.

$$
\begin{aligned}
i &= I_0e^{-Rt/L}, \\
\frac{di}{dt} &= -\frac RL i, \\
U_B &= \frac12Li^2.
\end{aligned}
$$

Tại thời điểm yêu cầu,

$$
\begin{aligned}
i &= 0{,}476\,\mathrm A, \\
\frac{di}{dt} &= -229\,\mathrm{A/s}, \\
U_B &= 4{,}26\times10^{-3}\,\mathrm J.
\end{aligned}
$$

Dòng vẫn theo chiều cũ, nhưng độ lớn đang giảm. Vì vậy dòng dương đi cùng đạo hàm âm là điều hoàn toàn nhất quán.
:::

::: exercise VP30.7.4
Trong quá trình dòng tăng của Hình 30.12, tìm (a) thời điểm độ lớn điện áp cuộn cảm bằng điện áp điện trở, (b) dòng lúc đó, (c) tốc độ biến thiên dòng lúc đó. Biểu diễn theo $\mathcal E$, $R$ và $L$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nguồn không đổi được chia điện áp cho $R$ và $L$. Cần tìm thời điểm hai điện áp bằng nhau.

**Hướng đi:**

- Dùng $v_R+v_L=\mathcal E$ để suy ra mỗi điện áp bằng một nửa điện áp nguồn.
- Kết hợp nghiệm dòng tăng và quan hệ $v_L=L\,di/dt$.

Điện áp cuộn cảm là $v_L=\mathcal E e^{-Rt/L}$. Điều kiện $v_L=\mathcal E/2$ cho

$$
t=\frac LR\ln2.
$$

Vì $v_R=\mathcal E/2$, dòng và tốc độ tăng tại đó là

$$
\begin{aligned}
i &= \frac{\mathcal E}{2R}, \\
\frac{di}{dt} &= \frac{\mathcal E}{2L}.
\end{aligned}
$$

Thời điểm này bằng $0{,}693$ hằng số thời gian, không phải một hằng số thời gian.
:::

### Dao động LC và RLC

Ôn các Ví dụ 30.8–30.10. Với cuộn và tụ lý tưởng, năng lượng trao đổi giữa điện trường và từ trường. Điện trở làm biên độ dao động giảm theo thời gian.

::: exercise VP30.10.1
Mạch LC của Hình 30.15 có $L=25{,}0\,\mu\mathrm H$, dao động với tần số $445\,\mathrm{Hz}$ và điện tích cực đại $5{,}00\,\mathrm{mC}$. Tìm (a) điện dung và (b) dòng cực đại.

![Hình 30.15: Mạch LC với quy ước chiều dòng và điện tích trên bản tụ.](img/young-30/hinh-30-15.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết $L$, $f$ và biên độ điện tích $Q$. Cần $C$ và $I_{\max}$.

**Hướng đi:**

- Đổi tần số thành tần số góc để dùng $\omega^2=1/(LC)$.
- Lấy đạo hàm điện tích dao động để có biên độ dòng $I_{\max}=\omega Q$.

$$
\begin{aligned}
\omega &= 2\pi f, \\
C &= \frac1{L(2\pi f)^2} \\
&= 5{,}12\times10^{-3}\,\mathrm F, \\
I_{\max} &= 2\pi fQ \\
&= 14{,}0\,\mathrm A.
\end{aligned}
$$

Tự cảm ở đề là microhenry, còn điện tích là millicoulomb. Không được đổi cả hai tiền tố thành cùng một bậc chỉ vì chúng xuất hiện trong một bài.
:::

::: exercise VP30.10.2
Một mạch LC gồm cuộn $30{,}0\,\mu\mathrm H$ và tụ $655\,\mu\mathrm F$. Tại $t=0$, tụ có điện tích cực đại $0{,}400\,\mathrm{mC}$. Tìm (a) thời điểm đầu tiên sau $t=0$ mà điện tích bằng không và (b) độ lớn dòng lúc đó.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mạch bắt đầu ở biên điện tích, nên điện tích về không sau một phần tư chu kỳ.

**Hướng đi:**

- Dùng $q=Q\cos\omega t$ với $\omega=1/\sqrt{LC}$ và điều kiện đầu đã cho.
- Khi tụ hết điện tích, toàn bộ năng lượng ở cuộn, nên dòng đạt độ lớn cực đại.

$$
\begin{aligned}
t_0 &= \frac{\pi}{2\omega} \\
&= \frac\pi2\sqrt{LC} \\
&= 2{,}20\times10^{-4}\,\mathrm s, \\
|i(t_0)| &= \omega Q \\
&= 2{,}85\,\mathrm A.
\end{aligned}
$$

Dòng có thể mang dấu âm theo quy ước $i=dq/dt$. Câu hỏi yêu cầu độ lớn nên kết quả dòng là số dương.
:::

::: exercise VP30.10.3
Tổng năng lượng điện trường và từ trường trong một mạch LC bằng $0{,}800\,\mathrm J$. Tại một thời điểm, hai phần năng lượng bằng nhau, điện tích tụ là $5{,}30\,\mathrm{mC}$ và dòng là $8{,}00\,\mathrm A$. Tìm (a) điện dung, (b) tự cảm và (c) tần số góc.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mỗi phần năng lượng bằng $0{,}400\,\mathrm J$. Biết điện tích và dòng ở đúng trạng thái ấy.

**Hướng đi:**

- Dùng $q^2/(2C)$ cho năng lượng tụ và $Li^2/2$ cho năng lượng cuộn.
- Sau khi xác định $C,L$, dùng tần số góc riêng của mạch LC.

$$
\begin{aligned}
C &= \frac{q^2}{2U_E} \\
&= 35{,}1\,\mu\mathrm F, \\
L &= \frac{2U_B}{i^2} \\
&= 0{,}0125\,\mathrm H, \\
\omega &= \frac1{\sqrt{LC}} \\
&= 1{,}51\times10^3\,\mathrm{rad/s}.
\end{aligned}
$$

Hai năng lượng bằng nhau không có nghĩa điện tích và dòng có cùng giá trị số. Chúng gắn với những hệ số năng lượng khác nhau và có đơn vị khác nhau.
:::

::: exercise VP30.10.4
Một mạch RLC nối tiếp có $L=42{,}0\,\mathrm{mH}$, điện dung $C$ và điện trở $R$. Khi không có điện trở, tần số góc là $624\,\mathrm{rad/s}$. Khi có điện trở, tần số góc còn $208\,\mathrm{rad/s}$. Tìm (a) $C$ và (b) $R$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết tần số góc riêng và tần số góc dao động tắt dần của cùng một bộ $L,C$.

**Hướng đi:**

- Dùng tần số khi $R=0$ để tìm điện dung.
- Dùng mức giảm bình phương tần số góc để tìm hệ số tắt dần $R/(2L)$.

$$
\begin{aligned}
C &= \frac1{L\omega_0^2} \\
&= 61{,}1\,\mu\mathrm F, \\
\frac{R}{2L} &= \sqrt{\omega_0^2-\omega_d^2}, \\
R &= 49{,}4\,\Omega.
\end{aligned}
$$

Tần số góc tắt dần khác không xác nhận hệ thuộc miền dưới tắt dần. Công thức không dùng cho trường hợp quá tắt dần, vốn không có tần số dao động thực.
:::

### Bài cầu nối: Phân tích một mạch LC

::: exercise Bài cầu nối 30
Một mạch LC như Hình 30.14 gồm cuộn $60{,}0\,\mathrm{mH}$ và tụ $250\,\mu\mathrm F$. Điện tích ban đầu của tụ là $6{,}00\,\mu\mathrm C$, còn dòng ban đầu có độ lớn $0{,}400\,\mathrm{mA}$.

(a) Tìm năng lượng cực đại tích trữ trong cuộn. (b) Tìm dòng cực đại. (c) Tìm điện áp cực đại của tụ. (d) Khi độ lớn dòng bằng nửa dòng cực đại, năng lượng cuộn và độ lớn điện áp tụ bằng bao nhiêu?

![Hình 30.14: Năng lượng trao đổi qua lại giữa tụ điện và cuộn cảm trong một chu kỳ dao động.](img/young-30/hinh-30-14.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $L=0{,}0600\,\mathrm H$, $C=250\times10^{-6}\,\mathrm F$, $q_0=6{,}00\times10^{-6}\,\mathrm C$ và $|i_0|=0{,}400\times10^{-3}\,\mathrm A$. Cả hai phần năng lượng ban đầu đều khác không.

**Hướng đi:**

- Nhận diện mạch LC lý tưởng là hệ bảo toàn năng lượng, tương tự vật gắn lò xo lý tưởng. Điện tích đóng vai trò li độ, còn dòng đóng vai trò vận tốc.
- Cộng năng lượng ban đầu của cả tụ lẫn cuộn. Không coi điện tích ban đầu là điện tích cực đại vì dòng đầu khác không.
- Dùng các trạng thái toàn bộ năng lượng nằm ở cuộn hoặc tụ để tìm những đại lượng cực đại.
- Khi dòng còn một nửa cực đại, năng lượng từ trường còn một phần tư tổng năng lượng vì nó phụ thuộc bình phương dòng.

Tổng năng lượng không đổi là

$$
\begin{aligned}
U &= \frac{q_0^2}{2C}+\frac12Li_0^2 \\
&= 7{,}68\times10^{-8}\,\mathrm J.
\end{aligned}
$$

(a) Khi điện tích tụ bằng không, toàn bộ năng lượng ở cuộn. Vì vậy

$$
U_{B,\max}=7{,}68\times10^{-8}\,\mathrm J.
$$

(b) Từ $LI_{\max}^2/2=U$,

$$
I_{\max}=\sqrt{\frac{2U}{L}}
=1{,}60\,\mathrm{mA}.
$$

(c) Khi dòng bằng không, toàn bộ năng lượng ở tụ. Khi ấy

$$
V_{\max}=\sqrt{\frac{2U}{C}}
=24{,}8\,\mathrm{mV}.
$$

(d) Với $|i|=I_{\max}/2$,

$$
\begin{aligned}
U_B &= \frac U4 \\
&= 1{,}92\times10^{-8}\,\mathrm J, \\
U_E &= \frac{3U}{4}, \\
|v_C| &= \sqrt{\frac{2U_E}{C}} \\
&= 21{,}5\,\mathrm{mV}.
\end{aligned}
$$

Ban đầu năng lượng trong cuộn chiếm 6,25% tổng năng lượng. Các dữ kiện chỉ cho độ lớn dòng, nên chưa xác định được phần năng lượng đó đang tăng hay giảm. Muốn kết luận phải biết chiều dòng so với dấu điện tích trên bản tụ đã chọn. Trong quy ước $i=dq/dt$, ta có $dU_B/dt=-qi/C$.
:::
