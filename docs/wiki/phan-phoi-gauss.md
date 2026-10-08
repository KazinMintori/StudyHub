---
title: "Phân phối Gauss"
wikiTerm: phan-phoi-gauss
prev: false
next: false
---

# Phân phối Gauss

Phân phối Gauss một biến được xác định bởi kỳ vọng $\mu$ và phương sai $\sigma ^{2}>0$. Mật độ có dạng chuông quanh $\mu$, còn $\sigma$ quyết định thang phân tán. Mật độ tại một điểm không phải xác suất của đúng điểm đó.

<WikiUsage />

## Giải thích kỹ thuật

**Mật độ một và nhiều chiều.** Với $Z\sim\mathcal N(\mu,\sigma^2)$,

$$p(z)=\frac1{\sqrt{2\pi\sigma^2}}\exp\left[-\frac{(z-\mu)^2}{2\sigma^2}\right],\qquad\sigma^2>0.$$

Trong nhiều chiều, vector Gauss dùng kỳ vọng $\mu$ và ma trận hiệp phương sai $\Sigma\succ0$. Trường hợp $\Sigma=\sigma^2I$ mô tả các thành phần độc lập cùng phương sai. Nếu $\Sigma$ suy biến, công thức mật độ thông thường trên toàn $\mathbb R^m$ không áp dụng trực tiếp. Nguồn: Convex Optimization, §7.1.

## Ví dụ

Z∼N(0,1) có kỳ vọng 0 và phương sai 1. Xác suất trên một khoảng được tính bằng tích phân mật độ.

## Khi nào cần dùng?

Mô hình hóa nhiễu, khởi tạo trọng số và suy ra loss bình phương.

## Tự kiểm tra

Với biến Gauss liên tục, $P(Z=0)$ có bằng mật độ p(0) không?

<details><summary>Xem đáp án</summary>

Không. Xác suất tại một điểm bằng 0, còn p(0) là giá trị mật độ.

</details>

## Thuật ngữ liên quan

- [Kỳ vọng](./ky-vong.md)
- [Phương sai](./phuong-sai.md)
- [Ma trận hiệp phương sai](./ma-tran-hiep-phuong-sai.md)
- [Likelihood](./likelihood.md)
