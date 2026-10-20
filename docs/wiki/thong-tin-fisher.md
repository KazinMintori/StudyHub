---
title: "Thông tin Fisher"
wikiTerm: thong-tin-fisher
prev: False
next: False
---

# Thông tin Fisher

Trong mô hình chính quy, thông tin Fisher là kỳ vọng bình phương đạo hàm log hợp lý theo tham số. Nó đo mức nhạy của phân phối đối với thay đổi tham số và xuất hiện trong cận phương sai Cramér–Rao.

<WikiUsage />

## Giải thích kỹ thuật

Đạo hàm của log hợp lý theo tham số được gọi là hàm điểm. Trong mô hình chính quy một tham số, kỳ vọng của hàm điểm bằng 0 và thông tin Fisher là kỳ vọng bình phương của nó. Với các quan sát độc lập, thông tin cộng lại.

Cận Cramér–Rao cho ước lượng không chệch của tham số bằng nghịch đảo thông tin của toàn mẫu, dưới các điều kiện chính quy cần thiết. Không bỏ qua điều kiện cho phép đổi thứ tự đạo hàm và tích phân hoặc điều kiện về miền hỗ trợ.

Xem [Tính đủ và hiệu quả ước lượng](/xac-suat-thong-ke/bai-giang/38-tinh-du-va-hieu-qua-uoc-luong).

## Ví dụ

Một phép thử Bernoulli với p bằng 1/2 có thông tin Fisher bằng 4 về p. Với n phép thử độc lập, thông tin bằng 4n.

## Khi nào cần dùng?

Đánh giá hiệu quả ước lượng và sai số tiệm cận khi thỏa điều kiện chính quy.

## Câu hỏi ôn lại

Có được áp dụng cận Cramér–Rao chỉ vì tính được đạo hàm không?

<details><summary>Xem đáp án</summary>

Không. Cần kiểm tra các điều kiện chính quy, đặc biệt khi miền giá trị của dữ liệu phụ thuộc tham số.

</details>

## Thuật ngữ liên quan

- [Ước lượng hợp lý cực đại](./uoc-luong-hop-ly-cuc-dai.md)
- [Phương sai](./phuong-sai.md)
- [Thống kê đủ](./thong-ke-du.md)
