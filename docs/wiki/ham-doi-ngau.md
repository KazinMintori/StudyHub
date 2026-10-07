---
title: "Hàm đối ngẫu Lagrange"
wikiTerm: ham-doi-ngau
prev: false
next: false
---

# Hàm đối ngẫu Lagrange

Hàm đối ngẫu g(λ,ν) là infimum của Lagrangian theo biến gốc, khi giữ các nhân tử cố định. Mỗi bộ nhân tử khả thi cho một cận dưới của bài cực tiểu; bài đối ngẫu chọn cận dưới lớn nhất.

<WikiUsage />

## Giải thích kỹ thuật

**Lấy infimum theo biến gốc trước.** Hàm $g(\lambda,\nu)=\inf_{x\in D}L(x,\lambda,\nu)$ giữ các điều kiện miền xác định nhưng bỏ các ràng buộc đã đưa vào Lagrangian. Nếu infimum không hữu hạn, $g=-\infty$ vẫn là một cận đúng nhưng không giúp nhiều.

$g$ luôn lõm theo các nhân tử vì nó là infimum của một họ hàm affine theo $(\lambda,\nu)$. Tính lõm này đúng ngay cả khi bài gốc không lồi. Bài đối ngẫu cực đại $g$ trên $\lambda\ge0$. Nguồn: Convex Optimization, §5.1.2–5.1.3.

## Ví dụ

Với L=(x−2)²+λ(x−1), lấy infimum theo x cho g(λ)=λ−λ²/4, λ≥0.

## Khi nào cần dùng?

Chứng nhận cận dưới và đo khoảng cách tới tối ưu.

## Tự kiểm tra

Vì sao bài đối ngẫu cực đại g thay vì cực tiểu g?

<details><summary>Xem đáp án</summary>

Vì mọi g là cận dưới; cận lớn hơn gần giá trị tối ưu gốc hơn.

</details>

## Thuật ngữ liên quan

- [Lagrangian](./lagrangian.md)
- [Đối ngẫu mạnh và khoảng cách đối ngẫu](./doi-ngau-manh.md)
- [Điều kiện Slater](./dieu-kien-slater.md)
