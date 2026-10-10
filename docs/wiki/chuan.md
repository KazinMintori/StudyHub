---
title: "Chuẩn vector"
wikiTerm: chuan
prev: false
next: false
---

# Chuẩn vector

Chuẩn đo độ lớn của vector. Chuẩn Euclid $\|x\|_{2} = \sqrt{x_1^2+\cdots+x_n^2}$. Khoảng cách giữa hai điểm x, y là $\|x-y\|_{2}$. Chuẩn không âm và chỉ bằng 0 ở vector không.

<WikiUsage />

## Giải thích kỹ thuật

**Các chuẩn thường gặp.** Với vector $x=(x_1,\ldots,x_n)$, chuẩn 1 cộng độ lớn của từng thành phần:

$$\|x\|_1=|x_1|+\cdots+|x_n|=\sum_{i=1}^n|x_i|.$$

Chuẩn Euclid cộng các bình phương trước khi lấy căn:

$$\|x\|_2=\sqrt{x_1^2+\cdots+x_n^2}=\sqrt{\sum_{i=1}^n x_i^2}.$$

Chỉ số $i$ chạy từ 1 đến $n$, qua tất cả thành phần của vector. Chuẩn cực đại (hay chuẩn Chebyshev) lấy độ lớn lớn nhất: $\|x\|_\infty=\max\{|x_1|,\ldots,|x_n|\}$. Mỗi chuẩn tạo một cách đo khoảng cách $d(x,y)=\|x-y\|$.

Chuẩn thỏa bất đẳng thức tam giác và tính đồng nhất $\|\alpha x\|=|\alpha|\|x\|$. Đừng nhầm chuẩn vector với chuẩn hóa dữ liệu theo trung bình và độ lệch chuẩn.

## Ví dụ

Với vector $v=(3,4)$, chuẩn Euclid là:

$$\|v\|_2=\sqrt{3^2+4^2}=\sqrt{9+16}=5.$$

## Khi nào cần dùng?

Hiểu khoảng cách, sai số, hướng đơn vị và điều kiện hội tụ.

## Tự kiểm tra

Chuẩn Euclid của $(0, -2)$ là bao nhiêu?

<details><summary>Xem đáp án</summary>

2, không phải −2.

</details>

## Thuật ngữ liên quan

- [Giới hạn](./gioi-han.md)
- [Tích vô hướng](./tich-vo-huong.md)
- [Vector](./vector.md)
