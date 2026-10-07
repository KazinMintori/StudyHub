---
title: "Lagrangian"
wikiTerm: lagrangian
prev: false
next: false
---

# Lagrangian

Lagrangian cộng mục tiêu với các ràng buộc đã nhân bởi các nhân tử. Với quy ước fᵢ(x)≤0, nhân tử bất đẳng thức λᵢ phải không âm; nhân tử đẳng thức không bị giới hạn dấu.

<WikiUsage />

## Giải thích kỹ thuật

**Vai trò của quy ước dấu.** Với bài min có $f_i(x)\le0$ và $h_j(x)=0$, đặt $L=f_0+\sum_i\lambda_if_i+\sum_j\nu_jh_j$, trong đó $\lambda_i\ge0$ còn $\nu_j\in\mathbb R$. Tại điểm khả thi, $L\le f_0$. Nếu viết bất đẳng thức theo chiều ngược, quy ước dấu của nhân tử cũng phải đổi.

Lagrangian không tự biến điểm cực tiểu theo $x$ thành nghiệm khả thi. Nó là công cụ tạo cận và điều kiện dừng; khả thi gốc vẫn phải được kiểm riêng. Nguồn: Convex Optimization, §5.1.1.

## Ví dụ

Với min (x−2)², x≤1: L(x,λ)=(x−2)²+λ(x−1), λ≥0.

## Khi nào cần dùng?

Tạo cận dưới, lập điều kiện KKT và phân tích độ nhạy.

## Tự kiểm tra

Vì sao nhân tử của x−1≤0 không được âm?

<details><summary>Xem đáp án</summary>

Vì tại điểm khả thi, λ(x−1) chỉ chắc chắn không dương khi λ≥0; đó là bước giữ cận dưới.

</details>

## Thuật ngữ liên quan

- [Điểm và miền khả thi](./mien-kha-thi.md)
- [Hàm đối ngẫu Lagrange](./ham-doi-ngau.md)
- [Điều kiện KKT](./kkt.md)
