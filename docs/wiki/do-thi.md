---
title: "Đồ thị"
wikiTerm: do-thi
prev: false
next: false
---

# Đồ thị

Đồ thị $G = (V, E)$ gồm tập đỉnh V và tập cạnh E nối các đỉnh. Đồ thị có hướng phân biệt $u \to  v$ với $v \to  u$. Đồ thị vô hướng thì không. Trọng số là số gắn trên cạnh, thường biểu diễn khoảng cách hoặc chi phí. Đường đi là chuỗi cạnh liên tiếp.

<WikiUsage />

## Giải thích kỹ thuật

**Biểu diễn đồ thị.** Danh sách kề lưu láng giềng của từng đỉnh và thường cần $O(|V|+|E|)$ bộ nhớ. Ma trận kề dùng bảng |$V|\times |V|$, thuận tiện kiểm tra cạnh nhưng cần $O(|V|^{2})$ bộ nhớ.

BFS và DFS duyệt danh sách kề trong $O(|V|+|E|)$ nếu mỗi đỉnh chỉ được xử lý một lần. Một đường đi ngắn nhất theo số cạnh có thể khác đường có tổng trọng số nhỏ nhất.

## Ví dụ

$V = \{A, B, C\}$, cạnh $A \to  B$ giá 2 và $B \to  C$ giá 3: đường $A \to  B \to  C$ có tổng chi phí 5.

## Khi nào cần dùng?

Mô hình hóa không gian tìm kiếm, mạng liên kết và bài toán đường đi.

## Tự kiểm tra

Hai đường có cùng số cạnh có nhất thiết cùng chi phí không?

<details><summary>Xem đáp án</summary>

Không. Trọng số các cạnh có thể khác nhau.

</details>

## Thuật ngữ liên quan

- [Cây](./cay.md)
- [Trạng thái](./trang-thai.md)
- [Hàng đợi](./hang-doi.md)
- [Ngăn xếp](./ngan-xep.md)
