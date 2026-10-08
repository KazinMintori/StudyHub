---
title: "Quy hoạch động và phương trình Bellman"
wikiTerm: quy-hoach-dong
prev: false
next: false
---

# Quy hoạch động và phương trình Bellman

Quy hoạch động tách quyết định hiện tại khỏi phần bài toán còn lại. Hàm giá trị V(s) lưu kết quả tốt nhất từ trạng thái s, còn phương trình Bellman so sánh chi phí hiện tại cộng với giá trị của trạng thái kế tiếp.

<WikiUsage />

## Giải thích kỹ thuật

**Nguyên lý tối ưu và trạng thái đủ.** Với thời hạn hữu hạn tất định, $V_t(s)=\min_a\{c_t(s,a)+V_{t+1}(T_t(s,a))\}$. Nếu phần còn lại của một phương án tối ưu không tối ưu từ trạng thái kế tiếp, thay nó bằng phần tốt hơn sẽ giảm tổng chi phí, tạo mâu thuẫn.

Lập luận phụ thuộc trạng thái chứa đủ thông tin quyết định các lựa chọn và chi phí tương lai. Với bài ngẫu nhiên, số hạng tương lai thường trở thành kỳ vọng có điều kiện. Với đồ thị có chu trình, không thể tự dùng một lượt tính ngược theo thứ tự DAG. Nguồn: Convex Optimization, §8.7 cho một đệ quy đường dài nhất và biến thể đường ngắn nhất trong Notes được tự biên soạn.

## Ví dụ

Nếu từ A đi thẳng tới đích tốn 5, còn đi $A\to B$ tốn 2 và từ B tới đích tốn 1, thì $V(A)=\min(5,2+1)=3$.

## Khi nào cần dùng?

Giải chuỗi quyết định, đường đi trên DAG và bài toán điều khiển hữu hạn.

## Tự kiểm tra

Vì sao trạng thái phải chứa đủ thông tin cho tương lai?

<details><summary>Xem đáp án</summary>

Vì nếu hai lịch sử có cùng nhãn trạng thái nhưng cho lựa chọn tương lai khác nhau, một giá trị V chung không còn đúng.

</details>

## Thuật ngữ liên quan

- [Đồ thị](./do-thi.md)
- [Trạng thái](./trang-thai.md)
- [Nghiệm cơ sở của quy hoạch tuyến tính](./nghiem-co-so.md)
