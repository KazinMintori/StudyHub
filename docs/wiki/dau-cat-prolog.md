---
title: "Dấu cắt trong Prolog"
---

# Dấu cắt trong Prolog

## Giải thích kỹ thuật

Mục tiêu đặc biệt viết bằng dấu chấm than. Khi được thực thi, nó bỏ các lựa chọn thay thế của lời gọi vị từ hiện hành và các lựa chọn đã sinh bởi mục tiêu bên trái trong mệnh đề đó.

Trong p(X) :- a(C), !, b(C,X), dấu cắt bỏ các cách chọn C khác của a/1. Các đáp án tiếp theo của b/2 vẫn có thể được tìm.

Dấu cắt có xóa lựa chọn của mọi lời gọi tổ tiên không?

Không. Phạm vi được xác định bởi lời gọi vị từ chứa dấu cắt.

## Khi nào dùng

Đọc phạm vi quay lui và kiểm tra một dấu cắt có làm thay đổi tập câu trả lời không.
