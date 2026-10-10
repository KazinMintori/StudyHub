---
course: toan-cho-ai
lecture: bai-00-on-tap-nen-tang
section: lecture
title: "Ôn tập nền tảng toán học cho AI"
prerequisites: ["ham-so", "dao-ham", "tap-hop"]
lessonStatus: ready
description: "Ôn tập toàn diện nền tảng toán học và tính toán số cho Trí tuệ Nhân tạo: Đại số ma trận, chuẩn, giải tích ma trận, phần bù Schur, SVD, đại số tuyến tính số (Cholesky, flops) và cội nguồn xác suất của bình phương tối thiểu."
---

Mọi mô hình trí tuệ nhân tạo, từ hồi quy tuyến tính cổ điển đến các mạng nơ-ron sâu với hàng trăm tỷ tham số, đều vận hành quanh một cơ chế cốt lõi: Ánh xạ dữ liệu đầu vào thành dự đoán, đo lường sai số bằng hàm mất mát, và lần theo đạo hàm để tinh chỉnh tham số. Khi mô hình dự đoán chệch hướng, ta cần biết chính xác tham số nào phải thay đổi, thay đổi bao nhiêu và theo chiều nào.

Bài giảng mở đầu này hệ thống hóa các trụ cột toán học và tính toán số nền tảng sẽ đồng hành cùng chúng ta xuyên suốt toàn bộ chương trình:
1. **Đại số ma trận và Chuẩn**: Công cụ biểu diễn đồng thời hàng triệu quan sát, đo lường khoảng cách và tận dụng năng lực tính toán song song trên GPU.
2. **Giải tích ma trận và Đạo hàm đa biến (Gradient & Hessian)**: Chiếc la bàn chỉ hướng dốc nhất để hạ thấp hàm mất mát và tấm gương phản chiếu độ cong địa hình tối ưu.
3. **Phần bù Schur và Phân tích giá trị kỳ dị (SVD)**: Các công cụ đại số cao cấp phân tích tính xác định dương của ma trận khối và bản chất hình học của không gian dữ liệu.
4. **Đại số tuyến tính số (Numerical Linear Algebra)**: Cấu trúc tính toán thực tế, phân tích Cholesky, khai thác ma trận thưa và ngân sách độ phức tạp tính toán (flops).
5. **Mô hình xác suất và Ước lượng hợp lý cực đại (MLE)**: Cội nguồn lý thuyết giải thích vì sao tiêu chuẩn sai số bình phương tối thiểu xuất hiện tự nhiên từ giả thiết nhiễu Gauss.

Toàn bộ công thức và biến đổi giải tích sẽ được gắn kết chặt chẽ với các ví dụ số học tường minh, giúp người học tự tay kiểm chứng từng bước biến đổi đại số mà không bị phân tâm bởi quy mô dữ liệu.

---

## 1. Biểu diễn dự đoán bằng phép nhân ma trận

Xét bài toán học có giám sát đơn giản: Ta muốn xây dựng một mô hình tuyến tính đơn tham số để dự đoán biến mục tiêu $\widehat b_i$ từ đầu vào $a_i$ theo quy tắc $\widehat b_i = a_i w$. 

Giả sử ta thu thập được ba quan sát thực nghiệm sau:

| Quan sát $i$ | Đầu vào $a_i$ | Đầu ra thực tế $b_i$ |
| :---: | :---: | :---: |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 2 |

Ở đây, các cặp $(a_i, b_i)$ là dữ liệu thực nghiệm đã cố định. Trọng số $w \in \mathbb{R}$ là tham số tự do mà chúng ta có quyền điều chỉnh để mô hình khớp dữ liệu nhất có thể. Chẳng hạn, nếu thử chọn $w = 1$, mô hình đưa ra ba dự đoán lần lượt là $1, 2, 3$. Hai dự đoán đầu khớp hoàn toàn với thực tế, nhưng ở quan sát thứ ba, mô hình dự đoán vượt giá trị thực tế một đơn vị ($\widehat b_3 - b_3 = 3 - 2 = 1$).

Thay vì viết ba phương trình rời rạc bằng vòng lặp tuần tự, trong kỹ nghệ AI ta gom toàn bộ đầu vào thành ma trận một cột và đầu ra thành một vector cột:

$$
A = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \quad
b = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}, \quad
\widehat b = A w, \quad
r = A w - b.
$$

- **Vector** $b, \widehat b, r \in \mathbb{R}^3$ là các danh sách số có thứ tự, trong đó mỗi phần tử đại diện cho một mẫu dữ liệu.
- **Ma trận** $A \in \mathbb{R}^{3 \times 1}$ là bảng số gồm 3 hàng và 1 cột.
- **Vector phần dư** $r = \widehat b - b$ phản ánh độ lệch giữa dự đoán và nhãn thực tế. Ta quy ước dấu phần dư là dự đoán trừ đi quan sát. Sự nhất quán về quy ước dấu này là điều kiện tiên quyết để tính đúng chiều của gradient sau này.

Trong bài toán tổng quát với $m$ quan sát và $n$ đặc trưng, ma trận dữ liệu có kích thước $A \in \mathbb{R}^{m \times n}$, vector trọng số $w \in \mathbb{R}^n$, còn nhãn thực tế và phần dư là các vector trong không gian $m$ chiều: $b, r \in \mathbb{R}^m$. Hàng thứ $i$ của ma trận $A$ (ký hiệu $a_i^T$) chứa đựng toàn bộ thông tin đặc trưng của mẫu thứ $i$, và tích vô hướng $a_i^T w$ sinh ra đúng giá trị dự đoán cho mẫu đó.

Một cách người ta hay dùng trong thực tế để không bao giờ nhầm lẫn chiều khi nhân ma trận là quy tắc **"khớp ở giữa, nở hai đầu"**: Khi nhân ma trận kích thước $(m \times k)$ với ma trận kích thước $(k \times n)$, hai chỉ số ở giữa bắt buộc phải trùng nhau để các phép nhân tích vô hướng thực hiện được, và kết quả thu được sẽ có kích thước chính là hai đầu ngoài cùng $(m \times n)$. Trong kỹ nghệ học sâu, tư duy ma trận hóa này (vectorization) giúp thuật toán chạy nhanh hơn hàng trăm lần trên phần cứng GPU/TPU so với các vòng lặp tuần tự.

---

## 2. Chuẩn vector và Chuẩn ma trận

Làm thế nào để đo lường độ lớn của một vector hoặc kích thước của một ma trận toán tử? Để làm được điều này, ta cần đến khái niệm **Chuẩn (Norm)**.

### 2.1. Chuẩn vector
Với hai vector $u, v \in \mathbb{R}^n$, **tích vô hướng** (inner product) được định nghĩa là:

$$
u^T v = \sum_{j=1}^n u_j v_j = u_1 v_1 + u_2 v_2 + \dots + u_n v_n.
$$

Cần phân biệt rõ: Đại lượng $u^T v$ là một số thực vô hướng (scalar), trong khi tích ngoài $u v^T$ lại tạo ra một ma trận kích thước $n \times n$. Hai cấu trúc này hoàn toàn khác biệt và không được hoán đổi cho nhau.

Các chuẩn vector thông dụng nhất trong học máy bao gồm:
1. **Chuẩn Euclid ($L_2$)**: Đo khoảng cách hình học thẳng hàng từ gốc tọa độ:
   $$
   \|u\|_2 = \sqrt{u^T u} = \sqrt{\sum_{j=1}^n u_j^2}.
   $$
2. **Chuẩn $L_1$ (Manhattan)**: Tổng giá trị tuyệt đối các tọa độ:
   $$
   \|u\|_1 = \sum_{j=1}^n |u_j| = |u_1| + |u_2| + \dots + |u_n|.
   $$
   Chuẩn $L_1$ đóng vai trò cốt tử trong hồi quy Lasso và nén tín hiệu nhờ đặc tính thúc đẩy nghiệm thưa (sparse solution).
3. **Chuẩn cực đại ($L_\infty$)**: Độ lệch lớn nhất trong các thành phần:
   $$
   \|u\|_\infty = \max_{1 \le j \le n} |u_j|.
   $$
4. **Chuẩn bậc $p$ tổng quát ($L_p$)**: Với $p \ge 1$:
   $$
   \|u\|_p = \left( \sum_{j=1}^n |u_j|^p \right)^{1/p}.
   $$

### 2.2. Chuẩn ma trận
Với ma trận $A \in \mathbb{R}^{m \times n}$, hai chuẩn quan trọng nhất là:
1. **Chuẩn Frobenius**: Tương đương với chuẩn Euclid coi ma trận như một vector kéo dài:
   $$
   \|A\|_F = \sqrt{\operatorname{tr}(A^T A)} = \sqrt{\sum_{i=1}^m \sum_{j=1}^n A_{ij}^2}.
   $$
2. **Chuẩn phổ (Spectral Norm / Chuẩn cảm sinh $L_2$)**: Đo độ khuếch đại lớn nhất mà ma trận $A$ có thể tác động lên một vector đơn vị:
   $$
   \|A\|_2 = \sup_{x \ne 0} \frac{\|A x\|_2}{\|x\|_2} = \sigma_{\max}(A),
   $$
   trong đó $\sigma_{\max}(A)$ là giá trị kỳ dị lớn nhất của ma trận $A$.

---

## 3. Giải tích ma trận và Đạo hàm nhiều biến

Khi tối ưu hóa các hàm số nhận đầu vào là vector hoặc ma trận, việc thành thạo các quy tắc đạo hàm ma trận là điều kiện bắt buộc để tính toán gradient nhanh chóng và chính xác.

### 3.1. Gradient và Vi phân toàn phần
Cho hàm mục tiêu khả vi $f: \mathbb{R}^n \to \mathbb{R}$. Vector **gradient** là vector cột chứa toàn bộ các đạo hàm riêng bậc nhất:

$$
\nabla f(w) = \begin{bmatrix} \frac{\partial f}{\partial w_1} \\ \vdots \\ \frac{\partial f}{\partial w_n} \end{bmatrix} \in \mathbb{R}^n.
$$

Mối liên hệ giữa gradient và vi phân toàn phần cấp một $df$:

$$
df = \sum_{j=1}^n \frac{\partial f}{\partial w_j} dw_j = (\nabla f(w))^T dw.
$$

Quy tắc vi phân này là bí quyết giúp ta tìm gradient của các biểu thức ma trận phức tạp mà không cần tách rời từng tọa độ.

### 3.2. Một số công thức đạo hàm ma trận cốt lõi
1. **Hàm tuyến tính**: Xét $f(w) = a^T w$. Vi phân $df = a^T dw$, suy ra:
   $$
   \nabla_w (a^T w) = a.
   $$
2. **Hàm toàn phương**: Xét $f(w) = \frac{1}{2} w^T P w$ với ma trận đối xứng $P = P^T$. Vi phân:
   $$
   df = \frac{1}{2} (dw^T P w + w^T P dw) = w^T P dw = (P w)^T dw \implies \nabla_w \left(\frac{1}{2} w^T P w\right) = P w.
   $$
3. **Đạo hàm theo vết ma trận (Trace)**:
   $$
   \nabla_X \operatorname{tr}(A X) = A^T, \qquad \nabla_X \operatorname{tr}(X^T A X) = (A + A^T) X.
   $$
4. **Đạo hàm của Logarit Định thức**: Cho ma trận đối xứng dương xác định $X \succ 0$:
   $$
   \nabla_X \log\det(X) = X^{-1}.
   $$

### 3.3. Gradient của Hàm mất mát Bình phương tối thiểu
Xét hàm mất mát:

$$
f(w) = \frac{1}{2} \|A w - b\|_2^2 = \frac{1}{2} (A w - b)^T (A w - b).
$$

Khai triển hàm mất mát:

$$
f(w) = \frac{1}{2} w^T A^T A w - b^T A w + \frac{1}{2} b^T b.
$$

Lấy vi phân theo biến $w$:

$$
df = w^T A^T A dw - b^T A dw = (A^T A w - A^T b)^T dw = [A^T (A w - b)]^T dw.
$$

Từ đó, ta thu được công thức gradient chuẩn mực:

$$
\boxed{\nabla f(w) = A^T r = A^T (A w - b).}
$$

Ý nghĩa hình học của gradient: **Vector gradient $\nabla f(w)$ luôn chỉ về hướng hàm số tăng nhanh nhất (dốc nhất)**. Do đó, hướng di chuyển tự nhiên để hạ thấp sai số là hướng ngược chiều gradient: Hướng $- \nabla f(w)$. Đây chính là nguyên lý của phương pháp **Gradient Descent**.

---

## 4. Ma trận Hessian, Tính xác định dương và Phần bù Schur

### 4.1. Ma trận Hessian và Khai triển Taylor bậc hai
Ma trận **Hessian** $H = \nabla^2 f(w) \in \mathbb{R}^{n \times n}$ tập hợp toàn bộ các đạo hàm riêng bậc hai:

$$
H_{ij} = \frac{\partial^2 f}{\partial w_i \partial w_j}.
$$

Hessian phản ánh độ cong địa hình của hàm mục tiêu qua khai triển Taylor bậc hai quanh điểm $w$:

$$
f(w + d) \approx f(w) + \nabla f(w)^T d + \frac{1}{2} d^T H d.
$$

Độ cong của hàm số theo hướng dịch chuyển $d \in \mathbb{R}^n$ được định đoạt bởi dạng toàn phương $d^T H d$:
- Nếu $d^T H d > 0$: Địa hình uốn cong lên trên theo hướng $d$ (đáy thung lũng).
- Nếu $d^T H d < 0$: Địa hình uốn cong xuống dưới theo hướng $d$ (đỉnh đồi).
- Nếu $d^T H d = 0$: Địa hình phẳng tuyến tính theo hướng $d$.

Với hàm mất mát bình phương tối thiểu $f(w) = \frac{1}{2}\|Aw - b\|_2^2$, đạo hàm của gradient $\nabla f(w) = A^TAw - A^Tb$ cho ra ma trận Hessian hằng số:

$$
H = \nabla^2 f(w) = A^T A.
$$

Dạng toàn phương của ma trận này với mọi vector $d \in \mathbb{R}^n$:

$$
d^T H d = d^T (A^T A) d = (A d)^T (A d) = \|A d\|_2^2 \ge 0.
$$

Vì chuẩn Euclid của một vector luôn không âm, ta có $d^T H d \ge 0$ với mọi hướng $d$. Một ma trận đối xứng thỏa mãn điều kiện này được gọi là **ma trận nửa xác định dương** (Positive Semidefinite, ký hiệu $H \succeq 0$). Điều này chứng minh rằng mặt mất mát của bài toán bình phương tối thiểu luôn là một mặt lồi paraboloid hướng lên trên.

Để Hessian là **dương xác định ngặt** (Positive Definite, ký hiệu $H \succ 0$, tức $d^T H d > 0$ với mọi $d \ne 0$), điều kiện cần và đủ là các cột của ma trận dữ liệu $A$ phải độc lập tuyến tính (ma trận $A$ đủ hạng cột: $\operatorname{rank}(A) = n$). Khi đó, nghiệm cực tiểu toàn cục được bảo đảm là duy nhất.

### 4.2. Phần bù Schur (Schur Complement)
Xét một ma trận khối đối xứng kích thước $(p + q) \times (p + q)$:

$$
M = \begin{bmatrix} A & B \\ B^T & C \end{bmatrix},
$$

trong đó $A \in \mathbb{S}^p$, $C \in \mathbb{S}^q$, và $B \in \mathbb{R}^{p \times q}$. Giả sử ma trận khối con $A$ khả nghịch ($A \succ 0$).

Ma trận **phần bù Schur** của $A$ trong $M$ được định nghĩa là:

$$
S = C - B^T A^{-1} B.
$$

> **Bổ đề Phần bù Schur**:
> 1. Ma trận khối $M$ dương xác định ($M \succ 0$) khi và chỉ khi:
>    $$
>    A \succ 0 \quad \text{và} \quad C - B^T A^{-1} B \succ 0.
>    $$
> 2. Nếu $A \succ 0$, ma trận khối $M$ nửa xác định dương ($M \succeq 0$) khi và chỉ khi:
>    $$
>    C - B^T A^{-1} B \succeq 0.
>    $$

**Ý nghĩa và Ứng dụng trong AI**:
- **Khử biến toàn phương**: Cực tiểu hóa dạng toàn phương theo biến $x$ trong biểu thức $\begin{bmatrix} x \\ y \end{bmatrix}^T \begin{bmatrix} A & B \\ B^T & C \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$ cho ra đúng dạng toàn phương thu gọn theo biến $y$: $y^T (C - B^T A^{-1} B) y$.
- **Phân phối chuẩn có điều kiện**: Nếu vector ghép $(X, Y)$ tuân theo phân phối Gauss với ma trận hiệp phương sai khối, ma trận hiệp phương sai của phân phối có điều kiện $Y \mid X$ chính là phần bù Schur của khối $X$.
- **Chuyển đổi bất đẳng thức ma trận tuyến tính (LMI)**: Phần bù Schur cho phép biến đổi các ràng buộc phi tuyến lồi (như $x^T P x \le t$) thành bất đẳng thức ma trận tuyến tính chuẩn tắc trong Quy hoạch nửa xác định (SDP).

---

## 5. Phân tích giá trị kỳ dị (SVD) và Ý nghĩa hình học

Mọi ma trận thực $A \in \mathbb{R}^{m \times n}$ đều có thể phân tích thành tích của ba ma trận:

$$
A = U \Sigma V^T,
$$

trong đó:
- $U \in \mathbb{R}^{m \times m}$ là ma trận trực giao ($U^T U = I_m$), các cột của $U$ là các vector kỳ dị trái (left singular vectors).
- $V \in \mathbb{R}^{n \times n}$ là ma trận trực giao ($V^T V = I_n$), các cột của $V$ là các vector kỳ dị phải (right singular vectors).
- $\Sigma \in \mathbb{R}^{m \times n}$ là ma trận đường chéo chữ nhật chứa các **giá trị kỳ dị** được xếp theo thứ tự giảm dần:
  $$
  \sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0 = \sigma_{r+1} = \dots = 0,
  $$
  với $r = \operatorname{rank}(A)$ là hạng của ma trận.

### 5.1. Ý nghĩa hình học của SVD
Phép nhân ma trận $x \mapsto A x$ có thể phân rã thành ba bước hình học cơ bản:
1. **Phép quay/phản xạ trong không gian gốc $\mathbb{R}^n$**: Nhân với ma trận trực giao $V^T$, chuyển hệ tọa độ sang các trục trực chuẩn $v_i$.
2. **Phép co giãn dọc theo các trục tọa độ**: Nhân với ma trận đường chéo $\Sigma$, kéo dãn vector theo từng trục với hệ số co giãn đúng bằng các giá trị kỳ dị $\sigma_i$.
3. **Phép quay/phản xạ trong không gian đích $\mathbb{R}^m$**: Nhân với ma trận trực giao $U$, đưa các trục đã co giãn về hướng của các vector trực chuẩn $u_i$.

Hệ quả hình học: Ma trận $A$ biến đổi quả cầu đơn vị $\|x\|_2 \le 1$ trong $\mathbb{R}^n$ thành một **khối ellipsoid** trong $\mathbb{R}^m$, với độ dài các bán trục chính đúng bằng các giá trị kỳ dị $\sigma_i$ và các trục đối xứng có phương trùng với các vector $u_i$.

### 5.2. Số điều kiện của ma trận (Condition Number)
Số điều kiện của ma trận khả nghịch $A \in \mathbb{R}^{n \times n}$ được định nghĩa là tỷ số giữa giá trị kỳ dị lớn nhất và nhỏ nhất:

$$
\kappa(A) = \frac{\sigma_{\max}(A)}{\sigma_{\min}(A)} = \frac{\sigma_1}{\sigma_n} \ge 1.
$$

Ý nghĩa thực tiễn:
- Nếu $\kappa(A) \approx 1$: Ma trận có điều hòa tốt (well-conditioned). Địa hình hàm mất mát gần như hình tròn đồng mức, thuật toán gradient descent hội tụ rất nhanh.
- Nếu $\kappa(A) \gg 1$: Ma trận có điều hòa xấu (ill-conditioned). Địa hình mất mát là một thung lũng hẹp và dài (khe núi sâu), gradient descent sẽ dao động zig-zag dữ dội và hội tụ rất chậm.

---

## 6. Đại số tuyến tính số trong Tối ưu hóa (Numerical Linear Algebra)

Khi triển khai các thuật toán tối ưu hóa trong thực tế, việc hiểu rõ chi phí tính toán và tính ổn định số học của các thuật toán đại số tuyến tính là kỹ năng phân biệt giữa một người làm lý thuyết thuần túy và một kỹ sư tính toán thực thụ.

### 6.1. Đơn vị đo độ phức tạp: Flop
Một **flop** (floating-point operation) là một phép tính số thực dấu phẩy động cơ bản gồm một phép cộng, trừ, nhân, hoặc chia.

Chi phí tính toán của các thao tác đại số cơ bản:
- Tích vô hướng của hai vector $x, y \in \mathbb{R}^n$: Tiêu tốn $2n$ flops (bao gồm $n$ phép nhân và $n-1$ phép cộng).
- Nhân ma trận với vector $A x$ với $A \in \mathbb{R}^{m \times n}$: Tiêu tốn $2mn$ flops.
- Nhân hai ma trận $A B$ với $A \in \mathbb{R}^{m \times p}$ và $B \in \mathbb{R}^{p \times n}$: Tiêu tốn $2mpn$ flops.

### 6.2. Giải hệ phương trình ma trận tam giác
Hệ phương trình có ma trận hệ số là ma trận tam giác (dưới hoặc trên) là khối cấu trúc cơ bản nhất của mọi thuật toán đại số tuyến tính số học:
1. **Thế tiến (Forward substitution)** cho hệ tam giác dưới $L y = b$ (với $L_{ii} \ne 0$):
   $$
   \begin{aligned}
   y_1 &= \frac{b_1}{L_{11}}, \\
   y_i &= \frac{1}{L_{ii}} \left( b_i - \sum_{j=1}^{i-1} L_{ij} y_j \right), \quad i = 2, \dots, n.
   \end{aligned}
   $$
   Số phép tính cần thực hiện là $\sum_{i=1}^n (2i - 1) = n^2$ flops.
2. **Thế lùi (Back substitution)** cho hệ tam giác trên $U x = y$: Hoàn toàn tương tự, giải từ $x_n$ ngược lên $x_1$ với chi phí đúng $n^2$ flops.

### 6.3. Phân tích LU cho ma trận vuông tổng quát
Với một ma trận vuông tổng quát không suy biến $A \in \mathbb{R}^{n \times n}$, phép khử Gauss với chiến lược chọn phần tử trục (pivoting) phân tích ma trận thành dạng:

$$
A = P L U,
$$

trong đó $P$ là ma trận hoán vị các hàng, $L$ là ma trận tam giác dưới với các số 1 trên đường chéo chính, và $U$ là ma trận tam giác trên không suy biến.
- Chi phí phân tích ma trận: Đạt $\frac{2}{3} n^3$ flops.
- Chi phí giải hệ $A x = b$: Sau khi đã có $P, L, U$, ta áp dụng hoán vị vector $P^T b$, giải thế tiến $L y = P^T b$ ($n^2$ flops) và giải thế lùi $U x = y$ ($n^2$ flops). Tổng chi phí giải sau khi phân tích chỉ là $2n^2$ flops.

### 6.4. Phân tích Cholesky: Cỗ máy giải hệ đối xứng xác định dương
Để giải hệ phương trình tuyến tính đối xứng xác định dương $H x = b$ (xuất hiện trong mọi bước lặp của phương pháp Newton và bài toán bình phương tối thiểu), ta không bao giờ tính ma trận nghịch đảo $H^{-1}$ một cách trực tiếp vì thao tác này vừa chậm vừa dễ tích lũy sai số số học.

Thay vào đó, ta sử dụng **Phân tích Cholesky**: Mọi ma trận đối xứng dương xác định $H \in \mathbb{S}_{++}^n$ đều có thể phân tích duy nhất thành dạng:

$$
H = L L^T,
$$

trong đó $L$ là ma trận tam giác dưới với các phần tử trên đường chéo chính dương ngặt ($L_{ii} > 0$).

Quy trình giải hệ $H x = b$ qua phân tích Cholesky gồm ba bước:
1. **Phân tích Cholesky**: Tìm ma trận tam giác dưới $L$ thỏa mãn $H = L L^T$. Chi phí tính toán là:
   $$
   \frac{1}{3} n^3 \text{ flops}.
   $$
2. **Thế tiến (Forward substitution)**: Giải hệ tam giác dưới $L y = b$. Chi phí là $n^2$ flops.
3. **Thế lùi (Back substitution)**: Giải hệ tam giác trên $L^T x = y$. Chi phí là $n^2$ flops.

Tổng chi phí để giải hệ là $\frac{1}{3} n^3 + 2n^2 \approx \frac{1}{3} n^3$ flops. Phân tích Cholesky nhanh gấp đôi phân tích LU tổng quát ($\frac{2}{3} n^3$ flops), tiết kiệm một nửa bộ nhớ lưu trữ vì chỉ cần lưu nửa tam giác dưới, và có độ ổn định số học tối ưu mà không cần bất kỳ hoán vị hàng nào.

### 6.5. Phân tích $LDL^T$ cho ma trận đối xứng không xác định dấu
Trong các bài toán tối ưu có ràng buộc đẳng thức, ma trận hệ KKT có dạng:

$$
K = \begin{bmatrix} H & A^T \\ A & 0 \end{bmatrix}.
$$

Ma trận $K$ đối xứng nhưng không xác định dương (nó luôn có cả giá trị riêng dương và giá trị riêng âm, tạo thành điểm yên ngựa). Ta không thể dùng phân tích Cholesky trực tiếp cho $K$.

Giải pháp tối ưu số học là **Phân tích $LDL^T$ với ma trận hoán vị**:

$$
K = P L D L^T P^T,
$$

trong đó $P$ là ma trận hoán vị, $L$ là ma trận tam giác dưới với đường chéo gồm các số 1, và $D$ là ma trận đường chéo khối gồm các khối con kích thước $1 \times 1$ và $2 \times 2$.
- Thuật toán Bunch–Kaufman tự động chọn các khối $1 \times 1$ hoặc $2 \times 2$ trên đường chéo để bảo đảm độ ổn định số học mà vẫn duy trì tính đối xứng.
- Chi phí phân tích: Đúng $\frac{1}{3} n^3$ flops, bằng một nửa chi phí phân tích LU tổng quát.

### 6.6. Khử ma trận khối (Block Elimination) và Phần bù Schur
Xét hệ phương trình tuyến tính cấu trúc khối:

$$
\begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \end{bmatrix},
$$

trong đó $A_{11} \in \mathbb{R}^{n_1 \times n_1}$ là ma trận không suy biến.
Ta có thể khử biến $x_1$ từ phương trình thứ nhất:
$$
x_1 = A_{11}^{-1} (b_1 - A_{12} x_2).
$$
Thay biểu thức này vào phương trình thứ hai:
$$
A_{21} A_{11}^{-1} (b_1 - A_{12} x_2) + A_{22} x_2 = b_2,
$$
dẫn đến hệ phương trình rút gọn theo riêng biến $x_2$:
$$
S x_2 = b_2 - A_{21} A_{11}^{-1} b_1,
$$
trong đó $S = A_{22} - A_{21} A_{11}^{-1} A_{12}$ chính là **Phần bù Schur** của khối $A_{11}$.

Quy trình giải hệ bằng phương pháp khử khối:
1. Giải $A_{11} \hat{x}_1 = b_1$ và giải $A_{11} Z = A_{12}$ (gồm $n_2$ hệ phương trình với cùng ma trận hệ số $A_{11}$).
2. Tính phần bù Schur $S = A_{22} - A_{21} Z$ và vế phải $\tilde{b}_2 = b_2 - A_{21} \hat{x}_1$.
3. Giải hệ phương trình kích thước nhỏ $S x_2 = \tilde{b}_2$.
4. Thu hồi nghiệm $x_1$: Giải $A_{11} x_1 = b_1 - A_{12} x_2$.

Phương pháp này rất hiệu quả khi $n_2 \ll n_1$ hoặc khi khối $A_{11}$ có cấu trúc đặc biệt (như ma trận đường chéo, ma trận băng hoặc phân tích Cholesky của nó đã được tính sẵn).

### 6.7. Công thức cập nhật Sherman–Morrison–Woodbury
Khi giải một chuỗi các hệ phương trình tuyến tính mà ma trận hệ số chỉ bị biến đổi bởi một số hạng hạng thấp (low-rank perturbation):

$$
(A + U C V)^{-1} = A^{-1} - A^{-1} U (C^{-1} + V A^{-1} U)^{-1} V A^{-1},
$$

với $A \in \mathbb{R}^{n \times n}$, $U \in \mathbb{R}^{n \times p}$, $C \in \mathbb{R}^{p \times p}$ và $V \in \mathbb{R}^{p \times n}$.
- Khi $p \ll n$, thay vì phải tính nghịch đảo ma trận $n \times n$ với chi phí $O(n^3)$, ta chỉ cần nghịch đảo ma trận kích thước nhỏ $p \times p$ với chi phí $O(p^3)$ cộng với các phép nhân ma trận.
- Công thức này là nền tảng của bộ lọc Kalman, thuật toán cập nhật Quasi-Newton (BFGS, DFP, SR1), và các mô hình học trực tuyến (Online Learning).

### 6.8. Khai thác Cấu trúc Ma trận Thưa và Ma trận Băng
Trong các bài toán học máy quy mô lớn (như đồ thị, bài toán quy hoạch mạng lưới, hay mô hình chuỗi thời gian), ma trận dữ liệu và ma trận Hessian thường chứa phần lớn phần tử bằng 0 (**ma trận thưa - sparse matrix**).

Nếu ma trận $H \in \mathbb{R}^{n \times n}$ là ma trận dạng băng (banded matrix) với độ rộng băng $k \ll n$ (chỉ có các phần tử cách đường chéo chính không quá $k$ vị trí là khác 0):
- Chi phí phân tích Cholesky giảm từ $O(n^3)$ xuống chỉ còn $O(n k^2)$ flops.
- Khi $k$ cố định, độ phức tạp là **tuyến tính $O(n)$** theo số chiều biến. Việc nhận diện và khai thác cấu trúc thưa giúp giảm thời gian giải bài toán từ nhiều ngày xuống vài giây.

---

## 7. Mật độ xác suất và Phân phối chuẩn Gauss

Tại sao trong thực tế người ta lại chọn chuẩn bình phương $\|Aw - b\|_2^2$ để tối ưu mà không phải chuẩn bậc 3 hay bậc 4? Để trả lời thấu đáo câu hỏi này, ta cần xem xét bài toán qua lăng kính của lý thuyết xác suất và thống kê.

Với một biến ngẫu nhiên liên tục $Z$ có hàm mật độ xác suất $p(z)$, xác suất để $Z$ rơi vào một khoảng $[a, b]$ được tính bằng tích phân của hàm mật độ:

$$
P(a \le Z \le b) = \int_a^b p(z) \, dz.
$$

Lưu ý rằng giá trị hàm mật độ $p(z)$ tại một điểm không phải là xác suất sinh ra đúng điểm đó (đối với biến liên tục, xác suất tại một điểm đơn lẻ luôn bằng 0). Hai đặc trưng quan trọng của phân phối là **kỳ vọng** $\mathbb{E}[Z] = \int z p(z) dz$ (trọng tâm phân phối) và **phương sai** $\operatorname{Var}(Z) = \mathbb{E}[(Z - \mathbb{E}[Z])^2]$ (mức độ phân tán quanh trọng tâm).

**Phân phối chuẩn (Gauss)** một biến với kỳ vọng $\mu$ và phương sai $\sigma^2 > 0$ có hàm mật độ hình chuông:

$$
p(z) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[ -\frac{(z - \mu)^2}{2\sigma^2} \right].
$$

Khi mở rộng sang vector ngẫu nhiên $Z \in \mathbb{R}^m$ với vector kỳ vọng $\mu \in \mathbb{R}^m$ và ma trận hiệp phương sai đối xứng dương xác định $\Sigma \succ 0$, hàm mật độ Gauss đa biến có dạng:

$$
p(z) = \frac{1}{(2\pi)^{m/2} \sqrt{\det\Sigma}} \exp\left[ -\frac{1}{2} (z - \mu)^T \Sigma^{-1} (z - \mu) \right].
$$

- Ma trận hiệp phương sai $\Sigma$ lưu giữ phương sai của từng thành phần trên đường chéo chính ($\Sigma_{ii} = \sigma_i^2$) và mức độ tương quan tuyến tính giữa các cặp thành phần ở các vị trí ngoài đường chéo ($\Sigma_{ij} = \operatorname{Cov}(Z_i, Z_j)$).
- Định thức $\det\Sigma$ phản ánh thể tích của ellipsoid phân tán dữ liệu, đóng vai trò chuẩn hóa diện tích tích phân của hàm mật độ về đúng bằng 1.
- Khi các thành phần sai số độc lập thống kê và có cùng phương sai $\sigma^2$, ma trận hiệp phương sai trở thành ma trận đường chéo $\Sigma = \sigma^2 I_m$. Lúc này, mật độ đa biến phân rã thành tích của $m$ mật độ Gauss độc lập: $p(z) = \prod_{i=1}^m p(z_i)$.

---

## 8. Cội nguồn xác suất của Bài toán Bình phương tối thiểu

Giờ đây ta có thể nhìn thấy mối liên hệ trực tiếp giữa học máy và xác suất thống kê.

Giả sử trong thực tế, quá trình sinh dữ liệu tuân theo mô hình tuyến tính bị làm nhiễu:

$$
b_i = a_i^T w + \varepsilon_i, \qquad \varepsilon_i \overset{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2).
$$

Nghĩa là nhãn thực tế $b_i$ là một biến ngẫu nhiên có kỳ vọng đúng bằng giá trị mô hình dự đoán $\mathbb{E}[b_i] = a_i^T w$, và bị sai lệch bởi một nhiễu ngẫu nhiên Gauss $\varepsilon_i$ không thiên vị với phương sai $\sigma^2$.

Theo mô hình này, mật độ xác suất có điều kiện của nhãn $b_i$ khi biết tham số $w$ là:

$$
p(b_i \mid w) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[ -\frac{(b_i - a_i^T w)^2}{2\sigma^2} \right].
$$

Vì các quan sát độc lập với nhau, xác suất đồng thời (hàm **Likelihood**, tức hàm hợp lý) của toàn bộ tập dữ liệu $b = (b_1, \dots, b_m)^T$ bằng tích các mật độ thành phần:

$$
\begin{aligned}
L(w) &= p(b \mid w) = \prod_{i=1}^m p(b_i \mid w) \\
&= \left( \frac{1}{2\pi\sigma^2} \right)^{m/2} \exp\left[ -\frac{1}{2\sigma^2} \sum_{i=1}^m (a_i^T w - b_i)^2 \right].
\end{aligned}
$$

Triết lý ước lượng hợp lý cực đại (**Maximum Likelihood Estimation - MLE**): Ta muốn tìm bộ tham số $w$ sao cho khả năng quan sát được tập dữ liệu hiện có trong thực tế là lớn nhất.

Để cực đại hóa một tích các hàm mũ, trong toán tối ưu người ta dùng phép biến đổi lấy **âm logarit tự nhiên** (Negative Log-Likelihood - NLL). Do hàm logarit đơn điệu tăng ngặt, việc cực đại hóa $L(w)$ hoàn toàn tương đương với việc cực tiểu hóa $-\log L(w)$:

$$
-\log p(b \mid w) = \frac{m}{2} \log(2\pi\sigma^2) + \frac{1}{2\sigma^2} \|Aw - b\|_2^2.
$$

Quan sát biểu thức trên:
- Số hạng đầu tiên $\frac{m}{2}\log(2\pi\sigma^2)$ là một hằng số độc lập với tham số $w$.
- Hệ số $\frac{1}{2\sigma^2}$ là một số dương cố định.

Do đó, bài toán tìm tham số $w$ để cực đại hóa hàm hợp lý Likelihood quy về chính xác:

$$
\arg\min_w \left[ -\log p(b \mid w) \right] \equiv \arg\min_w \frac{1}{2} \|Aw - b\|_2^2.
$$

Tiêu chuẩn bình phương tối thiểu không phải là một công thức cảm tính được chọn ngẫu nhiên. Nó là hệ quả toán học trực tiếp của nguyên lý cực đại hóa hàm hợp lý dưới giả thiết sai số quan sát tuân theo phân phối chuẩn Gauss độc lập.

Nếu các sai số quan sát có tương quan lẫn nhau với ma trận hiệp phương sai tổng quát $\Sigma \succ 0$, biểu thức NLL sẽ dẫn tới hàm mất mát bình phương có trọng số:

$$
f(w) = \frac{1}{2} (Aw - b)^T \Sigma^{-1} (Aw - b).
$$

Mỗi quan sát có phương sai lớn sẽ tự động bị ma trận $\Sigma^{-1}$ giảm trọng số ảnh hưởng trong hàm mất mát.

---

## 9. Hệ thống Bài tập Tự luyện Chuyên sâu

::: exercise 1. Kiểm tra tính xác định dương và Phần bù Schur cho ma trận khối
Xét ma trận khối đối xứng:
$$
M = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & c \end{bmatrix},
$$
trong đó $c \in \mathbb{R}$ là tham số thực.
1. Hãy phân rã ma trận $M$ thành cấu trúc khối $\begin{bmatrix} A & B \\ B^T & C \end{bmatrix}$ với khối con $A$ kích thước $2 \times 2$.
2. Tính phần bù Schur $S = C - B^T A^{-1} B$.
3. Sử dụng Bổ đề phần bù Schur để tìm điều kiện cần và đủ của $c$ để ma trận $M$ dương xác định ($M \succ 0$).
:::
::: solution
**Lời giải**:
1. Phân rã ma trận thành cấu trúc khối:
   $$
   A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}, \qquad B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}, \qquad C = [c].
   $$
   Khối con $A$ đối xứng, có định thức $\det(A) = 2(2) - 1(1) = 3 > 0$ và phần tử góc $A_{11} = 2 > 0$, do đó $A \succ 0$.

2. Tính ma trận nghịch đảo của $A$:
   $$
   A^{-1} = \frac{1}{3} \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}.
   $$
   Tính tích $B^T A^{-1} B$:
   $$
   B^T A^{-1} B = \begin{bmatrix} 0 & 1 \end{bmatrix} \left( \frac{1}{3} \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} \right) \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} -1 & 2 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \frac{2}{3}.
   $$
   Phần bù Schur là:
   $$
   S = C - B^T A^{-1} B = c - \frac{2}{3}.
   $$

3. Theo Bổ đề phần bù Schur, vì $A \succ 0$, ma trận khối $M \succ 0$ khi và chỉ khi $S > 0$:
   $$
   c - \frac{2}{3} > 0 \iff c > \frac{2}{3}.
   $$
   Như vậy, điều kiện cần và đủ để ma trận $M$ dương xác định là $c > \frac{2}{3}$.
:::

::: exercise 2. Thực hiện phân tích Cholesky và Giải hệ phương trình chuẩn tắc
Cho ma trận đối xứng dương xác định:
$$
H = \begin{bmatrix} 4 & 2 \\ 2 & 10 \end{bmatrix}, \qquad b = \begin{bmatrix} 8 \\ 16 \end{bmatrix}.
$$
1. Hãy tìm ma trận tam giác dưới $L = \begin{bmatrix} l_{11} & 0 \\ l_{21} & l_{22} \end{bmatrix}$ trong phân tích Cholesky $H = L L^T$.
2. Áp dụng phương pháp thế tiến và thế lùi để giải hệ phương trình $H x = b$.
:::
::: solution
**Lời giải**:
1. Khai triển tích $L L^T$:
   $$
   L L^T = \begin{bmatrix} l_{11} & 0 \\ l_{21} & l_{22} \end{bmatrix} \begin{bmatrix} l_{11} & l_{21} \\ 0 & l_{22} \end{bmatrix} = \begin{bmatrix} l_{11}^2 & l_{11} l_{21} \\ l_{11} l_{21} & l_{21}^2 + l_{22}^2 \end{bmatrix}.
   $$
   Đồng nhất các phần tử với ma trận $H$:
   - $l_{11}^2 = 4 \implies l_{11} = 2$ (chọn phần tử đường chéo dương).
   - $l_{11} l_{21} = 2 \implies 2 l_{21} = 2 \implies l_{21} = 1$.
   - $l_{21}^2 + l_{22}^2 = 10 \implies l_{22}^2 = 9$, suy ra $l_{22} = 3$.
   Do đó, ma trận Cholesky là:
   $$
   L = \begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix}.
   $$

2. Giải hệ phương trình $H x = b$ qua hai bước:
   - **Bước 1 (Thế tiến $L y = b$)**:
     $$
     \begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix} 8 \\ 16 \end{bmatrix} \implies \begin{cases} 2 y_1 = 8 \implies y_1 = 4, \\ 1(4) + 3 y_2 = 16 \implies 3 y_2 = 12 \implies y_2 = 4. \end{cases}
     $$
     Suy ra $y = \begin{bmatrix} 4 \\ 4 \end{bmatrix}$.
   - **Bước 2 (Thế lùi $L^T x = y$)**:
     $$
     \begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 4 \\ 4 \end{bmatrix} \implies \begin{cases} 3 x_2 = 4 \implies x_2 = \frac{4}{3}, \\ 2 x_1 + \frac{4}{3} = 4 \implies 2 x_1 = \frac{8}{3} \implies x_1 = \frac{4}{3}. \end{cases}
     $$
     Nghiệm duy nhất của hệ là $x = \begin{bmatrix} 4/3 \\ 4/3 \end{bmatrix}$.
:::

::: exercise 3. Phân tích SVD và Độ co giãn của ma trận dữ liệu
Cho ma trận $A = \begin{bmatrix} 3 & 0 \\ 0 & -2 \end{bmatrix}$.
1. Hãy xác định các giá trị kỳ dị $\sigma_1, \sigma_2$ và số điều kiện $\kappa(A)$.
2. Mô tả hình học ảnh của quả cầu đơn vị $\|x\|_2 \le 1$ qua ánh xạ $A$.
:::
::: solution
**Lời giải**:
1. Xét ma trận $A^T A = \begin{bmatrix} 9 & 0 \\ 0 & 4 \end{bmatrix}$.
   Các giá trị riêng của $A^T A$ là $\lambda_1 = 9$ và $\lambda_2 = 4$.
   Các giá trị kỳ dị của $A$ là căn bậc hai của các giá trị riêng này:
   $$
   \sigma_1 = \sqrt{9} = 3, \qquad \sigma_2 = \sqrt{4} = 2.
   $$
   Số điều kiện của ma trận là:
   $$
   \kappa(A) = \frac{\sigma_1}{\sigma_2} = \frac{3}{2} = 1.5.
   $$

2. Xét điểm $x = (x_1, x_2)^T$ nằm trên biên của quả cầu đơn vị: $x_1^2 + x_2^2 = 1$.
   Ảnh của $x$ qua ánh xạ $A$ là $y = A x = (3 x_1, -2 x_2)^T$.
   Đặt $y_1 = 3 x_1 \implies x_1 = y_1/3$ và $y_2 = -2 x_2 \implies x_2 = -y_2/2$.
   Thay vào phương trình quả cầu đơn vị:
   $$
   \left(\frac{y_1}{3}\right)^2 + \left(-\frac{y_2}{2}\right)^2 = 1 \iff \frac{y_1^2}{3^2} + \frac{y_2^2}{2^2} = 1.
   $$
   Đây chính là phương trình của một hình ellipse trong mặt phẳng với bán trục lớn bằng $\sigma_1 = 3$ dọc theo trục hoành và bán trục nhỏ bằng $\sigma_2 = 2$ dọc theo trục tung. Ánh xạ ma trận $A$ đã kéo giãn quả cầu tròn thành một khối ellipse có kích thước đúng bằng các giá trị kỳ dị.
:::

::: exercise 4. So sánh chi phí Flops và Thuật toán Khử khối Schur cho Hệ KKT
Xét hệ phương trình Newton–KKT xuất hiện trong tối ưu hóa có ràng buộc đẳng thức:
$$
\begin{bmatrix} H & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} v \\ w \end{bmatrix} = - \begin{bmatrix} g \\ h \end{bmatrix},
$$
trong đó $H \in \mathbb{S}_{++}^n$ đối xứng xác định dương và $A \in \mathbb{R}^{p \times n}$ có đủ hạng hàng ($p \le n$).
1. Trình bày chi tiết thuật toán khử ma trận khối bằng phần bù Schur để tìm nghiệm $(v, w)$.
2. Phân tích chi phí tính toán (số flops) khi giải hệ theo phương pháp khử khối:
   - Phân tích Cholesky ma trận $H = L L^T$.
   - Tính ma trận phần bù Schur $S = -A H^{-1} A^T$ thông qua giải $p$ hệ tam giác.
   - Giải hệ phương trình theo biến đối ngẫu $w$ và thu hồi nghiệm nguyên thủy $v$.
3. So sánh chi phí này với phương pháp giải trực tiếp bằng phân tích $LDL^T$ trên toàn bộ ma trận kích thước $(n+p) \times (n+p)$ khi số ràng buộc nhỏ hơn rất nhiều số chiều biến ($p \ll n$).
:::
::: solution
**Lời giải**:
1. Thuật toán khử ma trận khối Schur:
   - Từ phương trình thứ nhất, biểu diễn $v$ theo $w$:
     $$
     H v + A^T w = -g \implies v = -H^{-1} g - H^{-1} A^T w.
     $$
   - Thế biểu thức của $v$ vào phương trình thứ hai $A v = -h$:
     $$
     A (-H^{-1} g - H^{-1} A^T w) = -h \iff (A H^{-1} A^T) w = h - A H^{-1} g.
     $$
   - Đặt $M = A H^{-1} A^T = -S$. Vì $H \succ 0$ và $A$ đủ hạng hàng, ma trận $M \in \mathbb{S}_{++}^p$ đối xứng dương xác định.
   - Sau khi giải tìm được $w$, ta thu hồi $v$ từ phương trình: $H v = -(g + A^T w)$.

2. Phân tích chi phí Flops theo từng công đoạn:
   - Phân tích Cholesky $H = L L^T$: Tốn $\frac{1}{3} n^3$ flops.
   - Tính $H^{-1} A^T$: Giải $p$ hệ phương trình $H Z = A^T$ (với $Z = H^{-1} A^T \in \mathbb{R}^{n \times p}$) bằng hai lần thế tam giác qua $L$ và $L^T$. Mỗi vector cột tốn $2n^2$ flops, tổng cộng tốn $2p n^2$ flops.
   - Tính tích ma trận $M = A Z = A H^{-1} A^T$: Nhân ma trận $p \times n$ với ma trận $n \times p$, tận dụng tính đối xứng chỉ cần tính nửa tam giác, tốn khoảng $p^2 n$ flops.
   - Phân tích Cholesky ma trận kích thước nhỏ $M$ ($p \times p$): Tốn $\frac{1}{3} p^3$ flops.
   - Giải tìm $w$ và thu hồi $v$: Tốn thêm $2p^2 + 2n^2$ flops (các số hạng bậc hai nhỏ).
   - Tổng chi phí chủ đạo của phương pháp khử khối là:
     $$
     \frac{1}{3} n^3 + 2 p n^2 + p^2 n + \frac{1}{3} p^3 \text{ flops}.
     $$

3. So sánh hiệu năng:
   - Nếu giải trực tiếp toàn bộ hệ kích thước $(n+p) \times (n+p)$ bằng phân tích $LDL^T$, chi phí tính toán là:
     $$
     \frac{1}{3} (n + p)^3 = \frac{1}{3} n^3 + p n^2 + p^2 n + \frac{1}{3} p^3 \text{ flops}.
     $$
   - Khi $p \ll n$ (số ràng buộc đẳng thức rất ít so với số chiều biến tối ưu, chẳng hạn $n = 10000, p = 10$):
     Chi phí của cả hai phương pháp đều bị chi phối bởi số hạng $\frac{1}{3} n^3$ flops của phân tích ma trận Hessian. Tuy nhiên, phương pháp khử khối cho phép tận dụng trực tiếp tính xác định dương của $H$ để chạy thuật toán Cholesky nhanh nhất và ổn định nhất, không cần theo dõi chiến lược chọn trục (pivoting) phức tạp của $LDL^T$.
   - Đặc biệt, nếu Hessian $H$ có cấu trúc thưa hoặc đường chéo (như trong phương pháp điểm trong), việc tính $H^{-1} A^T$ chỉ tốn $O(p n)$ flops thay vì $2pn^2$, đưa tổng chi phí của phương pháp khử khối xuống chỉ còn $O(n) + O(p^3)$ flops, nhanh hơn hàng trăm lần so với giải hệ ma trận đầy đủ!
:::

---

## Tóm tắt cốt lõi

1. **Biểu diễn ma trận**: Gom dữ liệu thành ma trận $A \in \mathbb{R}^{m \times n}$ giúp tính toán đồng thời mọi dự đoán $A w$ và phần dư $r = A w - b$, khai phóng sức mạnh xử lý song song của GPU.
2. **Gradient và Hướng dốc nhất**: Gradient của hàm mất mát tổng bình phương là $\nabla f(w) = A^T(A w - b)$. Hướng $- \nabla f(w)$ là kim chỉ nam hạ thấp mất mát trong thuật toán Gradient Descent.
3. **Hessian và Độ cong địa hình**: Ma trận đạo hàm bậc hai $H = A^T A$ luôn nửa xác định dương ($H \succeq 0$), bảo đảm địa hình tối ưu luôn là một mặt lồi paraboloid. Khi $A$ đủ hạng cột, nghiệm cực tiểu là duy nhất.
4. **Phần bù Schur**: Công cụ kiểm tra tính xác định dương của ma trận khối, khử biến trong dạng toàn phương và giải hệ phương trình tuyến tính cấu trúc khối lớn.
5. **Phân tích SVD và Số điều kiện**: SVD giải mã cấu trúc hình học của ma trận qua tích phân rã $U \Sigma V^T$. Tỷ số $\kappa(A) = \sigma_{\max}/\sigma_{\min}$ đo lường độ méo mó của địa hình tối ưu.
6. **Đại số tuyến tính số**: Phân tích Cholesky ($H = L L^T$) tốn $\frac{1}{3} n^3$ flops là tiêu chuẩn vàng cho ma trận xác định dương. Ma trận đối xứng không xác định dùng $LDL^T$, và các hệ phương trình khối KKT lớn được tối ưu hóa vượt bậc qua kỹ thuật khử khối Schur.
7. **Cội nguồn xác suất**: Tiêu chuẩn bình phương tối thiểu là hệ quả toán học trực tiếp của nguyên lý Cực đại hóa hợp lý (MLE) khi sai số tuân theo phân phối chuẩn Gauss độc lập.

---

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press. Đọc kỹ Phụ lục A (Đại số tuyến tính, hình học giải tích và vi phân ma trận) và Phụ lục C (Đại số tuyến tính số, phân tích Cholesky, cấu trúc ma trận thưa).
- Gene H. Golub, Charles F. Van Loan, *Matrix Computations*, Johns Hopkins University Press.
- Gilbert Strang, *Linear Algebra and Learning from Data*, Wellesley-Cambridge Press.

Tiếp theo: [Bài 01: Nhập môn tối ưu hóa, Tập lồi và Hàm lồi](./bai-01-nhap-mon-toi-uu.md).
