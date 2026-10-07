---
title: "Hàng đợi ưu tiên"
wikiTerm: hang-doi-uu-tien
prev: false
next: false
---

# Hàng đợi ưu tiên

Hàng đợi ưu tiên lấy phần tử dựa trên khóa ưu tiên, thay vì thời điểm thêm. Với min-priority queue, khóa nhỏ nhất được lấy trước. Heap là một cách cài đặt phổ biến, cho thêm và lấy phần tử ưu tiên trong O(log n).

<WikiUsage />

## Giải thích kỹ thuật

**Heap không phải danh sách đã sắp xếp hoàn toàn.** Min-heap giữ khóa của nút cha không lớn hơn khóa của các con; do đó phần tử nhỏ nhất ở gốc. Các nút ở những nhánh khác nhau không nhất thiết có thứ tự.

Lấy phần tử ưu tiên thường tốn O(log n), đọc phần tử nhỏ nhất thường tốn O(1). Khi cùng một trạng thái có chi phí tốt hơn, thuật toán phải cập nhật khóa hoặc xử lý bản ghi cũ phù hợp.

## Ví dụ

Các nút có khóa A: 7, B: 3, C: 5. Cấu trúc min lấy B trước.

## Khi nào cần dùng?

Hiểu UCS, Dijkstra và A* khi chọn nút có chi phí nhỏ nhất.

## Tự kiểm tra

Khóa 2 được thêm sau khóa 9. Min-priority queue lấy khóa nào trước?

<details><summary>Xem đáp án</summary>

2, vì ưu tiên dựa trên giá trị khóa.

</details>

## Thuật ngữ liên quan

- [Hàng đợi](./hang-doi.md)
- [Heuristic](./heuristic.md)
- [Độ phức tạp](./do-phuc-tap.md)
