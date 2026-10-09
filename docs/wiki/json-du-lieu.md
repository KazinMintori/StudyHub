---
title: "JSON"
wikiTerm: json-du-lieu
prev: false
next: false
---

# JSON

JSON là định dạng văn bản biểu diễn đối tượng, mảng, chuỗi, số, Boolean và null. Phân tích JSON tạo cấu trúc dữ liệu; bước này chưa xác nhận các trường đáp ứng yêu cầu nghiệp vụ.

<WikiUsage />

## Giải thích kỹ thuật

`json.loads` phân tích văn bản JSON; `json.dumps` tạo văn bản từ cấu trúc Python phù hợp. `pd.json_normalize` trải các trường lồng nhau thành cột. Danh sách con có thể được giữ, mở hoặc tổng hợp tùy mục tiêu; mở danh sách thường làm tăng số dòng.

Nguồn đọc chính: Wes McKinney, *Python for Data Analysis*, [Chương 6, JSON Data](https://wesmckinney.com/book/accessing-data). Ví dụ trong mục này do StudyHub tự tạo.

## Ví dụ

Một phản hồi có trường items chứa danh sách các bản ghi, mỗi bản ghi có id và giá.

## Khi nào cần dùng?

Trao đổi dữ liệu lồng nhau và nhận phản hồi từ API.

## Câu hỏi ôn lại

JSON đọc được có tự chứng minh đủ trường cần dùng không?

<details><summary>Xem đáp án</summary>

Không. Cần kiểm tên trường, kiểu và các ràng buộc riêng.

</details>

## Thuật ngữ liên quan

- [API dữ liệu](./api-du-lieu.md)
- [Dữ liệu dạng dài](./du-lieu-dang-dai.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
