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

::: exercise 4. Thuật toán tìm kiếm đường thẳng quay lui Armijo trên hàm bậc hai lệch tỉ lệ
Xét hàm mục tiêu toàn phương có tỉ số điều kiện xấu:
$$
f(x) = \frac{1}{2}(3x_1^2 + 7x_2^2).
$$
Khởi tạo từ điểm $x^0 = (2, 4)^T$.
1. Tính gradient $g = \nabla f(x^0)$ và giá trị hàm số $f(x^0)$. Xét mô hình xấp xỉ tuyến tính có phạt chuẩn $Q_I(d) = f(x^0) + g^T d + \frac{1}{2}\|d\|_2^2$. Chứng minh hướng giảm dốc nhất chuẩn hóa chính là hướng gradient ngược $d_G = -g$.
2. Với các tham số quay lui Armijo $\alpha = 0{,}1$ và hệ số co bước $\beta = 0{,}5$, ngưỡng chấp nhận bước $t$ là:
   $$
   f(x^0 + t d_G) \le f(x^0) + \alpha t g^T d_G = 62 - 82t.
   $$
   Kiểm tra tuần tự các bước thử $t = 1$, $t = 0{,}5$, $t = 0{,}25$: Tính tọa độ điểm thử, giá trị hàm số thực tế, so sánh với ngưỡng Armijo và chỉ ra bước nhảy đầu tiên được chấp nhận.
3. Giải thích tại sao bước dài $t = 1$ làm hàm số tăng vọt (hiện tượng vọt lố qua hẻm núi), và nêu trực giác tại sao điều kiện Armijo kết thúc sau hữu hạn bước co.
:::

::: solution
1. **Gradient và hướng dốc nhất**:
   Gradient của hàm số tại điểm bất kỳ là $\nabla f(x) = (3x_1, 7x_2)^T$.
   Tại điểm khởi đầu $x^0 = (2, 4)^T$:
   $$
   g = \nabla f(x^0) = (3 \times 2, 7 \times 4)^T = (6, 28)^T.
   $$
   Giá trị hàm số:
   $$
   f(x^0) = \frac{1}{2}(3 \times 2^2 + 7 \times 4^2) = 62.
   $$
   Bình phương độ dài gradient: $\|g\|_2^2 = 6^2 + 28^2 = 36 + 784 = 820$.
   
   Mô hình cục bộ $Q_I(d)$:
   $$
   Q_I(d) = f(x^0) + g^T d + \frac{1}{2}\|d\|_2^2.
   $$
   Lấy đạo hàm theo $d$ và giải điều kiện triệt tiêu gradient:
   $$
   \nabla_d Q_I(d) = g + d = 0 \implies d_G = -g = (-6, -28)^T.
   $$
   Vì ma trận đơn vị $I \succ 0$, điểm này là cực tiểu toàn cục duy nhất của mô hình. Tích vô hướng với gradient: $g^T d_G = -\|g\|_2^2 = -820 < 0$, khẳng định $d_G$ là một hướng giảm hợp lệ.

2. **Kiểm tra quy tắc quay lui Armijo**:
   Ngưỡng chấp nhận Armijo:
   $$
   62 + \alpha t (-820) = 62 - 0{,}1 \times 820 t = 62 - 82t.
   $$
   - **Thử $t = 1$**:
     Điểm thử là $x = x^0 + d_G = (-4, -24)^T$.
     Giá trị hàm số:
     $$
     f(-4, -24) = \frac{1}{2}(3 \times 16 + 7 \times 576) = \frac{1}{2}(48 + 4032) = 2040.
     $$
     Ngưỡng yêu cầu: $62 - 82(1) = -20$.
     Vì $2040 > -20$, bước $t = 1$ bị từ chối thẳng thừng do vọt lố nghiêm trọng.
   - **Thử $t = 0{,}5$**:
     Điểm thử là $x = x^0 + 0{,}5 d_G = (-1, -10)^T$.
     Giá trị hàm số:
     $$
     f(-1, -10) = \frac{1}{2}(3 \times 1 + 7 \times 100) = \frac{703}{2} = 351{,}5.
     $$
     Ngưỡng yêu cầu: $62 - 82(0{,}5) = 62 - 41 = 21$.
     Vì $351{,}5 > 21$, bước $t = 0{,}5$ tiếp tục bị loại.
   - **Thử $t = 0{,}25$**:
     Điểm thử là $x = x^0 + 0{,}25 d_G = (0{,}5; -3)^T$.
     Giá trị hàm số:
     $$
     f(0{,}5; -3) = \frac{1}{2}(3 \times 0{,}25 + 7 \times 9) = \frac{1}{2}(0{,}75 + 63) = \frac{63{,}75}{2} = 31{,}875.
     $$
     Ngưỡng yêu cầu: $62 - 82(0{,}25) = 62 - 20{,}5 = 41{,}5$.
     Vì $31{,}875 \le 41{,}5$, điều kiện Armijo được thỏa mãn.
   
   Thuật toán quay lui dừng lại và chấp nhận bước nhảy $t^* = 0{,}25$.

3. **Bản chất hình học của hiện tượng vọt lố**:
   Độ cong của hàm số theo phương $x_2$ lớn hơn đáng kể so với phương $x_1$ ($7 > 3$). Khi bước nhảy theo gradient quá dài ($t = 1$), bước nhảy vượt qua đáy thung lũng parabol và leo thẳng lên vách đối diện, khiến hàm số tăng từ $62$ lên $2040$.
   
   Quy tắc Armijo bảo đảm dừng sau hữu hạn lần co nhờ khai triển Taylor bậc nhất:
   $$
   f(x^0 + t d) = f(x^0) + t g^T d + o(t).
   $$
   Khi $t \to 0$, số hạng $o(t)$ trở nên không đáng kể so với $(1 - \alpha)t g^T d < 0$, bảo đảm bất đẳng thức Armijo luôn nghiệm đúng với mọi $t$ đủ nhỏ.
:::

::: exercise 5. Hướng giảm dốc nhất theo chuẩn metric Hessian và nguồn gốc phương pháp Newton
Xét bài toán tìm hướng giảm dốc nhất dưới ràng buộc chuẩn ellipsoid do ma trận xác định dương $W \succ 0$ quy định:
$$
\min_{v \in \mathbb{R}^n} \quad g^T v \quad \text{sao cho} \quad v^T W v \le 1,
$$
với vector gradient $g \ne 0$.
1. Thiết lập hàm Lagrangian và hệ điều kiện KKT cho bài toán con trên. Chứng minh nhân tử Lagrange $\zeta > 0$, suy ra ràng buộc đạt dấu bằng trên biên ellipsoid.
2. Tìm nghiệm tối ưu $v^*$ và giá trị nhỏ nhất của $g^T v^*$. Định nghĩa chuẩn đối ngẫu $\|g\|_* = \sqrt{g^T W^{-1} g}$.
3. Khi đổi độ dài thành $d = \|g\|_* v^*$, chứng minh $d = -W^{-1} g$. Rút ra kết luận: Phương pháp Newton chính là phương pháp giảm dốc nhất khi chuẩn không gian được đo bằng ma trận Hessian cục bộ $W = \nabla^2 f(x)$.
:::

::: solution
1. **Thiết lập KKT cho bài toán con**:
   Hàm Lagrangian với nhân tử $\zeta \ge 0$:
   $$
   L(v, \zeta) = g^T v + \zeta(v^T W v - 1).
   $$
   Hệ điều kiện KKT:
   - Triệt tiêu gradient: $g + 2\zeta W v = 0$.
   - Khả thi gốc: $v^T W v \le 1$.
   - Khả thi đối ngẫu: $\zeta \ge 0$.
   - Bù trừ: $\zeta(v^T W v - 1) = 0$.
   
   Nếu $\zeta = 0$: Phương trình đạo hàm cho $g = 0$, mâu thuẫn với giả thiết $g \ne 0$.
   Do đó bắt buộc $\zeta > 0$.
   Theo điều kiện bù trừ, vì $\zeta > 0$, ràng buộc bắt buộc đạt dấu bằng:
   $$
   v^T W v = 1.
   $$

2. **Nghiệm tối ưu và chuẩn đối ngẫu**:
   Từ phương trình đạo hàm:
   $$
   2\zeta W v = -g \implies v = -\frac{1}{2\zeta} W^{-1} g.
   $$
   Thay vào ràng buộc $v^T W v = 1$:
   $$
   \left(-\frac{1}{2\zeta} W^{-1} g\right)^T W \left(-\frac{1}{2\zeta} W^{-1} g\right) = \frac{1}{4\zeta^2} g^T W^{-1} g = 1.
   $$
   Suy ra nhân tử Lagrange tối ưu:
   $$
   \zeta^* = \frac{1}{2}\sqrt{g^T W^{-1} g}.
   $$
   Đặt chuẩn đối ngẫu $\|g\|_* = \sqrt{g^T W^{-1} g}$, ta tìm được hướng giảm dốc nhất chuẩn hóa:
   $$
   v^* = -\frac{W^{-1} g}{\sqrt{g^T W^{-1} g}} = -\frac{W^{-1} g}{\|g\|_*}.
   $$
   Giá trị hàm mục tiêu tại nghiệm là:
   $$
   g^T v^* = -\frac{g^T W^{-1} g}{\|g\|_*} = -\frac{\|g\|_*^2}{\|g\|_*} = -\|g\|_* = -\sqrt{g^T W^{-1} g}.
   $$

3. **Mối liên hệ với phương pháp Newton**:
   Khi loại bỏ việc chuẩn hóa độ dài đơn vị và co dãn theo độ lớn gradient chuẩn đối ngẫu:
   $$
   d = \|g\|_* v^* = \|g\|_* \left(-\frac{W^{-1} g}{\|g\|_*}\right) = -W^{-1} g.
   $$
   Vector $d$ nghiệm đúng phương trình ma trận $W d = -g$.
   
   Khi chọn $W = \nabla^2 f(x) \succ 0$ là ma trận Hessian tại điểm hiện tại, phương trình trở thành:
   $$
   \nabla^2 f(x) d = -\nabla f(x) \implies d_N = -\big[\nabla^2 f(x)\big]^{-1} \nabla f(x).
   $$
   Đây chính là bước lặp Newton kinh điển.
   
   **Kết luận sâu sắc**: Phương pháp Newton không phải là một thuật toán xa lạ tách rời, mà chính là phương pháp hạ dốc nhất (steepest descent) tự nhiên nhất của bài toán khi ta trang bị cho không gian vector một metric Riemann cục bộ định hình bởi ma trận độ cong Hessian.
:::

::: exercise 6. Bước lặp Newton, đại lượng Newton Decrement và mức giảm mô hình xấp xỉ
Cho hàm số lồi trơn trên miền dương:
$$
\varphi(s) = s - \log s, \qquad s > 0.
$$
Xét điểm khởi tạo $s^0 = 0{,}25$.
1. Tính đạo hàm bậc một $\varphi'(s)$, đạo hàm bậc hai $\varphi''(s)$ và xác định gradient $g$, Hessian $H$ tại $s^0 = 0{,}25$.
2. Lập mô hình xấp xỉ Taylor bậc hai $Q_H(d)$ quanh điểm $s^0$. Giải phương trình dừng $Q_H'(d) = 0$ để tìm bước lặp Newton $d_N$ và điểm mới $s^1$.
3. Tính đại lượng giảm lượng Newton (Newton decrement) $\lambda(s^0)$, bình phương $\lambda(s^0)^2$ và mức giảm dự đoán của mô hình $\frac{1}{2}\lambda(s^0)^2$.
4. Tính mức giảm thực tế $\varphi(s^0) - \varphi(s^1)$ và sai số tối ưu thực tế $\varphi(s^0) - \varphi(s^*)$. Phân biệt rõ sự khác nhau giữa ba đại lượng này.
:::

::: solution
1. **Đạo hàm và ma trận Hessian**:
   Đạo hàm bậc một và bậc hai:
   $$
   \varphi'(s) = 1 - \frac{1}{s}, \qquad \varphi''(s) = \frac{1}{s^2}.
   $$
   Tại điểm $s^0 = 0{,}25 = \frac{1}{4}$:
   $$
   g = \varphi'(1/4) = 1 - 4 = -3, \qquad H = \varphi''(1/4) = \frac{1}{(1/4)^2} = 16.
   $$
   Vì $H = 16 > 0$, hàm số lồi chặt tại lân cận điểm đang xét.

2. **Mô hình bậc hai và bước lặp Newton**:
   Mô hình xấp xỉ Taylor bậc hai theo độ dời $d$:
   $$
   Q_H(d) = \varphi(1/4) + g d + \frac{1}{2} H d^2 = \varphi(1/4) - 3d + 8d^2.
   $$
   Đạo hàm theo $d$ và giải điều kiện triệt tiêu:
   $$
   Q_H'(d) = -3 + 16d = 0 \implies d_N = \frac{3}{16} = 0{,}1875.
   $$
   Điểm cập nhật mới sau một bước Newton thuần túy ($t = 1$):
   $$
   s^1 = s^0 + d_N = \frac{1}{4} + \frac{3}{16} = \frac{7}{16} = 0{,}4375.
   $$
   Kiểm tra đạo hàm tại điểm mới: $\varphi'(7/16) = 1 - \frac{16}{7} = -\frac{9}{7} \ne 0$, chứng tỏ điểm $s^1$ tiến gần hơn về nghiệm nhưng chưa phải nghiệm tối ưu.

3. **Newton decrement và mức giảm mô hình**:
   Đại lượng giảm lượng Newton được định nghĩa:
   $$
   \lambda(s^0) = \sqrt{g^T H^{-1} g} = \sqrt{(-3) \times \frac{1}{16} \times (-3)} = \sqrt{\frac{9}{16}} = \frac{3}{4} = 0{,}75.
   $$
   Bình phương của nó: $\lambda(s^0)^2 = \frac{9}{16} = 0{,}5625$.
   Mức giảm giá trị được dự đoán bởi mô hình bậc hai:
   $$
   Q_H(0) - Q_H(d_N) = -g d_N - \frac{1}{2} H d_N^2 = -(-3)\left(\frac{3}{16}\right) - 8\left(\frac{3}{16}\right)^2 = \frac{9}{16} - \frac{9}{32} = \frac{9}{32} = \frac{1}{2}\lambda(s^0)^2.
   $$
   Giá trị mức giảm dự đoán là $\frac{9}{32} = 0{,}28125$.

4. **So sánh mức giảm thực tế và sai số tối ưu**:
   - Nghiệm tối ưu toàn cục giải tích của $\varphi(s)$ là $s^* = 1$ với giá trị tối ưu $\varphi(1) = 1 - \log 1 = 1$.
   - Sai số tối ưu thực tế tại điểm khởi đầu:
     $$
     \varphi(s^0) - \varphi(s^*) = \left(\frac{1}{4} - \log\frac{1}{4}\right) - 1 = -\frac{3}{4} + \log 4 \approx -0{,}75 + 1{,}3863 = 0{,}6363.
     $$
   - Mức giảm thực tế sau một bước lặp:
     $$
     \begin{aligned}
     \varphi(s^0) - \varphi(s^1) &= \left(\frac{1}{4} + \log 4\right) - \left(\frac{7}{16} - \log\frac{7}{16}\right) \\
     &= -\frac{3}{16} + \log\frac{64}{7} \approx -0{,}1875 + 2{,}2130 = 0{,}2933.
     \end{aligned}
     $$
   
   **Phân biệt ba đại lượng**:
   - Mức giảm dự đoán $\frac{1}{2}\lambda^2 = 0{,}28125$: Dựa trên mô hình parabol thuần túy.
   - Mức giảm thực tế $\approx 0{,}2933$: Mức hạ thấp thực của hàm phi tuyến sau một bước cập nhật.
   - Sai số tối ưu thực tế $\approx 0{,}6363$: Khoảng cách giá trị còn lại đến cực tiểu toàn cục.
   
   Cả ba đại lượng có cùng bậc độ lớn nhưng không bao giờ trùng nhau đối với hàm phi toàn phương.
:::

::: exercise 7. Phương pháp Newton khả thi và khử ràng buộc đẳng thức affine
Xét bài toán tối ưu có ràng buộc đẳng thức:
$$
\begin{aligned}
\min_{x \in \mathbb{R}^3} \quad & f(x) = \frac{1}{2}(x_1^2 + 2x_2^2 + 3x_3^2) \\
\text{sao cho} \quad & x_1 + x_2 + x_3 = 1.
\end{aligned}
$$
1. Phương pháp Newton-KKT: Thiết lập hệ phương trình KKT bậc nhất cho bước lặp Newton $\Delta x$ và nhân tử đối ngẫu $w$. Giải hệ phương trình trực tiếp để tìm nghiệm tối ưu $x^*$ từ điểm xuất phát khả thi $x^0 = (1, 0, 0)^T$.
2. Phương pháp khử biến: Dùng ràng buộc $x_1 = 1 - x_2 - x_3$ để khử biến $x_1$, đưa bài toán về bài toán tối ưu không ràng buộc theo hai biến $(x_2, x_3)$. Tìm ma trận Hessian của bài toán rút gọn và kiểm chứng rằng bước lặp Newton trên không gian rút gọn cho cùng kết quả.
:::

::: solution
1. **Phương pháp Newton-KKT**:
   Gradient và Hessian của hàm mục tiêu:
   $$
   \nabla f(x) = \begin{bmatrix} x_1 \\ 2x_2 \\ 3x_3 \end{bmatrix}, \qquad H = \nabla^2 f(x) = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix}.
   $$
   Ma trận ràng buộc đẳng thức: $A = \begin{bmatrix} 1 & 1 & 1 \end{bmatrix}$, $b = 1$.
   
   Tại điểm khả thi $x^0 = (1, 0, 0)^T$, gradient là $\nabla f(x^0) = (1, 0, 0)^T$. Hệ phương trình Newton-KKT xác định hướng $\Delta x$ và nhân tử $w$:
   $$
   \begin{bmatrix} H & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} \Delta x \\ w \end{bmatrix} = \begin{bmatrix} -\nabla f(x^0) \\ 0 \end{bmatrix}.
   $$
   Khai triển hệ phương trình:
   $$
   \begin{aligned}
   \Delta x_1 + w &= -1 \implies \Delta x_1 = -1 - w, \\
   2\Delta x_2 + w &= 0 \implies \Delta x_2 = -\frac{w}{2}, \\
   3\Delta x_3 + w &= 0 \implies \Delta x_3 = -\frac{w}{3}.
   \end{aligned}
   $$
   Thay vào ràng buộc bảo toàn tính khả thi $A \Delta x = \Delta x_1 + \Delta x_2 + \Delta x_3 = 0$:
   $$
   (-1 - w) - \frac{w}{2} - \frac{w}{3} = 0 \iff -1 - w\left(1 + \frac{1}{2} + \frac{1}{3}\right) = 0 \iff w\left(\frac{11}{6}\right) = -1 \implies w = -\frac{6}{11}.
   $$
   Tính các thành phần của hướng cập nhật:
   $$
   \Delta x_1 = -1 - \left(-\frac{6}{11}\right) = -\frac{5}{11}, \quad \Delta x_2 = -\frac{-6/11}{2} = \frac{3}{11}, \quad \Delta x_3 = -\frac{-6/11}{3} = \frac{2}{11}.
   $$
   Cập nhật nghiệm mới:
   $$
   x^* = x^0 + \Delta x = \begin{bmatrix} 1 - 5/11 \\ 0 + 3/11 \\ 0 + 2/11 \end{bmatrix} = \begin{bmatrix} 6/11 \\ 3/11 \\ 2/11 \end{bmatrix}.
   $$
   Vì hàm mục tiêu là hàm toàn phương, phương pháp Newton tìm ra nghiệm tối ưu toàn cục chỉ sau đúng một bước lặp.

2. **Phương pháp khử biến (Elimination)**:
   Thay $x_1 = 1 - x_2 - x_3$ vào hàm mục tiêu:
   $$
   \begin{aligned}
   \tilde{f}(x_2, x_3) &= \frac{1}{2}(1 - x_2 - x_3)^2 + x_2^2 + \frac{3}{2}x_3^2 \\
   &= \frac{1}{2}(1 + x_2^2 + x_3^2 - 2x_2 - 2x_3 + 2x_2 x_3) + x_2^2 + \frac{3}{2}x_3^2 \\
   &= \frac{3}{2}x_2^2 + 2x_3^2 + x_2 x_3 - x_2 - x_3 + \frac{1}{2}.
   \end{aligned}
   $$
   Gradient và Hessian rút gọn:
   $$
   \nabla \tilde{f} = \begin{bmatrix} 3x_2 + x_3 - 1 \\ x_2 + 4x_3 - 1 \end{bmatrix}, \qquad \tilde{H} = \begin{bmatrix} 3 & 1 \\ 1 & 4 \end{bmatrix}.
   $$
   Giải phương trình dừng $\nabla \tilde{f} = 0$:
   $$
   \begin{cases} 3x_2 + x_3 = 1 \\ x_2 + 4x_3 = 1 \end{cases} \implies \begin{bmatrix} x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 3 & 1 \\ 1 & 4 \end{bmatrix}^{-1} \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \frac{1}{11}\begin{bmatrix} 4 & -1 \\ -1 & 3 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 3/11 \\ 2/11 \end{bmatrix}.
   $$
   Khôi phục lại $x_1$: $x_1 = 1 - \frac{3}{11} - \frac{2}{11} = \frac{6}{11}$.
   
   Kết quả hoàn toàn trùng khớp với phương pháp Newton-KKT. Khử biến giảm số chiều bài toán nhưng phá vỡ cấu trúc thưa thớt của ma trận Hessian, trong khi Newton-KKT bảo toàn cấu trúc thưa thớt ở không gian biến mở rộng.
:::

::: exercise 8. Tính tự điều chỉnh (Self-concordance) và cận sai số tối ưu độc lập hệ tọa độ
1. Một hàm số lồi $f: \mathbb{R} \to \mathbb{R}$ được gọi là hàm tự điều chỉnh (self-concordant) chuẩn hóa nếu thỏa mãn bất đẳng thức:
   $$
   |f'''(x)| \le 2 f''(x)^{3/2} \quad \forall x \in \operatorname{dom} f.
   $$
   Chứng minh rằng hàm chắn logarit tự nhiên $f(x) = -\log x$ trên miền $x > 0$ là một hàm tự điều chỉnh chuẩn hóa.
2. Với hàm tự điều chỉnh đa chiều, đại lượng giảm lượng Newton $\lambda(x) = \sqrt{\nabla f(x)^T [\nabla^2 f(x)]^{-1} \nabla f(x)}$ là một đại lượng bất biến affine (affine invariant). Khi $\lambda(x) < 0{,}68$, ta có cận sai số tối ưu giải tích:
   $$
   f(x) - p^* \le \lambda(x)^2.
   $$
   Giải thích tại sao tính chất này giúp lý thuyết tối ưu hóa giải phóng khỏi sự phụ thuộc vào các hằng số nhạy cảm hệ tọa độ như hằng số Lipschitz của gradient $L$ hay độ lồi mạnh $m$.
:::

::: solution
1. **Chứng minh tính tự điều chỉnh của hàm logarit**:
   Tính các cấp đạo hàm của $f(x) = -\log x$:
   $$
   f'(x) = -\frac{1}{x}, \qquad f''(x) = \frac{1}{x^2}, \qquad f'''(x) = -\frac{2}{x^3}.
   $$
   Lấy giá trị tuyệt đối của đạo hàm bậc ba:
   $$
   |f'''(x)| = \left|-\frac{2}{x^3}\right| = \frac{2}{x^3}.
   $$
   Biểu thức vế phải của định nghĩa:
   $$
   2 \big(f''(x)\big)^{3/2} = 2 \left(\frac{1}{x^2}\right)^{3/2} = 2 \left(\frac{1}{x^3}\right) = \frac{2}{x^3}.
   $$
   Ta thấy $|f'''(x)| = 2 \big(f''(x)\big)^{3/2}$ đạt dấu bằng với mọi $x > 0$.
   Do đó $f(x) = -\log x$ thỏa mãn định nghĩa hàm tự điều chỉnh chuẩn hóa với hằng số $2$.

2. **Ý nghĩa lý thuyết của tính tự điều chỉnh**:
   - **Tính bất biến Affine**: Dưới phép đổi biến tuyến tính khả nghịch $x = T y$, các đại lượng giải tích bậc nhất truyền thống như chuẩn gradient $\|\nabla f(x)\|_2$ bị biến dạng hoàn toàn phụ thuộc vào ma trận chuyển cơ sở $T$. Trái lại, đại lượng Newton decrement $\lambda(x)$ giữ nguyên giá trị chính xác trên mọi hệ tọa độ:
     $$
     \lambda_{\tilde{f}}(y) = \lambda_f(x).
     $$
   - **Thoát khỏi hằng số điều kiện**: Trong phân tích hội tụ gradient descent truyền thống, tốc độ hội tụ phụ thuộc nặng nề vào số điều kiện $\kappa = L/m$. Một phép đổi đơn vị đo lường đơn giản có thể làm $\kappa$ tăng vọt từ $10$ lên $10^6$, khiến các cận hội tụ lý thuyết trở nên vô nghĩa.
   - **Cận hội tụ phổ quát**: Lý thuyết tự điều chỉnh của Nesterov và Nemirovski chứng minh rằng khi $\lambda(x) \le 0{,}68$, thuật toán Newton bước vào pha hội tụ bậc hai (quadratic convergence) thuần túy. Số bước lặp cần thiết để đạt độ chính xác $\epsilon$ bị chặn trên bởi một hàm chỉ phụ thuộc vào sai số ban đầu và tham số tự điều chỉnh, hoàn toàn độc lập với ma trận điều kiện và số chiều không gian.
:::


---

## 8. Các chủ đề chuyên khảo về Phương pháp Điểm trong Nâng cao

Để làm chủ trọn vẹn họ phương pháp điểm trong từ lý thuyết đến triển khai thuật toán chuẩn công nghiệp, người học có thể đào sâu qua các chuyên đề nghiên cứu độc lập dưới đây:

<TopicMap />

---

## Tóm tắt cốt lõi

1. **Phương pháp dốc nhất theo các chuẩn**: Chuẩn Euclid sinh ra Gradient Descent, chuẩn toàn phương ma trận sinh ra phương pháp Newton, và chuẩn $L_1$ sinh ra phương pháp hạ dốc theo tọa độ.
2. **Backtracking Line Search**: Điều kiện Armijo bảo đảm mức giảm thực tế tương xứng với xấp xỉ tuyến tính, ngăn chặn hiện tượng bước nhảy quá trớn trong các hẻm núi hẹp.
3. **Phương pháp Newton và Newton Decrement**: Mô hình xấp xỉ bậc hai đạt tốc độ hội tụ bậc hai ở lân cận nghiệm. Đại lượng $\lambda(x)$ cung cấp tiêu chuẩn dừng bất biến affine chuẩn mực.
4. **Hàm tự tương hợp**: Đặt cơ sở lý thuyết chứng minh số bước lặp Newton bị chặn trên độc lập với hệ tọa độ và số chiều biến.
5. **Hệ phương trình Newton–KKT**: Công cụ thống nhất giải quyết các bài toán có ràng buộc đẳng thức từ điểm khởi tạo khả thi hoặc không khả thi.
6. **Phương pháp Điểm trong và Đường trung tâm**: Hàm chắn logarit $-\sum \log(-f_i(x))$ biến bài toán có ràng buộc thành chuỗi bài toán không ràng buộc trơn. Khoảng cách đối ngẫu tại mỗi điểm trên đường trung tâm được kiểm soát chính xác bằng $m/t$.

---

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press. Đọc kỹ Chương 9 (Tối ưu không ràng buộc), Chương 10 (Tối ưu ràng buộc đẳng thức), và Chương 11 (Phương pháp điểm trong).
- Yurii Nesterov, *Lectures on Convex Optimization*, Springer.
- Jorge Nocedal, Stephen J. Wright, *Numerical Optimization*, Springer.

Tiếp theo: [Bài 05: Tối ưu hóa trong Huấn luyện Học sâu: Mini-batch SGD và Momentum](./bai-05-toi-uu-huan-luyen.md).
