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

Toàn bộ hệ thống bài tập thực hành chuyên sâu của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu luyện tập.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở các bài tập thực chiến có hướng dẫn chi tiết và kiểm chứng tự động.
:::

