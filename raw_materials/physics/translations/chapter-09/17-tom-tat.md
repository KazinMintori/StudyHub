<!-- Nguồn: Tóm tắt chương 9, trang in 291, trang PDF 311. -->

## Tóm tắt chương 9: Chuyển động quay của vật rắn

### 1. Động học chuyển động quay

Khi một vật rắn quay quanh một trục cố định (thường được chọn là trục tọa độ $z$), vị trí của vật được xác định bởi tọa độ góc $\theta$.

Vận tốc góc $\omega_z$ là đạo hàm theo thời gian của tọa độ góc $\theta$:

$$
\begin{aligned}
\omega_z &= \lim_{\Delta t \to 0} \frac{\Delta \theta}{\Delta t} \\
&= \frac{d\theta}{dt} \tag{9.3}
\end{aligned}
$$

Gia tốc góc $\alpha_z$ là đạo hàm bậc nhất theo thời gian của vận tốc góc $\omega_z$, hoặc đạo hàm bậc hai của tọa độ góc $\theta$:

$$
\begin{aligned}
\alpha_z &= \lim_{\Delta t \to 0} \frac{\Delta \omega_z}{\Delta t} \\
&= \frac{d\omega_z}{dt} \tag{9.5}
\end{aligned}
$$

Trong trường hợp đặc biệt khi gia tốc góc $\alpha_z$ là hằng số, tọa độ góc $\theta$, vận tốc góc $\omega_z$ và gia tốc góc $\alpha_z$ liên hệ với nhau qua các phương trình động học:

$$
\theta = \theta_0 + \omega_{0z} t + \frac{1}{2} \alpha_z t^2 \tag{9.11}
$$

$$
\theta - \theta_0 = \frac{1}{2} (\omega_{0z} + \omega_z) t \tag{9.10}
$$

$$
\omega_z = \omega_{0z} + \alpha_z t \tag{9.7}
$$

$$
\omega_z^2 = \omega_{0z}^2 + 2\alpha_z (\theta - \theta_0) \tag{9.12}
$$

![Sơ đồ tổng kết 1: Động học chuyển động quay quanh trục cố định z. Tọa độ góc biến thiên từ góc theta1 tại thời điểm t1 đến góc theta2 tại thời điểm t2 với độ dời góc Delta theta.](./img/young-09/b-tom-tat-9-01.png)

### 2. Mối liên hệ giữa động học dài và động học góc

Tốc độ góc $\omega$ của vật rắn là độ lớn của vận tốc góc. Tốc độ biến thiên của tốc độ góc là $\alpha = \frac{d\omega}{dt}$.

Đối với một chất điểm bất kỳ trong vật rắn nằm cách trục quay một khoảng vuông góc $r$:

Tốc độ dài $v$ của chất điểm tỷ lệ với tốc độ góc $\omega$:

$$
v = r \omega \tag{9.13}
$$

Gia tốc tiếp tuyến $a_{\text{tan}}$ đặc trưng cho sự thay đổi về độ lớn của tốc độ dài:

$$
\begin{aligned}
a_{\text{tan}} &= \frac{dv}{dt} \\
&= r \alpha \tag{9.14}
\end{aligned}
$$

Gia tốc hướng tâm $a_{\text{rad}}$ đặc trưng cho sự thay đổi về phương chiều của vận tốc:

$$
\begin{aligned}
a_{\text{rad}} &= \frac{v^2}{r} \\
&= \omega^2 r \tag{9.15}
\end{aligned}
$$

![Sơ đồ tổng kết 2: Mối liên hệ giữa các đại lượng động học dài của điểm P và các đại lượng động học góc của vật rắn. Điểm P có thành phần gia tốc tiếp tuyến atan và gia tốc hướng tâm arad.](./img/young-09/b-tom-tat-9-02.png)

### 3. Momen quán tính và động năng quay

Momen quán tính $I$ của một vật rắn đối với một trục quay cho trước đặc trưng cho mức độ quán tính quay của vật. Giá trị $I$ càng lớn thì vật càng khó thay đổi trạng thái quay.

Momen quán tính được tính bằng tổng các tích khối lượng của từng phần tử hạt $m_i$ với bình phương khoảng cách vuông góc $r_i$ từ hạt đó tới trục quay:

$$
I = m_1 r_1^2 + m_2 r_2^2 + \dots
$$

Viết gọn dưới dạng dấu tổng:

$$
I = \sum_i m_i r_i^2 \tag{9.16}
$$

Động năng quay của một vật rắn quay quanh trục cố định phụ thuộc vào tốc độ góc $\omega$ và momen quán tính $I$ đối với trục quay đó:

$$
K = \frac{1}{2} I \omega^2 \tag{9.17}
$$

![Sơ đồ tổng kết 3: Vật rắn quay quanh một trục cố định với tốc độ góc omega. Mỗi hạt mi ở khoảng cách vuông góc ri tới trục quay đóng góp vào momen quán tính tổng cộng của vật thể.](./img/young-09/b-tom-tat-9-03.png)

### 4. Tính toán momen quán tính

Định lý trục song song thiết lập mối liên hệ giữa momen quán tính của một vật rắn có khối lượng $M$ đối với hai trục song song: Một trục đi qua khối tâm ($I_{\mathrm{cm}}$) và một trục song song đi qua điểm $P$ cách trục ban đầu một khoảng $d$:

$$
I_P = I_{\mathrm{cm}} + M d^2 \tag{9.19}
$$

Nếu vật thể có sự phân bố khối lượng liên tục, momen quán tính được xác định thông qua phép tính tích phân trên toàn thể tích của vật:

$$
I = \int r^2\, dm \tag{9.20}
$$

![Sơ đồ tổng kết 4: Định lý trục song song cho một vật thể có khối lượng M. Trục quay đi qua điểm P song song với trục đi qua khối tâm và cách nhau một khoảng cách vuông góc d.](./img/young-09/b-tom-tat-9-04.png)
