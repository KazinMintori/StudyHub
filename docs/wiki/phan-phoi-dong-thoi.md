---
title: "Phân phối đồng thời"
wikiTerm: phan-phoi-dong-thoi
prev: False
next: False
---

# Phân phối đồng thời

Phân phối đồng thời mô tả xác suất của nhiều biến ngẫu nhiên cùng lúc. Từ đó có thể tìm phân phối riêng của từng biến, phân phối có điều kiện và kiểm tra độc lập.

<WikiUsage />

## Giải thích kỹ thuật

Với biến rời rạc, đặt $p(x,y)=P(X=x,Y=y)$. Mọi xác suất không âm và tổng trên toàn bộ các cặp bằng 1. Cộng xác suất theo từng hàng hoặc cột cho các phân phối biên. Với mật độ liên tục, phải tích phân trên đúng miền hỗ trợ.

Hai biến độc lập khi phân phối đồng thời bằng tích hai phân phối biên, ở mọi điểm rời rạc hoặc hầu khắp nơi đối với mật độ. Chỉ kiểm tra một cặp giá trị chưa đủ.

Xem [Vector ngẫu nhiên và phân phối đồng thời](/xac-suat-thong-ke/bai-giang/31-vector-ngau-nhien-va-phan-phoi-dong-thoi).

## Ví dụ

Tung hai đồng xu cân bằng độc lập, gọi X và Y là các chỉ báo ngửa. Mỗi cặp (0, 0), (0, 1), (1, 0), (1, 1) có xác suất 1/4.

## Khi nào cần dùng?

Tính xác suất có nhiều điều kiện và mô hình hóa sự phụ thuộc.

## Câu hỏi ôn lại

Biết riêng phân phối của X và Y đã xác định phân phối đồng thời chưa?

<details><summary>Xem đáp án</summary>

Chưa. Hai phân phối biên không xác định cách X và Y phụ thuộc nhau.

</details>

## Thuật ngữ liên quan

- [Biến ngẫu nhiên](./bien-ngau-nhien.md)
- [Độc lập](./doc-lap.md)
- [Kỳ vọng có điều kiện](./ky-vong-co-dieu-kien.md)
