---
title: "Mảng"
wikiTerm: mang
prev: false
next: false
---

# Mảng

Mảng lưu các phần tử theo thứ tự và dùng chỉ mục để truy cập. Mảng liên tiếp trong bộ nhớ cho phép tính địa chỉ từ vị trí và kích thước phần tử. Cần phân biệt mảng số có cùng kiểu với list Python có thể chứa các đối tượng khác kiểu.

<WikiUsage />

## Giải thích kỹ thuật

**Địa chỉ và kích thước phần tử.** Trong mảng liên tiếp, địa chỉ phần tử i bằng địa chỉ đầu cộng i lần kích thước phần tử. Công thức giải thích truy cập trực tiếp O(1), nhưng không áp dụng nguyên dạng cho mọi đối tượng dãy.

Mảng nhiều chiều cần shape và strides để biết cách ánh xạ chỉ mục sang bộ nhớ. Thêm phần tử giữa một mảng liên tiếp có thể phải dịch dữ liệu.

## Ví dụ

Với a = [10, 20, 30], chỉ mục 0 chọn giá trị 10, còn chỉ mục 2 chọn giá trị 30.

## Khi nào cần dùng?

Hiểu lưu trữ, chỉ mục, vector hóa và thao tác trên dãy.

## Tự kiểm tra

Mảng có 4 phần tử và đánh số từ 0 có chỉ mục cuối là gì?

<details><summary>Xem đáp án</summary>

3.

</details>

## Thuật ngữ liên quan

- [Con trỏ &amp; tham chiếu](./con-tro.md)
- [Heuristic](./heuristic.md)
- [Đồ thị](./do-thi.md)
