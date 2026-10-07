---
title: "Cây"
wikiTerm: cay
prev: false
next: false
---

# Cây

Cây là đồ thị liên thông không có chu trình trong dạng vô hướng. Khi chọn một gốc, mỗi nút khác gốc có một nút cha; nút không có con gọi là lá. Độ sâu là số cạnh từ gốc tới nút. Cây nhị phân có tối đa hai con ở mỗi nút.

## Giải thích kỹ thuật

**Chiều cao và thứ tự.** Chiều cao đo đường dài nhất từ gốc tới lá theo quy ước đã chọn. Với cây nhị phân tìm kiếm có khóa phân biệt, mọi khóa bên trái nhỏ hơn khóa gốc và bên phải lớn hơn. Quy tắc này phải đúng ở mọi cây con.

Cây nhị phân thông thường không bắt buộc có quy tắc tìm kiếm. Cây lệch có chiều cao gần n, nên các thao tác phụ thuộc chiều cao có thể tốn O(n).

## Ví dụ

Gốc A có hai con B, C; B có con D. D là lá và có độ sâu 2.

## Khi nào cần dùng?

Đọc cây tìm kiếm, đệ quy, cây quyết định và cây nhị phân.

## Tự kiểm tra

Nút gốc có độ sâu bao nhiêu khi đếm theo số cạnh?

<details><summary>Xem đáp án</summary>

0.

</details>

## Thuật ngữ liên quan

- [Trạng thái](./trang-thai.md)
- [Đồ thị](./do-thi.md)
