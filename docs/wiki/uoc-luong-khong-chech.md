---
title: "Ước lượng không chệch"
wikiTerm: uoc-luong-khong-chech
prev: False
next: False
---

# Ước lượng không chệch

Một ước lượng không chệch có kỳ vọng bằng tham số cần ước lượng tại mọi giá trị tham số trong mô hình. Tính chất này nói về trung bình qua các mẫu lặp lại, không bảo đảm một kết quả ước lượng riêng lẻ gần tham số.

<WikiUsage />

## Giải thích kỹ thuật

Tính không chệch yêu cầu $E_\theta(T)=\theta$ với mọi giá trị tham số trong mô hình. Sai số bình phương trung bình phân rã thành phương sai cộng bình phương độ chệch.

Không chệch và nhất quán là hai tính chất khác nhau. Tính nhất quán xét một dãy ước lượng khi cỡ mẫu tăng. Một ước lượng không chệch vẫn có thể rất biến động tại cỡ mẫu đang có.

Xem [Ước lượng điểm, mômen và hợp lý cực đại](/xac-suat-thong-ke/bai-giang/37-uoc-luong-diem-momen-va-hop-ly-cuc-dai).

## Ví dụ

Với mẫu độc lập cùng phân phối có phương sai hữu hạn, trung bình mẫu là ước lượng không chệch của kỳ vọng tổng thể.

## Khi nào cần dùng?

So sánh độ chệch, phương sai và sai số bình phương trung bình của các ước lượng.

## Câu hỏi ôn lại

Ước lượng không chệch có luôn tốt hơn ước lượng chệch theo sai số bình phương trung bình không?

<details><summary>Xem đáp án</summary>

Không. Một ước lượng có độ chệch nhỏ nhưng phương sai thấp hơn có thể có sai số bình phương trung bình nhỏ hơn.

</details>

## Thuật ngữ liên quan

- [Ước lượng hợp lý cực đại](./uoc-luong-hop-ly-cuc-dai.md)
- [Thống kê đủ](./thong-ke-du.md)
- [Phương sai](./phuong-sai.md)
