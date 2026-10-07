---
title: "Biến & kiểu dữ liệu"
wikiTerm: bien-kieu
prev: false
next: false
---

# Biến & kiểu dữ liệu

Biến là tên dùng để truy cập giá trị; kiểu dữ liệu quy định các phép toán phù hợp. Trong Python, int biểu diễn số nguyên, float số thực gần đúng, str chuỗi, bool giá trị đúng/sai. Trong NumPy, dtype còn quy định kích thước và cách diễn giải dữ liệu trong bộ nhớ.

## Giải thích kỹ thuật

**Giá trị và cách lưu.** Trong Python, tên biến tham chiếu tới đối tượng; có thể gán lại tên đó cho đối tượng khác kiểu. NumPy dtype mô tả biểu diễn cố định như int32, float64, ảnh hưởng miền giá trị và độ chính xác.

Một phép toán đúng về đại số có thể tràn số nguyên cố định hoặc làm tròn số thực. Kiểm tra kiểu dữ liệu trước khi kết luận từ kết quả tính.

## Ví dụ

2+3=5 nhưng "2"+"3"="23". Hai chuỗi được nối thay vì cộng như số.

## Khi nào cần dùng?

Tránh nhầm số với chuỗi và hiểu ép kiểu, tràn số.

## Tự kiểm tra

"10" là số hay chuỗi trong Python?

<details><summary>Xem đáp án</summary>

Chuỗi. Dùng int("10") để chuyển thành số nguyên nếu dữ liệu hợp lệ.

</details>

## Thuật ngữ liên quan

- [List](./list.md)
- [Giá trị thiếu](./gia-tri-thieu.md)
