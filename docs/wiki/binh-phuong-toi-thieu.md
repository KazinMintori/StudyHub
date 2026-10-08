---
title: "Bình phương tối thiểu"
wikiTerm: binh-phuong-toi-thieu
prev: false
next: false
---

# Bình phương tối thiểu

Bình phương tối thiểu chọn tham số để tổng bình phương các phần dư nhỏ nhất. Bình phương làm sai lệch âm và dương cùng đóng góp không âm; nó cũng làm sai lệch lớn được phạt mạnh hơn.

<WikiUsage />

## Giải thích kỹ thuật

**Dạng ma trận.** Với $A\in\mathbb R^{m\times n}$, $b\in\mathbb R^m$, bài bình phương tối thiểu là $\min_x\|Ax-b\|_2^2$. Gradient của nửa tổng bình phương là $A^T(Ax-b)$; mọi nghiệm thỏa phương trình chuẩn $A^TAx=A^Tb$.

Nếu các cột của A độc lập, $A^TA$ dương xác định và nghiệm duy nhất. Khi tính số, giải bằng QR hoặc SVD thường ổn định hơn việc lập nghịch đảo $(A^TA)^{-1}$. Dưới giả định nhiễu Gauss độc lập, cùng phương sai cố định, cực đại likelihood tương đương cực tiểu tổng bình phương phần dư. Nguồn: Convex Optimization, §1.2.1, §7.1 và phụ lục A.5.

## Ví dụ

Với phần dư r=(1,−2), tổng bình phương là 1²+(−2)²=5.

## Khi nào cần dùng?

Khớp mô hình tuyến tính, ước lượng dưới nhiễu Gauss và xây bài toán QP.

## Tự kiểm tra

Đổi mọi phần dư r thành −r có làm tổng bình phương thay đổi không?

<details><summary>Xem đáp án</summary>

Không. Mỗi phần dư xuất hiện dưới dạng r².

</details>

## Thuật ngữ liên quan

- [Ma trận](./ma-tran.md)
- [Gradient](./gradient.md)
- [Phân phối Gauss](./phan-phoi-gauss.md)
- [Likelihood](./likelihood.md)
