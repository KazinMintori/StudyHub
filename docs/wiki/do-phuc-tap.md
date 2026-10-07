---
title: "Độ phức tạp"
wikiTerm: do-phuc-tap
prev: false
next: false
---

# Độ phức tạp

Độ phức tạp mô tả thời gian hoặc bộ nhớ tăng thế nào theo kích thước đầu vào n. O(f(n)) là chặn trên tiệm cận, bỏ qua hệ số hằng và các hạng nhỏ hơn khi n đủ lớn. Cần nêu đang xét trường hợp tốt, trung bình hay xấu nhất; ký hiệu O tự nó không nói điều đó.

## Giải thích kỹ thuật

**Big-O, Θ và Ω.** O là chặn trên tiệm cận; Ω là chặn dưới; Θ là chặn trên và dưới cùng bậc. Một thuật toán Θ(n) cũng thuộc O(n²), nhưng O(n²) là mô tả kém chặt hơn.

Phải phân biệt thời gian, bộ nhớ và mô hình tính toán. O(n) không tự nghĩa là “trường hợp xấu nhất”: trường hợp đang xét cần được nêu riêng.

## Ví dụ

Duyệt n phần tử tốn O(n); hai vòng lặp lồng nhau đều chạy n lần thường tốn O(n²).

## Khi nào cần dùng?

So sánh giải thuật và dự đoán tác động khi dữ liệu tăng.

## Tự kiểm tra

Tăng n gấp đôi, số bước tỷ lệ n² tăng khoảng bao nhiêu lần?

<details><summary>Xem đáp án</summary>

4 lần.

</details>

## Thuật ngữ liên quan

- [Heuristic](./heuristic.md)
- [Hàng đợi ưu tiên](./hang-doi-uu-tien.md)
- [Đồ thị](./do-thi.md)
