---
title: "Phân phối tiên nghiệm"
wikiTerm: phan-phoi-tien-nghiem
prev: False
next: False
---

# Phân phối tiên nghiệm

Trong mô hình Bayes, phân phối tiên nghiệm mô tả thông tin về tham số trước dữ kiện đang xét. Nó phải đi cùng mô hình và cách lựa chọn được giải thích rõ.

<WikiUsage />

## Giải thích kỹ thuật

Tiên nghiệm được phát biểu trước dữ kiện đang đưa vào hàm hợp lý. Nó có thể biểu diễn thông tin từ nghiên cứu trước hoặc lựa chọn mô hình khi thông tin còn ít. Cần kiểm tra độ nhạy của kết luận theo những tiên nghiệm hợp lý khác nhau.

Nếu phân phối tiên nghiệm và hậu nghiệm cùng thuộc một họ, ta có tính liên hợp đối với mô hình lấy mẫu đang xét. Beta liên hợp với mẫu Bernoulli, còn gamma liên hợp với số đếm Poisson theo quy ước hình dạng và tốc độ.

Xem [Suy luận Bayes và phân phối dự đoán](/xac-suat-thong-ke/bai-giang/45-suy-luan-bayes-va-du-doan).

## Ví dụ

Một tiên nghiệm đều cho xác suất thành công trên khoảng từ 0 đến 1 gán cùng xác suất cho các đoạn con cùng độ dài.

## Khi nào cần dùng?

Phát biểu thông tin ban đầu trước khi cập nhật Bayes và kiểm tra độ nhạy của kết luận.

## Câu hỏi ôn lại

Tiên nghiệm có nhất thiết là dữ liệu giả lập thêm vào mẫu không?

<details><summary>Xem đáp án</summary>

Không. Tiên nghiệm là một thành phần của mô hình xác suất, không phải những quan sát mới.

</details>

## Thuật ngữ liên quan

- [Phân phối hậu nghiệm](./phan-phoi-hau-nghiem.md)
- [Likelihood](./likelihood.md)
- [Xác suất có điều kiện](./xac-suat-co-dieu-kien.md)
