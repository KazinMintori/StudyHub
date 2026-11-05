---
title: "PageRank cá nhân hóa"
wikiTerm: pagerank-ca-nhan-hoa
prev: False
next: False
---

# PageRank cá nhân hóa

Phân phối điểm bất động của bước đi trên đồ thị có nhảy lại theo một phân phối ưu tiên. Phải nêu rõ xác suất theo liên kết và cách phân phối lại điểm ở nút cụt. Điểm đo tầm quan trọng theo mô hình này, không tự chứng nhận nội dung đúng.

<WikiUsage />

## Giải thích kỹ thuật

Giữ quy ước cột nguồn. Gọi $S$ là ma trận chuyển không âm có tổng mỗi cột bằng 1, sau khi đã xử lý nút cụt. Gọi $v$ là véc tơ xác suất nhảy và $0\le\beta<1$. Phép cập nhật là $F(x)=\beta Sx+(1-\beta)v$.

Với hai véc tơ, khoảng cách theo chuẩn tổng trị tuyệt đối sau cập nhật không vượt quá $\beta$ lần khoảng cách trước cập nhật. Do đó có duy nhất điểm bất động, kể cả khi một số phần tử của $v$ bằng 0. Điều này không có nghĩa mọi trang nhận điểm dương hoặc chuỗi Markov bất khả quy.

Nếu giữ nguyên $S$ và $\beta$, nghiệm phụ thuộc tuyến tính vào $v$. Có thể trộn các véc tơ điểm chủ đề bằng cùng trọng số dùng để trộn phân phối nhảy. Nếu quy tắc nút cụt cũng thay theo $v$, cần xét lại điều kiện giữ nguyên $S$.

## Ví dụ

Nếu bước nhảy chỉ đến trang A thì các trang nhận được điểm qua những đường đi xuất phát từ A. Trang không thể đến được có thể nhận điểm bằng 0.

## Khi nào cần dùng?

Xếp hạng theo chủ đề hoặc theo tập trang khởi đầu.

## Câu hỏi ôn lại

Phân phối nhảy chỉ hỗ trợ một trang có làm mất tính duy nhất của PageRank khi hệ số theo liên kết nhỏ hơn 1 không?

<details><summary>Xem đáp án</summary>

Không. Với ma trận chuyển đã xử lý nút cụt và giữ cố định, phép cập nhật vẫn là ánh xạ co.

</details>

## Thuật ngữ liên quan

- [TrustRank](./trustrank.md)
- [Đồ thị](./do-thi.md)
- [Ma trận](./ma-tran.md)
