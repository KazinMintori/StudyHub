---
title: "Phân phối hậu nghiệm"
wikiTerm: phan-phoi-hau-nghiem
prev: False
next: False
---

# Phân phối hậu nghiệm

Phân phối hậu nghiệm là phân phối của tham số sau khi điều kiện hóa theo dữ liệu trong mô hình Bayes. Nó kết hợp tiên nghiệm và hàm hợp lý, sau đó chuẩn hóa để tổng xác suất hoặc tích phân mật độ bằng 1.

<WikiUsage />

## Giải thích kỹ thuật

Nhân hàm hợp lý với mật độ tiên nghiệm cho một hàm chưa chuẩn hóa. Tích phân hàm đó trên miền tham số là hằng số chuẩn hóa, cần dương và hữu hạn. Với tham số rời rạc, thay tích phân bằng tổng trên các giá trị tham số.

Phân phối dự đoán lấy trung bình xác suất có điều kiện của dữ liệu tương lai theo hậu nghiệm. Thay tham số bằng trung bình hậu nghiệm không cho cùng kết quả trong mọi câu hỏi. Đặc biệt, kỳ vọng bình phương còn chứa phương sai của tham số.

Xem [Suy luận Bayes và phân phối dự đoán](/xac-suat-thong-ke/bai-giang/45-suy-luan-bayes-va-du-doan).

## Ví dụ

Tiên nghiệm beta với hai tham số bằng 1, cùng ba thành công trong bốn phép thử Bernoulli độc lập khi biết tham số, cho hậu nghiệm beta với hai tham số 4 và 2.

## Khi nào cần dùng?

Tính xác suất của tham số sau dữ liệu, khoảng xác suất hậu nghiệm và phân phối dự đoán.

## Câu hỏi ôn lại

Với tham số liên tục, mật độ hậu nghiệm tại một điểm có phải xác suất tham số bằng đúng điểm đó không?

<details><summary>Xem đáp án</summary>

Không. Xác suất trên một miền được tính bằng tích phân mật độ trên miền đó.

</details>

## Thuật ngữ liên quan

- [Phân phối tiên nghiệm](./phan-phoi-tien-nghiem.md)
- [Likelihood](./likelihood.md)
- [Kỳ vọng có điều kiện](./ky-vong-co-dieu-kien.md)
