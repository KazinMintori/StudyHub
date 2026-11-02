---
title: "Phân vị chuẩn tắc"
wikiTerm: phan-vi-chuan-tac
prev: False
next: False
---

# Phân vị chuẩn tắc

Phân vị chuẩn tắc là ngưỡng để diện tích xác suất về một phía bằng một mức đã cho. Phân vị đuôi trái được đánh chỉ số bằng xác suất nằm bên trái. Phân vị đuôi phải được đánh chỉ số bằng xác suất nằm bên phải.

<WikiUsage />

## Giải thích kỹ thuật

Với $Z\sim N(0,1)$, đặt $\Phi(x)=P(Z\le x)$. Phân vị đuôi trái mức $p$ là $q_p=\Phi^{-1}(p)$. Phân vị đuôi phải mức $\alpha$ là $z_\alpha=\Phi^{-1}(1-\alpha)$. Vì vậy:

$$
P(Z>z_\alpha)=\alpha.
$$

Đối xứng cho $z_{1-\alpha}=-z_\alpha$. Chẳng hạn $z_{0{,}025}\approx1{,}960$. Xem [Phân phối liên tục và xấp xỉ chuẩn](/xac-suat-thong-ke/bai-giang/14-phan-phoi-lien-tuc-va-xap-xi-chuan).

## Ví dụ

Ngưỡng xấp xỉ 1,645 có xác suất chuẩn tắc bên phải bằng 0,05 và xác suất bên trái bằng 0,95.

## Khi nào cần dùng?

Tra ngưỡng xác suất chuẩn trong bài toán khoảng tin cậy, kiểm định và thiết kế mức bảo đảm.

## Câu hỏi ôn lại

Ký hiệu mức 0,05 có luôn chỉ cùng một ngưỡng không?

<details><summary>Xem đáp án</summary>

Không. Cần biết mức đó là xác suất đuôi trái hay đuôi phải.

</details>

## Thuật ngữ liên quan

- [Phân phối Gauss](./phan-phoi-gauss.md)
- [Hàm phân phối tích lũy](./ham-phan-phoi-tich-luy.md)
- [Khoảng tin cậy](./khoang-tin-cay.md)
