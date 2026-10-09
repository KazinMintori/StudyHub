---
title: "Nối bảng theo khóa"
wikiTerm: noi-bang
prev: false
next: false
---

# Nối bảng theo khóa

Nối bảng tạo các cặp dòng khớp theo khóa. Kiểu nối quyết định dòng không khớp được giữ hay bỏ; số lần lặp khóa quyết định số cặp khớp.

<WikiUsage />

## Giải thích kỹ thuật

Với một khóa xuất hiện m lần bên trái và n lần bên phải, phép nối tạo m nhân n cặp cho khóa ấy. Kiểu nối quyết định việc giữ dòng không khớp. `validate` kiểm quan hệ số lần xuất hiện khóa; `indicator` ghi nhận nguồn khớp. Cần xử lý khóa thiếu vì pandas có thể khớp thiếu với thiếu.

Nguồn đọc chính: Wes McKinney, *Python for Data Analysis*, [Chương 8, mục 8.2](https://wesmckinney.com/book/data-wrangling). Ví dụ trong mục này do StudyHub tự tạo.

## Ví dụ

Ba dòng trái và hai dòng phải cùng khóa A tạo sáu cặp khớp.

## Khi nào cần dùng?

Bổ sung thông tin từ bảng danh mục và kiểm tra quan hệ dữ liệu.

## Câu hỏi ôn lại

Bảng phải là danh mục duy nhất thì dùng validate nào trong pandas?

<details><summary>Xem đáp án</summary>

many_to_one nếu bên trái có thể có nhiều dòng cùng khóa.

</details>

## Thuật ngữ liên quan

- [Dữ liệu dạng dài](./du-lieu-dang-dai.md)
- [Tổng hợp theo nhóm](./groupby.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
