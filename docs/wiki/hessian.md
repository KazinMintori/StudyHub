---
title: "Hessian"
wikiTerm: hessian
prev: false
next: false
---

# Hessian

Với hàm $f$ có đạo hàm bậc hai liên tục, Hessian $H$ có phần tử $H_{ij}=\frac{\partial^2 f}{\partial x_i\,\partial x_j}$. $H$ mô tả độ cong theo hướng $v$ qua số $v^THv$. Hessian khác gradient: Một bên là ma trận, một bên là vector.

<WikiUsage />

## Giải thích kỹ thuật

Với $f:\mathbb R^n\to\mathbb R$ có đạo hàm bậc hai liên tục, $H=\nabla^2f$ đối xứng. Với độ dời nhỏ $d$,

$$f(x+d)=f(x)+\nabla f(x)^Td+\tfrac12d^THd+o(\|d\|_2^2).$$

Ký hiệu $o(\|d\|_2^2)$ là phần dư mà tỉ số với $\|d\|_2^2$ tiến về 0 khi $d$ tiến về 0. Số $d^THd$ đo độ cong theo hướng $d$. Nó không phải một tọa độ riêng của Hessian. Trên miền mở lồi, hàm hai lần khả vi là lồi khi và chỉ khi Hessian PSD ở mọi điểm. Kiểm ở một điểm chưa đủ. Nguồn: Convex Optimization, §A.4.2 và §3.1.4.

## Ví dụ

Với $f(x,y)=x^2+3y^2$, gradient là $(2x,6y)^T$ và

$$\nabla^2f=\begin{bmatrix}2&0\\0&6\end{bmatrix}.$$

## Khi nào cần dùng?

Kiểm tính lồi của hàm hai lần khả vi và lập bước Newton.

## Tự kiểm tra

Hessian của $f(x,y)=(x+y)^{2}$ là gì?

<details><summary>Xem đáp án</summary>

Ta có

$$\nabla^2f=\begin{bmatrix}2&2\\2&2\end{bmatrix}.$$

Các phần tử ngoài đường chéo xuất hiện vì $x$ và $y$ cùng nằm trong một bình phương.

</details>

## Thuật ngữ liên quan

- [Gradient](./gradient.md)
- [Ma trận nửa xác định dương](./ma-tran-psd.md)
- [Trị riêng &amp; vector riêng](./tri-rieng.md)
- [Ma trận](./ma-tran.md)
