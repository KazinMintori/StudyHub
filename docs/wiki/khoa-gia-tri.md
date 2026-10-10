---
title: "Cặp khóa–giá trị"
wikiTerm: khoa-gia-tri
prev: false
next: false
---

# Cặp khóa–giá trị

Cặp (key, value) gắn một định danh hoặc khóa nhóm với dữ liệu đi kèm. Khóa không nhất thiết là duy nhất trong một luồng dữ liệu: Nhiều cặp cùng khóa sẽ được gom lại trước khi xử lý. Khái niệm này khác dictionary đã gom mỗi khóa thành một giá trị.

<WikiUsage />

## Giải thích kỹ thuật

**Gom theo khóa khác ghi đè.** Luồng MapReduce có thể chứa nhiều cặp cùng khóa. Shuffle gom tất cả giá trị cho khóa đó. Không chỉ giữ giá trị cuối như khi gán nhiều lần vào cùng khóa dictionary.

Chọn khóa quyết định cách chia nhóm và lượng dữ liệu trên từng máy. Khóa phổ biến quá mức có thể làm mất cân bằng tải.

## Ví dụ

("uet",1), ("uet",1), ("hoc",1) nhóm theo khóa thành "uet": [1,1], "hoc": [1].

## Khi nào cần dùng?

Đọc Map, Shuffle và Reduce trong xử lý phân tán.

## Tự kiểm tra

Sau nhóm, hai cặp (A,2), (A,3) có danh sách giá trị nào?

<details><summary>Xem đáp án</summary>

A: [2,3].

</details>

## Thuật ngữ liên quan

- [Dictionary](./dictionary.md)
- [Hàm băm](./bam.md)
- [Tính toán phân tán](./phan-tan.md)
