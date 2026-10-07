---
title: "Heuristic"
wikiTerm: heuristic
prev: false
next: false
---

# Heuristic

Heuristic h(n) ước lượng chi phí từ trạng thái n đến đích. Nó giúp ưu tiên hướng tìm kiếm có triển vọng. Một ước lượng admissible không vượt chi phí tối ưu thực sự còn lại; consistent còn thỏa h(n) ≤ c(n,n′) + h(n′) trên mỗi cạnh.

## Giải thích kỹ thuật

**Điều kiện tối ưu của A*.** Với h(goal)=0, admissible yêu cầu h không vượt chi phí tối ưu còn lại. Consistent yêu cầu h(n)≤c(n,n′)+h(n′) cho mỗi cạnh. Consistency giúp f không giảm dọc đường đi và cho phép đóng trạng thái thuận lợi hơn trong graph search.

Nếu chỉ có admissibility, một số cách cài đặt graph search phải cho phép mở lại trạng thái để giữ bảo đảm tối ưu. Một heuristic nhanh nhưng ước lượng quá cao có thể làm mất bảo đảm đó.

## Ví dụ

Khoảng cách đường chim bay không vượt độ dài đường bộ nếu mọi chi phí là độ dài không âm.

## Khi nào cần dùng?

Phân biệt tìm kiếm mù với Greedy và A*; đọc điều kiện tối ưu.

## Tự kiểm tra

Heuristic 8 có admissible nếu chi phí tối ưu còn lại là 5 không?

<details><summary>Xem đáp án</summary>

Không, vì 8 đã ước lượng quá cao.

</details>

## Thuật ngữ liên quan

- [Trạng thái](./trang-thai.md)
- [Hàng đợi ưu tiên](./hang-doi-uu-tien.md)
- [Đồ thị](./do-thi.md)
- [Độ phức tạp](./do-phuc-tap.md)
