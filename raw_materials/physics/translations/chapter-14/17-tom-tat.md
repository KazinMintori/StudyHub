## Tổng kết chương 14

### Chuyển động tuần hoàn

Chuyển động tuần hoàn lặp lại sau những khoảng thời gian bằng nhau. Các hệ dao động phục hồi được xét trong chương có vị trí cân bằng bền và lực đưa vật trở về khi bị lệch. Chu kỳ là thời gian một dao động đầy đủ, còn tần số là số dao động trong một giây:

$$
f=\frac1T,\qquad\omega=2\pi f.
$$

![Tổng kết chuyển động tuần hoàn: Con trượt–lò xo và các lực tại ba li độ âm, không và dương.](/vat-ly-1/bai-giang/img/young-14/r-theory-summary-periodic.png)

### Dao động điều hòa

Lực phục hồi tuyến tính $F_x=-kx$ với $k>0$ tạo gia tốc $a_x=-(k/m)x$. Khi không có lực cản hoặc ngoại lực khác, nghiệm là

$$
x=A\cos(\omega t+\phi),
$$

với

$$
\begin{aligned}
&\omega=\sqrt{\frac km},\\
&T=2\pi\sqrt{\frac mk}.
\end{aligned}
$$

![Tổng kết dao động điều hòa: Đồ thị li độ hình sin có biên độ A và chu kỳ T.](/vat-ly-1/bai-giang/img/young-14/r-theory-summary-shm.png)

Biên độ và pha do điều kiện đầu xác định. Vận tốc và gia tốc cũng biến thiên hình sin. Với cùng $m,k$, tần số điều hòa lý tưởng không phụ thuộc biên độ. Nhiều hệ thực chỉ gần điều hòa trong miền lệch nhỏ quanh cân bằng.

### Cơ năng dao động điều hòa

Không có tiêu tán, cơ năng giữ nguyên:

$$
\begin{aligned}
E&=\frac12mv_x^2+\frac12kx^2\\
&=\frac12kA^2.
\end{aligned}
$$

![Tổng kết năng lượng: Động năng và thế năng đổi theo li độ, còn tổng cơ năng không đổi.](/vat-ly-1/bai-giang/img/young-14/r-theory-summary-energy.png)

Tại biên, động năng bằng không. Tại cân bằng, thế năng đàn hồi nhỏ nhất và tốc độ lớn nhất. Trên miền chuyển động,

$$
v_x=\pm\omega\sqrt{A^2-x^2},
$$

trong đó dấu được chọn theo chiều chuyển động.

### Dao động điều hòa góc

Mômen phục hồi tuyến tính $\tau_z=-\kappa\theta$ cho

$$
\omega=\sqrt{\frac\kappa I},\qquad f=\frac1{2\pi}\sqrt{\frac\kappa I}.
$$

![Tổng kết dao động góc: Mômen lò xo của bánh xe cân bằng ngược dấu với góc lệch.](/vat-ly-1/bai-giang/img/young-14/r-theory-summary-angular.png)

Mômen quán tính $I$ phải lấy quanh đúng trục dao động. Hằng số xoắn $\kappa$ liên hệ mômen với góc tính bằng radian.

### Con lắc đơn

Con lắc đơn gồm chất điểm ở đầu dây không khối lượng, không dãn. Lực tiếp tuyến thật là $-mg\sin\theta$. Ở góc nhỏ tính bằng radian, chuyển động gần điều hòa:

$$
\omega=\sqrt{\frac gL},\qquad f=\frac1{2\pi}\sqrt{\frac gL},
$$

$$
T=2\pi\sqrt{\frac Lg}.
$$

![Tổng kết con lắc đơn: Trọng lực cung cấp thành phần phục hồi tiếp tuyến, lực căng dây giữ chuyển động trên cung tròn.](/vat-ly-1/bai-giang/img/young-14/r-theory-summary-simple-pendulum.png)

Chu kỳ góc nhỏ không phụ thuộc khối lượng và gần như không phụ thuộc biên độ. Khi biên độ góc tăng, cần hiệu chỉnh chu kỳ, không tiếp tục xem tính đẳng thời là chính xác.

### Con lắc vật lý

Vật có kích thước treo quanh trục cố định có mômen phục hồi $-mgd\sin\theta$. Với dao động nhỏ,

$$
\begin{aligned}
&\omega=\sqrt{\frac{mgd}{I}},\\
&T=2\pi\sqrt{\frac{I}{mgd}}.
\end{aligned}
$$

![Tổng kết con lắc vật lý: Trục treo, trọng tâm và cánh tay đòn của trọng lực xác định mômen phục hồi.](/vat-ly-1/bai-giang/img/young-14/r-theory-summary-physical-pendulum.png)

Khoảng cách $d$ từ trục tới trọng tâm và mômen quán tính $I$ quanh trục ấy cùng quyết định chu kỳ. Cùng vị trí trọng tâm chưa đủ để hai vật có cùng chu kỳ.

### Dao động tắt dần

Lực cản tuyến tính $F_d=-bv_x$ làm cơ năng giảm theo

$$
\frac{dE}{dt}=-bv_x^2.
$$

Với $0<b<2\sqrt{km}$, hệ còn dao động:

$$
x=Ae^{-bt/(2m)}\cos(\omega't+\phi),
$$

$$
\omega'=\sqrt{\frac km-\frac{b^2}{4m^2}}.
$$

![Tổng kết dao động tắt dần: Hai nghiệm có cản khác nhau cùng các đường bao biên giảm theo hàm mũ.](/vat-ly-1/bai-giang/img/young-14/r-theory-summary-damped.png)

Tại $b=2\sqrt{km}$ là tới hạn, còn $b>2\sqrt{km}$ là quá tới hạn. Trong tình huống lệch rồi thả từ nghỉ, hai chế độ này trở về mà không dao động qua lại.

### Dao động cưỡng bức và cộng hưởng

Với lực $F_{\max}\cos\omega_dt$ và $b>0$, biên độ đáp ứng ổn định là

$$
A=\frac{F_{\max}}{\sqrt{(k-m\omega_d^2)^2+b^2\omega_d^2}}.
$$

![Tổng kết cộng hưởng: Những đường biên độ theo tần số của cùng hệ với các mức cản khác nhau.](/vat-ly-1/bai-giang/img/young-14/r-theory-summary-forced.png)

Đáp ứng ổn định có tần số của lực cưỡng bức. Khi cản yếu, biên độ có đỉnh gần tần số riêng không cản. Tăng cản làm đỉnh thấp, rộng và dịch xuống tần số thấp, rồi có thể mất đỉnh dương. Tại tần số không, đáp ứng trở về độ lệch tĩnh $F_{\max}/k$.
