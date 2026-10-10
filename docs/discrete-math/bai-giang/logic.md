---
course: discrete-math
lecture: logic
section: lecture
title: "Logic mệnh đề & vị từ"
prerequisites: ["menh-de","luong-tu"]
lessonStatus: ready
description: "Nền tảng logic toán học, bảng chân trị, phép biến đổi tương đương, lượng từ vị từ và phương pháp suy luận hình thức."
---

Logic toán học là nền tảng giúp máy tính tư duy thông qua các giá trị chân lý đúng và sai ($1$ và $0$), đồng thời là cơ sở thiết kế các cổng logic trong mạch tích hợp vi xử lý.

---

## 1. Các phép toán mệnh đề cơ bản

Cho hai mệnh đề $p$ và $q$:

| $p$ | $q$ | Phủ định $\neg p$ | Hội $p \land q$ (AND) | Tuyển $p \lor q$ (OR) | Kéo theo $p \rightarrow q$ | Tương đương $p \leftrightarrow q$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | 0 | 1 | 1 | **1** | 1 |
| 1 | 0 | 0 | 0 | 1 | **0** | 0 |
| 0 | 1 | 1 | 0 | 1 | **1** | 0 |
| 0 | 0 | 1 | 0 | 0 | **1** | 1 |

::: tip Lưu ý về phép kéo theo $p \rightarrow q$
Phép kéo theo $p \rightarrow q$ chỉ **SAI** duy nhất trong trường hợp: **Tiền đề ĐÚNG mà Kết luận SAI** ($1 \rightarrow 0 = 0$).  
Nếu tiền đề $p$ đã SAI ($0$), thì dù $q$ nhận giá trị gì, mệnh đề $p \rightarrow q$ vẫn luôn **ĐÚNG** (chân lý rỗng).
:::

---

## 2. Các luật tương đương logic kinh điển

### Luật De Morgan
Luật De Morgan dùng để biến đổi phủ định của hội và tuyển:

$$
\begin{aligned}
\neg (p \land q) &\equiv \neg p \lor \neg q \\
\neg (p \lor q) &\equiv \neg p \land \neg q
\end{aligned}
$$

### Luật kéo theo và phản đảo
Mọi phép kéo theo đều có thể đưa về phép tuyển:

$$
p \rightarrow q \equiv \neg p \lor q
$$

Mệnh đề phản đảo luôn tương đương logic với mệnh đề gốc:

$$
p \rightarrow q \equiv \neg q \rightarrow \neg p
$$

### Phủ định của lượng từ vị từ
Khi đưa phép phủ định qua lượng từ, ta hoán đổi giữa lượng từ với mọi ($\forall$) và tồn tại ($\exists$):

$$
\begin{aligned}
\neg \forall x P(x) &\equiv \exists x \neg P(x) \\
\neg \exists x P(x) &\equiv \forall x \neg P(x)
\end{aligned}
$$

---

## 3. Hệ thống bài tập tự luyện {#bai-tap}

### Bài 1: Chứng minh tương đương logic bằng luật biến đổi

::: exercise Yêu cầu
Không dùng bảng chân trị, hãy sử dụng các luật tương đương logic cơ bản để chứng minh rằng:
$$
p \rightarrow (q \rightarrow r) \equiv (p \land q) \rightarrow r
$$
:::

::: solution
#### Lời giải chi tiết
Biến đổi vế trái bằng cách áp dụng luật kéo theo $A \rightarrow B \equiv \neg A \lor B$:

$$
\begin{aligned}
p \rightarrow (q \rightarrow r) &\equiv \neg p \lor (q \rightarrow r) \\
&\equiv \neg p \lor (\neg q \lor r) \quad (\text{Luật kéo theo cho ngoặc trong}) \\
&\equiv (\neg p \lor \neg q) \lor r \quad (\text{Tính chất kết hợp của phép tuyển}) \\
&\equiv \neg (p \land q) \lor r \quad (\text{Luật De Morgan}) \\
&\equiv (p \land q) \rightarrow r \quad (\text{Đưa về dạng kéo theo}).
\end{aligned}
$$

Đẳng thức được chứng minh hoàn tất.
:::

---

### Bài 2: Phủ định mệnh đề lượng từ vị từ phức tạp

::: exercise Yêu cầu
Cho vị từ $P(x, y)$ và $Q(x)$ xác định trên tập số thực $\mathbb{R}$. Hãy tìm mệnh đề phủ định của phát biểu sau sao cho dấu phủ định $\neg$ chỉ đứng ngay trước các vị từ cơ sở:
$$
\forall x \exists y \left( P(x, y) \rightarrow Q(x) \right)
$$
:::

::: solution
#### Lời giải chi tiết
Áp dụng quy tắc phủ định lượng từ và luật kéo theo:

1. Phủ định bên ngoài:
   $$
   \neg \left[ \forall x \exists y (P(x, y) \rightarrow Q(x)) \right] \equiv \exists x \forall y \neg \left[ P(x, y) \rightarrow Q(x) \right]
   $$

2. Biến đổi phần phủ định bên trong:
   Vì $P(x, y) \rightarrow Q(x) \equiv \neg P(x, y) \lor Q(x)$, nên:
   $$
   \neg \left[ P(x, y) \rightarrow Q(x) \right] \equiv \neg \left[ \neg P(x, y) \lor Q(x) \right]
   $$
   Áp dụng luật De Morgan:
   $$
   \neg \left[ \neg P(x, y) \lor Q(x) \right] \equiv P(x, y) \land \neg Q(x)
   $$

3. Kết quả phủ định cuối cùng:
   $$
   \exists x \forall y \left( P(x, y) \land \neg Q(x) \right)
   $$
:::

---

### Bài 3: Kiểm tra tính hằng đúng (Tautology)

::: exercise Yêu cầu
Xét biểu thức logic sau:
$$
E = \left[ (p \rightarrow q) \land (q \rightarrow r) \right] \rightarrow (p \rightarrow r)
$$
Hãy chứng minh $E$ là một hằng đúng (luôn có giá trị chân lý là 1 trên mọi trường hợp của $p, q, r$). Quy tắc suy luận này có tên gọi là gì?
:::

::: solution
#### Lời giải chi tiết
Đây là **Quy tắc tam đoạn luận giả định (Hypothetical Syllogism)**. Ta chứng minh bằng phương pháp phản chứng:

Giả sử biểu thức $E$ nhận giá trị SAI ($0$).
Vì $E$ có dạng $A \rightarrow B$, điều này chỉ xảy ra khi:
- Tiền đề $A = 1 \iff (p \rightarrow q) \land (q \rightarrow r) = 1$, tức là:
  $$p \rightarrow q = 1 \quad \text{và} \quad q \rightarrow r = 1$$
- Kết luận $B = 0 \iff p \rightarrow r = 0$, điều này xảy ra khi và chỉ khi:
  $$p = 1 \quad \text{và} \quad r = 0$$

Từ $p = 1$ và $p \rightarrow q = 1$, suy ra bắt buộc $q = 1$.
Từ $q = 1$ và $q \rightarrow r = 1$, suy ra bắt buộc $r = 1$.

Điều này mâu thuẫn trực tiếp với điều kiện $r = 0$ ở trên.
Do giả thiết phản chứng dẫn tới mâu thuẫn, biểu thức $E$ không bao giờ nhận giá trị 0. Vậy $E$ là một hằng đúng.
:::
