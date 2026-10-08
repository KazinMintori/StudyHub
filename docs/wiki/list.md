---
title: "List"
wikiTerm: list
prev: false
next: false
---

# List

List Python là dãy có thứ tự, có thể thay đổi và có thể chứa nhiều kiểu đối tượng. Chỉ mục bắt đầu từ 0. Chỉ mục âm đếm từ cuối. append thêm ở cuối. List khác mảng NumPy: list * 2 lặp lại dãy, không nhân số trong dãy.

<WikiUsage />

## Giải thích kỹ thuật

**Mutable và aliasing.** List có thể thay đổi tại chỗ. Gán `b = a` khiến hai tên dùng chung đối tượng, còn `b = a.copy()` tạo một list mới. Đây chỉ là sao chép nông, vì vậy các đối tượng lồng bên trong vẫn có thể dùng chung.

So sánh `a is b` kiểm tra hai tên có trỏ đến cùng đối tượng hay không, còn `a == b` so sánh giá trị. List khác mảng NumPy về quy tắc tính toán theo từng phần tử.

## Ví dụ

Với list a = [1, 2], phép a * 2 lặp lại dãy thành [1, 2, 1, 2]. Còn với mảng NumPy chứa [1, 2], nhân 2 theo từng phần tử cho [2, 4].

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
