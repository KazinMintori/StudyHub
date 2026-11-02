---
section: wiki
concept: nhat-quan-cung
title: "Tính nhất quán cung (Arc Consistency)"
---

## Giải thích kỹ thuật

### Định nghĩa toán học hình thức

Trong bài toán thỏa mãn ràng buộc nhị phân, một cung có hướng nối từ biến $X_i$ tới biến $X_j$ (ký hiệu là $X_i \to X_j$) được gọi là nhất quán cung (arc-consistent) nếu và chỉ nếu với mọi giá trị $a$ thuộc miền giá trị khả dĩ $D_i$, luôn tồn tại ít nhất một giá trị $b$ thuộc miền giá trị khả dĩ $D_j$ sao cho cặp giá trị $(a, b)$ thỏa mãn ràng buộc nhị phân $C_{i,j}$ giữa hai biến đó:

$$
\forall a \in D_i, \quad \exists b \in D_j : C_{i,j}(a, b)
$$

Nếu tồn tại một giá trị $a \in D_i$ không tìm thấy bất kỳ giá trị hỗ trợ (support) nào trong $D_j$, giá trị $a$ đó bắt buộc phải bị loại bỏ khỏi miền $D_i$ thông qua thủ tục $\text{REVISE}(X_i, X_j)$. Mạng lưới ràng buộc được gọi là đạt tính nhất quán cung hoàn toàn khi mọi cung có hướng trong đồ thị ràng buộc đều thỏa mãn điều kiện trên.

### Phản ví dụ đồ thị tam giác hai màu

Tính nhất quán cung là một dạng nhất quán cục bộ bậc hai (2-consistency) và không tương đương với tính khả thỏa toàn cục (satisfiability). Điều này được minh chứng rõ nét qua phản ví dụ đồ thị tam giác ba đỉnh:

Giả sử có ba biến số $A, B, C$ với miền giá trị ban đầu đều là $\{1, 2\}$. Các ràng buộc nhị phân yêu cầu các đỉnh kề nhau phải nhận giá trị khác nhau: $A \neq B, B \neq C, C \neq A$.

Khi xem xét từng cung có hướng riêng lẻ:

- Xét cung $A \to B$: Với giá trị $1 \in D_A$, tồn tại giá trị $2 \in D_B$ thỏa mãn $1 \neq 2$. Với giá trị $2 \in D_A$, tồn tại giá trị $1 \in D_B$ thỏa mãn $2 \neq 1$. Do đó cung $A \to B$ hoàn toàn nhất quán cung.
- Lập luận tương tự cho các cung còn lại: $B \to A, B \to C, C \to B, C \to A, A \to C$. Tất cả sáu cung có hướng đều thỏa mãn định nghĩa nhất quán cung.

Thuật toán AC-3 khi thực thi trên bài toán này sẽ xét hết hàng đợi cung rồi dừng mà không loại bỏ bất kỳ giá trị nào khỏi miền của ba biến. Tuy nhiên, một đồ thị tam giác ba đỉnh không thể được tô bằng hai màu. Bài toán hoàn toàn vô nghiệm (unsatisfiable). AC-3 không làm rỗng miền là điều kiện cần để CSP có nghiệm, nhưng chưa đủ để kết luận có nghiệm. Bản thân các miền ban đầu không bắt buộc đã nhất quán cung. Chẳng hạn, mạng A < B < C với các miền {1, 2, 3} có nghiệm (1, 2, 3) dù các miền ban đầu còn những giá trị không có hỗ trợ.
