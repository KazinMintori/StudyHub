---
title: "Ngăn xếp"
wikiTerm: ngan-xep
prev: false
next: false
---

# Ngăn xếp

Ngăn xếp lấy phần tử theo thứ tự vào sau, ra trước (LIFO). Thao tác push đặt phần tử lên đỉnh, còn pop lấy phần tử trên đỉnh ra. Ngăn xếp lời gọi lưu các hàm đang chờ kết quả, nhờ đó giúp ta theo dõi hoạt động của đệ quy.

<WikiUsage />

## Giải thích kỹ thuật

**Ngăn xếp lời gọi.** Khi hàm A gọi B, thông tin để tiếp tục A được giữ lại. B hoàn tất trước khi A tiếp tục, phù hợp thứ tự LIFO. Với đệ quy, mỗi lời gọi thường tạo một khung ngăn xếp mới.

Ngăn xếp trừu tượng không tự bảo đảm chương trình kết thúc. Điều kiện dừng của thuật toán phải được kiểm tra riêng.

## Ví dụ

Đặt A, B, C lần lượt lên ngăn xếp: Lấy ra C trước, rồi B, A.

## Khi nào cần dùng?

Hiểu DFS, quay lui, lời gọi hàm và kiểm tra dấu ngoặc.

## Tự kiểm tra

Sau push(A), push(B), pop(), đỉnh còn lại là gì?

<details><summary>Xem đáp án</summary>

A.

</details>

## Thuật ngữ liên quan

- [Hàng đợi](./hang-doi.md)
- [Đệ quy](./de-quy.md)
- [Cây](./cay.md)
