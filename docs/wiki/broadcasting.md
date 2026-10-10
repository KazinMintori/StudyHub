---
title: "Broadcasting"
wikiTerm: broadcasting
prev: false
next: false
---

# Broadcasting

Broadcasting cho phép NumPy thực hiện phép toán trên các mảng có kích thước tương thích mà không cần viết vòng lặp mở rộng. So kích thước từ trục cuối: Mỗi cặp phải bằng nhau hoặc có một bên bằng 1. Shape là bộ số mô tả kích thước theo từng trục.

<WikiUsage />

## Giải thích kỹ thuật

**Quy tắc tương thích.** So các kích thước từ trục cuối. Hai trục tương thích khi bằng nhau hoặc có một bên bằng 1. Trục thiếu được coi như kích thước 1.

(3,2)+(2,) cho (3,2). (3,2)+(3,) không tương thích. Muốn cộng một giá trị riêng cho từng hàng, đổi vector shape (3,) thành (3,1). Việc mở rộng là quy tắc tính toán, không nhất thiết sao chép cả dữ liệu đầu vào.

## Ví dụ

Mảng shape (3,2) cộng vector shape (2,) sẽ cộng vector đó vào từng hàng. Shape (3,) không tương thích trực tiếp với (3,2).

## Khi nào cần dùng?

Tránh cộng nhầm theo hàng/cột và đọc các phép biến đổi nhiều chiều.

## Tự kiểm tra

(4,3) có cộng được với (1,3) bằng broadcasting không?

<details><summary>Xem đáp án</summary>

Có. Trục đầu 1 được mở rộng thành 4.

</details>

## Thuật ngữ liên quan

- [Mảng](./mang.md)
- [Vector hóa](./vector-hoa.md)
- [Ma trận](./ma-tran.md)
- [Chỉ mục &amp; lát cắt](./chi-muc.md)
