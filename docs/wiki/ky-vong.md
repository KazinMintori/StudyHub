---
title: "Kỳ vọng"
wikiTerm: ky-vong
prev: false
next: false
---

# Kỳ vọng

Kỳ vọng là trung bình có trọng số theo xác suất. Nếu $X$ nhận hữu hạn giá trị $x_1,\ldots,x_k$ với xác suất $p_i=P(X=x_i)$, thì $\mathbb E[X]=x_1p_1+\cdots+x_kp_k$. Viết gọn, $\mathbb E[X]=\sum_{i=1}^k x_i p_i$: $i$ chạy qua các giá trị có thể nhận. Với vô hạn đếm được, cần kiểm tra điều kiện tồn tại kỳ vọng. Đây là trung bình dài hạn khi điều kiện hội tụ phù hợp. Nó không nhất thiết là kết quả của một lần thử. Kỳ vọng của tổng bằng tổng kỳ vọng nếu các kỳ vọng tồn tại.

<WikiUsage />

## Giải thích kỹ thuật

**Tồn tại và tuyến tính.** Kỳ vọng cần được kiểm tra tồn tại theo mô hình đang dùng. Với biến liên tục có mật độ, $\mathbb E[X]=\int x f(x)\,dx$ khi tích phân thích hợp tồn tại. Một phân phối có thể không có kỳ vọng hữu hạn.

$\mathbb E[aX+bY]=aE[X]+bE[Y]$ không cần X,Y độc lập khi các kỳ vọng tồn tại. Nhưng E[XY]=E[X]E[Y] thường cần thêm điều kiện, như độc lập và khả tích thích hợp.

## Ví dụ

Xúc xắc cân bằng có $\mathbb E[X]=(1+2+3+4+5+6)/6=3.5$ dù không có mặt 3.5.

## Khi nào cần dùng?

Hiểu trung bình, chi phí kỳ vọng và mục tiêu thống kê.

## Tự kiểm tra

X bằng 0 hoặc 10 với xác suất $\frac{1}{2}$ mỗi giá trị. E[X] là gì?

<details><summary>Xem đáp án</summary>

5.

</details>

## Thuật ngữ liên quan

- [Biến ngẫu nhiên](./bien-ngau-nhien.md)
- [Phương sai](./phuong-sai.md)
- [Tích phân](./tich-phan.md)
