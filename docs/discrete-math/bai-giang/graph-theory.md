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

Toàn bộ hệ thống bài tập thực hành chuyên sâu của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu luyện tập.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở các bài tập thực chiến có hướng dẫn chi tiết và kiểm chứng tự động.
:::

