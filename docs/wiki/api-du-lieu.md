---
title: "API dữ liệu"
wikiTerm: api-du-lieu
prev: false
next: false
---

# API dữ liệu

API dữ liệu là giao diện để chương trình yêu cầu và nhận dữ liệu theo quy tắc được công bố. API qua HTTP có thể yêu cầu tham số, xác thực và phân trang.

<WikiUsage />

## Giải thích kỹ thuật

Phản hồi thành công ở tầng HTTP chưa xác nhận đủ trường, đúng kiểu hay đủ trang. Quy trình cần timeout, kiểm trạng thái, kiểm schema và điều kiện dừng phân trang. Giữ URL, tham số và thời điểm lấy để đối chiếu. Chủ đề API được đọc cùng phần nạp dữ liệu của học phần.

Nguồn đọc chính: Wes McKinney, *Python for Data Analysis*, [Chương 6, mục 6.3](https://wesmckinney.com/book/accessing-data). Ví dụ trong mục này do StudyHub tự tạo.

## Ví dụ

Một API trả danh sách items cùng cursor của trang kế tiếp; cần đọc các trang để có dữ liệu trong phạm vi yêu cầu.

## Khi nào cần dùng?

Nạp dữ liệu từ hệ thống ngoài với kiểm tra trạng thái và cấu trúc.

## Câu hỏi ôn lại

Một phản hồi HTTP thành công có luôn chứa toàn bộ dữ liệu không?

<details><summary>Xem đáp án</summary>

Không. Nó có thể chỉ là một trang hoặc một phần kết quả.

</details>

## Thuật ngữ liên quan

- [Schema dữ liệu](./schema-du-lieu.md)
- [JSON](./json-du-lieu.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
