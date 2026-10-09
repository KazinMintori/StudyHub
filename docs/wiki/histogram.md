---
title: "Histogram"
wikiTerm: histogram
prev: false
next: false
---

# Histogram

Histogram chia miền giá trị số thành các khoảng rồi biểu diễn số lượng hoặc mật độ trong mỗi khoảng. Khi vẽ mật độ, diện tích cột phản ánh phần khối lượng trong khoảng.

<WikiUsage />

## Giải thích kỹ thuật

Mỗi cột ứng với một khoảng số. Biên khoảng quyết định các giá trị ở biên được đếm vào đâu. Với cột tần suất, độ cao đếm quan sát; với mật độ, diện tích biểu diễn phần khối lượng. Thay biên khoảng có thể đổi ấn tượng về phân phối nên cần kiểm độ ổn định của nhận xét.

Nguồn đọc chính: Wes McKinney, *Python for Data Analysis*, [Chương 9, mục 9.2](https://wesmckinney.com/book/plotting-and-visualization). Ví dụ trong mục này do StudyHub tự tạo.

## Ví dụ

Các khoảng đều từ 0 đến 40 của ví dụ giá có số lượng 0, 4, 4 và 2.

## Khi nào cần dùng?

Xem hình dạng phân phối của biến số.

## Câu hỏi ôn lại

Density=True có làm tổng độ cao các cột bằng 1 không?

<details><summary>Xem đáp án</summary>

Không nhất thiết. Tổng diện tích các cột bằng 1.

</details>

## Thuật ngữ liên quan

- [Trích xuất bằng LLM](./llm-trich-xuat.md)
- [Khoảng tứ phân vị](./khoang-tu-phan-vi.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
