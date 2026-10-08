---
title: "Quy hoạch hình học (GP)"
wikiTerm: quy-hoach-hinh-hoc
prev: false
next: false
---

# Quy hoạch hình học (GP)

Monomial là hàm $c\,x_1^{a_1}\cdots x_n^{a_n}$ với $c > 0$ và số mũ thực, posynomial là tổng các monomial. GP cực tiểu một posynomial với các ràng buộc posynomial $\le 1$ và monomial $= 1$ trên miền $x \succ 0$. Đổi biến $y = \log x$ rồi lấy logarit các hàm đưa GP về một bài toán lồi dùng hàm log-sum-exp.

<WikiUsage />

## Giải thích kỹ thuật

**Dạng lồi.** Với $y = \log x$, một monomial thành $e^{a^Ty + b}$ và một posynomial thành $\sum_k e^{a_k^Ty + b_k}$. Lấy logarit, ràng buộc posynomial thành $\log\sum_k e^{a_k^Ty + b_k} \le 0$, lồi, và ràng buộc monomial thành một phương trình affine. Tính lồi trong biến $\log x$ nghĩa là tập khả thi chứa trung bình nhân của hai điểm bất kỳ của nó.

**Ví dụ của sách.** Cân bằng ma trận theo chuẩn Frobenius, $\min_d \sum_{i,j} M_{ij}^2 d_i^2/d_j^2$, thiết kế dầm công-xôn và cực tiểu bán kính phổ Perron–Frobenius của ma trận có phần tử posynomial. Nguồn: Convex Optimization, §4.5.

## Ví dụ

Áp phích có phần chữ $wh \ge 600$, lề hai bên 2 cm, lề trên dưới 3 cm: cực tiểu $(w + 4)(h + 6)$ cho $w = 20$, $h = 30$.

## Khi nào cần dùng?

Thiết kế kỹ thuật, cân bằng ma trận, các mô hình có quan hệ lũy thừa giữa những đại lượng dương.

## Câu hỏi ôn lại

Một posynomial có lồi theo biến gốc x không?

<details><summary>Xem đáp án</summary>

Không nhất thiết, vì $\sqrt{x}$ là posynomial nhưng lõm. Điều chắc chắn là sau khi đổi biến $x = e^y$ và lấy logarit, nó trở thành hàm lồi.

</details>

## Thuật ngữ liên quan

- [Log-sum-exp và softmax](./log-sum-exp.md)
- [Bài toán tương đương](./bai-toan-tuong-duong.md)
- [Hàm lồi](./ham-loi.md)
