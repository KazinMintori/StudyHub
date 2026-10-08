---
title: "Đạo hàm riêng"
wikiTerm: dao-ham-rieng
prev: false
next: false
---

# Đạo hàm riêng

Đạo hàm riêng lấy đạo hàm theo một biến trong khi giữ các biến còn lại không đổi. Với hàm nhiều biến, một đạo hàm riêng chỉ mô tả một hướng thay đổi. Cần tập hợp chúng để có gradient.

<WikiUsage />

## Giải thích kỹ thuật

**Giữ biến khác không đổi.** $\frac{\partial f}{\partial x}$ được tính bằng cách dịch x và giữ y, z… cố định. Với $f(x,y)=x^{2}y$, ta có $\frac{\partial f}{\partial x}=2xy$ và $\frac{\partial f}{\partial y}=x^{2}$.

Có các đạo hàm riêng tại một điểm chưa tự bảo đảm hàm khả vi tại điểm đó. Điều kiện đủ thường dùng là các đạo hàm riêng liên tục trong một lân cận. Gradient tập hợp các đạo hàm riêng thành một vector.

## Ví dụ

Với $f(x,y)=x^2+3y$, các đạo hàm riêng là:

$$\frac{\partial f}{\partial x}=2x,\qquad\frac{\partial f}{\partial y}=3.$$

## Khi nào cần dùng?

Hiểu tối ưu nhiều chiều và các thành phần điện trường.

## Tự kiểm tra

Với $f(x,y) = xy$, $\frac{\partial f}{\partial x}$ là gì?

<details><summary>Xem đáp án</summary>

y, vì khi lấy đạo hàm theo x thì y được giữ cố định.

</details>

## Thuật ngữ liên quan

- [Đạo hàm](./dao-ham.md)
- [Gradient](./gradient.md)
- [Quy tắc chuỗi](./quy-tac-chuoi.md)
- [Hàm số](./ham-so.md)
