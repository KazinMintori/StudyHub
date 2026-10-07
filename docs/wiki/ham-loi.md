---
title: "Hàm lồi"
wikiTerm: ham-loi
prev: false
next: false
---

# Hàm lồi

Hàm f trên miền lồi là lồi nếu f(θx+(1−θ)y)≤θf(x)+(1−θ)f(y) với mọi x,y trong miền và θ trong [0,1]. Với hàm khả vi trên miền mở lồi, mặt phẳng tiếp tuyến luôn nằm dưới hàm.

<WikiUsage />

## Giải thích kỹ thuật

Trên miền mở lồi, nếu $f$ khả vi thì tính lồi tương đương

$$f(y)\ge f(x)+\nabla f(x)^T(y-x).$$

Với $f$ hai lần khả vi, có thể kiểm $\nabla^2f(x)\succeq0$ ở mọi điểm. Hàm lồi có thể không khả vi, chẳng hạn $|x|$ ở 0. Lồi nghiêm dùng dấu nhỏ hơn với $x\ne y$, $0<\theta<1$; nó không tự bảo đảm đạt nghiệm. Nguồn: Convex Optimization, §3.1.

## Ví dụ

$f(x)=x^2$: tại x=−1, y=2, θ=1/2, giá trị ở trung điểm là 1/4, còn trung bình hai giá trị là 5/2.

## Khi nào cần dùng?

Chứng nhận tối ưu toàn cục và kiểm dạng chuẩn của mô hình tối ưu.

## Tự kiểm tra

Hàm lồi có luôn duy nhất một nghiệm cực tiểu không?

<details><summary>Xem đáp án</summary>

Không. Hàm hằng có mọi điểm trong miền là nghiệm. Lồi nghiêm bảo đảm nhiều nhất một nghiệm trên miền khả thi lồi.

</details>

## Thuật ngữ liên quan

- [Tập lồi](./tap-loi.md)
- [Gradient](./gradient.md)
- [Hessian](./hessian.md)
