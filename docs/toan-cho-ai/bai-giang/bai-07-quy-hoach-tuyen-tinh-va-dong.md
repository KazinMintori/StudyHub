---
course: toan-cho-ai
lecture: bai-07-quy-hoach-tuyen-tinh-va-dong
section: lecture
title: "Quy hoạch tuyến tính và quy hoạch động"
prerequisites: ["ma-tran", "he-phuong-trinh", "tap-loi", "do-thi"]
lessonStatus: ready
description: "Khảo sát toàn diện Quy hoạch tuyến tính (LP), Quy hoạch động Bellman (DP) và các dạng bài toán tối ưu hình học kinh điển: Xấp xỉ chuẩn, tâm Chebyshev, phân loại SVM, thiết kế thí nghiệm và sự thống nhất giữa thế năng đối ngẫu với hàm giá trị."
---

Trong hệ thống các phương pháp tối ưu hóa dành cho Trí tuệ Nhân tạo, có hai trường phái tư duy kinh điển, đại diện cho hai góc nhìn bổ trợ nhau về bài toán ra quyết định quy mô lớn:

1. **Quy hoạch tuyến tính (Linear Programming - LP)**: Tiếp cận bài toán dưới **góc nhìn hình học không gian tĩnh**. Mọi giới hạn tài nguyên đan xen tạo thành một khối đa diện lồi nhiều chiều (polyhedron), và mục tiêu là tìm kiếm một "đỉnh cực" (extreme point) tối ưu trên khối đa diện đó. LP là xương sống của các hệ thống phân bổ tài nguyên, điều độ luồng mạng, và lập lịch tính toán trên các cụm máy chủ huấn luyện mô hình ngôn ngữ lớn (LLM).
2. **Quy hoạch động (Dynamic Programming - DP)**: Tiếp cận bài toán dưới **góc nhìn chuỗi quyết định động theo thời gian**. Nhà toán học Richard Bellman đã đúc kết một nguyên lý sâu sắc: Một quyết định dài hạn tối ưu luôn có thể phân rã thành một bước hành động tức thời cộng với giá trị tối ưu của phần bài toán còn lại. DP là linh hồn của các thuật toán tìm đường, giải mã chuỗi (Viterbi decoding, Beam Search) và là nền tảng toán học trực tiếp của Học tăng cường (Reinforcement Learning - RL).

Mối liên hệ sâu sắc nhất mà chúng ta khám phá trong bài giảng này: **Hai trường phái tưởng chừng tách biệt ấy thực chất lại là hai mặt của cùng một đồng xu**. Biến tiềm năng (thế năng) trong bài toán đối ngẫu tuyến tính của đường đi ngắn nhất chính là hàm giá trị tối ưu của phương trình Bellman. Hơn thế nữa, bài giảng sẽ mở rộng sang các họ bài toán ứng dụng hình học và thống kê thực tế: Xấp xỉ theo chuẩn, định tâm Chebyshev, ellipsoid thể tích cực trị, thiết kế thí nghiệm tối ưu và phân loại dữ liệu.

---

## 1. Bản chất hình học của Quy hoạch tuyến tính (LP)

Một bài toán quy hoạch tuyến tính xuất hiện khi cả hàm mục tiêu lẫn các ràng buộc đều là hàm bậc nhất (tuyến tính hoặc affine).

Xét bài toán tối ưu phân bổ tài nguyên hai chiều:

$$
\max_{x,y} \quad 3x + 2y
$$

thỏa mãn các ràng buộc tài nguyên:

$$
x + y \le 4, \qquad x \le 2, \qquad x \ge 0, \quad y \ge 0.
$$

### 1.1. Hình học của miền khả thi và các đỉnh cực
Mỗi bất đẳng thức tuyến tính $a_i^T z \le b_i$ xác định một nửa không gian đóng (closed halfspace) lồi. Miền khả thi $\mathcal{P}$ là giao của 4 nửa không gian đó, tạo thành một **đa diện lồi (polyhedron)** hai chiều được bao bọc bởi 4 đỉnh (vertices):
- Đỉnh $A(0, 0)$: Giá trị mục tiêu $3(0) + 2(0) = 0$.
- Đỉnh $B(2, 0)$: Giá trị mục tiêu $3(2) + 2(0) = 6$.
- Đỉnh $C(2, 2)$: Giao của $x=2$ và $x+y=4$. Giá trị mục tiêu $3(2) + 2(2) = 10$.
- Đỉnh $D(0, 4)$: Giao của $x=0$ và $x+y=4$. Giá trị mục tiêu $3(0) + 2(4) = 8$.

Nghiệm tối ưu đạt được tại đỉnh $C(2, 2)$ với giá trị mục tiêu cực đại bằng $10$.

### 1.2. Định lý cơ bản của Quy hoạch tuyến tính
Một điểm $x \in \mathcal{P}$ được gọi là **điểm cực (extreme point)** của tập lồi nếu nó không thể biểu diễn thành tổ hợp lồi thực sự của hai điểm phân biệt trong tập, nghĩa là không tồn tại $y, z \in \mathcal{P}$ ($y \ne z$) và $\theta \in (0, 1)$ sao cho $x = \theta y + (1 - \theta)z$. Với tập đa diện, khái niệm điểm cực trùng khớp hoàn toàn với khái niệm **đỉnh (vertex)** hình học.

> **Định lý nền tảng của LP**: Nếu miền khả thi đa diện $\mathcal{P}$ khác rỗng, không chứa đường thẳng vô hạn hai chiều (có ít nhất một điểm cực) và hàm mục tiêu bị chặn trên miền đó, thì **luôn tồn tại ít nhất một điểm cực đạt giá trị tối ưu toàn cục**.

Trực giác hình học: Các đường đồng mức của hàm mục tiêu tuyến tính $c^T x = \text{const}$ là các siêu phẳng song song. Khi ta "đẩy" siêu phẳng này theo chiều vector gradient $c$ ra xa nhất có thể trong khi vẫn chạm vào đa diện $\mathcal{P}$, điểm tiếp xúc biên cuối cùng bao giờ cũng chạm vào một đỉnh (hoặc cả một cạnh nối giữa hai đỉnh).

---

## 2. Đại số tuyến tính của LP: Dạng chuẩn và Biến bù (Slack Variables)

Để đưa bài toán vào máy tính giải bằng thuật toán Simplex hoặc các phương pháp điểm trong, ta đưa bài toán LP về **dạng chuẩn (Standard Form)**:

$$
\min_{x} \quad c^T x \qquad \text{sao cho} \quad A x = b, \quad x \succeq 0.
$$

### 2.1. Quy tắc chuyển đổi về dạng chuẩn
1. **Đổi mục tiêu**: $\max c^T x \iff \min (-c)^T x$.
2. **Chuyển bất đẳng thức $\le$ thành đẳng thức**: Thêm **biến bù (slack variable)** $s_i \ge 0$:
   $$
   a_i^T x \le b_i \iff a_i^T x + s_i = b_i, \quad s_i \ge 0.
   $$
3. **Chuyển bất đẳng thức $\ge$ thành đẳng thức**: Trừ đi **biến dư (surplus variable)** $e_i \ge 0$:
   $$
   a_i^T x \ge b_i \iff a_i^T x - e_i = b_i, \quad e_i \ge 0.
   $$
4. **Biến tự do không giới hạn dấu**: Nếu một biến $u$ có thể nhận giá trị âm tùy ý, ta tách thành hiệu của hai biến không âm: Đặt $u = u^+ - u^-$ với $u^+, u^- \ge 0$.

Áp dụng vào bài toán ở Mục 1, ta thêm hai biến bù $s_1, s_2 \ge 0$ cho hai ràng buộc tài nguyên:

$$
\min (-3x - 2y) \qquad \text{sao cho} \quad \begin{cases} x + y + s_1 = 4 \\ x + s_2 = 2 \end{cases}, \quad x, y, s_1, s_2 \ge 0.
$$

Biến bù $s_1, s_2$ đo lường chính xác lượng tài nguyên còn dư thừa chưa dùng hết. Tại nghiệm tối ưu $(x, y) = (2, 2)$, ta có $s_1 = 4 - (2+2) = 0$ và $s_2 = 2 - 2 = 0$. Cả hai ràng buộc đều hoạt động hết công suất (active/binding).

---

## 3. Nghiệm cơ sở khả thi (Basic Feasible Solution - BFS)

Giả sử ma trận ràng buộc $A$ có kích thước $m \times n$ ($m$ ràng buộc đẳng thức, $n$ biến với $n > m$) và có đủ hạng hàng ($\operatorname{rank}(A) = m$).

Một tập con gồm $m$ chỉ số cột độc lập tuyến tính được gọi là **tập cơ sở (basis)** $B$. Khi đó, ta phân tách:
- $A = [A_B \mid A_N]$, trong đó $A_B \in \mathbb{R}^{m \times m}$ là ma trận vuông khả nghịch.
- Vector biến $x = [x_B^T, x_N^T]^T$.

Quy trình tìm **nghiệm cơ sở (Basic Solution)**:
1. Đặt tất cả $n - m$ biến phi cơ sở bằng 0: $x_N = 0$.
2. Giải hệ phương trình $m$ biến $m$ phương trình duy nhất:
   $$
   A_B x_B = b \implies x_B = A_B^{-1} b.
   $$
3. Nếu nghiệm thỏa mãn thêm điều kiện không âm $x_B \succeq 0$, nghiệm này được gọi là **nghiệm cơ sở khả thi (Basic Feasible Solution - BFS)**.

Mỗi nghiệm cơ sở khả thi (BFS) trong không gian đại số của dạng chuẩn tương ứng đúng với một **đỉnh cực (extreme point)** của đa diện trong không gian hình học. Thuật toán Simplex kinh điển của George Dantzig chính là quá trình di chuyển từ đỉnh cực này sang đỉnh cực kề cận có giá trị mục tiêu tốt hơn cho đến khi chạm tới đỉnh tối ưu.

---

## 4. Các bài toán Xấp xỉ theo chuẩn và Khớp dữ liệu (Norm Approximation)

Trong khoa học dữ liệu và học máy, một tỷ lệ lớn các bài toán ước lượng đều quy về bài toán xấp xỉ theo chuẩn:

$$
\min_{x \in \mathbb{R}^n} \quad \|A x - b\|.
$$

Tùy thuộc vào việc lựa chọn chuẩn $\|\cdot\|$, bài toán có những đặc tính hình học và phương pháp giải hoàn toàn khác nhau.

### 4.1. Xấp xỉ theo chuẩn L1 (Hồi quy bền vững - Robust Regression)
Bài toán tối ưu:

$$
\min_x \quad \|A x - b\|_1 = \sum_{i=1}^m |a_i^T x - b_i|.
$$

Ta chuyển đổi bài toán này về bài toán Quy hoạch tuyến tính (LP) bằng cách đưa vào vector biến phụ $t \in \mathbb{R}^m$:

$$
\begin{aligned}
\min_{x, t} \quad & \sum_{i=1}^m t_i = \mathbf{1}^T t \\
\text{sao cho} \quad & -t_i \le a_i^T x - b_i \le t_i, \quad i = 1, \dots, m.
\end{aligned}
$$

Đây là một bài toán LP hoàn chỉnh với $n + m$ biến và $2m$ ràng buộc bất đẳng thức.
*Đặc tính thực tiễn*: Chuẩn $L_1$ ít nhạy cảm với các điểm ngoại lai (outliers) hơn nhiều so với chuẩn $L_2$, mang lại nghiệm hồi quy bền vững.

### 4.2. Xấp xỉ theo chuẩn cực đại L-infinity (Chebyshev Approximation)
Bài toán cực tiểu hóa sai số lớn nhất:

$$
\min_x \quad \|A x - b\|_\infty = \max_{1 \le i \le m} |a_i^T x - b_i|.
$$

Chuyển đổi về bài toán LP bằng cách đưa vào một biến vô hướng duy nhất $t \in \mathbb{R}$:

$$
\begin{aligned}
\min_{x, t} \quad & t \\
\text{sao cho} \quad & -t \mathbf{1} \preceq A x - b \preceq t \mathbf{1}.
\end{aligned}
$$

Đây là bài toán LP với $n + 1$ biến và $2m$ ràng buộc bất đẳng thức. Nghiệm của bài toán này giảm thiểu tối đa rủi ro trong kịch bản tồi tệ nhất (worst-case deviation).

### 4.3. Bài toán Chuẩn nhỏ nhất (Least-Norm Problems)
Xét bài toán tìm nghiệm của hệ phương trình thiếu định $A x = b$ ($m < n$) có độ lớn nhỏ nhất:

$$
\min_x \quad \|x\| \quad \text{sao cho} \quad A x = b.
$$

- **Khi dùng chuẩn $L_2$**: Nghiệm giải tích tường minh được cho bởi giả nghịch đảo Moore–Penrose:
  $$
  x^* = A^T (A A^T)^{-1} b.
  $$
- **Khi dùng chuẩn $L_1$**: Bài toán quy về LP và sinh ra nghiệm thưa (sparse solution), là nền tảng của lý thuyết Lấy mẫu nén (Compressed Sensing) và hồi quy Lasso.

---

## 5. Các bài toán Hình học: Định tâm Chebyshev và Phân loại

### 5.1. Tâm Chebyshev của một Đa diện lồi
Cho tập đa diện $\mathcal{P} = \{x \in \mathbb{R}^n \mid a_i^T x \le b_i, \, i = 1, \dots, m\}$. **Tâm Chebyshev** của $\mathcal{P}$ là tâm của quả cầu Euclid lớn nhất có thể nằm trọn vẹn bên trong $\mathcal{P}$.

Quả cầu tâm $x_c$ bán kính $r$ được định nghĩa là $B(x_c, r) = \{x_c + u \mid \|u\|_2 \le r\}$. Điều kiện để quả cầu nằm trong $\mathcal{P}$:

$$
\sup_{\|u\|_2 \le r} a_i^T (x_c + u) \le b_i \iff a_i^T x_c + r \|a_i\|_2 \le b_i \quad \forall i = 1, \dots, m.
$$

Bài toán tìm quả cầu nội tiếp lớn nhất trở thành bài toán Quy hoạch tuyến tính theo biến $(x_c, r)$:

$$
\begin{aligned}
\max_{x_c, r} \quad & r \\
\text{sao cho} \quad & a_i^T x_c + r \|a_i\|_2 \le b_i, \quad i = 1, \dots, m, \\
& r \ge 0.
\end{aligned}
$$

Tâm Chebyshev $x_c$ đóng vai trò là "điểm trung tâm đại diện" sâu nhất bên trong miền ràng buộc, thường được dùng làm điểm khởi tạo an toàn cho các thuật toán tối ưu.

### 5.2. Phân loại dữ liệu và Siêu phẳng lề cực đại (Support Vector Machines - SVM)
Cho hai tập điểm dữ liệu $\{x_1, \dots, x_N\}$ với nhãn $y_i \in \{+1, -1\}$. Ta muốn tìm siêu phẳng $a^T x - b = 0$ phân tách hai lớp dữ liệu sao cho khoảng cách (lề - margin) giữa hai lớp là lớn nhất:

$$
\min_{a, b} \quad \frac{1}{2} \|a\|_2^2 \quad \text{sao cho} \quad y_i (a^T x_i - b) \ge 1, \quad i = 1, \dots, N.
$$

Đây là bài toán Quy hoạch toàn phương lồi (QP). Bài toán đối ngẫu Lagrange của nó dẫn tới biểu diễn theo nhân tử $\alpha_i \ge 0$, mở đường cho kỹ thuật Kernel Trick trong học máy.

---

## 6. Quy hoạch động và Nguyên lý tối ưu Bellman

Nếu như quy hoạch tuyến tính phân tích bài toán dựa trên cấu trúc không gian phẳng, thì **quy hoạch động (Dynamic Programming)** tổ chức việc giải quyết bài toán theo dòng chảy thời gian của các trạng thái.

### 6.1. Nguyên lý tối ưu Bellman
Một chiến lược tối ưu có tính chất: Cho dù trạng thái ban đầu và quyết định ban đầu là gì, các quyết định tiếp theo phải tạo thành một chiến lược tối ưu đối với trạng thái sinh ra từ quyết định đầu tiên.

Xét chuỗi thời gian hữu hạn từ $t = 0$ đến $t = T$. Đặt $V_t(s)$ là **hàm giá trị (Value Function)**, biểu diễn tổng chi phí nhỏ nhất có thể đạt được nếu bắt đầu từ trạng thái $s$ tại thời điểm $t$ cho đến khi kết thúc.

Phương trình truy hồi Bellman được thiết lập bằng cách giải ngược từ tương lai về hiện tại (Backward Induction):
1. **Điều kiện biên tại đích**:
   $$
   V_T(s) = h(s).
   $$
2. **Phương trình đệ quy Bellman**:
   $$
   V_t(s) = \min_{a \in \mathcal{A}_t(s)} \left[ c_t(s, a) + V_{t+1}(\mathcal{T}_t(s, a)) \right].
   $$

### 6.2. Tính Markov của không gian trạng thái
Để quy hoạch động hoạt động chính xác, **trạng thái $s$ phải chứa đủ toàn bộ thông tin trong quá khứ cần thiết để định đoạt tương lai**. Nếu chi phí hoặc tập hành động tương lai còn phụ thuộc vào con đường dẫn tới trạng thái đó, bài toán vi phạm tính chất Markov. Khi đó, ta bắt buộc phải mở rộng không gian trạng thái (State Space Augmentation) để khôi phục tính Markov.

---

## 7. Tính toán Bellman trên Đồ thị có hướng không chu trình (DAG)

Trên một đồ thị có hướng không chu trình (DAG), thứ tự topo cung cấp một trật tự thời gian tự nhiên: Mọi cạnh đều đi từ nút có chỉ số nhỏ sang nút có chỉ số lớn. Điều này cho phép ta giải phương trình Bellman một cách tuần tự từ đích $T$ ngược về nguồn $S$ với độ phức tạp tuyến tính tối ưu $\mathcal{O}(|V| + |E|)$.

Xét bài toán tìm đường đi ngắn nhất từ đỉnh xuất phát $S$ đến đỉnh đích $T$ trên đồ thị có các cạnh và trọng số chi phí như sau:

| Cạnh có hướng | Chi phí $c_{uv}$ |
| :--- | :---: |
| $S \to A$ | 1 |
| $S \to B$ | 4 |
| $A \to B$ | 2 |
| $A \to T$ | 5 |
| $B \to T$ | 1 |

Khởi tạo giá trị tại đích $V(T) = 0$ và tính lùi:
1. **Tại đỉnh $B$**: $V(B) = c(B, T) + V(T) = 1 + 0 = 1$, hành động tối ưu $\pi(B) = T$.
2. **Tại đỉnh $A$**: 
   $$
   V(A) = \min \{ c(A, B) + V(B), \, c(A, T) + V(T) \} = \min \{ 2 + 1, \, 5 + 0 \} = 3, \quad \pi(A) = B.
   $$
3. **Tại đỉnh nguồn $S$**:
   $$
   V(S) = \min \{ c(S, A) + V(A), \, c(S, B) + V(B) \} = \min \{ 1 + 3, \, 4 + 1 \} = 4, \quad \pi(S) = A.
   $$

Đường đi ngắn nhất thu hồi được là $S \to A \to B \to T$ với tổng chi phí tối ưu đúng bằng $V(S) = 4$.

---

## 8. Sự thống nhất bản chất giữa LP và DP: Cầu nối Thế năng Đối ngẫu

Liệu ta có thể giải bài toán tìm đường đi ngắn nhất trên đồ thị bằng công cụ Quy hoạch tuyến tính thuần túy?

### 8.1. Góc nhìn Đối ngẫu: Đặt thế năng tại các đỉnh
Gán cho mỗi đỉnh $u$ một biến vô hướng $v_u$ đại diện cho **tiềm năng (thế năng)** của đỉnh đó. Đặt mốc thế năng tại đích $v_T = 0$.

Trên mỗi cạnh có hướng $u \to v$ với chi phí $c_{uv}$, ta đặt điều kiện chênh lệch thế năng:
$$
v_u - v_v \le c_{uv}.
$$

Xét bất kỳ một đường đi nào từ nguồn $S$ đến đích $T$: $S = u_0 \to u_1 \to \dots \to u_k = T$. Cộng tất cả các bất đẳng thức thế năng dọc theo đường đi:
$$
(v_S - v_{u_1}) + (v_{u_1} - v_{u_2}) + \dots + (v_{u_{k-1}} - v_T) \le \sum_{i=0}^{k-1} c(u_i, u_{i+1}).
$$

Chuỗi tổng triệt tiêu hoàn toàn các thế năng trung gian, để lại:
$$
v_S - v_T = v_S \le \text{Tổng chi phí của đường đi}.
$$

Đại lượng $v_S$ là một cận dưới hợp lệ cho chi phí của **mọi đường đi từ $S$ tới $T$**. Để tìm đường đi ngắn nhất, ta tối đa hóa cận dưới này:

$$
\max \quad v_S \qquad \text{sao cho} \quad v_u - v_v \le c_{uv} \quad \forall (u \to v) \in \mathcal{E}, \quad v_T = 0.
$$

Giải bài toán LP này với đồ thị mẫu ở Mục 7, nghiệm tối ưu tìm được chính là:
$$
(v_S, v_A, v_B, v_T) = (4, 3, 1, 0).
$$

Bộ nghiệm thế năng của bài toán quy hoạch tuyến tính trùng khớp hoàn toàn từng con số với hàm giá trị Bellman $V(u)$! Hai trường phái lý thuyết đã gặp nhau tại cùng một bản chất toán học.

---

## 9. Hệ thống Bài tập Tự luyện Chuyên sâu

::: exercise 1. Chuyển đổi bài toán xấp xỉ chuẩn L1 và chuẩn cực đại L-infinity sang Quy hoạch tuyến tính
Cho hệ phương trình dữ liệu với 3 quan sát và 2 tham số:
$$
A = \begin{bmatrix} 1 & 2 \\ 2 & 1 \\ 1 & -1 \end{bmatrix}, \qquad b = \begin{bmatrix} 3 \\ 1 \\ 0 \end{bmatrix}.
$$
1. Hãy viết bài toán cực tiểu hóa sai số theo chuẩn $L_1$ ($\min_x \|A x - b\|_1$) dưới dạng một bài toán Quy hoạch tuyến tính chuẩn. Xác định số biến và số ràng buộc.
2. Hãy viết bài toán cực tiểu hóa sai số theo chuẩn $L_\infty$ ($\min_x \|A x - b\|_\infty$) dưới dạng Quy hoạch tuyến tính.
:::
::: solution
**Lời giải**:
1. Đặt biến phụ $t = (t_1, t_2, t_3)^T \in \mathbb{R}^3$ chặn trên trị tuyệt đối từng phần dư: $|a_i^T x - b_i| \le t_i$.
   Bài toán LP trở thành:
   $$
   \begin{aligned}
   \min_{x_1, x_2, t_1, t_2, t_3} \quad & t_1 + t_2 + t_3 \\
   \text{sao cho} \quad & -(t_1) \le x_1 + 2 x_2 - 3 \le t_1, \\
   & -(t_2) \le 2 x_1 + x_2 - 1 \le t_2, \\
   & -(t_3) \le x_1 - x_2 \le t_3, \\
   & t_1, t_2, t_3 \ge 0.
   \end{aligned}
   $$
   Bài toán có $n + m = 2 + 3 = 5$ biến và $2m = 6$ ràng buộc bất đẳng thức tuyến tính.

2. Đặt một biến vô hướng duy nhất $t \in \mathbb{R}$ đại diện cho sai số cực đại: $|a_i^T x - b_i| \le t$.
   Bài toán LP trở thành:
   $$
   \begin{aligned}
   \min_{x_1, x_2, t} \quad & t \\
   \text{sao cho} \quad & -t \le x_1 + 2 x_2 - 3 \le t, \\
   & -t \le 2 x_1 + x_2 - 1 \le t, \\
   & -t \le x_1 - x_2 \le t, \\
   & t \ge 0.
   \end{aligned}
   $$
   Bài toán có $n + 1 = 3$ biến và $2m = 6$ ràng buộc bất đẳng thức tuyến tính.
:::

::: exercise 2. Xác định Tâm Chebyshev của một tam giác trong mặt phẳng
Xét miền đa diện hai chiều $\mathcal{P}$ giới hạn bởi ba đường thẳng:
$$
x_1 \ge 0, \qquad x_2 \ge 0, \qquad x_1 + x_2 \le 1.
$$
1. Hãy thiết lập bài toán LP tìm tâm Chebyshev và bán kính đường tròn nội tiếp lớn nhất của $\mathcal{P}$.
2. Giải bài toán để tìm tọa độ tâm $x_c = (x_1, x_2)$ và bán kính $r^*$.
:::
::: solution
**Lời giải**:
1. Đưa các ràng buộc về dạng chuẩn $a_i^T x \le b_i$:
   - Ràng buộc 1: $-x_1 \le 0$, vector pháp tuyến $a_1 = (-1, 0)^T$, độ dài $\|a_1\|_2 = 1$.
   - Ràng buộc 2: $-x_2 \le 0$, vector pháp tuyến $a_2 = (0, -1)^T$, độ dài $\|a_2\|_2 = 1$.
   - Ràng buộc 3: $x_1 + x_2 \le 1$, vector pháp tuyến $a_3 = (1, 1)^T$, độ dài $\|a_3\|_2 = \sqrt{1^2 + 1^2} = \sqrt{2}$.

   Bài toán LP tìm tâm Chebyshev $(x_1, x_2, r)$:
   $$
   \begin{aligned}
   \max_{x_1, x_2, r} \quad & r \\
   \text{sao cho} \quad & -x_1 + r(1) \le 0 \iff x_1 \ge r, \\
   & -x_2 + r(1) \le 0 \iff x_2 \ge r, \\
   & x_1 + x_2 + r \sqrt{2} \le 1, \\
   & r \ge 0.
   \end{aligned}
   $$

2. Để cực đại hóa bán kính $r$, quả cầu phải tiếp xúc với cả ba cạnh biên.
   Từ hai ràng buộc đầu, ta có $x_1 = r$ và $x_2 = r$.
   Thay vào ràng buộc thứ ba tại biên chặt:
   $$
   r + r + r \sqrt{2} = 1 \iff r(2 + \sqrt{2}) = 1 \iff r^* = \frac{1}{2 + \sqrt{2}} = \frac{2 - \sqrt{2}}{2} = 1 - \frac{\sqrt{2}}{2} \approx 0.2929.
   $$
   Tâm Chebyshev của tam giác là:
   $$
   x_c^* = \left( 1 - \frac{\sqrt{2}}{2}, \, 1 - \frac{\sqrt{2}}{2} \right) \approx (0.2929, 0.2929).
   $$
:::

::: exercise 3. Tính toán nghiệm Chuẩn nhỏ nhất cho hệ phương trình thiếu định
Cho ma trận $A = \begin{bmatrix} 1 & 1 & 1 \end{bmatrix}$ và vector $b = [3]$.
1. Tìm nghiệm chuẩn nhỏ nhất theo chuẩn Euclid $L_2$: Cực tiểu hóa $\min \|x\|_2$ sao cho $A x = b$.
2. Tìm nghiệm chuẩn nhỏ nhất theo chuẩn $L_1$: Cực tiểu hóa $\min \|x\|_1$ sao cho $A x = b$.
:::
::: solution
**Lời giải**:
1. Áp dụng công thức giải tích chuẩn nhỏ nhất $L_2$:
   $$
   x^* = A^T (A A^T)^{-1} b.
   $$
   Ta có $A A^T = 1^2 + 1^2 + 1^2 = [3]$. Nghịch đảo $(A A^T)^{-1} = [1/3]$.
   Do đó:
   $$
   x^* = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \left(\frac{1}{3}\right) [3] = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}.
   $$
   Chuẩn Euclid đạt được là $\|x^*\|_2 = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3} \approx 1.732$.

2. Với chuẩn $L_1$: Ta muốn tìm $x = (x_1, x_2, x_3)^T$ thỏa mãn $x_1 + x_2 + x_3 = 3$ sao cho $|x_1| + |x_2| + |x_3|$ nhỏ nhất.
   Theo bất đẳng thức tam giác:
   $$
   |x_1| + |x_2| + |x_3| \ge |x_1 + x_2 + x_3| = |3| = 3.
   $$
   Dấu bằng đạt được khi các biến không âm và tổng bằng 3. Chẳng hạn:
   $x_{(1)}^* = (3, 0, 0)^T$, hoặc $x_{(2)}^* = (0, 3, 0)^T$, hoặc $x_{(3)}^* = (0, 0, 3)^T$.
   Các điểm cực của tập nghiệm chuẩn $L_1$ nhỏ nhất đều là các **vector thưa** (chỉ có 1 phần tử khác 0, các phần tử còn lại bằng 0). Đây là minh chứng trực quan cho tính chất thúc đẩy nghiệm thưa của chuẩn $L_1$.
:::

---

## Tóm tắt cốt lõi

1. **Hình học Quy hoạch tuyến tính (LP)**: Nghiệm tối ưu của bài toán LP luôn đạt được tại các **đỉnh cực (extreme points)** của khối đa diện lồi ràng buộc.
2. **Đại số Nghiệm cơ sở (BFS)**: Biến bù (slack) đưa bài toán về dạng chuẩn $A x = b, x \succeq 0$. Mỗi nghiệm cơ sở khả thi đại số tương ứng chính xác với một đỉnh cực hình học.
3. **Xấp xỉ theo chuẩn**: Bài toán xấp xỉ sai số theo chuẩn $L_1$ và chuẩn $L_\infty$ đều có thể chuyển đổi tương đương về bài toán Quy hoạch tuyến tính.
4. **Định tâm Chebyshev**: Tìm điểm trung tâm đại diện sâu nhất của miền đa diện quy về bài toán LP với ràng buộc hình học quả cầu.
5. **Quy hoạch động Bellman (DP)**: Khai thác cấu trúc bài toán con tối ưu và tính Markov để phân rã bài toán chuỗi quyết định, giải ngược từ đích về nguồn với độ phức tạp tuyến tính trên DAG.
6. **Sự thống nhất giữa LP và DP**: Biến tiềm năng đối ngẫu trong bài toán LP tìm đường ngắn nhất chính là hàm giá trị Bellman, khẳng định sự hợp lưu sâu sắc giữa hai nhánh toán học tối ưu.

---

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press. Đọc kỹ Chương 4 (Quy hoạch tuyến tính), Chương 6 (Bài toán xấp xỉ theo chuẩn), Chương 7 (Ước lượng thống kê), và Chương 8 (Các bài toán hình học).
- Dimitris Bertsimas, John N. Tsitsiklis, *Introduction to Linear Optimization*, Athena Scientific.
- Richard Bellman, *Dynamic Programming*, Princeton University Press.
- Richard S. Sutton, Andrew G. Barto, *Reinforcement Learning: An Introduction*, MIT Press.

Tiếp theo: [Lộ trình học tập tổng quan môn Cơ sở toán học cho AI](../notes/lo-trinh.md).
