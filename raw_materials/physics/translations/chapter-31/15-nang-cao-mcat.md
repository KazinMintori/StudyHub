## Bài nâng cao và Đọc hiểu MCAT

### Bài tập nâng cao

::: exercise 31.66
Mạch điện RLC nối tiếp trên Hình P31.66 có nguồn điện xoay chiều $v_{\mathrm{in}}(t) = V_{\mathrm{in}}\cos(\omega t)$, trong đó $V_{\mathrm{in}}$ là biên độ điện áp vào và $\omega$ là tần số góc. Điện trở thuần, độ tự cảm và điện dung của các phần tử lần lượt là $R$, $L$ và $C$. Điện dung của tụ điện có thể biến thiên. Điện áp đầu ra lấy trên hai bản tụ điện có dạng $v_{\mathrm{out}}(t) = V_{\mathrm{out}}\cos(\omega t + \theta)$. (a) Biên độ điện áp đầu ra $V_{\mathrm{out}}$ bằng bao nhiêu? (b) Góc pha $\theta$ của điện áp đầu ra bằng bao nhiêu? (c) Giá trị của $\theta$ tại trạng thái cộng hưởng bằng bao nhiêu? (d) Nếu $R=100\,\Omega$, $L=1{,}00\,\mu\mathrm H$, và $V_{\mathrm{in}}=10{,}0\,\mathrm V$, giá trị nào của điện dung $C$ sẽ tạo ra tần số cộng hưởng là $100\,\mathrm{kHz}$? (e) Trong trường hợp đó, biên độ điện áp đầu ra tại cộng hưởng là bao nhiêu?

![Hình P31.66: Mạch R-L-C nối tiếp với tụ điện biến dung và điện áp ngõ ra lấy trên hai bản tụ](img/young-31/hinh-p31-66.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mạch RLC nối tiếp với nguồn xoay chiều $v_{\mathrm{in}}(t) = V_{\mathrm{in}}\cos(\omega t)$. Điện áp đầu ra lấy trên hai bản tụ điện $C$, $v_{\mathrm{out}}(t) = V_{\mathrm{out}}\cos(\omega t + \theta)$. Cuộn cảm có $L=1{,}00\,\mu\mathrm H$, điện trở $R=100\,\Omega$, $V_{\mathrm{in}}=10{,}0\,\mathrm V$.

**Hướng đi:**

- Viết phương trình dòng điện trong mạch, $i(t) = I\cos(\omega t - \phi)$ với $\tan\phi = \frac{\omega L - 1/(\omega C)}{R}$.
- Điện áp tức thời trên tụ điện trễ pha $90^\circ$ ($\pi/2\,\mathrm{rad}$) so với dòng điện, $v_{\mathrm{out}}(t) = I X_C \cos(\omega t - \phi - \pi/2)$.
- Từ đó xác định biên độ $V_{\mathrm{out}} = I X_C$ và góc pha $\theta = -\phi - \frac{\pi}{2}$.
- Khi cộng hưởng, $\phi = 0 \implies \theta = -\frac{\pi}{2}$.
- Với $f_0 = 100\,\mathrm{kHz}$, tính $\omega_0 = 2\pi f_0$ rồi suy ra $C = \frac{1}{\omega_0^2 L}$ và $V_{\mathrm{out}} = \frac{V_{\mathrm{in}}}{R}\omega_0 L$.

(a) Trở kháng toàn phần của mạch RLC nối tiếp: Đặt biến phản kháng thuần $X = \omega L - \frac{1}{\omega C}$, trở kháng toàn phần của mạch RLC nối tiếp:

$$
Z = \sqrt{R^2 + X^2}.
$$

Biên độ dòng điện chạy trong mạch:

$$
\begin{aligned}
I &= \frac{V_{\mathrm{in}}}{Z} \\
&= \frac{V_{\mathrm{in}}}{\sqrt{R^2 + X^2}}.
\end{aligned}
$$

Điện áp đầu ra lấy trên hai đầu tụ điện có biên độ:

$$
\begin{aligned}
V_{\mathrm{out}} &= I X_C \\
&= \frac{I}{\omega C} \\
&= \frac{V_{\mathrm{in}}}{\omega C Z}.
\end{aligned}
$$

Đặt $D = \omega C Z$. Khi đưa $\omega C$ vào trong căn thức:

$$
D^2 &= (\omega C R)^2 + (\omega^2 L C - 1)^2.
$$

Biên độ điện áp đầu ra trên hai bản tụ điện là $V_{\mathrm{out}} = V_{\mathrm{in}} / D$:

$$
V_{\mathrm{out}} = \frac{V_{\mathrm{in}}}{D}.
$$

(b) Dòng điện trong mạch có dạng $i(t) = I\cos(\omega t - \phi)$, trong đó góc lệch pha của dòng điện so với điện áp nguồn thỏa mãn:

$$
\tan\phi = \frac{X}{R},
$$

$$
\phi = \arctan\left(\frac{X}{R}\right).
$$

Điện áp tức thời trên hai bản tụ điện trễ pha $\pi/2\,\mathrm{rad}$ ($90^\circ$) so với dòng điện chạy qua nó:

$$
v_{\mathrm{out}}(t) = V_{\mathrm{out}} \cos(\omega t + \theta),
$$

$$
\theta = -\phi - \frac{\pi}{2}.
$$

Đồng nhất pha dao động:

$$
\begin{aligned}
\theta &= -\phi - \frac{\pi}{2} \\
&= -\arctan\left(\frac{X}{R}\right) - \frac{\pi}{2}.
\end{aligned}
$$

(c) Tại trạng thái cộng hưởng, cảm kháng cân bằng hoàn toàn với dung kháng, $\omega L - \frac{1}{\omega C} = 0$, kéo theo $\phi = 0$.

Góc pha của điện áp đầu ra khi đó là:

$$
\begin{aligned}
\theta &= -0 - \frac{\pi}{2} \\
&= -\frac{\pi}{2}\,\mathrm{rad} = -90^\circ.
\end{aligned}
$$

Điện áp đầu ra trên tụ điện trễ pha chính xác một góc vuông $90^\circ$ so với điện áp nguồn đầu vào.

(d) Với $R=100\,\Omega$, $L=1{,}00\,\mu\mathrm H = 1{,}00\times 10^{-6}\,\mathrm H$, $V_{\mathrm{in}}=10{,}0\,\mathrm V$, tần số cộng hưởng $f=100\,\mathrm{kHz} = 1{,}00\times 10^5\,\mathrm{Hz}$.

Tần số góc cộng hưởng:

$$
\begin{aligned}
\omega_0 &= 2\pi f \\
&= 2\pi \times (1{,}00\times 10^5\,\mathrm{Hz}) \\
&\approx 6{,}2832\times 10^5\,\mathrm{rad/s}.
\end{aligned}
$$

Giá trị điện dung cần chọn:

Với $\omega_0^2 \approx 3{,}9478\times 10^{11}\,\mathrm{rad^2/s^2}$:

$$
\begin{aligned}
C &= \frac{1}{\omega_0^2 L} \\
&\approx 2{,}533\times 10^{-6}\,\mathrm F \\
&= 2{,}533\,\mu\mathrm F.
\end{aligned}
$$

(e) Tại trạng thái cộng hưởng, biên độ dòng điện đạt giá trị cực đại:

$$
\begin{aligned}
I &= \frac{V_{\mathrm{in}}}{R} \\
&= 0{,}100\,\mathrm A.
\end{aligned}
$$

Biên độ điện áp đầu ra trên tụ điện:

Với $X_C = \omega_0 L \approx 0{,}62832\,\Omega$:

$$
\begin{aligned}
V_{\mathrm{out}} &= I X_C = I (\omega_0 L) \\
&= 0{,}100 \times 0{,}62832 \\
&\approx 0{,}06283\,\mathrm V \\
&= 62{,}83\,\mathrm{mV}.
\end{aligned}
$$

:::

::: exercise 31.67
Trong một mạch điện RLC nối tiếp, dòng điện tức thời được cho bởi $i(t) = I\cos(\omega t)$. Biên độ điện áp trên điện trở, cuộn cảm và tụ điện lần lượt là $V_R$, $V_L$ và $V_C$. (a) Chứng minh rằng công suất tức thời cung cấp cho điện trở là:

$$
\begin{aligned}
p_R(t) &= V_R I\cos^2(\omega t) \\
&= \frac{1}{2}V_R I \times [1 + \cos(2\omega t)].
\end{aligned}
$$

Biểu thức này cho giá trị công suất trung bình bằng bao nhiêu?

(b) Chứng minh rằng công suất tức thời cung cấp cho cuộn cảm là:

$$
\begin{aligned}
p_L(t) &= -V_L I \sin(\omega t) \times \cos(\omega t) \\
&= -\frac{1}{2}V_L I\sin(2\omega t).
\end{aligned}
$$

Biểu thức này cho giá trị công suất trung bình bằng bao nhiêu?

(c) Chứng minh rằng công suất tức thời cung cấp cho tụ điện là:

$$
\begin{aligned}
p_C(t) &= V_C I\sin(\omega t)\cos(\omega t) \\
&= \frac{1}{2}V_C I\sin(2\omega t).
\end{aligned}
$$

Biểu thức này cho giá trị công suất trung bình bằng bao nhiêu?

(d) Công suất tức thời do nguồn cung cấp cho mạch có dạng:

$$
\begin{aligned}
p(t) &= V I\cos(\omega t) \times [\cos\phi\cos(\omega t) \\
&\qquad - \sin\phi\sin(\omega t)].
\end{aligned}
$$

Hãy chứng minh rằng $p_R(t) + p_L(t) + p_C(t) = p(t)$ tại mọi thời điểm.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dòng điện chọn làm gốc pha, $i(t) = I\cos(\omega t)$. Khảo sát công suất tức thời và công suất trung bình trên từng phần tử, sau đó chứng minh định luật bảo toàn công suất tức thời cho toàn mạch.

**Hướng đi:**

- Viết biểu thức điện áp tức thời trên từng phần tử dựa vào độ lệch pha chuẩn, $v_R$ cùng pha với $i$, $v_L$ sớm pha $\pi/2$, $v_C$ trễ pha $\pi/2$.
- Nhân điện áp tức thời với dòng điện tức thời để tìm công suất tức thời $p(t) = v(t)i(t)$.
- Lấy trung bình theo thời gian: Số hạng không đổi cho giá trị trung bình. Các số hạng điều hòa tần số góc $2\omega$ có giá trị trung bình bằng không trên một chu kỳ.
- Dùng hệ thức phân tích vectơ điện áp nguồn, $V\cos\phi = V_R$ và $V\sin\phi = V_L - V_C$ để chứng minh tổng công suất tức thời bằng công suất nguồn cấp.

(a) Điện áp tức thời trên hai đầu điện trở thuần cùng pha với dòng điện:

$$
v_R(t) = V_R \cos(\omega t).
$$

Công suất tức thời cung cấp cho điện trở:

$$
\begin{aligned}
p_R(t) &= v_R(t) i(t) \\
&= V_R \cos(\omega t) \times I \cos(\omega t) \\
&= V_R I \cos^2(\omega t) \\
&= \frac{1}{2}V_R I \times [1 + \cos(2\omega t)].
\end{aligned}
$$

Giá trị trung bình của hàm cosin biến thiên theo thời gian trên một chu kỳ bằng không, $\langle \cos(2\omega t) \rangle = 0$. Do đó công suất tiêu thụ trung bình trên điện trở là:

$$
P_{R,\mathrm{tb}} = \frac{1}{2}V_R I.
$$

(b) Điện áp tức thời trên cuộn cảm sớm pha $\pi/2$ so với dòng điện:

$$
\begin{aligned}
v_L(t) &= V_L \cos\left(\omega t + \frac{\pi}{2}\right) \\
&= -V_L \sin(\omega t).
\end{aligned}
$$

Công suất tức thời cung cấp cho cuộn cảm:

$$
\begin{aligned}
p_L(t) &= v_L(t) i(t) \\
&= -V_L \sin(\omega t) \times I \cos(\omega t) \\
&= -\frac{1}{2}V_L I \sin(2\omega t).
\end{aligned}
$$

Vì $\langle \sin(2\omega t) \rangle = 0$, công suất trung bình cuộn cảm hấp thụ qua một chu kỳ bằng không:

$$
P_{L,\mathrm{tb}} = 0.
$$

(c) Điện áp tức thời trên tụ điện trễ pha $\pi/2$ so với dòng điện:

$$
\begin{aligned}
v_C(t) &= V_C \cos\left(\omega t - \frac{\pi}{2}\right) \\
&= V_C \sin(\omega t).
\end{aligned}
$$

Công suất tức thời cung cấp cho tụ điện:

$$
\begin{aligned}
p_C(t) &= v_C(t) i(t) \\
&= V_C \sin(\omega t) \times I \cos(\omega t) \\
&= \frac{1}{2}V_C I \sin(2\omega t).
\end{aligned}
$$

Vì $\langle \sin(2\omega t) \rangle = 0$, công suất trung bình tụ điện hấp thụ qua một chu kỳ bằng không:

$$
P_{C,\mathrm{tb}} = 0.
$$

(d) Cộng các công suất tức thời của ba phần tử tại cùng một thời điểm:

$$
\begin{aligned}
p_R(t) + p_L(t) + p_C(t) &= V_R I \cos^2(\omega t) - (V_L - V_C) I \\
\qquad \times \sin(\omega t)\cos(\omega t) &= I \cos(\omega t) \times [V_R \cos(\omega t) \\
&\qquad - (V_L - V_C)\sin(\omega t)].
\end{aligned}
$$

Mặt khác, theo giản đồ vectơ Fresnel của mạch nối tiếp, các hình chiếu của vectơ điện áp nguồn $\vec V$ lên phương cùng pha và vuông pha với dòng điện lần lượt là:

$$
V \cos\phi = V_R,
$$

$$
V \sin\phi = V_L - V_C.
$$

Thay các hệ thức này vào biểu thức trên:

$$
\begin{aligned}
p_R(t) + p_L(t) + p_C(t) &= I \cos(\omega t) \times [V\cos\phi \cos(\omega t) \\
\qquad - V\sin\phi \sin(\omega t)] &= V I \cos(\omega t) \times [\cos\phi \cos(\omega t) \\
\qquad - \sin\phi \sin(\omega t)] &= p(t).
\end{aligned}
$$

Hệ thức được chứng minh hoàn toàn, khẳng định định luật bảo toàn năng lượng tức thời nghiệm đúng tại mọi thời điểm trong mạch xoay chiều.
:::

::: exercise 31.68
(a) Ở tần số góc nào thì biên độ điện áp trên điện trở thuần trong mạch RLC nối tiếp đạt giá trị lớn nhất? (b) Ở tần số góc nào thì biên độ điện áp trên cuộn cảm đạt giá trị lớn nhất? (c) Ở tần số góc nào thì biên độ điện áp trên tụ điện đạt giá trị lớn nhất? Hãy khảo sát đầy đủ điều kiện tồn tại cực đại hữu hạn $0 < R^2 C / L < 2$ và phân tích các trường hợp giới hạn.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tìm tần số góc $\omega$ để biên độ điện áp trên từng phần tử $V_R$, $V_L$, $V_C$ đạt cực đại trong mạch RLC nối tiếp được cấp bởi nguồn có biên độ điện áp $V$ không đổi.

Xét $R>0$, $L>0$, $C>0$ và $\omega>0$. Với $R=0$, trạng thái cưỡng bức đúng cộng hưởng không có biên độ ổn định hữu hạn trong mô hình không tổn hao.

**Hướng đi:**

- Biểu diễn $V_R(\omega) = I(\omega)R$, $V_L(\omega) = \omega L I(\omega)$, $V_C(\omega) = \frac{I(\omega)}{\omega C}$.
- Dùng phép đổi biến phụ đối với mẫu số của hàm bình phương biên độ điện áp: Đặt $u = 1/\omega^2$ cho $V_L$, và $w = \omega^2$ cho $V_C$.
- Khảo sát tam thức bậc hai ở mẫu số để tìm tọa độ đỉnh cực tiểu và điều kiện để đỉnh nằm trong miền xác định dương ($u > 0$ và $w > 0$).
- Phân tích trường hợp giới hạn khi $R^2 C / L \ge 2$.

(a) Biên độ điện áp trên hai đầu điện trở thuần:

Với $X = \omega L - \frac{1}{\omega C}$:

$$
\begin{aligned}
V_R(\omega) &= I(\omega)R \\
&= \frac{V R}{\sqrt{R^2 + X^2}}.
\end{aligned}
$$

Vì tử số là hằng số, $V_R(\omega)$ đạt cực đại khi và chỉ khi mẫu số đạt cực tiểu. Điều này xảy ra khi thành phần phản kháng triệt tiêu:

$$
\omega L - \frac{1}{\omega C} = 0,
$$

$$
\omega_R = \frac{1}{\sqrt{LC}} = \omega_0.
$$

Biên độ điện áp trên điện trở đạt cực đại đúng tại tần số góc cộng hưởng tự nhiên $\omega_0$. Khi đó $V_{R,\mathrm{max}} = V$.

(b) Biên độ điện áp trên hai đầu cuộn cảm:

Với $X = \omega L - \frac{1}{\omega C}$:

$$
\begin{aligned}
V_L(\omega) &= \omega L I(\omega) \\
&= \frac{V \omega L}{\sqrt{R^2 + X^2}}.
\end{aligned}
$$

Chia cả tử và mẫu cho $\omega$ và đặt biến phụ $u = \frac{1}{\omega^2} > 0$:

$$
V_L(\omega) = \frac{V L}{\sqrt{f(u)}}
$$

với hàm số bậc hai dưới căn thức:

$$
\begin{aligned}
f(u) &= R^2 u + \left(L - \frac{u}{C}\right)^2 \\
&= \frac{1}{C^2} u^2 + \left(R^2 - \frac{2L}{C}\right)u + L^2.
\end{aligned}
$$

Đây là tam thức bậc hai theo $u$ với hệ số của $u^2$ bằng $1/C^2>0$. Đồ thị là parabol có bề lõm hướng lên. Đỉnh cực tiểu của tam thức nằm tại:

$$
\begin{aligned}
u^* &= -\frac{b}{2a} \\
&= \frac{\frac{2L}{C} - R^2}{\frac{2}{C^2}} \\
&= LC - \frac{R^2 C^2}{2} \\
&= LC \left(1 - \frac{R^2 C}{2L}\right).
\end{aligned}
$$

Để tồn tại một tần số góc hữu hạn $\omega_L > 0$ làm mẫu số đạt cực tiểu, vị trí đỉnh $u^*$ bắt buộc phải mang giá trị dương:

$$
\begin{aligned}
u^* > 0 &\iff 1 - \frac{R^2 C}{2L} > 0 \\
&\iff \frac{R^2 C}{L} < 2.
\end{aligned}
$$

Khi thỏa mãn điều kiện $0 < \frac{R^2 C}{L} < 2$, tần số góc để biên độ điện áp cuộn cảm đạt giá trị lớn nhất là:

$$
\begin{aligned}
\omega_L &= \frac{1}{\sqrt{u^*}} \\
&= \frac{1}{\sqrt{LC \left(1 - \frac{R^2 C}{2L}\right)}} \\
&= \frac{\omega_0}{\sqrt{1 - \frac{R^2 C}{2L}}}.
\end{aligned}
$$

Nhận xét: Trong miền này, mẫu số $\sqrt{1 - \frac{R^2 C}{2L}} < 1$, do đó $\omega_L > \omega_0$. Cực đại của điện áp cuộn cảm luôn nằm ở phía tần số cao hơn tần số cộng hưởng.

Nếu $\frac{R^2 C}{L} \ge 2$, đỉnh của parabol nằm ở $u^* \le 0$. Khi đó trên miền $u > 0$, hàm $f(u)$ là hàm đồng biến đơn điệu, giá trị nhỏ nhất đạt được ở giới hạn biên $u \to 0$ ($\omega \to \infty$). Trong trường hợp này, điện áp trên cuộn cảm không có cực đại địa phương hữu hạn mà tăng đơn điệu tiệm cận tới giá trị điện áp nguồn $V$ khi $\omega \to \infty$.

(c) Biên độ điện áp trên hai bản tụ điện:

Với $X = \omega L - \frac{1}{\omega C}$:

$$
\begin{aligned}
V_C(\omega) &= \frac{I(\omega)}{\omega C} \\
&= \frac{V}{\omega C \sqrt{R^2 + X^2}}.
\end{aligned}
$$

Đưa $\omega$ vào căn thức và đặt biến phụ $w = \omega^2 > 0$:

$$
V_C(\omega) = \frac{V/C}{\sqrt{g(w)}}
$$

với tam thức bậc hai dưới căn thức:

$$
\begin{aligned}
g(w) &= R^2 w + \left(w L - \frac{1}{C}\right)^2 \\
&= L^2 w^2 + \left(R^2 - \frac{2L}{C}\right)w + \frac{1}{C^2}.
\end{aligned}
$$

Hệ số của $w^2$ là $L^2 > 0$, parabol quay bề lõm lên trên và đạt cực tiểu tại đỉnh:

$$
\begin{aligned}
w^* &= -\frac{b}{2a} \\
&= \frac{\frac{2L}{C} - R^2}{2L^2} \\
&= \frac{1}{LC} - \frac{R^2}{2L^2} \\
&= \frac{1}{LC}\left(1 - \frac{R^2 C}{2L}\right).
\end{aligned}
$$

Để tồn tại tần số góc hữu hạn $\omega_C > 0$, ta cũng cần điều kiện $w^* > 0$, tức là:

$$
1 - \frac{R^2 C}{2L} > 0
$$

$$
\iff \frac{R^2 C}{L} < 2.
$$

Khi điều kiện $0 < \frac{R^2 C}{L} < 2$ được thỏa mãn, tần số góc để biên độ điện áp tụ điện đạt cực đại là:

$$
\begin{aligned}
\omega_C &= \sqrt{w^*} \\
&= \sqrt{\frac{1}{LC}\left(1 - \frac{R^2 C}{2L}\right)} \\
&= \omega_0 \sqrt{1 - \frac{R^2 C}{2L}}.
\end{aligned}
$$

Nhận xét: Vì $\sqrt{1 - \frac{R^2 C}{2L}} < 1$, ta luôn có $\omega_C < \omega_0$. Cực đại của điện áp tụ điện luôn nằm ở phía tần số thấp hơn tần số cộng hưởng. Đặc biệt, tích của hai tần số góc cực đại thỏa mãn hệ thức đối xứng:

$$
\begin{aligned}
\omega_C \omega_L &= \left(\omega_0 \sqrt{1 - \frac{R^2 C}{2L}}\right) \left(\frac{\omega_0}{\sqrt{1 - \frac{R^2 C}{2L}}}\right) \\
&= \omega_0^2.
\end{aligned}
$$

Nếu $\frac{R^2 C}{L} \ge 2$, đỉnh $w^* \le 0$, hàm $g(w)$ đồng biến đơn điệu trên toàn miền $w > 0$. Khi đó không tồn tại cực đại địa phương, và $V_C(\omega)$ giảm đơn điệu từ giới hạn $V$ khi $\omega\to0^+$ về $0$ khi $\omega \to \infty$.
:::

### Bài đọc hiểu ứng dụng sinh học (Đo điện thế ngoại bào)

**CHUYỂN ĐỔI TÍN HIỆU TỪ MỘT CHIỀU SANG XOAY CHIỀU TRONG ĐO ĐẠC SINH HỌC**

Một tế bào đơn lẻ, chẳng hạn như tế bào trứng (noãn bào), thường có tổ chức không gian định hướng rõ rệt, được thể hiện một phần qua tính bất đối xứng trên màng tế bào. Tính bất đối xứng này bao gồm sự phân bố không đồng đều của các cơ chế vận chuyển ion, dẫn đến sự xuất hiện của một dòng điện tổng đi vào một vùng màng và đi ra ở một vùng khác. Những dòng điện tế bào ổn định này có thể điều hòa tính phân cực của tế bào, dẫn tới sự định hình phân cực phôi. Do đó các nhà khoa học rất quan tâm đến việc đo đạc chúng.

Những dòng điện tế bào này chuyển động theo các vòng khép kín qua dịch ngoại bào. Định luật Ohm đòi hỏi phải tồn tại hiệu điện thế giữa hai điểm bất kỳ trong khối chất lỏng dẫn điện bao quanh tế bào. Mặc dù cường độ dòng điện có thể đáng kể, độ chênh lệch điện thế ngoại bào lại rất nhỏ, chỉ vào cỡ vài nanovolt ($\mathrm{nV}$). Nếu có thể lập bản đồ phân bố điện thế trong dịch bên ngoài tế bào, ta có thể tính được mật độ dòng điện bằng dạng vi phân của định luật Ohm khi biết điện trở suất của dịch. Với hai điện cực tĩnh cách nhau $10$ hay $20\,\mu\mathrm{m}$, phép đo chênh lệch điện thế này gặp trở ngại. Trở kháng một chiều của các điện cực rất cao, còn nhiễu nhiệt ở điện cực lấn át tín hiệu điện thế tế bào.

Một phương pháp đo đạc hiệu quả sử dụng một điện cực có đầu hình cầu bằng bạch kim (platinum), được kích thích dao động điều hòa qua lại giữa hai điểm trong dịch ngoại bào. Điện thế mà điện cực đo được so với một điện cực so sánh ở xa cũng sẽ biến thiên hình sin theo thời gian. Khi đó, hiệu điện thế một chiều giữa hai vị trí biên (hai điểm trong dịch) được chuyển đổi thành một hiệu điện thế xoay chiều dạng sóng sin. Điện cực bạch kim hoạt động tương đương với một tụ điện mắc nối tiếp với điện trở của dịch ngoại bào. Điện trở này, gọi là điện trở tiếp cận ($R_A$), có giá trị khoảng $\rho/(10a)$, trong đó $\rho$ là điện trở suất của dịch (thường tính bằng $\Omega\cdot\mathrm{cm}$) và $a$ là bán kính của đầu cầu điện cực. Trong mô hình đang xét, quả cầu bạch kim có đường kính $20\,\mu\mathrm{m}$ và điện dung $10\,\mathrm{nF}$. Điện trở suất của nhiều loại dịch sinh học điển hình là $100\,\Omega\cdot\mathrm{cm}$.

::: exercise 31.69
Trở kháng một chiều của điện cực bằng bao nhiêu, giả sử rằng điện cực hoạt động như một tụ điện lý tưởng?

(a) $0$.

(b) Vô cùng lớn.

(c) $\sqrt{2}\times 10^4\,\Omega$.

(d) $\sqrt{2}\times 10^6\,\Omega$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Khảo sát trở kháng của điện cực khi dùng dòng điện một chiều ($\omega = 0$).

**Hướng đi:**

- Điện cực được mô hình hóa gồm điện trở tiếp cận $R_A$ mắc nối tiếp với tụ điện $C$, $Z = \sqrt{R_A^2 + X_C^2}$.
- Với dòng một chiều, tần số góc bằng không, $\omega = 0$. Dung kháng của tụ điện $X_C = \frac{1}{\omega C} \to \infty$.

Dung kháng của tụ điện được xác định bởi:

$$
X_C = \frac{1}{\omega C}.
$$

Đối với dòng điện một chiều ở trạng thái ổn định ($\omega = 0$), dung kháng của tụ điện lý tưởng tiến tới vô cùng lớn:

$$
\lim_{\omega \to 0} X_C = \infty.
$$

Trở kháng toàn phần của điện cực:

$$
Z = \sqrt{R_A^2 + X_C^2} \to \infty.
$$

Tụ điện đóng vai trò như một mạch hở hoàn toàn đối với dòng điện một chiều, do đó trở kháng một chiều của điện cực là vô cùng lớn.

Chọn phương án (b).
:::

::: exercise 31.70
Nếu điện cực dao động qua lại giữa hai điểm cách nhau $20\,\mu\mathrm{m}$ với tần số bằng $(5000/\pi)\,\mathrm{Hz}$, trở kháng của điện cực bằng bao nhiêu?

(a) $0$.

(b) Vô cùng lớn.

(c) $\sqrt{2}\times 10^4\,\Omega$.

(d) $\sqrt{2}\times 10^6\,\Omega$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tần số dao động $f = \frac{5000}{\pi}\,\mathrm{Hz}$. Đầu cầu có đường kính $D=20\,\mu\mathrm{m}$, điện dung $C=10\,\mathrm{nF}$. Điện trở suất của dịch sinh học $\rho=100\,\Omega\cdot\mathrm{cm}$. Tìm trở kháng $Z$.

**Hướng đi:**

- Tính bán kính đầu cầu, $a = D/2 = 10\,\mu\mathrm{m} = 1{,}0\times 10^{-3}\,\mathrm{cm}$.
- Tính điện trở tiếp cận, $R_A \approx \frac{\rho}{10a}$.
- Tính tần số góc, $\omega = 2\pi f$ và dung kháng $X_C = \frac{1}{\omega C}$.
- Tính trở kháng toàn phần, $Z = \sqrt{R_A^2 + X_C^2}$.

Bán kính của quả cầu bạch kim:

$$
\begin{aligned}
a &= \frac{D}{2} = \frac{20\,\mu\mathrm m}{2} \\
&= 10\,\mu\mathrm m \\
&= 1{,}0\times 10^{-3}\,\mathrm{cm}.
\end{aligned}
$$

Điện trở tiếp cận của dịch ngoại bào quanh điện cực:

$$
\begin{aligned}
R_A &\approx \frac{\rho}{10a} \\
&= 10^4\,\Omega.
\end{aligned}
$$

Tần số góc dao động của điện cực:

$$
\begin{aligned}
\omega &= 2\pi f \\
&= 2\pi \times \left(\frac{5000}{\pi}\,\mathrm{Hz}\right) \\
&= 10^4\,\mathrm{rad/s}.
\end{aligned}
$$

Dung kháng của điện cực ở tần số này:

$$
\begin{aligned}
X_C &= \frac{1}{\omega C} \\
&= 10^4\,\Omega.
\end{aligned}
$$

Trở kháng toàn phần của điện cực:

$$
\begin{aligned}
Z &= \sqrt{R_A^2 + X_C^2} \\
&= 10^4 \sqrt{2}\,\Omega \\
&= \sqrt{2}\times 10^4\,\Omega.
\end{aligned}
$$

Chọn phương án (c).
:::

::: exercise 31.71
Tín hiệu từ điện cực dao động được đưa vào một bộ khuếch đại, hiển thị điện áp đo được dưới dạng giá trị hiệu dụng là $1{,}5\,\mathrm{nV}$. Hiệu điện thế giữa hai vị trí biên bằng bao nhiêu?

(a) $1{,}5\,\mathrm{nV}$.

(b) $3{,}0\,\mathrm{nV}$.

(c) $2{,}1\,\mathrm{nV}$.

(d) $4{,}2\,\mathrm{nV}$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện áp xoay chiều đo được có giá trị hiệu dụng $V_{\mathrm{rms}} = 1{,}5\,\mathrm{nV}$. Cần tìm hiệu điện thế giữa hai vị trí biên (độ chênh lệch điện thế đỉnh-đáy).

**Hướng đi:**

- Tín hiệu biến thiên điều hòa theo tọa độ dao động của điện cực, $v(t) = V_0 \cos(\omega t)$.
- Biên độ điện áp liên hệ với giá trị hiệu dụng qua $V_0 = V_{\mathrm{rms}}\sqrt{2}$.
- Khi điện cực đi từ vị trí biên này sang vị trí biên đối diện, điện thế biến thiên từ $-V_0$ đến $+V_0$. Độ chênh lệch điện thế giữa hai vị trí biên cực đại chính là hiệu điện thế đỉnh-đáy, $\Delta V = 2V_0$.

Biên độ của điện áp xoay chiều hình sin:

$$
\begin{aligned}
V_0 &= V_{\mathrm{rms}}\sqrt{2} \\
&= 1{,}5\,\mathrm{nV} \times \sqrt{2} \\
&\approx 2{,}12\,\mathrm{nV}.
\end{aligned}
$$

Khi đầu điện cực dao động điều hòa qua lại giữa hai vị trí biên trong dịch ngoại bào, thành phần điện thế xoay chiều, sau khi trừ giá trị trung bình, dao động từ $-V_0$ đến $+V_0$.

Hiệu điện thế giữa hai điểm cực biên tương ứng với độ chênh lệch đỉnh-đáy (peak-to-peak):

$$
\begin{aligned}
\Delta V &= V_0 - (-V_0) = 2V_0 \\
&= 2 \times 2{,}12\,\mathrm{nV} \\
&\approx 4{,}2\,\mathrm{nV}.
\end{aligned}
$$

Chọn phương án (d).
:::

::: exercise 31.72
Nếu tần số dao động của điện cực được tăng lên đến một giá trị rất lớn, trở kháng của điện cực sẽ. (a) Tiến tới vô cùng lớn.

(b) Tiến tới không.

(c) Tiến tới một giá trị không đổi khác không.

(d) Không thay đổi.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Khảo sát giới hạn của trở kháng điện cực $Z(\omega)$ khi tần số dao động $\omega \to \infty$.

**Hướng đi:**

- Biểu thức trở kháng của điện cực, $Z = \sqrt{R_A^2 + X_C^2} = \sqrt{R_A^2 + \left(\frac{1}{\omega C}\right)^2}$.
- Khảo sát giới hạn khi $\omega \to \infty$.

Dung kháng của điện cực phụ thuộc vào tần số góc:

$$
X_C = \frac{1}{\omega C}.
$$

Khi tần số dao động của điện cực tăng lên rất cao ($\omega \to \infty$), dung kháng của tụ điện giảm dần về không:

$$
\lim_{\omega \to \infty} X_C = \lim_{\omega \to \infty} \frac{1}{\omega C} = 0.
$$

Khi đó, trở kháng toàn phần của điện cực tiến tới:

$$
\begin{aligned}
\lim_{\omega \to \infty} Z &= \sqrt{R_A^2 + 0} \\
&= R_A = 10^4\,\Omega > 0.
\end{aligned}
$$

Trở kháng không bị triệt tiêu về không mà tiến tới điện trở thuần của dịch ngoại bào quanh điện cực ($R_A$), là một hằng số xác định khác không.

Chọn phương án (c).
:::
