## Bài tập nâng cao 35.54–35.56

::: exercise 35.54
Ánh sáng đơn sắc bước sóng $\lambda$ tới ba khe hẹp, khoảng giữa hai khe kề là $d$. Tại điểm $P$, điện trường từ khe giữa là $E\cos(\omega t)$, từ hai khe ngoài là $E\cos(\omega t+\phi)$ và $E\cos(\omega t-\phi)$, với:

$$
\phi=\frac{2\pi d\sin\theta}{\lambda}.
$$

(a) Dùng giản đồ pha hoặc đồng nhất thức lượng giác để tìm biên độ trường tổng $E_P$. (b) Tìm cường độ theo cực đại toàn hệ $I_0$ và $\phi$. (c) Ngoài cực đại bằng $I_0$ tại $\phi=2\pi m$, còn có cực đại nhỏ hơn ở những pha nào? (d) Cường độ cực đại nhỏ bằng bao nhiêu? (e) Pha của các vân tối gần tâm nhất là gì? (f) Với $\lambda=650\,\mathrm{nm}$, $d=0{,}200\,\mathrm{mm}$, màn xa $R=1{,}00\,\mathrm m$, cực đại nhỏ đầu tiên cách tâm bao nhiêu? (g) Cực đại tuyệt đối kế tâm cách tâm bao nhiêu?

![Hình P 35.54: Ba tia từ ba khe hẹp tới P, hai khe ngoài có độ lệch pha đối nhau so với khe giữa.](img/young-35/hinh-p35-54.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Ba đóng góp có cùng biên độ $E$, cùng tần số. Hai pha ngoài bằng $\pm\phi$ so với pha giữa.

**Hướng đi:**

- Dùng tổng ba vectơ pha cách đều góc vì ba khe được chiếu cùng biên độ, cùng pha và ở khoảng cách đều.
- Khai triển tổng ba trường tường minh trước khi rút gọn.
- Bình phương biên độ để tìm cường độ, chuẩn hóa bằng biên độ cực đại $3E$.
- Xét các điểm dừng của hàm cường độ để phân biệt cực đại nhỏ và vân tối.

(a) Trường tổng:

$$
E_{\rm net}(t)&=E\cos\omega t +E\cos(\omega t+\phi) +E\cos(\omega t-\phi).
$$

Hai số hạng ngoài cộng lại thành $2E\cos\omega t\cos\phi$, nên:

$$
\begin{aligned}
E_{\rm net}(t) &= E(1+2\cos\phi)\cos\omega t, \\
E_P &= E|1+2\cos\phi|.
\end{aligned}
$$

Hệ số có dấu âm chỉ pha tổng đổi thêm $\pi$, còn biên độ luôn không âm.

(b) Khi ba trường đồng pha, $E_{P,\max}=3E$:

$$
\frac I{I_0}=\frac{(1+2\cos\phi)^2}{9}.
$$

(c) Đạo hàm theo pha:

$$
\frac{\mathrm d(I/I_0)}{\mathrm d\phi} =-\frac49(1+2\cos\phi)\sin\phi.
$$

Các điểm dừng có $\sin\phi=0$ hoặc $1+2\cos\phi=0$. Bội chẵn của $\pi$ cho cực đại tuyệt đối. Bội lẻ:

$$
\phi=(2m+1)\pi,\qquad m\in\mathbb Z
$$

cho các cực đại nhỏ.

(d) Với $\cos\phi=-1$, nhận $I=I_0/9$.

(e) Vân tối có $\cos\phi=-1/2$. Hai giá trị gần 0 nhất là:

$$
\phi=\pm\frac{2\pi}{3}.
$$

![Phân bố cường độ ba khe: Hai cực tiểu nằm giữa cực đại tuyệt đối và cực đại phụ có độ cao một phần chín.](img/young-35/loi-giai-35-54.svg)

(f) Cực đại nhỏ đầu tiên có $|\phi|=\pi$, nên trong gần đúng góc nhỏ:

$$
\begin{aligned}
|y_{\rm lesser}| &\approx \frac{\lambda R}{2d} \\
&= 1{,}625\,\mathrm{mm}.
\end{aligned}
$$

(g) Cực đại tuyệt đối gần nhất khác cực đại trung tâm có $|\phi|=2\pi$:

$$
|y_{\rm main}|\approx\frac{\lambda R}d
=3{,}25\,\mathrm{mm}.
$$

Cực đại trung tâm tự nó là cực đại tuyệt đối ở $y=0$, nhưng ở đây đang tìm cực đại tuyệt đối kế tiếp.
:::

::: exercise 35.55
Thanh thủy tinh có chiết suất $1{,}48$ ở 20,0°C. Chiết suất tăng tuyến tính theo nhiệt độ với hệ số $2{,}50\times10^{-5}\,\mathrm{K^{-1}}$, hệ số nở dài $5{,}00\times10^{-6}\,\mathrm{K^{-1}}$. Ở 20,0°C, thanh dài 3,00 cm.

Đặt thanh trong một nhánh giao thoa kế Michelson, nung với tốc độ 5,00°C mỗi phút. Nguồn có bước sóng 589 nm, thanh ban đầu ở 20,0°C. Có bao nhiêu vân qua trường nhìn mỗi phút?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Khi thủy tinh nở trong một nhánh có gương cố định, phần tăng chiều dài của thanh thay thế một phần không khí. Chiết suất không khí lấy gần 1.

**Hướng đi:**

- Dùng $2(n-1)L$ vì bản thay thế cùng một đoạn không khí trên cả lượt tới lẫn lượt về của giao thoa kế.
- Độ tăng quang lộ do thanh là $(n-1)L$ một lượt, không phải chỉ $nL$ khi bỏ quên phần không khí bị thay thế.
- Lấy đạo hàm để tính cả biến thiên chiết suất lẫn nở dài.
- Nhân 2 do hai lượt qua thanh, rồi chia bước sóng để tính tốc độ số vân.

Gọi quang lộ dư hai lượt là $\Delta$:

$$
\begin{aligned}
\Delta &= 2(n-1)L, \\
&\frac{\mathrm d\Delta}{\mathrm dT} \\
&= 2L\left[\frac{\mathrm dn}{\mathrm dT}+(n-1)\alpha\right].
\end{aligned}
$$

Do đó, ở gần nhiệt độ ban đầu:

$$
\begin{aligned}
\frac{\mathrm dN}{\mathrm dt} &= \frac{2L}{\lambda}\left[\frac{\mathrm dn}{\mathrm dT}+(n-1)\alpha\right] \times\frac{\mathrm dT}{\mathrm dt} \\
&= 13{,}956\,\mathrm{min^{-1}} \\
&\approx 14{,}0\ \text{vân/phút}.
\end{aligned}
$$

Cả chiết suất và chiều dài đều tăng nên các đóng góp vào quang lộ dư cùng dấu. Đây là kết quả đến bậc nhất theo độ tăng nhiệt.
:::

::: exercise 35.56
Lưỡng lăng kính Fresnel có hai góc lăng kính $A$ rất nhỏ. Khe nguồn $S_0$ rất hẹp, cách lưỡng lăng kính một khoảng $a$.

(a) Chứng minh khoảng giữa hai nguồn kết hợp ảo $S_1,S_2$ bằng $d=2aA(n-1)$, với $n$ là chiết suất lăng kính. (b) Tìm khoảng vân ánh sáng xanh lục 500 nm trên màn cách lưỡng lăng kính 2,00 m. Cho $a=0{,}200\,\mathrm m$, $A=3{,}50\,\mathrm{mrad}$, $n=1{,}50$.

![Hình P 35.56: Hai nửa lưỡng lăng kính tạo hai ảnh ảo kết hợp của cùng nguồn S 0, có các chùm chồng lấp trên màn.](img/young-35/hinh-p35-56.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Các góc nhỏ, lưỡng lăng kính mỏng. Màn cách mặt phẳng nguồn ảo xấp xỉ $a+b$, với $b=2{,}00\,\mathrm m$.

**Hướng đi:**

- Dùng $R=a+b$ vì nguồn ảnh đối xứng làm hai chùm ảo truyền tới màn trên toàn khoảng từ nguồn đến màn.
- Dùng định luật Snell góc nhỏ để tìm độ lệch của một lăng kính mỏng.
- Kéo dài ngược hai chùm để xác định hai ảnh ảo của cùng nguồn.
- Tính khoảng vân với khoảng từ nguồn ảo tới màn, không chỉ khoảng lăng kính–màn.

(a) Với góc khúc xạ trong lăng kính $r_1,r_2$:

$$
\begin{aligned}
r_1+r_2 &= A, \\
i &\approx nr_1, \\
e &\approx nr_2.
\end{aligned}
$$

Độ lệch của mỗi nửa:

$$
\begin{aligned}
\delta &= i+e-A \\
&\approx (n-1)A.
\end{aligned}
$$

Hai nửa lệch theo hai phía đối nhau. Khi kéo dài ngược về mặt phẳng nguồn, mỗi ảnh lệch ngang khoảng $a\delta$, nên:

$$
d\approx2a\delta=2aA(n-1).
$$

(b):

$$
\begin{aligned}
d &= 0{,}700\,\mathrm{mm}, \\
R &= a+b=2{,}20\,\mathrm m, \\
\Delta y &= \frac{\lambda R}d \\
&= 1{,}57\,\mathrm{mm}.
\end{aligned}
$$

Hai nguồn ảo giữ quan hệ pha vì là hai ảnh của một khe nguồn chung.
:::
