---
title: "Tập affine"
wikiTerm: tap-affine
prev: false
next: false
---

# Tập affine

Tập C là affine nếu với mọi $x, y \in C$ và mọi số thực $\theta$, điểm $\theta x + (1-\theta)y$ vẫn thuộc C, tức C chứa trọn đường thẳng qua hai điểm bất kỳ của nó. Mọi tập affine có dạng $x_0 + V$ với V là một không gian con. Bao affine của một tập là tập affine nhỏ nhất chứa nó.

<WikiUsage />

## Giải thích kỹ thuật

**Từ tổ hợp affine tới không gian con.** Tổ hợp affine $\theta_1 x_1 + \cdots + \theta_k x_k$ với $\sum_i \theta_i = 1$ cho phép trọng số âm. Nếu $C$ affine và $x_0 \in C$ thì $V = C - x_0$ đóng với phép cộng và nhân vô hướng, nên là không gian con, và chiều của $C$ được định nghĩa là chiều của $V$.

**Tập nghiệm của hệ tuyến tính.** Tập $\{x : Ax = b\}$ là affine, và ngược lại mọi tập affine đều viết được dưới dạng này, với không gian con tương ứng là không gian không $\mathcal N(A)$. Vì vậy ràng buộc đẳng thức trong bài toán lồi phải affine: Một đẳng thức phi tuyến như $x_1^2 + x_2^2 = 1$ cho đường tròn, không lồi.

**Bao affine.** Bao affine $\operatorname{aff} C$ gồm mọi tổ hợp affine của các điểm trong $C$. Ba điểm không thẳng hàng trong $\mathbb R^3$ có bao affine là cả một mặt phẳng. Nguồn: Convex Optimization, §2.1.1–2.1.3.

## Ví dụ

Tập nghiệm của $x_1 + x_2 = 2$ là đường thẳng qua $(2, 0)$ và $(0, 2)$, một tập affine. Đoạn thẳng nối hai điểm đó thì lồi nhưng không affine.

## Khi nào cần dùng?

Mô tả tập nghiệm của hệ phương trình tuyến tính và các ràng buộc đẳng thức của bài toán lồi.

## Câu hỏi ôn lại

Tập affine có nhất thiết chứa gốc tọa độ không?

<details><summary>Xem đáp án</summary>

Không. Chỉ không gian con mới phải chứa gốc. Tập affine là một không gian con được tịnh tiến bởi một vector $x_0$.

</details>

## Thuật ngữ liên quan

- [Tập lồi](./tap-loi.md)
- [Hệ phương trình tuyến tính](./he-phuong-trinh.md)
- [Vector](./vector.md)
