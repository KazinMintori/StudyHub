---
title: "Hàng đợi"
wikiTerm: hang-doi
prev: false
next: false
---

# Hàng đợi

Trong một hàng phục vụ thông thường, người tới trước được xử lý trước. **Hàng đợi** mô tả quy tắc vào trước, ra trước (FIFO), hữu ích cho công việc chờ xử lý và thuật toán tìm kiếm theo chiều rộng.

<WikiUsage />

![Hình 1: Hàng đợi lấy A trước, còn ngăn xếp lấy C trước.](./img/atlas/queue-stack.svg)

## Giải thích kỹ thuật

Thao tác `enqueue` thêm phần tử vào cuối, còn `dequeue` lấy phần tử ở đầu. Hàng đợi cần lưu thông tin đủ để cả hai thao tác không phải di chuyển toàn bộ dãy sau mỗi lần lấy.

Trong Python, `collections.deque` hỗ trợ thêm cuối bằng `append` và lấy đầu bằng `popleft`. Dùng `list.pop(0)` cho cùng ý nghĩa thứ tự nhưng có thể phải dời các phần tử còn lại, nên chi phí khác nhau.

FIFO khác hàng đợi ưu tiên. Trong hàng đợi ưu tiên, phần tử được chọn theo khóa ưu tiên chứ không thuần theo thời điểm đến. Hai kiểu dữ liệu giải quyết hai quy tắc lập lịch khác nhau.

## Ví dụ có lời giải

Thêm A, B, C rồi phục vụ một phần tử:

```python
from collections import deque

queue = deque(["A", "B", "C"])
assert queue.popleft() == "A"
queue.append("D")
assert list(queue) == ["B", "C", "D"]
```

Trong BFS trên đồ thị không trọng số, các đỉnh cách nguồn một cạnh được đưa vào hàng đợi trước những đỉnh cách nguồn hai cạnh. Cùng với việc đánh dấu đã thăm đúng lúc, thứ tự này bảo đảm tìm khoảng cách theo số cạnh.

## Câu hỏi ôn lại

Tại sao đổi hàng đợi BFS thành ngăn xếp thường làm mất bảo đảm khoảng cách ngắn nhất?

::: details Xem lời giải
Ngăn xếp ưu tiên đỉnh mới được phát hiện, nên có thể đi sâu trên một nhánh trước khi xử lý các đỉnh gần nguồn còn lại. Thứ tự theo từng mức khoảng cách không còn được giữ.
:::

## Đọc tiếp

- [Ngăn xếp](./ngan-xep.md)
- [Hàng đợi ưu tiên](./hang-doi-uu-tien.md)
- [Đồ thị](./do-thi.md)

## Tài liệu tham khảo

- [Princeton, Algorithms, Bags, Queues, and Stacks](https://algs4.cs.princeton.edu/13stacks/).
