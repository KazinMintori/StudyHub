---
title: "DataFrame"
wikiTerm: dataframe
prev: false
next: false
---

# DataFrame

DataFrame là bảng hai chiều có nhãn hàng và nhãn cột trong pandas. Mỗi cột có một kiểu dữ liệu; các cột khác nhau có thể có kiểu khác nhau.

<WikiUsage />

## Giải thích kỹ thuật

DataFrame có hai trục được gắn nhãn. Chọn cột bằng tên trả Series; chọn bằng danh sách tên giữ bảng. `loc` dựa vào nhãn, còn `iloc` dựa vào vị trí. Kiểm dtype và ô thiếu trước khi tính; một phép tính chạy được chưa bảo đảm chọn đúng các quan sát.

Nguồn đọc chính: Wes McKinney, *Python for Data Analysis*, [Chương 5](https://wesmckinney.com/book/pandas-basics). Ví dụ trong mục này do StudyHub tự tạo.

## Ví dụ

Bảng bán hàng có cột id dạng chuỗi, giá dạng số và nhãn hàng 0, 1, 2.

## Khi nào cần dùng?

Chọn, lọc, nối và tổng hợp dữ liệu bảng.

## Câu hỏi ôn lại

df["gia"] và df[["gia"]] có cùng dạng kết quả không?

<details><summary>Xem đáp án</summary>

Không. Cách đầu trả Series, cách sau trả DataFrame một cột.

</details>

## Thuật ngữ liên quan

- [Tổng hợp theo nhóm](./groupby.md)
- [Giá trị thiếu](./gia-tri-thieu.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
