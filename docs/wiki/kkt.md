---
title: "Điều kiện KKT"
wikiTerm: kkt
prev: false
next: false
---

# Điều kiện KKT

Với bài min f₀(x), fᵢ(x)≤0, Ax=b khả vi, KKT gồm khả thi gốc, λ≥0, λᵢfᵢ(x)=0 và $\nabla f$₀(x)+Σλᵢ$\nabla f$ᵢ(x)+Aᵀν=0. Trong bài toán lồi, KKT đủ cho tối ưu. Để suy ra tính cần, phải có điều kiện phù hợp như Slater.

<WikiUsage />

## Giải thích kỹ thuật

Với các $f_i$ lồi khả vi và đẳng thức affine, nhân tử không âm làm Lagrangian lồi theo $x$. Điều kiện dừng cho biết $x$ cực tiểu Lagrangian; khả thi và bù trừ đưa giá trị Lagrangian về $f_0(x)$. Vì vậy khoảng cách đối ngẫu bằng 0 và nghiệm tối ưu.

Slater là điều kiện đủ cho đối ngẫu mạnh: có điểm trong nội tương đối của miền chung, thỏa đẳng thức và thỏa chặt bất đẳng thức. Với điều kiện này và nghiệm đạt, KKT cũng cần. Trong bài không lồi, nghiệm KKT có thể không tối ưu toàn cục. Nguồn: Convex Optimization, §5.2.3 và §5.5.3.

## Ví dụ

min (x−2)² với x≤1 có x*=1, λ*=2. Dừng: 2(1−2)+2=0. Bù trừ: 2(1−1)=0.

## Khi nào cần dùng?

Chứng nhận nghiệm ràng buộc và lập hệ Newton–KKT.

## Tự kiểm tra

λᵢ=0 có kéo theo fᵢ(x)<0 không?

<details><summary>Xem đáp án</summary>

Không. Bù trừ cho phép đồng thời λᵢ=0 và fᵢ(x)=0. Chiều chắc chắn là fᵢ(x)<0 kéo theo λᵢ=0.

</details>

## Thuật ngữ liên quan

- [Gradient](./gradient.md)
- [Hàm lồi](./ham-loi.md)
- [Hệ phương trình tuyến tính](./he-phuong-trinh.md)
