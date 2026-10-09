---
title: "Dữ liệu dạng dài"
wikiTerm: du-lieu-dang-dai
prev: false
next: false
---

# Dữ liệu dạng dài

Ở dạng dài, một biến phân loại được đặt trong một cột giá trị thay vì trải thành nhiều cột riêng. Khóa nhận diện mỗi quan sát cần được xác định theo các cột liên quan.

<WikiUsage />

## Giải thích kỹ thuật

`melt` đưa các tên cột thành giá trị của một cột mới. `pivot` đổi ngược lại khi mỗi cặp khóa có tối đa một giá trị. `pivot_table` bổ sung phép tổng hợp khi khóa lặp. Số dòng có thể đổi dù lượng thông tin không đổi, nên kiểm lại khóa sau chuyển dạng.

Nguồn đọc chính: Wes McKinney, *Python for Data Analysis*, [Chương 8, mục 8.3](https://wesmckinney.com/book/data-wrangling). Ví dụ trong mục này do StudyHub tự tạo.

## Ví dụ

Bảng có cột sách và vở được melt thành các cột quầy, mặt hàng và số lượng.

## Khi nào cần dùng?

Chuẩn bị dữ liệu cho groupby, nối và biểu đồ theo nhóm.

## Câu hỏi ôn lại

Pivot cần điều kiện gì với mỗi cặp khóa hàng và cột?

<details><summary>Xem đáp án</summary>

Có tối đa một giá trị cho mỗi cặp; nếu trùng cần phép tổng hợp rõ ràng.

</details>

## Thuật ngữ liên quan

- [JSON](./json-du-lieu.md)
- [Nối bảng theo khóa](./noi-bang.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
