---
title: "Nghiệm cơ sở của quy hoạch tuyến tính"
wikiTerm: nghiem-co-so
prev: false
next: false
---

# Nghiệm cơ sở của quy hoạch tuyến tính

Với Ax=b có m hàng độc lập, chọn m cột độc lập làm cơ sở, đặt các biến còn lại bằng 0 rồi giải cho các biến cơ sở. Nếu nghiệm thu được không âm trong dạng chuẩn, đó là nghiệm cơ sở khả thi.

<WikiUsage />

## Giải thích kỹ thuật

**Liên hệ với đỉnh.** Trong dạng chuẩn $Ax=b$, $x\ge0$, giả sử $A$ có hạng hàng $m$. Một cơ sở chọn $m$ cột độc lập $A_B$; nghiệm cơ sở đặt $x_N=0$ và giải $A_Bx_B=b$. Khả thi đòi $x_B\ge0$.

Một biến cơ sở bằng 0 tạo suy biến: nhiều cơ sở có thể biểu diễn cùng một đỉnh. Không phải mọi lựa chọn $m$ cột đều độc lập, và nghiệm giải được vẫn có thể chứa thành phần âm. Nguồn: Bertsimas & Tsitsiklis, Introduction to Linear Optimization, chương 2.

## Ví dụ

Chọn hai cột độc lập của hệ hai phương trình cho một ma trận vuông 2×2 rồi giải hai biến cơ sở.

## Khi nào cần dùng?

Mô tả các đỉnh của đa diện và hiểu cơ chế của simplex.

## Tự kiểm tra

Biến cơ sở có bắt buộc dương không?

<details><summary>Xem đáp án</summary>

Không. Nó có thể bằng 0; khi đó nghiệm cơ sở bị suy biến.

</details>

## Thuật ngữ liên quan

- [Hệ phương trình tuyến tính](./he-phuong-trinh.md)
- [Tập lồi](./tap-loi.md)
- [Điểm và miền khả thi](./mien-kha-thi.md)
