---
title: "Giá trị thiếu"
wikiTerm: gia-tri-thieu
prev: false
next: false
---

# Giá trị thiếu

Giá trị thiếu biểu thị thông tin chưa được biết hoặc không có; nó khác số 0 hay chuỗi rỗng có ý nghĩa. Trong tính toán số, NaN thường đại diện giá trị không xác định. Không kiểm tra NaN bằng phép so sánh bằng thông thường; dùng isna/isnan thích hợp.

<WikiUsage />

## Giải thích kỹ thuật

**NaN không bằng chính nó.** So sánh NaN==NaN cho false trong số thực IEEE thông thường. Dùng chức năng isna/isnan phù hợp thay vì kiểm tra bằng nhau. pandas còn có các dạng biểu diễn thiếu khác tùy kiểu dữ liệu.

Bỏ giá trị thiếu hoặc điền giá trị thay thế đều có thể thay đổi thống kê. Phải biết cơ chế thiếu và mục tiêu phân tích trước khi chọn phương án.

## Ví dụ

Một dòng chưa đo nhiệt độ không nên gán 0°C nếu 0 là nhiệt độ thật có thể xảy ra.

## Khi nào cần dùng?

Đọc làm sạch dữ liệu và tránh thay đổi ý nghĩa thống kê.

## Tự kiểm tra

Thiếu điểm thi có luôn được thay bằng điểm 0 không?

<details><summary>Xem đáp án</summary>

Không. Cần biết nguyên nhân thiếu và quy tắc của bài toán.

</details>

## Thuật ngữ liên quan

- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
- [Broadcasting](./broadcasting.md)
