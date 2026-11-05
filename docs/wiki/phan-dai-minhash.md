---
title: "Phân dải MinHash"
wikiTerm: phan-dai-minhash
prev: False
next: False
---

# Phân dải MinHash

Chia chữ ký thành các dải có cùng số hàng. Hai chữ ký khớp một dải khi mọi hàng trong dải đó bằng nhau. Cặp được tạo ứng viên nếu khớp ít nhất một dải. Mô hình xác suất chuẩn giả sử các hàng độc lập và không có va chạm phụ của bộ băm dải.

<WikiUsage />

## Giải thích kỹ thuật

Gọi $b$ là số dải và $r$ là số hàng trong một dải. Với các hàng MinHash độc lập và hai tập có Jaccard $s$, xác suất một dải khớp là $s^r$. Xác suất thành ứng viên là $p(s)=1-(1-s^r)^b$.

Mốc xác suất bằng một nửa là nghiệm của $p(s)=1/2$. Nó không trùng với mốc gần đúng $b^{-1/r}$. Khi tăng $b$ mà giữ $r$, xác suất giữ cặp tăng nhưng chữ ký cũng dài thêm. Khi giữ tổng số hàng, phải xét đồng thời thay đổi của cả hai tham số.

## Ví dụ

Chữ ký 100 hàng có thể chia thành 20 dải, mỗi dải 5 hàng, hoặc 10 dải, mỗi dải 10 hàng. Hai cách cho xác suất ứng viên khác nhau.

## Khi nào cần dùng?

Điều chỉnh mức đánh đổi giữa số ứng viên và nguy cơ bỏ sót.

## Câu hỏi ôn lại

Tăng số hàng mỗi dải và giữ số dải cố định làm xác suất ứng viên tăng hay giảm?

<details><summary>Xem đáp án</summary>

Nó giảm hoặc giữ nguyên vì việc khớp toàn bộ một dải đòi hỏi nhiều điều kiện đồng thời hơn.

</details>

## Thuật ngữ liên quan

- [MinHash](./minhash.md)
- [Băm nhạy cảm cục bộ](./lsh.md)
- [Độc lập](./doc-lap.md)
