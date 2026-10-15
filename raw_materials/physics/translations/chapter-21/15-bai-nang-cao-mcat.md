<!-- Source: Challenge and MCAT-style Problems21.93–21.101, printed716–717, PDF736–737. -->

## Bài tập nâng cao

::: exercise 21.93 ••• CP CALC
Hai thanh mảnh dài L, mỗi thanh có điện tích tổng $+Q$, song song và cách a. Thanh thứ nhất từ gốc lên trục y dương, thanh thứ hai có đầu dưới trên trục x dương. (a) Giải thích vì sao thành phần y của tổng lực lên thanh thứ hai bằng không. (b) Tìm thành phần x của lực nhỏ $dF_2$ lên đoạn $dy_2$ ở $y_2$ do thanh thứ nhất. Bước này cần tích phân trên các phần $dy_1$ của thanh thứ nhất. (c) Tích phân $dF_{2x}$ trên thanh thứ hai để tìm tổng lực $\vec F_2$. (d) Chứng tỏ khi $a\gg L$:

$$
\vec F_2\approx\frac{Q^2}{4\pi\varepsilon_0a^2}\hat{\mathbf i}.
$$

(e) Tìm công bên ngoài để đưa thanh thứ hai từ rất xa đến $x=a$, giữ thanh thứ nhất ở $x=0$. Công này là thế năng cấu hình. (f) Với $L=50.0\,\mathrm{cm}$, $a=10.0\,\mathrm{cm}$, $Q=10.0\,\mu\mathrm C$ và khối lượng mỗi thanh $m=500\,\mathrm g$, nếu thả hai thanh, tốc độ tương đối cuối cùng khi chúng xa nhau là bao nhiêu?
:::


<!-- detailed-solution:21.93 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hai thanh dài L cùng điện tích Q, nằm song song cách a.

**Hướng đi:**

- Mỗi phần tử chịu lực Coulomb của toàn thanh còn lại.
- Tích phân lần đầu theo y₁ để tìm lực phần tử, lần hai theo y₂ để có lực tổng.
- Đối xứng qua giữa chiều dài triệt tiêu thành phần y toàn thanh.

(a) Hai thanh đối xứng qua đường y = L/2. Với mỗi cặp phần tử tại y₁,y₂, có cặp phản chiếu tại L − y₁,L − y₂. Hai cặp có cùng khoảng cách và cùng điện tích, nhưng thành phần lực theo y trái dấu. Cộng toàn bộ các cặp cho F₂ᵧ = 0. Thành phần y lên từng đoạn riêng lẻ không nhất thiết bằng không.

(b) Với $\lambda=Q/L$:

$$
dF_{2x} = k\lambda^2a\,dy_2 \times\int_0^L\frac{dy_1}{[a^2+(y_2-y_1)^2]^{3/2}}.
$$

Giữ y₂ cố định rồi đặt u = y₂ − y₁, nên du = −dy₁. Khi y₁ chạy từ 0 đến L, u chạy từ y₂ đến y₂ − L. Đổi chiều cận loại dấu trừ:

$$
I(y_2)=\int_{y_2-L}^{y_2}\frac{du}{(a^2+u^2)^{3/2}}.
$$

Một nguyên hàm là:

$$
G(u)=\frac{u}{a^2\sqrt{a^2+u^2}}.
$$

Thật vậy, lấy đạo hàm u/√(a² + u²) cho a²/(a² + u²)^(3/2). Chia thêm a² trong G trả lại hàm dưới dấu tích phân. Thế cận:

$$
\begin{aligned}
I(y_2) &= G(y_2)-G(y_2-L) \\
&= \frac1{a^2}\left(\frac{y_2}{r_0}+\frac{L-y_2}{r_L}\right).
\end{aligned}
$$

Ở đây $r_0=\sqrt{a^2+y_2^2}$ và $r_L=\sqrt{a^2+(L-y_2)^2}$. Nhân I với hệ số kλ²a dy₂ trong biểu thức lực ban đầu:

$$
dF_{2x}=\frac{k\lambda^2}{a}\left(\frac{y_2}{r_0}+\frac{L-y_2}{r_L}\right)dy_2.
$$

(c) Tích phân trên $0\le y_2\le L$. Hai số hạng trong ngoặc có cùng tích phân, vì đặt v = L − y₂ biến số hạng thứ hai thành số hạng thứ nhất. Tích phân cần tính là:

$$
\begin{aligned}
J &= \int_0^L\frac{y\,dy}{\sqrt{a^2+y^2}} \\
&= \left[\sqrt{a^2+y^2}\right]_0^L \\
&= \sqrt{a^2+L^2}-a.
\end{aligned}
$$

Do đó:

$$
F_{2x} = \frac{2k\lambda^2}{a}J = \frac{2kQ^2}{L^2}\frac{J}{a}.
$$

Đặt $\eta=L/a\ll1$. Khai triển căn bậc hai đến số hạng bậc hai theo η:

$$
\begin{aligned}
\sqrt{a^2+L^2} &= a\sqrt{1+\eta^2} \\
&\approx a\left(1+\frac12\eta^2\right), \\
J &= a\left(\sqrt{1+\eta^2}-1\right) \\
&\approx \frac{a\eta^2}{2} \\
&= \frac{L^2}{2a}.
\end{aligned}
$$

Thay J vào biểu thức lực:

$$
F_{2x} = \frac{2kQ^2J}{L^2a} \approx \frac{kQ^2}{a^2}.
$$

Ở khoảng cách lớn, mỗi thanh phân bố điện tích tạo trường gần như điện tích điểm Q.

(e) Công ngoài khi đưa thanh chậm từ rất xa đến a bằng thế năng cuối. Lực đẩy hướng về phía khoảng cách tăng, còn lực ngoài hướng ngược lại, nên:

$$
U(a)=\int_a^\infty F_{2x}(s)\,ds.
$$

Thay biểu thức lực ở (c). Phần cần tích phân là √(s² + L²)/s − 1. Một nguyên hàm là:

$$
H(s) = \sqrt{s^2+L^2}-s -L\ln\frac{L+\sqrt{s^2+L^2}}s.
$$

Lấy đạo hàm H cho đúng √(s² + L²)/s − 1. Khi s tiến ra vô hạn, √(s² + L²) − s tiến về không và logarit cũng tiến về không. Vì vậy H(∞) = 0. Thế hai cận vào tích phân:

$$
U(a)=\frac{2kQ^2}{L^2}[H(\infty)-H(a)].
$$

Thế s = a vào H rồi đổi dấu từng số hạng, ta được:

$$
-H(a) = L\ln\frac{L+\sqrt{a^2+L^2}}a +a-\sqrt{a^2+L^2}.
$$

Nhân từng số hạng với hệ số 2kQ²/L² cho kết quả:

$$
U(a) = \frac{2kQ^2L}{L^2}\ln\frac{L+\sqrt{a^2+L^2}}a +\frac{2kQ^2a}{L^2} -\frac{2kQ^2}{L^2}\sqrt{a^2+L^2}.
$$

(f) Hai thanh có cùng khối lượng, từ nghỉ nên động lượng tổng bằng không. Mỗi thanh có tốc độ v ngược chiều nhau; $mv^2=U(a)$ và tốc độ tương đối $v_{\mathrm{rel}}=2v$. Thế dữ kiện cho U = 5,37 J, nên $v_{\mathrm{rel}}=2\sqrt{U/0.500}=6.55$ m/s.
:::

::: exercise 21.94 ••• CP CALC
Thanh cách điện cứng dài $2a$, khối lượng không đáng kể, gắn tâm vào trục tại gốc và quay trong mặt xy. Một đầu gắn cầu khối lượng M, điện tích Q, đầu kia gắn cầu cùng khối lượng M không mang điện. Trong vùng $y>0$ có trường $\vec E=-E\hat{\mathbf i}$, còn vùng $y<0$ không có trường. Gọi $\vec r$ từ tâm đến đầu mang điện và $\theta$ là góc với trục x dương. Ban đầu $\theta=0$, hệ được đẩy nhẹ theo chiều tăng góc. (a) Viết $\vec r$. (b) Tìm mômen quanh tâm khi $0\le\theta\le\pi$. (c) Tìm mômen khi $\pi\le\theta\le2\pi$. (d) Tìm mômen quán tính quanh z. (e) Dùng $\tau=-dU/d\theta$ để viết $U(\theta)$ trên $0\le\theta\le4\pi$, chọn $U(0)=0$ và bảo đảm liên tục. (f) Với tốc độ góc $\omega(\theta)$, dùng $\tau=I\,d^2\theta/dt^2$ để chứng tỏ $I\omega^2/2+U$ bảo toàn. (g) Từ bảo toàn năng lượng, tìm tốc độ góc ở lần thứ n mà đầu dương qua trục y âm.
:::


<!-- detailed-solution:21.94 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Thanh quay có một đầu Q, một đầu trung hòa, mỗi cầu M; trường −x chỉ ở nửa mặt phẳng trên.

**Hướng đi:**

- Tích có hướng vị trí–lực cho mômen.
- Tích phân mômen theo góc để có thế năng trên góc quay được theo dõi liên tục.
- Không buộc thế năng tuần hoàn khi trường thực hiện công khác không qua một vòng.

(a) $\vec r=a\cos\theta\hat{\mathbf i}+a\sin\theta\hat{\mathbf j}$. (b) Ở $0<\theta<\pi$, lực $-QE\hat{\mathbf i}$ cho $\vec\tau=QaE\sin\theta\hat{\mathbf k}$. (c) Ở $\pi<\theta<2\pi$, mômen bằng không. (d) $I=2Ma^2$.

(e) Với $U(0)=0$:

$$
U_1(\theta)=QaE(\cos\theta-1).
$$

Biểu thức này áp dụng khi $0\le\theta\le\pi$. Khi $\pi\le\theta\le2\pi$:

$$
U_2=-2QaE.
$$

Khi $2\pi\le\theta\le3\pi$:

$$
U_3(\theta)=QaE(\cos\theta-3).
$$

Khi $3\pi\le\theta\le4\pi$:

$$
U_4=-4QaE.
$$

Các giá trị hai phía mỗi điểm nối bằng nhau. (f) Nhân phương trình $I\ddot\theta=\tau=-U'(\theta)$ với $\dot\theta$ cho:

$$
\begin{aligned}
I\dot\theta\ddot\theta+U'(\theta)\dot\theta &= 0, \\
K &= \frac12I\dot\theta^2, \\
\frac d{dt}(K+U) &= 0.
\end{aligned}
$$

(g) Ở lần thứ n qua trục y âm, góc là $3\pi/2+2(n-1)\pi$ và U = −2nQaE. Bỏ năng lượng của cú đẩy vô cùng nhỏ:

$$
\omega_n = \sqrt{\frac{4nQaE}{I}} = \sqrt{\frac{2nQE}{Ma}}.
$$
:::

::: exercise 21.95 •••
Ba điện tích như Hình P21.95. $|q_1|=2.00\,\mu\mathrm C$, nhưng chưa biết dấu $q_1$ và giá trị $q_2$. $q_3=+4.00\,\mu\mathrm C$, tổng lực lên $q_3$ hoàn toàn hướng $-x$. (a) Với các dấu có thể của $q_1,q_2$, vẽ bốn cấu hình lực thành phần. (b) Từ hình và hướng tổng lực, suy ra dấu hai nguồn. (c) Tính độ lớn $q_2$. (d) Tính độ lớn tổng lực lên $q_3$.
:::

![Hình P21.95: Tam giác điện tích có các cạnh 3,00, 4,00 và 5,00 centimét](img/young-21/hinh-p21-95.png)


<!-- detailed-solution:21.95 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Q₃ dương, hai khoảng đến nguồn là 4,00 và 3,00 cm; lực tổng trái.

**Hướng đi:**

- Xét bốn sơ đồ dấu để chọn hai lực vừa có thành phần ngang trái vừa có thành phần đứng bù nhau.
- Hình tam giác 3–4–5 cho các tỷ số chiếu, không được coi một lực nằm ngang.

Nếu $q_1<0$, lực thứ nhất hút xuống trái. Để bù thành phần xuống và còn hướng trái, $q_2$ phải dương, đẩy lên trái. Ba cặp dấu còn lại không tạo tổng hoàn toàn trái.

Với $F_1=k|q_1q_3|/0.0400^2$ và $F_2=k|q_2q_3|/0.0300^2$, cân bằng đứng là $-(3/5)F_1+(4/5)F_2=0$. Do đó:

$$
\begin{aligned}
F_2 &= \frac34F_1, \\
q_2 &= \frac34|q_1|\left(\frac{0.0300}{0.0400}\right)^2 \\
&= +0.844\,\mu\mathrm C, \\
F &= \frac45F_1+\frac35F_2 \\
&= 56.2\,\mathrm N.
\end{aligned}
$$
:::

::: exercise 21.96 •••
Hai nguồn như Hình P21.96. $|q_1|=3.00\,\mu\mathrm C$, chưa biết dấu $q_1$ và giá trị $q_2$. Tổng trường tại P hoàn toàn hướng $-y$. (a) Vẽ bốn cấu hình trường thành phần ứng với các dấu nguồn. (b) Từ hình và hướng trường tổng, suy ra dấu nguồn. (c) Tìm độ lớn trường tổng.
:::

![Hình P21.96: Điểm P và hai nguồn tạo tam giác 5,0–12,0–13,0 centimét](img/young-21/hinh-p21-96.png)


<!-- detailed-solution:21.96 -->
::: solution Chi tiết
**Tóm tắt đề bài:** P cách q₁ 5,0 cm và q₂ 12,0 cm, hai nguồn cách 13,0 cm; trường tổng xuống.

**Hướng đi:**

- Dùng hình học tam giác vuông để chiếu trường thành phần.
- Muốn tổng đứng xuống, cả hai nguồn phải âm: Mỗi trường tại P hướng về một nguồn dưới, với thành phần ngang đối nhau.

Chọn gốc tại q₁, q₂ tại x = 0,130 m. Khi đó $x_P=0.050^2/0.130$, $y_P=(0.050)(0.120)/0.130$. Điều kiện thành phần ngang bằng không:

$$
\frac{|q_1|x_P}{0.050^3} = \frac{|q_2|(0.130-x_P)}{0.120^3}.
$$

Cho $q_1=-3.00$ µC, suy ra $q_2=-7.20$ µC. Thành phần đứng:

$$
\begin{aligned}
E_y &= -\frac{ky_P|q_1|}{0.050^3} -\frac{ky_P|q_2|}{0.120^3} \\
&= -1.17\times10^7\,\mathrm{N/C}.
\end{aligned}
$$

Bốn sơ đồ dấu được tạo bằng việc đảo riêng từng vector; chỉ hai nguồn âm đáp ứng hướng yêu cầu.
:::

::: exercise 21.97 ••• CALC
Hai thanh mảnh dài L nằm trên trục x. Thanh thứ nhất từ $x=a/2$ đến $x=a/2+L$, thanh thứ hai từ $x=-a/2$ đến $x=-a/2-L$. Mỗi thanh có điện tích dương đều Q. (a) Tính trường do thanh thứ hai tại các điểm trục x dương. (b) Chứng tỏ độ lớn lực giữa hai thanh là:

$$
F = \frac{Q^2}{4\pi\varepsilon_0L^2}\ln\left[\frac{(a+L)^2}{a(a+2L)}\right].
$$

(c) Khi $a\gg L$, chứng tỏ lực trở thành $Q^2/(4\pi\varepsilon_0a^2)$ và giải thích. Gợi ý: Dùng khai triển với $|z|\ll1$:

$$
\ln(1+z) = z-\frac12z^2 +\frac13z^3-\cdots.
$$

Giữ mọi khai triển ít nhất đến bậc $L^2/a^2$.
:::


<!-- detailed-solution:21.97 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hai thanh cùng trục, mỗi thanh dài L, điện tích Q, khoảng giữa hai đầu gần là a.

**Hướng đi:**

- Tính trường thanh trái tại điểm x dương rồi tích phân lực lên thanh phải.
- Các trường và lực cùng hướng trục nên không cần cộng thành phần đứng.

(a) Với mật độ Q/L:

Gọi u đo từ đầu gần của thanh trái về phía trái, 0 ≤ u ≤ L. Khoảng cách từ phần nguồn đến điểm x dương là x + a/2 + u. Đặt c = x + a/2 > 0:

$$
\begin{aligned}
E_x(x) &= \frac{kQ}{L}\int_0^L\frac{du}{(c+u)^2} \\
&= \frac{kQ}{L}\left[-\frac1{c+u}\right]_0^L \\
&= \frac{kQ}{L}\left(\frac1c-\frac1{c+L}\right).
\end{aligned}
$$

Thay lại c = x + a/2:

$$
\begin{aligned}
E_x(x) &= \frac{kQ}{L(x+a/2)} -\frac{kQ}{L(x+a/2+L)}, \\
E_y &= 0.
\end{aligned}
$$

(b)

Mỗi phần dx của thanh phải mang Qdx/L. Tổng lực là Q/L nhân tích phân trường trên thanh phải. Hai số hạng của Eₓ có hiệu nguyên hàm:

$$
J(x)=\ln\frac{x+a/2}{x+a/2+L}.
$$

Đạo hàm J là 1/(x + a/2) − 1/(x + a/2 + L). Ở hai cận:

$$
\begin{aligned}
J(a/2+L) &= \ln\frac{a+L}{a+2L}, \\
J(a/2) &= \ln\frac a{a+L}.
\end{aligned}
$$

Lấy giá trị trên trừ giá trị dưới, rồi dùng hiệu hai logarit bằng logarit tỷ số:

$$
\begin{aligned}
F &= \frac QL\int_{a/2}^{a/2+L}E_x(x)\,dx \\
&= \frac{kQ^2}{L^2}[J(a/2+L)-J(a/2)] \\
&= \frac{kQ^2}{L^2}\ln\frac{(a+L)^2}{a(a+2L)}.
\end{aligned}
$$

(c) Đặt z = L/a ≪ 1. Logarithm là $2\ln(1+z)-\ln(1+2z)$. Khai triển đến z² cho $(2z-z^2)-(2z-2z^2)=z^2$. Vì vậy $F\approx kQ^2/a^2$, đúng gần đúng hai nguồn điểm ở xa.
:::

## Bài tập đọc hiểu theo dạng MCAT

### BIO: Điện tích của ong

Côn trùng bay như ong có thể tích điện dương nhỏ khi bay. Trong một thí nghiệm trên 50 con, điện tích trung bình mỗi ong là $+(30\pm5)\,\mathrm{pC}$. Người nghiên cứu cũng đo điện tích ở thân cây có hoa trên cuống dài khi ong đến gần, đáp và bay đi. Cây thường trung hòa nên thân có điện tích tổng bằng không khi ong còn rất xa. Khi ong gần hoa, thân đã có một điện tích dương nhỏ trước khi ong đáp. Sau khi đáp, toàn cây dương và giữ điện tích dương sau khi ong rời đi. Thử với hoa nhân tạo có điện tích khác nhau cho thấy ong phân biệt hoa mang điện với hoa không mang điện, và có thể dùng điện tích dương của lần thăm trước làm dấu hiệu hoa đã được ghé, khi phấn có thể còn ít.

::: exercise 21.98
Một con ong có điện tích bằng giá trị trung bình trên. Điện tích này tương ứng xấp xỉ bao nhiêu electron thiếu?

(a) $1.9\times10^8$; (b) $3.0\times10^8$; (c) $1.9\times10^{18}$; (d) $3.0\times10^{18}$.
:::


<!-- detailed-solution:21.98 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Điện tích trung bình ong là +30 pC.

**Hướng đi:**

- Điện tích dương biểu thị thiếu electron.
- Chia độ lớn điện tích cho e để đếm số thiếu.

$$
N = \frac{30\times10^{-12}}{1.602\times10^{-19}}\approx1.9\times10^8.
$$

Chọn (a).
:::

::: exercise 21.99
Giải thích nào tốt nhất cho điện tích thân cây dương khi ong đến gần, trước khi đáp?

(a) Không khí dẫn tốt, nên điện tích dương chuyển từ ong qua không khí đến cây.

(b) Đất là kho điện tích lớn, nên ion dương bị kéo lên cuống về phía ong.

(c) Cây bị phân cực khi ong mang điện đến gần.

(d) Những con ong đến trước để lại điện tích dương trên thân.
:::


<!-- detailed-solution:21.99 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Thân cây dương trước khi ong dương chạm hoa.

**Hướng đi:**

- Chưa tiếp xúc nên cần xét phân bố lại điện tích, không mặc định đã truyền điện tích qua không khí.
- Ong dương hút electron về phía hoa, làm phần thân đang đo thiếu electron tương đối.

Cây bị phân cực dù tổng điện tích trước tiếp xúc có thể còn bằng không. Chọn (c). Sau khi ong đáp, sự trao đổi điện tích là giai đoạn khác.
:::

::: exercise 21.100
Một ong rời hoa đã để lại điện tích dương. Một ong khác có cùng lượng điện tích dương bay gần cây. Hình nào trong P21.100 biểu diễn đúng nhất đường sức giữa ong và hoa?
:::

![Hình P21.100: Bốn phương án đường sức giữa ong và hoa mang điện dương](img/young-21/hinh-p21-100.png)


<!-- detailed-solution:21.100 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Ong và hoa đều dương.

**Hướng đi:**

- Đường sức phải đi ra khỏi cả hai nguồn, không đi từ nguồn dương này kết thúc ở nguồn dương kia.
- Giữa chúng, các đường cong ra hai phía giống trường của hai nguồn cùng dấu.

Chọn (c): Mũi tên đi ra từ cả ong và hoa. Các phương án nối hai nguồn như lưỡng cực hoặc hướng mũi tên vào nguồn dương không phù hợp.
:::

::: exercise 21.101
Trong thí nghiệm tiếp theo, đặt $+40\,\mathrm{pC}$ ở tâm hoa nhân tạo tại đầu cuống dài $30\,\mathrm{cm}$. Ong không đến gần tâm hơn $15\,\mathrm{cm}$ trước khi bay đi. Quan sát gợi ý trường ngoài nhỏ nhất ong có thể cảm nhận gần giá trị nào?

(a) $2.4\,\mathrm{N/C}$; (b) $16\,\mathrm{N/C}$; (c) $2.7\times10^{-10}\,\mathrm{N/C}$; (d) $4.8\times10^{-10}\,\mathrm{N/C}$.
:::


<!-- detailed-solution:21.101 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Điện tích hoa +40 pC; khoảng gần nhất của ong là 0,15 m.

**Hướng đi:**

- Mô hình điện tích tại tâm cho trường $kQ/r^2$.
- Chiều dài cuống không đi vào khoảng cách từ ong đến điện tích tâm đã cho.

$$
E = \frac{k(40\times10^{-12})}{0.15^2}\approx16\,\mathrm{N/C}.
$$

Chọn (b).
:::
