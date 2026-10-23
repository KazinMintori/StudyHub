## 10.4 Công và công suất trong chuyển động quay

Khi đạp xe hoặc dùng động cơ quay một trục, năng lượng truyền đi qua tác dụng quay của lực. Để nối mômen lực với công, ta bắt đầu từ chuyển dời rất nhỏ của điểm đặt lực.

![Hình 10.21: Thành phần lực tiếp tuyến thực hiện công khi điểm đặt đi dọc cung tròn trong một góc quay nhỏ.](../img/young-10/a-hinh-10-21.png)

### Công do mômen lực thực hiện

Xét một điểm cách trục cố định khoảng $R$. Khi vật quay góc $d\theta$, điểm đặt đi được cung $ds=R\,d\theta$. Chỉ thành phần tiếp tuyến của lực góp vào công, nên:

$$
\begin{aligned}
dW&=F_t\,ds\\
&=F_tR\,d\theta\\
&=\tau_z\,d\theta.
\end{aligned} \tag{10.19}
$$

Ở đây, $\tau_z$ và $d\theta$ đều có dấu theo cùng chiều dương quanh trục. Lấy tích phân trên góc quay:

$$
W=\int_{\theta_1}^{\theta_2}\tau_z\,d\theta. \tag{10.20}
$$

Nếu mômen không đổi trên cả khoảng:

$$
W=\tau_z(\theta_2-\theta_1). \tag{10.21}
$$

Góc trong công thức công phải tính bằng radian. Mômen tính bằng newton mét, còn công tính bằng joule. Thành phần lực dọc trục và xuyên tâm không làm công trong chuyển động quay quanh trục cố định, vì vuông góc với chuyển dời tiếp tuyến.

### Định lý công và động năng quay

Với vật rắn có mômen quán tính không đổi, tổng mômen là $\tau_z=I\alpha_z$. Trong khoảng thời gian $dt$, ta có $d\theta=\omega_zdt$ và $d\omega_z=\alpha_zdt$. Vì thế, hai biểu thức $\alpha_zd\theta$ và $\omega_zd\omega_z$ đều bằng $\alpha_z\omega_zdt$:

$$
\alpha_z\,d\theta=\omega_z\,d\omega_z.
$$

Phép biến đổi không cần chia cho vận tốc góc, nên vẫn phù hợp ở thời điểm vật bắt đầu từ nghỉ. Công của tổng mômen ngoại lực là:

$$
\begin{aligned}
W&=\int_{\omega_{1z}}^{\omega_{2z}}I\omega_z\,d\omega_z\\
&=\tfrac12I\omega_{2z}^2-\tfrac12I\omega_{1z}^2.
\end{aligned} \tag{10.22}
$$

Công tổng cộng bằng độ biến thiên động năng quay. Cần phân biệt công của một lực với công của hợp lực. Chẳng hạn, rotor trực thăng quay đều vẫn nhận công dương từ động cơ, đồng thời chịu công âm do sức cản không khí.

![Hình 10.22: Rotor quay đều có động năng không đổi vì công dương của động cơ được cân bằng bởi công âm do không khí.](../img/young-10/a-hinh-10-22.png)

### Công suất tức thời

Chia quan hệ vi phân công cho $dt$ và dùng $\omega_z=d\theta/dt$:

$$
P=\tau_z\omega_z. \tag{10.23}
$$

Mômen cùng chiều vận tốc góc cho công suất dương, nghĩa là lực truyền năng lượng vào chuyển động quay. Khi hai đại lượng trái dấu, lực lấy năng lượng khỏi chuyển động quay. Đây là dạng quay tương ứng với công suất $\vec F\cdot\vec v$ của lực trong chuyển động tịnh tiến.

::: example Ví dụ 10.8: Công suất của động cơ quay đá mài

Động cơ tác dụng mômen không đổi $10\,\mathrm{N\cdot m}$ lên đá mài có mômen quán tính $2{,}0\,\mathrm{kg\cdot m^2}$. Hệ bắt đầu từ nghỉ. Tìm công của động cơ trong $8{,}0\,\mathrm s$, động năng đá mài lúc ấy và công suất trung bình.

**Tóm tắt đề bài:** Mômen duy nhất là mômen động cơ. $\tau_z=10\,\mathrm{N\cdot m}$, $I=2{,}0\,\mathrm{kg\cdot m^2}$ và $t=8{,}0\,\mathrm s$.

**Hướng đi:** Mômen không đổi cho gia tốc góc không đổi. Tìm góc quay và vận tốc góc bằng động học, rồi tính công, động năng và công suất trung bình bằng ba quan hệ độc lập.

**Lời giải:**

$$
\alpha_z=\tau_z/I=5{,}0\,\mathrm{rad/s^2}.
$$

Từ trạng thái nghỉ:

$$
\begin{aligned}
\Delta\theta&=\tfrac12\alpha_zt^2\\
&=160\,\mathrm{rad},\\
\omega_z&=\alpha_zt\\
&=40\,\mathrm{rad/s}.
\end{aligned}
$$

Công và động năng:

$$
\begin{aligned}
W&=\tau_z\Delta\theta=1600\,\mathrm J,\\
K&=\tfrac12I\omega_z^2=1600\,\mathrm J.
\end{aligned}
$$

Hai kết quả bằng nhau vì hệ bắt đầu từ nghỉ và không có mômen khác thực hiện công. Công suất trung bình:

$$
P_{\mathrm{av}}=W/t=200\,\mathrm W.
$$

Không được coi đây là công suất tức thời ở cuối khoảng. Trong ví dụ này, $P=\tau_z\omega_z$ tăng từ không lên $400\,\mathrm W$. Giá trị trung bình bằng một nửa giá trị cuối vì vận tốc góc tăng tuyến tính theo thời gian.
:::

### Câu tự kiểm 10.4

Tác dụng cùng mômen không đổi lên hai trụ có mômen quán tính khác nhau, đều bắt đầu từ nghỉ. Sau một vòng quay trọn vẹn, trụ nào có động năng lớn hơn?

- (i) Trụ 1.
- (ii) Trụ 2.
- (iii) Hai trụ có cùng động năng.

<details><summary>Xem giải thích</summary>

Chọn (iii). Cùng mômen và cùng góc quay $2\pi$ cho cùng công $W=2\pi\tau_z$. Vì động năng ban đầu đều bằng không, động năng cuối bằng nhau. Hai trụ có thể có vận tốc góc khác nhau vì mômen quán tính khác nhau.

</details>
