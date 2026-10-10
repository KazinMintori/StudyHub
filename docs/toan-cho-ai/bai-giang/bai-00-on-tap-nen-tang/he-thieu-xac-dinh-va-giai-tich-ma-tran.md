---
course: toan-cho-ai
lecture: bai-00-on-tap-nen-tang
topic: he-thieu-xac-dinh-va-giai-tich-ma-tran
section: topic
title: "Hệ Tuyến Tính Thiếu Xác Định và Giải Tích Ma Trận"
description: "Phương pháp giải hệ phương trình thiếu xác định, nghiệm chuẩn nhỏ nhất, phân tích LQ, nghịch đảo giả Moore-Penrose, phần bù Schur và giải tích hàm ma trận trong tối ưu hóa học máy."
---

Trong học máy và khoa học dữ liệu hiện đại, ta thường xuyên đối mặt với các bài toán có số lượng tham số lớn hơn rất nhiều so với số lượng điểm dữ liệu quan sát ($n > m$). Khi đó, hệ phương trình điều kiện $Ax = b$ trở thành hệ **thiếu xác định** (Underdetermined Linear System). Hệ này sở hữu vô số nghiệm khả dĩ tạo thành một không gian afin. Thách thức đặt ra là: Trong vô số nghiệm đó, nghiệm nào mang cấu trúc tối ưu về mặt hình học, có chuẩn nhỏ nhất, hoặc có tính thưa cao nhất?

Bên cạnh đó, để tối ưu hóa các mô hình xác suất và mạng nơ-ron, việc thao tác với các hàm ma trận (như hàm vết, định thức logarit, dạng toàn phương) đòi hỏi công cụ vi tích phân ma trận chuẩn xác. Bài học này hệ thống hóa toàn diện phương pháp giải hệ thiếu xác định và các bổ đề giải tích ma trận cốt lõi trong tối ưu hóa lồi.

---

## 1. Hệ Phương Trình Tuyến Tính Thiếu Xác Định

Xét hệ phương trình tuyến tính:

$$
A x = b,
$$

trong đó $A \in \mathbb{R}^{m \times n}$ là ma trận kích thước "béo" (fat matrix) với $m < n$, và ma trận có hạng hàng đủ $\operatorname{rank}(A) = m$. Vector vế phải $b \in \mathbb{R}^m$.

Vì $\operatorname{rank}(A) = m$, không gian cột của $A$ phủ kín toàn bộ không gian đích $\mathbb{R}^m$, do đó hệ luôn có nghiệm với mọi $b$. Không gian nghiệm của hệ là tập afin:

$$
\mathcal{S} = \{ x \in \mathbb{R}^n \mid A x = b \}.
$$

Nếu $x_0$ là một nghiệm riêng bất kỳ, thì toàn bộ tập nghiệm có dạng:

$$
\mathcal{S} = x_0 + \ker(A) = \{ x_0 + z \mid z \in \mathbb{R}^n, A z = 0 \}.
$$

Vì số chiều của không gian hạt nhân $\dim(\ker(A)) = n - m > 0$, hệ có vô số nghiệm.

---

## 2. Nghiệm Chuẩn $L_2$ Nhỏ Nhất (Least-Norm Solution)

Trong số vô vàn nghiệm của $\mathcal{S}$, nghiệm tự nhiên nhất là nghiệm nằm gần gốc tọa độ nhất theo chuẩn Euclid:

$$
\begin{aligned}
\min_{x} \quad & \frac{1}{2} \|x\|_2^2 \\
\text{s.t.} \quad & A x = b.
\end{aligned}
$$

Đây là bài toán quy hoạch toàn phương lồi nghiêm ngặt có ràng buộc đẳng thức.

### Thiết lập hàm Lagrange và nghiệm giải tích

Hàm Lagrange của bài toán với vector nhân tử $\nu \in \mathbb{R}^m$:

$$
L(x, \nu) = \frac{1}{2} x^T x + \nu^T (A x - b).
$$

Điều kiện tối ưu KKT bậc nhất:

$$
\begin{aligned}
\nabla_x L(x^*, \nu^*) &= x^* + A^T \nu^* = 0 \implies x^* = -A^T \nu^*, \\
\nabla_\nu L(x^*, \nu^*) &= A x^* - b = 0.
\end{aligned}
$$

Thế biểu thức $x^* = -A^T \nu^*$ vào ràng buộc đẳng thức:

$$
A (-A^T \nu^*) = b \implies (A A^T) (-\nu^*) = b.
$$

Vì ma trận $A$ có hạng hàng đủ $\operatorname{rank}(A) = m$, ma trận Gram $A A^T \in \mathbb{R}^{m \times m}$ đối xứng và xác định dương nghiêm ngặt ($A A^T \succ 0$), do đó khả nghịch hoàn toàn. Ta suy ra:

$$
-\nu^* = (A A^T)^{-1} b.
$$

Thế ngược lại, ta thu được nghiệm chuẩn nhỏ nhất duy nhất $x_{\text{ln}}$ (Least-Norm):

$$
x_{\text{ln}} = A^T (A A^T)^{-1} b.
$$

### Trực giác hình học và Định lý Pythagoras

Từ công thức trên, ta thấy $x_{\text{ln}} \in \operatorname{range}(A^T)$. Mặt khác, theo định lý cơ bản của đại số tuyến tính, không gian $\mathbb{R}^n$ được phân rã trực giao thành:

$$
\mathbb{R}^n = \operatorname{range}(A^T) \oplus \ker(A).
$$

Nghiệm $x_{\text{ln}}$ chính là hình chiếu trực giao của gốc tọa độ lên đa diện afin $\mathcal{S}$. 

Với mọi nghiệm khả dĩ khác $x \in \mathcal{S}$, ta luôn có thể biểu diễn $x = x_{\text{ln}} + z$ với $z \in \ker(A)$. Khi đó, tích vô hướng giữa hai thành phần:

$$
x_{\text{ln}}^T z = \left( A^T (A A^T)^{-1} b \right)^T z = b^T (A A^T)^{-1} (A z) = 0,
$$

bởi vì $A z = 0$. Theo định lý Pythagoras:

$$
\|x\|_2^2 = \|x_{\text{ln}} + z\|_2^2 = \|x_{\text{ln}}\|_2^2 + \|z\|_2^2 \ge \|x_{\text{ln}}\|_2^2.
$$

Đẳng thức xảy ra khi và chỉ khi $z = 0$, khẳng định tính duy nhất và tính tối tiểu của $x_{\text{ln}}$.

---

## 3. Thuật Toán Số Học Hiệu Năng Cao Qua Phân Tích $LQ$

Việc tính toán trực tiếp ma trận tích $A A^T$ rồi đảo ma trận $(A A^T)^{-1}$ rất dễ gặp mất ổn định số học khi ma trận có điều kiện xấu, đồng thời làm tăng bình phương số điều kiện: $\kappa(A A^T) = (\kappa(A))^2$.

Trong thực tế, ta sử dụng **phân tích $LQ$** của ma trận $A$ (tương đương với phân tích $QR$ của ma trận chuyển vị $A^T$).

### Thuật toán phân tích $LQ$

Phân tích ma trận $A \in \mathbb{R}^{m \times n}$ thành:

$$
A = L Q = \begin{bmatrix} L_1 & 0 \end{bmatrix} \begin{bmatrix} Q_1^T \\ Q_2^T \end{bmatrix} = L_1 Q_1^T,
$$

trong đó:
- $L_1 \in \mathbb{R}^{m \times m}$ là ma trận tam giác dưới khả nghịch với các phần tử đường chéo khác không.
- $Q_1 \in \mathbb{R}^{n \times m}$ có các cột trực chuẩn: $Q_1^T Q_1 = I_m$.
- $Q_2 \in \mathbb{R}^{n \times (n - m)}$ có các cột tạo thành cơ sở trực chuẩn cho $\ker(A)$.

### Quy trình giải 3 bước ổn định số học

Thế phân tích $A = L_1 Q_1^T$ vào công thức nghiệm chuẩn nhỏ nhất:

$$
\begin{aligned}
x_{\text{ln}} &= A^T (A A^T)^{-1} b \\
&= (Q_1 L_1^T) \left( (L_1 Q_1^T)(Q_1 L_1^T) \right)^{-1} b \\
&= Q_1 L_1^T (L_1 L_1^T)^{-1} b \\
&= Q_1 L_1^T (L_1^T)^{-1} L_1^{-1} b \\
&= Q_1 L_1^{-1} b.
\end{aligned}
$$

Thuật toán gồm ba bước:

1. **Phân tích $LQ$**: Thực hiện phân tích $A = L_1 Q_1^T$ với chi phí $O(m^2 n)$.
2. **Giải thế tiến (Forward substitution)**: Giải hệ tam giác dưới $L_1 y = b$ để tìm vector trung gian $y \in \mathbb{R}^m$ với chi phí $O(m^2)$.
3. **Phép nhân ma trận**: Tính nghiệm $x_{\text{ln}} = Q_1 y$ với chi phí $O(m n)$.

Quy trình này hoàn toàn không cần nghịch đảo ma trận, đảm bảo độ chính xác số học cao nhất.

---

## 4. Nghiệm Chuẩn $L_1$ Nhỏ Nhất và Tính Thưa (Sparse Recovery)

Nếu ta thay chuẩn $L_2$ bằng chuẩn $L_1$, bài toán tìm nghiệm trở thành:

$$
\begin{aligned}
\min_{x} \quad & \|x\|_1 = \sum_{j=1}^n |x_j| \\
\text{s.t.} \quad & A x = b.
\end{aligned}
$$

Bài toán này được gọi là **Basis Pursuit** trong lĩnh vực Nén cảm biến (Compressed Sensing).

### Đưa về Quy hoạch Tuyến tính (LP)

Ta phân rã mỗi biến $x_j$ thành hiệu của hai biến không âm: Biểu thức $x_j = u_j - v_j$ với $u_j \ge 0, v_j \ge 0$. Khi đó $|x_j| = u_j + v_j$, và bài toán trở thành LP dạng chuẩn:

$$
\begin{aligned}
\min_{u, v} \quad & \mathbf{1}^T u + \mathbf{1}^T v \\
\text{s.t.} \quad & A u - A v = b, \\
& u \ge 0, \quad v \ge 0.
\end{aligned}
$$

Khác với nghiệm $L_2$ thường làm dàn đều các trọng số ra toàn bộ các tọa độ, nghiệm chuẩn $L_1$ có xu hướng ép rất nhiều tọa độ về đúng giá trị 0, tạo ra một nghiệm **thưa** (Sparse solution). Đây là nền tảng toán học của việc phục hồi tín hiệu kích thước lớn chỉ từ một số lượng nhỏ các phép đo cảm biến.

---

## 5. Bổ Trợ Giải Tích Ma Trận Cốt Lõi

### Nghịch đảo giả Moore-Penrose ($A^+$)

Nghịch đảo giả Moore-Penrose $A^+ \in \mathbb{R}^{n \times m}$ của một ma trận $A \in \mathbb{R}^{m \times n}$ là ma trận duy nhất thỏa mãn bốn điều kiện Penrose:

1. $A A^+ A = A$.
2. $A^+ A A^+ = A^+$.
3. $(A A^+)^T = A A^+$.
4. $(A^+ A)^T = A^+ A$.

Các trường hợp đặc biệt quan trọng:

- Khi $\operatorname{rank}(A) = m < n$ (hạng hàng đủ, hệ thiếu xác định):
  $$
  A^+ = A^T (A A^T)^{-1}.
  $$
  Khi đó $A A^+ = I_m$, và nghiệm chuẩn nhỏ nhất viết gọn là $x_{\text{ln}} = A^+ b$.
- Khi $\operatorname{rank}(A) = n < m$ (hạng cột đủ, hệ thừa xác định / bình phương tối thiểu):
  $$
  A^+ = (A^T A)^{-1} A^T.
  $$
- Qua phân tích SVD $A = U \Sigma V^T$:
  $$
  A^+ = V \Sigma^+ U^T,
  $$
  trong đó $\Sigma^+$ thu được bằng cách nghịch đảo các giá trị kỳ dị khác không và giữ nguyên các giá trị bằng không.

### Bổ đề Nghịch Đảo Ma Trận Woodbury (Sherman-Morrison-Woodbury)

Khi cần cập nhật nghịch đảo của một ma trận sau khi bị biến đổi bởi một số hạng hạng thấp (Low-rank perturbation), công thức Woodbury là công cụ thiết yếu:

$$
(A + U C V)^{-1} = A^{-1} - A^{-1} U (C^{-1} + V A^{-1} U)^{-1} V A^{-1},
$$

trong đó $A \in \mathbb{R}^{n \times n}$, $C \in \mathbb{R}^{k \times k}$, $U \in \mathbb{R}^{n \times k}$, $V \in \mathbb{R}^{k \times n}$.

Trường hợp riêng cập nhật hạng 1 ($k = 1$, $U = u, V = v^T, C = 1$) là **công thức Sherman-Morrison**:

$$
(A + u v^T)^{-1} = A^{-1} - \frac{A^{-1} u v^T A^{-1}}{1 + v^T A^{-1} u}.
$$

Công thức này giảm chi phí tính toán cập nhật từ $O(n^3)$ xuống chỉ còn $O(n^2)$, đóng vai trò then chốt trong thuật toán lọc Kalman và hồi quy trực tuyến.

### Vi phân Các Hàm Ma Trận Tiêu Biểu

Bảng dưới đây tổng hợp đạo hàm và gradient của các hàm số ma trận phổ biến trong tối ưu hóa:

| Hàm số $f(X)$ | Miền xác định | Gradient $\nabla_X f(X)$ |
| :--- | :--- | :--- |
| $\operatorname{tr}(A X B)$ | $X \in \mathbb{R}^{m \times n}$ | $A^T B^T$ |
| $\operatorname{tr}(X^T A X)$ | $X \in \mathbb{R}^{n \times p}$ | $(A + A^T) X$ |
| $\frac{1}{2} x^T X x$ | $X \in \mathbb{S}^n$ | $\frac{1}{2} x x^T$ |
| $\log\det(X)$ | $X \in \mathbb{S}_{++}^n$ | $X^{-1}$ |
| $\operatorname{tr}(X^{-1})$ | $X \in \mathbb{S}_{++}^n$ | $-X^{-2}$ |

---

## 6. Bài Tập Tự Luyện Kèm Lời Giải Chi Tiết

### Bài tập 1: Tính Nghiệm Chuẩn Nhỏ Nhất và Kiểm Tra Tính Trực Giao

Cho ma trận $A \in \mathbb{R}^{2 \times 3}$ và vector $b \in \mathbb{R}^2$:

$$
A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}, \quad b = \begin{bmatrix} 2 \\ 4 \end{bmatrix}.
$$

1. Tính ma trận Gram $A A^T$ và nghịch đảo của nó.
2. Xác định nghiệm chuẩn nhỏ nhất $x_{\text{ln}} = A^T (A A^T)^{-1} b$.
3. Tìm cơ sở của không gian hạt nhân $\ker(A)$ và kiểm tra tính trực giao $x_{\text{ln}} \perp \ker(A)$.

#### Lời giải chi tiết:

1. Tính ma trận tích $A A^T$:
   $$
   A A^T = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1+1+0 & 0+1+0 \\ 0+1+0 & 0+1+1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}.
   $$

   Định thức: $\det(A A^T) = 2 \times 2 - 1 \times 1 = 3 \ne 0$.
   
   Nghịch đảo của ma trận $2 \times 2$:
   $$
   (A A^T)^{-1} = \frac{1}{3} \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}.
   $$

2. Tính vector trung gian $w = (A A^T)^{-1} b$:
   $$
   w = \frac{1}{3} \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} 2 \\ 4 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 4 - 4 \\ -2 + 8 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 0 \\ 6 \end{bmatrix} = \begin{bmatrix} 0 \\ 2 \end{bmatrix}.
   $$

   Nghiệm chuẩn nhỏ nhất:
   $$
   x_{\text{ln}} = A^T w = \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 2 \\ 2 \end{bmatrix}.
   $$

   Thử lại nghiệm:
   $$
   A x_{\text{ln}} = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} 0 \\ 2 \\ 2 \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \end{bmatrix} = b.
   $$

   Chuẩn bình phương: $\|x_{\text{ln}}\|_2^2 = 0^2 + 2^2 + 2^2 = 8$.

3. Tìm hạt nhân $\ker(A)$:
   $$
   A z = 0 \iff \begin{cases} z_1 + z_2 = 0 \\ z_2 + z_3 = 0 \end{cases} \iff z_1 = -z_2 = z_3.
   $$

   Chọn $z_2 = -1 \implies z_1 = 1, z_3 = 1$. Cơ sở của $\ker(A)$ là $v = (1, -1, 1)^T$.

   Kiểm tra tích vô hướng:
   $$
   x_{\text{ln}}^T v = 0(1) + 2(-1) + 2(1) = 0 - 2 + 2 = 0.
   $$

   Điều này khẳng định $x_{\text{ln}}$ vuông góc với toàn bộ không gian hạt nhân $\ker(A)$.

---

### Bài tập 2: Cập Nhật Nghịch Đảo Ma Trận Bằng Công Thức Sherman-Morrison

Trong mô hình hồi quy tuyến tính trực tuyến (Online Ridge Regression), ma trận hiệp phương sai mẫu được cập nhật sau khi nhận thêm một điểm dữ liệu mới $a \in \mathbb{R}^n$:

$$
V_{\text{new}} = V + a a^T,
$$

với $V \succ 0$ là ma trận khả nghịch đã biết trước nghịch đảo $V^{-1}$.

1. Áp dụng công thức Sherman-Morrison để biểu diễn $V_{\text{new}}^{-1}$ theo $V^{-1}$ và vector $a$.
2. Giả sử $V = I_2$ và điểm dữ liệu mới là $a = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$. Tính giá trị giải tích của $V_{\text{new}}^{-1}$.

#### Lời giải chi tiết:

1. Đặt $u = a$ và $v = a$. Áp dụng trực tiếp công thức Sherman-Morrison:
   $$
   V_{\text{new}}^{-1} = (V + a a^T)^{-1} = V^{-1} - \frac{V^{-1} a a^T V^{-1}}{1 + a^T V^{-1} a}.
   $$

   Đặt vector $q = V^{-1} a \in \mathbb{R}^n$ và số thực vô hướng $\gamma = 1 + a^T q = 1 + a^T V^{-1} a$. Biểu thức viết gọn:
   $$
   V_{\text{new}}^{-1} = V^{-1} - \frac{1}{\gamma} q q^T.
   $$

   Phép tính này chỉ đòi hỏi một phép nhân ma trận - vector ($V^{-1} a$) và một phép nhân ngoài vector ($q q^T$), tiêu tốn tổng cộng $O(n^2)$ phép tính thay vì $O(n^3)$ khi đảo ma trận từ đầu.

2. Áp dụng với dữ liệu cụ thể: $V = I_2 \implies V^{-1} = I_2$.
   
   Vector $q = I_2 a = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$.
   
   Đại lượng vô hướng $\gamma$:
   $$
   \gamma = 1 + a^T I_2 a = 1 + (1^2 + 2^2) = 1 + 5 = 6.
   $$

   Tích ngoài $q q^T$:
   $$
   q q^T = \begin{bmatrix} 1 \\ 2 \end{bmatrix} \begin{bmatrix} 1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}.
   $$

   Tính ma trận nghịch đảo mới:
   $$
   V_{\text{new}}^{-1} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} - \frac{1}{6} \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} = \begin{bmatrix} 1 - 1/6 & -2/6 \\ -2/6 & 1 - 4/6 \end{bmatrix} = \begin{bmatrix} 5/6 & -1/3 \\ -1/3 & 1/3 \end{bmatrix}.
   $$

   Kiểm tra lại bằng phép nhân trực tiếp:
   $$
   V_{\text{new}} = I_2 + a a^T = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} = \begin{bmatrix} 2 & 2 \\ 2 & 5 \end{bmatrix}.
   $$

   Tích của hai ma trận:
   $$
   \begin{bmatrix} 2 & 2 \\ 2 & 5 \end{bmatrix} \begin{bmatrix} 5/6 & -1/3 \\ -1/3 & 1/3 \end{bmatrix} = \begin{bmatrix} 10/6 - 2/3 & -2/3 + 2/3 \\ 10/6 - 5/3 & -2/3 + 5/3 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I_2.
   $$

---

### Bài tập 3: Tối Đa Hóa Entropy Ma Trận Hiệp Phương Sai (Maximum Entropy Covariance)

Xét bài toán ước lượng ma trận hiệp phương sai xác định dương $X \in \mathbb{S}_{++}^n$ tối đa hóa entropy thông tin chuẩn tắc Gauss có ràng buộc về vết:

$$
\begin{aligned}
\max_{X} \quad & \log\det(X) \\
\text{s.t.} \quad & \operatorname{tr}(S X) = n, \quad X \succ 0,
\end{aligned}
$$

trong đó $S \in \mathbb{S}_{++}^n$ là ma trận đối xứng xác định dương đã cho trước.

1. Chuyển bài toán về dạng cực tiểu lồi chuẩn tắc và thiết lập hàm Lagrange.
2. Áp dụng công thức vi phân ma trận để tìm điều kiện KKT.
3. Tìm nghiệm tối ưu giải tích $X^*$.

#### Lời giải chi tiết:

1. Bài toán tương đương với:
   $$
   \begin{aligned}
   \min_{X} \quad & -\log\det(X) \\
   \text{s.t.} \quad & \operatorname{tr}(S X) - n = 0, \quad X \succ 0.
   \end{aligned}
   $$

   Vì hàm $-\log\det(X)$ lồi nghiêm ngặt trên nón đối xứng xác định dương $\mathbb{S}_{++}^n$ và ràng buộc là tuyến tính theo $X$, đây là bài toán tối ưu lồi nghiêm ngặt có nghiệm tối ưu duy nhất.

   Hàm Lagrange với nhân tử đối ngẫu vô hướng $\nu \in \mathbb{R}$:
   $$
   L(X, \nu) = -\log\det(X) + \nu (\operatorname{tr}(S X) - n).
   $$

2. Lấy vi phân của hàm Lagrange theo ma trận đối xứng $X$:
   - Ta đã biết $\nabla_X (-\log\det(X)) = -X^{-1}$.
   - Với số hạng tuyến tính: $\nabla_X \operatorname{tr}(S X) = S$ (do $S$ đối xứng).

   Điều kiện KKT triệt tiêu gradient ma trận:
   $$
   \nabla_X L(X^*, \nu^*) = -(X^*)^{-1} + \nu^* S = 0 \implies (X^*)^{-1} = \nu^* S.
   $$

   Nghịch đảo cả hai vế (với điều kiện $\nu^* > 0$):
   $$
   X^* = \frac{1}{\nu^*} S^{-1}.
   $$

3. Xác định nhân tử $\nu^*$ bằng cách thế $X^*$ vào ràng buộc đẳng thức $\operatorname{tr}(S X^*) = n$:
   $$
   \operatorname{tr}\left( S \left( \frac{1}{\nu^*} S^{-1} \right) \right) = n \implies \frac{1}{\nu^*} \operatorname{tr}(I_n) = n.
   $$

   Vì $\operatorname{tr}(I_n) = n$, ta có:
   $$
   \frac{n}{\nu^*} = n \implies \nu^* = 1.
   $$

   Thế $\nu^* = 1$ trở lại, ta tìm được ma trận nghiệm tối ưu duy nhất:
   $$
   X^* = S^{-1}.
   $$

   Nghiệm này hoàn toàn thỏa mãn điều kiện xác định dương $X^* \succ 0$ do $S \succ 0$.

---

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Phụ lục A & C, Cambridge University Press.
- Gene H. Golub, Charles F. Van Loan, *Matrix Computations*, Johns Hopkins University Press.
