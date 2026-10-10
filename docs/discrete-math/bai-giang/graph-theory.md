---
course: discrete-math
lecture: graph-theory
section: lecture
title: "Lý thuyết đồ thị cơ bản"
prerequisites: ["do-thi","cay"]
lessonStatus: ready
description: "Khái niệm đồ thị vô hướng, có hướng, định lý bắt tay, đồ thị Euler, đồ thị Hamilton và công thức Euler cho đồ thị phẳng."
---

Lý thuyết đồ thị xuất phát từ bài toán kinh điển 7 cây cầu Königsberg của Leonhard Euler năm 1736: *Liệu có thể đi qua tất cả 7 cây cầu đúng 1 lần rồi quay về điểm xuất phát?* Lời giải phủ định của Euler đã khai sinh ra một phân ngành toán học hiện đại, là trái tim của các thuật toán mạng máy tính, định tuyến giao thông và mạng xã hội.

---

## Minh họa tương tác

<CodeIllustration type="search" />

---

## 1. Định lý bắt tay (Handshaking Theorem)

Trong một đơn đồ thị vô hướng hữu hạn $G=(V,E)$, gọi các đỉnh là $V=\{v_1,\ldots,v_n\}$. Bậc $\deg(v)$ là số cạnh kề với đỉnh $v$. Khi cộng bậc của toàn bộ các đỉnh trong đồ thị:

$$
\begin{aligned}
\sum_{v\in V}\deg(v) &= \deg(v_1) + \deg(v_2) + \dots + \deg(v_n) \\
&= 2|E|.
\end{aligned}
$$

Mỗi cạnh nối giữa hai đỉnh nên khi tính tổng bậc, mỗi cạnh được tính đúng hai lần tại hai đầu mút của nó.

::: tip Hệ quả quan trọng
Tổng bậc của tất cả các đỉnh trong một đồ thị vô hướng luôn là một **SỐ CHẴN**. Do đó, số lượng đỉnh có **bậc lẻ** trong bất kỳ đồ thị nào cũng bắt buộc phải là một **SỐ CHẴN**.
:::

---

## 2. Đồ thị Euler vs Đồ thị Hamilton

| Khái niệm | Định nghĩa đường đi & chu trình | Điều kiện tồn tại (Đồ thị vô hướng liên thông) |
| :--- | :--- | :--- |
| **Đường đi Euler** | Đi qua mọi **CẠNH** đúng một lần | Có đúng **0 hoặc 2 đỉnh bậc lẻ** |
| **Chu trình Euler** | Đi qua mọi **CẠNH** đúng một lần và khép kín | **Tất cả các đỉnh đều có bậc chẵn** |
| **Đường đi Hamilton** | Đi qua mọi **ĐỈNH** đúng một lần | Bài toán NP-đầy đủ (không có tiêu chuẩn cần và đủ đơn giản) |
| **Chu trình Hamilton** | Đi qua mọi **ĐỈNH** đúng một lần và khép kín | Điều kiện đủ: Định lý Dirac ($\text{deg}(v) \ge \frac{n}{2}$ với $n \ge 3$), Định lý Ore |

---

## 3. Công thức Euler cho đồ thị phẳng

Nếu một đồ thị liên thông phẳng được vẽ trên mặt phẳng sao cho không có hai cạnh nào cắt nhau ngoài các đỉnh:

$$
V - E + F = 2
$$

Trong đó $V$ là số đỉnh, $E$ là số cạnh, và $F$ là số miền mặt phẳng (bao gồm cả miền không bị chặn ở vô hạn phía ngoài).

---

## 4. Hệ thống bài tập tự luyện {#bai-tap}

### Bài 1: Ứng dụng Định lý bắt tay kiểm tra tính khả thi của đồ thị

::: exercise Yêu cầu
1. Một đồ thị vô hướng có 15 đỉnh, trong đó mỗi đỉnh đều có đúng bậc 4. Hãy tính tổng số cạnh của đồ thị này.
2. Liệu có tồn tại một đồ thị đơn vô hướng gồm 9 đỉnh mà bậc của các đỉnh lần lượt là:
   $$3, 3, 3, 3, 5, 5, 5, 5, 5?$$
:::

::: solution
#### Lời giải chi tiết
1. Áp dụng trực tiếp định lý bắt tay:
   $$
   \sum_{v \in V} \deg(v) = 15 \times 4 = 60
   $$
   Vì $\sum_{v \in V} \deg(v) = 2|E|$, ta suy ra:
   $$
   |E| = \frac{60}{2} = 30 \text{ cạnh}.
   $$

2. Xét dãy bậc gồm 9 đỉnh: $3, 3, 3, 3, 5, 5, 5, 5, 5$.
   - Các đỉnh có bậc là $3$ và $5$ đều là các đỉnh có bậc lẻ.
   - Số lượng đỉnh có bậc lẻ ở đây là $4 + 5 = 9$ đỉnh.
   - Vì $9$ là một số lẻ, điều này vi phạm trực tiếp hệ quả của định lý bắt tay (số đỉnh bậc lẻ trong bất kỳ đồ thị nào cũng phải là một số chẵn).
   - *Kết luận:* Không thể tồn tại một đồ thị như vậy.
:::

---

### Bài 2: Nhận diện chu trình và đường đi Euler

::: exercise Yêu cầu
Cho đồ thị lưỡng phân đầy đủ $K_{m, n}$ (gồm hai tập đỉnh độc lập có kích thước $m$ và $n$, mọi đỉnh thuộc tập này đều nối với mọi đỉnh thuộc tập kia).
1. Hãy xác định bậc của từng đỉnh trong $K_{m, n}$.
2. Tìm điều kiện của $m$ và $n$ để $K_{m, n}$ có chu trình Euler.
3. Tìm điều kiện của $m$ và $n$ để $K_{m, n}$ có đường đi Euler nhưng không có chu trình Euler.
:::

::: solution
#### Lời giải chi tiết
1. Trong đồ thị lưỡng phân đầy đủ $K_{m, n}$:
   - Mỗi đỉnh thuộc tập thứ nhất (gồm $m$ đỉnh) đều nối với toàn bộ $n$ đỉnh của tập thứ hai, do đó có bậc là $n$.
   - Mỗi đỉnh thuộc tập thứ hai (gồm $n$ đỉnh) đều nối với toàn bộ $m$ đỉnh của tập thứ nhất, do đó có bậc là $m$.

2. **Điều kiện để có chu trình Euler:**
   Đồ thị liên thông có chu trình Euler khi và chỉ khi tất cả các đỉnh đều có bậc chẵn.
   Do đó, bậc của mọi đỉnh phải là số chẵn, tức là **cả $m$ và $n$ đều phải là các số nguyên dương chẵn**.

3. **Điều kiện để có đường đi Euler (không khép kín):**
   Đồ thị liên thông có đường đi Euler khi và chỉ khi có đúng hai đỉnh bậc lẻ (các đỉnh còn lại đều có bậc chẵn).
   - Nếu $m = 2$ và $n$ là số lẻ: Khi đó $n$ đỉnh có bậc 2 (chẵn) và $m = 2$ đỉnh có bậc $n$ (lẻ). Đồ thị có đúng 2 đỉnh bậc lẻ.
   - Tương tự, nếu $n = 2$ và $m$ là số lẻ: Đồ thị có đúng 2 đỉnh bậc lẻ.
   - *Kết luận:* Điều kiện là **($m = 2$ và $n$ lẻ) hoặc ($n = 2$ và $m$ lẻ)**.
:::

---

### Bài 3: Ứng dụng công thức Euler chứng minh đồ thị không phẳng

::: exercise Yêu cầu
Trong một đơn đồ thị phẳng liên thông với $V \ge 3$ đỉnh và $E$ cạnh, mỗi miền mặt phẳng được bao bởi ít nhất 3 cạnh ($2E \ge 3F$).
1. Từ công thức Euler $V - E + F = 2$, hãy chứng minh bất đẳng thức:
   $$E \le 3V - 6$$
2. Sử dụng bất đẳng thức trên để chứng minh đồ thị đầy đủ 5 đỉnh $K_5$ không thể là đồ thị phẳng.
:::

::: solution
#### Lời giải chi tiết
1. Chứng minh bất đẳng thức:
   - Từ công thức Euler: $F = E - V + 2$.
   - Vì mỗi miền được giới hạn bởi ít nhất 3 cạnh và mỗi cạnh chỉ là biên của tối đa 2 miền, ta có hệ thức:
     $$3F \le 2E$$
   - Thay $F = E - V + 2$ vào bất đẳng thức:
     $$
     \begin{aligned}
     3(E - V + 2) &\le 2E \\
     3E - 3V + 6 &\le 2E \\
     E &\le 3V - 6.
     \end{aligned}
     $$

2. Áp dụng cho đồ thị đầy đủ $K_5$:
   - Đồ thị $K_5$ có $V = 5$ đỉnh.
   - Số cạnh của $K_5$ là:
     $$
     E = \binom{5}{2} = \frac{5 \times 4}{2} = 10 \text{ cạnh}.
     $$
   - Nếu $K_5$ là đồ thị phẳng, số cạnh của nó phải thỏa mãn bất đẳng thức:
     $$
     E \le 3V - 6 \iff 10 \le 3(5) - 6 = 15 - 6 = 9 \quad (\text{Vô lý!})
     $$
   - Mâu thuẫn này chứng minh rằng **đồ thị $K_5$ không thể vẽ trên mặt phẳng mà không có cạnh cắt nhau** (không phải là đồ thị phẳng).
:::
