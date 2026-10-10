---
title: "Schema dữ liệu"
wikiTerm: schema-du-lieu
prev: false
next: false
---

# Schema dữ liệu

Schema dữ liệu mô tả cấu trúc được chấp nhận: Trường, kiểu và các ràng buộc. Kiểm schema phát hiện lỗi cấu trúc nhưng chưa chứng minh nội dung đúng với thực tế.

<WikiUsage />

## Giải thích kỹ thuật

Một schema cho bảng có thể gồm tên cột, dtype, miền giá và khóa duy nhất. Schema cho phản hồi JSON mô tả trường và kiểu lồng nhau. Đầu ra đạt schema vẫn có thể sai nội dung, chẳng hạn một nhãn cảm xúc nằm trong tập cho phép nhưng không khớp văn bản. Kết hợp kiểm schema với kiểm dữ liệu và mẫu chuẩn.

Nguồn đọc chính: Wes McKinney, *Python for Data Analysis*, [Chương 6–7: Nền tảng nạp và làm sạch](https://wesmckinney.com/book/data-cleaning). Ví dụ trong mục này do StudyHub tự tạo.

## Ví dụ

Đầu ra nhận xét cần id, nhãn và bằng chứng dạng chuỗi; nhãn phải thuộc ba giá trị cho phép.

## Khi nào cần dùng?

Kiểm dữ liệu đọc vào và đầu ra của công cụ trích xuất.

## Câu hỏi ôn lại

Một nhãn hợp lệ theo schema có thể sai với văn bản không?

<details><summary>Xem đáp án</summary>

Có. Kiểu và miền giá trị đúng chưa chứng minh diễn giải đúng.

</details>

## Thuật ngữ liên quan

- [Biểu thức chính quy](./bieu-thuc-chinh-quy.md)
- [API dữ liệu](./api-du-lieu.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
