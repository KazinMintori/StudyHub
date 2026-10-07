---
title: "Đạo hàm riêng"
wikiTerm: dao-ham-rieng
prev: false
next: false
---

# Đạo hàm riêng

Đạo hàm riêng lấy đạo hàm theo một biến trong khi giữ các biến còn lại không đổi. Với hàm nhiều biến, một đạo hàm riêng chỉ mô tả một hướng thay đổi; cần tập hợp chúng để có gradient.

<WikiUsage />

## Giải thích kỹ thuật

**Giữ biến khác không đổi.** ∂f/∂x được tính bằng cách dịch x và giữ y, z… cố định. Với f(x,y)=x²y, ta có ∂f/∂x=2xy và ∂f/∂y=x².

Có các đạo hàm riêng tại một điểm chưa tự bảo đảm hàm khả vi tại điểm đó. Điều kiện đủ thường dùng là các đạo hàm riêng liên tục trong một lân cận. Gradient tập hợp các đạo hàm riêng thành một vector.

## Ví dụ

f(x,y) = x² + 3y: ∂f/∂x = 2x và ∂f/∂y = 3.

## Khi nào cần dùng?

Hiểu tối ưu nhiều chiều và các thành phần điện trường.

## Tự kiểm tra

Với f(x,y) = xy, ∂f/∂x là gì?

<details><summary>Xem đáp án</summary>

y, vì khi lấy đạo hàm theo x thì y được giữ cố định.

</details>

## Thuật ngữ liên quan

- [Đạo hàm](./dao-ham.md)
- [Gradient](./gradient.md)
- [Quy tắc chuỗi](./quy-tac-chuoi.md)
- [Hàm số](./ham-so.md)
