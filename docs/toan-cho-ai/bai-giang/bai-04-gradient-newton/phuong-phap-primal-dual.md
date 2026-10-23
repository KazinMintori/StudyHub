---
course: toan-cho-ai
lecture: bai-04-gradient-newton
topic: phuong-phap-primal-dual
section: topic
title: "Phương pháp Điểm trong Primal-Dual"
description: "Lý thuyết và thuật toán phương pháp điểm trong nguyên thủy - đối ngẫu (Primal-Dual Interior-Point), phần dư KKT, hướng tìm kiếm kết hợp và kỹ thuật giải hệ tuyến tính khối KKT hiệu năng cao."
---

Trong phương pháp hàm chắn logarit (Barrier Method), mỗi giá trị của tham số chắn dẫn đến một bài toán định tâm. Ta phải chọn độ chính xác của bài toán này trước khi tăng tham số và giải tiếp. Có thể cập nhật cả nghiệm và các nhân tử Lagrange trong cùng một bước Newton hay không?

Phương pháp điểm trong nguyên thủy - đối ngẫu (**Primal-Dual Interior-Point Method**) thực hiện ý tưởng đó. Thuật toán cập nhật đồng thời biến nguyên thủy $x$ và các nhân tử đối ngẫu $\lambda, \nu$ bằng cách tuyến tính hóa hệ điều kiện KKT. Với dạng trình bày trong bài này, điểm xuất phát vẫn cần $f_i(x)<0$ và $\lambda_i>0$. Tuy nhiên, nó có thể chưa thỏa mãn ràng buộc đẳng thức hoặc điều kiện triệt tiêu gradient Lagrange.

---

## 1. Hệ Điều Kiện KKT Bị Xáo Trộn và Độ Lệch Đối Ngẫu Đại Diện

Xét bài toán tối ưu lồi tổng quát:

$$
\begin{aligned}
&\min_{x} \quad f_0(x)\\
&\text{s.t.} \quad f_i(x) \le 0, \quad i = 1, \dots, m,\\
& A x = b,
\end{aligned}
$$

trong đó $f_0, f_1, \dots, f_m: \mathbb{R}^n \to \mathbb{R}$ là các hàm lồi khả vi liên tục hai lần, và ma trận $A \in \mathbb{R}^{p \times n}$ có hạng đủ $\operatorname{rank}(A) = p$.

Hệ điều kiện KKT của bài toán gồm bốn nhóm dưới đây. Với bài toán lồi, một điểm thỏa mãn hệ này là nghiệm tối ưu. Chiều ngược lại cần điều kiện chính quy thích hợp, chẳng hạn điều kiện Slater.

1. **Khả thi nguyên thủy**: Biểu thức $f_i(x^*) \le 0$ với mọi $i = 1, \dots, m$ và $A x^* = b$.
2. **Khả thi đối ngẫu**: Điều kiện $\lambda_i^* \ge 0$ với mọi $i = 1, \dots, m$.
3. **Triệt tiêu gradient Lagrange**: Ta có $\nabla f_0(x^*) + Df(x^*)^T \lambda^* + A^T \nu^* = 0$.
4. **Bù trừ tương hỗ**: Tích $\lambda_i^* f_i(x^*) = 0$ với mọi $i = 1, \dots, m$.

### Hệ KKT bị xáo trộn (Perturbed KKT Conditions)

Thay vì giải trực tiếp điều kiện bù trừ $\lambda_i f_i(x) = 0$, ta đặt tích $-\lambda_i f_i(x)$ bằng một đại lượng dương $\eta = 1/t > 0$.

Đặt $h$ là tổng có trọng số của các gradient ràng buộc:

$$
h = \sum_{i=1}^m \lambda_i \nabla f_i(x).
$$

Để thấy rõ phép cộng này, đặt $v_i=\lambda_i\nabla f_i(x)$. Khi có hai ràng buộc, $h=v_1+v_2$. Trong trường hợp tổng quát:

$$
h = v_1+v_2+\dots+v_m.
$$

$$
\begin{aligned}
&\nabla f_0(x) + h + A^T \nu = 0, \\
&-\lambda_i f_i(x) = \eta, \\
&A x = b.
\end{aligned}
$$
Phương trình bù trừ được áp dụng với mọi $i = 1, \dots, m$, đồng thời $f_i(x) < 0$ và $\lambda_i > 0$.

Họ nghiệm của hệ này, khi tồn tại và $\eta>0$ thay đổi, tạo thành **đường trung tâm nguyên thủy - đối ngẫu** (Primal-Dual Central Path). Mỗi điểm trên đường trung tâm có khoảng cách đối ngẫu bằng $m\eta$. Khi $\eta\to0$, khoảng cách đó tiến về $0$. Nếu họ nghiệm có điểm tụ hữu hạn, mỗi điểm tụ thỏa mãn hệ KKT và cho nghiệm tối ưu của bài toán gốc.

### Độ lệch đối ngẫu đại diện (Surrogate Duality Gap)

Một điểm $(x, \lambda, \nu)$ thỏa mãn $f_i(x)<0$ và $\lambda_i>0$ có thể chưa thỏa mãn $Ax=b$ hoặc điều kiện triệt tiêu gradient Lagrange. Khi đó, tổng các tích bù trừ chưa chắc bằng khoảng cách đối ngẫu. Ta dùng giá trị trung bình của chúng làm **độ lệch đối ngẫu đại diện**:

$$
\begin{aligned}
\hat{\eta}(x, \lambda)
&= -\frac{1}{m} \sum_{i=1}^m \lambda_i f_i(x) \\
&= -\frac{1}{m} \lambda^T f(x).
\end{aligned}
$$

Đặt $u_i = -\lambda_i f_i(x)$ là tích bù trừ dương của ràng buộc thứ $i$. Khi có hai ràng buộc, $2\hat{\eta} = u_1 + u_2$. Với $m$ ràng buộc, khai triển tường minh cho ta:

$$
m\hat{\eta} = u_1 + u_2 + \dots + u_m.
$$

Đại lượng $\hat{\eta}(x, \lambda)$ đo lường mức độ vi phạm trung bình của điều kiện bù trừ tương hỗ. Nếu điểm đang xét khả thi nguyên thủy và thỏa mãn điều kiện triệt tiêu gradient Lagrange, khoảng cách đối ngẫu bằng $m\hat{\eta}(x,\lambda)$. Điều kiện gradient bảo đảm $x$ đạt giá trị nhỏ nhất của hàm Lagrange vì hàm này lồi theo $x$.

---

## 2. Các Vector Phần Dư KKT

Để đo lường mức độ thỏa mãn hệ điều kiện KKT bị xáo trộn tại điểm hiện tại $(x, \lambda, \nu)$, ta chia sai số thành ba thành phần phần dư:

Ký hiệu $J = Df(x)$ là ma trận Jacobi, gồm các gradient ràng buộc viết theo hàng:

$$
J = \begin{bmatrix}
\nabla f_1(x)^T \\
\vdots \\
\nabla f_m(x)^T
\end{bmatrix}.
$$

Ta có $J \in \mathbb{R}^{m \times n}$. Đồng thời, đặt $\Lambda = \operatorname{diag}(\lambda)$ và $\eta = 1/t$ để viết gọn các biểu thức dưới đây.

1. **Phần dư đối ngẫu (Dual residual)**:
   $$
   r_d = \nabla f_0(x) + J^T \lambda + A^T \nu,
   $$
   trong đó $r_d$ viết tắt cho $r_{\text{dual}}(x, \lambda, \nu)$ và $r_d \in \mathbb{R}^n$.

2. **Phần dư bù trừ trung tâm (Centering residual)**:
   $$
   r_c = -\Lambda f(x) - \eta\mathbf{1},
   $$
   trong đó $r_c$ viết tắt cho $r_{\text{cent}}(x, \lambda)$ và $r_c \in \mathbb{R}^m$. Ma trận $\Lambda$ có các phần tử đường chéo $\lambda_1, \dots, \lambda_m$, còn $\mathbf{1} = (1, \dots, 1)^T$. Thành phần thứ $i$ của vector này là:
   $$
   (r_c)_i = -\lambda_i f_i(x) - \eta.
   $$

3. **Phần dư nguyên thủy (Primal residual)**:
   $$
   r_p = A x - b.
   $$
   Ký hiệu $r_p$ viết tắt cho $r_{\text{pri}}(x)$ và $r_p \in \mathbb{R}^p$.

Gộp ba phần dư thành vector tổng thể $r(x, \lambda, \nu) \in \mathbb{R}^{n + m + p}$:

$$
r(x, \lambda, \nu) = \begin{bmatrix} r_d \\ r_c \\ r_p \end{bmatrix}.
$$

Hệ phương trình KKT bị xáo trộn tương đương với phương trình phi tuyến $r(x, \lambda, \nu) = 0$.

---

## 3. Hướng Tìm Kiếm Primal-Dual và Phương Pháp Newton

Để tìm bước cập nhật, gom các biến vào vector $z = (x, \lambda, \nu)$ và đặt:

$$
\Delta z = \begin{bmatrix}
\Delta x \\
\Delta \lambda \\
\Delta \nu
\end{bmatrix}.
$$

Ta áp dụng xấp xỉ tuyến tính Taylor bậc nhất cho hệ phi tuyến $r(z + \Delta z) = 0$:

$$
\begin{aligned}
r(z + \Delta z)
&\approx r(z) + \nabla r(z)\Delta z \\
&= 0.
\end{aligned}
$$

Đặt $F = \operatorname{diag}(f(x))$. Lấy đạo hàm từng khối của $r$ theo $(x, \lambda, \nu)$, ta thu được ma trận KKT khối:

$$
K = \begin{bmatrix}
H & J^T & A^T \\
-\Lambda J & -F & 0 \\
A & 0 & 0
\end{bmatrix}.
$$

Hướng tìm kiếm là nghiệm của hệ tuyến tính:

$$
K\Delta z = -r(z),
$$

trong đó ma trận Hessian kết hợp $H \in \mathbb{R}^{n \times n}$ được xác định bởi:

$$
H = \nabla^2 f_0(x) + \sum_{i=1}^m \lambda_i \nabla^2 f_i(x).
$$

Do tính lồi của các hàm $f_i$ và điều kiện $\lambda_i > 0$, ma trận $H$ luôn nửa xác định dương. Nếu một Hessian thành phần xác định dương tại điểm đang xét và có hệ số dương, thì $H$ xác định dương tại điểm đó.

### Phân rã hướng Affine-Scaling và Hướng Centering

Trong thực tế, ta thường chọn tham số đích $1/t = \sigma \hat{\eta}$, với $\sigma \in [0, 1]$ được gọi là **tham số định tâm** (Centering parameter):

- Khi $\sigma = 0$: Tham số $1/t = 0$, hướng tìm kiếm thuần túy nhằm triệt tiêu phần dư và giảm khoảng cách đối ngẫu về 0. Hướng này gọi là **hướng affine-scaling** (Affine-scaling direction).
- Khi $\sigma = 1$: Giá trị đích của từng tích bù trừ bằng giá trị trung bình hiện tại. Hướng Newton vì vậy điều chỉnh sự chênh lệch giữa các tích này, đồng thời giảm các phần dư còn lại.
- Trong quy hoạch tuyến tính, thuật toán **Mehrotra Predictor-Corrector** tính hướng dự đoán affine-scaling rồi dùng bước dự đoán để chọn $\sigma$. Lần giải hệ tiếp theo bổ sung số hạng hiệu chỉnh bậc hai. Số hạng này đến từ tích các biến thiên của nhân tử đối ngẫu và biến bù tương ứng, không phải tích hai thành phần bất kỳ của $\Delta\lambda$ và $\Delta x$.

---

## 4. Chiến Lược Bước Nhảy và Line Search Backtracking

Sau khi tính được hướng tìm kiếm $(\Delta x, \Delta \lambda, \Delta \nu)$, ta cần chọn độ dài bước nhảy $s > 0$ sao cho:

1. Biến đối ngẫu vẫn giữ dương nghiêm ngặt: $\lambda + s \Delta \lambda > 0$.
2. Biến nguyên thủy vẫn nằm trong miền xác định và thỏa mãn bất đẳng thức nghiêm ngặt: $f_i(x + s \Delta x) < 0$.
3. Chuẩn của vector phần dư $\|r(x, \lambda, \nu)\|_2$ giảm đáng kể.

### Xác định cận trên bước nhảy $s_{\max}$

Đầu tiên, ta chặn bước nhảy đối ngẫu để đảm bảo $\lambda_i + s \Delta \lambda_i > 0$. Đặt tập các bước vẫn giữ được tính không âm:

$$
\mathcal S = \{s \in [0,1] \mid \lambda + s\Delta\lambda \ge 0\}.
$$

Chỉ những thành phần đang giảm mới chặn bước. Ký hiệu $I_d$ là tập các chỉ số có $\Delta\lambda_i < 0$, khi đó:

$$
\begin{aligned}
s_{\max}^{\text{dual}}
&= \sup\mathcal S \\
&= \min\left(1,\min_{i\in I_d}\frac{-\lambda_i}{\Delta\lambda_i}\right).
\end{aligned}
$$

Tương tự, với các hàm ràng buộc bất đẳng thức (nếu là hàm tuyến tính $f_i(x) = a_i^T x - b_i$), ta có thể tính chính xác:

$$
s_{\max}^{\text{pri}} = \min\left(1,\min_{i\in I_p}\frac{-f_i(x)}{a_i^T\Delta x}\right).
$$

Ở đây $I_p$ gồm các chỉ số có $a_i^T\Delta x > 0$. Nếu $I_d$ hoặc $I_p$ rỗng, lấy giá trị phép lấy min bên trong tương ứng bằng $+\infty$, vì không có thành phần nào chặn bước.

Để tránh điểm chạm vào biên quá sớm, ta đặt cận bước khởi tạo:

$$
s_{\max} = 0.99 \min \left( s_{\max}^{\text{pri}}, s_{\max}^{\text{dual}} \right).
$$

### Thuật toán Line Search theo chuẩn phần dư

Bắt đầu với $s = s_{\max}$, ta thực hiện co bước $s := \beta s$ ($\beta \in (0.5, 0.8)$) cho đến khi thỏa mãn hai điều kiện:

1. Tính khả thi miền trong: Điểm $x + s \Delta x \in \mathbf{dom} f_0$ và $f_i(x + s \Delta x) < 0$ với mọi $i = 1, \dots, m$.
2. Điều kiện giảm chuẩn phần dư Armijo:
   $$
   \|r(z + s\Delta z)\|_2 \le (1 - \alpha s)\|r(z)\|_2,
   $$
   với tham số $\alpha \in (0.01, 0.1)$.

Trong quá trình tìm bước này, tham số đích $\eta$ được giữ cố định để hai chuẩn phần dư đo cùng một hệ phương trình.

---

## 5. Kỹ Thuật Số Học Giải Hệ Tuyến Tính Khối KKT

Hệ phương trình KKT ở Mục 3 có kích thước lớn $(n + m + p) \times (n + m + p)$ và không đối xứng do phương trình thứ hai. Việc giải trực tiếp hệ này rất tốn kém. Trong thực tế tính toán, ta luôn thực hiện kỹ thuật **khử biến** để đưa về hệ đối xứng nhỏ hơn.

### Khử biến đối ngẫu $\Delta \lambda$

Từ phương trình thứ hai trong hệ KKT:

$$
-\Lambda J\Delta x - F\Delta\lambda = -r_c.
$$

Vì $f_i(x) < 0$ với mọi $i$, ma trận đường chéo $F$ khả nghịch. Chuyển vế rồi nhân với $F^{-1}$, ta rút được $\Delta\lambda$ theo $\Delta x$:

$$
\Delta\lambda = F^{-1}(r_c - \Lambda J\Delta x).
$$

Khai triển cho từng tọa độ, đặt $d_i = \nabla f_i(x)^T\Delta x$ là biến thiên tuyến tính của ràng buộc thứ $i$:

$$
\begin{aligned}
\Delta\lambda_i
&= \frac{(r_c)_i - \lambda_i d_i}{f_i(x)} \\
&= \frac{-\lambda_i f_i(x) - \eta - \lambda_i d_i}{f_i(x)}.
\end{aligned}
$$

### Hệ KKT rút gọn đối xứng

Đặt vector trung gian $u$ và ma trận trọng số đường chéo $D$ như sau:

$$
u = F^{-1}r_c, \qquad D = -F^{-1}\Lambda.
$$

Các phần tử trên đường chéo của $D$ được xác định bởi:

$$
D_{ii} = -\frac{\lambda_i}{f_i(x)} > 0.
$$

Tính dương này đến từ $\lambda_i > 0$ và $f_i(x) < 0$. Biểu thức vừa rút cho hướng đối ngẫu trở thành:

$$
\Delta\lambda = u + DJ\Delta x.
$$

Để thế vào phương trình thứ nhất mà vẫn nhìn rõ từng khối, đặt $v = J^T\Delta\lambda$. Khi đó:

$$
v = J^Tu + J^TDJ\Delta x.
$$

Phương trình thứ nhất là:

$$
H\Delta x + v + A^T\Delta\nu = -r_d.
$$

Gộp các số hạng chứa $\Delta x$, ta đặt ma trận Hessian hiệu dụng và vector vế phải:

$$
H_{\text{eff}} = H + J^TDJ,
$$

$$
g = r_d + J^Tu.
$$

Như vậy, phương trình sau khi khử là:

$$
H_{\text{eff}}\Delta x + A^T\Delta\nu = -g.
$$

Ta luôn có $H_{\text{eff}}\succeq0$. Để bảo đảm $H_{\text{eff}}\succ0$, cần thêm điều kiện $\ker(H)\cap\ker(J)=\{0\}$, chẳng hạn $H\succ0$ hoặc $J$ có hạng cột đầy đủ. Bài tập 2 chứng minh điều kiện này trong trường hợp toàn phương.

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
g \\
r_p
\end{bmatrix}.
$$

Hệ phương trình này là hệ KKT đối xứng kinh điển, có thể giải bằng một trong hai phương án hiệu năng cao:

1. **Khử khối ma trận Schur**: Khi $H_{\text{eff}}\succ0$ và $p$ nhỏ hơn nhiều so với $n$, ta tính phân tích Cholesky $H_{\text{eff}} = L L^T$. Đặt ma trận bù Schur và vector vế phải:
   $$
   S_A = A H_{\text{eff}}^{-1} A^T,
   $$
   $$
   b_A = r_p - A H_{\text{eff}}^{-1}g.
   $$
   Sau đó giải hệ kích thước $p\times p$:
   $$
   S_A\Delta\nu = b_A.
   $$
2. **Phân tích $LDL^T$ không xác định đối xứng**: Khi ma trận $A$ có cấu trúc thưa lớn, ta giải trực tiếp hệ khối $(n + p) \times (n + p)$ bằng thuật toán $LDL^T$ với kỹ thuật xoay trục đường chéo (Bunch-Kaufman pivoting).

---

## 6. So Sánh Hiệu Năng: Barrier Method và Primal-Dual

Bảng dưới đây tổng kết sự khác biệt cốt lõi giữa hai họ phương pháp điểm trong:

| Tiêu chí | Phương pháp Hàm chắn (Barrier Method) | Phương pháp Primal-Dual |
| :--- | :--- | :--- |
| **Khởi tạo nghiệm** | Dạng cơ bản cần khả thi nghiêm ngặt, có thể tìm bằng Pha I | Dạng trong bài vẫn cần $f_i(x)<0$, nhưng cho phép phần dư đẳng thức và đối ngẫu khác $0$ |
| **Số vòng lặp** | Hai tầng (vòng lặp ngoài cập nhật $t$, vòng lặp trong chạy Newton) | Một tầng duy nhất (cập nhật đồng thời $x, \lambda, \nu$) |
| **Cơ chế giảm sai số** | Giải bài toán định tâm theo từng giá trị $t$ | Tính hướng Newton cho đồng thời các phần dư KKT |
| **Tham số điều khiển** | Hệ số tăng $t$ và độ chính xác của bước định tâm | Tham số định tâm $\sigma$ và quy tắc chọn bước |
| **Ổn định số** | Hessian có thể kém điều kiện khi tiến gần biên | Hệ KKT cũng có thể kém điều kiện và cần xử lý số thích hợp |

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
   &c - s + A^T\nu = 0, \\
   &XS\mathbf{1} = \eta\mathbf{1}, \\
   &Ax = b, \\
   &x > 0, \quad s > 0.
   \end{aligned}
   $$
   Ba phương trình lần lượt thể hiện tính khả thi đối ngẫu, điều kiện định tâm và tính khả thi nguyên thủy. Ở đây $X = \operatorname{diag}(x)$ và $S = \operatorname{diag}(s)$, với các phần tử đường chéo tương ứng là $x_1,\dots,x_n$ và $s_1,\dots,s_n$.

2. Các vector phần dư tại điểm hiện tại $(x, s, \nu)$:
   $$
   \begin{aligned}
   r_d &= c - s + A^T \nu, \\
   r_c &= X S \mathbf{1} - \eta \mathbf{1}, \\
   r_p &= A x - b.
   \end{aligned}
   $$

   Ta tiếp tục dùng $r_d$, $r_c$, $r_p$ cho ba phần dư tương ứng. Tuyến tính hóa hệ phương trình tại bước lặp hiện tại, ta được ma trận khối:
   $$
   K_{\mathrm{LP}} = \begin{bmatrix}
   0 & -I & A^T \\
   S & X & 0 \\
   A & 0 & 0
   \end{bmatrix}.
   $$
   Đặt $\Delta z_{\mathrm{LP}} = (\Delta x,\Delta s,\Delta\nu)$. Hệ xác định hướng là:
   $$
   K_{\mathrm{LP}}\Delta z_{\mathrm{LP}}
   = -\begin{bmatrix}
   r_d \\
   r_c \\
   r_p
   \end{bmatrix}.
   $$

3. Từ phương trình thứ hai: $S\Delta x + X\Delta s = -r_c$. Vì $x_i > 0$, ma trận $X$ khả nghịch hoàn toàn, suy ra:
   $$
   \Delta s = -X^{-1}r_c - X^{-1}S\Delta x.
   $$

   Thế $\Delta s$ vào phương trình thứ nhất:
   $$
   -\Delta s + A^T\Delta\nu = -r_d.
   $$
   Sau phép thế, phương trình tương đương là:
   $$
   X^{-1}S\Delta x + A^T\Delta\nu = -r_d - X^{-1}r_c.
   $$

   Đặt ma trận đường chéo $\Theta = S^{-1} X \succ 0$ với $\Theta_{ii} = x_i / s_i$. Nhân cả hai vế với $\Theta$:
   $$
   \Delta x + \Theta A^T\Delta\nu = -\Theta r_d - S^{-1}r_c.
   $$

   Đặt $q = \Theta r_d + S^{-1}r_c$. Nhân ma trận $A$ vào hai vế và kết hợp với phương trình thứ ba $A\Delta x = -r_p$, ta thu được phương trình chuẩn xác định $\Delta\nu$:
   $$
   (A\Theta A^T)\Delta\nu = r_p - Aq.
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
   trong đó $D$ là ma trận đường chéo với:
   $$
   D_{ii} = -\frac{\lambda_i}{g_i^Tx-h_i}.
   $$

   Do tính khả thi miền trong, ta luôn có $\lambda_i > 0$ và $g_i^T x - h_i < 0$, dẫn đến $D_{ii} > 0$ với mọi $i = 1, \dots, m$.

2. Để chứng minh $H_{\text{eff}} \succ 0$, ta xét dạng toàn phương $v^T H_{\text{eff}} v$ với một vector bất kỳ $v \in \mathbb{R}^n$:
   $$
   v^T H_{\text{eff}} v = v^T P v + v^T G^T D G v.
   $$

   Vì $P \succeq 0$, ta có $v^T P v \ge 0$.

   Vì $D$ là ma trận đường chéo với các phần tử dương nghiêm ngặt $D_{ii} > 0$, đặt $w = G v \in \mathbb{R}^m$, ta có:
   $$
   \begin{aligned}
   v^TG^TDGv &= w^TDw \\
   &= \sum_{i=1}^m D_{ii}w_i^2 \\
   &\ge 0.
   \end{aligned}
   $$

   Do đó $v^T H_{\text{eff}} v \ge 0$.

   Bây giờ, giả sử $v^T H_{\text{eff}} v = 0$. Vì cả hai số hạng đều không âm, đẳng thức xảy ra khi và chỉ khi:
   $$
   v^T P v = 0 , \quad w^T D w = 0.
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
     \begin{aligned}
     r_d &= f_0'(x) + \lambda f_1'(x) \\
     &= 1 + (1)(-1) \\
     &= 0.
     \end{aligned}
     $$
     (Điểm hiện tại đã thỏa mãn cân bằng đối ngẫu).
   - Phần dư bù trừ trung tâm:
     $$
     \begin{aligned}
     r_c &= -\lambda f_1(x) - \eta \\
     &= -(1)(-2) - 1 \\
     &= 2 - 1 = 1.
     \end{aligned}
     $$
   - Phần dư nguyên thủy: Không có ràng buộc đẳng thức nên $r_p = 0$.

3. Thiết lập hệ phương trình KKT:
   - Hessian $H = f_0''(x) + \lambda f_1''(x) = 0 + 0 = 0$.
   - Ma trận Jacobi $Df(x) = [-1]$.
   
   Thay các giá trị vào ma trận hệ số:
   $$
   K = \begin{bmatrix}
   0 & -1 \\
   -(1)(-1) & -(-2)
   \end{bmatrix}.
   $$

   Rút gọn các hệ số, ta thu được hệ tương đương:
   $$
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
   - Với biến nguyên thủy: Điều kiện miền trong là $2-s>0$, tương đương $s<2$. Kết hợp với giới hạn $s\le1$, ta có $s_{\max}^{\text{pri}}=1$.
   - Theo hệ số an toàn ở Mục 4, bước khởi tạo là $s_{\max}=0.99$. Bước $s=0.8$ nhỏ hơn cận này và giữ được tính dương của cả hai biến.
   
   Cập nhật với bước $s = 0.8$:
   $$
   \begin{aligned}
   x_{\text{new}} &= x + s\Delta x \\
   &= 2 + 0.8(-1) = 1.2, \\
   \lambda_{\text{new}} &= \lambda + s\Delta\lambda \\
   &= 1 + 0.8(0) = 1.
   \end{aligned}
   $$

   Kiểm tra độ lệch đối ngẫu đại diện mới:
   $$
   \begin{aligned}
   \hat{\eta}_{\text{new}} &= -\lambda_{\text{new}}f_1(x_{\text{new}}) \\
   &= -(1)(-1.2) = 1.2.
   \end{aligned}
   $$

   Khoảng cách đối ngẫu đã giảm từ $2$ xuống còn $1.2$, đưa điểm lặp tiến gần hơn về nghiệm tối ưu $x^* = 0$.

---

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
- Jorge Nocedal, Stephen J. Wright, *Numerical Optimization*, Springer.
