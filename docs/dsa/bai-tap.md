---
title: Bài tập ôn luyện - Cấu trúc dữ liệu và giải thuật
description: Tuyển tập bài tập phân tích độ phức tạp thuật toán, cây cân bằng AVL, bảng băm, đồ thị Dijkstra và cây khung nhỏ nhất.
---

# Bài tập ôn luyện: Cấu trúc dữ liệu và giải thuật

Tài liệu tuyển chọn hệ thống bài tập cho môn Cấu trúc dữ liệu và giải thuật (DSA), bao gồm phân tích độ phức tạp thời gian, cấu trúc dữ liệu nâng cao (AVL, Heap, Bảng băm) và thuật toán đồ thị.

---

## Phần 1. Phân tích độ phức tạp & Cấu trúc dữ liệu tuyến tính

### Bài 1.1: Định lý thợ (Master Theorem) và phân tích đệ quy
Sử dụng Định lý thợ để xác định bậc độ phức tạp thời gian tiệm cận $T(n)$ cho các hệ thức truy hồi sau:

1. $T(n) = 2T(n/2) + O(n)$ (Thuật toán Merge Sort)
2. $T(n) = 4T(n/2) + O(n)$
3. $T(n) = 3T(n/4) + O(n^2)$
4. $T(n) = 8T(n/2) + O(n^3)$

#### Lời giải gợi ý
Dạng chuẩn của định lý thợ: $T(n) = a T(n/b) + f(n)$ với $a \ge 1, b > 1$. Xét giá trị $c_{\text{crit}} = \log_b a$:
1. $a = 2, b = 2 \implies \log_2 2 = 1$. Ở đây $f(n) = \Theta(n) = \Theta(n^1)$. Rơi vào trường hợp 2 của Định lý thợ:
   $$T(n) = \Theta(n \log n)$$
2. $a = 4, b = 2 \implies \log_2 4 = 2$. Ở đây $f(n) = O(n^1)$. Vì $1 < 2$, rơi vào trường hợp 1:
   $$T(n) = \Theta(n^{\log_b a}) = \Theta(n^2)$$
3. $a = 3, b = 4 \implies \log_4 3 \approx 0.793$. Ở đây $f(n) = O(n^2)$. Vì $2 > 0.793$, rơi vào trường hợp 3:
   $$T(n) = \Theta(f(n)) = \Theta(n^2)$$
4. $a = 8, b = 2 \implies \log_2 8 = 3$. Ở đây $f(n) = \Theta(n^3)$. Trường hợp 2:
   $$T(n) = \Theta(n^3 \log n)$$

---

## Phần 2. Cây nhị phân tìm kiếm & Cây cân bằng AVL

### Bài 2.1: Chèn phần tử và phép quay trên cây AVL
Cây AVL là cây nhị phân tìm kiếm (BST) tự cân bằng sao cho tại mọi nút, độ chênh lệch chiều cao giữa cây con trái và cây con phải (hệ số cân bằng $\text{BalanceFactor} = h_{\text{left}} - h_{\text{right}}$) luôn thuộc tập $\{-1, 0, 1\}$.

Cho cây AVL rỗng. Lần lượt chèn các khóa sau vào cây:
$$10, 20, 30, 40, 50, 25$$

1. Vẽ hoặc mô tả cây sau khi chèn 3 phần tử đầu tiên $10, 20, 30$. Chỉ rõ loại phép quay (Rotation) cần thực hiện.
2. Vẽ cây sau khi chèn tiếp $40, 50$ và chỉ rõ phép quay tương ứng.
3. Chèn phần tử $25$, chỉ rõ vị trí mất cân bằng và loại phép quay kép (Double Rotation) được kích hoạt.

#### Lời giải gợi ý
1. Chèn $10 \to 20 \to 30$:
   - Tạo thành chuỗi lệch phải (Right-Right): Nút $10$ có độ cao cây con phải là $2$, cây con trái là $0 \implies BF(10) = -2$.
   - Thực hiện **Phép quay đơn sang trái (Left Rotation)** tại nút $10$:
     - Nút $20$ trở thành gốc mới.
     - Con trái của $20$ là $10$, con phải là $30$. Cây cân bằng hoàn hảo ($h = 2$).

2. Chèn tiếp $40, 50$:
   - Chèn $40$: Vào con phải của $30$. Cây vẫn cân bằng ($BF(20) = -1$).
   - Chèn $50$: Vào con phải của $40$. Tại nút $30$, nhánh phải có độ cao 2, nhánh trái độ cao 0 $\implies BF(30) = -2$ (dạng Right-Right).
   - Thực hiện **Phép quay đơn sang trái (Left Rotation)** tại nút $30$:
     - Nút $40$ lên làm con phải của $20$.
     - Con trái của $40$ là $30$, con phải là $50$. Cây cân bằng.

3. Chèn tiếp $25$:
   - $25 > 20 \implies$ đi sang phải. $25 < 40 \implies$ đi sang trái. $25 < 30 \implies$ làm con trái của $30$.
   - Kiểm tra hệ số cân bằng từ dưới lên:
     $BF(30) = 1$ (cân bằng).
     $BF(40) = h_{\text{left}}(30) - h_{\text{right}}(50) = 2 - 1 = 1$ (cân bằng).
     Tại nút gốc $20$: Nhánh trái (chứa $10$) có $h = 1$. Nhánh phải (chứa $40$) có $h = 3 \implies BF(20) = 1 - 3 = -2$ (mất cân bằng).
     Tại nút con phải $40$, $BF(40) = 1 > 0 \implies$ dạng **Right-Left (RL)**.
   - Kích hoạt **Phép quay kép Right-Left**:
     - Bước 1: Quay phải tại $40$. Nút $30$ lên thay $40$, $40$ trở thành con phải của $30$.
     - Bước 2: Quay trái tại gốc $20$. Nút $30$ trở thành gốc mới của toàn cây!
     - Cây cân bằng hoàn toàn sau thao tác: Gốc là $30$, cây con trái có gốc $20$ (với con $10, 25$), cây con phải có gốc $40$ (với con $50$).

---

## Phần 3. Bảng băm & Xử lý xung đột (Hashing)

### Bài 3.1: Dò tuyến tính (Linear Probing) và Băm kép (Double Hashing)
Cho bảng băm có kích thước $M = 7$ với các vị trí đánh số từ $0$ đến $6$. Hàm băm chính là $h_1(k) = k \pmod 7$.

Lần lượt chèn các khóa sau vào bảng băm:
$$12, 26, 19, 33, 40$$

1. Sử dụng phương pháp **Dò tuyến tính (Linear Probing)** với hàm kiểm tra vị trí:
   $$h(k, i) = (h_1(k) + i) \pmod 7, \quad i = 0, 1, 2, \dots$$
   Xác định vị trí cuối cùng của từng khóa trong bảng băm và tính số lần xung đột (collisions).
2. Sử dụng phương pháp **Băm kép (Double Hashing)** với hàm băm thứ hai $h_2(k) = 1 + (k \pmod 5)$ và hàm vị trí:
   $$h(k, i) = (h_1(k) + i \cdot h_2(k)) \pmod 7, \quad i = 0, 1, 2, \dots$$
   Xác định vị trí cuối cùng của các khóa và so sánh hiện tượng dồn cụm (clustering).

#### Lời giải gợi ý
1. Dò tuyến tính:
   - Khóa $12$: $12 \pmod 7 = 5 \implies$ ô 5 (trống).
   - Khóa $26$: $26 \pmod 7 = 5 \implies$ xung đột ô 5! Thử $i=1$: $(5+1)\%7 = 6 \implies$ ô 6 (trống). (1 xung đột)
   - Khóa $19$: $19 \pmod 7 = 5 \implies$ xung đột ô 5, thử ô 6 (xung đột), thử ô 0: $(5+2)\%7 = 0 \implies$ ô 0 (trống). (2 xung đột)
   - Khóa $33$: $33 \pmod 7 = 5 \implies$ xung đột 5, 6, 0. Thử ô 1: $(5+3)\%7 = 1 \implies$ ô 1 (trống). (3 xung đột)
   - Khóa $40$: $40 \pmod 7 = 5 \implies$ xung đột 5, 6, 0, 1. Thử ô 2: $(5+4)\%7 = 2 \implies$ ô 2 (trống). (4 xung đột)
   - Bảng cuối cùng:
     - Ô 0: 19
     - Ô 1: 33
     - Ô 2: 40
     - Ô 3: Trống
     - Ô 4: Trống
     - Ô 5: 12
     - Ô 6: 26

2. Băm kép giúp bước nhảy phụ thuộc vào giá trị của khóa, phân tán đều các khóa bị trùng giá trị băm đầu tiên và triệt tiêu hoàn toàn hiện tượng dồn cụm cấp 1 (Primary Clustering).

---

## Phần 4. Giải thuật đồ thị (Graph Algorithms)

### Bài 4.1: Thuật toán Dijkstra tìm đường đi ngắn nhất
Cho đồ thị có trọng số không âm với các đỉnh $\{A, B, C, D, E\}$ và các cạnh có hướng:
- $(A, B, 4), (A, C, 2)$
- $(B, C, 1), (B, D, 5)$
- $(C, B, 1), (C, D, 8), (C, E, 10)$
- $(D, E, 2)$
- $(E, D, 1)$

1. Áp dụng thuật toán Dijkstra để tìm khoảng cách ngắn nhất từ đỉnh nguồn $A$ đến tất cả các đỉnh còn lại.
2. Lập bảng theo dõi khoảng cách tạm thời $d[\cdot]$ và tập đỉnh đã cố định khoảng cách qua từng bước lặp.
3. Rút ra cây đường đi ngắn nhất (Shortest Path Tree) xuất phát từ $A$.

#### Lời giải gợi ý
- Khởi tạo: $d[A] = 0; d[B] = d[C] = d[D] = d[E] = \infty$. Tập đỉnh đã chốt $S = \emptyset$.
- Bước 1: Chọn $A$ ($d[A] = 0$). Chốt $A \implies S = \{A\}$.
  Cập nhật lân cận của $A$:
  - $d[B] = \min(\infty, 0 + 4) = 4$
  - $d[C] = \min(\infty, 0 + 2) = 2$
- Bước 2: Trong các đỉnh chưa chốt $\{B(4), C(2), D(\infty), E(\infty)\}$, đỉnh nhỏ nhất là $C$ ($d[C] = 2$). Chốt $C \implies S = \{A, C\}$.
  Cập nhật lân cận của $C$:
  - $d[B] = \min(4, 2 + 1) = 3$ (rút ngắn được qua $C$!)
  - $d[D] = \min(\infty, 2 + 8) = 10$
  - $d[E] = \min(\infty, 2 + 10) = 12$
- Bước 3: Trong các đỉnh chưa chốt $\{B(3), D(10), E(12)\}$, nhỏ nhất là $B$ ($d[B] = 3$). Chốt $B \implies S = \{A, C, B\}$.
  Cập nhật lân cận của $B$:
  - $d[D] = \min(10, 3 + 5) = 8$ (rút ngắn qua $B$!)
- Bước 4: Trong các đỉnh chưa chốt $\{D(8), E(12)\}$, nhỏ nhất là $D$ ($d[D] = 8$). Chốt $D \implies S = \{A, C, B, D\}$.
  Cập nhật lân cận của $D$:
  - $d[E] = \min(12, 8 + 2) = 10$ (rút ngắn qua $D$!)
- Bước 5: Chốt đỉnh cuối cùng $E$ ($d[E] = 10$).
- Kết quả khoảng cách ngắn nhất:
  - $d[A] = 0$
  - $d[B] = 3$ (đường đi: $A \to C \to B$)
  - $d[C] = 2$ (đường đi: $A \to C$)
  - $d[D] = 8$ (đường đi: $A \to C \to B \to D$)
  - $d[E] = 10$ (đường đi: $A \to C \to B \to D \to E$)
