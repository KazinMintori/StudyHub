---
title: "Gradient"
wikiTerm: gradient
prev: false
next: false
---

# Gradient

Gradient ∇f là vector các đạo hàm riêng. Tại điểm khả vi, nó chỉ hướng tăng nhanh nhất của f theo khoảng cách Euclid. Hướng −∇f là hướng giảm nhanh nhất tại điểm đó; một bước quá dài theo hướng này vẫn có thể làm giá trị tăng.

## Giải thích kỹ thuật

**Công thức và xấp xỉ cục bộ.** Với hàm khả vi f: ℝⁿ→ℝ, gradient là:

$$\nabla f(x)=\left(\frac{\partial f}{\partial x_1},\ldots,\frac{\partial f}{\partial x_n}\right).$$

Với độ dời nhỏ Δx, ta có f(x+Δx)≈f(x)+∇f(x)·Δx. Đạo hàm theo hướng đơn vị u bằng ∇f(x)·u, lớn nhất khi u cùng hướng gradient nếu gradient khác 0. Khi gradient bằng 0, không có một hướng tăng nhanh nhất được xác định từ công thức này.

**Gradient Descent** cập nhật x mới=x cũ−η∇f(x cũ). Hướng giảm là thông tin cục bộ; bước η quá dài vẫn có thể làm f tăng. Với f(x)=x², x mới=(1−2η)x cũ: 0<η<1 làm |x| giảm, η=1 làm đổi dấu giữ độ lớn, η>1 có thể gây phân kỳ.

## Ví dụ

f(x,y) = x²+y²: ∇f = (2x, 2y). Tại (1, 2), gradient là (2, 4).

## Khi nào cần dùng?

Hiểu Gradient Descent và E = −∇V.

## Tự kiểm tra

Gradient của f(x,y) = x+2y là gì?

<details><summary>Xem đáp án</summary>

(1, 2).

</details>

## Thuật ngữ liên quan

- [Đạo hàm riêng](./dao-ham-rieng.md)
- [Vector](./vector.md)
- [Đạo hàm](./dao-ham.md)
- [Chuẩn vector](./chuan.md)
- [Điện thế](./dien-the.md)
