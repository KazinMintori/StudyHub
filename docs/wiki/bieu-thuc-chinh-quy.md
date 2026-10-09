---
title: "Biểu thức chính quy"
wikiTerm: bieu-thuc-chinh-quy
prev: false
next: false
---

# Biểu thức chính quy

Biểu thức chính quy là mẫu mô tả cách khớp một tập chuỗi. Ký tự đặc biệt có ý nghĩa trong mẫu; tìm một đoạn khớp khác với yêu cầu toàn chuỗi khớp.

<WikiUsage />

## Giải thích kỹ thuật

`contains` tìm một đoạn khớp; `match` kiểm từ đầu; `fullmatch` kiểm toàn bộ chuỗi. Dấu chấm và các ký tự đặc biệt cần được thoát khi muốn khớp literal. Dùng chuỗi raw của Python cho mẫu nhiều dấu gạch chéo ngược. Regex kiểm được định dạng, chưa tự xác nhận ý nghĩa thực tế của mã.

Nguồn đọc chính: Wes McKinney, *Python for Data Analysis*, [Chương 7, mục 7.4](https://wesmckinney.com/book/data-cleaning). Ví dụ trong mục này do StudyHub tự tạo.

## Ví dụ

Mẫu SP-[0-9]{3} dùng với fullmatch nhận SP-001 và loại ghi chú SP-001.

## Khi nào cần dùng?

Kiểm định dạng và trích xuất trường ổn định từ văn bản.

## Câu hỏi ôn lại

Muốn tìm dấu chấm thật thì có thể dùng cách nào?

<details><summary>Xem đáp án</summary>

Tìm literal với regex=False, hoặc thoát dấu chấm trong mẫu regex.

</details>

## Thuật ngữ liên quan

- [Múi giờ](./mui-gio.md)
- [Schema dữ liệu](./schema-du-lieu.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
