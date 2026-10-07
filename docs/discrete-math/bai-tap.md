---
title: Bài tập ôn luyện - Toán rời rạc
description: Tuyển tập bài tập logic hình thức, chứng minh quy nạp, quan hệ tương đương, giải tích tổ hợp và lý thuyết đồ thị.
---

# Bài tập ôn luyện: Toán rời rạc

Tài liệu cung cấp hệ thống bài tập cho môn Toán rời rạc, thiết kế theo chuẩn mực toán học cấu trúc cho khoa học máy tính: suy luận logic, ánh xạ - quan hệ, tổ hợp rời rạc và lý thuyết đồ thị.

---

## Phần 1. Logic mệnh đề & Phương pháp chứng minh quy nạp

### Bài 1.1: Chứng minh quy nạp toán học
1. Chứng minh bằng phương pháp quy nạp toán học rằng với mọi số nguyên dương $n \ge 1$:
   $$1^2 + 2^2 + 3^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}$$
2. Chứng minh rằng với mọi số nguyên dương $n \ge 1$, biểu thức $4^n - 1$ luôn chia hết cho $3$.

#### Lời giải gợi ý
1. Chứng minh công thức tổng bình phương:
   - **Bước cơ sở ($n = 1$):**
     Vế trái: $1^2 = 1$.
     Vế phải: $\frac{1(1+1)(2(1)+1)}{6} = \frac{1 \cdot 2 \cdot 3}{6} = 1$.
     Đẳng thức đúng với $n = 1$.
   - **Bước quy nạp:**
     Giả sử mệnh đề đúng với số nguyên dương $k \ge 1$, tức là:
     $$1^2 + 2^2 + \dots + k^2 = \frac{k(k+1)(2k+1)}{6}$$
     Ta cần chứng minh mệnh đề đúng với $n = k + 1$, tức là:
     $$1^2 + 2^2 + \dots + k^2 + (k+1)^2 = \frac{(k+1)((k+1)+1)(2(k+1)+1)}{6} = \frac{(k+1)(k+2)(2k+3)}{6}$$
     Thật vậy:
     $$\text{VT} = \frac{k(k+1)(2k+1)}{6} + (k+1)^2 = (k+1) \left[ \frac{k(2k+1) + 6(k+1)}{6} \right]$$
     $$= (k+1) \left[ \frac{2k^2 + 7k + 6}{6} \right] = \frac{(k+1)(k+2)(2k+3)}{6} = \text{VP}$$
     Theo nguyên lý quy nạp toán học, đẳng thức đúng với mọi $n \ge 1$.

2. Chứng minh $4^n - 1$ chia hết cho 3:
   - Với $n = 1$: $4^1 - 1 = 3$ chia hết cho 3.
   - Giả sử đúng với $n = k$: $4^k - 1 = 3m$ ($m \in \mathbb{Z}$).
   - Với $n = k + 1$:
     $$4^{k+1} - 1 = 4 \cdot 4^k - 1 = 4(3m + 1) - 1 = 12m + 4 - 1 = 12m + 3 = 3(4m + 1)$$
     chia hết cho 3. Điều phải chứng minh.

---

## Phần 2. Quan hệ & Cấu trúc thứ tự (Relations & POSet)

### Bài 2.1: Quan hệ tương đương và Lớp tương đương
Xét tập hợp các số nguyên $\mathbb{Z}$. Định nghĩa quan hệ hai ngôi $R$ trên $\mathbb{Z}$ như sau:
$$a \, R \, b \iff a \equiv b \pmod 5 \quad (a - b \text{ chia hết cho } 5)$$

1. Chứng minh rằng $R$ là một quan hệ tương đương (thỏa mãn 3 tính chất: phản xạ, đối xứng và bắc cầu).
2. Xác định các lớp tương đương rời nhau phân hoạch tập $\mathbb{Z}$. Chỉ ra các phần tử tiêu biểu.

#### Lời giải gợi ý
1. Chứng minh 3 tính chất:
   - **Phản xạ (Reflexive):** Với mọi $a \in \mathbb{Z}$, $a - a = 0 = 5 \cdot 0 \implies a - a$ chia hết cho $5 \implies a \, R \, a$.
   - **Đối xứng (Symmetric):** Giả sử $a \, R \, b \implies a - b = 5k$ ($k \in \mathbb{Z}$). Khi đó $b - a = -(a - b) = 5(-k)$. Vì $-k \in \mathbb{Z}$, $b - a$ chia hết cho $5 \implies b \, R \, a$.
   - **Bắc cầu (Transitive):** Giả sử $a \, R \, b$ và $b \, R \, c$. Khi đó $a - b = 5k$ và $b - c = 5m$. Cộng hai đẳng thức: $(a - b) + (b - c) = a - c = 5(k + m)$. Vì $k + m \in \mathbb{Z}$, $a - c$ chia hết cho $5 \implies a \, R \, c$.
   Vậy $R$ là một quan hệ tương đương.

2. Các lớp tương đương chính là các lớp đồng dư modulo 5:
   $$[0] = \{\dots, -10, -5, 0, 5, 10, \dots\} = \{5k \mid k \in \mathbb{Z}\}$$
   $$[1] = \{\dots, -9, -4, 1, 6, 11, \dots\} = \{5k + 1 \mid k \in \mathbb{Z}\}$$
   $$[2] = \{\dots, -8, -3, 2, 7, 12, \dots\} = \{5k + 2 \mid k \in \mathbb{Z}\}$$
   $$[3] = \{\dots, -7, -2, 3, 8, 13, \dots\} = \{5k + 3 \mid k \in \mathbb{Z}\}$$
   $$[4] = \{\dots, -6, -1, 4, 9, 14, \dots\} = \{5k + 4 \mid k \in \mathbb{Z}\}$$
   Tập thương $\mathbb{Z}/R = \{[0], [1], [2], [3], [4]\}$.

---

## Phần 3. Giải tích tổ hợp & Hệ thức truy hồi (Combinatorics)

### Bài 3.1: Giải hệ thức truy hồi tuyến tính thuần nhất
Cho dãy số $(a_n)$ thỏa mãn hệ thức truy hồi tuyến tính cấp 2:
$$a_n = 5a_{n-1} - 6a_{n-2} \quad \text{với mọi } n \ge 2$$
với các điều kiện đầu: $a_0 = 1, a_1 = 4$.

1. Viết phương trình đặc trưng của hệ thức truy hồi.
2. Tìm các nghiệm đặc trưng $r_1, r_2$.
3. Xác định nghiệm tổng quát và sử dụng điều kiện đầu để tìm công thức tường minh của số hạng tổng quát $a_n$.

#### Lời giải gợi ý
1. Phương trình đặc trưng:
   $$r^2 - 5r + 6 = 0$$

2. Giải phương trình:
   $$(r - 2)(r - 3) = 0 \implies r_1 = 2, \quad r_2 = 3$$

3. Nghiệm tổng quát có dạng:
   $$a_n = C_1 \cdot 2^n + C_2 \cdot 3^n$$
   Thay điều kiện đầu:
   - Với $n = 0$: $a_0 = C_1 + C_2 = 1 \implies C_2 = 1 - C_1$.
   - Với $n = 1$: $a_1 = 2C_1 + 3C_2 = 4$.
   Thay $C_2$ vào:
   $$2C_1 + 3(1 - C_1) = 4 \iff 3 - C_1 = 4 \implies C_1 = -1$$
   Suy ra $C_2 = 1 - (-1) = 2$.
   Vậy công thức tường minh của dãy số:
   $$a_n = 2 \cdot 3^n - 2^n$$

---

## Phần 4. Lý thuyết đồ thị & Cây (Graph Theory)

### Bài 4.1: Bổ đề bắt tay và tính phẳng của đồ thị
1. Phát biểu Bổ đề bắt tay (Handshaking Lemma) và chứng minh rằng trong mọi đồ thị vô hướng, số đỉnh có bậc lẻ luôn là một số chẵn.
2. Cho đồ thị phẳng liên thông $G$ có $V = 6$ đỉnh và phân chia mặt phẳng thành $F = 8$ miền (mặt). Hỏi đồ thị $G$ có bao nhiêu cạnh $E$?
3. Chứng minh đồ thị lưỡng phân đầy đủ $K_{3,3}$ không phải là đồ thị phẳng.

#### Lời giải gợi ý
1. Bổ đề bắt tay: Trong đồ thị vô hướng $G = (V, E)$, tổng bậc của tất cả các đỉnh bằng hai lần số cạnh:
   $$\sum_{v \in V} \deg(v) = 2|E|$$
   Vì $2|E|$ luôn là số chẵn, nên tổng bậc của các đỉnh có bậc lẻ phải là một số chẵn. Điều này chỉ xảy ra khi số lượng các đỉnh có bậc lẻ là một số chẵn.

2. Áp dụng công thức Euler cho đồ thị phẳng liên thông:
   $$V - E + F = 2 \iff 6 - E + 8 = 2 \iff 14 - E = 2 \implies E = 12$$

3. Trong đồ thị lưỡng phân, không có chu trình độ dài 3 (mọi chu trình đều có độ dài chẵn $\ge 4$). Do đó mỗi miền được bao bởi ít nhất 4 cạnh: $2E \ge 4F \implies F \le E/2$.
   Theo công thức Euler: $V - E + F = 2 \implies 2 = V - E + F \le V - E + E/2 = V - E/2$.
   Suy ra $E \le 2V - 4$.
   Với $K_{3,3}$, ta có $V = 6, E = 3 \times 3 = 9$.
   Thế vào bất đẳng thức: $9 \le 2(6) - 4 = 8$ (Vô lý!).
   Vậy $K_{3,3}$ không thể là đồ thị phẳng (theo định lý Kuratowski).
