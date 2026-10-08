---
course: discrete-math
lecture: graph-theory
section: lecture
title: "Lý thuyết đồ thị cơ bản"
prerequisites: ["do-thi","cay"]
lessonStatus: ready
---


Lý thuyết đồ thị xuất phát từ bài toán kinh điển 7 cây cầu Königsberg của Euler năm 1736: *Liệu có thể đi qua tất cả 7 cây cầu đúng 1 lần rồi quay về điểm xuất phát?*

---

## Minh họa tương tác

<CodeIllustration type="search" />

## 1. Định lý Bắt Tay (Handshaking Theorem)

Trong một đơn đồ thị vô hướng hữu hạn $G=(V,E)$, gọi các đỉnh là $V=\{v_1,\ldots,v_n\}$. Bậc $\deg(v)$ là số cạnh kề với đỉnh $v$. Cộng bậc của từng đỉnh:

$$
\deg(v_1)+\cdots+\deg(v_n)
=\sum_{v\in V}\deg(v)=2|E|.
$$

Dưới dấu tổng, $v\in V$ yêu cầu đi qua tất cả đỉnh của đồ thị. $|E|$ là số cạnh. Mỗi cạnh có hai đầu nên được đếm hai lần. Ví dụ đường đi ba đỉnh $v_1-v_2-v_3$ có các bậc 1, 2, 1: tổng bậc $1+2+1=4$ bằng hai lần số cạnh $2\cdot2$.

::: tip Hệ quả Quan trọng Thường Ra Trắc Nghiệm
Tổng bậc của tất cả các đỉnh luôn là một **SỐ CHẴN**. Do đó, số đỉnh có **bậc lẻ** trong bất kỳ đồ thị nào cũng phải là một **SỐ CHẴN**.
:::

---

## 2. Đồ thị Euler vs Đồ thị Hamilton

| Khái niệm | Định nghĩa | Điều kiện tồn tại (Đồ thị vô hướng liên thông) |
| :--- | :--- | :--- |
| **Đường đi Euler** | Đi qua mọi **CẠNH** đúng 1 lần | Có đúng **0 hoặc 2 đỉnh bậc lẻ** |
| **Chu trình Euler** | Đi qua mọi **CẠNH** đúng 1 lần & khép kín | **Tất cả các đỉnh đều có bậc chẵn** |
| **Đường đi Hamilton** | Đi qua mọi **ĐỈNH** đúng 1 lần | Bài toán NP-đầy đủ (không có điều kiện cần và đủ đơn giản) |
| **Chu trình Hamilton** | Đi qua mọi **ĐỈNH** đúng 1 lần & khép kín | Điều kiện đủ: Định lý Dirac ($\text{deg}(v) \ge \frac{n}{2}$), Định lý Ore |

---

## 3. Công thức Euler cho Đồ thị Phẳng

Nếu một đồ thị liên thông phẳng được vẽ trên mặt phẳng mà không có cạnh nào cắt nhau:
$$V - E + F = 2$$
*(Trong đó: $V$ là số đỉnh, $E$ là số cạnh, $F$ là số miền mặt phẳng bao gồm cả miền vô hạn bên ngoài).*
