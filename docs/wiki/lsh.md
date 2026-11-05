---
title: "Băm nhạy cảm cục bộ"
wikiTerm: lsh
prev: False
next: False
---

# Băm nhạy cảm cục bộ

Họ hàm băm ngẫu nhiên có xác suất va chạm cao hơn cho các đối tượng gần nhau theo một độ đo đã chọn. Nó giúp tìm ứng viên để xác minh tiếp, với khả năng có ứng viên sai và bỏ sót. Họ băm phải phù hợp với độ đo.

<WikiUsage />

## Giải thích kỹ thuật

Họ băm phải được chọn theo độ đo của đối tượng. MinHash có xác suất va chạm bằng Jaccard cho tập khác rỗng. Băm bằng dấu của tích vô hướng với một hướng ngẫu nhiên đẳng hướng cho các véc tơ khác 0 có xác suất va chạm phụ thuộc góc, không trực tiếp bằng Jaccard.

LSH là bước lọc ứng viên. Bước xác minh bằng độ đo chính xác loại được ứng viên không đạt ngưỡng, nhưng không khôi phục được các cặp đã bị bộ lọc bỏ sót. Khi có một thùng băm rất lớn, số cặp trong thùng vẫn có thể tăng theo bình phương kích thước thùng.

## Ví dụ

Trong LSH cho chữ ký MinHash, hai tài liệu là ứng viên nếu trùng toàn bộ các hàng trong ít nhất một dải.

## Khi nào cần dùng?

Giảm số cặp cần so sánh chính xác trong bài toán tìm tương đồng.

## Câu hỏi ôn lại

Mốc gần đúng của đường cong LSH có phải ngưỡng bảo đảm mọi cặp phía trên đều được giữ không?

<details><summary>Xem đáp án</summary>

Không. Xác suất thay đổi liên tục theo độ tương đồng. Ngưỡng quyết định kết quả được áp dụng riêng ở bước xác minh.

</details>

## Thuật ngữ liên quan

- [MinHash](./minhash.md)
- [Phân dải MinHash](./phan-dai-minhash.md)
- [Hàm băm](./bam.md)
