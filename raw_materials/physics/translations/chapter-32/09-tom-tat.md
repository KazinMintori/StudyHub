## Tổng kết chương

### Phương trình Maxwell và sóng điện từ

Hệ phương trình Maxwell dự đoán sự tồn tại của sóng điện từ lan truyền trong chân không với tốc độ bằng tốc độ ánh sáng $c$. Thang sóng điện từ trải rộng ít nhất từ $1\,\mathrm{Hz}$ đến $10^{24}\,\mathrm{Hz}$ cùng dải bước sóng tương ứng. Ánh sáng khả kiến với bước sóng từ $380\,\mathrm{nm}$ đến $750\,\mathrm{nm}$ chỉ chiếm một dải hẹp trong phổ này.

Trong sóng phẳng, điện trường $\vec{E}$ và từ trường $\vec{B}$ đồng nhất trên mọi mặt phẳng vuông góc với phương truyền sóng. Định luật cảm ứng Faraday và định luật Ampere thiết lập mối quan hệ độ lớn giữa hai trường. Điều kiện đồng thời thỏa mãn cả hai định luật cho biểu thức tốc độ ánh sáng theo hằng số điện và hằng số từ.

Một sóng phẳng chạy trong chân không là sóng ngang: Điện trường $\vec{E}$ và từ trường $\vec{B}$ vuông góc với nhau và vuông góc với phương truyền sóng. Hướng lan truyền của sóng được xác định bởi tích có hướng $\vec{E} \times \vec{B}$.

![Tổng kết 32.1: Sóng điện từ phẳng lan truyền trong chân không có các vector trường vuông góc với nhau và vuông góc với phương truyền sóng.](img/young-32/tom-tat-32-01.png)

Quan hệ giữa các đại lượng trường trong chân không:

$$
\begin{aligned}
E &= cB, \\
B &= \epsilon_0 \mu_0 cE, \\
c &= \frac{1}{\sqrt{\epsilon_0 \mu_0}}
\end{aligned}
$$

### Sóng điện từ hình sin

Sóng điện từ phẳng hình sin lan truyền trong chân không theo chiều dương trục $x$ được mô tả bởi các hàm sóng:

$$
\begin{aligned}
\vec{E}(x, t) &= \hat{\jmath} E_{\max} \times \cos(kx - \omega t), \\
\vec{B}(x, t) &= \hat{k} B_{\max} \times \cos(kx - \omega t), \\
E_{\max} &= c B_{\max}
\end{aligned}
$$

Nếu sóng truyền theo chiều âm trục $x$, pha $kx-\omega t$ được thay bằng $kx+\omega t$. Đồng thời phải đảo dấu tương đối giữa hai vector trường. Chẳng hạn, khi điện trường hướng $+y$, từ trường phải hướng $-z$ để tích có hướng chỉ theo $-x$.

![Tổng kết 32.2: Sóng điện từ hình sin lan truyền theo chiều dương trục x với điện trường phân cực theo trục y và từ trường dao động theo trục z.](img/young-32/tom-tat-32-02.png)

Biên độ điện trường và biên độ từ trường của sóng phẳng chạy trong chân không luôn liên hệ chặt chẽ qua tốc độ ánh sáng $c$.

### Sóng điện từ trong vật chất

Khi sóng điện từ lan truyền qua môi trường điện môi tuyến tính, đồng nhất, đẳng hướng, không tổn hao và được coi không tán sắc ở tần số đang xét, tốc độ pha $v$ của sóng được xác định bởi:

$$
\begin{aligned}
v &= \frac{1}{\sqrt{\epsilon \mu}} \\
&= \frac{1}{\sqrt{K K_{\mathrm{m}}}} \frac{1}{\sqrt{\epsilon_0 \mu_0}} \\
&= \frac{c}{\sqrt{K K_{\mathrm{m}}}}
\end{aligned}
$$

Trong đó $K = \epsilon/\epsilon_0$ là hằng số điện môi và $K_{\mathrm{m}} = \mu/\mu_0$ là độ từ thẩm tương đối của môi trường. Với phần lớn chất điện môi không từ tính thông thường, $K > 1$ và $K_{\mathrm{m}} \approx 1$ nên tốc độ truyền sóng nhỏ hơn tốc độ ánh sáng trong chân không ($v < c$).

### Năng lượng và động lượng trong sóng điện từ

Tốc độ truyền năng lượng trên một đơn vị diện tích của sóng điện từ trong chân không được biểu diễn bởi vector Poynting $\vec{S}$:

$$
\vec{S} = \frac{1}{\mu_0} \vec{E} \times \vec{B}
$$

Cường độ bức xạ $I$ là độ lớn của vector Poynting trung bình theo thời gian: $I = |\langle \vec{S} \rangle| = S_{\text{av}}$. Đối với sóng hình sin:

$$
\begin{aligned}
I &= S_{\text{av}} \\
&= \frac{E_{\max} B_{\max}}{2\mu_0} \\
&= \frac{E_{\max}^2}{2\mu_0 c} \\
&= \frac{1}{2} \sqrt{\frac{\epsilon_0}{\mu_0}} E_{\max}^2 \\
&= \frac{1}{2} \epsilon_0 c E_{\max}^2
\end{aligned}
$$

Sóng điện từ cũng mang động lượng. Tốc độ truyền động lượng trên một đơn vị diện tích là:

$$
\frac{1}{A} \frac{dp}{dt} = \frac{S}{c} = \frac{EB}{\mu_0 c}
$$

![Tổng kết 32.3: Năng lượng điện từ truyền qua tiết diện A trong thời gian dt được xác định bởi vector Poynting S.](img/young-32/tom-tat-32-03.png)

Khi sóng đập vào một bề mặt vuông góc với phương truyền, sóng tác dụng một áp suất bức xạ $p_{\text{rad}}$:

Đối với bề mặt hấp thụ hoàn toàn:

$$
\begin{aligned}
p_{\text{rad}} &= \frac{S_{\text{av}}}{c} \\
&= \frac{I}{c}
\end{aligned}
$$

Đối với bề mặt phản xạ hoàn toàn:

$$
\begin{aligned}
p_{\text{rad}} &= \frac{2 S_{\text{av}}}{c} \\
&= \frac{2I}{c}
\end{aligned}
$$

### Sóng dừng điện từ

Nếu đặt một bề mặt dẫn điện lý tưởng tại vị trí $x = 0$, sóng tới và sóng phản xạ giao thoa tạo thành sóng dừng điện từ:

$$
\begin{aligned}
E_y(x, t) &= -2E_{\max} \times \sin kx \sin \omega t, \\
B_z(x, t) &= -2B_{\max} \times \cos kx \cos \omega t
\end{aligned}
$$

Các mặt phẳng nút của điện trường $\vec{E}$ xuất hiện tại $kx = 0, \pi, 2\pi, \dots$ tương ứng với $x = 0, \lambda/2, \lambda, \dots$

Các mặt phẳng nút của từ trường $\vec{B}$ xuất hiện tại $kx = \pi/2, 3\pi/2, 5\pi/2, \dots$ tương ứng với $x = \lambda/4, 3\lambda/4, 5\lambda/4, \dots$

![Tổng kết 32.4: Mặt phẳng dẫn điện lý tưởng tạo sóng dừng với nút điện trường và bụng từ trường tại bề mặt phản xạ.](img/young-32/tom-tat-32-04.png)

Tại những điểm có cả hai biên độ khác không, dao động của điện trường và từ trường lệch pha nhau $90^\circ$ theo thời gian. Cường độ bức xạ trung bình (độ lớn vector Poynting trung bình theo thời gian) trong sóng dừng triệt tiêu tại mọi điểm: $I = |\langle \vec{S} \rangle| = S_{\text{av}} = 0$.

Trong hộp cộng hưởng hai thành dẫn song song cách nhau khoảng cách $L$, các mode dao động riêng có bước sóng và tần số gián đoạn:

$$
\begin{aligned}
\lambda_n &= \frac{2L}{n}, \\
f_n &= n \frac{c}{2L} \quad (n = 1, 2, 3, \dots)
\end{aligned}
$$
