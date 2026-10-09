---
title: "Cửa sổ trượt"
wikiTerm: cua-so-truot
prev: false
next: false
---

# Cửa sổ trượt

Cửa sổ trượt chọn một miền quan sát gần mỗi vị trí rồi tính thống kê trên miền ấy. Miền có thể được xác định bằng số quan sát hoặc khoảng thời gian; hai cách không luôn tương đương.

<WikiUsage />

## Giải thích kỹ thuật

`rolling(window=2)` chọn theo hai quan sát, còn `rolling("2D")` chọn theo khoảng thời gian. `min_periods` đặt số giá trị hợp lệ tối thiểu. Cửa sổ căn giữa có thể chứa quan sát tương lai; không dùng những giá trị chưa có tại thời điểm dự đoán.

Nguồn đọc chính: Wes McKinney, *Python for Data Analysis*, [Chương 11, mục 11.7](https://wesmckinney.com/book/time-series). Ví dụ trong mục này do StudyHub tự tạo.

## Ví dụ

Dãy 10, 20, 30 với cửa sổ hai quan sát cho trung bình 15 và 25 ở hai vị trí cuối.

## Khi nào cần dùng?

Làm trơn chuỗi và tính thống kê cục bộ.

## Câu hỏi ôn lại

Cửa sổ hai quan sát có luôn dài hai ngày không?

<details><summary>Xem đáp án</summary>

Không. Điều đó phụ thuộc thời điểm của các quan sát.

</details>

## Thuật ngữ liên quan

- [Ngoại lai](./ngoai-lai.md)
- [Múi giờ](./mui-gio.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
