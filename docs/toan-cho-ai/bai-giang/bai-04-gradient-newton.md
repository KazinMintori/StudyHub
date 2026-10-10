---
course: toan-cho-ai
lecture: bai-04-gradient-newton
section: lecture
title: "Tối ưu không ràng buộc và ràng buộc đẳng thức"
prerequisites: ["gradient", "hessian", "ma-tran-psd", "he-phuong-trinh", "kkt"]
lessonStatus: ready
description: "Khảo sát toàn diện các thuật toán tối ưu hóa liên tục: Phương pháp dốc nhất theo các chuẩn, tìm kiếm bước Backtracking, phương pháp Newton, hệ Newton-KKT, hàm tự tương hợp, và phương pháp điểm trong (Barrier, Central Path, Primal-Dual)."
---

Các bài giảng trước đã trang bị cho chúng ta hệ thống điều kiện toán học để nhận diện và chứng nhận một nghiệm tối ưu. Bài giảng này chuyển giao trọng tâm từ lý thuyết nhận diện sang bài toán thuật toán tính toán: Bắt đầu từ một điểm khởi tạo tùy ý trong không gian, làm thế nào để xây dựng một dãy điểm lặp hội tụ nhanh chóng, chính xác và ổn định về nghiệm tối ưu toàn cục?

Quá trình tìm đường trong không gian tối ưu hóa đòi hỏi thuật toán phải đưa ra ba quyết định độc lập tại mỗi bước lặp:
1. **Chọn hướng di chuyển** (Descent Direction): Đi theo vector nào để hàm mục tiêu suy giảm?
2. **Chọn độ dài bước** (Step Size / Learning Rate): Di chuyển bao xa theo hướng đã chọn để không bị vọt qua đáy thung lũng?
3. **Tiêu chí dừng** (Stopping Criteria): Khi nào mức độ tiệm cận nghiệm đã đủ tin cậy để dừng tính toán?

Chúng ta sẽ khảo sát một phổ rộng các thuật toán: Từ phương pháp dốc nhất theo các chuẩn khác nhau ($L_2, L_1, L_\infty$), kỹ thuật tìm kiếm bước Backtracking (Armijo), phương pháp Newton bậc hai và đại lượng Newton decrement, mở rộng sang tối ưu ràng buộc đẳng thức qua hệ Newton–KKT, lý thuyết hàm tự tương hợp Nesterov–Nemirovski, và đỉnh cao là **Phương pháp điểm trong (Interior-Point Methods)**, cỗ máy giải các bài toán tối ưu lồi tổng quát có ràng buộc bất đẳng thức.

---

## 1. Hướng giảm và Độ dài bước di chuyển

Tại điểm hiện tại $x \in \mathbb{R}^n$, thuật toán lặp cập nhật vị trí mới theo quy tắc:

$$
x^+ = x + t \Delta x,
$$

trong đó $\Delta x \in \mathbb{R}^n$ là vector hướng di chuyển và $t > 0$ là độ dài bước nhảy.

Đạo hàm định hướng của hàm số $f$ dọc theo tia $t \mapsto f(x + t \Delta x)$ tại $t = 0$ được tính bằng tích vô hướng $\nabla f(x)^T \Delta x$. Một vector $\Delta x$ được gọi là **hướng giảm** (descent direction) nếu tích vô hướng này âm:

$$
\nabla f(x)^T \Delta x < 0.
$$

Khi điều kiện này thỏa mãn, giải tích bảo đảm rằng luôn tồn tại một bước nhảy $t > 0$ đủ nhỏ sao cho $f(x + t \Delta x) < f(x)$.

---

## 2. Phương pháp dốc nhất theo các chuẩn khác nhau (Steepest Descent)

Khái niệm "hướng dốc nhất" phụ thuộc trực tiếp vào cách chúng ta đo lường độ dài của một bước di chuyển. Với một chuẩn tổng quát $\|\cdot\|$ trên $\mathbb{R}^n$, hướng dốc nhất chuẩn hóa (normalized steepest descent direction) được định nghĩa là hướng làm cho đạo hàm định hướng âm nhất trên quả cầu đơn vị của chuẩn đó:

$$
\Delta x_{\mathrm{nsd}} = \arg\min_{v} \left\{ \nabla f(x)^T v \mid \|v\| \le 1 \right\}.
$$

Hướng dốc nhất chưa chuẩn hóa (unnormalized steepest descent direction) được tỷ lệ hóa theo độ lớn của gradient: $\Delta x_{\mathrm{sd}} = \|\nabla f(x)\|_* \Delta x_{\mathrm{nsd}}$, trong đó $\|\cdot\|_*$ là chuẩn đối ngẫu.

### 2.1. Chuẩn Euclid ($L_2$): Phương pháp Gradient Descent cổ điển
Khi sử dụng chuẩn Euclid $\|v\|_2 = \sqrt{v^T v}$, bất đẳng thức Cauchy–Schwarz khẳng định:

$$
\nabla f(x)^T v \ge -\|\nabla f(x)\|_2 \|v\|_2 = -\|\nabla f(x)\|_2.
$$

Đẳng thức đạt được khi và chỉ khi $v$ chỉ ngược chiều với gradient:

$$
\Delta x_{\mathrm{nsd}} = -\frac{\nabla f(x)}{\|\nabla f(x)\|_2}, \qquad \Delta x_{\mathrm{sd}} = -\nabla f(x).
$$

Đây chính là thuật toán **Gradient Descent**: Di chuyển thẳng theo hướng ngược chiều vector gradient.

### 2.2. Chuẩn toàn phương: Mối liên hệ với Phương pháp Newton
Xét chuẩn toàn phương xác định bởi ma trận đối xứng dương xác định $P \succ 0$: $\|v\|_P = (v^T P v)^{1/2}$. Hướng dốc nhất theo chuẩn này là:

$$
\Delta x_{\mathrm{sd}} = -P^{-1} \nabla f(x).
$$

Khi ta chọn $P = \nabla^2 f(x)$ (ma trận Hessian tại điểm hiện tại), hướng dốc nhất theo chuẩn địa phương này trở thành:

$$
\Delta x_{\mathrm{nt}} = -[\nabla^2 f(x)]^{-1} \nabla f(x).
$$

Đây chính là **hướng Newton**! Kết quả này cho thấy một trực giác sâu sắc: Phương pháp Newton thực chất chính là phương pháp dốc nhất, nhưng được đo lường trong hệ chuẩn elip tự nhiên tạo bởi độ cong Hessian tại từng điểm.

### 2.3. Chuẩn $L_1$: Phương pháp Tọa độ (Coordinate Descent)
Với chuẩn $\|v\|_1 = \sum |v_i|$, quả cầu đơn vị là một khối bát diện đều (cross-polytope). Giá trị nhỏ nhất của $\nabla f(x)^T v$ đạt được tại một trong các đỉnh của quả cầu đơn vị, tức là tại tọa độ $i^*$ có trị tuyệt đối đạo hàm riêng lớn nhất:

$$
i^* = \arg\max_{i=1,\dots,n} |(\nabla f(x))_i|.
$$

Hướng dốc nhất theo chuẩn $L_1$ chỉ dịch chuyển duy nhất trên tọa độ $i^*$:

$$
\Delta x_{\mathrm{nsd}} = -\operatorname{sign}\left(\frac{\partial f(x)}{\partial x_{i^*}}\right) e_{i^*}.
$$

Đây chính là phương pháp **Coordinate Descent (Hạ dốc theo tọa độ)**: Mỗi bước chỉ cập nhật đúng một tham số nhạy cảm nhất.

### 2.4. Chuẩn $L_\infty$: Bước đi hình hộp
Với chuẩn cực đại $\|v\|_\infty = \max |v_i|$, quả cầu đơn vị là khối siêu lập phương $[-1, 1]^n$. Hướng dốc nhất đạt được tại một đỉnh của khối lập phương:

$$
(\Delta x_{\mathrm{nsd}})_i = -\operatorname{sign}\left(\frac{\partial f(x)}{\partial x_i}\right) \quad \forall i = 1, \dots, n.
$$

Mỗi tọa độ đều di chuyển một bước có độ dài cố định $\pm 1$ tùy theo dấu của gradient.

---

## 3. Tìm kiếm bước bằng thuật toán Backtracking (Điều kiện Armijo)

Trong thực tế tính toán, việc tìm kiếm độ dài bước tối ưu chính xác (exact line search) đòi hỏi giải một bài toán tối ưu phụ một chiều rất tốn kém. Kỹ thuật **Backtracking Line Search** tìm kiếm một bước nhảy chấp nhận được với chi phí cực thấp.

Thuật toán chọn hai tham số: $\alpha \in (0, 0.5)$ (hệ số giảm chấp nhận được) và $\beta \in (0, 1)$ (hệ số thu nhỏ bước). Bắt đầu với bước thử $t = 1$, ta liên tục co ngắn bước $t \leftarrow \beta t$ cho tới khi điểm thử nghiệm nằm trong miền xác định và thỏa mãn **điều kiện Armijo**:

$$
f(x + t \Delta x) \le f(x) + \alpha t \nabla f(x)^T \Delta x.
$$

Ý nghĩa hình học: Vì $\nabla f(x)^T \Delta x < 0$, vế phải là một đường thẳng xấp xỉ tuyến tính dốc xuống với độ dốc bằng một tỷ lệ $\alpha$ so với độ dốc thực tế. Điều kiện yêu cầu hàm mục tiêu phải thực sự giảm ít nhất một tỷ lệ $\alpha$ so với mức giảm kỳ vọng tuyến tính.

```python
def backtracking_line_search(f, grad_f, x, dx, alpha=0.1, beta=0.5):
    """Tìm độ dài bước nhảy thỏa mãn điều kiện Armijo."""
    t = 1.0
    slope = grad_f(x).dot(dx)
    while f(x + t * dx) > f(x) + alpha * t * slope:
        t *= beta
    return t
```

---

## 4. Phương pháp Newton và Mô hình xấp xỉ bậc hai

### 4.1. Hướng Newton và Đại lượng Newton Decrement
Phương pháp Newton khai thác thông tin độ cong của ma trận Hessian $H = \nabla^2 f(x) \succ 0$. Tại điểm hiện tại, phương pháp Newton dựng một mô hình xấp xỉ Taylor bậc hai theo vector độ dời $v$:

$$
q(v) = f(x) + \nabla f(x)^T v + \frac{1}{2} v^T \nabla^2 f(x) v.
$$

Cực tiểu hóa mô hình toàn phương này dẫn tới hệ phương trình Newton:

$$
\nabla_v q(v) = \nabla f(x) + \nabla^2 f(x) v = 0 \iff \boxed{\nabla^2 f(x) \Delta x_{\mathrm{nt}} = -\nabla f(x).}
$$

Trong phương pháp Newton, đại lượng **Newton decrement** $\lambda(x)$ được định nghĩa là:

$$
\lambda(x) = \left( \nabla f(x)^T [\nabla^2 f(x)]^{-1} \nabla f(x) \right)^{1/2} = \left( \Delta x_{\mathrm{nt}}^T \nabla^2 f(x) \Delta x_{\mathrm{nt}} \right)^{1/2}.
$$

Đại lượng này mang ba ý nghĩa toán học đặc biệt:
1. **Ước lượng độ giảm mục tiêu**: Đại lượng $\frac{1}{2}\lambda(x)^2$ chính là mức độ suy giảm hàm mục tiêu mà mô hình xấp xỉ bậc hai dự đoán:
   $$
   f(x) - \inf_v q(v) = \frac{1}{2} \lambda(x)^2.
   $$
2. **Tính bất biến Affine**: Khác với gradient norm $\|\nabla f(x)\|_2$ (vốn thay đổi mạnh khi đổi hệ đơn vị đo), đại lượng $\lambda(x)$ hoàn toàn **bất biến dưới mọi phép đổi tọa độ affine tuyến tính** ($x = T y$).
3. **Tiêu chí dừng chuẩn xác**: Khi $\frac{1}{2}\lambda(x)^2 \le \epsilon$, ta dừng thuật toán với bảo đảm chắc chắn rằng sai số mục tiêu không vượt quá $\epsilon$.

### 4.2. Tốc độ hội tụ hai pha của Phương pháp Newton
Phương pháp Newton có hai pha hội tụ phân biệt rõ rệt:
1. **Pha giảm chậm (Damped Newton phase)**: Khi điểm bắt đầu ở xa nghiệm, $\lambda(x) \ge \gamma$. Mỗi bước lặp làm hàm mục tiêu giảm ít nhất một đại lượng hằng số hữu hạn $\gamma > 0$. Số bước lặp trong pha này bị chặn trên bởi:
   $$
   \frac{f(x^{(0)}) - p^*}{\gamma}.
   $$
2. **Pha hội tụ bậc hai (Quadratic convergence phase)**: Khi $\lambda(x) < \gamma$ (bước vào lân cận nghiệm), thuật toán luôn chọn bước đầy đủ $t = 1$. Sai số suy giảm với tốc độ bậc hai:
   $$
   \lambda(x^{(k+1)}) \le c \lambda(x^{(k)})^2.
   $$
   Tại pha này, số chữ số thập phân chính xác của nghiệm tăng gấp đôi sau mỗi bước lặp! Thông thường chỉ cần từ 5 đến 6 bước lặp Newton trong pha này để đạt độ chính xác máy tối đa.

---

## 5. Hàm tự tương hợp (Self-concordant Functions)

Một thách thức kinh điển của giải tích tối ưu truyền thống là tốc độ hội tụ của phương pháp Newton phụ thuộc vào các hằng số độ cong không xác định trong từng hệ tọa độ. Yurii Nesterov và Arkadi Nemirovski đã giải quyết triệt để vấn đề này qua lý thuyết **Hàm tự tương hợp (Self-concordant Functions)**.

Một hàm lồi một biến khả vi ba lần $f: \mathbb{R} \to \mathbb{R}$ được gọi là tự tương hợp nếu nó thỏa mãn bất đẳng thức:

$$
|f'''(x)| \le 2 [f''(x)]^{3/2} \quad \forall x \in \operatorname{dom} f.
$$

Ý nghĩa bản chất: **Tốc độ thay đổi của độ cong (đạo hàm bậc ba) bị khống chế chặt chẽ bởi chính độ cong bậc hai tại điểm đó**.

Đối với hàm nhiều biến, hàm $f: \mathbb{R}^n \to \mathbb{R}$ là tự tương hợp nếu hàm một biến thu hẹp $t \mapsto f(x + t v)$ là tự tương hợp trên mọi đường thẳng đi qua miền xác định.
- Hàm toàn phương lồi là tự tương hợp vì đạo hàm bậc ba triệt tiêu: $f''' = 0$.
- Hàm chắn logarit $f(x) = -\log x$ với $x > 0$ là tự tương hợp vì:
  $$
  |f'''(x)| = \frac{2}{x^3} = 2 \left(\frac{1}{x^2}\right)^{3/2} = 2 [f''(x)]^{3/2}.
  $$

Lý thuyết tự tương hợp khẳng định rằng: Số bước lặp của phương pháp Newton để giải một bài toán tự tương hợp bị chặn trên bởi một hằng số chỉ phụ thuộc vào độ chính xác $\epsilon$ và giá trị mục tiêu khởi đầu, hoàn toàn độc lập với hệ tọa độ và số chiều biến!

---

## 6. Tối ưu có Ràng buộc Đẳng thức và Hệ phương trình Newton–KKT

Xét bài toán tối ưu với ràng buộc đẳng thức affine:

$$
\min_x \quad f(x) \quad \text{sao cho} \quad A x = b.
$$

### 6.1. Phương pháp Khử biến (Elimination Method)
Nếu ta tìm được một nghiệm riêng $\hat x$ thỏa mãn $A \hat x = b$ và một ma trận $F \in \mathbb{R}^{n \times (n-p)}$ có các cột tạo thành cơ sở của không gian hạch $\operatorname{null}(A)$ ($A F = 0$), mọi điểm khả thi đều có thể biểu diễn duy nhất dưới dạng:

$$
x = F z + \hat x, \quad z \in \mathbb{R}^{n-p}.
$$

Bài toán có ràng buộc đẳng thức quy về bài toán không ràng buộc theo biến $z$:

$$
\min_{z \in \mathbb{R}^{n-p}} \quad \tilde f(z) = f(F z + \hat x).
$$

Phương pháp khử biến thích hợp khi số ràng buộc $p$ nhỏ hoặc ma trận $A$ có cấu trúc đơn giản.

### 6.2. Phương pháp Newton Khả thi (Feasible Newton Method)
Nếu điểm hiện tại $x$ đã khả thi ($A x = b$), để điểm mới $x + \Delta x$ tiếp tục khả thi, vector hướng di chuyển bắt buộc phải nằm trong không gian hạch của $A$: $A \Delta x = 0$.

Cực tiểu hóa mô hình bậc hai dưới điều kiện $A \Delta x = 0$ dẫn đến hệ phương trình **Newton–KKT**:

$$
\begin{bmatrix} \nabla^2 f(x) & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} \Delta x_{\mathrm{nt}} \\ w \end{bmatrix} = \begin{bmatrix} -\nabla f(x) \\ 0 \end{bmatrix}.
$$

### 6.3. Phương pháp Newton Khởi đầu Không khả thi (Infeasible Start Newton)
Nếu ta không có sẵn một điểm khả thi thỏa mãn $A x = b$, ta có thể xuất phát từ một điểm $x$ tùy ý và để phương pháp Newton đồng thời giải quyết hai nhiệm vụ: Tiến tới nghiệm tối ưu và triệt tiêu sai số ràng buộc.

Định nghĩa hai phần dư của hệ KKT:
- Phần dư đối ngẫu: $r_{\mathrm{dual}} = \nabla f(x) + A^T \nu$.
- Phần dư gốc: $r_{\mathrm{pri}} = A x - b$.

Hệ phương trình Newton–KKT khởi tạo không khả thi:

$$
\begin{bmatrix} \nabla^2 f(x) & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} \Delta x \\ \Delta \nu \end{bmatrix} = -\begin{bmatrix} r_{\mathrm{dual}} \\ r_{\mathrm{pri}} \end{bmatrix}.
$$

Tiêu chuẩn tìm kiếm bước Backtracking trong trường hợp này đo bằng **chuẩn phần dư tổng hợp**:
$$
\|r(x + t \Delta x, \nu + t \Delta \nu)\|_2 \le (1 - \alpha t) \|r(x, \nu)\|_2.
$$

### 6.4. Kỹ thuật giải số học Hệ phương trình Newton–KKT (Phụ lục C)
Mỗi bước lặp của phương pháp Newton đòi hỏi phải giải hệ phương trình tuyến tính khối Newton–KKT:
$$
\begin{bmatrix} H & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} \Delta x \\ w \end{bmatrix} = - \begin{bmatrix} g \\ h \end{bmatrix}.
$$

Trong thực tế tính toán, ta không bao giờ tính ma trận nghịch đảo trực tiếp mà lựa chọn một trong hai chiến lược số học chuyên biệt:
1. **Phương pháp Khử ma trận khối bằng Phần bù Schur**:
   Vì Hessian $H = \nabla^2 f(x) \succ 0$, ta tính phân tích Cholesky của $H$: $H = L L^T$ ($\frac{1}{3} n^3$ flops).
   Từ phương trình thứ nhất, $\Delta x = -H^{-1} g - H^{-1} A^T w$.
   Thay vào phương trình thứ hai, ta giải hệ phương trình rút gọn kích thước $p \times p$ theo nhân tử đối ngẫu $w$:
   $$
   (A H^{-1} A^T) w = h - A H^{-1} g.
   $$
   Ma trận $M = A H^{-1} A^T \succ 0$ là ma trận đối xứng xác định dương. Ta giải hệ $p \times p$ bằng phân tích Cholesky trên $M$ với chi phí $\frac{1}{3} p^3$ flops, sau đó thu hồi $\Delta x$.
   Phương pháp này tối ưu vượt trội khi số ràng buộc nhỏ ($p \ll n$) hoặc khi ma trận Hessian $H$ có cấu trúc thưa, đường chéo (như trong phương pháp điểm trong).
2. **Phương pháp Phân tích $LDL^T$ trực tiếp**:
   Khi số ràng buộc lớn ($p \approx n$) hoặc khi $H$ không thuận tiện để đảo khối, ta phân tích toàn bộ ma trận hệ KKT kích thước $(n+p) \times (n+p)$ bằng phân tích $P L D L^T P^T$ (thuật toán Bunch–Kaufman) với chi phí $\frac{1}{3} (n+p)^3$ flops. Phương pháp này bảo đảm độ ổn định số học tối ưu ngay cả khi ma trận KKT có các giá trị riêng mang dấu đối nghịch.

---

## 7. Phương pháp Điểm trong (Interior-Point Methods)

Đỉnh cao của giải tích tối ưu hóa lồi hiện đại là **Phương pháp điểm trong**, được thiết kế để giải bài toán lồi tổng quát có ràng buộc bất đẳng thức:

$$
\begin{aligned}
\min_x \quad & f_0(x) \\
\text{sao cho} \quad & f_i(x) \le 0, \quad i = 1, \dots, m, \\
& A x = b.
\end{aligned}
$$

Giả sử bài toán khả thi ngặt (thỏa mãn điều kiện Slater).

### 7.1. Hàm chắn Logarit (Logarithmic Barrier)
Ý tưởng của phương pháp là xấp xỉ hàm chỉ thị của miền khả thi bất đẳng thức bằng một hàm số trơn khả vi bên trong miền khả thi ngặt:

$$
\phi(x) = -\sum_{i=1}^m \log(-f_i(x)), \qquad \operatorname{dom} \phi = \{x \in \mathcal{D} \mid f_i(x) < 0, \, i = 1, \dots, m\}.
$$

Gradient và Hessian của hàm chắn logarit:

$$
\begin{aligned}
\nabla \phi(x) &= \sum_{i=1}^m \frac{1}{-f_i(x)} \nabla f_i(x), \\
\nabla^2 \phi(x) &= \sum_{i=1}^m \frac{1}{f_i(x)^2} \nabla f_i(x) \nabla f_i(x)^T + \sum_{i=1}^m \frac{1}{-f_i(x)} \nabla^2 f_i(x).
\end{aligned}
$$

### 7.2. Đường trung tâm (Central Path)
Với mỗi tham số trọng số $t > 0$, ta xét bài toán tối ưu có ràng buộc đẳng thức:

$$
\min_x \quad t f_0(x) + \phi(x) \quad \text{sao cho} \quad A x = b.
$$

Nghiệm duy nhất của bài toán này được ký hiệu là $x^*(t)$. Tập hợp tất cả các điểm $\{x^*(t) \mid t > 0\}$ tạo thành một đường cong trơn trong không gian khả thi ngặt, được gọi là **đường trung tâm (central path)**.

Điểm $x^*(t)$ thỏa mãn điều kiện tối ưu KKT: Tồn tại $\hat \nu \in \mathbb{R}^p$ sao cho $A x^*(t) = b$ và:

$$
t \nabla f_0(x^*(t)) + \nabla \phi(x^*(t)) + A^T \hat \nu = 0.
$$

Chia cả hai vế cho $t > 0$:

$$
\nabla f_0(x^*(t)) + \sum_{i=1}^m \underbrace{\left( \frac{1}{-t f_i(x^*(t))} \right)}_{\lambda_i^*(t)} \nabla f_i(x^*(t)) + A^T \underbrace{\left(\frac{\hat \nu}{t}\right)}_{\nu^*(t)} = 0.
$$

Đặt $\lambda_i^*(t) = -\frac{1}{t f_i(x^*(t))} > 0$ và $\nu^*(t) = \hat \nu / t$. Bộ nhân tử này hoàn toàn thỏa mãn tính khả thi đối ngẫu! Giá trị hàm đối ngẫu tương ứng là:

$$
g(\lambda^*(t), \nu^*(t)) = f_0(x^*(t)) + \sum_{i=1}^m \lambda_i^*(t) f_i(x^*(t)) = f_0(x^*(t)) - \frac{m}{t}.
$$

Hệ quả nền tảng: **Khoảng cách đối ngẫu tại điểm $x^*(t)$ đúng bằng $m/t$**:

$$
\boxed{f_0(x^*(t)) - p^* \le \frac{m}{t}.}
$$

Khi cho $t \to +\infty$, khoảng cách đối ngẫu $m/t \to 0$, và điểm trên đường trung tâm $x^*(t)$ tiến thẳng về nghiệm tối ưu toàn cục $x^*$ của bài toán gốc!

### 7.3. Thuật toán Hàm chắn (Barrier Method)
Thuật toán hàm chắn giải một chuỗi các bài toán tối ưu không ràng buộc (hoặc chỉ có ràng buộc đẳng thức) bằng phương pháp Newton:

1. **Khởi tạo**: Chọn điểm khả thi ngặt $x = x^{(0)}$, $t = t^{(0)} > 0$, hệ số tăng $\mu > 1$ (thường chọn $\mu = 10 \sim 20$), và ngưỡng dung sai sai số $\epsilon > 0$.
2. **Vòng lặp trong (Centering step)**: Giải bài toán tìm cực tiểu của $t f_0 + \phi$ với ràng buộc $A x = b$ bằng phương pháp Newton, lấy điểm xuất phát là nghiệm $x$ hiện tại.
3. **Cập nhật**: Đặt $x := x^*(t)$.
4. **Kiểm tra tiêu chí dừng**: Nếu $m/t < \epsilon$, dừng thuật toán và trả về nghiệm $x$.
5. **Tăng tham số phạt**: Đặt $t := \mu t$ và quay lại bước 2.

Vì mỗi bước ngoài tăng $t$ lên $\mu$ lần, khoảng cách đối ngẫu giảm theo cấp số nhân. Số vòng lặp ngoài để đạt độ chính xác $\epsilon$ bị chặn trên chặt chẽ bởi:

$$
\left\lceil \frac{\log(m / (t^{(0)} \epsilon))}{\log \mu} \right\rceil.
$$

Thực tế kiểm chứng: Thuật toán hàm chắn luôn kết thúc trong khoảng từ **20 đến 50 bước lặp ngoài**, bất kể bài toán có kích thước hàng triệu biến và ràng buộc.

---

## 8. Hệ thống Bài tập Tự luyện Chuyên sâu

::: exercise 1. Hướng dốc nhất theo chuẩn L1 và chuẩn cực đại L-infinity
Cho hàm số hai biến $f(x_1, x_2)$ có gradient tại điểm hiện tại là $\nabla f(x) = (3, -4)^T$.
1. Tìm hướng dốc nhất chuẩn hóa $\Delta x_{\mathrm{nsd}}$ theo chuẩn Euclid $L_2$.
2. Tìm hướng dốc nhất chuẩn hóa theo chuẩn $L_1$ và chuẩn $L_\infty$.
:::
::: solution
**Lời giải**:
1. Chuẩn Euclid của gradient: $\|\nabla f(x)\|_2 = \sqrt{3^2 + (-4)^2} = 5$.
   Hướng dốc nhất theo chuẩn $L_2$:
   $$
   \Delta x_{\mathrm{nsd}, 2} = -\frac{\nabla f(x)}{\|\nabla f(x)\|_2} = -\frac{1}{5} \begin{bmatrix} 3 \\ -4 \end{bmatrix} = \begin{bmatrix} -0.6 \\ 0.8 \end{bmatrix}.
   $$

2. **Theo chuẩn $L_1$**:
   Tọa độ có trị tuyệt đối gradient lớn nhất là tọa độ thứ hai vì $|-4| = 4 > |3| = 3$.
   Do đó hướng dốc nhất theo chuẩn $L_1$ chỉ di chuyển trên tọa độ thứ hai:
   $$
   \Delta x_{\mathrm{nsd}, 1} = -\operatorname{sign}(-4) e_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}.
   $$
   Tích vô hướng đạt được là $\nabla f(x)^T \Delta x = 3(0) + (-4)(1) = -4$.

3. **Theo chuẩn $L_\infty$**:
   Mọi tọa độ đều nhận giá trị cực biên $\pm 1$:
   $$
   \Delta x_{\mathrm{nsd}, \infty} = -\operatorname{sign}(\nabla f(x)) = \begin{bmatrix} -\operatorname{sign}(3) \\ -\operatorname{sign}(-4) \end{bmatrix} = \begin{bmatrix} -1 \\ 1 \end{bmatrix}.
   $$
   Tích vô hướng đạt được là $\nabla f(x)^T \Delta x = 3(-1) + (-4)(1) = -7$.
:::

::: exercise 2. Đường trung tâm và Khoảng cách đối ngẫu của Quy hoạch Tuyến tính
Xét bài toán quy hoạch tuyến tính một biến:
$$
\min_{x \in \mathbb{R}} \quad c x \quad \text{sao cho} \quad x \ge 0 \quad (\text{tức } -x \le 0),
$$
với hằng số $c > 0$.
1. Thiết lập hàm chắn logarit $\phi(x)$ và bài toán tìm điểm trên đường trung tâm $x^*(t)$.
2. Tìm nghiệm $x^*(t)$ và tính khoảng cách đối ngẫu tương ứng.
:::
::: solution
**Lời giải**:
1. Ràng buộc chuẩn tắc: $f_1(x) = -x \le 0$. Hàm chắn logarit:
   $$
   \phi(x) = -\log(-f_1(x)) = -\log(x) \quad \text{với } x > 0.
   $$
   Hàm mục tiêu trên đường trung tâm với tham số $t > 0$:
   $$
   \psi_t(x) = t c x - \log(x).
   $$

2. Tìm cực tiểu bằng cách đạo hàm theo $x$:
   $$
   \psi_t'(x) = t c - \frac{1}{x} = 0 \iff x^*(t) = \frac{1}{t c}.
   $$
   Đạo hàm bậc hai $\psi_t''(x) = 1/x^2 > 0$, chứng minh $x^*(t) = \frac{1}{tc}$ là nghiệm duy nhất.
   Giá trị hàm mục tiêu gốc tại điểm này là:
   $$
   f_0(x^*(t)) = c \left(\frac{1}{t c}\right) = \frac{1}{t}.
   $$
   Vì nghiệm tối ưu thực tế là $x^* = 0$ với chi phí $p^* = 0$, khoảng cách đối ngẫu thực tế là:
   $$
   f_0(x^*(t)) - p^* = \frac{1}{t} - 0 = \frac{1}{t}.
   $$
   Kết quả này hoàn toàn trùng khớp với công thức lý thuyết tổng quát $m/t$ với số ràng buộc $m = 1$. Khi $t \to +\infty$, điểm $x^*(t) \to 0$ tiệm cận chính xác về nghiệm tối ưu toàn cục.
:::

::: exercise 3. Tính số bước lặp ngoài của Thuật toán Hàm chắn
Một bài toán quy hoạch lồi có $m = 1000$ ràng buộc bất đẳng thức. Thuật toán hàm chắn khởi tạo với $t^{(0)} = 1$ và hệ số nhân $\mu = 10$.
Hỏi sau bao nhiêu bước lặp ngoài thì thuật toán bảo đảm tìm được nghiệm có sai số hàm mục tiêu không vượt quá $\epsilon = 10^{-6}$?
:::
::: solution
**Lời giải**:
Khoảng cách đối ngẫu sau $k$ bước lặp ngoài là:
$$
\frac{m}{t^{(k)}} = \frac{m}{t^{(0)} \mu^k} = \frac{1000}{1 \cdot 10^k} = \frac{10^3}{10^k} = 10^{3 - k}.
$$
Để bảo đảm sai số không vượt quá $\epsilon = 10^{-6}$, ta cần:
$$
10^{3 - k} \le 10^{-6} \iff 3 - k \le -6 \iff k \ge 9.
$$
Như vậy, chỉ sau đúng **9 bước lặp ngoài**, thuật toán hàm chắn đã đưa sai số mục tiêu từ ngưỡng 1000 ban đầu xuống dưới $10^{-6}$.
:::

---

## Tóm tắt cốt lõi

1. **Phương pháp dốc nhất theo các chuẩn**: Chuẩn Euclid sinh ra Gradient Descent, chuẩn toàn phương ma trận sinh ra phương pháp Newton, và chuẩn $L_1$ sinh ra phương pháp hạ dốc theo tọa độ.
2. **Backtracking Line Search**: Điều kiện Armijo bảo đảm mức giảm thực tế tương xứng với xấp xỉ tuyến tính, ngăn chặn hiện tượng bước nhảy quá trớn trong các hẻm núi hẹp.
3. **Phương pháp Newton và Newton Decrement**: Mô hình xấp xỉ bậc hai đạt tốc độ hội tụ bậc hai kỳ vĩ gần nghiệm. Đại lượng $\lambda(x)$ cung cấp tiêu chuẩn dừng bất biến affine chuẩn mực.
4. **Hàm tự tương hợp**: Đặt cơ sở lý thuyết chứng minh số bước lặp Newton bị chặn trên độc lập với hệ tọa độ và số chiều biến.
5. **Hệ phương trình Newton–KKT**: Công cụ thống nhất giải quyết các bài toán có ràng buộc đẳng thức từ điểm khởi tạo khả thi hoặc không khả thi.
6. **Phương pháp Điểm trong và Đường trung tâm**: Hàm chắn logarit $-\sum \log(-f_i(x))$ biến bài toán có ràng buộc thành chuỗi bài toán không ràng buộc trơn. Khoảng cách đối ngẫu tại mỗi điểm trên đường trung tâm được kiểm soát chính xác bằng $m/t$.

---

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press. Đọc kỹ Chương 9 (Tối ưu không ràng buộc), Chương 10 (Tối ưu ràng buộc đẳng thức), và Chương 11 (Phương pháp điểm trong).
- Yurii Nesterov, *Lectures on Convex Optimization*, Springer.
- Jorge Nocedal, Stephen J. Wright, *Numerical Optimization*, Springer.

Tiếp theo: [Bài 05: Tối ưu hóa trong Huấn luyện Học sâu: Mini-batch SGD và Momentum](./bai-05-toi-uu-huan-luyen.md).
