---
title: "Hessian"
wikiTerm: hessian
prev: false
next: false
---

# Hessian

Với hàm f có đạo hàm bậc hai liên tục, Hessian H có phần tử Hᵢⱼ=∂²f/∂xᵢ∂xⱼ. H mô tả độ cong theo hướng v qua số vᵀHv. Hessian khác gradient: một bên là ma trận, một bên là vector.

<WikiUsage />

## Giải thích kỹ thuật

Với $f:\mathbb R^n\to\mathbb R$ có đạo hàm bậc hai liên tục, $H=\nabla^2f$ đối xứng. Với độ dời nhỏ $d$,

$$f(x+d)=f(x)+\nabla f(x)^Td+\tfrac12d^THd+o(\|d\|_2^2).$$

Ký hiệu $o(\|d\|_2^2)$ là phần dư mà tỉ số với $\|d\|_2^2$ tiến về 0 khi $d$ tiến về 0. Số $d^THd$ đo độ cong theo hướng $d$; nó không phải một tọa độ riêng của Hessian. Trên miền mở lồi, hàm hai lần khả vi là lồi khi và chỉ khi Hessian PSD ở mọi điểm. Kiểm ở một điểm chưa đủ. Nguồn: Convex Optimization, §A.4.2 và §3.1.4.

## Ví dụ

f(x,y)=x²+3y² có gradient (2x,6y) và Hessian diag(2,6).

## Khi nào cần dùng?

Kiểm tính lồi của hàm hai lần khả vi và lập bước Newton.

## Tự kiểm tra

Hessian của f(x,y)=(x+y)² là gì?

<details><summary>Xem đáp án</summary>

[[2,2],[2,2]]. Có số hạng chéo vì hai biến cùng xuất hiện trong một bình phương.

</details>

## Thuật ngữ liên quan

- [Gradient](./gradient.md)
- [Ma trận nửa xác định dương](./ma-tran-psd.md)
- [Trị riêng &amp; vector riêng](./tri-rieng.md)
- [Ma trận](./ma-tran.md)
