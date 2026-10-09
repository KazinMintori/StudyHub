---
title: "Tổng hợp theo nhóm"
wikiTerm: groupby
prev: false
next: false
---

# Tổng hợp theo nhóm

Tổng hợp theo nhóm chia dữ liệu theo khóa rồi tính một đại lượng cho từng nhóm. Cần xác định khóa, cách xử lý khóa thiếu và đại lượng tổng hợp.

<WikiUsage />

## Giải thích kỹ thuật

Khóa nhóm quyết định quan sát nào được đặt cùng nhau. `agg` trả kết quả rút gọn; `transform` trả giá trị tương ứng từng dòng để gán lại. `size`, `count` và `nunique` đếm ba đại lượng khác nhau. Kiểm `dropna` cho khóa thiếu và `observed` cho khóa phân loại.

Nguồn đọc chính: Wes McKinney, *Python for Data Analysis*, [Chương 10](https://wesmckinney.com/book/data-aggregation). Ví dụ trong mục này do StudyHub tự tạo.

## Ví dụ

Hai giá 20 và 40 của nhóm A có trung bình 30; transform đưa 30 về từng dòng A.

## Khi nào cần dùng?

Tính thống kê theo loại hàng, địa điểm hoặc kỳ.

## Câu hỏi ôn lại

Agg và transform có cùng số dòng kết quả không?

<details><summary>Xem đáp án</summary>

Thông thường không. Agg rút gọn theo nhóm; transform giữ các dòng tương ứng đầu vào.

</details>

## Thuật ngữ liên quan

- [Nối bảng theo khóa](./noi-bang.md)
- [DataFrame](./dataframe.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
