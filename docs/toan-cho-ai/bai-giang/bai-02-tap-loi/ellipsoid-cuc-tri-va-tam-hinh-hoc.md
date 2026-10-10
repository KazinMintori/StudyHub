---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: ellipsoid-cuc-tri-va-tam-hinh-hoc
section: topic
title: "Ellipsoid thể tích cực trị và Các điểm tâm hình học"
description: "Mô hình hóa ellipsoid bao ngoài nhỏ nhất Loewner-John, ellipsoid nội tiếp thể tích cực đại bên trong đa diện, tâm Chebyshev và tâm giải tích thông qua quy hoạch tuyến tính và log-det."
---

Trong hình học lồi và tối ưu hóa số trị, một tập lồi phức tạp (chẳng hạn như một đa diện có hàng ngàn mặt biên hoặc bao lồi của hàng triệu điểm dữ liệu) thường rất khó thao tác trực tiếp. Để đơn giản hóa tính toán, người ta tìm cách xấp xỉ tập lồi đó bằng một **ellipsoid** (hình bầu dục nhiều chiều). Trong tất cả các hình học lồi, ellipsoid là đối tượng duy nhất vừa giữ được tính trơn bậc hai hoàn hảo, vừa có thể biểu diễn gọn gàng qua ánh xạ affine của quả cầu Euclid.

Hai bài toán hình học kinh điển nảy sinh một cách tự nhiên:
1. Tìm ellipsoid có thể tích nhỏ nhất bao trùm toàn bộ tập dữ liệu (Ellipsoid Loewner–John).
2. Tìm ellipsoid có thể tích lớn nhất nằm lọt hoàn toàn bên trong một đa diện.

Đi kèm với các ellipsoid này là các khái niệm **tâm hình học** (Tâm Chebyshev và Tâm giải tích), đóng vai trò sống còn trong việc chọn điểm khởi đầu cho các thuật toán tối ưu hóa quy mô lớn và đánh giá độ bền vững (adversarial robustness) của các mô hình học máy.

## 1. Biểu diễn toán học của Ellipsoid

Một ellipsoid $\mathcal{E}$ trong không gian $n$ chiều $\mathbb{R}^n$ có thể được tham số hóa theo hai cách tương đương:

### Cách 1: Dạng ma trận nghịch đảo và tâm (Dạng định chuẩn)
$$
\mathcal{E} = \big\{ x \in \mathbb{R}^n \mid (x - x_c)^T P^{-1} (x - x_c) \le 1 \big\},
$$
trong đó $x_c \in \mathbb{R}^n$ là tâm của ellipsoid và $P \in \mathbb{S}_{++}^n$ là ma trận đối xứng xác định dương. Nếu viết $P^{-1} = A^2$ với $A \in \mathbb{S}_{++}^n$ và đặt $b = -A x_c$, ta có:

$$
\mathcal{E} = \big\{ x \in \mathbb{R}^n \mid \|Ax + b\|_2 \le 1 \big\}.
$$

Thể tích của ellipsoid khi đó tỷ lệ nghịch với định thức của $A$:

$$
\operatorname{Vol}(\mathcal{E}) \propto \det(A^{-1}) = \frac{1}{\det A}.
$$

### Cách 2: Dạng ánh xạ affine của quả cầu đơn vị (Dạng sinh)
$$
\mathcal{E} = \big\{ B u + d \mid \|u\|_2 \le 1 \big\},
$$
trong đó $d \in \mathbb{R}^n$ là tâm và $B \in \mathbb{S}_{++}^n$ là ma trận định dạng các trục bán kính. Thể tích của ellipsoid tỷ lệ thuận trực tiếp với định thức của $B$:

$$
\operatorname{Vol}(\mathcal{E}) \propto \det B.
$$

Cách biểu diễn 1 rất thuận tiện khi xét bài toán bao ngoài (ràng buộc điểm nằm trong ellipsoid), trong khi cách biểu diễn 2 rất thuận lợi cho bài toán nội tiếp (ràng buộc ellipsoid nằm trong đa diện).

## 2. Ellipsoid Loewner–John (Bao ngoài thể tích cực tiểu)

Cho tập lồi bị chặn $C \subset \mathbb{R}^n$ có phần trong khác rỗng. Ta tìm ellipsoid $\mathcal{E} = \{x \mid \|Ax + b\|_2 \le 1\}$ có thể tích nhỏ nhất chứa $C$.

Cực tiểu hóa thể tích tương đương với việc cực đại hóa $\det A$, hay cực tiểu hóa $-\log \det A$:

$$
\begin{aligned}
\min_{A, b} \quad & -\log \det A \\
\text{sao cho} \quad & \sup_{x \in C} \|Ax + b\|_2 \le 1, \\
& A \in \mathbb{S}_{++}^n.
\end{aligned}
$$

### Trường hợp $C$ là bao lồi của tập hữu hạn điểm
Nếu $C = \operatorname{conv}\{x_1, x_2, \dots, x_m\}$, một ellipsoid chứa $C$ khi và chỉ khi nó chứa toàn bộ $m$ điểm mút $x_1, \dots, x_m$. Ràng buộc vô hạn được thu gọn thành đúng $m$ bất đẳng thức chuẩn bậc hai:

$$
\begin{aligned}
\min_{A, b} \quad & -\log \det A \\
\text{sao cho} \quad & \|Ax_i + b\|_2 \le 1, \quad \forall i = 1, \dots, m, \\
& A \in \mathbb{S}_{++}^n.
\end{aligned}
$$

Vì hàm mục tiêu $-\log \det A$ là hàm lồi ngặt và các ràng buộc $\|Ax_i + b\|_2 \le 1$ là các ràng buộc lồi theo biến $(A, b)$, bài toán này là một bài toán tối ưu lồi giải được chuẩn xác bằng phương pháp điểm trong.

```mermaid
flowchart LR
    A["Tập lồi C"] --> B["Ellipsoid Loewner-John bao ngoài E"]
    B --> C["Co lại tâm theo tỷ lệ 1/n"]
    C --> D["Ellipsoid con nằm lọt trong C: (1/n)E ⊆ C ⊆ E"]
```

### Định lý Loewner–John về tỷ lệ kẹp
Định lý kinh điển của nhà toán học Charles Loewner và Fritz John chỉ ra rằng: Nếu $\mathcal{E}$ là ellipsoid Loewner–John của tập lồi $C$, và ta co ellipsoid này lại quanh tâm $x_c$ của nó theo tỷ lệ $1/n$:

$$
x_c + \frac{1}{n} (\mathcal{E} - x_c) \subseteq C \subseteq \mathcal{E}.
$$

Hệ số co $1/n$ này là cận chặt nhất trong trường hợp tổng quát (đạt được tại một hình đơn hình). Nếu tập $C$ đối xứng qua gốc tọa độ ($C = -C$), tỷ lệ kẹp tăng vọt lên tới $1/\sqrt{n}$. Đây là bảo đảm lý thuyết vững chắc cho thấy mọi tập lồi nhiều chiều đều có thể xấp xỉ xích sao bằng một ellipsoid.

## 3. Ellipsoid nội tiếp thể tích cực đại bên trong đa diện

Bây giờ ta đảo ngược bài toán: Cho một tập đa diện bị chặn được mô tả bởi hệ $m$ bất đẳng thức tuyến tính:

$$
\mathcal{P} = \big\{ x \in \mathbb{R}^n \mid a_i^T x \le b_i, \; \forall i = 1, \dots, m \big\}.
$$

Ta muốn tìm một ellipsoid $\mathcal{E} = \{Bu + d \mid \|u\|_2 \le 1\}$ có thể tích lớn nhất nằm lọt hoàn toàn bên trong $\mathcal{P}$.

Điều kiện $\mathcal{E} \subseteq \mathcal{P}$ đồng nghĩa với việc với mọi vector $u$ có $\|u\|_2 \le 1$ và mọi mặt biên $i$:

$$
a_i^T (Bu + d) \le b_i.
$$

Lấy giá trị lớn nhất theo $u$ trên quả cầu đơn vị:

$$
\sup_{\|u\|_2 \le 1} a_i^T (Bu + d) = a_i^T d + \sup_{\|u\|_2 \le 1} (B a_i)^T u = a_i^T d + \|B a_i\|_2.
$$

Do đó, điều kiện hình học phức tạp được rút gọn thành một hệ bất đẳng thức nón bậc hai rất gọn gàng:

$$
a_i^T d + \|B a_i\|_2 \le b_i, \qquad \forall i = 1, \dots, m.
$$

Bài toán tìm ellipsoid nội tiếp lớn nhất trở thành bài toán tối ưu lồi:

$$
\begin{aligned}
\max_{B, d} \quad & \log \det B \\
\text{sao cho} \quad & \|B a_i\|_2 + a_i^T d \le b_i, \quad \forall i = 1, \dots, m, \\
& B \in \mathbb{S}_{++}^n.
\end{aligned}
$$

Hàm mục tiêu $\log \det B$ là hàm lõm, các ràng buộc $\|B a_i\|_2 + a_i^T d \le b_i$ là các ràng buộc lồi theo cặp biến $(B, d)$. Ta có thể giải bài toán này để tìm được hình dạng và hướng xoay lý tưởng của cấu trúc bên trong đa diện.

## 4. Các điểm tâm hình học của Đa diện

Khi cần chọn một điểm đại diện "nằm sâu nhất" bên trong một đa diện (ví dụ để làm điểm khởi đầu cho thuật toán tối ưu hoặc chọn bộ tham số an toàn nhất), hai khái niệm tâm hình học đóng vai trò trung tâm:

### Tâm Chebyshev (Chebyshev Center)
Tâm Chebyshev là tâm của quả cầu Euclid lớn nhất nội tiếp bên trong đa diện $\mathcal{P}$. 

Nếu quả cầu có tâm $x_c \in \mathbb{R}^n$ và bán kính $r \ge 0$, điều kiện quả cầu nằm trong $\mathcal{P}$ tương ứng với trường hợp $B = r I_n$ ở mục trước:

$$
\|r I_n a_i\|_2 + a_i^T x_c \le b_i \iff a_i^T x_c + r \|a_i\|_2 \le b_i.
$$

Cực đại hóa bán kính $r$ dẫn trực tiếp tới một **Quy hoạch tuyến tính (LP)**:

$$
\begin{aligned}
\max_{x_c, r} \quad & r \\
\text{sao cho} \quad & a_i^T x_c + r \|a_i\|_2 \le b_i, \quad \forall i = 1, \dots, m, \\
& r \ge 0.
\end{aligned}
$$

Bán kính tối ưu $r^*$ chính là khoảng cách từ tâm Chebyshev tới mặt phẳng biên gần nhất của đa diện.

### Tâm giải tích (Analytic Center)
Tâm giải tích là điểm cực tiểu hóa hàm chắn logarit (Logarithmic Barrier) của toàn bộ các mặt biên:

$$
x_{\mathrm{ac}} = \arg\min_{x \in \operatorname{int}(\mathcal{P})} \phi(x) = -\sum_{i=1}^m \log(b_i - a_i^T x).
$$

Hàm số $\phi(x)$ là hàm lồi ngặt và tiến ra $+\infty$ khi $x$ tiến tới bất kỳ mặt biên nào. Đạo hàm của hàm chắn tại tâm giải tích triệt tiêu:

$$
\nabla \phi(x_{\mathrm{ac}}) = \sum_{i=1}^m \frac{a_i}{b_i - a_i^T x_{\mathrm{ac}}} = 0.
$$

Về mặt cơ học, điều này có nghĩa là tâm giải tích là điểm cân bằng tĩnh học: Nếu mỗi mặt biên tác dụng một lực đẩy tỉ lệ nghịch với khoảng cách tới điểm đó, thì tâm giải tích là vị trí mà tổng các lực đẩy triệt tiêu hoàn toàn. Tâm giải tích phụ thuộc vào cách biểu diễn các phương trình mặt phẳng (nếu nhân đôi một ràng buộc, lực đẩy từ phía đó tăng gấp đôi).

## 5. Ví dụ tính toán minh họa

Xét đa diện hai chiều $\mathcal{P} \subset \mathbb{R}^2$ được giới hạn bởi tam giác:

$$
x_1 \ge 0, \quad x_2 \ge 0, \quad x_1 + x_2 \le 1.
$$

Viết lại dưới dạng chuẩn $a_i^T x \le b_i$:
- Mặt 1: Bất đẳng thức $-x_1 \le 0$, cho $a_1 = (-1, 0)^T$, $b_1 = 0$, $\|a_1\|_2 = 1$.
- Mặt 2: Bất đẳng thức $-x_2 \le 0$, cho $a_2 = (0, -1)^T$, $b_2 = 0$, $\|a_2\|_2 = 1$.
- Mặt 3: Bất đẳng thức $x_1 + x_2 \le 1$, cho $a_3 = (1, 1)^T$, $b_3 = 1$, $\|a_3\|_2 = \sqrt{2}$.

### Tìm tâm Chebyshev
Các ràng buộc bán kính trở thành:
1. $-x_1 + r(1) \le 0 \implies x_1 \ge r$.
2. $-x_2 + r(1) \le 0 \implies x_2 \ge r$.
3. $x_1 + x_2 + r\sqrt{2} \le 1$.

Để cực đại hóa $r$, ta chọn $x_1 = x_2 = r$. Thay vào bất đẳng thức thứ ba:

$$
2r + r\sqrt{2} \le 1 \iff r(2 + \sqrt{2}) \le 1 \implies r^* = \frac{1}{2 + \sqrt{2}} = 1 - \frac{\sqrt{2}}{2} \approx 0{,}2929.
$$

Tâm Chebyshev tương ứng:

$$
x_c^* = \left(1 - \frac{\sqrt{2}}{2}, 1 - \frac{\sqrt{2}}{2}\right) \approx (0{,}2929, 0{,}2929).
$$

Đây chính là tâm đường tròn nội tiếp tam giác vuông cân đơn vị.

## Bài tập tự luyện

::: exercise Tìm tâm giải tích của tam giác đơn vị
Xét tam giác đơn vị ở ví dụ trên với hàm chắn logarit:

$$
\phi(x) = -\log(x_1) - \log(x_2) - \log(1 - x_1 - x_2).
$$

1. Tính gradient của $\phi(x)$ theo $(x_1, x_2)$.
2. Giải hệ phương trình $\nabla \phi(x) = 0$ để tìm tọa độ tâm giải tích $x_{\mathrm{ac}}$.
3. So sánh tọa độ của tâm giải tích với tâm Chebyshev và trọng tâm tam giác.
:::

::: solution
1. **Tính đạo hàm riêng**:
   $$
   \begin{aligned}
   \frac{\partial \phi}{\partial x_1} &= -\frac{1}{x_1} + \frac{1}{1 - x_1 - x_2}, \\
   \frac{\partial \phi}{\partial x_2} &= -\frac{1}{x_2} + \frac{1}{1 - x_1 - x_2}.
   \end{aligned}
   $$

2. **Tìm nghiệm triệt tiêu gradient**:
   Cho $\nabla \phi(x) = 0$:
   $$
   \frac{1}{x_1} = \frac{1}{x_2} = \frac{1}{1 - x_1 - x_2}.
   $$
   Suy ra $x_1 = x_2$. Đặt $x_1 = x_2 = u$, ta có:
   $$
   \frac{1}{u} = \frac{1}{1 - 2u} \iff 1 - 2u = u \iff 3u = 1 \implies u = \frac{1}{3}.
   $$
   Vậy tâm giải tích là điểm $x_{\mathrm{ac}} = (1/3, 1/3)$.

3. **Bình luận so sánh**:
   - Trọng tâm hình học tam giác:
     $$
     x_{\mathrm{centroid}} = \frac{1}{3}(0,0) + \frac{1}{3}(1,0) + \frac{1}{3}(0,1) = \left(\frac{1}{3}, \frac{1}{3}\right).
     $$
     Trong trường hợp đơn hình chuẩn, tâm giải tích trùng khớp hoàn toàn với trọng tâm.
   - Tâm Chebyshev: Điểm $x_c \approx (0{,}2929, 0{,}2929)$ nằm gần gốc tọa độ hơn một chút do chịu lực cản bởi mặt cạnh huyền dốc $\sqrt{2}$.
:::

## Tóm tắt

Ellipsoid thể tích cực trị và các điểm tâm hình học cung cấp những công cụ đại số mạnh mẽ để đơn giản hóa cấu trúc của các tập lồi nhiều chiều:
- **Ellipsoid Loewner–John**: Bao ngoài chặt chẽ nhất, bảo đảm hệ số co kẹp $1/n$ trong không gian $n$ chiều qua bài toán cực tiểu hóa $-\log \det A$.
- **Ellipsoid nội tiếp thể tích cực đại**: Tìm cấu trúc trơn lớn nhất bên trong đa diện thông qua bài toán cực đại hóa $\log \det B$ với các ràng buộc nón bậc hai.
- **Tâm Chebyshev & Tâm giải tích**: Đưa việc tìm điểm đại diện trung tâm về một Quy hoạch tuyến tính (LP) hoặc bài toán tối ưu hàm chắn không ràng buộc, đóng vai trò bản lề trong phương pháp điểm trong và đánh giá độ bền vững tham số của các mô hình AI.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press, Chapter 8: Geometric Problems (§§8.4–8.5).
