---
course: discrete-math
lecture: relations
section: lecture
title: "Quan hệ & ánh xạ"
prerequisites: ["tap-hop","quan-he","ham-so"]
lessonStatus: ready
---


Quan hệ là cách chúng ta mô tả mối liên kết giữa các phần tử trong cùng một tập hợp hoặc giữa các tập hợp khác nhau.

---

## 1. Bốn Tính Chất Cơ Bản của Quan hệ Trên Tập $A$

Cho quan hệ hai ngôi $R$ trên tập $A$:

1. **Phản xạ (Reflexive):** Mọi phần tử đều có quan hệ với chính nó:
   $$\forall x \in A, (x, x) \in R$$
2. **Đối xứng (Symmetric):** Nếu $x$ quan hệ với $y$ thì $y$ cũng quan hệ với $x$:
   $$\forall x, y \in A, (x, y) \in R \implies (y, x) \in R$$
3. **Phản đối xứng (Antisymmetric):** Nếu $x$ quan hệ với $y$ và $y$ quan hệ với $x$ thì bắt buộc $x = y$:
   $$\forall x, y \in A, ((x, y) \in R \land (y, x) \in R) \implies x = y$$
4. **Bắc cầu (Transitive):** Nếu $x$ quan hệ với $y$ và $y$ quan hệ với $z$ thì $x$ quan hệ với $z$:
   $$\forall x, y, z \in A, ((x, y) \in R \land (y, z) \in R) \implies (x, z) \in R$$

---

## 2. Quan hệ Tương đương vs Quan hệ Thứ tự

- **Quan hệ tương đương (Equivalence Relation):** Thỏa mãn 3 tính chất: **Phản xạ + Đối xứng + Bắc cầu**.
  - *Ví dụ:* Quan hệ "đồng dư modulo $m$" ($a \equiv b \pmod m$), quan hệ "cùng ngày sinh".
- **Quan hệ thứ tự bộ phận (Partial Order - Poset):** Thỏa mãn 3 tính chất: **Phản xạ + Phản đối xứng + Bắc cầu**.
  - *Ví dụ:* Quan hệ "nhỏ hơn hoặc bằng" ($\le$), quan hệ "chia hết" ($a \mid b$).
