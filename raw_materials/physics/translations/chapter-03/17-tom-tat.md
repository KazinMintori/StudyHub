## Tóm tắt chương 3

### 1. Vector vị trí, vận tốc và gia tốc

Vector vị trí $\vec{r}$ của một điểm $P$ trong không gian ba chiều là vector nối từ gốc tọa độ $O$ đến điểm $P$. Các thành phần tọa độ của vector vị trí là $x$, $y$ và $z$:

$$
\vec{r} = x\hat{\imath} + y\hat{\jmath} + z\hat{k} \tag{3.1}
$$

Vector vận tốc trung bình $\vec{v}_{\mathrm{tb}}$ trong khoảng thời gian $\Delta t$ bằng độ dời $\Delta\vec{r}$ chia cho khoảng thời gian $\Delta t$:

$$
\vec{v}_{\mathrm{tb}} = \frac{\Delta\vec{r}}{\Delta t} \tag{3.2}
$$

Vector vận tốc tức thời $\vec{v}$ là đạo hàm của vector vị trí $\vec{r}$ theo thời gian. Các thành phần của vector vận tốc tức thời là đạo hàm theo thời gian của các tọa độ $x$, $y$, $z$:

$$
\vec{v} = \lim_{\Delta t \to 0} \frac{\Delta\vec{r}}{\Delta t} = \frac{d\vec{r}}{dt} \tag{3.3}
$$

$$
v_x = \frac{dx}{dt}
$$

$$
v_y = \frac{dy}{dt}
$$

$$
v_z = \frac{dz}{dt} \tag{3.4}
$$

Tốc độ tức thời là độ lớn của vector vận tốc tức thời $|\vec{v}|$. Vector vận tốc của chất điểm luôn tiếp tuyến với quỹ đạo tại mọi điểm chuyển động.

Vector gia tốc trung bình $\vec{a}_{\mathrm{tb}}$ trong khoảng thời gian $\Delta t$ bằng độ biến thiên vận tốc $\Delta\vec{v}$ chia cho $\Delta t$:

$$
\vec{a}_{\mathrm{tb}} = \frac{\Delta\vec{v}}{\Delta t} \tag{3.8}
$$

Vector gia tốc tức thời $\vec{a}$ là đạo hàm của vector vận tốc $\vec{v}$ theo thời gian. Các thành phần của nó là đạo hàm theo thời gian của $v_x$, $v_y$, $v_z$:

$$
\vec{a} = \lim_{\Delta t \to 0} \frac{\Delta\vec{v}}{\Delta t} = \frac{d\vec{v}}{dt} \tag{3.9}
$$

$$
a_x = \frac{dv_x}{dt}
$$

$$
a_y = \frac{dv_y}{dt}
$$

$$
a_z = \frac{dv_z}{dt} \tag{3.10}
$$

Thành phần gia tốc song song với vận tốc làm thay đổi tốc độ (độ lớn vận tốc), trong khi thành phần gia tốc vuông góc với vận tốc làm thay đổi hướng chuyển động của chất điểm.

![Tóm tắt các vector động học trong không gian](/vat-ly-1/bai-giang/img/young-03/r-theory-tom-tat-01.png)

*Hình 3.T1: Vector vị trí, vector vận tốc trung bình và vector gia tốc trung bình trong mặt phẳng hai chiều.*

---

### 2. Chuyển động ném vật (Projectile Motion)

Trong chuyển động ném vật bỏ qua lực cản của không khí, gia tốc của vật là gia tốc rơi tự do hướng thẳng đứng xuống dưới. Các thành phần là $a_x=0$ và $a_y=-g$. Khi chọn gốc tọa độ tại vị trí ném ban đầu ($x_0 = 0$, $y_0 = 0$), tọa độ và các thành phần vận tốc là các hàm số đơn giản của thời gian:

$$
x = (v_0\cos\alpha_0)t \tag{3.19}
$$

$$
y = (v_0\sin\alpha_0)t - \frac{1}{2}gt^2 \tag{3.20}
$$

$$
v_x = v_0\cos\alpha_0 \tag{3.21}
$$

$$
v_y = v_0\sin\alpha_0 - gt \tag{3.22}
$$

Quỹ đạo của chuyển động ném vật luôn là một đường parabol. Tầm bay xa trên mặt phẳng ngang là:

$$
R = \frac{v_0^2\sin 2\alpha_0}{g} \tag{3.26}
$$

Tầm bay xa cực đại trên mặt đất đạt được khi góc ném ban đầu là $\alpha_0 = 45^\circ$.

![Tóm tắt chuyển động ném vật](/vat-ly-1/bai-giang/img/young-03/r-theory-tom-tat-02.png)

*Hình 3.T2: Quỹ đạo parabol của chuyển động ném vật với vector vận tốc tại từng vị trí đặc trưng.*

---

### 3. Chuyển động tròn đều và không đều (Circular Motion)

Khi chất điểm chuyển động trên đường tròn bán kính $R$ với tốc độ không đổi $v$, chuyển động đó là chuyển động tròn đều. Vector gia tốc luôn hướng thẳng vào tâm đường tròn và vuông góc với vector vận tốc. Độ lớn của gia tốc hướng tâm này được tính theo tốc độ $v$ hoặc theo chu kỳ $T$ (thời gian để đi hết một vòng quay):

$$
a_{\mathrm{rad}} = \frac{v^2}{R} \tag{3.27}
$$

$$
v = \frac{2\pi R}{T} \tag{3.28}
$$

$$
a_{\mathrm{rad}} = \frac{4\pi^2 R}{T^2} \tag{3.29}
$$

Nếu tốc độ biến đổi theo thời gian (chuyển động tròn không đều), ngoài thành phần hướng tâm $a_{\mathrm{rad}}$ luôn hướng vào tâm, gia tốc còn có thêm thành phần tiếp tuyến $a_{\mathrm{tan}}$ song song với quỹ đạo:

$$
a_{\mathrm{tan}} = \frac{d|\vec{v}|}{dt} \tag{3.30}
$$

Thành phần tiếp tuyến $a_{\mathrm{tan}}$ bằng tốc độ biến thiên của tốc độ. Nó cùng hướng với vận tốc khi vật tăng tốc và ngược hướng khi vật giảm tốc.

![Tóm tắt chuyển động tròn](/vat-ly-1/bai-giang/img/young-03/r-theory-tom-tat-03.png)

*Hình 3.T3: Phân bố vector vận tốc và gia tốc hướng tâm trong chuyển động tròn đều.*

---

### 4. Vận tốc tương đối (Relative Velocity)

Khi một vật thể $P$ chuyển động đối với hệ quy chiếu $B$, và bản thân hệ quy chiếu $B$ lại chuyển động đối với hệ quy chiếu $A$:
- Ký hiệu $\vec{v}_{P/B}$ là vận tốc của $P$ đối với $B$.
- Ký hiệu $\vec{v}_{P/A}$ là vận tốc của $P$ đối với $A$.
- Ký hiệu $\vec{v}_{B/A}$ là vận tốc của $B$ đối với $A$.

Nếu các vận tốc đều cùng nằm trên một đường thẳng (chuyển động một chiều):

$$
v_{P/A-x} = v_{P/B-x} + v_{B/A-x} \tag{3.32}
$$

Trong không gian hai hoặc ba chiều tổng quát, quy tắc cộng vector vận tốc (phép biến đổi vận tốc Galilei) là:

$$
\vec{v}_{P/A} = \vec{v}_{P/B} + \vec{v}_{B/A} \tag{3.35}
$$

Đổi chiều vai trò hai hệ quy chiếu:

$$
\vec{v}_{A/B} = -\vec{v}_{B/A} \tag{3.36}
$$

Nếu hệ quy chiếu $B$ chuyển động thẳng đều đối với hệ quy chiếu $A$, gia tốc của vật là như nhau trong cả hai hệ quy chiếu:

$$
\vec{a}_{P/A} = \vec{a}_{P/B} \tag{3.37}
$$

![Tóm tắt vận tốc tương đối](/vat-ly-1/bai-giang/img/young-03/r-theory-tom-tat-04.png)

*Hình 3.T4: Quy tắc cộng vector vận tốc tương đối giữa máy bay, luồng không khí và bề mặt Trái Đất.*
