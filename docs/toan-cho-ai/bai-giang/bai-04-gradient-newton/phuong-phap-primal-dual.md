---
course: toan-cho-ai
lecture: bai-04-gradient-newton
topic: phuong-phap-primal-dual
section: topic
title: "Phương pháp Điểm trong Primal-Dual"
description: "Lý thuyết và thuật toán phương pháp điểm trong nguyên thủy - đối ngẫu (Primal-Dual Interior-Point), phần dư KKT, hướng tìm kiếm kết hợp và kỹ thuật giải hệ tuyến tính khối KKT hiệu năng cao."
---

Trong các bài học trước về phương pháp hàm chắn logarit (Barrier Method), ta đã thấy quy trình tối ưu hóa giải bài toán lồi có ràng buộc bất đẳng thức thông qua một chuỗi các bài toán không ràng buộc xấp xỉ. Tuy nhiên, Barrier Method bộc lộ hai hạn chế lớn trong thực tế: Thứ nhất, thuật toán đòi hỏi nghiệm xuất phát phải khả thi nghiêm ngặt, hoặc phải giải một bài toán Pha I riêng biệt rất tốn kém. Thứ hai, mỗi bước lặp ngoài đòi hỏi giải gần như chính xác bài toán định tâm bên trong bằng phương pháp Newton, khiến tổng chi phí tính toán tăng cao.

Phương pháp điểm trong nguyên thủy - đối ngẫu (**Primal-Dual Interior-Point Method**) khắc phục triệt để các nhược điểm này. Đây là thuật toán tiêu chuẩn công nghiệp được triển khai trong hầu hết các bộ giải tối ưu hóa hiện đại như MOSEK, SDPT3, SeDuMi, OSQP hay Ipopt. Thuật toán cập nhật đồng thời biến nguyên thủy $x$ và các nhân tử đối ngẫu $\lambda, \nu$ tại mỗi bước lặp, không yêu cầu điểm lặp phải khả thi nghiêm ngặt (Infeasible Start), và đạt tốc độ hội tụ siêu tuyến tính ở lân cận nghiệm tối ưu.

---

## 1. Hệ Điều Kiện KKT Bị Xáo Trộn và Độ Lệch Đối Ngẫu Đại Diện

Xét bài toán tối ưu lồi tổng quát:

$$
\begin{aligned}
\min_{x} \quad & f_0(x) \\
\text{s.t.} \quad & f_i(x) \le 0, \quad i = 1, \dots, m, \\
& A x = b,
\end{aligned}
$$

trong đó $f_0, f_1, \dots, f_m: \mathbb{R}^n \to \mathbb{R}$ là các hàm lồi khả vi liên tục hai lần, và ma trận $A \in \mathbb{R}^{p \times n}$ có hạng đủ $\operatorname{rank}(A) = p$.

Hệ điều kiện tối ưu KKT của bài toán gồm bốn nhóm:

1. **Khả thi nguyên thủy**: Biểu thức $f_i(x^*) \le 0$ với mọi $i = 1, \dots, m$ và $A x^* = b$.
2. **Khả thi đối ngẫu**: Điều kiện $\lambda_i^* \ge 0$ với mọi $i = 1, \dots, m$.
3. **Triệt tiêu gradient Lagrange**: Ta có $\nabla f_0(x^*) + Df(x^*)^T \lambda^* + A^T \nu^* = 0$.
4. **Bù trừ tương hỗ**: Tích $\lambda_i^* f_i(x^*) = 0$ với mọi $i = 1, \dots, m$.

### Hệ KKT bị xáo trộn (Perturbed KKT Conditions)

Thay vì giải trực tiếp điều kiện bù trừ rời rạc $\lambda_i f_i(x) = 0$, ta nới lỏng tích này về một đại lượng dương $\eta = 1/t > 0$:

$$
\begin{aligned}
\nabla f_0(x) + \sum_{i=1}^m \lambda_i \nabla f_i(x) + A^T \nu &= 0, \\
-\lambda_i f_i(x) &= \eta, \quad i = 1, \dots, m, \\
A x &= b, \\
f_i(x) < 0, \quad \lambda_i &> 0, \quad i = 1, \dots, m.
\end{aligned}
$$

Khi $\eta \to 0$ (tương đương $t \to \infty$), nghiệm $(x^*(\eta), \lambda^*(\eta), \nu^*(\eta))$ của hệ phương trình trên sẽ hội tụ chính xác về nghiệm tối ưu $(x^*, \lambda^*, \nu^*)$ của bài toán gốc. Tập hợp các nghiệm $(x^*(\eta), \lambda^*(\eta), \nu^*(\eta))$ khi $\eta > 0$ thay đổi quét nên **đường trung tâm nguyên thủy - đối ngẫu** (Primal-Dual Central Path).

### Độ lệch đối ngẫu đại diện (Surrogate Duality Gap)

Tại một điểm bất kỳ $(x, \lambda, \nu)$ thỏa mãn điều kiện miền trong $f_i(x) < 0$ và $\lambda_i > 0$, điểm này có thể chưa thỏa mãn ràng buộc đẳng thức $Ax = b$ hoặc chưa cân bằng gradient đối ngẫu. Do đó, khoảng cách đối ngẫu lý thuyết chuẩn có thể chưa xác định. Ta định nghĩa **độ lệch đối ngẫu đại diện**:

$$
\hat{\eta}(x, \lambda) = -\frac{1}{m} \sum_{i=1}^m \lambda_i f_i(x) = -\frac{1}{m} \lambda^T f(x).
$$

Khai triển tường minh:

$$
\hat{\eta}(x, \lambda) = \frac{1}{m} \left( -\lambda_1 f_1(x) - \lambda_2 f_2(x) - \dots - \lambda_m f_m(x) \right).
$$

Đại lượng $\hat{\eta}(x, \lambda)$ đo lường mức độ vi phạm trung bình của điều kiện bù trừ tương hỗ. Nếu điểm $(x, \lambda, \nu)$ đồng thời khả thi nguyên thủy và đối ngẫu, thì tổng khoảng cách đối ngẫu chính bằng $m \hat{\eta}(x, \lambda)$.

---

## 2. Các Vector Phần Dư KKT

Để đo lường mức độ thỏa mãn hệ điều kiện KKT bị xáo trộn tại điểm hiện tại $(x, \lambda, \nu)$, ta chia sai số thành ba thành phần phần dư:

1. **Phần dư đối ngẫu (Dual residual)**:
   $$
   r_{\text{dual}}(x, \lambda, \nu) = \nabla f_0(x) + Df(x)^T \lambda + A^T \nu \in \mathbb{R}^n,
   $$
   trong đó ma trận Jacobi $Df(x) = \begin{bmatrix} \nabla f_1(x)^T \\ \vdots \\ \nabla f_m(x)^T \end{bmatrix} \in \mathbb{R}^{m \times n}$.

2. **Phần dư bù trừ trung tâm (Centering residual)**:
   $$
   r_{\text{cent}}(x, \lambda) = -\operatorname{diag}(\lambda) f(x) - \frac{1}{t} \mathbf{1} \in \mathbb{R}^m,
   $$
   trong đó $\operatorname{diag}(\lambda) = \operatorname{diag}(\lambda_1, \dots, \lambda_m)$ và $\mathbf{1} = (1, \dots, 1)^T$. Thành phần thứ $i$ của vector này là:
   $$
   (r_{\text{cent}})_i = -\lambda_i f_i(x) - \frac{1}{t}.
   $$

3. **Phần dư nguyên thủy (Primal residual)**:
   $$
   r_{\text{pri}}(x) = A x - b \in \mathbb{R}^p.
   $$

Gộp ba phần dư thành vector tổng thể $r(x, \lambda, \nu) \in \mathbb{R}^{n + m + p}$:

$$
r(x, \lambda, \nu) = \begin{bmatrix} r_{\text{dual}}(x, \lambda, \nu) \\ r_{\text{cent}}(x, \lambda) \\ r_{\text{pri}}(x) \end{bmatrix}.
$$

Hệ phương trình KKT bị xáo trộn tương đương với phương trình phi tuyến $r(x, \lambda, \nu) = 0$.

---

## 3. Hướng Tìm Kiếm Primal-Dual và Phương Pháp Newton

Để tìm bước cập nhật $(\Delta x, \Delta \lambda, \Delta \nu)$, ta áp dụng xấp xỉ tuyến tính Taylor bậc nhất cho hệ phi tuyến $r(x + \Delta x, \lambda + \Delta \lambda, \nu + \Delta \nu) = 0$:

$$
r(x + \Delta x, \lambda + \Delta \lambda, \nu + \Delta \nu) \approx r(x, \lambda, \nu) + \nabla r(x, \lambda, \nu) \begin{bmatrix} \Delta x \\ \Delta \lambda \\ \Delta \nu \end{bmatrix} = 0.
$$

Lấy đạo hàm từng khối của $r$ theo $(x, \lambda, \nu)$, ta thu được hệ phương trình ma trận tuyến tính KKT khối:

$$
\begin{bmatrix}
H & Df(x)^T & A^T \\
-\operatorname{diag}(\lambda) Df(x) & -\operatorname{diag}(f(x)) & 0 \\
A & 0 & 0
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta \lambda \\
\Delta \nu
\end{bmatrix}
=
-\begin{bmatrix}
r_{\text{dual}} \\
r_{\text{cent}} \\
r_{\text{pri}}
\end{bmatrix},
$$

trong đó ma trận Hessian kết hợp $H \in \mathbb{R}^{n \times n}$ được xác định bởi:

$$
H = \nabla^2 f_0(x) + \sum_{i=1}^m \lambda_i \nabla^2 f_i(x).
$$

Do tính lồi của các hàm $f_i$ và điều kiện $\lambda_i > 0$, ma trận $H$ luôn nửa xác định dương (và xác định dương nếu ít nhất một hàm là lồi nghiêm ngặt).

### Phân rã hướng Affine-Scaling và Hướng Centering

Trong thực tế, ta thường chọn tham số đích $1/t = \sigma \hat{\eta}$, với $\sigma \in [0, 1]$ được gọi là **tham số định tâm** (Centering parameter):

- Khi $\sigma = 0$: Tham số $1/t = 0$, hướng tìm kiếm thuần túy nhằm triệt tiêu phần dư và giảm khoảng cách đối ngẫu về 0. Hướng này gọi là **hướng affine-scaling** (Affine-scaling direction).
- Khi $\sigma = 1$: Thuật toán tập trung kéo điểm lặp về trục đối xứng của đường trung tâm.
- Thuật toán nổi tiếng **Mehrotra Predictor-Corrector** giải hệ trên hai lần trong mỗi bước lặp: Lần đầu tính hướng dự đoán affine-scaling $(\Delta x_{\text{aff}}, \Delta \lambda_{\text{aff}})$, xác định bước nhảy tối đa cho phép, từ đó tính độ giảm khoảng cách đối ngẫu để chọn $\sigma$ thích nghi, rồi giải lần hai có bổ sung số hạng hiệu chỉnh phi tuyến bậc hai $(\Delta \lambda_{\text{aff}})_i (\Delta x_{\text{aff}})_i$.

---

## 4. Chiến Lược Bước Nhảy và Line Search Backtracking

Sau khi tính được hướng tìm kiếm $(\Delta x, \Delta \lambda, \Delta \nu)$, ta cần chọn độ dài bước nhảy $s > 0$ sao cho:

1. Biến đối ngẫu vẫn giữ dương nghiêm ngặt: $\lambda + s \Delta \lambda > 0$.
2. Biến nguyên thủy vẫn nằm trong miền xác định và thỏa mãn bất đẳng thức nghiêm ngặt: $f_i(x + s \Delta x) < 0$.
3. Chuẩn của vector phần dư $\|r(x, \lambda, \nu)\|_2$ giảm đáng kể.

### Xác định cận trên bước nhảy $s_{\max}$

Đầu tiên, ta chặn bước nhảy đối ngẫu để đảm bảo $\lambda_i + s \Delta \lambda_i > 0$:

$$
s_{\max}^{\text{dual}} = \sup \{ s \in [0, 1] \mid \lambda + s \Delta \lambda \ge 0 \} = \min \left( 1, \min_{i: \Delta \lambda_i < 0} \left( -\frac{\lambda_i}{\Delta \lambda_i} \right) \right).
$$

Tương tự, với các hàm ràng buộc bất đẳng thức (nếu là hàm tuyến tính $f_i(x) = a_i^T x - b_i$), ta có thể tính chính xác:

$$
s_{\max}^{\text{pri}} = \min \left( 1, \min_{i: a_i^T \Delta x > 0} \left( -\frac{f_i(x)}{a_i^T \Delta x} \right) \right).
$$

Để tránh điểm chạm vào biên quá sớm, ta đặt cận bước khởi tạo:

$$
s_{\max} = 0.99 \min \left( s_{\max}^{\text{pri}}, s_{\max}^{\text{dual}} \right).
$$

### Thuật toán Line Search theo chuẩn phần dư

Bắt đầu với $s = s_{\max}$, ta thực hiện co bước $s := \beta s$ ($\beta \in (0.5, 0.8)$) cho đến khi thỏa mãn hai điều kiện:

1. Tính khả thi miền trong: Điểm $x + s \Delta x \in \mathbf{dom} f_0$ và $f_i(x + s \Delta x) < 0$ với mọi $i = 1, \dots, m$.
2. Điều kiện giảm chuẩn phần dư Armijo:
   $$
   \|r(x + s \Delta x, \lambda + s \Delta \lambda, \nu + s \Delta \nu)\|_2 \le (1 - \alpha s) \|r(x, \lambda, \nu)\|_2,
   $$
   với tham số $\alpha \in (0.01, 0.1)$.

---

## 5. Kỹ Thuật Số Học Giải Hệ Tuyến Tính Khối KKT

Hệ phương trình KKT ở Mục 3 có kích thước lớn $(n + m + p) \times (n + m + p)$ và không đối xứng do phương trình thứ hai. Việc giải trực tiếp hệ này rất tốn kém. Trong thực tế tính toán, ta luôn thực hiện kỹ thuật **khử biến** để đưa về hệ đối xứng nhỏ hơn.

### Khử biến đối ngẫu $\Delta \lambda$

Từ phương trình thứ hai trong hệ KKT:

$$
-\operatorname{diag}(\lambda) Df(x) \Delta x - \operatorname{diag}(f(x)) \Delta \lambda = -r_{\text{cent}}.
$$

Vì $f_i(x) < 0$ với mọi $i$, ma trận đường chéo $\operatorname{diag}(f(x))$ khả nghịch hoàn toàn. Rút $\Delta \lambda$ theo $\Delta x$:

$$
\Delta \lambda = -\operatorname{diag}(f(x))^{-1} \left( r_{\text{cent}} + \operatorname{diag}(\lambda) Df(x) \Delta x \right).
$$

Khai triển cho từng tọa độ:

$$
\Delta \lambda_i = -\frac{(r_{\text{cent}})_i + \lambda_i \nabla f_i(x)^T \Delta x}{f_i(x)} = -\frac{-\lambda_i f_i(x) - 1/t + \lambda_i \nabla f_i(x)^T \Delta x}{f_i(x)}.
$$

### Hệ KKT rút gọn đối xứng

Thế biểu thức $\Delta \lambda$ vào phương trình thứ nhất:

$$
H \Delta x + Df(x)^T \left[ -\operatorname{diag}(f(x))^{-1} \left( r_{\text{cent}} + \operatorname{diag}(\lambda) Df(x) \Delta x \right) \right] + A^T \Delta \nu = -r_{\text{dual}}.
$$

Gộp các số hạng chứa $\Delta x$:

$$
\left( H + Df(x)^T \operatorname{diag}\left(-\frac{\lambda}{f(x)}\right) Df(x) \right) \Delta x + A^T \Delta \nu = -r_{\text{dual}} + Df(x)^T \operatorname{diag}(f(x))^{-1} r_{\text{cent}}.
$$

Đặt ma trận trọng số đường chéo $D = \operatorname{diag}\left(-\frac{\lambda_1}{f_1(x)}, \dots, -\frac{\lambda_m}{f_m(x)}\right)$. Vì $\lambda_i > 0$ và $f_i(x) < 0$, mọi phần tử trên đường chéo của $D$ đều dương nghiêm ngặt:

$$
D_{ii} = -\frac{\lambda_i}{f_i(x)} > 0.
$$

Đặt ma trận Hessian tương đương:

$$
H_{\text{eff}} = H + Df(x)^T D Df(x) \succ 0.
$$

Hệ tuyến tính rút gọn chỉ còn ẩn $(\Delta x, \Delta \nu)$ với kích thước $(n + p) \times (n + p)$:

$$
\begin{bmatrix}
H_{\text{eff}} & A^T \\
A & 0
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta \nu
\end{bmatrix}
=
-\begin{bmatrix}
r_{\text{dual}} - Df(x)^T \operatorname{diag}(f(x))^{-1} r_{\text{cent}} \\
r_{\text{pri}}
\end{bmatrix}.
$$

Hệ phương trình này là hệ KKT đối xứng kinh điển, có thể giải bằng một trong hai phương án hiệu năng cao:

1. **Khử khối ma trận Schur**: Khi $p$ nhỏ hơn nhiều so với $n$, ta tính phân tích Cholesky của $H_{\text{eff}} = L L^T$, sau đó giải hệ bù Schur kích thước $p \times p$:
   $$
   (A H_{\text{eff}}^{-1} A^T) \Delta \nu = A H_{\text{eff}}^{-1} g - r_{\text{pri}}.
   $$
2. **Phân tích $LDL^T$ không xác định đối xứng**: Khi ma trận $A$ có cấu trúc thưa lớn, ta giải trực tiếp hệ khối $(n + p) \times (n + p)$ bằng thuật toán $LDL^T$ với kỹ thuật xoay trục đường chéo (Bunch-Kaufman pivoting).

---

## 6. So Sánh Hiệu Năng: Barrier Method và Primal-Dual

Bảng dưới đây tổng kết sự khác biệt cốt lõi giữa hai họ phương pháp điểm trong:

| Tiêu chí | Phương pháp Hàm chắn (Barrier Method) | Phương pháp Primal-Dual |
| :--- | :--- | :--- |
| **Khởi tạo nghiệm** | Bắt buộc khả thi nghiêm ngặt (cần chạy Pha I) | Cho phép khởi đầu phi khả thi (Infeasible Start) |
| **Số vòng lặp** | Hai tầng (vòng lặp ngoài cập nhật $t$, vòng lặp trong chạy Newton) | Một tầng duy nhất (cập nhật đồng thời $x, \lambda, \nu$) |
| **Tốc độ hội tụ** | Tuyến tính theo tham số $t$ | Siêu tuyến tính (Superlinear) ở lân cận nghiệm |
| **Độ nhạy tham số** | Phụ thuộc vào việc chọn tham số nhân $\mu \approx 10 - 20$ | Rất linh hoạt, tham số $\sigma$ tự thích nghi |
| **Độ chính xác** | Đạt $10^{-6}$ ổn định, khó đạt $10^{-10}$ do Hessian suy biến | Dễ dàng đạt $10^{-10}$ đến $10^{-14}$ |

---

## 7. Bài Tập Tự Luyện Kèm Lời Giải Chi Tiết

### Bài tập 1: Hệ phương trình Primal-Dual cho Quy hoạch Tuyến tính (LP)

Cho bài toán quy hoạch tuyến tính dạng chuẩn:

$$
\min_{x} \quad c^T x \quad \text{s.t.} \quad A x = b, \quad x \ge 0,
$$

với $A \in \mathbb{R}^{p \times n}$ có hạng đủ $\operatorname{rank}(A) = p$.

1. Hãy viết hệ phương trình KKT bị xáo trộn với tham số $\eta = 1/t > 0$.
2. Thiết lập hệ phương trình tuyến tính xác định hướng primal-dual $(\Delta x, \Delta s, \Delta \nu)$ (với $s \ge 0$ là biến bù hoặc biến nhân tử đối ngẫu liên kết với $x \ge 0$).
3. Biến đổi để khử $\Delta s$, đưa về hệ phương trình đối xứng theo $(\Delta x, \Delta \nu)$.

#### Lời giải chi tiết:

1. Đặt biến đối ngẫu tương ứng với ràng buộc bất đẳng thức $-x \le 0$ là $s \in \mathbb{R}^n$ ($s > 0$), và với ràng buộc đẳng thức $Ax = b$ là $\nu \in \mathbb{R}^p$.

   Hệ điều kiện KKT bị xáo trộn:
   $$
   \begin{aligned}
   c - s + A^T \nu &= 0 \quad (\text{Khả thi đối ngẫu}), \\
   X S \mathbf{1} &= \eta \mathbf{1} \quad (\text{Bù trừ trung tâm}), \\
   A x &= b \quad (\text{Khả thi nguyên thủy}), \\
   x > 0, \quad s &> 0,
   \end{aligned}
   $$
   trong đó $X = \operatorname{diag}(x_1, \dots, x_n)$ và $S = \operatorname{diag}(s_1, \dots, s_n)$.

2. Các vector phần dư tại điểm hiện tại $(x, s, \nu)$:
   $$
   \begin{aligned}
   r_{\text{dual}} &= c - s + A^T \nu, \\
   r_{\text{cent}} &= X S \mathbf{1} - \eta \mathbf{1}, \\
   r_{\text{pri}} &= A x - b.
   \end{aligned}
   $$

   Tuyến tính hóa hệ phương trình tại bước lặp hiện tại:
   $$
   \begin{bmatrix}
   0 & -I & A^T \\
   S & X & 0 \\
   A & 0 & 0
   \end{bmatrix}
   \begin{bmatrix}
   \Delta x \\
   \Delta s \\
   \Delta \nu
   \end{bmatrix}
   =
   -\begin{bmatrix}
   r_{\text{dual}} \\
   r_{\text{cent}} \\
   r_{\text{pri}}
   \end{bmatrix}.
   $$

3. Từ phương trình thứ hai: $S \Delta x + X \Delta s = -r_{\text{cent}}$. Vì $x_i > 0$, ma trận $X$ khả nghịch hoàn toàn, suy ra:
   $$
   \Delta s = -X^{-1} r_{\text{cent}} - X^{-1} S \Delta x.
   $$

   Thế $\Delta s$ vào phương trình thứ nhất:
   $$
   -\Delta s + A^T \Delta \nu = -r_{\text{dual}} \implies X^{-1} S \Delta x + A^T \Delta \nu = -r_{\text{dual}} - X^{-1} r_{\text{cent}}.
   $$

   Đặt ma trận đường chéo $\Theta = S^{-1} X \succ 0$ với $\Theta_{ii} = x_i / s_i$. Nhân cả hai vế với $\Theta$:
   $$
   \Delta x + \Theta A^T \Delta \nu = -\Theta r_{\text{dual}} - S^{-1} r_{\text{cent}}.
   $$

   Nhân ma trận $A$ vào hai vế và kết hợp với phương trình thứ ba $A \Delta x = -r_{\text{pri}}$, ta thu được phương trình chuẩn xác định $\Delta \nu$:
   $$
   (A \Theta A^T) \Delta \nu = -r_{\text{pri}} + A \left( \Theta r_{\text{dual}} + S^{-1} r_{\text{cent}} \right).
   $$

   Ma trận $A \Theta A^T \in \mathbb{R}^{p \times p}$ là ma trận đối xứng xác định dương, giải được bằng phân tích Cholesky với chi phí $O(p^3) + O(p^2 n)$. Sau khi có $\Delta \nu$, ta tính ngược lại $\Delta x$ và $\Delta s$ hoàn toàn bằng các phép nhân ma trận - vector.

---

### Bài tập 2: Tính Xác Định Dương của Hệ KKT Rút Gọn trong Quy hoạch Toàn phương (QP)

Xét bài toán quy hoạch toàn phương lồi có ràng buộc bất đẳng thức:

$$
\min_{x} \quad \frac{1}{2} x^T P x + q^T x \quad \text{s.t.} \quad G x \le h,
$$

với $P \in \mathbb{S}_+^n$ và $G \in \mathbb{R}^{m \times n}$.

1. Thiết lập ma trận Hessian hiệu dụng $H_{\text{eff}}$ của hệ KKT rút gọn.
2. Giả sử $P$ chỉ nửa xác định dương ($P \succeq 0$, có thể có trị riêng bằng 0) nhưng $\ker(P) \cap \ker(G) = \{0\}$. Chứng minh rằng ma trận $H_{\text{eff}}$ luôn xác định dương nghiêm ngặt ($H_{\text{eff}} \succ 0$) tại mọi bước lặp của thuật toán primal-dual.

#### Lời giải chi tiết:

1. Với hàm mục tiêu $f_0(x) = \frac{1}{2} x^T P x + q^T x$, ta có $\nabla^2 f_0(x) = P$.

   Các hàm ràng buộc bất đẳng thức là hàm afin: Cụ thể $f_i(x) = g_i^T x - h_i$ với $g_i$ là dòng thứ $i$ của ma trận $G$. Do đó $\nabla^2 f_i(x) = 0$ và ma trận Jacobi $Df(x) = G$.

   Theo công thức ở Mục 5, ma trận Hessian hiệu dụng là:
   $$
   H_{\text{eff}} = P + G^T D G,
   $$
   trong đó $D = \operatorname{diag}\left(-\frac{\lambda_1}{g_1^T x - h_1}, \dots, -\frac{\lambda_m}{g_m^T x - h_m}\right)$.

   Do tính khả thi miền trong, ta luôn có $\lambda_i > 0$ và $g_i^T x - h_i < 0$, dẫn đến $D_{ii} > 0$ với mọi $i = 1, \dots, m$.

2. Để chứng minh $H_{\text{eff}} \succ 0$, ta xét dạng toàn phương $v^T H_{\text{eff}} v$ với một vector bất kỳ $v \in \mathbb{R}^n$:
   $$
   v^T H_{\text{eff}} v = v^T P v + v^T G^T D G v.
   $$

   Vì $P \succeq 0$, ta có $v^T P v \ge 0$.

   Vì $D$ là ma trận đường chéo với các phần tử dương nghiêm ngặt $D_{ii} > 0$, đặt $w = G v \in \mathbb{R}^m$, ta có:
   $$
   v^T G^T D G v = w^T D w = \sum_{i=1}^m D_{ii} w_i^2 \ge 0.
   $$

   Do đó $v^T H_{\text{eff}} v \ge 0$.

   Bây giờ, giả sử $v^T H_{\text{eff}} v = 0$. Vì cả hai số hạng đều không âm, đẳng thức xảy ra khi và chỉ khi:
   $$
   v^T P v = 0 \quad \text{và} \quad w^T D w = 0.
   $$

   - Do $P \succeq 0$, điều kiện $v^T P v = 0$ kéo theo $P v = 0$, tức là $v \in \ker(P)$.
   - Do $D_{ii} > 0$ với mọi $i$, điều kiện $\sum_{i=1}^m D_{ii} w_i^2 = 0$ đòi hỏi $w_i = 0$ với mọi $i$, tức là $w = G v = 0$, suy ra $v \in \ker(G)$.

   Kết hợp hai điều kiện trên:
   $$
   v \in \ker(P) \cap \ker(G).
   $$

   Theo giả thiết đề bài, $\ker(P) \cap \ker(G) = \{0\}$, suy ra bắt buộc $v = 0$.

   Như vậy, với mọi vector $v \ne 0$, ta luôn có $v^T H_{\text{eff}} v > 0$. Điều này chứng minh $H_{\text{eff}} \succ 0$, đảm bảo hệ tuyến tính KKT luôn có nghiệm duy nhất và giải được ổn định bằng phân tích Cholesky.

---

### Bài tập 3: Mô Phỏng Một Bước Lặp Primal-Dual Trực Quan

Xét bài toán tối ưu trên $\mathbb{R}$:

$$
\min_{x} \quad x \quad \text{s.t.} \quad -x \le 0.
$$

Tại bước lặp hiện tại, nghiệm thử là $x = 2$ và nhân tử đối ngẫu là $\lambda = 1$.

1. Tính độ lệch đối ngẫu đại diện $\hat{\eta}$ tại điểm này.
2. Với tham số định tâm $\sigma = 0.5$, hãy tính giá trị mục tiêu $\eta$ và các vector phần dư KKT.
3. Giải hệ phương trình KKT để tìm hướng di chuyển $(\Delta x, \Delta \lambda)$.
4. Xác định cận bước nhảy tối đa $s_{\max}$ và giá trị nghiệm mới sau khi cập nhật với bước $s = 0.8$.

#### Lời giải chi tiết:

1. Hàm mục tiêu $f_0(x) = x$ có đạo hàm $f_0'(x) = 1$. Hàm ràng buộc $f_1(x) = -x$ có $f_1'(x) = -1$.
   
   Tại $x = 2$, hàm ràng buộc nhận giá trị $f_1(2) = -2 < 0$.
   
   Độ lệch đối ngẫu đại diện:
   $$
   \hat{\eta} = -\lambda f_1(x) = -(1)(-2) = 2.
   $$

2. Với tham số định tâm $\sigma = 0.5$:
   $$
   \eta = \frac{1}{t} = \sigma \hat{\eta} = 0.5 \times 2 = 1.
   $$

   Tính các vector phần dư (trong bài toán 1 chiều, chúng là các số thực):
   - Phần dư đối ngẫu:
     $$
     r_{\text{dual}} = f_0'(x) + \lambda f_1'(x) = 1 + (1)(-1) = 0.
     $$
     (Điểm hiện tại đã thỏa mãn cân bằng đối ngẫu).
   - Phần dư bù trừ trung tâm:
     $$
     r_{\text{cent}} = -\lambda f_1(x) - \eta = -(1)(-2) - 1 = 2 - 1 = 1.
     $$
   - Phần dư nguyên thủy: Không có ràng buộc đẳng thức nên $r_{\text{pri}} = 0$.

3. Thiết lập hệ phương trình KKT:
   - Hessian $H = f_0''(x) + \lambda f_1''(x) = 0 + 0 = 0$.
   - Ma trận Jacobi $Df(x) = [-1]$.
   
   Hệ phương trình tìm $(\Delta x, \Delta \lambda)$:
   $$
   \begin{bmatrix}
   0 & -1 \\
   -(1)(-1) & -(-2)
   \end{bmatrix}
   \begin{bmatrix}
   \Delta x \\
   \Delta \lambda
   \end{bmatrix}
   =
   -\begin{bmatrix}
   0 \\
   1
   \end{bmatrix}
   \iff
   \begin{bmatrix}
   0 & -1 \\
   1 & 2
   \end{bmatrix}
   \begin{bmatrix}
   \Delta x \\
   \Delta \lambda
   \end{bmatrix}
   =
   \begin{bmatrix}
   0 \\
   -1
   \end{bmatrix}.
   $$

   Giải hệ phương trình đại số:
   - Từ phương trình thứ nhất: $-\Delta \lambda = 0 \implies \Delta \lambda = 0$.
   - Thế vào phương trình thứ hai: $\Delta x + 2(0) = -1 \implies \Delta x = -1$.

   Vậy hướng tìm kiếm là $(\Delta x, \Delta \lambda) = (-1, 0)$.

4. Đánh giá bước nhảy:
   - Vì $\Delta \lambda = 0$, nhân tử đối ngẫu không đổi nên $s_{\max}^{\text{dual}} = 1$.
   - Với biến nguyên thủy: Ta cần $x + s \Delta x = 2 - s > 0 \iff s < 2$. Do đó bước nhảy bị chặn bởi 1, tức là $s_{\max} = 1$.
   
   Cập nhật với bước $s = 0.8$:
   $$
   \begin{aligned}
   x_{\text{new}} &= x + s \Delta x = 2 + 0.8(-1) = 1.2, \\
   \lambda_{\text{new}} &= \lambda + s \Delta \lambda = 1 + 0.8(0) = 1.
   \end{aligned}
   $$

   Kiểm tra độ lệch đối ngẫu đại diện mới:
   $$
   \hat{\eta}_{\text{new}} = -\lambda_{\text{new}} f_1(x_{\text{new}}) = -(1)(-1.2) = 1.2.
   $$

   Khoảng cách đối ngẫu đã giảm từ $2$ xuống còn $1.2$, đưa điểm lặp tiến gần hơn về nghiệm tối ưu $x^* = 0$.

---

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
- Jorge Nocedal, Stephen J. Wright, *Numerical Optimization*, Springer.
