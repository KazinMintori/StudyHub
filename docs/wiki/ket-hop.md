---
title: "Tính kết hợp & giao hoán"
wikiTerm: ket-hop
prev: false
next: false
---

# Tính kết hợp & giao hoán

Phép toán kết hợp thỏa (a⊙b)⊙c=a⊙(b⊙c), cho phép đổi cách nhóm. Giao hoán thỏa a⊙b=b⊙a, cho phép đổi thứ tự. Hai tính chất khác nhau. Trong số thực tính bằng máy, sai số làm phép cộng không luôn kết hợp chính xác.

## Giải thích kỹ thuật

**Gom cục bộ cần giữ đủ thông tin.** Tính kết hợp cho đổi dấu ngoặc; giao hoán cho đổi thứ tự. Nối chuỗi kết hợp nhưng không giao hoán. Khi tính trên máy, làm tròn số thực có thể phá kết hợp chính xác của phép cộng.

Muốn tính trung bình phân tán, gửi cặp (tổng,số lượng), cộng hai thành phần rồi chia ở cuối. Trung bình các trung bình không giữ đủ thông tin nếu kích thước nhóm khác nhau.

## Ví dụ

Cộng số nguyên kết hợp và giao hoán; nối chuỗi kết hợp nhưng không giao hoán: "ab" khác "ba".

## Khi nào cần dùng?

Hiểu khi nào có thể gom cục bộ kết quả và thiết kế Combine.

## Tự kiểm tra

Lấy trung bình hai trung bình có luôn cho trung bình chung không?

<details><summary>Xem đáp án</summary>

Không. Cần tính cả số phần tử của mỗi nhóm để lấy trung bình có trọng số.

</details>

## Thuật ngữ liên quan

- [Tính toán phân tán](./phan-tan.md)
- [Hàm trong lập trình](./ham-lap-trinh.md)
- [Kỳ vọng](./ky-vong.md)
