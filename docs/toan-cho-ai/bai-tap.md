---
title: Bài tập ôn luyện - Cơ sở toán cho AI
description: Tuyển tập bài tập giải tích tối ưu hóa, hình học tập lồi, đại số tuyến tính và phương pháp đạo hàm trong Trí tuệ nhân tạo.
---

# Bài tập ôn luyện: Cơ sở toán cho AI

Hệ thống bài tập ôn luyện môn Cơ sở toán cho AI được xây dựng theo các chuẩn mực toán học giải tích và đại số tuyến tính ứng dụng trong học máy (Machine Learning & Deep Learning).

---

## Phần 1. Tối ưu hóa không ràng buộc & Gradient Descent

### Bài 1.1: Tính toán Gradient và ma trận Hessian
Cho hàm mất mát hai biến $f(x_1, x_2)$ được định nghĩa như sau:
$$f(x_1, x_2) = 2x_1^2 + x_2^2 - 2x_1 x_2 + 4x_1 - 6x_2$$

1. Tính vector gradient $\nabla f(x_1, x_2)$.
2. Tính ma trận Hessian $H = \nabla^2 f(x_1, x_2)$.
3. Kiểm tra tính xác định dương (positive definiteness) của ma trận $H$ và kết luận tính lồi của hàm $f$.
4. Tìm điểm dừng (stationary point) $x^* = (x_1^*, x_2^*)$ và xác định giá trị cực tiểu toàn cục $f(x^*)$.
5. Giả sử ta áp dụng Gradient Descent từ điểm khởi tạo $x^{(0)} = (0, 0)^T$ với tốc độ học (learning rate) $\eta = 0.1$. Tính toán tọa độ của điểm $x^{(1)}$ sau một bước lặp cập nhật.

#### Lời giải gợi ý
1. Lấy đạo hàm riêng cấp 1 theo từng biến:
   $$\frac{\partial f}{\partial x_1} = 4x_1 - 2x_2 + 4$$
   $$\frac{\partial f}{\partial x_2} = 2x_2 - 2x_1 - 6$$
   Vector gradient:
   $$\nabla f(x_1, x_2) = \begin{bmatrix} 4x_1 - 2x_2 + 4 \\ -2x_1 + 2x_2 - 6 \end{bmatrix}$$

2. Lấy đạo hàm riêng cấp 2:
   $$\frac{\partial^2 f}{\partial x_1^2} = 4, \quad \frac{\partial^2 f}{\partial x_1 \partial x_2} = -2, \quad \frac{\partial^2 f}{\partial x_2^2} = 2$$
   Ma trận Hessian:
   $$H = \begin{bmatrix} 4 & -2 \\ -2 & 2 \end{bmatrix}$$

3. Xét các định thức con chính:
   $$\Delta_1 = 4 > 0, \quad \Delta_2 = \det(H) = 4(2) - (-2)^2 = 8 - 4 = 4 > 0$$
   Do tất cả các định thức con chính đều dương, ma trận Hessian $H$ xác định dương tại mọi điểm $(x_1, x_2) \in \mathbb{R}^2$. Do đó $f(x_1, x_2)$ là hàm lồi ngặt (strictly convex function) trên toàn miền.

4. Giải hệ phương trình điểm dừng $\nabla f(x_1, x_2) = \mathbf{0}$:
   $$\begin{cases} 4x_1 - 2x_2 = -4 \\ -2x_1 + 2x_2 = 6 \end{cases}$$
   Cộng hai phương trình vế theo vế: $2x_1 = 2 \implies x_1^* = 1$.
   Thay vào phương trình thứ hai: $-2(1) + 2x_2 = 6 \implies 2x_2 = 8 \implies x_2^* = 4$.
   Điểm dừng duy nhất là $x^* = (1, 4)^T$. Vì $f$ lồi ngặt, đây là điểm cực tiểu toàn cục.
   Giá trị cực tiểu:
   $$f(1, 4) = 2(1)^2 + 4^2 - 2(1)(4) + 4(1) - 6(4) = 2 + 16 - 8 + 4 - 24 = -10$$

5. Tại $x^{(0)} = (0, 0)^T$:
   $$\nabla f(0, 0) = \begin{bmatrix} 4 \\ -6 \end{bmatrix}$$
   Công thức cập nhật Gradient Descent:
   $$x^{(1)} = x^{(0)} - \eta \nabla f(x^{(0)}) = \begin{bmatrix} 0 \\ 0 \end{bmatrix} - 0.1 \begin{bmatrix} 4 \\ -6 \end{bmatrix} = \begin{bmatrix} -0.4 \\ 0.6 \end{bmatrix}$$

---

## Phần 2. Hình học tập lồi và phân tích hàm lồi

### Bài 2.1: Chứng minh tập lồi và tổ hợp lồi
1. Chứng minh rằng hình cầu đóng chuẩn Euclid (Euclidean ball) trong $\mathbb{R}^n$:
   $$B(x_0, r) = \{x \in \mathbb{R}^n \mid \|x - x_0\|_2 \le r\}$$
   là một tập lồi.
2. Cho tập hợp $S = \{x \in \mathbb{R}^2 \mid x_1^2 + x_2^2 \le 4\}$. Lấy hai điểm $u = (1, 1)$ và $v = (-1, \sqrt{2})$. Hãy chỉ ra rằng mọi tổ hợp lồi $w = \theta u + (1 - \theta)v$ (với $\theta \in [0, 1]$) đều thuộc $S$.
3. Nêu định nghĩa tập nón lồi (convex cone) và chứng minh nón bán xác định dương $S_+^n = \{X \in \mathbb{R}^{n \times n} \mid X = X^T, X \succeq 0\}$ là một nón lồi.

#### Lời giải gợi ý
1. Lấy bất kỳ hai điểm $x, y \in B(x_0, r)$ và $\theta \in [0, 1]$. Xét điểm $z = \theta x + (1 - \theta)y$:
   $$\|z - x_0\|_2 = \|\theta x + (1 - \theta)y - x_0\|_2 = \|\theta (x - x_0) + (1 - \theta)(y - x_0)\|_2$$
   Theo bất đẳng thức tam giác và tính thuần nhất của chuẩn:
   $$\|z - x_0\|_2 \le \theta \|x - x_0\|_2 + (1 - \theta) \|y - x_0\|_2 \le \theta r + (1 - \theta) r = r$$
   Do đó $z \in B(x_0, r)$, kết luận hình cầu đóng là tập lồi.

2. Áp dụng trực tiếp tính lồi của chuẩn hoặc hàm khoảng cách bình phương (do $x_1^2 + x_2^2 = \|x\|_2^2 \le 4$).

---

## Phần 3. Đại số tuyến tính & Phân rã ma trận

### Bài 3.1: Trị riêng, vector riêng và phân rã phổ
Cho ma trận đối xứng $A \in \mathbb{R}^{2 \times 2}$:
$$A = \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}$$

1. Tìm đa thức đặc trưng và xác định các giá trị riêng $\lambda_1, \lambda_2$ của $A$.
2. Tìm các vector riêng đơn vị tương ứng $q_1, q_2$. Chứng minh hai vector này trực giao nhau.
3. Viết phân rã phổ (Spectral Decomposition):
   $$A = Q \Lambda Q^T = \lambda_1 q_1 q_1^T + \lambda_2 q_2 q_2^T$$
4. Tính ma trận chiếu (projection matrix) lên không gian con sinh bởi vector riêng ứng với giá trị riêng lớn nhất.

#### Lời giải gợi ý
1. Phương trình đặc trưng:
   $$\det(A - \lambda I) = \det\begin{bmatrix} 4 - \lambda & 2 \\ 2 & 1 - \lambda \end{bmatrix} = (4 - \lambda)(1 - \lambda) - 4 = \lambda^2 - 5\lambda = \lambda(\lambda - 5) = 0$$
   Suy ra $\lambda_1 = 5, \lambda_2 = 0$.

2. Tìm vector riêng:
   - Với $\lambda_1 = 5$: $(A - 5I)v = 0 \iff \begin{bmatrix} -1 & 2 \\ 2 & -4 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = 0 \iff -v_1 + 2v_2 = 0 \implies v_1 = 2v_2$.
     Chuẩn hóa: $q_1 = \frac{1}{\sqrt{5}} \begin{bmatrix} 2 \\ 1 \end{bmatrix}$.
   - Với $\lambda_2 = 0$: $A v = 0 \iff 4v_1 + 2v_2 = 0 \implies v_2 = -2v_1$.
     Chuẩn hóa: $q_2 = \frac{1}{\sqrt{5}} \begin{bmatrix} -1 \\ 2 \end{bmatrix}$.
   Tích vô hướng: $q_1^T q_2 = \frac{1}{5}(2(-1) + 1(2)) = 0 \implies$ trực giao.

3. Phân tích phổ:
   $$A = 5 \left(\frac{1}{5} \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}\right) + 0 = \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}$$

---

## Phần 4. Tối ưu hóa có ràng buộc & Điều kiện KKT

### Bài 4.1: Bài toán cực tiểu hóa có ràng buộc đẳng thức bằng nhân tử Lagrange
Tìm khoảng cách ngắn nhất từ gốc tọa độ $(0, 0)$ đến siêu phẳng (đường thẳng) $2x_1 + 3x_2 = 6$.
Quy về bài toán tối ưu lồi:
$$\min_{x_1, x_2} f(x_1, x_2) = \frac{1}{2}(x_1^2 + x_2^2) \quad \text{với ràng buộc } 2x_1 + 3x_2 - 6 = 0$$

1. Thiết lập hàm Lagrange $L(x_1, x_2, \lambda)$.
2. Giải hệ phương trình điểm dừng của hàm Lagrange.
3. Tính nghiệm tối ưu $x^*$ và khoảng cách Euclid ngắn nhất $d^* = \|x^*\|_2$.

#### Lời giải gợi ý
1. Hàm Lagrange:
   $$L(x_1, x_2, \lambda) = \frac{1}{2}(x_1^2 + x_2^2) + \lambda (2x_1 + 3x_2 - 6)$$

2. Lấy đạo hàm riêng:
   $$\frac{\partial L}{\partial x_1} = x_1 + 2\lambda = 0 \implies x_1 = -2\lambda$$
   $$\frac{\partial L}{\partial x_2} = x_2 + 3\lambda = 0 \implies x_2 = -3\lambda$$
   $$\frac{\partial L}{\partial \lambda} = 2x_1 + 3x_2 - 6 = 0$$
   Thay $x_1, x_2$ vào ràng buộc:
   $$2(-2\lambda) + 3(-3\lambda) - 6 = 0 \iff -13\lambda = 6 \implies \lambda = -\frac{6}{13}$$
   Suy ra tọa độ nghiệm tối ưu:
   $$x_1^* = \frac{12}{13}, \quad x_2^* = \frac{18}{13}$$

3. Khoảng cách ngắn nhất:
   $$d^* = \sqrt{\left(\frac{12}{13}\right)^2 + \left(\frac{18}{13}\right)^2} = \frac{\sqrt{144 + 324}}{13} = \frac{\sqrt{468}}{13} = \frac{6\sqrt{13}}{13} = \frac{6}{\sqrt{13}}$$
