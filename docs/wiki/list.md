---
title: "List"
wikiTerm: list
prev: false
next: false
---

# List

List Python là dãy có thứ tự, có thể thay đổi và có thể chứa nhiều kiểu đối tượng. Chỉ mục bắt đầu từ 0; chỉ mục âm đếm từ cuối. append thêm ở cuối. List khác mảng NumPy: list * 2 lặp lại dãy, không nhân số trong dãy.

## Giải thích kỹ thuật

**Mutable và aliasing.** List có thể thay đổi tại chỗ. Gán b=a cho hai tên dùng cùng đối tượng; b=a.copy() tạo list mới nhưng chỉ sao chép nông, nên các đối tượng lồng bên trong có thể vẫn dùng chung.

So sánh a is b kiểm tra cùng đối tượng, còn a==b kiểm tra bằng nhau theo giá trị. List khác mảng số NumPy về quy tắc toán học từng phần tử.

## Ví dụ

a=[1,2]; a*2 cho [1,2,1,2], còn một mảng NumPy [1,2] nhân 2 cho [2,4].

## Khi nào cần dùng?

Đọc Python cơ bản trước khi chuyển sang NumPy và pandas.

## Tự kiểm tra

Với a=[4,5,6], a[-1] là gì?

<details><summary>Xem đáp án</summary>

6.

</details>

## Thuật ngữ liên quan

- [Dictionary](./dictionary.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
