---
title: "Trạng thái"
wikiTerm: trang-thai
prev: false
next: false
---

# Trạng thái

Trạng thái mô tả đủ thông tin để xác định tình huống hiện tại và các hành động hợp lệ tiếp theo. Bài toán tìm kiếm cần trạng thái đầu, tập hành động, quy tắc chuyển trạng thái và điều kiện đích. Trạng thái khác với nút tìm kiếm: nhiều đường đi có thể tới cùng một trạng thái.

## Giải thích kỹ thuật

**Đủ thông tin cho tương lai.** Hai lịch sử khác nhau có thể gom thành cùng trạng thái nếu chúng cho cùng các hành động hợp lệ, chi phí và kết quả tương lai liên quan. Nếu lịch sử làm thay đổi lựa chọn tiếp theo, phải đưa thông tin đó vào trạng thái.

Trong tìm kiếm trên đồ thị, nút thường chứa trạng thái cùng đường đi, nút cha và chi phí đã đi. So sánh trạng thái để tránh lặp khác với lưu nút để tái tạo lời giải.

## Ví dụ

Trong mê cung đơn giản, trạng thái có thể là ô (hàng, cột). Nếu có chìa khóa, trạng thái cần thêm thông tin đã nhặt chìa khóa hay chưa.

## Khi nào cần dùng?

Thiết kế bài toán tìm kiếm và tránh bỏ sót thông tin khi mô hình hóa.

## Tự kiểm tra

Chỉ lưu vị trí có đủ cho mê cung có cửa khóa không?

<details><summary>Xem đáp án</summary>

Không. Cần lưu cả trạng thái chìa khóa để biết cửa nào đi qua được.

</details>

## Thuật ngữ liên quan

- [Hàng đợi](./hang-doi.md)
- [Cây](./cay.md)
- [Đồ thị](./do-thi.md)
