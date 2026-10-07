---
title: "Hàng đợi"
wikiTerm: hang-doi
prev: false
next: false
---

# Hàng đợi

Hàng đợi lấy phần tử theo thứ tự vào trước, ra trước (FIFO). Thêm ở cuối và lấy ở đầu. Trong BFS, hàng đợi giữ các nút chờ duyệt, nên các nút ở tầng hiện tại được xử lý trước tầng tiếp theo.

<WikiUsage />

## Giải thích kỹ thuật

**Chi phí cài đặt.** Hàng đợi có thể dùng danh sách liên kết hoặc vùng nhớ vòng. Trong mô hình thích hợp, thêm cuối và lấy đầu đều tốn O(1). Xóa phần tử đầu của một mảng bằng cách dịch toàn bộ phần còn lại có thể tốn O(n).

Đây là lý do cần phân biệt cấu trúc trừu tượng hàng đợi với một cách cài đặt cụ thể. Quy tắc FIFO quyết định thứ tự duyệt BFS.

## Ví dụ

Thêm A, rồi B, rồi C: thứ tự lấy ra là A, B, C.

## Khi nào cần dùng?

Hiểu BFS, xử lý tác vụ và dữ liệu theo thứ tự đến.

## Tự kiểm tra

Thêm 2, 5, 8 vào hàng đợi. Phần tử được lấy đầu tiên là gì?

<details><summary>Xem đáp án</summary>

2.

</details>

## Thuật ngữ liên quan

- [Ngăn xếp](./ngan-xep.md)
- [Đồ thị](./do-thi.md)
- [Trạng thái](./trang-thai.md)
