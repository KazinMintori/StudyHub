---
title: "MinHash"
wikiTerm: minhash
prev: False
next: False
---

# MinHash

Với một hoán vị của vũ trụ phần tử, MinHash của tập khác rỗng là phần tử đầu tiên của tập theo thứ tự đó. Nếu hoán vị được chọn đều ngẫu nhiên và dùng chung cho hai tập, xác suất hai MinHash trùng nhau đúng bằng độ tương đồng Jaccard.

<WikiUsage />

## Giải thích kỹ thuật

Phần tử nhỏ nhất của $A\cup B$ theo một hoán vị ngẫu nhiên đều có khả năng như nhau là bất kỳ phần tử nào trong hợp. Hai MinHash bằng nhau đúng khi phần tử này thuộc giao. Vì thế xác suất va chạm bằng kích thước giao chia kích thước hợp.

Với $k$ hoán vị độc lập, gọi $I_i$ bằng 1 khi hàng thứ $i$ trùng nhau và bằng 0 nếu không. Trung bình $(I_1+I_2+\cdots+I_k)/k$ là ước lượng không chệch của Jaccard. Nếu $s$ là Jaccard thật, phương sai của trung bình là $s(1-s)/k$. Một chữ ký hữu hạn vẫn có sai số.

## Ví dụ

Hai tập có Jaccard bằng 3/5 sẽ cho MinHash trùng nhau với xác suất 3/5 trong mô hình hoán vị ngẫu nhiên đều.

## Khi nào cần dùng?

Nén tập thành chữ ký để ước lượng Jaccard và tạo ứng viên tìm kiếm tương đồng.

## Câu hỏi ôn lại

Một hàm băm bất kỳ có tự động bảo đảm định lý MinHash chính xác không?

<details><summary>Xem đáp án</summary>

Không. Định lý phát biểu cho hoán vị ngẫu nhiên đều. Các họ băm thực dụng cần được xem xét về sai lệch, tính độc lập và va chạm.

</details>

## Thuật ngữ liên quan

- [Độ tương đồng Jaccard](./jaccard.md)
- [Độc lập](./doc-lap.md)
- [Phân dải MinHash](./phan-dai-minhash.md)
