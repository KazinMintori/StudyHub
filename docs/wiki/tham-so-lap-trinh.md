---
title: "Tham số trong lập trình"
wikiTerm: tham-so-lap-trinh
prev: false
next: false
---

# Tham số trong lập trình

Trong định nghĩa hàm, tham số là tên đại diện cho dữ liệu đầu vào. Khi gọi hàm, đối số là giá trị cụ thể được truyền vào. Nghĩa này thuộc lập trình và khác tham số của một mô hình toán học.

<WikiUsage />

## Giải thích kỹ thuật

**Tên trong định nghĩa, giá trị trong lời gọi.** Với `def f(x, scale=1)`, `x` và `scale` là tham số. Trong `f(data, scale=2)`, `data` và `2` là đối số. Tham số mặc định được dùng khi lời gọi không truyền giá trị tương ứng.

Khi gọi hàm, Python dùng cơ chế chia sẻ đối tượng. Nếu đối số là list và hàm sửa list tại chỗ, bên gọi có thể quan sát thay đổi. Đây là cơ chế của lời gọi hàm. Nó không liên quan đến “tham số mô hình” trong một bài toán tối ưu.

## Ví dụ

Trong def double(x): Return 2*x, x là tham số. Trong double(3), số 3 là đối số.

## Khi nào cần dùng?

Đọc chữ ký hàm, truyền dữ liệu và phân biệt định nghĩa hàm với lời gọi hàm.

## Câu hỏi ôn lại

Trong lời gọi pow(2, 3), 2 và 3 là tham số hay đối số?

<details><summary>Xem đáp án</summary>

Đó là các đối số, còn tên tham số nằm trong định nghĩa của hàm pow.

</details>

## Thuật ngữ liên quan

- [Hàm trong lập trình](./ham-lap-trinh.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
- [List](./list.md)
