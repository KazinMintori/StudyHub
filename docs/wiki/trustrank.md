---
title: "TrustRank"
wikiTerm: trustrank
prev: False
next: False
---

# TrustRank

Biến thể PageRank cá nhân hóa với phân phối nhảy đặt trên các trang hạt giống được đánh giá đáng tin. Nó lan truyền điểm qua cạnh theo giả thiết các liên kết từ trang đáng tin cung cấp tín hiệu hữu ích. Đây là tín hiệu xếp hạng, không phải một phép kiểm chứng nội dung.

<WikiUsage />

## Giải thích kỹ thuật

Tập hạt giống và trọng số nhảy là dữ kiện đầu vào của mô hình. Chúng cần được đánh giá độc lập với kết quả xếp hạng. Điểm TrustRank thấp có thể phản ánh khoảng cách đến hạt giống hoặc sự thiếu bao phủ, nên không đủ để kết luận một trang là rác.

Khi so sánh PageRank thông thường $r_i>0$ và TrustRank $t_i$, chỉ số spam mass là $1-t_i/r_i$. Chỉ số này có thể âm khi $t_i>r_i$. Nó không phải xác suất nhãn rác. Muốn diễn giải phép so sánh, phải ghi rõ đồ thị, hệ số theo liên kết, chuẩn hóa và cách xử lý nút cụt của hai lần tính.

## Ví dụ

Một trang ngoài tập hạt giống vẫn có điểm TrustRank dương nếu nhận liên kết từ vùng có điểm.

## Khi nào cần dùng?

Phân tích và hạn chế tác động của thao túng liên kết.

## Câu hỏi ôn lại

Một trang có TrustRank thấp có chắc chắn là trang rác không?

<details><summary>Xem đáp án</summary>

Không. Trang có thể chưa được nối tốt với tập hạt giống, hoặc tập hạt giống chưa bao quát chủ đề của trang.

</details>

## Thuật ngữ liên quan

- [PageRank cá nhân hóa](./pagerank-ca-nhan-hoa.md)
- [HITS](./hits.md)
