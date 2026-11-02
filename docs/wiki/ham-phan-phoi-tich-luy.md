---
title: "Hàm phân phối tích lũy"
wikiTerm: ham-phan-phoi-tich-luy
prev: False
next: False
---

# Hàm phân phối tích lũy

Hàm phân phối tích lũy tại một ngưỡng cho xác suất biến ngẫu nhiên không vượt quá ngưỡng đó. Theo quy ước dùng dấu nhỏ hơn hoặc bằng, hàm liên tục phải. Quy ước dấu nhỏ hơn nghiêm ngặt tạo hàm liên tục trái và khác tại các điểm có khối lượng dương.

<WikiUsage />

## Giải thích kỹ thuật

Đặt $F(x)=P(X\le x)$ và $G(x)=P(X<x)$. Hai hàm liên hệ bởi $G(x)=F(x^-)$ và $F(x)=G(x^+)$. Với $a<b$:

$$
\begin{aligned}
P(a<X\le b)&=F(b)-F(a),\\
P(a\le X<b)&=G(b)-G(a).
\end{aligned}
$$

Xác suất tại điểm là độ cao bước nhảy. Hai quy ước có cùng giới hạn tại vô cùng và chỉ khác tại những điểm có khối lượng dương. Xem [Biến ngẫu nhiên](/xac-suat-thong-ke/bai-giang/12-bien-ngau-nhien).

## Ví dụ

Với các xác suất 0,2, 0,5, 0,3 tại 0, 1, 2, hàm dùng dấu nhỏ hơn hoặc bằng có giá trị 0,7 tại ngưỡng 1. Hàm dùng dấu nhỏ hơn nghiêm ngặt có giá trị 0,2 tại đó.

## Khi nào cần dùng?

Tính xác suất trên các khoảng, xác suất tại điểm và chuyển đổi giữa các quy ước đầu mút.

## Câu hỏi ôn lại

Hai quy ước có khác nhau với biến có mật độ không?

<details><summary>Xem đáp án</summary>

Không. Xác suất tại một điểm bằng 0 nên hai hàm trùng nhau.

</details>

## Thuật ngữ liên quan

- [Biến ngẫu nhiên](./bien-ngau-nhien.md)
- [Phân vị chuẩn tắc](./phan-vi-chuan-tac.md)
