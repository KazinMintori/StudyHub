---
title: "Ellipsoid"
wikiTerm: ellipsoid
prev: false
next: false
---

# Ellipsoid

Ellipsoid là tập $\{x : (x - x_c)^T P^{-1} (x - x_c) \le 1\}$ với P đối xứng xác định dương. Các bán trục nằm theo vector riêng của P và có độ dài bằng căn bậc hai của trị riêng tương ứng.

<WikiUsage />

## Giải thích kỹ thuật

**Hai cách biểu diễn.** Ngoài dạng dùng $P$, ellipsoid còn là ảnh affine của quả cầu đơn vị, $\{x_c + Au : \|u\|_2 \le 1\}$ với $A = P^{1/2}$. Khi $A$ suy biến, ta được một ellipsoid suy biến, dẹt xuống một không gian thấp chiều hơn.

**Thể tích và liên hệ thống kê.** Thể tích của ellipsoid tỉ lệ với $(\det P)^{1/2}$, nên nhiều bài toán tìm ellipsoid nhỏ nhất hay lớn nhất dẫn tới cực trị của $\log\det$. Các tập mức của mật độ Gauss $\mathcal N(\mu, \Sigma)$ là ellipsoid với tâm $\mu$ và ma trận tỉ lệ với $\Sigma$. Nguồn: Convex Optimization, §2.2.2 và §8.4.

## Ví dụ

Với $x_c = 0$ và $P = \operatorname{diag}(4, 1)$, ellipsoid là $x_1^2/4 + x_2^2 \le 1$, có bán trục dài 2 theo trục $x_1$ và bán trục dài 1 theo trục $x_2$.

## Khi nào cần dùng?

Mô tả vùng bất định, vùng tin cậy của phân phối Gauss và các tập lồi trơn trong bài toán tối ưu.

## Câu hỏi ôn lại

Quả cầu Euclid bán kính r là ellipsoid với ma trận P bằng gì?

<details><summary>Xem đáp án</summary>

$P = r^2 I$.

</details>

## Thuật ngữ liên quan

- [Ma trận nửa xác định dương](./ma-tran-psd.md)
- [Trị riêng &amp; vector riêng](./tri-rieng.md)
- [Phân phối Gauss](./phan-phoi-gauss.md)
