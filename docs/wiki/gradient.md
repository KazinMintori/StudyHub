---
title: "Gradient"
wikiTerm: gradient
prev: false
next: false
---

# Gradient

Gradient $\nabla f$ là vector các đạo hàm riêng. Tại điểm khả vi, nó chỉ hướng tăng nhanh nhất của f theo khoảng cách Euclid. Hướng $-\nabla f$ là hướng giảm nhanh nhất tại điểm đó. Một bước quá dài theo hướng này vẫn có thể làm giá trị tăng.

<WikiUsage />

## Giải thích kỹ thuật

**Công thức và xấp xỉ cục bộ.** Với hàm khả vi $f:\mathbb{R}^n\to\mathbb{R}$, gradient là:

$$\nabla f(x)=\left(\frac{\partial f}{\partial x_1},\ldots,\frac{\partial f}{\partial x_n}\right).$$

Với độ dời nhỏ $\Delta x$, ta có $f(x+\Delta x)\approx f(x)+\nabla f(x)\cdot\Delta x$. Đạo hàm theo hướng đơn vị u bằng $\nabla f(x)\cdot u$, lớn nhất khi u cùng hướng gradient nếu gradient khác 0. Khi gradient bằng 0, không có một hướng tăng nhanh nhất được xác định từ công thức này.

**Gradient Descent** cập nhật $x_{k+1}=x_k-\eta\nabla f(x_k)$. Hướng giảm là thông tin cục bộ. Bước $\eta$ quá dài vẫn có thể làm f tăng. Với $f(x)=x^2$, $x_{k+1}=(1-2\eta)x_k$: $0<\eta<1$ làm |x| giảm, $\eta=1$ làm đổi dấu giữ độ lớn, $\eta>1$ có thể gây phân kỳ.

## Ví dụ

$f(x,y)=x^2+y^2$: $\nabla f=(2x,2y)$. Tại (1, 2), gradient là (2, 4).

## Khi nào cần dùng?

Hiểu Gradient Descent và $\mathbf{E}=-\nabla V$.

## Tự kiểm tra

Gradient của $f(x,y) = x+2y$ là gì?

<details><summary>Xem đáp án</summary>

(1, 2).

</details>

## Thuật ngữ liên quan

- [Đạo hàm riêng](./dao-ham-rieng.md)
- [Vector](./vector.md)
- [Đạo hàm](./dao-ham.md)
- [Chuẩn vector](./chuan.md)
- [Điện thế](./dien-the.md)
