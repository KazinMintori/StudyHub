---
title: "Quy tắc chuỗi"
wikiTerm: quy-tac-chuoi
prev: false
next: false
---

# Quy tắc chuỗi

Đạo hàm của hợp hàm nhân tốc độ thay đổi của lớp ngoài với lớp trong: d[g(f(x))]/dx = g′(f(x))f′(x). Với nhiều biến, cộng các đóng góp theo mọi đường phụ thuộc. Đây là nền tảng của lan truyền ngược.

## Giải thích kỹ thuật

**Nhiều đường phụ thuộc.** Nếu z=f(x(t),y(t)), dz/dt=(∂f/∂x)(dx/dt)+(∂f/∂y)(dy/dt). Mỗi đường từ t tới z đóng góp một tích các đạo hàm trên đường đó.

Trong lan truyền ngược, đồ thị tính toán tổ chức những phép nhân và cộng này. Bỏ sót một nhánh phụ thuộc làm gradient sai dù công thức ở các nhánh khác đúng.

## Ví dụ

y = (3x+1)²: y′ = 2(3x+1)×3 = 6(3x+1).

## Khi nào cần dùng?

Hiểu đạo hàm hàm mục tiêu và backpropagation.

## Tự kiểm tra

Đạo hàm của sin(2x) là gì?

<details><summary>Xem đáp án</summary>

2cos(2x).

</details>

## Thuật ngữ liên quan

- [Trị riêng &amp; vector riêng](./tri-rieng.md)
- [Tích phân](./tich-phan.md)
- [Vector](./vector.md)
