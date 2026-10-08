---
title: "Lagrangian"
wikiTerm: lagrangian
prev: false
next: false
---

# Lagrangian

Lagrangian cộng mục tiêu với các ràng buộc đã nhân bởi các nhân tử. Với quy ước $f_{i}(x)\le 0$, nhân tử bất đẳng thức $\lambda _{i}$ phải không âm, còn nhân tử đẳng thức không bị giới hạn dấu.

<WikiUsage />

## Giải thích kỹ thuật

**Vai trò của quy ước dấu.** Với bài cực tiểu $f_0(x)$ có $m$ bất đẳng thức $f_i(x)\le0$ và $p$ đẳng thức $h_j(x)=0$, mỗi ràng buộc góp một số hạng vào Lagrangian:

$$\begin{aligned}
L(x,\lambda,\nu)=f_0(x)
&+\lambda_1f_1(x)+\cdots+\lambda_mf_m(x)\\
&+\nu_1h_1(x)+\cdots+\nu_ph_p(x).
\end{aligned}$$

Viết gọn:

$$L=f_0+\sum_{i=1}^m\lambda_i f_i+\sum_{j=1}^p\nu_j h_j.$$

$i$ chạy qua các bất đẳng thức, $j$ chạy qua các đẳng thức. Tổng của nhóm rỗng bằng 0. Các nhân tử $\lambda_i\ge0$, còn $\nu_j\in\mathbb R$. Tại điểm khả thi, $L\le f_0$. Nếu viết bất đẳng thức theo chiều ngược, quy ước dấu của nhân tử cũng phải đổi.

Lagrangian không tự biến điểm cực tiểu theo $x$ thành nghiệm khả thi. Nó là công cụ tạo cận và điều kiện dừng. Khả thi gốc vẫn phải được kiểm riêng. Nguồn: Convex Optimization, §5.1.1.

## Ví dụ

Với $\min (x-2)^{2}$, $x\le 1$: $L(x,\lambda )=(x-2)^{2}+\lambda (x-1)$, $\lambda \ge 0$.

## Khi nào cần dùng?

Tạo cận dưới, lập điều kiện KKT và phân tích độ nhạy.

## Tự kiểm tra

Vì sao nhân tử của $x-1\le 0$ không được âm?

<details><summary>Xem đáp án</summary>

Vì tại điểm khả thi, $\lambda (x-1)$ chỉ chắc chắn không dương khi $\lambda \ge 0$. Đó là bước giữ cận dưới.

</details>

## Thuật ngữ liên quan

- [Điểm và miền khả thi](./mien-kha-thi.md)
- [Hàm đối ngẫu Lagrange](./ham-doi-ngau.md)
- [Điều kiện KKT](./kkt.md)
