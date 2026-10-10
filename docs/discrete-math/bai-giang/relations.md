---
course: discrete-math
lecture: relations
section: lecture
title: "Quan hệ & ánh xạ"
prerequisites: ["tap-hop","quan-he","ham-so"]
lessonStatus: ready
description: "Bản chất quan hệ hai ngôi, bốn tính chất cơ bản, quan hệ tương đương, phân hoạch tập hợp và quan hệ thứ tự bộ phận."
---

Quan hệ là công cụ toán học mô tả mối liên kết giữa các phần tử trong cùng một tập hợp hoặc giữa các tập hợp khác nhau, đóng vai trò nền tảng trong lý thuyết cơ sở dữ liệu quan hệ (RDBMS) và hệ thống phân cấp kiểu dữ liệu.

---

## 1. Bốn tính chất cơ bản của quan hệ hai ngôi

Cho quan hệ hai ngôi $R$ trên tập hợp $A$ (tức là $R \subseteq A \times A$):

1. **Tính phản xạ (Reflexive):** Mọi phần tử đều có quan hệ với chính nó:
   $$\forall x \in A, (x, x) \in R$$
2. **Tính đối xứng (Symmetric):** Nếu $x$ có quan hệ với $y$ thì $y$ cũng có quan hệ với $x$:
   $$\forall x, y \in A, (x, y) \in R \implies (y, x) \in R$$
3. **Tính phản đối xứng (Antisymmetric):** Nếu $x$ quan hệ với $y$ và $y$ quan hệ với $x$ thì bắt buộc $x$ và $y$ phải trùng nhau:
   $$\forall x, y \in A, \left( (x, y) \in R \land (y, x) \in R \right) \implies x = y$$
4. **Tính bắc cầu (Transitive):** Nếu $x$ quan hệ với $y$ và $y$ quan hệ với $z$ thì kéo theo $x$ quan hệ với $z$:
   $$\forall x, y, z \in A, \left( (x, y) \in R \land (y, z) \in R \right) \implies (x, z) \in R$$

---

## 2. Quan hệ tương đương và Quan hệ thứ tự bộ phận

### Quan hệ tương đương (Equivalence Relation)
Một quan hệ $R$ được gọi là quan hệ tương đương nếu nó thỏa mãn đủ ba tính chất: **Phản xạ, Đối xứng và Bắc cầu**.
- Mỗi quan hệ tương đương chia tập $A$ thành các **lớp tương đương (equivalence classes)** rời nhau, tạo nên một phân hoạch hoàn chỉnh của tập $A$.
- Ví dụ: Quan hệ đồng dư modulo $m$ trên tập số nguyên $\mathbb{Z}$ ($a \equiv b \pmod m$).

### Quan hệ thứ tự bộ phận (Partial Order - POSet)
Một quan hệ $R$ được gọi là quan hệ thứ tự bộ phận nếu nó thỏa mãn đủ ba tính chất: **Phản xạ, Phản đối xứng và Bắc cầu**.
- Cặp $(A, R)$ khi đó được gọi là một tập sắp thứ tự bộ phận (Partially Ordered Set - POSet).
- Ví dụ: Quan hệ nhỏ hơn hoặc bằng ($\le$) trên tập số thực, hoặc quan hệ bao hàm tập con ($\subseteq$) trên tập các tập con.

---

## 3. Hệ thống bài tập tự luyện {#bai-tap}

### Bài 1: Khảo sát các tính chất của quan hệ số học

::: exercise Yêu cầu
Xét tập các số nguyên dương $\mathbb{Z}^+ = \{1, 2, 3, \dots\}$. Khảo sát 4 tính chất (Phản xạ, Đối xứng, Phản đối xứng, Bắc cầu) của hai quan hệ sau:
1. Quan hệ chia hết $R_1$: $(a, b) \in R_1 \iff a \mid b$ ($a$ là ước của $b$).
2. Quan hệ $R_2$: $(a, b) \in R_2 \iff a + b \text{ là số chẵn}$.
:::

::: solution
#### Lời giải chi tiết
1. **Xét quan hệ chia hết $R_1$:**
   - *Phản xạ:* Với mọi $a \in \mathbb{Z}^+$, $a = 1 \cdot a$ nên $a \mid a$. Tính chất phản xạ thỏa mãn.
   - *Đối xứng:* Không thỏa mãn. Ví dụ $2 \mid 4$ nhưng $4 \nmid 2$.
   - *Phản đối xứng:* Giả sử $a \mid b$ và $b \mid a$. Vì $a, b > 0$, suy ra $a \le b$ và $b \le a$, kéo theo $a = b$. Tính chất phản đối xứng thỏa mãn.
   - *Bắc cầu:* Nếu $a \mid b$ và $b \mid c$, tồn tại $k, m \in \mathbb{Z}^+$ sao cho $b = ka$ và $c = mb$. Khi đó $c = m(ka) = (mk)a$, suy ra $a \mid c$. Tính chất bắc cầu thỏa mãn.
   - *Kết luận:* $R_1$ là một quan hệ thứ tự bộ phận (POSet).

2. **Xét quan hệ $R_2$ ($a + b$ chẵn):**
   - *Phản xạ:* $a + a = 2a$ luôn là số chẵn với mọi $a$. Phản xạ thỏa mãn.
   - *Đối xứng:* $a + b = b + a$, nếu $a + b$ chẵn thì $b + a$ cũng chẵn. Đối xứng thỏa mãn.
   - *Phản đối xứng:* Không thỏa mãn. Ví dụ với $a = 1, b = 3$: $1 + 3 = 4$ (chẵn) và $3 + 1 = 4$ (chẵn), nhưng $1 \ne 3$.
   - *Bắc cầu:* $a + b$ chẵn nghĩa là $a$ và $b$ cùng tính chẵn lẻ. Nếu $(a, b) \in R_2$ ($a, b$ cùng chẵn hoặc cùng lẻ) và $(b, z) \in R_2$ ($b, z$ cùng tính chẵn lẻ), thì kéo theo $a$ và $z$ cùng tính chẵn lẻ, tức là $a + z$ chẵn. Bắc cầu thỏa mãn.
   - *Kết luận:* $R_2$ là một quan hệ tương đương.
:::

---

### Bài 2: Xác định lớp tương đương và phân hoạch

::: exercise Yêu cầu
Cho quan hệ tương đương $R$ trên tập số nguyên $\mathbb{Z}$ định nghĩa bởi:
$$
a \, R \, b \iff a \equiv b \pmod 4
$$
1. Hãy tìm các lớp tương đương $[0], [1], [2], [3]$.
2. Chỉ ra phân hoạch của tập $\mathbb{Z}$ do quan hệ này tạo ra.
:::

::: solution
#### Lời giải chi tiết
1. Lớp tương đương $[a]$ là tập hợp tất cả các số nguyên $x$ thỏa mãn $x \equiv a \pmod 4$:
   $$
   [a] = \{ x \in \mathbb{Z} \mid x - a = 4k, k \in \mathbb{Z} \} = \{ 4k + a \mid k \in \mathbb{Z} \}
   $$
   Cụ thể:
   - $[0] = \{ \dots, -8, -4, 0, 4, 8, \dots \}$ (Tập hợp các số nguyên chia hết cho 4).
   - $[1] = \{ \dots, -7, -3, 1, 5, 9, \dots \}$ (Tập hợp các số nguyên chia cho 4 dư 1).
   - $[2] = \{ \dots, -6, -2, 2, 6, 10, \dots \}$ (Tập hợp các số nguyên chia cho 4 dư 2).
   - $[3] = \{ \dots, -5, -1, 3, 7, 11, \dots \}$ (Tập hợp các số nguyên chia cho 4 dư 3).

2. Bốn lớp tương đương này đôi một rời nhau và hợp của chúng phủ kín tập số nguyên:
   $$
   [0] \cap [1] = [0] \cap [2] = \dots = \emptyset \quad \text{và} \quad [0] \cup [1] \cup [2] \cup [3] = \mathbb{Z}
   $$
   Họ các tập hợp $\{[0], [1], [2], [3]\}$ chính là phân hoạch của $\mathbb{Z}$.
:::

---

### Bài 3: Phần tử tối đại và tối tiểu trong POSet

::: exercise Yêu cầu
Xét tập hợp $S = \{2, 3, 4, 6, 8, 12, 24\}$ cùng với quan hệ chia hết $\mid$.
1. Cặp $(S, \mid)$ có phải là một thứ tự toàn phần không?
2. Tìm các phần tử tối đại (Maximal elements) và phần tử tối tiểu (Minimal elements) của POSet này. Có tồn tại phần tử lớn nhất (Greatest element) và nhỏ nhất (Least element) không?
:::

::: solution
#### Lời giải chi tiết
1. $(S, \mid)$ không phải là thứ tự toàn phần vì tồn tại các cặp phần tử không thể so sánh được với nhau theo quan hệ chia hết. Ví dụ: $2 \nmid 3$ và $3 \nmid 2$, hay $4 \nmid 6$ và $6 \nmid 4$.

2. Phân tích các phần tử đặc biệt:
   - **Phần tử tối tiểu:** Là phần tử trong $S$ mà không có phần tử nào khác trong $S$ là ước thực sự của nó. Quan sát tập $S$, các số $2$ và $3$ không có ước nào khác trong $S$. Do đó, các phần tử tối tiểu là **$2$ và $3$**.
   - Vì có hai phần tử tối tiểu khác nhau, POSet này **không có phần tử nhỏ nhất**.
   - **Phần tử tối đại:** Là phần tử trong $S$ mà không là ước thực sự của bất kỳ phần tử nào khác trong $S$. Trong tập này, số $24$ là bội số của tất cả các phần tử còn lại ($2, 3, 4, 6, 8, 12$ đều chia hết $24$). Vì vậy, phần tử tối đại duy nhất là **$24$**.
   - Vì $24$ là bội của mọi phần tử trong $S$, $24$ đồng thời là **phần tử lớn nhất**.
:::
