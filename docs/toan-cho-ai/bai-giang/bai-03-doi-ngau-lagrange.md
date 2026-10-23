---
course: toan-cho-ai
lecture: bai-03-doi-ngau-lagrange
section: lecture
title: "Đối ngẫu Lagrange"
prerequisites: ["ham-loi", "gradient", "he-phuong-trinh"]
lessonStatus: ready
description: "Lý thuyết đối ngẫu Lagrange toàn diện: Hàm Lagrangian, đối ngẫu yếu, hàm liên hợp Fenchel, hình học đối ngẫu, điểm yên ngựa Minimax, điều kiện KKT, bổ đề Farkas và ứng dụng trong học máy."
---

Khi đối mặt với một bài toán tối ưu có ràng buộc trong thực tế, làm thế nào để chúng ta khẳng định chắc chắn rằng phương án tìm được là phương án tốt nhất, không thể cải thiện thêm được nữa? Việc tìm ra một điểm khả thi có chi phí thấp mới chỉ giải quyết một nửa bài toán. Nửa còn lại đòi hỏi một chứng nhận toán học không thể bác bỏ: Một ngưỡng cận dưới mà mọi phương án hợp lệ đều không thể vượt qua. Nếu ta chứng minh được rằng chi phí thực tế không bao giờ thấp hơn một ngưỡng $d^*$, và đồng thời ta tìm được một phương án khả thi đạt đúng ngưỡng $d^*$ đó, thì phương án ấy chắc chắn là nghiệm tối ưu toàn cục.

Lý thuyết **Đối ngẫu Lagrange (Lagrangian Duality)** chính là nền tảng toán học thiết lập các chứng nhận cận dưới như vậy. Bằng cách chuyển đổi các ràng buộc cứng thành các khoản chi phí phạt mềm tích hợp vào hàm mục tiêu, đối ngẫu Lagrange mở ra một bài toán song hành phản chiếu bài toán gốc. Không chỉ cung cấp công cụ nhận diện nghiệm, lý thuyết này còn mở rộng sang hàm liên hợp Fenchel, hình học siêu phẳng tựa, lý thuyết trò chơi minimax, phân tích độ nhạy kinh tế học (giá bóng), và khai sinh ra hệ điều kiện Karush–Kuhn–Tucker (KKT), chuẩn mực tối cao của giải tích tối ưu hiện đại.

---

## 1. Hàm Lagrangian và Bản chất dấu của các nhân tử

Xét bài toán tối ưu chuẩn tắc với biến vector $x \in \mathbb{R}^n$, gồm $m$ ràng buộc bất đẳng thức và $p$ ràng buộc đẳng thức:

$$
\begin{aligned}
&\min_{x} \quad f_0(x)\\
&\text{s.t.}\quad f_i(x) \le 0, \quad i = 1, \dots, m,\\
&\phantom{\text{subject to}\quad } h_j(x) = 0, \quad j = 1, \dots, p.
\end{aligned}
$$

Đặt $\mathcal D_0=\operatorname{dom}f_0$. Gọi $\mathcal D_f$ và $\mathcal D_h$ lần lượt là miền xác định chung của các hàm ràng buộc bất đẳng thức và đẳng thức:

$$
\begin{aligned}
\mathcal D_f &= \bigcap_{i=1}^m\operatorname{dom}f_i,\\
\mathcal D_h &= \bigcap_{j=1}^p\operatorname{dom}h_j.
\end{aligned}
$$

Như vậy, $\mathcal D_f$ gồm những điểm mà cả $f_1,\dots,f_m$ đều xác định. Miền $\mathcal D_h$ được hiểu tương tự. Miền xác định của toàn bài toán là:

$$
\mathcal D=\mathcal D_0\cap\mathcal D_f\cap\mathcal D_h.
$$

Ý tưởng nền tảng của phương pháp là đưa các ràng buộc vào hàm mục tiêu thông qua phép tổ hợp tuyến tính. Với các nhân tử $\lambda_i$ và $\nu_j$, đặt hai khoản điều chỉnh:

$$
\begin{aligned}
F_\lambda(x)&=\sum_{i=1}^m\lambda_i f_i(x)\\
&=\lambda_1f_1(x)+\dots+\lambda_mf_m(x),\\
H_\nu(x)&=\sum_{j=1}^p\nu_jh_j(x)\\
&=\nu_1h_1(x)+\dots+\nu_ph_p(x).
\end{aligned}
$$

Hàm **Lagrangian** là tổng của chi phí gốc và hai khoản điều chỉnh trên:

$$
L(x,\lambda,\nu)=f_0(x)+F_\lambda(x)+H_\nu(x).
$$

Trong đó:
- Vector $\lambda = (\lambda_1, \dots, \lambda_m)^T \in \mathbb{R}^m$ là vector **nhân tử Lagrange** gắn với các ràng buộc bất đẳng thức.
- Vector $\nu = (\nu_1, \dots, \nu_p)^T \in \mathbb{R}^p$ là vector **nhân tử Lagrange** gắn với các ràng buộc đẳng thức.

Một câu hỏi tự nhiên xuất hiện: Vì sao ta bắt buộc phải áp đặt điều kiện không âm $\lambda_i \ge 0$ cho các bất đẳng thức?

Để trả lời, ta xét một điểm khả thi bất kỳ $\widetilde x$ của bài toán gốc. Theo định nghĩa miền khả thi:
- Điểm $\widetilde x$ thỏa mãn $f_i(\widetilde x) \le 0$ với mọi $i = 1, \dots, m$. Khi ta chọn $\lambda_i \ge 0$, tích $\lambda_i f_i(\widetilde x)$ là tích của một số không âm với một số không dương, do đó luôn không dương: $\lambda_i f_i(\widetilde x) \le 0$.
- Đồng thời $\widetilde x$ thỏa mãn $h_j(\widetilde x) = 0$ với mọi $j = 1, \dots, p$, vì vậy số hạng $\nu_j h_j(\widetilde x) = 0$ triệt tiêu hoàn toàn bất kể dấu của $\nu_j$.

Cộng các số hạng, ta có $F_\lambda(\widetilde x)\le0$ và $H_\nu(\widetilde x)=0$. Vì vậy, với mọi điểm khả thi $\widetilde x$ và mọi bộ nhân tử thỏa mãn $\lambda \succeq 0$:

$$
L(\widetilde x,\lambda,\nu)\le f_0(\widetilde x).
$$

Như vậy, trên toàn bộ miền khả thi của bài toán gốc, hàm Lagrangian luôn đánh giá thấp hơn hoặc bằng giá trị chi phí thực tế. 

Từ quan sát cốt lõi này, ta định nghĩa **hàm đối ngẫu Lagrange** $g: \mathbb{R}^m \times \mathbb{R}^p \to \mathbb{R} \cup \{-\infty\}$ bằng cách lấy cận dưới đúng (infimum) của hàm Lagrangian theo toàn bộ không gian biến $x \in \mathcal{D}$:

$$
g(\lambda,\nu)=\inf_{x\in\mathcal D}L(x,\lambda,\nu).
$$

Phép lấy infimum ở đây được thực hiện trên toàn bộ miền $\mathcal{D}$ mà không cần giữ lại bất kỳ ràng buộc nào của bài toán gốc. Do giá trị nhỏ nhất của một hàm trên toàn không gian luôn nhỏ hơn hoặc bằng giá trị của nó tại một điểm khả thi cụ thể $\widetilde x$, ta có chuỗi bất đẳng thức:

$$
g(\lambda, \nu) \le L(\widetilde x, \lambda, \nu) \le f_0(\widetilde x).
$$

Bất đẳng thức trên nghiệm đúng với mọi điểm khả thi $\widetilde x$. Lấy cận dưới đúng theo toàn bộ các điểm khả thi $\widetilde x$, ta thu được kết luận:

$$
g(\lambda, \nu) \le p^* \quad \forall \lambda \succeq 0, \, \forall \nu,
$$

trong đó $p^*$ là giá trị tối ưu toàn cục của bài toán gốc.

Đặc tính quan trọng này được gọi là **Định lý Đối ngẫu yếu (Weak Duality)**. Cần nhấn mạnh một điều: Định lý đối ngẫu yếu luôn đúng cho mọi bài toán tối ưu, hoàn toàn không đòi hỏi hàm mục tiêu hay các miền ràng buộc phải có tính lồi.

---

## 2. Tính toán hàm đối ngẫu trên bài toán một chiều

Để nắm bắt trực giác tính toán, ta xét bài toán tối ưu một chiều:

$$
\min_{x \in \mathbb{R}} \quad f_0(x) = (x - 2)^2 \quad \text{s.t.} \quad x \le 1.
$$

Đưa ràng buộc về dạng chuẩn tắc: $f_1(x) = x - 1 \le 0$. Hàm Lagrangian với nhân tử $\lambda \ge 0$ là:

$$
L(x, \lambda) = (x - 2)^2 + \lambda(x - 1).
$$

Để tính hàm đối ngẫu $g(\lambda)$, ta xem $\lambda$ là tham số cố định và tìm cực tiểu của $L(x, \lambda)$ theo biến $x$ trên $\mathbb{R}$. Đạo hàm bậc nhất theo $x$:

$$
\frac{\partial L}{\partial x}=2(x-2)+\lambda=0.
$$

Giải phương trình trên được $x(\lambda)=2-\lambda/2$. Đạo hàm bậc hai $\frac{\partial^2 L}{\partial x^2} = 2 > 0$, nên đây là điểm cực tiểu toàn cục duy nhất. Khi thay nghiệm vào Lagrangian, hai hiệu lần lượt là $x(\lambda)-2=-\lambda/2$ và $x(\lambda)-1=1-\lambda/2$:

$$
\begin{aligned}
g(\lambda)&=\frac{\lambda^2}{4}+\lambda\left(1-\frac{\lambda}{2}\right)\\
&= \lambda - \frac{\lambda^2}{4}.
\end{aligned}
$$

Hàm đối ngẫu $g(\lambda) = \lambda - \lambda^2/4$ cung cấp một cận dưới cho giá trị tối ưu gốc với mỗi giá trị $\lambda \ge 0$:
- Khi chọn $\lambda = 0$: Ta có $g(0) = 0 \le p^*$. Điểm cực tiểu tương ứng là $x(0) = 2$ (điểm này vi phạm ràng buộc $x \le 1$).
- Khi chọn $\lambda = 1$: Ta có $g(1) = 1 - 0.25 = 0.75 \le p^*$.
- Khi chọn $\lambda = 4$: Ta có $g(4) = 4 - 4 = 0 \le p^*$.

Rõ ràng, mục tiêu của ta là tìm cận dưới lớn nhất và chặt chẽ nhất. Điều này dẫn trực tiếp tới **Bài toán đối ngẫu Lagrange**:

$$
\max_{\lambda \ge 0} \quad g(\lambda) = \lambda - \frac{\lambda^2}{4}.
$$

Giải bài toán tìm cực đại này: Lấy đạo hàm $g'(\lambda) = 1 - \lambda/2 = 0 \iff \lambda^* = 2 \ge 0$.

Giá trị tối ưu đối ngẫu đạt được là:

$$
d^* = g(\lambda^*) = 2 - \frac{2^2}{4} = 1.
$$

Đối chiếu lại với bài toán gốc: Nghiệm tối ưu khả thi là $x^* = 1$, cho giá trị mục tiêu $f_0(x^*) = (1 - 2)^2 = 1$.

Như vậy, $p^* = d^* = 1$. Khoảng cách đối ngẫu bằng 0, và cận dưới đối ngẫu đã chạm đúng giá trị tối ưu gốc.

---

## 3. Tính lõm tự nhiên của hàm đối ngẫu

Một tính chất đẹp đẽ và sâu sắc của lý thuyết đối ngẫu là: **Hàm đối ngẫu $g(\lambda, \nu)$ luôn là một hàm lõm (concave), bất kể bài toán gốc có lồi hay không**.

Bản chất của điều này xuất phát từ cấu trúc của Lagrangian: Với mỗi điểm $x$ cố định, ánh xạ

$$
(\lambda,\nu)\mapsto L(x,\lambda,\nu)
$$

là một hàm affine theo cặp biến $(\lambda, \nu)$. 

Hàm đối ngẫu $g(\lambda, \nu) = \inf_{x \in \mathcal{D}} L(x, \lambda, \nu)$ chính là cận dưới đúng (infimum) của một họ các hàm affine. Vì mỗi hàm affine đều vừa lồi vừa lõm, infimum của một họ tùy ý các hàm affine luôn tạo thành một **hàm lõm**.

Ta kiểm chứng điều này bằng định nghĩa hàm lõm. Với hai bộ nhân tử $u$, $v$ và $\theta\in[0,1]$, đặt $w=\theta u+(1-\theta)v$. Tại mỗi $x$, viết gọn $A_x=L(x,u)$ và $B_x=L(x,v)$. Tính affine cho:

$$
\begin{aligned}
L(x,w)&=\theta A_x+(1-\theta)B_x\\
&\ge\theta g(u)+(1-\theta)g(v).
\end{aligned}
$$

Bước bất đẳng thức dùng $A_x\ge g(u)$, $B_x\ge g(v)$ và các trọng số không âm. Lấy infimum theo $x$ ở vế trái được:

$$
g(w)\ge\theta g(u)+(1-\theta)g(v).
$$

Đây chính là tính lõm của $g$. Hệ quả thực tiễn quan trọng:

> Bài toán đối ngẫu Lagrange:
> $$
> \max_{\lambda \succeq 0, \, \nu} g(\lambda, \nu) \quad \Longleftrightarrow \quad \min_{\lambda \succeq 0, \, \nu} -g(\lambda, \nu)
> $$
> **luôn luôn là một bài toán tối ưu lồi**, ngay cả khi bài toán gốc là một bài toán phi lồi phức tạp thuộc lớp NP-khó.

::: info Tại sao bài toán đối ngẫu luôn tìm cực đại của g mà không phải cực tiểu?
Mỗi giá trị $g(\lambda, \nu)$ là một cận dưới của giá trị tối ưu gốc $p^*$ ($g \le p^*$). Cận dưới càng lớn thì càng áp sát giá trị thực tế $p^*$, tức là thông tin đánh giá nghiệm càng chuẩn xác. Cực tiểu hóa một cận dưới sẽ đẩy giá trị về $-\infty$, hoàn toàn không mang lại giá trị chứng nhận nào.
:::

---

## 4. Hàm liên hợp Fenchel và Bất đẳng thức Fenchel–Young

Để hiểu sâu cơ chế tính toán hàm đối ngẫu trên các bài toán nhiều chiều phức tạp, ta cần công cụ biến đổi hàm số mạnh mẽ bậc nhất của giải tích lồi: **Hàm liên hợp (Conjugate function)**, hay còn gọi là biến đổi Legendre–Fenchel.

### 4.1. Định nghĩa và Diễn giải hình học
Cho hàm số $f: \mathbb{R}^n \to \mathbb{R}$. Hàm liên hợp $f^*: \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ được định nghĩa là:

$$
f^*(y) = \sup_{x \in \operatorname{dom} f} \left( y^T x - f(x) \right).
$$

Miền xác định của hàm liên hợp $\operatorname{dom} f^*$ bao gồm tất cả các vector $y$ sao cho supremum trên là hữu hạn (tức hàm tuyến tính $y^T x - f(x)$ bị chặn trên).

Về mặt hình học trong không gian một chiều: Biểu thức $y x - f(x)$ đo lường khoảng cách theo phương thẳng đứng giữa đường thẳng $g(x) = y x$ và đồ thị hàm số $f(x)$. Điểm $x$ đạt supremum chính là điểm mà tiếp tuyến của đồ thị $f(x)$ có hệ số góc đúng bằng $y$. Tung độ gốc của tiếp tuyến này chính là $-f^*(y)$.

Một đặc tính quan trọng: Vì $f^*(y)$ là supremum của một họ các hàm affine theo biến $y$ ($y \mapsto x^T y - f(x)$), nên **hàm liên hợp $f^*$ luôn là hàm lồi**, bất kể hàm số ban đầu $f$ có lồi hay không.

### 4.2. Bất đẳng thức Fenchel–Young
Từ định nghĩa supremum, với mọi $x \in \operatorname{dom} f$ và mọi $y \in \operatorname{dom} f^*$, ta có bất đẳng thức:

$$
f^*(y)\ge y^Tx-f(x).
$$

Chuyển vế và dùng $y^Tx=x^Ty$:

$$
x^Ty\le f(x)+f^*(y).
$$

Đây chính là **Bất đẳng thức Fenchel–Young**. Đẳng thức xảy ra khi và chỉ khi $y$ thuộc dưới vi phân của $f$ tại $x$: $y \in \partial f(x)$ (nếu $f$ khả vi thì $y = \nabla f(x)$).

### 4.3. Các ví dụ tính toán hàm liên hợp kinh điển

1. **Hàm toàn phương lồi**: Xét $f(x) = \frac{1}{2} x^T P x$ với ma trận đối xứng xác định dương $P \succ 0$.
   Lấy đạo hàm của $y^T x - \frac{1}{2} x^T P x$ theo $x$:
   $$
   y-Px=0\implies x=P^{-1}y.
   $$
   Đặt $z=P^{-1}y$, nên $Pz=y$. Thay vào định nghĩa:
   $$
   \begin{aligned}
   f^*(y)&=y^Tz-\frac12z^TPz\\
   &=\frac12y^Tz=\frac12y^TP^{-1}y.
   \end{aligned}
   $$

2. **Hàm chuẩn Euclid bình phương**: Xét $f(x) = \frac{1}{2} \|x\|_2^2$.
   Theo kết quả trên với $P = I$:
   $$
   f^*(y) = \frac{1}{2} \|y\|_2^2.
   $$

3. **Hàm entropy âm**: Xét $f(x) = \sum_{i=1}^n x_i \log x_i$ trên tập $\operatorname{dom} f = \mathbb{R}_{++}^n$.
   Biểu thức cần tối đa: $\sum_{i=1}^n (y_i x_i - x_i \log x_i)$. Vì các biến độc lập, ta đạo hàm theo từng $x_i$:
   $$
   y_i - \log x_i - 1 = 0 \implies x_i = e^{y_i - 1}.
   $$
   Thay vào:
   $$
   \begin{aligned}
   f^*(y)&=\sum_{i=1}^ne^{y_i-1}[y_i-(y_i-1)]\\
   &= \sum_{i=1}^n e^{y_i - 1} = \frac{1}{e} \sum_{i=1}^n e^{y_i}.
   \end{aligned}
   $$

4. **Hàm Log-Sum-Exp**: Xét $f(x) = \log\left(\sum_{i=1}^n e^{x_i}\right)$.
   Gọi $\Delta_n$ là tập các vector xác suất $y\succeq0$ có tổng các thành phần bằng 1:
   $$
   \sum_{i=1}^ny_i=y_1+\dots+y_n=1.
   $$
   Hàm liên hợp liên quan đến entropy của phân phối xác suất. Với quy ước $0\log0=0$:
   $$
   f^*(y)=\begin{cases}
   \sum_{i=1}^ny_i\log y_i,&y\in\Delta_n,\\
   +\infty,&y\notin\Delta_n.
   \end{cases}
   $$

### 4.4. Mối liên hệ mật thiết giữa Hàm liên hợp và Đối ngẫu Lagrange
Xét bài toán tối ưu với ràng buộc tuyến tính:

$$
\begin{aligned}
&\min_x f_0(x)\\
&Ax\le b,\quad Cx=d.
\end{aligned}
$$

Với $\lambda\succeq0$ và $\nu\in\mathbb R^p$, đặt:

$$
\begin{aligned}
q&=-A^T\lambda-C^T\nu,\\
c&=b^T\lambda+d^T\nu.
\end{aligned}
$$

Khi khai triển các tích và gom những số hạng chứa $x$, hàm Lagrangian trở thành:

$$
L(x,\lambda,\nu)=f_0(x)-q^Tx-c.
$$

Lấy infimum theo $x$, trong đó $q$ và $c$ được giữ cố định:

$$
\begin{aligned}
g(\lambda,\nu)+c&=\inf_x[f_0(x)-q^Tx]\\
&=-\sup_x[q^Tx-f_0(x)]\\
&=-f_0^*(q).
\end{aligned}
$$

Công thức trên cho thấy: Việc tính hàm đối ngẫu Lagrange của bất kỳ bài toán có ràng buộc tuyến tính nào thực chất quy về việc tìm **hàm liên hợp $f_0^*$ của hàm mục tiêu**. Đây là một cầu nối đại số mẫu mực giữa giải tích lồi và đối ngẫu.

---

## 5. Hàm Log-lồi, Log-lõm và Tính lồi theo Nón

### 5.1. Hàm Log-lồi và Log-lõm
Một hàm số $f: \mathbb{R}^n \to \mathbb{R}_{++}$ nhận giá trị dương được gọi là **log-lồi (log-convex)** nếu hàm số $\log f(x)$ là hàm lồi. Tương tự, $f$ được gọi là **log-lõm (log-concave)** nếu $\log f(x)$ là hàm lõm.

Điều kiện tương đương qua vi phân bậc hai: Tại điểm $x$, viết gọn $a=f(x)>0$, $v=\nabla f(x)$ và $H=\nabla^2f(x)$. Nếu $f$ khả vi hai lần, Hessian của $\log f$ là:

$$
\nabla^2\log f(x)=\frac Ha-\frac{vv^T}{a^2}.
$$

Do đó:
- Hàm $f$ log-lồi khi và chỉ khi: $f(x) \nabla^2 f(x) \succeq \nabla f(x) \nabla f(x)^T$.
- Hàm $f$ log-lõm khi và chỉ khi: $f(x) \nabla^2 f(x) \preceq \nabla f(x) \nabla f(x)^T$.

Một số tính chất và ứng dụng quan trọng trong học máy:
1. **Phân phối chuẩn nhiều chiều**: Với $\Sigma\succ0$, đặt $z=x-\mu$ và hằng số chuẩn hóa:
   $$
   C=\frac1{(2\pi)^{n/2}|\Sigma|^{1/2}}.
   $$
   Hàm mật độ xác suất Gauss là:
   $$
   p(x)=C\exp\left(-\frac12z^T\Sigma^{-1}z\right).
   $$
   có logarit là một hàm toàn phương lõm, do đó hàm mật độ chuẩn là **log-lõm**.
2. **Hàm tích chập bảo toàn tính log-lõm**: Định lý Prékopa–Leindler khẳng định rằng tích chập của hai hàm log-lõm tiếp tục là một hàm log-lõm. Tính chất này bảo đảm tính đơn đỉnh của nhiều phân phối xác suất hợp thành trong thống kê.
3. **Phân phối Logistic và hàm Sigmoid**: Hàm phân phối tích lũy logistic $F(x) = \frac{1}{1 + e^{-x}}$ là log-lõm, bảo đảm tính lồi của bài toán hồi quy logistic trong học máy.

### 5.2. Tính lồi theo Bất đẳng thức tổng quát (Nón lồi)
Cho $K \subseteq \mathbb{R}^m$ là một nón lồi chính quy (proper cone). Ta định nghĩa thứ tự riêng phần theo nón: $x \preceq_K y \iff y - x \in K$.

Một hàm vector $f: \mathbb{R}^n \to \mathbb{R}^m$ được gọi là **lồi theo nón $K$ (K-convex)** nếu với mọi $x, y \in \operatorname{dom} f$ và $\theta \in [0, 1]$, đặt $z=\theta x+(1-\theta)y$ thì:

$$
f(z)\preceq_K\theta f(x)+(1-\theta)f(y).
$$

Tính chất này cho phép mở rộng lý thuyết đối ngẫu từ các ràng buộc bất đẳng thức từng tọa độ sang các ràng buộc ma trận bán xác định dương (SDP) với nón $\mathbb{S}_+^n$ hoặc nón Lorentz bậc hai (SOCP).

---

## 6. Diễn giải hình học của Đối ngẫu Lagrange

Để hiểu cội nguồn bản chất của đối ngẫu mạnh và điều kiện Slater, ta xét cách hình học hóa bài toán tối ưu trong không gian các giá trị ràng buộc và mục tiêu.

### 6.1. Tập giá trị đạt được $\mathcal{G}$ và Tập trên $\mathcal{A}$
Xét bài toán có một ràng buộc bất đẳng thức duy nhất, cực tiểu hóa $f_0(x)$ thỏa mãn $f_1(x) \le 0$. Ta định nghĩa tập giá trị đạt được $\mathcal{G} \subset \mathbb{R} \times \mathbb{R}$ như sau:

$$
\mathcal{G} = \{ (f_1(x), f_0(x)) \in \mathbb{R}^2 \mid x \in \mathcal{D} \}.
$$

Trong mặt phẳng tọa độ $(u, t)$ với $u = f_1(x)$ và $t = f_0(x)$:
- Miền khả thi gốc ứng với nửa mặt phẳng bên trái $u \le 0$.
- Giá trị tối ưu gốc $p^*$ là tung độ nhỏ nhất của các điểm thuộc $\mathcal{G}$ nằm trên nửa mặt phẳng trái:
  $$
  p^* = \inf \{ t \mid (u, t) \in \mathcal{G}, \, u \le 0 \}.
  $$

Ta mở rộng $\mathcal{G}$ thành tập trên $\mathcal{A} = \mathcal{G} + (\mathbb{R}_+ \times \mathbb{R}_+)$. Một cặp $(u,t)$ thuộc $\mathcal A$ khi tồn tại $x\in\mathcal D$ thỏa mãn đồng thời:

$$
f_1(x)\le u,\qquad f_0(x)\le t.
$$

Nếu bài toán gốc là bài toán lồi, thì tập $\mathcal{A}$ luôn là một **tập lồi** trong $\mathbb{R}^2$.

### 6.2. Siêu phẳng tựa và Giá trị hàm đối ngẫu
Xét đường thẳng đi qua điểm $(u, t)$ có vector pháp tuyến $(\lambda, 1)$ với $\lambda \ge 0$:

$$
\lambda u + t = \alpha.
$$

Hàm Lagrangian được viết lại thành:

$$
L(x, \lambda) = f_0(x) + \lambda f_1(x) = t + \lambda u.
$$

Cận dưới đúng của đại lượng này trên $\mathcal{G}$ chính là giá trị của hàm đối ngẫu:

$$
\begin{aligned}
g(\lambda)&=\inf_{(u,t)\in\mathcal G}(\lambda u+t)\\
&=\inf_{(u,t)\in\mathcal A}(\lambda u+t).
\end{aligned}
$$

Về mặt hình học, phương trình $\lambda u + t = g(\lambda)$ định nghĩa một **đường thẳng tựa (supporting line)** đỡ tập $\mathcal{A}$ từ phía dưới. Điểm giao của đường thẳng tựa này với trục tung ($u = 0$) có tọa độ $(0, g(\lambda))$.

Vì đường thẳng này nằm hoàn toàn dưới tập $\mathcal{A}$, giao điểm của nó với trục tung $(0, g(\lambda))$ bắt buộc phải nằm dưới điểm tối ưu $(0, p^*)$. Điều này trực quan hóa bất đẳng thức đối ngẫu yếu:

$$
g(\lambda) \le p^*.
$$

Việc giải bài toán đối ngẫu $\max_{\lambda \ge 0} g(\lambda)$ tương đương với việc xoay hệ số góc của đường thẳng tựa (thay đổi $\lambda \ge 0$) sao cho giao điểm trên trục tung được đẩy lên cao nhất có thể!

```
         t (f_0)
         ^
         |         Tập trên A (Lồi)
         |        /----------------/
         |       /                /
     p* -+----->* (0, p*)        /
         |       \              /
         |        \------------/
   g(λ*) +-------/ (Đường thẳng tựa đỡ A tại biên)
         |      /  Vector pháp tuyến (λ*, 1)
         |     /
         +----+------------------------> u (f_1)
             0
```

### 6.3. Trực giác hình học của Điều kiện Slater và Đối ngẫu mạnh
Khi nào thì đường thẳng tựa có thể chạm tới đúng điểm $(0, p^*)$, tức $d^* = g(\lambda^*) = p^*$?
- Điểm $(0, p^*)$ nằm trên biên của tập lồi $\mathcal{A}$. Theo định lý siêu phẳng tựa, luôn tồn tại một siêu phẳng tựa đỡ $\mathcal{A}$ tại điểm biên này.
- Vector pháp tuyến của siêu phẳng tựa có dạng $(\lambda, \mu)$ với $(\lambda, \mu) \ge 0$ và không đồng thời bằng 0.
- Nếu $\mu > 0$, ta có thể chuẩn hóa $\mu = 1$, đưa về dạng $(\lambda, 1)$ và suy ra $p^* = d^*$.
- Trường hợp duy nhất làm đối ngẫu mạnh thất bại là khi siêu phẳng tựa bị **thẳng đứng** ($\mu = 0$). Khi đó, siêu phẳng tựa có dạng $\lambda u = 0$, nghĩa là tập $\mathcal{A}$ chỉ tiếp xúc với trục tung mà không có điểm nào nằm hẳn sang nửa mặt phẳng âm $u < 0$.
- **Điều kiện Slater** yêu cầu tồn tại một điểm $\bar x$ sao cho $f_1(\bar x) < 0$. Điểm này bảo đảm tập $\mathcal{A}$ có điểm nằm sâu bên trong nửa mặt phẳng trái ($u < 0$). Do đó, siêu phẳng tựa **tuyệt đối không thể thẳng đứng**! Từ đó suy ra $\mu > 0$, bảo đảm đối ngẫu mạnh $p^* = d^*$ xảy ra.

### 6.4. Khi nào xảy ra Khoảng cách đối ngẫu dương ($\Delta = p^* - d^* > 0$)?
Trong các bài toán phi lồi, tập $\mathcal{G}$ không lồi và có thể bị "lõm khuyết" ở biên dưới. Khi đó, đường thẳng tựa của bao lồi của $\mathcal{G}$ bị chặn lại ở đáy vết lõm, khiến giao điểm cao nhất với trục tung $d^*$ nằm thấp hơn đáng kể so với điểm tối ưu thực tế $p^*$. Khoảng chênh lệch $\Delta = p^* - d^* > 0$ chính là khoảng cách đối ngẫu.

---

## 7. Điều kiện Slater và Đối ngẫu mạnh (Strong Duality)

Khoảng cách đối ngẫu được định nghĩa là:

$$
\Delta = p^* - d^* \ge 0.
$$

Khi $\Delta = 0$, tức $p^* = d^*$, bài toán thỏa mãn **Đối ngẫu mạnh (Strong Duality)**. Cận dưới đối ngẫu đạt tới độ chính xác tuyệt đối, phản ánh đúng giá trị mục tiêu tối ưu gốc.

> **Định lý Slater**: Xét bài toán tối ưu lồi dạng chuẩn (hàm mục tiêu $f_0$ và các ràng buộc bất đẳng thức $f_i$ đều lồi, ràng buộc đẳng thức là affine $Ax = b$). Nếu tồn tại một điểm $\bar x$ thuộc phần trong tương đối của miền xác định ($\bar x \in \operatorname{relint}\mathcal{D}$) thỏa mãn chặt các bất đẳng thức:
> $$
> \begin{aligned}
> &f_i(\bar x)<0,\quad i=1,\dots,m,\\
> &A\bar x=b,
> \end{aligned}
> $$
> thì bài toán đạt đối ngẫu mạnh ($p^* = d^*$). Hơn nữa, nếu giá trị tối ưu $p^*$ hữu hạn, tồn tại bộ nhân tử $(\lambda^*,\nu^*)$ đạt giá trị tối ưu đối ngẫu.

Một điểm $\bar x$ thỏa mãn $f_i(\bar x) < 0$ được gọi là một **điểm khả thi ngặt (strictly feasible point)**.

**Trường hợp nới lỏng cho ràng buộc affine**: Nếu có $k$ ràng buộc đầu tiên $f_1, \dots, f_k$ là các hàm affine ($f_i(x) = a_i^T x - b_i$), ta không cần đòi hỏi bất đẳng thức ngặt $f_i(\bar x) < 0$ cho các ràng buộc này mà chỉ cần $f_i(\bar x) \le 0$. Đặc biệt, nếu toàn bộ các ràng buộc đều là affine (như trong Quy hoạch tuyến tính - LP), điều kiện Slater quy về yêu cầu bài toán có miền khả thi khác rỗng. Khi một bài toán LP khả thi và bị chặn, đối ngẫu mạnh luôn được bảo đảm.

---

## 8. Điểm yên ngựa và Lý thuyết trò chơi Minimax

Lý thuyết đối ngẫu Lagrange có mối giao thoa sâu sắc với lý thuyết trò chơi của John von Neumann thông qua khái niệm **Điểm yên ngựa (Saddle-point)**.

### 8.1. Lagrangian dưới góc nhìn Trò chơi hai người
Giả sử bài toán gốc không có ràng buộc đẳng thức để đơn giản hóa ký hiệu. Xét hàm mục tiêu cực đại hóa vô hạn:

$$
\sup_{\lambda\succeq0}L(x,\lambda).
$$

Ở đây $L(x,\lambda)=f_0(x)+F_\lambda(x)$, với $F_\lambda$ là tổng có trọng số đã định nghĩa ở mục 1. Hãy quan sát:
- Nếu $x$ vi phạm ràng buộc, tức tồn tại một chỉ số $k$ sao cho $f_k(x) > 0$: Ta có thể cho $\lambda_k \to +\infty$ để đẩy giá trị biểu thức lên $+\infty$.
- Nếu $x$ khả thi, tức $f_i(x) \le 0$ với mọi $i$: Số hạng $\sum \lambda_i f_i(x)$ luôn $\le 0$. Giá trị lớn nhất đạt được khi ta chọn $\lambda_i = 0$ cho các ràng buộc không chặt, khi đó tổng bằng 0 và giá trị cực đại đúng bằng $f_0(x)$.

Do đó, ta có biểu diễn hàm mục tiêu gốc:

$$
\sup_{\lambda \succeq 0} L(x, \lambda) = \begin{cases} f_0(x), & x \text{ feasible}, \\ +\infty, & x \text{ infeasible}. \end{cases}
$$

Bài toán tối ưu gốc tương đương với bài toán Min-Max:

$$
p^* = \inf_x \sup_{\lambda \succeq 0} L(x, \lambda).
$$

Trong khi đó, theo định nghĩa, bài toán đối ngẫu Lagrange chính là bài toán Max-Min:

$$
d^* = \sup_{\lambda \succeq 0} \inf_x L(x, \lambda).
$$

Bất đẳng thức đối ngẫu yếu $d^* \le p^*$ chính là biểu hiện cụ thể của **Bất đẳng thức Max-Min tổng quát**:

$$
\sup_{\lambda \succeq 0} \inf_x L(x, \lambda) \le \inf_x \sup_{\lambda \succeq 0} L(x, \lambda).
$$

### 8.2. Điểm yên ngựa của Lagrangian
Một cặp điểm $(x^*, \lambda^*)$ với $\lambda^* \succeq 0$ được gọi là một **điểm yên ngựa** của hàm Lagrangian $L$ nếu với mọi $x$ và mọi $\lambda \succeq 0$:

$$
L(x^*, \lambda) \le L(x^*, \lambda^*) \le L(x, \lambda^*).
$$

Nói cách khác:
- $x^*$ là cực tiểu toàn cục của hàm $x \mapsto L(x, \lambda^*)$.
- $\lambda^*$ là cực đại toàn cục của hàm $\lambda \mapsto L(x^*, \lambda)$ trên miền $\lambda \succeq 0$.

> **Định lý Điểm yên ngựa**: Cặp điểm $(x^*, \lambda^*)$ là một điểm yên ngựa của hàm Lagrangian khi và chỉ khi $x^*$ là nghiệm tối ưu gốc, $\lambda^*$ là nghiệm tối ưu đối ngẫu, và bài toán thỏa mãn đối ngẫu mạnh ($p^* = d^*$).

### 8.3. Ứng dụng trong Trí tuệ Nhân tạo: Huấn luyện Đối kháng và GANs
Trong học sâu, cấu trúc Min-Max này là nền tảng của mô hình Mạng đối sinh (Generative Adversarial Networks - GANs). Mạng sinh $G$ cố gắng cực tiểu hóa sai số nhận diện, trong khi mạng phân biệt $D$ cố gắng cực đại hóa độ chính xác phát hiện:

$$
\min_G \max_D V(D, G).
$$

Hội tụ của quá trình huấn luyện GAN tương ứng với việc tìm ra một điểm yên ngựa Nash của trò chơi hai người có tổng bằng không. Tương tự, trong Học tăng cường bền vững (Robust Reinforcement Learning) và Tối ưu hóa đối kháng (Adversarial Training), đối ngẫu minimax bảo đảm thuật toán hoạt động an toàn trước các nhiễu loạn độc hại tồi tệ nhất.

---

## 9. Bốn nhóm điều kiện Karush–Kuhn–Tucker (KKT)

Giả sử các hàm mục tiêu và ràng buộc đều khả vi. Hệ điều kiện **Karush–Kuhn–Tucker (KKT)** là cầu nối đại số hoàn chỉnh liên kết nghiệm gốc $x^*$ và nghiệm đối ngẫu $(\lambda^*, \nu^*)$:

| Nhóm điều kiện | Biểu thức toán học | Ý nghĩa hình học & Bản chất |
| :--- | :--- | :--- |
| **1. Khả thi gốc** (Primal Feasibility) | $f_i(x^*) \le 0, \; i=1,\dots,m$<br>$h_j(x^*) = 0, \; j=1,\dots,p$ | Điểm $x^*$ phải là một phương án hợp lệ, nằm trọn vẹn trong miền ràng buộc. |
| **2. Khả thi đối ngẫu** (Dual Feasibility) | $\lambda_i^* \ge 0, \; i=1,\dots,m$ | Nhân tử không âm, bảo đảm hình phạt cho hành vi vi phạm luôn cùng chiều tăng chi phí. |
| **3. Bù trừ** (Complementary Slackness) | $\lambda_i^* f_i(x^*) = 0, \; i=1,\dots,m$ | Hoặc ràng buộc không chặt ($f_i < 0 \implies \lambda_i^* = 0$), hoặc ràng buộc chặt ($f_i = 0$). |
| **4. Triệt tiêu gradient** (Stationarity) | $\nabla_x L(x^*, \lambda^*, \nu^*) = 0$<br>($\nabla f_0 + \sum \lambda_i^* \nabla f_i + \sum \nu_j^* \nabla h_j = 0$) | Gradient hàm mục tiêu cân bằng hoàn hảo với lực cản pháp tuyến từ các mặt ràng buộc. |

### 9.1. Ý nghĩa bản chất của Điều kiện bù trừ (Complementary Slackness)
Đẳng thức $\lambda_i^* f_i(x^*) = 0$ là trái tim của giải tích tối ưu có ràng buộc. Do $\lambda_i^* \ge 0$ và $f_i(x^*) \le 0$, tích của chúng bằng 0 dẫn tới hai kịch bản loại trừ lẫn nhau:
1. **Ràng buộc không hoạt động (Inactive/Slack)**: Nếu $f_i(x^*) < 0$ (nghiệm nằm an toàn sâu bên trong miền khả thi), bắt buộc $\lambda_i^* = 0$. Ràng buộc này hoàn toàn không cản trở mục tiêu tối ưu, việc nới lỏng nó không làm thay đổi nghiệm.
2. **Ràng buộc hoạt động (Active/Tight)**: Nếu $\lambda_i^* > 0$ (nhân tử dương ngặt), bắt buộc $f_i(x^*) = 0$. Nghiệm tối ưu đang bị ép sát vào mặt biên giới hạn bởi ràng buộc này.

> **Minh họa trong Học máy (Support Vector Machines - SVM)**:
> Trong bài toán phân lớp SVM, điều kiện bù trừ giải thích trọn vẹn tại sao siêu phẳng phân chia chỉ phụ thuộc vào một số ít điểm dữ liệu nằm sát lề (các Support Vectors có $\lambda_i^* > 0$). Hàng triệu điểm dữ liệu nằm đúng phía phân loại cách xa lề đều có $\lambda_i^* = 0$ và bị triệt tiêu hoàn toàn khỏi mô hình dự đoán.

### 9.2. Vai trò của KKT: Bài toán lồi so với Phi lồi
- **Với bài toán lồi khả vi thỏa điều kiện Slater**: Hệ KKT là **điều kiện cần và đủ** cho tối ưu toàn cục. Bất kỳ bộ điểm $(x^*, \lambda^*, \nu^*)$ nào thỏa mãn bốn nhóm KKT đều bảo đảm $x^*$ là nghiệm tối ưu toàn cục.
- **Với bài toán phi lồi**: KKT chỉ là **điều kiện cần** cho điểm dừng cục bộ. Một điểm thỏa mãn KKT có thể là cực tiểu cục bộ, cực đại cục bộ, hoặc một điểm yên ngựa.

---

## 10. Quy hoạch toàn phương (QP) và Hệ phương trình Newton–KKT

Xét bài toán Quy hoạch toàn phương với ràng buộc đẳng thức affine:

$$
\begin{aligned}
&\min_{x\in\mathbb R^n}f_0(x),\\
&Ax=b,
\end{aligned}
$$

với $f_0(x)=\frac12x^TPx+q^Tx$. Ma trận $P \in \mathbb{S}_+^n$ bán xác định dương và $A \in \mathbb{R}^{p \times n}$ có các hàng độc lập tuyến tính.

Hàm Lagrangian với vector nhân tử $\nu \in \mathbb{R}^p$:

$$
L(x,\nu)=f_0(x)+\nu^T(Ax-b).
$$

Áp dụng hệ điều kiện KKT:
1. Khả thi gốc: $A x^* = b$.
2. Triệt tiêu gradient:
   $$
   Px^*+q+A^T\nu^*=0.
   $$
   Chuyển $q$ sang vế phải được $Px^*+A^T\nu^*=-q$.

Ghép hai điều kiện này lại thành một hệ phương trình tuyến tính khối duy nhất:

$$
\begin{bmatrix} P & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x^* \\ \nu^* \end{bmatrix} = \begin{bmatrix} -q \\ b \end{bmatrix}.
$$

Ma trận khối ở vế trái được gọi là **Ma trận KKT**. Đây là một ma trận đối xứng không xác định (symmetric indefinite matrix). Trong Bài 04, ta sẽ thấy hệ phương trình Newton-KKT này chính là bước lặp cốt lõi để giải các bài toán tối ưu phi tuyến có ràng buộc đẳng thức bằng phương pháp Newton.

---

## 11. Độ nhạy nhân tử và Giá bóng kinh tế học (Shadow Price)

Xét bài toán tối ưu bị nhiễu bởi vector thông số tài nguyên $u \in \mathbb{R}^m$ và $v \in \mathbb{R}^p$:

$$
\begin{aligned}
&p^*(u, v) = \min_{x} \quad f_0(x)\\
&f_i(x)\le u_i,\quad i=1,\dots,m,\\
&h_j(x)=v_j,\quad j=1,\dots,p.
\end{aligned}
$$

Giả sử bài toán lồi thỏa mãn điều kiện Slater và hàm giá trị tối ưu $p^*(u, v)$ khả vi tại gốc $(0, 0)$. Định lý độ nhạy khẳng định mối liên hệ trực tiếp:

$$
\begin{aligned}
\lambda_i^*&=-\partial_{u_i}p^*(0,0),\\
\nu_j^*&=-\partial_{v_j}p^*(0,0).
\end{aligned}
$$

Ký hiệu $\partial_{u_i}$ và $\partial_{v_j}$ chỉ đạo hàm riêng theo từng thành phần tương ứng.

Ý nghĩa kinh tế học: Nhân tử Lagrange $\lambda_i^*$ đo lường tốc độ suy giảm của chi phí tối ưu khi ta nới lỏng thêm một đơn vị tài nguyên ở ràng buộc thứ $i$ ($u_i$ tăng từ 0 lên $\epsilon$). Nếu $\lambda_i^* = 50$, điều đó có nghĩa là nếu doanh nghiệp bỏ tiền mua thêm 1 đơn vị tài nguyên $i$, chi phí vận hành tối ưu sẽ giảm xấp xỉ 50 đơn vị tiền tệ. Đây chính là khái niệm **giá bóng** (shadow price) trong kinh tế học quản trị và quy hoạch sản xuất.

---

## 12. Định lý về các Phương án thay thế và Bổ đề Farkas

Lý thuyết đối ngẫu không chỉ giải các bài toán tối ưu hóa mà còn trả lời câu hỏi nhị phân: Một hệ phương trình hoặc bất đẳng thức có nghiệm hay không? Công cụ giải quyết vấn đề này là các **Định lý về các phương án thay thế (Theorems of Alternatives)**, mở đầu bằng **Bổ đề Farkas**.

### 12.1. Khái niệm Chứng chỉ vô nghiệm (Certificates of Infeasibility)
Để chứng minh một hệ bất đẳng thức có nghiệm, ta chỉ cần chỉ ra một nghiệm cụ thể $\bar x$. Nhưng làm thế nào để chứng minh một hệ bất đẳng thức **hoàn toàn vô nghiệm**? Ta cần tìm một vector đối ngẫu đóng vai trò là một "chứng chỉ toán học" xác nhận sự mâu thuẫn nội tại của hệ.

### 12.2. Bổ đề Farkas (Farkas' Lemma)
Cho ma trận $A \in \mathbb{R}^{m \times n}$ và vector $b \in \mathbb{R}^m$. Xét hai hệ phương trình:
- **Hệ 1**: Tồn tại $x \in \mathbb{R}^n$ sao cho $A x \le b$.
- **Hệ 2**: Tồn tại $\lambda \in \mathbb{R}^m$ sao cho $\lambda \succeq 0$, $A^T \lambda = 0$ và $b^T \lambda < 0$.

> **Định lý Farkas**: Đúng một và chỉ một trong hai hệ trên có nghiệm. Không bao giờ xảy ra trường hợp cả hai hệ cùng có nghiệm, hoặc cả hai hệ cùng vô nghiệm.

**Chứng minh tính loại trừ (Không thể cùng có nghiệm)**:
Giả sử phản chứng cả hai hệ đều có nghiệm $x$ và $\lambda$. Nhân vô hướng vector $\lambda \succeq 0$ với bất đẳng thức $A x \le b$:

$$
\lambda^T (A x) \le \lambda^T b = b^T \lambda.
$$

Biến đổi vế trái: $\lambda^T (A x) = (A^T \lambda)^T x = 0^T x = 0$.
Do đó: $0 \le b^T \lambda$. Điều này mâu thuẫn trực tiếp với điều kiện $b^T \lambda < 0$ của Hệ 2. Sự mâu thuẫn chứng minh hai hệ không thể đồng thời có nghiệm.

Vector $\lambda$ ở Hệ 2 chính là **chứng chỉ vô nghiệm** của Hệ 1: Nó tạo ra một tổ hợp tuyến tính không âm của các hàng ma trận $A$ triệt tiêu hoàn toàn thành vector 0, trong khi tổ hợp tương ứng của vế phải $b$ lại cho ra một số âm ngặt, tạo thành mệnh đề vô lý $0 \le \text{negative}$.

---

## 13. Tối ưu hai hàm Toàn phương và Bổ đề S-procedure (Phụ lục B)

Trong tối ưu hóa phi lồi, đối ngẫu mạnh thường hiếm khi xảy ra. Tuy nhiên, tồn tại một ngoại lệ toán học tuyệt đẹp và rất quan trọng trong kỹ thuật điều khiển tự động và học máy bền vững: **Bài toán tối ưu với đúng hai hàm toàn phương**.

### 13.1. Bài toán cực tiểu hóa với một ràng buộc toàn phương
Xét bài toán tối ưu với biến $x \in \mathbb{R}^n$:

$$
\begin{aligned}
&\min_{x\in\mathbb R^n}f_0(x),\\
&f_1(x)\le0,
\end{aligned}
$$

trong đó, với $k=0,1$:

$$
f_k(x)=x^TA_kx+2b_k^Tx+c_k.
$$

Các ma trận $A_0,A_1\in\mathbb S^n$ đối xứng thực tùy ý.
Điểm đáng chú ý ở đây là: Các ma trận $A_0, A_1$ **hoàn toàn không cần xác định dương**. Do đó, bài toán này nhìn chung là **phi lồi**: Hàm mục tiêu có thể có dạng yên ngựa, và miền ràng buộc có thể là phần ngoài của một hyperboloid.

Để viết gọn các hệ số của Lagrangian, đặt:
$$
\begin{aligned}
P_\lambda&=A_0+\lambda A_1,\\
q_\lambda&=b_0+\lambda b_1,\\
r_\lambda&=c_0+\lambda c_1.
\end{aligned}
$$

Khi đó:
$$
L(x,\lambda)=x^TP_\lambda x+2q_\lambda^Tx+r_\lambda.
$$

Hàm này bị chặn dưới theo $x$ khi và chỉ khi $P_\lambda\succeq0$ và $q_\lambda$ thuộc không gian ảnh của $P_\lambda$. Điều kiện thứ hai loại bỏ thành phần tuyến tính khác 0 trên không gian hạt nhân của ma trận.

Khi $P_\lambda\succ0$, điểm cực tiểu duy nhất là:
$$
x^*(\lambda)=-P_\lambda^{-1}q_\lambda.
$$
Thay nghiệm này vào, ta thu được hàm đối ngẫu Lagrange:
$$
g(\lambda)=r_\lambda-q_\lambda^TP_\lambda^{-1}q_\lambda.
$$

Sử dụng Bổ đề phần bù Schur, bài toán đối ngẫu Lagrange $\max_{\lambda \ge 0} g(\lambda)$ được viết tương đương dưới dạng một bài toán Quy hoạch nửa xác định (SDP):

$$
\begin{aligned}
&\max_{\lambda\ge0,\,\gamma\in\mathbb R}\gamma,\\
&\begin{bmatrix}P_\lambda&q_\lambda\\q_\lambda^T&r_\lambda-\gamma\end{bmatrix}\succeq0.
\end{aligned}
$$

### 13.2. Định lý Dines và Cội nguồn của Đối ngẫu mạnh Phi lồi
Một câu hỏi đặt ra: Vì sao bài toán phi lồi với một ràng buộc toàn phương vẫn đạt đối ngẫu mạnh khi có điểm Slater và giá trị tối ưu hữu hạn?

Một công cụ hình học để chứng minh kết quả này là định lý Dines cho hai dạng toàn phương **thuần nhất**. Với hai ma trận đối xứng $Q_0,Q_1$, đặt:

$$
\Phi(z)=(z^TQ_1z,\,z^TQ_0z).
$$

> **Định lý Dines**: Tập $\{\Phi(z)\mid z\in\mathbb R^N\}$ là một nón lồi trong $\mathbb R^2$.

Điều kiện thuần nhất có nghĩa là không có số hạng tuyến tính hoặc hằng số. Không được suy rộng phát biểu này thành tính lồi của tập ảnh của hai hàm toàn phương affine tùy ý.

Các số hạng affine có thể được đưa vào dạng thuần nhất bằng cách thêm một tọa độ. Kết hợp kỹ thuật này với định lý tách dẫn tới bổ đề S-procedure ở mục tiếp theo. Với điểm Slater ngặt và giá trị tối ưu hữu hạn, kết quả bảo đảm:
$$
p^*=d^*.
$$

### 13.3. Bổ đề S-procedure
Từ tính chất đối ngẫu mạnh của hai hàm toàn phương, ta thu được một công cụ giải tích có tầm ảnh hưởng sâu rộng trong lý thuyết điều khiển và học máy: **Bổ đề S-procedure**.

Xét bài toán kiểm tra xem một điều kiện ràng buộc toàn phương $F_1(x) \le 0$ có bảo đảm một tiêu chuẩn chất lượng toàn phương $F_0(x) \le 0$ hay không:

$$
F_1(x) \le 0 \implies F_0(x) \le 0.
$$

Giả sử tồn tại điểm $\bar{x}$ sao cho $F_1(\bar{x}) < 0$ (điều kiện Slater).
Mệnh đề kéo theo trên tương đương với việc bài toán tối ưu sau có giá trị tối ưu không âm:
$$
\min_{x} \quad -F_0(x) \quad \text{s.t.} \quad F_1(x) \le 0.
$$
Áp dụng đối ngẫu mạnh, giá trị tối ưu của bài toán trên lớn hơn hoặc bằng 0 khi và chỉ khi bài toán đối ngẫu của nó khả thi với giá trị không âm.

> **Định lý Bổ đề S-procedure**: Mệnh đề $F_1(x) \le 0 \implies F_0(x) \le 0$ nghiệm đúng với mọi $x \in \mathbb{R}^n$ khi và chỉ khi tồn tại một số thực không âm $\lambda \ge 0$ sao cho:
> $$
> F_0(x) \le \lambda F_1(x) \quad \forall x \in \mathbb{R}^n,
> $$
> điều này tương đương với bất đẳng thức ma trận nửa xác định:
> $$
> \begin{bmatrix} A_0 & b_0 \\ b_0^T & c_0 \end{bmatrix} \preceq \lambda \begin{bmatrix} A_1 & b_1 \\ b_1^T & c_1 \end{bmatrix}.
> $$

**Ý nghĩa phương pháp**: S-procedure chuyển điều kiện đúng trên mọi điểm $x\in\mathbb R^n$ thành một bất đẳng thức ma trận tuyến tính (LMI) theo biến vô hướng $\lambda\ge0$.

### 13.4. Bổ đề Finsler (Finsler's Lemma)
Một biến thể thuần nhất kinh điển của S-procedure là **Bổ đề Finsler**:
Cho hai ma trận đối xứng $A, B \in \mathbb{S}^n$. Xét dạng toàn phương thuần nhất:

$$
x^T B x = 0, \, x \ne 0 \implies x^T A x > 0.
$$

Bổ đề Finsler khẳng định rằng mệnh đề trên đúng khi và chỉ khi tồn tại một hệ số vô hướng $\mu \in \mathbb{R}$ sao cho:
$$
A + \mu B \succ 0.
$$
Kết quả này cho phép chuyển đổi bài toán kiểm tra độ cong dương trên một mặt siêu cong thành việc tìm một ma trận tổng dương xác định trong không gian đại số.

### 13.5. Ứng dụng trong Kiểm thử Độ bền bỉ của Mô hình AI (Robust AI Verification)
Trong học máy an toàn, ta cần bảo đảm rằng một mô hình mạng nơ-ron hoặc bộ phân loại không bị đánh lừa bởi các nhiễu đối kháng (adversarial perturbations).

Giả sử biên phân chia quyết định của mô hình trong không gian đặc trưng cục bộ được xấp xỉ bằng một hàm bậc hai $q(x) = x^T A x + 2 b^T x + c$. Vùng an toàn của hệ thống là $q(x) \le 0$.
Tập hợp các nhiễu vật lý hoặc sai số cảm biến được mô hình hóa bằng một ellipsoid bất định. Đặt $z=x-x_0$ và giả sử $P\succ0$:
$$
\mathcal E=\{x\in\mathbb R^n\mid z^TPz\le1\}.
$$
Để chứng minh hệ thống an toàn tuyệt đối trước mọi nhiễu trong $\mathcal{E}$, ta cần chứng minh:
$$
z^TPz\le1\implies q(x)\le0.
$$
Đặt $v=Px_0$ và $\delta=x_0^TPx_0-1$. Hai ma trận hệ số là:
$$
M=\begin{bmatrix}A&b\\b^T&c\end{bmatrix},\qquad
N=\begin{bmatrix}P&-v\\-v^T&\delta\end{bmatrix}.
$$
Áp dụng bổ đề S-procedure, ta chỉ cần tìm $\lambda\ge0$ sao cho:
$$
M\preceq\lambda N.
$$
Bằng cách giải bài toán LMI này, ta có được một chứng nhận an toàn toán học nghiêm ngặt cho mô hình AI mà không cần phải thực hiện bất kỳ phép đo thử nghiệm ngẫu nhiên nào.

---

## 14. Hệ thống Bài tập Tự luyện Chuyên sâu {#bai-tap-tu-luyen}

::: exercise 1. Tính toán hàm liên hợp của hàm Entropy và hàm Log-Sum-Exp
1. Cho hàm entropy âm một chiều $f(x) = x \log x$ với miền xác định $x > 0$. Hãy tính hàm liên hợp $f^*(y)$ và xác định miền xác định $\operatorname{dom} f^*$.
2. Cho hàm log-sum-exp hai chiều $f(x_1, x_2) = \log(e^{x_1} + e^{x_2})$. Hãy tìm $f^*(y_1, y_2)$.
:::
::: solution
**Lời giải**:
1. Với $f(x) = x \log x$ trên $x > 0$:
   $$
   f^*(y) = \sup_{x > 0} (x y - x \log x).
   $$
   Với $y$ cố định, đặt $\phi_y(x)=xy-x\log x$. Điều kiện đạo hàm theo $x$ là:
   $$
   \phi_y'(x)=y-\log x-1=0.
   $$
   Suy ra $x=e^{y-1}>0$.
   Đạo hàm bậc hai là $-1/x < 0$, do đó điểm cực trị là cực đại toàn cục duy nhất.
   Thay $x = e^{y-1}$ vào biểu thức:
   $$
   \begin{aligned}
   f^*(y)&=e^{y-1}[y-(y-1)]\\
   &=e^{y-1}.
   \end{aligned}
   $$
   Miền xác định là toàn bộ trục số thực: $\operatorname{dom} f^* = \mathbb{R}$.

2. Với $f(x_1, x_2) = \log(e^{x_1} + e^{x_2})$:
   Biểu thức $y_1 x_1 + y_2 x_2 - \log(e^{x_1} + e^{x_2})$.
   - Nếu $y_1 < 0$, ta cho $x_1 \to -\infty$ và giữ $x_2$ cố định, biểu thức sẽ tiến tới $+\infty$. Tương tự với $y_2 < 0$. Do đó bắt buộc $y_1 \ge 0, y_2 \ge 0$.
   - Khi chọn $x_1=x_2=t$, đặt $s=y_1+y_2$. Biểu thức trở thành hàm $h(t)$:
     $$
     \begin{aligned}
     h(t)&=st-\log(2e^t)\\
     &=(s-1)t-\log2.
     \end{aligned}
     $$
     Để biểu thức bị chặn trên khi $t \to \pm\infty$, ta bắt buộc phải có $y_1 + y_2 = 1$.
   - Khi $y_1 \ge 0, y_2 \ge 0$ và $y_1 + y_2 = 1$: Đặt $Z=e^{x_1}+e^{x_2}$ và $H(y)=y_1\log y_1+y_2\log y_2$. Bất đẳng thức log-sum cho:
     $$
     y_1x_1+y_2x_2-\log Z\le H(y).
     $$
   Với $y_1,y_2>0$, dấu bằng đạt được khi $x_i=\log y_i$. Ở biên, giá trị này được tiến tới bằng giới hạn. Vì vậy, với quy ước $0\log0=0$, trên đơn hình $\Delta_2$ ta có:
   $$
   f^*(y)=H(y).
   $$
   Ngoài $\Delta_2$, ta có $f^*(y)=+\infty$.
:::

::: exercise 2. Nới lỏng Đối ngẫu Lagrange cho Quy hoạch Số nguyên Boolean (Boolean LP)
Xét bài toán quy hoạch số nguyên nhị phân:
$$
\begin{aligned}
&\min_{x\in\mathbb R^n}c^Tx,\\
&Ax\preceq b,\\
&x_i\in\{0,1\},\quad i=1,\dots,n.
\end{aligned}
$$
1. Hãy viết lại ràng buộc $x_i \in \{0, 1\}$ dưới dạng đẳng thức toàn phương liên tục.
2. Thiết lập hàm Lagrangian và xây dựng bài toán đối ngẫu Lagrange.
3. Chứng minh rằng giá trị tối ưu đối ngẫu $d^*$ cung cấp một cận dưới cho bài toán quy hoạch số nguyên ban đầu.
:::
::: solution
**Lời giải**:
1. Điều kiện $x_i \in \{0, 1\}$ tương đương với phương trình bậc hai: $x_i(1 - x_i) = 0$, tức là $x_i - x_i^2 = 0$ với mọi $i = 1, \dots, n$.
   Bài toán trở thành:
   $$
   \begin{aligned}
   &\min_x c^Tx,\\
   &Ax-b\preceq0,\\
   &x_i-x_i^2=0,\quad i=1,\dots,n.
   \end{aligned}
   $$

2. Thiết lập hàm Lagrangian với nhân tử $\lambda \in \mathbb{R}^m$ ($\lambda \succeq 0$) và $\nu \in \mathbb{R}^n$. Gọi $a_i$ là cột thứ $i$ của $A$ và đặt $r_i=c_i+a_i^T\lambda+\nu_i$. Khi gom các số hạng theo từng biến:
   $$
   \begin{aligned}
   L(x,\lambda,\nu)&=-b^T\lambda+\sum_{i=1}^n\ell_i(x_i),\\
   \ell_i(x_i)&=-\nu_ix_i^2+r_ix_i.
   \end{aligned}
   $$

   Để $L(x, \lambda, \nu)$ bị chặn dưới theo $x$, hệ số của $x_i^2$ bắt buộc phải không âm, tức $-\nu_i \ge 0 \implies \nu_i \le 0$.
   - Nếu $\nu_i<0$: Đỉnh parabol đạt cực tiểu tại $x_i=r_i/(2\nu_i)$, với giá trị $r_i^2/(4\nu_i)$.
   - Nếu $\nu_i=0$: Hàm $\ell_i$ bị chặn dưới khi và chỉ khi $r_i=0$, khi đó giá trị cực tiểu bằng 0.
   - Nếu $\nu_i>0$, hoặc $\nu_i=0$ nhưng $r_i\ne0$: Ta có $g(\lambda,\nu)=-\infty$.

   Đặt $I_- = \{i\mid\nu_i<0\}$. Trên miền hữu hạn vừa nêu, hàm đối ngẫu là:
     $$
     g(\lambda,\nu)=-b^T\lambda+\sum_{i\in I_-}\frac{r_i^2}{4\nu_i}.
     $$

3. Bài toán đối ngẫu Lagrange:
   $$
   \begin{aligned}
   &\max_{\lambda,\nu}g(\lambda,\nu),\\
   &\lambda\succeq0,\quad\nu\preceq0,\\
   &r_i=0\quad\text{khi }\nu_i=0.
   \end{aligned}
   $$
   Theo định lý đối ngẫu yếu, với mọi cặp nhân tử khả thi $(\lambda, \nu)$, ta luôn có $g(\lambda, \nu) \le p^*$. Do đó, việc giải bài toán đối ngẫu lồi này cung cấp một cận dưới hữu hiệu cho bài toán quy hoạch số nguyên NP-khó gốc. Đây chính là kỹ thuật nới lỏng đối ngẫu Lagrange (Lagrangian Relaxation) được áp dụng phổ biến trong tối ưu tổ hợp.
:::

::: exercise 3. Điểm yên ngựa và Trò chơi Ma trận Hữu hạn
Xét trò chơi ma trận hai người có tổng bằng 0 với ma trận thưởng phạt $A \in \mathbb{R}^{m \times n}$. Người chơi 1 chọn phân phối xác suất $p \in \Delta_m = \{p \in \mathbb{R}_+^m \mid \sum p_i = 1\}$, người chơi 2 chọn phân phối xác suất $q \in \Delta_n = \{q \in \mathbb{R}_+^n \mid \sum q_j = 1\}$. Chi phí kỳ vọng là $p^T A q$.
1. Hãy phát biểu bài toán dưới dạng hai bài toán tối ưu Min-Max và Max-Min.
2. Sử dụng định lý đối ngẫu mạnh để chứng minh Định lý Minimax của von Neumann:
   $$
   \min_{p \in \Delta_m} \max_{q \in \Delta_n} p^T A q = \max_{q \in \Delta_n} \min_{p \in \Delta_m} p^T A q.
   $$
:::
::: solution
**Lời giải**:
1. Người chơi 1 muốn cực tiểu hóa chi phí khi người chơi 2 phản ứng tối ưu:
   $$
   \min_{p \in \Delta_m} \max_{q \in \Delta_n} p^T A q.
   $$
   Vì hàm $q \mapsto p^T A q$ là tuyến tính trên đơn hình $\Delta_n$, giá trị cực đại đạt được tại một trong các đỉnh của đơn hình (tức là tại một cột $j$ của $A$). Do đó:
   $$
   \max_{q \in \Delta_n} p^T A q = \max_{j = 1, \dots, n} (A^T p)_j.
   $$
   Bài toán trở thành bài toán quy hoạch tuyến tính:
   $$
   \begin{aligned}
   &\min_{p,t}t,\\
   &A^Tp\preceq t\mathbf1,\\
   &\mathbf1^Tp=1,\quad p\succeq0.
   \end{aligned}
   $$

2. Thiết lập bài toán đối ngẫu của bài toán LP trên:
   Đặt biến đối ngẫu $q \in \mathbb{R}^n$ ($q \succeq 0$) cho ràng buộc $A^T p - t \mathbf{1} \preceq 0$, và biến vô hướng $s \in \mathbb{R}$ cho ràng buộc $\mathbf{1}^T p = 1$.
   Đặt $u=A^Tp-t\mathbf1$ và $v=1-\mathbf1^Tp$. Lagrangian là:
   $$
   L=t+q^Tu+sv.
   $$
   Gom theo hai biến gốc $t,p$, đặt $a=1-\mathbf1^Tq$ và $b=Aq-s\mathbf1$, ta được:
   $$
   L=s+ta+p^Tb.
   $$
   Cận dưới theo $t$ hữu hạn khi và chỉ khi $\mathbf{1}^T q = 1$.
   Cận dưới theo $p \succeq 0$ hữu hạn khi và chỉ khi $A q - s \mathbf{1} \succeq 0 \iff A q \succeq s \mathbf{1}$.
   Bài toán đối ngẫu là:
   $$
   \begin{aligned}
   &\max_{q,s}s,\\
   &Aq\succeq s\mathbf1,\\
   &\mathbf1^Tq=1,\quad q\succeq0,
   \end{aligned}
   $$
   Gọi $V$ là giá trị tối ưu này. Với mỗi $q$, giá trị nhỏ nhất của $p^TAq$ trên $\Delta_m$ bằng thành phần nhỏ nhất của $Aq$. Vì vậy:
   $$
   \begin{aligned}
   V&=\max_{q\in\Delta_n}\min_{i=1,\dots,m}(Aq)_i\\
   &=\max_{q\in\Delta_n}\min_{p\in\Delta_m}p^TAq.
   \end{aligned}
   $$
   Các đơn hình xác suất đều khác rỗng và compact, nên chi phí kỳ vọng bị chặn và hai bài toán LP đều có giá trị tối ưu hữu hạn. Theo đối ngẫu mạnh của quy hoạch tuyến tính, hai giá trị này bằng nhau. Điều này chứng minh Định lý Minimax của von Neumann.
:::

::: exercise 4. Xác lập Chứng chỉ vô nghiệm bằng Bổ đề Farkas
Xét hệ bất đẳng thức tuyến tính:
$$
\begin{cases}
x_1 + 2 x_2 \le 1 \\
-x_1 + x_2 \le -2 \\
-x_2 \le -1
\end{cases}
$$
1. Hãy biểu diễn hệ trên dưới dạng ma trận $A x \le b$.
2. Sử dụng Bổ đề Farkas để tìm một vector nhân tử $\lambda \ge 0$ chứng minh hệ vô nghiệm.
:::
::: solution
**Lời giải**:
1. Đặt biến $x = (x_1, x_2)^T$. Hệ viết dưới dạng $A x \le b$ với:
   $$
   \begin{aligned}
   A&=\begin{bmatrix}1&2\\-1&1\\0&-1\end{bmatrix},\\
   b&=\begin{bmatrix}1\\-2\\-1\end{bmatrix}.
   \end{aligned}
   $$

2. Theo Bổ đề Farkas, để chứng minh hệ $A x \le b$ vô nghiệm, ta cần tìm vector $\lambda = (\lambda_1, \lambda_2, \lambda_3)^T \ge 0$ thỏa mãn:
   $$
   A^T \lambda = 0 , \quad b^T \lambda < 0.
   $$
   Khai triển hệ phương trình $A^T \lambda = 0$:
   $$
   \begin{aligned}
   &\lambda_1-\lambda_2=0,\\
   &2\lambda_1+\lambda_2-\lambda_3=0.
   \end{aligned}
   $$
   Phương trình đầu cho $\lambda_2=\lambda_1$. Thế vào phương trình sau, ta được $\lambda_3=3\lambda_1$.
   Chọn $\lambda_1 = 1 > 0$, suy ra $\lambda_2 = 1 > 0$ và $\lambda_3 = 3 > 0$. Vector $\lambda = (1, 1, 3)^T$ hoàn toàn thỏa mãn điều kiện không âm $\lambda \ge 0$.
   Tính tích vô hướng $b^T \lambda$:
   $$
   \begin{aligned}
   b^T\lambda&=1-2-3\\
   &=-4<0.
   \end{aligned}
   $$
   Cả ba điều kiện của Hệ 2 trong Bổ đề Farkas đều được thỏa mãn. Vector $\lambda = (1, 1, 3)^T$ là một chứng chỉ toán học tuyệt đối khẳng định rằng hệ bất đẳng thức ban đầu vô nghiệm.
:::

::: exercise 5. Bổ đề S-procedure và Điều kiện Bao hàm giữa hai Ellipsoid
Xét hai ellipsoid trong $\mathbb{R}^n$ có tâm tại gốc tọa độ:
$$
\mathcal E_k=\{x\in\mathbb R^n\mid x^TA_kx\le1\},
$$
với $k=1,2$ và $A_1,A_2\in\mathbb S_{++}^n$ là các ma trận đối xứng xác định dương.
1. Hãy viết điều kiện bao hàm $\mathcal{E}_1 \subseteq \mathcal{E}_2$ dưới dạng mệnh đề kéo theo giữa hai bất đẳng thức toàn phương.
2. Áp dụng Bổ đề S-procedure để thiết lập điều kiện ma trận tương đương cho mệnh đề bao hàm trên, và chứng minh rằng $\mathcal{E}_1 \subseteq \mathcal{E}_2 \iff A_1 \succeq A_2$.
3. Giải thích ý nghĩa hình học của kết quả này trong bài toán xấp xỉ bao bọc tập dữ liệu học máy.
:::
::: solution
**Lời giải**:
1. Đặt $F_1(x)=x^TA_1x-1$ và $F_0(x)=x^TA_2x-1$. Điều kiện $\mathcal E_1\subseteq\mathcal E_2$ đồng nghĩa với việc mọi điểm của ellipsoid thứ nhất đều thuộc ellipsoid thứ hai:
   $$
   F_1(x)\le0\implies F_0(x)\le0.
   $$
   Vì tại gốc tọa độ $x=0$, ta có $F_1(0)=-1<0$, điều kiện Slater ngặt được thỏa mãn.

2. Áp dụng Bổ đề S-procedure: Mệnh đề $F_1(x) \le 0 \implies F_0(x) \le 0$ đúng khi và chỉ khi tồn tại $\lambda \ge 0$ sao cho:
   $$
   F_0(x) \le \lambda F_1(x) \quad \forall x \in \mathbb{R}^n.
   $$
   Đặt $B=\lambda A_1-A_2$. Chuyển các số hạng sang cùng một vế, điều kiện trên tương đương với:
   $$
   x^TBx+1-\lambda\ge0\quad\forall x\in\mathbb R^n.
   $$
   Bất đẳng thức này nghiệm đúng với mọi $x \in \mathbb{R}^n$ khi và chỉ khi:
   - Hệ số tự do không âm: $1 - \lambda \ge 0 \implies \lambda \le 1$.
   - Ma trận liên kết nửa xác định dương: $\lambda A_1 - A_2 \succeq 0 \implies A_2 \preceq \lambda A_1$.

   Vì $\lambda \le 1$ và $A_1 \succ 0$, ta có:
   $$
   A_2\preceq\lambda A_1\preceq A_1.
   $$
   Ngược lại, nếu $A_1 \succeq A_2$, ta chỉ cần chọn đúng $\lambda = 1 \ge 0$, lúc đó $x^T A_2 x - 1 \le 1 \cdot (x^T A_1 x - 1)$ tự động thỏa mãn với mọi $x$.
   Do đó, điều kiện cần và đủ để $\mathcal{E}_1 \subseteq \mathcal{E}_2$ là $A_1 \succeq A_2$.

3. Ý nghĩa hình học:
   Trên mỗi hướng đơn vị $u$, bán kính của ellipsoid $\mathcal E_k$ là $r_k(u)=1/\sqrt{u^TA_ku}$. Điều kiện $A_1\succeq A_2$ có nghĩa là $u^TA_1u\ge u^TA_2u$ trên mọi hướng. Vì vậy, $r_1(u)\le r_2(u)$ và ellipsoid thứ nhất nằm trong ellipsoid thứ hai. Các trục chính của hai ellipsoid có thể khác hướng, nên chỉ so sánh độ dài bán trục là chưa đủ để kết luận bao hàm.
:::

::: exercise 6. Kiểm tra điều kiện Slater khi có ràng buộc đẳng thức và giải hệ KKT
Xét bài toán tối ưu lồi với hai biến quyết định $x = (x_1, x_2)^T \in \mathbb{R}^2$:
$$
\begin{aligned}
&\min_{x} \quad x_1^2 + x_2^2\\
&\text{s.t.}\quad x_1 + x_2 = 1,\\
&\phantom{\text{subject to}\quad } x_1 \ge 0, \quad x_2 \ge 0.
\end{aligned}
$$
1. Đưa bài toán về dạng chuẩn tắc. Tìm một điểm thỏa mãn điều kiện Slater ngặt khi có sự hiện diện của ràng buộc đẳng thức affine.
2. Kiểm tra tính hữu hạn của giá trị tối ưu gốc $p^*$ và phát biểu kết luận của Định lý Slater về đối ngẫu mạnh và sự tồn tại nghiệm đối ngẫu.
3. Thiết lập hàm Lagrangian và hệ điều kiện Karush-Kuhn-Tucker (KKT). Tìm nghiệm tối ưu gốc $x^*$ và bộ nhân tử đối ngẫu tối ưu $(\lambda^*, \nu^*)$.
:::

::: solution
1. **Dạng chuẩn tắc và điểm Slater**:
   Viết các ràng buộc dưới dạng bất đẳng thức chuẩn tắc $f_i(x) \le 0$:
   $$
   f_i(x)=-x_i\le0,\quad i=1,2,
   $$
   cùng ràng buộc đẳng thức affine $h_1(x) = x_1 + x_2 - 1 = 0$.
   
   Để thỏa mãn điều kiện Slater tổng quát khi có ràng buộc đẳng thức $Ax = b$, ta cần tìm một điểm $\bar{x}$ nằm trong phần trong tương đối (relative interior), tức thỏa mãn bất đẳng thức ngặt $f_i(\bar{x}) < 0$ và đồng thời nghiệm đúng ràng buộc đẳng thức.
   
   Chọn điểm $\bar{x} = (0{,}5; 0{,}5)$:
   - Ràng buộc bất đẳng thức: Thỏa mãn ngặt $-0{,}5 < 0$ và $-0{,}5 < 0$.
   - Ràng buộc đẳng thức: $0{,}5 + 0{,}5 = 1$ (thỏa mãn chính xác).
   
   Do đó, điểm $\bar{x} = (0{,}5; 0{,}5)$ là điểm Slater hợp lệ của bài toán.

2. **Tính hữu hạn và kết luận của Định lý Slater**:
   Hàm mục tiêu $x_1^2 + x_2^2 \ge 0$ bị chặn dưới bởi 0. Điểm $\bar{x} = (0{,}5; 0{,}5)$ khả thi và có giá trị mục tiêu $0{,}5^2 + 0{,}5^2 = 0{,}5$, suy ra $0 \le p^* \le 0{,}5$.
   
   Hàm mục tiêu và các hàm ràng buộc bất đẳng thức đều lồi, ràng buộc đẳng thức là affine. Vì điều kiện Slater được thỏa mãn và $p^*$ hữu hạn, Định lý Slater bảo đảm:
   - Đối ngẫu mạnh xảy ra: $p^* = d^*$.
   - Nghiệm của bài toán đối ngẫu $(\lambda^*, \nu^*)$ chắc chắn tồn tại và đạt được giá trị cực đại hữu hạn.

3. **Thiết lập Lagrangian và giải hệ KKT**:
   Với $\lambda_1,\lambda_2\ge0$ và $\nu\in\mathbb R$, đặt $\ell_i(x_i)=x_i^2+(\nu-\lambda_i)x_i$ cho $i=1,2$. Hàm Lagrangian là:
   $$
   L=\ell_1(x_1)+\ell_2(x_2)-\nu.
   $$
   Hệ điều kiện KKT gồm:
   - Khả thi gốc: $x_1 + x_2 = 1$, $x_1 \ge 0$, $x_2 \ge 0$.
   - Khả thi đối ngẫu: $\lambda_1 \ge 0$, $\lambda_2 \ge 0$.
   - Bù trừ (Complementary slackness): $\lambda_1 x_1 = 0$, $\lambda_2 x_2 = 0$.
   - Triệt tiêu đạo hàm:
     $$
     \begin{aligned}
     \frac{\partial L}{\partial x_1} &= 2x_1 - \lambda_1 + \nu = 0, \\
     \frac{\partial L}{\partial x_2} &= 2x_2 - \lambda_2 + \nu = 0.
     \end{aligned}
     $$
   
   Xét ứng viên đối xứng $x_1^* = 0{,}5 > 0$ và $x_2^* = 0{,}5 > 0$.
   Theo điều kiện bù trừ, vì $x_1^* > 0$ và $x_2^* > 0$, bắt buộc:
   $$
   \lambda_1^* = 0, \qquad \lambda_2^* = 0.
   $$
   Thay vào phương trình đạo hàm:
   $$
   1+\nu=0\implies\nu^*=-1.
   $$
   Lưu ý: Nhân tử Lagrange của ràng buộc đẳng thức $\nu$ được phép nhận giá trị âm tùy ý.
   
   Bộ nghiệm $(x^*, \lambda^*, \nu^*) = ((0{,}5; 0{,}5), (0, 0), -1)$ thỏa mãn trọn vẹn cả bốn nhóm điều kiện KKT. Do tính lồi của bài toán, bộ này chứng nhận nghiệm tối ưu toàn cục duy nhất với giá trị tối ưu $p^* = d^* = 0{,}5$.
:::

::: exercise 7. Giới hạn của định lý đối ngẫu và sự không đạt nghiệm đối ngẫu khi vi phạm Slater
Xét bài toán tối ưu một biến sau:
$$
\min_{x \in \mathbb{R}} x \quad \text{s.t.} \quad x^2 \le 0.
$$
1. Xác định tập khả thi, nghiệm tối ưu gốc $x^*$ và giá trị tối ưu $p^*$. Kiểm tra xem bài toán có thỏa mãn điều kiện Slater không.
2. Thiết lập hàm Lagrangian và tính hàm đối ngẫu Lagrange $g(\lambda)$ trong hai trường hợp $\lambda = 0$ và $\lambda > 0$.
3. Tìm giá trị tối ưu đối ngẫu $d^* = \sup_{\lambda \ge 0} g(\lambda)$. Đối ngẫu mạnh có xảy ra không? Nghiệm tối ưu đối ngẫu có tồn tại không?
4. Kiểm tra xem hệ điều kiện dừng KKT có nghiệm hay không và rút ra kết luận sâu sắc về vai trò của điều kiện chính quy (qualification conditions).
:::

::: solution
1. **Khảo sát bài toán gốc và kiểm tra Slater**:
   Tập khả thi chỉ gồm một điểm duy nhất $\{x \in \mathbb{R} \mid x^2 \le 0\} = \{0\}$.
   Do đó nghiệm tối ưu gốc là $x^* = 0$, với giá trị tối ưu $p^* = 0$.
   
   Điều kiện Slater đòi hỏi tồn tại điểm $\bar{x}$ thỏa mãn bất đẳng thức ngặt $\bar{x}^2 < 0$. Vì bình phương của số thực luôn không âm, không tồn tại điểm nào thỏa mãn. Do đó điều kiện Slater bị vi phạm hoàn toàn.

2. **Hàm Lagrangian và hàm đối ngẫu**:
   Hàm Lagrangian với $\lambda \ge 0$:
   $$
   L(x, \lambda) = x + \lambda x^2.
   $$
   - Khi $\lambda = 0$: $L(x, 0) = x$. Cực tiểu của hàm tuyến tính trên $\mathbb{R}$ là:
     $$
     g(0) = \inf_{x \in \mathbb{R}} x = -\infty.
     $$
   - Khi $\lambda>0$: Biểu thức $L(x,\lambda)=\lambda x^2+x$ là tam thức bậc hai có hệ số bậc hai dương. Đặt $z=x+1/(2\lambda)$, phép hoàn thành bình phương cho:
     $$
     L(x,\lambda)=\lambda z^2-\frac1{4\lambda}.
     $$
     Do đó cực tiểu đạt tại $x = -\frac{1}{2\lambda}$, cho giá trị hàm đối ngẫu:
     $$
     g(\lambda) = -\frac{1}{4\lambda}.
     $$

3. **Khoảng cách đối ngẫu và sự đạt nghiệm**:
   Hàm đối ngẫu là $g(\lambda) = -\frac{1}{4\lambda} < 0$ với mọi $\lambda > 0$.
   Khi $\lambda \to +\infty$, ta có $-\frac{1}{4\lambda} \to 0$. Do đó:
   $$
   d^* = \sup_{\lambda > 0} \left(-\frac{1}{4\lambda}\right) = 0.
   $$
   So sánh hai giá trị: Ta có $p^* = 0$ và $d^* = 0$.
   Như vậy, đối ngẫu mạnh vẫn xảy ra ($p^* = d^* = 0$, khoảng cách đối ngẫu bằng 0).
   
   Tuy nhiên, không tồn tại bất kỳ giá trị hữu hạn nào của $\lambda \ge 0$ để đạt được $g(\lambda) = 0$, vì với mọi $\lambda < +\infty$ hữu hạn thì $-\frac{1}{4\lambda} < 0$. Ta kết luận: Bài toán đạt đối ngẫu mạnh nhưng **không đạt nghiệm đối ngẫu** (the dual supremum is not attained).

4. **Kiểm tra điều kiện dừng KKT**:
   Điều kiện triệt tiêu đạo hàm KKT tại điểm tối ưu gốc $x^* = 0$:
   $$
   \nabla_xL(0,\lambda)=1\ne0.
   $$
   Vì vậy, điều kiện dừng không thể thỏa mãn với bất kỳ $\lambda\in\mathbb R$ nào.
   
   **Nhận xét sâu sắc**: Điểm $x^* = 0$ là nghiệm tối ưu toàn cục duy nhất của một bài toán lồi trơn, nhưng không tồn tại bất kỳ nhân tử Lagrange KKT nào đi kèm. Điều này chứng minh rằng điều kiện cần KKT chỉ có hiệu lực khi bài toán thỏa mãn một điều kiện chính quy (chẳng hạn như điều kiện Slater). Khi vi phạm Slater, siêu phẳng tựa của tập giá trị trở thành siêu phẳng thẳng đứng, khiến nhân tử đối ngẫu bị đẩy ra vô hạn.
:::

::: exercise 8. Ứng dụng KKT và phân tích độ nhạy trong hồi quy tham số
Xét bài toán ước lượng một tham số trọng số $w \in \mathbb{R}$ với ngân sách chặn độ lớn $\tau > 0$:
$$
\min_{w \in \mathbb{R}} \frac{1}{2}(w - 3)^2 \quad \text{s.t.} \quad w^2 \le \tau.
$$
1. Khi $\tau = 1$, thiết lập hệ điều kiện KKT. Giải tất cả các nhánh suy ra từ điều kiện bù trừ và loại bỏ các nghiệm ngoại lai để tìm $(w^*, \lambda^*)$.
2. Tổng quát hóa cho tham số $\tau > 0$ tùy ý: Tìm nghiệm tối ưu $w^*(\tau)$, nhân tử đối ngẫu $\lambda^*(\tau)$, và hàm giá trị tối ưu $p^*(\tau)$ theo hai trường hợp $0 < \tau < 9$ và $\tau \ge 9$.
3. Kiểm chứng công thức độ nhạy vi phân (phân tích giá bóng):
   $$
   \frac{\mathrm{d} p^*}{\mathrm{d} \tau} = -\lambda^*(\tau).
   $$
4. Tại điểm ngưỡng $\tau = 9$, ràng buộc có hoạt động không, và nhân tử Lagrange nhận giá trị gì?
:::

::: solution
1. **Giải KKT khi $\tau = 1$**:
   Đặt $a=w-3$ và $b=w^2-1$. Hàm Lagrangian là:
   $$
   L(w,\lambda)=\frac12a^2+\lambda b.
   $$
   Hệ điều kiện KKT:
   - Khả thi gốc: $w^2 \le 1 \iff -1 \le w \le 1$.
   - Khả thi đối ngẫu: $\lambda \ge 0$.
   - Bù trừ: $\lambda(w^2 - 1) = 0$.
   - Triệt tiêu đạo hàm: $(w - 3) + 2\lambda w = 0$.
   
   Khảo sát hai nhánh từ điều kiện bù trừ:
   - **Nhánh 1: $\lambda = 0$**.
     Thay vào điều kiện dừng: $w - 3 = 0 \implies w = 3$. Điểm này có $w^2 = 9 > 1$, vi phạm tính khả thi gốc. Nhánh này bị loại.
   - **Nhánh 2**: Trường hợp $w^2 = 1 \implies w = 1$ hoặc $w = -1$.
     - Nếu $w = -1$: Đạo hàm $(-1 - 3) + 2\lambda(-1) = 0$ dẫn đến $\lambda = -2 < 0$. Vi phạm tính khả thi đối ngẫu $\lambda \ge 0$. Loại.
     - Nếu $w = 1$: Đạo hàm $(1 - 3) + 2\lambda(1) = 0$ dẫn đến $\lambda = 1 \ge 0$. Thỏa mãn trọn vẹn.
   
   Vậy nghiệm tối ưu duy nhất khi $\tau = 1$ là $w^* = 1$, nhân tử đối ngẫu $\lambda^* = 1$, giá trị mất mát tối ưu $p^*(1) = \frac{1}{2}(1 - 3)^2 = 2$.

2. **Tổng quát hóa theo tham số $\tau > 0$**:
   Hàm mục tiêu có cực tiểu tự do tại $w = 3$.
   - **Trường hợp $0 < \tau < 9$**:
     Miền khả thi là $[-\sqrt{\tau}, \sqrt{\tau}]$. Vì $3 > \sqrt{\tau}$, điểm khả thi gần $3$ nhất chính là đầu mút phải $w^*(\tau) = \sqrt{\tau}$.
     Thay vào phương trình đạo hàm $(w - 3) + 2\lambda w = 0$:
     $$
     \lambda^*(\tau)=\frac{3-\sqrt\tau}{2\sqrt\tau}>0.
     $$
     Giá trị mất mát tối ưu là:
     $$
     \begin{aligned}
     p^*(\tau)&=\frac12(\sqrt\tau-3)^2\\
     &=\frac12(\tau-6\sqrt\tau+9).
     \end{aligned}
     $$
   - **Trường hợp $\tau \ge 9$**:
     Điểm tự do $w = 3$ thỏa mãn $3^2 = 9 \le \tau$ nên khả thi.
     Do đó $w^*(\tau) = 3$, nhân tử $\lambda^*(\tau) = 0$, và giá trị mất mát $p^*(\tau) = 0$.

3. **Kiểm chứng định lý độ nhạy vi phân**:
   Với $0 < \tau < 9$, lấy đạo hàm của hàm giá trị tối ưu theo tham số ràng buộc $\tau$:
   $$
   \begin{aligned}
   \frac{\mathrm dp^*}{\mathrm d\tau}&=\frac12(1-3\tau^{-1/2})\\
   &=\frac12-\frac3{2\sqrt\tau}\\
   &=-\frac{3-\sqrt\tau}{2\sqrt\tau}.
   \end{aligned}
   $$
   Đối chiếu với nhân tử đối ngẫu $\lambda^*(\tau)$:
   $$
   \frac{\mathrm{d} p^*}{\mathrm{d} \tau} = -\lambda^*(\tau).
   $$
   Công thức hoàn toàn khớp khít. Ý nghĩa kinh tế và kỹ thuật: Nhân tử Lagrange chính là "giá bóng" (shadow price), đo lường tốc độ suy giảm của hàm mục tiêu khi ta nới lỏng ngân sách tài nguyên thêm một lượng vi phân.

4. **Tại điểm ngưỡng $\tau = 9$**:
   Tại $\tau = 9$, ta có $w^* = 3$ và $(w^*)^2 = 9 = \tau$. Ràng buộc đạt dấu bằng nên là ràng buộc hoạt động (active constraint). Tuy nhiên nhân tử đối ngẫu $\lambda^*(9) = \frac{3 - \sqrt{9}}{2\sqrt{9}} = 0$.
   
   **Kết luận**: Ràng buộc hoạt động không nhất thiết phải có nhân tử Lagrange dương ngặt. Khi nghiệm không ràng buộc tình cờ nằm ngay trên biên của miền khả thi, ràng buộc hoạt động nhưng nhân tử Lagrange bằng đúng 0.
:::

::: exercise 9. Giải tích đối ngẫu hai chiều và chứng nhận khoảng cách đối ngẫu bằng 0
Xét bài toán tìm vector có bình phương độ dài nhỏ nhất thỏa mãn tổng các tọa độ đạt yêu cầu:
$$
\min_{x \in \mathbb{R}^2} (x_1^2 + x_2^2) \quad \text{s.t.} \quad x_1 + x_2 \ge 1.
$$
1. Kiểm tra tính lồi, điều kiện Slater và tính hữu hạn của giá trị tối ưu gốc $p^*$.
2. Thiết lập hàm Lagrangian và tính tường minh hàm đối ngẫu Lagrange $g(\lambda)$ trên miền $\lambda \ge 0$.
3. Giải bài toán đối ngẫu để tìm $\lambda^*$ và giá trị tối ưu đối ngẫu $d^*$.
4. Dùng đẳng thức hoàn thành bình phương của Lagrangian tại $\lambda^*$ để viết một chứng nhận đại số không thể bác bỏ rằng khoảng cách đối ngẫu bằng 0.
:::

::: solution
1. **Kiểm tra tính lồi và điều kiện Slater**:
   Hàm mục tiêu $f_0(x) = x_1^2 + x_2^2$ có Hessian $2I \succ 0$ nên lồi chặt.
   Ràng buộc viết lại thành $f_1(x) = 1 - x_1 - x_2 \le 0$ là hàm affine.
   Điểm $\bar{x} = (1, 1)$ có $1 - 1 - 1 = -1 < 0$, thỏa mãn điều kiện Slater ngặt.
   Vì $x_1^2 + x_2^2 \ge 0$ và có điểm khả thi hữu hạn (chẳng hạn $(1, 0)$ có chi phí 1), giá trị tối ưu $p^*$ là hữu hạn và thỏa mãn $0 \le p^* \le 1$.

2. **Hàm Lagrangian và hàm đối ngẫu**:
   Với $\lambda\ge0$, đặt $u_i=x_i-\lambda/2$ cho $i=1,2$. Hoàn thành bình phương từng biến:
   $$
   \begin{aligned}
   x_i^2-\lambda x_i&=\left(x_i-\frac\lambda2\right)^2-\frac{\lambda^2}4\\
   &=u_i^2-\frac{\lambda^2}4.
   \end{aligned}
   $$
   Do $L=x_1^2+x_2^2+\lambda(1-x_1-x_2)$, suy ra:
   $$
   L(x,\lambda)=u_1^2+u_2^2+\lambda-\frac{\lambda^2}2.
   $$
   Cực tiểu theo $x$ đạt được tại $x_1(\lambda) = x_2(\lambda) = \frac{\lambda}{2}$.
   Hàm đối ngẫu Lagrange:
   $$
   g(\lambda) = \inf_{x \in \mathbb{R}^2} L(x, \lambda) = \lambda - \frac{\lambda^2}{2}.
   $$

3. **Giải bài toán đối ngẫu**:
   Bài toán đối ngẫu Lagrange:
   $$
   \max_{\lambda \ge 0} \quad g(\lambda) = \lambda - \frac{\lambda^2}{2}.
   $$
   Đạo hàm: $g'(\lambda) = 1 - \lambda = 0 \implies \lambda^* = 1 \ge 0$.
   Đạo hàm bậc hai $g''(\lambda) = -1 < 0$, hàm số lõm ngặt và đạt cực đại tại $\lambda^* = 1$.
   Giá trị tối ưu đối ngẫu là:
   $$
   d^* = g(1) = 1 - \frac{1^2}{2} = \frac{1}{2}.
   $$

4. **Chứng nhận khoảng cách đối ngẫu bằng 0**:
   Tại nhân tử đối ngẫu tối ưu $\lambda^* = 1$, Lagrangian trở thành:
   $$
   L(x,1)=u_1^2+u_2^2+\frac12,
   $$
   trong đó $u_i=x_i-1/2$.
   Vì tổng hai bình phương luôn không âm với mọi $x \in \mathbb{R}^2$, ta có:
   $$
   L(x, 1) \ge \frac{1}{2} \quad \forall x \in \mathbb{R}^2.
   $$
   Mặt khác, với mọi điểm $x$ khả thi bất kỳ của bài toán gốc ($x_1 + x_2 \ge 1$), ta có:
   $$
   f_0(x)\ge L(x,1)\ge\frac12.
   $$
   Bất đẳng thức này chứng minh rằng *mọi điểm khả thi đều có chi phí không nhỏ hơn $\frac{1}{2}$*.
   
   Xét điểm $x^* = (0{,}5; 0{,}5)$: Điểm này khả thi vì $0{,}5 + 0{,}5 = 1 \ge 1$, và có chi phí đúng bằng:
   $$
   \begin{aligned}
   f_0(x^*)&=0{,}5^2+0{,}5^2\\
   &=0{,}25+0{,}25\\
   &=0{,}5.
   \end{aligned}
   $$
   Điểm khả thi $x^*$ đạt đúng cận dưới đối ngẫu $d^* = 0{,}5$, chứng minh $p^* = d^* = 0{,}5$ và khoảng cách đối ngẫu bằng 0. Nghiệm tối ưu toàn cục duy nhất là $x^* = (0{,}5; 0{,}5)$.
:::


---

## Tóm tắt cốt lõi

1. **Hàm Lagrangian và Đối ngẫu yếu**: Thông qua việc đưa các ràng buộc vào hàm mục tiêu với nhân tử $\lambda \succeq 0$, hàm đối ngẫu $g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$ luôn tạo ra một cận dưới không thể vượt qua: $g(\lambda, \nu) \le p^*$.
2. **Tính lõm của bài toán đối ngẫu**: Là infimum của một họ các hàm affine, hàm đối ngẫu luôn là hàm lõm. Bài toán cực đại hóa cận dưới luôn luôn là một bài toán tối ưu lồi, bất kể tính chất của bài toán gốc.
3. **Hàm liên hợp Fenchel**: Cầu nối toán học liên kết giải tích lồi với đối ngẫu. Bất đẳng thức Fenchel–Young $x^T y \le f(x) + f^*(y)$ thiết lập mối quan hệ tiếp tuyến nền tảng.
4. **Bản chất hình học của đối ngẫu**: Hàm đối ngẫu $g(\lambda)$ biểu diễn giao điểm của siêu phẳng tựa đỡ tập $\mathcal{A}$ với trục tung. Điều kiện Slater ngăn chặn siêu phẳng tựa thẳng đứng, bảo đảm đối ngẫu mạnh ($p^* = d^*$).
5. **Điểm yên ngựa Minimax**: Điểm tối ưu của bài toán đối ngẫu mạnh chính là điểm yên ngựa của hàm Lagrangian, tương ứng với trạng thái cân bằng trong lý thuyết trò chơi và huấn luyện đối kháng (GANs).
6. **Hệ điều kiện KKT**: Bốn nhóm điều kiện (Khả thi gốc, Khả thi đối ngẫu, Bù trừ, Triệt tiêu gradient) xác lập tiêu chuẩn cần và đủ cho tính tối ưu toàn cục của các bài toán lồi khả vi.
7. **Chứng chỉ vô nghiệm và Bổ đề Farkas**: Đối ngẫu cung cấp cơ chế nhị phân kiểm tra tính khả thi của hệ thống ràng buộc mà không cần thử nghiệm từng điểm.
8. **Hai hàm toàn phương và Bổ đề S-procedure**: Bài toán cực tiểu hóa hàm toàn phương với một ràng buộc toàn phương đạt đối ngẫu mạnh khi có điểm Slater ngặt và giá trị tối ưu hữu hạn. Định lý Dines cho hai dạng toàn phương thuần nhất là một công cụ hình học trong chứng minh. S-procedure chuyển điều kiện kéo theo giữa hai bất đẳng thức toàn phương thành một bất đẳng thức ma trận tuyến tính (LMI).

---

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press. Đọc kỹ Chương 5 (Đối ngẫu Lagrange), Phụ lục B (Các bài toán với hai hàm toàn phương, S-procedure, chứng minh đối ngẫu mạnh).
- Dimitri P. Bertsekas, *Convex Optimization Theory*, Athena Scientific.
- R. Tyrrell Rockafellar, *Convex Analysis*, Princeton University Press.

Tiếp theo: [Bài 04: Thuật toán Gradient Descent và Phương pháp Newton](./bai-04-gradient-newton.md).
