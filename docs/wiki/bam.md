---
title: "Hàm băm"
wikiTerm: bam
prev: false
next: false
---

# Hàm băm

Hàm băm chuyển dữ liệu thành một giá trị trong miền đích hữu hạn. Đầu vào khác nhau có thể trùng giá trị băm: đó là va chạm. Hàm băm cần phù hợp với mục tiêu: tra cứu, chia phân vùng hay bảo mật có các yêu cầu khác nhau.

## Giải thích kỹ thuật

**Va chạm cần xử lý.** Bảng băm phải có cách phân biệt các khóa rơi vào cùng vùng, chẳng hạn liên kết danh sách hoặc tìm vị trí khác. Một hash hữu hạn không thể đảm bảo không va chạm cho miền đầu vào vô hạn.

Hàm băm dùng để chia phân vùng không tự đáp ứng yêu cầu bảo mật. Kiểm tra mục đích, phân bố dữ liệu và chi phí tính trước khi lựa chọn.

## Ví dụ

h(x)=x mod 4: 2 và 6 đều băm thành 2. Không thể suy ra hai đầu vào bằng nhau chỉ vì hash bằng nhau.

## Khi nào cần dùng?

Hiểu bảng băm, phân vùng dữ liệu và Shuffle.

## Tự kiểm tra

Hash giống nhau có chứng minh dữ liệu giống nhau không?

<details><summary>Xem đáp án</summary>

Không, vì có thể có va chạm.

</details>

## Thuật ngữ liên quan

- [Đồ thị](./do-thi.md)
- [Đệ quy](./de-quy.md)
