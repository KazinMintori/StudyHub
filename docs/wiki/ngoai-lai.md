---
title: "Ngoại lai"
wikiTerm: ngoai-lai
prev: false
next: false
---

# Ngoại lai

Ngoại lai là quan sát khác biệt đáng kể theo một tiêu chí đã chọn. Việc bị gắn cờ chưa chứng minh đó là lỗi; cần điều tra đơn vị, cơ chế thu thập và bối cảnh.

<WikiUsage />

## Giải thích kỹ thuật

Một điểm có thể khác biệt do lỗi đo, sai đơn vị hoặc do cơ chế thật của dữ liệu. Hàng rào IQR và boxplot chỉ cung cấp tiêu chí gắn cờ. Kiểm tác động lên kết quả khi giữ và loại điểm, rồi dùng bằng chứng về nguồn để quyết định cách xử lý.

Nguồn đọc chính: Wes McKinney, *Python for Data Analysis*, [Chương 7, mục 7.2](https://wesmckinney.com/book/data-cleaning). Ví dụ trong mục này do StudyHub tự tạo.

## Ví dụ

Trong dãy 10, 12, 14, 16, 100, giá 100 nằm ngoài hàng rào IQR của ví dụ.

## Khi nào cần dùng?

Kiểm chất lượng và độ nhạy của kết quả tổng hợp.

## Câu hỏi ôn lại

Có nên luôn xóa điểm ngoài râu boxplot không?

<details><summary>Xem đáp án</summary>

Không. Điểm đó có thể là quan sát thật và có ý nghĩa.

</details>

## Thuật ngữ liên quan

- [Khoảng tứ phân vị](./khoang-tu-phan-vi.md)
- [Cửa sổ trượt](./cua-so-truot.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
