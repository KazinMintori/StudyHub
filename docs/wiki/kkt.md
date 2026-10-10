---
title: "Điều kiện KKT"
wikiTerm: kkt
prev: false
next: false
---

# Điều kiện KKT

Với bài toán $\min_x f_0(x)$ có $m$ ràng buộc $f_i(x)\le0$, đẳng thức $Ax=b$ và các hàm khả vi, KKT gồm khả thi gốc, nhân tử không âm, điều kiện bù trừ $\lambda_i f_i(x)=0$ và điều kiện dừng của Lagrangian. Trong bài toán lồi, KKT đủ cho tối ưu. Để suy ra tính cần, phải có điều kiện phù hợp như Slater.

<WikiUsage />

## Giải thích kỹ thuật

Với $m$ ràng buộc bất đẳng thức, điều kiện dừng cộng một vector cho mỗi ràng buộc:

$\begin{aligned}
0={}&\nabla f_0(x)+\lambda_1\nabla f_1(x)\\
&+\cdots+\lambda_m\nabla f_m(x)+A^T\nu.
\end{aligned}$

Viết gọn:

$0=\nabla f_0(x)+\sum_{i=1}^m\lambda_i\nabla f_i(x)+A^T\nu.$

Với các $f_i$ lồi khả vi và đẳng thức affine, nhân tử không âm làm Lagrangian lồi theo $x$. Điều kiện dừng cho biết $x$ cực tiểu Lagrangian. Khả thi và bù trừ đưa giá trị Lagrangian về $f_0(x)$. Vì vậy khoảng cách đối ngẫu bằng 0 và nghiệm tối ưu.

Slater là điều kiện đủ cho đối ngẫu mạnh: Có điểm trong nội tương đối của miền chung, thỏa đẳng thức và thỏa chặt bất đẳng thức. Với điều kiện này và nghiệm đạt, KKT cũng cần. Trong bài không lồi, nghiệm KKT có thể không tối ưu toàn cục. Nguồn: Convex Optimization, §5.2.3 và §5.5.3.

## Ví dụ

$\min (x-2)^{2}$ với $x\le 1$ có $x^\star=1$, $\lambda^\star=2$. Dừng: $2(1-2)+2=0$. Bù trừ: $2(1-1)=0$.

## Khi nào cần dùng?

Chứng nhận nghiệm ràng buộc và lập hệ Newton–KKT.

## Tự kiểm tra

$\lambda _{i}=0$ có kéo theo $f_{i}(x)<0$ không?

<details><summary>Xem đáp án</summary>

Không. Bù trừ cho phép đồng thời $\lambda _{i}=0$ và $f_{i}(x)=0$. Chiều chắc chắn là $f_{i}(x)<0$ kéo theo $\lambda _{i}=0$.

</details>

## Thuật ngữ liên quan

- [Gradient](./gradient.md)
- [Hàm lồi](./ham-loi.md)
- [Hệ phương trình tuyến tính](./he-phuong-trinh.md)
