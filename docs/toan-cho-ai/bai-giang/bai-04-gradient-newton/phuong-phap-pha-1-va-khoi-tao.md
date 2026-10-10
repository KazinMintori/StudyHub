---
course: toan-cho-ai
lecture: bai-04-gradient-newton
topic: phuong-phap-pha-1-va-khoi-tao
section: topic
title: "Phương pháp Pha I và tìm điểm khả thi khởi đầu"
description: "Kỹ thuật biến bù tìm điểm khả thi ngặt, phương pháp cực tiểu tổng độ vi phạm sum of infeasibilities, tiêu chí dừng sớm và ứng dụng trong các bài toán tối ưu thực tế."
---

Các thuật toán tối ưu hóa có ràng buộc kinh điển (đặc biệt là phương pháp hàm chắn logarit và phương pháp Newton khả thi) đều hoạt động dựa trên một giả định cốt tử: Ta đã có sẵn một điểm xuất phát $x^{(0)}$ khả thi ngặt, tức thỏa mãn $f_i(x^{(0)}) < 0$ với mọi $i = 1, \dots, m$ và $A x^{(0)} = b$. 

Thế nhưng trong các ứng dụng thực tế với hàng nghìn ràng buộc phức tạp, việc chỉ ra một điểm thỏa mãn tất cả các điều kiện này bằng mắt thường là điều bất khả thi, thậm chí ta còn chưa biết liệu bài toán có nghiệm khả thi nào hay không. Để giải quyết nút thắt này, lý thuyết tối ưu hóa phân chia quá trình giải thành hai giai đoạn rõ rệt:
- **Pha I (Phase I)**: Tìm một điểm khả thi ngặt hoặc chứng nhận bài toán gốc vô nghiệm.
- **Pha II (Phase II)**: Xuất phát từ điểm khả thi tìm được ở Pha I để tối ưu hóa hàm mục tiêu gốc $f_0(x)$.

## 1. Phương pháp Pha I biến bù cơ bản (Basic Phase I Method)

Xét bài toán tối ưu lồi tổng quát:

$$
\begin{aligned}
\text{minimize}\quad & f_0(x) \\
\text{subject to}\quad & f_i(x) \le 0, \quad i = 1, \dots, m, \\
& A x = b.
\end{aligned}
$$

Để tìm một điểm khả thi ngặt cho hệ ràng buộc trên, ta đưa vào một biến vô hướng bổ sung $s \in \mathbb{R}$ đóng vai trò là "mức độ vi phạm trần" lớn nhất của các ràng buộc. Bài toán Pha I được thiết lập như sau:

$$
\begin{aligned}
\text{minimize}\quad & s \\
\text{subject to}\quad & f_i(x) \le s, \quad i = 1, \dots, m, \\
& A x = b,
\end{aligned}
$$

với các biến tối ưu là $(x, s) \in \mathbb{R}^n \times \mathbb{R}$.

### Tính khả thi hiển nhiên của Pha I
Ưu thế vượt bậc của bài toán Pha I là ta luôn luôn có sẵn một điểm khởi đầu khả thi ngặt mà không tốn bất kỳ chi phí tính toán nào:
1. Trước hết, tìm một điểm $x^{(0)}$ bất kỳ thỏa mãn hệ phương trình tuyến tính $A x = b$ (bằng phép chiếu trực giao hoặc khử Gauss).
2. Sau đó, chọn giá trị biến bù ban đầu:
   $$
   s^{(0)} > \max_{i=1,\dots,m} f_i(x^{(0)}).
   $$

Khi đó, cặp $(x^{(0)}, s^{(0)})$ hiển nhiên thỏa mãn $f_i(x^{(0)}) < s^{(0)}$ và $A x^{(0)} = b$, cho phép ta lập tức áp dụng phương pháp hàm chắn để giải bài toán Pha I.

### Phân tích kết quả của Pha I
Gọi $(x^*, s^*)$ là nghiệm tối ưu toàn cục của bài toán Pha I:
- **Trường hợp $s^* < 0$**: Tồn tại một điểm $x^*$ thỏa mãn $f_i(x^*) \le s^* < 0$ với mọi $i = 1, \dots, m$. Điểm $x^*$ chính là một điểm khả thi ngặt, hoàn tất mục tiêu của Pha I và sẵn sàng làm điểm xuất phát cho Pha II.
- **Trường hợp $s^* > 0$**: Giá trị vi phạm nhỏ nhất có thể vẫn dương, đồng nghĩa với việc bài toán gốc hoàn toàn vô nghiệm khả thi (Infeasible). Các nhân tử Lagrange của Pha I tại nghiệm cung cấp một chứng chỉ bất khả thi (Infeasibility Certificate) theo định lý về các phương án thay thế của Farkas.
- **Trường hợp $s^* = 0$**: Hệ ràng buộc có nghiệm nhưng không có nghiệm khả thi ngặt (miền khả thi có phần trong rỗng, điều kiện Slater bị vi phạm).

### Tiêu chí dừng sớm (Early Stopping)
Trong ứng dụng thực tế, ta hoàn toàn không cần thiết phải giải bài toán Pha I cho đến khi hội tụ về nghiệm cực tiểu $s^*$. Mục tiêu duy nhất của Pha I là tìm một điểm có $s < 0$. Do đó, ngay khi quá trình lặp của Pha I chạm tới một điểm $(x^{(k)}, s^{(k)})$ thỏa mãn:

$$
s^{(k)} < 0,
$$

thuật toán lập tức ngắt Pha I và chuyển giao điểm $x^{(k)}$ sang làm điểm khởi đầu cho Pha II, tiết kiệm đáng kể thời gian tính toán.

## 2. Phương pháp cực tiểu tổng độ vi phạm (Sum of Infeasibilities)

Phương pháp biến bù cơ bản gán cùng một mức độ nới lỏng $s$ cho tất cả các ràng buộc. Trong trường hợp bài toán vô nghiệm khả thi, nó không cho ta biết những ràng buộc cụ thể nào đang mâu thuẫn với nhau. Để khắc phục điều này, người ta sử dụng phương pháp cực tiểu tổng độ vi phạm theo chuẩn $\ell_1$:

$$
\begin{aligned}
\text{minimize}\quad & \mathbf{1}^T s = \sum_{i=1} s_i \\
\text{subject to}\quad & f_i(x) \le s_i, \quad i = 1, \dots, m, \\
& s_i \ge 0, \quad i = 1, \dots, m, \\
& A x = b,
\end{aligned}
$$

với biến quyết định là $x \in \mathbb{R}^n$ và vector biến bù $s = (s_1, \dots, s_m)^T \in \mathbb{R}^m$.

### Ý nghĩa của chuẩn $\ell_1$ trong chẩn đoán mô hình
Mỗi thành phần $s_i$ đo lường chính xác mức độ vi phạm của riêng ràng buộc thứ $i$. Do hàm mục tiêu là chuẩn $\ell_1$ của vector $s$, nghiệm tối ưu của bài toán này có tính chất thúc đẩy độ thưa (sparsity-inducing):
- Hầu hết các biến bù sẽ bằng 0 ($s_i^* = 0$), tương ứng với các ràng buộc được thỏa mãn hoàn toàn.
- Chỉ một số ít biến bù mang giá trị dương ($s_j^* > 0$), chỉ điểm chính xác các ràng buộc xung đột gây ra hiện tượng bất khả thi của hệ thống.

Nếu giá trị tối ưu của bài toán bằng 0 ($\mathbf{1}^T s^* = 0$), ta suy ra $s^* = 0$ và điểm $x^*$ khả thi với bài toán gốc.

## 3. Bài tập tự luyện

::: exercise 1. Khởi tạo Pha I cơ bản cho hệ bất đẳng thức tuyến tính
Xét hệ bất đẳng thức tuyến tính gồm 3 ràng buộc trên mặt phẳng $\mathbb{R}^2$:
$$
\begin{aligned}
f_1(x) &= x_1 + x_2 - 2 \le 0, \\
f_2(x) &= -x_1 + x_2 - 2 \le 0, \\
f_3(x) &= -x_2 - 1 \le 0.
\end{aligned}
$$
1. Chọn điểm khởi đầu $x^{(0)} = (2, 2)^T$. Xác định giá trị biến bù ban đầu $s^{(0)}$ tối thiểu để cặp $(x^{(0)}, s^{(0)})$ khả thi ngặt với bài toán Pha I.
2. Tìm nghiệm tối ưu $(x^*, s^*)$ của bài toán Pha I.
3. Kết luận về tính khả thi của hệ bất đẳng thức gốc.
:::

::: solution
1. **Xác định giá trị $s^{(0)}$**:
   Tính giá trị của từng hàm ràng buộc tại $x^{(0)} = (2, 2)^T$:
   - $f_1(x^{(0)}) = 2 + 2 - 2 = 2$.
   - $f_2(x^{(0)}) = -2 + 2 - 2 = -2$.
   - $f_3(x^{(0)}) = -2 - 1 = -3$.
   Độ vi phạm lớn nhất:
   $$
   \max_{i=1, 2, 3} f_i(x^{(0)}) = \max\{2, -2, -3\} = 2.
   $$
   Để cặp $(x^{(0)}, s^{(0)})$ khả thi ngặt ($f_i(x^{(0)}) < s^{(0)}$ với mọi $i$), ta chỉ cần chọn $s^{(0)} > 2$ (chẳng hạn $s^{(0)} = 2{,}5$ hoặc $s^{(0)} = 3$).

2. **Tìm nghiệm tối ưu của Pha I**:
   Bài toán Pha I:
   $$
   \begin{aligned}
   \text{minimize}\quad & s \\
   \text{subject to}\quad & x_1 + x_2 - 2 \le s, \\
   & -x_1 + x_2 - 2 \le s, \\
   & -x_2 - 1 \le s.
   \end{aligned}
   $$
   Cộng hai bất đẳng thức đầu tiên:
   $$
   (x_1 + x_2 - 2) + (-x_1 + x_2 - 2) \le 2s \implies 2x_2 - 4 \le 2s \implies x_2 - 2 \le s.
   $$
   Kết hợp với bất đẳng thức thứ ba $-x_2 - 1 \le s$:
   $$
   (x_2 - 2) + (-x_2 - 1) \le s + s \implies -3 \le 2s \implies s \ge -\frac{3}{2} = -1{,}5.
   $$
   Dấu bằng $s^* = -1{,}5$ đạt được khi:
   - Hai hàm đầu bằng nhau: $x_1 + x_2 = -x_1 + x_2$, suy ra $x_1^* = 0$.
   - Khi đó $x_2 - 2 = -1{,}5$, suy ra $x_2^* = 0{,}5$.
   - Kiểm tra bất đẳng thức thứ ba: $-x_2^* - 1 = -0{,}5 - 1 = -1{,}5 = s^*$.
   Vậy nghiệm tối ưu của Pha I là $(x^*, s^*) = \big((0, 0{,}5)^T, -1{,}5\big)$.

3. **Kết luận về tính khả thi**:
   Vì $s^* = -1{,}5 < 0$, hệ bất đẳng thức gốc có nghiệm khả thi ngặt. Điểm $x^* = (0, 0{,}5)^T$ là một điểm khả thi ngặt lý tưởng (nằm sâu bên trong miền khả thi với khoảng cách an toàn bằng $1{,}5$) để khởi động Pha II.
:::

::: exercise 2. Phát hiện mâu thuẫn bằng phương pháp Sum of Infeasibilities
Xét hệ hai bất đẳng thức trên trục số thực: Giả sử $x \ge 3$ và $x \le 1$.
1. Viết bài toán cực tiểu tổng độ vi phạm $\min (s_1 + s_2)$ với $s_1, s_2 \ge 0$.
2. Tìm nghiệm tối ưu giải tích $(x^*, s_1^*, s_2^*)$.
3. Giải thích ý nghĩa của giá trị tối ưu đối với tính bất khả thi của hệ thống.
:::

::: solution
1. **Thiết lập bài toán**:
   Các hàm ràng buộc: Đặt $f_1(x) = 3 - x \le 0$ và $f_2(x) = x - 1 \le 0$.
   Bài toán tổng độ vi phạm:
   $$
   \begin{aligned}
   \text{minimize}\quad & s_1 + s_2 \\
   \text{subject to}\quad & 3 - x \le s_1, \\
   & x - 1 \le s_2, \\
   & s_1 \ge 0, \quad s_2 \ge 0.
   \end{aligned}
   $$

2. **Tìm nghiệm tối ưu**:
   Cộng hai bất đẳng thức ràng buộc:
   $$
   (3 - x) + (x - 1) \le s_1 + s_2 \implies 2 \le s_1 + s_2.
   $$
   Do đó tổng độ vi phạm luôn bị chặn dưới bởi 2: $s_1 + s_2 \ge 2$.
   Dấu bằng $s_1 + s_2 = 2$ đạt được tại mọi điểm $x \in [1, 3]$:
   - Với $x \in [1, 3]$, ta có $s_1 = 3 - x \ge 0$ và $s_2 = x - 1 \ge 0$.
   - Tổng: $s_1 + s_2 = (3 - x) + (x - 1) = 2$.
   Một nghiệm đại diện là $x^* = 2$ với $s_1^* = 1$ và $s_2^* = 1$.

3. **Ý nghĩa thống kê và hình học**:
   Giá trị tối ưu $s_1^* + s_2^* = 2 > 0$ chứng minh hệ thống ban đầu hoàn toàn vô nghiệm khả thi. Con số 2 phản ánh chính xác khoảng cách giữa hai tập nghiệm rời nhau $[3, +\infty)$ và $(-\infty, 1]$ (khoảng trống giữa hai mút $3 - 1 = 2$).
:::

::: exercise 3. Cơ chế kích hoạt dừng sớm trong Pha I
Giả sử ta giải bài toán Pha I cơ bản bằng phương pháp giảm gradient kết hợp tìm kiếm đường thẳng (Backtracking Line Search) với bước lặp $x^{(k+1)} = x^{(k)} + t^{(k)} \Delta x^{(k)}$.
1. Nêu điều kiện dừng sớm (Early Stopping Condition) của Pha I.
2. Tại sao ta không nên tiếp tục lặp cho đến khi $\nabla s \approx 0$ nếu mục đích cuối cùng là giải bài toán gốc?
3. Khi chuyển giao điểm $x^{(k)}$ sang Pha II, giá trị tham số hàm chắn $t$ nên được khởi tạo như thế nào?
:::

::: solution
1. **Điều kiện dừng sớm**:
   Tại mỗi bước lặp $k$, sau khi cập nhật biến $(x^{(k)}, s^{(k)})$, thuật toán kiểm tra ngay điều kiện:
   $$
   s^{(k)} < 0 \quad \text{hoặc} \quad \max_{i=1,\dots,m} f_i(x^{(k)}) < 0.
   $$
   Nếu điều kiện này thỏa mãn, thuật toán lập tức phát tín hiệu dừng Pha I mà không cần chờ điều kiện hội tụ gradient.

2. **Lý do không nên lặp đến tối ưu**:
   Nghiệm tối ưu $(x^*, s^*)$ của bài toán Pha I là điểm "nằm sâu nhất" trong miền khả thi (cực tiểu hóa mức vi phạm). Tuy nhiên, điểm này hoàn toàn không có mối liên hệ nào với hàm mục tiêu gốc $f_0(x)$. Việc cố gắng tìm $s^*$ chỉ tiêu tốn tài nguyên tính toán vô ích cho một hàm mục tiêu phụ, trong khi Pha II chỉ cần bất kỳ điểm nào thỏa mãn tính khả thi ngặt.

3. **Khởi tạo tham số hàm chắn $t$ cho Pha II**:
   Khi bước vào Pha II với điểm khởi đầu $x^{(0)} = x^{(k)}$, ta xây dựng hàm chắn logarit:
   $$
   \phi(x) = -\sum_{i=1}^m \log\big(-f_i(x)\big).
   $$
   Tham số hàm chắn ban đầu $t^{(0)} > 0$ thường được chọn sao cho độ lớn của gradient hàm mục tiêu $t \nabla f_0(x)$ tương đương với độ lớn của gradient hàm chắn $\nabla \phi(x)$:
   $$
   t^{(0)} \approx \frac{\|\nabla \phi(x^{(0)})\|_2}{\|\nabla f_0(x^{(0)})\|_2}.
   $$
   Cách chọn này bảo đảm bước lặp đầu tiên của phương pháp Newton trong Pha II cân bằng hài hòa giữa việc giảm mục tiêu gốc và việc giữ khoảng cách an toàn với biên khả thi.
:::

## Tóm tắt

Phương pháp Pha I là cây cầu thiết yếu đưa các thuật toán điểm trong từ lý thuyết vào ứng dụng thực tế. Bằng việc đưa vào các biến bù nới lỏng, bài toán tìm điểm khả thi ngặt được chuyển hóa thành một bài toán tối ưu lồi phụ có điểm khởi đầu hiển nhiên. 

Tiêu chí dừng sớm cho phép tiết kiệm tối đa thời gian tính toán bằng cách kết thúc Pha I ngay khi tìm được một điểm khả thi ngặt, trong khi biến thể cực tiểu hóa tổng độ vi phạm $\ell_1$ cung cấp công cụ chẩn đoán đắc lực giúp xác định chính xác các ràng buộc xung đột khi hệ thống bất khả thi.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press, Chapter 11: Interior-Point Methods (§11.4).
