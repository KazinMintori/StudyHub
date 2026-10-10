---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: khop-ham-va-noi-suy
section: topic
title: "Khớp hàm, làm mượt spline và nội suy lồi"
description: "Biểu diễn hàm bằng họ hàm cơ sở, khớp hàm có ràng buộc hình dạng đơn điệu và lồi, bài toán làm mượt spline dẫn về quy hoạch toàn phương, xấp xỉ minimax Chebyshev và ứng dụng trong mạng nơ-ron lồi."
---

Trong thực tế khoa học dữ liệu và kỹ thuật, các quan sát thực nghiệm thường bị nhiễu và rời rạc. Một nhiệm vụ trung tâm là tìm một hàm số liên tục $f(x)$ bám sát các điểm dữ liệu $(x_i, y_i)$, đồng thời thỏa mãn các quy luật tiên nghiệm về mặt vật lý như: Hàm chi phí không bao giờ giảm (tính đơn điệu), hoặc hàm năng lượng có đáy duy nhất (tính lồi). Nếu không có các ràng buộc hình dạng này, các hàm số xấp xỉ bậc cao rất dễ rơi vào hiện tượng quá khớp (overfitting) hoặc tạo ra các bước nhảy phi lý giữa các điểm đo.

Chủ đề này nghiên cứu việc mô hình hóa bài toán khớp hàm và nội suy dưới lăng kính của tối ưu hóa lồi, từ việc sử dụng các họ hàm cơ sở tuyến tính, kỹ thuật làm mượt spline dẫn về quy hoạch toàn phương, đến bài toán nội suy bảo toàn tính lồi rời rạc.

## 1. Biểu diễn hàm bằng họ hàm cơ sở

Một cách tiếp cận chuẩn mực để xấp xỉ một hàm số chưa biết $f: \mathbb{R}^n \to \mathbb{R}$ là chọn trước một tập hợp $k$ hàm cơ sở độc lập $\{f_1, f_2, \dots, f_k\}$ và biểu diễn $f(x)$ dưới dạng tổ hợp tuyến tính:

$$
f(x) = \sum_{j=1}^k \theta_j f_j(x),
$$

trong đó $\theta = (\theta_1, \dots, \theta_k)^T \in \mathbb{R}^k$ là vector tham số cần tối ưu.

Mặc dù các hàm cơ sở $f_j(x)$ có thể phi tuyến đối với biến $x$ (chẳng hạn như đa thức $x^j$, hàm lượng giác $\cos(j \omega x)$, hay các hàm bán kính Gauss $e^{-\gamma \|x - c_j\|_2^2}$), giá trị hàm $f(x)$ và các đạo hàm của nó lại hoàn toàn là **hàm affine đối với vector tham số $\theta$**. Cụ thể:

$$
\begin{aligned}
f(x) &= a(x)^T \theta \quad \text{với } a(x) = \begin{bmatrix} f_1(x) \\ \vdots \\ f_k(x) \end{bmatrix}, \\
f'(x) &= a'(x)^T \theta \quad \text{với } a'(x) = \begin{bmatrix} f'_1(x) \\ \vdots \\ f'_k(x) \end{bmatrix}, \\
f''(x) &= a''(x)^T \theta \quad \text{với } a''(x) = \begin{bmatrix} f''_1(x) \\ \vdots \\ f''_k(x) \end{bmatrix}.
\end{aligned}
$$

Tính chất affine theo $\theta$ này là chìa khóa then chốt: Mọi ràng buộc hoặc tiêu chí tối ưu tuyến tính trên giá trị hàm và đạo hàm đều chuyển hóa thành các ràng buộc lồi trên không gian tham số $\theta$.

## 2. Khớp hàm có ràng buộc hình dạng (Shape-Constrained Fitting)

Giả sử ta thu thập được tập dữ liệu gồm $m$ quan sát $(x_i, y_i)$ với $i = 1, \dots, m$. Sai số dự đoán tại điểm $x_i$ là:

$$
r_i(\theta) = f(x_i) - y_i = a(x_i)^T \theta - y_i.
$$

Vector phần dư được viết gọn dưới dạng ma trận: $r(\theta) = A \theta - y$, trong đó $A_{ij} = f_j(x_i)$.

### Ràng buộc đơn điệu (Monotonicity)
Trong các bài toán kinh tế học hay định giá tài sản, hàm số thường bắt buộc phải không giảm, tức $f'(x) \ge 0$ với mọi $x \in [x_{\min}, x_{\max}]$. Trên thực tế, ta có thể áp đặt ràng buộc này tại một lưới dày gồm $N$ điểm kiểm tra $\{t_1, \dots, t_N\}$:

$$
a'(t_p)^T \theta \ge 0, \qquad p = 1, \dots, N.
$$

Đây là một hệ gồm $N$ bất đẳng thức tuyến tính theo $\theta$, định hình một đa diện lồi khả thi trong không gian tham số.

### Ràng buộc lồi (Convexity)
Để bảo đảm hàm xấp xỉ là hàm lồi trên đoạn một chiều, ta yêu cầu đạo hàm bậc hai không âm: $f''(x) \ge 0$. Tương tự, trên lưới điểm kiểm tra, điều kiện này tương đương với:

$$
a''(t_p)^T \theta \ge 0, \qquad p = 1, \dots, N.
$$

Khi kết hợp tiêu chí bình phương tối thiểu với các ràng buộc trên, ta thu được một bài toán Quy hoạch toàn phương (QP):

$$
\begin{aligned}
\text{minimize}\quad & \|A \theta - y\|_2^2 \\
\text{subject to}\quad & A' \theta \succeq 0, \\
& A'' \theta \succeq 0,
\end{aligned}
$$

trong đó các hàng của ma trận $A'$ và $A''$ lần lượt chứa các vector gradient $a'(t_p)^T$ và $a''(t_p)^T$.

## 3. Làm mượt Spline (Smoothing Splines)

Khi không muốn giới hạn hàm $f(x)$ trong một số lượng hàm cơ sở cố định trước, ta có thể tìm hàm số $f$ trong không gian vô hạn chiều của các hàm khả vi liên tục cấp hai trên đoạn $[a, b]$. Mục tiêu là tối thiểu hóa hàm mục tiêu kết hợp:

$$
J(f) = \sum_{i=1}^m \big(f(x_i) - y_i\big)^2 + \lambda \int_a^b \big(f''(t)\big)^2 \, \mathrm{d}t,
$$

với tham số điều chuẩn $\lambda > 0$. Số hạng tích phân đo lường "độ cong" hay độ gập ghềnh của đường cong: Nếu đường cong càng uốn lượn mạnh thì tích phân này càng lớn, ngược lại với đường thẳng thì tích phân bằng đúng 0.

Định lý cổ điển về spline khẳng định rằng: Hàm số tối ưu hóa phiếm hàm $J(f)$ luôn luôn là một **spline bậc ba tự nhiên (natural cubic spline)** với các nút (knots) đặt tại chính các điểm dữ liệu $x_1 < x_2 < \dots < x_m$.

Một spline bậc ba tự nhiên là một hàm số đa thức bậc ba trên mỗi khoảng $[x_i, x_{i+1}]$, liên tục đến đạo hàm bậc hai tại các nút và có đạo hàm bậc hai triệt tiêu tại hai đầu mút ($f''(a) = f''(b) = 0$).

Đặt vector giá trị tại các nút là $v = (f(x_1), \dots, f(x_m))^T \in \mathbb{R}^m$. Tích phân độ cong có thể được biểu diễn chính xác dưới dạng toàn phương:

$$
\int_a^b \big(f''(t)\big)^2 \, \mathrm{d}t = v^T K v,
$$

trong đó $K \in \mathbb{R}^{m \times m}$ là ma trận độ cứng (stiffness matrix), đối xứng và nửa xác định dương ($K \succeq 0$), được tính trực tiếp từ khoảng cách giữa các nút liên tiếp $h_i = x_{i+1} - x_i$. Khi đó, bài toán làm mượt spline quy về bài toán QP hữu hạn chiều đối với vector giá trị $v$:

$$
\text{minimize}\quad \|v - y\|_2^2 + \lambda v^T K v.
$$

Nghiệm tối ưu giải tích được xác định tường minh:

$$
v^* = (I + \lambda K)^{-1} y.
$$

Vì $K \succeq 0$ và $\lambda > 0$, ma trận $I + \lambda K$ luôn đối xứng xác định dương và khả nghịch, bảo đảm nghiệm tồn tại duy nhất.

## 4. Nội suy lồi rời rạc (Convex Interpolation)

Trong nhiều bài toán học máy, ta không có công thức giải tích của hàm số mà chỉ có một tập hợp $m$ điểm dữ liệu rời rạc $(x_i, y_i)$ trong không gian $\mathbb{R}^n$. Câu hỏi đặt ra là: Khi nào tồn tại một hàm lồi $f: \mathbb{R}^n \to \mathbb{R}$ nội suy chính xác dữ liệu, tức $f(x_i) = y_i$ với mọi $i = 1, \dots, m$?

Điều kiện cần và đủ để tồn tại một hàm lồi nội suy là: Tồn tại các vector dưới gradient $g_i \in \mathbb{R}^n$ tại mỗi điểm $x_i$ sao cho thỏa mãn hệ bất đẳng thức dưới gradient của hàm lồi:

$$
y_j \ge y_i + g_i^T(x_j - x_i), \qquad \forall i, j = 1, \dots, m, \; i \ne j.
$$

Khi hệ bất đẳng thức này thỏa mãn, ta có thể xây dựng một hàm lồi nội suy tường minh bằng cách lấy bao trên (pointwise maximum) của các siêu phẳng tiếp tuyến:

$$
f_{\text{interp}}(x) = \max_{i=1,\dots,m} \big(y_i + g_i^T(x - x_i)\big).
$$

Hàm $f_{\text{interp}}(x)$ là giá trị lớn nhất của $m$ hàm affine, do đó nó tự động là một hàm lồi trên toàn bộ $\mathbb{R}^n$ và thỏa mãn $f_{\text{interp}}(x_i) = y_i$. Việc kiểm tra sự tồn tại của các vector $g_i$ chính là một bài toán tìm nghiệm khả thi của hệ bất đẳng thức tuyến tính (LP khả thi).

## 5. Bài tập tự luyện

::: exercise 1. Khớp đa thức bậc 3 có ràng buộc đơn điệu không giảm
Cho tập dữ liệu gồm 4 điểm trên đoạn $[-1, 1]$: $(-1, -2)$, $(-0{,}5, -0{,}8)$, $(0{,}5, 0{,}7)$, $(1, 2{,}1)$. Ta muốn khớp dữ liệu bằng đa thức bậc 3: $f(x) = \theta_0 + \theta_1 x + \theta_2 x^2 + \theta_3 x^3$.
1. Xác định điều kiện giải tích trên các hệ số $\theta_1, \theta_2, \theta_3$ để $f'(x) \ge 0$ với mọi $x \in \mathbb{R}$.
2. Thiết lập bài toán Quy hoạch toàn phương (QP) xấp xỉ bình phương tối thiểu khi thay ràng buộc trên toàn trục thực bằng việc kiểm tra tính đơn điệu tại ba điểm $x \in \{-1, 0, 1\}$.
:::

::: solution
1. **Điều kiện đơn điệu trên toàn trục thực**:
   Đạo hàm của $f(x)$ là một tam thức bậc hai:
   $$
   f'(x) = 3\theta_3 x^2 + 2\theta_2 x + \theta_1.
   $$
   Để $f'(x) \ge 0$ với mọi $x \in \mathbb{R}$, tam thức bậc hai này phải có hệ số bậc hai dương và biệt thức $\Delta'$ không dương:
   $$
   \theta_3 > 0 \quad \text{và} \quad \Delta' = \theta_2^2 - 3\theta_1 \theta_3 \le 0.
   $$
   (Trường hợp suy biến: Nếu $\theta_3 = 0$, ta cần $\theta_2 = 0$ và $\theta_1 \ge 0$).
   Ràng buộc $\theta_2^2 - 3\theta_1 \theta_3 \le 0$ có thể biểu diễn qua nón bậc hai xoay (Rotated Second-Order Cone): $2(\sqrt{3/2}\theta_1)(\sqrt{3/2}\theta_3) \ge \theta_2^2$.

2. **Thiết lập bài toán QP trên lưới điểm**:
   Tại các điểm kiểm tra $x \in \{-1, 0, 1\}$:
   - Tại $x = 0$: $f'(0) = \theta_1 \ge 0$.
   - Tại $x = 1$: $f'(1) = \theta_1 + 2\theta_2 + 3\theta_3 \ge 0$.
   - Tại $x = -1$: $f'(-1) = \theta_1 - 2\theta_2 + 3\theta_3 \ge 0$.
   
   Ma trận dữ liệu $A \in \mathbb{R}^{4 \times 4}$ tại các điểm $x_i \in \{-1, -0{,}5, 0{,}5, 1\}$ có các hàng là $[1, x_i, x_i^2, x_i^3]$. Bài toán QP có dạng:
   $$
   \begin{aligned}
   \text{minimize}\quad & \|A \theta - y\|_2^2 \\
   \text{subject to}\quad & \theta_1 \ge 0, \\
   & \theta_1 + 2\theta_2 + 3\theta_3 \ge 0, \\
   & \theta_1 - 2\theta_2 + 3\theta_3 \ge 0.
   \end{aligned}
   $$
   Đây là bài toán QP chuẩn mực với mục tiêu toàn phương lồi và các ràng buộc affine.
:::

::: exercise 2. Nghiệm ma trận của bài toán làm mượt Spline
Xét bài toán làm mượt spline trên $m$ điểm quan sát: Đặt $\min_{v \in \mathbb{R}^m} \|v - y\|_2^2 + \lambda v^T K v$ với $\lambda > 0$ và ma trận độ cứng $K \succeq 0$.
1. Chứng minh rằng hàm mục tiêu là hàm lồi mạnh (strongly convex) theo $v$.
2. Tìm vector gradient của hàm mục tiêu và suy ra nghiệm tối ưu duy nhất $v^*$.
3. Khảo sát hành vi của nghiệm khi $\lambda \to 0$ và khi $\lambda \to \infty$ (giả sử không gian triệt tiêu của $K$ chỉ gồm các vector biểu diễn đường thẳng $v = c_0 \mathbf{1} + c_1 x$).
:::

::: solution
1. **Chứng minh tính lồi mạnh**:
   Khai triển hàm mục tiêu:
   $$
   J(v) = (v - y)^T (v - y) + \lambda v^T K v = v^T (I + \lambda K) v - 2 y^T v + y^T y.
   $$
   Ma trận Hessian của $J(v)$ là $\nabla^2 J(v) = 2(I + \lambda K)$.
   Vì $K \succeq 0$ (mọi trị riêng $\lambda_i(K) \ge 0$) và $\lambda > 0$, ta có:
   $$
   \nabla^2 J(v) \succeq 2I \succ 0.
   $$
   Ma trận Hessian bị chặn dưới bởi $2I$, chứng minh $J(v)$ là hàm lồi mạnh với tham số lồi mạnh $m = 2$.

2. **Gradient và nghiệm tối ưu**:
   Đặt gradient bằng 0:
   $$
   \nabla J(v) = 2(I + \lambda K) v - 2y = 0 \implies (I + \lambda K) v = y.
   $$
   Vì $I + \lambda K \succ 0$, ma trận này khả nghịch. Nghiệm tối ưu duy nhất là:
   $$
   v^* = (I + \lambda K)^{-1} y.
   $$

3. **Khảo sát các giới hạn**:
   - Khi $\lambda \to 0$: $v^* \to I^{-1} y = y$. Mô hình nội suy hoàn hảo mọi điểm dữ liệu, không có hiệu ứng làm mượt.
   - Khi $\lambda \to \infty$: Số hạng phạt độ cong $v^T K v$ chiếm ưu thế tuyệt đối, buộc $v$ phải nằm trong không gian triệt tiêu của $K$ ($\operatorname{null}(K)$). Vì không gian này tương ứng với các hàm có $f''(t) = 0$ (đường thẳng affine $f(x) = c_0 + c_1 x$), nghiệm $v^*$ hội tụ về đường thẳng hồi quy tuyến tính bình phương tối thiểu thông thường.
:::

::: exercise 3. Kiểm chứng điều kiện nội suy lồi một chiều
Cho 3 điểm dữ liệu một chiều: $(0, 1)$, $(1, 0)$, và $(3, 2)$.
1. Viết hệ bất đẳng thức dưới gradient đối với các hệ số góc $g_0, g_1, g_2 \in \mathbb{R}$.
2. Tìm một bộ nghiệm $(g_0, g_1, g_2)$ thỏa mãn hệ.
3. Xây dựng hàm lồi nội suy $f_{\text{interp}}(x)$ trên đoạn $[0, 3]$.
:::

::: solution
1. **Hệ bất đẳng thức dưới gradient**:
   Điều kiện $y_j \ge y_i + g_i(x_j - x_i)$ với mọi $i, j \in \{0, 1, 2\}$:
   - Với $i = 0$ ($x_0 = 0, y_0 = 1$):
     - Khi $j = 1$: Ta có $0 \ge 1 + g_0(1 - 0)$, suy ra $g_0 \le -1$.
     - Khi $j = 2$: Ta có $2 \ge 1 + 3g_0$, suy ra $g_0 \le 1/3$.
     - Kết hợp lại: $g_0 \le -1$.
   - Với $i = 1$ ($x_1 = 1, y_1 = 0$):
     - Khi $j = 0$: Ta có $1 \ge 0 - g_1$, suy ra $g_1 \ge -1$.
     - Khi $j = 2$: Ta có $2 \ge 0 + 2g_1$, suy ra $g_1 \le 1$.
     - Kết hợp lại: $-1 \le g_1 \le 1$.
   - Với $i = 2$ ($x_2 = 3, y_2 = 2$):
     - Khi $j = 0$: Ta có $1 \ge 2 - 3g_2$, suy ra $g_2 \ge 1/3$.
     - Khi $j = 1$: Ta có $0 \ge 2 - 2g_2$, suy ra $g_2 \ge 1$.
     - Kết hợp lại: $g_2 \ge 1$.

2. **Chọn nghiệm cụ thể**:
   Ta có thể chọn:
   $$
   g_0 = -1, \qquad g_1 = 0, \qquad g_2 = 1.
   $$
   Dãy hệ số góc $g_0 \le g_1 \le g_2$ thỏa mãn tính chất đơn điệu tăng của dưới gradient đối với hàm lồi một chiều.

3. **Xây dựng hàm lồi nội suy**:
   $$
   \begin{aligned}
   f_{\text{interp}}(x) &= \max\big\{ 1 + (-1)(x - 0), \; 0 + 0(x - 1), \; 2 + 1(x - 3) \big\} \\
   &= \max\big\{ 1 - x, \; 0, \; x - 1 \big\}.
   \end{aligned}
   $$
   Kiểm tra tại các điểm mút:
   - $f_{\text{interp}}(0) = \max\{1, 0, -1\} = 1 = y_0$.
   - $f_{\text{interp}}(1) = \max\{0, 0, 0\} = 0 = y_1$.
   - $f_{\text{interp}}(3) = \max\{-2, 0, 2\} = 2 = y_2$.
   
   Hàm số nội suy chính xác cả 3 điểm và là một hàm lồi hợp lệ trên toàn trục số thực.
:::

## Tóm tắt

Khớp hàm và nội suy là cầu nối thiết yếu giữa dữ liệu thực nghiệm và lý thuyết tối ưu hóa. Bằng cách biểu diễn hàm qua tổ hợp tuyến tính các hàm cơ sở, các yêu cầu hình dạng tiên nghiệm như tính đơn điệu ($f' \ge 0$) hay tính lồi ($f'' \ge 0$) được mô hình hóa thành các ràng buộc affine trên không gian tham số. 

Bài toán làm mượt spline dung hòa mâu thuẫn giữa độ khớp dữ liệu và độ gập ghềnh tích phân, dẫn đến nghiệm giải tích tường minh qua ma trận độ cứng nửa xác định dương. Trong khi đó, nội suy lồi rời rạc được chứng nhận thông qua sự tồn tại của vector dưới gradient thỏa mãn hệ bất đẳng thức lồi, cho phép kiến tạo hàm lồi toàn cục bằng phép lấy bao trên của các siêu phẳng tiếp tuyến.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press, Chapter 6: Approximation and Fitting (§6.5).
