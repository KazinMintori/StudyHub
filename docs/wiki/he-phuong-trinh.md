---
title: "Hệ phương trình tuyến tính"
wikiTerm: he-phuong-trinh
prev: false
next: false
---

# Hệ phương trình tuyến tính

Hệ Ax=b gồm các phương trình tuyến tính cùng dùng một vector ẩn x. Hệ có nghiệm khi b thuộc không gian sinh bởi các cột A. Nếu A vuông và khả nghịch thì nghiệm duy nhất; nếu A suy biến thì hệ có thể vô nghiệm hoặc có nhiều nghiệm.

<WikiUsage />

## Giải thích kỹ thuật

Nếu $A$ kích thước $m\times n$, thì $x\in\mathbb R^n$, $b\in\mathbb R^m$. Tập nghiệm nếu khác rỗng có dạng $x_0+\{v:Av=0\}$. Điều này giải thích vì sao hệ thiếu hạng có thể có nhiều nghiệm.

Với ma trận vuông khả nghịch, dùng thuật toán giải hệ thay vì tính ma trận nghịch đảo rồi nhân. Phương trình chuẩn $A^TAw=A^Tb$ đặc trưng nghiệm bình phương tối thiểu; khi tính số, QR/SVD có thể thích hợp hơn việc lập $A^TA$. Nguồn: Convex Optimization, §A.5.1–A.5.4 và §1.2.1.

## Ví dụ

x+y=3, x−y=1 cho x=2, y=1. Hai phương trình x+y=3 và 2x+2y=7 lại mâu thuẫn.

## Khi nào cần dùng?

Giải phương trình chuẩn của hồi quy, hệ KKT và bước Newton.

## Tự kiểm tra

A có hai hàng giống nhau thì có luôn vô nghiệm không?

<details><summary>Xem đáp án</summary>

Không. Hai vế phải tương ứng bằng nhau thì hai phương trình trùng nhau; vế phải khác nhau thì mâu thuẫn.

</details>

## Thuật ngữ liên quan

- [Ma trận](./ma-tran.md)
- [Vector](./vector.md)
- [Hessian](./hessian.md)
