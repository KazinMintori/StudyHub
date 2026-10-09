---
course: toan-cho-ai
lecture: bai-07-quy-hoach-tuyen-tinh-va-dong
section: lecture
title: "Quy hoạch tuyến tính và quy hoạch động"
prerequisites: ["ma-tran", "he-phuong-trinh", "tap-loi", "do-thi"]
lessonStatus: ready
description: "Khám phá hình học đa diện, nghiệm cơ sở trong quy hoạch tuyến tính và nguyên lý Bellman; vén màn mối liên hệ kỳ diệu giữa biến tiềm năng đối ngẫu và hàm giá trị trên đồ thị."
---

Trong bức tranh toàn cảnh của toán học tối ưu hóa dành cho Trí tuệ Nhân tạo, có hai trường phái tư duy kinh điển, đại diện cho hai góc nhìn hoàn toàn khác nhau về bài toán ra quyết định quy mô lớn:

1. **Quy hoạch tuyến tính (Linear Programming - LP)**: Tiếp cận bài toán dưới **góc nhìn hình học không gian tĩnh**. Mọi giới hạn tài nguyên đan xen tạo thành một khối đa diện lồi nhiều chiều (polyhedron), và mục tiêu là tìm kiếm một "đỉnh cực" (extreme point) cao nhất hoặc thấp nhất trên khối đa diện đó. LP là xương sống của các hệ thống phân bổ tài nguyên, điều độ luồng mạng, và lập lịch tính toán trên các cụm máy chủ huấn luyện mô hình ngôn ngữ lớn (LLM).
2. **Quy hoạch động (Dynamic Programming - DP)**: Tiếp cận bài toán dưới **góc nhìn chuỗi quyết định động theo thời gian**. Nhà toán học Richard Bellman đã đúc kết một chân lý sâu sắc: một quyết định dài hạn tối ưu luôn có thể phân rã thành một bước hành động tức thời cộng với giá trị tối ưu của phần bài toán còn lại. DP là linh hồn của các thuật toán tìm đường, giải mã chuỗi (Viterbi decoding, Beam Search trong mô hình ngôn ngữ) và là nền tảng toán học trực tiếp của Học tăng cường (Reinforcement Learning - RL).

Điều kỳ diệu nhất mà chúng ta sẽ khám phá trong bài giảng này: **hai trường phái tưởng chừng tách biệt ấy thực chất lại là hai mặt của cùng một đồng xu**. Biến tiềm năng (thế năng) trong bài toán đối ngẫu tuyến tính của đường đi ngắn nhất chính là hàm giá trị tối ưu của phương trình Bellman.

---

## 1. Bản chất hình học của Quy hoạch tuyến tính (LP)

Một bài toán quy hoạch tuyến tính xuất hiện khi cả hàm mục tiêu lẫn các ràng buộc đều là hàm bậc nhất (tuyến tính hoặc affine).

Xét bài toán tối ưu phân bổ tài nguyên hai chiều:

$$
\max_{x,y} 3x + 2y
$$

thỏa mãn các ràng buộc tài nguyên:

$$
x + y \le 4, \qquad x \le 2, \qquad x \ge 0, \quad y \ge 0.
$$

### Hình học của miền khả thi và các đỉnh cực

Mỗi bất đẳng thức tuyến tính $a_i^T z \le b_i$ xác định một nửa không gian đóng (closed halfspace) lồi. Miền khả thi $\mathcal{P}$ là giao của 4 nửa không gian đó, tạo thành một **đa diện lồi (polyhedron)** hai chiều được bao bọc bởi 4 đỉnh (vertices):
- Đỉnh $A(0, 0)$: Giá trị mục tiêu $3(0) + 2(0) = 0$.
- Đỉnh $B(2, 0)$: Giá trị mục tiêu $3(2) + 2(0) = 6$.
- Đỉnh $C(2, 2)$: Giao của $x=2$ và $x+y=4$. Giá trị mục tiêu $3(2) + 2(2) = 10$.
- Đỉnh $D(0, 4)$: Giao của $x=0$ và $x+y=4$. Giá trị mục tiêu $3(0) + 2(4) = 8$.

Nghiệm tối ưu đạt được tại đỉnh $C(2, 2)$ với giá trị mục tiêu cực đại bằng $10$.

<MathLab type="lp">

```js
const values = vertices.map(([x,y]) => c1*x+c2*y);
const best = Math.max(...values);
```

</MathLab>

### Định lý cơ bản của Quy hoạch tuyến tính

Một điểm $x \in \mathcal{P}$ được gọi là **điểm cực (extreme point)** của tập lồi nếu nó không thể biểu diễn thành tổ hợp lồi thực sự của hai điểm phân biệt trong tập, nghĩa là không tồn tại $y, z \in \mathcal{P}$ ($y \ne z$) và $\theta \in (0, 1)$ sao cho $x = \theta y + (1 - \theta)z$. Với tập đa diện, khái niệm điểm cực trùng khớp hoàn toàn với khái niệm **đỉnh (vertex)** hình học.

::: tip Định lý nền tảng về sự tồn tại của đỉnh tối ưu
Nếu miền khả thi đa diện $\mathcal{P}$ khác rỗng, không chứa đường thẳng vô hạn hai chiều (có ít nhất một điểm cực) và hàm mục tiêu bị chặn trên miền đó, thì **luôn tồn tại ít nhất một điểm cực đạt giá trị tối ưu**.
:::

*Trực giác sư phạm*: Các đường đồng mức của hàm mục tiêu tuyến tính $c_1 x + c_2 y = \text{const}$ là các đường thẳng song song. Khi ta "đẩy" đường thẳng này theo chiều vector gradient $c = (c_1, c_2)^T$ ra xa nhất có thể trong khi vẫn chạm vào đa diện $\mathcal{P}$, điểm tiếp xúc cuối cùng bao giờ cũng chạm vào một đỉnh (hoặc cả một cạnh nối hai đỉnh). 

Chẳng hạn, nếu ta thay đổi vector trọng số thành $c_1 = 1, c_2 = 1$, đường mức sẽ song song với cạnh $x + y = 4$. Khi đó, mọi điểm nằm trên đoạn thẳng nối giữa hai đỉnh $(0, 4)$ và $(2, 2)$ đều là nghiệm tối ưu với cùng giá trị mục tiêu bằng 4.

---

## 2. Đại số tuyến tính của LP: Dạng chuẩn và Biến bù (Slack Variables)

Để đưa bài toán vào máy tính giải bằng thuật toán Simplex hoặc các phương pháp điểm trong (Interior-point methods), ta đưa mọi bài toán LP về **dạng chuẩn (Standard Form)**:

$$
\min_{x} c^T x \qquad \text{sao cho} \quad A x = b, \quad x \succeq 0.
$$

### Kỹ thuật chuyển đổi về dạng chuẩn
1. **Đổi mục tiêu**: $\max f(x) \iff \min -f(x)$.
2. **Chuyển bất đẳng thức $\le$ thành đẳng thức**: Thêm **biến bù (slack variable)** $s_i \ge 0$:
   $$
   a_i^T x \le b_i \iff a_i^T x + s_i = b_i, \quad s_i \ge 0.
   $$
3. **Chuyển bất đẳng thức $\ge$ thành đẳng thức**: Trừ đi **biến dư (surplus variable)** $e_i \ge 0$:
   $$
   a_i^T x \ge b_i \iff a_i^T x - e_i = b_i, \quad e_i \ge 0.
   $$
4. **Biến tự do không giới hạn dấu**: Nếu một biến $u$ có thể nhận giá trị âm tùy ý, ta tách thành hiệu của hai biến không âm: $u = u^+ - u^-$ với $u^+, u^- \ge 0$.

Áp dụng vào bài toán ở Mục 1, ta thêm hai biến bù $s_1, s_2 \ge 0$ cho hai ràng buộc tài nguyên:

$$
\min (-3x - 2y) \qquad \text{sao cho} \quad \begin{cases} x + y + s_1 = 4 \\ x + s_2 = 2 \end{cases}, \quad x, y, s_1, s_2 \ge 0.
$$

*Ý nghĩa thực tế của biến bù*: Biến slack đo lường chính xác lượng tài nguyên còn dư thừa chưa dùng hết. Tại nghiệm tối ưu $(x, y) = (2, 2)$, ta có $s_1 = 4 - (2+2) = 0$ và $s_2 = 2 - 2 = 0$. Cả hai ràng buộc đều hoạt động hết công suất (active/binding), không còn dư thừa một chút tài nguyên nào!

---

## 3. Nghiệm cơ sở khả thi (Basic Feasible Solution - BFS)

Giả sử ma trận ràng buộc $A$ có kích thước $m \times n$ ($m$ ràng buộc đẳng thức, $n$ biến với $n > m$) và có đủ hạng hàng ($\operatorname{rank}(A) = m$).

Một tập con gồm $m$ chỉ số cột độc lập tuyến tính được gọi là **tập cơ sở (basis)** $B$. Khi đó, ta phân tách:
- $A = [A_B \mid A_N]$, trong đó $A_B$ là ma trận vuông cấp $m \times m$ khả nghịch.
- Vector biến $x = [x_B^T, x_N^T]^T$.

Quy trình tìm **nghiệm cơ sở (Basic Solution)**:
1. Đặt tất cả $n - m$ biến phi cơ sở bằng 0: $x_N = 0$.
2. Giải hệ phương trình $m$ biến $m$ phương trình duy nhất:
   $$
   A_B x_B = b \implies x_B = A_B^{-1} b.
   $$
3. Nếu nghiệm thỏa mãn thêm điều kiện không âm $x_B \succeq 0$, nghiệm này được gọi là **nghiệm cơ sở khả thi (Basic Feasible Solution - BFS)**.

::: important Cầu nối giữa Đại số và Hình học
Mỗi **nghiệm cơ sở khả thi (BFS)** trong không gian đại số của dạng chuẩn tương ứng 1-1 với một **đỉnh cực (extreme point)** của đa diện trong không gian hình học. Thuật toán Simplex kinh điển của George Dantzig chính là quá trình nhảy từ đỉnh cực này sang đỉnh cực lân cận có giá trị mục tiêu tốt hơn cho đến khi chạm tới đỉnh tối ưu.
:::

Xét bài toán mẫu với ma trận:

$$
A = \begin{bmatrix} 1 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 \end{bmatrix}, \qquad b = \begin{bmatrix} 4 \\ 2 \end{bmatrix}.
$$

- **Trường hợp 1**: Chọn cơ sở $B = \{x, y\}$ (biến phi cơ sở $s_1 = s_2 = 0$).
  $$
  A_B = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} \implies \begin{cases} x + y = 4 \\ x = 2 \end{cases} \implies \begin{cases} x = 2 \\ y = 2 \end{cases}.
  $$
  Vì $x, y \ge 0$, đây là một BFS, tương ứng đúng đỉnh $(2, 2)$ với mục tiêu $10$.
- **Trường hợp 2**: Chọn cơ sở $B = \{s_1, s_2\}$ (biến phi cơ sở $x = y = 0$).
  $$
  A_B = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \implies s_1 = 4, \quad s_2 = 2.
  $$
  Đây cũng là một BFS khả thi, tương ứng đỉnh gốc tọa độ $(0, 0)$ với mục tiêu bằng $0$.

### Chứng chỉ tối ưu đối ngẫu: Không cần duyệt hết các đỉnh

Làm thế nào để chứng minh với toàn thế giới rằng giá trị $10$ tại $(2, 2)$ thực sự là giá trị cực đại mà không cần phải kiểm tra vô số điểm trong đa diện?

Một cách người ta hay dùng trong thực tế là tạo ra một **chứng chỉ đối ngẫu (dual certificate)** bằng cách nhân các ràng buộc với các trọng số dương $\lambda_1, \lambda_2 \ge 0$ rồi cộng lại:
- Nhân ràng buộc (1) với hệ số $\lambda_1 = 2$: $2x + 2y \le 2 \cdot 4 = 8$.
- Nhân ràng buộc (2) với hệ số $\lambda_2 = 1$: $1x \le 1 \cdot 2 = 2$.
- Cộng vế theo vế:
  $$
  (2x + 2y) + x \le 8 + 2 \iff 3x + 2y \le 10.
  $$

Bất đẳng thức này đúng với **mọi điểm khả thi** trong toàn bộ đa diện! Vì giá trị mục tiêu không thể nào vượt quá $10$, mà tại điểm $(2, 2)$ ta đã đạt đúng bằng $10$, điểm $(2, 2)$ bắt buộc phải là nghiệm tối ưu tuyệt đối. Bộ trọng số $(\lambda_1, \lambda_2) = (2, 1)$ chính là nghiệm của bài toán đối ngẫu Lagrange mà chúng ta đã nghiên cứu ở Bài 03!

---

## 4. Quy hoạch động và Nguyên lý tối ưu Bellman

Nếu như quy hoạch tuyến tính phân tích bài toán dựa trên cấu trúc không gian phẳng, thì **quy hoạch động (Dynamic Programming)** tổ chức việc giải quyết bài toán theo dòng chảy thời gian của các trạng thái.

### Nguyên lý tối ưu Bellman (1957)
> *"Một chiến lược tối ưu có tính chất là: cho dù trạng thái ban đầu và quyết định ban đầu là gì, các quyết định tiếp theo phải tạo thành một chiến lược tối ưu đối với trạng thái sinh ra từ quyết định đầu tiên."*

Xét chuỗi thời gian hữu hạn từ $t = 0$ đến $t = T$. Tại bước $t$:
- Hệ thống ở trạng thái $s \in \mathcal{S}$.
- Người ra quyết định chọn hành động $a \in \mathcal{A}_t(s)$.
- Chịu chi phí tức thời $c_t(s, a)$ và chuyển tất định sang trạng thái kế tiếp $s' = \mathcal{T}_t(s, a)$.
- Tại thời điểm kết thúc $T$, chịu chi phí kết thúc $h(s_T)$.

Đặt $V_t(s)$ là **hàm giá trị (Value Function)** — biểu diễn tổng chi phí nhỏ nhất có thể đạt được nếu bắt đầu từ trạng thái $s$ tại thời điểm $t$ cho đến khi kết thúc.

Phương trình truy hồi Bellman được thiết lập bằng cách giải ngược từ tương lai về hiện tại (Backward Induction):
1. **Điều kiện biên tại đích**:
   $$
   V_T(s) = h(s).
   $$
2. **Phương trình đệ quy Bellman**:
   $$
   V_t(s) = \min_{a \in \mathcal{A}_t(s)} \left[ c_t(s, a) + V_{t+1}(\mathcal{T}_t(s, a)) \right].
   $$

### Trực giác then chốt: Tính Markov của không gian trạng thái
Để quy hoạch động hoạt động chính xác, **trạng thái $s$ phải chứa đủ toàn bộ thông tin trong quá khứ cần thiết để định đoạt tương lai**. Nếu chi phí hoặc tập hành động tương lai còn phụ thuộc vào việc "ta đã đi đến trạng thái này bằng con đường nào", thì bài toán đã vi phạm tính chất Markov. Khi đó, ta bắt buộc phải mở rộng định nghĩa của trạng thái (ví dụ: gộp thêm biến nhiên liệu còn lại, thời gian đã trôi qua) để khôi phục lại tính Markov.

---

## 5. Tính toán các giá trị Bellman trên Đồ thị có hướng không chu trình (DAG)

Trên một đồ thị có hướng không có chu trình (Directed Acyclic Graph - DAG), thứ tự sắp xếp topo (topological sort) cung cấp một trật tự thời gian tự nhiên: mọi cạnh đều đi từ nút có chỉ số topo nhỏ sang nút có chỉ số topo lớn. Điều này cho phép ta giải phương trình Bellman một cách tuần tự từ đỉnh đích $T$ ngược về đỉnh nguồn $S$ với độ phức tạp tuyến tính cực kỳ tối ưu $\mathcal{O}(|V| + |E|)$.

Xét bài toán tìm đường đi ngắn nhất từ đỉnh xuất phát $S$ đến đỉnh đích $T$ trên đồ thị có các cạnh và trọng số chi phí như sau:

| Cạnh có hướng | Chi phí $c_{uv}$ |
| :--- | :---: |
| $S \to A$ | 1 |
| $S \to B$ | 4 |
| $A \to B$ | 2 |
| $A \to T$ | 5 |
| $B \to T$ | 1 |

<MathLab type="bellman">

```js
// Các nút kế tiếp đã được tính; đích T có V(T)=0.
V[node] = Math.min(...edges[node].map(([to,c]) => c+V[to]));
```

</MathLab>

### Quá trình quy nạp ngược Bellman từng bước

Ta khởi tạo giá trị tại đích $V(T) = 0$ và tính lùi:

1. **Tại đỉnh $B$**: Chỉ có một lựa chọn đi tới $T$:
   $$
   V(B) = c(B, T) + V(T) = 1 + 0 = 1, \qquad \pi(B) = T.
   $$
2. **Tại đỉnh $A$**: Có hai lựa chọn ($A \to B$ hoặc $A \to T$):
   $$
   V(A) = \min \begin{cases} c(A, B) + V(B) = 2 + 1 = 3 \\ c(A, T) + V(T) = 5 + 0 = 5 \end{cases} = 3, \qquad \pi(A) = B.
   $$
3. **Tại đỉnh nguồn $S$**: Có hai lựa chọn ($S \to A$ hoặc $S \to B$):
   $$
   V(S) = \min \begin{cases} c(S, A) + V(A) = 1 + 3 = 4 \\ c(S, B) + V(B) = 4 + 1 = 5 \end{cases} = 4, \qquad \pi(S) = A.
   $$

### Thu hồi đường đi tối ưu
Sau khi có bảng giá trị $V$ và bảng vết hành động $\pi$:
$$
S \xrightarrow{\pi(S) = A} A \xrightarrow{\pi(A) = B} B \xrightarrow{\pi(B) = T} T.
$$
Đường đi ngắn nhất là $S \to A \to B \to T$ với tổng chi phí tối ưu đúng bằng $V(S) = 4$.

::: tip Mở rộng: Bài toán Đường đi dài nhất (Critical Path)
Nếu ta thay toán tử $\min$ bằng $\max$, thuật toán sẽ tìm đường đi dài nhất trên DAG:
- $V_{\max}(T) = 0$.
- $V_{\max}(B) = 1 + 0 = 1$.
- $V_{\max}(A) = \max\{2 + 1, 5 + 0\} = 5$.
- $V_{\max}(S) = \max\{1 + 5, 4 + 1\} = 6$.

Thuật toán này là nền tảng của phương pháp phân tích đường găng (Critical Path Method - CPM) trong quản lý dự án công nghệ và tối ưu hóa độ trễ đường truyền tín hiệu trong thiết kế vi mạch tích hợp (VLSI delay placement).
:::

---

## 6. Cầu nối kỳ diệu: Biểu diễn bài toán đường đi bằng Quy hoạch tuyến tính

Hãy tạm quên đi phương trình Bellman trong chốc lát. Liệu ta có thể giải bài toán tìm đường đi ngắn nhất trên đồ thị bằng công cụ Quy hoạch tuyến tính thuần túy?

### Góc nhìn Đối ngẫu: Đặt thế năng tại các đỉnh

Gán cho mỗi đỉnh $u$ một biến vô hướng $v_u$ đại diện cho **tiềm năng (thế năng)** của đỉnh đó. Đặt mốc thế năng tại đích $v_T = 0$.

Trên mỗi cạnh có hướng $u \to v$ với chi phí $c_{uv}$, ta đặt điều kiện nhất quán về độ chênh lệch thế năng:
$$
v_u \le c_{uv} + v_v \iff v_u - v_v \le c_{uv}.
$$

*Ý nghĩa vật lý*: Thế năng tại điểm đầu $u$ không bao giờ được phép vượt quá thế năng tại điểm cuối $v$ cộng thêm chi phí di chuyển từ $u$ sang $v$.

Bây giờ, xét bất kỳ một đường đi nào từ nguồn $S$ đến đích $T$, giả sử là $S = u_0 \to u_1 \to u_2 \to \cdots \to u_k = T$. Viết các bất đẳng thức thế năng dọc theo đường đi:
$$
\begin{aligned}
v_S - v_{u_1} &\le c(S, u_1), \\
v_{u_1} - v_{u_2} &\le c(u_1, u_2), \\
&\;\;\vdots \\
v_{u_{k-1}} - v_T &\le c(u_{k-1}, T).
\end{aligned}
$$

Cộng tất cả các bất đẳng thức này lại! Một sự triệt tiêu đại số hoàn hảo (telescoping sum) diễn ra: tất cả các thế năng trung gian $v_{u_i}$ đều bị khử sạch sẽ:
$$
v_S - v_T \le \sum_{i=0}^{k-1} c(u_i, u_{i+1}) \implies v_S \le \text{Tổng chi phí của đường đi}.
$$

Bất đẳng thức này chứng minh rằng: **giá trị $v_S$ là một cận dưới hợp lệ cho chi phí của MỌI đường đi từ $S$ tới $T$**. Để tìm đường đi ngắn nhất, ta chỉ cần đẩy cận dưới này lên mức cao nhất có thể!

Ta thu được bài toán Quy hoạch tuyến tính:

$$
\max v_S \qquad \text{sao cho} \quad \begin{cases} v_u - v_v \le c_{uv} \quad \forall (u \to v) \in \mathcal{E} \\ v_T = 0 \end{cases}.
$$

Giải bài toán LP này với đồ thị mẫu ở Mục 5, nghiệm tối ưu tìm được chính là:
$$
(v_S, v_A, v_B, v_T) = (4, 3, 1, 0).
$$

Bộ nghiệm thế năng của bài toán quy hoạch tuyến tính trùng khớp từng con số một với hàm giá trị Bellman $V(u)$! Hai đỉnh cao lý thuyết xuất phát từ hai tư duy hoàn toàn khác nhau đã gặp nhau tại cùng một chân lý toán học.

### Góc nhìn Thuận nghịch: Bài toán luồng cực tiểu (Min-cost Flow)
Nếu xét bài toán thuận (Primal LP), ta coi việc tìm đường đi là bài toán đẩy một đơn vị luồng hàng hóa (1 unit of flow) từ $S$ sang $T$ qua mạng lưới các cạnh với chi phí đơn vị $c_{uv}$:
$$
\min_{x} \sum_{(u, v) \in \mathcal{E}} c_{uv} x_{uv} \qquad \text{sao cho bảo toàn luồng tại mọi đỉnh}.
$$
Nhờ tính chất **đơn mô-đun toàn phần (Total Unimodularity)** của ma trận liên thuộc đồ thị, nghiệm cơ sở khả thi của bài toán LP này luôn luôn tự động nhận giá trị nguyên $x_{uv} \in \{0, 1\}$. Cạnh nào có $x_{uv} = 1$ chính là cạnh nằm trên đường đi tối ưu!

---

## Bài tập tự luyện

::: exercise 1. Khảo sát một cơ sở đại số khác trong LP
Trong bài toán LP dạng chuẩn ở Mục 2:
$$
x + y + s_1 = 4, \qquad x + s_2 = 2, \qquad x, y, s_1, s_2 \ge 0.
$$
Hãy chọn tập cột ứng với các biến $\{y, s_2\}$ làm cơ sở $B$. Hãy tính nghiệm cơ sở tương ứng và xác định giá trị hàm mục tiêu cực đại ban đầu $3x + 2y$.
:::
::: solution
Tập biến cơ sở là $x_B = [y, s_2]^T$. Đặt các biến phi cơ sở bằng 0: $x = 0, s_1 = 0$.
Thay vào hệ phương trình:
- Phương trình (1): $0 + y + 0 = 4 \implies y = 4$.
- Phương trình (2): $0 + s_2 = 2 \implies s_2 = 2$.

Vì $y = 4 \ge 0$ và $s_2 = 2 \ge 0$, nghiệm cơ sở này hoàn toàn khả thi (BFS).
Nghiệm tương ứng với đỉnh $D(0, 4)$ trên hình học đa diện, với giá trị mục tiêu:
$$
3x + 2y = 3(0) + 2(4) = 8.
$$
:::

::: exercise 2. Tính cục bộ khi cấu trúc đồ thị thay đổi
Giả sử chi phí của cạnh $S \to B$ giảm từ $4$ xuống $2$, trong khi tất cả các cạnh khác giữ nguyên trọng số.
1. Những giá trị Bellman nào bắt buộc phải tính lại, và những giá trị nào được giữ nguyên?
2. Xác định đường đi ngắn nhất mới và tổng chi phí tương ứng.
:::
::: solution
1. Vì thuật toán Bellman giải ngược từ đích về nguồn, các đỉnh nằm ở phía sau cạnh $S \to B$ (gồm $T, B, A$) hoàn toàn không chịu ảnh hưởng bởi chi phí của cạnh xuất phát từ $S$. Do đó:
   - $V(T) = 0$, $V(B) = 1$, $V(A) = 3$ được **giữ nguyên không đổi**.
2. Ta chỉ cần tính lại giá trị tại nút nguồn $S$:
   $$
   V(S) = \min \begin{cases} c(S, A) + V(A) = 1 + 3 = 4 \\ c(S, B) + V(B) = 2 + 1 = 3 \end{cases} = 3.
   $$
   Lựa chọn tối ưu chuyển sang hành động đi tới $B$ ($\pi(S) = B$).
   Đường đi ngắn nhất mới là $S \to B \to T$ với tổng chi phí tối ưu bằng $3$.
:::

::: exercise 3. Nguyên lý mở rộng không gian trạng thái khi thiếu thông tin
Một robot tự hành cần tìm đường đi từ điểm $S$ đến đích $T$. Mỗi đoạn đường $u \to v$ tiêu tốn thời gian $c_{uv}$ và lượng pin $e_{uv}$. Robot mang theo bình pin dung lượng tối đa $Q$. Nếu ta chỉ mô tả trạng thái bằng tên đỉnh hiện tại $u$, thuật toán Bellman có đảm bảo tìm được hành trình tối ưu không? Nếu không, cần khắc phục thế nào?
:::
::: solution
1. **Không đảm bảo**. Nếu chỉ lưu trạng thái là tên đỉnh $u$, hệ thống vi phạm nghiêm trọng tính chất Markov. Một phương án đến được $u$ nhanh hơn nhưng tiêu tốn cạn pin có thể dẫn tới bế tắc ở các chặng sau; trong khi một phương án đến $u$ chậm hơn một chút nhưng còn nhiều pin lại có thể hoàn thành chuyến đi an toàn. Quyết định tối ưu trong tương lai phụ thuộc mật thiết vào lượng pin tích lũy từ quá khứ.
2. **Khắc phục**: Ta áp dụng nguyên lý **mở rộng không gian trạng thái (State Space Augmentation)**. Trạng thái mới là một cặp có thứ tự $s = (u, q)$, trong đó $u$ là vị trí hiện tại và $q \in [0, Q]$ là lượng pin còn lại. Khi đó, phương trình Bellman được thiết lập lại:
   $$
   V(u, q) = \min_{v \in \mathcal{N}(u), e_{uv} \le q} \left[ c_{uv} + V(v, q - e_{uv}) \right].
   $$
   Đây chính là phương pháp chuẩn mực được áp dụng trong Học tăng cường và Điều khiển tối ưu hiện đại.
:::

---

## Tóm tắt cốt lõi

1. **Hình học Quy hoạch tuyến tính (LP)**: Nghiệm tối ưu của bài toán LP luôn có thể tìm thấy tại các **đỉnh cực (extreme points)** của khối đa diện lồi ràng buộc.
2. **Đại số Nghiệm cơ sở (BFS)**: Biến bù (slack) đưa bài toán về dạng chuẩn. Mỗi nghiệm cơ sở khả thi đại số tương ứng chính xác với một đỉnh cực hình học.
3. **Quy hoạch động Bellman (DP)**: Khai thác cấu trúc bài toán con tối ưu và tính Markov để phân rã bài toán chuỗi quyết định, giải ngược từ đích về nguồn với độ phức tạp tuyến tính trên DAG.
4. **Sự hợp lưu giữa LP và DP**: Biến tiềm năng đối ngẫu trong bài toán LP tìm đường ngắn nhất chính là hàm giá trị Bellman, khẳng định sự thống nhất nội tại sâu sắc giữa hai nhánh toán học tối ưu.

---

## Tài liệu đọc thêm và Nghiên cứu chuyên sâu

Dành cho bạn đọc muốn đào sâu nền tảng toán học của Quy hoạch tuyến tính và Quy hoạch động:

- **Stephen Boyd & Lieven Vandenberghe**, *Convex Optimization*, Cambridge University Press, Chương 4 (Linear programming) và Chương 8 (Geometric problems).
- **Dimitris Bertsimas & John N. Tsitsiklis**, *Introduction to Linear Optimization*, Athena Scientific. Bộ giáo trình kinh điển chuẩn mực thế giới về hình học đa diện, thuật toán Simplex và tính đơn mô-đun toàn phần.
- **Richard Bellman**, *Dynamic Programming*, Princeton University Press. Tác phẩm khởi nguyên đặt nền móng cho toàn bộ lý thuyết điều khiển tối ưu hiện đại.
- **Richard S. Sutton & Andrew G. Barto**, *Reinforcement Learning: An Introduction*, MIT Press. Giáo trình bắt buộc để thấy phương trình Bellman vận hành trong các thuật toán AI đột phá như Q-learning, Policy Gradient và AlphaGo.

---

[Bài 06: Các phương pháp tối ưu trong học sâu](./bai-06-phuong-phap-thich-nghi.md) · [Lộ trình học tập](../notes/lo-trinh.md)
