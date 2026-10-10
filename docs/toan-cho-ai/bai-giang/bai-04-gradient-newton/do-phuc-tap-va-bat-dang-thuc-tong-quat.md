---
course: toan-cho-ai
lecture: bai-04-gradient-newton
topic: do-phuc-tap-va-bat-dang-thuc-tong-quat
section: topic
title: "Độ phức tạp và điểm trong trên nón chính quy"
description: "Phân tích độ phức tạp hội tụ của phương pháp hàm chắn logarit, vai trò của tham số tự tương hợp nu, mở rộng hàm chắn cho nón Lorentz SOCP và nón ma trận nửa xác định dương SDP."
---

Một trong những thành tựu rực rỡ nhất của giải tích tối ưu hiện đại vào cuối thế kỷ 20 là chứng minh rằng các bài toán quy hoạch lồi tổng quát—bao gồm Quy hoạch nón bậc hai (SOCP) và Quy hoạch nửa xác định (SDP)—đều có thể giải được trong thời gian đa thức (polynomial time). Chìa khóa mở ra bước đột phá này là lý thuyết hàm tự tương hợp (Self-Concordant Functions) của Yurii Nesterov và Arkadi Nemirovski, cho phép định lượng chính xác số bước lặp Newton cần thiết để hội tụ về nghiệm tối ưu với độ chính xác tùy ý.

Chủ đề này phân tích độ phức tạp tính toán của phương pháp hàm chắn logarit, mối quan hệ đánh đổi khi lựa chọn hệ số tăng tham số $\mu$, và cách mở rộng hàm chắn lên các nón chính quy tổng quát như nón Lorentz và nón ma trận nửa xác định dương (PSD).

## 1. Phân tích độ phức tạp của phương pháp hàm chắn

Phương pháp hàm chắn giải bài toán tối ưu có ràng buộc bất đẳng thức thông qua một chuỗi các bài toán không ràng buộc xấp xỉ có trọng số $t > 0$:

$$
\text{minimize}\quad t f_0(x) + \phi(x),
$$

trong đó $\phi(x) = -\sum_{i=1}^m \log(-f_i(x))$ là hàm chắn logarit. 

Mỗi chu kỳ lặp lớn (outer iteration) bao gồm:
1. **Bước định tâm (Centering step)**: Sử dụng phương pháp Newton để tính nghiệm tối ưu xấp xỉ $x^*(t)$ ứng với giá trị $t$ hiện tại.
2. **Cập nhật tham số**: Tăng tham số theo hệ số co dãn $\mu > 1$:
   $$
   t^+ = \mu t.
   $$

Tại nghiệm định tâm $x^*(t)$, khoảng cách đối ngẫu lý thuyết giữa nghiệm nguyên thủy và nghiệm đối ngẫu được chứng minh bằng đúng:

$$
f_0(x^*(t)) - d^* \le \frac{m}{t}.
$$

### Số bước lặp ngoài (Outer Iterations)
Giả sử ta khởi đầu từ $t = t^{(0)} > 0$ và yêu cầu dung sai dừng cuối cùng là $\epsilon > 0$. Sau $k$ bước lặp ngoài, tham số đạt giá trị $t^{(k)} = \mu^k t^{(0)}$. Điều kiện dừng đạt được khi khoảng cách đối ngẫu nhỏ hơn $\epsilon$:

$$
\frac{m}{\mu^k t^{(0)}} \le \epsilon \iff \mu^k \ge \frac{m}{t^{(0)} \epsilon}.
$$

Lấy logarit tự nhiên hai vế, ta thu được số bước lặp ngoài chính xác:

$$
N_{\text{outer}} = \left\lceil \frac{\log\left(\frac{m}{t^{(0)} \epsilon}\right)}{\log \mu} \right\rceil.
$$

Công thức này cho thấy số bước lặp ngoài chỉ tăng trưởng theo tốc độ logarit của độ chính xác nghịch đảo $\log(1/\epsilon)$, giải thích vì sao phương pháp điểm trong đạt được độ chính xác số học rất cao (ví dụ: Sai số nằm trong khoảng từ $10^{-8}$ đến $10^{-12}$) chỉ sau một số ít bước lặp ngoài.

### Số bước lặp Newton bên trong (Inner Newton Iterations)
Câu hỏi then chốt tiếp theo là: Tại mỗi bước ngoài, khi ta nhảy tham số từ $t$ lên $\mu t$, phương pháp Newton cần bao nhiêu bước lặp bên trong để tìm lại điểm định tâm mới $x^*(\mu t)$?

Khi hàm mục tiêu và các hàm ràng buộc thỏa mãn tính chất tự tương hợp với tham số $\nu$, Nesterov và Nemirovski đã chứng minh rằng số bước lặp Newton trong mỗi bước ngoài bị chặn trên bởi:

$$
N_{\text{Newton}} \le \frac{\mu - 1 - \log \mu}{\gamma} + c,
$$

với các hằng số $\gamma > 0$ và $c > 0$ độc lập với kích thước bài toán.

Đặc biệt, nếu ta chọn hệ số tăng tiệm cận $\mu = 1 + \frac{1}{\sqrt{\nu}}$, số bước Newton trong mỗi bước ngoài trở thành một hằng số $O(1)$. Nhân với số bước ngoài $N_{\text{outer}} = O(\sqrt{\nu} \log(1/\epsilon))$, ta thu được cận trên độ phức tạp toàn cục:

$$
N_{\text{total}} = O\left(\sqrt{\nu} \log\left(\frac{m}{t^{(0)} \epsilon}\right)\right) \text{ bước Newton.}
$$

Với bài toán có $m$ bất đẳng thức vô hướng, tham số tự tương hợp là $\nu = m$.

## 2. Điểm trong trên Nón chính quy (Conic Interior-Point)

Trong các bài toán tối ưu hiện đại, ràng buộc thường không xuất hiện dưới dạng từng bất đẳng thức vô hướng riêng rẽ mà ở dạng bất đẳng thức nón tổng quát:

$$
f(x) \preceq_K 0,
$$

trong đó $K \subset \mathbb{R}^p$ là một nón chính quy (lồi, đóng, có phần trong khác rỗng và nhọn).

Để áp dụng phương pháp điểm trong, ta cần một **hàm chắn nón (generalized logarithm)** $\psi: \operatorname{int}(K) \to \mathbb{R}$ có tính chất tự tương hợp và thỏa mãn đẳng thức tỷ lệ:

$$
\psi(s u) = \psi(u) + \nu \log s, \qquad \forall s > 0, \; u \in \operatorname{int}(K),
$$

với $\nu$ là bậc của hàm chắn (barrier parameter).

### Nón bậc hai Lorentz (Second-Order Cone - SOCP)
Nón Lorentz trong không gian $\mathbb{R}^{n+1}$ được định nghĩa là:

$$
K_{\text{soc}} = \big\{ (x, t) \in \mathbb{R}^n \times \mathbb{R} \mid \|x\|_2 \le t \big\}.
$$

Hàm chắn chuẩn mực trên phần trong của nón Lorentz là:

$$
\psi(x, t) = -\log(t^2 - \|x\|_2^2).
$$

Tham số rào chắn của nón Lorentz luôn bằng $\nu = 2$, hoàn toàn độc lập với số chiều không gian $n$. Đây là lý do vì sao bài toán SOCP giải nhanh hơn bài toán LP tương đương có cùng số lượng biến.

### Nón ma trận nửa xác định dương (PSD Cone - SDP)
Xét nón các ma trận đối xứng nửa xác định dương cỡ $k \times k$: $\mathbb{S}_+^k$. Phần trong của nón là tập các ma trận đối xứng xác định dương $\mathbb{S}_{++}^k$.

Hàm chắn chuẩn mực trên $\mathbb{S}_{++}^k$ là:

$$
\psi(X) = -\log \det(X).
$$

Tham số rào chắn của nón ma trận này bằng đúng số chiều ma trận: $\nu = k$.

### Đạo hàm và Hessian của hàm chắn ma trận
Để thực hiện bước lặp Newton trong giải thuật SDP, ta cần tính gradient và Hessian của $\psi(X) = -\log\det(X)$:
1. **Gradient (đạo hàm cấp một)**:
   $$
   \nabla \psi(X) = -X^{-1}.
   $$
2. **Hessian (đạo hàm cấp hai)**: Áp dụng lên một ma trận hướng đối xứng $H \in \mathbb{S}^k$:
   $$
   \nabla^2 \psi(X)[H] = X^{-1} H X^{-1}.
   $$
   Dạng toàn phương Hessian áp dụng lên $H$:
   $$
   \operatorname{tr}\big(H \nabla^2 \psi(X)[H]\big) = \operatorname{tr}\big(H X^{-1} H X^{-1}\big) = \|X^{-1/2} H X^{-1/2}\|_F^2 \ge 0.
   $$

Dạng toàn phương này triệt tiêu khi và chỉ khi $H = 0$, chứng minh rằng hàm chắn ma trận $-\log\det(X)$ là lồi ngặt trên toàn bộ nón $\mathbb{S}_{++}^k$.

## 3. Bài tập tự luyện

::: exercise 1. Tính số bước lặp ngoài trong Quy hoạch tuyến tính
Một bài toán Quy hoạch tuyến tính (LP) có $m = 200$ ràng buộc bất đẳng thức. Thuật toán hàm chắn bắt đầu với tham số $t^{(0)} = 1$ và hệ số nhân $\mu = 10$. Yêu cầu dung sai hội tụ cuối cùng là $\epsilon = 10^{-6}$.
1. Tính khoảng cách đối ngẫu ban đầu tại $t^{(0)}$.
2. Tính số bước lặp ngoài cần thiết để đạt độ chính xác $\epsilon$.
3. Nếu thay đổi hệ số nhân thành $\mu = 2$, số bước lặp ngoài sẽ thay đổi như thế nào?
:::

::: solution
1. **Khoảng cách đối ngẫu ban đầu**:
   Tại $t^{(0)} = 1$, khoảng cách đối ngẫu là:
   $$
   \text{Gap}^{(0)} = \frac{m}{t^{(0)}} = \frac{200}{1} = 200.
   $$

2. **Số bước lặp ngoài với $\mu = 10$**:
   Tỷ số thu hẹp khoảng cách đối ngẫu:
   $$
   \frac{m}{t^{(0)} \epsilon} = \frac{200}{1 \times 10^{-6}} = 200 \times 10^6 = 2 \times 10^8.
   $$
   Số bước lặp ngoài:
   $$
   N_{\text{outer}} = \left\lceil \frac{\log_{10}(2 \times 10^8)}{\log_{10}(10)} \right\rceil = \lceil 8 + \log_{10}(2) \rceil = \lceil 8 + 0{,}3010 \rceil = \lceil 8{,}3010 \rceil = 9.
   $$
   Như vậy, chỉ cần đúng 9 bước lặp ngoài để giảm sai số từ 200 xuống dưới $10^{-6}$.

3. **Khi thay đổi $\mu = 2$**:
   Số bước lặp ngoài mới:
   $$
   N_{\text{outer}} = \left\lceil \frac{\ln(2 \times 10^8)}{\ln(2)} \right\rceil = \left\lceil \frac{19{,}1138}{0{,}6931} \right\rceil = \lceil 27{,}576 \rceil = 28 \text{ bước.}
   $$
   Số bước lặp ngoài tăng gấp khoảng 3 lần (từ 9 lên 28 bước). Tuy nhiên, mỗi bước ngoài với $\mu = 2$ lại đòi hỏi rất ít bước Newton bên trong vì điểm khởi đầu gần điểm định tâm mới hơn.
:::

::: exercise 2. Kiểm chứng tính tự tương hợp của hàm chắn nón Lorentz
Cho nón Lorentz trong $\mathbb{R}^3$: $K = \{(x_1, x_2, t) \mid x_1^2 + x_2^2 \le t^2, \; t > 0\}$. Hàm chắn là $\psi(x, t) = -\log(t^2 - x_1^2 - x_2^2)$.
1. Tính gradient của $\psi(x, t)$ theo vector biến $(x_1, x_2, t)$.
2. Kiểm tra đẳng thức tỷ lệ $\psi(s x, s t) = \psi(x, t) - 2 \log s$ với mọi $s > 0$.
3. Kết luận về tham số rào chắn $\nu$ của nón Lorentz.
:::

::: solution
1. **Tính gradient**:
   Đặt $u = t^2 - x_1^2 - x_2^2 > 0$ trên phần trong của nón. Khi đó $\psi = -\log u$.
   Đạo hàm riêng theo các biến:
   $$
   \frac{\partial \psi}{\partial x_1} = -\frac{1}{u} (-2x_1) = \frac{2x_1}{t^2 - x_1^2 - x_2^2},
   $$
   $$
   \frac{\partial \psi}{\partial x_2} = -\frac{1}{u} (-2x_2) = \frac{2x_2}{t^2 - x_1^2 - x_2^2},
   $$
   $$
   \frac{\partial \psi}{\partial t} = -\frac{1}{u} (2t) = -\frac{2t}{t^2 - x_1^2 - x_2^2}.
   $$
   Vector gradient:
   $$
   \nabla \psi(x, t) = \frac{2}{t^2 - \|x\|_2^2} \begin{bmatrix} x_1 \\ x_2 \\ -t \end{bmatrix}.
   $$

2. **Kiểm tra đẳng thức tỷ lệ**:
   Với $s > 0$:
   $$
   \begin{aligned}
   \psi(s x, s t) &= -\log\big((s t)^2 - (s x_1)^2 - (s x_2)^2\big) \\
   &= -\log\big(s^2 (t^2 - x_1^2 - x_2^2)\big) \\
   &= -\log(s^2) - \log(t^2 - x_1^2 - x_2^2) \\
   &= -2 \log s + \psi(x, t).
   \end{aligned}
   $$

3. **Kết luận về tham số $\nu$**:
   Đối chiếu với định nghĩa tổng quát $\psi(s u) = \psi(u) - \nu \log s$, ta kết luận tham số rào chắn của nón Lorentz là:
   $$
   \nu = 2.
   $$
   Tham số này không phụ thuộc vào số chiều của vector $x$ (ở đây dù $x \in \mathbb{R}^2$ hay $x \in \mathbb{R}^{1000}$, $\nu$ vẫn bằng 2).
:::

::: exercise 3. Đánh đổi giữa lặp trong và lặp ngoài khi chọn tham số $\mu$
Trong phương pháp hàm chắn logarit, phân tích ưu và nhược điểm của hai chiến lược chọn tham số:
1. Chiến lược $\mu$ nhỏ (chẳng hạn $\mu = 1{,}1$ hoặc $\mu = 1 + 1/\sqrt{m}$).
2. Chiến lược $\mu$ lớn (chẳng hạn $\mu = 20$ hoặc $\mu = 100$).
3. Trong các bộ giải phần mềm thương mại thực tế, người ta thường chọn giá trị $\mu$ trong khoảng nào?
:::

::: solution
1. **Chiến lược $\mu$ nhỏ**:
   - **Ưu điểm**: Tham số $t$ tăng rất từ tốn, do đó điểm định tâm cũ $x^*(t)$ nằm rất gần điểm định tâm mới $x^*(\mu t)$. Phương pháp Newton bên trong hầu như chỉ mất 1 đến 2 bước lặp là hội tụ (luôn nằm trong vùng hội tụ bậc hai).
   - **Nhược điểm**: Số bước lặp ngoài $N_{\text{outer}} = O(\sqrt{m} \log(1/\epsilon))$ rất lớn, khiến tổng thời gian giải thực tế bị kéo dài.

2. **Chiến lược $\mu$ lớn**:
   - **Ưu điểm**: Tham số $t$ tăng vọt sau mỗi vòng, số bước lặp ngoài $N_{\text{outer}}$ rất nhỏ (thường chỉ 5 đến 15 bước là đạt độ chính xác $10^{-8}$).
   - **Nhược điểm**: Bước nhảy tham số quá lớn khiến điểm định tâm cũ nằm xa điểm định tâm mới. Phương pháp Newton bên trong phải mất nhiều bước lặp dò đường (Backtracking) để tìm lại vùng cực tiểu, thậm chí có nguy cơ vấp phải sự mất ổn định số học.

3. **Lựa chọn thực tế**:
   Trong các thư viện tối ưu hóa thực tế (như MOSEK, SeDuMi, SDPT3), người ta không chọn các giá trị cực đoan lý thuyết mà áp dụng giá trị thực nghiệm trung hòa:
   $$
   \mu \in [10, 50].
   $$
   Khoảng giá trị này mang lại sự cân bằng hoàn hảo: Vừa giữ số bước ngoài dưới 20 bước, vừa bảo đảm số bước Newton bên trong chỉ dao động trung bình từ 3 đến 6 bước mỗi vòng lặp.
:::

## Tóm tắt

Phân tích độ phức tạp của phương pháp hàm chắn khẳng định tính khả thi vượt trội của tối ưu hóa lồi trên các quy mô dữ liệu lớn. Nhờ tốc độ thu hẹp khoảng cách đối ngẫu theo hàm mũ $m/(\mu^k t^{(0)})$, số bước lặp ngoài chỉ tăng theo logarit của độ chính xác nghịch đảo.

Hơn thế nữa, thông qua việc định nghĩa hàm chắn tự tương hợp trên các nón chính quy, lý thuyết điểm trong thống nhất toàn bộ các họ bài toán LP, SOCP và SDP dưới một khung giải thuật chung. Việc nắm vững cấu trúc đạo hàm của các hàm chắn nón (như $-\log(t^2 - \|x\|^2)$ và $-\log\det X$) là chìa khóa để triển khai các bộ giải tối ưu hiện đại đạt hiệu năng số học cao.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press, Chapter 11: Interior-Point Methods (§§11.5–11.6).
