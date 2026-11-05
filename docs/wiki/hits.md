---
title: "HITS"
wikiTerm: hits
prev: False
next: False
---

# HITS

Thuật toán gán hai loại điểm trên đồ thị liên kết. Điểm authority cộng đóng góp từ các hub trỏ đến trang. Điểm hub cộng điểm authority của các trang mà nó trỏ đến. Các véc tơ được chuẩn hóa trong quá trình lặp.

<WikiUsage />

## Giải thích kỹ thuật

Đặt $L_{ij}=1$ khi trang $i$ trỏ đến trang $j$. Một bước HITS tính véc tơ authority từ $L^T h$, chuẩn hóa, rồi tính véc tơ hub từ $La$ và chuẩn hóa. Với quy ước này, hàng của $L$ là trang nguồn, khác cách đánh chỉ số ma trận chuyển theo cột của PageRank.

Kết hợp hai phép cập nhật cho thấy authority gắn với $L^TL$ và hub gắn với $LL^T$. Hai véc tơ tương ứng với các véc tơ kỳ dị phải và trái của $L$. Nếu trị kỳ dị lớn nhất không đơn thì không thể khẳng định có một hướng điểm trội duy nhất độc lập khởi tạo. Ma trận toàn 0 làm bước chuẩn hóa mất nghĩa và cần được xử lý riêng.

## Ví dụ

Một danh mục liên kết có thể là hub tốt, còn trang giải thích chuyên sâu được danh mục trỏ đến có thể là authority tốt.

## Khi nào cần dùng?

Phân biệt vai trò dẫn đường với vai trò được tham khảo trong một mạng liên kết.

## Câu hỏi ôn lại

Ma trận dùng trong HITS có cần chia mỗi cột theo bậc ra như PageRank không?

<details><summary>Xem đáp án</summary>

Không. HITS cơ bản dùng ma trận kề, rồi chuẩn hóa các véc tơ điểm. Đó là mô hình khác với bước đi xác suất của PageRank.

</details>

## Thuật ngữ liên quan

- [Ma trận](./ma-tran.md)
- [Trị riêng &amp; vector riêng](./tri-rieng.md)
- [Đồ thị](./do-thi.md)
