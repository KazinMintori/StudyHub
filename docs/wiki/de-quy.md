---
title: "Đệ quy"
wikiTerm: de-quy
prev: false
next: false
---

# Đệ quy

Hàm đệ quy gọi lại chính nó trên bài toán nhỏ hơn. Cần có điều kiện dừng và mỗi lần gọi phải tiến về điều kiện đó. Các lời gọi chưa hoàn thành nằm trên ngăn xếp, vì vậy đệ quy quá sâu có thể vượt giới hạn ngăn xếp.

<WikiUsage />

## Giải thích kỹ thuật

**Hai yêu cầu kết thúc.** Có ít nhất một trường hợp cơ sở, và mọi nhánh lời gọi phải tiến về trường hợp cơ sở. Một hàm có câu lệnh dừng nhưng nhánh khác gọi lại với cùng tham số vẫn có thể không kết thúc.

Để phân tích, viết quan hệ truy hồi của số bước và độ sâu ngăn xếp. Chứng minh bằng quy nạp thường đi cùng cấu trúc đệ quy.

## Ví dụ

factorial(n) = n × factorial($n-1$), với factorial(0) = 1. Từ $n = 3$, ta lần lượt về 2, 1, 0.

## Khi nào cần dùng?

Hiểu DFS, chia để trị, quay lui và chứng minh bằng quy nạp.

## Tự kiểm tra

Nếu hàm cứ gọi lại với cùng n và không dừng, chuyện gì xảy ra?

<details><summary>Xem đáp án</summary>

Lời gọi tiếp tục tăng tới khi vượt giới hạn ngăn xếp hoặc tài nguyên.

</details>

## Thuật ngữ liên quan

- [Ngăn xếp](./ngan-xep.md)
- [Quy nạp toán học](./quy-nap.md)
- [Cây](./cay.md)
- [Độ phức tạp](./do-phuc-tap.md)
